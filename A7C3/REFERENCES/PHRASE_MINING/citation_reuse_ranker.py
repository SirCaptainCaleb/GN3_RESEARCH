#!/usr/bin/env python3
"""Rank active archaeology results by distinct-file inbound reuse.

The A7C3 corpus contains an implicit theorem-dependency graph through R<number>
references. This script counts how many *different source files* cite each active
result. The output is a discovery signal for reusable theorem parents, not an
audit or automatic Spare-Part promotion rule.
"""
from __future__ import annotations

import argparse
import csv
import re
from collections import defaultdict
from pathlib import Path

FILE_RE = re.compile(r"^# FILE: (.+?)\s*$", re.M)
R_REF_RE = re.compile(r"\bR\d+\b")
ACTIVE_RE = re.compile(r"/ARCHAEOLOGY/RESULTS/USABLE/ACTIVE/(R\d+)\.md$")


def parse_documents(text: str):
    matches = list(FILE_RE.finditer(text))
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        yield m.group(1).strip(), text[m.end():end]


def section(body: str, heading: str) -> str:
    m = re.search(
        rf"^##\s+{re.escape(heading)}\s*$\n(.*?)(?=^##\s+|\Z)",
        body,
        flags=re.M | re.S,
    )
    return m.group(1).strip() if m else ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("corpus", type=Path)
    ap.add_argument("--out", type=Path, default=Path("citation_reuse_rank.csv"))
    args = ap.parse_args()

    docs = list(parse_documents(args.corpus.read_text(encoding="utf-8")))

    active = {}
    for path, body in docs:
        m = ACTIVE_RE.search(path)
        if not m:
            continue
        rid = m.group(1)
        tm = re.search(r"^#\s+(.+?)\s*$", body, flags=re.M)
        active[rid] = {
            "path": path,
            "title": tm.group(1).strip() if tm else rid,
            "body": body,
        }

    inbound = defaultdict(set)
    for path, body in docs:
        for rid in set(R_REF_RE.findall(body)):
            if rid in active and path != active[rid]["path"]:
                inbound[rid].add(path)

    rows = []
    for rid, rec in active.items():
        body = rec["body"]
        hypotheses = section(body, "Hypotheses").lower()
        scope = section(body, "Scope").lower()
        proof = section(body, "Proof")
        direct_refs = set(R_REF_RE.findall(section(body, "Hypotheses") + " " + proof)) - {rid}
        smallest = "smallest" in hypotheses and "counterexample" in hypotheses
        order_free = "order-free" in scope or "order free" in scope
        proof_words = len(re.findall(r"\b\w+\b", proof))
        rows.append({
            "rid": rid,
            "title": rec["title"],
            "path": rec["path"],
            "inbound_documents": len(inbound[rid]),
            "direct_dependency_count": len(direct_refs),
            "smallest_counterexample_hypothesis": smallest,
            "order_free_scope": order_free,
            "proof_words": proof_words,
        })

    rows.sort(key=lambda r: (-r["inbound_documents"], r["rid"]))
    with args.out.open("w", newline="", encoding="utf-8") as f:
        fields = [
            "rank", "rid", "title", "inbound_documents", "path",
            "direct_dependency_count", "smallest_counterexample_hypothesis",
            "order_free_scope", "proof_words",
        ]
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for rank, row in enumerate(rows, 1):
            w.writerow({"rank": rank, **row})

    for rank, row in enumerate(rows[:40], 1):
        print(
            f"{rank:2d}. {row['rid']:>5}  cites={row['inbound_documents']:>3}  "
            f"deps={row['direct_dependency_count']:>2}  "
            f"{row['title'][:82]}"
        )


if __name__ == "__main__":
    main()
