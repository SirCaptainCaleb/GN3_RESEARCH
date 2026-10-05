# What a topological proof must actually show

## Metadata

- ID: antipodal_reachability_and_topological_frontier_subsection_c
- Parent Section: antipodal_reachability_and_topological_frontier
- Position: 3
- Row version: 4
- Development version: 4
- Composition version: 1
- Composition stale: False

## Composition

The current topology program is therefore not “find any antipodal path.” It is to rule out the antipodally invariant corridor \(N\) in the ranked memory lift arising from a boundary tournament extension.

Three constraints must be preserved simultaneously:

1. **Distinguished poles.** The output must connect the prescribed source and target, not an arbitrary antipodal pair.
2. **Geodesicity.** Rank must increase at every step, equivalently every original coordinate/vertex is used exactly once.
3. **Memory compatibility.** Edge color in the lift represents a triple of successive cube directions, so a theorem on ordinary cube-edge colorings cannot be applied without carrying the two-step state.

The staircase link supplies an antipodal \((n-2)\)-sphere of permutations, while the reachability criterion supplies an antipodal separation \(R\mid N\mid A(R)\). A plausible closure route is to convert this separation into an antipodal labeling or continuous odd map on the link and then show that Tucker/Borsuk-Ulam/Sperner-type parity forces a forbidden self-intersection or a simplex encoding a red-blue geodesic switch.

What remains unproved is precisely that last implication. The corridor formulation is intended to make the needed topological statement sharp enough to attack directly.

## Development

The current topology program is therefore not “find any antipodal path.” It is to rule out the antipodally invariant corridor \(N\) in the ranked memory lift arising from a boundary tournament extension.

Three constraints must be preserved simultaneously:

1. **Distinguished poles.** The output must connect the prescribed source and target, not an arbitrary antipodal pair.
2. **Geodesicity.** Rank must increase at every step, equivalently every original coordinate/vertex is used exactly once.
3. **Memory compatibility.** Edge color in the lift represents a triple of successive cube directions, so a theorem on ordinary cube-edge colorings cannot be applied without carrying the two-step state.

The staircase link supplies an antipodal \((n-2)\)-sphere of permutations, while the reachability criterion supplies an antipodal separation \(R\mid N\mid A(R)\). A plausible closure route is to convert this separation into an antipodal labeling or continuous odd map on the link and then show that Tucker/Borsuk-Ulam/Sperner-type parity forces a forbidden self-intersection or a simplex encoding a red-blue geodesic switch.

What remains unproved is precisely that last implication. The corridor formulation is intended to make the needed topological statement sharp enough to attack directly.
