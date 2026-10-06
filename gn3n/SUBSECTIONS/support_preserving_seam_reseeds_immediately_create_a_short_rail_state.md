# Support-preserving seam reseeds immediately create a short-rail state

## Metadata

- ID: support_preserving_seam_reseeds_immediately_create_a_short_rail_state
- Parent Section: article_vii_synthesis_and_exact_frontier
- Position: 116
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Support-preserving seam reseeds immediately create a short-rail state

Let \(H\) be a no-two-cover boundary tournament with
\[
\kappa_2(H)\ge2,
\]
and let
\[
S
\]
be globally maximal among Hamiltonian supports with two-coverable complement.

Suppose a Hamiltonian seam four-support
\[
K\subseteq V(H)-S,\qquad |K|=4,
\]
lies in the reseed branch and, moreover, in the support-preserving alternative of [[seam_reseeding_either_preserves_or_splits_the_maximal_support]]:
\[
H-K=S\mid R
\]
for a Hamiltonian path \(R\).

Since \(S,K,R\) partition \(V(H)\), the same equality can be read as a new displayed complementary two-cover of \(S\):
\[
\boxed{H-S=K\mid R.}
\]

Thus the globally maximal support \(S\) now has a complementary path of order exactly four.

If \(|R|\le2\), the interface is already bounded.

Assume \(|R|\ge3\). Because \(\kappa_2(H)\ge2\), [[deletion_critical_complement_forks_only_require_two_cover_distance_at_least_two]] applies to this new complementary two-cover: every one-vertex deletion of
\[
H-S=K\mid R
\]
is non-Hamiltonian, and the audited second-layer seam forks are available.

Endpoint saturation of \(S\) is independent of which two-cover of \(H-S\) is displayed. Hence the seam four-support theorem applies to the state
\[
S\mid K\mid R.
\]

At either legitimate oriented seam, exactly one of the established bounded outputs occurs:
- a transversal Hamiltonian four-support / local disturbance;
- an admissible bounded seam seed;
- or a pure cross-seam rail four-support.

In the pure cross-seam descent branch, one displayed complementary rail has order
\[
|K|=4.
\]
Therefore [[cross_seam_descent_is_low_distance_unless_both_rails_are_long]] applies immediately: if the descended graph still has no two-cover, its two-cover deletion distance is at most two.

Hence:

> **Short-rail reseed theorem.** A support-preserving seam reseed cannot generate a new unbounded maximal-support residue. Reinterpreting the reseed cover as the complementary two-cover \(K\mid R\) exposes an order-four rail, so one further seam step lands in bounded disturbance/reseeding or deletion distance at most two.

Consequently the only genuinely new reseed branch left by [[seam_reseeding_either_preserves_or_splits_the_maximal_support]] is the support-splitting branch, where every two-cover of \(H-K\) under consideration cuts the displayed Hamilton path \(S\) across at least one edge.
