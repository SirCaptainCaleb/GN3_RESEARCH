#!/usr/bin/env python3
"""Build GN3 durable role-context pages from Supabase.

Supabase remains canonical. These pages intentionally omit live research state;
workers obtain that through GN3 synchronization RPCs.
"""

from __future__ import annotations

import html
import json
import os
import sys
import urllib.error
import urllib.request
from collections import defaultdict
from pathlib import Path

SUPABASE_URL = os.environ["SUPABASE_URL"].rstrip("/")
SUPABASE_KEY = os.environ["SUPABASE_SECRET_KEY"]
PAGE_CHARS = 20_000
OUT = Path("_site")

ROLES = {
    "researcher": {
        "title": "Researcher",
        "description": "Durable mathematical and research-method context for GN3 Researchers.",
    },
    "vice_director": {
        "title": "Vice Director",
        "description": "Durable mathematical, architectural, and integration context for the GN3 Vice Director.",
    },
    "astra": {
        "title": "Astra",
        "description": "Durable mathematical context plus the scarce strategic Director protocol.",
    },
    "auditor": {
        "title": "Auditor",
        "description": "Durable audit, language, computation, and certification protocol. Exact audit targets remain live Supabase state.",
    },
}


def rpc(name: str, payload: dict) -> object:
    headers = {
        "apikey": SUPABASE_KEY,
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "gn3-pages-builder/1.0",
    }
    # New sb_secret_* keys are API keys, not JWTs. Legacy service_role
    # JWTs still use Authorization: Bearer in addition to apikey.
    if not SUPABASE_KEY.startswith("sb_secret_"):
        headers["Authorization"] = f"Bearer {SUPABASE_KEY}"

    request = urllib.request.Request(
        f"{SUPABASE_URL}/rest/v1/rpc/{name}",
        data=json.dumps(payload).encode("utf-8"),
        method="POST",
        headers=headers,
    )
    try:
        with urllib.request.urlopen(request, timeout=90) as response:
            value = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Supabase RPC {name} failed: HTTP {exc.code}: {detail}") from exc

    # Be tolerant of scalar-json and one-row wrappers.
    if isinstance(value, list) and len(value) == 1 and isinstance(value[0], dict):
        return value[0]
    return value


def get_state() -> dict:
    state = rpc("gn3_get_state", {})
    if not isinstance(state, dict) or "repository_revision" not in state:
        raise RuntimeError(f"Unexpected gn3_get_state response: {type(state)!r}")
    return state


def get_manifest(role: str) -> dict:
    manifest = rpc("gn3_pages_manifest", {"p_role": role})
    if not isinstance(manifest, dict) or not isinstance(manifest.get("documents"), list):
        raise RuntimeError(f"Unexpected manifest for {role}")
    return manifest


def fetch_bodies(ids: list[str], revision: int) -> dict[str, str]:
    if not ids:
        return {}

    cursor = 0
    chunks: dict[str, list[tuple[int, int, str, int]]] = defaultdict(list)
    seen_revision = None

    while True:
        page = rpc(
            "gn3_get_documents",
            {
                "p_ids": ids,
                "p_content": "body",
                "p_cursor": cursor,
                "p_page_chars": PAGE_CHARS,
                "p_expected_revision": revision,
                "p_include_trashed": False,
            },
        )
        if not isinstance(page, dict):
            raise RuntimeError("Unexpected gn3_get_documents response")

        page_revision = page.get("repository_revision")
        if page_revision != revision:
            raise RuntimeError(
                f"Revision drift while assembling Pages: expected {revision}, got {page_revision}"
            )
        seen_revision = page_revision

        for item in page.get("items", []):
            chunks[item["id"]].append(
                (
                    int(item["chunk_start"]),
                    int(item["chunk_end"]),
                    item.get("content_chunk", ""),
                    int(item["source_body_chars"]),
                )
            )

        if page.get("complete"):
            break

        next_cursor = page.get("next_cursor")
        if next_cursor is None:
            raise RuntimeError("Incomplete GN3 document stream without next_cursor")
        cursor = int(next_cursor)

    if seen_revision != revision:
        raise RuntimeError("No revision-pinned document stream was returned")

    bodies: dict[str, str] = {}
    for doc_id in ids:
        parts = sorted(chunks.get(doc_id, []), key=lambda x: x[0])
        if not parts:
            raise RuntimeError(f"GN3 document {doc_id} was omitted from batch response")

        expected_start = 0
        source_chars = parts[0][3]
        assembled = []

        for start, end, text, reported_source_chars in parts:
            if reported_source_chars != source_chars:
                raise RuntimeError(f"Source length changed while reading {doc_id}")
            if start != expected_start:
                raise RuntimeError(
                    f"Gap/overlap while reading {doc_id}: expected {expected_start}, got {start}"
                )
            if end < start:
                raise RuntimeError(f"Invalid chunk bounds for {doc_id}")
            assembled.append(text)
            expected_start = end

        body = "".join(assembled)
        if expected_start != source_chars or len(body) != source_chars:
            raise RuntimeError(
                f"Incomplete body for {doc_id}: assembled {len(body)} of {source_chars} chars"
            )
        bodies[doc_id] = body

    return bodies


