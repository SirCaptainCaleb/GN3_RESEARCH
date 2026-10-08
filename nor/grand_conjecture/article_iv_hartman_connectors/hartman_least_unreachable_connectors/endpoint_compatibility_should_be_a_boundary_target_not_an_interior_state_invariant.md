# Endpoint compatibility should be a boundary target, not an interior state invariant

## Composition

A proposed Hartman state space allows all monochromatic orders containing x,z and treats compatible endpoint pairs as boundary targets. Endpoint deletion preserves monochromaticity, and its reverse is legal when the new boundary window has the required color. This enlarges the repair graph but requires a theorem ensuring a spanning reachable state hits both compatible targets.

## Development

For the Hartman repair complex, enlarge the state space from compatible connectors to monochromatic connector orders containing x,z, without requiring the two exposed endpoint pairs to be compatible at every intermediate state. Compatibility is needed only for the final spanning connector used by the homogeneous-cut closure theorem. This relaxation creates canonical reversible boundary moves: deleting a shore coordinate from the left or right endpoint of a monochromatic order removes ternary windows and creates none, so monochromaticity is automatically preserved. Reversing such a deletion is an endpoint absorption whenever the single new boundary window has the target color. Thus endpoint compatibility naturally belongs among the explicit boundary target classes of the repair complex. The least-unreachable label should record failure to reach a state with the desired compatible left or right port, rather than requiring those ports throughout every repair trajectory.
