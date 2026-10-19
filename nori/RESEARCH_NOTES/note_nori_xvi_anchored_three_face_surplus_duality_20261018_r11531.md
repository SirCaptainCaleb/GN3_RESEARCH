# Anchored quadratic three-face incompatibility and blue-surplus deletion duality

- Stable ID: note_nori_xvi_anchored_three_face_surplus_duality_20261018_r11531
- Author: Independent NORI1 mathematician
- Primary home: subsection:obstruction_compatibility_and_a_programme_for_nori1_closure
- Labels: NORI1, Article-XVI, anchored-face-cuts, 2-SAT, surplus-duality, mixed-integer-sharpness, shared-edge-compatibility
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11531_1
- Updated session: session_nori_r11531_1
- Disposition: none
- Successor: none

## Related references

- note:note_nori_xvi_odd_rank_quadratic_face_pairwise_gluing_20261018_r11531
- note:note_nori_xvi_weighted_face_cut_dual_20261018_r11531

## Research note

ARTICLE XVI: ANCHORED QUADRATIC TRIPLE AND SURPLUS DUALITY (proved, NORI1 open).

THEOREM A. For any r>=5 put n=r+2, T=r(r-1). In the common facet x_(r+1)=0 let j=2, M=sum_(i=0)^r e_i, M0=M XOR e0, Mj=M XOR ej. Define r-faces with ordered poles A: x_j=0, poles(0,Mj); B: x_0=0, poles(0,M0); C: x_j=1, poles(M0,e0 XOR ej). In each face, a blocked red antipodal geodesic with red endpoint stars requires >=T blue edges. At equality, rigidity forces the blue early or late rank layer (choice0 or1). The compatibility matrices of pure patterns are AB=[[1,0],[0,1]], BC=[[0,1],[1,0]], AC=[[1,1],[1,1]].

Pin two RED anchors, both outside B: a is the direction1 edge from Mj XOR e1 XOR e3 to Mj XOR e3, and c is the direction3 edge from e0 XOR ej XOR e1 to e0 XOR ej XOR e1 XOR e3. Anchor a forbids A1 but permits A0; anchor c forbids C1 but permits C0. Thus at equality A0,C0 are forced, requiring simultaneously B0 via AB and B1 via BC. Contradiction. Every PAIR of these anchored face prescriptions admits minimum cost T in both faces, and extends to a legal antipodally odd coloring because all prescribed edges lie in one facet and antipodal mates lie in the opposite facet. Therefore simultaneous blocking and anchors imply max(Nblue(A),Nblue(B),Nblue(C))>=T+1 for ALL r>=5. Full rank-uniform proof /mnt/data/nori_xvi_anchored_triple_and_surplus_duality.md. Verification /mnt/data/nori_xvi_anchored_quadratic_triple_verify.py passed r=5,...,11.

FINITE Q7 STRENGTHENING. For r5,T20, a mixed-integer model with 176 union-face edges, 360 red-path-blocker inequalities and 28 pinned-red edges achieves and proves minimum possible maximum blue-face count 23. A feasible coloring has per-face counts (23,23,23). Its LP relaxation yields 22, demonstrating an integrality gap. Verifier /mnt/data/nori_xvi_anchored_triple_milp.py. The uniform theorem establishes only T+1, not T+3 in all ranks.

THEOREM B (quantitative 2-SAT deletion principle). For any family of proper rank-r_i>=5 faces F_i with blocked full red monotone geodesics and red endpoint stars in one legal coloring, let T_i=r_i(r_i-1) and q_i=Nblue(F_i)-T_i>=0. Given consistent pinned edge-orbit colors, make a Boolean variable per face selecting its early/late pure quadratic minimum blocker. Introduce unary clauses forbidding patterns inconsistent with pins, and binary clauses forbidding patterns disagreeing on shared or antipodal orbit colors. For weights lambda_i>=0 let tau_lambda be the minimum total weight of face variables whose deletion makes this 2-CNF satisfiable. Then
 sum_i lambda_i q_i >= tau_lambda.
Proof: every face with q_i=0 must have one of its two pure patterns, and those patterns form a valid assignment after deleting every face with q_i>0. Each deleted face pays at least one integral excess edge, so its weight is at most lambda_i q_i.

Combining with antipodal edge-orbit capacity, w(e)=sum_(i:e in F_i)lambda_i, yields the necessary global compatibility inequality
 sum_i lambda_i T_i + tau_lambda <= sum_(orbits {e,bar e}) max(w(e),w(bar e)),
where pinned orbits instead contribute their prescribed blue member weight. This combines shared-color integrality constraints and face-blue capacity. No theorem yet forces such a contradiction from all shortest red antipodal paths in an arbitrary legal coloring; NORI1 remains OPEN.

ADDITIONAL INDEPENDENT TWO-SAT CHECK. /mnt/data/nori_xvi_quadratic_surplus_2sat_verify.py verifies directly from the symbolic binary pattern relations A=B, B!=C, A=0,C=0 that the full anchored triple is unsatisfiable, every pair remains satisfiable, and the minimum variable-deletion cost tau is one. This supports the dimension-uniform symbolic proof and the weighted generalization, independent of the full face-edge verifier.
