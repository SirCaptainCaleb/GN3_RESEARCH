# The directed prefix prism fails the Hartman invariance test — preserved pre-item development

## Composition

(none yet)

## Development

The literal threshold-prefix automaton is directed and acyclic. If z→z' is a legal extension, the set of boundary targets reachable forward from z' can be a proper subset of the set reachable from z. Consequently adjacent same-polarity states need not have equal reachable-target sets.

Thus a label defined as the least unreachable target is not constant along directed same-color edges. This destroys the key Hartman implication.

The failure is structural rather than cosmetic: Hartman's method requires connected components of a reversible graph or cell complex. Therefore the NOR implementation must forget directed extension as the component relation and instead use audited reversible repair moves—flat repair squares, A2/braid cells, synchronized replacements, and K22 exchange cells.
