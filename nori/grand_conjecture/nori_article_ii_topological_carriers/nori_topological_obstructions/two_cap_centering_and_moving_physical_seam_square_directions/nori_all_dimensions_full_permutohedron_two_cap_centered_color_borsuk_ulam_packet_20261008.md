# All-dimensional full-sphere two-cap Tucker packet forces an actual central switch or monochromatic center cores of both colors

# ALL-DIMENSION full-permutohedral two-cap centered-color forcing with no loss of topological index

Let n>=6, c be ANY active NORI ordered-three-face binary coloring, x∈Q_n any prescribed root, i a distinguished coordinate direction, and a,b two distinct directions other than i. Put T=[n]\{i,a,b}, |T|=n−3. Work on the FULL standard permutohedron boundary ∂P_n≅S^(n−2), whose original vertices correspond to all actual full n-edge geodesic orders pi from x, and whose antipodal involution reverses the direction word.

For each original order pi, let w(pi) be its actual physical ordered-three-face window-color word of length n−2. Define one REAL centered-window scalar h(pi) as follows:
- If n=2m+1 is ODD, let
  h(pi)=2w_m(pi)−1∈{−1,+1},
  where m is the unique central three-face window index.
- If n=2m is EVEN, let
  h(pi)=w_(m−1)(pi)+w_m(pi)−1∈{−1,0,+1},
  where positions m−1,m are the two central three-face windows.

**LEMMA (physical NORI reversal makes h ODD).** In EVERY dimension, h(rev pi)=−h(pi). Proof: actual physical full-path reversal at fixed root x gives w(rev pi)=1−reverse(w(pi)). For odd n the single central window maps to its complemented self, so 2w−1 negates. For even n the two central windows swap and each complements, so (1−v)+(1−u)−1=−(u+v−1). No additional face-color symmetry is assumed.

For any full actual direction order pi and fixed i, let v_i(pi)_j∈{0,1} for j≠i be the projected physical position of the unique i-edge on the x-rooted full path:
  v_i(pi)_j=x_j XOR 1_{j occurs before i in pi}.
Then v_i(rev pi)=1−v_i(pi). At each original vertex define the actual color/geometry vector
  F(v_pi)=((v_i(pi)_j−1/2)_(j∈T),h(pi))∈R^(n−2).
Extend it equivariantly by face-barycenter averages and PL interpolation on the barycentric subdivision of the full permutohedron boundary, yielding a continuous odd map F:∂P_n→R^(n−2).

**THEOREM (physical two-cap centered-certificate Borsuk–Ulam packet).** For EVERY choices of n,c,x,i,a,b above, there exist at most n−1 ACTUAL full x-rooted antipodal geodesic direction orders pi_1,...,pi_s, with positive convex weights alpha_r totaling1, such that:
1. All the orders belong to ONE common proper permutohedron face and hence share a nonempty proper initial used-coordinate support S which is necessarily EITHER S⊆{a,b}, 1<=|S|<=2, OR [n]\S⊆{a,b}, 1<=|[n]\S|<=2. Thus they form a genuine same-root one- or two-direction EARLY/LATE CAP packet, with common actual physical cube vertex after the corresponding cut.
2. For each j∈T, the selected actual paths are perfectly balanced in which occurs before i:
   sum_r alpha_r 1_{j before i in pi_r}=1/2.
   Thus BOTH relative orders of j and i occur among the selected genuine paths.
3. Their actual center-window colors satisfy
   sum_r alpha_r h(pi_r)=0.
   In ODD dimensions, the packet necessarily includes genuinely colored CENTRAL ordered-three-face windows of BOTH 0 and 1, each with total convex weight1/2.
   In EVEN dimensions, EITHER at least one selected actual full path has h=0, meaning its TWO central consecutive ordered-three-face windows have DIFFERENT colors (a real central switch), OR the packet contains paths with h=−1 and h=+1, meaning genuine MONOCHROMATIC CENTERED FOUR-edge subpaths of BOTH colors 0 and1. Either alternative may coexist; the disjunction is exact.

**PROOF.** The full permutohedron boundary is an antipodal (n−2)-sphere, so the odd continuous F into R^(n−2) has a zero by Borsuk–Ulam. As each face-barycenter value is an average of ACTUAL permutation-vertex vectors from that face, the zero lies in the convex hull of genuine full-path vectors belonging to a common proper face H. Carathéodory's theorem yields at most (n−2)+1=n−1 genuine full-path vertices and positive weights representing zero. Vanishing of the first n−3 coordinates gives condition2; vanishing of the final scalar gives condition3. Every proper permutohedron face is contained in some facet H_S enforcing first-block support S. If i∉S, all directions in S precede i on every selected order; the balanced T-coordinates force S∩T=empty, so S⊆{a,b}. If i∈S, all directions outside S follow i, so T⊆S, yielding [n]\S⊆{a,b}. This proves condition1. For odd n, h takes only −1,+1, so zero average requires both with weights1/2. For even n, h∈{−1,0,+1}: zero average either uses at least one zero or requires both signs, which translate exactly to the stated physical ordered-window certificates. QED.

**WHY THIS IS A GENUINE TOPOLOGICAL STEP.** The construction uses the EXTRA UNIT of cohomological index of the FULL (n−2)-sphere rather than the endpoint-opposed zero-level (n−3)-index nerve. It buys an ACTUAL CENTRAL FACE-COLOR constraint without leaving a third unbalanced endpoint-cap direction: the leftover cap has EXACTLY two directions a,b. This is a physically grounded, all-dimension generalization of Item nori_odd_full_permutohedron_two_cap_actual_opposite_central_face_colors_20261008.

**WHAT IS NOT YET PROVED.** Even though the packet has two-direction cap geometry and genuine central one-change/monochromatic-opposite-color witnesses, those central windows need not be co-located on the same physical face or extend to the complementary same-root REVERSED-TWO-TAIL monochromatic reachability branches of the exact grand extraction theorem. In particular a central switch along a full path does not imply the path has ONLY one switch, and an opposite-color pair of four-edge monochromatic central cores need not share a middle-square connector. An additional global physical order-exchange/Hex/Tucker seam-compatibility forcing theorem is necessary. The unrestricted active NORI grand conjecture remains open.
