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
SCHEMAS = ("gn3n", "nor", "linp", "nori")
TABLES = ("nodes","article_sections","dictionary","compositions","composition_sources")
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
    body = (row.get("body") or "").lstrip()
    if body.startswith("# "):
        return body
    return f"# {row.get('title') or row['id']}\n\n{body}"

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
        frontier = status.get("frontier") or {}
        bits += [
            f"- Composition version: {status.get('composition_version')}",
            f"- Composition stale: {status.get('stale')}",
            f"- Subsections existing when composed: {frontier.get('subsections_existing_when_composed')}",
            f"- Subsections now: {frontier.get('subsections_now')}",
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
    if comp:
        bits += ["", "## Composition", "", comp.get("body") or ""]
    frontier = status.get("frontier") or {}
    if frontier and not frontier.get("current", False):
        bits += ["", "## Frontier", "",
                 f"- Development version when composed: {frontier.get('development_version_when_composed')}",
                 f"- Development version now: {frontier.get('development_version_now')}"]
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
        f"- Sections existing when composed: {(status.get('frontier') or {}).get('sections_existing_when_composed')}",
        f"- Sections now: {(status.get('frontier') or {}).get('sections_now')}",
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

def api_text(schema: str) -> str:
    if schema == "nori":
        return """# NORI manuscript API

## Startup and reading
- `nori.boot()` once per independent conversation only. Reuse its `session_id` for every subsequent write. In continued sessions call `nori.status()` and `nori.changes(snapshot_revision, null, 100)`.
- Read the active Article compositions and relevant Section/Subsection manuscripts, including the curated known-obstructions Appendix inside the manuscript when pertinent. `nori.search(query, filters := {})` searches current composed manuscript text and Toolkit. `nori.read_manuscript(type,id,version := null)` reads exact historical composition versions.
- The hierarchy is Article → Section → Subsection, where **Subsection is the smallest durable publication unit**. No Item creation, enumeration or editing, and no Result nodes.

## Research notes: selective non-manuscript memory
- nori.save_note(session,payload,expected_version:=null): create title/body with home_type=project|article|section|subsection and home_id (nori for project); optional stable id, author, labels, related [{type,id,version?}], epistemic_status, lifecycle. Manifests may pin exact manuscript composition versions; note-to-note links track the current note. Revisions require exact expected_version.
- nori.read_note(id,version:=null) reads the current or immediately previous note revision ONLY. On revision, the previous snapshot replaces any older snapshot; no unbounded note history. nori.search_notes(query:='',filters:={}) searches/browses with home_type,home_id,label,lifecycle,epistemic_status,linked_to,limit,offset.
- nori.notes_for(type,id) finds primary-home and linked notes. read_manuscript includes related_notes metadata; manuscripts never automatically incorporate note bodies.
- lifecycle active|resolved|superseded is separate from epistemic_status. Resolution and supersession require disposition, and supersession requires a valid successor_id.
- **Editorial rule:** negative results default to research notes even when completely proved, extensive, or occupying an entire Section. Exception: decisive refutations of important conjectures (such as NORI3 Q9) or independently significant theorems. Mixed manuscripts retain self-standing mathematical advances and link scoped obstruction notes. Preserve proofs, precise hypotheses and certificates when reclassifying; never discard content merely because it is negative.
- Separate brainstorm writes are retired in NORI; use only the selective research-note entity. The selective RESEARCH_NOTES/QUESTIONS.md map records alternatives and obstructions without ordering the agenda. Read pertinent notes, not all notes at startup.

## Manuscript publication
- `nori.publish_subsection(session, subsection_id, body, expected_composition_version, source_note := '')` directly revises a Subsection manuscript. Pass null expected version for its first composition, otherwise exact current version. Version conflicts reject the write.
- `nori.new_subsection(session,section_id,payload,expected_section_version)` creates a coherent new Subsection; then compose it.
- `nori.compose(session,type,id,payload,expected_composition_version)` revises Section and Article exposition. Provide `body` and `depends_on` direct-child IDs; Subsections use `[]`.
- `nori.record_manuscript_audit(session,type,id,exact_composition_version,verdict,claim,explanation,references)` records optional, precisely versioned mathematical verification/corrections.
- `nori.stage_batch_chunk`, `nori.review_staged_batch`, `nori.commit_staged_batch` and `nori.discard_staged_batch` retain all-or-nothing publication.

## History and judgment
- For retired identifiers only: `nori.historical_item(old_id)`, `nori.historical_find(query,limit)` redirect to the fixed GitHub backup and successor Subsection. Historic Items are not active research.
- Grand objective: define ONE natural mathematical structure C and ONE concrete conjecture U(C). Prove explicit reductions showing that resolving U settles both unrestricted NORI1 and the intended long vertex-simple tight-path conclusion for ALL ordinary boundary tournaments. Use NORI1 as a toy mathematical laboratory and boundary tournaments as a test of the SAME conjecture. Explain the implication from U to BOTH results, and what refuting U would establish.
- A serious session may produce **nothing worth publishing**. No tasks, claims, leases, checkpoints, ranked queue, or mandatory progress report.
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
    if schema == 'nori':
        data['research_notes'] = rows(schema, 'research_notes')
        data['research_note_versions'] = rows(schema, 'research_note_versions')

    # Canonical data: all Article/Section/Subsection/Item/Result/Toolkit/auxiliary
    # document records are stored in the single typed nodes table. The following
    # dictionaries are in-memory projections for the existing Markdown builders,
    # not extra database tables, queries, or persistent caches.
    projected = {"documents": [], "research": [], "section_subsections": [],
                 "items": [], "item_results": [], "brainstorms": []}
    source_by_type = {
        "article": "documents", "overview": "documents",
        "guide": "documents", "reflexes": "documents",
        "section": "research", "toolkit": "research",
        "subsection": "section_subsections", "item": "items",
        "result": "item_results", "brainstorm": "brainstorms",
    }
    for node in data["nodes"]:
        group = source_by_type.get(node["type"])
        if group:
            rec = dict(node.get("data") or {})
            rec["id"] = node["id"]
            rec["consumes"] = node.get("consumes", [])
            rec["consumed_by"] = node.get("consumed_by", [])
            rec["type"] = node["type"]
            projected[group].append(rec)
    data.update(projected)
    if schema == 'nori':
        # Retired mathematical units remain in database history, not in publication.
        data['section_subsections'] = [x for x in data['section_subsections'] if x.get('archived_at') is None]
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

    if schema != "nori":
        write(root / "OVERVIEW.md", doc_md(overview) if overview else "# Overview\n\nNo overview.")
    write(root / "GUIDE.md", doc_md(guide) if guide else "# Guide\n\nNo guide.")
    write(root / "REFLEXES.md", doc_md(reflexes) if reflexes else "# Research Reflexes\n\nNo reflexes.")
    write(root / "DICTIONARY.md", dictionary_text(data["dictionary"]))
    write(root / "API.md", api_text(schema))
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
        "Subsections are coherent publication manuscripts. Negative-result notes remain separate, and retired Subsections are excluded from the current tree.",
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


    if schema == "nori":
        # Independent research-memory export, excluded from manuscript compositions.
        notes = sorted(data["research_notes"], key=lambda n: ((n.get("title") or "").casefold(), n["id"]))
        history = data["research_note_versions"]
        note_index = [
            "# NORI selective research notes", "",
            "Non-manuscript research memory. Manuscript text and numbering are unaffected. Only the current revision and one immediately prior snapshot are retained.",
            "Find related notes using nori.notes_for(type,id), search with nori.search_notes, or read the current/previous revision via nori.read_note(id,version).", "",
        ]
        by_manuscript = {}
        by_question = {"active": [], "obstructions": [], "closed": []}
        for n in notes:
            name = safe_name(n["id"])
            meta = [
                "# " + n["title"], "",
                "- Stable ID: " + n["id"],
                "- Author: " + str(n.get("author") or "unspecified; session provenance retained"),
                "- Primary home: " + n["home_type"] + ":" + n["home_id"],
                "- Labels: " + ", ".join(n.get("labels") or []),
                "- Lifecycle: " + n.get("lifecycle","active"),
                "- Epistemic status: " + n.get("epistemic_status","open"),
                "- Current version: " + str(n.get("version")),
                "- Retention: current and at most one previous snapshot",
                "- Created session: " + n.get("created_session",""),
                "- Updated session: " + n.get("updated_session",""),
                "- Disposition: " + str(n.get("disposition") or "none"),
                "- Successor: " + str(n.get("successor_id") or "none"),
                "", "## Related references", "",
            ]
            refs = n.get("related") or []
            meta.extend(["- " + str(ref.get("type")) + ":" + str(ref.get("id")) +
                         (", exact version " + str(ref["version"]) if "version" in ref else "")
                         for ref in refs] or ["- None"])
            meta += ["", "## Research note", "", n.get("body") or ""]
            write(root / "RESEARCH_NOTES" / (name + ".md"), "\n".join(meta))
            for h in history:
                if h.get("note_id") != n["id"]:
                    continue
                snap = h.get("snapshot") or {}
                text_ = "\n".join(["# " + str(snap.get("title")), "",
                          "- Note: " + n["id"], "- Version: " + str(h["version"]),
                          "- Session: " + str(h.get("session_id")),
                          "- Author: " + str(snap.get("author") or "unspecified"),
                          "- Recorded: " + str(h.get("recorded_at")),
                          "- Lifecycle: " + str(snap.get("lifecycle")),
                          "- Epistemic status: " + str(snap.get("epistemic_status")),
                          "", str(snap.get("body") or "")])
                write(root / "RESEARCH_NOTES" / "HISTORY" / name / ("v" + str(h["version"]) + ".md"), text_)
            entry = "- [" + n["title"] + "](" + name + ".md) (" + n["home_type"] + ":" + n["home_id"] + "; " + n.get("lifecycle","active") + "; " + n.get("epistemic_status","open") + ")"
            note_index.append(entry)
            paragraphs = [p.strip().replace("\n", " ") for p in (n.get("body") or "").split("\n\n")]
            insight = next((p for p in paragraphs if p and not p.startswith("#")), "")
            q_entry = entry + (" — " + insight[:290] + ("…" if len(insight)>290 else "") if insight else "")
            for typ, ident in [(n["home_type"],n["home_id"])] + [
                (ref["type"],ref["id"]) for ref in refs if ref.get("type") in ("article","section","subsection")
            ]:
                by_manuscript.setdefault((typ,ident), []).append(n)
            if n.get("lifecycle") != "active":
                by_question["closed"].append(q_entry + " — " + str(n.get("disposition") or ""))
            elif "obstruction" in (n.get("labels") or []) and n.get("epistemic_status") in ("proved","method_limitation"):
                by_question["obstructions"].append(q_entry)
            else:
                by_question["active"].append(q_entry)
        note_index += ["", "[Editorial migration map: retired Subsections and their preserved destinations](MIGRATION.md)"]
        write(root / "RESEARCH_NOTES" / "README.md", "\n".join(note_index))
        for (typ,ident), entries in by_manuscript.items():
            lines = [
                "# Research notes linked to " + typ + " " + ident, "",
                "Sidecar only; no note body is included in the mathematical manuscript.", "",
            ]
            for n in sorted(entries,key=lambda n:n["title"].casefold()):
                lines.append("- [" + n["title"] + "](../" + safe_name(n["id"]) + ".md) — " +
                             n.get("lifecycle","active") + "/" + n.get("epistemic_status","open"))
            write(root / "RESEARCH_NOTES" / "BY_MANUSCRIPT" / (safe_name(ident) + ".md"), "\n".join(lines))
        question_map = [
            "# Consequential questions and established obstructions", "",
            "Discovery map, NOT a ranked task list. Consult the active manuscript (including its known-obstructions appendix) for proved mathematics. Read only relevant notes.", "",
            "## Open questions and mechanisms", "",
            *(by_question["active"][:12] or ["- None recorded."]),
            *(["- Additional open notes: see README.md or search_notes; the displayed selection is alphabetical, not a ranking."] if len(by_question["active"])>12 else []),
            "", "## Established and method-scoped obstructions", "",
            *(by_question["obstructions"][:12] or ["- Review the known-obstructions appendix in the active manuscript."]),
            *(["- Further obstructions: see README.md or search_notes."] if len(by_question["obstructions"])>12 else []),
            "", "## Resolved and superseded", "",
            *(by_question["closed"][:6] or ["- None recorded."]),
            *(["- More resolved/superseded notes: see README.md or search_notes."] if len(by_question["closed"])>6 else [])
        ]
        write(root / "RESEARCH_NOTES" / "QUESTIONS.md", "\n".join(question_map))

        # Every retired manuscript has an exact publication-to-note pointer.
        retired_subsections = sorted(
            [n for n in data["nodes"] if n.get("type") == "subsection" and n.get("archived_at")],
            key=lambda n: ((n.get("section_id") or ""), (n.get("subsection_no") or 0),n["id"])
        )
        retired_sections = sorted(
            [n for n in data["nodes"] if n.get("type") == "section" and n.get("archived_at")],
            key=lambda n:n["id"])
        migration = [
            "# Research-note migration and manuscript retirements", "",
            "Editorial retirement preserves entire proof texts in notes and original exact composition versions in the database. Retired manuscripts no longer appear in the assembled publication.",
            "", "## Fully retired Subsections", "",
        ]
        for old in retired_subsections:
            links = []
            for note in notes:
                if any(ref.get("type") == "subsection" and ref.get("id") == old["id"] for ref in (note.get("related") or [])):
                    links.append("[" + note["title"] + "](" + safe_name(note["id"]) + ".md)")
            replacement_id = (old.get("data") or {}).get("editorial_consolidated_into")
            if replacement_id:
                successor = next((x for x in data["nodes"] if x.get("id") == replacement_id), None)
                sec_id = successor.get("section_id") if successor else None
                if successor and not sec_id:
                    sec_id = (successor.get("data") or {}).get("section_id")
                art_id = next((a["article_id"] for a in data["article_sections"] if a.get("section_id") == sec_id), None)
                if art_id:
                    links.append("[Complete proof consolidated into " + replacement_id + "](../grand_conjecture/" +
                                 art_id + "/" + sec_id + "/" + replacement_id + ".md)")
                else:
                    links.append("Complete proof consolidated into active Subsection " + replacement_id)
            migration.append("- " + old["id"] + " (" + str(old.get("section_id") or "?") + ") -> " +
                            (", ".join(links) if links else "UNLINKED: audit needed"))
        migration += ["", "## Fully retired Sections", ""]
        for old in retired_sections:
            links = []
            for note in notes:
                if any(ref.get("type") == "section" and ref.get("id") == old["id"] for ref in (note.get("related") or [])):
                    links.append("[" + note["title"] + "](" + safe_name(note["id"]) + ".md)")
            migration.append("- " + old["id"] + " -> " + (", ".join(links) if links else "UNLINKED: audit needed"))
        migration += ["", "## Active Subsections with extracted negative proof blocks", ""]
        active_sub_ids = {n["id"] for n in data["nodes"] if n.get("type") == "subsection" and not n.get("archived_at")}
        for note in notes:
            for ref in note.get("related") or []:
                if ref.get("type") == "subsection" and ref.get("id") in active_sub_ids and "version" in ref:
                    migration.append("- [" + note["title"] + "](" + safe_name(note["id"]) + ".md) -> " +
                                     ref["id"] + " (source composition v" + str(ref["version"]) + ")")
        write(root / "RESEARCH_NOTES" / "MIGRATION.md", "\n".join(migration))


    for b in data["brainstorms"]:
        write(
            root / "BRAINSTORMS" / (safe_name(b["id"]) + ".md"),
            f"# {b.get('title') or b['id']}\n\n{b.get('seed') or ''}\n\n{b.get('body') or ''}"
        )

    boot = f"""# Startup instructions

Review startup notices returned by the project's boot API. Preserve its session ID for the conversation and refresh live status/changes on follow-ups.

Read BROADCASTS.md first. Then read GUIDE.md, REFLEXES.md, DICTIONARY.md, API.md, and the manuscript tree under grand_conjecture/. Select pertinent Article compositions, their supporting Section/Subsection proofs, and relevant research notes. The project's objective and known obstructions are defined in its research state, not duplicated in auxiliary documents.

Use the snapshot revision below as the freshness baseline when calling changes(...); refresh the artifact if it is stale. Follow the project's actual publication hierarchy, and preserve precise hypotheses and proofs.

Snapshot revision: {rev.get('revision')}
Generated: {rev.get('generated_at')}
"""
    write(root / "BOOT.md", boot)

    # The research manuscript is exported as the database's canonical folder tree.
    # Auxiliary material (guide, toolkit, brainstorms, etc.) remains at the schema root.
    for old in ("ARTICLES", "SECTIONS", "SUBSECTIONS"):
        shutil.rmtree(root / old, ignore_errors=True)
    tree = tree_paths(schema)
    if schema == "nori":
        # Only selected-child parent compositions represent current papers.
        by_id = {n["id"]: n for n in data["nodes"]}
        superseded = {
            n["id"] for n in data["nodes"]
            if n.get("data", {}).get("research_status") == "superseded"
        }
        current_articles = [a for a in articles if a["id"] not in superseded]
        for node in tree:
            relative = Path(node["path"])
            if relative.is_absolute() or ".." in relative.parts or relative.parts[0] != "grand_conjecture":
                raise ValueError(f"invalid canonical tree path: {relative}")
            identifier = relative.stem
            node_info = by_id.get(identifier, {})
            if node_info.get("type") in ("article", "section"):
                # Eliminate independently authored parent summaries.
                continue
            if identifier in superseded:
                write(root / "SUPERSEDED" / relative.relative_to("grand_conjecture"),
                      "# SUPERSEDED RESEARCH — retained for historical reference\n\n"
                      + (node_info.get("data", {}).get("superseded_reason") or
                         "Superseded by the refutation of the NORI3 one-switch conjecture.")
                      + "\n\n" + (node.get("content") or ""))
            else:
                write(root / relative, node.get("content") or "")
        # Latest database parent composition is the selected-child assembly.
        current_comps = {}
        for composition in data["compositions"]:
            if composition["node_type"] in ("article", "section"):
                key = (composition["node_type"], composition["node_id"])
                if key not in current_comps or (
                    composition.get("composition_version") or 0
                ) > (current_comps[key].get("composition_version") or 0):
                    current_comps[key] = composition
        active_article_ids = {a["id"] for a in current_articles}
        article_by_section = {
            x["section_id"]: x["article_id"]
            for x in data["article_sections"]
            if x["article_id"] in active_article_ids
        }
        for a in current_articles:
            comp = current_comps.get(("article", a["id"]))
            if not comp:
                raise ValueError(f"missing assembled Article composition {a['id']}")
            write(root / "grand_conjecture" / a["id"] / "MANUSCRIPT.md", comp["body"])
        for section_id, article_id in article_by_section.items():
            if section_id in superseded:
                continue
            comp = current_comps.get(("section", section_id))
            if not comp:
                raise ValueError(f"missing assembled Section composition {section_id}")
            write(root / "grand_conjecture" / article_id / section_id / "MANUSCRIPT.md", comp["body"])

        archive = ["# Superseded research", "",
                   "These manuscripts retain their proofs but are not active.",
                   ""]
        for a in articles:
            if a["id"] in superseded:
                archive.append("- " + a["title"] + ": " +
                    str(by_id[a["id"]].get("data", {}).get("superseded_reason") or "Superseded"))
        write(root / "SUPERSEDED" / "README.md", "\n".join(archive))
        index = ["# Active research Articles", "",
                 "Each paper assembles selected Subsection compositions through "
                 "Section compositions. Superseded work is retained in "
                 "[SUPERSEDED](../SUPERSEDED/README.md).", ""]
        for a in current_articles:
            index.append(f"- [{a.get('title') or a['id']}]({safe_name(a['id'])}/MANUSCRIPT.md)")
    else:
        for node in tree:
            relative = Path(node["path"])
            if relative.is_absolute() or ".." in relative.parts or relative.parts[0] != "grand_conjecture":
                raise ValueError(f"invalid canonical tree path: {relative}")
            write(root / relative, node.get("content") or "")
        index = ["# Grand conjecture", "",
                 "Research hierarchy: Articles → Sections → Subsections → Items.",
                 "Each level's composition is adjacent to its corresponding directory.", ""]
        for a in articles:
            index.append(f"- [{a.get('title') or a['id']}]({safe_name(a['id'])}.md)")
    write(root / "grand_conjecture" / "README.md", "\n".join(index))


    write_json(root / "MANIFEST.json", {
        "schema": schema,
        "research_note_count": len(data.get("research_notes", [])),
        "active_subsection_count": len([n for n in data["nodes"] if n.get("type")=="subsection" and not n.get("archived_at")]),
        "retired_subsection_count": len([n for n in data["nodes"] if n.get("type")=="subsection" and n.get("archived_at")]),
        "active_section_count": len([n for n in data["nodes"] if n.get("type")=="section" and not n.get("archived_at")]),
        "retired_section_count": len([n for n in data["nodes"] if n.get("type")=="section" and n.get("archived_at")]),
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
        "item_count": len(data["items"]),
        "result_count": len(data["item_results"]),
        "brainstorm_count": len(data["brainstorms"]),
        "startup_broadcasts": broadcasts,
        "mirror_format": 20 if schema == "nori" else 18,
        "composition_model": "selected-child-assembly-v1" if schema == "nori" else "recursive-composition-v7",
    })

def tree_paths(schema: str) -> list[dict[str, Any]]:
    """Read the canonical database tree, in paginated filesystem form."""
    out, offset = [], 0
    while True:
        page = rpc("research_mirror_tree_paths", {
            "p_schema": schema, "p_offset": offset, "p_limit": PAGE
        })
        got = page["rows"]
        out.extend(got)
        if page["complete"]:
            return out
        offset += len(got)


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

# Regeneration marker: composition clean slate 2026-10-07; resync NOR, GN3N, and LINP.
# Resync marker: restored historical consumed_by links 2026-10-08 across NOR, GN3N, LINP.
