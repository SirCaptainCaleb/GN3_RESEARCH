#!/usr/bin/env python3
"""Finalize the NORI publication artifact without retaining superseded work."""
from __future__ import annotations

import json
import os
import shutil
from pathlib import Path


def main() -> None:
    if os.environ.get("RESEARCH_SCHEMA") != "nori":
        return

    root = Path(".mirror-stage/nori")
    manifest_path = root / "MANIFEST.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    # Superseded nodes, compositions, and tree entries are filtered by the
    # public mirror RPCs before the generator reads them. The generator's
    # legacy archive placeholder must never reach GitHub or the artifact.
    shutil.rmtree(root / "SUPERSEDED", ignore_errors=True)

    object_groups = {
        "articles": "article_versions",
        "sections": "section_versions",
        "subsections": "subsection_versions",
    }
    published = {}
    for label, key in object_groups.items():
        records = manifest.get(key, {})
        for record in records.values():
            record["research_status"] = "active"
            record["superseded"] = False
        published[label] = {
            object_id: {"research_status": "active", "superseded": False}
            for object_id in records
        }

    manifest["publication_status"] = "active_only"
    manifest["published_objects"] = published
    manifest["supersession"] = {
        "status": "superseded",
        "exported": False,
        "database_retention": "Supabase retains full manuscript and status",
        "historical_recovery": "earlier Git commits",
    }
    manifest["mirror_format"] = 22
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    if (root / "SUPERSEDED").exists():
        raise RuntimeError("Superseded archive must not be published")
    print("NORI artifact: active objects identified; superseded work omitted")


if __name__ == "__main__":
    main()
