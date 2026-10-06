# The odd-cycle case

## Composition

Assume now that \(J\) is the cycle of Lemma 4. Write
\[
V(H)=\{d_0,\ldots ,d_{2k}\},
\]
and write the support vertices cyclically as \(S_0,\ldots ,S_{2k}\), where \(e_{d_i}=S_iS_{i+1}\). Membership alternation gives
\[
S_i=\{d_{i+1},d_{i+3},\ldots ,d_{i+2k-1}\},
\]
with indices modulo \(2k+1\).

If two consecutive selected covers have an order disagreement, Proposition 8 has its analogue immediately. Hence suppose consecutive selected covers are compatible. Their common support orders agree, so each \(S_i\) has a Hamilton order \(P_i\) used by both incident deletion covers.

## 6.1 Consecutive double deletions

For each \(i\), let \(T_i\) be any two-cover of
\[
H-\{d_i,d_{i+1}\},
\]
which exists by minimality. Put
\[
K_i=S_i-\{d_{i+1}\}=S_{i+2}-\{d_i\}.
\]

**Lemma 9.** For some \(i\), either \(T_i\) has an edge joining two distinct nonempty path pieces obtained by deleting an internal exchanged label from one of the incident selected covers, or the two inherited covers of the double deletion have an order disagreement.

**Proof.** Suppose neither event occurs for any \(i\). Then each exchanged label is an endpoint of the relevant support path, and deleting \(d_i,d_{i+1}\) leaves the same ordered supports \(K_i,S_{i+1}\). Let \(\varepsilon_i\in\{L,R\}\) denote the end of \(K_i\) at which \(d_{i+1}\) is restored to obtain \(P_i\), equivalently the end at which \(d_i\) is restored to obtain \(P_{i+2}\).

If \(\varepsilon_{i+2}=\varepsilon_i\), the two successive restorations at that end force the next removed label to equal the preceding one, contradicting the distinctness of the cycle labels. Hence
\[
\varepsilon_{i+2}\ne\varepsilon_i
\]
for every \(i\). Addition by \(2\) is one cycle modulo \(2k+1\). Following it around the odd number of indices reverses the end an odd number of times and returns to the starting index with the opposite value, a contradiction. \(\square\)

## 6.2 Rank transport

For consecutive compatible covers,
\[
S_i\cap S_{i+2}=S_i-\{d_{i+1}\}=S_{i+2}-\{d_i\}.
\]
Lemma 3 shows that \(P_i\) and \(P_{i+2}\) arise from a common order by inserting \(d_{i+1}\) and \(d_i\) in equal or adjacent slots. An adjacent-slot transition supplies a tight triple reversing the two inserted labels across the intervening common vertex.

**Lemma 10.** At least \(k-1\) of the \(2k+1\) step-two transitions use adjacent slots. Their number is congruent to \(k-1\pmod 2\), and every adjacent transposition of consecutive ranks \(1,\ldots ,k\) occurs at least once.

**Proof.** Follow the \(k\) positions of the support order while replacing \(d_{i+1}\) by \(d_i\) and advancing from \(S_i\) to \(S_{i+2}\). An equal-slot transition preserves the rank positions; an adjacent-slot transition applies one simple adjacent transposition. After one circuit, the deterministic replacement of labels induces a \(k\)-cycle on the rank positions. A factorization of a \(k\)-cycle into adjacent transpositions uses every simple generator and has at least \(k-1\) factors. Its parity is \(k-1\), giving the congruence. \(\square\)

Thus the odd cycle contains linearly many explicitly located reversals. Their existence is not the remaining difficulty.

## 6.3 Incidence identities

Let \(C\) be the ordinary cycle on ground vertices \(d_0,\ldots ,d_{2k}\), with edge \(\{d_{i-1},d_i\}\). The support identities are
\[
\mathbf 1_{S_i}+\mathbf 1_{S_{i+1}}=\mathbf 1_V-\mathbf 1_{\{d_i\}},
\qquad
\sum_i\mathbf 1_{S_i}=k\mathbf 1_V.
\]

Let \(T\) be the support of a tight path that is a vertex cover of \(C\), and write \(|T|=k+r\). Define
\[
I(T)=\{i:d_{i-1},d_i\in T\}.
\]

**Lemma 11.** One has
\[
|I(T)|=2r-1,\qquad
\mathbf 1_T+\sum_{i\in I(T)}\mathbf 1_{S_i}=r\mathbf 1_V.
\]

**Proof.** Put \(t_i=\mathbf 1_T(d_i)\) and \(a_i=t_{i-1}+t_i\). Since \(T\) covers every edge of \(C\), \(a_i\in\{1,2\}\), and \(a_i-1\) is the indicator of \(I(T)\). Then
\[
\sum_i a_i\mathbf 1_{S_i}
 =\sum_j t_j(\mathbf 1_{S_j}+\mathbf 1_{S_{j+1}})
 =|T|\mathbf 1_V-\mathbf 1_T.
\]
Subtracting \(\sum_i\mathbf 1_{S_i}=k\mathbf 1_V\) gives the second identity. Summing the \(a_i\) gives
\[
2|T|=(2k+1)+|I(T)|,
\]
which gives the first. \(\square\)

