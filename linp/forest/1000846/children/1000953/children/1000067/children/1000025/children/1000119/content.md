# STS doubling cannot beat the one-third leading coefficient

## Statement

Let D be any Steiner triple system obtained by doubling an STS on u vertices with an arbitrary one-factorization of K_{u+1}. For all sufficiently large u, D contains a linear path with at least u-1 edges using only mixed blocks. Consequently, if ell(D) is one plus the maximum linear-path length of D, then |E(D)|/(|V(D)| ell(D))<=1/3. Thus no asymptotic family of ordinary doubled STSs can improve the leading 1/3 lower-bound coefficient.

## Body

Write W for the u+1 new vertices and color each edge pq of K_W by the old vertex x whose one-factor F_x contains pq. A rainbow graph path p_0...p_r lifts to the mixed hyperedge path {x_i,p_{i-1},p_i}: consecutive triples meet at p_i, nonconsecutive graph edges are vertex-disjoint, and rainbow colors ensure that nonconsecutive triples do not meet in U. Bowtell, Montgomery, Müyesser and Pokrovskiy (arXiv:2608.06369, 2026) prove that every sufficiently large properly edge-coloured K_N contains a rainbow path on N-1 vertices, hence N-2 edges. Taking N=u+1 gives a mixed-only linear path of length u-1 in D. Since |V(D)|=2u+1 and |E(D)|=(2u+1)(2u)/6, the first forbidden path length ell(D) is at least u, so |E(D)|/(|V(D)| ell(D))=u/(3 ell(D))<=1/3. The recursive/base STS structure is irrelevant to this obstruction.
