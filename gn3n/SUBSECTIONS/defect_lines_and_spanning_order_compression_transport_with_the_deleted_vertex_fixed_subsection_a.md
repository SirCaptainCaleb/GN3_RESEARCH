# defect_lines_and_spanning_order_compression_transport_with_the_deleted_vertex_fixed_subsection_a

## Metadata

- ID: defect_lines_and_spanning_order_compression_transport_with_the_deleted_vertex_fixed_subsection_a
- Parent Section: defect_lines_and_spanning_order_compression_transport_with_the_deleted_vertex_fixed
- Position: 1
- Row version: 2
- Development version: 2
- Composition version: None
- Composition stale: True

## Cold composition

(none yet)

## Development

Assume the middle join is tight. Write
\[
H-x=P\mid Q.
\]
Move the last vertex of \(P\) across \(x\) toward \(Q\). If all new consecutive triples are tight, this produces another deletion cover of the same \(H-x\), with component orders \((|P|-1,|Q|+1)\). At the first failed move, the failed triple reverses and combines with the inherited neighboring triples to give a Hamiltonian four-set whose complement is covered by the remaining prefix and suffix.

**Lemma 3.** Repeating this move in one direction terminates with either
1. a deletion cover of the same \(H-x\) having one path of order \(3\); or
2. a Hamiltonian four-set whose complement has a two-cover.

**Proof.** Every successful move decreases the chosen component order by one and preserves \(x\). The move can therefore succeed at most until that component has order \(3\). If it fails earlier, the preceding paragraph gives (2). \(\square\)

The three-vertex-side case contains a stronger transport.

Let
\[
P=(p_0,p_1,p_2),\qquad Q=(q_0,\ldots ,q_s),\qquad
X=V(P)\cup\{x\}.
\]

**Lemma 4.** Suppose \(s\ge6\). Then at least two vertices \(z\in X\) have all six tight triples
\[
(q_1,q_0,z),\ (q_2,q_1,z),\ (q_3,q_2,z),
\]
\[
(z,q_s,q_{s-1}),\ (z,q_{s-1},q_{s-2}),\ (z,q_{s-2},q_{s-3}).
\]
For either such \(z\), there is a sequence of pairwise repartitions in which \(z\) is retained while a two-coverable complementary support is transported from the left end of \(Q\) to the right end.

**Proof.** The set \(X\) is non-Hamiltonian, since otherwise \(X\mid Q\) would two-cover \(H\). The sets \(X\cup\{q_0\}\) and \(X\cup\{q_s\}\) are also non-Hamiltonian, because their complements are inherited tight paths.

Consider \(X\cup\{q_0,q_s\}\). Its two deletions by \(q_0,q_s\) are non-Hamiltonian. The remaining four vertex deletions are Hamiltonian; otherwise the six-vertex Hamiltonian-deletion count would be violated. Hence, for every \(z\in X\),
\[
(X-\{z\})\cup\{q_0,q_s\}
\]
is Hamiltonian. Its complement
\[
\{z,q_1,\ldots ,q_{s-1}\}
\]
cannot be Hamiltonian, so \(z\) cannot be inserted at either end of the inherited path \((q_1,\ldots ,q_{s-1})\). Boundary reversal gives
\[
(q_2,q_1,z),\qquad(z,q_{s-1},q_{s-2}).
\]

Apply the same argument to the six-sets \(X\cup\{q_0,q_1\}\) and \(X\cup\{q_{s-1},q_s\}\). At least three choices of \(z\in X\) work on each side, so at least two choices work on both sides. Their complementary non-Hamiltonian paths give the four additional tight triples displayed above.

For transport, use the four seven-vertex sets
\[
X\cup\{q_0,q_1,q_2\},\
X\cup\{q_0,q_1,q_s\},\
X\cup\{q_0,q_{s-1},q_s\},\
X\cup\{q_{s-2},q_{s-1},q_s\}.
\]
For one such set \(W\), join \(a,b\in W\) when \(W-\{a,b\}\) is Hamiltonian. Each vertex has at least four neighbors, since deleting it leaves a six-set with at least four Hamiltonian five-vertex deletions. Consecutive graphs share six vertices; after removing the unique outside vertex each leaves at least eight edges on the common six-set, so the two edge sets intersect because \(8+8>15\). If \(z\) is one of the two vertices found above, it has at least three neighbors in each common five-vertex neighborhood, so the shared edge can be chosen incident with \(z\).

