#!/usr/bin/env python3
"""Audit anchored projective-turn incidence in dimensions 3--6.

Standalone Python (standard library). The mathematical argument is dimension-uniform.
"""
from collections import Counter, defaultdict
from itertools import permutations
from math import factorial
from random import Random

def proj(x, n):
    return min(x, x ^ ((1 << n) - 1))

def orbit(x, i, n):
    x &= ~(1 << i)
    y = (x ^ ((1 << n) - 1)) & ~(1 << i)
    return i, min(x, y)

def supports(n):
    found = {}
    for x in range(1 << n):
        for p in permutations(range(n)):
            v = x
            E, T = [], []
            for k, i in enumerate(p):
                E.append(orbit(v, i, n))
                T.append((proj(v, n), tuple(sorted((p[k - 1], i)))))
                v ^= 1 << i
            key = frozenset(E)
            ts = frozenset(T)
            assert len(key) == len(ts) == n
            if key in found:
                assert found[key] == ts
            else:
                found[key] = ts
    assert len(found) == (1 << (n - 2)) * factorial(n - 1)
    return found

def multiplicity(e, t, n):
    i, x = e
    y, (j, k) = t
    if y in (proj(x, n), proj(x ^ (1 << i), n)):
        return factorial(n - 2) if i in (j, k) else 0
    if i in (j, k):
        return 0
    y = y if (y >> i) & 1 else y ^ ((1 << n) - 1)
    S = y ^ x ^ (1 << i)
    assert ((S >> i) & 1) == 0
    a = S.bit_count()
    if not 1 <= a <= n - 2 or ((S >> j) & 1) == ((S >> k) & 1):
        return 0
    return factorial(a - 1) * factorial(n - 2 - a)

def verify(n):
    O = supports(n)
    edges = sorted(set().union(*O.keys()))
    turns = sorted(set().union(*O.values()))
    incidence = defaultdict(int)
    for E, T in O.items():
        for e in E:
            for t in T:
                incidence[e, t] += 1
    assert len(edges) == n * 2 ** (n - 2)
    for e in edges:
        assert sum(incidence[e, t] for t in turns) == n * factorial(n - 1)
        for t in turns:
            assert incidence[e, t] == multiplicity(e, t, n), (n, e, t)

    rng = Random(n * 67)
    for _ in range(5):
        bits = {e: rng.randrange(2) for e in edges}
        def color(x, i):
            e = orbit(x, i, n)
            base = x & ~(1 << i)
            return bits[e] ^ (base != e[1])
        def change(t):
            y, (i, j) = t
            return int(color(y, i) != color(y, j))
        energy = {E: 2 * sum(change(t) for t in T) for E, T in O.items()}
        for e in edges:
            anchored = sum(multiplicity(e, t, n) * change(t) for t in turns)
            assert 2 * anchored == sum(v for E, v in energy.items() if e in E)
            assert sum(v for E, v in energy.items() if e not in E) == sum(energy.values()) - 2 * anchored
    print("Q%d: %d supports, %d orbits, %d turns; all incidence pairs checked" %
          (n, len(O), len(edges), len(turns)))

def balanced_five_cube():
    n = 5
    O = supports(n)
    def c(x, i):
        if i == 0:
            return (x >> 1) & 1
        if i == 1:
            return 1 ^ (x & 1)
        return (x & 1) if i % 2 == 0 else (1 ^ (x & 1))
    def T(turns):
        return 2 * sum(c(y, i) != c(y, j) for y, (i, j) in turns)
    e = (4, 6)
    total = Counter(T(V) for V in O.values())
    inside = Counter(T(V) for E, V in O.items() if e in E)
    outside = Counter(T(V) for E, V in O.items() if e not in E)
    assert total == {2: 32, 6: 128, 10: 32}
    assert inside == {6: 18, 10: 6}
    assert outside == {2: 32, 6: 110, 10: 26}
    print("Balanced Q5: full mean=6; conditioned mean=7; avoidance mean=41/7.")

if __name__ == "__main__":
    for n in (3, 4, 5, 6):
        verify(n)
    balanced_five_cube()
