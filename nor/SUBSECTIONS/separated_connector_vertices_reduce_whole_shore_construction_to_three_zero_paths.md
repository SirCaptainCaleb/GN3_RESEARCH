# Audit correction: separated connector vertices require ordered boundary parity

## Metadata

- ID: separated_connector_vertices_reduce_whole_shore_construction_to_three_zero_paths
- Parent Section: monochromatic_connector_blocks
- Position: 12
- Row version: 2
- Development version: 2
- Composition version: 1
- Composition stale: False

## Composition

The unrestricted three-zero-path gluing claim is withdrawn: ordered boundary parity survives even when the underlying tournament triples are transitive. Independent x,z motion enlarges the state space. The correct interface is explicit three-path port data or the general switchable square-path characterization.

## Development


The previous development claim that every ternary window meeting x or z and two shore vertices is automatically zero was false: alpha is alternating, so the coordinate order still matters even when the underlying tournament triple is transitive.

The valid conclusion is weaker. Allowing x and z to move independently enlarges the connector state space, but a decomposition L,x,M,z,R is monochromatic only after checking the ordered boundary windows explicitly. There is no unconditional three-zero-path cover theorem from transitivity alone.

The correct global abstraction is the switchable directed-square-path characterization of the next subsection: after path-normalizing switching, a monochromatic-zero connector is exactly an order whose distance-one and distance-two edges all point forward, with zero switching parity on the two exposed endpoint edges. This permits independent motion of x and z without discarding the ordered parity constraints.

Accordingly this subsection should be treated only as a correction of the overly rigid adjacent-xz state-space intuition, not as a proved three-path reduction.
