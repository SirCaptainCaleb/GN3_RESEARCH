# Fixed-endpoint matching shells should force trapped-component escape

## Statement

Let H be a minimum counterexample and let X|P|Q be a spanning three-cover in a trapped pairwise-repartition component, where X is a Hamiltonian four-set and P=(p_1,...,p_m) has m>=7. Suppose X=A disjoint-union B with |A|=|B|=2 and both A union {p_1,p_m} and B union {p_1,p_m} are Hamiltonian, with non-Hamiltonian path-cover-two complements. Then either the trapped component contains a spanning three-cover of strictly smaller quadratic potential than X|P|Q, or H has a spanning two-cover.

## Body

This is the exact residual branch left by four_side_endpoint_matching_bridge01 after the adjacent-edge case is consumed by overlap amplification.

The two Hamiltonian four-sets share the fixed endpoint pair {p_1,p_m}; their remaining two-vertex parts partition X. A direct replacement of X|P by one of these four-sets does not yet give a legal pairwise repartition, because the complementary residue consists of the other two vertices of X together with the inherited interior path (p_2,...,p_{m-1}), whose Hamiltonicity is not currently controlled. Thus the missing step is not existence of another small Hamiltonian support, but proving that this 2+2 fixed-endpoint matching geometry forces an actual two-path repartition of X union P, or forces a sequence of pairwise repartitions inside the same trapped component that lowers Phi.

The checkerboard equality theorem 27a05b61e8c3 does not directly solve this residue: it concerns four cross endpoint pairs of a two-cover complement to a Hamiltonian four-set, whereas here the common pair consists of the two ends of one long path and the matching partitions the original four-side. Fixed-pair amplification also does not directly apply because only the two matched pairs are known Hamiltonian over the fixed endpoint pair, not the complete four-grid.

Hence this statement isolates the first genuinely component-respecting transport problem suggested by the current proof rehearsal.
