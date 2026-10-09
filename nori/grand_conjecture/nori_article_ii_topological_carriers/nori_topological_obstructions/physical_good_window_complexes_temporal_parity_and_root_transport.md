# Physical good-window complexes, temporal parity, and root transport

# Physically certified window topology and root transport

Let \(c\) be an antipodal-reversal-odd binary coloring of ordered physical three-faces of \(Q_n\), \(n\ge6\). A direction-distinct geodesic has a window of three successive ordered free directions at each internal position; the window color depends on its physical face and order. A geodesic is *good* if these colors change at most once.

Define \(W=W_c\) as the simplicial complex whose vertices are actual ordered physical three-face windows and whose simplices are sets of windows appearing *jointly in one actual good geodesic*. An antipodal-reversal involution \(\tau\) sends \((F,\pi)\) to \((\bar F,\operatorname{rev}\pi)\). It acts freely: two windows of a direction-distinct path have distinct free-coordinate sets, while a window and its \(\tau\)-mate have the same free set and different ordered physical labels. Pairwise window compatibility alone need not certify a simplex.

## Exact metric extraction

The center \(m(F)\in\{0,\frac12,1\}^n\) of a physical face defines \(d(u,v)=\|m(F_u)-m(F_v)\|_1\). This distance is integer-valued on pairs of three-faces: free coordinates belonging to exactly one face contribute a total of \(3-|\operatorname{free}F_u\cap\operatorname{free}F_v|\), and differing common fixed coordinates contribute integers.

**Lemma.** If two ordered windows occur in positions \(i<j\) of the same geodesic, then \(d(u,v)=j-i\).

**Proof.** Between successive windows one free direction exits and another enters, changing their face center in two coordinates by one half each. Each coordinate moves monotonically during a direction-distinct geodesic, so the successive \(\ell^1\) displacements of size one add without cancellation. \(\square\)

**Theorem (faithful grand extraction).** NORI holds for \(c\) exactly when \(W_c\) has an edge \(\{u,v\}\) satisfying \(d(u,v)=n-3\).

**Proof.** The extreme windows of a good full \(n\)-edge geodesic furnish such an edge. Conversely, an edge has a single actual good-path certificate. Trimming that certificate between the selected windows produces a good path of exactly \(3+d(u,v)=n\) distinct-coordinate edges, hence a full antipodal geodesic. \(\square\)

In constructing edges, metric coincidence by itself is insufficient. Ordered triples separated by one window must overlap in their last/first two directions; those separated by two must overlap in one specified direction. Disjoint triples permit precisely the common fixed coordinates on which the two physical faces differ as intervening directions. Together with consistent exterior fixed bits, these literal incidence rules give an exact test for existence of a common direction-distinct path.

## Temporal cohomology

On every edge of \(W\) define \(\beta(uv)=d(u,v)\bmod2\). Any triangle has a common actual witness, with window positions \(i<j<k\); thus its coboundary equals \((j-i)+(k-j)+(k-i)=0\bmod2\). Consequently \(\beta\) is a \(\tau\)-invariant one-cocycle. Write \(\bar\beta\in H^1(W/\tau;\mathbb F_2)\) for its descent, and \(w\) for the characteristic class of the antipodal double cover. The cocycle \(\alpha(uv)=\beta(uv)+c(u)+c(v)\) is also invariant, and records same-color transitions along consecutive-window edges. Tracking the change of endpoint colors when choosing different lifts of quotient vertices yields
\[
[\bar\alpha]=[\bar\beta]+w. \tag{1}
\]
The universal physical window-shift graph is connected, so the covering class is nonzero; a physical five-window pentagon has \(\beta\)-value one while lifting closed, so \(\bar\beta\) and \(w\) are independent.

## Physical pentagons give genuine good paths

