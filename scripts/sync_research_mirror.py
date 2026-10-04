# Artifact refresh trigger: validates cleanup and artifact metadata publishing.
# Artifact startup is consumed through the GitHub Actions artifact download path.
#!/usr/bin/env python3
from __future__ import annotations

import json, os, re, shutil, urllib.error, urllib.request
from pathlib import Path
from typing import Any

SUPABASE_URL = os.environ["SUPABASE_URL"].rstrip("/")
SUPABASE_KEY = os.environ["SUPABASE_SECRET_KEY"]
STAGE = Path(".mirror-stage")
SCHEMAS = ("gn3n", "linp")
TABLES = ("documents","research","section_subsections","article_sections","brainstorms","dictionary")
PAGE = 500

def headers():
    h = {"apikey": SUPABASE_KEY, "Content-Type": "application/json", "Accept": "application/json",
         "User-Agent": "research-mirror-v8/1.0"}
    if not SUPABASE_KEY.startswith("sb_secret_"):
        h["Authorization"] = f"Bearer {SUPABASE_KEY}"
    return h

def rpc(name: str, payload: dict[str, Any]) -> Any:
    req = urllib.request.Request(
        f"{SUPABASE_URL}/rest/v1/rpc/{name}",
        data=json.dumps(payload).encode(),
        headers=headers(),
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"{name} failed: {e.code}: {e.read().decode(errors='replace')}") from e

def rows(schema: str, table: str) -> list[dict[str, Any]]:
    out, offset = [], 0
    while True:
        page = rpc("research_mirror_rows", {
            "p_schema": schema, "p_table": table, "p_offset": offset, "p_limit": PAGE
        })
        got = page["rows"]
        out.extend(got)
        if page["complete"]:
            return out
        offset += len(got)

def context(schema: str, kind: str) -> Any:
    return rpc("research_mirror_context", {"p_schema": schema, "p_kind": kind, "p_arg": None})

