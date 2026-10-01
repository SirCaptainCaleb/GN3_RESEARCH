# Two-hole alternate paths have an exact alternating blocker-matching defect identity

## Statement

Let H be a linear 3-uniform hypergraph on 2ell-1 vertices, and let Q be an (ell-2)-edge linear path. Write V(H)\V(Q)={a,b}. For h in {a,b}, let epsilon be 1 if there is an edge {a,b,w} for some w in V(Q), and 0 otherwise. Then epsilon is well-defined and common to both holes.

For each h in {a,b}, every edge through h other than the possible common edge {a,b,w} has its other two vertices in V(Q). These blocker pairs form a matching M_h on V(Q), with
  |M_h|=d_H(h)-epsilon.
Moreover M_a and M_b are edge-disjoint.

Let N=|V(Q)|=2ell-3, let U_h be the number of vertices of V(Q) unmatched by M_h, and let p be the number of path components of M_a union M_b, counting isolated vertices as path components. Then
  U_h = N-2d_H(h)+2epsilon
and
  U_a+U_b=2p.
Equivalently,
  p = N-d_H(a)-d_H(b)+2epsilon
    = 2ell-3-d_H(a)-d_H(b)+2epsilon.

In particular, if delta(H)>=floor(2ell/3)+1, then
  p <= 2ell-5-2floor(2ell/3)+2epsilon
and hence p<=2ell-3-2floor(2ell/3).

## Body

There are exactly two vertices outside Q. Fix a. If an edge f through a had no other vertex on Q, then its two other vertices would both have to lie in {b}, impossible in a 3-uniform edge. Thus every a-edge has at least one additional Q-vertex.

If f has exactly one additional Q-vertex w, its third vertex must be b, so f={a,b,w}. By linearity there is at most one edge containing the pair {a,b}; denote its existence by epsilon=1. The same exceptional edge is the only possible one-contact edge at b.

Every other edge through a therefore has both remaining vertices in V(Q). Distinct a-edges have disjoint blocker pairs, since they already share a and a second common vertex would violate linearity. Hence these pairs form a matching M_a of size d_H(a)-epsilon. Similarly for M_b. The two matchings share no edge uv, because {a,u,v} and {b,u,v} would intersect in the two vertices u,v.

Thus
U_h=N-2|M_h|=N-2d_H(h)+2epsilon.

The union of two edge-disjoint matchings has maximum degree at most two and each component is an alternating path, alternating cycle, or isolated vertex. In every path component, including an isolated vertex, the total number of unmatched incidences with respect to the two matchings is exactly two; in every alternating cycle it is zero. Summing unmatched incidences gives U_a+U_b=2p. Substitution yields the displayed formula for p.

The minimum-degree bound follows by d_H(a),d_H(b)>=delta(H) and epsilon<=1.
