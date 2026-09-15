#!/usr/bin/env python3
"""Mine reusable multiword phrases from the A7C3 SEARCH_CORPUS.

The miner is deliberately dependency-free. It ranks phrases primarily by document
frequency (how many source files use the phrase), then by total frequency.  A
second "promotion candidate" ranking suppresses near-duplicate subphrases and
weights phrase length/association slightly so that mathematical mechanisms rise
above boilerplate.
"""
from __future__ import annotations

import argparse
import csv
import html
import math
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

FILE_RE = re.compile(r"^# FILE: (.+?)\s*$", re.M)
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
CODE_FENCE_RE = re.compile(r"```.*?```", re.S)
LINK_RE = re.compile(r"\[([^\]]+)\]\([^\)]+\)")
# Domain-friendly tokenization. Hyphenated compounds remain one token.
TOKEN_RE = re.compile(r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*|\d+(?:\.\d+)?")

STOP = {
    "a","an","the","and","or","but","if","then","else","when","while","for","of","on","in","to","from","by","with","without","at","as","is","are","was","were","be","been","being","it","its","this","that","these","those","there","here","we","our","their","they","them","he","she","his","her","you","your","i","me","my","so","thus","hence","therefore","because","since","such","any","all","each","every","some","one","two","three","four","five","six","can","cannot","could","would","should","may","might","must","will","do","does","did","not","no","yes","than","into","onto","over","under","between","among","through","along","around","before","after","above","below","same","other","another","both","either","neither","more","less","most","least","only","also","already","still","now","new","old","first","second","later","earlier","exactly","indeed","namely","where","which","who","whose","what","why","how","let","lets","given","suppose","assume","have","has","had","having","get","gets","got","make","makes","made","take","takes","taken","using","use","used","via","within","outside","inside","up","down","out","off","per","etc"
}

# Terms that appear because archived results share a document template. These
# are not banned internally, but phrases made entirely of them are discarded.
TEMPLATE = {
    "statement","hypotheses","scope","applicability","persistence","exclusions",
    "nonclaims","nonclaim","proof","provenance","result","results","remark",
    "remarks","discussion","conclusion","corollary","lemma","theorem","definition",
    "accepted","audited","audit","historical","workspace","engine","engines",
}

# Corpus bookkeeping labels repeated across hundreds of archaeology records. They
# are useful metadata, but not mathematical phrase candidates.
METADATA = {
    "record", "records", "note", "notes", "status", "review", "lifecycle",
    "curation", "migration", "legacy", "usable", "unusable", "invalid", "quarantined",
    "targeted", "pending", "pass", "adjusted", "superseded", "archive",
    "archaeology", "source", "file", "files", "created", "updated",
}
METADATA_BIGRAMS = {
    ("record", "notes"), ("record", "status"), ("review", "status"),
    ("review", "note"), ("lifecycle", "note"), ("curation", "note"),
    ("usable", "legacy"), ("apply", "accepted"),
}

GENERIC_CONTENT = STOP | TEMPLATE | {
    "case","cases","claim","claims","argument","condition","conditions","property",
    "properties","construction","constructions","output","outputs","input","inputs",
    "object","objects","vertex","vertices","edge","edges","path","paths","set","sets",
}

@dataclass(frozen=True)
class Row:
    phrase: str
    n: int
    df: int
    tf: int
    doc_pct: float
    association: float
    boundary_entropy: float
    score: float
    samples: tuple[str, ...]


def parse_documents(text: str) -> list[tuple[str, str]]:
    matches = list(FILE_RE.finditer(text))
    docs: list[tuple[str, str]] = []
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        docs.append((m.group(1).strip(), text[start:end]))
    return docs


def clean_text(s: str) -> str:
    s = html.unescape(s)
    s = CODE_FENCE_RE.sub(" ", s)
    s = HTML_COMMENT_RE.sub(" ", s)
    s = LINK_RE.sub(r"\1", s)
    # Normalize frequent notation variants without attempting semantic rewriting.
    s = s.replace("–", "-").replace("—", "-").replace("−", "-")
    s = re.sub(r"level\s*-?\s*\(\s*(\d+)\s*\)", r"level-\1", s, flags=re.I)
    s = re.sub(r"\b([a-z]+)\s*-\s*([a-z]+)\b", r"\1-\2", s, flags=re.I)
    # Keep sentence/line boundaries. We do not form phrases across them.
    return s.lower()


def segments(s: str) -> Iterable[list[str]]:
    # Hard breaks on prose punctuation, markdown headings/lists, and line breaks.
    for chunk in re.split(r"[\n\r.!?;:]+", s):
        toks = TOKEN_RE.findall(chunk)
        if toks:
            yield toks


def informative(ng: tuple[str, ...]) -> bool:
    if len(ng) < 2:
        return False
    if ng[0] in STOP or ng[-1] in STOP:
        return False
    if all(t in STOP for t in ng):
        return False
    # Reject pure template/generic prose but allow domain phrases such as
    # "tight path" and "source vertex" even though path/vertex are generic.
    if all(t in GENERIC_CONTENT for t in ng):
        return False
    # Strip archaeology/template labels from the discovery surface.
    if any(bg in METADATA_BIGRAMS for bg in zip(ng, ng[1:])):
        return False
    if all(t in (GENERIC_CONTENT | METADATA) for t in ng):
        return False
    # Pure symbolic-variable juxtapositions ("u v", "b c", ...) are common in
    # formulas but carry no reusable phrase semantics. Require at least one
    # lexical token of length >= 3 or a hyphenated compound.
    if not any(len(t) >= 3 or "-" in t for t in ng):
        return False
    if sum(any(c.isalpha() for c in t) for t in ng) < 2:
        return False
    # IDs and version-like fragments are provenance, not reusable mathematics.
    if any(re.fullmatch(r"[rdegso]\d+", t) for t in ng):
        return False
    return True


def association_score(ng: tuple[str, ...], unigram: Counter[str], total_tokens: int, tf: int) -> float:
    """Geometric mean pairwise normalized PMI, mapped to a stable positive scale."""
    if len(ng) < 2 or tf <= 0:
        return 0.0
    vals = []
    for a, b in zip(ng, ng[1:]):
        # Approximate pair probability by phrase frequency for stability. This is
        # intentionally conservative: common lexicalized phrases receive >1,
        # accidental juxtapositions stay near 1 or below.
        pa = unigram[a] / total_tokens
        pb = unigram[b] / total_tokens
        pab = tf / total_tokens
        pmi = math.log((pab + 1e-12) / (pa * pb + 1e-12))
        vals.append(max(-4.0, min(8.0, pmi)))
    mean = sum(vals) / len(vals)
    return max(0.05, 1.0 + mean / 8.0)


def entropy(counter: Counter[str]) -> float:
    total = sum(counter.values())
    if total <= 1:
        return 0.0
    return -sum((c/total) * math.log(c/total) for c in counter.values() if c)


def boundary_entropies(docs: list[tuple[str, str]], candidates: set[tuple[str, ...]], min_n: int, max_n: int) -> dict[tuple[str, ...], float]:
    """Return geometric mean of left/right context entropy for candidate phrases.

    Phrase-mining literature often uses branching entropy to distinguish complete
    lexical units from fragments. For example, if `proper tight` is almost
    always followed by `cycle`, its right entropy is low; `proper tight cycle`
    generally has more varied neighbors and scores as the more complete phrase.
    """
    left: dict[tuple[str, ...], Counter[str]] = defaultdict(Counter)
    right: dict[tuple[str, ...], Counter[str]] = defaultdict(Counter)
    for _, body in docs:
        for toks in segments(clean_text(body)):
            L = len(toks)
            for n in range(min_n, max_n + 1):
                if L < n:
                    continue
                for i in range(L - n + 1):
                    ng = tuple(toks[i:i+n])
                    if ng not in candidates:
                        continue
                    left[ng][toks[i-1] if i else "<B>"] += 1
                    right[ng][toks[i+n] if i+n < L else "<B>"] += 1
    return {
        ng: math.sqrt((1.0 + entropy(left[ng])) * (1.0 + entropy(right[ng])))
        for ng in candidates
    }


def is_contiguous_subphrase(short: tuple[str, ...], long: tuple[str, ...]) -> bool:
    if len(short) >= len(long):
        return False
    n = len(short)
    return any(long[i:i+n] == short for i in range(len(long)-n+1))


def mine(docs: list[tuple[str, str]], min_n: int, max_n: int, min_df: int) -> tuple[list[Row], list[Row]]:
    tf: Counter[tuple[str, ...]] = Counter()
    df: Counter[tuple[str, ...]] = Counter()
    unigram: Counter[str] = Counter()
    sample_files: dict[tuple[str, ...], list[str]] = defaultdict(list)
    total_tokens = 0

    for path, body in docs:
        seen: set[tuple[str, ...]] = set()
        cleaned = clean_text(body)
        for toks in segments(cleaned):
            unigram.update(toks)
            total_tokens += len(toks)
            L = len(toks)
            for n in range(min_n, max_n + 1):
                if L < n:
                    continue
                for i in range(L - n + 1):
                    ng = tuple(toks[i:i+n])
                    if not informative(ng):
                        continue
                    tf[ng] += 1
                    seen.add(ng)
        for ng in seen:
            df[ng] += 1
            if len(sample_files[ng]) < 4:
                sample_files[ng].append(path)

    eligible = {ng for ng, d in df.items() if d >= min_df}
    b_entropy = boundary_entropies(docs, eligible, min_n, max_n)

    rows: list[Row] = []
    N = len(docs)
    for ng in eligible:
        d = df[ng]
        f = tf[ng]
        assoc = association_score(ng, unigram, max(1, total_tokens), f)
        complete = b_entropy.get(ng, 1.0)
        # Primary ubiquity is document frequency. tf, lexical association, phrase
        # completeness (branching entropy), and length only rank candidates.
        score = d * math.log1p(f) * (1.0 + 0.10 * (len(ng) - min_n)) * assoc * complete
        rows.append(Row(
            phrase=" ".join(ng), n=len(ng), df=d, tf=f,
            doc_pct=100.0*d/N, association=assoc, boundary_entropy=complete, score=score,
            samples=tuple(sample_files[ng]),
        ))

    raw = sorted(rows, key=lambda r: (-r.df, -r.tf, -r.n, r.phrase))

    # Redundancy suppression: keep the longer phrase when it accounts for nearly
    # all uses of a shorter one. This makes the candidate list read like concepts.
    by_ng = {tuple(r.phrase.split()): r for r in rows}
    ordered = sorted(by_ng.items(), key=lambda kv: (-kv[1].score, -kv[1].df, -kv[1].n))[:5000]
    kept: list[Row] = []
    kept_ng: list[tuple[str, ...]] = []
    for ng, r in ordered:
        redundant = False
        for lng, lr in zip(kept_ng, kept):
            if is_contiguous_subphrase(ng, lng):
                if lr.df >= 0.78 * r.df and lr.tf >= 0.60 * r.tf:
                    redundant = True
                    break
        if not redundant:
            kept_ng.append(ng)
            kept.append(r)
    candidates = sorted(kept, key=lambda r: (-r.score, -r.df, -r.tf))
    return raw, candidates


def write_csv(path: Path, rows: list[Row], limit: int | None = None) -> None:
    use = rows if limit is None else rows[:limit]
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["rank","phrase","n","document_frequency","total_frequency","document_percent","association","boundary_entropy","candidate_score","sample_files"])
        for i, r in enumerate(use, 1):
            w.writerow([i, r.phrase, r.n, r.df, r.tf, f"{r.doc_pct:.2f}", f"{r.association:.4f}", f"{r.boundary_entropy:.4f}", f"{r.score:.3f}", " | ".join(r.samples)])


