# High-degree hub / bounded-core dichotomy

## Statement

Prove a structural dichotomy for P_l-free linear triple systems: either a positive fraction of edges lie in stars centered at a small set S of high-degree vertices, in which case remove S and charge star edges sharply using linearity; or the remaining hypergraph has maximum degree O(l) and sufficiently large average degree to force a loose path by an expansion argument. Optimize the threshold defining S so that the two cases meet below the current 43/48 leading coefficient.

## Body

Why it might matter globally:
Current arguments are very local around a longest path. A hub/core decomposition could convert the extremal problem into two simpler global regimes: concentrated incidence, where linearity severely limits overlap among links, and diffuse incidence, where breadth-first expansion should force long paths. The gain would attack the coefficient at its source rather than refine a local defect count.

Plausible first attack:
Let S={v:d(v)>=tau l}. Bound edges meeting S by summing degrees but subtracting the strong overlap restrictions coming from pairwise-linear links. For H-S, root a loose-path BFS from an edge and derive a recurrence for the number of newly exposed vertices when Delta(H-S)<tau l. Determine whether some fixed tau makes both bounds beat 43/48 asymptotically.