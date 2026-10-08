# Same-side endpoint reduction

### Same-side endpoint squares return to bounded support

**Lemma 29 (same-side endpoint reduction).** In the quiet double same-slot square of Lemma 25, suppose both cores use endpoint slots on the same side. Then either (H) has a two-cover, or (H) contains a Hamiltonian support of order four or five whose complement is non-Hamiltonian with path-cover number two.

**Proof.** Reverse both core orders if necessary, so that the common slots are the left endpoint slots. Thus
[
(p,c_1,c_2,c_3,c_4),qquad
(x,c_1,c_2,c_3,c_4)
]
and
[
(q,d_1,d_2,d_3,d_4),qquad
(x,d_1,d_2,d_3,d_4)
]
are Hamilton paths.

Consider the two-cover
[
Cmid Q,qquad Q=(q,d_1,d_2,d_3,d_4)
]
of (H-{p,x}). Both (p) and (x) attach at the left endpoint of (C). If either also attached at the left endpoint of (Q), assigning the two omitted labels to different components would give a two-cover of (H). Hence
[
(p,q,d_1),qquad(x,q,d_1)
]
are non-tight, and boundary antisymmetry gives
[
(d_1,q,p),qquad(d_1,q,x)
]
tight.

Similarly, from the two-cover
[
Dmid P,qquad P=(p,c_1,c_2,c_3,c_4)
]
of (H-{q,x}), absence of a two-cover forces
[
(q,p,c_1),qquad(x,p,c_1)
]
non-tight, and hence
[
(c_1,p,q),qquad(c_1,p,x)
]
tight.

Put
[
K_C={c_1,p,q,x},qquad
K_D={d_1,p,q,x}.
]
If (K_C) is Hamiltonian, its complement is two-covered by
[
(c_2,c_3,c_4)mid(d_1,d_2,d_3,d_4).
]
That complement cannot be Hamiltonian, since together with (K_C) it would two-cover (H). Thus its path-cover number is two. The same argument applies if (K_D) is Hamiltonian.

It remains that both (K_C) and (K_D) are non-Hamiltonian. They share the three-set
[
T={p,q,x}.
]
By the small-order theorem that two non-Hamiltonian four-sets (Tcup{u}) and (Tcup{v}) force their five-vertex union to be Hamiltonian,
[
F={c_1,d_1,p,q,x}
]
is Hamiltonian. Its complement is two-covered by
[
(c_2,c_3,c_4)mid(d_2,d_3,d_4).
]
Again the complement cannot be Hamiltonian, or (F) together with it would two-cover (H). Hence its path-cover number is exactly two. (square)

Thus the same-side endpoint square feeds directly back into the bounded four/five-support comparison machinery.

### The central slot is also bounded support

**Lemma 30 (central-slot reduction).** In the quiet double same-slot square of Lemma 25, suppose the common slot of (p,x) in
[
C=(c_1,c_2,c_3,c_4)
]
is the central gap between (c_2,c_3). Then either (H) has a two-cover, or (H) contains a Hamiltonian four-support whose complement is non-Hamiltonian with path-cover number two.

**Proof.** Lemma 27 gives the Hamiltonian four-set
[
K={c_2,c_3,p,x}.
]
Its complement is covered by the two tight paths
[
(c_1,c_4)mid(q,d_1,d_2,d_3,d_4).
]
Here ((c_1,c_4)) is a two-vertex path and the second component is the displayed Hamilton path (Q). Thus
[
operatorname{pc}(H-K)le2.
]
If (H-K) were Hamiltonian, a Hamilton path on (K) together with one on (H-K) would two-cover (H). Hence
[
operatorname{pc}(H-K)=2.
]
(square)

The same argument applies when the central slot occurs on (D). Therefore, after Lemmas 27--30, every exact-slot configuration returns to bounded four/five-support comparison except the opposite-endpoint case. In that remaining case Lemma 27 supplies an explicit cross reversal through (x).

### Exact-slot synchronization has no independent terminal branch

