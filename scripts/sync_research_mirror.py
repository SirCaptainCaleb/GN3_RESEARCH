# Artifact refresh trigger: validates cleanup and artifact metadata publishing.
# Artifact startup is consumed through the GitHub Actions artifact download path.
#!/usr/bin/env python3
# Recursive composition mirror format 16.
from __future__ import annotations

import json, os, re, shutil, urllib.error, urllib.request
from pathlib import Path
from typing import Any

SUPABASE_URL = os.environ["SUPABASE_URL"].rstrip("/")
SUPABASE_KEY = os.environ["SUPABASE_SECRET_KEY"]
STAGE = Path(".mirror-stage")
SCHEMAS = ("gn3n", "linp")
TABLES = ("documents","research","section_subsections","article_sections","brainstorms","dictionary","compositions","composition_sources")
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

def latest_composition(data: dict[str, list[dict[str, Any]]], node_type: str, node_id: str) -> dict[str, Any] | None:
    rows_ = [
        c for c in data.get("compositions", [])
        if c.get("node_type") == node_type and c.get("node_id") == node_id
    ]
    return max(rows_, key=lambda x: x.get("composition_version") or 0) if rows_ else None


def composition_status(data: dict[str, list[dict[str, Any]]], node_type: str, node_id: str) -> dict[str, Any]:
    comp = latest_composition(data, node_type, node_id)
    if not comp:
        return {
            "has_composition": False,
            "composition_version": None,
            "stale": False,
            "stale_children": [],
            "development_changed": False,
        }

    target_version = comp.get("composition_version")
    snap_rows = [
        s for s in data.get("composition_sources", [])
        if s.get("target_type") == node_type
        and s.get("target_id") == node_id
        and s.get("target_composition_version") == target_version
    ]
    snap = {(s.get("source_type"), s.get("source_id")): s for s in snap_rows}
    subs = data.get("section_subsections", [])
    memberships = data.get("article_sections", [])

    development_changed = False
    stale_children: list[dict[str, Any]] = []

    if node_type == "subsection":
        row = next((s for s in subs if s.get("id") == node_id), None)
        old = snap.get(("subsection", node_id))
        if row is not None:
            current_version = row.get("development_version") or row.get("version")
            development_changed = old is None or current_version != old.get("source_version")

    elif node_type == "section":
        current_children = {
            s["id"]: s for s in subs if s.get("section_id") == node_id
        }
        for child_id in sorted(current_children):
            child_comp = latest_composition(data, "subsection", child_id)
            current_comp = child_comp.get("composition_version") if child_comp else None
            old = snap.get(("subsection", child_id))
            if current_comp is not None and (
                old is None
                or (
                    bool(old.get("depends_on"))
                    and current_comp != old.get("source_composition_version")
                )
            ):
                stale_children.append({
                    "source_id": child_id,
                    "parent_saw_composition_version": old.get("source_composition_version") if old else None,
                    "current_composition_version": current_comp,
                    "depends_on": bool(old.get("depends_on")) if old else False,
                })
        for (source_type, child_id), old in snap.items():
            if source_type == "subsection" and old.get("depends_on") and child_id not in current_children:
                stale_children.append({
                    "source_id": child_id,
                    "parent_saw_composition_version": old.get("source_composition_version"),
                    "current_composition_version": None,
                    "depends_on": True,
                })

    elif node_type == "article":
        current_children = {
            m["section_id"]: m for m in memberships if m.get("article_id") == node_id
        }
        for child_id in sorted(current_children):
            child_comp = latest_composition(data, "section", child_id)
            current_comp = child_comp.get("composition_version") if child_comp else None
            old = snap.get(("section", child_id))
            if current_comp is not None and (
                old is None
                or (
                    bool(old.get("depends_on"))
                    and current_comp != old.get("source_composition_version")
                )
            ):
                stale_children.append({
                    "source_id": child_id,
                    "parent_saw_composition_version": old.get("source_composition_version") if old else None,
                    "current_composition_version": current_comp,
                    "depends_on": bool(old.get("depends_on")) if old else False,
                })
        for (source_type, child_id), old in snap.items():
            if source_type == "section" and old.get("depends_on") and child_id not in current_children:
                stale_children.append({
                    "source_id": child_id,
                    "parent_saw_composition_version": old.get("source_composition_version"),
                    "current_composition_version": None,
                    "depends_on": True,
                })

    return {
        "has_composition": True,
        "composition_version": target_version,
        "stale": development_changed if node_type == "subsection" else bool(stale_children),
        "stale_children": stale_children,
        "development_changed": development_changed,
        "composed_through_revision": comp.get("composed_through_event_id"),
        "source_note": comp.get("source_note") or "",
        "body_chars": len(comp.get("body") or ""),
    }

