# Switch-position intersection and cut-exchange in the Freudenthal sphere

- Stable ID: note_nori_xvii_switch_position_intersection_cut_exchange_r12147
- Author: unspecified; session provenance retained
- Primary home: subsection:central_freudenthal_subdivision_and_the_all_root_geodesic_chamber_sphere
- Labels: NORI1, topology, Freudenthal, switch-position, cut-exchange, minimizers
- Lifecycle: active
- Epistemic status: proved
- Current version: 17
- Retention: current and at most one previous snapshot
- Created session: session_nori_r12147_2
- Updated session: session_nori_r12147_2
- Disposition: none
- Successor: none

## Related references

- None

## Research note

# Switch-position topological intersection and cut-exchange (session session_nori_r12147_2)

Scope: unrestricted antipodally odd edge coloring of Q_n. Theorems below are proved; no NORI1 closure or universal spatial matching is claimed.

## A. Two-face-flag switch-position intersection

Suppose n>=4 and there is no monochromatic full antipodal geodesic. Each rooted full geodesic P has >=2 ordinary switches, since a one-switch path can be re-rooted at its change point to give a monochromatic full geodesic. Let w_i(P) be its original edge colors, d_j(P)=[w_j!=w_(j+1)] for j<n, and k(P)=sum_(j=1)^(n-2)d_j(P)>=1. Define q(P)=(d_1,...,d_(n-2))/k(P), a probability vector, and f(P)=(-1)^w_1(P) q(P) in R^(n-2).

The chamber involution tau of the dual all-root Freudenthal sphere X_n sends f(P) to -f(P). Extend f piecewise affinely on the barycentric subdivision, putting the mean of the chamber labels at each dual-cell barycenter. An equivariant map avoiding zero on the (n-2)-skeleton would normalize to an equivariant map X_n^(n-2)->S^(n-3). Passing to quotients would kill w_1^(n-2), contrary to its nonzero restriction from RP^(n-1)=X_n/tau. Hence some dual cell D of dimension <=n-2 has zero in the convex hull of its chamber labels. Enlarge to a dual (n-2)-cell D(F subsetneq G), where F,G are two proper cube faces, so every represented path refines the same two-face flag.

Caratheodory gives <=n-1 paths P with weights t_P>=0 summing to one and sum t_P f(P)=0. Summing all entries of q(P) gives equal total weight 1/2 from paths starting in each color. Normalizing the two cohorts yields probability measures mu_0,mu_1 on these original cube geodesics such that E_(mu_0)q(P)=E_(mu_1)q(P). This is a topologically forced equality of normalized early-switch-position distributions in one shared two-face flag.

Rationality yields an integer switch-event version: choose rational convex-combination weights; multiply the cohort weights divided by k(P) by a common denominator. The resulting two integer multisets of full geodesics have the same number of switches at every position j<=n-2. Their total numbers of paths need not agree. These integer switch-event relations do not give common roots or common middle vertices.

## B. Color-sensitive cut exchange

Let P,Q be full antipodal geodesics with the same root x and same middle vertex u after j steps, 1<=j<n. Then their first j used dimensions coincide as sets, as do their remaining dimensions. Define R=P[0,j]*Q[j,n], R'=Q[0,j]*P[j,n]. These are full antipodal geodesics in the original cube, traversing each dimension once and preserving the colors of all used edges.

