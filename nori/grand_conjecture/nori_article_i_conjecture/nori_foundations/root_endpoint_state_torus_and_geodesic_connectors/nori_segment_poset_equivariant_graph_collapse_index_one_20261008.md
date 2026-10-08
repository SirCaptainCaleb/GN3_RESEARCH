# All hereditary ordered-segment complexes collapse equivariantly to the directed-edge graph; index one

# Strong topological no-go: all higher ordered-segment reachability simplices homotopically collapse to the directed-edge graph

Let n>=2. Let P_n be the poset of all directed geodesic segments in Q_n ordered by oriented CONTIGUOUS subsegment inclusion, with involution Theta(P)=(bar v_k,...,bar v_0). Let G be ANY Theta-invariant, DOWNWARD-CLOSED subset of P_n containing every rank-0 vertex and every rank-1 directed edge. This includes the full NORI one-switch admissible segment poset G_n(c), because a contiguous subsegment of an admissible ordered-three-face word has at most as many changes.

**Theorem 1 (contractible lower link).** For every admitted directed segment P=(v_0,...,v_k) with k>=2, the order complex of its strict lower interval
L(P)={Q in G: Q<P}
is contractible. Since G is downward closed, this interval contains precisely all proper oriented contiguous subsegments of P.

Proof. Divide the proper intervals into two subposets:
L_left={subsegments of (v_0,...,v_(k-1))};
L_right={subsegments of (v_1,...,v_k)}.
Every proper contiguous interval omits the first or last vertex, so L(P)=L_left union L_right. Each subposet has a maximum element, hence its order complex is a cone. Their intersection consists of subsegments of (v_1,...,v_(k-1)), which has a maximum since k>=2, so its order complex is a cone as well. The geometric realization is a union of two contractible subcomplexes with contractible nonempty intersection, hence contractible. (For k=2 the intersection is the singleton (v_1), so the statement still holds.)

**Theorem 2 (equivariant homotopy reduction to a graph).** The inclusion
|G_(<=1)| -> |G|
is a Theta-equivariant homotopy equivalence, where G_(<=1) contains just the rank-0 and rank-1 segment vertices. More concretely, remove all maximal-rank elements in descending order k=n,n-1,...,2. At the time a rank-k element is removed, all its higher-rank elements have been removed, so its simplicial link is exactly |L(P)|, contractible by Theorem 1. Removing a vertex with contractible link is a homotopy equivalence, since its closed star is a cone attached along a contractible base. Distinct rank-k vertices are incomparable and have no simplex containing both. Theta preserves rank and freely permutes these vertices in pairs. Therefore the contractions can be implemented simultaneously over Theta-paired vertex stars, giving an equivariant homotopy equivalence at each rank. Alternatively, since both spaces are free Z2 CW complexes, the nonequivariant homotopy equivalences at each step imply equivariant homotopy equivalences by the equivariant Whitehead theorem. Iteration proves the claim.

**Theorem 3 (the absolute antipodal index is EXACTLY ONE).** The rank<=1 complex is the connected bipartite graph with one node for each physical vertex x and one node for each ORIENTED physical edge (x,y), with its two incidence edges joining the oriented-edge node to x and y. Every undirected physical cube edge thus produces two parallel subdivided arcs between its endpoints. The graph is connected. Theta acts freely when n>=2, because a directed edge cannot equal its complemented reversal except in Q_1. Its connected double cover of the quotient has nonzero first Stiefel--Whitney class w, so index>=1; since the quotient is a graph, w^2=0 and index<=1. By Theorem 2 the SAME conclusion holds for ALL G:
index_Z2(|G|)=1.

**Major implication.** The previously constructed full-NORI ordered-segment face-carrier map is correct and has exact geodesic extraction, but the absolute Z2 index of its entire admissible path complex is ALWAYS ONE regardless of n or the coloring, even in dimensions where the complex has many high-dimensional flag simplices. No pure absolute Borsuk–Ulam/Tucker dimension argument on this segment-poset order complex can force NORI closure. The obstruction is genuinely homotopical: all higher path vertices are added along contractible links. The previously constructed explicit odd map into S^(n-1) was a weaker upper bound; the present theorem proves the sharp index one. A viable topological proof must preserve extra RELATIVE information (the map to the physical face lattice, rank/terminal strata, reachability target fibers) or work with a different carrier where higher-dimensional cells are not homotopically removable. This does NOT refute the NORI conjecture.

The theorem applies more generally to EVERY hereditary collection of directed geodesic segments containing all length-0/1 segments, independent of any color constraints.
