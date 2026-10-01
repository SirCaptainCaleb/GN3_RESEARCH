#!/usr/bin/env python3
from __future__ import annotations

import hashlib, json, os, shutil, urllib.request, urllib.error
from pathlib import Path
from typing import Any

SUPABASE_URL = os.environ["SUPABASE_URL"].rstrip("/")
SUPABASE_KEY = os.environ["SUPABASE_SECRET_KEY"]
STAGE = Path(".mirror-stage")
PAGE = 500

SCHEMAS = {"gn3n": "gn3n", "linp": "linp", "template": "__template__"}
TABLES = [
    "objects","edges","reasoning_nodes","certificates","object_authors",
    "standardization_dictionary","standardization_dictionary_sections","state",
    "architecture_migration_notes","atlas_legacy_snapshots",
]
CORE_POLICIES = [
    "startup_kernel","worker_kernel","project_policy",
    "research_full_guidance","architecture_invariants",
]
MODE_POLICIES = [
    "mode_audit","mode_brainstorm","mode_coordination","mode_isolated_research",
    "mode_literature_bridge","mode_methodology_review","mode_proof_rehearsal",
    "mode_reasoning_hygiene","mode_research",
]

def headers():
    h = {
        "apikey": SUPABASE_KEY,
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "research-mirror/1.0",
    }
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
        detail = e.read().decode(errors="replace")
        raise RuntimeError(f"{name} failed: HTTP {e.code}: {detail}") from e

def mirror_rows(schema: str, table: str) -> list[dict[str, Any]]:
    out = []
    offset = 0
    while True:
        page = rpc("research_mirror_rows", {
            "p_schema": schema, "p_table": table,
            "p_offset": offset, "p_limit": PAGE,
        })
        rows = page["rows"]
        out.extend(rows)
        if page["complete"]:
            return out
        offset += len(rows)

def context(schema: str, kind: str, arg: str | None = None) -> Any:
    return rpc("research_mirror_context", {
        "p_schema": schema, "p_kind": kind, "p_arg": arg,
    })

def scalar(v: Any) -> str:
    if v is None: return "null"
    if v is True: return "true"
    if v is False: return "false"
    if isinstance(v, (int, float)): return str(v)
    return json.dumps(str(v), ensure_ascii=False)

def yaml_lines(value: Any, indent: int = 0) -> list[str]:
    pad = " " * indent
    if isinstance(value, dict):
        lines = []
        for k in sorted(value):
            v = value[k]
            if isinstance(v, (dict, list)):
                lines.append(f"{pad}{k}:")
                lines.extend(yaml_lines(v, indent + 2))
            else:
                lines.append(f"{pad}{k}: {scalar(v)}")
        return lines
    if isinstance(value, list):
        lines = []
        for v in value:
            if isinstance(v, (dict, list)):
                lines.append(f"{pad}-")
                lines.extend(yaml_lines(v, indent + 2))
            else:
                lines.append(f"{pad}- {scalar(v)}")
        return lines
    return [f"{pad}{scalar(value)}"]

def write_yaml(path: Path, value: Any):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(yaml_lines(value)) + "\n", encoding="utf-8")

def write_json(path: Path, value: Any):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def write_text(path: Path, text: str):
    """Write generated prose with exactly one terminal newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip("\n") + "\n", encoding="utf-8")

def write_exact_text(path: Path, text: str):
    """Write source-controlled text byte-for-byte as UTF-8; no normalization."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(text.encode("utf-8"))

def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def body_of(v: Any) -> str:
    return str(v.get("body") or "") if isinstance(v, dict) else str(v or "")

CONTENT_STATEMENT_MARKER = "## Statement"
CONTENT_BODY_MARKER = "## Body"

def content_md(o: dict[str, Any]) -> str:
    """Compose content.md while preserving statement/body text exactly."""
    title = o.get("title") or ""
    statement = o.get("statement")
    body = o.get("body")
    if statement is None:
        statement = ""
    if body is None:
        body = ""
    heading = f"# {title}" if title else f"# {o['id']}"
    return (
        heading + "\n\n"
        + CONTENT_STATEMENT_MARKER + "\n\n"
        + statement + "\n\n"
        + CONTENT_BODY_MARKER + "\n\n"
        + body
    )

