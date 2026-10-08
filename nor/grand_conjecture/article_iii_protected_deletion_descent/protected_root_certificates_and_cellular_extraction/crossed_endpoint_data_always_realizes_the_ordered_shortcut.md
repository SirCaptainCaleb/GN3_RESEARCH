# Crossed endpoint data always realizes the ordered shortcut

## Composition

(none yet)

## Development

## Crossed endpoint data always realizes the ordered shortcut

Fix distinct coordinates (x,z) and a good order
[
O=(w_1,ldots,w_m)
]
of (Vsetminus{x,z}).

Assume the basic three-block orders have not already produced a spanning NOR order or the desired transition root (x	o z). The only remaining endpoint data are the two crossed types of §304.

The physical-root convention from §228 is: every genuine transition carrier
[
(a,b,c,d)
]
carries root
[
a	o d
]
independently of whether its local transition is (01) or (10).

### Type II

Here
[
(A,B,C,D;E,F)=(0,1,1,0;0,0),
]
with
[
A=alpha(x,w_1,w_2),quad
B=alpha(z,w_1,w_2),quad
E=alpha(x,z,w_1).
]
Thus
[
R_1:=alpha(x,z,w_1)=0.
]
Tetrahedral parity on ({x,z,w_1,w_2}) gives
[
R_2oplus R_1=Aoplus B=1,
]
so (R_2=1).

The packet
[
(w_1,x,z,w_2)
]
has transition word (0,1). Its two off-faces are
[
alpha(w_1,x,w_2)=1-A=1,qquad
alpha(w_1,z,w_2)=1-B=0.
]
Hence it is fully curved.

Swap both endpoint pairs. The opposite corner
[
(x,w_1,w_2,z)
]
is again a genuine fully-curved transition carrier, and its root is
[
oxed{x	o z}.
]

### Type I

Here
[
(A,B,C,D;E,F)=(1,0,0,1;1,1).
]
At the right end,
[
R_m:=alpha(x,z,w_m)=F=1.
]
Parity on ({x,z,w_{m-1},w_m}) gives
[
R_{m-1}oplus R_m=Coplus D=1,
]
so (R_{m-1}=0).

Therefore
[
(w_{m-1},x,z,w_m)
]
has local word (0,1). Its off-faces are
[
alpha(w_{m-1},x,w_m)=1-C=1,qquad
alpha(w_{m-1},z,w_m)=1-D=0,
]
so it is fully curved.

Double endpoint swapping gives
[
(x,w_{m-1},w_m,z),
]
a fully-curved transition carrier with root
[
oxed{x	o z}.
]

### Theorem

Both crossed endpoint types realize the desired ordered shortcut (x	o z) by an explicit fully-curved four-coordinate carrier.

Thus the crossed endpoint residue is not a terminal shortcut obstruction.

### Consequence

For distinct (x,z), choose a good order of (Vsetminus{x,z}). The complete endpoint case analysis now gives either a spanning NOR-good full order or a genuine transition carrier joining (x,z).

If the directly obtained carrier is oriented (z	o x), reversing that full carrier gives (x	o z).

Hence in a minimum counterexample every ordered pair of distinct coordinates admits an actual fully-curved transition carrier with root (x	o z).

This resolves the certified-shortcut realization problem at the physical-root level.