Fix a physical cube vertex \(z\) and five cyclic directions \(p_0,\ldots,p_4\). Let \(u_i\) be the ordered three-face *through \(z\)* with order \((p_i,p_{i+1},p_{i+2})\), with indices mod five. Each consecutive pair is an actual four-edge witness, so the five mandatory edges form a pentagon in \(W\) of odd \(\beta\)-value. Put \(h_i=c(u_i)\) and \(\delta_i=h_i+h_{i+1}\in\mathbb F_2\). Since \(\sum_i\delta_i=0\), the cyclic change count belongs to \(\{0,2,4\}\). Counting cyclic adjacent pairs of changes gives respectively \(0\), at most \(1\), or \(3\) bad consecutive three-window words. Thus exactly \(5,4,\) or \(2\) of the five cyclic three-window words are good.

The word \((h_i,h_{i+1},h_{i+2})\) is witnessed by the physical five-edge geodesic with direction order \((p_i,\ldots,p_{i+4})\) and start \(z\oplus e_{p_i}\oplus e_{p_{i+1}}\). It supplies the chord \(u_i u_{i+2}\) and its triangle exactly when the word is good; an alternating word has no compatible good-path witness because the intervening ordered physical window is uniquely forced. Hence the local induced five-vertex complex is a pentagon plus precisely \(g\in\{2,4,5\}\) free chord–triangle pairs, each collapsing away to the original pentagon.

The 120 orders on any five directions split into 24 cyclic classes; each contributes at least two good two-bit-rerooted paths. Summing over reference vertices \(z\) and using the bijection
\[
(z,p)\mapsto(z\oplus e_{p_1}\oplus e_{p_2},p)
\]
proves that at least **\(2/5\)** of all actual rooted five-edge paths on a fixed five-coordinate support are good. On each physical five-cube this yields at least \(\lceil (2/5)32\rceil=13\) distinct good roots.

The same odd-cycle argument gives equality of two consecutive windows with probability at least \(1/5\) for a uniformly rooted five-block. For a uniformly chosen full root \(X\) and full direction order \(p\), each of its \(n-3\) comparisons has that marginal law after adjoining one unused direction to its actual four-edge block. Linearity, with no independence assumption, yields
\[
\mathbb E D(X,p)\le \tfrac45(n-3),\qquad
\exists (X,p):D(X,p)\le\lfloor\tfrac45(n-3)\rfloor. \tag{2}
\]
This holds for arbitrary physical ordered-three-face colorings, even without oddness. For ordered \(r\)-faces the analogous bound is \((2r-2)(n-r)/(2r-1)\) when \(n\ge2r-1\).

## The dimension bound and the correct closure class

If the maximum length of a good geodesic is \(k\ge5\), a top-dimensional simplex comprises all \(k-2\) ordered windows of a good length-\(k\) witness. Delete an internal window. Consecutive retained ordered triples overlap in at least one direction; the shared direction occurs once along any direction-distinct path, fixing the relative window positions. The extreme retained physical windows then determine their full direction support and root up to free bits common to all windows, which preserve the entire physical window sequence. Thus the deleted internal window is uniquely forced. Its complementary codimension-one face is free. Performing these collapses in \(\tau\)-paired pairs removes all top-dimensional simplices.

For \(n\ge6\), the resulting equivariant collapses give
\[
\operatorname{ind}_{\mathbb Z_2}(W)\le n-4
\quad\text{for every coloring,}\qquad
\operatorname{ind}_{\mathbb Z_2}(W)\le n-5
\quad\text{under grand failure}. \tag{3}
\]
Therefore **any nonzero degree-\((n-4)\) cohomology class** on \(W/\tau\), for example \(w^{n-4}\) or \(\bar\beta\,w^{n-5}\), is a sufficient certificate of a good full geodesic. The formerly proposed degree \(n-3\) is unavailable even when a full good path exists; a direct equivariant map from the entire index-\((n-3)\) endpoint-balanced permutohedral carrier into \(W\) is ruled out.