def research_md(row: dict[str, Any], subsections: list[dict[str, Any]] | None = None,
                data: dict[str, list[dict[str, Any]]] | None = None) -> str:
    bits = [f"# {row.get('title') or row['id']}"]
    if row.get("simplified_statement"):
        bits += ["", f"**Summary:** {row['simplified_statement']}"]
    if row.get("statement"):
        bits += ["", "## Statement", "", row["statement"]]
    if row.get("body"):
        bits += ["", "## Composition" if row.get("kind") == "section" else "## Body", "", row["body"]]

    bits += ["", "## Metadata", "",
             f"- ID: {row['id']}",
             f"- Kind: {row.get('kind')}",
             f"- Version: {row.get('version')}",
             f"- Math version: {row.get('math_version')}",
             f"- Audit: {row.get('audit_status')}",
             f"- Refutation: {row.get('refutation_status')}"]

    if row.get("kind") == "section" and data is not None:
        status = composition_status(data, "section", row["id"])
        bits += [
            f"- Composition version: {status.get('composition_version')}",
            f"- Composition stale: {status.get('stale')}",
            "", "## Development tree", "",
        ]
        subsections = subsections or []
        if not subsections:
            bits.append("- No Subsections recorded.")
        else:
            for s in sorted(subsections, key=lambda x: x.get("subsection_no") or 0):
                ss = composition_status(data, "subsection", s["id"])
                title = s.get("title") or "(untitled)"
                bits.append(
                    f"- [Subsection {s.get('subsection_no')} — {title}](../SUBSECTIONS/{safe_name(s['id'])}.md) "
                    f"(`{s['id']}`; development v{s.get('development_version') or s.get('version')}; "
                    f"composition v{ss.get('composition_version')}; stale={ss.get('stale')})"
                )
        if status.get("stale_children"):
            bits += ["", "### Stale child compositions", ""]
            for x in status["stale_children"]:
                bits.append(
                    f"- {x.get('source_id')}: parent saw composition "
                    f"v{x.get('parent_saw_composition_version')} → current "
                    f"v{x.get('current_composition_version')}"
                )
    return "\n".join(bits)


def subsection_md(row: dict[str, Any], data: dict[str, list[dict[str, Any]]]) -> str:
    comp = latest_composition(data, "subsection", row["id"])
    status = composition_status(data, "subsection", row["id"])
    bits = [
        f"# {row.get('title') or row['id']}",
        "",
        "## Metadata",
        "",
        f"- ID: {row['id']}",
        f"- Parent Section: {row.get('section_id')}",
        f"- Position: {row.get('subsection_no')}",
        f"- Row version: {row.get('version')}",
        f"- Development version: {row.get('development_version') or row.get('version')}",
        f"- Composition version: {status.get('composition_version')}",
        f"- Composition stale: {status.get('stale')}",
    ]
    deps = row.get("declared_dependencies") or []
    if deps:
        bits.append(f"- Provisional declared dependencies: {json.dumps(deps, ensure_ascii=False)}")
    bits += ["", "## Composition", "", comp.get("body") if comp else "(none yet)",
             "", "## Development", "", row.get("body") or ""]
    if status.get("development_changed"):
        bits += ["", "## Uncompressed development", "",
                 "- Development has changed since this Subsection's current composition."]
    return "\n".join(bits)

