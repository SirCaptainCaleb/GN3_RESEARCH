#!/usr/bin/env python3
"""NORI1 zero-frequency turn Gram theorem: explicit seven-cube certificate.

Run: python scripts/nori_zero_mode_spectral_certificate.py
Pure Python 3.10+, no dependencies.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations

n = 7
full = (1 << n) - 1
masks = (8, 8, 8, 1, 1, 1, 1)
offsets = (0, 0, 0, 0, 0, 0, 1)
flipped = {0, 1 << 3, full, full ^ (1 << 3)}

def c(i, x):
    bit = ((masks[i] & x).bit_count() % 2) ^ offsets[i]
    if i == 3 and x in flipped:
        bit ^= 1
    return bit

# Verify the two legal coloring identities directly.
for x in range(1 << n):
    for i in range(n):
        assert c(i, x) == c(i, x ^ (1 << i))
        assert c(i, x) == 1 - c(i, x ^ full)

pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
p = {
    (i, j): Fraction(sum(c(i, x) != c(j, x) for x in range(1 << n)), 1 << n)
    for i, j in pairs
}
R = sum(p.values())
d = [sum(value for (i, j), value in p.items() if i == a or j == a)
     for a in range(n)]
z = [(di - R / (n - 1)) / (n - 2) for di in d]
residual_squared = sum((value - z[i] - z[j]) ** 2
                       for (i, j), value in p.items())

signed_square = Fraction(
    sum((n - 2 * sum(c(i, x) for i in range(n))) ** 2
        for x in range(1 << n)),
    1 << n
)
mu = (n * n - signed_square) / (n - 1)
lower_variance = Fraction(8, n - 1) * residual_squared
no_witness_upper = (2 * n - mu) * (mu - 6)
witness_lower = (lower_variance - no_witness_upper) / (8 * (n - 1))

assert signed_square == Fraction(103, 8)
assert mu == Fraction(289, 48) > 6
assert residual_squared == Fraction(8753, 7680)
assert lower_variance == Fraction(8753, 5760)
assert no_witness_upper == Fraction(383, 2304)
assert witness_lower == Fraction(5197, 184320) > 0

# Independently enumerate rooted paths. Each coherent support is represented
# 2n times when roots range over one representative of each antipodal vertex pair.
rooted_hist = Counter()
for x in range(1 << (n - 1)):
    for pi in permutations(range(n)):
        y = x
        word = []
        for i in pi:
            word.append(c(i, y))
            y ^= 1 << i
        switches = sum(word[k] != word[k + 1] for k in range(n - 1))
        switches += (word[-1] == word[0])
        rooted_hist[2 * switches] += 1

hist = {turns: count // (2 * n) for turns, count in rooted_hist.items()}
assert all(v % (2 * n) == 0 for v in rooted_hist.values())
assert hist == {2: 3944, 6: 15160, 10: 3808, 14: 128}
M = (1 << (n - 2)) * 720
assert sum(hist.values()) == M == 23040
assert hist[2] >= (M * witness_lower).__ceil__() == 650

print("Legal coloring verified.")
print("Mean cyclic turn energy:", mu)
print("Direction-pair residual squared:", residual_squared)
print("Variance lower bound:", lower_variance)
print("No-witness variance upper bound:", no_witness_upper)
print("Certified good-support fraction:", witness_lower)
print("Certified good-support count: at least", (M * witness_lower).__ceil__())
print("Enumerated support histogram:", hist)
