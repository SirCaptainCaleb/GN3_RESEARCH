# A pure three circuit forms a full curvature tube with flat cross walls

## Metadata

- ID: a_pure_three_circuit_forms_a_full_curvature_tube_with_flat_cross_walls
- Parent Section: directed_nor_union_closed_bridge
- Position: 89
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

In the pure-orientation whole-front size-three branch, the circuit pair cycle propagates through every vertex of the monochromatic path, including the rear endpoint. Each fiber U union {f_j} is fully curved, while every cross tetrahedron consisting of a circuit edge and an adjacent path edge has all four face colors equal and is flat. The obstruction is therefore a full-fiber tube joined by flat cross walls.

## Development

## A pure three-circuit forms a full-curvature tube with flat cross walls

Continue the pure-orientation whole-front size-three setup. Let
[
P=(f_1,ldots,f_m)
]
be a (sigma)-monochromatic path, let
[
U={a,b,c}
]
be the whole omitted set, and suppose (U) is a (	au)-front circuit, (	au=1-sigma), with fixed directed pair cycle
[
a	o b	o c	o a.
]

The established propagation theorem gives, for every (j<m),
[
alpha(a,b,f_j)
=
alpha(b,c,f_j)
=
alpha(c,a,f_j)
=
	au,
]
and
[
alpha(u,f_j,f_{j+1})=	au
qquad(uin U).
]

### Endpoint extension: the cycle also persists at (f_m)

Take a circuit edge (y	o z), with third vertex (x). Suppose for contradiction that it flips at the final pivot:
[
alpha(y,z,f_m)=sigma.
]
Then reversal gives
[
alpha(z,y,f_m)=	au.
]
The reverse-cyclic ordering ((z,y,x)) of (U) has
[
alpha(z,y,x)=	au.
]

Also the rear singleton blocker is
[
alpha(f_{m-1},f_m,z)=	au,
]
because cyclic invariance turns
[
alpha(z,f_{m-1},f_m)=	au
]
into the same value.

Therefore
[
(f_1,ldots,f_m,z,y,x)
]
has status word
[
sigma^{m-2},	au,	au,	au,
]
with exactly one change. This contradicts counterexamplehood.

Hence no circuit edge flips at (f_m). Thus the same directed pair cycle occurs at every pivot
[
f_1,ldots,f_m.
]

### Corollary 1: every fiber is fully curved

For every (j=1,ldots,m), the tetrahedron
[
Ucup{f_j}
]
has face pattern
[
sigma,	au,sigma,	au
]
in cyclic circuit order, hence is fully curved.

So the whole monochromatic path carries a tube of fully-curved tetrahedral fibers.

### Corollary 2: adjacent cross walls are completely flat

Fix a circuit edge, say (a	o b), and an adjacent path pair (f_j,f_{j+1}). On the cross tetrahedron
[
Q={a,b,f_j,f_{j+1}}
]
the four relevant face colors are
[
alpha(a,b,f_j)=	au,
]
[
alpha(a,b,f_{j+1})=	au,
]
[
alpha(a,f_j,f_{j+1})=	au,
]
[
alpha(b,f_j,f_{j+1})=	au.
]

Thus all four face orientations agree. In particular (Q) is flat, with every pivot link transitive.

The same holds for each of the three circuit edges.

### Five-cell picture

For every (j<m), the five-set
[
Ucup{f_j,f_{j+1}}
]
has:
- the two fully-curved facets (Ucup{f_j}) and (Ucup{f_{j+1}});
- the three cross facets obtained from one circuit edge plus (f_j,f_{j+1}), all completely flat.

Hence a whole-front size-three pure-orientation obstruction is a rigid curvature tube:
[
oxed{	ext{full fiber}};-;oxed{	ext{three flat walls}};-;oxed{	ext{full fiber}}
]
repeated along the entire monochromatic path.

### Closure target

The obstruction is no longer arbitrary local curvature. A closure proof for the size-three branch can focus on this full/flat tube. The natural move is to exploit a flat cross wall to transport or interleave a circuit vertex through the monochromatic path while preserving one-change behavior, and then use the full-fiber predecessor rule at the opposite end.
