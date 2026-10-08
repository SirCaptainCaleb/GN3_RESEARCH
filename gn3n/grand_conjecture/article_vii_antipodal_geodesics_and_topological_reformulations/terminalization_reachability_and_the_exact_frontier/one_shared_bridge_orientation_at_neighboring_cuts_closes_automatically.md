# One shared-bridge orientation at neighboring cuts closes automatically

## Composition

(none yet)

## Development

## One shared-bridge orientation at neighboring cuts closes automatically

Retain the notation of [[a_shared_bridge_at_neighboring_cuts_exposes_four_new_repair_labels]] in its monotone-corridor application:
[
A={x,y,c_1,c_2},quad
r=c_{j+1},quad v=c_{j+2},quad s=c_{j+3},
]
[
T=(c_3,ldots,c_j),qquad U=(c_N,ldots,c_{j+4}),
]
where (j=u) or (u+1), so (T,U) have order at least two and ((c_2,c_3,c_4)) is tight.

Assume (v) is a bridge in both neighboring packet tests and that neither test already yields a two-cover. Then the cited neighboring-cut lemma gives the third packet
[
S_v=Acup{r,s}
]
and proves that every deletion (S_v-w), (win A), is Hamiltonian.

**Lemma.** In this residual situation, the first bridge cannot have orientation
[
(T,v,U,s).
]

**Proof.** If ((T,v,U,s)) is tight, then its contiguous subpath
[
R=(T,v,U)
]
is tight and is exactly the complement of (S_v) together with the packet vertex (c_2) still unused after deleting (c_2) from (S_v).

By the preceding packet conclusion,
[
S_v-{c_2}
]
is Hamiltonian. On the other hand (T) begins with (c_3,c_4), and the original monotone corridor has status (1) at position (2); hence
[
(c_2,c_3,c_4)
]
is tight. Therefore
[
(c_2,R)=(c_2,T,v,U)
]
is a tight path.

The two disjoint paths
[
S_v-{c_2}
qquad	ext{and}qquad
(c_2,T,v,U)
]
partition the full reflected-double span, giving a two-cover. This contradicts the residual assumption. (square)

Consequently, if the shared label (v) bridges the first neighboring packet test in a genuine obstruction, its orientation is forced to be
[
(U,s,v,T).
]

There is a right-end mirror of the same statement, obtained by using
[
A^{m R}={x,y,c_{N-1},c_N}
]
and the reversed tail decomposition. Thus a surviving shared bridge is not merely restricted to the at-most-two bad deletion labels; its **bridge orientation is forced inward from both packet ends**.

This orientation constraint is stronger than the seven-vertex degree bound and is the next compatibility datum to propagate across the three mobile cuts.