def verify_content_md(rendered: str, o: dict[str, Any]) -> None:
    """Prove that the exact Supabase statement/body survived composition."""
    title = o.get("title") or ""
    heading = f"# {title}" if title else f"# {o['id']}"
    prefix = heading + "\n\n" + CONTENT_STATEMENT_MARKER + "\n\n"
    if not rendered.startswith(prefix):
        raise RuntimeError(f"content prefix mismatch for {o['id']}")
    rest = rendered[len(prefix):]
    separator = "\n\n" + CONTENT_BODY_MARKER + "\n\n"
    statement = o.get("statement") or ""
    body = o.get("body") or ""
    expected = statement + separator + body
    if rest != expected:
        raise RuntimeError(f"lossy content serialization detected for {o['id']}")

def metadata(o: dict[str, Any]) -> dict[str, Any]:
    omit = {"statement", "body", "tree_path", "trashed_at"}
    m = {k: v for k, v in o.items() if k not in omit}
    # Integrity hashes refer to the exact UTF-8 source strings in Supabase.
    m["statement_sha256"] = sha256_text(o.get("statement") or "")
    m["body_sha256"] = sha256_text(o.get("body") or "")
    return m

def render_forest(objects: list[dict[str, Any]], mode: str) -> str:
    active = [o for o in objects if o.get("trashed_at") is None]
    active.sort(key=lambda o: (o.get("tree_path") or "", str(o.get("id"))))
    lines = []
    for o in active:
        depth = max(0, len([p for p in (o.get("tree_path") or "").strip("/").split("/") if p]) - 1)
        pre = "  " * depth
        if mode == "simplified":
            val = (o.get("simplified_statement") or "").strip() or f"‹{o.get('title','')}›"
            lines.append(f"{pre}• [{o['id']}] {val}")
        else:
            lines.append(f"{pre}• [{o['id']}] {o.get('title','')}")
            sub = pre + "    "
            lines.append(f"{sub}STATEMENT")
            st = (o.get("statement") or "").strip() or "‹none›"
            lines.extend(f"{sub}{x}" for x in st.splitlines())
            if mode == "full":
                lines.append(f"{sub}BODY / PROOF")
                bd = (o.get("body") or "").strip() or "‹none›"
                lines.extend(f"{sub}{x}" for x in bd.splitlines())
            lines.append("")
    return "\n".join(lines)

def atlas_text(atlas: dict[str, Any]) -> str:
    entries = atlas.get("entries") or []
    by_id = {e.get("id"): e for e in entries}
    memo = {}
    def depth(e):
        eid = e.get("id")
        if eid in memo: return memo[eid]
        p = e.get("parent_container_id")
        memo[eid] = 0 if not p or p not in by_id else depth(by_id[p]) + 1
        return memo[eid]
    lines = []
    for e in entries:
        mark = []
        if e.get("pending_count"): mark.append(f"pending={e['pending_count']}")
        if e.get("obstructed_count"): mark.append(f"obstructed={e['obstructed_count']}")
        suffix = f" [{' '.join(mark)}]" if mark else ""
        lines.append(f"{'  '*depth(e)}• [{e.get('id')}] {(e.get('summary') or e.get('title') or '').strip()}{suffix}")
    return "\n".join(lines)

def startup_atlas_text(sa: dict[str, Any]) -> str:
    lines, seen = [], set()
    for e in (sa.get("core_map") or []) + (sa.get("deep_landmarks") or []):
        if e.get("id") in seen: continue
        seen.add(e.get("id"))
        d = int(e.get("depth") or 0)
        mark = []
        if e.get("pending"): mark.append("pending")
        if e.get("obstructed"): mark.append("obstructed")
        suffix = f" [{' '.join(mark)}]" if mark else ""
        lines.append(f"{'  '*d}• [{e.get('id')}] {(e.get('summary') or e.get('title') or '').strip()}{suffix}")
    return "\n".join(lines)

