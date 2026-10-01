# Strong-rainbow shadow formulation of the punctured-Steiner residual obstruction

## Statement

Let R be any linear 3-uniform hypergraph, and let S be its 2-shadow, coloring each covered pair uv by the unique third vertex c(uv) such that {u,v,c(uv)}∈E(R). Let
  Q=v_0v_1...v_k
be a simple graph path in S. Then the corresponding hyperedges
  E_i={v_{i-1},v_i,c(v_{i-1}v_i)}
form a k-edge linear hypergraph path in this order if and only if the k colors c(v_{i-1}v_i) are pairwise distinct and none belongs to {v_0,...,v_k}.

Call such a graph path strongly rainbow.

Consequently, in the punctured-Steiner residual R of efe44a01f2dc on 2d-1 vertices, a hypothetical nonspecial maximum-rank edge forces the following: for every pair {a,b} in either terminal matching F_y or F_z, the colored shadow S contains no strongly-rainbow path of length d-2 ending at a and avoiding b, and none ending at b and avoiding a. Meanwhile the uncolored shadow is K_{2d-1} minus the four matching classes F_x,F_y,F_z,L_R of e6c8f5225c3f; its complement has degree two at the three high vertices and degree four at every low vertex.

## Body

Because R is linear, each covered pair uv belongs to a unique hyperedge, so the third-vertex coloring is well-defined and proper.

For the path Q, consecutive parent hyperedges E_i,E_{i+1} both contain v_i. They cannot share any second vertex because R is linear, so consecutive intersections are exactly the intended joints v_i.

Now consider nonconsecutive parent edges E_i,E_j, |i-j|>1. Their graph-edge endpoints are disjoint because Q is a simple graph path and the two edges are nonconsecutive. Hence a nonconsecutive intersection can occur only if:
- their colors coincide; or
- the color of one edge equals an endpoint of the other graph edge.
Thus all nonconsecutive parent edges are disjoint exactly when the edge colors are pairwise distinct and no edge color is any graph-path vertex. Under this condition the E_i form a linear hypergraph path. Conversely, any repeated color or color/path-vertex coincidence creates an unwanted nonconsecutive intersection (or, if the coincident path vertex is on an adjacent graph edge, linearity of the underlying triple forces the same obstruction through the corresponding triangle); hence a lifted linear path requires precisely the stated strong-rainbow condition.

Apply this to the residual R from efe44a01f2dc. Its forbidden residual (d-2)-edge endpoint paths are exactly strongly-rainbow shadow paths of length d-2. The no-path assertion for every pair of F_y and F_z is therefore the stated strong-rainbow endpoint obstruction.

Finally e6c8f5225c3f gives
  E(complement S)=F_x ⊔ F_y ⊔ F_z ⊔ L_R.
A high vertex q* is omitted by F_q and by L_R (its leave mate q lies outside R), so it lies in exactly the other two star matchings and has complement degree two. Every low vertex lies once in each F_x,F_y,F_z and once in L_R, hence has complement degree four.
