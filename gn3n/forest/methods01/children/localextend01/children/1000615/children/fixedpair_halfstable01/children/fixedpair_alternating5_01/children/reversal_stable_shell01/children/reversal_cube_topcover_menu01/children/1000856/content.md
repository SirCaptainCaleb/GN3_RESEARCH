# Every path-cover-two Boolean cube has endpoint, support, order, or almost-total internality

## Statement

Let G be a boundary tournament and let T be a set of r>=2 vertices. Suppose every induced state G-S, for S subseteq T, is non-Hamiltonian with path-cover number two. Then at least one of the following holds for two-covers of G: (1) some two-cover has two distinct labels of T simultaneously as displayed endpoints; (2) two two-covers of G have different unordered support partitions; (3) two Hamilton paths on one common component support of two covers of G exhibit relative-order disagreement; (4) at least r-1 labels of T are internal in every two-cover of G.

## Body

Apply pc2_square_topcover_normal01 to the top state G for every unordered pair {d,e} subseteq T. Its hypotheses hold because G, G-d, G-e, and G-{d,e} are among the assumed Boolean-cube states. If any pair-square yields simultaneous endpoints, support-partition disagreement, or relative-order disagreement, we obtain (1), (2), or (3). Otherwise, for every unordered pair {d,e}, at least one of d,e is internal in every two-cover of G. Let I be the set of labels in T that are internal in every two-cover of G. Then every edge of the complete graph on T meets I, so T-I is an independent set in K_r and therefore has size at most one. Hence |I|>=r-1, giving (4). No minimum-counterexample, reversal, Hamiltonian-support, or fixed value of r is used.