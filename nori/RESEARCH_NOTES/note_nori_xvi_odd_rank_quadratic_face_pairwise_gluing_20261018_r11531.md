# Quadratic face gluing, anchored incompatibility, and orbit-capacity limits

- Stable ID: note_nori_xvi_odd_rank_quadratic_face_pairwise_gluing_20261018_r11531
- Author: Independent NORI1 mathematician
- Primary home: subsection:obstruction_compatibility_and_a_programme_for_nori1_closure
- Labels: NORI1, Article-XVI, quadratic-cut, face-compatibility, pairwise-to-global, antipodal-parity, structural-theorem, verified
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11531_1
- Updated session: session_nori_r11531_1
- Disposition: none
- Successor: none

## Related references

- note:note_nori_xvi_weighted_face_cut_dual_20261018_r11531
- note:note_nori_xvi_near_minimum_monotone_face_cut_rigidity_20261018_r11531

## Research note

# Pairwise-to-global gluing for quadratic-minimum blue face cuts of odd rank

SETUP. Let n=r+2 with odd r>=5. Fix a common facet H={x_(n-1)=0} of Q_n. Take any finite family of rank-r faces F inside H, each with two designated opposite poles s_F,t_F. Require the entire source and sink face stars red and require every full monotone geodesic between the poles to contain blue. Assume each face is constrained to use the minimum r(r-1) blue edges. The earlier quadratic minimum-rigidity theorem gives precisely two possible patterns: all rank1-to-rank2 edges blue measured from s_F, or all rank(r-2)-to-rank(r-1) edges blue. Write L_F(p) for the corresponding rank1-to-rank2 blue layer centered at p in {s_F,t_F}, all other F edges red.

LEMMA 1 (overlap restriction). Two distinct rank-r faces F,G in a common rank-(r+1) facet are disjoint or meet in an (r-1)-face K. Write d=r-1>=4. If chosen center p of F lies in K, L_F(p) restricted to K is the whole rank1-to-rank2 BLUE layer about p IN K; if p lies outside K, its restriction is the complete blue edge star about the projection p' in K. This follows by comparing the Hamming-distance rank from p with the rank from its projection, which differs by zero or one.

LEMMA 2 (compatibility and parity). For d>=4, the two K-patterns cannot coincide: the star has d blue edges while the rank1-to-rank2 layer has d(d-1). Each pattern also determines its center: a star has a unique degree-d blue center, while the blue rank1 layer has precisely d vertices of blue degree d-1>=3, whose common neighbor is the center. Thus compatible overlapping prescriptions have their selected centers either both inside K and equal, or both outside K with the same projection. In both cases those centers have the same ambient vertex parity. Simultaneously replacing the two centers by the other pole of their respective faces preserves compatibility: both inside/outside statuses toggle and both shared projections are complemented. This also holds when F=G with different prescribed pole presentations; disjoint faces impose no restriction.

THEOREM (odd-rank pairwise gluing). Assume every PAIR of prescribed rank-r faces admits some choices of their two saturated quadratic patterns compatible on all shared edges. Then all faces simultaneously admit such patterns inside ONE legal antipodally odd coloring of Q_n. PROOF. Since r is odd, each opposite-pole pair has precisely one even-parity pole. Choose that even pole for every face. For each pair, by hypothesis there is a compatible pair of centers; by Lemma 2 they have equal parity. If odd, switch both to the opposite poles to obtain a compatible even-even pair. Hence the global even-pole choices agree on every shared edge. Color all remaining common-facet edges freely; every antipodal edge mate lies in the disjoint opposite facet. Assign it the complemented color and complete other edge orbits arbitrarily. QED.

CONSEQUENCE. The previously proved pairwise-viable but jointly impossible three-face BLUE endpoint-star patterns cannot be reproduced within this family of saturated quadratic cuts of odd rank and a common facet. The next global NORI1 forcing mechanism must use cuts above the quadratic minimum, pairwise-incompatible face demands, additional red path anchors, or more general face arrangements. The theorem is a structural limitation of a SPECIFIED programme, not NORI1 closure. For even r, poles have the same vertex parity and the proof does not apply.