def article_md(row: dict[str, Any], sequence_rows: list[dict[str, Any]],
               research_by_id: dict[str, dict[str, Any]],
               data: dict[str, list[dict[str, Any]]]) -> str:
    status = composition_status(data, "article", row["id"])
    bits = [
        f"# {row.get('title') or row['id']}",
        "",
        "## Composition status",
        "",
        f"- Composition version: {status.get('composition_version')}",
        f"- Stale: {status.get('stale')}",
        f"- Composed through revision: {status.get('composed_through_revision')}",
        "",
        "## Composition",
        "",
        row.get("body") or "(no Article composition yet)",
        "",
        "## Contained Sections",
        "",
    ]
    members = sorted(
        [s for s in sequence_rows if s.get("article_id") == row["id"]],
        key=lambda s: s.get("position") or 0,
    )
    if not members:
        bits.append("- No Sections are currently contained.")
    else:
        for s in members:
            r = research_by_id.get(s.get("section_id"))
            if not r:
                continue
            ss = composition_status(data, "section", r["id"])
            bits.append(
                f"- {s.get('position')}. [{r.get('title') or r['id']}](../SECTIONS/{safe_name(r['id'])}.md) "
                f"(`{r['id']}`; composition v{ss.get('composition_version')}; stale={ss.get('stale')})"
            )
    if status.get("stale_children"):
        bits += ["", "## Stale child compositions", ""]
        for x in status["stale_children"]:
            bits.append(
                f"- {x.get('source_id')}: parent saw composition "
                f"v{x.get('parent_saw_composition_version')} → current "
                f"v{x.get('current_composition_version')}"
            )
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

The artifact is a snapshot; these RPCs are the live worker interface.

## Startup and reading

### boot()
Starts a session and returns the artifact snapshot/revision, persistent startup broadcasts, and stewardship notices. Read broadcasts before selecting a research tactic.

### search(query, filters := {})
Discovers Articles, Sections, Subsection development, Toolkit, documents, and optionally Brainstorms.

### read(ids, math_versions := {}, cursor := null, page_chars := 9000)
Reads exact durable content. Article and Section bodies are compositions. Stable Subsection IDs are also readable; a Subsection read shows both its composition and full development body.

### composition_status(node_type, node_id)
Returns one stale flag. For Sections and Articles it also returns stale_children: direct child compositions that require parent reconsideration. Raw child development never stales a parent.

### changes(since_revision := 0, until_revision := null, limit := 100)
Returns compact live events plus current Article/Section composition states.

## Development

### new_subsection(session_id, section_id, payload, expected_section_version)
Creates a cheap local development container. Multiple Subsections may be developed in parallel.

### save_subsection(session_id, section_id, payload, expected_section_version, expected_subsection_version)
Edits any Subsection. Supply payload.subsection_id (or payload.id). Development edits do not rewrite or stale the parent Section, bump its math version, or regenerate an Article. payload.dependencies are stored provisionally on the Subsection.

### compose(session_id, node_type, node_id, payload, expected_version)
The one recursive cold-composition operation for subsection, section, and article. payload.body is required and must be a deliberate rewrite. Section and Article composition also require payload.depends_on: the direct child IDs this composition relies on, using [] when none. A substantive Section composition must explicitly declare canonical mathematical dependencies.

Parent staleness is composition-to-composition. Recomposing a depended-on child stales the parent. Recomposing an explicitly excluded child does not. A newly added child remains invisible to parent staleness until it receives a composition; that first composition stales the parent as a signal worth reconsidering.

### save_research(session_id, payload, expected_version := null)
Creates/edits Sections or Toolkit. New route-shaped work should normally develop in Subsections; Toolkit remains for broadly reusable mathematics.

### save_document(session_id, payload, expected_version := null)
Creates/edits documents and Article containment. Article prose is never generated from section_ids. Supplying an Article body performs a manual composition.


