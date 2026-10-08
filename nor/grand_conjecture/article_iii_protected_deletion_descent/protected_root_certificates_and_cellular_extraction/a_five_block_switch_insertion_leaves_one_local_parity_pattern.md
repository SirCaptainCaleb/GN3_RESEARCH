# A five-block switch insertion leaves one local parity pattern

## Composition

(none yet)

## Development

## Exact switch insertion by the five-coordinate connector

Let
[
C_0=(u,x,z,v,w)
]
be the five-coordinate connector from §344 with internal word (000), and let
[
C_1=(w,v,z,x,u)
]
be its reversal with internal word (111).

In the switching-normalized split, every vertex of the opposite shore (B) dominates every vertex of either connector order.

Let
[
P_B=(b_1,ldots,b_r)
]
be a NOR-good order of (B), normalized by
[
c(P_B)=0^p1^q,qquad p,qge1.
]
Choose switching bits making (P_B) a directed Hamiltonian path in an equivalent tournament representative, and put
[
e_i=sigma(b_i)oplussigma(b_{i+1})
=1oplus t(b_i,b_{i+1}).
]

The unique switch of (c(P_B)) is
[
c_p=0,qquad c_{p+1}=1.
]

Insert one connector block in the gap
[
b_{p+1}mid b_{p+2},
]
with the usual clipping in the shortest cases. This removes the two old switch-straddling windows.

### Zero connector

Using (C_0), the complete new local packet is
[
e_p,;0,0,0,0,0,;e_{p+2}.
]

All unchanged windows before the packet are zero and all unchanged windows after it are one. Therefore if
[
e_p=0,
]
the full order has at most one change.

### One connector

Using (C_1), the new local packet is
[
e_p,;1,1,1,1,1,;e_{p+2}.
]

Therefore if
[
e_{p+2}=1,
]
the full order has at most one change.

### Residual state

Hence if neither connector orientation yields a spanning NOR order, necessarily
[
oxed{e_p=1,qquad e_{p+2}=0.}
]

Equivalently,
[
t(b_p,b_{p+1})=0,qquad
t(b_{p+2},b_{p+3})=1.
]

Thus the full shore phase-alignment problem reduces at the switch to one local two-bit state. Any reversible repair of the shore order that changes either of these two bits immediately makes one of the two connector orientations close NOR.

This gives a sharply reduced target for a least-unreachable/component argument: show that the local state ((1,0)) cannot persist throughout the entire repair component of good shore orders.
