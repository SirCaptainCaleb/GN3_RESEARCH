# A blocked center in a four-core extension star forces a complete outer-pair six-shell or positioned disturbance

## Statement

Let H be a boundary tournament, let C be a four-vertex set, let r_0,r_1,...,r_k be distinct vertices outside C with k>=2, and for each i choose a Hamilton path P_i on C union {r_i}. Suppose C union {r_0,r_i} is non-Hamiltonian for every i=1,...,k. Then at least one of the following holds: (1) two chosen paths P_i,P_j have relative-order disagreement on C; (2) H contains a Hamiltonian four-set inside C union {r_0,...,r_k}; (3) for some distinct i,j and c in C, a tight triple on {r_i,c,r_j} reverses a displayed root-core edge of P_i or P_j; (4) for every two distinct leaves r_i,r_j with 1<=i<j<=k, the six-set C union {r_i,r_j} is Hamiltonian.

## Body

Assume none of outcomes (1)-(3) occurs. Fix distinct leaves r_i,r_j. Apply three_fourcore_extensions_sync01 to the three Hamiltonian five-extensions C union {r_0}, C union {r_i}, C union {r_j}, with the already chosen Hamilton paths P_0,P_i,P_j. The order-disagreement, Hamiltonian-four-set, and root-core-reversal outcomes of the synchronizer are excluded by assumption. Hence its Hamiltonian six-set outcome occurs for some pair among {r_0,r_i,r_j}. By hypothesis both center-leaf unions C union {r_0,r_i} and C union {r_0,r_j} are non-Hamiltonian. Therefore the only possible pair is {r_i,r_j}, and C union {r_i,r_j} is Hamiltonian. Since i,j were arbitrary distinct leaves, every leaf pair gives a Hamiltonian six-set.
