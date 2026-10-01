# The density-plus-seven-sixths potential bound is never attained in the dense regime

## Statement

Let H be a finite linear 3-graph with phi(v)>=3 for every vertex. Then equality cannot hold in
  average(phi)>=m/n+7/6.

Equivalently,
  sum_v phi(v) > m + (7/6)n.

More structurally, any hypothetical equality configuration would force every nonspecial edge to be ascending and would give the strict-potential auxiliary DAG positive indegree at every vertex, impossible.

## Body

Assume equality:
  S:=sum_v phi(v)=m+(7/6)n.

By 45050da20aaa, every vertex is Type A, so every vertex lies in exactly four special edges. Hence the number s of special edges satisfies
  3s=4n,
thus
  s=(4/3)n.

Let A be the number of ascending nonspecial edges. The certified ascending accounting inequality 419519f0efa5 gives
  3m-A <= 2S-n.
Substituting S=m+7n/6 gives
  3m-A <= 2m+(7/3)n-n
         = 2m+(4/3)n,
so
  A >= m-(4/3)n.

But the total number of nonspecial edges is
  m-s = m-(4/3)n.
Every ascending edge is nonspecial, hence
  A <= m-s = m-(4/3)n.
Therefore equality holds:
  A=m-s,
so every nonspecial edge is ascending.

Now form the auxiliary digraph of b1fffccc673c, orienting each nonspecial edge from its unique entrance to its two terminals. Since every nonspecial edge is ascending, every arc strictly raises phi.

At a vertex v, because every nonspecial edge is ascending, the indegree of this auxiliary digraph is exactly the number t_ns(v) of nonspecial terminal incidences. Type A gives
  t_ns(v)=2phi(v)-5.
Since phi(v)>=3,
  d^-(v)=2phi(v)-5>=1
for every vertex.

However choose a vertex v of minimum endpoint potential. No strict-potential arc can enter v, because every arc x->v satisfies phi(v)>=phi(x)+1. Thus d^-(v)=0, contradiction.

Therefore equality in the density-plus-seven-sixths bound is impossible.