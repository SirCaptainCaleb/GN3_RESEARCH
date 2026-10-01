# Private-vertex slack bounds the number of forest joints

## Statement

In the |D|=k critical-core normal form, let sigma=2k-(m+2c), where m,c are the edge and component counts of the universal path forest F=H-D, and let J be its forest joints. Then (k-1)|J|<=k sigma. In particular, for 0<=sigma<=k-2 one has |J|<=sigma. Hence small private slack forces H-D to be a matching with only O(sigma) joints.

## Body


Assume the extremal threshold-set case |D|=k, and let F=H-D have m edges and c nonempty path components. Let
  r=m+2c
be the number of forest-private vertices and define the private-vertex slack
  sigma=2k-r >=0.
Let J be the set of forest joints, so
  |J|=m-c.

By the color-complete normal form c15cf7354428, for every private vertex x and every d in D there is a unique hyperedge through {x,d}. Thus, fixing d, the degree-k star of d contains every one of the r private vertices exactly once among its non-d slots.

The k hyperedges through d have exactly 2k non-d slots in total. Therefore only
  2k-r=sigma
of those slots remain available for vertices outside the forest-private set; in particular at most sigma d-star incidences can lie at forest joints.

Summing over d in D gives
  I(D,J) <= k sigma,
where I(D,J) counts incidences (d,v) for which d in D, v in J, and some hyperedge contains both.

On the other hand, fix a forest joint v. Since H[X]=F, v lies in exactly two edges avoiding D. Since v notin D, d_H(v)>=k+1. Hence at least
  k-1
additional incident edges meet D. Each such edge contributes at least one D-incidence at v, so
  I(D,{v})>=k-1.

Summing over all forest joints yields
  (k-1)|J| <= k sigma.
Thus
  |J| <= floor(k sigma/(k-1)).

In particular, if 0<=sigma<=k-2, then
  |J|<=sigma,
because k sigma/(k-1)=sigma+sigma/(k-1)<sigma+1.

Since a path forest satisfies |J|=m-c and r=m+2c, we also have
  3c+|J|=2k-sigma.
Thus for small slack the universal forest differs from a matching by at most sigma joint vertices.