def write_compact_csv(path: Path, rows: list[Row]) -> None:
    """Write the complete objective common-to-least ranking in compact form."""
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["rank", "phrase", "files", "uses"])
        for i, r in enumerate(rows, 1):
            w.writerow([i, r.phrase, r.df, r.tf])


def write_markdown(path: Path, raw: list[Row], candidates: list[Row], n_docs: int, top: int) -> None:
    def table(rows: list[Row], n: int) -> str:
        out = ["| Rank | Phrase | Files | Uses | File % | Score |", "|---:|---|---:|---:|---:|---:|"]
        for i, r in enumerate(rows[:n], 1):
            p = r.phrase.replace("|", "\\|")
            out.append(f"| {i} | `{p}` | {r.df} | {r.tf} | {r.doc_pct:.1f}% | {r.score:.1f} |")
        return "\n".join(out)

    text = f"""# A7C3 Phrase-Mining Report\n\nCorpus documents: **{n_docs}**. Phrases are 2-6 token exact normalized n-grams.\n\nThe **raw ubiquity ranking** is sorted by number of distinct source files containing the phrase, then by total occurrences. The **promotion-candidate ranking** uses the same counts but suppresses near-duplicate subphrases and lightly rewards longer, strongly associated, phrase-complete expressions. Phrase completeness is estimated with left/right branching entropy, a standard way to demote fragments such as `proper tight` when a longer expression such as `proper tight cycle` carries the stable boundary. Frequency is a discovery signal, **not** evidence that a result is true, audited, reusable, or suitable for `SPARE_PARTS/`.\n\n## Most ubiquitous phrases\n\n{table(raw, top)}\n\n## Promotion candidates\n\n{table(candidates, top)}\n\n## Interpretation\n\nUse this report as a triage map. For a high-ranking mathematical phrase, search the archaeology for the strongest accepted general theorem carrying that mechanism, verify that it is genuinely reusable and not already owned by a surviving Engine, and only then rescue it as a Spare Part. Template language and broad ambient terminology may rank highly merely because the corpus is homogeneous.\n"""
    path.write_text(text, encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("corpus", type=Path)
    ap.add_argument("--out-dir", type=Path, default=Path("."))
    ap.add_argument("--min-n", type=int, default=2)
    ap.add_argument("--max-n", type=int, default=6)
    ap.add_argument("--min-df", type=int, default=5)
    ap.add_argument("--top", type=int, default=100)
    args = ap.parse_args()

    docs = parse_documents(args.corpus.read_text(encoding="utf-8"))
    raw, candidates = mine(docs, args.min_n, args.max_n, args.min_df)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    write_csv(args.out_dir / "phrase_ranking.csv", raw)
    write_compact_csv(args.out_dir / "phrase_ranking_compact.csv", raw)
    write_csv(args.out_dir / "phrase_promotion_candidates.csv", candidates)
    write_markdown(args.out_dir / "phrase_report.md", raw, candidates, len(docs), args.top)
    print(f"documents={len(docs)} raw_phrases={len(raw)} candidates={len(candidates)}")
    print("\nTop promotion candidates:")
    for i, r in enumerate(candidates[:30], 1):
        print(f"{i:2d}. {r.phrase:55s} df={r.df:4d} tf={r.tf:5d} score={r.score:9.1f}")

if __name__ == "__main__":
    main()
