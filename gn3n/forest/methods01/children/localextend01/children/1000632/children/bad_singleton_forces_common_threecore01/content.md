# One bad singleton extension forces a common three-core across two exterior pairs

## Statement

Let W be a four-vertex set in a boundary tournament, and let E_1,E_2 be disjoint two-vertex sets disjoint from W. For i=1,2 define A_i={w in W:(W-{w}) union E_i is Hamiltonian}. If W union {e} is non-Hamiltonian for at least one e in E_1 union E_2, then A_1 intersect A_2 is nonempty. Equivalently, some three-set W-{w} extends Hamiltonianly across both exterior pairs.

## Body

By two_endpoint_pairs_threecore_or_split01, either A_1 intersect A_2 is nonempty or A_1 and A_2 are disjoint two-subsets of W. In the latter case c0ec8ff0e968 implies that W union {e} is Hamiltonian for every e in E_1 union E_2, contradicting the hypothesis. Hence A_1 intersect A_2 is nonempty.