## Brainstorms

### brainstorms(active_only := true)
Lists loose exploratory work.

### save_brainstorm(session_id, payload, expected_version := null)
Creates/edits a Brainstorm.

### promote_brainstorm(session_id, brainstorm_id, payload := {}, expected_version)
Promotes developed work into a Section while preserving the Brainstorm.

## Dependencies, audits, and stewardship

### context(research_id)
Shows canonical mathematical dependencies, consumers, supersessions, Article references, and origin. These dependencies are orthogonal to composition dependencies.

### request_audit(session_id, target_type, target_id, target_version)
Queues an independent audit of a canonical Section/Toolkit math version or Article version.

### claim_chore(session_id, kinds := {audit,recomposition,maintenance})
Claims one stewardship task. Recomposition chores follow stale composition frontiers, not raw development or arbitrary size limits. Calling compose successfully resolves the matching recomposition chore.

### finish_chore(session_id, chore_id, outcome := {})
Completes audits and maintenance chores.

## Atomic publication batches

stage_batch_chunk → review_staged_batch → commit_staged_batch is the atomic path for large multi-object publication. Batch operations include new_subsection, save_subsection, compose, save_research, save_document, and Brainstorm operations.

### artifact_help()
Returns artifact recovery/rebuild information.

### help()
Returns a compact machine-readable summary.

