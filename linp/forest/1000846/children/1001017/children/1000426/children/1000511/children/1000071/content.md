# Intersection-graph fences force cycle-rich leading-scale constructions

## Statement

For a finite linear 3-graph H, linear hypergraph paths are exactly induced paths in the hyperedge intersection graph I(H), whose edges admit the natural vertex-clique cover in which each vertex of I(H) belongs to three cliques and each graph edge belongs to exactly one.

This representation sharply restricts chord-rich P_ell-free constructions. If E(H)=A∪B with every edge in A intersecting every edge in B, then each side has matching number at most three and vertex-cover number at most nine, so H has a vertex cover of size at most 18. More generally, if I(H) is chordal then |E(H)|<=3|V(H)|/2.

Consequently, if H is P_ell-free with ell>=4 and has n vertices and m edges, then H contains at least (m-3n/2)/ell pairwise edge-disjoint linear cycles whenever this quantity is positive. In particular, m>(1/3+epsilon)ell n forces more than (1/3+epsilon-3/(2ell))n pairwise edge-disjoint linear cycles.

## Body

The certified Pathmaker lemma identifies a linear path in H with an induced graph path in I(H). For a linear 3-graph, the hyperedges through each hypergraph vertex form a clique of I(H); every intersection-graph vertex lies in exactly three such cliques, while linearity makes every intersection-graph edge belong to exactly one.

First consider a complete cross-intersection E(H)=A∪B. Fix f in B. Four pairwise disjoint edges in A would all have to meet the three vertices of f, impossible, so nu(A)<=3. The union of a maximal matching in A is therefore a vertex cover of A of size at most 9. Symmetrically B has a vertex cover of size at most 9, giving a cover of all H of size at most 18. Thus recursive join/cograph constructions immediately fall into a bounded-transversal regime.

The stronger chordal bound uses a perfect-elimination ordering e_1,...,e_m of I(H). At a simplicial hyperedge e={a,b,c}, partition its remaining neighbors by which vertex of e they meet. Within each class, the two off-e vertices are pairwise disjoint. If one class had size at least three while another were nonempty, an edge in the second class would need its two off-e vertices to meet three disjoint off-e pairs, impossible. Hence at least two of a,b,c have current hypergraph degree at most three. Charge the removed hyperedge to two such vertices. A fixed hypergraph vertex receives at most three charges from the moment it is first charged onward. Thus 2m<=3n and m<=3n/2.

Finally greedily delete induced cycles from I(H) until the remainder is chordal. The deleted cycles are vertex-disjoint in I(H), hence edge-disjoint linear cycles in H. In a P_ell-free H, each chosen induced cycle has length at most ell: an induced cycle of length at least ell+1 would yield an induced path on ell vertices after deleting one cycle vertex, hence a linear P_ell in H. If k cycles are deleted, at most k ell hyperedges are removed and the chordal remainder has at most 3n/2 edges. Therefore
m-k ell <= 3n/2,
so k >= (m-3n/2)/ell.
Substituting m>(1/3+epsilon)ell n gives the displayed leading-scale consequence.

The conclusion is a construction fence: asymptotically dense P_ell-free examples cannot obtain path suppression merely by making I(H) nearly chordal; they must contain substantial induced-cycle structure.
