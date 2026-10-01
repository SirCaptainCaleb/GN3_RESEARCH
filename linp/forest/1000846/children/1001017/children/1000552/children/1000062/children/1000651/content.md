# General upper bound improved to (ell-11/6)n by terminal-snake localization

## Statement

For every ell>=3, every n-vertex linear 3-uniform hypergraph with no linear path P_ell^(3) has at most (ell-11/6)n edges. Equivalently ex_L(n,P_ell^(3)) <= (ell-11/6)n. This improves the Devine--Milans general bound (ell-3/2)n by n/3.

## Body

Let H be an n-vertex P_ell-free linear 3-graph with m edges. Let b be the number of nonspecial edges and s=m-b the number of special edges.

Every nonspecial edge has exactly two terminal snake vertices. Therefore, if t(v) denotes the number of nonspecial edges for which v is terminal,
  2b = sum_v t(v).
By the nonspecial terminal cumulative bound, and because phi(v)<=ell-1 in a P_ell-free hypergraph,
  t(v) <= 2phi(v)-3 <= 2ell-5
for every vertex with phi(v)>=2, while t(v)=0 for phi(v)<=1. Hence
  2b <= (2ell-5)n,
so
  b <= ((2ell-5)/2)n.

On the other hand, the certified special-edge hinge inequality 699ece64f652 gives
  3m-b <= (2ell-3)n.
Substituting the bound on b,
  3m <= (2ell-3)n + ((2ell-5)/2)n
     = ((6ell-11)/2)n.
Therefore
  m <= ((6ell-11)/6)n
    = (ell-11/6)n.

No computation is used. The gain over the source bound is exactly
  (ell-3/2) - (ell-11/6) = 1/3.
The leading coefficient remains one; the result shows that tracking the last blocker of nonspecial terminal incidences extracts a genuine additional constant-order term from the snake method.
