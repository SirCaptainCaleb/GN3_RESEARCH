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

THEOREM 4 (the universal index-FOUR CEILING: short physical root sheets cannot supply an index-n proof). Assume the GRAND conjecture FAILS, hence no admitted path is full, U is off the diagonal and swap acts FREELY. Let U_3 be the union of boxes B(P) for length-THREE (one-window) paths. These paths are automatically admitted for EVERY ordered triple, root, and physical exterior assignment. Consequently
 U_3 = ⋃_(W⊂[n], |W|=3; exterior bits ε∈{0,1}^([n]\W))
        F_W(ε) × F_W(1−ε),
where F_W(ε) is the full 3-dimensional root coordinate face with bits ε fixed outside W. This is coloring-independent.

Put δ(a,b)=b−a. Each 3-path box has δ_i=±1 outside its three free directions and arbitrary δ_i∈[−1,1] in those three directions. Hence δ(U_3) is PRECISELY the THREE-SKELETON X_3=(∂[−1,1]^n)^(3) of the centrally antipodal cube boundary. The map
  s(δ)=((1−δ)/2,(1+δ)/2)
is an equivariant section X_3→U_3 of δ. The homotopy keeping δ fixed and moving the midpoint (a+b)/2 linearly to (1/2,...,1/2) remains IN THE ORIGINAL BOX: outside W the two bits are already complementary endpoints, while inside W both coordinates are free. Thus U_3 Θ-equivariantly STRONGLY deformation retracts onto the section s(X_3).

The free antipodal three-skeleton X_3 has cohomological Z2 index EXACTLY 3 for n>=4. Upper bound: dim X_3=3. Lower bound: X_3/Θ is the 3-skeleton of ∂[−1,1]^n/Θ≅RP^(n−1), with its ordinary quotient cubical CW structure. Inclusion of a CW 3-skeleton into RP^(n−1) induces an INJECTION in H³(F2), so the third power of the first antipodal-cover class survives.

Now every LONGER admitted path (k>=4) has root-sheet dimension m(k)<=2, so B(P) has dimension at most FOUR (k=4:4; k=5:2; k>=6:0). The finite union U is a Θ-invariant cubical CW complex obtained by attaching to U_3 ONLY cubical cells of dimension <=4 (some attachments may share faces), hence its free-action quotient (U/Θ,U_3/Θ) has no relative cochains above degree4. Therefore H^j(U/Θ,U_3/Θ;F2)=0 for j>=5. Since U_3/Θ≃X_3/Θ has no cohomology above degree3, the long exact pair sequence gives
   H^j(U/Θ;F2)=0 for ALL j>=5.
So ind_Z2(U)<=4. Conversely U_3⊂U has w_1^3≠0, so ind_Z2(U)>=3. By equivariant nerve equivalence E≃_Θ U,
   3 <= ind_Z2(E) <= 4.
This is UNIFORM in cube dimension n and in the physical NORI coloring under the grand no-closure assumption.

**CRUCIAL TOPOLOGICAL CONSEQUENCE.** The universal 3-face geometry furnishes exactly a genuine index-3 antipodal base, and longer fixed-window root sheets can raise it at most to index4. For n>=5, the exact signed-unused Tucker closure criterion demands index>=n to force a zero in R^n. Therefore NO argument operating solely on the static two-sided root-invariance boxes of certified <=1-switch paths can provide such a high-index proof. To reach the unrestricted GRAND NORI conjecture, one MUST adjoin genuinely NEW topological cells coming from ORDER/PREFIX EXCHANGES, WITNESS-PRESERVING TRANSPORT, root/support memory holonomy, or higher-dimensional compatible repairs whose equivariant topology is not captured by the boxes. The theorem is an exact constructive carrier and an exact sharp dimensional NO-GO, not a counterexample to grand NORI.

## The two antipodal involutions have radically different indices: a concrete mobile-root obstruction

Let n≥8 be EVEN and fix rho∈F2^n. Take the valid active NORI coloring
\[
c_\rho(F,(a,b,c))=\bigoplus_{i\notin\{a,b,c\}}(F_i\oplus\rho_i),
\tag{1}
\]
independent of the ordered free triple's orientation. It is antipodally reversal odd because the number n−3 of fixed exterior coordinates is odd. For any full direction permutation p, let B_p⊆Q_n be the set of starting roots x whose ACTUAL full p-geodesic has opposite first and last ordered three-face colors.