A physically certified annulus gives a conditional next step. Let \(P\) be a physical odd pentagon and \(Q\) a genuine path in \(W\) joining one of its windows to its antipodal mate. If the loops \(p=[P]\), \(q=[Q]\) commute up to based homotopy in \(W/\tau\) through actual jointly good-path-certified simplices, they induce \(f:T^2\to W/\tau\) with \(f^*\bar\beta=a+\varepsilon b\) and \(f^*w=b\). Hence \(f^*(\bar\beta\smile w)=a\smile b\ne0\). This proves \(\bar\beta\smile w\ne0\) **under the stated physical annulus hypothesis**.

The remaining missing implication is global: the local pentagons, their root transport, and their individually certified triangles must be glued across actual physical roots and orders so as to produce degree-\((n-4)\) cohomology or, directly, a certified edge at distance \(n-3\). The theorems above supply faithful extraction and unconditional local density; they do not yet prove the unrestricted grand conjecture.

## Recent consequences and compatibility conditions

# Genuine good-window carrier has a connected four-sheeted temporal/antipodal voltage cover

Assume n≥5 and an active NORI coloring of actual physical ordered three-faces, with c(bar F,rev pi)=1-c(F,pi). Let W=W_good(c) be the finite simplicial complex whose vertices are ACTUAL ordered physical 3-face windows and whose simplices are finite window sets jointly contained in ONE actual at-most-one-switch geodesic. The antipodal physical reversal tau acts freely simplicially. Let Y=W/tau.

For any edge uv in W set beta(uv)=d_1(m(F_u),m(F_v)) mod 2, with physical face centers m. By the proved intrinsic distance theorem nori_good_window_set_complex_metric_parity_extension_and_full_span_edge_20261009, any simplex has a common actual good path and d_1 between two windows equals their INTEGER window-position separation on that path. Consequently beta is a genuine tau-invariant 1-cocycle: on each triangle at positions i<j<k the sum of the three edge distances equals (j-i)+(k-j)+(k-i)=0 mod2. Let beta_bar be its descended class in H^1(Y;F2). Write w for the first Stiefel–Whitney class of the actual two-fold cover W→Y.

**Theorem 1 (connected physical window-shift graph).** The 1-skeleton of W is connected, independently of the coloring. Indeed the actual ordered-window SHIFT graph H has one edge for each legal pair of overlapping ordered windows along a 4-edge path; every such path is admitted because it has only two color windows and at most one change. For each coordinate direction i, the induced window-shift graph H_i consisting of ordered windows whose free triple contains i and shift edges having i as one of the two middle directions is CONNECTED by the proved coordinate-retaining shift-graph lemma (Item nori_certified_square_complex_connected_antipodal_one_class_20261008). Any H_i and H_j share windows whose free triple contains both i,j; all windows belong to some H_i. Hence H, and therefore W, is connected.

**Theorem 2 (two independent literal holonomies).** The two degree-one cohomology classes beta_bar and w are LINEARLY INDEPENDENT in H^1(Y;F2). More concretely, the covering associated with the character pair
  pi1(Y) → F2×F2,
  [gamma] → ( <beta_bar,gamma>, <w,gamma> )
is SURJECTIVE. There exists a connected regular 4-sheeted cover of Y with deck group Z2×Z2, with a literal path/window lift model given below.

**Proof.** Fix any physical cube vertex z and any five distinct directions p0,...,p4 in cyclic order. Let u_i denote the ACTUAL oriented 3-face through z with free order (p_i,p_(i+1),p_(i+2)), indices mod5. Every consecutive pair (u_i,u_(i+1)) is realized on one genuine 4-edge geodesic and is thus an edge of W regardless of its two colors. These five edges form a LITERAL CLOSED PENTAGON in W. Each edge has physical-window center distance 1, so beta evaluates to 5=1 mod2 on that closed pentagon. This pentagon is a closed LIFT in W, hence its image in Y has w-voltage zero. It therefore witnesses the character pair (beta_bar,w)=(1,0).

