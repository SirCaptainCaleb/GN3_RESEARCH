# Two-cap centering and moving physical seam-square directions

# Two-cap centering and moving physical seam-square directions

The antipodal boundary sphere of the full permutohedron supports an odd map formed from projected coordinate positions together with actual central ordered-face colors. Its zero yields a convex packet of complete geodesics in a common proper face. The face leaves at most two endpoint-cap directions, suggesting a physical two-coordinate seam square on which a repair might occur.

## Equivariant suspension-LIFT criterion: witness-compatible fillings generate genuine antipodal cohomological index

Let X be a finite CW complex (e.g. a simplicial/cubical NORI witness complex) with a FREE continuous involution tau, and suppose X=A∪tau(A) for subcomplex A. Write C=A∩tau(A), a tau-invariant genuine intersection subcomplex. Throughout S^k carries the standard antipodal involution and its upper hemisphere in S^(k+1) is a closed (k+1)-ball with equator S^k.

**Theorem 1 (equivariant index LOWER bound from a one-sided filling).** Suppose there exists a continuous equivariant map
  g:S^k -> C,   g(-u)=tau(g(u)),
AND the map g regarded as an ordinary map S^k->A is nullhomotopic, equivalently extends to a continuous map
  G:D^(k+1) -> A
whose boundary restriction is g. Then there exists a continuous tau-equivariant map
  F:S^(k+1) -> X.
In particular, the first Stiefel–Whitney class w∈H¹(X/tau;F2) has
  w^(k+1) != 0.
Thus the cohomological antipodal index of X is at least k+1.

**Proof.** Regard the upper hemisphere H_+ of S^(k+1) as D^(k+1), its equator as S^k, and use G to define F on H_+. On the lower hemisphere H_-= -H_+, define
  F(-z)=tau(G(z))   for z∈H_+.
On the equator, where both hemisphere prescriptions apply, they agree because G(-u)=g(-u)=tau(g(u))=tau(G(u)). Thus the gluing lemma yields a continuous globally equivariant F:S^(k+1)→X. Passing to free-involution quotients gives f:RP^(k+1)→X/tau; the pullback of the cover's w is the tautological generator a∈H¹(RP^(k+1);F2), by equivariance/pullback of principal Z2-bundles. Hence f*(w^(k+1))=a^(k+1)≠0, establishing w^(k+1)≠0. QED.

**Theorem 2 (relative suspension sandwich for CONTRACTIBLE A).** If A is nonempty and contractible (in particular if A is a literal simplex or cone), then every equivariant map g:S^k→C for k>=0 has an ordinary nullhomotopic composite S^k→A, so the suspension lift applies. Consequently
  ind_Z2(C)+1 <= ind_Z2(X)
provided C is nonempty and the index is defined via maximum nonzero w power. The general UPPER index bound from Item nori_equivariant_two_shore_overlap_dimension_bounds_antipodal_index_20261008 says
  ind_Z2(X) <= dim(C)+1.
Thus for a contractible one-shore carrier A,
  ind_Z2(C)+1 <= ind_Z2(X) <= dim(C)+1,
where the left inequality requires an equivariant map from a sphere S^k realizing ind(C); a free complex can have high cohomological index without an equivariant sphere map from that dimension, so in FULL generality replace ind(C) on the left by
  coind(C)=max{k: exists equivariant S^k→C}.
The rigorously valid sandwich is
  coind(C)+1 <= ind(X) <= dim(C)+1.
This proviso distinguishes topological index from coindex; conflating them would be false.

**Corollary 3 (an actionable NORI monochromatic-disk test).** Let X=X_c be the actual cubical center-square witness complex of an active NORI coloring, and A=X_0 be the genuine color-0 certified square subcomplex together with all physical cube vertices. Let C=X_0∩X_1 be its color-overlap subcomplex. Suppose C contains a tau-equivariant closed loop g:S¹→C: geometrically, an antipodally paired physical loop whose full set of edges each admits BOTH-color genuine monochromatic centered four-path certificates. If this loop also bounds a continuous disk in X_0 (for example a finite combinatorial disk tiled by color-0 certified squares with compatible boundaries), then
  w_1(X_c/tau)^2≠0.
This is exactly the missing TOP-DIMENSIONAL counterpart of the previous result: absence of any common-edge certificate forces w1²=0, while the presence of an equivariant common-edge CYCLE which can be capped by honest monochromatic squares forces w1²≠0.

**Important geometric warning.** A cycle being a mod-2 homological boundary in X_0 does NOT automatically give a nullhomotopy; the theorem assumes an actual disk/nullhomotopy. A single isolated common edge, even accompanied by its antipodal mate, gives no equivariant S¹ loop unless there are connecting common edges.

**Corollary 4 (the EXACT root-profile two-shore carrier).** Let K=A∪tau(A) be the exact LABEL-SPACE carrier of nori_reversed_tail_root_profile_nerve_tucker_label_reduction_20261008 and nori_reversed_tail_mixed_profile_interface_equivariant_suspension_20261008, where A=union_x Delta(L_x), C=A∩tau(A). The universal singleton support labels guarantee that A is a CONE, not generally a simplex, hence contractible. Therefore any equivariant map S^k→C caps in A and induces an equivariant S^(k+1)→K; an equivariant loop in C yields nonzero w1² on K. The SIGNED-ROOT NERVE N is a DIFFERENT complex: its positive and negative vertex shore simplices do not themselves cover the mixed faces, and one must NOT write N=A∪tau(A) with only those shore simplices. Rather, the previously proved equivariant nerve equivalence K≃_tau N transfers the resulting cohomological index statement from K to N. The challenge is to build the equivariant loop inside actual mixed-label C, where each simplex has real common-reachability certificates.

