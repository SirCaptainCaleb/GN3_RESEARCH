# Link-forest compression via the 2-shadow

## Statement

Exploit linearity to encode a 3-uniform linear hypergraph H by its 2-shadow graph G together with the unique hyperedge label on each shadow edge. Seek a theorem of the form: if H contains no loose path of length l, then after deleting o(n) exceptional vertices, G admits an orientation or forest decomposition in which each hyperedge contributes a labeled triangle and every sufficiently long ordinary graph path with pairwise compatible labels lifts to a loose hypergraph path. Prove a density bound on such labeled-triangle systems directly, aiming to force a liftable path at shadow average degree below the current hypergraph threshold.

## Body

Why it might matter globally:
This changes representation completely. The 2-shadow of a linear triple system has edge-disjoint triangles, so graph-path and forest extremal tools may see global density more cleanly than endpoint-rank charging. A lifting theorem with only sublinear label conflicts could improve the leading coefficient uniformly in l.

Plausible first attack:
Fix a longest loose path P and characterize exactly which shadow edges incident to vertices of P are non-liftable extensions because their triangle labels collide with P. Try to prove that along any ordinary shadow path, each previously used hyperedge label blocks only O(1) future steps, yielding a greedy lifting lemma from graph paths whose length is a constant factor larger than l.
