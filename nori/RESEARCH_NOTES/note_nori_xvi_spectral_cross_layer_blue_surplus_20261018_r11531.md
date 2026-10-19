# Spectral cross-layer stability, cubic blue costs, and deep-orbit capacity

- Stable ID: note_nori_xvi_spectral_cross_layer_blue_surplus_20261018_r11531
- Author: Independent NORI1 mathematician
- Primary home: subsection:obstruction_compatibility_and_a_programme_for_nori1_closure
- Labels: NORI1, Article-XVI, spectral-stability, cross-layer-pairs, anchored-blue-cuts, cubic-cut, sharp-inequality, proved
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11531_1
- Updated session: session_nori_r11531_1
- Disposition: none
- Successor: none

## Related references

- note:note_nori_xvi_anchored_three_face_surplus_duality_20261018_r11531
- note:note_nori_xvi_weighted_face_cut_dual_20261018_r11531

## Research note

# Cross-layer spectral stability and sharp graded blue-edge forcing in Boolean faces

Let r>=5. In a directed Q_r suppose both endpoint edge stars are red and every monotone full geodesic is blue-blocked. Set T=r(r-1), Nblue=T+q (q>=0). Let A be the red edges of rank1-to-rank2, indexed as ordered initial direction pairs (i,j), and C the red edges of rank(r-2)-to-rank(r-1), indexed as ordered final direction pairs (k,l). Put a=|A|, b=|C|, and M=the number of blue edges in middle ranks 2,...,r-3. Let D be the number of pairs ((i,j),(k,l)) in A x C with four distinct directions.

THEOREM 1 (weighted deep-edge surplus). q >= (r-4)/(r-2)*M. Proof: a uniformly random monotone full geodesic uses an edge at rank k with probability 1/[r C(r-1,k)]. A blue first/last interior edge contributes at most 1/T and a deep blue edge contributes at most 2/[T(r-2)]. Since every geodesic has >=1 blue edge, T <= (Nblue-M)+2M/(r-2), giving the inequality. No reachability-downset hypothesis is made.

THEOREM 2 (simultaneous red terminal pairs force deep blue witnesses). D <= 2(r-3)*M. Proof: each red initial ordered pair and red final ordered pair with disjoint supports has (r-4)! geodesic completions; every one must have a middle blue edge. A specified middle rank-k edge belongs to k!(r-k-1)! <=2(r-3)! permutations. Count pairs (geodesic,blue edge) and divide by (r-4)!.

THEOREM 3 (spectral cross-layer inequality). Let T=r(r-1), d=(r-2)(r-3). The T x T disjointness matrix on ordered pairs of distinct directions has constant eigenvalue d, and every nonconstant eigenvalue of magnitude <=2(r-3). Its nonzero eigenvalues are d, -2(r-3), 2. To verify, pass first to unordered direction pairs and their vertex-pair incidence matrix H. The disjointness matrix equals J+I-H^T H, and H H^T=(r-2)I+J, giving eigenvalues C(r-2,2), -(r-3), 1. Duplicating each unordered pair into its two orientations doubles these eigenvalues and adds zero eigenvalues. Expander mixing yields
 D >= [d/T]*a*b -2(r-3)*sqrt(a*b).
Combining Theorems 1 and 2 gives the UNIVERSAL BLUE-SURPLUS INEQUALITY
 q >= (r-4)*a*b/[2r(r-1)] - (r-4)*sqrt(a*b)/(r-2).
It applies to arbitrary undirected colorings and arbitrary blue-blocked faces with red endpoint stars, not merely near-minimum blue cuts.

ASYMPTOTIC POLARIZATION. If the blue surplus q=O(r), solving the displayed quadratic inequality in sqrt(a*b) gives a*b=O(r^2). More explicitly,
 sqrt(a*b) <= [r(r-1)/(r-2)]*[1+sqrt(1+2q(r-2)^2/((r-4)r(r-1)))].
Thus if one near-terminal interior rank layer has Omega(r^2) RED edges, the opposite near-terminal interior layer has O(1) red edges whenever q=O(r). This is stable endpoint-layer polarization without requiring a complete blue layer or assuming the red reachable vertex set is downward closed.

THEOREM 4 (sharp incremental anchoring). If ALL last interior layer edges are red (b=T), then D=a*(r-2)*(r-3). Theorems 1 and 2 give q >= (r-4)*a/2, or Nblue >= r(r-1)+(r-4)*a/2. This is sharp for EVERY EVEN a between 0 and T. Proof of sharpness: choose any a/2 rank2 vertices, let U consist of all vertices at ranks 0 and 1 plus those chosen rank2 vertices, color every upward edge leaving U blue and all other edges red. The rank1-to2 red edge count is a, the last interior layer is red, the blue cut has T+a(r-4)/2 edges, and all monotone pole-to-pole paths are blocked.

CUBIC COROLLARY. If both first and last interior layers and both endpoint stars are red, then a=b=T, forcing Nblue >= r(r-1)(r-2)/2. This cubic bound is sharp: color the entire rank2-to3 layer blue, and all other face edges red. More generally, protecting the first s and final t whole edge-rank layers red forces Nblue >= r*min_(s<=k<=r-t-1) C(r-1,k), achieved by a complete minimizing intermediate rank layer. This yields higher-order polynomial blue costs from multiple protected red layers.

SCOPE. Theorems are unrestricted combinatorial implications. They strengthen Article XVI's anchored-face quantitative forcing without assuming a quadratic-minimum blocker; the unresolved NORI1 step is to force sufficiently many overlapping high-red-anchor face obligations from shortest antipodal paths, such that shared antipodal blue orbit capacity is exceeded. NORI1 remains OPEN.

FULL INDEPENDENT MANUSCRIPT: /mnt/data/nori_xvi_cross_layer_spectral_blue_surplus.md. STANDALONE AUDIT: /mnt/data/nori_xvi_spectral_cut_stability_verify.py checks 505 cut-based blocked faces in Q5-Q9, including non-downward-closed source sides and added non-cut blue edges, checks the matrix spectral norms by numerical diagonalization, and confirms equality in the sharp a=2,b=T example at every rank 5-9. The proof is dimension-uniform. Separate supporting finite optimization of the anchored triple gives global min-max blue values 23 for rank5 and 40 for rank6; rank7 currently has only bounds 52-60, so no rank7 optimality claim is made.

GLOBAL ANCHORED DEEP-ORBIT CAPACITY THEOREM. Let F range over any collection of blocked directed proper faces of ranks r_F>=5 in ONE legal antipodally odd Q_n coloring, with RED endpoint stars. In each face let A_F^*,C_F^* be any KNOWN RED subsets of its first and last interior layers, and D_F^* the number of disjoint-support pairs of ordered direction pairs in A_F^* x C_F^*. For nonnegative weights lambda_F, define W(e)=sum_(F where e is in a strictly middle rank of F)lambda_F. Then
  sum_F [lambda_F D_F^*/(2(r_F-3))] <= sum_(antipodal edge orbits {e,bar e}) max(W(e),W(bar e)).
If the orbit color is already pinned, replace its maximum with the weight of the prescribed blue member. PROOF: each F contains at least D_F^*/[2(r_F-3)] blue middle-layer edges by the cross-layer pair theorem. Weight and sum, regroup by full-cube edges, then use the one-blue-member-per-antipodal-orbit law. This is a nonvacuous necessary compatibility TEST when enough RED anchors are forced; it does not claim that NORI1 counterexamples always yield a violating family. Full proof, including the new Section 7: /mnt/data/nori_xvi_cross_layer_spectral_blue_surplus.md.
