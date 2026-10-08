# Pure triangle orientations reduce to pivot tournament path optimization

## Composition

When the defect field vanishes, fixing a pivot gives a tournament on the remaining vertices. Along a directed Hamilton path in that tournament, the NOR status is determined by whether each consecutive length-two step closes a directed triangle through the pivot in the relevant center tournament. Thus the residual defect-free problem is to choose a pivot and Hamilton path whose triangle-closure indicator word has at most one change.

## Development

## Pure triangle orientations reduce to pivot-tournament path optimization

Suppose the ternary defect field vanishes, so
[
h(a,b,c)=alpha(a,b,c)
]
for an alternating orientation (alpha) of every unordered triangle.

Fix a pivot (o). Define a tournament (G_o) on (Vsetminus{o}) by
[
a	o b
quadLongleftrightarrowquad
alpha(o,a,b)=alpha(a,b,o)=0.
]
Alternation guarantees that exactly one of (a	o b) and (b	o a) holds.

Let
[
u_1	o u_2	ocdots	o u_m
]
be a directed Hamilton path in (G_o). Then the spanning order
[
(o,u_1,ldots,u_m)
]
has first ternary status (0). For each later index (i),
[
alpha(u_i,u_{i+1},o)=0,
qquad
alpha(o,u_{i+1},u_{i+2})=0.
]
Thus in the center tournament at (u_{i+1}) one has
[
u_i	o o	o u_{i+2}.
]
The next status
[
alpha(u_i,u_{i+1},u_{i+2})
]
equals (0) precisely when (u_i	o u_{i+2}) in that center tournament, and equals (1) precisely when
[
u_i	o o	o u_{i+2}	o u_i
]
is a directed triangle.

Therefore the status word of the pivot order is exactly the indicator sequence of these centered triangle closures, preceded by an initial (0).

Consequently the defect-free ternary NOR problem is equivalent to the following pivot-path optimization problem:

> Find a pivot (o) and a directed Hamilton path of (G_o) for which the consecutive centered-triangle-closure indicators have at most one change.

This reformulation isolates the residual global difficulty after the defect-field insertion theorem. The defect field can always be avoided along some Hamilton order; what remains is to optimize a Hamilton path in an ordinary tournament against a second, position-dependent triangle-closure cost.

A monochromatic spanning order corresponds to a Hamilton path with no closure triangles. A one-change NOR order permits those closure triangles to occur in one contiguous phase.

This is also the exact information missing from support-only Sperner selectors: the pivot path records an ordered tail, while the closure indicator records whether the switch has been used.