def build_markdown(role: str, manifest: dict, bodies: dict[str, str]) -> str:
    info = ROLES[role]
    lines = [
        f"# GN3 — {info['title']} durable context",
        "",
        info["description"],
        "",
        "**Scope.** This is a generated, read-only view of slow-changing GN3 context. "
        "Supabase GN3 is canonical. Live guidance, research-tree state, active research, "
        "audit queues, failures, removals, and frontier movement are intentionally excluded; "
        "obtain live state through the GN3 synchronization interface.",
        "",
        f"**Transport.** The exporter reads Supabase through revision-pinned GN3 RPCs with "
        f"a maximum content page of {PAGE_CHARS:,} characters and verifies every assembled body.",
        "",
    ]

    if role in ("researcher", "vice_director"):
        lines += [
            "**Fresh live state.** After reading this page in full, call "
            f"`gn3_sync('{role}', since_revision := null, cursor := 0, page_chars := 12000, expected_revision := null)`. "
            "Consume every returned page at the pinned repository revision. Thereafter use the last "
            "fully consumed revision as numeric `since_revision` for delta synchronization.",
            "",
            "**Fallback.** If this generated page is unavailable, incomplete, or visibly truncated, "
            f"use `gn3_startup('{role}', ...)` and consume the complete canonical startup stream.",
            "",
        ]
    elif role == "astra":
        lines += [
            "**Astra live layer.** This page supplies durable context only. Astra still uses "
            "`gn3_startup('astra', ...)` for the current strategic/live layer until a dedicated "
            "Astra live-sync interface replaces that step.",
            "",
        ]
    elif role == "auditor":
        lines += [
            "**Auditor live target.** The exact audit target and dependency closure are not compiled "
            "into this durable page because they vary by assignment. Use "
            "`gn3_startup('auditor', target_id, ...)` for the exact assigned target context.",
            "",
        ]

    current_section = None
    for doc in manifest["documents"]:
        section = doc["section"]
        if section != current_section:
            current_section = section
            lines += ["", f"# {section}", ""]

        doc_id = doc["id"]
        lines += [
            f"## {doc['title']}",
            "",
            f"_GN3 document: `{doc_id}`_",
            "",
            bodies[doc_id].rstrip(),
            "",
        ]

    return "\n".join(lines).rstrip() + "\n"


def render_html(title: str, markdown_text: str) -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<style>
:root {{ color-scheme: light dark; }}
body {{
  margin: 0 auto;
  max-width: 1180px;
  padding: 1.5rem;
  font-family: system-ui, sans-serif;
  line-height: 1.45;
}}
nav {{ margin-bottom: 1rem; }}
pre {{
  white-space: pre-wrap;
  overflow-wrap: anywhere;
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.92rem;
}}
a {{ text-underline-offset: 0.15em; }}
</style>
</head>
<body>
<nav><a href="index.html">GN3 role contexts</a></nav>
<pre>{html.escape(markdown_text)}</pre>
</body>
</html>
"""


def build_index() -> str:
    cards = []
    for role, info in ROLES.items():
        cards.append(
            f'<li><a href="{role}.html"><strong>{html.escape(info["title"])}</strong></a>'
            f'<br>{html.escape(info["description"])}</li>'
        )
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>GN3 Agent Context</title>
<style>
:root {{ color-scheme: light dark; }}
body {{ margin: 0 auto; max-width: 900px; padding: 2rem; font-family: system-ui, sans-serif; line-height: 1.5; }}
li {{ margin: 1.1rem 0; }}
a {{ text-underline-offset: 0.15em; }}
</style>
</head>
<body>
<h1>GN3 Agent Context</h1>
<p>Compiled durable context for GN3 research roles. Supabase GN3 remains canonical; live state is synchronized separately.</p>
<ul>{''.join(cards)}</ul>
</body>
</html>
"""


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    state = get_state()
    revision = int(state["repository_revision"])

    manifests = {role: get_manifest(role) for role in ROLES}

    all_ids: list[str] = []
    seen: set[str] = set()
    for role in ROLES:
        for doc in manifests[role]["documents"]:
            doc_id = doc["id"]
            if doc_id not in seen:
                seen.add(doc_id)
                all_ids.append(doc_id)

    bodies = fetch_bodies(all_ids, revision)

    for role, info in ROLES.items():
        md = build_markdown(role, manifests[role], bodies)
        (OUT / f"{role}.md").write_text(md, encoding="utf-8")
        (OUT / f"{role}.html").write_text(
            render_html(f"GN3 — {info['title']} durable context", md),
            encoding="utf-8",
        )

    (OUT / "index.html").write_text(build_index(), encoding="utf-8")

    # Keep Jekyll out of the deployment path; these are already-built static files.
    (OUT / ".nojekyll").write_text("", encoding="utf-8")

    print(
        f"Built {len(ROLES)} GN3 role pages from {len(all_ids)} durable documents "
        f"at coherent repository revision {revision}."
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"GN3 Pages build failed: {exc}", file=sys.stderr)
        raise
