# Index-graph normal form for a saturated boundary fan

## Statement

In the exact saturated-fan setting of 29164b69be06, put t=q-1 and for each i=2,...,t let A_i=g_i\V(g_1∪...∪g_{i-1}); then |A_i|=2 and the A_i partition V(Q)\g_1. Form a loopless multigraph J on indices {2,...,t} by adding, for each double-blocking edge through a, an edge ij when its two blocker vertices lie in A_i and A_j. Then Δ(J)<=2. If S=2, J has q-2 vertices and q-3 edges and therefore exactly one path component, all other components being cycles. If S=3, J has q-2 vertices and q-4 edges and therefore exactly two path components (isolated vertices counted as path components), all other components being cycles.

## Body

Each edge g_i with i>=2 adds exactly two new vertices relative to the preceding prefix, so the sets A_i have size two and partition V(Q)\g_1. A double-blocking edge through a cannot use two vertices from one A_i, since both lie in g_i and then that edge would intersect g_i in two vertices, contradicting linearity. Hence it determines an edge ij with i≠j. Distinct double blockers use disjoint blocker vertices, so each index i is incident in J at most |A_i|=2 times; thus Δ(J)<=2. In the S=2 case the number of indices is q-2 and D=q-3, so |E(J)|=|V(J)|-1. Every finite graph of maximum degree at most two is a disjoint union of paths and cycles. Writing p for the number of path components (isolated vertices included), one has |E(J)|=|V(J)|-p, because each cycle contributes equally many edges and vertices while each path contributes one fewer edge than vertices. Thus p=1. For S=3, D=q-4=|V(J)|-2, so p=2 by the same identity.