Because the connected W is a free antipodal double cover of Y, some edge path P within W joins any chosen window u to tau u. Its image in Y is a loop with w-voltage 1 (lift changes sheets) and beta_bar-voltage epsilon∈F2, depending on P. Together the two loop voltages (1,0) and (epsilon,1) generate all of F2×F2. Thus the joint character pair is surjective and the classes are independent. \(\square\)

**Theorem 3 (explicit path-certified four-sheeted cover).** Form the beta-parity double cover of W as follows. Its vertices are ordered pairs (u,t) with u an ACTUAL physical window of W and t∈F2. Over any simplex σ={u_0,...,u_k} of W, include precisely its two lifted simplices with labels
  t(u_i)=h+beta(u_0,u_i) for some h∈F2.
The cocycle equation makes the lifting independent of the choice of base vertex u_0 and compatible on common faces. The beta-double cover is CONNECTED because W is connected and the literal pentagon has odd beta-voltage. Physical reversal lifts by
  tilde_tau(u,t)=(tau u,t),
while parity-deck change is
  kappa(u,t)=(u,t+1).
These commuting free involutions generate four deck transformations, giving a CONNECTED REGULAR cover
  (beta-cover of W) → Y
with deck group {1,kappa,tilde_tau,kappa tilde_tau}≅(Z2)^2, over each quotient-window vertex exactly four lifted windows. Every cell is the lift of a simplex already certified by ONE actual good geodesic: there are no invented geodesics or simplex fillings.

**Theorem 4 (three genuine nonzero one-classes and a conditional maximum-distance cup-product extraction).** Let alpha be the descended 1-cocycle with edge value
  alpha(uv)=beta(uv)+c(u)+c(v) mod2,
so on consecutive-window edges it is precisely the monochromatic-shift indicator. The cohomology identity from the good-window theorem gives [alpha_bar]=[beta_bar]+w. Since beta_bar and w are independent, the three classes w,beta_bar,alpha_bar are ALL NONZERO and distinct.

For r=3, if ANY homogeneous polynomial P(w,beta_bar) of total cohomological degree n−3 has NONZERO evaluation in H^(n−3)(Y;F2) — for example w^(n−3), beta_bar·w^(n−4), beta_bar^2·w^(n−5), or alpha_bar^(n−3) — then an actual full n-edge NORI geodesic with at most ONE change MUST exist.

**Proof of conditional extraction.** Under hypothetical grand failure every simplex of W comes from an actual admissible path with at most n−1 edges, hence at most n−3 windows and dimension at most n−4. Because the quotient by free simplicial tau has the same dimension, H^(n−3)(Y;F2)=0. Thus nonzero total-degree-(n−3) cup product forces an n−3-dimensional simplex in W, certified by at least n−2 distinct physical windows on ONE actual good geodesic. Since a direction-distinct path with n edges has at most n−2 windows, this certificate must be a FULL good antipodal geodesic. \(\square\)

**Why this is useful, and exact remaining gap.** The temporal/window-index parity and physical antipodal sheet-flip are two genuinely INDEPENDENT topological monodromies, present for EVERY coloring, with an explicit faithful fourfold lift. This does not by itself prove a NONZERO PRODUCT of degree two or higher: a wedge of two circles also has independent H^1 classes with all degree-two cup products zero. The new, mathematically precise topology-first closure target is to show that actual root/order/witness-incidence cells force ONE high-degree MIXED PRODUCT in the good-window complex quotient. Unlike a pure fixed-root Borsuk–Ulam index, such a product could simultaneously detect rooted progression and physical antipodal transport. The physical five-window Möbius band from Item nori_physical_five_window_mobius_band_pairwise_nonhelly_good_window_complex_20261008 realizes the beta-loop geometrically, while the global window-shift connectivity supplies the w-loop. Demonstrating nontrivial higher-dimensional cup products between these loops is the remaining global compatibility theorem, not yet established.

# A higher-dimensional good-window carrier with exact physical metric and parity class

Inputs:
- exact root-sheet fiber and physical reversal formulas;
- nori_window_shift_monochromatic_edges_universal_cohomology_class_20261008;
- nori_good_contiguous_path_flag_complex_equivariantly_collapses_to_window_graph_20261009.

