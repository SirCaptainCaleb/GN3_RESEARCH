# Relative projective index beyond root permutohedra and nonlinear profile fibers

- Stable ID: note_nori_xvii_relative_root_cell_index_profile_fibers_r12094
- Author: session_nori_r12094_4
- Primary home: subsection:central_freudenthal_subdivision_and_the_all_root_geodesic_chamber_sphere
- Labels: NORI1, topology, Freudenthal, profile-transport
- Lifecycle: active
- Epistemic status: proved
- Current version: 7
- Retention: current and at most one previous snapshot
- Created session: session_nori_r12094_4
- Updated session: session_nori_r12108_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

# Relative projective zero localization for full-path profiles

Let n>=2 and c be an antipodally odd binary coloring of the original edges of Q_n. For a rooted full antipodal path P=(x,pi), write w(P) in {0,1}^n with its entries indexed by original direction. Put H={v in R^n:sum_i v_i=0} and z(P)=w(P)-(sum_i w_i(P)/n)1 in H. Let X be the dual regular CW sphere of the barycentric cubical boundary, whose 0-cells are full-path chambers (x,pi), and whose top cells D_F are indexed by nonempty proper original cube faces F.

THEOREM (nonroot projective zero localization). Assume that no full antipodal path of c is monochromatic. Then there is an original cube face F of dimension at least two and a probability distribution on full paths whose cubical face flag contains F, for which the direction-indexed color means agree:
  E[w_1(P)]=...=E[w_n(P)].
Equivalently, 0 is in the convex hull of the z(P) for the chambers incident to D_F.

PROOF. Suppose the convex hull misses 0 for every D_F with dim F>=2. For every original cube edge e of direction i, all paths refining e start with that same edge, so their i-th color entry equals c(e), an extreme value 0 or 1. Their z(P) cannot have 0 in its convex hull: if a convex average of w(P) equals a constant vector, its i-th entry forces that constant to equal c(e); extremality forces every participating w(P) to be the same constant vector, contradicting the hypothesis. Thus the convex profile hull also misses 0 on every D_e.

Construct the odd continuous map f:X->H using the barycentric subdivision of the dual cellulation: send each dual face barycenter to the arithmetic mean of its chamber-vertex z(P)'s, and interpolate on nested flags. Each cell D_F maps inside the convex hull of its incident chamber labels. Under the supposition, f avoids 0 outside the interiors of the root dual cells D_x (dim F=0).

For every root x, the cell D_x is the (n-1)-dimensional permutohedron of all orders pi rooted at x. Its boundary is S^(n-2). Reversal of direction order gives an internal free central involution pi -> reverse(pi); the rooted profile obeys w(x,reverse(pi))=1-w(x,pi). The averaging construction is odd under this internal involution on all of D_x. Since its boundary lies in cells D_F with dim F>=1, f does not vanish on boundary(D_x). Thus its normalized boundary map S^(n-2)->S(H)=S^(n-2) is odd and has odd degree modulo 2. Hence f has odd local zero index in the interior of each root cell.

The closed D_x for distinct original roots x are disjoint, since distinct original cube vertices do not share a simplex in the barycentric cubical subdivision. Geometric antipodality pairs D_x with D_(bar x), giving 2^(n-1) root-cell pairs. This number is even for n>=2, so the root-cell zero orbits contribute zero to the mod-two total.

On the other hand, a generic equivariant perturbation of f, supported away from the already zero-free complement and respecting its boundary values on each D_x, has an odd total number of antipodal zero orbits. This is the top Stiefel-Whitney evaluation u^(n-1) on RP^(n-1), for the associated bundle gamma^(direct_sum (n-1)), where u=w_1(gamma). Contradiction. Therefore some D_F with dim F>=2 has a convex profile hull containing 0. QED.

SHARPNESS AS A WITNESS-DECODING BARRIER. For any n>=4, set c_0(x)=x_1, c_1(x)=x_0, c_2(x)=1+x_0 and c_i(x)=x_0 for every i>=3, over F2. Every rule ignores its own direction bit and has odd antipodal parity. Let F be the two-face with free directions 0,1 and all others fixed to zero. Every chamber path whose face flag contains F traverses 0,1 first, then the other directions. Its colors in directions 2 and 3 are opposite, since both are evaluated after direction 0 is flipped; hence none of these chamber paths is monochromatic. Yet the two rooted paths with order (1,0,2,3,...,n-1), rooted at e_0 and e_1 respectively, have direction-indexed profiles (1,1,1,0,0,...,0) and (0,0,0,1,1,...,1). Their average is (1/2)1. Thus the forced fractional zero may occur already in a square-face dual cell with no monochromatic path among its incident chambers. The full coloring nonetheless has monochromatic geodesics elsewhere.

