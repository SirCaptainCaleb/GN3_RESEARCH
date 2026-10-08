# The directed prefix prism fails the Hartman invariance test

## Metadata

- ID: the_directed_prefix_prism_fails_the_hartman_invariance_test
- Parent Section: hartman_least_unreachable_connectors
- Position: 2
- Row version: 1
- Development version: 1
- Composition version: 2
- Composition stale: False

## Composition

Forward target sets may shrink along directed append edges, so the acyclic prefix prism lacks component-invariant least-unreachable labels. Use a verified reversible connector graph for that mechanism; legal prefix reachability remains a separate exact NOR encoding.

## Development

The literal threshold-prefix automaton is directed and acyclic. If z→z' is a legal extension, the set of boundary targets reachable forward from z' can be a proper subset of the set reachable from z. Consequently adjacent same-polarity states need not have equal reachable-target sets.

Thus a label defined as the least unreachable target is not constant along directed same-color edges. This destroys the key Hartman implication.

The failure is structural rather than cosmetic: Hartman's method requires connected components of a reversible graph or cell complex. Therefore the NOR implementation must forget directed extension as the component relation and instead use audited reversible repair moves—flat repair squares, A2/braid cells, synchronized replacements, and K22 exchange cells.
