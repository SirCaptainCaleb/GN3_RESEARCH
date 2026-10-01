# Special/ascending compatibility improves the universal average endpoint potential floor to density plus one

## Statement

Let H be a finite linear 3-graph on n vertices with m edges, and assume phi(v)>=2 for every vertex. Then
  (1/n)sum_v phi(v) >= m/n + 1.

In particular, if |E(H)|=d|V(H)|, then
  average(phi)>=d+1.

## Body

For each vertex v put
  alpha(v)=(2phi(v)-3)-t_ns(v)>=0,
  beta(v)=(2phi(v)-1)-d_D^-(v)>=0.
By 064168e95fae,
  alpha(v)+beta(v)>=1
for every v. Hence, writing
  A=sum_v alpha(v), B=sum_v beta(v),
we have
  A+B>=n.                                              (1)

By e503661c0fab, if
  average(phi)=m/n+5/6+epsilon,
then
  (1/2)A+B=3epsilon n.                                 (2)

Since A,B>=0,
  (1/2)A+B >= (1/2)(A+B) >= n/2.
Combining with (2) gives
  3epsilon n>=n/2,
so epsilon>=1/6. Therefore
  average(phi)
  >= m/n+5/6+1/6
  = m/n+1.
This proves the claim.