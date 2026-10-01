# The lowest Type-A potential level forces a large exceptional entrance set

## Statement

Assume the near-floor setting of 92cce33dd917. Let R be the non-Type-A vertices. Suppose Type-A vertices exist, let
  p0=min{phi(v): v notin R},
and let
  X={v notin R: phi(v)=p0}.
Then
  |R|>=2p0-5.

Consequently, if
  sum_v phi(v)=m+(7/6+eta)n,
then
  eta n >= (2p0-5)/6.

If in addition H has minimum degree delta, then p0>=ceil((delta+1)/2), so
  eta n >= [2ceil((delta+1)/2)-5]/6.

## Body

Fix v∈X. Since v is Type A,
  t_ns(v)=2p0-5.
Consider any nonspecial edge e for which v is a terminal, and let x be its unique entrance.

If e is ascending, then phi(x)=phi(e)-1. Because v is terminal,
  phi(e)<=phi(v)=p0,
so
  phi(x)<=p0-1.
By definition of p0 no Type-A vertex has potential below p0, hence x∈R.

If e is nonascending, then d059bf8631a0 says a Type-A vertex cannot be the unique entrance of a nonascending nonspecial edge. Hence again x∈R.

Thus every one of the 2p0-5 nonspecial terminal incidences at v is carried by an edge whose unique entrance lies in R.

Count such terminal incidences over v∈X. There are exactly
  (2p0-5)|X|.
For a fixed pair (x,v)∈R×X, at most one hyperedge can have entrance x and contain terminal v: two distinct such edges would share the pair {x,v}, violating linearity. Therefore the number of these incidences is at most |R||X|. Since X is nonempty,
  (2p0-5)|X|<=|R||X|,
so
  |R|>=2p0-5.

By 92cce33dd917, |R|<=6eta n, yielding
  eta n>=(2p0-5)/6.

Finally the certified minimum-degree endpoint-potential floor gives
  p0>=ceil((delta+1)/2),
which yields the last inequality.