Write a=w_1(P), b=w_1(Q), z=w_n(P), y=w_n(Q); p=w_j(P), p'=w_(j+1)(P), q=w_j(Q), q'=w_(j+1)(Q). Set t_P=[z=a], t_Q=[y=b] and D(W)=sum_(i=1)^(n-1)[w_i(W)!=w_(i+1)(W)]+[w_n(W)=w_1(W)]. Cancelling the unchanged within-segment switches yields
D(R)+D(R')-D(P)-D(Q)
=[p!=q']+[q!=p']-[p!=p']-[q!=q']+[y=a]+[z=b]-[z=a]-[y=b].

**Synchronized opposite-phase lemma.** If a!=b, p!=q, p!=p', and q!=q', the two old joins are switches and the two new joins are unswitched. The seam contribution changes by 2-2(t_P+t_Q), so
D(R)+D(R')=D(P)+D(Q)-2(t_P+t_Q).
If P,Q both globally minimize D with value d, the case t_P+t_Q>=1 is impossible because at least one recombined path would have D<d. Therefore t_P=t_Q=0. In this equality case R,R' also have D=d, neither switches at the cut, and both have seam contribution one. Thus a phase-opposed synchronized cut of two global minimizers necessarily creates two further minimizers, moving the two switches from the cut to the two twisted closing seams.

The rank-four checkerboard square in the central Freudenthal manuscript illustrates the equality phenomenon: words 0101 and 1010 (both twisted defect three, closing seam zero) recombine at the shared two-direction prefix endpoint into 0110 and 1001 (also twisted defect three, closing seam one). This local equality geometry occurs in a coloring possessing good geodesics at other roots.

## C. Transfer obligation and judgment

The first theorem matches switch POSITIONS. The second lemma requires switches at the SAME original cube vertex with the SAME root, as well as opposite color phase. The first theorem does not produce these conditions, and does not place its support among global minimizers. It is a fractional certificate whose rational version yields integer event counts, rather than an individual monochromatic path.

The geometric opportunity is to study transport between neighboring dual (n-2)-cells through rank-three face-flag residues. Such transport would need to preserve the vertex/root data of switch events and enforce the phase hypotheses of B, thereby converting a topological obstruction into an original-edge-preserving path exchange. A claim of universal spatial transport or odd holonomy is currently OPEN. Any further work should confront those conditions rather than restating convex overlap.

## D. Phase-resolved topological switch-event matching

Assume n>=4 and that the antipodally odd coloring has no monochromatic full antipodal geodesic. Every such geodesic P has at least two ordinary color switches. Choose any omitted temporal index h in {1,...,n-1}, and put
\[
k_h(P)=\sum_{\substack{1\le j<n\\j\ne h}} [w_j(P)\ne w_{j+1}(P)]\ge1,\qquad
\Gamma_h(P)=\frac1{k_h(P)}
 \sum_{\substack{1\le j<n\\j\ne h}}
 (-1)^{w_j(P)}[w_j(P)\ne w_{j+1}(P)]e_j
 \in\mathbb R^{n-2}.
\]
Here e_j are basis vectors indexed by the retained temporal positions. Each chamber label is nonzero, and antipodal translation satisfies Gamma_h(tau P)=-Gamma_h(P).

**Theorem (phase-resolved matching).** For EVERY omitted index h, there is a two-face-flag dual (n-2)-cell D(F subsetneq G) and a nonempty positive integer multiset M of full original-cube geodesics refining that same face flag such that for every retained temporal position j, the number (counted with multiplicity) of paths in M switching 0->1 at j equals the number switching 1->0 at j. In particular at least one retained j supports a switch of both orientations in M.

*Proof.* Extend Gamma_h to the dual sphere X_n by giving each cell barycenter the mean of its chamber labels and linearly interpolating over chains of nested dual cells. This is an odd PL map. Were it nonzero on the (n-2)-skeleton, radial normalization would yield an equivariant map X_n^(n-2)->S^(n-3). The projective quotient would send the covering class w_1 to the generator of H^1(RP^(n-3);F_2), contradicting w_1^(n-2) !=0 on the source quotient. Thus zero occurs in a dual cell of dimension <=n-2, contained in a two-face-flag dual cell. The barycentric interpolation shows 0 is a convex combination of Gamma_h(P) from its chamber vertices. Choose a rational convex combination (a nonempty rational solution exists since this is a finite rational linear system), and multiply its weights divided by k_h(P) by a common positive integer. This gives M and the claimed per-index cancellations. Each path has at least one retained switch, so M contains a matched pair of opposite switch orientations at some j. QED.

This theorem is stronger than matching first-color cohorts, because it pairs the colors IMMEDIATELY BEFORE the selected switches. It does not imply the two selected paths share their root or vertex at j, or that they globally minimize defect.

## E. Stronger synchronized cut-exchange law

Let P,Q share a root and their cube vertex after j steps; suppose BOTH switch at j with opposite pre-switch colors w_j(P)!=w_j(Q). Form R=P_prefix*Q_suffix, R'=Q_prefix*P_suffix; the common prefix direction set ensures both are direction-once full antipodal geodesics using original colored edges.

Put a=w_1(P), b=w_1(Q), z=w_n(P), y=w_n(Q), t_P=[z=a], t_Q=[y=b]. At the old cut there were two switches and at both new joins none. The seam differences yield the complete dichotomy
\[
D(R)+D(R')=
\begin{cases}
D(P)+D(Q)-2,&a=b,\\
D(P)+D(Q)-2(t_P+t_Q),&a\ne b.
\end{cases}
\]
For a=b the seam sum is unchanged. For a!=b the new seams total 2-t_P-t_Q, whereas the old seams total t_P+t_Q.

**Global-minimum consequence.** If P and Q both globally minimize twisted defect d, then necessarily a!=b AND t_P=t_Q=0; the two recombinations also attain defect d. Thus, for any fixed root x, intermediate vertex u, and cut rank j, opposite pre-switch phases among global minimizers require opposite initial phases and zero old closing-seam contributions. A globally minimum path having closing-seam contribution one cannot participate in such a pair. This applies to arbitrary nonlinear legal colorings and any cube dimension.

The previous phase-opposed lemma is the a!=b branch of this identity.

## F. Root-fixed topological index obstruction

Let D_x denote the top-dimensional dual cell of the central Freudenthal sphere indexed by an original cube vertex x. Its vertices are all rooted orders (x,pi), and D_x is a type-A permutohedron of dimension n-1. Distinct D_x are DISJOINT: a maximal central face flag begins at only one original cube vertex. Antipodality sends D_x to D_(bar x).

Consequently the union Y of all root-fixed dual cells D_x is a disjoint union of permutohedra in antipodal pairs. It admits a continuous antipodally odd map Y->S^0: give each D_x a constant sign, opposite on D_(bar x). The quotient covering Y->Y/tau is trivial on every component, so w_1(Y/tau)=0. The same is true of any antipodally invariant subcomplex of Y, including the union of root-fixed dual face-flag cells D(x subsetneq G).

**Implication for topological forcing.** The nonzero projective power w_1^(n-2) on the whole dual sphere cannot by itself force the zero of a phase-resolved profile to occur in a root-fixed two-face-flag cell. Yet that special cell is where every chamber has one common root and passes through the common vertex after rank dim G, making the cut-exchange law immediately available if opposite switches occur at that rank. A forcing argument must supply additional color-dependent root transport or constrain zeros in other two-face-flag cells. This is a structural obstruction to extracting the integral exchange solely from equivariant index.


## G. Canonical root-rotation gallery; defect as projective interface count

Let P=(x;i_1,...,i_n), let u_k=x xor {i_1,...,i_k}, and set P_k=(u_k;i_(k+1),...,i_n,i_1,...,i_k) for 0<=k<=n, with P_n=tau P. Join P_k to P_(k+1) through the following chamber-gallery moves: first r_0 (slide the root along the first direction), then s_1,s_2,...,s_(n-1) (move that direction from first position to last). Its concatenation Gamma_P projects from a path P->tau P to a noncontractible loop gamma_P in X_n/tau=RP^(n-1).

For a chamber C put b(C)=the binary color of its first original cube edge, and on each dual chamber-graph edge CC' put eta(CC')=[b(C)!=b(C')]. Every r_0 edge and every s_k edge for k>=2 has eta=0; only s_1 may cross the sign interface. Since antipodal translation complements both b values, eta descends to a cellular F_2 cocycle on the projective quotient. On any closed quotient loop, its mod-2 integral is the deck transformation of its lift, so [eta]=w_1.

**Theorem.** The NUMBER OF INTERFACE-CROSSING GALLERY EDGES of gamma_P is
\[
D(P)=\sum_{j=1}^{n-1}[w_j(P)\ne w_(j+1)(P)]+[w_n(P)=w_1(P)].
\]
*Proof.* The root slide r_0 keeps the same first edge. At the s_1 move after the kth root slide, the first edge changes from the original path's (k+1)st edge to its (k+2)nd edge for k<n-1. At k=n-1, the second edge is the antipodal image of the original first edge, of color 1-w_1. Every remaining s_k (k>=2) preserves the first edge. The resulting sequence of interface-crossing tests reads the adjacent changes in the antiperiodic word (w_1,...,w_n,1-w_1), giving D(P). QED.

The signed interface crossing count along the lifted gallery is always (-1)^w_1(P), because crossings alternate sign and its first and last signs are opposites. The projective class captures D(P) mod 2; the additional D(P)-1 unsigned crossings appear in cancelable algebraic pairs. A continuous loop cancellation need not preserve canonical root-rotation galleries or produce a valid direction-once antipodal cube geodesic. Finding such a color-sensitive admissible cancellation is open.

## H. Sign-region components are monochromatic original-edge components

Fix a in F_2, and retain the chamber-graph edges between chambers whose first original cube edge has color a. For each original color-a edge e, its chamber fiber is connected: r_0 exchanges the starting endpoint, and s_2,...,s_(n-1) permute the remaining direction order. Edges between distinct first-edge fibers are necessarily s_1 adjacencies; their first edges are incident at the same original root. Conversely any two original color-a edges incident at a common cube vertex give an s_1 adjacency by taking their directions first in opposite orders.

**Proposition.** Connected components of the first-edge-color-a chamber graph correspond bijectively to edge-containing connected components of the original color-a cube subgraph.

The first-edge coloring interface by itself therefore reproduces ordinary monochromatic edge connectivity. The canonical galleries add the required ordering information: their intersection counts recover the full twisted path defect. Consequently root transport must exploit those constrained galleries and their 2-dimensional exchange relations, beyond connectivity of the first-edge sign regions.

## I. Open admissible cancellation

The union of root-fixed dual permutohedra has trivial equivariant index (part F), while the canonical root-rotation galleries travel between those root fibers. If unrestricted NORI1 fails, every such gallery has at least three sign-interface crossings. The relevant missing implication is a theorem that combines the original cube's same-edge coloring constraints, adjacent dual-cell 2-dimensional relations, and global minimum-defect conditions to decrease the crossings by two inside the family of canonical root-rotation galleries gamma_P. Arbitrary homotopy in projective space provides only parity and does not satisfy this original-path admissibility condition.


## J. One interface crossing among arbitrary galleries is antipodal monochromatic reachability

Let n>=3. A gallery path from a chamber C to tau C represents the generator of pi_1(X_n/tau). Let eta count, as an ordinary nonnegative integer, its first-edge-color changes.

**Proposition.** There exists a gallery from some C to tau C having just ONE eta crossing if and only if the original cube contains a monochromatic edge path from some vertex x to its antipode bar x; repeated directions are allowed along this path.

*Proof.* Suppose the gallery crosses from color a to color 1-a at a single s_1 edge. The crossing changes its first original edge from an a-edge e to an (1-a)-edge f incident at a common root x. The portion before the crossing lies in a single component C_a of the first-edge-color-a chamber graph; the portion after it lies in a single (1-a)-component, which must equal tau C_a because the endpoint is antipodal to the starting chamber. By the component correspondence in H, original a-edges e and tau f lie in one connected component of the a-colored original-edge graph. The first touches x; the second touches bar x. Hence x and bar x are joined by a monochromatic original-edge path.

Conversely suppose x and bar x belong to the same nontrivial a-colored connected component C_a. Pick an a-edge e incident with x and an a-edge g incident with bar x. Then f=tau g is a (1-a)-edge incident with x. Take two chambers K,K' rooted at x with first directions e,f respectively and with the other direction second; they are adjacent across s_1. The edge K->K' is the unique sign crossing. The first-edge color-(1-a) chamber component of K' is tau C_a, and it also contains tau K. By H, K' can be joined to tau K through chambers having first-edge color 1-a. Their concatenation gives the required gallery K->tau K. QED.

**Significance.** Reducing the interface-crossing count among UNRESTRICTED projective chamber galleries reaches the classical monochromatic antipodal graph-connectivity question. In contrast, NORI1 asks for a one-crossing CANONICAL root-rotation gallery gamma_P, which by G is equivalent to twisted defect one and hence to a monochromatic direction-once antipodal cube geodesic after cyclic re-rooting. The gap is an admissible gallery normal-form theorem, preserving cube direction simplicity, rather than a missing parity identity. No such normal-form theorem has been established.


## K. Signed interface flux and the limits of scalar holonomy

For chambers C of the central Freudenthal sphere X_n, let b(C)=c(first cube edge of C) in {0,1} and s(C)=1-2b(C). Define on oriented dual chamber edges C->C'
theta(C,C')=(s(C)-s(C'))/2=b(C')-b(C).
This is the integral coboundary db on X_n; therefore its sum around every lifted closed gallery is zero, and every gallery C->tau C has theta sum 1-2b(C)=s(C). It is anti-invariant under tau. On Y=X_n/tau=RP^(n-1) it defines a cochain with sign-local-system coefficients Z_-. For n>=3, H^1(Y;Z_-)=Z/2 and theta represents its nonzero class: its integral on a loop lifting C->tau C is odd, while an integral twisted coboundary has even such integral. Reduction modulo two is w_1. Thus additive signed interface flux alone contains only the universal parity obstruction, irrespective of the unsigned number of crossings.

Likewise every chamber cost increment Delta_D(C,C')=D(C')-D(C) is an integral coboundary on the full gallery graph. Summing either scalar increment around closed loops cannot yield a nonzero flux. This rules out a proposed contradiction based solely on such sums, leaving direction-labeled, noncommutative, or admissibility-restricted transports open.

## L. Local square-cancellation rule, including twisted boundary

For n>=3 let P' arise from P by swapping consecutive directions at positions j,j+1, retaining the root. Their two replaced cube edges have color pair (a,b) in P and (a',b') in P'. All other edge colors agree. Define L=w_(j-1)(P) when j>1, and L=1-w_n(P) when j=1. Define R=w_(j+2)(P) when j<n-1, and R=1-w_1(P) when j=n-1. These values are unchanged under the swap. Then
D(P')-D(P)=([L!=a']+[a'!=b']+[b'!=R])-([L!=a]+[a!=b]+[b!=R]).
Both triple variations have parity [L!=R]. Therefore D(P')-D(P) is -2,0, or +2. A reduction by two occurs if and only if either
(i) L=R, the old triple has two switches, and a'=b'=L; or
(ii) L!=R, the old quadruple (L,a,b,R) is fully alternating and the new triple has one switch.
The replacement preserves every original direction and shares all unchanged cube edges. For a globally minimum-defect P, neither descending alternative is possible at any consecutive direction pair. Cyclic root rotation preserves D (it cyclically shifts the antiperiodic word), so every cyclic re-rooting of any global minimizer satisfies this same family of simultaneous local constraints on its own cube squares.

The topological task remaining is to force one permitted descending square or integral multi-route exchange through relations among the original cube edges. Additive interface parity and additive energy alone cannot establish such a forcing statement.


## M. Projective index persists after removing every fixed-root chamber cell

Let m=n-1>=2 and X=X_n be the antipodal all-root dual cell sphere. For each original cube vertex x, let D_x be the closed dual m-cell containing the chambers rooted at x; D_x is a permutohedron. The 2^n cells D_x are pairwise disjoint, because no maximal central face flag contains two distinct outer cube vertices, and tau(D_x)=D_(bar x).

Put U=union_x D_x and A=X\U. Then A/tau is RP^m with 2^(n-1) disjoint closed m-balls excised (up to collars). In particular the restriction
H^(m-1)(RP^m;F_2) -> H^(m-1)(A/tau;F_2)
is injective. One proof: remove slightly larger disjoint open m-ball neighborhoods of the D_x/tau cells; excision gives H^(j)(RP^m,complement;F_2)=0 for j<m, and the long cohomology sequence gives injectivity at j=m-1. This also establishes the same assertion for A after passing to the collar.

**Theorem (unavoidable variable-root zero in rank m-1).** The covering class of A->A/tau satisfies w_1^(m-1)!=0. Hence EVERY continuous odd map F:X->R^(m-1) vanishes at some point of A, strictly outside all root-fixed D_x. Otherwise F/||F|| on A would be equivariant A->S^(m-2), making w_1^(m-1) vanish in its quotient, contradiction. For m=2 the target is S^0 and the nontrivial cover w_1 already forbids such an odd map.

This identifies an index obstacle in the previously published rank-(n-2) switch-profile zero theorems: the ambient equivariant index alone necessarily forces zeros in the variable-root part, so it cannot isolate the root-fixed permutohedra where suffix recombinations share their root.

## N. Relative odd-degree localization after raising target rank

Let A_0=X minus the union of the OPEN interiors of all D_x, so A_0 contains every boundary sphere of those cells and A is its interior. For m=n-1>=2, the top Stiefel-Whitney class of the associated vector bundle
E=(tautological real line bundle)^(direct sum m)
over RP^m is w_m(E)=w_1^m !=0.

Nevertheless there ARE odd maps g:A_0->R^m\{0}. To see this, identify X equivariantly with the standard sphere S^m; choose a point v inside the interior of one original-root cell D_x and define
G(z)=z-<z,v>v in v-perp = R^m.
This is odd, and its only zeros are z=+v and z=-v, both inside the paired cells D_x,D_(bar x). Thus G/||G|| restricts to an odd sphere-valued map on A_0.

**Relative localization theorem.** Given ANY odd continuous g:A_0->R^m\{0}, the sum modulo two of the degrees of its normalized restrictions to the boundary spheres of one representative D_x from each antipodal pair is 1. Consequently an odd extension of g to X must have zeros in the original-root cells, and a transverse extension has an odd number of antipodal zero pairs there.

*Proof.* The nonzero g is a nonvanishing section of E over A_0/tau. The mod-two relative obstruction to extending this section over the removed m-balls equals the top Stiefel-Whitney class w_m(E). Evaluating it on the mod-two relative fundamental class of (RP^m,A_0/tau) gives <w_1^m,[RP^m]>=1. The local obstruction on an m-ball is the degree modulo two of g/||g|| on its boundary. Their sum is therefore odd. A transverse extension counts those local degrees via its isolated zeros. QED.

The rank-(n-1) relative architecture permits an equivariant obstruction to be placed among root-fixed path families. It does NOT supply a coloring-sensitive g nonzero on the variable-root region, nor a decoder turning a zero within one D_x into two paths passing through a common intermediate cube vertex. This is a conditional geometric option, not an NORI1 implication. It suggests that the missing color-dependent transport should be sought before imposing a new topological labeling; for rank n-2 the desired localization is obstructed in principle.


## O. The phase-signed switch field is a discrete color derivative; localization to at least two root-free directions

For a rooted antipodal full geodesic P write its binary word w_1,...,w_n. Assume n>=4 and that the coloring has no monochromatic full antipodal geodesic. Then the ordinary switch count is at least two, so
k(P)=sum_(j=1)^(n-2)[w_j!=w_(j+1)]>=1.
The phase-signed profile introduced above has entries
Gamma_j(P)=(-1)^w_j [w_j!=w_(j+1)]/k(P)
=(w_(j+1)-w_j)/k(P), 1<=j<=n-2,
where the last equality is in the integers. Thus Gamma is the normalized finite difference of the original binary color word. Convex cancellation among these labels is a path-weighted fractional color-profile balance; it introduces no independent edge-incidence invariant.

Nevertheless it has a useful strict separating functional. Define
L(v)=sum_(t=1)^(n-2) sum_(j=1)^t v_j
=sum_(j=1)^(n-2)(n-1-j)v_j.
Then telescoping gives
L(Gamma(P))=(1/k(P)) sum_(h=2)^(n-1)(w_h-w_1)
=(-1)^w_1 N(P)/k(P),
where N(P)=#{h:2<=h<=n-1, w_h!=w_1}. Since k(P)>=1, N(P)>=1. Hence L(Gamma(P)) has strictly positive sign if the first edge is color zero and strictly negative sign if it is color one.

In the all-root Freudenthal dual sphere X_n, denote by D_F the top dual cell indexed by a nonempty proper cube face F. Every chamber vertex of D_e, for an original cube edge e, uses e as its first original edge. Any barycentric PL extension of Gamma obtained by averaging chamber labels on dual cells consequently has a constant strict sign under L on all of D_e, and cannot vanish there.

By the earlier punctured-sphere index theorem, every odd map X_n->R^(n-2) must vanish outside the union of all root-fixed D_x. Apply that theorem to this odd extension of Gamma. Since it is nonzero on every D_e, at least one of its zeros lies outside
union_(dim F<=1) D_F.
The top dual cells cover X_n, so such a zero belongs to a D_F with dim F>=2. Its chamber labels come from rooted full cube geodesics first traversing F, and the zero is a convex combination of labels of geodesics starting in BOTH colors. Therefore the original square-containing face F has edges of both colors.

**Quantifier limitation.** This zero is guaranteed in a top dual face carrier D_F with dim F>=2. The punctured-sphere argument by itself does not place it in an (n-2)-dimensional dual cell indexed by a two-face flag. It does not give a shared root, a shared middle cube vertex, or a global minimum-defect witness. The localization identifies where topology and first-edge color meet without solving integrality.

## P. Independent middle-layer colors obstruct braid-only forcing

Let F be a proper three-dimensional face in Q_n, n>=4, with opposite corners u and v. The six direction-once paths from u to v have three shared lower-edge possibilities, six pairwise distinct middle-layer edges, and three shared upper-edge possibilities. Fix all lower and upper edges to color a. The middle edge used by each of the six direction orders is different, so its color b_pi may be chosen independently for each permutation pi. As F and its antipodal face have disjoint edges, these prescriptions extend to a legal antipodally odd coloring on the whole cube.

Choosing b_pi=1-a for every pi gives the same three-edge word (a,1-a,a) for every route around the rank-three braid hexagon. Fix a common prefix and suffix using all remaining directions and color their edges a. The resulting six full direction-once antipodal paths all have twisted defect THREE: two internal changes and one twisted closing change. Every adjacent interchange restricted to the three-face preserves this defect, so the entire rank-three braid hexagon is a neutral defect-three plateau.

No assertion of global defect minimality is made. The result shows that braid-cell shared-edge constraints in one proper three-face cannot alone force a descending square or phase-opposed switch pair. Any topological forcing argument must use compatibility across other face carriers or simultaneous global minimum-path conditions; analyzing isolated braid hexagons cannot supply unrestricted NORI1 closure.


## Q. Any bounded-face coloring extends to a balanced legal ambient coloring

**Theorem (unrestricted local-face extension under vertex balance).** Fix k>=1 and any binary coloring f of the undirected edges of Q_k. For every even n>=2k+2 and any embedded k-dimensional face F in Q_n, there exists a legal antipodally odd edge coloring c of Q_n whose restriction to F equals f and for which every vertex has precisely n/2 incident edges of each color. The statement allows arbitrary nonlinear f.

*Proof.* By translating exterior bits, assume F is specified by all n-k exterior bits equal to zero. Write I={1,...,k}. Select distinct exterior partners j_i (i in I), and two further exterior directions t,u. The remaining exterior directions, if any, may be paired arbitrarily. For every i in I let f_i(z) be the bit on the i-edge of F indexed by z in {0,1}^{I\{i\}}. Define
g_i(z,s)=f_i(z) when s=0,
g_i(z,s)=1-f_i(1-z) when s=1.
Then g_i(1-z,1-s)=1-g_i(z,s). On the ambient cube set
c_i(x)=g_i(x_{I\{i\}},x_t),
c_{j_i}(x)=1-g_i(x_{I\{i\}},x_t).
Both functions ignore their respective edge-direction bits, so they color undirected edges consistently. They complement under the full cube antipode. For the pair (t,u) and all remaining exterior pairs (p,q), set c_p(x)=x_1 and c_q(x)=1-x_1. These also ignore their own bits and complement under the antipode. Every direction pair contains one incident edge of each color at every vertex, proving vertex balance. On F, x_t=0, so c_i|F=f_i. QED.

**Consequence for rank-three forcing.** In every even n>=8, a balanced legal ambient coloring can realize all twelve edge colors of any chosen Q3 face, including the braid-plateau pattern with lower and upper edges zero and six middle edges one. Hence balance and antipodal oddness alone cannot restrict the six braid-route color words or prohibit their common 010 word. This does NOT show that these six paths globally minimize twisted defect in the ambient coloring, or that the extension is a NORI1 counterexample.

**Research implication.** A proof using vertex balance and face-local relations needs an additional globally imposed condition: global minimizer inequalities, simultaneous face transport, or other constraints coupling the assigned face with the rest of the cube. The theorem applies to all fixed k as the ambient even dimension grows, so adding finitely many directions to an isolated local laboratory does not generate those global constraints.


## R. Monochromatic permutohedral witness spaces and square-prism transport

Fix an original cube root x, a direction subset S, and a color a in F_2. Write Perm(S) for the type-A permutohedron, whose vertices are the permutations of S and whose faces are indexed by ordered partitions B_1|...|B_t of S. For a permutation pi of S let P(x,pi) be the corresponding direction-simple geodesic prefix from x to x^S.

Define the **monochromatic order complex** O_x^a(S) to be the CW subcomplex of Perm(S) consisting of those faces B_1|...|B_t for which EVERY permutation refining that ordered partition gives a color-a path P(x,pi). This is a CW subcomplex because faces of an ordered-partition face have fewer refining permutations, so the color condition is hereditary. Vertices are single direction-simple, shared-edge-consistent monochromatic paths. For S empty let O_x^a(empty) be a point representing the empty path in either color.

**Theorem 1 (colored-edge face inclusion).** Let i notin S, put y=x^i, and suppose the original edge xy has color a. The operation of prefixing direction i defines a canonical cellular embedding
T_i: O_y^a(S) -> O_x^a(S union {i}),
whose image lies in the permutohedral facet {i}|S. Every vertex image is an original-cube path with mutually distinct directions, and the map retains its ordered word of cube edges after the new initial edge.

*Proof.* Each permitted tail from y uses S, so prefixing i creates a color-a path with direction support S union {i}. The face indexed B_1|...|B_t maps to the face {i}|B_1|...|B_t. Its refinements all have the chosen red/blue initial i-edge followed by monochromatic tails. The standard ordered-partition face relation makes this a cellular embedding. QED.

**Theorem 2 (monochromatic square prism).** Let i,j notin S and z=x^{i,j}. Assume all four original edges of the ij-square through x have color a. Then the two composite prefix maps from O_z^a(S) to O_x^a(S union {i,j}) occur at the two ends of a canonical embedded cellular prism
Perm({i,j}) times O_z^a(S) -> O_x^a(S union {i,j}),
where Perm({i,j}) is the 1-cell with endpoint direction orders ij and ji.

*Proof.* Every permutation of {i,j} traverses two a-colored edges and finishes at z. Subsequent tails are the same paths from z, so each refinement of {i,j}|B_1|...|B_t is a-colored. The face of Perm(S union {i,j}) corresponding to this partition is the product Perm({i,j}) times Perm(B_1) times ... times Perm(B_t), and restricts to the indicated prism on O_z^a(S). Its endpoints are the two concatenation maps. QED.

**Higher coherence.** For any R disjoint from S such that every edge of the original R-face from x to x^R has color a, the same argument embeds Perm(R) times O_(x^R)^a(S) in O_x^a(S union R). For |R|=3 this includes the full type-A braid hexagon AND its filling 2-cell; for larger R it includes all higher permutohedral face coherences. The construction therefore absorbs the exchange relation into a path-carrying CW cell whenever the relevant original face is monochromatic. When a face contains mixed colors, some concatenations or higher cells may be absent; this absence is retained instead of asserting a false chain cancellation. Antipodal translation sends O_x^a(S) isomorphically to O_(bar x)^(1-a)(S), preserving direction orders.

**Converse and scope.** O_x^a([n]) is nonempty if and only if a monochromatic antipodal direction-simple geodesic of color a exists from root x. The local prism theorems preserve witnesses and all higher all-monochromatic-face coherence, but they do not establish global nonemptiness of O_x^a([n]) for some root. In particular the disjoint union of root-fixed complexes has insufficient antipodal index; the remaining task is a global homotopy-coherent diagram of these path spaces across roots, supporting a topological forcing argument.

## S. Median three-arm obstruction expressed in monochromatic path spaces

Let P be a globally minimum-twisted-defect full geodesic with d=D(P)>=3 odd. Choose any admissible triple p_0,p_1,p_2 of red-to-blue seam-boundary vertices on the doubled antiperiodic color cycle, with all three forward seam gaps g_i between 1 and d-1 and sum g_i=2d. Their coordinatewise median m has three nonempty, disjoint direction supports A_i=D(m,p_i) partitioning [n].

Put M_i=O_m^0(A_i) disjoint-union O_m^1(A_i). Then
M_0 times M_1 times M_2 is EMPTY.

*Proof.* Otherwise select one vertex H_i in each M_i. These are monochromatic median arms with s_i=0 internal changes and first colors alpha_i in F_2. The established three-route reconstruction in this same original coloring gives three complete direction-simple geodesics R_i satisfying
sum_(i=0)^2 D(R_i)=d+Delta,
where Delta=sum_i [alpha_i != alpha_(i+1)] is either 0 or 2. Since d>=3, d+Delta<=d+2<3d. Thus some R_i has D(R_i)<d, contradicting global minimality. QED.

This product-emptiness conclusion is an integral, root-specific condition on a hypothetical counterexample. Unlike fractional switch-profile cancellation, every point in each nonempty M_i lies in a face consisting of original monochromatic witnesses; any triple of vertices reconstructs an improved full path. The remaining forcing question is whether the all-root central Freudenthal incidence and partially defined prism maps can imply that at least one admissible seam triangle has all three M_i nonempty. Such a theorem would settle unrestricted NORI1. Neither a global index theorem for this diagram nor the required nonempty triple has been established.


## T. Color-sensitive path-space factorization

For root x, color a, and direction set S, let O_x^a(S) be the monochromatic permutohedral witness complex of part R. For nonempty disjoint T,U with S=T union U, the ordered-partition facet F_(T|U)=Perm(T) times Perm(U) satisfies the STRICT identity
O_x^a(S) intersect F_(T|U) = O_x^a(T) times O_(x^T)^a(U).
Indeed every order refining T|U uniquely concatenates a T-path from x and U-path from x^T. It is a-colored iff both constituent paths are a-colored; the equivalence holds for every product face. This is integral root- and vertex-matched witness factorization.

The union of all monochromatic witness spaces across roots, supports, and colors, glued by every same-color prefix map and monochromatic square/face prism, retains a locally constant color a. Antipodal translation complements a. Thus its color map to S^0 is antipodally odd, so its projective covering has zero w_1. Nontrivial index requires mixed-color transition structure.

Disconnected witness fibers persist in arbitrary rank. For k>=3, color red only the two monotone Q_k paths from 0 to all ones given by orders 1,...,k and k,...,1. They have no shared interior vertex, and each interior vertex has a unique red increasing successor. Thus only these two full orders are red; no monochromatic square exchange joins them. O_0^0([k]) is two isolated vertices. The pattern extends legally from a proper face into Q_(k+1); the previously proved balanced local-face extension (part Q) also embeds it in a balanced legal Q_n for even n>=2k+2.

## U. Balanced median support obstruction

For n=6h partition the directions into B_0,B_1,B_2 of size 2h. Pair directions inside each block, and pick a controller direction t_l in the NEXT block B_(l+1 mod 3). For paired i,j in B_l prescribe c_i(x)=x_(t_l), c_j(x)=1-x_(t_l). Each color function ignores its edge direction; antipodality complements it; each pair contributes one edge of each color at each vertex. The coloring is legal and vertex-balanced.

For ANY root y, no monochromatic geodesic can use all directions of B_l: both directions of each pair occur, while their controlling bit outside B_l remains fixed, giving opposite colors. Thus O_y^0(B_l)=O_y^1(B_l)=empty.

For a path P rooted at zero with order B_0,B_1,B_2, select times 0,4h,8h on the doubled antiperiodic path. The three cyclic gaps are 4h=2n/3<n. Their coordinatewise median is m=1_(B_1), and the median-arm direction supports are B_1,B_0,B_2, all of length 2h=n/3<=n/2. All six color-specific arm complexes are empty. Therefore balance plus short arm length cannot produce prescribed-support monochromatic arms. The selected P is not asserted globally minimum. The open forcing mechanism must use global minimum-defect constraints and color-sensitive mixed-color transport.


## V. Switch-filtration collision detects global minimum twisted defect

Let n>=2, c be any antipodally odd binary edge coloring of Q_n, and X_x be the fixed-root Freudenthal triangulation. For integer r>=0 let K_x^[r] subset boundary(Q_n) denote the simplicial subcomplex generated by the simplices spanned by proper prefixes of full direction-once geodesics from x having at most r ordinary switches; either first color is admitted. Every simplex admits a prefix witness with its color word and direction order. K_x^[r] is a cone with apex x, and its antipodal translate is K_(bar x)^[r]. These two subcomplexes use the same un-oriented triangulation because reversing each saturated chain from x gives one from bar x.

**Theorem (first collision detects twisted-defect minimum).** Put d_*(c)=min_P D(P), where P ranges over all full original-cube antipodal geodesics, and D(P)=ordinary_switches(P)+[last_color(P)=first_color(P)]. Then for all r>=0,
exists x with K_x^[r] intersect tau K_x^[r] nonempty iff d_*(c)<=2r+1.
Consequently, if r_* is the first integer with any such intersection, d_*(c)=2r_*+1.

*Proof.* Any intersection of these two subcomplexes contains a common vertex, since they are subcomplexes of one triangulation. A common vertex is an original cube vertex y=x^S, with proper nonempty direction supports S and S^c witnessing two prefixes P,Q from x with <=r switches and antipodal endpoints y,tau y. Concatenate reverse(P) with Q to obtain one full antipodal direction-simple geodesic W, with ordinary switch count at most 2r+1. Its twisted defect is odd and no larger than 2r+1.

Conversely, any full geodesic with twisted defect <=2r+1 has ordinary switch count s<=2r+1. If s>0, cut at a middle switch so that the two arms have <=r internal switches each. If s=0 cut at any internal vertex. Reverse the two arms to give proper prefixes from their common root x to the two antipodal original endpoints. Their supports are complementary and their common vertex in the rooted Freudenthal triangulation lies in K_x^[r] intersect tau K_x^[r]. Every twisted defect is odd, proving the minimum formula. QED.

Define Y_x^[r]=boundary(Q_n) minus (K_x^[r] union tau K_x^[r]). By Alexander duality for two contractible cone complexes,
reduced H_(n-2)(Y_x^[r];Z) is Z if the cones are disjoint, and zero if they meet. Indeed the corresponding reduced H^0 of the removed union has rank one before contact and zero after contact. Thus d_*(c) is twice the first disappearance rank of this Alexander-dual homology class at any root, plus one. At every r<r_*, each Y_x^[r] has the integral homology of S^(n-2) and nonzero covering w_1^(n-2), by the same free-involution Serre spectral sequence used in the color-blind budget-zero carrier.

**Tightness at first contact.** Suppose d_*(c)=2r+1 and complementary prefix witnesses P,Q at one x have internal switch counts p,q<=r and initial colors a,b. Their concatenation has ordinary switch count s=p+q+[a!=b], which must equal 2r or 2r+1: otherwise its twisted defect would be <2r+1. If a=b then p=q=r. If a!=b, the only possibilities are (p,q)=(r,r), (r-1,r), or (r,r-1) (with negative entries discarded at r=0). Thus both arms at a first contact nearly exhaust their budgets.

## W. Optimal seam simplices lie in the first-collision intersections

Let P be any full original antipodal geodesic of twisted defect d=2r+1>=3. Write its antiperiodic doubled path as vertices v_t and edge colors w_t, with v_(t+n)=tau v_t and w_(t+n)=1-w_t. List seam-vertex times where consecutive edge colors differ as
... < s_i < s_(i+1) < ...,
so s_(i+d)=s_i+n. Put x_i=v_(s_i).

**Theorem (seam-run intersection simplex).** For each i, the simplex
Delta_i = conv{v_t : s_(i-r-1)<=t<=s_(i-r)}
of the original Freudenthal triangulation belongs to BOTH K_(x_i)^[r] and tau K_(x_i)^[r]. Its dimension is
g_i=s_(i-r)-s_(i-r-1)>=1.
The antipode sends Delta_i to Delta_(i+d), and one period has d such simplices with sum_(i=1)^d g_i=n.

*Proof.* The backward segment from x_i to v_(s_(i-r-1)) has r internal switches, at s_(i-r),...,s_(i-1), and fewer than n edges. It is a direction-simple prefix and its Freudenthal simplex contains Delta_i. The forward segment from x_i to v_(s_(i+r+1)) has r internal switches at s_(i+1),...,s_(i+r), and also has fewer than n edges. Because s_(i-r-1)+n=s_(i+r) and s_(i-r)+n=s_(i+r+1), the antipodal translate of the forward segment's Freudenthal simplex also contains Delta_i. The g_i successive directions are distinct, so Delta_i has dimension g_i. Antipodality and the dimension sum follow from seam periodicity. QED.

For each interior integer t of this run interval, the two truncated prefixes from x_i to v_t and tau v_t have switch counts (r,r). At one endpoint their counts are (r,r-1), and at the other they are (r-1,r), matching the first-contact saturation alternatives above. In particular if P attains the GLOBAL minimum d_*(c)>=3, these d antipodal-paired positive-dimensional simplices lie in the VERY FIRST nonempty intersections of the two rooted cone filtrations; their dimensions sum to n. This supplies a spatially structured incidence family, not just independent complementary support pairs.

## X. Flatness of the pre-collision top-homology root-transport system

Let xy be an original color-a edge in direction i, and fix r<r_*. Let C_x^[r],a be the restriction to the i-fixed facet through x of the subcone of K_x^[r] represented by a-initial paths; define C_y analogously. Each is a contractible cone with its corresponding root apex. Define the bridge
B_xy^[r],a = C_x^[r],a union [x,y] union C_y^[r],a.
Prepending xy to a path starting in a does not increase its switch count and preserves direction simplicity because the path stays in the i-fixed facet. Therefore B_xy^[r],a is a contractible subcomplex of K_x^[r] intersect K_y^[r]. It is disjoint from its antipode, because K_x^[r] and tau K_x^[r] are disjoint. Let Y_B be the complement of B_xy^[r],a union its antipode in the cubical boundary sphere. The inclusions
Y_x^[r] -> Y_B <- Y_y^[r]
induce top integral homology isomorphisms by naturality of Alexander duality, identifying the generators marked by the original roots. Since each generator maps to its root-marked counterpart, every closed original-root loop has identity top-homology transport; the comparisons for successive r are compatible under inclusion.

Consequently BEFORE first collision, the whole all-root persistent top-homology system is merely a constant rank-one system: ordinary top homology, its antipodal index, and transport around root squares cannot force premature death at r=0. Any proof of NORI1 via this filtration must control the nontrivial CHAIN-LEVEL or direction-support data attached to the first-collision simplices, or another color-sensitive global constraint. No such forcing theorem is claimed.

Computational checks of the first-collision identity on randomized antipodally odd colorings in ranks 2 through 5 were consistent with the proofs. The seam-simplex dimension formula was separately checked on several antiperiodic words. These checks are not used in the proofs.


## Y. The two antipodal actions and a root-uniform projective obstruction

Let n>=3, m=n-1, and assume no monochromatic full antipodal geodesic. For a root x define the color-blind Freudenthal prefix cone K_x (union of both colors) in the geometric cube boundary S^m. It is a cone with apex x, its antipode tau K_x is disjoint, and Y_x=S^m\(K_x union tau K_x). Root antipodality gives K_(bar x)=tau K_x and Y_(bar x)=Y_x.

Write v_x for the normalized centered Euclidean root sign vector in S^m. The map
rho_x(z)=(z-<z,v_x>v_x)/||z-<z,v_x>v_x||
is defined on Y_x and maps into the orthogonal equator S(v_x^perp). It is a Z_2-equivariant homotopy equivalence with respect to z->-z: the inclusion Y_x -> S^m\{+v_x,-v_x} is an integral homology equivalence by Alexander duality and naturality for the two deleted contractible components, and both spaces have the homotopy type of S^(m-1) using the PL regular-neighborhood ball theorem. The larger complement deformation-retracts by rho_x. For m>=2 this yields a homotopy equivalence (and an equivariant one by the free-action Whitehead principle).

Crucially, rho_(bar x)(z)=rho_x(z), whereas rho_x(-z)=-rho_x(z). Root change and fiber antipodality are distinct. Their distinction identifies the rank-m orthogonal-complement bundle E=gamma^perp over RP^m for ROOT-even sections; it is NOT the tangent bundle, whose deck action also negates tangent vectors. Since gamma plus E is trivial of rank m+1,
w(E)=(1+u)^(-1)=1+u+...+u^m,
where u=w_1(gamma). In particular w_m(E)=u^m!=0 for EVERY m>=1, including dimensions where T RP^m is parallelizable.

**Theorem (projective root-selector collision).** Every even continuous map f:S^m -> S^m (f(-p)=f(p)) has some p with f(p)=+p or f(p)=-p. Indeed, if none, then s([p])=f(p)-<f(p),p>p is a nowhere-zero section of E, contradicting w_m(E)!=0.

**Root-cell relative version.** Let X_n be the dual all-root Freudenthal sphere, identified antipodally with S^m, and D_x its top-dimensional root-fixed dual cells. Delete the interiors of all D_x and call the remaining antipodally invariant subcomplex A. A root-even nonvanishing section of E can be defined on A: choose an arbitrary point a in the interior of one root cell D_x and put s(p)=a-<a,p>p; its only zeros lie at +a,-a inside the chosen pair of root cells. For ANY root-even nowhere-zero section on A, the sum modulo two of the relative degrees of its normalized boundary restrictions on one representative of each root-cell antipodal pair equals 1. This is the relative top Stiefel-Whitney obstruction, w_m(E), evaluated on the projective fundamental class. It localizes a compulsory odd obstruction to root-fixed cells, unlike the rank-(m-1) switch-profile obstruction whose zeros remain compulsory in the variable-root region.

**Precise unresolved forcing gate.** Under absence of NORI1, can one construct a color-dependent root-even selector on the variable-root subcomplex A, retaining original used-direction sets on shared faces, whose boundary map on each D_x is nullhomotopic whenever there is no monochromatic full path from x? Such a construction would contradict the odd relative-degree sum and prove NORI1. Topology proves the parity, but supplies NEITHER this color-sensitive selector NOR the root-local degree-zero decoding; either assertion is open. Merely choosing an arbitrary root-even section on A is possible for every coloring, and its root-cell boundary degrees necessarily sum to one.

The root-projection equivalences themselves are color-independent: they cannot prove NORI1 from ordinary homology or scalar projection alone. The place where the coloring could enter is the compatibility of selections over overlapping root-face carriers in the common central Freudenthal subdivision. A root-edge colored bridge covers the original geometric edge and permits continuous motion of the projection axis across that edge while avoiding its antipodal excluded edge. Mixed-color squares and higher missing-face regions do not automatically supply such fillings. The prior rank-three example with every boundary square covered but an unfilled three-dimensional cap shows why testing square filling alone cannot solve this gate.


## Z. Obstruction-degree gauge audit and relative topology of uniform-direction faces

Session session_nori_r12147_2. This is a correction of the interpretation of the projective root-reversal construction, not a proof of NORI1.

Write m=n-1>=2. In the dual all-root Freudenthal m-sphere X, the codimension-one dual cell of any chain of proper original faces F subsetneq G is incident with precisely the two top dual cells D_F and D_G. Let f be an odd nonvanishing map on the dual (m-1)-skeleton with target S^(m-1). Define the mod-two attaching-degree cochain omega_f(F)=deg_2(f on boundary D_F). Its cohomology class on X/tau=RP^m is u^m!=0.

**Gauge lemma.** A degree-one bubble inserted in the relative interior of D_(F<G), with its antipodal mate, toggles omega(F) and omega(G), and no other top-cell charge. Thus omega' = omega + delta chi_(F<G). When F and G are non-root fully color-varying faces, such a perturbation can avoid all root-cell boundaries and all cells on which a uniform free-direction color imposes a strict hemisphere condition. Individual charges on nested mixed faces therefore are not color invariants.

**Color-free model with both symmetries.** Let r_i(pi)=2 pos_pi(i)-(n+1), so r(pi) is a nonzero vector in W=1^perp. Put eps(x)=(-1)^(x_1) and Psi(x,pi)=eps(x)r(pi). Both identities
Psi(bar x,pi)=-Psi(x,pi) and Psi(x,reverse(pi))=-Psi(x,pi)
hold without using an edge coloring. Equivariant skeletal extension therefore forces degree one on every root-cell boundary and total non-root charge one, just as the color-sign field does. The projective parity and the root reversal symmetry alone contain no information about monochromatic cube paths. The hemisphere restrictions derived from fixed-color direction families are the essential input from c.

**Canonical relative obstruction.** Under the hypothetical absence of monochromatic complete geodesics, form the chamber profile v(P)=s(P)-mean(s(P))*1 in W from the direction-indexed original edge signs and extend equivariantly by averaging on dual cells. For a proper face F with some free direction i of constant edge color epsilon, the i-component satisfies epsilon v_i(P)>0 on every chamber refining F, so the extension is zero-free throughout D_F. Let U(c) be the antipodally invariant union of all such uniform-direction D_F. The normalized field over U(c) defines a nowhere-zero section s_c of E=m gamma over U(c)/tau, where gamma is the sign line bundle over RP^m.

The relative Euler obstruction e(E,s_c) belongs to H^m(RP^m,U(c)/tau;F2), maps to the absolute class u^m, and has an invariant meaning independent of the chosen skeletal completion. Put A=X minus the interiors of all root-fixed D_x. The question relevant to NORI1 is whether s_c admits a nowhere-zero extension over A/tau that also retains the root-reversal oddness of the resulting restrictions to each boundary D_x. If it did under the no-good-path hypothesis, the root-boundary degrees would all be one and their total over 2^(n-1) antipodal root pairs would be zero, contradicting the ambient class u^m=1. Therefore such an extension cannot exist in a bad coloring.

This identifies the missing color-sensitive forcing obligation as vanishing of a RELATIVE extension obstruction over the variable-root cells, using shared original-edge and direction-simple path compatibility. Merely redistributing the noncanonical face degrees cannot establish the vanishing. The color-free Psi need not obey any prescribed coloring hemisphere condition.


## AA. Root-reversal symmetry as a relative mixed-face obstruction

Session session_nori_r12147_2. Let m=n-1>=2, X the antipodal all-root Freudenthal dual m-sphere, A=X minus the open interiors of its root-indexed dual m-cells, U the antipodally invariant union of the dual cells D_F corresponding to proper positive-dimensional cube faces F with some constant-color free direction, and B=U union boundary(A). All statements use F2 coefficients.

Let M_c have vertex set the antipodal orbits of non-root proper cube faces F for which every free direction takes both edge colors in F. Connect two vertex orbits if they admit nested face representatives F subsetneq G.

**Theorem (mixed-face component computation).**
H_m(A/tau,B/tau;F2) is the vector space of locally constant functions on M_c, and
H^m(A/tau,B/tau;F2) is isomorphic to F2 raised to the number of connected components of M_c.

Proof: Relative m-cells are the mixed faces. A relative (m-1)-facet indexed by F<G survives iff both faces are mixed: facets meeting a uniform-direction top cell lie in U, while facets meeting a removed root top cell lie in boundary(A). A mod-two top chain is a cycle iff its coefficients agree across each surviving facet, which is equivalent to constancy on each connected component. Field duality completes the result.

**Theorem (unconstrained relative extension vanishes).**
H^m(A/tau,U/tau;F2)=0. For every mixed face F choose a root vertex x in F. The dual facet indexed by x<F is in A outside U and touches only D_F among the remaining top cells. The coefficient of the relative boundary of any top chain on that facet is the coefficient of D_F alone. Thus the top boundary is injective, top relative homology vanishes, and so does top relative cohomology.

Under the no-monochromatic-geodesic hypothesis, the normalized direction-sign color field on U gives a nonvanishing section of E=m gamma. Since S^(m-1) has no homotopy groups below dimension m-1 and the top relative obstruction group over (A,U) vanishes, this section admits a nonvanishing extension over ALL A, if no local direction-order reversal symmetry is required on root boundaries.

However any such extension must violate the additional root-internal reversal-odd boundary condition at some root: otherwise every one of the 2^(n-1) antipodal root-cell pairs would contribute degree one, totaling zero, contrary to the nonzero universal u^m class. This is an essential failure, not just a defect of pointwise equivariance: some root boundary must have even degree.

By contrast, when the boundary data on each root permutohedron are prescribed to be reversal-odd, the relative obstruction to extending them together with the nonvanishing coloring field on U is an element of H^m(A/tau,B/tau;F2), with one possible obstruction degree per connected mixed-face family. Its total evaluation is odd. Once boundary data are fixed, the class is invariant under changing the remaining skeletal extension, although component charges may change if the reversal-odd root boundary maps themselves are replaced.

A dimension-uniform proof of NORI1 through this program must use the shared original cube edges and direction-simple paths to force a compatible extension that ALSO preserves every root-reversal symmetry. Ordinary homology and unconstrained extension cannot do this: the obstruction is entirely in simultaneous compatibility of local root involutions across the mixed-face diagram. The requisite compatibility theorem remains open.


## AB. Projective selector obstruction: cycle-graphical zonotope

Session session_nori_r12147_2. Let q(P)=x xor B(P), where B(P) is the set of blue directions along rooted full geodesic P=(x,pi). Then q(tau P)=q(P), q(x,rev pi)=bar q(P), and q(P) equals x or bar x iff P is monochromatic. The sign-vector map b_i(P)=(-1)^(q(P)_i) is even under root antipodality and odd under within-root order reversal. Its continuous even extension over the full all-root sphere always exists because the quotient is RP^(n-1) and S^(n-1) is (n-2)-connected. Projective coincidence of this extension does not force incidence at an integral chamber.

**Theorem (complete selector image at a bad root).** Let n>=3 and define the legal antipodally odd affine coloring c_i(x)=x_(i+1 mod n). At root x=0 and order pi, the blue directions are
B_0(pi)={i:i+1 precedes i in pi}.
They form the backward edges of the directed n-cycle relative to pi. Every order gives a nonempty proper subset, since a directed cycle cannot be consistently oriented by a linear order. Conversely any nonempty proper B gives an acyclic orientation of C_n and therefore has a topological order pi realizing B. Hence {q(0,pi):pi in S_n}=Q_n without {0,1^n}. No root-zero path is monochromatic.

The map from orders pi to B_0(pi) is the braid-fan quotient to the graphical fan of C_n. Its graphical zonotope has 2^n-2 vertices, indexed by acyclic cycle orientations (standard graphical-zonotope theorem, Chapoton--Pilaud, Prop. 1.33--1.35, https://ahl.centre-mersenne.org/item/10.5802/ahl.225.pdf). For n cyclic rotation orders the paths have colors 0^(n-1)1 and q takes the n singleton values e_i. The average of their centered sign vectors v_(e_i)=((-1)^((e_i)_j))_j equals ((n-2)/n)v_0, on the positive root axis, without any monochromatic path among those witnesses.

For a general root x, B_x(pi)=shift(x) xor B_0(pi), where shift(x)_i=x_(i+1). A root admits monochromatic paths of both colors iff x is not constant. Thus only 0 and 1^n are bad roots, while all other roots satisfy NORI1. This family refutes any prescribed-root decoder based only on the nontrivial size, dimension, or projective parity of the available selector set. The missing topological mechanism must couple different roots through shared cube edges while retaining the path-order witnesses.

**Reversal-root dilation.** Within the all-root chamber graph, let J reverse pi and r_0 flip x along pi_1. Then J r_0 J flips x along pi_n, a move of gallery distance 2n-1: move pi_n to first, flip root, move it back. The color-word changes under this nonlocal root move are Delta_(pi_n)c_(pi_j) at the original edges in positions j<n, with the last edge unchanged. Thus transport between the two involutions requires information across an unbounded family of original squares; a lone scalar facet condition cannot guarantee it.
