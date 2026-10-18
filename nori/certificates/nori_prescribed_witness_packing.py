#!/usr/bin/env python3
"""NORI1 prescribed-witness orbit-disjoint packing test for Q4, Q5, Q6.

Uses stdlib ctypes and system libz3.so.4.  Reports finite SAT answers;
no independently checked UNSAT proof log is included.
Usage: python nori_prescribed_witness_packing.py [4|5|6]
"""
import ctypes
import sys
from itertools import permutations

n = int(sys.argv[1])
full = (1 << n) - 1
orbit_ids = {}
for i in range(n):
    for x in range(1 << n):
        a = x & ~(1 << i)
        b = (x ^ full) & ~(1 << i)
        orbit_ids.setdefault((i, min(a, b)), len(orbit_ids))

def edge_orbit(x, i):
    a = x & ~(1 << i)
    b = (x ^ full) & ~(1 << i)
    return orbit_ids[i, min(a, b)], int(a > b)

# Automorphism normalization: red witness rooted at 0 in order 0,1,...,n-1.
path = []
v = 0
for i in range(n):
    path.append(edge_orbit(v, i))
    v ^= 1 << i
pivot_support = {j for j, s in path}
clauses = set()
for root in range(1 << n):
    for order in permutations(range(n)):
        v = root
        edges = []
        for i in order:
            edges.append(edge_orbit(v, i))
            v ^= 1 << i
        if any(j in pivot_support for j, s in edges):
            continue
        for target in (0, 1):
            clauses.add(tuple(sorted((j, s ^ target) for j, s in edges)))

lines = ["(set-option :timeout 60000)"]
lines += [f"(declare-const x{j} Bool)" for j in range(len(orbit_ids))]
for j, sign in path:
    lines.append("(assert " + (f"x{j}" if sign else f"(not x{j})") + ")")
for clause in sorted(clauses):
    literals = [
        f"x{j}" if sign == 0 else f"(not x{j})"
        for j, sign in clause
    ]
    lines.append("(assert (or " + " ".join(literals) + "))")
lines.append("(check-sat)")
lib = ctypes.CDLL("/usr/lib/x86_64-linux-gnu/libz3.so.4")
lib.Z3_mk_config.restype = ctypes.c_void_p
lib.Z3_mk_context.argtypes = [ctypes.c_void_p]
lib.Z3_mk_context.restype = ctypes.c_void_p
lib.Z3_eval_smtlib2_string.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
lib.Z3_eval_smtlib2_string.restype = ctypes.c_char_p
ctx = lib.Z3_mk_context(lib.Z3_mk_config())
answer = lib.Z3_eval_smtlib2_string(ctx, ("\n".join(lines)+"\n").encode()).decode().strip()
print("dimension", n, "variables", len(orbit_ids), "clauses", len(clauses),
      "SAT answer", answer)
assert answer == ("sat" if n == 4 else "unsat")
if n == 4:
    # Explicit countermodel uses orbit variables 4,9,10,12 set to one.
    bits = 0x1610
    assert all(((bits >> j) & 1) == sign for j, sign in path)
    for clause in clauses:
        assert any(((bits >> j) & 1) != sign for j, sign in clause)
    print("Q4 prescribed-witness countermodel", hex(bits), "checked")
