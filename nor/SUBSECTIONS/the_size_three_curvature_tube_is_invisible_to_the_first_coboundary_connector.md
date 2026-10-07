# The size-three curvature tube is invisible to the first coboundary connector

## Metadata

- ID: the_size_three_curvature_tube_is_invisible_to_the_first_coboundary_connector
- Parent Section: directed_nor_union_closed_bridge
- Position: 88
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development


## The size-three curvature tube is invisible to the first coboundary connector

Combine the pure-orientation three-circuit propagation theorem with the tetrahedral curvature decomposition.

Let U={a,b,c} be the entire omitted set of a maximal sigma-monochromatic path

P=(f_1,...,f_m),

and suppose U is a tau-front circuit at (f_1,f_2).

Counterexamplehood forces the same directed pair cycle on U to persist at every pivot f_j and forces every singleton relation

alpha(u,f_j,f_{j+1})=tau.

Hence for each j:

1. the tetrahedron U union {f_j} is fully curved;
2. for each cycle edge xy of U, the cross tetrahedron {x,y,f_j,f_{j+1}} is flat, because the edge does not flip between pivots.

Therefore every local five-set

U union {f_j,f_{j+1}}

has exactly two fully-curved tetrahedral facets,

U union {f_j},
U union {f_{j+1}},

and its three cross facets are flat.

In particular the coboundary bit delta f vanishes on all five tetrahedral facets of this transport packet.

### Consequence

The first curvature connector -- the Poincare-dual support of the singly-curved tetrahedra delta f=1 -- sees nothing on the persistent size-three tube.

Thus a Connector/Sperner proof based only on the support of delta f can eliminate partial transport but cannot eliminate the zero-flip circuit branch.

The hard branch has passed into the coboundary-flat / edge-potential layer. There the relevant data are the fully-curved universal switch gadgets themselves, equivalently directed-cycle structure in the representing tournament when an edge potential exists.

This gives a two-stage topology program:

1. use the coboundary connector to rule out or route around singly-curved transport;
2. on any surviving delta f=0 carrier, switch to tournament structure, homogeneous cuts, interleavings, or another connector invariant sensitive to full curvature.

Trying to force the first connector through the persistent circuit tube is structurally impossible because its defining cochain is identically zero there.


## Frontier

- Development version when composed: None
- Development version now: 1
