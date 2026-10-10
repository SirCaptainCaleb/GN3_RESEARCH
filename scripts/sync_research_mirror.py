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
- Read `OVERVIEW.md`, `KNOWN_OBSTRUCTIONS.md`, all eight Article compositions, and the relevant Section/Subsection manuscripts. `nori.search(query, filters := {})` searches **current composed manuscript text**, overview and Toolkit. `nori.read_manuscript(type,id,version := null)` reads exact historical composition versions.
- The hierarchy is Article → Section → Subsection, where **Subsection is the smallest durable publication unit**. No Item creation, enumeration or editing, and no Result nodes.

## Manuscript publication
- `nori.publish_subsection(session, subsection_id, body, expected_composition_version, source_note := '')` directly revises a Subsection manuscript. Pass null expected version for its first composition, otherwise exact current version. Version conflicts reject the write.
- `nori.new_subsection(session,section_id,payload,expected_section_version)` creates a coherent new Subsection; then compose it.
- `nori.compose(session,type,id,payload,expected_composition_version)` revises Section and Article exposition. Provide `body` and `depends_on` direct-child IDs; Subsections use `[]`.
- `nori.record_manuscript_audit(session,type,id,exact_composition_version,verdict,claim,explanation,references)` records optional, precisely versioned mathematical verification/corrections.
- `nori.stage_batch_chunk`, `nori.review_staged_batch`, `nori.commit_staged_batch` and `nori.discard_staged_batch` retain all-or-nothing publication.

## History and judgment
- For retired identifiers only: `nori.historical_item(old_id)`, `nori.historical_find(query,limit)` redirect to the fixed GitHub backup and successor Subsection. Historic Items are not active research.
- Publish mathematics that deserves space in a research paper pursuing the grand conjecture. Establish correctness, explain its mathematical significance, and integrate it into a coherent argument.
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
    write(root / "API.md", api_text(schema))
    if schema == "nori":
        # Research guidance is specific to NORI; the shared universal guide still
        # documents atomic Items for other project schemas.
        write(root / "GUIDE.md", """# NORI manuscript research guide

**Publish mathematics that deserves space in a research paper pursuing the grand conjecture. Establish correctness, explain its mathematical significance, and integrate it into a coherent argument.**

## Research freely
Begin by developing your own view of what could resolve the full conjecture. Use the repository to test and improve that view. Give particular attention to assumptions and representations shared by existing approaches: their common obstacle may indicate that a different formulation is needed.

Before investing deeply in a subsidiary question, identify the mathematical implication that would make its solution useful. Make that implication explicit enough to examine. If the strongest plausible answer would leave the main argument in essentially the same position, reconsider the question.

Treat a succession of tractable extensions as a reason to step back. Look for the conceptual change that would make those extensions matter. Choose finite-dimensional computations to discriminate between general claims or reveal mechanisms.

When an approach already has substantial development, assess what additional insight your investigation could supply. Consider a substantially different route when the existing work repeatedly reaches the same obstacle.

Spend your effort on the strongest mathematical opportunity you can identify. Report an inconclusive outcome plainly when that is where the investigation ends.

## Manuscript structure and publication
Read the grand conjecture, OVERVIEW.md, KNOWN_OBSTRUCTIONS.md, and all eight Article compositions before choosing your approach; follow relevant Sections and Subsections for proofs. Historical effort is evidence about cost, not a ranking. Independently challenge inherited formulations and pursue original routes.

Articles, Sections, and Subsections form one assembled manuscript. **A Subsection is the smallest durable mathematical publication.** Revise a Subsection when a proof or correction belongs there. Create a new one only for coherent substantial development. Section and Article prose should connect arguments rather than repeat every proof. Check adjacent manuscripts before publishing; combine overlapping statements, preserve distinct meaningful proofs, and state exact dependencies and uncertainty.

Publish only substantial proofs, useful reductions, consequential counterexamples, meaningful corrections, or well-motivated promising mechanisms. A short decisive lemma qualifies; length, work expended, and another tractable special case do not themselves justify publication. An uncertain idea should be labeled accurately. A serious session may finish with **nothing worth publishing**; routine failed attempts do not need a permanent record.

The concise Known obstructions appendix preserves reusable false implications and their exact scopes. Revise the appendix when new mathematics changes a route's interpretation; never confuse a failure of a method with refutation of the conjecture.

Use the boot session_id for writes. Publish Subsections with `publish_subsection` and optimistic composition versions; use `compose` for Sections and Articles. Stage related writes and commit atomically when needed. Historical identifiers are recoverable from a fixed GitHub snapshot through explicit lookup only. No Items, tasks, leases, checkpoints, or compulsory progress reporting.
""")
        write(root / "REFLEXES.md", """# NORI research reflexes

Develop your own view of what might close the conjecture; inspect the repository to test it, not to inherit its direction. Examine the shared assumptions of developed approaches and consider a different representation when each reaches the same obstacle.

Before a subsidiary calculation, say what precise general implication its best answer could establish. Stop or switch if the strongest plausible answer leaves that implication untouched. Treat a string of easy extensions as an occasion for conceptual reconsideration.

Work deeply when a proof mechanism is promising. Compare an established route to substantially different ones on mathematical grounds. Inspect related Subsections and the Known obstructions appendix before publication.

Put correct, significant mathematics into the coherent manuscript. Preserve decisive counterexamples and honest hypotheses; consolidate redundant strengthening; keep failed routine investigations private. Inconclusive work with no paper-worthy outcome is entirely acceptable.
""")
        appendix = latest_composition(data, "subsection", "appendix_known_obstructions_to_proposed_nori_mechanisms")
        if appendix:
            write(root / "KNOWN_OBSTRUCTIONS.md", appendix.get("body") or "")

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
        "Subsections are organizational containers with optional publication-quality compositions. Their mathematical development lives exclusively in their Items and Results.",
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