def write(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")

def write_json(path: Path, value: Any):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def safe_name(s: str) -> str:
    return "".join(c if c.isalnum() or c in "._-" else "_" for c in s)[:180] or "item"

def doc_md(row: dict[str, Any]) -> str:
    return f"# {row.get('title') or row['id']}\n\n{row.get('body') or ''}"

def research_md(row: dict[str, Any], subsections: list[dict[str, Any]] | None = None) -> str:
    bits = [f"# {row.get('title') or row['id']}"]
    if row.get("simplified_statement"):
        bits += ["", f"**Summary:** {row['simplified_statement']}"]
    if row.get("statement"):
        bits += ["", "## Statement", "", row["statement"]]
    if row.get("body"):
        bits += ["", "## Body", "", row["body"]]
    bits += ["", "## Metadata", "",
             f"- ID: {row['id']}",
             f"- Kind: {row.get('kind')}",
             f"- Version: {row.get('version')}",
             f"- Math version: {row.get('math_version')}",
             f"- Audit: {row.get('audit_status')}",
             f"- Refutation: {row.get('refutation_status')}"]
    if row.get("kind") == "toolkit":
        bits.append(f"- Toolkit status: {'Limbo' if row.get('toolkit_limbo') else 'Promoted'}")
    if row.get("kind") == "section":
        bits += ["", "## Authoring state", ""]
        subsections = subsections or []
        if not subsections:
            bits.append("- No Subsections recorded.")
        else:
            for s in sorted(subsections, key=lambda x: x.get("subsection_no") or 0):
                state = "HOT" if s.get("state") == "hot" else "crystallized"
                title = s.get("title") or "(untitled)"
                bits.append(
                    f"- Subsection {s.get('subsection_no')} — {state}, version {s.get('version')}: {title}"
                )
    return "\n".join(bits)

def article_md(row: dict[str, Any], sequence_rows: list[dict[str, Any]], research_by_id: dict[str, dict[str, Any]]) -> str:
    bits = [f"# {row.get('title') or row['id']}"]
    members = sorted(
        [s for s in sequence_rows if s.get("article_id") == row["id"]],
        key=lambda s: s.get("position") or 0,
    )
    if not members:
        bits += ["", "No Sections are currently integrated."]
        return "\n".join(bits)
    for s in members:
        r = research_by_id.get(s.get("section_id"))
        if not r:
            continue
        body = re.sub(r"(?m)^## ", "### ", r.get("body") or "")
        bits += [
            "", "---", "",
            f"## Section — {r.get('title') or r['id']}",
            "", f"<!-- section_id: {r['id']} -->", "",
            body,
        ]
    return "\n".join(bits)

def dictionary_text(items: list[dict[str, Any]]) -> str:
    by_section: dict[str, list[dict[str, Any]]] = {}
    for x in items:
        by_section.setdefault(x.get("section") or "general", []).append(x)
    out = []
    for section in sorted(by_section):
        heading = "Review Queue" if section == "review_queue" else section.replace("_", " ").title()
        out += [f"## {heading}", ""]
        if section == "review_queue":
            out += [
                "Before using an entry in this section, either replace it with a precise canonical definition or mark it prohibited.",
                ""
            ]
        for x in sorted(by_section[section], key=lambda r: (r.get("term") or "").casefold()):
            term = x.get("term") or ""
            status = x.get("status") or ""
            pref = x.get("preferred_term") or ""
            if status == "alias" and pref:
                term += f" [alias -> {pref}]"
            elif status == "prohibited" and pref:
                term += f" [prohibited; use {pref}]"
            elif status == "prohibited":
                term += " [prohibited]"
            out.append(f"{term}: {x.get('definition') or ''}")
            if x.get("notes"):
                out.append(f"  Note: {x['notes']}")
            out.append("")
    return "\n".join(out)

def api_text() -> str:
    return """# Research API

These RPCs are the worker-facing interface to live research state. The artifact is a snapshot; use the API whenever current state, exact versions, or publication matters.

## Startup and navigation

### `boot()`
Starts a research session against the current database revision. It returns the session ID required by mutation RPCs, startup notices, artifact metadata, and the snapshot revision. Call it once at startup; call it again after deliberately refreshing a stale artifact.

### `search(query, filters := {})`
Finds relevant Sections, Toolkit entries, Articles and other documents, and optionally Brainstorms by title and mathematical content. Use it for discovery, not as a substitute for reading a manuscript. Useful filters include `kind`, `toolkit_type`, `toolkit_limbo`, `article_id`, and `result_level`.

### `read(ids, math_versions := {}, cursor := null, page_chars := 9000)`
Returns exact durable content for named objects, one bounded page at a time. Reading an Article ID returns its prose document compiled from its ordered Sections with explicit Section boundaries; reading a Section ID returns that Section directly. Pass `next_cursor` back until `complete=true`; `math_versions` can request a retained prior mathematical version when available.

### `context(research_id)`
Shows how one research object sits in the mathematical structure: direct premises and consumers, supersession links, referring Articles, and originating Brainstorm. Use it when following dependencies or deciding where new work belongs.

### `changes(since_revision := 0, until_revision := null, limit := 100)`
Checks what changed after a known artifact/database revision without shipping the changed documents themselves. It returns policy/document events plus current Article and Section versions. Use it for startup freshness checks. Continue from the artifact for matching manuscript versions; call `read()` for each manuscript whose live version is newer.

### `brainstorms(active_only := true)`
Returns the compact Brainstorm collection, including seeds, status, and promotion targets. Use it to scan orthogonal ideas cheaply without searching full manuscript text.

### `dictionary()`
Returns the current canonical terminology and Review Queue in readable form. Use it before introducing or relying on project-specific terminology.

## Publishing research

### `save_research(session_id, payload, expected_version := null)`
Creates or edits a Section or Toolkit object with optimistic version checking. Use `kind: "section"` for Sections. Substantive publications must explicitly declare their dependencies; nonsubstantive edits do not change the mathematical version. New Toolkit entries begin in Toolkit Limbo.

### `save_subsection(session_id, section_id, payload, expected_section_version, expected_subsection_version)`
Edits the current hot Subsection of a Section. This is the normal path for route development. Substantive changes update the assembled Section, bump its mathematical version, and replace its declared dependencies.

### `repair_subsection(session_id, section_id, subsection_no, payload, expected_section_version, expected_subsection_version)`
Edits an older crystallized Subsection in place while preserving the Section manuscript structure. Use it when earlier text itself needs correction; ordinary continuing research belongs in the hot Subsection.

### `crystallize_subsection(session_id, section_id, expected_section_version, expected_subsection_version, next_title := '')`
Freezes the current hot Subsection and opens a new empty hot Subsection. Use it when a coherent stage of a Section is complete and the next stage should begin separately.

### `save_document(session_id, payload, expected_version := null)`
Creates or edits project documents such as Articles and the overview, with version checking and audit bookkeeping. An Article is a prose document automatically composed from an ordered Section sequence. Set `section_ids` to integrate, remove, or reorder mature Sections; the generated Article body is refreshed from that sequence.

## Brainstorms

### `save_brainstorm(session_id, payload, expected_version := null)`
Creates, edits, closes, or annotates a Brainstorm entry. Brainstorms are deliberately low-cost exploratory space and need not satisfy Toolkit or Section publication standards.

### `promote_brainstorm(session_id, brainstorm_id, payload := {}, expected_version)`
Atomically turns a developed Brainstorm into a Section and closes the Brainstorm with a link to the new Section. The promotion payload must declare the new Section's dependencies.

## Audits and chores

### `request_audit(session_id, target_type, target_id, target_version)`
Queues an independent audit of the current mathematical version of a research object or the current version of an Article. Use `article` as the target type for an Article.

### `claim_chore(session_id, kinds := {audit,maintenance})`
Claims one available audit or bounded maintenance task using a lease. Audit claims enforce independence from the authors of the mathematical version being checked.

### `finish_chore(session_id, chore_id, outcome := {})`
Completes a claimed chore. For audits it records pass/fail status and, when needed, whether optimistically retargeted consumer dependencies remain compatible.

## Atomic publication batches

Use these when one logical publication changes several shared objects together. The sequence is stage → review → commit.

### `stage_batch_chunk(session_id, batch_id, part_no, chunk)`
Stores part of a potentially large JSON publication batch. These are transport chunks for the batch payload, unrelated to mathematical Subsections. Re-staging a part invalidates any previous review.

### `review_staged_batch(session_id, batch_id)`
Parses the staged operations and reports concurrent shared-state changes since the session baseline.

### `commit_staged_batch(session_id, batch_id, overlap_checked)`
Atomically executes a reviewed staged batch.

### `discard_staged_batch(session_id, batch_id)`
Abandons an uncommitted staged batch and its stored transport chunks.

## Recovery and introspection

### `artifact_help()`
Returns the current artifact identifier and recovery instructions for rebuilding or locating the research-context artifact.

### `help()`
Returns a compact machine-readable overview of the API and conventions.
"""

def toolkit_entry_line(r: dict[str, Any]) -> str:
    fn = safe_name(r["id"]) + ".md"
    typ = r.get("toolkit_type") or "other"
    summary = (r.get("simplified_statement") or "").strip()
    line = f"- [{r.get('title') or r['id']}]({fn}) — {typ}"
    if summary:
        line += f" — {summary}"
    return line

def build(schema: str):
    root = STAGE / schema
    data = {t: rows(schema, t) for t in TABLES}
    rev = context(schema, "revision")
    universal_docs = context(schema, "universal_documents")

    live_docs = [d for d in data["documents"] if d.get("archived_at") is None]
    overview = next((d for d in live_docs if d.get("kind") == "overview"), None)
    guide = next((d for d in universal_docs if d.get("kind") == "guide"), None)
    reflexes = next((d for d in universal_docs if d.get("kind") == "reflexes"), None)
    articles = sorted(
        [d for d in live_docs if d.get("kind") == "article"],
        key=lambda d: (d.get("position") is None, d.get("position") or 0, d.get("id") or "")
    )

    write(root / "OVERVIEW.md", doc_md(overview) if overview else "# Overview\n\nNo overview.")
    write(root / "GUIDE.md", doc_md(guide) if guide else "# Guide\n\nNo guide.")
    write(root / "REFLEXES.md", doc_md(reflexes) if reflexes else "# Research Reflexes\n\nNo reflexes.")
    write(root / "DICTIONARY.md", dictionary_text(data["dictionary"]))
    write(root / "API.md", api_text())

    active_research = [r for r in data["research"] if r.get("archived_at") is None]
    research_by_id = {r["id"]: r for r in active_research}
    subsections_by_section: dict[str, list[dict[str, Any]]] = {}
    for s in data["section_subsections"]:
        subsections_by_section.setdefault(s["section_id"], []).append(s)

    article_index = ["# Articles", ""]
    for d in articles:
        fn = safe_name(d["id"]) + ".md"
        members = sorted(
            [s for s in data["article_sections"] if s.get("article_id") == d["id"]],
            key=lambda s: s.get("position") or 0,
        )
        article_index.append(f"- {fn} — {d.get('title') or d['id']}")
        for s in members:
            r = research_by_id.get(s.get("section_id"))
            if r:
                article_index.append(f"  - Section: {r.get('title') or r['id']} (`{r['id']}`)")
        write(root / "ARTICLES" / fn, article_md(d, data["article_sections"], research_by_id))
    if not articles:
        article_index.append("No active Articles.")
    write(root / "ARTICLES" / "README.md", "\n".join(article_index))

    article_by_id = {d["id"]: d for d in articles}
    memberships_by_section: dict[str, list[dict[str, Any]]] = {}
    for s in data["article_sections"]:
        memberships_by_section.setdefault(s.get("section_id"), []).append(s)

    section_index = [
        "# Sections",
        "",
        "Sections are section-sized mathematical manuscripts assembled from ordered Subsections. Articles are prose documents compiled from ordered mature Sections; standalone Sections remain active development routes.",
        "",
    ]
    section_items = sorted(
        [r for r in active_research if r.get("kind") == "section"],
        key=lambda r: (r.get("title") or "").casefold(),
    )
    if section_items:
        for r in section_items:
            fn = safe_name(r["id"]) + ".md"
            memberships = sorted(
                memberships_by_section.get(r["id"], []),
                key=lambda s: (s.get("article_id") or "", s.get("position") or 0),
            )
            if memberships:
                where = "; ".join(
                    f"{article_by_id.get(s.get('article_id'), {}).get('title') or s.get('article_id')} at position {s.get('position')}"
                    for s in memberships
                )
                section_index.append(f"- [{r.get('title') or r['id']}]({fn}) (`{r['id']}`) — integrated: {where}")
            else:
                section_index.append(f"- [{r.get('title') or r['id']}]({fn}) (`{r['id']}`) — standalone development")
    else:
        section_index.append("No active Sections.")
    write(root / "SECTIONS" / "README.md", "\n".join(section_index))

    for r in active_research:
        folder = "SECTIONS" if r.get("kind") == "section" else "TOOLKIT"
        write(
            root / folder / (safe_name(r["id"]) + ".md"),
            research_md(r, subsections_by_section.get(r["id"], []))
        )

    toolkit_items = sorted(
        [r for r in active_research if r.get("kind") == "toolkit"],
        key=lambda r: ((r.get("toolkit_type") or ""), (r.get("title") or "").casefold(), r.get("id") or "")
    )
    promoted = [r for r in toolkit_items if not r.get("toolkit_limbo")]
    limbo = [r for r in toolkit_items if r.get("toolkit_limbo")]

    toolkit_index = [
        "# Toolkit",
        "",
        "Toolkit entries are usable mathematical results. The distinction below concerns breadth of reuse, not mathematical certainty.",
        "",
        "## Toolkit",
        "",
        "These entries have received an independent extensibility review and were judged broadly reusable.",
        "",
    ]
    if promoted:
        toolkit_index.extend(toolkit_entry_line(r) for r in promoted)
    else:
        toolkit_index.append("No entries have yet been promoted from Toolkit Limbo.")

    toolkit_index += [
        "",
        "## Toolkit Limbo",
        "",
        "These entries remain available for use, but their broad extensibility has not yet received the skeptical independent review required for promotion.",
        "",
    ]
    if limbo:
        toolkit_index.extend(toolkit_entry_line(r) for r in limbo)
    else:
        toolkit_index.append("Toolkit Limbo is empty.")

    write(root / "TOOLKIT" / "README.md", "\n".join(toolkit_index))

    for b in data["brainstorms"]:
        write(root / "BRAINSTORMS" / (safe_name(b["id"]) + ".md"),
              f"# {b.get('title') or b['id']}\n\n{b.get('seed') or ''}\n\n{b.get('body') or ''}")

    boot = f"""# Startup instructions

Review startup_notices returned by boot().

Use the extracted artifact as the working research context. Read OVERVIEW.md, GUIDE.md, REFLEXES.md, DICTIONARY.md, API.md, and TOOLKIT/README.md. Then read ARTICLES/README.md. If the prompt asks you to continue an existing Article, read that Article in its entirety, including all of its Sections, before continuing it. Otherwise, read every listed Article in its entirety before choosing which Article or route to work on. Article files are compiled from ordered Sections and mark every Section boundary; read the corresponding SECTIONS file or call read([section_id]) when one Section is the relevant target.

Choose a route and call changes(...) once using this artifact's snapshot revision as the freshness baseline. Compare the chosen Article and Section versions with MANIFEST.json. Continue directly from the artifact for every matching version. For each manuscript whose live version is newer, read the current manuscript completely with read([id]), following next_cursor until complete=true, and use that refreshed manuscript as the local working copy.

When target_revision materially exceeds the artifact snapshot revision, use artifact_help() to refresh the artifact, call boot() again, and continue from the refreshed artifact.

Then begin research under GUIDE.md and REFLEXES.md.

Snapshot revision: {rev.get('revision')}
Generated: {rev.get('generated_at')}
"""
    write(root / "BOOT.md", boot)

    write_json(root / "MANIFEST.json", {
        "schema": schema,
        "snapshot_revision": rev.get("revision"),
        "generated_at": rev.get("generated_at"),
        "universal_document_versions": {d["id"]: d.get("version") for d in universal_docs},
        "article_versions": {d["id"]: d.get("version") for d in articles},
        "article_sequences": {
            d["id"]: [
                {
                    "position": s.get("position"),
                    "id": s.get("section_id"),
                    "version": research_by_id.get(s.get("section_id"), {}).get("version"),
                    "math_version": research_by_id.get(s.get("section_id"), {}).get("math_version"),
                }
                for s in sorted(
                    [x for x in data["article_sections"] if x.get("article_id") == d["id"]],
                    key=lambda x: x.get("position") or 0,
                )
            ]
            for d in articles
        },
        "section_versions": {
            r["id"]: {"version": r.get("version"), "math_version": r.get("math_version")}
            for r in active_research if r.get("kind") == "section"
        },
        "toolkit_promoted_count": len(promoted),
        "toolkit_limbo_count": len(limbo),
        "brainstorm_count": len(data["brainstorms"]),
        "mirror_format": 10,
    })

def main():
    if STAGE.exists():
        shutil.rmtree(STAGE)
    STAGE.mkdir()
    for schema in SCHEMAS:
        print(f"Building clean mirror for {schema}")
        build(schema)
    print("Mirror staging complete.")

if __name__ == "__main__":
    main()
