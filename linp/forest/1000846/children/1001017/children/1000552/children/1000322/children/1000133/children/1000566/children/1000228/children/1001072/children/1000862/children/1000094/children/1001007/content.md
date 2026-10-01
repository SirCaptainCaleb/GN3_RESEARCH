# One unit of critical-core slack permits at most one forest joint

## Statement

In the |D|=k critical-core normal form, if m+2c=2k-1 then every threshold star is entirely DXX and has exactly one forest-joint endpoint. Hence the total D-to-joint incidence is k. Since every forest joint needs at least k-1 such incidences, there is at most one joint. Therefore H-D is either a matching, or a matching with exactly one two-edge path component.

## Body


Assume |D|=k and one unit of private-vertex slack:
  m+2c=2k-1.
Let F=H-D and let P be the set of forest-private vertices, so |P|=2k-1.

By 1663a127e081, for each d in D the d-colored matching has exactly k edges and uses the entire degree-k star of d. Hence every edge through d is DXX. Since the matching has 2k distinct X-endpoints and must saturate all 2k-1 private vertices, exactly one of its endpoints is a forest joint and all other 2k-1 endpoints are private.

Therefore each d contributes exactly one incidence with the forest-joint set J. Summing over d,
  I(D,J)=k.

Now fix a forest joint v in J. Since v has forest degree two and v notin D, its total degree is at least k+1. All edges outside F meet D, so v is incident with at least
  k-1
DXX edges. By linearity these edges use distinct vertices of D. Thus v contributes at least k-1 incidences to I(D,J).

Consequently
  (k-1)|J| <= k.
For k>=3 this forces
  |J|<=1.

Since a path forest with m edges and c nonempty components has exactly m-c joint vertices,
  m-c<=1.

If m=c, every component is a single edge, and
  3c=m+2c=2k-1.

If m=c+1, exactly one component has length two and all others have length one, and
  3c+1=m+2c=2k-1,
so
  3c=2k-2.

Thus the one-slack branch has only two possible forest shapes: a matching, or a matching with one pair of adjacent forest edges.
