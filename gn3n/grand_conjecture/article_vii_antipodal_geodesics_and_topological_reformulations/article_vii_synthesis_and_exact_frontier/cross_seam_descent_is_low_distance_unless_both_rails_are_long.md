# Cross-seam descent is low-distance unless both rails are long

## Composition

(none yet)

## Development

## Cross-seam descent is low-distance unless both complementary rails are long

Let \(H\) satisfy \(\kappa_2(H)=2\), and let
\[
S\mid P\mid Q
\]
be a saturated maximal-support state as in [[both_hole_seed_maximalization_yields_a_saturated_deletion_critical_complement]], with
\[
P=(p_1,\ldots,p_m),\qquad Q=(q_1,\ldots,q_t),
\qquad m,t\ge3.
\]
Put
\[
G=H-S.
\]
Then \(G-v\) is non-Hamiltonian for every \(v\in V(G)\).

### The complementary two-cover has order at least seven

If \(m=t=3\), then \(|V(G)|=6\) and all six one-vertex deletions of \(G\) are non-Hamiltonian. This contradicts the four-of-six theorem, which guarantees at least four Hamiltonian five-deletions of every six-vertex boundary tournament. Hence
\[
\boxed{m+t\ge7.}
\]
In particular at least one of \(P,Q\) has order at least four.

### Pure cross-seam descent

Suppose the \(P\to Q\) seam is in the pure cross-seam branch of [[every_deletion_critical_complement_corner_forces_a_hamiltonian_four_support]], so
\[
K=\{p_{m-1},p_m,q_1,q_2\}
\]
is Hamiltonian.

Assume \(H-K\) has no spanning two-cover; this is the descent branch of [[maximal_support_seams_reduce_to_reseeding_or_four_vertex_descent]]. The inherited paths give
\[
H-K
=
S\mid
(p_1,\ldots,p_{m-2})
\mid
(q_3,\ldots,q_t).
\]

If \(m=3\), the middle residual path is the singleton \(\{p_1\}\). Deleting \(p_1\) leaves the two Hamiltonian paths
\[
S\mid(q_3,\ldots,q_t).
\]
Since \(H-K\) itself has no two-cover,
\[
\boxed{\kappa_2(H-K)=1.}
\]

If \(m=4\), deleting the two-vertex residual path
\[
\{p_1,p_2\}
\]
leaves
\[
S\mid(q_3,\ldots,q_t),
\]
so
\[
\boxed{\kappa_2(H-K)\le2.}
\]

The same statements hold with \(P,Q\) exchanged and at the opposite oriented seam.

Therefore a pure seam descent can escape the already-developed deletion-distance-one/two machinery only when both complementary paths have order at least five:
\[
\boxed{m,t\ge5.}
\]

This isolates the genuinely new maximal-support descent regime from the short-rail cases. No cyclic rotation, path reversal, minimum-counterexample induction, or finite computation is used.
