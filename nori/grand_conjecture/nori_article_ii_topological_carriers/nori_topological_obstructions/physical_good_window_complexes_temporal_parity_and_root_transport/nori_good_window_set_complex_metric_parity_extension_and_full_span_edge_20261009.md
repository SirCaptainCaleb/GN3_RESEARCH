# Good-window complex extends connector parity; forced-window collapses sharpen the grand index target to n−4

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
