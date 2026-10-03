#!/usr/bin/env python3
from __future__ import annotations

import json, os, shutil, urllib.error, urllib.request
from pathlib import Path
from typing import Any

SUPABASE_URL = os.environ["SUPABASE_URL"].rstrip("/")
SUPABASE_KEY = os.environ["SUPABASE_SECRET_KEY"]
STAGE = Path(".mirror-stage")
SCHEMAS = ("gn3n", "linp")
# Guide text is mirrored verbatim from Supabase.
TABLES = ("documents","research","research_line_chunks","research_versions","dependencies","supersessions","brainstorms","dictionary")
PAGE = 500

def headers():
    h = {"apikey": SUPABASE_KEY, "Content-Type": "application/json", "Accept": "application/json",
         "User-Agent": "research-mirror-v7/1.0"}
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

def dictionary_text(items: list[dict[str, Any]]) -> str:
    by_section: dict[str, list[dict[str, Any]]] = {}
    for x in items:
        by_section.setdefault(x.get("section") or "General", []).append(x)
    out = []
    for section in sorted(by_section):
        out += [f"## {section}", ""]
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

def build(schema: str):
    root = STAGE / schema
    data = {t: rows(schema, t) for t in TABLES}
    rev = context(schema, "revision")
    help_doc = context(schema, "help")

    for table, value in data.items():
        write_json(root / "raw" / f"{table}.json", value)

    live_docs = [d for d in data["documents"] if d.get("archived_at") is None]
    overview = next((d for d in live_docs if d.get("kind") == "overview"), None)
    guide = next((d for d in live_docs if d.get("kind") == "guide"), None)
    main_lines = sorted(
        [d for d in live_docs if d.get("kind") == "main_line"],
        key=lambda d: (d.get("position") is None, d.get("position") or 0, d.get("id") or "")
    )

    write(root / "OVERVIEW.md", doc_md(overview) if overview else "# Overview\n\nNo overview.")
    write(root / "GUIDE.md", doc_md(guide) if guide else "# Guide\n\nNo guide.")
    write(root / "DICTIONARY.md", dictionary_text(data["dictionary"]))
    write_json(root / "API.json", help_doc)

    index = ["# Main Lines", ""]
    for d in main_lines:
        fn = safe_name(d["id"]) + ".md"
        index.append(f"- {fn} — {d.get('title') or d['id']}")
        write(root / "MAIN_LINES" / fn, doc_md(d))
    if not main_lines:
        index.append("No active Main Lines.")
    write(root / "MAIN_LINES" / "README.md", "\n".join(index))

    active_research = [r for r in data["research"] if r.get("archived_at") is None]
    chunks_by_line: dict[str, list[dict[str, Any]]] = {}
    for c in data["research_line_chunks"]:
        chunks_by_line.setdefault(c["line_id"], []).append(c)
    for r in active_research:
        folder = "RESEARCH_LINES" if r.get("kind") == "line" else "TOOLKIT"
        write(
            root / folder / (safe_name(r["id"]) + ".md"),
            research_md(r, chunks_by_line.get(r["id"], []))
        )
    if not any(r.get("kind") == "line" for r in active_research):
        write(root / "RESEARCH_LINES" / "README.md", "# Research Lines\n\nNo active Research Lines.")
    if not any(r.get("kind") == "toolkit" for r in active_research):
        write(root / "TOOLKIT" / "README.md", "# Toolkit\n\nNo active Toolkit entries.")

    for b in data["brainstorms"]:
        write(root / "BRAINSTORMS" / (safe_name(b["id"]) + ".md"),
              f"# {b.get('title') or b['id']}\n\n{b.get('seed') or ''}\n\n{b.get('body') or ''}")

    boot = f"""# Startup instructions

This is the current {schema} research snapshot.

Read, in this order:

1. OVERVIEW.md
2. GUIDE.md
3. DICTIONARY.md
4. API.json
5. MAIN_LINES/README.md and then every Main Line it lists

The Main Lines are deliberately last: they are the final attention-primer before route selection.

## Hard research rules

- Mathematical writing must be publication-precise: explicit hypotheses, quantified variables and parameters, exact exceptional cases, standard terminology, and checkable logical inferences.
- Mathematical manuscripts must contain no proof-process or research-process meta-language. Do not narrate workers, routes, frontier status, audits, databases, scheduler state, what remains to be proved, what would complete the proof, or what an approach is trying to do. State the mathematics directly.
- Computation is banned for mathematical research: no brute-force enumeration, computer search, numerical experiments, scripts, code, CAS, SAT/SMT solvers, or computational test beds.
- External web search is banned for mathematical research. Work from this project artifact, the narrowly permitted project-state reads described below, and mathematical reasoning.

After choosing a route, perform one narrow live freshness check before proof work:
- call changes(...) to obtain the compact live Main Line and Research Line version lists;
- compare the chosen Main Line version, if any, with main_line_versions in MANIFEST.json;
- compare the chosen Research Line version, if any, with research_line_versions in MANIFEST.json;
- if either chosen version differs, fetch only that manuscript with read([id]) and use the live manuscript;
- policy_events from changes(...) may be read normally.

Do not use changes(...) as a mathematical changelog. Mathematical updates live in the Main Line and Research Line manuscripts themselves.

After that route-specific freshness check, do not consult Supabase, GitHub, search/read/context, or any other shared research state while doing mathematical research. Work only from the startup snapshot, any refreshed chosen manuscripts, and your own local notes. Keep intermediate reasoning local.

Publish only after substantial progress. Publication is a separate synchronization phase:
- encode the complete save_batch operations array;
- upload it in numbered chunks with stage_batch_chunk(...);
- call review_staged_batch(...) and compare against concurrent findings since startup;
- resolve or remove overlaps;
- call commit_staged_batch(...) to commit the reviewed batch atomically.

If shared state changes after review, commit will refuse and require a fresh overlap review.

Research Lines are authored in crystallizing chunks. The line file reads as one assembled manuscript; its Authoring state footer identifies the single hot chunk and its version. Ordinary additions edit only that hot chunk with save_line_chunk(...). When the chunk becomes a coherent publication-style unit, freeze it with crystallize_line_chunk(...) and continue in the new hot chunk.

After a substantial publication, reread the Research Line you are continuing before resuming work. This is the normal mathematical refresh point. Re-read a Main Line only when its version changed or its global relationship has materially shifted.

Snapshot event: {rev.get('event_id')}
Generated: {rev.get('generated_at')}
"""
    write(root / "BOOT.md", boot)

    write_json(root / "MANIFEST.json", {
        "schema": schema,
        "snapshot_event_id": rev.get("event_id"),
        "generated_at": rev.get("generated_at"),
        "tables": list(TABLES),
        "main_line_count": len(main_lines),
        "main_line_versions": {d["id"]: d.get("version") for d in main_lines},
        "research_line_count": sum(r.get("kind") == "line" for r in active_research),
        "research_line_versions": {
            r["id"]: {"version": r.get("version"), "math_version": r.get("math_version")}
            for r in active_research if r.get("kind") == "line"
        },
        "toolkit_count": sum(r.get("kind") == "toolkit" for r in active_research),
        "brainstorm_count": len(data["brainstorms"]),
        "mirror_format": 7,
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
