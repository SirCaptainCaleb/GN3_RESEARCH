# Correction: zero-exit bridge requires positional exit-edge alignment

## Metadata

- ID: correction_zero_exit_bridge_requires_positional_exit_edge_alignment
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 166
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Correction to [[failed_rooted_corridor_absorption_supplies_three_zero_exit_carrier_labels]]. The algebraic implication is valid only after positional alignment is established. If the actual protected-carrier exit edge is the ordered edge (x,y), then h(y,x,t_i)=1 implies by boundary antisymmetry that h(t_i,x,y)=0, so each t_i has zero exit. However, [[rooted_corridor_absorption_reduces_to_a_bounded_three_hook_residue]] alone does not prove that an independently arising terminal-pair carrier factor uses (x,y) as its exit edge. Therefore the earlier wording 'automatically supplies three zero-exit carrier labels' is too strong globally. The correct statement is conditional: failed rooted absorption supplies three zero-exit candidates whenever the carrier and corridor interfaces are positionally aligned. Establishing that alignment, or constructing a carrier enlargement with that exit edge, remains a separate obligation. Under alignment the only further local repair condition is the required mutual adjacency to the current cycle vertex and its two neighbors.

## Frontier

- Development version when composed: None
- Development version now: 1