Lemmas 27--30 close the slot analysis completely.

**Corollary 31 (slot-closure reduction).** In the order-eleven prescribed-root normal form, every quiet double same-slot configuration yields at least one of:

1. a two-cover of \(H\);
2. an external tight triple reversing an end edge of a displayed path;
3. a Hamiltonian support of order four or five whose complement is non-Hamiltonian with path-cover number two.

Consequently, after the bounded-support reductions already established in Article III, every exact-slot configuration returns to the two global disturbance interfaces:
\[
\text{external endpoint reversal}
\qquad\text{or}\qquad
\text{split/leave-and-return}.
\]

**Proof.** If both cores use endpoint slots on the same side, Lemma 29 gives outcome 1 or 3. If at least one core uses the central slot, Lemma 30 gives outcome 1 or a Hamiltonian four-support with two-coverable complement, hence outcome 3. If the two cores use opposite endpoint slots, Lemma 27 gives either a two-cover or a cross reversal through \(x\). In the displayed five-path on the core whose endpoint slot contains \(x\), that cross triple reverses the terminal edge, so outcome 2 holds.

Finally, an order-five support in outcome 3 reduces to order four by Lemma 9 of [[defect_lines_and_spanning_order_compression_a_hamiltonian_five_set_beside_a_long_path]]. Applying the strengthened endpoint-deletion Lemma 8 of [[defect_lines_and_spanning_order_compression_an_endpoint_rooted_hamiltonian_four_set]] to the resulting four-support yields either a two-cover, an external endpoint reversal, or a split/leave-and-return disturbance. \(\square\)

Thus the entire order-eleven synchronization analysis contributes structure, but no new terminal geometry. The only unresolved local-to-global conversions are the same two already isolated before the order-eleven refinement:
\[
\boxed{\text{external endpoint reversal}}
\qquad\text{and}\qquad
\boxed{\text{split/leave-and-return disturbance}}.
\]


### Split and leave-and-return disturbances already force an external reversal

**Lemma 32 (split-to-reversal collapse).** Let (H) satisfy (operatorname{pc}(H)>2), and let
[
M=(m_0,ldots,m_t)mid A=(a_0,ldots,a_r)mid B=(b_0,ldots,b_s)
]
be a spanning three-cover. Suppose an inherited displayed edge (m_i m_{i+1}) of (M) is singled out, for example because its endpoints lie in different comparison-path blocks, or because the comparison path leaves (M) between the two blocks and later returns. Then (H) contains an external tight triple reversing an edge of one of the displayed paths (M,A,B).

**Proof.** Apply Proposition 2.1 of [[coversurg01]] to the cut of (M) between (m_i) and (m_{i+1}). Pair the prefix (M[0,i]) with (A), and pair (B) with the suffix (M[i+1,t]). Every consecutive triple in these two spanning sequences is inherited except possibly the present members of
[
(m_{i-1},m_i,a_0),qquad
(m_i,a_0,a_1),qquad
(b_{s-1},b_s,m_{i+1}),qquad
(b_s,m_{i+1},m_{i+2}).
]
At least one present triple is non-tight, since otherwise the two concatenated sequences form a spanning two-cover of (H).

Boundary antisymmetry reverses any failed triple. Respectively the four possibilities give
[
(a_0,m_i,m_{i-1}),qquad
(a_1,a_0,m_i),qquad
(m_{i+1},b_s,b_{s-1}),qquad
(m_{i+2},m_{i+1},b_s),
]
whenever the corresponding triple exists. Each is an external tight triple reversing an edge of one of the displayed paths. (square)

In particular, both positional outcomes of the endpoint-deletion comparison—an inherited displayed edge split between two comparison paths, and a leave-and-return disturbance through a nonempty exterior segment—feed immediately into the external-reversal interface.

**Corollary 33 (single remaining interface).** After the reductions of Article III, the only unresolved local-to-global conversion is
[
oxed{	ext{external endpoint reversal}.}
]
The split/leave-and-return branch is not independent.
