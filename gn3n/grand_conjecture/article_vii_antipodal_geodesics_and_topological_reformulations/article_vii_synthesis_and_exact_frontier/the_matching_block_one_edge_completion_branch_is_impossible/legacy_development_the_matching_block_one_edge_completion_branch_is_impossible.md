# The matching-block one-edge completion branch is impossible — preserved pre-item development

## Composition

(none yet)

## Development

## The matching-block six-shadow cannot complete to one edge order

Let
\[
U=C\cup\{a,b\},\qquad C=C_+\sqcup C_-,
\]
be the canonical matching-block six-set, with
\[
C_+=\{y_1,y_2\},\qquad C_-=\{z_1,z_2\}.
\]
Assume
\[
H[C\cup\{a\}],\qquad H[C\cup\{b\}]
\]
are non-Hamiltonian. The matching-block hooks give, for every \(y\in C_+\), \(z\in C_-\),
\[
ay<yz<az,\qquad bz<yz<by
\]
in any edge order representing the corresponding comparisons.

We first record a general five-vertex observation.

**Sandwich lemma.** Let \(L=\{p,q\}\), \(R=\{r,s\}\), and \(w\) be a fifth vertex in an edge-ordered complete graph. Suppose
\[
wx<xy<wy\qquad(x\in L,\ y\in R).
\]
If the induced five-set \(L\cup R\cup\{w\}\) has no monotone Hamilton path, then
\[
rs<pq.
\]

**Proof.** Relabel \(p,q\) so that \(wp<wq\), and relabel \(r,s\) so that \(wr<ws\).

If \(pq<pr\), then
\[
(q,p,r,w,s)
\]
is monotone because
\[
pq<pr<wr<ws.
\]
Likewise, if \(pq<qr\), then
\[
(p,q,r,w,s)
\]
is monotone. Hence non-Hamiltonicity forces
\[
pr<pq,\qquad qr<pq.
\]

If \(qr<rs\), then
\[
(p,w,q,r,s)
\]
is monotone because
\[
wp<wq<qr<rs.
\]
If \(qs<rs\), then
\[
(p,w,q,s,r)
\]
is monotone. Hence non-Hamiltonicity forces
\[
rs<qr,\qquad rs<qs.
\]
Combining \(rs<qr<pq\) gives \(rs<pq\). \(\square\)

Now suppose, toward contradiction, that the full comparison digraph of \(U\) is acyclic, so one edge order represents all of \(H[U]\).

Apply the sandwich lemma to the bad five-set \(C+a\), with
\[
L=C_+,\qquad R=C_-.
\]
The relations \(ay<yz<az\) give
\[
z_1z_2<y_1y_2.
\]

Apply the same lemma to the bad five-set \(C+b\), now with
\[
L=C_-,\qquad R=C_+,
\]
using \(bz<yz<by\). This gives
\[
y_1y_2<z_1z_2,
\]
a contradiction.

Therefore:

> **No-completion theorem.** The canonical matching-block six-shadow is never fully edge-orderable when both overlapping five-sets \(C+a\) and \(C+b\) are non-Hamiltonian.

Combined with [[the_matching_block_six_set_is_edge_orderable_after_deleting_one_shadow_edge]] and [[one_edge_completion_failure_forces_a_hamiltonian_support_of_order_four_to_six]], the missing shadow edge \(ab\) must create a comparison cycle, and that first completion obstruction exposes a Hamiltonian support
\[
R,\qquad \{a,b\}\subseteq R\subseteq U,\qquad 4\le |R|\le6.
\]

Thus the active one-edge-completion branch is eliminated: the matching-block equality residue always returns to the bounded Hamiltonian-support handoff.
