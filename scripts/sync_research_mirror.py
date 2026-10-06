# Artifact refresh trigger: validates cleanup and artifact metadata publishing.
# Artifact startup is consumed through the GitHub Actions artifact download path.
#!/usr/bin/env python3
# Recursive composition mirror format 17.
from __future__ import annotations

import json, os, re, shutil, urllib.error, urllib.request
from pathlib import Path
from typing import Any

SUPABASE_URL = os.environ["SUPABASE_URL"].rstrip("/")
SUPABASE_KEY = os.environ["SUPABASE_SECRET_KEY"]
STAGE = Path(".mirror-stage")
SCHEMAS = ("gn3n", "nor", "linp")
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
    subs = data.get("section_subsections", [])
    memberships = data.get("article_sections", [])

    if not comp:
        frontier: dict[str, Any]
        if node_type == "section":
            current = [s for s in subs if s.get("section_id") == node_id]
            frontier = {
                "current": False,
                "subsections_now": len(current),
                "subsections_existing_when_composed": 0,
                "latest_subsection_no_now": max((s.get("subsection_no") or 0 for s in current), default=None),
                "latest_subsection_no_when_composed": None,
            }
        elif node_type == "article":
            current = [m for m in memberships if m.get("article_id") == node_id]
            frontier = {
                "current": False,
                "sections_now": len(current),
                "sections_existing_when_composed": 0,
                "latest_section_position_now": max((m.get("position") or 0 for m in current), default=None),
                "latest_section_position_when_composed": None,
            }
        else:
            row = next((s for s in subs if s.get("id") == node_id), None)
            frontier = {
                "current": False,
                "development_version_now": (row or {}).get("development_version") or (row or {}).get("version"),
                "development_version_when_composed": None,
            }
        return {
            "has_composition": False,
            "composition_version": None,
            "stale": False,
            "stale_dependencies": [],
            "frontier": frontier,
        }

    target_version = comp.get("composition_version")
    snap_rows = [
        s for s in data.get("composition_sources", [])
        if s.get("target_type") == node_type
        and s.get("target_id") == node_id
        and s.get("target_composition_version") == target_version
    ]
    snap = {(s.get("source_type"), s.get("source_id")): s for s in snap_rows}
    stale_dependencies: list[dict[str, Any]] = []

    if node_type == "subsection":
        row = next((s for s in subs if s.get("id") == node_id), None)
        old = snap.get(("subsection", node_id))
        current_version = (row or {}).get("development_version") or (row or {}).get("version")
        seen_version = old.get("source_version") if old else None
        frontier = {
            "current": current_version == seen_version,
            "development_version_now": current_version,
            "development_version_when_composed": seen_version,
        }

    elif node_type == "section":
        current_sources = {
            s["id"]: s for s in subs if s.get("section_id") == node_id
        }
        for source_id, old in [
            (sid, row) for (stype, sid), row in snap.items()
            if stype == "subsection" and bool(row.get("depends_on"))
        ]:
            source_comp = latest_composition(data, "subsection", source_id)
            current_comp = source_comp.get("composition_version") if source_comp else None
            if current_comp != old.get("source_composition_version"):
                stale_dependencies.append({
                    "source_id": source_id,
                    "composition_saw_version": old.get("source_composition_version"),
                    "current_composition_version": current_comp,
                })

        seen_rows = [s for s in snap_rows if s.get("source_type") == "subsection"]
        latest_now = max((s.get("subsection_no") or 0 for s in current_sources.values()), default=None)
        latest_seen = max((s.get("source_position") or 0 for s in seen_rows), default=None)
        frontier = {
            "current": len(seen_rows) == len(current_sources) and latest_seen == latest_now,
            "subsections_now": len(current_sources),
            "subsections_existing_when_composed": len(seen_rows),
            "latest_subsection_no_now": latest_now,
            "latest_subsection_no_when_composed": latest_seen,
        }

    elif node_type == "article":
        current_sources = {
            m["section_id"]: m for m in memberships if m.get("article_id") == node_id
        }
        for source_id, old in [
            (sid, row) for (stype, sid), row in snap.items()
            if stype == "section" and bool(row.get("depends_on"))
        ]:
            source_comp = latest_composition(data, "section", source_id)
            current_comp = source_comp.get("composition_version") if source_comp else None
            if current_comp != old.get("source_composition_version"):
                stale_dependencies.append({
                    "source_id": source_id,
                    "composition_saw_version": old.get("source_composition_version"),
                    "current_composition_version": current_comp,
                })

        seen_rows = [s for s in snap_rows if s.get("source_type") == "section"]
        latest_now = max((m.get("position") or 0 for m in current_sources.values()), default=None)
        latest_seen = max((s.get("source_position") or 0 for s in seen_rows), default=None)
        frontier = {
            "current": len(seen_rows) == len(current_sources) and latest_seen == latest_now,
            "sections_now": len(current_sources),
            "sections_existing_when_composed": len(seen_rows),
            "latest_section_position_now": latest_now,
            "latest_section_position_when_composed": latest_seen,
        }

    else:
        raise ValueError(f"invalid composition node type: {node_type}")

    return {
        "has_composition": True,
        "composition_version": target_version,
        "stale": bool(stale_dependencies),
        "stale_dependencies": stale_dependencies,
        "frontier": frontier,
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
        if status.get("stale_dependencies"):
            bits += ["", "### Stale composition dependencies", ""]
            for x in status["stale_dependencies"]:
                bits.append(
                    f"- {x.get('source_id')}: composition saw "
                    f"v{x.get('composition_saw_version')} → current "
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
    if status.get("stale_dependencies"):
        bits += ["", "## Stale composition dependencies", ""]
        for x in status["stale_dependencies"]:
            bits.append(
                f"- {x.get('source_id')}: composition saw "
                f"v{x.get('composition_saw_version')} → current "
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
Starts a session and returns the artifact snapshot revision, startup broadcasts, notices, and session ID.

### search(query, filters := {})
Discovers Articles, Sections, Subsections, Toolkit, documents, and Brainstorms.

### read(ids, math_versions := {}, cursor := null, page_chars := 9000)
Reads durable Article, Section, Subsection, Toolkit, and Brainstorm content.

### context(research_id)
Shows mathematical dependencies, consumers, supersessions, Article references, and origin.

### composition_status(node_type, node_id)
Shows the current composition version, explicit dependency staleness, and frontier metadata describing what material existed when the composition was written.

### dependencies(node_type, node_id)
Shows the dependency manifest for a manuscript node.

### changes(since_revision := 0, until_revision := null, limit := 100)
Returns live events and current composition state since a revision.

## Development

### new_subsection(session_id, section_id, payload, expected_section_version)
Creates a local Subsection development branch.

### save_subsection(session_id, section_id, payload, expected_section_version, expected_subsection_version)
Edits an existing Subsection by stable ID.

### compose(session_id, node_type, node_id, payload, expected_composition_version)
Writes a deliberately lossy composition. payload contains body and, for Sections and Articles, depends_on as an explicit array of direct lower-level composition IDs. Use [] when independent. Pass NULL only for the first composition; otherwise pass the current composition version. Only the current and immediately previous composition are retained.

### save_research(session_id, payload, expected_version := null)
Creates or edits Section structure/metadata or a Toolkit object.

### save_document(session_id, payload, expected_version := null)
Creates or edits a project document or Article structure/metadata.

## Brainstorms

### brainstorms(active_only := true)
Lists exploratory work.

### save_brainstorm(session_id, payload, expected_version := null)
Creates or edits a Brainstorm.

### promote_brainstorm(session_id, brainstorm_id, payload := {}, expected_version)
Promotes a Brainstorm into manuscript development while preserving its source history.

## Audits and stewardship

### request_audit(session_id, target_type, target_id, target_version)
Queues an independent audit of a canonical version.

### claim_chore(session_id, kinds := {audit,recomposition,maintenance})
Claims one stewardship task.

### finish_chore(session_id, chore_id, outcome := {})
Completes a claimed audit or maintenance task.

## Atomic publication batches

Use stage_batch_chunk, review_staged_batch, and commit_staged_batch for multi-operation publication. stage_batch_chunk accepts JSON text or base64:<blob>; base64 is decoded as UTF-8 before review and commit.

Compose operations carry payload.body, payload.depends_on, expected_composition_version, and optional source_note. Development operations use their ordinary payload contracts.

### artifact_help()
Returns artifact recovery and rebuild information.

### help()
Returns the compact machine-readable interface summary.
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
        "These persistent project directives remain in force until explicitly removed.",
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
        "mirror_format": 17,
        "composition_model": "recursive-composition-v6",
    })

def main():
    selected = os.environ.get("RESEARCH_SCHEMA", "").strip()
    if selected:
        if selected not in SCHEMAS:
            raise SystemExit(f"Unsupported RESEARCH_SCHEMA={selected!r}; expected one of {SCHEMAS}")
        schemas = (selected,)
    else:
        schemas = SCHEMAS

    if STAGE.exists():
        shutil.rmtree(STAGE)
    STAGE.mkdir()
    for schema in schemas:
        print(f"Building clean mirror for {schema}")
        build(schema)
    print("Mirror staging complete.")

if __name__ == "__main__":
    main()
