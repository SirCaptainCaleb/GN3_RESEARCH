#!/usr/bin/env python3
"""Exhaustive audit of the fixed-facet bridge-affinity theorem in Q4.

Uses only the Python standard library. All 4,096 arbitrary facet colorings
and 16 legal bridge assignments per facet are tested.
"""
from itertools import permutations


def verify():
    d = 3
    n = 1 << d
    top = n - 1
    eidx = {}
    for i in range(d):
        for x in range(n):
            if not (x >> i) & 1:
                eidx[x, i] = eidx[x ^ (1 << i), i] = len(set(eidx.values()))
    assert len(set(eidx.values())) == 12
    root_pairs = [(x, x ^ top) for x in range(n // 2)]
    orders = list(permutations(range(d)))
    paths = []
    for x in range(n):
        for pi in orders:
            y = x
            edges = []
            for i in pi:
                edges.append(eidx[y, i])
                y ^= 1 << i
            paths.append((x, edges))
    observed = 0
    for mask in range(1 << 12):
        colors = [(mask >> i) & 1 for i in range(12)]
        nplus = [0] * n
        for x, edges in paths:
            w = [colors[i] for i in edges]
            nplus[x] += all(w[k] <= w[k + 1] for k in range(d - 1))
        paired = sum(nplus[x] > 0 and nplus[barx] > 0
                     for x, barx in root_pairs)
        singly = sum((nplus[x] > 0) != (nplus[barx] > 0)
                     for x, barx in root_pairs)
        bad_count = 0
        for gmask in range(1 << (n // 2)):
            predicted = sum(nplus[x] if not ((gmask >> k) & 1)
                            else nplus[barx]
                            for k, (x, barx) in enumerate(root_pairs))
            direct = 0
            for k, (x, _) in enumerate(root_pairs):
                g = (gmask >> k) & 1
                for pi in orders:
                    y = x
                    word = [g]
                    for i in pi:
                        word.append(colors[eidx[y, i]])
                        y ^= 1 << i
                    turns = sum(word[j] != word[j + 1]
                                for j in range(d))
                    turns += word[-1] != (1 - word[0])
                    direct += turns == 1
            assert direct == predicted, (mask, gmask)
            bad_count += direct == 0
            observed += 1
        predicted_bad = 0 if paired else (1 << (n // 2 - singly))
        assert bad_count == predicted_bad, mask
    print("PASS:", observed, "legal Q4 colorings; full support count agrees.")
    print("PASS: bad-extension subcube enumeration for each arbitrary facet.")


if __name__ == "__main__":
    verify()
