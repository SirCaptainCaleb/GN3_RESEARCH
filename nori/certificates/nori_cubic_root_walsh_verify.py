#!/usr/bin/env python3
"""Independent certificate: Q7 cubic root-Walsh forcing beyond two moments."""
from collections import Counter
from fractions import Fraction as F
from math import factorial

n = 7
order = tuple(range(n))
S = (1 << 1) | (1 << 2)
R = (1 << 3) | (1 << 4)

def c(x, i):
    return (x >> ((i + 1) % n)) & 1

def grade(root):
    x = root
    word = []
    for i in order:
        word.append(c(x, i))
        x ^= 1 << i
    return (sum(word[t] != word[t + 1] for t in range(n - 1))
            + (word[-1] == word[0]))

values = [grade(x) for x in range(1 << (n - 1))]
hist = Counter(values)
assert hist == {1: 7, 3: 35, 5: 21, 7: 1}, hist

def hat(mask):
    return F(sum((-1) ** (x & mask).bit_count() * y
                 for x, y in enumerate(values)), len(values))

mean = hat(0)
variance = F(sum(y * y for y in values), len(values)) - mean * mean
m, a, b, d = mean - 3, hat(S), hat(R), hat(S ^ R)
det = m ** 3 - m * (a*a + b*b + d*d) + 2*a*b*d
assert (mean, variance) == (F(7, 2), F(7, 4))
assert (m, a, b, d, det) == (F(1,2), F(-1,2), F(-1,2),
                              F(0), F(-1,8))
assert variance == (mean - 3) * (7 - mean)
support_counts = {g: factorial(n - 1) * v // 2 for g, v in hist.items()}
assert sum(support_counts.values()) == (1 << (n - 2)) * factorial(n - 1)
print("Q7 folded-root grade histogram:", sorted(hist.items()))
print("Q7 projective-support grade histogram:", sorted(support_counts.items()))
print("root Walsh (m,a,b,d):", m, a, b, d)
print("cubic principal minor determinant:", det)
print("mean and variance:", mean, variance)