Every such edge \(ab\) yields a Hamiltonian five-set and a complementary support equal to an inherited interval of \(Q\) together with \(\{a,b\}\). The complement is non-Hamiltonian but is covered by that interval and the two-vertex path \((a,b)\). Following the shared edges gives the required sequence. \(\square\)

### The three-vertex-side terminal state strictly descends

Retain Lemma 4:
\[
P=(p_0,p_1,p_2),\qquad
Q=(q_0,\ldots,q_s),\qquad
X=V(P)\cup\{x\},
\]
with \(s\ge6\). Lemma 4 supplies distinct vertices
\[
z_1,z_2\in X
\]
such that, for \(i=1,2\),
\[
(q_1,q_0,z_i),\qquad
(z_i,q_s,q_{s-1})
\]
are tight.

Then the singleton-lift three-cover
\[
P\mid\{x\}\mid Q
\]
admits a strict decrease of
\[
\Phi=|P_1|^2+|P_2|^2+|P_3|^2
\]
inside its pairwise-repartition component.

**Proof.** For each \(z=z_i\), exactly one of
\[
(q_0,z,q_s),\qquad(q_s,z,q_0)
\]
is tight.

Suppose first that
\[
(q_0,z,q_s)
\]
is tight for at least one carrier \(z\). Then
\[
F_z=(q_1,q_0,z,q_s,q_{s-1})
\]
is a Hamiltonian five-path.

The set \(X-\{z\}\) has order three and is therefore Hamiltonian. The remaining vertices of \(Q\) form the inherited tight path
\[
(q_2,\ldots,q_{s-2}),
\]
with the empty short-interval conventions unnecessary because \(s\ge6\).

Starting from
\[
P\mid\{x\}\mid Q,
\]
first repartition \(P\mid\{x\}\) as
\[
(X-\{z\})\mid\{z\}.
\]
Then repartition
\[
\{z\}\mid Q
\]
as
\[
F_z\mid(q_2,\ldots,q_{s-2}).
\]
Thus the original profile
\[
3\mid1\mid(s+1)
\]
reaches
\[
3\mid5\mid(s-3)
\]
in the same pairwise-repartition component. The potential change is
\[
\Delta\Phi
=
3^2+5^2+(s-3)^2
-
\bigl(3^2+1^2+(s+1)^2\bigr)
=
32-8s<0.
\]

It remains that
\[
(q_s,z_i,q_0)
\]
is tight for both \(i=1,2\). Then \(z_1,z_2\) are parallel middle vertices between \(q_s\) and \(q_0\). The parallel-middle lemma gives a Hamiltonian four-support
\[
K=\{q_s,q_0,z_1,z_2\}.
\]

The two-set \(X-\{z_1,z_2\}\) is a tight path, and the remaining vertices of \(Q\) form the inherited tight path
\[
(q_1,\ldots,q_{s-1}).
\]
First repartition
\[
P\mid\{x\}
\]
as
\[
(X-\{z_1,z_2\})\mid\{z_1,z_2\},
\]
then repartition
\[
\{z_1,z_2\}\mid Q
\]
as
\[
K\mid(q_1,\ldots,q_{s-1}).
\]
This reaches profile
\[
2\mid4\mid(s-1)
\]
with
\[
\Delta\Phi
=
2^2+4^2+(s-1)^2
-
\bigl(3^2+1^2+(s+1)^2\bigr)
=
10-4s<0.
\]

Thus every three-vertex-side terminal state of the fixed-root transport has a strict \(\Phi\)-decrease in the same repartition component. \(\square\)

Consequently the elaborate seven-set transport at the end of Lemma 4 is not needed merely to prove progress from the \(3\)-vs-long state. The two simultaneous end-reversal carriers already force strict descent by a two-step pairwise repartition.
