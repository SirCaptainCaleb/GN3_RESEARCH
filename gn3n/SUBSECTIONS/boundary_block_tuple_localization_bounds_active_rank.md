# Boundary-block tuple localization bounds active rank

## Metadata

- ID: boundary_block_tuple_localization_bounds_active_rank
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 80
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Let F be protected at positive witness depth r, and restrict to chambers whose selected unsigned edge remains e_r. Suppose a boundary face block B meets a depth-r determining window in its final k positions, k<=4, with all other block orders fixed.

Lemma. The signed depth-r label depends on the order of B only through the ordered k-tuple occupying those final k positions.

Reason: the two depth-r positive occurrences are determined by their determining windows; protection excludes strictly inward witnesses; on the fixed-e_r stratum, farther-out witnesses cannot replace e_r. Thus changing B away from those k positions cannot change which depth-r occurrences are present or their intrinsic/tie orientation.

Consequently, among the N-1 adjacent generators of an N-vertex left boundary block, only the k-1 generators internal to the terminal tuple and the one generator crossing into it can change the depth-r label. At most k<=4 generators are active. The symmetric right boundary block contributes at most four more.

Therefore the sign-changing boundary interaction factors through rank at most eight, independent of the total boundary-block orders. Generators deeper in the blocks, and generators in blocks disjoint from both determining windows, are label-neutral and can be collapsed using the inherited-mask frozen-carrier construction.

This does not produce the missing outward repair for a genuine two-deletion reflected double, nor does it solve compatibility between independently normalized ambient faces. It removes the separate concern that arbitrarily large one-sided boundary blocks force unbounded Coxeter coherence once a tuple-level repair is available.

## Frontier

- Development version when composed: None
- Development version now: 1
