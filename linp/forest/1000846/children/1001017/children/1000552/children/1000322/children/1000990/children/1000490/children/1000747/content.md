# Balanced equality orientation is an almost-regular self-colored matching graph

## Statement

The balanced d-outregular orientation of an exact equality obstruction induces a simple properly edge-colored graph G on the same vertex set: every color x is a d-edge matching avoiding vertex x, every color occurs exactly d times, and d_G(v)=d_H(v)-d=2d-k_v. Every strong-rainbow graph path lifts to a linear hypergraph path. Hence the equality target k_v>=2d is exactly an isolated vertex in G; in the stalled branch G has average degree 2d and minimum degree at least 2d-kappa-3.

## Body

Let H be an exact minimal equality obstruction equipped with the balanced incidence orientation from 6c52dba65423. Thus every hyperedge has a unique chosen source and every vertex is source of exactly d hyperedges.

Construct a graph G on V(H). For every oriented hyperedge
  e={x,y,z}
with source x, add the graph edge yz and color it by x.

Then:

(1) G is simple and properly edge-colored.
Simplicity follows from linearity: the same pair yz cannot occur in two hyperedges. For a fixed color x, two x-colored edges sharing y would come from two hyperedges sharing the pair {x,y}, impossible. Hence each color class is a matching.

(2) Every color class has exactly d edges, because every vertex x is the chosen source of exactly d hyperedges.

(3) Color x is never incident with graph vertex x, since an x-colored edge consists of the other two vertices of a triple sourced at x.

(4) For every vertex v,
  d_G(v)=d_H(v)-d.
Indeed the hyperedges through v split into the d hyperedges sourced at v, which produce graph edges not incident with v, and the remaining d_H(v)-d hyperedges sourced at one of their other vertices, each producing one graph edge incident with v.

In equality charge coordinates d_H(v)=3d-k_v,
  d_G(v)=2d-k_v.                                    (1)

Thus the equality target k_v>=2d is exactly the existence of an isolated vertex in G. A counterexample to E_ell corresponds to d_G(v)>=1 for every vertex.

(5) Strong-rainbow paths in G lift exactly to linear hypergraph paths. Let
  v_0v_1...v_t
be a graph path with pairwise distinct edge colors c_1,...,c_t such that no color c_i lies among the graph-path vertices v_0,...,v_t. The corresponding hyperedges
  {c_i,v_{i-1},v_i}
form a linear t-edge hypergraph path: consecutive edges meet at v_i, nonconsecutive graph edges have disjoint graph vertices, distinct colors prevent color-color collisions, and strong-rainbow disjointness prevents color-vertex collisions. Only this forward lifting implication is used here.

In the stalled branch max k<=kappa+3,
  delta(G)>=2d-kappa-3.
Since G has dn edges, its average degree is exactly 2d. Therefore the stalled equality obstruction yields an almost-2d-regular properly colored graph in which every one of the n colors is a d-edge matching avoiding its namesake vertex, but which has no strong-rainbow P_ell.
