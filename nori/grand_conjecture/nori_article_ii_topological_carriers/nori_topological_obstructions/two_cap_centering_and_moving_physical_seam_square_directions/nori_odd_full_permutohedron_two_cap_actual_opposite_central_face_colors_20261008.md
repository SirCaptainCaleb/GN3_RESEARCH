# Full permutohedral Borsuk–Ulam forces an actual opposite-color central-window path packet with only two leftover cap directions

# Odd-dimensional FULL-SPHERE two-cap Tucker theorem: actual opposite central ordered-three-face colors and balanced physical i-edge positions

Let n=2m+1>=7 be ODD, and let c be ANY active NORI ordered-three-face binary coloring satisfying c(bar F,reverse pi)=1-c(F,pi). Fix ANY physical cube root x, ANY distinguished direction i∈[n], and ANY two other distinct directions a,b∈[n]\{i}. Put T=[n]\{i,a,b}, so |T|=n-3.

Let P_n be the genuine centrally symmetric (n−1)-dimensional permutohedron, whose original vertices v_pi correspond to ALL ACTUAL full antipodal cube geodesic direction permutations pi from x, with central antipodal involution pi→rev pi. Its boundary ∂P_n is an actual free antipodal sphere S^(n−2), of cohomological index n−2.

For each actual full order pi, define:
(1) v_i(pi)∈{0,1}^([n]\{i}) to be the projected actual physical i-edge position along its x-rooted full geodesic, namely root bits x_j XOR 1_{j BEFORE i in pi}. Under reversal, v_i(rev pi)=1−v_i(pi).
(2) q(pi)=the ACTUAL binary color of the CENTRAL ordered-three-face window of the full path: its index is j=m=(n−1)/2 out of the n−2=2m−1 windows. Since active NORI full-path physical reversal gives w(x,rev pi)=1−reverse(w(x,pi)), the central position j=m maps to ITSELF while its color complements:
  q(rev pi)=1−q(pi).
Thus epsilon(pi)=(-1)^q(pi)∈{+1,−1} is an honest Θ-ODD signed label of a genuine physical central ordered three-face window.

**THEOREM (FULL-SPHERE TWO-CAP ACTUAL COLOR PACKET).** For EVERY choices of x,i,a,b above, there exist at most n−1 ACTUAL full x-rooted antipodal geodesics with direction orders pi_1,...,pi_s, together with strictly positive weights alpha_r summing to1, such that:
A. ALL selected permutations lie in a common PROPER permutohedron face, hence share one nonempty proper prefix used-direction set S. Necessarily EITHER
  (EARLY CAP) S⊆{a,b}, so 1<=|S|<=2,
OR
  (LATE CAP) [n]\S⊆{a,b}, so n−2<=|S|<=n−1.
Therefore the packet lies in a literal one/two-direction endpoint-cap chart prescribed by a,b, and its full paths share the corresponding early or late physical cube vertex.
B. Their ACTUAL central ordered-three-face window colors include BOTH 0 and1, indeed
  sum_(r:q(pi_r)=0) alpha_r = sum_(r:q(pi_r)=1) alpha_r=1/2.
C. For EVERY coordinate j∈T, the weighted fraction of selected actual orders having j BEFORE i is EXACTLY1/2:
  sum_r alpha_r 1_{j appears before i in pi_r}=1/2.
Hence for each j∈T, at least one selected genuine full path traverses j before i and one traverses it after i.

**PROOF.** At each original permutohedron vertex v_pi prescribe the vector
  F(v_pi)=((v_i(pi)_j−1/2)_{j∈T}, epsilon(pi))∈R^{(n−3)+1}=R^(n−2).
Both blocks transform by NEGATION under central reversal pi→rev pi. Extend these original-vertex values continuously and equivariantly over ∂P_n, for example by taking at each proper face barycenter the arithmetic mean of values on that face's original permutation vertices and interpolating linearly on the antipodally equivariant barycentric face-flag triangulation. All face means and the resulting PL map satisfy F(τz)=−F(z).

By the Borsuk–Ulam theorem for the free antipodal sphere ∂P_n≅S^(n−2), this odd map to R^(n−2) has a zero z. Let H be the unique minimal proper permutohedron face containing z. Every vertex of the face-flag barycentric simplex containing z has F-value which is an arithmetic mean of actual original-permutation-vertex F-values inside H. Therefore 0 is in the CONVEX HULL of the actual vector values F(v_pi) for genuine permutation vertices pi of H. By Carathéodory's theorem in R^(n−2), at most n−1 genuine vertex vectors suffice for a positive convex representation 0=sum alpha_r F(v_pi_r).

The last scalar coordinate of F enforces sum alpha epsilon(pi_r)=0, so there are actual central window colors of BOTH bits and their weights each total1/2, proving B. The projected i-position coordinates enforce exactly the weighted before/after balances C (root bits x_j only complement positions, so centering-zero is equivalent to order fraction1/2).

Any proper permutohedron face H lies in a facet H_S fixing a nonempty proper prefix support S. If i∉S, every coordinate j∈S necessarily precedes i in EVERY permutation of H, so balancing in every j∈T forces S∩T=empty. Since i∉S too, S⊆[n]\(T∪{i})={a,b}, establishing EARLY CAP. If i∈S, each j outside S necessarily comes AFTER i in every permutation of H, so balancing forces T⊆S. Thus [n]\S⊆[n]\(T∪{i})={a,b}, giving LATE CAP. Finally a proper facet cannot contain both pi and rev pi, so the opposite central colors in this packet are not merely tautological full-path reversal copies. QED.

**WHY THIS IS A STRENGTHENING.** The previous index-(n−3) endpoint-opposed path nerve could balance n−3 i-edge coordinates with TWO leftover cap coordinates but could not simultaneously force an additional independent odd signed witness color. For ODD n, the central physical three-face color is itself an odd scalar on the FULL permutohedral boundary S^(n−2), whose index is ONE HIGHER. Consequently one gains genuine opposite-color central three-face windows at NO EXTRA CAP COST. This is a direct dimension-independent topology-first conclusion, with fully physical path/color provenance.

**EXACT REMAINING GRAND GAP.** The resulting central windows of colors 0 and1 can occur on DISTINCT physical three-faces, and their full paths need not have at most one color change. The early/late two-cap support S may be {a,b} (or its complement), not necessarily separate the fixed directions a,b. Therefore the theorem does NOT itself produce the exact same-root complementary reversed-two-tail monochromatic reachability intersection. One must force alignment/transport of the central opposite-color physical faces through the MOVING root/seam square, or show that the genuinely balanced packet contains compatible monochromatic branches. No such unconditional extraction is proved here.
