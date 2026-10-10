# Exact 9-vertex tight-four Ramsey SAT verification and Q12 central-edge closure

# Exact tight-four Ramsey verification and Q12 central-edge closure

**Computer-assisted theorem.** Every binary coloring of the 4-subsets of a nine-element set contains a monochromatic tight 4-uniform path on eight distinct vertices (five consecutive 4-subset windows). Nine is sharp: on eight vertices, coloring each 4-set by membership of a fixed point makes every spanning eight-vertex tight path bichromatic, since the five windows have empty intersection and union all eight vertices.

**Reproducible exhaustive verifier** (Python/Z3). Every counterexample to the theorem is exactly a satisfying assignment to the finite Boolean formula below. The solver returned UNSAT. Its 126 variables represent all 4-subsets; its 181440 reversal classes of 8-letter injective words give 362880 clauses of width five. This is an exact SAT reduction, not a sampling procedure.

```python
from itertools import combinations, permutations
from z3 import Bool, Not, Or, Solver, unsat
V = range(9)
x = {T: Bool('x' + '_'.join(map(str,T))) for T in combinations(V,4)}
s = Solver()
count = 0
for p in permutations(V,8):
    if p > p[::-1]: continue
    w = [x[tuple(sorted(p[i:i+4]))] for i in range(5)]
    s.add(Or(*w), Or(*(Not(t) for t in w)))
    count += 1
assert count == 181440
assert s.check() == unsat
```

**Corollary 1 (odd-complement 6-set coloring).** If |U|=12 and lambda:binom(U,6)->F2 satisfies lambda(U minus S)=1+lambda(S), there exists a monochromatic tight six-uniform path on ELEVEN distinct vertices, with SIX consecutive six-set windows.

Proof. Fix a two-point core H={h1,h2} and select nine of the remaining ten directions. Apply the verified theorem to the four-set coloring T ↦ lambda(H union T), obtaining eight distinct a1,...,a8 whose five consecutive four-windows are monochromatic, color q. Inserting h1,h2 after a4 produces ten-letter order (a1,a2,a3,a4,h1,h2,a5,a6,a7,a8) with FIVE monochromatic six-set windows. Let u,v be the two unused directions. The six-set appearing when u is prepended and the six-set appearing when v is appended are complementary in U, hence have opposite colors. Exactly one has color q. Choose that end extension, obtaining eleven-letter mono tight six-path. QED.

**Corollary 2 (genuine Q12 antipodal physical edge geodesic).** Every antipodally odd physical undirected edge coloring of Q12 for which each middle-belt edge has the color lambda(S) of its unique rank-six incident vertex S has a monochromatic full twelve-edge antipodal geodesic. Colors outside the belt may be arbitrary under antipodal oddness.

Proof. Take monochromatic tight six-path z1,...,z11 from Corollary 1, and let z12 be the unused coordinate. Start at the rank-five support {z1,...,z5}; flip in order (z6,z1,z7,z2,z8,z3,z9,z4,z10,z5,z11,z12). The six successive rank-six supports encountered are precisely the six consecutive size-six windows in z1,...,z11. Each of the twelve edges meets precisely one of these rank-six vertices, all labeled q. The path flips each coordinate exactly once, reaching its antipode. QED.

**Proof status.** The finite lemma and downstream special-edge corollaries are verified computationally by an exact Boolean satisfiability solver. A solver-independent short derivation or independently checkable UNSAT proof would strengthen the certificate. Unrestricted physical-edge coloring and the active ordered-three-face NORI conjecture remain OPEN.

**Promising generalization.** For every r≥2, conjecture any 2-coloring of binom([2r+1],r) contains a mono tight r-path on 2r distinct vertices. Cases r=2,3 have elementary proofs, and r=4 is established by finite verification here. If this generalizes to every r, the two-core insertion and odd-complement two-unused end-extension prove central-vertex-sign EDGE closure in every even cube dimension. The active NORI conjecture still requires additional physical ordered-three-face transfer.
