# Nonbacktracking incidence expansion

## Statement

Use the bipartite incidence graph B between hypergraph vertices and hyperedges. It is C4-free and every hyperedge-node has degree 3. Seek a pruning lemma giving a subgraph with minimum left-to-right branching whenever m/n exceeds (1-epsilon)l. Then grow nonbacktracking alternating walks from an edge-node. Conjecture that in a C4-free bipartite graph with right degree 3, sufficiently large average branching over l layers forces an alternating path whose right vertices correspond to pairwise nonintersecting nonconsecutive hyperedges, hence a linear P_l.

## Body

Why it might matter globally:
This attacks the leading term through expansion rather than endpoint accounting. Linearity becomes the strong C4-free condition, so collisions in a breadth-first exploration are expensive and potentially quantifiable. Even a weak collision lemma could yield a fixed constant improvement over l-3/2, while a sharper tree-excess argument might approach the longer-term 2l/3-scale target.

Plausible first attack:
Prune to a nonempty incidence subgraph with controlled minimum weighted degree, then expose two or three BFS layers from a hyperedge-node. Classify the first way a nonbacktracking exploration can fail to give an induced hypergraph path: a repeated left vertex or a cross-edge to an earlier right vertex. Use C4-freeness to inject such failures into distinct local incidences and derive a branching-versus-collision inequality.