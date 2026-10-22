# Twisted minimizers: prefix reachability barriers and Freudenthal rank-slice obstruction

- Stable ID: note_nori_twisted_minimizer_prefix_barrier_rank_slices_20261020_r12020
- Author: session_nori_r12020_1
- Primary home: subsection:central_freudenthal_subdivision_and_the_all_root_geodesic_chamber_sphere
- Labels: NORI1, topology, geodesic-reachability, root-slide, Freudenthal, method-obstruction
- Lifecycle: active
- Epistemic status: proved
- Current version: 4
- Retention: current and at most one previous snapshot
- Created session: session_nori_r12020_1
- Updated session: session_nori_r12002_4
- Disposition: none
- Successor: none

## Related references

- subsection:central_freudenthal_subdivision_and_the_all_root_geodesic_chamber_sphere
- subsection:two_end_localization_of_second_switch_chain_extensions

## Research note

# Twisted minimizers and central-Freudenthal rank carriers

Let n>=3 and let c be an antipodally odd binary edge coloring of Q_n. A full antipodal geodesic P has color word w_1,...,w_n. Define the twisted cyclic defect D(P)=sum_{j=1}^{n-1}[w_j!=w_{j+1}]+[w_n=w_1]. Under a root slide, the word changes to (w_2,...,w_n,1-w_1), so D is invariant, odd, and D=1 precisely when a root slide is monochromatic.

## Prefix replacement and a reachability barrier

Suppose w_1=w_n=a and let u_k denote the vertex reached after k steps of P. Put r_k=#{1<=j<=k:w_j!=w_{j+1}} for k<n. If Q is a monochromatic geodesic from u_0 to u_k of color b, the concatenation R of Q and the suffix of P from u_k uses every original dimension once and satisfies
D(P)-D(R)=2 floor(r_k/2) if b=a, and D(P)-D(R)=2 ceil(r_k/2) if b=1-a.

Proof. Write q=b, and let s_tail count changes of P strictly after position k. Then D(R)=s_tail+[q!=w_{k+1}]+[w_n=q], while D(P)=r_k+s_tail+1. Since w_{k+1}=a+(r_k mod 2), subtraction gives the formulas.

Corollary. If P minimizes D over all full antipodal geodesics and has w_1=w_n=a, then for every k at or after the second ordinary change of P, neither color has a monochromatic geodesic from u_0 to u_k. At or after the first change, color 1-a has no such geodesic.

## A dimension-uniform early barrier

Suppose d=min_P D(P)>=3. The d twisted defect positions in one period of length n have positive cyclic spacings l_1,...,l_d summing to n. Root a minimizing geodesic immediately after any of these defects. It then has matching first and last colors, and its second ordinary change is at position l_j+l_{j+1}. Since the average of these d sums is 2n/d, some rooted minimizer has second change t<=floor(2n/d)<=floor(2n/3). Thus some root x and complete dimension-simple chain x=u_0,...,u_n have the property that none of u_t,...,u_{n-1} is reachable from x by a monochromatic geodesic of either color.

A minimizer with globally latest second-change position is also rooted immediately after a twisted defect: moving a root located inside a twisted monochromatic run backward to its preceding defect shifts both first ordinary changes strictly later. Consequently the earlier lexicographic synchronized-splice exclusion also follows directly from the matching-endpoint-color case.

## Rank-slice index obstruction

Let X be the regular dual cell complex to L_n=sd(boundary([0,2]^n)), with central antipodal involution tau. For a proper face F of rank k, let D_F be its closed dual cell, and let Y_k be the union of all D_F with rank(F)=k, 0<=k<n. Distinct rank-k faces cannot occur together in a cubical face flag, so these closed dual cells are pairwise disjoint. Each D_F is contractible and tau exchanges D_F and D_{bar F}; hence the double cover Y_k -> Y_k/tau is trivial, and w_1(Y_k/tau)=0. In contrast X/tau is RP^{n-1}, so w_1^{n-2} is nonzero for n>=3 and lifts to H^{n-2}(X/tau,Y_k/tau;F_2) by the long cohomology sequence. Any index-based transfer from a complementary label pair to a common retained rank-k face therefore requires crossing cells that change that rank-k face. This is a limitation of purely equivariant fixed-rank forcing; shared-edge incidence may impose further restrictions.

