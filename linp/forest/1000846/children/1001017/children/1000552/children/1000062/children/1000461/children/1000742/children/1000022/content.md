# Near the seven-sixths floor, full-rank nonspecial terminal vertices have density at most three eta

## Statement

Let H be a finite linear 3-graph with phi(v)>=3 for every vertex and write
  sum_v phi(v)=m+(7/6+eta)n,
with eta>=0.

Let F be the set of vertices v for which there exists a nonspecial edge h terminal at v with
  phi(h)=phi(v).
Then
  |F|<=3 eta n.

Equivalently, outside at most 3 eta n vertices, every nonspecial terminal edge e at v satisfies
  phi(e)<=phi(v)-1.

## Body

For a vertex v put p=phi(v) and
  a(v)=(2p-3)-t_ns(v),
  b(v)=(2p-1)-d_D^-(v).
The exact global slack identity gives
  sum_v[(1/2)a(v)+b(v)]=n+3eta n.

By the weighted local defect theorem 9fe13355ecae and Type-B exclusion 45050da20aaa, every vertex has local weight at least one.

Now fix v∈F and choose a nonspecial edge h of rank p terminal at v. The incident low-rank capacity theorem a570ca900001, applied with q=p, gives
  d_D^-(v)<=2p-3,
because every snake-incoming edge at v has rank at most p and hence lies in J_p(v).
Therefore
  b(v)=(2p-1)-d_D^-(v)>=2.
Since a(v)>=0,
  (1/2)a(v)+b(v)>=2.

Thus vertices in F contribute at least one extra unit above the universal local baseline one. Consequently
  n+3eta n
  =sum_v[(1/2)a(v)+b(v)]
  >=(n-|F|)*1+|F|*2
  =n+|F|.
Hence |F|<=3eta n.
