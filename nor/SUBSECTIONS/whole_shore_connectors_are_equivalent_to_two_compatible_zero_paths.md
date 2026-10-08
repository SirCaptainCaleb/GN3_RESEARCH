# Whole-shore connectors are equivalent to two compatible zero paths

## Metadata

- ID: whole_shore_connectors_are_equivalent_to_two_compatible_zero_paths
- Parent Section: monochromatic_connector_blocks
- Position: 9
- Row version: 1
- Development version: 1
- Composition version: 2
- Composition stale: False

## Composition

In the adjacent ordered-xz subfamily, a whole-shore compatible connector is equivalent to two disjoint nonempty zero paths with forward exposed pairs. Their unconditional gluing is P,x,z,Q. This bypasses separated-position cross-edge residues once all four ports are repaired.

## Development

Call an order P of shore vertices a compatible zero path when all consecutive ternary windows of P have color zero and its first and last ordered pairs are forward whenever those pairs exist. If A is partitioned into two nonempty compatible zero paths P and Q, then P,x,z,Q is a monochromatic zero connector with forward endpoint pairs. Conversely, any compatible monochromatic zero connector with x,z consecutive can be written P,x,z,Q, and its boundary windows force P and Q to have the same compatible zero-path property. Hence spanning connector construction is equivalent to covering A by two compatible zero paths. The transitive two-block construction is the special case in which both zero paths are transitive tournament orders.
