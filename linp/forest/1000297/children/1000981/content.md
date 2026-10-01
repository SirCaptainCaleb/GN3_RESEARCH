# Clique-cover induced-path threshold

## Statement

Pass completely to the edge-intersection graph G of the linear 3-graph, with every adjacency colored by the unique shared hypergraph vertex. Thus E(G) is partitioned into color-cliques, every vertex of G lies in exactly three such cliques, and a linear hypergraph path corresponds to an induced graph path whose consecutive edge-colors are distinct. Conjecture that any such 3-clique-covered graph with average color-clique incidence above 3(l-c) for some absolute c>3/2 contains an induced l-vertex path with distinct consecutive colors. Prove this directly as a graph theorem, bypassing longest-hyperpath charging.

## Body

Why it might matter globally:
A constant improvement in the graph theorem translates directly into a better leading coefficient for ex_L(n,P_l^(3)). The representation isolates the special structure absent from arbitrary induced-path-free graphs: each graph vertex belongs to exactly three intersection cliques, and each graph edge lies in exactly one clique. It may expose global induced-path machinery that the current endpoint-local proof never sees.

Plausible first attack:
Study a longest induced path Q in the clique-covered graph. For each off-path vertex, record the first and last clique of Q it meets. Use inducedness to show that the set of attachment positions is highly clustered; then double-count incidences between off-path vertices and path cliques. Test whether a three-clique membership condition forces a uniform deficit from the naive l-3/2 coefficient.