Let c be an active ordered-r-face coloring, n>r, and let W_good be the finite simplicial complex whose vertices are ACTUAL ordered physical r-face windows. A finite set of window vertices spans a simplex precisely when all occur along ONE actual direction-distinct geodesic whose complete window word has at most one color change. Taking faces is allowed; a simplex need not list consecutive windows. Keep the actual good path as its certificate.

Physical antipodal reversal induces a simplicial involution tau. It is FREE: one geodesic cannot contain a window and its antipodal reversed mate, since these have the same free-coordinate set and a direction-distinct path has distinct free-coordinate sets at distinct window positions. The two ordered windows themselves are distinct under the active coloring law.

## 1. Metric positions are intrinsic to physical windows
For an unordered physical face F let m(F) in {0,1/2,1}^n be its center. For two ordered windows u=(F,pi), v=(G,rho) define
 d(u,v)=||m(F)-m(G)||_1.
This is always an INTEGER for two r-faces: each coordinate free in exactly one face contributes 1/2, and there are 2(r-|free(F) intersect free(G)|) such coordinates; the remaining contributions are 0 or 1.

If u and v occur at window positions i<j along a direction-distinct path, then
 d(u,v)=j-i.
Indeed the successive face centers move monotonically in each physical coordinate. Each window shift moves the exiting and entering free coordinates by 1/2 each in their fixed path directions, giving L1 step length one. Coordinatewise monotonicity makes lengths additive.

Thus their window-position separation is determined by their actual physical faces, independently of which compatible path order witnesses them.

## 2. Exact grand extraction is a maximum-distance edge
Grand closure holds iff W_good has an edge {u,v} with
 d(u,v)=n-r.
The first and last windows of a full good path give such an edge. Conversely, an edge has an actual good-path certificate. Trim that path to the interval from its earlier named window through its later named window. The resulting good path has exactly
 r+d(u,v)
edges. At distance n-r it therefore has n distinct directions and is a full grand witness.

In particular, under hypothetical failure every edge distance is <=n-r-1 and
 dim W_good <= n-r-1.
Always dim W_good<=n-r. This elementary dimension bound admits the stronger free-face reduction in section 5 below. That reduction makes the exponent n-r unattainable even when grand paths exist; the useful forcing exponent is n-r-1 (for r>=3 and n>=r+3).

## 3. The window parity class extends to every dimension
Assign each edge the mod-two value
 beta(uv)=d(u,v) mod2.
This is a SIMPLICIAL 1-COCYCLE on W_good. For any triangle, place its three windows in their actual common good path in order i<j<k. The metric identity gives
 beta(uv)+beta(vw)+beta(uw)
 =(j-i)+(k-j)+(k-i)=0 mod2.
The same edge value is used in every witnessing simplex because d is intrinsic.

It is tau-invariant since physical complementation preserves L1 distances. It therefore descends to a cocycle beta_bar on the quotient (equivalently use the associated cellular/Delta-complex quotient or a common subdivision).

For r=3, W_good contains the ENTIRE physical window-shift graph H: every four-edge geodesic has at most one color change. On H every beta-edge value is 1. The established centered pentagon therefore evaluates beta to 1, proving that the graph parity class SURVIVES in this higher-dimensional carrier. In particular these pentagons cannot become boundaries in W_good.

Define
 alpha(uv)=beta(uv)+c(u)+c(v) mod2.
Then alpha is also a tau-invariant cocycle. On consecutive-window edges it is exactly the monochromatic-shift indicator. Thus the actual connector class extends consistently to higher-dimensional good-path cells, with no arbitrary filling of odd pentagons.

Let w be the cover class on W_good/tau. Choosing lifts of quotient vertices and recording the edge voltage gives the exact cohomology identity
 [alpha_bar]=[beta_bar]+w.