The theorem localizes a relative antipodal obstruction outside root and original-edge dual cells, but does not round a fractional profile into a monochromatic witness. A further topological mechanism must relate the different higher-face profile carriers, retaining shared original edge colors and direction order.

NONLINEAR FIBER TRANSPORT. For each order pi define F_pi(x)=w(x,pi) and W_pi its image on all roots. Then W_pi is invariant under profile complementation, and W_(reverse pi)=W_pi. If rho pi cyclically shifts first direction i to the end, then F_(rho pi)(x^i)=F_pi(x)+e_i; thus W_(rho pi)=W_pi+e_i. For an initial block S shifted to the end, W_(rho_S pi)=W_pi+1_S. Therefore the absence of any monochromatic full path forces W_pi to avoid every prefix indicator of pi and every suffix indicator, for every pi. For an adjacent exchange of consecutive i,j after prefix S, the pointwise profile difference is Delta_j c_i(x^S)e_i+Delta_i c_j(x^S)e_j. Each derivative ignores the root bits i,j and is invariant under antipodal complementation of the other root bits. Consequently all four profiles over any fixed assignment of the other n-2 root bits are translated by one common vector under that exchange. These statements preserve arbitrary nonlinear shared-edge dependence, but integrability of the resulting transport does not itself prove existence of a monochromatic full path.

## Sensitivity constraints on a face bearing a fractional zero

Suppose c admits no monochromatic full antipodal geodesic, and let F be a proper original cube face with free direction set S such that the convex hull of the centered complete-path profiles of all flags through F contains zero. For every i in S, the i-edges of F have both colors. Indeed, if all i-edges in F had a fixed color a, every full path through F would have profile entry w_i=a. A convex combination with all direction marginals equal then has common marginal a, and extremality of a in {0,1} forces every participating profile to be the constant vector a 1, a contradiction.

Consequently, for each i in S, there are a different direction j in S and an ij-square inside F with Delta_j c_i=1. Form the directed graph i->j when that derivative is nonzero on at least one square in F. Every vertex has positive outdegree, so this graph contains a directed cycle. Combined with the previously proved nonroot fractional localization, a hypothetical counterexample supplies a proper cube face bearing a centered fractional zero AND an internal directed sensitivity cycle. The cycle may use witnesses from different squares; no simultaneous common-square claim follows.

If |S|=2, both cross-derivatives must equal one on the unique square F. Thus its two parallel i-edges have opposite colors and its two parallel j-edges have opposite colors. Its ordinary square curvature is zero, since both directional derivatives are one. This is a necessary property of any 2-face dual cell carrying a centered zero in a counterexample.

## Facet-cell profile prism

Let F be an original facet with free set S=[n]\{j}, and let H_F be the set of direction-indexed {0,1}^S profiles of all oriented spanning geodesics of F. The profile set of full paths whose face flags contain F is

  W(D_F)=H_F x {0,1}.

To see this, every such full path first traverses some spanning path Q in F and then the final outside j-edge. If Q goes from x to x^S, reversing Q preserves its color profile in S and changes the last j-edge from the one incident to x^S to that incident to x. Because j-edge colors are invariant under flipping bit j and complemented under full antipodality, these two final j-edge colors are opposite. Both full paths have flags containing F.

Hence the centered full-profile convex hull for the dual facet cell contains zero if and only if the convex hull of H_F intersects the line of constant profiles t 1_S, 0<=t<=1. Under the no-full-path hypothesis, neither endpoint of this diagonal is attainable: any monochromatic spanning geodesic of F extends to a monochromatic full geodesic via the favorable j-edge at one of its endpoints. Therefore such a face's fractional intersection must occur at 0<t<1.

## Limitation: fractional square-face zeros may coexist with large path defect

For every even n>=6, take the legal flat coloring
  c_i(x)=sum_(k!=i) x_k mod 2.
