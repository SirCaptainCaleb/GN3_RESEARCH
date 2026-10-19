# Weighted face-cut capacity, quadratic rainbow packing and minimum rigidity

- Stable ID: note_nori_xvi_weighted_face_cut_dual_20261018_r11531
- Author: Independent NORI1 mathematician
- Primary home: subsection:obstruction_compatibility_and_a_programme_for_nori1_closure
- Labels: NORI1, Article-XVI, weighted-geodesic-cut, endpoint-degree, quadratic-sharp, antipodal-orbit-dual, overlap-compatibility, proved
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11531_1
- Updated session: session_nori_r11531_1
- Disposition: none
- Successor: none

## Related references

- note:note_nori_xvi_near_minimum_monotone_face_cut_rigidity_20261018_r11531
- note:note_nori_xvi_walk_pumping_shortest_repair_20261018

## Research note

# Weighted endpoint-degree face cuts and antipodal-orbit capacity

Let F be any directed r-dimensional Boolean cube, with distinguished source and sink. For an edge e beginning at rank k write w_F(e)=1/C(r-1,k), and let N_k be the number of blue edges of that rank. Suppose every source-to-sink monotone full geodesic includes blue.

THEOREM 1 (all-dimensional weighted face cut). Uniformly random direction orders traverse each rank-k edge with probability 1/[r C(r-1,k)]. Since every full geodesic contains blue,
 sum_(k=0)^(r-1) N_k / C(r-1,k) >= r.
Let a,b be the number of RED edges at source and sink poles, respectively. For r>=3 their edge stars are disjoint, with N_0=r-a and N_(r-1)=r-b. Therefore
 sum_(k=1)^(r-2) N_k / C(r-1,k) >= a+b-r,
and when a+b>r the total BLUE interior edge count is at least (r-1)(a+b-r), using C(r-1,k)>=r-1 on all interior levels.

SHARP QUADRATIC COROLLARY. If both full face endpoint stars are red, every monotone-path blocker contains at least r(r-1) blue edges. It is attained by taking all r(r-1) edges from rank1 to rank2 blue and all other face edges red. Prescribe this coloring in a facet Q_r of Q_(r+1) and complement all antipodal mate edge colors to obtain a full legal coloring, proving the sharp threshold is compatible with antipodal oddness.

WEIGHTED NEAR-EQUALITY COROLLARY. Under full-red-endpoint stars, if the total number of blue face edges is r(r-1)+q, then
 sum_(k=2)^(r-3) [1-(r-1)/C(r-1,k)]N_k <= q.
PROOF: multiply the weighted cut inequality by r-1 and rearrange. This restricts blue edges farther from the two poles whenever the blocker is close to the sharp quadratic threshold. For r>=5 all displayed coefficients are nonnegative and those indexed at deeper middle levels are positive.

THEOREM 2 (global shared-antipodal-edge capacity). Let c be any legal antipodally odd coloring of Q_n, and let FAMILY be arbitrary directed cube faces F of dimensions r_F>=2, each purported to have no red full monotone source-to-sink geodesic. Choose weights lambda_F>=0. For each undirected edge e put
 W(e)=sum_(F containing e) lambda_F / C(r_F-1,k_F(e))
where k_F(e) is the rank of the lower poleward endpoint of e along F. Put L=sum_F lambda_F*r_F. Then
 L <= sum_(antipodal edge orbits O={e,bar e}) max(W(e),W(bar e)).
More strongly, if some orbit colors are already prescribed by red shortest paths or other valid data, replace the corresponding maximum by the weight W(blue member) determined by that orbit. If this upper capacity is LESS than L, the proposed blocked-face and anchored-edge requirements cannot coexist in one legal coloring.

PROOF. Apply Theorem 1 on each face, multiply by lambda_F, and sum. Rearranging gives L<=sum_(e blue) W(e). Antipodal oddness forces precisely one blue member per orbit, and the upper capacity follows. There are no small-cut or star assumptions. The capacity criterion is sufficient for detecting incompatibility, not a complete characterization.

