# A size three curvature tube creates crossed endpoint circuits — preserved pre-item development

## Composition

(none yet)

## Development

## A size-three curvature tube creates crossed-endpoint circuits

Continue the pure-orientation whole-front size-three setup. Let
[
P=(f_1,ldots,f_m)
]
be (sigma)-monochromatic, let (U={a,b,c}) be the whole omitted set, and suppose (U) is a (	au)-front circuit at ((f_1,f_2)), (	au=1-sigma), with directed pair cycle
[
a	o b	o c	o a.
]
The curvature-tube theorem gives the same (	au)-pair cycle at every pivot (f_j), and
[
alpha(u,f_j,f_{j+1})=	au
qquad(uin U).
]

### Step 1: front-to-rear long chord

Fix a cyclic ordering ((x,y,z)) of (U), so
[
alpha(x,y,f_1)=alpha(y,z,f_2)=	au.
]
The flat-wall identities give
[
alpha(x,f_1,y)=sigma,qquad
alpha(f_1,y,f_2)=sigma,qquad
alpha(y,f_2,z)=sigma.
]
Therefore the five-vertex prefix
[
(x,f_1,y,f_2,z)
]
is (sigma)-monochromatic.

Consider the spanning order
[
(x,f_1,y,f_2,z,f_m,f_{m-1},ldots,f_3).
]
After the unknown bridge
[
B_z:=alpha(f_2,z,f_m),
]
the next status is
[
alpha(z,f_m,f_{m-1})=sigma
]
because (alpha(z,f_{m-1},f_m)=	au), and all later reversed-path statuses are (	au).

If (B_z=sigma), the whole word is a (sigma)-run followed by a (	au)-run, hence has at most one change. Counterexamplehood therefore forces
[
alpha(f_2,z,f_m)=	au.
]
Swapping the first two arguments gives
[
alpha(z,f_2,f_m)=sigma.
]
Cycling the choice of (z) through (U) yields
[
oxed{alpha(u,f_2,f_m)=sigmaquad(uin U).}
	ag{1}
]

### Step 2: crossed circuit at ((f_2,f_m))

At pivot (f_2), the (	au)-pair cycle on (U) is
[
a	o b	o c	o a.
]
Hence the (sigma)-pair relation is the reverse cycle
[
b	o a,qquad c	o b,qquad a	o c.
]

By (1), every singleton is (sigma)-feasible at tail ((f_2,f_m)). Every reverse-cycle pair is also (sigma)-feasible there: its first window has color (sigma) at pivot (f_2), and its second window is a singleton window from (1).

No ordering of all three vertices is (sigma)-tight. A cyclic ordering of (U) has internal color (sigma), but its final ordered pair is a (	au)-cycle edge at pivot (f_2); a reverse-cyclic ordering already has internal color (	au).

Therefore
[
oxed{U	ext{ is a }sigma	ext{-front circuit at }(f_2,f_m)}
]
with reversed pair cycle.

### Step 3: mirrored crossed circuit

Applying the same argument to the reversed path (P^{m rev}), whose color is (	au), yields
[
alpha(u,f_{m-1},f_1)=	au
qquad(uin U),
]
and hence
[
oxed{U	ext{ is a }	au	ext{-front circuit at }(f_{m-1},f_1)}
]
with the original pair cycle.

### Interpretation

The size-three curvature tube has a crossed-endpoint self-map:
[
(f_1,f_2;	au,	ext{cycle})
longmapsto
(f_2,f_m;sigma,	ext{reverse cycle}),
]
and symmetrically from the rear.

Thus the tube creates new punctured-Boolean three-circuits on nonadjacent terminal pairs. A closure route is to iterate this crossed-endpoint transformation whenever a compatible monochromatic carrier can be supplied, or to combine the two crossed circuits to force incompatible colors on a common terminal pair.
