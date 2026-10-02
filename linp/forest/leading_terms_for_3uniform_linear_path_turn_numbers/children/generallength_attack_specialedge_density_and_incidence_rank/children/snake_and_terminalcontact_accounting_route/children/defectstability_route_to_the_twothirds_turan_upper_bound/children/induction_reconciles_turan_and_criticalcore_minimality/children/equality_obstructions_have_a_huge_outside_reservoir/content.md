# Exact-density equality obstructions have a huge outside reservoir

## Statement

Let ell>=4 and d=floor(2ell/3). If a linear 3-graph H satisfies |E(H)|=d|V(H)|, then |V(H)|>=6d+1. Consequently any P_ell-free equality-layer graph has at least
6d-2ell+2
vertices outside every linear path of length at most ell-1. Explicitly, this outside-vertex lower bound is 2ell+2 when ell≡0 mod3, 2ell-2 when ell≡1 mod3, and 2ell when ell≡2 mod3.

## Body

The average vertex degree of H is
  (3|E(H)|)/|V(H)| = 3d.
Hence some vertex has degree at least 3d.

In a linear 3-uniform hypergraph on n vertices, every edge through a fixed vertex v uses a disjoint pair of vertices from V(H)\{v}. Therefore
  d_H(v)<=floor((n-1)/2).
Thus
  3d <= (n-1)/2,
so
  n>=6d+1.

A linear path of length q uses exactly 2q+1 vertices. In a P_ell-free graph q<=ell-1, so every such path uses at most 2ell-1 vertices. Therefore the number of vertices outside the path is at least
  (6d+1)-(2ell-1)=6d-2ell+2.

Now substitute d=floor(2ell/3):
- ell=3r: d=2r, so the bound is 12r-6r+2=2ell+2;
- ell=3r+1: d=2r, so the bound is 12r-(6r+2)+2=2ell-2;
- ell=3r+2: d=2r+1, so the bound is 12r+6-(6r+4)+2=2ell.

Thus an exact-density equality obstruction is necessarily very non-spanning: every longest-path witness leaves roughly 2ell vertices outside.