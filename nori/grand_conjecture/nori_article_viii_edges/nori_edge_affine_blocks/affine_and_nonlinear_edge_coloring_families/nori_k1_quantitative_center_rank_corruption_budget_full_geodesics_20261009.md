# Closed-form central-rank orbit sizes and explicit total-fault thresholds for antipodal edge geodesics

QUANTITATIVE COROLLARY to contemporaneous team Item nori_k1_robust_central_rank_fault_tolerant_geodesic_closure_both_parities_20261009: that item proves the general per-direction orbit-density bounds. The contribution here is the explicit CLOSED BINOMIAL FORM of all orbit sizes and the SIMPLE UNWEIGHTED TOTAL-FAULT BUDGETS: for EVEN dimension with both selected direction groups even, sum_i D_i < (1/2) C(u,u/2) C(l,l/2) guarantees any target; for ODD dimension and any bridge h selected from the odd-sized target class, sum_(i!=h) D_i < (1/4) C(u,u/2) C(l,l/2) guarantees any target even when ALL physical h-edge colors are arbitrary. Full derivation and the even odd/odd group formulas follow. This item is a companion EXPLICIT ENUMERATIVE SHARPENING, not an independent competing statement of the general fault-tolerance theorem.

ROBUST CENTRAL-RANK THEOREM (original antipodally odd physical edge coloring, both parity dimensions). The recent full-target center-rank results remain true if a quantified sparse set of physical central-band edges violate the per-direction uniformity condition. The sharp formulas below follow by a literal root/order orbit count, not an independent-edge heuristic.

Write a fixed prescribed target direction-color vector T in F2^n and choose arbitrary reference bits a_i for each direction. Set U={i:T_i=a_i}, L={i:T_i=1+a_i}, with sizes u,l.

PART A (EVEN n=2k, any u,l parity). For each i in U, call an i-edge BAD if it has exterior Hamming rank k and actual color unequal to a_i; for each i in L, BAD means exterior rank k−1 and actual color unequal to 1+a_i. Consider only the physical i-edges in the following attainable suborbits Omega_i:

(A1) If u,l are even: for i in U, exterior L coordinates contain exactly l/2 ones and exterior U\{i} exactly u/2 ones. For i in L, exterior U coordinates contain u/2 ones and exterior L\{i} exactly l/2−1 ones. Each accessible i-orbit has cardinality
  M_i = (1/2) binom(u,u/2) binom(l,l/2),
for every nonempty U or L. Empty groups have no corresponding directions.

(A2) If u,l are odd: for i in U, exterior L coordinates contain (l+1)/2 ones and exterior U\{i} exactly (u−1)/2 ones, giving
  M_i = binom(l,(l+1)/2) binom(u−1,(u−1)/2).
For i in L, exterior U coordinates contain (u−1)/2 ones and exterior L\{i} exactly (l−1)/2 ones, giving
  M_i = binom(u,(u−1)/2) binom(l−1,(l−1)/2).

Let D_i be the number of BAD actual physical i-edges in Omega_i. If
  SUM_(i in [n]) D_i/M_i < 1,
THEN there is a genuine FULL antipodal n-edge geodesic with exact direction-color vector T. In particular if T is constant there is a monochromatic full antipodal geodesic.

Proof. Use exactly the actual oscillating full n-geodesic families constructed in Item nori_k1_even_dimension_center_rank_uniformity_oscillating_geodesic_all_targets_20261009: if both group sizes are even, place all U directions first then L, and use total vertex Hamming weights k,k+1,k,... for U and k,k−1,k,... for L. If both group sizes are odd, start weight k+1, traverse U first with weights k+1,k,k+1,...,k, then L with weights k,k−1,k,...,k−1. Given every within-group permutation, the root bits are uniquely specified by whether that named direction is traversed upward or downward; total initial ones matches the prescribed initial Hamming weight, so every state is physical. Independent UNIFORM random permutations of U and L induce the uniform distributions on each Omega_i because the coordinate-permutation group on U\{i} and on L (or vice versa) is transitive on the stated uniform cardinality subsets and leaves the family invariant. In particular every individual BAD physical i-edge is encountered with probability EXACTLY 1/M_i. The union bound yields P(any encountered BAD edge) <=sum_i D_i/M_i<1, so at least one true full geodesic encounters no BAD edge. It realizes T coordinatewise by the appropriate central-layer colors. QED.

PART B (ODD n=2k+1, bridge direction h). Exactly one of |U|,|L| is odd; choose ANY h in that odd-sized class. Remove h, leaving u,l even with u+l=2k. The surviving U,L directions have their upper-track reference edges at exterior rank k+1, respectively lower-track reference edges at exterior rank k−1. Follow the previous Item nori_k1_odd_dimension_near_center_rank_uniformity_antipodal_bridge_all_targets_20261009: concatenate L,h,U; start weight k, oscillate k↔k−1 through L, take h from k to k+1, oscillate k+1↔k+2 through U. Every physical nonbridge direction-i edge lies in an orbit Omega_i of EXACT size
  M_i=(1/2)binom(l,l/2)binom(u,u/2),
with h-bit held at0 for lower directions or1 for upper directions. The within-group permutation distribution on Omega_i is uniform. Let D_i count BAD i-edges in Omega_i relative to the required a_i or 1+a_i. Put M=binom(l,l/2)binom(u,u/2). If
  SUM_(i !=h) D_i/M_i < 1/2
(equivalently SUM_(i!=h) D_i < M/4),
then the full target-color geodesic exists for ARBITRARY colors on ALL h-direction physical edges, without any restriction on h at all.

Proof. The physical bridge h-edge has exterior ones in EXACTLY l/2 L-positions and u/2 U-positions. Exchanging positions (1,2),(3,4),... INSIDE each independently ordered EVEN-sized group complements ALL these exterior h-bits. Since at least one group is nonempty for n>=3, this is a fixed-point-free involution on the uniform family of u!l! full rooted path states. The two bridge edges are physical antipodes with opposite colors, so P(bridge has target T_h)=1/2 EXACTLY. By uniform orbit incidence, P(any nonbridge BAD edge) <=SUM_i D_i/M_i <1/2. Hence the positive-probability intersection of 'bridge correct' and 'no nonbridge bad edge' contains a genuine full target-color antipodal geodesic. QED.

INTERPRETATION. In even n with u,l even, a sufficient unweighted total-error criterion is
  SUM_i D_i < (1/2) binom(u,u/2)binom(l,l/2).
In odd n after selecting a bridge, the corresponding sufficient criterion is SUM_(i!=h)D_i <(1/4)binom(u,u/2)binom(l,l/2). These robustness budgets can be exponentially large. They yield concrete necessary density obstructions to hypothetical universal edge counterexamples and strictly extend the previous exact layer-constant theorems, allowing arbitrary NONLINEAR and locally corrupted physical edge colors. They do not prove unrestricted edge conjecture; when defects exceed these budgets, this particular union-bound template is inconclusive.
