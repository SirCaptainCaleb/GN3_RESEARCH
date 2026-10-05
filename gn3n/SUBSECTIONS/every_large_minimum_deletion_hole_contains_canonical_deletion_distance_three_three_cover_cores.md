# Correction: minimum holes contain canonical exact three-deletion cores

## Metadata

- ID: every_large_minimum_deletion_hole_contains_canonical_deletion_distance_three_three_cover_cores
- Parent Section: article_vii_synthesis_and_exact_frontier
- Position: 16
- Row version: 2
- Development version: 2
- Composition version: None
- Composition stale: False

## Cold composition

(none yet)

## Development

## Correction: every large minimum deletion hole contains canonical exact three-deletion cores

Let
\[
X\subseteq V(H),\qquad |X|=k=\kappa_2(H)\ge3,
\]
be a minimum two-cover deletion set, and let
\[
H-X=P\mid Q
\]
be a displayed two-cover.

Choose any three-element subset
\[
U=\{u,v,w\}\subseteq X
\]
and put
\[
G_U=H-(X-U).
\]

Then
\[
\boxed{\kappa_2(G_U)=3.}
\]

Indeed, deleting the three vertices \(U\) leaves the two-cover \(P\mid Q\), so
\[
\kappa_2(G_U)\le3.
\]
If \(\kappa_2(G_U)\le2\), then deleting \(X-U\) together with at most two further vertices would two-cover \(H\), using at most
\[
(k-3)+2=k-1
\]
deletions, contradicting minimality of \(X\).

Moreover minimum-hole synchronization makes \(u,v,w\) common reversers of the same exposed initial edges of \(P,Q\). Therefore [[three_common_initial_reversers_force_a_root_advancing_five_path]] supplies a **one-step root-advance five-path** inside \(G_U\).

The earlier version of this addendum additionally asserted
\[
\operatorname{pc}(G_U)=3
\]
by invoking [[three_common_reversers_force_a_three_cover_by_finite_root_advance]]. That recursive theorem is not established: its recursion removes corridor vertices without supplying a path-count-preserving lift covering the removed vertices, as recorded in [[root_advance_recursion_drops_three_corridor_vertices_without_a_covering_lift]]. The path-cover conclusion is therefore withdrawn.

### Valid elevation

Every high-deletion-distance minimum hole contains a large family
\[
\{G_U:U\in\binom X3\}
\]
of induced **exact deletion-distance-three cores**, all sharing the same inherited two-cover after deletion of their synchronized triple, and every core carries a bounded root-advance certificate.

Thus arbitrary deletion distance still compresses canonically to the fixed layer
\[
\boxed{\kappa_2=3}
\]
for local analysis; what remains unproved is that these cores themselves have path-cover number three.
