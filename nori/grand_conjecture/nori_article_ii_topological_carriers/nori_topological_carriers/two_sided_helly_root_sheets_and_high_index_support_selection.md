# Two-sided Helly root sheets and high-index support selection

# Two-sided Helly root sheets and high-index support selection

A two-sided monochromatic path has an initial root sheet, a terminal sheet and ordered overlap memory. When all admissible path witnesses sharing a physical root are assembled into a nerve, a Helly property may hold for the literal root sheets while failing for the compatibility needed to splice two different paths. This section isolates the corresponding dimension and index phenomena.

## Macroscopic-cut Tucker theorem: genuine endpoint-opposed NORI geodesics meet at a central-rank physical vertex

Let n>=7 and let c be ANY active NORI binary coloring of genuine PHYSICAL ORDERED three-faces on Q_n, with c(bar F,rev pi)=1-c(F,pi). Fix ANY cube root x.

Let K_x be the genuine endpoint-opposed permutohedral face nerve of Item nori_permutohedron_actual_opposite_endpoint_geodesic_star_nerve_high_index_20261008. Its vertices are ACTUAL full rooted geodesics (x,pi) with opposite first/last three-face window colors, and a simplex means that its order-permutation vertices all lie in a common proper face of the (n−1)-dimensional standard permutohedron P_n. Its reversal involution is free, and the established theorem gives
 w^(n−3) != 0 in H^(n−3)(|K_x|/tau;F2).

For each actual endpoint-opposed full geodesic pi, let m=n−3 be the number of internal switch positions and let j_*(pi) denote the MEDIAN of its ODD set of switch positions. Give pi the signed MEDIAN-TUCKER label lambda(pi)∈{±1,...,±r}, r=ceil((n−3)/2), as defined in proved Item nori_genuine_endpoint_opposed_permutohedral_tucker_complementary_median_switch_pair_20261008: the sign records whether its median switch lies before or after the midpoint; at an exact central switch (when n is even) use a signed comparison of the two central direction names to resolve the reversal-fixed median. Then lambda(rev pi)=−lambda(pi). Two opposite median labels imply mirrored median switch positions, or two central switches with opposite signed central-direction comparisons.

**THEOREM (INTERIOR / MACROSCOPIC TUCKER CUT).** Put
 k=floor((n+1)/4).
For EVERY active NORI coloring, EVERY physical root x and EVERY n>=7, there exist TWO actual rooted full endpoint-opposed antipodal geodesics (x,pi),(x,sigma), satisfying:
1. lambda(pi)=−lambda(sigma);
2. their full coordinate permutations possess a COMMON nonempty PROPER PREFIX SUPPORT S with
       k <= |S| <= n−k;
3. the two actual physical paths therefore pass through the SAME intermediate cube vertex y=x XOR S at the SAME time |S|, and each has at least k edges on each side of this cut;
4. sigma != rev pi (indeed a proper permutohedron facet never contains a pair of centrally antipodal permutation vertices).

For n>=11, k>=3, so each of the two sides contains at least ONE genuine internal ordered-three-face window. For n>=15, k>=4, and asymptotically the cut lies between roughly n/4 and 3n/4. This substantially strengthens the earlier unrestricted proper-cut Tucker pair.

**Proof.** We prove a general zero-localization lemma.

Let X=|K_x|, with free involution tau and nonvanishing w^d for d=n−3. Let lambda:X^(0)->{±1,...,±r} be ANY antipodally odd labeling; extend the corresponding signed standard basis vectors ±e_j by affine interpolation to an odd PL map f:X->R^r.

Fix 2<=k<=floor(n/2). Define the OUTER-CUT SUBCOMPLEX O_k⊆K_x as the union, over all nonempty proper direction sets T satisfying either |T|<=k−1 OR |T|>=n−k+1, of the full simplex on the actual endpoint-opposed permutation vertices whose FIRST |T| directions form precisely the set T. Every such simplex lies in the corresponding standard permutohedron facet H_T.

**Lemma A: ind(O_k)<=2k−3.** For each permitted T, write D_T for that full simplex. These finite closed subcomplexes cover O_k. A nonempty intersection D_T1∩...∩D_Ts can exist only when the T_i form a STRICT INCLUSION CHAIN: a full direction permutation can begin with EVERY T_i precisely if the sets are nested. An allowed strict chain uses at most k−1 distinct low ranks and k−1 distinct high ranks, totaling at most 2k−2 vertices. Hence the nerve N of the cover has dimension <=2k−3.

