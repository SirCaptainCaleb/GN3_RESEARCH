# Support-pair rank is exactly two-cover deletion distance

## Composition

(none yet)

## Development

## Hamiltonian support-pair rank is exactly two-cover deletion distance

Let \(H\) be a boundary tournament on \(n\) vertices. Let \(\mathcal P(H)\) be the poset of ordered pairs
\[
(A,B)
\]
of disjoint Hamiltonian supports with \(|A|,|B|\ge2\), ordered by componentwise inclusion, as in [[hamiltonian_support_pairs_and_smith_chains_give_a_direct_closure_target]].

For
\[
(A,B)\in\mathcal P(H)
\]
define its support deficiency by
\[
\delta(A,B)=n-|A|-|B|.
\]

Assume the relevant minimum two-cover deletion leaves at least four vertices. In every no-two-cover state considered in Articles I--VII this normalization is automatic: a deletion two-cover has two nonempty components, and a singleton component can be paired with an endpoint moved from the other path, producing two Hamiltonian supports of order at least two without changing their union.

Then
\[
\boxed{
\kappa_2(H)
=
\min_{(A,B)\in\mathcal P(H)}\delta(A,B)
=
n-\max_{(A,B)\in\mathcal P(H)}(|A|+|B|).
}
\]

### Proof

If \((A,B)\in\mathcal P(H)\), put
\[
X=V(H)\setminus(A\cup B).
\]
Then
\[
H-X=A\mid B
\]
is a two-cover. Therefore
\[
\kappa_2(H)\le |X|=\delta(A,B).
\]
Taking the minimum over support pairs gives
\[
\kappa_2(H)\le \min\delta.
\]

Conversely choose a minimum deletion set \(X\) with
\[
|X|=\kappa_2(H)
\]
and a two-cover
\[
H-X=P\mid Q.
\]
After the normalization just described, the two component supports define
\[
(V(P),V(Q))\in\mathcal P(H)
\]
with
\[
\delta(V(P),V(Q))=|X|=\kappa_2(H).
\]
Hence equality holds.

Thus a minimum hole is exactly the complement of a maximum-total-support vertex of \(\mathcal P(H)\). No path order survives in the invariant.

### Quantitative dimension consequence

Let
\[
K(H)=\Delta\mathcal P(H).
\]
If
\[
\kappa_2(H)=k,
\]
then every support pair has total order at most \(n-k\). Since the minimum total order in \(\mathcal P(H)\) is \(4\), every strict chain has at most
\[
(n-k)-4
\]
strict rank increases. Therefore
\[
\boxed{\dim K(H)\le n-k-4.}
\]

Equivalently, any topological or Smith-chain construction that forces
\[
\dim K(H)\ge d
\]
immediately gives
\[
\boxed{\kappa_2(H)\le n-d-4.}
\]

More specifically, if \(K(H)\) admits Smith chains
\[
c_0,\ldots,c_d,
\qquad
\operatorname{aug}(c_0)=1,
\qquad
\partial c_i=(1+T)c_{i-1},
\]
then the Smith-chain argument already used for \(d=n-4\) shows that \(K(H)\) cannot have dimension at most \(d-1\). Hence
\[
\kappa_2(H)\le n-d-4.
\]

### Strategic reinterpretation of Article VII

This identifies the order-free invariant that the exact inversion theory was measuring.

The exact-word theorem discovered
\[
\kappa_2(H)=\min_\pi \max(0,q(\pi)-p(\pi)-1)
\]
inside permutation space. The support-pair theorem realizes the same number as a plain rank deficiency:
\[
\kappa_2(H)=n-\max(|A|+|B|).
\]

Consequently:

- the grand theorem is exactly the assertion that \(\mathcal P(H)\) reaches total support \(n\);
- a genuine minimum pair is exactly a top-rank support pair of total order \(n-2\);
- the current Article VII reduction to \(\kappa_2\le2\) lands exactly at
  \[
  \dim K(H)\le n-6;
  \]
- full closure by the Smith route asks for two further dimensions, from the two-hole rank frontier \(n-6\) to the universal source height \(n-4\).

This suggests that the late minimum-pair machinery should be re-read as candidate fillings for the **last two Smith equations**, rather than as endpoint-surgery lemmas. Hole-containing four/five seeds, minimum-hole synchronization, and seed-preserving maximalization are potentially useful precisely when they create mixed support-pair chains that fill those final codimension-one and codimension-zero obstructions.

The abstraction is earlier than the deletion-cover compatibility frontier: once deletion distance is introduced, support-pair rank can replace path-order compatibility as the primary closure coordinate.