Use the extracted artifact as the working research context. Read BROADCASTS.md **first**, before selecting any research tactic. Then read OVERVIEW.md, GUIDE.md, REFLEXES.md, DICTIONARY.md, API.md, and TOOLKIT/README.md. Then read grand_conjecture/README.md.

Call changes(...) once using this artifact's snapshot revision as the freshness baseline. If the snapshot is substantially stale, regenerate it before downloading.

For NORI, read KNOWN_OBSTRUCTIONS.md, each Article's composition and relevant Section/Subsection manuscripts. Article-level MANUSCRIPT.md files assemble the hierarchy. The Subsection is the smallest publication unit; judge mathematical significance independently. A session may end with no publication.\n\nThen begin research under GUIDE.md and REFLEXES.md.

Snapshot revision: {rev.get('revision')}
Generated: {rev.get('generated_at')}
"""
    write(root / "BOOT.md", boot)

    # The research manuscript is exported as the database's canonical folder tree.
    # Auxiliary material (guide, toolkit, brainstorms, etc.) remains at the schema root.
    for old in ("ARTICLES", "SECTIONS", "SUBSECTIONS"):
        shutil.rmtree(root / old, ignore_errors=True)
    tree = tree_paths(schema)
    for node in tree:
        relative = Path(node["path"])
        if relative.is_absolute() or ".." in relative.parts or relative.parts[0] != "grand_conjecture":
            raise ValueError(f"invalid canonical tree path: {relative}")
        write(root / relative, node.get("content") or "")
    index = ["# Grand conjecture", "",
             "Research hierarchy: Articles → Sections → Subsections." if schema == "nori" else "Research hierarchy: Articles → Sections → Subsections → Items.",
             "Each level's composition is adjacent to its corresponding directory.", ""]
    for a in articles:
        if schema == "nori":
            index.append(f"- [{a.get('title') or a['id']}]({safe_name(a['id'])}/MANUSCRIPT.md)")
        else:
            index.append(f"- [{a.get('title') or a['id']}]({safe_name(a['id'])}.md)")
    write(root / "grand_conjecture" / "README.md", "\n".join(index))
    if schema == "nori":
        # A readable assembled paper alongside the individually revisable
        # Article, Section and Subsection compositions. Preserve their exact text.
        sections_by_id = {x["id"]: x for x in section_items}
        for a in articles:
            combined = [f"# {a.get('title') or a['id']}", ""]
            main = latest_composition(data, "article", a["id"])
            if main:
                combined += ["## Article synopsis and main argument", "", main.get("body") or "", ""]
            members = sorted((x for x in data["article_sections"] if x.get("article_id") == a["id"]),
                             key=lambda x: (x.get("position") or 0, x.get("section_id") or ""))
            for member in members:
                sec = sections_by_id.get(member["section_id"])
                if not sec:
                    continue
                combined += [f"## {sec.get('title') or sec['id']}", ""]
                sc = latest_composition(data, "section", sec["id"])
                if sc:
                    combined += [sc.get("body") or "", ""]
                subs = sorted(subsections_by_section.get(sec["id"], []),
                              key=lambda x: (x.get("subsection_no") or 0, x.get("id") or ""))
                for sub in subs:
                    subc = latest_composition(data, "subsection", sub["id"])
                    if subc:
                        combined += [f"### {sub.get('title') or sub['id']}", "", subc.get("body") or "", ""]
            write(root / "grand_conjecture" / a["id"] / "MANUSCRIPT.md", "\n".join(combined))



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
        "item_count": len(data["items"]),
        "result_count": len(data["item_results"]),
        "brainstorm_count": len(data["brainstorms"]),
        "startup_broadcasts": broadcasts,
        "mirror_format": 19 if schema == "nori" else 18,
        "composition_model": "recursive-composition-v7",
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
