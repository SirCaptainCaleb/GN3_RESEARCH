#!/usr/bin/env python3
"""Build a coherent GN3N context bundle for LLM workers.

The bundle is intentionally file-oriented: GitHub Actions transports it as an
artifact ZIP, so large corpora never need to cross a connector as one giant
JSON/text field.

Supabase remains canonical. This exporter is read-only and never calls
gn3n.startup(), so builds do not allocate fake worker IDs.
"""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path
from typing import Any

SUPABASE_URL = os.environ["SUPABASE_URL"].rstrip("/")
SUPABASE_KEY = os.environ["SUPABASE_SECRET_KEY"]
SCHEMA = os.environ.get("GN3_SCHEMA", "gn3n")
OUT = Path(os.environ.get("GN3_CONTEXT_OUT", "_context_artifact"))
PAGE_SIZE = 1000

MODE_POLICIES = [
    "mode_audit",
    "mode_brainstorm",
    "mode_coordination",
    "mode_isolated_research",
    "mode_literature_bridge",
    "mode_methodology_review",
    "mode_proof_rehearsal",
    "mode_reasoning_hygiene",
    "mode_research",
]
CORE_POLICIES = [
    "startup_kernel",
    "worker_kernel",
    "project_policy",
    "research_full_guidance",
    "architecture_invariants",
]

# Mirrors the current GN3N startup-atlas configuration. These can be overridden
# from Actions without changing code if project tuning changes.
STARTUP_CORE_DEPTH = int(os.environ.get("GN3_STARTUP_ATLAS_CORE_DEPTH", "2"))
STARTUP_BALANCE_DEPTH = int(os.environ.get("GN3_STARTUP_ATLAS_BALANCE_DEPTH", "1"))
STARTUP_LANDMARK_LIMIT = int(os.environ.get("GN3_STARTUP_ATLAS_LANDMARK_LIMIT", "18"))
STARTUP_BRANCH_LANDMARK_LIMIT = int(
    os.environ.get("GN3_STARTUP_ATLAS_BRANCH_LANDMARK_LIMIT", "3")
)
STARTUP_MIN_SUBTREE_OBJECTS = int(
    os.environ.get("GN3_STARTUP_ATLAS_MIN_SUBTREE_OBJECTS", "12")
)


def headers(*, profile: bool = True) -> dict[str, str]:
    h = {
        "apikey": SUPABASE_KEY,
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": "gn3-context-artifact/1.0",
    }
    # New sb_secret_* keys are API keys, not JWTs. Legacy service_role JWTs
    # still use Authorization: Bearer in addition to apikey.
    if not SUPABASE_KEY.startswith("sb_secret_"):
        h["Authorization"] = f"Bearer {SUPABASE_KEY}"
    if profile:
        h["Accept-Profile"] = SCHEMA
        h["Content-Profile"] = SCHEMA
    return h


def request_json(url: str, *, method: str = "GET", payload: Any = None) -> Any:
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, method=method, headers=headers())
    try:
        with urllib.request.urlopen(req, timeout=120) as response:
            raw = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code} for {url}: {detail}") from exc
    return json.loads(raw)


def rpc(name: str, payload: dict[str, Any] | None = None) -> Any:
    return request_json(
        f"{SUPABASE_URL}/rest/v1/rpc/{name}",
        method="POST",
        payload=payload or {},
    )


def table_all(
    table: str,
    *,
    select: str,
    filters: dict[str, str] | None = None,
    order: str | None = None,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    offset = 0
    while True:
        params: list[tuple[str, str]] = [("select", select)]
        for key, value in (filters or {}).items():
            params.append((key, value))
        if order:
            params.append(("order", order))
        params += [("limit", str(PAGE_SIZE)), ("offset", str(offset))]
        url = (
            f"{SUPABASE_URL}/rest/v1/{table}?"
            + urllib.parse.urlencode(params, doseq=True, safe="(),.*")
        )
        page = request_json(url)
        if not isinstance(page, list):
            raise RuntimeError(f"Unexpected {table} response: {type(page)!r}")
        rows.extend(page)
        if len(page) < PAGE_SIZE:
            break
        offset += len(page)
    return rows


def body_of(value: Any) -> str:
    if isinstance(value, dict):
        return str(value.get("body") or "")
    return str(value or "")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=False) + "\n",
        encoding="utf-8",
    )