If \(r=1\), Lemma 11 says that \(T\) and one selected support \(S_i\) are disjoint and cover \(V(H)\). Therefore a Hamiltonian vertex cover of the ground cycle of order \(k+1\) gives a two-cover of \(H\).

## Odd cycle forces bounded support


### The spanning odd cycle immediately yields bounded support

**Lemma 12 (odd-cycle bounded-support reduction).** Assume the selected support graph is the spanning odd cycle
\[
S_0S_1\cdots S_{2k}S_0,
\]
with edge \(S_iS_{i+1}\) labeled \(d_i\). Then either \(H\) has a two-cover, or \(H\) contains a Hamiltonian four-support \(K\) with
\[
\operatorname{pc}(H-K)=2.
\]

**Proof.** Fix \(i\). The selected deletion cover at \(d_i\) is
\[
H-d_i=S_i\mid S_{i+1}.
\]
Choose displayed Hamilton orders
\[
P_i=(s_1,\ldots,s_k),
\qquad
P_{i+1}=(t_1,\ldots,t_k)
\]
on these two supports.

Neither \(S_i\cup\{d_i\}\) nor \(S_{i+1}\cup\{d_i\}\) is Hamiltonian. Indeed, a Hamilton path on the first set together with \(P_{i+1}\), or a Hamilton path on the second together with \(P_i\), would give a spanning two-cover of \(H\).

Hence \(d_i\) cannot be prepended to either displayed path. Therefore
\[
(d_i,s_1,s_2),
\qquad
(d_i,t_1,t_2)
\]
are non-tight. Boundary antisymmetry gives
\[
(s_2,s_1,d_i),
\qquad
(t_2,t_1,d_i)
\]
tight.

Thus the single exterior vertex \(d_i\) reverses the initial edges of the two vertex-disjoint tight paths \(P_i\) and \(P_{i+1}\). Exactly one of
\[
(s_1,d_i,t_1),
\qquad
(t_1,d_i,s_1)
\]
is tight. In the first case
\[
(s_2,s_1,d_i,t_1)
\]
is a Hamiltonian four-path; in the second
\[
(t_2,t_1,d_i,s_1)
\]
is a Hamiltonian four-path. Hence a Hamiltonian four-support \(K\) exists.

Since \(K\) is proper in a minimum counterexample, minimum-counterexample calculus gives
\[
\operatorname{pc}(H-K)\le2.
\]
Its complement cannot be Hamiltonian, or a Hamilton path on \(H-K\) together with a Hamilton path on \(K\) would two-cover \(H\). Thus
\[
\operatorname{pc}(H-K)=2.
\]
\(\square\)

The crucial point is that the common-reverser argument uses **one deleted label and two disjoint displayed end edges**. Two different deleted labels reversing one common edge do not suffice.

Therefore the spanning odd cycle is not an independent terminal support-graph geometry. At arbitrary order it immediately returns to the bounded-support/maximal-support route. Combined with the forest analysis, the selected support graph has no quiet global residue outside the bounded-support and reversal/disturbance interfaces.


## Metadata

- ID: deletion_covers_and_the_support_graph_the_odd_cycle_case
- Kind: section
- Version: 4
- Math version: 3
- Audit: unaudited
- Refutation: unrefuted
- Composition version: 1
- Composition stale: False
- Subsections existing when composed: 5
- Subsections now: 5

## Development tree

- [Subsection 1 — (untitled)](../SUBSECTIONS/deletion_covers_and_the_support_graph_the_odd_cycle_case_subsection_a.md) (`deletion_covers_and_the_support_graph_the_odd_cycle_case_subsection_a`; development v1; composition v1; stale=False)
- [Subsection 2 — 6.1 Consecutive double deletions](../SUBSECTIONS/deletion_covers_and_the_support_graph_the_odd_cycle_case_subsection_b.md) (`deletion_covers_and_the_support_graph_the_odd_cycle_case_subsection_b`; development v1; composition v1; stale=False)
- [Subsection 3 — 6.2 Rank transport](../SUBSECTIONS/deletion_covers_and_the_support_graph_the_odd_cycle_case_subsection_c.md) (`deletion_covers_and_the_support_graph_the_odd_cycle_case_subsection_c`; development v1; composition v1; stale=False)
- [Subsection 4 — 6.3 Incidence identities](../SUBSECTIONS/deletion_covers_and_the_support_graph_the_odd_cycle_case_subsection_d.md) (`deletion_covers_and_the_support_graph_the_odd_cycle_case_subsection_d`; development v2; composition v1; stale=False)
- [Subsection 5 — Odd cycle forces bounded support](../SUBSECTIONS/deletion_covers_and_the_support_graph_the_odd_cycle_case_subsection_e.md) (`deletion_covers_and_the_support_graph_the_odd_cycle_case_subsection_e`; development v3; composition vNone; stale=False)
