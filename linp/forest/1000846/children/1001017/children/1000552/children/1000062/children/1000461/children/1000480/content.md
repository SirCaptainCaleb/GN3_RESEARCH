# General snake upper bound improved to (ell-2)n

## Statement

For every ell>=4, every n-vertex linear 3-uniform hypergraph with no linear path P_ell^(3) has at most (ell-2)n edges. Thus ex_L(n,P_ell^(3)) <= (ell-2)n. The proof combines the ordinary snake hinge with a second-order terminal blocker count; it improves the Devine--Milans (ell-3/2)n bound by n/2.

## Body

Let H be an n-vertex P_ell-free linear 3-graph, ell>=4, with m edges. Let b be the number of nonspecial edges and s=m-b the number of special edges.

For each vertex v choose a maximum phi(v)-edge path P_v ending at v with last vertex v. Let t(v) count nonspecial edges for which v is terminal, and let D(v) count those terminal incidences e!=h_v whose two off-v vertices both lie on P_v outside its last edge. Put
  D=sum_v D(v).

Every nonspecial edge has exactly two terminal vertices, so
  sum_v t(v)=2b.

We claim
  2b-D <= (2ell-6)n.                                      (1)
Indeed, if phi(v)>=3, the terminal saturation lemma gives
  t(v)-D(v)<=2phi(v)-4<=2ell-6.
If phi(v)=2, then t(v)<=1<=2ell-6 because ell>=4. If phi(v)<=1 then t(v)=0. Summing proves (1).

Now use the chosen maximum endpoint-path double-blocker compensation 3a0d8866aba9. Its double-blocker count B includes every incidence counted by D, so B>=D. Therefore
  2m+s+D <= 2m+s+B <= (2ell-3)n.
Since 2m+s=3m-b,
  3m-b+D <= (2ell-3)n,
or
  3m <= (2ell-3)n + (b-D).                                (2)

From (1) and D>=0,
  2(b-D)=2b-2D <= 2b-D <= (2ell-6)n,
so
  b-D <= (ell-3)n.
Substituting into (2) gives
  3m <= (2ell-3)n + (ell-3)n
      = (3ell-6)n.
Hence
  m <= (ell-2)n.

