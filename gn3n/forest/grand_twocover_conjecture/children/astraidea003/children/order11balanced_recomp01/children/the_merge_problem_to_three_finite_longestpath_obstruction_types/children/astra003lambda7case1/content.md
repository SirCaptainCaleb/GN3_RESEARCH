# The 4|4 endpoint-kernel branch is impossible when the longest path has order seven

## Statement

Let H be a hypothetical order-eleven minimum counterexample with a longest tight path Y=(L,u,x2,x3,x4,v,R) of order seven and non-Hamiltonian four-vertex complement S. In Proposition 5.1 of codim4_01, the 4|4 endpoint/complement case cannot occur. Indeed one displayed four-path reverses and concatenates with the middle triple (x2,x3,x4) to give a Hamiltonian seven-set, whose complementary displayed four-path is Hamiltonian, producing a spanning two-cover.

## Body


Let
[
Y=(L,u,x_2,x_3,x_4,v,R)
]
be a globally longest tight path of order seven in a hypothetical order-eleven minimum counterexample (H), and let
[
S=V(H)-V(Y),
qquad |S|=4.
]
As in codim4_01, (S) is non-Hamiltonian.

Put
[
N=(x_2,x_3,x_4).
]
Apply Proposition 5.1 of codim4_01 to the eight vertices
[
Scup{L,u,v,R}.
]

Assume its first case occurs. Then, with the notation of that proposition, there is an exact (4|4) cover
[
Amid B
]
where
[
A=(u,L,o_0,o_1)
]
is a tight four-path and
[
B=(i_0,i_1,R,v)
]
is the complementary tight four-path.

Reverse (A). Since reversal preserves tight paths,
[
(o_1,o_0,L,u)
]
is a tight four-path.

Now append the middle triple (N). The seven-vertex order
[
(o_1,o_0,L,u,x_2,x_3,x_4)
]
is tight: its first two consecutive triples are those of the reversed path (A), while
[
(L,u,x_2),quad (u,x_2,x_3),quad (x_2,x_3,x_4)
]
are consecutive triples of the original tight path (Y).

Therefore
[
V(A)cup V(N)
]
is a Hamiltonian seven-set.

The complementary vertex set is exactly (V(B)), and (B) is Hamiltonian. Hence
[
(Acup N)mid B
]
is a spanning two-path cover of (H), contradiction.

Equivalently, this directly contradicts the universal seven-set no-merge barrier astra003sevenbarrier applied to the (4|4|3) state
[
Nmid Amid B.
]

Thus the first, balanced (4|4), case of codim4_01 Proposition 5.1 is impossible in the order-eleven (lambda=7) branch. Only the (6|2) endpoint-kernel case can remain.
