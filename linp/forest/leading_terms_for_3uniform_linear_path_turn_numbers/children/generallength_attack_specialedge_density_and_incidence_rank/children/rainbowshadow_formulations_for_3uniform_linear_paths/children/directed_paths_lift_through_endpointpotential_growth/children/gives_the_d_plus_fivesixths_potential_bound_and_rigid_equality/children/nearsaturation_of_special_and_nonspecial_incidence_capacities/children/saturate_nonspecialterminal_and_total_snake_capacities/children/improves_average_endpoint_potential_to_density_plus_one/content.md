# Local capacity incompatibility improves average endpoint potential to density plus one

## Statement

Let H be a finite linear 3-graph in which phi(v)>=2 for every vertex, with n vertices and m edges. Then
  (1/n) sum_v phi(v) >= m/n + 1.
Equivalently,
  sum_v phi(v) >= m+n.

More precisely, with
  delta_ns(v)=(2phi(v)-3)-t_ns(v),
  delta_sn(v)=(2phi(v)-1)-d_D^-(v),
one has delta_ns(v),delta_sn(v)>=0 and delta_ns(v)+delta_sn(v)>=1 for every v, while
  (1/2)sum_v delta_ns(v)+sum_v delta_sn(v)
   =3[sum_v phi(v)-m-(5/6)n].
Therefore the right-hand side is at least n/2.

## Body

By the certified nonspecial-terminal capacity and snake-indegree capacity, delta_ns(v),delta_sn(v) are nonnegative for every vertex.

The new local incompatibility lemma 064168e95fae proves that delta_ns(v) and delta_sn(v) cannot both vanish. Since they are integers,
  delta_ns(v)+delta_sn(v)>=1.

For nonnegative integers a,b with a+b>=1,
  (1/2)a+b >= 1/2.
Summing over all vertices gives
  (1/2)Delta_ns+Delta_sn >= n/2.

By the exact global slack identity e503661c0fab,
  (1/2)Delta_ns+Delta_sn
   =3 epsilon n,
where
  (1/n)sum_v phi(v)=m/n+5/6+epsilon.
Hence
  3epsilon n>=n/2,
so epsilon>=1/6. Therefore
  (1/n)sum_v phi(v)>=m/n+1.

Equality holds only if every vertex has (delta_ns(v),delta_sn(v))=(1,0): indeed this is the unique nonnegative integer pair with a+b>=1 and (1/2)a+b=1/2. Thus at equality every vertex saturates total snake indegree,
  d_D^-(v)=2phi(v)-1,
while missing exactly one unit from nonspecial-terminal capacity,
  t_ns(v)=2phi(v)-4.
This equality profile is a new candidate rigid layer.