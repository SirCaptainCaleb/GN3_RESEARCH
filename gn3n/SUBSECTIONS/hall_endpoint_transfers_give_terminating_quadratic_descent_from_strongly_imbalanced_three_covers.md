# Superseded: Hall descent direction remains open

## Metadata

- ID: hall_endpoint_transfers_give_terminating_quadratic_descent_from_strongly_imbalanced_three_covers
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 227
- Row version: 3
- Development version: 3
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Superseded audit note

The original version claimed that applying the four-path Hall-obstruction theorem to an isolated dominant component automatically transfers an endpoint out of that component, hence decreases the quadratic three-cover potential. That directional inference was not justified by the older Hall theorem.

A first attempted repair, [[isolated_hall_blocks_force_opposite_transfer_polarity_or_strict_potential_descent]] together with [[opposite_hall_polarity_repairs_strong_imbalance_quadratic_descent]], was itself invalidated by [[audit_same_hall_transfer_polarity_is_not_excluded_by_boundary_antisymmetry]]. The invalid step treated cyclic rotation of an ordered triple as preserving its boundary-tournament orientation. It does not. One same-polarity Hall pattern therefore remains possible, and strong imbalance does not yet force an outward transfer.

What remains valid is only the conditional potential calculation: whenever a legal transfer is already known to move one endpoint from a component of order c to a component of order d<=c-2, the quadratic potential decreases by at least two. Do not use this subsection as a theorem asserting existence or direction of such a transfer. The directional Hall residue remains open.
