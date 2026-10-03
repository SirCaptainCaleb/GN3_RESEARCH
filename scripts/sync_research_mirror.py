# Artifact refresh trigger: validates cleanup and artifact metadata publishing.
# Artifact startup is consumed through the GitHub Actions artifact download path.
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
# Exact manuscript reads are paged server-side at 9000 characters.
# Search results use packed 9k pages; offset counts complete pages.
# Search responses are one 9000-character ranked page by default.
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
    reflexes = next((d for d in live_docs if d.get("kind") == "reflexes"), None)
    main_lines = sorted(
        [d for d in live_docs if d.get("kind") == "main_line"],
        key=lambda d: (d.get("position") is None, d.get("position") or 0, d.get("id") or "")
    )

    write(root / "OVERVIEW.md", doc_md(overview) if overview else "# Overview\n\nNo overview.")
    write(root / "GUIDE.md", doc_md(guide) if guide else "# Guide\n\nNo guide.")
    write(root / "REFLEXES.md", doc_md(reflexes) if reflexes else "# Research Reflexes\n\nNo reflexes.")
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
    toolkit_items = sorted(
        [r for r in active_research if r.get("kind") == "toolkit"],
        key=lambda r: ((r.get("toolkit_type") or ""), (r.get("title") or "").casefold(), r.get("id") or "")
    )
    toolkit_index = ["# Toolkit", ""]
    if toolkit_items:
        for r in toolkit_items:
            fn = safe_name(r["id"]) + ".md"
            typ = r.get("toolkit_type") or "other"
            summary = (r.get("simplified_statement") or "").strip()
            line = f"- [{r.get('title') or r['id']}]({fn}) — {typ}"
            if summary:
                line += f" — {summary}"
            toolkit_index.append(line)
    else:
        toolkit_index.append("No active Toolkit entries.")
    write(root / "TOOLKIT" / "README.md", "\n".join(toolkit_index))

    for b in data["brainstorms"]:
        write(root / "BRAINSTORMS" / (safe_name(b["id"]) + ".md"),
              f"# {b.get('title') or b['id']}\n\n{b.get('seed') or ''}\n\n{b.get('body') or ''}")

    boot = f"""# Startup instructions

This is the current {schema} research snapshot. Review startup_notices returned by boot(). Read OVERVIEW.md, GUIDE.md, REFLEXES.md, DICTIONARY.md, API.json, and TOOLKIT/README.md, then read MAIN_LINES/README.md and every listed Main Line last, immediately before choosing a route.

Mathematical work must be publication-precise and contain no proof-process or research-process meta-language. Computation, computer search, brute force, numerical experimentation, code, CAS/SAT/SMT tools, and external web search are banned.

After choosing a route, strongly consider one route-specific search across existing Research Lines and Toolkit entries with include_documents=false to avoid rediscovering known mathematics. This is a research reflex, not a gate: proof work must never be blocked because the search was skipped. Then call changes(...) once. Compare only the chosen Main Line and Research Line versions, if any, with MANIFEST.json. If a chosen manuscript changed, page through it with read([id]); pass next_cursor back into read(...) until complete=true. changes(...) is a freshness signal, not a mathematical changelog.

If the snapshot is stale enough that refreshing the relevant context piecemeal would require substantial rereading, do not reconstruct a large new snapshot through many delta reads. Refresh the artifact instead. In GitHub Actions for SirCaptainCaleb/GN3_RESEARCH, find the most recent "Sync research mirror" run, fetch its jobs, and rerun its "sync" job with the workflow-job rerun capability. When that rerun succeeds it automatically triggers "Build research context artifact", which publishes the new artifact metadata back to Supabase. Then call boot() again and download the newly identified startup artifact. If no usable Sync run exists, call artifact_help() for the deeper recovery path.

Then work from the refreshed startup context and local reasoning without consulting shared research state.

Follow the recurring research behavior in REFLEXES.md throughout the session.

Publish only after substantial progress. Every substantive durable research operation must explicitly declare dependencies, using [] when genuinely self-contained. Stage the complete save_batch payload in connector-sized parts, review concurrent findings with review_staged_batch(...), resolve overlap, and commit atomically with commit_staged_batch(...). If another worker publishes after review, review again. Use repair_line_chunk(...) only for a version-guarded correction to an older crystallized subsection. After publication, reread the Research Line you are continuing before resuming research.

Snapshot revision: {rev.get('revision')}
Generated: {rev.get('generated_at')}
"""
    write(root / "BOOT.md", boot)

    write_json(root / "MANIFEST.json", {
        "schema": schema,
        "snapshot_revision": rev.get("revision"),
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
