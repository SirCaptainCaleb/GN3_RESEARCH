# Audit: largest Hamiltonian supports are only proved at least half-order — preserved pre-item development

## Composition

(none yet)

## Development

## Audit: the largest-support argument gives only a half-order lower bound

The development in [[largest_hamiltonian_supports_in_minimum_counterexamples_have_half_order]] correctly proves the following.

Let \(H\) be a minimum-order counterexample on \(n\) vertices, and let \(S\) be a proper Hamiltonian support of maximum cardinality \(s\). For every vertex \(z\), a deletion cover of \(H-z\) has two Hamiltonian components, each of order at most \(s\). Hence
\[
n-1\le 2s,
\]
so
\[
\boxed{s\ge \left\lceil\frac{n-1}{2}\right\rceil.}
\]
Consequently, for any two-cover
\[
H-S=P\mid Q,
\]
\[
|P|+|Q|=n-s\le s+1.
\]

However, this does **not** prove that \(s\) equals one half of \(n\), nor does it supply an upper bound of the form \(s\le\lceil n/2\rceil\). A largest proper Hamiltonian support may, on the present argument, be strictly larger than half the vertex set.

Therefore the mathematically justified statement is:

> A largest proper Hamiltonian support in a minimum counterexample has order **at least** half the graph (up to the parity rounding above), and its two-coverable complement has total order at most \(s+1\).

Any later argument that uses exact half-order or rules out a highly unbalanced complementary two-cover from subsection 212 alone is unsupported and should instead use an additional extremal or routing lemma.
