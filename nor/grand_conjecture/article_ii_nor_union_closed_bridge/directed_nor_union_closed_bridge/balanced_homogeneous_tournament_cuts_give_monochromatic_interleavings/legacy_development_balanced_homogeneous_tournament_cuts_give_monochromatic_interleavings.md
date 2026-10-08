# Balanced homogeneous tournament cuts give monochromatic interleavings — preserved pre-item development

## Balanced homogeneous tournament cuts give monochromatic interleavings

Work in the coboundary-flat pure-orientation sector, with tournament representation
[
alpha(a,b,c)=1oplus t(a,b)oplus t(b,c)oplus t(c,a),
]
where (t(x,y)=0) means (x	o y) in the representing tournament.

Suppose
[
V=Adotcup B,
qquad
A	o B,
]
meaning every tournament edge between the two parts is directed from (A) to (B). Assume
[
igl||A|-|B|igr|le1.
]

Choose directed Hamilton paths
[
a_1	o a_2	ocdots	o a_r
]
in (T[A]), and
[
b_1	o b_2	ocdots	o b_s
]
in (T[B]).

Interleave them, starting with either side of larger cardinality:
[
a_1,b_1,a_2,b_2,ldots
]
when (rge s), with the evident final unmatched (a_r) if (r=s+1).

### Theorem

Every consecutive ternary status in this interleaved order equals (1). Hence the order is monochromatic.

### Proof

A consecutive triple has one of two forms.

For
[
(a_i,b_i,a_{i+1}),
]
the tournament edge bits in written cyclic order are
[
t(a_i,b_i)=0,
qquad
t(b_i,a_{i+1})=1,
qquad
t(a_{i+1},a_i)=1,
]
because (A	o B) and (a_i	o a_{i+1}). Therefore
[
alpha(a_i,b_i,a_{i+1})
=
1oplus0oplus1oplus1
=
1.
]

For
[
(b_i,a_{i+1},b_{i+1}),
]
one has
[
t(b_i,a_{i+1})=1,
qquad
t(a_{i+1},b_{i+1})=0,
qquad
t(b_{i+1},b_i)=1,
]
so again the status is (1).

If one part has one extra vertex, the alternating pattern simply ends after the last triple of the same two forms. (square)

### Consequences

Any balanced homogeneous cut closes the coboundary-flat sector monochromatically.

In particular, a tournament formed by two directed 3-cycles with every cross edge from the first cycle to the second—although it refutes the directed-Hamilton two-chord route—has the monochromatic interleaving
[
a_1,b_1,a_2,b_2,a_3,b_3.
]

More generally, if the strongly connected component condensation of the representing tournament has a prefix whose total size is (lfloor n/2floor) or (lceil n/2ceil), the prefix and suffix form such a balanced homogeneous cut and NOR closes immediately.