## Facet degree of the first-change face selector

Fix a rank-(n-1) facet F. Under hypothetical failure of NORI1, F has no monochromatic spanning geodesic, since a spanning monochromatic path of length n-1 extends to a full antipodal monochromatic geodesic using one of the antipodally paired endpoint edges in the missing dimension. Every complete flag through F consequently has its first color change at a position <=n-2. Select the barycenter of the proper face of F reached at this change. These selected vertices belong to the flags of sd(boundary F).

The boundary of the dual cell D_F is the dual cellulation of sd(boundary F). More generally, for any triangulated sphere K and any choice of one vertex of each maximal simplex, the induced map on dual 0-cells extends over all dual cells within closed-star carriers and is homotopic to the identity. Indeed for the dual cell D_sigma of a nonempty simplex sigma of K, every selected vertex in a maximal simplex containing sigma belongs to st_K(sigma); these stars are contractible and nested under refinements, and the identity map is carried by the same stars. The carrier extensions are therefore homotopic. Hence any such star-carried first-change selector on boundary(D_F) has degree +1 or -1 as a map to boundary F.

It cannot extend over D_F while remaining in boundary F. This explains why simply restricting the color-dependent face labels to the (n-2)-skeleton of the outer cube fails to produce a global low-index map: the facet dual cells carry unavoidable nonzero attaching degrees. A further forcing mechanism needs an additional color-sensitive relation rather than convex averaging of different flags.

These statements establish structural barriers and a rank-relative obstruction; they do not yield NORI1.

## Induced run cycles, switch distance, and a crosspolytope filtration

For distinct cube vertices u,v let s_c(u,v) be the minimum number of color changes among all geodesics joining them. For a globally D-minimizing antipodal geodesic with d=D>=3, extend its word by antipodal complement and mark the 2d successive twisted color-run boundary vertices v_0,...,v_(2d-1). These are distinct, v_(i+d)=bar(v_i), and any d consecutive runs use every original direction once.

THEOREM. For 1<=k<=d, s_c(v_i,v_(i+k))=k-1. For 1<=k<d, every geodesic achieving k-1 switches from v_i to v_(i+k) begins and ends in the same colors as the k-run subpath.

PROOF. For k<d, the k-run arc has length <n and uses distinct directions. Any substitute geodesic joins the same endpoints, so it uses the same set of directions, and adjoining the original complementary-direction remainder produces a full antipodal geodesic. Let a be the original first color of the arc; its last is a+(k-1) mod 2. In the antipodally doubled cyclic word, the two exterior run colors are 1-a and a+k mod2. The original arc with its two interfaces contributes k+1 color changes. A replacement with s internal changes, first color alpha and last color beta, contributes
 [alpha!=(1-a)] + s + [beta!=(a+k mod2)].
Global D minimality requires this quantity >=k+1. It is at most s+2, hence s>=k-1. If s=k-1, both interface indicators equal one, implying alpha=a and beta=a+(k-1). The original arc achieves k-1. For k=d, v_(i+d)=bar(v_i), any full geodesic with s changes satisfies D<=s+1, so s>=d-1, and the d-run half of the doubled path achieves equality. Reversal supplies the cyclic short-distance formula
 s_c(v_i,v_j)=min(|i-j|,2d-|i-j|)-1
for distinct marked vertices. QED.

For integer r>=0 define G_r(c) on the original cube vertices by uv an edge iff s_c(u,v)<=r, and K_r(c) to be its flag complex. For every 0<=r<=d-2, the induced graph of G_r on the 2d marked vertices is the (r+1)-st power of the cycle C_(2d), i.e. cyclic distance <=r+1. In particular G_0 has an induced antipodal C_(2d). For r=d-2, all distinct nonantipodal marked vertex pairs are adjacent, and no antipodal pair is adjacent (by d minimality). The induced flag subcomplex is the boundary of the d-dimensional crosspolytope, with its standard free antipodal involution. Thus K_(d-2) contains an equivariantly embedded S^(d-1); its quotient carries nonzero w_1^(d-1). There are no antipodal edges anywhere in G_(d-2), so the involution on K_(d-2) is free.

