# Pure size three front circuits force the same pair cycle at the rear pivot — preserved pre-item development

## Development

## Pure size-three front circuits force the same pair cycle at the rear pivot

Work in the pure alternating sector (h=alpha). Let
[
P=(f_1,ldots,f_m)
]
be a (sigma)-monochromatic path whose whole omitted set is
[
U={a,b,c}.
]
Assume (U) is a (	au)-front circuit at ((f_1,f_2)), where (	au=1-sigma), with (	au)-pair cycle
[
a	o b	o c	o a.
]

For every (xin U), a facet witness for (Usetminus{x}) spliced to (P) gives a one-change deletion order of (Vsetminus{x}). Endpoint blocking at the rear therefore forces
[
alpha(f_{m-1},f_m,x)=	au.
]
By alternation,
[
alpha(x,f_m,f_{m-1})=sigma.
]
Hence every singleton of (U) is (sigma)-feasible at the reversed rear tail
[
(f_m,f_{m-1}).
]

Choose an inclusion-minimal (sigma)-infeasible support (Dsubseteq U) there.

### Lemma: pure alternating fixed-tail circuits cannot have size two

Suppose ({x,y}) were a two-element circuit for color (sigma) at a tail ((r,s)), with both singletons feasible. Then the second window in either pair order has color (sigma). Pair infeasibility would therefore require
[
alpha(x,y,r)
esigma
quad	ext{and}quad
alpha(y,x,r)
esigma.
]
But alternation gives
[
alpha(y,x,r)=1-alpha(x,y,r),
]
so exactly one of these two colors is (sigma), contradiction.

Thus (|D|
e2). Since all singletons are feasible, (|D|ge2), and since (Dsubseteq U), necessarily
[
D=U.
]

Therefore (U) is a (sigma)-front circuit at ((f_m,f_{m-1})).

### Rear cycle orientation

The internal color of the original cyclic ordering
[
(a,b,c)
]
is (sigma), while the reverse cyclic orderings have color (	au).

For a three-element circuit of color (sigma), the cyclic ordering determined by its pair-feasibility cycle has internal color (1-sigma=	au). Hence the rear (sigma)-pair cycle must be the reverse of the original front (	au)-cycle:
[
b	o a,qquad c	o b,qquad a	o c
]
in color (sigma) at pivot (f_m).

Equivalently, by swapping each ordered pair, the original cycle edges satisfy
[
oxed{
alpha(a,b,f_m)
=
alpha(b,c,f_m)
=
alpha(c,a,f_m)
=
	au.
}
]

### Significance

Although pair-cycle propagation through the interior of (P) remains unproved, the same (	au)-cycle is now rigorously pinned at both endpoint pivots (f_1) and (f_m).

Combined with the corrected rotate-or-wrap lemma, the middle of the path becomes an interpolation problem between identical boundary cycles: a change of any circuit edge can occur only together with a forced opposite-color cyclic wrap of the core.