Fix the 2-face F whose free directions are S={0,1} and whose other bits are zero. Let P be any full path with face flag containing F: its first two directions are 0,1 in some order, and all remaining directions belong to T={2,...,n-1}. If the root x lies in F, then for each position t>=3 the traversed T-edge color equals parity(x)+(t-1 mod 2). Thus the n-2 tail colors strictly alternate, producing at least n-3 ordinary switches; its twisted defect is at least n-3 (and thus at least three).

Nevertheless, uniform choice of the four roots in F and uniform independent orders within S and T gives mean direction color 1/2 in every direction: each i in S has color x_(S\{i}) plus a fixed position parity, while each i in T has color parity(x) plus its position parity. Both are fair bits when x is uniform in F. Hence zero lies in the convex hull of centered profiles incident to D_F, although no incident full path has twisted defect one. The legal coloring has successful full paths elsewhere; this is an obstruction to decoding a FACE-LOCAL fractional zero into a witness on that face, not a counterexample to NORI1.

Distinct root dual cells are disjoint even as closed cells, because no face flag contains two different original cube vertices. The preceding relative-index proof counts zero indices in their interiors, provided their boundaries are zero-free.

The remaining global objective is to exploit how zero-bearing face cells and their first/last directional witness data overlap throughout the complete central Freudenthal complex. No face-local rounding assertion is justified by the fractional degree alone.


## Relative local-index parity

Retain the centered profile labeling z(P) and the dual regular CW sphere X of the cubical barycentric subdivision, with top dual cells D_F indexed by nonempty proper original cube faces F. In particular ALL D_F have dimension n-1; the dimension of F determines the type of the underlying primal vertex, not the dimension of its dual cell. Distinct root cells D_x and D_y are disjoint as closed cells: a maximal face flag contains a unique original cube vertex, so the corresponding chamber-vertex sets are disjoint. Their boundaries meet dual cells of higher original faces but not one another.

THEOREM (relative local-index parity). Suppose no monochromatic full antipodal geodesic exists. The barycentric PL extension f:X->H of the centered profile labels admits an arbitrarily small antipodally odd perturbation f' such that:
(1) f' is nonzero on the boundary of every top dual cell and has isolated zeros in their interiors;
(2) for each root x the restriction f'|D_x is odd under the internal central inversion of the rooted permutohedron, taking pi to reverse(pi);
(3) no edge dual cell D_e contains a zero;
(4) defining nu_F as the mod-two local zero number of f' in D_F, one has
   nu_x=1 for every root x, nu_e=0 for every original cube edge e, and
   sum_(antipodal face orbits [F] with 2<=dim F<=n-1) nu_F = 1 mod 2.

Proof. The original barycentric extension respects geometric antipodality and, on each D_x, the independent rooted reversal involution pi->reverse(pi), since its centered labels satisfy both sign reversals. The closed root dual cells are disjoint, so their boundary maps can be perturbed in antipodally paired root cells preserving this local involution. The involution acts freely on each rooted permutohedral boundary; an arbitrarily small symmetric perturbation avoids zero there by generic-position arguments because the boundary has dimension n-2 and H has dimension n-1. Extend these boundary perturbations across the root disks while preserving local oddness and perturb the remainder equivariantly, obtaining isolated zeros away from dual-cell boundaries. The edge-cell convex hulls originally avoid zero by the extreme fixed-first-edge argument, so sufficiently small perturbations preserve their zero-free property.

The normalized boundary map on D_x is an odd self-map of S^(n-2), hence its mod-two degree is one and nu_x=1. There are 2^(n-1) root orbits, an even number for n>=2. The global section of (n-1) copies of the antipodal real line bundle over RP^(n-1) has mod-two zero number <u^(n-1),[RP^(n-1)]>=1. Subtracting the even root contributions and the zero edge contributions proves (4).

A nonzero nu_F implies 0 is contained in the original convex hull of incident chamber profiles: otherwise compactness leaves a positive distance between that hull and zero, contradicting a sufficiently small perturbation with a zero inside D_F. Therefore the theorem strengthens the earlier fractional carrier-existence statement to an ODD total number of locally charged nonroot face-cell orbits. The flat-coloring examples with numerous fractional convex zeros do not show which of their zero-bearing cells carry nonzero local index.

A possible forcing route is to prove vanishing of every nonroot local index under the hypothetical absence of all monochromatic full paths, using shared-square witness coherence or the established three-route median exchange. Such an index-vanishing theorem, not a blanket face-local convex rounding rule, would contradict (4) and close unrestricted NORI1. No such vanishing theorem is established.


