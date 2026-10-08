# Hartman’s least-unreachable labeling principle and the NOR translation

## Metadata

- ID: hartmans_least_unreachable_labeling_principle_and_the_nor_translation
- Parent Section: hartman_least_unreachable_connectors
- Position: 1
- Row version: 1
- Development version: 1
- Composition version: 2
- Composition stale: False

## Composition

Least-unreachable labels are constant on reversible repair components. A Sperner argument can force connector existence once boundary exclusion, component coherence, and simultaneous absorption are proved. These hypotheses encode compatibility before topology; the component and carrier construction remains conditional.

## Development

Hartman's Connector proof suggests labeling a state by the least boundary target that is not reachable inside its own monochromatic component. The decisive feature is component invariance: adjacent states of the same color lie in one monochromatic component and therefore have the same reachable-target set and the same least-unreachable label. A Sperner-complete cell then contradicts the limited number of underlying colors.

For NOR, the natural targets are threshold faces, endpoint/collar classes, or protected-root exits. The conceptual gain is that connectivity is encoded before the topological step: a successful Sperner contradiction yields an actual connected repair component rather than an algebraic relation that must later be glued.

The first candidate state space came from the threshold-prefix reachability formulation. This identified the right boundary data but did not yet supply a reversible component relation. The remainder of Article IV develops the corrected state spaces on which Hartman's component-invariance mechanism can genuinely operate.
