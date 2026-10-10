# Complete face-dependent Q8 one-sentinel closure: dichotomy and two UNSAT certificates

THEOREM (complete Q8 closure with one genuine exterior coordinate; computer-assisted). Let c color the PHYSICAL ORDERED three-faces of Q8, obeying c(bar F,reverse pi)=1-c(F,pi). Fix one distinguished direction t. Assume that for each ordered free triple pi the face color depends on its exterior fixed bits only through the bit x_t when t is NOT in pi; when t is free, its color depends on no exterior bit. Then some full antipodal eight-geodesic has a window-color word with at most one change. The assumption allows genuine face-position dependence, so this strictly extends coordinate-only Q8 closure.

MATHEMATICAL REDUCTION. Relabel t=7 and V={0,...,6}. For all ordered triples pi on V let H(pi)=c(F,pi) at t-exterior bit 0 (the other exterior bits are immaterial). The antipodal-reversal law forces color at t-bit 1 to equal 1-H(reverse pi). H is an ARBITRARY 210-bit ordered-triple coloring; NO reversal-oddness of H is assumed. For ordered triples pi containing 7, denote their position-independent labels by G(pi); then G(reverse pi)=1-G(pi), contributing exactly 63 Boolean variables. There are 210+63=273 independent Boolean variables.

For a full eight-direction order p and a starting sentinel bit b, let j=position of 7 in p. For window index i with ordered triple pi=p[i:i+3]: if 7 lies inside pi its color is G(pi); otherwise its color is H(pi) for b XOR [j<i]=0, and 1-H(reverse pi) for b XOR [j<i]=1. Every other starting-root bit is immaterial. The full window word has six bits. Forbid each of the twelve binary words with zero or one color change by one six-literal clause OR_i(window_i != target_i). Reversing p at the SAME root sends its word to the complement of the reversed word by the physical NORI law; hence it suffices to inspect half of all 8-permutations, for both sentinel-root bits, giving (8!/2)*2*12=483840 clauses.

A DICHOTOMY ON THE CHART H is exhaustive.
Case I. H has a monochromatic tight directed five-path on five distinct vertices of V. By relabeling V and globally flipping all colors, normalize H(012)=H(123)=H(234)=0. Add these three unit clauses. The full 273-variable CNF with the 483840 badness clauses is UNSAT (libz3.so.4).
Case II. H has NO monochromatic tight directed five-path. For each ordered five-tuple q in V, forbid both H(q0q1q2)=H(q1q2q3)=H(q2q3q4)=0 and the analogous all-1 assignment. These are 2*7P5=5040 three-literal clauses. With the same full 483840 badness clauses the 273-variable CNF is UNSAT (libz3.so.4).
Thus a hypothetical coloring with no good full Q8 geodesic lies in neither exhaustive case; contradiction.

REPRODUCIBLE REFERENCE CHECKER (Python 3 with z3-solver):
from itertools import permutations
from z3 import Bool,Not,Or,Solver,unsat
V=range(8); t=7; W=list(permutations(V,3))
H={q:Bool('H'+''.join(map(str,q))) for q in W if t not in q}
G={}
for q in W:
    if t in q and q not in G:
        a=Bool('G'+''.join(map(str,q)))
        G[q]=a; G[q[::-1]]=Not(a)
assert len(H)==210 and len(G)==126
def h(q,b):
    if t in q:return G[q]
    return H[q] if b==0 else Not(H[q[::-1]])
good={tuple([a]*j+[1-a]*(6-j)) for a in (0,1) for j in range(7)}
assert len(good)==12
for case in (0,1):
    S=Solver()
    if case==0:
        for i in range(3):S.add(Not(H[tuple(range(i,i+3))]))
    else:
        for q in permutations(range(7),5):
            w=[H[q[i:i+3]] for i in range(3)]
            S.add(Or(*w));S.add(Or(*(Not(a) for a in w)))
    for p in permutations(V):
        if p>p[::-1]:continue
        loc=p.index(t)
        for b in (0,1):
            w=[h(p[i:i+3],b^(loc<i)) for i in range(6)]
            for g in good:
                S.add(Or(*(w[i] if g[i]==0 else Not(w[i]) for i in range(6))))
    assert S.check()==unsat
Executed with direct ctypes calls to the system Z3 C library on 2026-10-09: Case I UNSAT in 9.84 s; Case II UNSAT in 7.87 s, each with 273 variables and 483840 six-literal no-good clauses. A separate SAT tactic independently rechecked Case I UNSAT (~10.35 s).

IMPORTANT SCOPE. The theorem is a special FACE-DEPENDENT rank-eight case and therefore a strictly stronger bridge than coordinate-only Q8. It does not establish full physical Q8 or all-dimensional NORI, because a generic ordered-face color can depend on five independent exterior bits. Any all-dimension upgrade must control multiple exterior coordinates simultaneously. A two-sentinel extension was formulated with 438 variables and 967680 no-good clauses; initial SAT solving did not finish. This identifies a natural next bridge between coordinate-only combinatorics and the full physical geometry. Request independent certificate audit before elevating to a publication composition.
