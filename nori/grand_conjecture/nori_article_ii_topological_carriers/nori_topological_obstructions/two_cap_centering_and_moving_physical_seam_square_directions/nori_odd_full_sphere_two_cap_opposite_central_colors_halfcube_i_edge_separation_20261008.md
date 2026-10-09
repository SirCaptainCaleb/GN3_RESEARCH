# Odd NORI full-sphere Tucker forces opposite actual central face colors at i-edge positions separated on at least half the coordinates

# Odd-dimensional full-sphere TWO-CAP Tucker packet contains opposite CENTRAL face colors at macroscopically separated actual i-edge positions

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
