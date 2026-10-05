# Slot synchronization reductions

## Metadata

- ID: defect_lines_and_spanning_order_compression_the_remaining_lemma_subsection_c
- Parent Section: defect_lines_and_spanning_order_compression_the_remaining_lemma
- Position: 3
- Row version: 4
- Development version: 4
- Composition version: 1
- Composition stale: False

## Cold composition

### Central slots and opposite endpoint slots

The nine slot pairs left by Lemma 26 separate into two immediate structural classes.

**Lemma 27 (central bridge or cross reversal).** Work in the quiet double same-slot square of Lemma 25.

1. Suppose the common insertion slot of (p,x) in
   [
   C=(c_1,c_2,c_3,c_4)
   ]
   is the central gap between (c_2,c_3). Then
   [
   {c_2,c_3,p,x}
   ]
   is a Hamiltonian four-set. The analogous statement holds on (D).

2. Suppose the common slot of (p,x) in (C) is the right endpoint slot and the common slot of (q,x) in
   [
   D=(d_1,d_2,d_3,d_4)
   ]
   is the left endpoint slot. Then either (H) has a two-cover or
   [
   (d_1,x,c_4)
   ]
   is tight. Symmetrically, if the slots are left on (C) and right on (D), then either (H) has a two-cover or
   [
   (c_1,x,d_4)
   ]
   is tight after the corresponding reversal of notation.

**Proof.** For (1), the two Hamilton paths on (Ccup{p}) and (Ccup{x}) induce the same core order and insert their exceptional vertices into the same internal edge (c_2c_3). Lemma 4(3) of the compatible one-vertex extension calculus gives a Hamilton path on the four-set ({c_2,c_3,p,x}).

For (2), the endpoint-slot assumptions give Hamilton paths
[
(c_1,c_2,c_3,c_4,x)
qquad	ext{and}qquad
(x,d_1,d_2,d_3,d_4).
]
Hence every consecutive triple in
[
(c_1,c_2,c_3,c_4,x,d_1,d_2,d_3,d_4)
]
is tight except possibly
[
(c_4,x,d_1).
]
If this triple is tight, the displayed nine vertices form one tight path; the remaining two vertices are (p,q), which form a tight two-vertex path. Thus (H) has a two-cover.

Therefore in a minimum counterexample ((c_4,x,d_1)) is non-tight. Boundary antisymmetry gives
[
(d_1,x,c_4)
]
tight. The opposite orientation is symmetric. (square)

Thus after Lemmas 25--27 the exact-slot residue has only three genuinely different forms:

- at least one core uses the central slot, producing a Hamiltonian four-bridge through (x) and its displaced label;
- the two cores use opposite endpoint slots, producing an explicit cross reversal through (x);
- both cores use endpoint slots on the same side.

The last case is the only endpoint-slot pattern with no additional structure yet forced.

### Reciprocal swaps force a three-extension common core

**Lemma 28.** In the order-eleven normal form
[
H-x=Pmid Q,quad P=Ccup{p},quad Q=Dcup{q},
]
there is a four-set (E) with three distinct vertices (r_1,r_2,r_3
otin E) such that every (Ecup{r_i}) is Hamiltonian and has two-coverable complement.

**Proof.** By [[extremal01]], (Pmid Q) has at least five double-good reciprocal-swap cells. If one uses row (p), say ((p,d)), then (C+p,C+x,C+d) are three Hamiltonian extensions of (C). A cell in column (q) is symmetric.

Otherwise all five cells lie in the (4	imes4) matrix (C	imes D). Some row or column has degree at least two. Suppose (cin C) has distinct neighbors (d_1,d_2in D), and put
[
E=(C-{c})cup{p}.
]
Then (E+c=P) is Hamiltonian, and double-goodness gives (E+d_1,E+d_2) Hamiltonian. Their complements are two-coverable: for (E+c) use (Qmid{x}); for (E+d_i), use the swapped Hamiltonian five-set ((Q-{d_i})cup{c}) together with ({x}). The column case is symmetric. (square)

