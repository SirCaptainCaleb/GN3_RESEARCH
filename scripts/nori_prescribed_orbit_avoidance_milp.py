#!/usr/bin/env python3
"""Orbit-avoidance feasibility for legal NORI1 colorings.

Requires NumPy and SciPy (HiGHS backend). Run:
  python scripts/nori_prescribed_orbit_avoidance_milp.py 5 60

Status 2 (infeasible) proves: every legal Q_n coloring has a
monochromatic coherent support avoiding the fixed orbit (0,0).
Hypercube automorphisms make all fixed orbits equivalent.
"""
import sys
import itertools
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import lil_matrix

def project(x, n):
    return min(x, x ^ ((1 << n) - 1))

def orbit(x, i, n):
    a = x & ~(1 << i)
    b = (a ^ ((1 << n) - 1)) & ~(1 << i)
    return i, min(a, b)

def build(n):
    supports = {}
    for root in range(1 << n):
        for order in itertools.permutations(range(n)):
            x = root
            edges, turns = [], []
            for k, i in enumerate(order):
                edges.append(orbit(x, i, n))
                turns.append((project(x, n), tuple(sorted((order[k-1], i)))))
                x ^= 1 << i
            supports[frozenset(edges)] = frozenset(turns)

    edges = sorted(set().union(*supports.keys()))
    turns = sorted(set().union(*supports.values()))
    ei = {e:k for k,e in enumerate(edges)}
    ti = {t:k for k,t in enumerate(turns)}
    ne, nt = len(edges), len(turns)
    ns = len(supports)
    assert ns == 2**(n-2)*__import__("math").factorial(n-1)
    A = lil_matrix((nt+ns, ne+2*nt), dtype=np.float64)
    lower = np.zeros(nt+ns)
    upper = np.zeros(nt+ns)

    # For every turn t, variables x_e, x_f, y_t, h_t obey
    # y_t - x_e - x_f + 2 h_t = b_t (an XOR equation).
    for t,k in ti.items():
        vertex,(i,j) = t
        e = orbit(vertex,i,n)
        f = orbit(vertex,j,n)
        b = int((vertex & ~(1<<i)) != e[1]) ^ int(
            (vertex & ~(1<<j)) != f[1])
        A[k,ei[e]] = A[k,ei[f]] = -1
        A[k,ne+k] = 1
        A[k,ne+nt+k] = 2
        lower[k] = upper[k] = b

    selected_orbit = (0, 0)
    for z,(E,T) in enumerate(supports.items()):
        for t in T:
            A[nt+z,ne+ti[t]] = 1
        # The sum of projective turn changes is odd. Excluding
        # monochromatic support means this sum must be at least 3.
        lower[nt+z] = 3 if selected_orbit not in E else 1
        upper[nt+z] = n

    return A.tocsr(),lower,upper,ne,nt,ns

def solve(n, seconds=60):
    A,lower,upper,ne,nt,ns = build(n)
    nv = ne+2*nt
    print(f"n={n}; {ne} orbit colors, {nt} turns, {ns} supports; {nv} binary variables",flush=True)
    result = milp(np.zeros(nv), integrality=np.ones(nv),
        bounds=Bounds(np.zeros(nv),np.ones(nv)),
        constraints=LinearConstraint(A,lower,upper),
        options={"time_limit":seconds,"disp":True})
    print("STATUS",result.status, result.message)
    if result.x is not None:
        print("FEASIBLE COLOR",
          hex(sum(int(z>0.5)<<k for k,z in enumerate(result.x[:ne]))))
    return result

if __name__ == "__main__":
    solve(int(sys.argv[1]) if len(sys.argv)>1 else 5,
          float(sys.argv[2]) if len(sys.argv)>2 else 60)
