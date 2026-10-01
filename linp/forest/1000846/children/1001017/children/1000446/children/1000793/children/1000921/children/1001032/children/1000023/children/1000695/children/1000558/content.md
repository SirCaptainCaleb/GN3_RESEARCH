# Dense equality cores have average endpoint potential at least density plus seven-sixths

## Statement

Let H be a finite linear 3-graph on n vertices with m edges and assume phi(v)>=3 for every vertex. Then
  (1/n)sum_v phi(v) >= m/n + 7/6.

In particular, every exact-density equality-layer candidate with minimum degree high enough to force phi(v)>=3 satisfies
  average(phi)>=d+7/6
when m=d n.

If equality holds, then at every vertex v exactly one of the following local slack patterns occurs:
  Type A: a(v)=2, b(v)=0;
  Type B: a(v)=0, b(v)=1.
Accordingly, Type A vertices lie in exactly four special edges and Type B vertices lie in exactly one special edge.

## Body

Write
  average(phi)=m/n+5/6+epsilon.
By e503661c0fab,
  (1/2)A+B=3epsilon n,
where A=sum_v a(v), B=sum_v b(v).

By 9fe13355ecae, for every vertex with phi(v)>=3,
  (1/2)a(v)+b(v)>=1.
Summing gives
  (1/2)A+B>=n.
Therefore
  3epsilon n>=n,
so epsilon>=1/3. Hence
  average(phi)>=m/n+5/6+1/3=m/n+7/6.

If equality holds, then every local inequality must itself be equality:
  (1/2)a(v)+b(v)=1.
Since a(v),b(v) are nonnegative integers and the patterns (0,0),(1,0) are impossible, the only solutions are
  (a,b)=(2,0) or (0,1).

The number s_v of special incidences at v is
  s_v=d_D^-(v)-t_ns(v)
     =[2phi(v)-1-b(v)]-[2phi(v)-3-a(v)]
     =2+a(v)-b(v).
Thus Type A has s_v=4 and Type B has s_v=1.
