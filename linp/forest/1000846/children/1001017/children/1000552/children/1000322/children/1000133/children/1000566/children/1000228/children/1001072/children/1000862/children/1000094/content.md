# Color-complete critical cores satisfy m plus 2c at most 2k

## Statement

In the extremal |D|=k color-complete path-forest normal form, if H-D has m edges and c nonempty path components, then m+2c<=2k. If m+2c=2k, every edge incident with every d in D is a DXX connector pairing two forest-private vertices. If m+2c=2k-1, every d-edge is again DXX, with exactly one joint endpoint among the k matching edges.

## Body


Assume the color-complete path-forest normal form c15cf7354428. Let F=H[X] have m edges and c nonempty components. As in c45d6694704c, the number of forest-degree-one vertices is
  r=m+2c.

Fix d in D. The d-colored edges on X form a matching that saturates every one of these r private vertices. A matching edge covers at most two private vertices, so the d-colored matching has at least
  ceil(r/2)
edges.

Every d-colored matching edge corresponds to a distinct hyperedge of H containing d. Since d has degree exactly k,
  ceil(r/2) <= k.
Therefore
  r=m+2c <= 2k.

If r=2k, then the matching for every d has exactly k edges and every one of the k hyperedges through d belongs to the DXX color lift and pairs two forest-private vertices. In particular no edge through d contains a second vertex of D, and no d-edge uses a forest joint.

If r=2k-1, then again ceil(r/2)=k, so every edge through d belongs to the DXX color lift. The k matching edges saturate all 2k-1 private vertices and have one remaining X-endpoint; hence exactly one matching edge has a forest-joint endpoint and all others pair private vertices. Again no edge through d contains a second D-vertex.

More generally, if
  sigma=2k-r >=0,
then the number of edges through d not needed merely to saturate the r private vertices is at most floor(sigma/2). Thus small slack forces almost the entire degree-k star of every d into the proper colored DXX lift.