## Dual-face link decomposition and perturbation dependence of local charges

Let F be a proper original cube face with s free directions S and t=n-s fixed directions T. The link of its barycenter b_F in the barycentric subdivision of the boundary cube splits as a join of two face-poset order complexes:
  lk(b_F) = sd(boundary Q_s) * sd(boundary Delta^(t-1)),
with the usual empty-sphere convention for s=0 or t=1. The lower factor records nested nonempty proper subfaces of F; the upper factor records nested proper nonempty superfaces of F, indexed by proper nonempty subsets of the fixed directions T. Their sphere dimensions are s-1 and t-2; their join has dimension n-2. Thus every dual top cell D_F is an (n-1)-ball with a canonical link decomposition.

Its chamber vertices are indexed by x in V(F), an order pi_S of S, and an order pi_T of T: the full geodesic first traverses S inside F, then T starting at x xor 1_S. Write H_S(x) for the profiles of all S-spanning paths from x inside F, and H_T(x xor 1_S) for all T-spanning paths from x xor 1_S in the complementary outside-direction face. The profile set incident to D_F is the union of root-coupled products
  W(D_F) = union_(x in V(F)) [ H_S(x) x H_T(x xor 1_S) ].
There is full independence of the two orders conditional on x, but their joint distribution is coupled by that same original root and uses the shared original edges. For t=1 this specializes to the previously proved facet-profile prism.

CAUTION ON LOCAL ZERO INDEX. For a chosen generic equivariant perturbation of the centered-profile section, the parity of zeros inside D_F is well defined. But its value is not generally an invariant of F and the edge coloring alone: if the unperturbed map has a zero on a common boundary between D_F and D_G, supported small perturbations can move that zero into either adjacent top cell, changing their individual parity values while preserving the total mod-two index. The earlier relative localization theorem correctly establishes existence of some generic perturbation and the odd total over all nonroot, nonedge face orbits, but that alone does NOT define intrinsic charges on specific faces and does not justify a per-face vanishing assertion without additional boundary control.

To pursue a valid cancellation theorem, either fix a compatible perturbation and prove a cancellation valid for THAT perturbation, or use the relative Euler obstruction class on a zero-free subcomplex and evaluate it against a canonical projective cycle. The invariant is the cohomology class/total evaluation, not the arbitrary distribution of zero orbits among overlapping dual cells. This agrees with the prior Article XIV primary-cell obstruction-cocycle guidance. The link join structure suggests using a filtration by the original face rank s, with boundary-crossing terms explicitly retained.

A diagnostic finite check, not a dimension-uniform theorem: for the facet with free directions {0,1,2} in Q4, there are 65536 legal antipodally odd edge colorings and 1440 with no monochromatic full geodesic incident to this facet. A numerical general-position winding calculation in the barycentrically subdivided facet dual cell returned parity zero for all 1440 using one coherent interpolation/perturbation scheme. This motivates studying a facet-relative cancellation but is not a proof of perturbation-independent vanishing, and no such global cancellation theorem has been established.


## Canonical obstruction after excising root dual cells

For n>=3, let X be the dual all-root Freudenthal sphere, let tau be the geometric antipodal involution, and let D_x be its pairwise disjoint closed root permutohedral cells. Put M=(X minus union_x interior D_x)/tau. This is RP^(n-1) with 2^(n-1) open (n-1)-balls removed. The centered profile map f, perturbed equivariantly to be nonzero on all root boundaries while preserving each root's internal reversal symmetry, gives a nonzero boundary section of E=(n-1)gamma over boundary M, where gamma is the sign line bundle of the antipodal cover.

The relative top obstruction to extending this boundary section to a zero-free section over M is the mod-two Euler obstruction in H^(n-1)(M,boundary M;F2). Its evaluation on the relative fundamental class equals one. Proof: the Euler obstruction on closed RP^(n-1) evaluates as <u^(n-1),[RP^(n-1)]>=1. Every removed root pair contributes an odd boundary degree, and there are 2^(n-1) such pairs, even for n>=2. The root contributions cancel modulo two, leaving relative obstruction evaluation 1.

This relative obstruction is a well-defined GLOBAL quantity independent of how zeros are redistributed across nonroot dual cells by generic perturbations. It is a cleaner statement than saying an individual face has an intrinsic local index; no such face-specific invariance was established. Under absence of a monochromatic full path, all edge dual cells are zero-free by their fixed-direction-color extremality, so any representative of this nontrivial relative obstruction is supported away from edge cells, but its cohomology class must be handled on the whole punctured projective space.

