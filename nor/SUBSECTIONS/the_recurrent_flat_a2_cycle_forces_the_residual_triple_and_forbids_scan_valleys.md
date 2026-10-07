# The recurrent flat A2 cycle forces the residual triple and forbids scan valleys

## Metadata

- ID: the_recurrent_flat_a2_cycle_forces_the_residual_triple_and_forbids_scan_valleys
- Parent Section: ternary_protected_bridges_and_scan_obstructions
- Position: 8
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## The recurrent flat A2 cycle forces the residual triple and forbids scan valleys

Work in the recurrent flat A2 replacement cycle with residual coordinates
[
U={x,y,z}
]
and common local deletion carriers
[
ldots,A,B,z,y,C,D,ldots quad(	ext{omit }x),
]
[
ldots,A,B,y,x,C,D,ldots quad(	ext{omit }z),
]
[
ldots,A,B,x,z,C,D,ldots quad(	ext{omit }y),
]
all with the same one-change word (0^p1^q). The known local identities are
[
alpha(A,B,u)=0quad(uin U),
]
[
alpha(B,x,z)=alpha(B,z,y)=alpha(B,y,x)=1,
]
[
alpha(x,z,C)=alpha(z,y,C)=alpha(y,x,C)=1,
]
and the common suffix from (C,D,ldots) is in the color-1 phase.

### The residual triple is forced

[
oxed{alpha(x,y,z)=1.}
]

Indeed consider the deletion carrier omitting (x), and insert (x) between (B) and (z):
[
ldots,A,B,x,z,y,C,D,ldots.
]
The affected statuses are
[
alpha(A,B,x)=0,
]
[
alpha(B,x,z)=1,
]
[
alpha(x,z,y)=1-alpha(x,y,z),
]
[
alpha(z,y,C)=1.
]
If (alpha(x,y,z)=0), then all statuses from (alpha(B,x,z)) onward are (1), while the inherited prefix through (alpha(A,B,x)) is (0). This is a spanning one-change order, contradiction. Hence (alpha(x,y,z)=1).

### A companion weave without its final residual

For each (uin U), choose the corresponding seven-coordinate weave from the A2 theorem and delete its final coordinate (u). The remaining protected front block uses the other two residual coordinates and has status word
[
0,1,1,1,
]
ending in the original ordered suffix pair ((C,D)).

For example, for (u=y) the front block is
[
(A,B,x,z,C,D)
]
with statuses (0,1,1,1). The analogous statement holds cyclically for (u=x,z).

Thus the omitted residual (u) may be inserted at any later gap of the untouched common color-1 suffix while every coordinate outside that insertion packet stays fixed.

Let
[
s_u(j)=alpha(u,t_j,t_{j+1})
]
be its scan along the common suffix (T=(t_1,t_2,ldots)), with (t_1=C,t_2=D).

If (u) is inserted between (t_j) and (t_{j+1}) at an interior gap, the three new statuses are
[
s_u(j-1),qquad 1-s_u(j),qquad s_u(j+1).
]
Therefore a scan valley
[
s_u(j-1)s_u(j)s_u(j+1)=101
]
produces the packet
[
111.
]
The protected front block already has word (0,1,1,1), and the suffix outside the insertion packet is all (1). Hence this would give a spanning one-change order.

### Corollary

For every residual coordinate (uin{x,y,z}), its full suffix scan is (101)-free.

Since every scan starts with value (1) at the front and ends with value (0) at the rear, any surviving scan can change from (0) back to (1) only after at least two consecutive zeros. In particular isolated zero defects in a residual scan are impossible.

This adds a genuine global constraint to the Klein-four holonomy formulation of the A2 recurrence.

## Frontier

- Development version when composed: None
- Development version now: 1
