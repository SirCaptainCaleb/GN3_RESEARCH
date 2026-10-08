# Reseeding forces the maximal support to dominate the complement — preserved pre-item development

## Reseeding forces the maximal support to dominate the complement

Let
\[
S\mid P\mid Q
\]
be a global maximal-support normalization in a no-two-cover boundary tournament \(H\), where
\[
|S|=k,\qquad |P|=m,\qquad |Q|=t.
\]
Thus \(S\) has maximum cardinality among all proper Hamiltonian supports whose complement is two-coverable.

Let \(K\) be any Hamiltonian four-support such that
\[
\operatorname{pc}(H-K)\le2.
\]
Since \(H\) itself has no two-cover, \(H-K\) is not Hamiltonian. Hence write
\[
H-K=A\mid B
\]
with both \(A,B\) Hamiltonian and nonempty.

Now \(A\) is itself an admissible Hamiltonian support in \(H\): its complement is
\[
H-A=B\mid K,
\]
a two-cover. By maximality of \(S\),
\[
|A|\le k.
\]
Likewise
\[
|B|\le k.
\]
Therefore
\[
|V(H)|-4
=
|A|+|B|
\le2k.
\]
Since
\[
|V(H)|=k+m+t,
\]
we obtain
\[
\boxed{m+t\le k+4.}
\]

Thus:

> **Reseed size bound.** Any admissible seam four-support can occur only when the displayed complementary two-cover has total order at most four more than the maximal support.

Equivalently, if
\[
m+t>k+4,
\]
then every Hamiltonian seam four-support \(K\) supplied by the deletion-critical seam theorem necessarily lies in the descent branch
\[
\operatorname{pc}(H-K)\ge3.
\]

This applies to transversal seam supports and to the explicit pure cross-seam supports.

### Consequence for opposite pure seams

If both oriented seams are pure and
\[
m+t>k+4,
\]
then neither seam can reseed in the original graph. The first seam therefore descends by four vertices. The opposite disjoint seam survives that descent when \(m,t\ge5\), giving the second descent/reseed fork of [[opposite_pure_seams_give_two_step_reseeding_or_eight_vertex_descent]].

Hence the only way a seam avoids forced hereditary descent in a complement-heavy maximal-support state is for the maximal support to satisfy the sharp majority-type bound
\[
k\ge m+t-4.
\]

No minimum-counterexample induction is used; only global maximality of \(S\) among admissible Hamiltonian supports.
