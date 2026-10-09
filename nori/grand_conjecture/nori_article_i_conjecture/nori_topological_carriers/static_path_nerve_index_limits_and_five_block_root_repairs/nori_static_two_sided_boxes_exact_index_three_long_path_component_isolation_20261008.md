# Static physical boxes have exact index three; long paths are isolated root/support blocks

# The two-sided physical-box carrier has EXACT index three: constant-dimensional odd test and isolated long-path blocks

This combines the actual 2n-bit endpoint difference, the exact physical root-sheet fiber theorem, and the Helly box-intersection theorem. Inputs:
- nori_two_sided_root_sheet_helly_equivariant_exact_grand_fixedpoint_index_four_ceiling_20261008
- nori_two_sided_box_exact_root_support_edge_test_high_index_packet_graph_selection_20261008
- nori_root_complement_endpoint_swap_signed_unused_tucker_high_index_exact_extraction_20261008.

The earlier bound 3<=ind(E)<=4 sharpens to EXACTLY 3 for the incomplete-path part. The strengthening is coloring-independent.

## 1. Difference-image dimension, rather than product-box dimension
Let P=(x,pi) have length k>=3, used W, unused D, and common window-free set M of size max(6-k,0). Its box is
 B(P)=S(P) times S(Theta P).
For delta(a,b)=b-a, its image is the affine coordinate polytope
 delta(B(P))={
 z: z_i=1-2x_i for i in D;
    z_i=0 for i in W\M;
    z_i in [-1,1] for i in M }.
Its affine dimension is |M|<=3. Its LINEAR span has dimension at most |M|+1<=4. If P is incomplete, D is nonempty and this polytope omits zero.

There are finitely many such span subspaces over ALL incomplete rooted direction-distinct paths; this collection does not depend on the coloring or admissibility. Choose a linear map L:R^n->R^4 injective on EACH of these finitely many subspaces. Such L exists: for any fixed subspace of dimension <=4, failure of injectivity is a proper algebraic subset of the matrix space; a finite union of these proper algebraic sets cannot exhaust it.

Then f=L composed with delta is continuous and factor-swap odd, and is NONZERO on every incomplete-path box. On any full-path box delta is identically zero, so f=0 there. Thus on the union of boxes of ACTUALLY ADMITTED <=1-switch paths,
 f(a,b)=0 iff (a,b) belongs to a full admitted-path box.
Any such zero gives a literal grand witness.

This compresses the n-dimensional signed-unused test to FOUR real coordinates on the static box carrier. The linear map can be chosen once for each n, before seeing the coloring.

## 2. Exact cohomological index of the incomplete carrier
Let U_inc be the union of boxes of all admitted INCOMPLETE paths. For n>=4 the universal length-three paths give the earlier index-three base: their union equivariantly retracts to the antipodal 3-skeleton of the n-cube boundary, so w^3 is nonzero.

The nonzero odd map f:U_inc->R^4 normalizes to U_inc->S^3, hence w^4=0. Therefore
 ind_Z2(U_inc)=3.
The equivariant Helly nerve of these incomplete boxes also has EXACT index 3.

This remains true if EVERY incomplete path is admitted, independently of its window colors. Thus the index-three ceiling is a property of static physical-face invariance geometry itself. Under grand failure the full admissible box carrier equals its incomplete part and has exactly this index.

For a free source X with w_X^4!=0, any equivariant continuous map from X into the full admissible carrier forces a grand witness. The earlier packet graph-selection criterion therefore requires source index >=4. Its numerical range improves from n>=t+7 to n>=t+6, including the single-root endpoint-balanced packet source in n>=7.

## 3. Isolation of all paths of length at least six
Suppose B(P) intersects B(Q). The exact edge criterion implies
 W(P)\W(Q) subset M(P),
 W(Q)\W(P) subset M(Q).
Indeed W(P) triangle W(Q) subset M(P) union M(Q), and M(Q) subset W(Q), M(P) subset W(P).

If |W(P)|>=6, then M(P)=empty, so W(P) subset W(Q). In particular |W(Q)|>=6, hence M(Q)=empty also. Thus W(P)=W(Q), and the root part of the edge criterion then gives x(P)=x(Q).

Conversely, two paths with length >=6, the same used support W, and the same root x have IDENTICAL singleton boxes
 B(P)=B(Q)={(x,x XOR ([n]\W))}.
Therefore each nonempty collection of admitted long orders with fixed (x,W) forms ONE COMPLETE SIMPLEX COMPONENT of the nerve, disjoint from all shorter-path components and from all other (x,W) blocks.

If W is proper, Theta exchanges this component with the distinct block (x XOR ([n]\W),W), so these component pairs contribute index zero. If W=[n], the component is Theta-invariant and contains fixed points, and every one of its vertices is already a full grand witness.

Thus static box overlap NEVER transports a short path into a path of length >=6. Its topology beyond the universal base cannot be used as a physical extension mechanism. Long-path admission changes only the isolated block inventory.

## 4. Consequence for the proposed Helly graph-selection proof
Take a CONNECTED, invariant source component with nonzero w^4. Such a component exists whenever a finite source has w^4!=0: exchanged component pairs have trivial cover class, and cohomology is componentwise.

Any equivariant map of this component to the full box nerve has connected image lying in one target component. It cannot land in the incomplete portion, by its index-three upper bound. Hence it must land in an isolated FULL-root simplex component. For a simplicial graph selection, EVERY selected state on this source component is therefore ALREADY A FULL GOOD PATH.

In particular a selection using only proper partial paths is impossible for every coloring, including colorings that possess grand witnesses elsewhere. The conditional selection equivalence remains correct, and this theorem identifies the difficulty hidden in its formulation: obtaining a high-index compatible selection already entails choosing full witnesses on the relevant component.

A useful new carrier must consequently include actual extension/order-exchange incidence beyond static equality of physical windows. The signed-unused face-deletion approach has precisely such incidence available; the static Helly nerve does not encode it.

## 5. Ordered-r-face extension
For window size r and partial length k>=r, |M|=max(2r-k,0)<=r. The same proof compresses delta to R^(r+1), once and for all for each n,r. When n>=r+1, the universal r-path boxes give the antipodal r-skeleton base, so the incomplete static carrier has EXACT cohomological index r.

Every path of length k>=2r forms an isolated (root,used-support) simplex block, by M=empty. This identifies the finite-memory origin of both the index ceiling and the loss of extension connectivity.

## Status
All claims above are proved structural results and exact extraction statements. They sharpen the shared topological frontier and exclude a purely static partial-box selection proof. A forcing theorem on an extension-compatible carrier is still required for unrestricted grand closure.
