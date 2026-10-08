# Audit correction: fully ported zero paths still have a cross-endpoint obstruction

## Metadata

- ID: two_fully_ported_zero_paths_give_a_spanning_connector
- Parent Section: monochromatic_connector_blocks
- Position: 27
- Row version: 3
- Development version: 3
- Composition version: 1
- Composition stale: False

## Composition

Two fully ported zero paths always glue through adjacent x,z as P,x,z,Q, and hence close the homogeneous split. Separated candidates use independent cross-edge conditions; their simultaneous failure creates no additional obstruction to the adjacent construction. This elevates the port-repaired cover to direct spanning closure.

## Development

Let P and Q be disjoint nonempty zero paths partitioning A, with both exposed ordered pairs forward whenever they exist. The adjacent-pair order P,x,z,Q is a spanning compatible zero connector by §9: internal windows are inherited, the outer splice windows use the forward path pairs, and the central windows use the zero shore signature. Singleton path clipping preserves both exposed forward pairs. The homogeneous-cut insertion theorem closes the full switching split.

For separated special vertices, z,P,x,Q additionally requires q_1->p_r, and z,Q,x,P requires the independent edge p_1->q_s. Failure of the first does not force the second. This crossed-endpoint residue concerns those separated candidates only; it is bypassed by the already proved adjacent-pair connector. Thus fully ported zero paths give spanning closure without a further cross-edge hypothesis.
