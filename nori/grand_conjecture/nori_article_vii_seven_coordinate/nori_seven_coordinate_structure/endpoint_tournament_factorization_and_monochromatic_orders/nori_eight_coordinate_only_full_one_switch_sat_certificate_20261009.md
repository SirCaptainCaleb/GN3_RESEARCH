# Complete Q8 coordinate-only one-switch closure: 168-variable UNSAT certificate

THEOREM (computer-assisted, complete coordinate-only Q8). Let V have eight directions. Let h:V^3_distinct->{0,1} satisfy h(c,b,a)=1-h(a,b,c). Then there is a permutation p of V whose six consecutive triple values h(p_i,p_{i+1},p_{i+2}), i=1,...,6, have at most one color change. Consequently every coordinate-only antipodal-reversal-odd coloring of the physical ordered three-faces of Q8 has a full good antipodal geodesic from EVERY starting vertex. For arbitrary n>=8, every such coordinate-only coloring has a full n-geodesic with at most n-7 switches (choose any eight directions, then append all unused directions).

REDUCTION. The established six-direction monochromatic-five-facet theorem (Item nori_six_direction_monochromatic_facet_transfer_20261008) gives five directions a,b,c,d,e with h(abc)=h(bcd)=h(cde). Relabel as 0,1,2,3,4 and globally complement colors to impose h(012)=h(123)=h(234)=0. Suppose every eight-permutation had at least two changes. Encode a Boolean x_{abc} for each unordered reversal orbit {(a,b,c),(c,b,a)} of ordered distinct triples; there are 3*binom(8,3)=168 orbits. A reversed triple denotes the complement of its orbit variable. For any permutation p, the six window literals W(p) are thus fixed in terms of these 168 Boolean variables. Every possible at-most-one-change word is 0^k 1^(6-k) or 1^k 0^(6-k), 0<=k<=6, giving exactly twelve distinct binary words. For every p and every such good word w, impose the CNF clause OR_{i=1..6}(W_i(p) != w_i). Under the assumed absence of a good path all these clauses must hold. Since W(reverse(p))=1-reverse(W(p)), the good-word condition is reversal invariant; include only lexicographically one of p and its reverse. This gives 8!/2 * 12 = 241920 clauses and the three unit constraints h(012)=h(123)=h(234)=0. A complete SAT solver returned UNSAT; the contradiction proves the claim modulo this exact finite-verification certificate.

INDEPENDENT REPRODUCIBLE CHECK (Python 3 with z3-solver):
from itertools import permutations
from z3 import Bool, Not, Or, Solver, unsat
V=range(8)
h={}
for t in permutations(V,3):
    if t not in h:
        x=Bool('x'+str(len(h)//2))
        h[t]=x
        h[t[::-1]]=Not(x)
S=Solver()
for t in [(0,1,2),(1,2,3),(2,3,4)]:
    S.add(Not(h[t]))
G={tuple([v]*k+[1-v]*(6-k)) for v in (0,1) for k in range(7)}
assert len(G)==12 and len(h)==336
for p in permutations(V):
    if p>p[::-1]:
        continue
    w=[h[p[i:i+3]] for i in range(6)]
    for g in G:
        S.add(Or(*(w[i] if g[i]==0 else Not(w[i]) for i in range(6))))
assert S.check()==unsat

EXECUTED VERIFICATION. An independent direct ctypes binding to installed libz3.so.4 constructed the same 168-variable, 241920-clause SAT instance with the three zero seed labels and returned Z3_L_FALSE (UNSAT) on 2026-10-09, solve time ~3.08 seconds. A second encoding used the established seven-direction coordinate-only closure and selected a good seven-order. Its monochromatic word extends to a good full eight-order immediately. Reversal reduces every genuinely switched word to the seed 0^1 1^4 or 0^2 1^3, with the remaining direction labelled 7. Both corresponding 168-variable, 241920-clause SAT instances were independently checked UNSAT (~1.38 and ~1.56 seconds respectively), providing a separate normalization cross-check. The first case has a Z3 unsat core involving only 154 of 20160 reversal-classes of 8-permutations.

SCOPE AND FRONTIER. The result is for coordinate-only ternary labels; in a general NORI coloring, two physical three-faces with the same free ordered directions and different exterior bits may have distinct colors. The reduction's identification of these variables is then unjustified. No conclusion for unrestricted face-dependent Q7/Q8 or the general grand conjecture follows from this certificate. A desirable next step is an exact physical-root/face transport analogue of the 8-direction contradiction, or a human-readable forced-window certificate independent of a SAT solver. The present statement is a computer-assisted finite theorem awaiting independent certificate audit.
