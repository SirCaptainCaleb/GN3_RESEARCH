#!/usr/bin/env python3
"""Build a single mechanically searchable text corpus from A7C3 source files."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
A7C3 = ROOT / "A7C3"
OUTPUT = A7C3 / "SEARCH_CORPUS.md"
INCLUDE_SUFFIXES = {".md", ".txt"}


def included_files() -> list[Path]:
    files: list[Path] = []
    for path in A7C3.rglob("*"):
        if not path.is_file():
            continue
        if path == OUTPUT:
            continue
        if path.suffix.lower() not in INCLUDE_SUFFIXES:
            continue
        files.append(path)
    return sorted(files, key=lambda p: p.relative_to(ROOT).as_posix())


def main() -> None:
    files = included_files()
    parts = [
        "# A7C3 Search Corpus\n\n",
        "<!-- GENERATED FILE. DO NOT EDIT BY HAND. -->\n",
        "<!-- Source: all .md and .txt files under A7C3/, sorted by repository path. -->\n\n",
        f"Indexed source files: {len(files)}\n\n",
    ]

    for path in files:
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")
        parts.extend(
            [
                "\n\n---\n\n",
                f"# FILE: {rel}\n\n",
                f"<!-- BEGIN FILE: {rel} -->\n\n",
                text,
                "\n" if not text.endswith("\n") else "",
                f"\n<!-- END FILE: {rel} -->\n",
            ]
        )

    OUTPUT.write_text("".join(parts), encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)} from {len(files)} files")


if __name__ == "__main__":
    main()
