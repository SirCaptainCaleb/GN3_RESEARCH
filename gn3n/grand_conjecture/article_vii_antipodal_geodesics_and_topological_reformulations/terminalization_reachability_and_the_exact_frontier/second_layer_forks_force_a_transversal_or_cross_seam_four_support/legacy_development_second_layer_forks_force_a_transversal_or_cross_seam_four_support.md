# Second-layer forks force a transversal or cross-seam four-support — preserved pre-item development

## Development

## Second-layer forks force a four-support at every complementary seam

Let (H) satisfy (kappa_2(H)=2). Let
[
Smid Pmid Q
]
be a maximal-support normalization, with
[
S=(s_1,ldots,s_k),quad
P=(p_1,ldots,p_m),quad
Q=(q_1,ldots,q_t),
]
and assume (k,m,tge3).

Maximal-support nonaugmentability gives, in particular,
[
h(q_1,s_k,s_{k-1})=1,
qquad
h(s_2,s_1,p_m)=1.
]

Apply [[deletion_critical_complements_force_second_layer_junction_forks]] at the seam from the terminal end of (P) to the initial end of (Q).

Deleting (p_m) gives
[
h(q_1,p_{m-1},p_{m-2})=1
quad	ext{or}quad
h(q_2,q_1,p_{m-1})=1.
	ag{A}
]

Deleting (q_1) gives
[
h(q_2,p_m,p_{m-1})=1
quad	ext{or}quad
h(q_3,q_2,p_m)=1.
	ag{B}
]

There are two possibilities.

### Exposed-carrier branch

If the first alternative of (A) holds, the exposed endpoint (q_1) reverses terminal edges of both (S) and the shortened path
[
(p_1,ldots,p_{m-1}).
]
The valid common-reverser lemma therefore yields a Hamiltonian four-support meeting (S,P,Q).

Likewise, if the second alternative of (B) holds, the exposed endpoint (p_m) reverses initial edges of both (S) and
[
(q_2,ldots,q_t),
]
and the initial-initial common-reverser lemma again yields a Hamiltonian four-support meeting all three components.

### Pure cross-seam branch

Suppose neither exposed-carrier alternative occurs. Then the remaining two forks are forced:
[
h(q_2,q_1,p_{m-1})=1,
qquad
h(q_2,p_m,p_{m-1})=1.
]
Thus (q_1,p_m) are two parallel middle vertices between the fixed endpoints
[
q_2, p_{m-1}.
]
By the two-parallel-middle lemma, exactly one of
[
(q_2,q_1,p_{m-1},p_m),
qquad
(q_2,p_m,p_{m-1},q_1)
]
is a tight Hamiltonian four-path.

Hence
[
oxed{{q_2,q_1,p_{m-1},p_m}	ext{ is Hamiltonian}.}
]

Therefore:

> **Seam four-support dichotomy.** At every (P	o Q) seam of a maximal-support (kappa_2=2) state with both complementary paths of order at least three, either a Hamiltonian four-support is transversal to (S|P|Q), or the two first layers at the seam form the explicit cross-seam Hamiltonian four-support
> [
> {q_2,q_1,p_{m-1},p_m}.
> ]

The (Q	o P) seam gives the symmetric opposite-side certificate.

This uses only literal boundary flips from endpoint-deletion criticality and the audited parallel-middle/common-reverser lemmas. No cyclic rotation or path reversal is used.
