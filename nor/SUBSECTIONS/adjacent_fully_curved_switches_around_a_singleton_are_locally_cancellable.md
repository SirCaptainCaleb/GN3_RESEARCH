# Adjacent fully curved switches around a singleton are locally cancellable

## Metadata

- ID: adjacent_fully_curved_switches_around_a_singleton_are_locally_cancellable
- Parent Section: directed_nor_union_closed_bridge
- Position: 124
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Adjacent fully-curved switches around a singleton are locally cancellable

Work in the coboundary-flat pure-orientation sector. Let five consecutive coordinates be
[
v_0,v_1,v_2,v_3,v_4
]
and suppose their three consecutive statuses are
[
0,1,0
]
after globally complementing colors if necessary:
[
alpha(0,1,2)=0,qquad
alpha(1,2,3)=1,qquad
alpha(2,3,4)=0.
]
Assume the two transition tetrahedra
[
Q_0={0,1,2,3},qquad Q_1={1,2,3,4}
]
are both fully curved.

### Face determination

Full curvature of (Q_0) forces
[
alpha(0,1,3)=1,qquad
alpha(0,2,3)=0.
]
Full curvature of (Q_1) forces
[
alpha(1,2,4)=0,qquad
alpha(1,3,4)=1.
]

Because the whole sector is coboundary-flat, the remaining three tetrahedral facets of the five-set are flat. Equivalently the three still-undetermined increasing-order triangle values satisfy
[
alpha(0,1,4)=alpha(0,2,4)=alpha(0,3,4)=:tin{0,1}.
]

Thus the entire relevant five-set geometry has only one remaining bit.

### Proposition: local cancellation

The five vertices admit a monochromatic order.

If (t=0), use
[
(2,0,1,4,3).
]
Its statuses are
[
alpha(2,0,1)=0,qquad
alpha(0,1,4)=0,qquad
alpha(1,4,3)=0,
]
because (alpha(2,0,1)=alpha(0,1,2)=0) by cyclic invariance and
[
alpha(1,4,3)=1-alpha(1,3,4)=0.
]

If (t=1), use
[
(1,0,2,4,3).
]
Its statuses are
[
alpha(1,0,2)=1,qquad
alpha(0,2,4)=1,qquad
alpha(2,4,3)=1,
]
using reversal of (alpha(0,1,2)=0) and (alpha(2,3,4)=0).

Hence in either case the five-set can be reordered with zero internal switches.

### Consequence for the extremal four-change carrier

If the remaining (2|1) corner is also fully curved, then the two adjacent full switches bordering the singleton run form exactly this five-set configuration. Therefore the pair of universal switches is not intrinsically irreducible: their five-coordinate core can be replaced by a monochromatic block.

The unresolved issue is purely reconnection. The displayed monochromatic orders change the ordered boundary pairs of the five-block, so up to four external ternary windows can change when the block is substituted into the full cyclic carrier. A global closure proof for the all-four-curved terminal state now reduces to controlling those reconnection windows, rather than the internal curvature gadget.

## Frontier

- Development version when composed: None
- Development version now: 1
