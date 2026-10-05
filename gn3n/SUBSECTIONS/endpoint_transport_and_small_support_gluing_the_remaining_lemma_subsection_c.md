# Every deletion cover yields a four-support

## Metadata

- ID: endpoint_transport_and_small_support_gluing_the_remaining_lemma_subsection_c
- Parent Section: endpoint_transport_and_small_support_gluing_the_remaining_lemma
- Position: 3
- Row version: 3
- Development version: 3
- Composition version: 1
- Composition stale: False

## Cold composition

### Every deletion cover contains a doubly reversed end edge

**Lemma 14 (four-fold deletion reversal).** Let (H) be a minimum counterexample and let
[
H-x=Pmid Q,
qquad
P=(p_1,ldots,p_m),
qquad
Q=(q_1,ldots,q_s)
]
be any deletion cover. Then (m,sge2), and the omitted vertex (x) reverses all four displayed end edges:
[
(p_2,p_1,x),qquad
(x,p_m,p_{m-1}),
]
[
(q_2,q_1,x),qquad
(x,q_s,q_{s-1})
]
are tight.

**Proof.** Minimum-counterexample calculus gives (m,sge2).

If ((x,p_1,p_2)) were tight, then
[
(x,p_1,ldots,p_m)mid Q
]
would be a spanning two-cover of (H). Hence ((x,p_1,p_2)) is non-tight, and boundary antisymmetry gives
[
(p_2,p_1,x)
]
tight.

Likewise, if ((p_{m-1},p_m,x)) were tight, then
[
(p_1,ldots,p_m,x)mid Q
]
would two-cover (H). Thus its boundary flip
[
(x,p_m,p_{m-1})
]
is tight. The two statements for (Q) are symmetric. (square)

The omitted label is therefore not merely an external reverser somewhere: it simultaneously reverses both exposed ends of both paths in every deletion cover.

**Corollary 15 (every deletion cover yields a Hamiltonian four-support).** Under the hypotheses of Lemma 14, some displayed end edge of (P) or (Q) has two distinct exterior reversers. Consequently (H) contains a Hamiltonian four-support (K) with
[
operatorname{pc}(H-K)=2,
]
and (H-K) is non-Hamiltonian.

**Proof.** Try to concatenate the displayed orders (P,Q). Since
[
P,Qmid{x}
]
cannot be a two-cover, at least one of the two junction triples
[
(p_{m-1},p_m,q_1),
qquad
(p_m,q_1,q_2)
]
is non-tight.

If the first is non-tight, boundary antisymmetry gives
[
(q_1,p_m,p_{m-1})
]
tight. Together with Lemma 14,
[
(x,p_m,p_{m-1})
]
is tight as well. Thus the terminal edge (p_{m-1}p_m) of (P) has two distinct exterior reversers (x,q_1).

If instead the second junction triple is non-tight, then
[
(q_2,q_1,p_m)
]
is tight. Lemma 14 also gives
[
(q_2,q_1,x)
]
tight. Thus the initial edge (q_1q_2) of (Q) has two distinct exterior reversers (p_m,x).

In either case Lemma 38 of the spanning-order compression analysis applies. Since (n>10), choose the additional distinct vertex required there. It yields a Hamiltonian four-set (K).

Minimum-counterexample calculus gives
[
operatorname{pc}(H-K)le2.
]
The complement cannot be Hamiltonian, or a Hamilton path on (K) together with one on (H-K) would two-cover (H). Hence
[
operatorname{pc}(H-K)=2.
]
(square)

This is an arbitrary-order reduction from the general counterexample to the four-support interface. It uses no longest-path choice, no bounded-order classification, and no special support-graph geometry: **every deletion cover already contains enough endpoint failure to force such a four-support.**

The remaining issue is therefore not whether the general problem reaches order-four support—it does canonically from every deleted vertex—but whether the resulting four-support can be chosen with enough retained endpoint incidence to manufacture the one-defect bridge or a direct two-cover.

## Development

### Every deletion cover contains a doubly reversed end edge

**Lemma 14 (four-fold deletion reversal).** Let (H) be a minimum counterexample and let
[
H-x=Pmid Q,
qquad
P=(p_1,ldots,p_m),
qquad
Q=(q_1,ldots,q_s)
]
be any deletion cover. Then (m,sge2), and the omitted vertex (x) reverses all four displayed end edges:
[
(p_2,p_1,x),qquad
(x,p_m,p_{m-1}),
]
[
(q_2,q_1,x),qquad
(x,q_s,q_{s-1})
]
are tight.

**Proof.** Minimum-counterexample calculus gives (m,sge2).

If ((x,p_1,p_2)) were tight, then
[
(x,p_1,ldots,p_m)mid Q
]
would be a spanning two-cover of (H). Hence ((x,p_1,p_2)) is non-tight, and boundary antisymmetry gives
[
(p_2,p_1,x)
]
tight.

Likewise, if ((p_{m-1},p_m,x)) were tight, then
[
(p_1,ldots,p_m,x)mid Q
]
would two-cover (H). Thus its boundary flip
[
(x,p_m,p_{m-1})
]
is tight. The two statements for (Q) are symmetric. (square)

The omitted label is therefore not merely an external reverser somewhere: it simultaneously reverses both exposed ends of both paths in every deletion cover.

**Corollary 15 (every deletion cover yields a Hamiltonian four-support).** Under the hypotheses of Lemma 14, some displayed end edge of (P) or (Q) has two distinct exterior reversers. Consequently (H) contains a Hamiltonian four-support (K) with
[
operatorname{pc}(H-K)=2,
]
and (H-K) is non-Hamiltonian.

**Proof.** Try to concatenate the displayed orders (P,Q). Since
[
P,Qmid{x}
]
cannot be a two-cover, at least one of the two junction triples
[
(p_{m-1},p_m,q_1),
qquad
(p_m,q_1,q_2)
]
is non-tight.

If the first is non-tight, boundary antisymmetry gives
[
(q_1,p_m,p_{m-1})
]
tight. Together with Lemma 14,
[
(x,p_m,p_{m-1})
]
is tight as well. Thus the terminal edge (p_{m-1}p_m) of (P) has two distinct exterior reversers (x,q_1).

If instead the second junction triple is non-tight, then
[
(q_2,q_1,p_m)
]
is tight. Lemma 14 also gives
[
(q_2,q_1,x)
]
tight. Thus the initial edge (q_1q_2) of (Q) has two distinct exterior reversers (p_m,x).

In either case Lemma 38 of the spanning-order compression analysis applies. Since (n>10), choose the additional distinct vertex required there. It yields a Hamiltonian four-set (K).

Minimum-counterexample calculus gives
[
operatorname{pc}(H-K)le2.
]
The complement cannot be Hamiltonian, or a Hamilton path on (K) together with one on (H-K) would two-cover (H). Hence
[
operatorname{pc}(H-K)=2.
]
(square)

This is an arbitrary-order reduction from the general counterexample to the four-support interface. It uses no longest-path choice, no bounded-order classification, and no special support-graph geometry: **every deletion cover already contains enough endpoint failure to force such a four-support.**

The remaining issue is therefore not whether the general problem reaches order-four support—it does canonically from every deleted vertex—but whether the resulting four-support can be chosen with enough retained endpoint incidence to manufacture the one-defect bridge or a direct two-cover.
