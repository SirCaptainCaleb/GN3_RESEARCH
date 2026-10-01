# Small-core or cheap-peeling dichotomy

## Statement

Conjecture a structural dichotomy for P_l^(3)-free linear 3-graphs: either there is a vertex of degree at most l-c for some fixed c>3/2, or there is a set S of O(l) vertices meeting a positive fraction of all edges in a way that leaves every component of H-S with bounded edge/vertex ratio strictly below l-3/2. Iterating the low-degree deletion outside the exceptional cores would give a global density bound with an improved leading coefficient.

## Body

Why it might matter globally:
The present benchmark can be viewed as a degeneracy-style density bound. A separator alternative would explain why genuinely high minimum degree cannot persist globally without concentrating around a small core; linearity severely limits how dense edges through such a core can overlap. This could turn local obstruction patterns into a reusable global decomposition theorem rather than ever-finer path-end casework.

Plausible first attack:
Assume minimum degree exceeds l-c and take a longest linear path P. Every external edge must hit P. For each outside vertex, encode the set of path vertices hit by its incident edges. Try to prove that either many edges are forced into one of O(l) path vertices (yielding the core S), or the attachment sets are sufficiently spread that alternating between outside edges and subsegments of P extends P. Quantify the resulting concentration/spread dichotomy.
