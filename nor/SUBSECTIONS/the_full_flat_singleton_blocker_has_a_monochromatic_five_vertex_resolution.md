# The full flat singleton blocker has a monochromatic five vertex resolution

## Metadata

- ID: the_full_flat_singleton_blocker_has_a_monochromatic_five_vertex_resolution
- Parent Section: directed_nor_union_closed_bridge
- Position: 181
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## The full-flat singleton blocker has a monochromatic five-vertex resolution

Work in the coboundary-flat pure-orientation ternary sector. Let five consecutive coordinates
[
0,1,2,3,4
]
carry a singleton threshold-defect pattern
[
alpha(0,1,2)=0,qquad
alpha(1,2,3)=1,qquad
alpha(2,3,4)=0.
]
Assume the left transition tetrahedron
[
Q_L={0,1,2,3}
]
is fully curved, while the right transition tetrahedron
[
Q_R={1,2,3,4}
]
is flat. This is exactly the unique curvature type which blocks the rightward elementary transport of subsection 177.

Full curvature of (Q_L) gives
[
alpha(0,1,3)=1,qquad
alpha(0,2,3)=0.
]
Flatness of (Q_R) gives
[
alpha(1,2,4)=1,qquad
alpha(1,3,4)=0.
]

Put
[
t=alpha(0,1,4).
]
The tetrahedral coboundary identities on the remaining four-subsets force
[
alpha(0,2,4)=alpha(0,3,4)=1-t.
]

### Proposition

The five-set always has a monochromatic Hamilton order.

If (t=0), use
[
(1,0,2,4,3).
]
Its statuses are
[
alpha(1,0,2)=1,qquad
alpha(0,2,4)=1,qquad
alpha(2,4,3)=1.
]

If (t=1), use
[
(1,0,3,4,2).
]
Its statuses are
[
alpha(1,0,3)=0,qquad
alpha(0,3,4)=0,qquad
alpha(3,4,2)=0.
]

Hence the unique elementary right-transport blocker is not an intrinsically irreducible five-coordinate obstruction.

### Boundary observation

In the (t=0) branch, the monochromatic order
[
(1,0,2,4,3)
]
starts with the reversed original left boundary pair ((1,0)) and ends with the reversed original right boundary pair ((4,3)). Therefore if both exterior windows originally have color (0), reversing both boundary pairs flips both immediate reconnection colors to (1), matching the internal monochromatic block. This branch admits a two-sided compatible local color flip.

The (t=1) branch is internally monochromatic but changes the right boundary pair set, so its global use still requires one-sided reconnection analysis.

This complements subsection 177: every singleton defect either transports one rank by an adjacent swap, or lies in a full-flat packet which itself has an explicit monochromatic five-set resolution.

## Frontier

- Development version when composed: None
- Development version now: 1
