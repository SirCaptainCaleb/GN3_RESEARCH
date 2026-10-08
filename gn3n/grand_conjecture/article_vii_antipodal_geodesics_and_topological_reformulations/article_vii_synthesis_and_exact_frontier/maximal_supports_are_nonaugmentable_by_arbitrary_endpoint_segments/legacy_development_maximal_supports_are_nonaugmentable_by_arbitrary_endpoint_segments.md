# Maximal supports are nonaugmentable by arbitrary endpoint segments — preserved pre-item development

## Composition

(none yet)

## Development

## Maximal supports are nonaugmentable by arbitrary endpoint segments

Let
\[
S\subsetneq V(H)
\]
be Hamiltonian and maximal among Hamiltonian supports whose complement is two-coverable. Fix
\[
H-S=P\mid Q,
\]
with displayed tight paths
\[
P=(p_1,\ldots,p_m),\qquad Q=(q_1,\ldots,q_t).
\]

Choose integers
\[
a,b,c,d\ge0,\qquad a+b\le m,\qquad c+d\le t,
\]
and let \(E\) consist of the first \(a\) and last \(b\) vertices of \(P\), together with the first \(c\) and last \(d\) vertices of \(Q\). Assume \(E\ne\varnothing\).

Deleting \(E\) from the displayed complementary paths leaves at most two contiguous inherited intervals,
\[
(p_{a+1},\ldots,p_{m-b})
\quad\text{and}\quad
(q_{c+1},\ldots,q_{t-d}),
\]
with empty intervals omitted. Hence
\[
\operatorname{pc}\bigl(H-(S\cup E)\bigr)\le2.
\]

If \(H[S\cup E]\) were Hamiltonian and \(S\cup E\ne V(H)\), then \(S\cup E\) would be a larger admissible Hamiltonian support, contradicting maximality of \(S\). If \(S\cup E=V(H)\), its Hamiltonicity would itself give a spanning Hamilton path and hence a two-cover. Therefore
\[
\boxed{H[S\cup E]\text{ is non-Hamiltonian}}
\]
for every nonempty union \(E\) of endpoint segments of the displayed complementary paths.

This strictly strengthens exposed-endpoint absolute nonaugmentability.

### Seam consequence

In the pure cross-seam branch of the deletion-critical seam theorem,
\[
K_{PQ}=\{p_{m-1},p_m,q_1,q_2\}
\]
is Hamiltonian. Nevertheless maximality forces each of
\[
S\cup\{p_{m-1},p_m\},\qquad
S\cup\{q_1,q_2\},\qquad
S\cup K_{PQ}
\]
to be non-Hamiltonian.

The mirror seam block
\[
K_{QP}=\{q_{t-1},q_t,p_1,p_2\}
\]
satisfies the analogous three nonaugmentability conclusions.

Thus every explicit seam four-support is a Hamiltonian packet that is globally incompatible with adjoining either of its two rail pairs, or the whole packet, to the maximal support. Any successful seam conversion must therefore change the inherited order of \(S\), change the displayed complementary decomposition, or pass through a different admissible seed; simple endpoint-segment absorption is completely excluded.
