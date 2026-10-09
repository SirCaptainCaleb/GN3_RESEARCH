# Single-bit Tucker labeling forces two genuine endpoint-opposed NORI geodesics through a common near-midpoint cube vertex

# NEAR-BISECTION TUCKER THEOREM: a single odd switch-side bit forces genuine compatible full NORI paths meeting near the cube middle

Let n>=7, let c be ANY active reversal-antipodally odd NORI ordered-three-face coloring of Q_n, and fix EVERY physical cube root x. Let K_x be the genuinely witnessed endpoint-opposed full-path permutohedral face nerve; its proven mod-two antipodal cover class w satisfies
 w^(n-3) != 0.

Every vertex pi of K_x is a genuine full x-rooted antipodal cube geodesic whose first and last ordered-three-face colors are opposite. Hence its switch-position set S(pi)⊆{1,...,m}, m=n-3, is ODD and nonempty. Write j_med(pi) for its unique median element.

**CANONICAL ONE-BIT ODD LABEL.** Define eps(pi)∈{+1,-1} by
- eps(pi)=+1 if j_med(pi)<(m+1)/2;
- eps(pi)=-1 if j_med(pi)>(m+1)/2;
- only when m is odd (equivalently n even), if j_med(pi)=(m+1)/2, put eps(pi)=+1 if p_(n/2)<p_(n/2+1) in a fixed direction-name total order and eps(pi)=-1 otherwise.
Under the genuine NORI full-path involution pi↦rev pi at SAME x, the window word becomes the reverse AND complement, so the switch set reverses positions j↦m+1-j; at the exact central switch the central ordered direction names interchange. Hence
  eps(rev pi)=-eps(pi).
The label uses only ONE signed bit, unlike the detailed ±ceil((n-3)/2)-valued median position label.

**MAIN THEOREM (genuine near-midpoint Tucker connector, ALL n>=7).** Put
  k=floor((n-2)/2).
Then at EVERY x there are two genuinely endpoint-opposed FULL antipodal NORI geodesics (x,pi),(x,sigma) such that:
1. eps(pi)=−eps(sigma). Their median switches lie on opposite sides of the word center (or at least one median is central, in which case the assigned central direction-name comparison provides the sign).
2. Their direction orders share a PREFIX USED-DIRECTION SET S at some rank ell satisfying
       k <= ell <= n−k.
3. They therefore meet at the SAME ACTUAL PHYSICAL INTERMEDIATE CUBE VERTEX y=x XOR S after ell steps, and both have at least k distinct-coordinate edges on EACH side of the meeting.
4. Their permutations are not simply mutual reversals, because no proper permutohedron face contains centrally opposite original vertices.

Consequently for every n>=9, k>=3, and both halves admit genuine internal three-face windows. The shared cut is MACROSCOPICALLY NEAR THE MIDDLE: when n=2q it has rank among q−1,q,q+1; when n=2q+1 it has rank among q−1,q,q+1,q+2. This is much stronger geometry than the original arbitrary proper-rank Tucker pair and strictly sharper in cut location than the signed median ±r variant.

**PROOF (dimension bound for low-rank outer facets, followed by relative index).** Define O_k to be the subcomplex of K_x consisting of simplices whose actual order-permutation vertices share an outer prefix support T of size |T|<=k−1 or |T|>=n−k+1. This is the union of one full simplex D_T per such T, with D_T containing the endpoint-opposed full permutation vertices in the permutohedron facet indexed by T.

As proved in nori_macroscopic_inner_cut_tucker_median_complement_actual_full_paths_20261008, the finite equivariant nerve of the cover {D_T} consists only of strict inclusion chains of T, so its dimension is <=2k−3, and an equivariant cover-nerve map O_k→N gives w^(2k−2)|O_k=0. A small invariant regular neighborhood U⊃O_k has the same cohomological vanishing.

Interpolate the single-bit vertex labels eps∈{±1} affinely to an odd PL scalar f:|K_x|→R. Suppose, contrary to the desired conclusion, every zero of f lies in O_k. Then on the invariant open complement V=|K_x|\O_k the odd map f is NONZERO and its sign gives an equivariant map V→S^0, so w|V=0. The open cover U∪V=|K_x| therefore has w^(2k−2)|U=0 and w|V=0. Their relative cup product implies
   w^(2k−1)=0 on K_x/tau.
But for k=floor((n-2)/2), 2k−1<=n−3, contradicting the established nonzero w^(n−3). Thus there exists z∈f^−1(0)\O_k.

Let sig_z be the smallest supporting simplex of z. A scalar convex combination of ±1 equals zero in its relative interior ONLY when the supporting simplex contains actual vertices pi,sigma with opposite eps. The simplex lies in K_x but NOT in O_k; consequently all its vertices belong to some common proper permutohedron facet H_S, and NO containing facet can have an outer rank. Hence k<=|S|<=n−k, proving the shared near-mid prefix support. Both actual geodesics meet at y=x XOR S and the reversed copy cannot belong to H_S. QED.

**TOPOLOGY-FIRST GRAND RESEARCH TARGET.** Combining this theorem with nori_permutohedral_tucker_common_vertex_hub_two_seam_splice_defect_additivity_20261008, every n>=9 and every x has a genuine TWO-PATH prefix/suffix exchange RECTANGLE centered at a cut near n/2. Its only two new windows are actual ordered three-faces through the common intermediate physical vertex y. If y is a locally rigid bichromatic hub and both chosen branch-end colors match the hub's certified middle-direction bits across opposite classes, the splice defect equals the sum of branch defects plus precisely ONE; two monochromatic branch sides give full grand closure. These extra color compatibility conditions are NOT forced by the present topological theorem. A future cellwise combinatorial extraction must control them. Unrestricted NORI grand closure remains open.

**METHOD TRANSFER.** More generally in a free involution permutohedral face nerve with w^d!=0, ANY odd ±r signed-labeling forces a complementary pair of genuine original vertices in an inner rank-k facet whenever r+2k−2<=d. For the one-bit eps, r=1 gives a near-bisection with k close to n/2. The formal separation between a high-index topological forcing step and an exact physical ordered-window splice condition is deliberate.
