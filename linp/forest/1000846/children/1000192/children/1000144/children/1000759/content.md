# Ramani (2026): four-edge paths via incidence rank

## Statement

For every r>=2, every n-vertex linear r-uniform P_4^r-free hypergraph has at most (r+1)n/r edges, with equality precisely for vertex-disjoint unions of Steiner systems S(2,r,r^2).

## Body

Paper: Mahesh Ramani, 'Linear Turán Numbers of Four-Edge Uniform Paths via Incidence Rank', arXiv:2609.20173, updated 2026-09-18. The key theorem is the rank inequality (r+1) rank_R N(H) >= r|E(H)| for a linear r-uniform hypergraph whose line graph is a cograph; equality holds exactly when every edge-containing component is S(2,r,r^2). Since rank_R N(H)<=|V(H)| and P4-freeness is equivalent to the line graph being P4-free/cograph, this yields the sharp Turán bound. For r=3 it recovers 4n/3 and subsumes the P4-specific section in linear_paths.tex.