Hence every balanced order-eleven deletion state enters the three-extension configuration of [[longest_paths_and_reversal_structure_a_common_four_vertex_core]]. The same-direction endpoint residue cannot remain isolated under reciprocal-swap mobility.



## Development

### Central slots and opposite endpoint slots

The nine slot pairs left by Lemma 26 separate into two immediate structural classes.

**Lemma 27 (central bridge or cross reversal).** Work in the quiet double same-slot square of Lemma 25.

1. Suppose the common insertion slot of (p,x) in
   [
   C=(c_1,c_2,c_3,c_4)
   ]
   is the central gap between (c_2,c_3). Then
   [
   {c_2,c_3,p,x}
   ]
   is a Hamiltonian four-set. The analogous statement holds on (D).

2. Suppose the common slot of (p,x) in (C) is the right endpoint slot and the common slot of (q,x) in
   [
   D=(d_1,d_2,d_3,d_4)
   ]
   is the left endpoint slot. Then either (H) has a two-cover or
   [
   (d_1,x,c_4)
   ]
   is tight. Symmetrically, if the slots are left on (C) and right on (D), then either (H) has a two-cover or
   [
   (c_1,x,d_4)
   ]
   is tight after the corresponding reversal of notation.

**Proof.** For (1), the two Hamilton paths on (Ccup{p}) and (Ccup{x}) induce the same core order and insert their exceptional vertices into the same internal edge (c_2c_3). Lemma 4(3) of the compatible one-vertex extension calculus gives a Hamilton path on the four-set ({c_2,c_3,p,x}).

For (2), the endpoint-slot assumptions give Hamilton paths
[
(c_1,c_2,c_3,c_4,x)
qquad	ext{and}qquad
(x,d_1,d_2,d_3,d_4).
]
Hence every consecutive triple in
[
(c_1,c_2,c_3,c_4,x,d_1,d_2,d_3,d_4)
]
is tight except possibly
[
(c_4,x,d_1).
]
If this triple is tight, the displayed nine vertices form one tight path; the remaining two vertices are (p,q), which form a tight two-vertex path. Thus (H) has a two-cover.

Therefore in a minimum counterexample ((c_4,x,d_1)) is non-tight. Boundary antisymmetry gives
[
(d_1,x,c_4)
]
tight. The opposite orientation is symmetric. (square)

Thus after Lemmas 25--27 the exact-slot residue has only three genuinely different forms:

- at least one core uses the central slot, producing a Hamiltonian four-bridge through (x) and its displaced label;
- the two cores use opposite endpoint slots, producing an explicit cross reversal through (x);
- both cores use endpoint slots on the same side.

The last case is the only endpoint-slot pattern with no additional structure yet forced.

### Reciprocal swaps force a three-extension common core

**Lemma 28.** In the order-eleven normal form
[
H-x=Pmid Q,quad P=Ccup{p},quad Q=Dcup{q},
]
there is a four-set (E) with three distinct vertices (r_1,r_2,r_3
otin E) such that every (Ecup{r_i}) is Hamiltonian and has two-coverable complement.

**Proof.** By [[extremal01]], (Pmid Q) has at least five double-good reciprocal-swap cells. If one uses row (p), say ((p,d)), then (C+p,C+x,C+d) are three Hamiltonian extensions of (C). A cell in column (q) is symmetric.

Otherwise all five cells lie in the (4	imes4) matrix (C	imes D). Some row or column has degree at least two. Suppose (cin C) has distinct neighbors (d_1,d_2in D), and put
[
E=(C-{c})cup{p}.
]
Then (E+c=P) is Hamiltonian, and double-goodness gives (E+d_1,E+d_2) Hamiltonian. Their complements are two-coverable: for (E+c) use (Qmid{x}); for (E+d_i), use the swapped Hamiltonian five-set ((Q-{d_i})cup{c}) together with ({x}). The column case is symmetric. (square)

Hence every balanced order-eleven deletion state enters the three-extension configuration of [[longest_paths_and_reversal_structure_a_common_four_vertex_core]]. The same-direction endpoint residue cannot remain isolated under reciprocal-swap mobility.
