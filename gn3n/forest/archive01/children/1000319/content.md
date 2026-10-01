# Dual obstruction via path-cut witnesses

## Statement

Seek a min-max theorem for boundary tournaments: either H has a two-path cover, or there exists a finite obstruction certificate assigning to every tight path a small set of forbidden continuation triples so that any attempt to concatenate path pieces crosses one of these witnesses. Conjecture that every minimal such dual certificate induces a cyclic dependency among boundary faces that is impossible in a Strong Level-(1) boundary tournament.

## Body

Why it might matter globally:
This attacks the theorem from the opposite side. Rather than constructing a cover directly, characterize what a genuine obstruction would have to look like and then use the boundary structure to rule it out. A strong dual theorem could bypass the current endpoint-transport bottleneck entirely.

Plausible first attack:
Formalize a path-extension digraph whose states are ordered terminal pairs and whose arcs append one vertex when the corresponding oriented triple is legal. Translate a spanning two-cover into two disjoint state-walks covering all vertices. For a hypothetical minimal failure, derive a smallest vertex/transition separator and prove that minimality forces each separator element to be tight; then inspect whether the resulting alternating dependency of oriented triples violates the boundary condition.
