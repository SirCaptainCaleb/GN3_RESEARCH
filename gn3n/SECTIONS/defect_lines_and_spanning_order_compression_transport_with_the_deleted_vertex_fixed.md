# Transport with the deleted vertex fixed

## Body

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

## Metadata

- ID: defect_lines_and_spanning_order_compression_transport_with_the_deleted_vertex_fixed
- Kind: section
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted

## Authoring state

- Subsection 1 — HOT, version 1: (untitled)
