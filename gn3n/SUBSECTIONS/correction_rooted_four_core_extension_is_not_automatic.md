# Correction: rooted four-core extension is not automatic

## Metadata

- ID: correction_rooted_four_core_extension_is_not_automatic
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 33
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Correction to the rooted-four-core reduction

The Hamiltonian (5|4) core lemma in [[order_nine_bridge_reduces_to_rooted_four_core_synchronization]] is valid, but the subsequent claimed automatic rooted extension of the entire four-side (A) by each exterior vertex is **not justified**.

The relevant boundary-tournament axiom identifies only the reversal pair
[
(x,y,z)leftrightarrow(z,y,x).
]
Cyclic rotations are separate ordered triples and cannot be treated as automatically equivalent. Accordingly, the prescribed-endpoint theorem in [[localextend01]] says only that from a tight three-path and two further vertices one obtains a Hamiltonian support of order (4) or (5) containing the prescribed exterior vertex at an endpoint. It does **not** state that, for an arbitrary Hamiltonian four-set (A) and exterior vertex (z), the whole five-set (Acup{z}) is Hamiltonian.

Therefore retain only the audited part:

**Nine-core lemma.** Every nine-vertex boundary tournament has at least (34) complementary Hamiltonian (5|4) partitions.

This remains useful for the adjacent-window problem because it supplies many candidate four-cores and five-cores, but an additional extension/selection argument is required to make the two ten-window repairs compatible.

Any argument treating cyclic rotations of a tight triple as automatically tight is invalid in the present model and must not be used.

## Frontier

- Development version when composed: None
- Development version now: 1
