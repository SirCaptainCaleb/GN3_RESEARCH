#!/usr/bin/env python3
"""Rank accepted archaeology theorems as possible reusable Spare Parts.

Input:
  1. SEARCH_CORPUS.md
  2. phrase_promotion_candidates.csv produced by a7c3_phrase_miner.py

This is discovery tooling only. A high score is not an audit or a publication
verdict. Human theorem archaeology is still required before promotion.
"""
from __future__ import annotations

import argparse
import csv
import html
import math
import re
from collections import defaultdict
from pathlib import Path

FILE_RE = re.compile(r"^# FILE: (.+?)\s*$", re.M)
TOKEN_RE = re.compile(r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*|\d+(?:\.\d+)?")

AMBIENT = {
    "strong level-1", "exact two-cover", "tight path", "hamilton path",
    "spanning two-cover", "tight trimer", "boundary antisymmetry",
    "smallest strong level-1 counterexample",
    "hypothetical smallest strong level-1 counterexample",
    "hypothetical smallest", "exact cover", "smallest counterexample",
    "boundary tournament", "closes h", "two-cover of h", "proper tight",
    "tight hamilton", "strong level-1 boundary tournament", "distinct vertices",
}


def parse_documents(text: str):
    ms = list(FILE_RE.finditer(text))
    for i, m in enumerate(ms):
        end = ms[i + 1].start() if i + 1 < len(ms) else len(text)
        yield m.group(1).strip(), text[m.end():end]


def clean(s: str) -> str:
    s = html.unescape(s)
    s = re.sub(r"```.*?```", " ", s, flags=re.S)
    s = re.sub(r"<!--.*?-->", " ", s, flags=re.S)
    s = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", s)
    s = s.replace("–", "-").replace("—", "-").replace("−", "-")
    s = re.sub(r"level\s*-?\s*\(\s*(\d+)\s*\)", r"level-\1", s, flags=re.I)
    return s.lower()


def segments(s: str):
    for chunk in re.split(r"[\n\r.!?;:]+", s):
        toks = TOKEN_RE.findall(chunk)
        if toks:
            yield toks


def section(body: str, heading: str) -> str:
    m = re.search(
        rf"^##\s+{re.escape(heading)}\s*$\n(.*?)(?=^##\s+|\Z)",
        body,
        flags=re.M | re.S,
    )
    return m.group(1).strip() if m else ""


def load_phrase_weights(path: Path, n_docs: int):
    out = {}
    with path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            phrase = row["phrase"]
            df = int(row["document_frequency"])
            tf = int(row["total_frequency"])
            assoc = float(row["association"])
            entropy = float(row["boundary_entropy"])
            n = int(row["n"])
            if df < 8 or df > 0.25 * n_docs or assoc < 1.30 or phrase in AMBIENT:
                continue
            idf = math.log((n_docs + 1) / (df + 1))
            weight = idf * math.log1p(tf) * assoc * entropy * (1 + 0.12 * (n - 2))
            out[tuple(phrase.split())] = weight
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("corpus", type=Path)
    ap.add_argument("phrase_candidates", type=Path)
    ap.add_argument("--out", type=Path, default=Path("portable_source_candidates.csv"))
    args = ap.parse_args()

    docs = list(parse_documents(args.corpus.read_text(encoding="utf-8")))
    weights = load_phrase_weights(args.phrase_candidates, len(docs))
    wanted = set(weights)
    rows = []

    for path, body in docs:
        if "/ARCHAEOLOGY/RESULTS/USABLE/ACTIVE/" not in path:
            continue

        found = set()
        token_count = 0
        for toks in segments(clean(body)):
            token_count += len(toks)
            for n in range(2, 7):
                for i in range(max(0, len(toks) - n + 1)):
                    ng = tuple(toks[i:i+n])
                    if ng in wanted:
                        found.add(ng)
        if not found:
            continue

        signals = sorted(((weights[x], " ".join(x)) for x in found), reverse=True)
        mechanism_score = sum(w for w, _ in signals[:30]) / max(1.0, math.log2(16 + token_count))

        hypotheses = section(body, "Hypotheses").lower()
        scope = section(body, "Scope").lower()
        proof = section(body, "Proof")
        refs = set(re.findall(r"\bR\d+\b", section(body, "Hypotheses") + " " + proof))
        smallest_hyp = "smallest" in hypotheses and "counterexample" in hypotheses
        order_free = "order-free" in scope or "order free" in scope
        broad_no_smallest = (
            "no smallest-counterexample" in scope
            or "no smallest counterexample" in scope
            or ("smallest-counterexample" in scope and "not used" in scope)
        )
        generic = any(x in scope for x in ("generic", "combinatorial parent", "universal", "pure "))
        proof_words = len(re.findall(r"\b\w+\b", proof))

        multiplier = 1.0
        if order_free:
            multiplier *= 1.45
        if broad_no_smallest:
            multiplier *= 1.25
        if generic:
            multiplier *= 1.12
        if smallest_hyp:
            multiplier *= 0.48
        multiplier /= 1 + 0.10 * len(refs)
        multiplier /= 1 + 0.00035 * max(0, proof_words - 650)
        portability_score = mechanism_score * multiplier

        title_m = re.search(r"^#\s+(.+?)\s*$", body, flags=re.M)
        title = title_m.group(1) if title_m else Path(path).name
        rows.append((
            portability_score, mechanism_score, path, title, len(refs),
            smallest_hyp, order_free, proof_words,
            " | ".join(p for _, p in signals[:8]),
        ))

    rows.sort(key=lambda r: (-r[0], -r[1], r[2]))
    with args.out.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow([
            "rank", "portability_score", "mechanism_score", "path", "title",
            "dependency_count", "smallest_counterexample_hypothesis",
            "order_free_scope", "proof_words", "top_signals",
        ])
        for i, row in enumerate(rows, 1):
            w.writerow([i, f"{row[0]:.3f}", f"{row[1]:.3f}", *row[2:]])

    for i, row in enumerate(rows[:30], 1):
        print(f"{i:2d}. {row[3][:70]:70s} portable={row[0]:8.2f}")


if __name__ == "__main__":
    main()