The cover is equivariant under permutation reversal, which carries H_T to H_(T^c). The nerve carries the induced involution T->T^c; no nonempty chain is invariant, since a nonempty proper T and its disjoint complement can never be comparable. Thus N is a free involution complex of dimension <=2k−3.

Using an arbitrarily small equivariant open thickening of the finite compact subcomplexes D_T inside O_k, chosen sufficiently small to preserve ALL intersection patterns (possible because the cover is finite and each forbidden finite intersection has a positive minimum max-distance), an equivariant partition of unity gives a continuous equivariant map |O_k|->|N|. Therefore w^(2k−2) vanishes on O_k/tau. A regular invariant neighborhood U of O_k in X retracts equivariantly onto O_k, so w^(2k−2)|U=0.

**Lemma B: if d >= r+2k−2, an f-zero lies OUTSIDE O_k.** Suppose not: Z=f^(-1)(0)⊆O_k. Let V=X\O_k, an invariant open subset avoiding f-zeros. On V, normalized f/||f|| defines an equivariant map to S^(r−1), forcing w^r|V=0. The open sets U,V cover X, and w^(2k−2) vanishes on U while w^r vanishes on V. The standard relative cohomology cup-product argument then forces
   w^(r+2k−2)=0 on X/tau,
contradicting w^d!=0 whenever r+2k−2<=d. Hence some z in f^(-1)(0) lies outside O_k.

Let sigma_z be the unique minimal supporting simplex of z. Since z lies outside O_k, sigma_z does NOT belong to any outer T-facet simplex D_T. But it belongs to SOME simplex of K_x, so all its actual path permutations lie in a common proper permutohedron face, and hence in at least one facet H_S for a nonempty proper S. Since the supporting simplex is not covered by any outer facet, each such S obeys k<=|S|<=n−k.

At the zero f(z)=0, the positive barycentric weights of the supporting vertices sum to zero signed-coordinate vector. Since each vertex vector is one of ±e_1,...,±e_r, for at least one index j there are TWO supporting actual permutation vertices carrying the COMPLEMENTARY labels +j and −j. Both lie in H_S, so their coordinate words share exact prefix support S. Their physical rooted cube geodesics therefore meet at y=x XOR S after |S| edges, with k edges or more on either side. Their signed median defects are complementary by their labels, and central reversal copies cannot share a proper face. This proves the main theorem.

Finally choose k=floor((n+1)/4). With d=n−3 and r=ceil((n−3)/2), one has d−r=floor((n−3)/2), and the integer inequality 2k−2<=d−r holds exactly for k<=floor((n+1)/4). Hence the claimed optimal bound from this dimension-counting argument. QED.

**Relevance to active NORI GRAND CLOSURE.** This FORCES a Tucker pair of GENUINE same-root, endpoint-opposed full geodesics at a COMMON MACROSCOPIC INTERIOR CUT, even in dimensions where a previously forced shared rank-1 or rank-2 cut would have lacked complete three-face windows on one side. It makes the physical two-seam splice theorem directly applicable for n>=11. The actual color of each new seam window is the color of an ordered physical face through y. There is still NO proof that one of the four prefix-suffix splices has <=1 color change or that y is a hub with the required mixed class selector. The Tucker theorem is UNCONDITIONAL; the color-compatible defect-reducing extraction remains the OPEN grand forcing step.

**General template.** Any genuine free-τ permutohedral face nerve with w^d≠0 and an odd ±r labeling has a complementary-label pair sharing a prefix-coordinate support of size k..n−k whenever r+2k−2<=d. The method may be reused with a SMALLER signed-label alphabet to force cuts even closer to n/2.

## EXACT TWO-SIDED HELLY NERVE OF PHYSICAL NORI PATH WITNESSES — GRAND FIXED POINT AND UNIVERSAL INDEX-FOUR CEILING

Let n>=6 and let c be ANY active binary NORI coloring of actual physical ORDERED 3-faces, c(bar F,rev π)=1−c(F,π). Let P range over ALL ACTUAL directed direction-distinct cube geodesic PATH STATES (root + direction word) of length k between 3 and n inclusive whose consecutive physical ordered-three-face windows have AT MOST ONE color change. (Length3 is always admitted, since its word has one color.) Let ΘP be the physical antipodal complement and vertex-sequence reversal; Θ preserves this path class and is a fixed-point-free involution on its VERTICES.

For each admitted rooted P=(x,π), define its exact certified root sheet
 S(P) = x + span_F2{e_i:i belongs to every ordered-three-face window of π}.
