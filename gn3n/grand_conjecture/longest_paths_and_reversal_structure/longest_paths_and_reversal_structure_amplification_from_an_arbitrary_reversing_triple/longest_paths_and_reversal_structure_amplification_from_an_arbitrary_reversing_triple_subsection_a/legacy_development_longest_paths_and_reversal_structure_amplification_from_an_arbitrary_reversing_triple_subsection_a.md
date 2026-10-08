#  — preserved pre-item development

## Composition

(none yet)

## Development

Let \(T\) be the vertex set of a reversing tight triple, and let \(J_T\) be the graph on \(V(H)-T\) in which \(yz\) is an edge exactly when \(T\cup\{y,z\}\) is Hamiltonian.

**Lemma 8.**
\[
\alpha(J_T)\le2.
\]

**Proof.** A reversing tight triple is itself a tight three-vertex path. Apply the bad-extension-pair theorem from [[localextend01]] to this path and the exterior set \(V(H)-T\). The nonedges of \(J_T\) are exactly the bad extension pairs, and those form a triangle-free graph. Hence \(\alpha(J_T)\le2\). \(\square\)

Thus the complement of \(J_T\) is triangle-free, so Mantel's theorem gives
\[
|E(J_T)|
\ge
\binom{m}{2}-\left\lfloor\frac{m^2}{4}\right\rfloor,
\qquad m=|V(H)-T|.
\]
Every edge gives a Hamiltonian five-set containing the same reversal and having two-coverable complement. Hence some exterior vertex lies in several such edges, producing Hamiltonian five-sets with a common four-vertex core. The insertion-position analysis following Lemma 6 then gives a Hamiltonian four- or six-set, an order disagreement, or another positioned reversal.
