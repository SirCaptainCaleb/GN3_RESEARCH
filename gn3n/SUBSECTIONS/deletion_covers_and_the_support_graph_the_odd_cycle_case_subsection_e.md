# Odd cycle forces bounded support

## Metadata

- ID: deletion_covers_and_the_support_graph_the_odd_cycle_case_subsection_e
- Parent Section: deletion_covers_and_the_support_graph_the_odd_cycle_case
- Position: 5
- Row version: 3
- Development version: 3
- Composition version: None
- Composition stale: False

## Cold composition

(none yet)

## Development


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
