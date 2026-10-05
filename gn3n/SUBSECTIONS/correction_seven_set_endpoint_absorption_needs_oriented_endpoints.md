# Correction: seven-set endpoint absorption needs oriented endpoints

## Metadata

- ID: correction_seven_set_endpoint_absorption_needs_oriented_endpoints
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 41
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Correction: the seven-set endpoint theorem is unoriented

The preceding addendum [[rooted_corridor_absorption_reduces_to_a_bounded_three_hook_residue]] used more than the cited theorem supplies.

The theorem in [[localextend01]] states that a prescribed vertex (x) occurs as **an endpoint** of the Hamiltonian four-side in a (4|3) cover of a seven-set, with at least three possible path-neighbors. It does not prescribe whether the Hamilton order is
[
(ldots,t,x)
]
or
[
(x,t,ldots).
]

These orientations are not interchangeable: reversing a tight path is not in general tight in the same boundary tournament. Therefore one cannot assume that every available neighbor (t) is a predecessor of (x), and the concatenation test
[
(t,x,y)
]
with a frozen inward corridor (x,y,z,ldots) is not justified for those covers in which (x) is the initial endpoint.

The valid retained conclusion is only:

- there are at least three distinct vertices (t) which can occur adjacent to (x) in some endpoint-rooted Hamiltonian four-side of a (4|3) cover.

To obtain the desired rooted absorption, one needs an **oriented endpoint** strengthening: enough of those covers must place (x) at the terminal end, or there must be a separate argument converting the initial-endpoint cases into a compatible repartition.

Thus the reflected-double branch remains reduced to a bounded rooted interface problem, but not yet to the claimed three wrong-way hooks residue. This is the same orientation subtlety already flagged in [[correction_rooted_four_core_extension_is_not_automatic]].
