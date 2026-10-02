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
    "standardization_dictionary","state",
    "architecture_migration_notes",
]
CORE_POLICIES = [
    "worker_kernel",
    "project_policy",
    "research_full_guidance",
    "architecture_invariants",
    "artifact_kernel",
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

def write_dictionary_text(path: Path, rows: list[dict[str, Any]]):
    """Write one plain-text dictionary entry per line: term = definition [note]."""
    path.parent.mkdir(parents=True, exist_ok=True)
    items = sorted(rows, key=lambda r: str(r.get("term") or "").casefold())
    lines = []
    for row in items:
        term = str(row.get("term") or "")
        definition = str(row.get("definition") or "")
        note = str(row.get("notes") or "")
        value = definition
        if note:
            value = f"{value} [{note}]" if value else f"[{note}]"
        lines.append(f"{term} = {value}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")

def write_json(path: Path, value: Any):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def write_rpc_signatures(path: Path, catalog: list[dict[str, Any]]):
    """Write one plain RPC signature per line, preserving types and defaults."""
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = []
    for item in catalog:
        name = str(item.get("name") or "")
        inputs = str(item.get("inputs") or "")
        lines.append(f"{name}({inputs})")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")

def write_rpc_definitions(path: Path, catalog: list[dict[str, Any]]):
    """Write exact implementation lookup after a worker narrows candidate RPCs."""
    path.parent.mkdir(parents=True, exist_ok=True)
    parts = []
    for item in catalog:
        name = str(item.get("name") or "")
        inputs = str(item.get("inputs") or "")
        result = str(item.get("result") or "")
        definition = str(item.get("definition") or "")
        parts.append(f"## {name}({inputs}) -> {result}\n\n```sql\n{definition}\n```")
    path.write_text("\n\n".join(parts) + "\n", encoding="utf-8")

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

def proof_rehearsal_root(objects: list[dict[str, Any]]) -> dict[str, Any] | None:
    """Find the current comprehensive proof-rehearsal root without schema-specific logic."""
    active = [o for o in objects if o.get("trashed_at") is None]
    by_id = {o.get("id"): o for o in active}
    preferred = by_id.get("proof_rehearsals01")
    if preferred and str(preferred.get("title") or "").strip() == "Comprehensive Proof Rehearsals":
        return preferred

    candidates = [
        o for o in active
        if str(o.get("title") or "").strip() == "Comprehensive Proof Rehearsals"
    ]
    if not candidates:
        return None
    candidates.sort(key=lambda o: (
        o.get("lifecycle_status") != "active",
        str(o.get("updated_at") or ""),
        str(o.get("id") or ""),
    ))
    return candidates[0]

def write_research_main_lines(path: Path, objects: list[dict[str, Any]]) -> tuple[str | None, int]:
    """Export direct children of the current comprehensive proof-rehearsal root."""
    path.mkdir(parents=True, exist_ok=True)
    root = proof_rehearsal_root(objects)
    if root is None:
        write_text(
            path / "README.md",
            "# Research main lines\n\n"
            "No Comprehensive Proof Rehearsals root is defined yet. "
            "Add direct children beneath that root to populate this folder."
        )
        return None, 0

    kids = [
        o for o in objects
        if o.get("trashed_at") is None and o.get("parent_id") == root.get("id")
    ]
    kids.sort(key=lambda o: (
        o.get("position") is None,
        o.get("position") or 0,
        str(o.get("id") or ""),
    ))

    index = [
        "# Research main lines",
        "",
        f"Source root: [{root.get('id')}] {root.get('title')}",
        "",
    ]
    if kids:
        for child in kids:
            filename = f"{child['id']}.md"
            index.append(f"- `{filename}` — {child.get('title') or child['id']}")
            rendered = content_md(child)
            verify_content_md(rendered, child)
            write_exact_text(path / filename, rendered)
    else:
        index.append("No proof-rehearsal children have been added yet.")

    write_text(path / "README.md", "\n".join(index))
    return str(root.get("id")), len(kids)

def metadata(o: dict[str, Any]) -> dict[str, Any]:
    omit = {"statement", "body", "tree_path", "trashed_at"}
    m = {k: v for k, v in o.items() if k not in omit}
    # Integrity hashes refer to the exact UTF-8 source strings in Supabase.
    m["statement_sha256"] = sha256_text(o.get("statement") or "")
    m["body_sha256"] = sha256_text(o.get("body") or "")
    return m

def render_forest(objects: list[dict[str, Any]], mode: str) -> str:
    active = {o["id"]: o for o in objects if o.get("trashed_at") is None}
    children: dict[str | None, list[str]] = {}
    for o in active.values():
        children.setdefault(o.get("parent_id"), []).append(o["id"])

    def sibling_key(oid: str):
        o = active[oid]
        return (
            o.get("position") is None,
            o.get("position") or 0,
            str(oid),
        )

    for ids in children.values():
        ids.sort(key=sibling_key)

    lines = []

    def emit(oid: str, depth: int):
        o = active[oid]
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
        for kid in children.get(oid, []):
            emit(kid, depth + 1)

    for oid in children.get(None, []):
        emit(oid, 0)
    return "\n".join(lines)

def frontier_payload(
    objects: list[dict[str, Any]],
    edges: list[dict[str, Any]],
    state_rows: list[dict[str, Any]],
) -> dict[str, Any]:
    """Reproduce frontier() from the mirrored live rows."""
    active = {o["id"]: o for o in objects if o.get("trashed_at") is None}
    state = state_rows[0] if state_rows else {}
    root_id = state.get("grand_theorem_id")
    root = active.get(root_id)
    root_path = (root or {}).get("tree_path")
    if not root_path:
        return {
            "entries": [],
            "frontier_count": 0,
            "repository_revision": state.get("revision"),
            "definition": "Active theorem-facing terminal research objects visible for work.",
            "note": "Grand-theorem root unavailable in mirror.",
        }

    hidden_paths = [
        o.get("tree_path") for o in active.values()
        if o.get("atlas_hidden") and o.get("tree_path")
    ]

    superseded = set()
    for e in edges:
        if e.get("kind") != "supersedes":
            continue
        metadata = e.get("metadata") or {}
        if metadata.get("supersession_state", "effective") != "effective":
            continue
        replacement = active.get(e.get("from_id"))
        if replacement and replacement.get("lifecycle_status") == "active" and replacement.get("audit_status") != "failed":
            superseded.add(e.get("to_id"))

    fenced = set()
    for e in edges:
        if e.get("kind") != "fence":
            continue
        fence = active.get(e.get("from_id"))
        if fence and fence.get("lifecycle_status") == "active" and fence.get("audit_status") != "failed":
            fenced.add(e.get("to_id"))

    visible: dict[str, dict[str, Any]] = {}
    for oid, o in active.items():
        tree_path = o.get("tree_path") or ""
        if o.get("lifecycle_status") != "active":
            continue
        if o.get("audit_status") == "failed":
            continue
        if o.get("object_type") == "fence":
            continue
        if (o.get("attention") or "available") == "hidden":
            continue
        if (o.get("support_status") or "unchecked") == "blocked":
            continue
        if not tree_path.startswith(root_path):
            continue
        if any(tree_path.startswith(hp) for hp in hidden_paths):
            continue
        if oid in superseded:
            continue
        visible[oid] = o

    visible_parents = {o.get("parent_id") for o in visible.values()}
    leaves = [o for oid, o in visible.items() if oid not in visible_parents]

    def atlas_height_key(o: dict[str, Any]) -> int:
        try:
            return int(o.get("atlas_height"))
        except (TypeError, ValueError):
            return -1

    def attention_rank(o: dict[str, Any]) -> int:
        return {"focus": 0, "available": 1}.get(o.get("attention"), 2)

    leaves.sort(key=lambda o: (
        attention_rank(o),
        o.get("atlas_height") is None,
        -atlas_height_key(o),
        str(o.get("tree_path") or ""),
        str(o.get("id") or ""),
    ))

    entries = []
    for o in leaves:
        summary = str(o.get("simplified_statement") or "").strip() or str(o.get("title") or "")
        entries.append({
            "id": o.get("id"),
            "parent_id": o.get("parent_id"),
            "title": o.get("title"),
            "summary": summary,
            "category": o.get("research_level") or o.get("object_type"),
            "mathematical_status": o.get("mathematical_status"),
            "audit_status": o.get("audit_status"),
            "support_status": o.get("support_status"),
            "attention": o.get("attention"),
            "pending": o.get("audit_status") == "pending",
            "obstructed": (o.get("support_status") == "blocked") or (o.get("id") in fenced),
            "atlas_height": o.get("atlas_height"),
            "research_interface": o.get("research_interface") or {},
        })

    return {
        "entries": entries,
        "frontier_count": len(entries),
        "repository_revision": state.get("revision"),
        "definition": "Active theorem-facing terminal research objects that are visible for work: nonhidden, nonfailed, nonblocked, non-superseded leaves of the grand-theorem reasoning tree.",
        "note": "Flat frontier only. After choosing an item, call ancestry() or simplified_ancestry() separately for route context.",
    }


def frontier_text(frontier: dict[str, Any]) -> str:
    """Render the mathematical working surface of frontier() without JSON scaffolding."""
    lines = [
        "# Research frontier",
        "",
        f"Repository revision: {frontier.get('repository_revision')}",
        f"Frontier objects: {frontier.get('frontier_count', 0)}",
        "",
        str(frontier.get("definition") or ""),
        "",
        str(frontier.get("note") or ""),
    ]

    interface_order = [
        "given", "produces", "need", "consumer", "warning", "implication",
        "role", "first_attack", "global_relevance", "trust",
    ]

    for e in frontier.get("entries") or []:
        summary = str(e.get("summary") or e.get("title") or "").strip()
        lines.extend(["", f"## [{e.get('id')}] {summary}"])

        statuses = [
            str(e.get("attention") or ""),
            str(e.get("category") or ""),
            str(e.get("mathematical_status") or ""),
            str(e.get("audit_status") or ""),
            str(e.get("support_status") or ""),
        ]
        if e.get("pending"):
            statuses.append("pending")
        if e.get("obstructed"):
            statuses.append("obstructed")
        statuses = [s for s in statuses if s]
        if statuses:
            lines.append(" · ".join(statuses))

        if e.get("parent_id"):
            lines.append(f"Parent: [{e.get('parent_id')}]")

        interface = e.get("research_interface") or {}
        keys = [k for k in interface_order if interface.get(k) not in (None, "", [], {})]
        keys += sorted(
            k for k, v in interface.items()
            if k not in interface_order and v not in (None, "", [], {})
        )
        for key in keys:
            label = key.replace("_", " ").title()
            value = interface[key]
            if isinstance(value, (dict, list)):
                value = json.dumps(value, ensure_ascii=False, separators=(",", ":"))
            lines.append(f"**{label}:** {value}")

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
    write_dictionary_text(
        root / "vocabulary" / "standardization_dictionary.txt",
        rows["standardization_dictionary"],
    )
    write_yaml(root / "state" / "project.yaml", rows["state"])
    write_yaml(root / "state" / "architecture_migration_notes.yaml", rows["architecture_migration_notes"])

    ctx = root / "_context"
    main_line_root_id, main_line_count = write_research_main_lines(
        ctx / "research_main_lines", objects
    )
    hindex = context(schema, "help")
    topics = hindex.get("topics") or []

    frontier = frontier_payload(objects, rows["edges"], rows["state"])
    write_json(ctx / "frontier.json", frontier)
    write_text(ctx / "frontier.md", frontier_text(frontier))

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
        filename = "kernel" if key == "artifact_kernel" else key
        write_text(ctx / "policies" / f"{filename}.md", body_of(policies[key]))
    for key in MODE_POLICIES:
        write_text(ctx / "roles" / f"{key.removeprefix('mode_')}.md", body_of(policies[key]))

    write_json(ctx / "rpc_signatures.json", context(schema, "rpc_signatures"))
    write_json(ctx / "rpc_list.json", context(schema, "rpc_list"))
    rpc_catalog = context(schema, "rpc_catalog")
    write_json(ctx / "rpc_catalog.json", rpc_catalog)
    write_rpc_signatures(ctx / "rpc_signatures.txt", rpc_catalog)
    write_rpc_definitions(ctx / "rpc_definitions.md", rpc_catalog)
    write_text(ctx / "simplified_forest.md", render_forest(objects, "simplified"))
    write_text(ctx / "statement_forest.md", render_forest(objects, "statement"))
    write_text(ctx / "statement_plus_proof_forest.md", render_forest(objects, "full"))

    state = rows["state"][0] if rows["state"] else {}
    bootstrap = f"""# {folder} artifact bootstrap

This directory is the artifact snapshot for repository revision {state.get('revision')}. Supabase remains authoritative for live state and updates.

If you reached this file through {schema}.boot(), the worker identity and boot contract are already established. Legacy startup is quarantined; do not call {schema}.startup().

## Mandatory startup reading

Before the first continue()/sync() call, read ALL of:

1. startup_bootstrap.md
2. kernel.md
3. project_policy.md
4. standardization_dictionary.txt
5. rpc_signatures.txt
6. research_main_lines/README.md
7. every other Markdown document in research_main_lines/

Do not sample research_main_lines/. The complete proof-rehearsal set is the primary mathematical boot context. The standardization dictionary is mandatory; use its definitions rather than inferring project terminology from the rehearsals.

After continue() assigns a mode, and before doing the assigned work, read exactly the matching roles/<mode>.md. That role file is the final mandatory startup document.

No other artifact file is required at startup by default.

## On-demand only

- rpc_definitions.md — consult only when rpc_signatures.txt is insufficient.
- research_lookup/frontier.md
- research_lookup/simplified_forest.md
- research_lookup/statement_forest.md
- research_lookup/statement_plus_proof_forest.md

research_lookup/ is not part of ordinary startup. Use it only when a concrete need remains unresolved after the mandatory material, or when exact historical/result-tree detail is required. Legacy Atlas is quarantined and is not part of the worker interface or generated artifact.

Pull exact live mathematics from Supabase only when needed, especially for changes after this artifact revision or before state-sensitive mutations. continue(worker_id) will report context files whose live hashes have changed since the artifact snapshot rather than resending unchanged artifact material.

Repository revision at export: {state.get('revision')}
"""
    write_text(ctx / "startup_bootstrap.md", bootstrap)

    write_json(root / "mirror_manifest.json", {
        "folder": folder,
        "supabase_schema": schema,
        "repository_revision": state.get("revision"),
        "live_object_count": len(active),
        "root_count": len(roots),
        "research_main_lines_root_id": main_line_root_id,
        "research_main_line_count": main_line_count,
        "mirror_format": 2,
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

# Manual research-mirror sync trigger after object-ID integrity cleanup; no functional effect.
