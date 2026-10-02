# The hard four-side endpoint shell always yields a Hamiltonian five-side or order disagreement

## Statement

In the setup of four_side_endpoint_matching_bridge01, the hard non-Hamiltonian six-shell cannot terminate in a fixed-endpoint matching residue. Instead there is a five-set S containing the two long-path endpoints such that either S is Hamiltonian, with non-Hamiltonian path-cover-two complement in H, or S is non-Hamiltonian and Hamilton paths on four distinct one-vertex deletions of S exhibit order disagreement.

## Body

By hard_fourside_endpoint_graph_can_never_be_a_perfect_matching, the endpoint-deletion graph J necessarily contains two adjacent edges. Let W,W' be the corresponding Hamiltonian four-windows. Each contains the fixed endpoint pair {p_1,p_m}, the two windows overlap in three vertices, and each has non-Hamiltonian path-cover-two complement by four_side_endpoint_matching_bridge01. Put S=W union W'. Then |S|=5.

Apply yield_a_hamiltonian_fiveset_or_four_hamiltonian_foursubsets. If S is Hamiltonian, it is proper in a minimum counterexample; H-S cannot be Hamiltonian or H would have a spanning two-cover, while minimality gives pc(H-S)<=2. Hence H-S is non-Hamiltonian with path-cover number exactly two.

Otherwise S is non-Hamiltonian and at least four of its one-vertex deletions are Hamiltonian. Apply astra004fourgooddisagree to S and any Hamilton paths on four such deletions. It yields order disagreement between two of them.

Thus the hard endpoint shell has only the two asserted outputs.