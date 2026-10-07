# Coboundary flat orientations reduce exactly to tournament two chord words

## Metadata

- ID: coboundary_flat_orientations_reduce_exactly_to_tournament_two_chord_words
- Parent Section: directed_nor_union_closed_bridge
- Position: 65
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Coboundary-flat orientations reduce exactly to tournament two-chord words

Fix a global linear order on (V), and encode the alternating triangle orientation by unordered face bits
[
f({a,b,c})
]
on increasing triples.

Assume
[
delta f=0
]
on every four-set. Equivalently, there are no singly-curved tetrahedra; every tetrahedron is flat or fully curved.

### Proposition 1: edge-potential representation

There is an unordered edge labeling
[
g:inom V2	o{0,1}
]
such that for every unordered triple
[
{a,b,c},
qquad
f(abc)=g(ab)oplus g(ac)oplus g(bc).
]

#### Proof
Fix a root (r). Put
[
g(ra)=0
]
for all (a
e r), and for (a,b
e r) put
[
g(ab)=f(rab)
]
with the arguments sorted when evaluating (f).

For (a,b,c
e r), the cocycle identity on the four-set ({r,a,b,c}) gives
[
f(abc)
=
f(rab)oplus f(rac)oplus f(rbc),
]
which is exactly the required edge sum. Triples containing (r) are immediate. (square)

### Proposition 2: tournament representation

Define a tournament edge bit on ordered pairs by
[
t(a,b)=[a>b]oplus g(ab),
]
where ([a>b]) refers to the fixed global order. Then
[
t(b,a)=1-t(a,b).
]

For every ordered triple of distinct vertices,
[
alpha(a,b,c)
=
1oplus t(a,b)oplus t(b,c)oplus t(c,a).
	ag{1}
]

Indeed, if (p(a,b,c)) is the parity of the permutation from increasing order to ((a,b,c)), then
[
alpha(a,b,c)=f({a,b,c})oplus p(a,b,c),
]
while
[
[a>b]oplus[b>c]oplus[c>a]=1oplus p(a,b,c).
]
Substituting the edge-potential identity gives (1).

### Corollary 3: NOR becomes a distance-two shortcut problem

Take any directed Hamilton path of the tournament (T),
[
v_1	o v_2	ocdots	o v_n,
]
using the convention
[
t(v_i,v_{i+1})=0.
]
Then (1) reduces to
[
alpha(v_i,v_{i+1},v_{i+2})
=
t(v_i,v_{i+2}).
	ag{2}
]

Thus the ternary status is (0) exactly when the distance-two shortcut is forward,
[
v_i	o v_{i+2},
]
and is (1) exactly when it is backward,
[
v_{i+2}	o v_i.
]

Therefore the pure-orientation NOR problem in the coboundary-flat sector is equivalent to:

> Find a directed Hamilton path in a tournament whose distance-two shortcut directions change at most once.

### Local transition surgery

Suppose four consecutive vertices of a directed Hamilton path are
[
a	o b	o c	o d.
]
If the first shortcut is forward and the second backward,
[
a	o c,qquad d	o b,
]
then
[
a	o c	o d	o b
]
is also a directed path on those four vertices.

Hence a forward-to-backward shortcut transition admits a local path surgery that removes (b) from its old position and places it after (d). Since (d	o b), the ordinary tournament path-insertion procedure can continue moving (b) rightward through the remaining suffix until a directed Hamilton path is restored.

A closure route is to find a monotone potential under this bubbling operation, so that all forward shortcuts precede all backward shortcuts (or vice versa). Such a sorted shortcut word is exactly a NOR order in the (delta f=0) sector.


## Frontier

- Development version when composed: None
- Development version now: 1