def depth_from_path(tree_path: str | None) -> int:
    if not tree_path:
        return 0
    return max(0, len([x for x in tree_path.strip("/").split("/") if x]) - 1)


def render_forest(
    objects: list[dict[str, Any]],
    *,
    mode: str,
) -> str:
    lines: list[str] = []
    for obj in objects:
        depth = depth_from_path(obj.get("tree_path"))
        indent = "  " * depth
        obj_id = obj["id"]
        title = (obj.get("title") or "").strip()
        simplified = (obj.get("simplified_statement") or "").strip()
        statement = (obj.get("statement") or "").strip()
        body = (obj.get("body") or "").strip()

        if mode == "simplified":
            text = simplified or f"‹{title}›"
            lines.append(f"{indent}• [{obj_id}] {text}")
            continue

        lines.append(f"{indent}• [{obj_id}] {title}")
        subindent = indent + "    "
        if statement:
            lines.append(f"{subindent}STATEMENT")
            lines.extend(f"{subindent}{line}" for line in statement.splitlines())
        else:
            lines.append(f"{subindent}STATEMENT ‹none›")

        if mode == "full":
            lines.append(f"{subindent}BODY / PROOF")
            if body:
                lines.extend(f"{subindent}{line}" for line in body.splitlines())
            else:
                lines.append(f"{subindent}‹none›")
        lines.append("")
    return "\n".join(lines)


def atlas_outline(entries: list[dict[str, Any]]) -> str:
    by_id = {e.get("id"): e for e in entries if e.get("id")}
    memo: dict[str, int] = {}

    def d(e: dict[str, Any]) -> int:
        eid = str(e.get("id"))
        if eid in memo:
            return memo[eid]
        parent = e.get("parent_container_id")
        if not parent or parent not in by_id:
            memo[eid] = 0
        else:
            memo[eid] = d(by_id[parent]) + 1
        return memo[eid]

    lines = []
    for e in entries:
        depth = d(e)
        summary = (e.get("summary") or e.get("title") or "").strip()
        markers = []
        if int(e.get("pending_count") or 0):
            markers.append(f"pending={e['pending_count']}")
        if int(e.get("obstructed_count") or 0):
            markers.append(f"obstructed={e['obstructed_count']}")
        suffix = f" [{' '.join(markers)}]" if markers else ""
        lines.append(f"{'  ' * depth}• [{e.get('id')}] {summary}{suffix}")
    return "\n".join(lines)


