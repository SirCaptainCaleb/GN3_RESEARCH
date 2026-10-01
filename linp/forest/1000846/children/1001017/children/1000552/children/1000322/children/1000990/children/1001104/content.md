# Exact Turan density has Steiner order at least 6d plus one

## Statement

Every n-vertex linear triple system with |E(H)|=dn satisfies n>=6d+1. Equality n=6d+1 holds iff H is a Steiner triple system. More generally, if n=6d+1+s, then the uncovered-pair leave graph has exactly ns/2 edges and average degree s.

## Body

Let H be an n-vertex linear 3-uniform hypergraph with
  |E(H)|=dn.
Then the average vertex degree is
  (1/n)sum_v d_H(v)=3d.

Linearity gives
  d_H(v)<=floor((n-1)/2)
for every vertex v, because the edges through v use pairwise disjoint pairs from V(H)\{v}. Hence
  3d <= (n-1)/2,
so
  n>=6d+1.                                           (1)

If n=6d+1, then the maximum possible degree is
  (n-1)/2=3d,
which equals the average degree. Therefore every vertex has degree exactly 3d. Each vertex is paired, across its incident triples, with all n-1 other vertices exactly once. Equivalently every unordered pair of vertices belongs to exactly one hyperedge, so H is a Steiner triple system STS(6d+1).

More generally write
  n=6d+1+s,  s>=0.
Define the pair-deficiency at v by
  eps(v)=(n-1)-2d_H(v),
the number of vertices not paired with v in any hyperedge. Then eps(v)>=0 and
  sum_v eps(v)
   = n(n-1)-2sum_v d_H(v)
   = n(n-1)-6dn
   = ns.
Thus the average uncovered-pair degree is exactly s.

Equivalently, the graph U of uncovered pairs on V(H) has
  d_U(v)=eps(v)
and exactly
  |E(U)|=ns/2
edges. The equality-density linear triple system is therefore precisely a partial Steiner triple system whose leave graph has average degree s=n-(6d+1).

At s=0 it is a Steiner triple system; for small s it is globally a low-deficiency perturbation of one.
