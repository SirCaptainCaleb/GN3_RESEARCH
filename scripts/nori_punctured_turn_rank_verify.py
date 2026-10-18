#!/usr/bin/env python3
"""Binary-rank certificate for coherent-support turn incidence with one orbit removed.

Build one support per direction-0 orbit and order of remaining directions.
Rows are bitsets of projective turns. In characteristic 2 the computed ranks
give lower bounds for real ranks; combined with the theorem's upper bounds
they certify equality. Requires Python 3.10+ only.
"""
from itertools import permutations
from math import comb, factorial

def add_rank(basis, row):
    while row:
        k = row.bit_length() - 1
        if k in basis:
            row ^= basis[k]
        else:
            basis[k] = row
            return
def verify(n):
    top = (1 << n) - 1
    pv = lambda x: min(x, x ^ top)
    vertices = sorted(set(pv(x) for x in range(1 << n)))
    pairs = [(i,j) for i in range(n) for j in range(i+1,n)]
    vidx = {v:k for k,v in enumerate(vertices)}
    pidx = {p:k for k,p in enumerate(pairs)}
    nc = len(pairs)
    starts = [x for x in range(1<<n) if x%2==0
              and x <= ((x^top)&~1)]
    assert len(starts) == 2**(n-2)
    full, deleted = {}, {}
    for x in starts:
        for tail in permutations(range(1,n)):
            p = (0,)+tail
            cur = x
            mask = 0
            for k,i in enumerate(p):
                a,b = sorted((p[k-1],i))
                mask |= 1 << (vidx[pv(cur)]*nc + pidx[a,b])
                cur ^= 1<<i
            add_rank(full, mask)
            if x != starts[0]:
                add_rank(deleted, mask)
    total = 2**(n-2)*factorial(n-1)
    print("Q%d: %d supports, full rank %d, orbit-deleted rank %d"
          % (n,total,len(full),len(deleted)))
    if n >= 5:
        R = 2**(n-1)*comb(n,2)-n*2**(n-2)-(n-1)
        assert len(full)==R
        assert len(deleted)==R-(2*n-3)

if __name__ == "__main__":
    for n in (4,5,6,7):
        verify(n)
