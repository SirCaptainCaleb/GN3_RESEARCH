# Mod-three strengthened induction with an equality-structure layer

## Statement

A viable induction for the dense-core all-special conjecture should carry two statements: STRICT(r), all-specialness above 2r/3 for every r, and an EQUALITY(r) structural classification when 3 divides r. All one-degree induction failures occur exactly at smaller parameters divisible by three. The order-11 equality blocker cycle at r=6 and the order-12 open-defect analysis are the prototype equality structures that the strengthened induction should propagate.

## Body


The ordinary induction for the dense-core conjecture has a single modular defect. Put
  k_r=floor(2r/3)+1.
Deleting one vertex from a critical spanning candidate at parameter ell lowers minimum degree by at most one. The comparison
  k_ell-1 >= k_{ell-1}
holds for ell congruent to 0 or 2 mod 3, and fails by exactly one for ell congruent to 1 mod 3. In the latter case r=ell-1 is divisible by 3 and the deletion lands exactly at degree
  2r/3,
the equality threshold.

The same phenomenon appears in the lower-rank path-hull induction. A rank-q witness hull has forbidden length r=q+1 and a nonspecial edge forces
  delta(G)<=floor(2r/3).
If r is not divisible by 3, this upper bound lies strictly below the real number 2r/3. If r is divisible by 3, the only numerically tight possibility is exactly
  delta(G)=2r/3.

Thus all arithmetically tight failures of the strict induction are concentrated at smaller parameters divisible by three.

This suggests strengthening the induction package.

STRICT(r):
Every P_r-free linear 3-graph of minimum degree >2r/3 is all-special.

EQUALITY(r), only for r divisible by 3:
Classify nonspecial configurations at minimum degree exactly 2r/3 in the critical near-spanning orders encountered by induction. The classification should record the blocker-defect topology, not necessarily list isomorphism types. Its model case is r=6:
- on 2r-1=11 vertices the human equality counterexample has a maximum-rank nonspecial edge whose two terminal blocker matchings close into alternating cycles with zero open single-blocker defect;
- adding one vertex changes the topology from closed saturation toward open blocker defects, as in the order-12 analysis.

The intended inductive use is:
1. For ell congruent to 0 or 2 mod 3, one-vertex deletion of the spanning top-rank core lies in STRICT(ell-1).
2. For ell congruent to 1 mod 3, one-vertex deletion lands in EQUALITY(ell-1), where ell-1 is divisible by 3. The equality classification should then show that restoring the deleted vertex either opens a blocker defect and hence supplies a rotation/second entrance, or preserves a fully closed saturated equality geometry incompatible with the strict degree k_ell.
3. In a lower-rank path hull, if r=q+1 is not divisible by 3 there is genuine degree slack; if r is divisible by 3 and the hull is tight, EQUALITY(r) supplies the structural information that the crude low-degree conclusion lacks.

Thus the order-11/order-12 proofs are not merely base cases. They identify the equality layer that a mod-3 strengthened induction must carry.
