# Same profile flat returns are either backtracks or a local three cycle — preserved pre-item development

## Development

## Same-profile flat returns are either backtracks or a local three-cycle

Continue the minimum-run coboundary-flat ternary dynamics of §206.

Start from
[
O=(v_1,ldots,v_m)
]
with normalized run profile ((p,q)), omitted coordinate (x), and the forced right replacement at
[
y=v_{p+3}.
]

Let
[
z=v_{p+2}.
]

### Case 1: d=e=3 is an exact backtrack

If the right replacement has (d=3), then the new deletion carrier (O') has switch rank
[
p'=p+3.
]
The replacement inserted (x) exactly in position (p+3), while omitting (y=v_{p+3}).

The forced next move is the left replacement at the new switch coordinate. If (e=3), that left replacement replaces the coordinate occupying position (p'=p+3), namely (x), by the omitted coordinate (y).

Therefore the original deletion order and omitted coordinate are restored exactly:
[
(O,x)longrightarrow(O',y)longrightarrow(O,x).
]

Thus the (d=e=3) same-profile return is a literal two-edge backtrack and contributes no nontrivial recurrence.

### Case 2: d=e=2 is a three-coordinate exchange

If (d=2), the right replacement changes the local order
[
ldots,z,y,ldots
]
to
[
ldots,z,x,ldots
]
and omits (y). The switch rank becomes (p+2).

The forced left replacement at that switch replaces (z) by the omitted coordinate (y). Hence after the two moves the local state is
[
ldots,y,x,ldots
]
with (z) omitted.

Write a state by the ordered pair occupying the two protected positions, followed by the omitted coordinate. Then this two-step move is
[
(z,y; x)longmapsto(y,x; z).
	ag{1}
]

If the same (d=e=2) return occurs again, apply the identical coordinate bookkeeping to the new state:
[
(y,x; z)longmapsto(x,z; y).
	ag{2}
]

A third occurrence gives
[
(x,z; y)longmapsto(z,y; x),
	ag{3}
]
which is the original state.

Thus repeated (d=e=2) returns form the local 3-cycle
[
(z,y; x)
	o
(y,x; z)
	o
(x,z; y)
	o
(z,y; x).
]

### Consequence

Combining with reversal-minimality:

- residual drift ((p,q)	o(p+1,q-1)) is strictly finite;
- (d=e=3) same-profile returns are immediate backtracks;
- the only nontrivial recurrent flat-sector mechanism is the explicit three-coordinate protected exchange cycle above.

Therefore unconditional closure of the coboundary-flat ternary sector is reduced to ruling out this one local 3-cycle, or showing that one of its three states necessarily chooses a different replacement branch and escapes.