The sphere is built from pairwise paths, without a jointly witnessed family. Already d=3, the triangular face {v_0,v_2,v_4} in the octahedral complex cannot lie on one cube geodesic: its three pairwise Hamming distances are the sums of the sizes of the three nonempty direction blocks taken two at a time, so all three triangle inequalities are strict. Hence this high-index carrier alone has no common-direction-order extraction theorem. A forcing step must exploit compatibility of different path witnesses or a color-sensitive map on the flag complex; ordinary equivariant index is insufficient.


## The rank-three coherent chamber annulus

Suppose the preceding minimum twisted defect is d=3, and let A,B,C be the three nonempty direction blocks, so the six run vertices are (using x xor supports)
v0=x, v1=x^A, v2=x^(A+B), v3=bar x, v4=x^(B+C), v5=x^C.
The induced flag complex in K_1 on these vertices is the octahedral S^2, having the eight triangular facets obtained by choosing one vertex from each antipodal pair {v0,v3},{v1,v4},{v2,v5}.

A triple of these six vertices occurs on a common direction-simple cube geodesic iff it is one of the six triples {v_i,v_(i+1),v_(i+2)}, indices modulo 6. The six listed triples occur on the original antipodal Petrie cycle, within one n-edge half. The two omitted triples are {v0,v2,v4} and {v1,v3,v5}. Their three pairwise Hamming distances are |A|+|B|, |B|+|C|, |A|+|C|, all with strict triangle inequalities, so no one vertex lies between the other two. Thus they cannot be contained in a cube geodesic.

The resulting common-geodesic-compatible subcomplex of the octahedral boundary comprises six triangles in a ring, topologically an annulus. Its boundary components are the two omitted triangular cycles; the involution tau exchanges these components and acts by a half rotation on the core hexagon. Its quotient is a Möbius band, whose first Stiefel-Whitney class is nonzero but whose square vanishes. Hence the pairwise witness sphere has index 2, whereas the common-geodesic-compatible subcomplex has index 1.

This is a geometry-only obstruction to deriving a shared direction-simple witness from the octahedral index class. Any chain correction restoring the two missing triangles must use combinations of distinct paths, additional vertices or face data, or a color-sensitive compatibility identity beyond common path incidence. It supplies no contradiction to NORI1.


## Median-star obstruction for the three-run hexagon

Let A,B,C partition [n] into nonempty sets, let x be a root, and suppose a full antipodal geodesic using A then B then C has monochromatic block words a,(1-a),a, respectively. Put v0=x, v1=x^A, v2=x^(A+B), v3=bar x, v4=x^(B+C), v5=x^C, and let u=x^B, so bar u=x^(A+C). Each original block path is a geodesic. Their antipodal images give the other three alternating hexagon edges.

THEOREM. If there are monochromatic geodesics from u to each of v0, v2, v4, then c admits a full antipodal geodesic with at most one change, hence a monochromatic full antipodal geodesic after a root slide.

PROOF. Let q be the color of a u-to-v0 monochromatic geodesic, which uses all B directions once. If q=a, concatenate this geodesic, the given a-colored v0-to-v1 path using A, and the antipodal image (with color 1-p) of any p-colored u-to-v4 geodesic using C, now running v1-to-bar u. This is a full direction-simple antipodal geodesic with its first two blocks both color a, hence at most one change. If q=1-a, concatenate u-to-v0, the (1-a)-colored v0-to-v5 path using C (the antipodal image of the original C run), and the antipodal image of a u-to-v2 monochromatic A-geodesic running v5-to-bar u. Again its first two blocks match, and it has at most one change. Any one-change full antipodal geodesic becomes monochromatic by a cyclic root slide under antipodal oddness. QED.

Consequently a hypothetical NORI1 counterexample with such a three-run cycle must have at least one of the three opposite-corner block pairs (u,v0),(u,v2),(u,v4) admitting no monochromatic geodesic of either color. These are the three radii from the median of the alternating triangle {v0,v2,v4}; their antipodal counterparts are the radii from bar u to the opposite triangle. This locates a color-sensitive obstruction to filling the missing two facets of the octahedral carrier. Existence of the other two arms is not automatically guaranteed by cube topology; arbitrary proper-face edge colorings can block monochromatic spanning geodesics. The result is conditional and does not close NORI1.
