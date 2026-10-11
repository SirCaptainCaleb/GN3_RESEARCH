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
- Publish correct consequential mathematics on the remaining NORI extremal and restricted-class questions. Establish correctness, explain its mathematical significance, and integrate it into a coherent argument.
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

    write(root / "OVERVIEW.md", doc_md(overview) if overview else "# Overview\n\nNo overview.")
    write(root / "GUIDE.md", doc_md(guide) if guide else "# Guide\n\nNo guide.")
    write(root / "REFLEXES.md", doc_md(reflexes) if reflexes else "# Research Reflexes\n\nNo reflexes.")
    write(root / "DICTIONARY.md", dictionary_text(data["dictionary"]))
    write(root / "API.md", api_text(schema))
    if schema == "nori":
        # Research guidance is specific to NORI; the shared universal guide still
        # documents atomic Items for other project schemas.
        write(root / "GUIDE.md", """# NORI manuscript research guide

**Publish mathematics that resolves consequential questions after the unrestricted NORI3 conjecture's refutation. Establish correctness, precise scope, and its effect on an open problem.**

## Research freely
Begin with TWO PRIMARY mathematical problems: unrestricted NORI1 for EVERY legal physical-edge coloring, and the long vertex-simple tight-path problem for EVERY ordinary boundary 3-tournament, without assuming any global edge order or acyclicity. Seek a common structure or theorem advancing both. Edge-ordered tournaments are a FALLBACK or a source of techniques, not a replacement for the general boundary-tournament problem. Seek a genuine common theorem or transfer, not just two cases packaged in one definition. Study boundary-compatible reversal symmetry and global edge-order realizability only when they materially advance this NORI1-preserving goal. Unrestricted NORI2 and unrestricted NORI3 logarithmic extremal refinements are no longer research targets. Use the repository to test and improve your view. Give particular attention to assumptions and representations shared by existing approaches: their common obstacle may indicate that a different formulation is needed.

Before investing deeply in a subsidiary question, identify the mathematical implication that would make its solution useful. Make that implication explicit enough to examine. If the strongest plausible answer would leave the main argument in essentially the same position, reconsider the question.

Treat a succession of tractable extensions as a reason to step back. Look for the conceptual change that would make those extensions matter. Choose finite-dimensional computations to discriminate between general claims or reveal mechanisms.

When an approach already has substantial development, assess what additional insight your investigation could supply. Consider a substantially different route when the existing work repeatedly reaches the same obstacle.

Spend your effort on the strongest mathematical opportunity you can identify. Report an inconclusive outcome plainly when that is where the investigation ends.

## Strengthening criterion
A proposed framework has TWO preservation tests. (1) Retain the ENTIRE original NORI1 class, including arbitrary nonlinear antipodally odd physical-edge colorings; never replace it by an affine or special subclass. (2) Retain the ENTIRE direction-only boundary 3-tournament class whenever feasible: for each triple of distinct directions a,b,c, a rule b(a,b,c) obeying b(c,b,a)=1-b(a,b,c) must be admitted by c(F,(a,b,c))=b(a,b,c) on every physical face. As an absolute minimum, no proposal may discard edge-ordered-graph boundary tournaments arising from ANY global strict edge order prec on K_n via b(a,b,c)=1_{ {a,b} prec {b,c} }. This subclass is precisely the acyclic-comparison-orientation edge-order-realizable class, and its increasing vertex-simple paths are the motivating tight paths. A proposal preserving only that minimum instead of all boundary tournaments must identify explicitly what additional hypothesis excludes the rest and why it is indispensable. Do not silently narrow either family. Same-face reversal-oddness and antipodal invariance form a plausible 3-face subclass, but reversal of a one-element order is the identity, so same-face reversal-oddness cannot literally be required for NORI1. Explain explicitly how any uniform definition handles that degeneracy. Before proposing a subsidiary theorem, test its hypotheses explicitly against BOTH mandatory families, and identify its actual implication for arbitrary NORI1 edge colorings and edge-ordered increasing tight paths; strive for the entire boundary tournament class. An improvement restricted solely to a peripheral subclass is not progress toward the requested strengthening. Excluding the logarithmic (3,3)-tournament construction is necessary but not sufficient. Mere piecewise definitions, new constants, and unrelated restricted classes are not consequential.

## Selective research notes — separate from manuscript publication
Save a note only when another researcher could make a materially better decision. Use the narrowest primary home (Project, Article, Section or Subsection), and link additional relevant manuscripts or notes. Record the precise claim, scope, evidence, why it matters, and a discriminating next step where applicable. Before starting or revisiting an approach, inspect the Known obstructions appendix and only the relevant notes. Extend existing notes on the same question rather than fragmenting them.

**Default destination for negative results is a research note, EVEN IF rigorous, lengthy, technically sophisticated, or currently developed as a complete Section or Subsection.** This includes counterexamples to a proposed implication, methods that provably cannot close a gap, bounded exhaustive exclusions, and failed generalizations whose principal value is redirecting future research. Proof size and amount of effort do not by themselves confer publication status. Make a genuine exception for a negative theorem or counterexample that decisively resolves a central conjecture, establishes an independently important mathematical result, or makes another substantial standalone contribution (for example, the legal Q9 refutation and its all-dimensional consequences). Evaluate mathematical significance, NOT the positive/negative label alone.

For mixed material, preserve the independently significant positive theorem or reduction in a coherent Subsection and put the method-specific obstruction, exact failure certificate or unsuccessful extension in a linked research note. An entire Section dominated by negative method audits may properly be consolidated into notes; preserve every reusable rigorous proof and provenance while revising the containing Article/Section compositions rather than silently discarding mathematics. The Known Obstructions appendix remains a curated high-level synthesis, with detailed evidence linked from notes, not a dumping ground for all negative experiments. Distinguish proved false implications, exhaustive exclusions within explicit bounds, limitations of a specific method and attempts that merely failed. Keep epistemic status separate from lifecycle; resolve or supersede notes with an explanation and successor link. Notes are never automatically composed into manuscripts; neither publication nor a note is mandatory. Notes, recency and convenient next steps do not rank the research agenda.

## Manuscript structure and publication
Read the original (now refuted) grand conjecture, the latest counterexamples, OVERVIEW.md, KNOWN_OBSTRUCTIONS.md, and all eight Article compositions before choosing your approach; follow relevant Sections and Subsections for proofs. Historical effort is evidence about cost, not a ranking. Independently challenge inherited formulations and pursue original routes.

Articles, Sections, and Subsections form one assembled manuscript. **A Subsection is the smallest durable mathematical publication.** Revise a Subsection when a proof or correction belongs there. Create a new one only for coherent substantial development. Section and Article prose should connect arguments rather than repeat every proof. Check adjacent manuscripts before publishing; combine overlapping statements, preserve distinct meaningful proofs, and state exact dependencies and uncertainty.

Publish coherent, correct, independently consequential theorems, reductions, decisive counterexamples to central conjectures, and necessary corrections. A short decisive lemma may qualify; length, proof sophistication, effort spent, and the existence of a complete counterexample to a subsidiary METHOD are insufficient for manuscript admission. Negative results ordinarily go to selective notes even when extensive. A negative result may remain a manuscript only if its actual mathematical consequence is independently publication-worthy. An inconclusive session may leave neither manuscript nor note; routine failed attempts have no preservation requirement.

The Known obstructions appendix preserves counterexamples and reusable false implications with their exact scopes. The unrestricted original NORI3 one-switch conjecture and all fixed k>=3 switch hierarchies are disproved. Do not treat these as open questions or revive the obsolete universal square-root monochromatic-path target. Distinguish them from the open unrestricted NORI1 full-monochromatic-geodesic problem and NORI1-preserving strengthened variants of the higher-face problems. Do not initiate old unrestricted NORI2 investigations. Preserve established logarithmic NORI3 counterexamples as obstructions against overly weak proposed generalizations.

Use the boot session_id for writes. Publish Subsections with `publish_subsection` and optimistic composition versions; use `compose` for Sections and Articles. Stage related writes and commit atomically when needed. Historical identifiers are recoverable from a fixed GitHub snapshot through explicit lookup only. No Items, tasks, leases, checkpoints, or compulsory progress reporting.
""")
        write(root / "REFLEXES.md", """# NORI research reflexes

Develop your own view of a consequential remaining theorem or obstruction, not a proof of the refuted unrestricted grand conjecture. Inspect the repository to test it, not to inherit its direction. Examine the shared assumptions of developed approaches and consider a different representation when each reaches the same obstacle.

Before a subsidiary calculation, say what precise general implication its best answer could establish. Stop or switch if the strongest plausible answer leaves that implication untouched. Treat a string of easy extensions as an occasion for conceptual reconsideration.

Work deeply when a proof mechanism is promising. Compare an established route to substantially different ones on mathematical grounds. Inspect related Subsections and the Known obstructions appendix before publication.

Put independently consequential mathematics into coherent manuscripts; decisive counterexamples to central conjectures may belong there. **A negative result's default home is a research note, even if long, rigorous or Section-sized**, when it chiefly limits a proposed implication or method. Preserve its precise proof and certificate in the note instead of promoting a methodological dead end into the publication manuscript. For mixed work publish the independently meaningful theorem and link the detailed obstruction note. Assess entire existing Sections and Subsections with the same criterion; keep historical provenance and don't erase mathematics merely to shorten the paper. Distinguish proved, bounded computational, method-specific and inconclusive negative information. Update existing notes rather than duplicating them. No quotas, required notes, progress reports or ranked agenda. Inconclusive work without a manuscript or note is acceptable.
""")
        appendix = latest_composition(data, "subsection", "appendix_known_obstructions_to_proposed_nori_mechanisms")
        if appendix:
            write(root / "KNOWN_OBSTRUCTIONS.md", appendix.get("body") or "")
        write(root / "WORKER_PROMPT.md", """# NORI research worker

You are an independent mathematician studying surviving NORI problems after the unrestricted grand conjecture was disproved.
Use Supabase RESEARCH (`fewmvjslkhoygixiimgn`), schema `nori`.
In a new conversation begin with `select * from nori.boot();` and preserve
its session_id. In this continuing conversation reuse the existing session_id;
refresh with `nori.status()` and `nori.changes(...)`.

Read BOOT.md, OVERVIEW.md, GUIDE.md, REFLEXES.md, KNOWN_OBSTRUCTIONS.md,
API.md and all eight Article compositions; investigate relevant Sections and
Subsections, especially the legal Q9 counterexample, multilevel switch amplification,
and self-dual Devine-Milans logarithmic-path construction.
The NORI3 one-switch conjecture and fixed k>=3 switch hierarchy are false.
Every fixed k>=3 admits unbounded compulsory switches, and S3(n)=Omega(n/log n).
The original universal square-root monochromatic-path target is also false.

The TWO EQUALLY PRIMARY targets are: (1) solve unrestricted NORI1 for
all legal antipodally odd physical edge colorings; (2) solve the long
vertex-simple monochromatic tight-path problem for ALL ordinary boundary
3-tournaments b satisfying b(c,b,a)=1-b(a,b,c). Do not assume a global
edge order or acyclic line-graph comparison orientation for target (2).
A strengthened NORI theory must preserve BOTH full classes.
The boundary 3-tournaments induced by global orders on edges of K_n are
a USEFUL FALLBACK if the general boundary case hits a proved obstacle,
NOT a substitute for its solution. A theorem restricted to edge-ordered
cases must identify the remaining gap and seek a general transfer.
Do not work on old unrestricted NORI2, or further refine the unrestricted
NORI3 logarithmic obstruction for its own sake.

Investigate independently a consequential route toward such a unification.
A candidate three-face symmetry is separate same-face reversal oddness
c(F,rev(pi))=1-c(F,pi) and antipodal invariance c(bar F,pi)=c(F,pi).
It excludes the existing logarithmic NORI3 examples and contains ALL
boundary 3-tournaments, including edge-ordered comparison tournaments.
But it cannot be imposed verbatim for k=1, where reversal is the identity.
A serious framework must explain how ALL legal NORI1 instances and the
edge-ordered boundary instances survive, without simply juxtaposing
unrelated cases. Check proposed definitions against BOTH families.

Prioritize a proven common long/spanning-path theorem, a meaningful lift
or transfer preserving real physical faces and original-direction
simplicity, or a rigorous obstruction to a proposed unified structure.
Never confuse line-graph directed paths with vertex-simple increasing
paths of the underlying edge-ordered K_n.
Edge-order acyclicity and boundary comparisons are useful only insofar
as they illuminate this common NORI1-preserving problem.

Challenge shared assumptions and representations. Before substantial work,
identify the exact implication its strongest possible result would establish.
Avoid routine construction improvements, unrestricted NORI2, and
small-dimensional searches without a consequential NORI1-preserving implication. Explore new formulations independently.

Publish only correct, independently significant, coherent mathematics using
`nori.publish_subsection` or the Section/Article composition interface.
Subsections are the smallest publication unit. **Negative results ordinarily
belong in research notes, however rigorous or extensive, even when a whole
Section currently consists of methodological obstructions.** Manuscript
exceptions include decisive refutations of important conjectures (e.g.
physical Q9 NORI3) and independently important negative theorems. For mixed
work, publish a real standalone theorem and link the detailed negative note;
do not lose certificates, hypotheses, or provenance when reorganizing.
Review related work before either kind of preservation. There are no Items, claims,
leases, checkpoints, assigned rankings or publication quotas.

Persist manuscript advances selectively. Check RESEARCH_NOTES/QUESTIONS.md and related notes before revisiting a route. **Use nori.save_note as the default for consequential negative results, even proved and Section-sized ones**, not merely unfinished work. Attach narrowly and revise existing notes on the same question. Distinguish proved counterexamples, bounded exclusions, method limits and unsuccessful attempts. Promote material only when it makes a standalone significant mathematical contribution, including truly decisive conjecture refutations. A session may end with no manuscript and no note.
""")

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
            "Discovery map, NOT a ranked task list. Consult manuscripts and KNOWN_OBSTRUCTIONS.md for proved mathematics. Read only relevant notes.", "",
            "## Open questions and mechanisms", "",
            *(by_question["active"][:12] or ["- None recorded."]),
            *(["- Additional open notes: see README.md or search_notes; the displayed selection is alphabetical, not a ranking."] if len(by_question["active"])>12 else []),
            "", "## Established and method-scoped obstructions", "",
            *(by_question["obstructions"][:12] or ["- See KNOWN_OBSTRUCTIONS.md."]),
            *(["- Further obstructions: see README.md or search_notes."] if len(by_question["obstructions"])>12 else []),
            "", "## Resolved and superseded", "",
            *(by_question["closed"][:6] or ["- None recorded."]),
            *(["- More resolved/superseded notes: see README.md or search_notes."] if len(by_question["closed"])>6 else [])
        ]
        write(root / "RESEARCH_NOTES" / "QUESTIONS.md", "\n".join(question_map))

    for b in data["brainstorms"]:
        write(
            root / "BRAINSTORMS" / (safe_name(b["id"]) + ".md"),
            f"# {b.get('title') or b['id']}\n\n{b.get('seed') or ''}\n\n{b.get('body') or ''}"
        )

    boot = f"""# Startup instructions

Review startup_notices returned by boot().

Use the extracted artifact as the working research context. Read BROADCASTS.md **first**, before selecting any research tactic. Then read OVERVIEW.md, GUIDE.md, REFLEXES.md, DICTIONARY.md, API.md, and TOOLKIT/README.md. Then read grand_conjecture/README.md.

Call changes(...) once using this artifact's snapshot revision as the freshness baseline. If the snapshot is substantially stale, regenerate it before downloading.

For NORI, read KNOWN_OBSTRUCTIONS.md and RESEARCH_NOTES/QUESTIONS.md, each Article's composition and relevant Section/Subsection manuscripts. Follow ONLY relevant notes, not all of them at startup. **Negative mathematical results normally belong to research notes even if rigorous and Section-sized; decisive conjecture refutations and independently important negative theorems are manuscript exceptions.** Keep proofs and provenance when reclassifying mixed manuscripts. Notes never rank the agenda. Article-level MANUSCRIPT.md files assemble the hierarchy. The Subsection is the smallest publication unit; a session may end with no manuscript and no note.\n\nThen begin research under GUIDE.md and REFLEXES.md.

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
        # Render a coherent paper without duplicating complete parent-level
        # proofs at each hierarchy level. Full parent compositions remain
        # accessible beside the assembled manuscript.
        def contextual_preamble(body: str) -> str:
            paragraphs = []
            for para in (body or "").strip().split("\n\n"):
                p = para.strip()
                if not p or p.startswith("#"):
                    continue
                if p.startswith(("**Theorem", "**Lemma", "Theorem ", "Lemma ", "Proof.", "Proof:")):
                    break
                if len(p) > 1750:
                    break
                paragraphs.append(p)
                if len(paragraphs) >= 2 or sum(len(x) for x in paragraphs) >= 1400:
                    break
            return "\n\n".join(paragraphs)

        sections_by_id = {x["id"]: x for x in section_items}
        for a in articles:
            combined = [f"# {a.get('title') or a['id']}", ""]
            main = latest_composition(data, "article", a["id"])
            if main:
                combined += ["## Article setting and orientation", "",
                             contextual_preamble(main.get("body") or ""), "",
                             f"*Full Article composition: [source manuscript](../{a['id']}.md).*", ""]
            members = sorted((x for x in data["article_sections"] if x.get("article_id") == a["id"]),
                             key=lambda x: (x.get("position") or 0, x.get("section_id") or ""))
            for member in members:
                sec = sections_by_id.get(member["section_id"])
                if not sec:
                    continue
                combined += [f"## {sec.get('title') or sec['id']}", ""]
                sc = latest_composition(data, "section", sec["id"])
                if sc:
                    combined += [contextual_preamble(sc.get("body") or ""), "",
                                 f"*Full Section composition: [source manuscript]({sec['id']}.md).*", ""]
                subs = sorted(subsections_by_section.get(sec["id"], []),
                              key=lambda x: (x.get("subsection_no") or 0, x.get("id") or ""))
                for sub in subs:
                    subc = latest_composition(data, "subsection", sub["id"])
                    if subc:
                        combined += [f"### {sub.get('title') or sub['id']}", "", subc.get("body") or "", ""]
            write(root / "grand_conjecture" / a["id"] / "MANUSCRIPT.md", "\n".join(combined))



    write_json(root / "MANIFEST.json", {
        "schema": schema,
        "research_note_count": len(data.get("research_notes", [])),
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
