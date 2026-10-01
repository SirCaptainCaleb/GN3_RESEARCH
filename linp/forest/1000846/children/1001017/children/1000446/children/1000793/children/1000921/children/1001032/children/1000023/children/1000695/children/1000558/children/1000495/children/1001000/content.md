# The (ell-13/6)n upper bound has an additional additive Theta(ell) improvement

## Statement

For every integer ell>=6 and every n-vertex linear 3-uniform P_ell-free hypergraph H,
  |E(H)| <= (ell-13/6)n - c_ell,
where
  c_ell = [2 ceil((ell-1)/2)-5]/6.
Equivalently,
  c_ell=(ell-5)/6 for even ell,
  c_ell=(ell-6)/6 for odd ell.

Thus the new (ell-13/6)n bound admits an additional additive improvement of order ell.

## Body

Set alpha=ell-13/6 and c=c_ell. Suppose for contradiction that a P_ell-free linear triple system H satisfies
  m>alpha n-c,
and choose H with n minimum.

If some vertex had degree at most alpha, deleting it would leave a P_ell-free graph H-v with
  |E(H-v)| >= m-alpha > alpha(n-1)-c,
contradicting minimality. Hence
  delta(H)>alpha.
Because delta(H) is integral and
  alpha=ell-13/6,
we obtain
  delta(H)>=ell-2.

Therefore the certified endpoint-potential floor gives
  phi(v)>=ceil((delta+1)/2)>=ceil((ell-1)/2)>=3
for every v.

Write
  sum_v phi(v)=m+(7/6+eta)n,
so eta>=0 by 7cae1cb001ac.

Let R be the set of non-Type-A vertices.

Case 1: there is no Type-A vertex. Then R=V(H), and the stability bound 92cce33dd917 gives
  n=|R|<=6eta n,
so
  eta n>=n/6.
Since delta(H)>=ell-2 and H is linear, any vertex of degree delta has 2delta distinct neighbors, hence
  n>=2delta+1>=2ell-3.
Thus
  eta n >= (2ell-3)/6 >= c
for ell>=6.

Case 2: Type-A vertices exist. Let p0 be the minimum potential of a Type-A vertex. By a3bf58adee0d,
  eta n >= (2p0-5)/6.
Using the endpoint-potential floor,
  p0>=ceil((delta+1)/2)>=ceil((ell-1)/2),
and therefore
  eta n >= [2ceil((ell-1)/2)-5]/6=c.

So in all cases
  sum_v phi(v)>=m+(7/6)n+c.

But H is P_ell-free, so phi(v)<=ell-1 for every v, hence
  (ell-1)n >= m+(7/6)n+c.
Rearranging,
  m <= (ell-13/6)n-c,
contradiction.
