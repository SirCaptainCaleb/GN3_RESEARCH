# Special/nonspecial incidence compatibility gives the d plus five-sixths potential bound and rigid equality

## Statement

Let H be a finite linear 3-graph on n vertices with m edges, and assume phi(v)>=2 for every vertex. Let s be the number of special edges. Then
  m-sum_v phi(v)+(3/2)n <= s
  <= 2sum_v phi(v)-n-2m.

Consequently
  (1/n)sum_v phi(v) >= m/n + 5/6.

In particular, at exact density m=d n,
  average(phi) >= d+5/6.

Moreover, equality average(phi)=m/n+5/6 holds if and only if both displayed special-edge bounds are equalities; in that case
  s=2n/3.
Thus an equality-layer obstruction attaining the minimum possible average endpoint potential has exactly two-thirds as many special edges as vertices and simultaneously saturates both the nonspecial-terminal capacity and the total snake-indegree capacity.

## Body

Every nonspecial edge has exactly two terminal snake incidences, so the total number of nonspecial terminal incidences is 2(m-s). By the certified cumulative nonspecial-terminal bound 0e550ff0eadd and phi(v)>=2,
  2(m-s)
  <= sum_v (2phi(v)-3)
  = 2sum_v phi(v)-3n.
Rearranging gives
  s >= m-sum_v phi(v)+(3/2)n.                         (1)

On the other hand every nonspecial edge contributes two snake incidences and every special edge contributes three. Hence the total snake indegree is 2m+s. By the certified snake indegree bound,
  2m+s
  <= sum_v (2phi(v)-1)
  = 2sum_v phi(v)-n,
so
  s <= 2sum_v phi(v)-n-2m.                            (2)

Compatibility of (1) and (2) requires
  m-S+(3/2)n <= 2S-n-2m,
where S=sum_v phi(v). Therefore
  3S >= 3m+(5/2)n,
or
  S/n >= m/n+5/6.

If equality holds in this final inequality, then the lower and upper bounds (1),(2) coincide. Substituting S=m+(5/6)n into either yields
  s=(2/3)n.
Conversely equality in both (1) and (2) gives equality in the compatibility inequality and hence in the average-potential bound.
