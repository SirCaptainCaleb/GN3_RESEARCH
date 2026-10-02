# Order eleven has no longest path of order seven

## Statement

A hypothetical order-eleven minimum counterexample cannot have maximum tight-path order seven. In the codimension-four endpoint kernel, the 4|4 case is excluded by astra003lambda7case1; in the remaining 6|2 case, the outgoing two-edge block at the terminal endpoint appends to the inherited suffix of the longest seven-path, producing a Hamiltonian seven-set whose complementary displayed four-set is Hamiltonian, hence a spanning two-cover.

## Body


Let
[
Y=(L,u,x_2,x_3,x_4,v,R)
]
be a globally longest tight path of order seven in a hypothetical order-eleven minimum counterexample (H), with four-vertex complement
[
S=V(H)-V(Y).
]

Apply Proposition 5.1 of the certified codimension-four module codim4_01.

The first case of that proposition, the (4|4) endpoint/complement cover, is impossible by astra003lambda7case1.

It remains to exclude the second case.

In that case the middle matching block of (S) has edges
[
O={b,z},qquad I={i_0,i_1},
]
where (O) is outgoing at (L) and incoming at (R), while (I) is incoming at (L) and outgoing at (R). Proposition 5.1 gives the tight six-path
[
(u,L,b,z,R,v)
]
and the complementary two-vertex path (I).

In particular
[
A=(u,L,b,z)
]
is a tight four-path.

Because (I) is outgoing at (R), choose an orientation ((i_0,i_1)) of (I) for which
[
(R,i_0,i_1)
]
is tight.

Proposition 1.2 of codim4_01 says that for every (sin S),
[
(s,R,v)
]
is tight. Taking (s=i_0) and reversing gives
[
(v,R,i_0)
]
tight.

The inherited suffix
[
(x_2,x_3,x_4,v,R)
]
is a tight subpath of (Y). Consequently
[
(x_2,x_3,x_4,v,R,i_0,i_1)
]
is a tight Hamiltonian path on the seven-set
[
{x_2,x_3,x_4,v,R,i_0,i_1}.
]

Its complementary four-set is exactly
[
{L,u,b,z}=V(A),
]
which is Hamiltonian.

Thus
[
(x_2,x_3,x_4,v,R,i_0,i_1)mid(u,L,b,z)
]
is a spanning two-path cover of (H), contradiction.

Therefore the second case of codim4_01 Proposition 5.1 is impossible as well. Since its two cases are exhaustive, a hypothetical order-eleven minimum counterexample cannot have maximum tight-path order seven.
