# Correction: terminal-shadow lifting requires strong-rainbow, not ordinary rainbow

## Statement

Let G be the terminal-pair graph of a linear 3-uniform hypergraph, with an edge uv colored by the entrance x of its parent hyperedge {x,u,v}. A simple graph path
v_0v_1...v_k
with edge colors x_1,...,x_k lifts in the displayed order to a linear hypergraph path
{x_i,v_{i-1},v_i}, i=1,...,k,
if and only if:
(1) the colors x_i are pairwise distinct; and
(2) no color x_i belongs to the graph-path vertex set {v_0,...,v_k} except in the impossible incident cases excluded by linearity.

Thus ordinary rainbow is insufficient in a self-colored terminal graph. The correct lifting condition is strong-rainbow: pairwise distinct colors, all avoiding the graph-path vertices.

Consequently the counting and degree-stability conclusions (1),(2) of 420e9aea15cc remain unaffected, but its lifting assertion (3) must be replaced by the strong-rainbow statement above; in particular G_11 is not thereby proved rainbow-P_ell-free.

## Body

For the graph path, consecutive parent hyperedges meet in the intended terminal v_i. Because the hypergraph is linear, they have no second common vertex.

For two nonconsecutive graph edges, their terminal endpoint sets are disjoint because the graph path is simple. Hence their parent triples can intersect only through an entrance color: either the two entrance colors coincide, or the entrance color of one parent edge is a terminal vertex of the other graph edge. Pairwise distinct colors eliminate the first possibility but not the second.

Therefore ordinary rainbowness does not guarantee a linear lift. Requiring every entrance color to avoid every graph-path terminal vertex eliminates the second possibility as well, and then all nonconsecutive parent triples are disjoint. This is exactly the strong-rainbow lifting criterion already recorded in ea7f4204e4b1 and the lifting fence 3f3913b64464.

The derivations of |U_11|=(11/16-o(1))S and of the weighted degree stability in 420e9aea15cc precede and do not use its final lifting paragraph, so those conclusions survive unchanged.