**Theorem (complete topology of the same-order balanced-root locus).** For every full order p=(p1,...,pn),
\[
\boxed{
B_p=\Bigl\{x:\bigoplus_{j\in\{1,2,3,n-2,n-1,n\}}
(x_{p_j}\oplus\rho_{p_j})=0\Bigr\}.
}
\tag{2}
\]
Thus, as an induced physical cube-edge graph, B_p is exactly the disjoint union of 32 full coordinate (n−6)-cubes, indexed by the even six-bit assignments to the FIRST and LAST three directions of p. Under physical root complement x↦bar x, these 32 components are paired, with **no antipodally invariant connected component**. In particular:
- Every x∈B_p has bar x∈B_p, so **same-order antipodal root-pair endpoint synchronization is perfect** for this coloring.
- Yet no edge of the root cube in any of the six distinguished directions joins two B_p vertices; thus there is NO physical cube path lying entirely in B_p from x to bar x.
- The geometric cubical realization of B_p has an equivariant continuous map to S⁰, by assigning a sign to the two members of each paired component. Consequently the cohomological index under PHYSICAL ROOT complement is **zero**, even though the separate fixed-root PERMUTATION-REVERSAL carrier has topological index at least n−3.

**Proof.** Put s_i=x_i⊕rho_i. Along a p-geodesic from x, the initial physical ordered face has fixed exterior coordinates p4,...,pn, so
\[
w_1=\bigoplus_{j=4}^n s_{p_j}.
\]
The terminal physical ordered face has fixed exterior coordinates p1,...,p(n−3), all of which have been flipped once, hence
\[
w_{n-2}=(n-3\bmod2)\oplus\bigoplus_{j=1}^{n-3}s_{p_j}
=1\oplus\bigoplus_{j=1}^{n-3}s_{p_j}.
\]
Therefore
\[
w_1\oplus w_{n-2}
=1\oplus\bigoplus_{j\in\{1,2,3,n-2,n-1,n\}}s_{p_j},
\]
since the middle direction positions 4,...,n−3 appear twice and cancel. This is one precisely when the six-bit parity is zero, proving (2).

Within B_p the six distinguished starting bits can never change along a physical cube edge, because flipping one of them changes their parity from even to odd. All n−6 middle root bits are unconstrained, so every even assignment of the six distinguished bits defines an entire connected (n−6)-cube, and no edge connects different assignments. There are 2^5=32 even assignments. Physical antipodality complements all six distinguished bits; complementing SIX bits leaves parity even and sends every six-bit pattern to a DISTINCT pattern. Hence components occur in antipodal pairs and admit a componentwise ±1 equivariant map to S⁰. This proves all claims. \(\square\)