def build_startup_atlas(
    full_atlas: dict[str, Any],
    objects_by_id: dict[str, dict[str, Any]],
    fence_targets: set[str],
) -> dict[str, Any]:
    entries = list(full_atlas.get("entries") or [])
    by_id = {e["id"]: e for e in entries}
    ordinals = {e["id"]: i for i, e in enumerate(entries)}

    enriched: list[dict[str, Any]] = []
    for e0 in entries:
        e = dict(e0)
        ancestry: list[str] = []
        seen: set[str] = set()
        cur: dict[str, Any] | None = e
        while cur and cur.get("id") not in seen:
            seen.add(cur["id"])
            ancestry.append(cur["id"])
            pid = cur.get("parent_container_id")
            cur = by_id.get(pid) if pid else None
        ancestry.reverse()
        titles = [str(by_id[x].get("title") or "") for x in ancestry]
        depth = len(ancestry) - 1
        if len(ancestry) > STARTUP_BALANCE_DEPTH:
            balance_key = ancestry[STARTUP_BALANCE_DEPTH]
        else:
            balance_key = ancestry[-1]
        score = (
            8.0 * (int(e.get("pending_count") or 0) + int(e.get("obstructed_count") or 0))
            + 2.0
            * (
                int(e.get("subtree_pending_count") or 0)
                + int(e.get("subtree_obstructed_count") or 0)
            )
            + min(int(e.get("subtree_object_count") or 0), 60) / 8.0
            + min(int(e.get("descendant_container_count") or 0), 12)
        )
        e["_ord"] = ordinals[e["id"]]
        e["_depth"] = depth
        e["_ancestry_ids"] = ancestry
        e["_ancestry_titles"] = titles
        e["_balance_key"] = balance_key
        e["_landmark_score"] = score
        enriched.append(e)

    core = [e for e in enriched if e["_depth"] <= STARTUP_CORE_DEPTH]
    editorial = [
        e
        for e in enriched
        if e["_depth"] > STARTUP_CORE_DEPTH and e.get("atlas_height") is not None
    ]
    candidates = [
        e
        for e in enriched
        if e["_depth"] > STARTUP_CORE_DEPTH
        and e.get("atlas_height") is None
        and (
            int(e.get("subtree_object_count") or 0) >= STARTUP_MIN_SUBTREE_OBJECTS
            or int(e.get("pending_count") or 0) + int(e.get("obstructed_count") or 0) > 0
            or int(e.get("subtree_pending_count") or 0)
            + int(e.get("subtree_obstructed_count") or 0)
            > 0
        )
    ]

    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for e in candidates:
        grouped[e["_balance_key"]].append(e)

    automatic_pool: list[dict[str, Any]] = []
    for group in grouped.values():
        group.sort(
            key=lambda e: (
                -e["_landmark_score"],
                -int(e.get("subtree_object_count") or 0),
                e["_depth"],
                e["_ord"],
            )
        )
        automatic_pool.extend(group[:STARTUP_BRANCH_LANDMARK_LIMIT])

    automatic_pool.sort(
        key=lambda e: (
            -e["_landmark_score"],
            -int(e.get("subtree_object_count") or 0),
            e["_depth"],
            e["_ord"],
        )
    )
    automatic = automatic_pool[:STARTUP_LANDMARK_LIMIT]

    def clean(e: dict[str, Any], *, deep: bool) -> dict[str, Any]:
        out = {k: v for k, v in e.items() if not k.startswith("_")}
        out["depth"] = e["_depth"]
        if deep:
            out["ancestry_ids"] = e["_ancestry_ids"]
            out["ancestry_titles"] = e["_ancestry_titles"]
        obj = objects_by_id.get(e["id"], {})
        if obj.get("audit_status") is not None:
            out["audit_status"] = obj.get("audit_status")
            out["pending"] = obj.get("audit_status") == "pending"
        if obj.get("support_status") is not None:
            out["support_status"] = obj.get("support_status")
        out["obstructed"] = (
            obj.get("support_status") == "blocked" or e["id"] in fence_targets
        )
        return out

    core_sorted = sorted(core, key=lambda e: e["_ord"])
    deep_sorted = sorted(editorial, key=lambda e: e["_ord"]) + sorted(
        automatic, key=lambda e: e["_ord"]
    )

    return {
        "purpose": (
            "First-contact research briefing: enough breadth and depth for a strong "
            "fresh mathematician to choose among plausible routes, understand why "
            "the main route is where it is, and recognize reusable machinery without "
            "loading the entire conceptual Atlas."
        ),
        "core_map": [clean(e, deep=False) for e in core_sorted],
        "deep_landmarks": [clean(e, deep=True) for e in deep_sorted],
        "coverage": {
            "full_container_count": len(entries),
            "core_map_count": len(core),
            "editorial_landmark_count": len(editorial),
            "automatic_landmark_count": len(automatic),
            "startup_container_count": len(core) + len(editorial) + len(automatic),
            "omitted_hyperlocal_count": max(
                0, len(entries) - len(core) - len(editorial) - len(automatic)
            ),
        },
        "selection_config": {
            "core_depth": STARTUP_CORE_DEPTH,
            "balance_depth": STARTUP_BALANCE_DEPTH,
            "landmark_limit": STARTUP_LANDMARK_LIMIT,
            "branch_landmark_limit": STARTUP_BRANCH_LANDMARK_LIMIT,
            "min_subtree_objects": STARTUP_MIN_SUBTREE_OBJECTS,
        },
        "repository_revision": full_atlas.get("repository_revision"),
    }