**Research strategy: topology first, combinatorics inside it.** Pursue a growing family of genuine root/terminal-memory witness cells to construct an equivariant circle (and higher sphere) in C. The four-edge opposite-color reversed-tail diamonds are local candidate 1-cells, but they prove SAME support for the two reversed tails, whereas the GRAND fixed point needs COMPLEMENTARY support. They cannot be treated as cells of C until that compatibility is established. If a valid equivariant loop in C is established, the index rises through the cone structure. The remaining high-index-to-fixed-point step must then use the root-probability difference field V(a,b)=a-b and the exact deleted-product dimension obstruction: index or coindex at least p−1 (where p is retained profile count) is too high for a hypothetical no-closure carrier Z⊆S^(p−2). No such high-index lower bound is presently proved.

**No grand-closure claim.** This result is a complete general topological lemma and an exact set of sufficient witness conditions. The major combinatorial problem is supplying honest overlap loops and their fillings from the physical ordered-three-face constraints, and then reaching the required index threshold.

## Odd-dimensional FULL-SPHERE two-cap Tucker theorem: actual opposite central ordered-three-face colors and balanced physical i-edge positions

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

## Odd-dimensional full-sphere TWO-CAP Tucker packet contains opposite CENTRAL face colors at macroscopically separated actual i-edge positions

Let n>=7 be odd, c any active NORI ordered-three-face coloring, x any cube starting root, i any distinguished direction, and a,b any two other distinct directions. Put T=[n]\{i,a,b}, of size k=n−3. The proved actual FULL permutohedron sphere Borsuk–Ulam theorem nori_odd_full_permutohedron_two_cap_actual_opposite_central_face_colors_20261008 (or the all-dimensional theorem's odd specialization) gives ACTUAL full x-rooted cube-geodesic direction orders pi_1,...,pi_s all in ONE common proper permutohedron face, with convex weights alpha_r>0, sum=1, satisfying:
- common EARLY/LATE one- or two-direction used-support cap S⊆{a,b} or complement(S)⊆{a,b};
- each REAL central ordered-three-face color q(pi_r)∈{0,1}, with sum_(q=0)alpha=sum_(q=1)alpha=1/2;
- for each j∈T, sum_r alpha_r 1_{j precedes i in pi_r}=1/2.

**THEOREM (quantitative opposite-color actual physical edge separation).** Among these <=n−1 genuine full-path packet witnesses there exist TWO ACTUAL orders pi_0,pi_1 satisfying ALL:
1. Their CENTRAL physical ordered-three-face windows have OPPOSITE actual NORI colors: q(pi_0)=0, q(pi_1)=1.
2. The unique physical i-edges visited by the two x-rooted full cube geodesics lie at projected cube positions v_i(pi_0),v_i(pi_1) whose Hamming distance, on coordinates in T alone, is at least
\[
\boxed{d_H(v_i(pi_0)|_T,v_i(pi_1)|_T)\ge \left\lceil\frac{n-3}{2}\right\rceil.}
\]
3. Their full permutations still lie in ONE common proper permutohedron face, and so share one actual EARLY or LATE used-direction CAP of at most two coordinate directions, chosen from the arbitrarily prescribed pair a,b. Hence their full geodesics meet at the common early/late physical cube vertex x XOR S. The pair cannot simply be related by full antipodal direction-order reversal, because their orders lie in a proper face together.

**PROOF.** Choose two INDEPENDENT random actual packet permutations P_0,P_1, conditioning P_0 to have actual central color0 and P_1 color1, and sampling within each color class with probabilities 2alpha_r (these sum to1 within each class). For each j∈T let
 u_j=Pr[j appears BEFORE i in P_0],
 v_j=Pr[j appears BEFORE i in P_1].
Because the two color classes each have total original weight1/2 and the unconditional coordinate-before-i probability is1/2,
 (u_j+v_j)/2=1/2, hence v_j=1-u_j.
The probability that the two independently chosen actual orders DISAGREE on the before-i indicator for coordinate j is therefore
 u_j(1-v_j)+(1-u_j)v_j
 =u_j^2+(1-u_j)^2
 \ge 1/2.
Sum these probabilities over all k=n−3 coordinates j∈T:
\[
\mathbb E\left[\#\{j∈T:\text{their orders place j on opposite sides of i}\}\right]\ge k/2.
\]
The Hamming distance of the two literal physical projected i-edge positions equals this disagreement count because each edge location bit is root bit x_j XOR its before-i indicator. The distance is integer-valued; therefore at least one ACTUAL opposite-central-color pair in the packet has distance >=ceil(k/2), proving item2. Items1 and3 hold for every such conditioned pair by construction and the common proper-face property. QED.

**TIGHTNESS OF THE AVERAGING LEMMA.** The inequality u²+(1-u)²>=1/2 is sharp at u=1/2, so one cannot improve this half-coordinate separation constant solely from the conditional central-color balance and individual coordinate-position balance; extra physical NORI compatibility is necessary.

**TOPOLOGICAL RELEVANCE.** For EVERY odd n>=7, EVERY root x and every prescribed three directions i,a,b, one can force TWO ACTUAL full antipodal geodesics sharing a tiny (size<=2) endpoint cap, with genuine opposite physical central ordered-face colors and physical i-edge positions differing on nearly half the remaining cube coordinates. This is a high-dimensional, root-mobile color-separation certificate suitable for a Hartman/Hex connector attempt. It does NOT ensure the two central physical faces intersect, that their orders give monochromatic complementary reversed-two-direction terminal tails, or that either whole path is one-switch. The global grand NORI forcing theorem remains open.

One must allow that physical seam square to move with the chosen permutohedron face: fixing its coordinate pair in advance destroys the required antipodal index. This is an exact limit of the current topological strategy.
