# At order eleven, a longest six-path must expose crossing or order disagreement

## Statement

Let H be a hypothetical order-eleven minimum counterexample with maximum tight-path order six. In the final codimension-five endpoint normalization, the neutral two-end exchange outcome is impossible. Therefore some endpoint-deletion exact two-cover has at least two path edges crossing the longest-path/complement cut, or an endpoint comparison exposes explicit relative-order disagreement.

## Body

Let
[
Y=(y_0,y_1,y_2,y_3,y_4,y_5)
]
be a globally longest tight path of order six in a hypothetical order-eleven minimum counterexample (H), and let
[
F=V(H)-V(Y),
qquad |F|=5.
]
The complement (F) is non-Hamiltonian.

Apply the final endpoint normalization theorem of codim5_01.

If its first or second conclusion holds, we already obtain respectively:
1. an endpoint-deletion exact two-cover with at least two ordinary edges crossing between the surviving (Y)-vertices and (F); or
2. explicit relative-order disagreement with an inherited Hamilton order.

It remains to exclude conclusion 3.

Assume therefore there are distinct
[
ell,rin F
]
such that
[
Y'=(ell,y_1,y_2,y_3,y_4,r)
]
is a tight path and its complementary five-set is non-Hamiltonian.

Put
[
M=(y_1,y_2,y_3,y_4),qquad
a=y_0,qquad c=y_5.
]
Then both
[
(a,M,c)
quad	ext{and}quad
(ell,M,r)
]
are tight. By the certified common-middle rectangle theorem commonmiddle01, the mixed paths
[
(a,M,r),qquad (ell,M,c)
]
are tight as well.

The four endpoint vertices
[
a,ell,c,r
]
together with (M) use eight vertices of (H). Let
[
T=V(H)-igl(V(M)cup{a,ell,c,r}igr),
qquad |T|=3.
]
Thus the hypotheses of the certified four-endpoint-barrier theorem in commonmiddle01 hold.

Hence there exists
[
sin T
]
such that, in particular,
[
(y_1,y_0,s)
]
is tight.

By reversal,
[
(s,y_0,y_1)
]
is tight. Since
[
(y_0,y_1,y_2,y_3,y_4,y_5)
]
is the original tight path, the seven-vertex sequence
[
(s,y_0,y_1,y_2,y_3,y_4,y_5)
]
is a tight path.

This contradicts astra003nolambda7, which excludes every tight path of order seven in a hypothetical order-eleven minimum counterexample.

Therefore conclusion 3 of codim5_01 cannot occur. Every order-eleven (lambda=6) counterexample must fall into conclusion 1 or 2: crossing multiplicity at least two, or explicit relative-order disagreement.
