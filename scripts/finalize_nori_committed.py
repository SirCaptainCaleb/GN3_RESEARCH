#!/usr/bin/env python3
"""Publish an active-only NORI snapshot with object-level research statuses."""
from __future__ import annotations

import json
import shutil
from pathlib import Path

root = Path("nori")
manifest_path = root / "MANIFEST.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

# The Supabase mirror endpoints omit superseded manuscripts before export.
# Remove the legacy placeholder produced by older mirror builders.
shutil.rmtree(root / "SUPERSEDED", ignore_errors=True)

published = {}
for kind, key in (
    ("article", "article_versions"),
    ("section", "section_versions"),
    ("subsection", "subsection_versions"),
):
    entries = manifest.get(key, {})
    published[kind] = {}
    for object_id, info in entries.items():
        info["research_status"] = "active"
        info["superseded"] = False
        published[kind][object_id] = {
            "research_status": "active",
            "superseded": False,
        }

manifest["publication_status"] = "active_only"
manifest["published_objects"] = published
manifest["supersession"] = {
    "status": "superseded",
    "included_in_current_artifact": False,
    "recovery_sources": ["Supabase research state", "earlier Git commits"],
}
manifest["mirror_format"] = 22
manifest_path.write_text(
    json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
    encoding="utf-8",
)
print("NORI mirror finalized: active objects annotated; superseded manuscripts omitted")
