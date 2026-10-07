# A holonomy flip gives opposite monochromatic six-vertex orders

## Metadata

- ID: a_holonomy_flip_gives_opposite_monochromatic_six_vertex_orders
- Parent Section: ternary_protected_bridges_and_scan_obstructions
- Position: 45
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## A holonomy flip gives opposite monochromatic six-vertex orders

Work in the special perfect-blocker branch of ternary subsection 43. At a holonomy flip write the six protected coordinates as

(a,x,b,c,d,e),

with blocker scan bits
alpha(x,a,b)=alpha(x,b,c)=alpha(x,c,d)=alpha(x,d,e)=1,

old carrier windows
alpha(a,b,c)=alpha(b,c,d)=alpha(c,d,e)=0,

and adjacent double-full holonomies
h_j=1, h_{j+1}=0.

The holonomy identities give
alpha(a,b,d)=alpha(a,c,d)=1,
alpha(b,c,e)=alpha(b,d,e)=0.

### Color-1 order

Consider
(x,a,b,d,c,e).
Its consecutive ternary statuses are

alpha(x,a,b)=1,
alpha(a,b,d)=1,
alpha(b,d,c)=1-alpha(b,c,d)=1,
alpha(d,c,e)=1-alpha(c,d,e)=1.

Hence this six-coordinate order is monochromatic color 1.

### Color-0 order

Consider
(a,d,b,c,e,x).
The first three statuses are

alpha(a,d,b)=1-alpha(a,b,d)=0,
alpha(d,b,c)=alpha(b,c,d)=0
by cyclic invariance,
alpha(b,c,e)=0.

It remains to compute alpha(c,e,x). In the increasing quadruple (x,c,d,e), coboundary flatness gives the four-face parity identity
alpha(x,c,d)+alpha(x,c,e)+alpha(x,d,e)+alpha(c,d,e)=0.
The blocker scan gives alpha(x,c,d)=alpha(x,d,e)=1 and the old carrier gives alpha(c,d,e)=0, so alpha(x,c,e)=0. Cyclic invariance yields alpha(c,e,x)=0.

Therefore
(a,d,b,c,e,x)
is monochromatic color 0.

### Consequence

Every 1-to-0 holonomy interface in the special perfect-blocker tube is a genuine two-color six-vertex switch gadget: the same physical six-set has both a color-1 Hamilton order and a color-0 Hamilton order.

This is stronger than the five-old-coordinate weave of subsection 43 and is independent of the final free old five-set bit alpha(a,b,e).

The two orders export their boundary changes in opposite directions: the color-1 order places x at the left endpoint, while the color-0 order places x at the right endpoint. Thus the remaining task is purely boundary reconnection. One should compare the two exported boundary packets against the surrounding perfect-blocker scan; an obstruction to both reconnections would have to survive two opposite monochromatic interiors rather than an arbitrary full/flat packet.

## Frontier

- Development version when composed: None
- Development version now: 1
