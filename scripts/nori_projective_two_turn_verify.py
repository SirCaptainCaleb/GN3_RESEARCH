#!/usr/bin/env python3
"""Projective two-turn incidence, cyclic moments and Fourier spectra for NORI1.

Run: python nori_projective_two_turn_verify.py
Requires Python 3.10+, numpy and sympy.
"""
import itertools
import math
import random
from collections import Counter
import sympy as sp

def project(x, n):
    return min(x, x ^ ((1 << n) - 1))

def support(x, order, n):
    v = x
    result = []
    for pos, i in enumerate(order):
        result.append((project(v, n), tuple(sorted((order[pos - 1], i)))))
        v ^= 1 << i
    return frozenset(result)

def all_supports(n):
    return set(support(x, p, n) for x in range(1 << n)
               for p in itertools.permutations(range(n)))

def multiplicity(n, t, u):
    x, first = t
    y, second = u
    if t == u:
        return math.factorial(n - 2)
    if x == y:
        return 0
    shared = set(first) & set(second)
    if len(shared) == 2:
        return 0
    if len(shared) == 1:
        h = next(iter(shared))
        return math.factorial(n - 3) if project(x ^ (1 << h), n) == y else 0
    i, j = first
    d = x ^ y
    if ((d >> i) & 1) == ((d >> j) & 1):
        return 0
    B = d if ((d >> j) & 1) else (d ^ ((1 << n) - 1))
    k, l = second
    if ((B >> k) & 1) == ((B >> l) & 1):
        return 0
    a = B.bit_count()
    return math.factorial(a - 2) * math.factorial(n - a - 2)

def legal_colors(n, seed):
    random.seed(seed)
    bits = {}
    top = (1 << n) - 1
    for x in range(1 << n):
        for i in range(n):
            e = min(x, x ^ (1 << i))
            if (i, e) not in bits:
                partner = min(e ^ top, (e ^ top) ^ (1 << i))
                b = random.getrandbits(1)
                bits[i, e], bits[i, partner] = b, b ^ 1
    return lambda x, i: bits[i, min(x, x ^ (1 << i))]

def check(n):
    os = all_supports(n)
    assert len(os) == 2 ** (n - 2) * math.factorial(n - 1)
    turns = sorted(set().union(*os))
    observed = Counter(tuple(sorted((t, u))) for o in os
                       for t, u in itertools.combinations_with_replacement(sorted(o), 2))
    for j, t in enumerate(turns):
        for u in turns[j:]:
            assert observed[t, u] == multiplicity(n, t, u), (n, t, u)
    for seed in range(3):
        c = legal_colors(n, seed)
        I = {t: int(c(t[0], t[1][0]) != c(t[0], t[1][1])) for t in turns}
        energies = [2 * sum(I[t] for t in o) for o in os]
        first = 2 * math.factorial(n - 2) * sum(
            sum(c(x, i) for i in range(n)) *
            (n - sum(c(x, i) for i in range(n)))
            for x in range(1 << (n - 1)))
        assert sum(energies) == first
        second = 4 * sum(
            multiplicity(n, t, u) * I[t] * I[u] * (1 if t == u else 2)
            for a, t in enumerate(turns) for u in turns[a:])
        assert second == sum(E * E for E in energies)
    print(f"Q{n}: {len(os)} supports, {len(turns)} turns, "
          f"{len(turns) * (len(turns) + 1) // 2} pair checks; moments pass")

def check_five_cube_spectrum():
    n = 5
    pairs = list(itertools.combinations(range(n), 2))
    expected = {
        0: {sp.Integer(0): 4, sp.Integer(6): 5, sp.Integer(30): 1},
        2: {sp.Integer(0): 2, sp.Integer(6): 2,
            10 - 4*sp.sqrt(5): 1, 10 + 4*sp.sqrt(5): 1,
            7 - sp.sqrt(17): 2, 7 + sp.sqrt(17): 2},
        4: {sp.Integer(0): 4, sp.Integer(6): 3, sp.Integer(14): 3},
    }
    for m in (0, 3, 15):
        K = sp.Matrix([[
            sum(multiplicity(n, (0, p), (y, q)) *
                (-1 if ((y & m).bit_count() % 2) else 1)
                for y in range(1 << (n - 1)))
            for q in pairs] for p in pairs])
        assert K.eigenvals() == expected[m.bit_count()]
    print("Q5 exact Fourier spectra pass: lambda5 = 10-4*sqrt(5) > 1")

if __name__ == "__main__":
    for dimension in (3, 4, 5, 6):
        check(dimension)
    check_five_cube_spectrum()
