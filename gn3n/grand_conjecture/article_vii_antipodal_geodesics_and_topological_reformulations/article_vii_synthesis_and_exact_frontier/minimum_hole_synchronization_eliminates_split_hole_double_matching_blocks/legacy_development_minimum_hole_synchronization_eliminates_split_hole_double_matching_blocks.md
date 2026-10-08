# Minimum-hole synchronization eliminates split-hole double matching blocks — preserved pre-item development

## Composition

(none yet)

## Development

## Split-hole double matching blocks are impossible under minimum-hole synchronization

First record a four-vertex closure fact.

**Lemma.** Let \(\{a,b,c,d\}\) induce a non-Hamiltonian boundary tournament. If
\[
h(a,b,c)=1,
\]
then
\[
\boxed{h(c,d,a)=1.}
\]

**Proof.** Suppose instead \(h(c,d,a)=0\). Boundary antisymmetry gives
\[
h(a,d,c)=1.
\]
Exactly one of
\[
h(b,c,d),\qquad h(d,c,b)
\]
is tight. In the first case
\[
(a,b,c,d)
\]
is a Hamiltonian four-path. In the second case
\[
(a,d,c,b)
\]
is a Hamiltonian four-path. Both contradict non-Hamiltonicity. \(\square\)

Now retain the hard seam equality packet
\[
W=\{x,y,q_2,q_1,p_m,p_{m-1}\}
\]
from [[hard_seam_equality_packets_reduce_to_split_hole_double_matching_blocks]], and assume the first split-hole matching pattern
\[
\{x,q_1\},\qquad \{y,p_m\}.
\]
Because these are the two matching edges of the good two-deletion graph, every cross pair is a nonedge. In particular the following three four-sets are non-Hamiltonian:
\[
W-\{q_1,y\}=\{x,p_m,p_{m-1},q_2\},
\]
\[
W-\{q_1,p_m\}=\{x,y,p_{m-1},q_2\},
\]
\[
W-\{x,p_m\}=\{y,q_1,p_{m-1},q_2\}.
\]

Minimum-hole synchronization gives
\[
h(x,p_m,p_{m-1})=1
\]
at the terminal end of \(P\). Apply the lemma to the first non-Hamiltonian four-set with
\[
(a,b,c,d)=(x,p_m,p_{m-1},q_2).
\]
It forces
\[
\boxed{h(p_{m-1},q_2,x)=1.}
\]

At the initial end of \(Q\), synchronization gives
\[
h(q_2,q_1,y)=1.
\]
Apply the lemma to the third non-Hamiltonian four-set with
\[
(a,b,c,d)=(q_2,q_1,y,p_{m-1}).
\]
It forces
\[
\boxed{h(y,p_{m-1},q_2)=1.}
\]

Therefore
\[
(y,p_{m-1},q_2,x)
\]
is a tight Hamiltonian four-path on
\[
\{x,y,p_{m-1},q_2\}
=
W-\{q_1,p_m\},
\]
contradicting the asserted non-Hamiltonicity of the middle cross-pair deletion.

The other split matching
\[
\{x,p_m\},\qquad \{y,q_1\}
\]
is identical after exchanging \(x\) and \(y\).

Hence:

> **No split-hole residue.** The split-hole double-matching normal forms isolated in [[hard_seam_equality_packets_reduce_to_split_hole_double_matching_blocks]] cannot occur in a genuine minimum-pair seam, because minimum-hole four-end synchronization forces one of their required bad four-deletions to be Hamiltonian.

Consequently the hard seam equality branch has no new static residue. Every such seam instead yields one of the previously established outputs: adjacent overlapping Hamiltonian supports, the explicit cross-seam rail four-support, or an admissible inner five-/six-seed.
