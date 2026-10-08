# Transitive pivot links force a global cyclic order — preserved pre-item development

## Composition

(none yet)

## Development

## Transitive pivot links force a global cyclic order

Let (alpha) be an alternating orientation of every unordered triple of a finite vertex set (V). For each pivot (o), define the link tournament (G_o) on (Vsetminus{o}) by
[
a	o_o b quadLongleftrightarrowquad alpha(o,a,b)=0.
]

### Theorem

If every link tournament (G_o) is transitive, then there is a cyclic ordering of (V) whose every consecutive triple has (alpha)-color (0). In fact, fixing any pivot (o) and writing its unique transitive order as
[
v_1<_o v_2<_ocdots<_o v_{n-1},
]
the linear order
[
(o,v_1,ldots,v_{n-1})
]
is (alpha)-monochromatic.

### Proof

Take indices (i<j<k). Since (v_i<_o v_j),
[
alpha(o,v_i,v_j)=0.
]
Cyclic permutation of an oriented triangle preserves its orientation, so
[
alpha(v_j,o,v_i)=0.
]
Thus in the link tournament (G_{v_j}),
[
o	o_{v_j} v_i.
]

Similarly, (v_j<_o v_k) gives
[
alpha(o,v_j,v_k)=0,
]
hence
[
alpha(v_j,v_k,o)=0,
]
so in (G_{v_j}),
[
v_k	o_{v_j} o.
]

Therefore
[
v_k	o_{v_j} o	o_{v_j} v_i.
]
By transitivity of (G_{v_j}),
[
v_k	o_{v_j} v_i,
]
which means
[
alpha(v_j,v_k,v_i)=0.
]
A cyclic permutation gives
[
alpha(v_i,v_j,v_k)=0.
]

In particular, taking (j=i+1) and (k=i+2), every consecutive triple of
[
(o,v_1,ldots,v_{n-1})
]
has color (0). (square)

### Interpretation

The relation (alpha=0) is therefore a genuine cyclic order whenever all of its pivot links are transitive. A pure-orientation counterexample to ternary NOR must contain a directed triangle in at least one link tournament.

This identifies the first local obstruction to the global simplex orientation being cyclic: nontransitivity of a pivot link. It also supplies a clean target for path optimization. Directed triangles in (G_o) are precisely the places where the pivot has multiple locally competing Hamilton-path orders; those alternatives are potential moves for reducing the centered triangle-closure variation of the pivot path.
