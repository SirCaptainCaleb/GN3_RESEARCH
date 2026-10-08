# Deletion-critical complements force second-layer junction forks — preserved pre-item development

## Development

## A \(\kappa_2=2\) maximal-support complement is endpoint-deletion-critical and forces second-layer junction forks

Let \(H\) satisfy
\[
\kappa_2(H)=2,
\]
and let \(S\subsetneq V(H)\) be any Hamiltonian support such that
\[
H-S=P\mid Q
\]
is a two-cover. Write
\[
P=(p_1,\ldots,p_m),\qquad Q=(q_1,\ldots,q_t).
\]

Then the complement
\[
G=H-S
\]
has Hamiltonian deletion distance at least two.

Indeed, if \(G-v\) were Hamiltonian for some \(v\in V(G)\), then a Hamilton path on \(S\) together with one on \(G-v\) would two-cover
\[
H-v,
\]
contradicting \(\kappa_2(H)=2\). Hence
\[
\boxed{G-v\text{ is non-Hamiltonian for every }v\in V(G).}
\]

Assume \(m,t\ge3\). Deleting an exposed endpoint now gives genuine one-step inward information.

### Terminal \(P\)-fork

Delete \(p_m\). The inherited paths
\[
P^-=(p_1,\ldots,p_{m-1}),\qquad Q
\]
cover \(G-p_m\), but their union is non-Hamiltonian. Therefore the displayed concatenation
\[
(p_1,\ldots,p_{m-1},q_1,\ldots,q_t)
\]
cannot have both junction triples tight. Thus at least one of
\[
h(p_{m-2},p_{m-1},q_1),\qquad
h(p_{m-1},q_1,q_2)
\]
is zero. Boundary antisymmetry gives
\[
\boxed{
h(q_1,p_{m-1},p_{m-2})=1
\quad\text{or}\quad
h(q_2,q_1,p_{m-1})=1.
}
\]

So either the exposed endpoint \(q_1\) reverses the next edge inward on \(P\), or the new exposed endpoint \(p_{m-1}\) reverses the initial edge of \(Q\).

### Initial \(Q\)-fork

Delete \(q_1\). The same argument applied to
\[
P\mid(q_2,\ldots,q_t)
\]
gives
\[
\boxed{
h(q_2,p_m,p_{m-1})=1
\quad\text{or}\quad
h(q_3,q_2,p_m)=1.
}
\]

Thus either the new endpoint \(q_2\) reverses the terminal edge of \(P\), or the exposed endpoint \(p_m\) reverses the next edge inward on \(Q\).

The opposite two boundary corners are obtained symmetrically by deleting \(p_1\) and \(q_t\).

Hence every admissible Hamiltonian support in a genuine \(\kappa_2=2\) state carries four audit-safe second-layer reversal forks in its two-coverable complement.

This is the correct replacement for the withdrawn cyclic-rotation propagation claims. No cyclic permutation of a triple is used: every new reversal is the literal boundary flip of a failed junction in a one-vertex deletion of the complement.

### Maximal-support consequence

If \(S\) is maximal among Hamiltonian supports with two-coverable complement, each exposed endpoint of \(P\mid Q\) already reverses both displayed end edges of \(S\). Therefore whenever the first alternative in one of the forks occurs, the same exposed endpoint reverses two vertex-disjoint same-type edges: one in \(S\) and one one layer inside the opposite complementary path. The valid common-reverser lemma then yields a transversal Hamiltonian four-support.

The remaining fork alternative transfers the reversal carrier to the newly exposed second-layer vertex. Thus the maximal-support obstruction has a finite one-layer carrier-switch structure rather than an unconstrained inward propagation.