Its real cubical hull |S(P)|⊂[0,1]^n is an axis-aligned coordinate face of dimension m(k)=max(6−k,0), and EVERY binary root in S(P) produces the SAME entire sequence of physical window faces in the SAME direction order and hence the same <=1-switch property. This is the exact physical-face fiber theorem of nori_exact_middle_window_root_fiber_dimension_and_root_support_antipodal_action_20261008. We reuse S for both its finite vertex set and its real cubical hull when no ambiguity arises.

Define the TWO-SIDED PHYSICAL CERTIFICATE BOX
   B(P)= |S(P)| × |S(ΘP)| ⊂ [0,1]^(2n).
It is a coordinate product box of dimension 2m(k)<=6. Let
   U = ⋃_(admitted P) B(P)
and define the actual two-sided HELLY NERVE E whose vertices are the admitted path states P and whose simplices are the finite families σ with ⋂_(P∈σ) B(P) nonempty.

THEOREM 1 (honest flag complex with the CORRECT physical involution). Any family of coordinate product faces of [0,1]^(2n) is 2-Helly: pairwise intersection implies whole-family intersection, because each intersection condition is consistency of prescribed 0/1 values on fixed coordinates. Hence E is the FLAG (clique) complex of its genuine pairwise box-intersection graph. Every E simplex is certified simultaneously by one REAL starting cube root for its original path states and one REAL starting root for all their Θ-images; unlike convex averaging, both roots may be chosen Boolean because the intersection box is a coordinate face. The involution Θ is SIMPLICIAL, since
   B(ΘP)=swap(B(P)),  swap(a,b)=(b,a).
The finite convex-box nerve lemma applies equivariantly: E is Θ-equivariantly homotopy equivalent to U with its factor-swap involution. One can construct the equivariant map E→U explicitly on barycentric subdivision: to the barycenter of a nerve simplex σ assign the coordinate center of ⋂_(P∈σ)B(P); nested simplices have their centers inside the smallest intersection, so linear interpolation stays in U. Every map commutes with swap. The reverse nerve map can be built using sufficiently small swap-symmetric open thickenings of the finitely many coordinate boxes, their contractible intersections, and an equivariant partition of unity.

THEOREM 2 (EXACT grand closure fixed-point equivalence). The following are equivalent:
 (i) there is a FULL n-edge antipodal geodesic of c with at most one window-color change;
 (ii) the geometric union U intersects the swap-fixed DIAGONAL {(r,r):r∈[0,1]^n};
 (iii) E has a Θ-fixed point;
 (iv) E has an edge joining one path state P to its physical Θ-image ΘP.

PROOF. Let W be used directions of P, D=[n]\W. Physical reversal sends its root x to x XOR D and its order to rev π. Every coordinate i∈D is fixed in S(P) to bit x_i and fixed in S(ΘP) to bit 1−x_i. Hence if D nonempty, the two sheets S(P),S(ΘP) are disjoint. If D empty, W=[n], the starting roots of P and ΘP are THE SAME, and their middle-coordinate root-sheet translation sets are identical under reversal, so S(P)=S(ΘP). Thus B(P) meets the diagonal iff P is a FULL good path, and B(P)∩B(ΘP) nonempty iff P is FULL. This proves (i)⇔(ii)⇔(iv). An opposite edge has Θ-fixed midpoint. Conversely a Θ-fixed point in the nerve has a Θ-INVARIANT minimal supporting simplex; any vertex P in that simplex has ΘP there too, forcing their intersection B(P)∩B(ΘP) and hence a FULL good path. QED.

THEOREM 3 (NONSPURIOUS odd unused-sign labeling, with honest simplicial cells). Define the signed-unused-coordinate vector η(P)=bar(endpoint(P))−root(P)∈{-1,0,+1}^n. As previously proved, η(ΘP)=−η(P), and η_i(P) is nonzero precisely for UNUSED coordinate i. For any simplex σ of E, the original sheets S(P), P∈σ, have a COMMON ACTUAL ROOT r. Whenever coordinate i is unused in P and Q it is fixed in both S(P),S(Q), so r_i=x_i(P)=x_i(Q), hence η_i(P)=η_i(Q). Thus NO E simplex ever contains both +1 and−1 at the same coordinate: E is SIGN-COHERENT. Its affine η-map E→R^n is Θ-ODD, and its zero is a LITERAL FULL admissible path certificate, not a spurious averaged coincidence.



*The scope-specific limitation and complete proof are preserved in linked research note note_antipodal_involution_index_and_bichromatic_bad_root_limits.*
