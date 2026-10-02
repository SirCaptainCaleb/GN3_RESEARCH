# Ordered-pair extension cuts do not encode vertex-simple path covers

## Statement

Let D(H) be the directed graph whose states are ordered pairs (u,v) of distinct vertices and whose arcs (u,v)->(v,w) correspond to tight triples (u,v,w). Tight vertex-simple paths map to directed paths in D(H), but the converse fails at the level needed for a path-cover min-max theorem: directed walks, and even state-simple directed paths, need not correspond to vertex-simple ground sequences; moreover disjoint state-graph paths need not have disjoint ground-vertex supports. Therefore an ordinary vertex- or edge-cut certificate in D(H) is not a dual certificate for absence of a spanning two-path cover. Any faithful state-space formulation must additionally encode used ground vertices or an equivalent set-packing constraint.

## Body

A tight path (v_0,...,v_k) gives the state sequence
(v_0,v_1),(v_1,v_2),...,(v_{k-1},v_k),
and every transition is an arc of D(H). Thus D(H) correctly records local continuation legality.

The reverse implication loses the global vertex-simplicity condition. A directed walk in D(H) only checks each consecutive tight triple. Nothing in the state (u,v) records vertices used earlier, so a later state may contain a ground vertex already used much earlier. Tight cycles make this especially explicit: traversing the state cycle more than once is a legal directed walk while repeating every ground vertex.

Requiring the state-graph path itself to be simple still does not repair the issue. Reusing a ground vertex with a different neighboring ordered pair does not repeat a state. Likewise two state-disjoint directed paths may contain states involving the same ground vertex, so state-disjointness is weaker than disjointness of the corresponding path supports.

Consequently, Menger-type cuts or max-flow/min-cut duality in the ordered-pair graph separate locally legal state walks, not vertex-simple tight paths or pairs of disjoint tight paths covering V(H). To make the representation faithful one must augment a state by its used ground-vertex set, or impose an equivalent global set-packing constraint. Either repair destroys the proposed small local terminal-pair separator model.

This does not rule out a dual obstruction theorem in another formulation; it rules out the naive ordered-pair extension digraph as a faithful carrier of the desired min-max certificate.