SHORT-PATH INTERFACE. For every pair of consecutive traversals of a direction j in a shortest red path, the projected opposite face F is forced to have no all-red monotone geodesic. Theorem 1 therefore converts any certified red degrees a,b at the two face poles into a blue interior-edge lower bound, without assuming the face cut is economical. Theorem 2 combines several such requirements through their shared global edge orbit variables. An unrestricted NORI1 proof would still require a forcing argument selecting enough simultaneous gap faces and red edge anchors so that some positive-weight capacity certificate is violated. No such universal selection theorem is proved here.

VERIFICATION. Self-contained manuscript /mnt/data/nori_xvi_weighted_face_cut_capacity.md. Independent Python nori_xvi_endpoint_degree_weighted_cuts_verify.py tested 2317 random and sharp directed face colorings in dimensions 3-9 and independently checked random direction-edge occupancy formulas. Independent nori_xvi_antipodal_weighted_capacity_verify.py tested 360 legal odd Q5-Q7 colorings and families of overlapping blocked faces, checking their weighted capacity for true orbit color assignments. All tests passed. An additional finite mincut scan suggests a possible stronger endpoint-degree formula but NO unproved dimension-uniform formula is asserted. NORI1 remains OPEN.

## Quadratic rainbow packing and rigidity at minimum capacity

THEOREM (interior-edge-disjoint full geodesics). For any r>=3, Q_r has r(r-1) full source-sink monotone geodesics with pairwise disjoint edges at ranks 1 through r-2; sharing is permitted only at source and sink stars, with each terminal edge used r-1 times. PROOF. Assign capacity 1 to each edge of an interior rank and r-1 to source and sink edges. Uniformly average all r! geodesics and scale the resulting flow by T=r(r-1). Every interior rank-k edge has load (r-1)/C(r-1,k)<=1, and each terminal edge has load r-1. This is a feasible flow of value T. Integral max-flow supplies an integral flow of at least T. The rank-1-to-rank-2 layer has total capacity T, so the value is T, and decomposition gives T full geodesics with disjoint interior edges. Every terminal edge saturates by the total-flow count. This strengthens the quadratic bound to a constructive rainbow packing, independent of the coloring.

THEOREM (sharp equality rigidity for r>=5). Assume all face endpoint-star edges are RED, every monotone source-sink geodesic has some BLUE edge, and the face has only T=r(r-1) blue edges. Then the blue edges form EITHER the ENTIRE rank-1-to-rank-2 layer OR the ENTIRE rank-(r-2)-to-rank-(r-1) layer. PROOF. All geodesics have >=1 blue edge. Each blue interior edge has uniform geodesic probability <=1/T, and there are T blue edges, so mean blue count <=1. Hence every geodesic has precisely one blue edge and every blue edge must have maximal occupancy 1/T, restricting it to the first or last interior layer. Write X_ab for the blue bit on the first interior edge determined by ordered first directions a,b, and Y_cd for the blue bit on the last interior edge determined by ordered final directions c,d. For disjoint ordered pairs (a,b),(c,d), completion to a direction permutation gives X_ab+Y_cd=1 in integers. If two first ordered pairs have intersecting supports, their union has at most three directions; since r>=5, a final ordered pair disjoint from both exists, giving equality of their X values. The intersection graph on ordered pairs is connected, so X is constant over all pairs, and Y is the complementary constant. Hence only the two complete-layer possibilities.

SHARP DIMENSION BOUNDARY. In r=4, a mixed minimum 12-blue-edge cut exists: take all rank1-to-rank2 edges except those entering vertex {0,1}, and add the two rank2-to-rank3 edges leaving {0,1}. Each full geodesic crosses the resulting blue cut once; both endpoint stars remain red. So r>=5 is necessary for the two-layer rigidity statement.

VERIFIERS. /mnt/data/nori_xvi_quadratic_rainbow_packing_verify.py uses integral maximum flow to construct and check T path packings for r=3,...,9. /mnt/data/nori_xvi_quadratic_cut_rigidity_verify.py checks pure-layer sharp patterns and the Q4 mixed minimum exception in dimensions 3-8. Complete proofs in /mnt/data/nori_xvi_weighted_face_cut_capacity.md. No global theorem currently forces a hypothetical NORI1 counterexample to produce enough heavily RED-anchored, near-minimum face blockers; NORI1 remains OPEN.
