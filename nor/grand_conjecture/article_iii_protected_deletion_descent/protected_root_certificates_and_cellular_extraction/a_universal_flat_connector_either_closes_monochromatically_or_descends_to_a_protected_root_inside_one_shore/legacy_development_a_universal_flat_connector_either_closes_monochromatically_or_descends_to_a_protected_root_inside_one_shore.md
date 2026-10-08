# A universal flat connector either closes monochromatically or descends to a protected root inside one shore — preserved pre-item development

## Development

## Universal flat connectors have a strict shore descent

Work in the coboundary-flat alternating ternary sector. Fix distinct coordinates (x,z) and assume there is no fully-curved transition carrier of the protected root (x	o z).

Let
[
d(u)=alpha(x,z,u)
]
on (Vsetminus{x,z}), and put
[
A={u:d(u)=0},qquad B={u:d(u)=1}.
]
The clone case is already excluded in a minimum counterexample, so both shores are nonempty.

By the universal-connector theorem, for every (ain A,bin B),
[
alpha(x,a,b)=1,qquad alpha(z,a,b)=0.
]

### Tournament normal form

Use the valid tournament representation
[
alpha(a,b,c)=t(a,b)oplus t(b,c)oplus t(c,a),
]
with (t(u,v)=1) meaning (u	o v).

Switch the representative so that (x) is a sink:
[
u	o xqquad	ext{for every }u
e x.
]

Then (z	o x), and
[
d(u)=alpha(x,z,u)=t(z,u)oplus1.
]
Hence
[
z	o A,qquad B	o z.
]

For (ain A,bin B),
[
1=alpha(x,a,b)=t(a,b)oplus1,
]
so
[
b	o a.
]

Therefore the tournament has the exact ordinal-sum structure
[
oxed{T[B] 	o z 	o T[A] 	o x.}
]

### If both shores are transitive, NOR closes

Suppose (T[A]) and (T[B]) are both transitive. List each shore in its dominance order:
[
b_1	ocdots	o b_s,qquad
a_1	ocdots	o a_r.
]

Then
[
(b_1,ldots,b_s,z,a_1,ldots,a_r,x)
]
is a directed transitive Hamiltonian path of the full tournament: every earlier layer dominates every later layer.

Every consecutive triple on a transitive directed path has
[
alpha=1oplus1oplus0=0.
]
Thus the full ternary word is monochromatic zero, giving a spanning NOR order.

Hence in a minimum counterexample at least one shore is nontransitive.

### A nontransitive shore gives a protected root with shore-local provenance

Assume (T[A]) is nontransitive. Every nontransitive tournament contains a directed triangle. Write one as
[
b	o y	o a	o b
]
with (a,b,yin A).

Consider the four-coordinate order
[
(x,a,b,y).
]

Since (x) is a sink,
[
alpha(x,a,b)=t(a,b)oplus1=1oplus1=0.
]
Also
[
alpha(a,b,y)=1
]
because (a	o b	o y	o a) is a directed triangle.

So ((x,a,b,y)) is a (0	o1) transition carrier with physical root
[
x	o y.
]

Its off-faces are
[
alpha(x,a,y)=1,qquad
alpha(x,b,y)=0,
]
because (y	o a) and (b	o y). Thus the off-face pair is the reverse (1,0), so the carrier is fully curved.

Therefore
[
oxed{x	o y}
]
is an actual protected root whose other coordinates (a,b,y) all lie in the single shore (A).

The same argument applies to a nontransitive (B)-shore.

### Theorem

For a pair (x,z) with no protected shortcut (x	o z), the universal two-shore connector has exactly two outcomes:

1. both shores are transitive, in which case the ordinal-sum order is monochromatic and NOR closes;
2. one shore is nontransitive, in which case a directed triangle entirely in that shore yields a fully-curved protected root (x	o y) supported on (x) plus three coordinates of that shore.

Thus the phase-alignment obstruction admits a **strict shore descent**. No arbitrary global shore order has to be aligned first.

### Closure relevance

The descended protected carrier preserves the opposite shore completely outside its active four-set. Hence the remaining compatibility problem can be attacked recursively on a strictly smaller shore while the rest of the universal connector stays frozen.

This supplies a concrete recursive version of the Hartman principle: failure to reach the desired phase-aligned boundary does not produce an arbitrary new obstruction; it exposes the first nontransitive shore cell, namely a directed triangle, and that cell is already a protected exit.
