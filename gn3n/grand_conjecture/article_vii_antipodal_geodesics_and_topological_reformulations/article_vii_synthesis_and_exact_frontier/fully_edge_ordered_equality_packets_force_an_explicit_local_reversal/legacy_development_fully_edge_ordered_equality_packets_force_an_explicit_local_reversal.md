# Fully edge-ordered equality packets force an explicit local reversal — preserved pre-item development

## Fully edge-ordered four-of-six equality packets force an explicit local reversal

Let \(U\) be a six-vertex four-of-six equality packet: \(H[U]\) is non-Hamiltonian and exactly four one-vertex deletions are Hamiltonian. Assume moreover that \(H[U]\) is edge-orderable.

By [[four_of_six_equality_endpoints_force_local_order_disagreement]], among the four Hamiltonian five-deletions there are two, say
\[
U-\{a\},\qquad U-\{b\},
\]
with Hamilton tight paths \(P,Q\) whose four common vertices occur in different relative orders.

Apply Section 4 of [[pathcalc01]] to \(P,Q\). Since their relative orders disagree, one of the following must occur on \(U\):

1. an ordered edge of \(Q\) is the reverse of an ordered edge of \(P\);
2. a tight triple reverses an ordered edge of one path at an intersection with the other;
3. there is a vertex-simple tight cycle.

The third alternative is impossible in an edge-orderable boundary tournament. Indeed, a tight cycle
\[
(v_0,v_1,\ldots,v_{m-1},v_0)
\]
would require the ordinary path edges to satisfy
\[
v_0v_1<v_1v_2<\cdots<v_{m-1}v_0<v_0v_1,
\]
contradicting the strict total edge order.

Therefore:

> **Edge-ordered equality reversal theorem.** Every fully edge-orderable four-of-six equality packet contains either a reversed common ordered edge between two Hamiltonian five-deletion paths, or a positioned tight triple reversing an ordered edge of one of those paths.

In particular, after [[two_bad_five_extensions_either_edge_order_the_six_set_or_expose_a_hamiltonian_support]], the two-bad-\(K_5\) frontier has no featureless branch:
- failure of edge-order amalgamation exposes a Hamiltonian support of order \(4,5,\) or \(6\) containing both distinguished exterior labels;
- successful amalgamation forces an explicit reversed-edge or reversing-triple defect inside the same six-set.

Thus every branch of the six-label equality packet now lands in one of the two established Article VII currencies: bounded Hamiltonian support or positioned reversal. The remaining task is no longer to classify the six-set itself, but to prove that these positioned reversals are compatible with the protected carrier handoff or force a spanning two-cover.
