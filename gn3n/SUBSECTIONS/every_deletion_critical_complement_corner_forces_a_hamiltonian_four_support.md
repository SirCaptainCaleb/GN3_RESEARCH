# Every deletion-critical oriented seam forces a Hamiltonian four-support

## Metadata

- ID: every_deletion_critical_complement_corner_forces_a_hamiltonian_four_support
- Parent Section: article_vii_synthesis_and_exact_frontier
- Position: 107
- Row version: 2
- Development version: 2
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Every deletion-critical oriented seam forces a Hamiltonian four-support

Retain the saturated state of [[both_hole_seed_maximalization_yields_a_saturated_deletion_critical_complement]]:
\[
S=(s_1,\ldots,s_k),\qquad
H-S=P\mid Q,
\]
with
\[
P=(p_1,\ldots,p_m),\qquad Q=(q_1,\ldots,q_t),
\]
and assume \(k,m,t\ge3\).

Consider first the oriented seam from the terminal end of \(P\) to the initial end of \(Q\).

Deletion-criticality of the complement gives the two forks
\[
h(q_1,p_{m-1},p_{m-2})=1
\quad\text{or}\quad
h(q_2,q_1,p_{m-1})=1, \tag{F1}
\]
and
\[
h(q_2,p_m,p_{m-1})=1
\quad\text{or}\quad
h(q_3,q_2,p_m)=1. \tag{F2}
\]

Maximal-support endpoint saturation also gives
\[
h(q_1,s_k,s_{k-1})=1,
\qquad
h(s_2,s_1,p_m)=1.
\]

If the first alternative of (F1) holds, the same carrier \(q_1\) reverses two vertex-disjoint terminal edges, one in \(P\) and one in \(S\). The valid terminal-terminal common-reverser lemma gives a Hamiltonian four-support meeting \(S,P,Q\).

If the second alternative of (F2) holds, the same carrier \(p_m\) reverses two vertex-disjoint initial edges, one in \(S\) and one in \(Q\). The valid initial-initial common-reverser lemma again gives a Hamiltonian four-support meeting \(S,P,Q\).

The only way to avoid these transversal outputs is therefore
\[
h(q_2,q_1,p_{m-1})=1,
\qquad
h(q_2,p_m,p_{m-1})=1.
\]
Thus \(q_1\) and \(p_m\) are parallel middle vertices between the fixed ordered pair
\[
(q_2,p_{m-1}).
\]
By the parallel-middle lemma, at least one of
\[
(q_2,q_1,p_{m-1},p_m),
\qquad
(q_2,p_m,p_{m-1},q_1)
\]
is a tight Hamiltonian four-path. Hence
\[
\boxed{\{p_{m-1},p_m,q_1,q_2\}}
\]
is Hamiltonian.

Therefore the oriented seam \(P\to Q\) has the dichotomy:

> either a transversal Hamiltonian four-support meets \(S,P,Q\), or the four adjacent rail vertices
> \[
> \{p_{m-1},p_m,q_1,q_2\}
> \]
> form a Hamiltonian support.

Applying the same argument to the opposite displayed concatenation \(Q\to P\) gives the mirror dichotomy at the terminal-\(Q\)/initial-\(P\) seam:
either a transversal Hamiltonian four-support occurs, or
\[
\boxed{\{q_{t-1},q_t,p_1,p_2\}}
\]
is Hamiltonian.

These are the two oriented seams furnished by the displayed path orders. No initial-initial or terminal-terminal seam is asserted, because reversing a displayed tight path is not valid in general.

No cyclic rotation, path reversal, or recursive propagation is used. The inputs are exactly:
- the one-vertex deletion-critical junction forks;
- exposed-endpoint reversal of the maximal support;
- the valid same-type common-reverser lemma;
- the parallel-middle lemma.

Thus the second-layer fork state collapses at each of the two legitimate oriented seams to a deterministic bounded four-support certificate.
