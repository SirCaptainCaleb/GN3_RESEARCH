# Every order-eleven omission state forces synchronized endpoint disturbance

## Statement

Let H be a hypothetical order-eleven minimum counterexample and let P|Q|(x) be any exact 5|5|1 state. Put X=P union {x}. For any three good deletion labels D subseteq X with X-d Hamiltonian, the fixed-complement family F_d=(X-d)|Q is support-compatible. Choosing arbitrary exact deletion covers at the two endpoints of a Hamilton order of Q, some d in D is support-incompatible with both endpoint covers. Consequently the certified synchronized-endpoint theorem forces either a direct ordinary path edge between X-d and Q-y in one endpoint cover, or explicit relative-order disagreement. The symmetric conclusion holds after exchanging P and Q.

## Body

# Order-eleven omission states are synchronized endpoint-disturbance states

Let H be a hypothetical minimum counterexample of order eleven and let

P|Q|(x)

be any spanning 5|5|1 state. Put X=V(P) union {x}. Since X is a non-Hamiltonian six-set, four-of-six supplies at least four labels d in X for which X-d is Hamiltonian. Choose any three such labels and call the set D.

For each d in D choose a Hamilton path on X-d and retain the fixed Hamilton path Q. This gives exact deletion covers

F_d=(X-d)|Q.

By the certified support-compatible deletion-clique theorem, these covers are pairwise support-compatible and localize exactly to the decomposition V(H)=X disjoint-union Q, with X non-Hamiltonian and Q Hamiltonian.

Fix a Hamilton order Q=(q_0,...,q_4) and choose arbitrary exact two-covers G_0 of H-q_0 and G_4 of H-q_4. The certified synchronized-family theorem e92b0f47c1a6 says each endpoint cover can be support-compatible with at most one member F_d. Since |D|=3, some single d in D is support-incompatible with both G_0 and G_4.

Apply the certified refinement 5e8a13d9c742 to this localized state F_d. It yields one of two outcomes:

1. one endpoint cover contains an ordinary path edge directly joining a vertex of X-d to a vertex of Q-{q_i}; or
2. the two endpoint probes expose explicit relative-order disagreement, hence the standard reversed-edge / reversing-tight-triple / tight-cycle witness.

Therefore every order-eleven 5|5|1 state is already a synchronized endpoint-disturbance producer. No missing omission edge or extremal singleton-label count is required.

The argument is symmetric after exchanging P and Q: the second non-Hamiltonian six-set Q union {x} supplies an independent fixed-complement family with untouched path P and therefore the same direct-mixed-edge-or-order-disagreement dichotomy.
