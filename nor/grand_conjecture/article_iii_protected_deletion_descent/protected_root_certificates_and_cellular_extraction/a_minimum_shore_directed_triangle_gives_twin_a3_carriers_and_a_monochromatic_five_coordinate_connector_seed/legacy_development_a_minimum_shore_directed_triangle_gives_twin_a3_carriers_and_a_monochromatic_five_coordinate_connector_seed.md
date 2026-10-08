# A minimum-shore directed triangle gives twin A3 carriers and a monochromatic five-coordinate connector seed — preserved pre-item development

## Development

## Twin A3 structure over a minimum signature shore

Continue with a minimum shortcut-free split
[
A={a:alpha(x,z,a)=0},
qquad
B={b:alpha(x,z,b)=1}.
]

For any (a,bin A), tetrahedral parity on ({x,z,a,b}) gives
[
alpha(x,a,b)=alpha(z,a,b),
]
because both pair-signature values
[
alpha(x,z,a),alpha(x,z,b)
]
are zero.

Thus (x) and (z) are exact ternary twins on every ordered pair drawn from (A).

### Directed triangle

By §337 the induced tournament on (A) has no source or sink, hence contains a directed triangle. Choose
[
u	o v	o w	o u.
]

In the switching normalization (B	o z	o A	o x), each directed shore edge has
[
alpha(x,u,v)=alpha(z,u,v)=0,
]
and cyclically
[
alpha(x,v,w)=alpha(z,v,w)=0,
qquad
alpha(x,w,u)=alpha(z,w,u)=0.
]

Meanwhile
[
alpha(u,v,w)=1
]
because (u,v,w) form a directed tournament triangle.

Hence the two tetrahedra
[
{x,u,v,w},qquad {z,u,v,w}
]
have identical face-color tables after replacing (xleftrightarrow z). In particular the protected A3 triangle of §342 occurs in two parallel carrier faces with exactly the same local ternary data.

### A monochromatic five-coordinate weave

Consider
[
Pi=(u,x,z,v,w).
]
Its three ternary windows are
[
alpha(u,x,z)=alpha(x,z,u)=0,
]
[
alpha(x,z,v)=0,
]
and
[
alpha(z,v,w)=0.
]
Therefore
[
oxed{w(Pi)=000.}
]

By reversal,
[
(w,v,z,x,u)
]
has word (111).

Thus every minimum unresolved switching split contains a five-coordinate monochromatic order using:

- both connector vertices (x,z);
- three coordinates from the minimum shore;
- a directed triangle of the shore tournament.

### Significance

This seed is stronger than the bare common-A3 positive dependence. It gives an actual local NOR-good carrier containing the missing connector pair (x,z) with no internal reconnection uncertainty.

Embedding this five-block into any ambient full order and applying monochromatic-band combing yields a finite dichotomy:

1. the monochromatic band expands to a spanning monochromatic NOR order; or
2. expansion stops at a fully-curved protected barrier while the five-coordinate seed remains intact on the protected side.

The remaining task is therefore boundary propagation of a **fixed monochromatic connector block**, rather than extraction from an abstract A3 root cycle.

This also gives a natural Hartman state: the repair component of the five-block, with boundary targets recording which exterior coordinates can be absorbed while retaining the (000) connector seed.
