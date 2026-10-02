# Every equality-layer bad witness omits a vertex of degree at least d plus two

## Statement

Let ell>=5 and d=floor(2ell/3). If a linear 3-graph H satisfies |E(H)|=d|V(H)| and P is any q-edge path with q<=ell-1, then not all vertices outside P can have degree d+1. In fact some vertex outside P has degree at least d+2. Thus in an equality-layer obstruction every nonspecial witness omits a genuinely higher-degree vertex, and the all-threshold outside-reservoir branch is impossible.

## Body


Fix ell>=5 and put d=floor(2ell/3). Let H be an n-vertex linear 3-uniform hypergraph with
  |E(H)|=d n.
Let P be any linear path with q<=ell-1 edges, and put
  s=|V(P)|=2q+1.

Assume for contradiction that every vertex outside P has degree at most d+1.

A basic linearity bound gives
  d_H(v)<= (n-1)/2
for every vertex v: the edges through v use pairwise disjoint pairs of vertices from V(H)\{v}.

Therefore
  sum_v d_H(v)
  <= (d+1)(n-s) + s(n-1)/2.                         (1)

But exact density gives
  sum_v d_H(v)=3|E(H)|=3dn.                         (2)

Subtract the right side of (1) from (2):
  3dn - [(d+1)(n-s)+s(n-1)/2]
  = n(2d-1-s/2) + s(d+3/2).                        (3)

For ell>=5 one has
  ell-1 <= 2d-2.
Indeed this is immediate in each residue class modulo three. Hence
  q<=ell-1<=2d-2,
so
  s=2q+1<=4d-3<4d-2.
Thus
  2d-1-s/2>0,
and both terms on the right side of (3) are strictly positive. This contradicts (1),(2).

Consequently every q-edge path P with q<=ell-1 has at least one outside vertex of degree at least d+2.

In particular, in a vertex-minimal equality-layer obstruction to S_ell, every nonspecial witness path has a degree-(d+2)-or-higher vertex outside it. Therefore the exact-threshold outside-reservoir hypothesis of 1409ac78949b/17810cf2d92b never occurs for ell>=5. The matching-saturation branch developed there is a valid conditional structural analysis, but it is not a live equality obstruction.

This shifts the equality problem decisively toward high-degree outside vertices: every bad witness omits at least one vertex with two or more units of degree above the minimum threshold d.
