# Three exterior roots force a mixed four-support over every prescribed core pair — preserved pre-item development

## Analytic strengthening: three exterior roots force a mixed Hamiltonian four-support over every prescribed core pair

Let \(C\) be any vertex set with at least two vertices, let
\[
u,v\in C
\]
be any prescribed distinct core labels, and let
\[
x,y,z
\]
be three distinct exterior labels.

Then at least one of
\[
\{u,v,x,y\},\qquad
\{u,v,x,z\},\qquad
\{u,v,y,z\}
\]
is Hamiltonian.

### Proof

Apply the fixed-pair bad-extension theorem to the fixed pair
\[
\{u,v\}
\]
and exterior set
\[
X=\{x,y,z\}.
\]

The graph on \(X\) joining two roots \(r,s\) exactly when
\[
H[\{u,v,r,s\}]
\]
is non-Hamiltonian is bipartite. In particular it is triangle-free.

If all three displayed mixed four-sets were non-Hamiltonian, this bad-pair graph would be the triangle \(K_3\), contradiction. Hence at least one displayed four-set is Hamiltonian. \(\square\)

### Consequences

This strictly strengthens the computational statement
[[pairwise_complete_root_triples_force_a_seven_support_or_mixed_four_support]].

No hypotheses are needed that
\[
C+r
\quad\text{or}\quad
C+r+s
\]
be Hamiltonian, and there is no need to test the full seven-set. For every prescribed pair of core labels, any three exterior roots already force a Hamiltonian mixed four-support.

Therefore the purported quiet common-core states in
[[quiet_six_root_common_cores_force_dense_six_supports_and_order_at_least_seventeen]]
and
[[quiet_six_root_states_grow_to_seven_supports_or_are_exactly_order_seventeen]]
cannot be quiet once three exterior roots are present: a bounded Hamiltonian four-support exists immediately.

In particular the order-seventeen \(K_3\sqcup K_3\) exception and the later seven-support growth alternative are unnecessary for the bounded-disturbance dichotomy. The common-core density hierarchy may still be useful for other purposes, but it is not needed to force a bounded Hamiltonian disturbance.

This proof is purely structural and uses only the fixed-pair orientation-class theorem; it replaces the finite MILP certificate in this application.