**Why this matters for the topology-first NORI program.** The previously proved same-order joint endpoint-balance theorem \`nori_same_order_antipodal_root_pairs_endpoint_opposition_disjoint_triple_orbits_20261008\` establishes actual full-path packet synchronization at x and bar x for all n≥10, and the high-index permutohedral theorem gives large index under DIRECTION-ORDER REVERSAL at each fixed x. Neither fact alone supplies an antipodally connected set of physical roots for a fixed order: the full-parity coloring realizes both phenomena while B_p has physical-root antipodal index ZERO.

The two involutions are categorically different:
(i) π↦rev π at fixed root x acts on a HIGH-INDEX permutohedral sphere; and
(ii) x↦bar x at fixed permutation π acts on a possibly disconnected ROOT-cube endpoint-balance locus.
They commute but their cohomological indices do NOT transfer. A grand proof must use legitimate root/order transition **cells coupling the two actions**, or the exact color-free reversed-two-tail support extraction, rather than infer physical-root connectedness from permutohedral high index or antipodal endpoint balance alone.

The construction is NOT a grand counterexample: by the already proved three-residue-chain affine theorem, each full permutation admits eight FULL MONOCHROMATIC roots elsewhere. It is a topological obstruction to a proposed fixed-order root-connection lemma, not a failure of NORI.

## Elevation: extremely bichromatic physical hubs can both be bad roots

The same valid parity NORI coloring (1) proves a sharper, more physical obstruction to a topological one-hub extraction.

**Theorem 2 (antipodal pairs of highly overlapping bichromatic hubs without good rooted full paths).** Let n≥8 be EVEN, and let \(i\in[n]\) be any coordinate. Put
\[
z=\rho\oplus e_i.
\]
Then:

1. At the physical vertex z, **every** middle-direction square involving i is a genuine MONOCHROMATIC 4-edge connector square of color 0 (some appropriate outer directions certify it). Every middle-direction square NOT involving i is a genuine MONOCHROMATIC 4-edge connector square of color 1. More precisely, every unordered coordinate pair \(\{i,j\}\) is color-0-certified, every pair \(\{j,k\}\subseteq[n]\setminus\{i\}\) is color-1-certified.
2. Consequently every physical incident cube edge in direction \(j\ne i\) has **BOTH** colors of genuine centered-mono4 square certificates. The edge in direction i has at least a color-0 certificate. So z is a strongly bichromatic hub with at least n−1 **doubly certified incident physical edges**; its antipode \(\bar z\) enjoys the same property with the two colors interchanged.
3. Nevertheless, for **every possible full direction permutation p**, BOTH actual rooted full antipodal geodesics from z and from \(\bar z\) have at least
\[
\boxed{D(z,p)=D(\bar z,p)\ge n-5\ge3}
\tag{8}
\]
ordered-three-face color changes. In particular NEITHER bichromatic hub supports any one-change FULL geodesic, despite its abundant opposite-color square overlaps.
4. In dimensions n≥8 the Kneser-strengthened theorem \`nori_same_order_antipodal_root_pairs_endpoint_opposition_disjoint_triple_orbits_20261008\` also supplies a *single identical complete direction permutation* p for which both z and bar z have opposite first/last face colors. These actual simultaneously endpoint-balanced paths still have at least n−5 changes.

**Proof.** At z the exterior difference \(z\oplus\rho\) has bit1 ONLY in direction i. For any physical ordered three-face THROUGH z whose free direction set is T, parity coloring (1) therefore assigns 0 when i∈T and 1 when i∉T, independent of the free direction order. A centered 4-edge connector with ordered directions (a,b,c,d) has two physical ordered three-face windows through z with free triples \(\{a,b,c\}\) and \(\{b,c,d\}\). They are BOTH color0 when the special i lies in the common inner pair \(\{b,c\}\); they are BOTH color1 when the four directions avoid i. All required distinct outer coordinates exist since n≥8. This proves (1) and the first assertions of (2). Antipodal reversal gives the claims at bar z.

For an arbitrary rooted full order p, use the exact rank-parity switch formula proved in \`nori_even_parity_bad_root_maximal_permutohedral_index_linear_radius_no_go_20261008\`:
\[
s_j(z,p)=1\oplus \mathbf1_{\{p_j=i\}}\oplus\mathbf1_{\{p_{j+3}=i\}},
\quad j=1,\ldots,n-3.
\]
Because i occurs at exactly ONE position in the permutation, at most TWO of the n−3 switch bits can be zero (those with i at position j or j+3). Hence at least n−5 switch bits equal1. At bar z the root-difference bit vector relative to rho is the complement of the singleton support, and both comparison terms \(s_{p_j},s_{p_{j+3}}\) are complemented, so their XOR is unchanged. Therefore the switch vectors of the two antipodal rooted paths are identical, proving (8). The final endpoint-balance claim follows from the Kneser theorem as already established. \(\square\)

**Sharp topological lesson.** Local *bichromatic hub overlap* can be nearly maximal at BOTH antipodal endpoints, and same-order endpoint-opposed packets can coexist at the pair, while every rooted full path at those physical vertices remains catastrophically multi-switch. Consequently neither the local doubly-certified-edge alternative nor fixed-antipode-pair permutohedral high index can be a universal direct extraction theorem. Successful grand closure must engage a third/moving root, a certificate-preserving global root-order orbit, or exact complementary-support monochromatic witness intersection elsewhere. The obstruction is a valid NORI coloring that DOES have good full paths at other roots; no grand counterexample is claimed.
\n\n**Direct certificate for part (4).** The shared endpoint-opposed order in this explicit parity example needs no appeal to the general Kneser theorem: choose any full permutation placing the unique exceptional direction i in one of the MIDDLE positions 4,...,n−3 (available for n≥8). Formula (2) then assigns even parity zero to the six first/last position bits at root z; the antipodal root has the same even parity because six bits are complemented. Hence both rooted full paths have opposite endpoint colors in that identical direction order. Their lower bound n−5 on internal switches continues to apply. This gives a completely explicit obstruction certificate.

The strong antipodal index of an ambient path complex does not guarantee a selector into the low-dimensional subset of compatible terminal memories. A valid proof must provide that selector or a replacement certificate.
