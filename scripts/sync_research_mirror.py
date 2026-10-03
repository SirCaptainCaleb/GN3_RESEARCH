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
TABLES = ("documents","research","research_line_chunks","main_line_research_lines","brainstorms","dictionary")
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

def research_md(row: dict[str, Any], chunks: list[dict[str, Any]] | None = None) -> str:
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
    if row.get("parent_line_id"):
        bits.append(f"- Parent line: {row['parent_line_id']}")
    if row.get("kind") == "line":
        bits += ["", "## Authoring state", ""]
        chunks = chunks or []
        if not chunks:
            bits.append("- No chunks recorded.")
        else:
            for c in sorted(chunks, key=lambda x: x.get("chunk_no") or 0):
                state = "HOT" if c.get("state") == "hot" else "crystallized"
                title = c.get("title") or "(untitled)"
                bits.append(
                    f"- Chunk {c.get('chunk_no')} — {state}, version {c.get('version')}: {title}"
                )
    return "\n".join(bits)

def main_line_md(row: dict[str, Any], sequence_rows: list[dict[str, Any]], research_by_id: dict[str, dict[str, Any]]) -> str:
    bits = [f"# {row.get('title') or row['id']}"]
    members = sorted(
        [s for s in sequence_rows if s.get("main_line_id") == row["id"]],
        key=lambda s: s.get("position") or 0,
    )
    if not members:
        bits += ["", "No Research Lines are currently integrated."]
        return "\n".join(bits)
    for s in members:
        r = research_by_id.get(s.get("research_line_id"))
        if not r:
            continue
        body = re.sub(r"(?m)^## ", "### ", r.get("body") or "")
        bits += [
            "", "---", "",
            f"## Research Line — {r.get('title') or r['id']}",
            "", f"<!-- research_line_id: {r['id']} -->", "",
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
Finds relevant Research Lines, Toolkit entries, documents, and optionally Brainstorms by title and mathematical content. Use it for discovery, not as a substitute for reading a manuscript. Useful filters include `kind`, `toolkit_type`, `toolkit_limbo`, `main_line_id`, and `result_level`.

### `read(ids, math_versions := {}, cursor := null, page_chars := 9000)`
Returns exact durable content for named objects, one bounded page at a time. Reading a Main Line ID compiles its ordered Research Line sequence with explicit Research Line boundaries; reading a Research Line ID returns that segment directly. Pass `next_cursor` back until `complete=true`; `math_versions` can request a retained prior mathematical version when available.

### `context(research_id)`
Shows how one research object sits in the mathematical structure: direct premises and consumers, parent/child Research Lines, supersession links, referring Main Lines, and originating Brainstorm. Use it when following dependencies or deciding where new work belongs.

### `changes(since_revision := 0, until_revision := null, limit := 100)`
Checks what changed after a known artifact/database revision without shipping the changed documents themselves. It returns policy/document events plus current Main Line and Research Line versions. Use it for startup freshness checks. Continue from the artifact for matching manuscript versions; call `read()` for each manuscript whose live version is newer.

### `brainstorms(active_only := true)`
Returns the compact Brainstorm collection, including seeds, status, and promotion targets. Use it to scan orthogonal ideas cheaply without searching full manuscript text.

### `dictionary()`
Returns the current canonical terminology and Review Queue in readable form. Use it before introducing or relying on project-specific terminology.

## Publishing research

### `save_research(session_id, payload, expected_version := null)`
Creates or edits a Research Line or Toolkit object with optimistic version checking. Substantive publications must explicitly declare their dependencies; nonsubstantive edits do not change the mathematical version. New Toolkit entries begin in Toolkit Limbo. An independent reviewer promotes an entry by a nonsubstantive edit setting `toolkit_limbo=false`.

### `save_line_chunk(session_id, line_id, payload, expected_line_version, expected_chunk_version)`
Edits the current hot chunk of a Research Line. This is the normal path for route development. Substantive changes update the assembled line, bump its mathematical version, and replace its declared dependencies.

### `repair_line_chunk(session_id, line_id, chunk_no, payload, expected_line_version, expected_chunk_version)`
Edits an older crystallized chunk in place while preserving the chunked manuscript structure. Use it only when earlier text itself needs correction; ordinary continuing research belongs in the hot chunk.

### `crystallize_line_chunk(session_id, line_id, expected_line_version, expected_chunk_version, next_title := '')`
Freezes the current hot chunk as a completed manuscript section and opens a new empty hot chunk. Use it when a coherent stage of a Research Line is complete and the next stage should begin separately.

### `save_document(session_id, payload, expected_version := null)`
Creates or edits project documents such as Main Lines and the overview, with version checking and audit bookkeeping. Main Line content is an ordered Research Line sequence: set `research_line_ids` to integrate, remove, or reorder mature Research Lines. Main Line prose is compiled from those Research Lines rather than stored independently.

## Brainstorms

### `save_brainstorm(session_id, payload, expected_version := null)`
Creates, edits, closes, or annotates a Brainstorm entry. Brainstorms are deliberately low-cost exploratory space and need not satisfy Toolkit or Research Line publication standards.

### `promote_brainstorm(session_id, brainstorm_id, payload := {}, expected_version)`
Atomically turns a developed Brainstorm into a Research Line and closes the Brainstorm with a link to the new line. The promotion payload must declare the new line's dependencies.

## Audits and chores

### `request_audit(session_id, target_type, target_id, target_version)`
Queues an independent audit of the current mathematical version of a research object or the current version of a Main Line. The target version is explicit so an audit cannot silently drift onto newer work.

### `claim_chore(session_id, kinds := {audit,maintenance})`
Claims one available audit or bounded maintenance task using a lease. Audit claims enforce independence from the authors of the mathematical version being checked.

### `finish_chore(session_id, chore_id, outcome := {})`
Completes a claimed chore. For audits it records pass/fail status and, when needed, whether optimistically retargeted consumer dependencies remain compatible.

## Atomic publication batches

Use these when one logical publication changes several shared objects together. The sequence is stage → review → commit; do not bypass it for substantial multi-object publication.

### `stage_batch_chunk(session_id, batch_id, part_no, chunk)`
Stores part of a potentially large JSON publication batch. Re-staging a part invalidates any previous review of that batch.

### `review_staged_batch(session_id, batch_id)`
Parses the staged operations and reports concurrent shared-state changes since the session baseline. Use the result to check mathematical overlap before committing.

### `commit_staged_batch(session_id, batch_id, overlap_checked)`
Atomically executes a reviewed staged batch. It refuses to commit if the batch changed after review or if another session changed shared research after the overlap review.

### `discard_staged_batch(session_id, batch_id)`
Abandons an uncommitted staged batch and its stored chunks. Use it when a proposed publication is obsolete or must be rebuilt from scratch.

## Recovery and introspection

### `artifact_help()`
Returns the current artifact identifier and recovery instructions for rebuilding or locating the research-context artifact. This is an exceptional recovery path, not part of ordinary research.

### `help()`
Returns a compact machine-readable overview of the API and conventions. Prefer this Markdown reference for normal reading; use `help()` when the artifact is unavailable or you suspect the live API has changed since the snapshot.
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
    main_lines = sorted(
        [d for d in live_docs if d.get("kind") == "main_line"],
        key=lambda d: (d.get("position") is None, d.get("position") or 0, d.get("id") or "")
    )

    write(root / "OVERVIEW.md", doc_md(overview) if overview else "# Overview\n\nNo overview.")
    write(root / "GUIDE.md", doc_md(guide) if guide else "# Guide\n\nNo guide.")
    write(root / "REFLEXES.md", doc_md(reflexes) if reflexes else "# Research Reflexes\n\nNo reflexes.")
    write(root / "DICTIONARY.md", dictionary_text(data["dictionary"]))
    write(root / "API.md", api_text())

    active_research = [r for r in data["research"] if r.get("archived_at") is None]
    research_by_id = {r["id"]: r for r in active_research}
    chunks_by_line: dict[str, list[dict[str, Any]]] = {}
    for c in data["research_line_chunks"]:
        chunks_by_line.setdefault(c["line_id"], []).append(c)

    index = ["# Main Lines", ""]
    for d in main_lines:
        fn = safe_name(d["id"]) + ".md"
        members = sorted(
            [s for s in data["main_line_research_lines"] if s.get("main_line_id") == d["id"]],
            key=lambda s: s.get("position") or 0,
        )
        index.append(f"- {fn} — {d.get('title') or d['id']}")
        for s in members:
            r = research_by_id.get(s.get("research_line_id"))
            if r:
                index.append(f"  - Research Line: {r.get('title') or r['id']} (`{r['id']}`)")
        write(root / "MAIN_LINES" / fn, main_line_md(d, data["main_line_research_lines"], research_by_id))
    if not main_lines:
        index.append("No active Main Lines.")
    write(root / "MAIN_LINES" / "README.md", "\n".join(index))
    main_by_id = {d["id"]: d for d in main_lines}
    memberships_by_line: dict[str, list[dict[str, Any]]] = {}
    for s in data["main_line_research_lines"]:
        memberships_by_line.setdefault(s.get("research_line_id"), []).append(s)

    research_line_index = [
        "# Research Lines",
        "",
        "Research Lines are the section-sized mathematical manuscripts. Main Lines compile ordered mature Research Lines; standalone Research Lines remain active development routes.",
        "",
    ]
    line_items = sorted(
        [r for r in active_research if r.get("kind") == "line"],
        key=lambda r: (r.get("title") or "").casefold(),
    )
    if line_items:
        for r in line_items:
            fn = safe_name(r["id"]) + ".md"
            memberships = sorted(memberships_by_line.get(r["id"], []), key=lambda s: (s.get("main_line_id") or "", s.get("position") or 0))
            if memberships:
                where = "; ".join(
                    f"{main_by_id.get(s.get('main_line_id'), {}).get('title') or s.get('main_line_id')} at position {s.get('position')}"
                    for s in memberships
                )
                research_line_index.append(f"- [{r.get('title') or r['id']}]({fn}) (`{r['id']}`) — integrated: {where}")
            else:
                research_line_index.append(f"- [{r.get('title') or r['id']}]({fn}) (`{r['id']}`) — standalone development")
    else:
        research_line_index.append("No active Research Lines.")
    write(root / "RESEARCH_LINES" / "README.md", "\n".join(research_line_index))

    for r in active_research:
        folder = "RESEARCH_LINES" if r.get("kind") == "line" else "TOOLKIT"
        write(
            root / folder / (safe_name(r["id"]) + ".md"),
            research_md(r, chunks_by_line.get(r["id"], []))
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

Use the extracted artifact as the working research context. Read OVERVIEW.md, GUIDE.md, REFLEXES.md, DICTIONARY.md, API.md, and TOOLKIT/README.md. Then read MAIN_LINES/README.md and every listed Main Line last. Main Line files are compiled from ordered Research Lines and mark every Research Line boundary; read the corresponding RESEARCH_LINES file or call read([research_line_id]) when one segment is the relevant target.

Choose a route and call changes(...) once using this artifact's snapshot revision as the freshness baseline. Compare the chosen Main Line and Research Line versions with MANIFEST.json. Continue directly from the artifact for every matching version. For each manuscript whose live version is newer, read the current manuscript completely with read([id]), following next_cursor until complete=true, and use that refreshed manuscript as the local working copy.

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
        "main_line_versions": {d["id"]: d.get("version") for d in main_lines},
        "main_line_sequences": {
            d["id"]: [
                {
                    "position": s.get("position"),
                    "id": s.get("research_line_id"),
                    "version": research_by_id.get(s.get("research_line_id"), {}).get("version"),
                    "math_version": research_by_id.get(s.get("research_line_id"), {}).get("math_version"),
                }
                for s in sorted(
                    [x for x in data["main_line_research_lines"] if x.get("main_line_id") == d["id"]],
                    key=lambda x: x.get("position") or 0,
                )
            ]
            for d in main_lines
        },
        "research_line_versions": {
            r["id"]: {"version": r.get("version"), "math_version": r.get("math_version")}
            for r in active_research if r.get("kind") == "line"
        },
        "toolkit_promoted_count": len(promoted),
        "toolkit_limbo_count": len(limbo),
        "brainstorm_count": len(data["brainstorms"]),
        "mirror_format": 9,
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
