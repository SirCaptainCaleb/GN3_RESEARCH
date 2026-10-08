# The maximal-support seed lies in the central six witness band — preserved pre-item development

## Development

## The universal maximal-support seed lies inside the central six-label witness band

Retain a genuine minimum deletion pair
\[
X=\{x,y\},
\qquad
H-X=P\mid Q,
\]
with displayed orders
\[
P=(p_1,\ldots,p_s),\qquad Q=(q_1,\ldots,q_t).
\]

Use the corridor-facing terminal endpoints and put
\[
K=\{p_s,q_t,x,y\}.
\]

If \(K\) is Hamiltonian, then its complement is covered by
\[
(p_1,\ldots,p_{s-1})\mid(q_1,\ldots,q_{t-1}),
\]
so \(K\) is a Hamiltonian four-support with two-coverable complement.

If \(K\) is non-Hamiltonian, add \(p_{s-1}\) and let
\[
U=K\cup\{p_{s-1}\}.
\]
If \(U\) is Hamiltonian, its complement is covered by
\[
(p_1,\ldots,p_{s-2})\mid(q_1,\ldots,q_{t-1}).
\]
If \(U\) is non-Hamiltonian, Section 7 of [[smallset01]] says that \(K\) is its unique possible non-Hamiltonian four-subset. Therefore
\[
U-\{q_t\}
=
\{p_{s-1},p_s,x,y\}
\]
is Hamiltonian, and its complement is covered by
\[
(p_1,\ldots,p_{s-2})\mid Q.
\]

Thus in every case there is a Hamiltonian support
\[
S_0
\]
of order four or five with two-coverable complement and
\[
\boxed{
S_0\subseteq
\{p_{s-1},p_s,x,y,q_t,q_{t-1}\}.
}
\]

The right-hand mirror gives the same conclusion with \(q_{t-1}\) as the fifth candidate.

By [[minimum_hole_rebasing_collapses_the_unbounded_reflected_corridor_to_six_vertices]], this six-set is exactly the central label band supporting every positive witness in the minimum-hole concatenation of a genuine \(\kappa_2=2\) state.

Therefore:

> **Central-six support theorem.** The same six-label band which contains the complete positive-witness geometry of a genuine two-deletion state also contains a Hamiltonian four- or five-support whose complement is two-coverable.

This is the first direct identification of the combinatorial maximal-support seed with the bounded carrier-localization band. No long corridor labels are needed to produce the seed.

Consequently the two Article VII interfaces are no longer merely parallel reductions:
- the protected carrier loop is localized to at most six reservoir/exterior labels;
- the genuine two-deletion obstruction contains, inside its central six witness labels, a Hamiltonian seed for maximal-support normalization.

The remaining bridge can therefore be sought entirely through how this central-six Hamiltonian seed sits in the protected four-label middle face and its pair-locus relation.