A sufficient forcing step for unrestricted NORI1 would construct a zero-free extension of the boundary profile section across M in the hypothetical no-geodesic case, using original shared-edge and direction-support incidence; relative Euler parity would contradict it. This is the required global compatibility implication, not a claim that such an extension has been found.


SYMMETRY-COMPATIBLE BLOCK LABEL (session_nori_r12107_2). For a proper face with free set S and outside set T, a dual chamber (x,pi_S,pi_T) has a face involution (x^S,reverse pi_S,reverse pi_T). It preserves the signed color profile on S and negates it on T. Write J_T for this partial sign change. The ordinary centered quotient R^n/span(1) does NOT admit J_T, since J_T(1)=1_S-1_T. The minimal J_T-invariant kernel containing 1 is span(1_S,1_T). Thus the maximal equivariant quotient is H_S plus H_T of dimension n-2, with label Psi=(y_S-mean(y_S),y_T-mean(y_T)). Every chamber vertex with Psi=0 is separately monochromatic in its S and T blocks, hence its full path has at most one switch and root-slides to a monochromatic antipodal geodesic. For adjacent cuts S and S union {i}, their kernels intersect in span(1) and sum to span(1,1_S,e_i), yielding a common quotient of dimension n-3 and a one-scalar gluing deficit.

ROOT BOUNDARY CAUTION. For even n>=4, the legal flat coloring c_i(x)=sum of x_j over j!=i has every path rooted at 0 alternating, with maximal twisted defect n-1. Yet on the rooted permutohedral boundary facet indexed by an ordered partition S|T with both blocks even, averaging all internal orders gives mean profile 1/2 in every direction, so the centered profile vanishes on that facet. Root boundaries are not automatically zero-free from absence of a local monochromatic witness. The relative Euler construction requires an independent compatible generic perturbation. Neither the split label nor the rank-one gluing formula supplies a global forcing theorem yet.

## Face reversal and profile-only convex limitations

Let S|T be a proper direction cut, y(P) the signed direction-color vector, and Psi_S the vector obtained by subtracting the respective block means. The face involution R_F fixes the S-part of Psi and negates the T-part. When S={i}, the S-part vanishes; therefore Psi(P) and Psi(R_F P) are opposites in the same original-edge dual cell. Every such convex carrier contains zero, even when no incident path is monochromatic.

Define V_T(P)=sum_(j in T)(y_j(P)-mean_T(y(P)))^2, which equals (4/|T|) times the number of pairs of T-directions having unequal colors. Thus V_T=0 iff T is monochromatic; otherwise V_T>=4(|T|-1)/|T|. Augment the face label by the scalar mean_S(y(P))*V_T(P). The augmented label is odd under cube antipodality, and the face involution fixes its scalar. A chamber-vertex zero means the two blocks are separately monochromatic, hence root sliding produces a full monochromatic antipodal path. On an edge dual cell S={i}, the color sign y_i is fixed, and under the absence of full monochromatic paths every T-block is mixed. Therefore the augmented scalar has one fixed sign and magnitude at least 4(n-2)/(n-1) on all chamber vertices incident to that edge dual cell. Convex averaging retains this strict halfspace when the variance is evaluated on each path before taking averages.

Nevertheless, no odd profile-only feature can eliminate all higher-face fractional zeros. For even n>=6 choose the legal flat coloring c_i(x)=sum_(j!=i)x_j mod 2. Let F have even nonempty free set S and even nonempty complement T. Given any incident full geodesic P, swap adjacent direction pairs throughout its S-block and T-block, keeping the root fixed. Each direction moves by one position and its color is parity(root)+root_i+(position-1) mod2. Therefore the paired geodesic Pstar has y(Pstar)=-y(P). For EVERY odd feature Phi on signed direction-color profiles, Phi(y(Pstar))=-Phi(y(P)); its convex carrier on D_F contains zero. Taking |S|=2, the n-2 outside directions form an alternating tail, so every incident path has at least n-3 twisted seams. All swaps use the same cube-edge coloring and preserve original direction simplicity. Hence any successful global forcing scheme must retain shared-edge or path-incidence information not recoverable from an individual profile, rather than merely increasing the degree of odd profile moments.