Persistent startup broadcasts are administered in research_core with add_startup_broadcast(...) and remove_startup_broadcast(...). They have no expiry.
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
    broadcasts = context(schema, "startup_broadcasts")

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

    broadcast_lines = [
        "# Startup broadcasts", "",
        "These are persistent project directives. They do not expire; they remain in force until explicitly removed.",
        "",
    ]
    if broadcasts:
        for b in broadcasts:
            broadcast_lines += [
                f"## {b.get('title') or b.get('broadcast_id')}",
                "",
                b.get("body") or "",
                "",
                f"- ID: {b.get('broadcast_id')}",
                f"- Scope: {b.get('scope')}",
                "",
            ]
    else:
        broadcast_lines.append("No active startup broadcasts.")
    write(root / "BROADCASTS.md", "\n".join(broadcast_lines))

    active_research = [r for r in data["research"] if r.get("archived_at") is None]
    research_by_id = {r["id"]: r for r in active_research}
    subsections_by_section: dict[str, list[dict[str, Any]]] = {}
    for s in data["section_subsections"]:
        subsections_by_section.setdefault(s["section_id"], []).append(s)

    article_index = [
        "# Articles", "",
        "Articles are top-level routes. Each file contains a manually written composition plus links to its contained Sections.",
        "",
    ]
    for d in articles:
        fn = safe_name(d["id"]) + ".md"
        status = composition_status(data, "article", d["id"])
        article_index.append(
            f"- [{d.get('title') or d['id']}]({fn}) (`{d['id']}`) — "
            f"composition v{status.get('composition_version')}; stale={status.get('stale')}"
        )
        write(root / "ARTICLES" / fn, article_md(d, data["article_sections"], research_by_id, data))
    if not articles:
        article_index.append("No active Articles.")
    write(root / "ARTICLES" / "README.md", "\n".join(article_index))

    article_by_id = {d["id"]: d for d in articles}
    membership_by_section = {
        m.get("section_id"): m for m in data["article_sections"]
    }

    section_index = [
        "# Sections", "",
        "Sections are coherent research regions with manually written compositions and preserved Subsection development. They may remain uncontained while their Article-level route is unclear.",
        "",
    ]
    section_items = sorted(
        [r for r in active_research if r.get("kind") == "section"],
        key=lambda r: (r.get("title") or "").casefold(),
    )
    for r in section_items:
        fn = safe_name(r["id"]) + ".md"
        membership = membership_by_section.get(r["id"])
        status = composition_status(data, "section", r["id"])
        if membership:
            art = article_by_id.get(membership.get("article_id"), {})
            where = f"Article: {art.get('title') or membership.get('article_id')} at position {membership.get('position')}"
        else:
            where = "uncontained development"
        section_index.append(
            f"- [{r.get('title') or r['id']}]({fn}) (`{r['id']}`) — {where}; "
            f"composition v{status.get('composition_version')}; stale={status.get('stale')}"
        )
        write(
            root / "SECTIONS" / fn,
            research_md(r, subsections_by_section.get(r["id"], []), data)
        )
    if not section_items:
        section_index.append("No active Sections.")
    write(root / "SECTIONS" / "README.md", "\n".join(section_index))

    subsection_index = [
        "# Subsections", "",
        "Subsections are cheap local development containers. Their files preserve full development independently of whatever survives into parent compositions.",
        "",
    ]
    for s in sorted(
        data["section_subsections"],
        key=lambda x: (x.get("section_id") or "", x.get("subsection_no") or 0),
    ):
        status = composition_status(data, "subsection", s["id"])
        fn = safe_name(s["id"]) + ".md"
        subsection_index.append(
            f"- [{s.get('title') or s['id']}]({fn}) (`{s['id']}`) — "
            f"parent {s.get('section_id')}; development v{s.get('development_version') or s.get('version')}; "
            f"composition v{status.get('composition_version')}; stale={status.get('stale')}"
        )
        write(root / "SUBSECTIONS" / fn, subsection_md(s, data))
    write(root / "SUBSECTIONS" / "README.md", "\n".join(subsection_index))

    toolkit_items = sorted(
        [r for r in active_research if r.get("kind") == "toolkit"],
        key=lambda r: ((r.get("toolkit_type") or ""), (r.get("title") or "").casefold(), r.get("id") or "")
    )
    for r in toolkit_items:
        write(root / "TOOLKIT" / (safe_name(r["id"]) + ".md"), research_md(r))

    toolkit_index = [
        "# Toolkit", "",
        "Toolkit is for genuinely reusable mathematics whose natural formulation transcends its originating route. There is no intermediate Toolkit state: an object either is Toolkit or it is not. Route-local lemma graphs belong in Sections/Subsections.",
        "",
    ]
    toolkit_index.extend(toolkit_entry_line(r) for r in toolkit_items)
    if not toolkit_items:
        toolkit_index.append("Toolkit is empty.")
    write(root / "TOOLKIT" / "README.md", "\n".join(toolkit_index))

    for b in data["brainstorms"]:
        write(
            root / "BRAINSTORMS" / (safe_name(b["id"]) + ".md"),
            f"# {b.get('title') or b['id']}\n\n{b.get('seed') or ''}\n\n{b.get('body') or ''}"
        )

    boot = f"""# Startup instructions

Review startup_notices returned by boot().

Use the extracted artifact as the working research context. Read BROADCASTS.md **first**, before selecting any research tactic. Then read OVERVIEW.md, GUIDE.md, REFLEXES.md, DICTIONARY.md, API.md, and TOOLKIT/README.md. Then read ARTICLES/README.md.

Call changes(...) once using this artifact's snapshot revision as the freshness baseline. If the snapshot is substantially stale, regenerate it before downloading.

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
        "article_versions": {
            d["id"]: {
                "version": d.get("version"),
                "composition": composition_status(data, "article", d["id"]),
            }
            for d in articles
        },
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
            r["id"]: {
                "version": r.get("version"),
                "math_version": r.get("math_version"),
                "composition": composition_status(data, "section", r["id"]),
            }
            for r in section_items
        },
        "subsection_versions": {
            s["id"]: {
                "section_id": s.get("section_id"),
                "version": s.get("version"),
                "development_version": s.get("development_version") or s.get("version"),
                "composition": composition_status(data, "subsection", s["id"]),
            }
            for s in data["section_subsections"]
        },
        "toolkit_count": len(toolkit_items),
        "brainstorm_count": len(data["brainstorms"]),
        "startup_broadcasts": broadcasts,
        "mirror_format": 16,
        "composition_model": "recursive-composition-v6",
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