INDEPENDENT VERIFICATION. /mnt/data/nori_xvi_quadratic_layer_gluing_verify.py exhausts every oriented rank-r face within a single facet of Q7 (r5; 384 descriptions) and Q9 (r7; 2048 descriptions), testing every pair and all four layer choices. All nonempty compatibility matrices are 1111, 0110, or 1001 (binary mask interpreted as compatible pole choices); their allowed centers have matching parity. Q7 pair frequencies: impossible 63360, free 6144, opposite-label 2112, same-label 1920. Q9 frequencies: impossible 1935360, free 131072, opposite-label 15360, same-label 14336. /mnt/data/nori_xvi_quadratic_layer_pairwise_gluing.md contains the self-contained dimension-uniform proof. No full dimensional NORI1 proof is claimed.

## A positive anchored two-face forcing theorem, and a capacity-dual limitation

THEOREM (two anchored faces must pay a blue surplus). For any r>=5 put n=r+2 and work in common facet x_(r+1)=0. Let F be the r-face x_0=0, free directions {1,...,r}; let G be the r-face x_1=0, free directions {0,2,...,r}. Give both the distinguished source pole 0 and the opposite sink pole within that face. REQUIRE: both source/sink endpoint stars in each face are RED, and each face blocks every RED full monotone antipodal geodesic. In addition prescribe two RED edges:
  eF: direction 1 from v=sum_(i=2)^(r-1)e_i to v+e_1, belonging to F but not G;
  eG: direction 0 from e_2 to e_2+e_0, belonging to G but not F.
Then at least one face has >=r(r-1)+1 BLUE edges.

PROOF. If both faces had <=T=r(r-1) blue edges, the established quadratic lower bound and equality rigidity (r>=5) would force each blue set to be one complete interior layer, early rank1-to-rank2 or late rank(r-2)-to-rank(r-1). The red anchor eF lies in F's late layer, so F must use the EARLY layer; eG lies in G's early layer, so G must use the LATE layer. The overlap K=F intersect G is an (r-1)-face with d=r-1>=4. F's early layer restricts on K to the entire rank1-to-rank2 layer of K, with d(d-1) blue edges. G's late layer, viewed as the early layer around G's opposite pole outside K, restricts on K to one full blue star, with d blue edges. These cannot describe the same colored overlap since d(d-1)>d. Contradiction. The anchors themselves are consistent and each individual face can realize its preferred minimum cut separately.

FINITE SHARPNESS (Q7). A reproducible integer-linear-program model for r=5,n=7 uses 128 undirected edges in F union G, 240 monotone full-geodesic clauses, red endpoint-star constraints and the two red anchors. The optimized minimum of max{Nblue(F),Nblue(G)} is 21=T+1, and one attained assignment has counts 20,21. Hence this lower bound is sharp at r=5. No sharpness claim for higher r is made. Verifier: /mnt/data/nori_xvi_quadratic_anchor_milp_verify.py. Dimension-uniform paper: /mnt/data/nori_xvi_quadratic_layer_pairwise_gluing.md.

THEOREM (unanchored weighted-capacity limitation). In the previous antipodal edge-orbit weighted face dual, let lambda_F>=0 be any face multipliers, all face ranks r_F>=2, and let W(e)=sum_(F containing e)lambda_F / C(r_F-1,k_F(e)). Let U=sum_(antipodal orbits {e,bar e})max{W(e),W(bar e)} and L=sum_F lambda_F*r_F. Each rank-r face has total weight sum_(edges e in F)1/C(r-1,k_F(e))=r^2. Therefore
  U >= (1/2)sum_(all edges)W(e)=(1/2)sum_F lambda_F*r_F^2 >=sum_F lambda_F*r_F=L.
So the bare face-blocking inequalities, without any fixed edge colors or other strengthened constraints, can NEVER violate the weighted orbit-capacity test. Any successful use of that dual method must employ red path anchors or another source of asymmetry; this is a proved structural limitation, not a claim that all dual methods fail.

RESEARCH STATUS. The odd-rank unanchored pairwise-to-global theorem in the preceding section remains valid. The new anchored theorem provides a positive shared-edge forcing mechanism across two faces, applicable for every r>=5. The missing unrestricted step is to derive sufficiently many such anchored overlapping face demands from shortest red antipodal paths in every hypothetical NORI1 counterexample. NORI1 is OPEN.
