# Minimum degree gives an additive gap above the seven-sixths potential floor

## Statement

Let H be a finite linear 3-graph on n vertices with m edges and minimum degree delta>=4. Then
  sum_v phi(v)
  >= m + (7/6)n
     + [2ceil((delta+1)/2)-5]/6.

Consequently, if H is P_ell-free, then
  m
  <= (ell-13/6)n
     - [2ceil((delta+1)/2)-5]/6.

## Body

By the minimum-degree endpoint-potential floor 6a4d9b21f0c3,
  phi(v)>=ceil((delta+1)/2)>=3
for every vertex.

Write
  sum_v phi(v)=m+(7/6+eta)n.
By 7cae1cb001ac, eta>=0.

If H has a Type-A vertex, let p0 be the minimum potential of a Type-A vertex. Then a3bf58adee0d gives
  eta n >= (2p0-5)/6
          >= [2ceil((delta+1)/2)-5]/6.

If H has no Type-A vertex, then every vertex has local weighted defect at least 3/2, because Type A is the unique weight-one state by 9fe13355ecae and 45050da20aaa. The exact global slack identity therefore gives
  n+3eta n >= (3/2)n,
so
  eta n>=n/6.

It remains only to observe that
  n >= 2ceil((delta+1)/2)-5.
Indeed linearity gives delta<=(n-1)/2, and the right side is at most delta-3 or delta-4 according to parity, hence is less than n. Therefore the no-Type-A case also implies
  eta n >= [2ceil((delta+1)/2)-5]/6.

This proves the first inequality.

If H is P_ell-free, every endpoint potential is at most ell-1, so
  (ell-1)n >= sum_v phi(v).
Substituting the first inequality and rearranging gives the edge bound.