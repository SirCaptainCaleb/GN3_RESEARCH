# Exact clique-cover reformulation of linear triple systems

## Statement

A graph F is the intersection graph of a linear 3-uniform hypergraph on an indexed ground set X if and only if F admits an indexed family (C_x)_{x∈X} of cliques, allowing empty and singleton cliques, such that every vertex of F belongs to exactly three C_x and every edge of F belongs to exactly one C_x. Under this correspondence, P_ell^(3)-freeness is exactly induced-P_ell-freeness of F.

## Body

Forward direction: for each hypergraph vertex x let C_x be the set of hyperedges containing x. It is a clique in the intersection graph. A graph vertex e belongs to exactly the three cliques indexed by the vertices of e. By linearity, two intersecting hyperedges have a unique common vertex, so every graph edge lies in exactly one C_x. Conversely, given such an indexed clique family, assign to each graph vertex q the triple E_q={x:q∈C_x}. If q and q' are adjacent, the graph edge qq' lies in exactly one C_x, hence E_q and E_q' meet in exactly one point. If q and q' are nonadjacent, they cannot lie together in any clique C_x, hence the triples are disjoint. Thus the resulting 3-graph is linear and has F as its intersection graph. The final assertion follows from the Pathmaker lemma.