On a lifted closed centered pentagon, w evaluates 0 and beta_bar evaluates 1. Using the established connectedness of H (n>=5), its free cover has nonzero w; since H is contained in W_good, w remains nonzero there. Hence beta_bar and w are linearly independent in H^1 of the quotient. Their higher cup products are now well-defined in a genuinely higher-dimensional path-certified carrier. Nonvanishing of a higher product remains to be proved.

## 4. Why this carrier differs from interval flags
There is a natural equivariant simplicial map from the barycentric contiguous-path poset to the barycentric subdivision of W_good, sending a good path to its set of physical windows. Different path orders can map to the same face or have faces intersect along a NONCONTIGUOUS set of shared windows. The fibers of this identification need not be contractible.

These cross-order identifications retain the information discarded by the interval-poset collapse. Each resulting simplex still has one literal good-path certificate, so the maximum-distance edge extraction remains exact. Static root-box incidence and ordinary contiguous-extension incidence alone do not provide these shared-window cells.

## 5. Forced intermediate windows give one further dimension reduction
Suppose r>=3, and restrict to a hereditary family of good paths of maximum length at most k, where k>=r+2. Then the corresponding window complex equivariantly collapses to a complex of dimension at most k-r-1.

Proof. A top-dimensional simplex sigma consists of ALL t=k-r+1>=3 windows of a good length-k path P. Remove one INTERNAL window w_j, retaining the first and last windows. Consecutive retained windows have position gaps one or two, hence their ordered r-tuples overlap in at least r-2>=1 directions. Any path containing two such tuples must place them at their original signed position difference: a shared coordinate can occur only once, and its two prescribed tuple positions determine that difference. Chaining these overlaps fixes the whole retained window order and all k directions of P.

Moreover, the first and last retained physical windows already have free-set intersection M(P). Thus any root producing the retained physical windows differs from P's root only in M(P), which preserves ALL physical windows. The deleted middle window is therefore uniquely forced. No OTHER simplex of maximum size t can contain sigma without w_j, and no larger simplex exists at this rank bound. Hence sigma without w_j is a free codimension-one face of sigma.

The involution pairs the maximum simplices freely. Choose internal windows in paired mirror positions, and perform the elementary collapses in antipodal pairs. Their free faces are distinct and cannot belong to another maximum simplex by the uniqueness just proved. Removing all maximum simplices leaves dimension at most t-2=k-r-1. QED.

For the full good-window complex this gives, for r>=3 and n>=r+3:
 - ALWAYS: ind_Z2(W_good)<=n-r-1;
 - under GRAND FAILURE: ind_Z2(W_good)<=n-r-2.
For the second line, if a length-(n-1) good path exists, apply the collapse with k=n-1; if all good paths are shorter, the raw dimension bound already gives the conclusion.

Therefore the SHARPENED SUFFICIENT INDEX TARGET is
 w_1(W_good/tau)^(n-r-1) !=0  ==> grand closure.
For ordered three-faces the exponent is n-4, while hypothetical failure gives index at most n-5.

This also clarifies the comparison with the endpoint-balanced permutohedral carrier of index at least n-3: no equivariant map of that entire high-index source into W_good can exist, even for colorings with grand witnesses, because W_good ALWAYS has index at most n-4. A source restriction losing one index, or a different cohomological comparison, is required. An additional odd scalar zero locus has the appropriate index lower bound n-4, but no witness-preserving transfer from such a locus is established here.

## 6. Closure frontier
The good-window complex provides:
 - exact extraction through a maximum-distance edge;
 - higher-dimensional continuation of the two independent window/cover classes;
 - an explicit free-face reduction separating the possible index n-4 from the no-grand ceiling n-5 for ordered three-faces.

The remaining forcing task is to prove nonzero w^(n-4), or another sufficient invariant, using physical cross-order and cross-root witness identifications. Static box intersections and ordinary interval inclusions have the separate low-index obstructions proved in the companion items. A common proper permutation face alone does not certify a simplex of W_good. The grand conjecture remains open.