def startup_atlas_outline(startup: dict[str, Any]) -> str:
    combined = []
    seen: set[str] = set()
    for e in list(startup.get("core_map") or []) + list(startup.get("deep_landmarks") or []):
        if e.get("id") in seen:
            continue
        seen.add(e.get("id"))
        combined.append(e)
    lines = []
    for e in combined:
        depth = int(e.get("depth") or 0)
        summary = (e.get("summary") or e.get("title") or "").strip()
        markers = []
        if e.get("pending"):
            markers.append("pending")
        if e.get("obstructed"):
            markers.append("obstructed")
        suffix = f" [{' '.join(markers)}]" if markers else ""
        lines.append(f"{'  ' * depth}• [{e.get('id')}] {summary}{suffix}")
    return "\n".join(lines)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    state_rows = table_all(
        "state",
        select="revision,phase,grand_theorem_id",
        filters={"singleton": "eq.true"},
    )
    if len(state_rows) != 1:
        raise RuntimeError(f"Expected one GN3N state row, got {len(state_rows)}")
    state = state_rows[0]
    revision = int(state["revision"])

    objects = table_all(
        "objects",
        select=(
            "id,parent_id,tree_path,position,object_type,title,statement,body,"
            "simplified_statement,mathematical_status,research_level,lifecycle_status,"
            "audit_status,support_status,atlas_height,atlas_hidden,semantic_container_text,"
            "trashed_at"
        ),
        filters={"trashed_at": "is.null"},
        order="tree_path.asc",
    )
    objects_by_id = {o["id"]: o for o in objects}

    fence_edges = table_all(
        "edges",
        select="from_id,to_id,kind",
        filters={"kind": "eq.fence"},
        order="to_id.asc",
    )
    fence_targets = {
        e["to_id"]
        for e in fence_edges
        if (
            objects_by_id.get(e["from_id"], {}).get("lifecycle_status") == "active"
            and objects_by_id.get(e["from_id"], {}).get("audit_status") != "failed"
        )
    }

    # Snapshot consistency: fail rather than silently producing a mixed-revision bundle.
    state_after = table_all(
        "state",
        select="revision,phase,grand_theorem_id",
        filters={"singleton": "eq.true"},
    )[0]
    if int(state_after["revision"]) != revision:
        raise RuntimeError(
            f"Repository revision moved during object snapshot: {revision} -> "
            f"{state_after['revision']}. Retry the workflow."
        )

    full_atlas = rpc("atlas", {"p_category": None, "p_limit": None})
    if int(full_atlas.get("repository_revision", -1)) != revision:
        raise RuntimeError("Atlas revision does not match object snapshot")

    startup_atlas = build_startup_atlas(full_atlas, objects_by_id, fence_targets)

    help_index = rpc("help", {"p_topic": None})
    help_topics = list(help_index.get("topics") or [])
    help_docs: dict[str, Any] = {}
    for topic in help_topics:
        help_docs[topic] = rpc("help", {"p_topic": topic})

    rpc_list = rpc("rpc_list", {})
    rpc_signatures = rpc("rpc_signatures", {"p_name": None})
    dictionary = rpc("standardization_dictionary", {})

    policies: dict[str, Any] = {}
    for key in CORE_POLICIES + MODE_POLICIES:
        policies[key] = rpc("get_policy", {"p_policy_key": key})

    # Verify again after all RPC reads. We want one coherent revision per ZIP.
    final_state = table_all(
        "state",
        select="revision,phase,grand_theorem_id",
        filters={"singleton": "eq.true"},
    )[0]
    if int(final_state["revision"]) != revision:
        raise RuntimeError(
            f"Repository revision moved during export: {revision} -> "
            f"{final_state['revision']}. Retry the workflow."
        )

    grand = objects_by_id.get(str(state.get("grand_theorem_id")), {})
    startup_help = help_docs.get("startup", {})
    startup_kernel = body_of(policies.get("startup_kernel"))
    project_policy = (objects_by_id.get("project_policy", {}).get("body") or "").strip()
    research_nudges = (objects_by_id.get("research_nudges", {}).get("body") or "").strip()
    scheduler_guidance = (
        objects_by_id.get("scheduler_guidance", {}).get("body") or ""
    ).strip()

    bootstrap = f"""GN3N WORKER BOOTSTRAP
Repository revision: {revision}
Project schema: {SCHEMA}

This artifact intentionally contains no worker ID and does not call startup()
while being built. A live session should still begin with:

    select * from {SCHEMA}.startup();

Retain the returned worker_id. Then call:

    select * from {SCHEMA}.continue(worker_id);

The ZIP supplies a coherent read-only snapshot of broad context. Live worker
identity, assignments, deltas, claims, broadcasts, and other ephemeral state
still come from Supabase.

Grand theorem:
[{grand.get('id', state.get('grand_theorem_id'))}] {grand.get('title', '')}
{grand.get('statement', '')}

=== STARTUP HELP ===
{body_of(startup_help)}

=== STARTUP KERNEL ===
{startup_kernel}

=== PROJECT POLICY ===
{project_policy}

=== RESEARCH NUDGES ===
{research_nudges}

=== CURRENT SCHEDULER GUIDANCE AT EXPORT TIME ===
{scheduler_guidance or '‹none›'}
"""
    write_text(OUT / "00_startup_bootstrap.txt", bootstrap)

    write_json(
        OUT / "00_manifest.json",
        {
            "schema": SCHEMA,
            "repository_revision": revision,
            "phase": state.get("phase"),
            "grand_theorem_id": state.get("grand_theorem_id"),
            "object_count": len(objects),
            "generated_by": "scripts/build_gn3_context_artifact.py",
            "coherent_revision": True,
            "files": [
                "00_startup_bootstrap.txt",
                "help/*",
                "roles/*",
                "policies/*",
                "atlas/atlas.txt",
                "atlas/atlas.json",
                "atlas/startup_atlas.txt",
                "atlas/startup_atlas.json",
                "forests/simplified_forest.txt",
                "forests/statement_forest.txt",
                "forests/statement_plus_proof_forest.txt",
                "vocabulary/standardization_dictionary.json",
            ],
        },
    )

    write_json(OUT / "help" / "_index.json", help_index)
    for topic, doc in help_docs.items():
        write_text(OUT / "help" / f"{topic}.txt", body_of(doc))
    write_json(OUT / "help" / "rpc_signatures.json", rpc_signatures)
    if isinstance(rpc_list, list):
        write_text(OUT / "help" / "rpc_list.txt", "\n".join(map(str, rpc_list)))
    else:
        write_json(OUT / "help" / "rpc_list.json", rpc_list)

    for key in CORE_POLICIES:
        write_text(OUT / "policies" / f"{key}.txt", body_of(policies[key]))
    for key in MODE_POLICIES:
        write_text(OUT / "roles" / f"{key.removeprefix('mode_')}.txt", body_of(policies[key]))

    write_json(OUT / "atlas" / "atlas.json", full_atlas)
    write_text(
        OUT / "atlas" / "atlas.txt",
        atlas_outline(list(full_atlas.get("entries") or [])),
    )
    write_json(OUT / "atlas" / "startup_atlas.json", startup_atlas)
    write_text(OUT / "atlas" / "startup_atlas.txt", startup_atlas_outline(startup_atlas))

    write_text(
        OUT / "forests" / "simplified_forest.txt",
        render_forest(objects, mode="simplified"),
    )
    write_text(
        OUT / "forests" / "statement_forest.txt",
        render_forest(objects, mode="statement"),
    )
    write_text(
        OUT / "forests" / "statement_plus_proof_forest.txt",
        render_forest(objects, mode="full"),
    )

    write_json(OUT / "vocabulary" / "standardization_dictionary.json", dictionary)

    # Small machine-readable index useful to future consumers without opening
    # any of the potentially huge forest files.
    write_json(
        OUT / "objects_index.json",
        [
            {
                "id": o["id"],
                "parent_id": o.get("parent_id"),
                "tree_path": o.get("tree_path"),
                "title": o.get("title"),
                "object_type": o.get("object_type"),
                "lifecycle_status": o.get("lifecycle_status"),
                "mathematical_status": o.get("mathematical_status"),
                "audit_status": o.get("audit_status"),
                "support_status": o.get("support_status"),
            }
            for o in objects
        ],
    )

    total_bytes = sum(p.stat().st_size for p in OUT.rglob("*") if p.is_file())
    print(
        f"Built GN3N context bundle at revision {revision}: "
        f"{len(objects)} non-trashed objects, {total_bytes:,} uncompressed bytes."
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"GN3N context artifact build failed: {exc}", file=sys.stderr)
        raise