def build_schema(folder: str, schema: str):
    root = STAGE / folder
    rows = {t: mirror_rows(schema, t) for t in TABLES}
    objects = rows["objects"]
    active = {o["id"]: o for o in objects if o.get("trashed_at") is None}

    children: dict[str | None, list[str]] = {}
    for o in active.values():
        children.setdefault(o.get("parent_id"), []).append(o["id"])
    for ids in children.values():
        ids.sort(key=lambda oid: ((active[oid].get("position") is None), active[oid].get("position") or 0, oid))

    def emit(oid: str, parent_dir: Path):
        o = active[oid]
        d = parent_dir / str(oid)
        write_yaml(d / "metadata.yaml", metadata(o))
        rendered = content_md(o)
        verify_content_md(rendered, o)
        write_exact_text(d / "content.md", rendered)
        if (d / "content.md").read_bytes() != rendered.encode("utf-8"):
            raise RuntimeError(f"content.md byte verification failed for {o['id']}")
        cdir = d / "children"
        cdir.mkdir(parents=True, exist_ok=True)
        kids = children.get(oid, [])
        if not kids:
            write_text(cdir / ".gitkeep", "")
        for kid in kids:
            emit(kid, cdir)

    forest = root / "forest"
    forest.mkdir(parents=True, exist_ok=True)
    roots = children.get(None, [])
    for oid in roots:
        emit(oid, forest)
    if not roots:
        write_text(forest / ".gitkeep", "")

    for table in ["edges", "reasoning_nodes", "certificates", "object_authors"]:
        write_yaml(root / "relations" / f"{table}.yaml", rows[table])
    write_yaml(root / "vocabulary" / "standardization_dictionary.yaml", rows["standardization_dictionary"])
    write_yaml(root / "vocabulary" / "standardization_dictionary_sections.yaml", rows["standardization_dictionary_sections"])

    # Machine-readable integrity copies use JSON's fully specified escaping.
    # JSON is also valid YAML 1.2, and these hashes make silent text loss detectable.
    write_json(root / "vocabulary" / "standardization_dictionary.json", rows["standardization_dictionary"])
    write_json(root / "vocabulary" / "standardization_dictionary_sections.json", rows["standardization_dictionary_sections"])
    write_yaml(root / "state" / "project.yaml", rows["state"])
    write_yaml(root / "state" / "architecture_migration_notes.yaml", rows["architecture_migration_notes"])
    write_yaml(root / "state" / "atlas_legacy_snapshots.yaml", rows["atlas_legacy_snapshots"])

    ctx = root / "_context"
    atlas = context(schema, "atlas")
    satlas = context(schema, "startup_atlas")
    hindex = context(schema, "help")
    topics = hindex.get("topics") or []

    write_json(ctx / "atlas.json", atlas)
    write_text(ctx / "atlas.md", atlas_text(atlas))
    write_json(ctx / "startup_atlas.json", satlas)
    write_text(ctx / "startup_atlas.md", startup_atlas_text(satlas))

    write_json(ctx / "help" / "_index.json", hindex)
    help_docs = {}
    for topic in topics:
        doc = context(schema, "help", topic)
        help_docs[topic] = doc
        write_text(ctx / "help" / f"{topic}.md", body_of(doc))

    policies = {}
    for key in CORE_POLICIES + MODE_POLICIES:
        try:
            policies[key] = context(schema, "policy", key)
        except Exception:
            policies[key] = {}
    for key in CORE_POLICIES:
        write_text(ctx / "policies" / f"{key}.md", body_of(policies[key]))
    for key in MODE_POLICIES:
        write_text(ctx / "roles" / f"{key.removeprefix('mode_')}.md", body_of(policies[key]))

    write_json(ctx / "rpc_signatures.json", context(schema, "rpc_signatures"))
    write_json(ctx / "rpc_list.json", context(schema, "rpc_list"))
    write_text(ctx / "simplified_forest.md", render_forest(objects, "simplified"))
    write_text(ctx / "statement_forest.md", render_forest(objects, "statement"))
    write_text(ctx / "statement_plus_proof_forest.md", render_forest(objects, "full"))

    state = rows["state"][0] if rows["state"] else {}
    gt = active.get(str(state.get("grand_theorem_id")), {})
    bootstrap = f"""# {folder} startup bootstrap

Repository revision: {state.get('revision')}
Supabase schema: {schema}

This mirror does not allocate a worker ID. A live worker still begins with:

    select * from {schema}.startup();

Retain the returned worker ID, then follow the live continuation protocol.

## Grand theorem

[{gt.get('id', state.get('grand_theorem_id'))}] {gt.get('title','')}

{gt.get('statement','')}

## Startup help

{body_of(help_docs.get('startup', {}))}

## Startup kernel

{body_of(policies.get('startup_kernel'))}
"""
    write_text(ctx / "startup_bootstrap.md", bootstrap)

    write_json(root / "mirror_manifest.json", {
        "folder": folder,
        "supabase_schema": schema,
        "repository_revision": state.get("revision"),
        "live_object_count": len(active),
        "root_count": len(roots),
        "mirror_format": 1,
    })

def main():
    if STAGE.exists():
        shutil.rmtree(STAGE)
    STAGE.mkdir()
    for folder, schema in SCHEMAS.items():
        print(f"Building {folder} from {schema}...")
        build_schema(folder, schema)
    print("Mirror staging complete.")

if __name__ == "__main__":
    main()
