# defect_lines_and_spanning_order_compression_a_hamiltonian_five_set_beside_a_long_path_subsection_a

## Metadata

- ID: defect_lines_and_spanning_order_compression_a_hamiltonian_five_set_beside_a_long_path_subsection_a
- Parent Section: defect_lines_and_spanning_order_compression_a_hamiltonian_five_set_beside_a_long_path
- Position: 1
- Row version: 3
- Development version: 3
- Composition version: None
- Composition stale: False

## Cold composition

(none yet)

## Development

Let
\[
X\mid P\mid Q
\]
be a three-cover with \(|X|=5\) and \(P=(p_1,\ldots ,p_m)\), \(m\ge7\).

**Lemma 8.** One of the following holds:
1. a pairwise repartition of \(X\mid P\) strictly decreases \(\Phi\);
2. a pairwise repartition preserves the component orders \(\{5,m\}\) and replaces one vertex of \(X\) by an endpoint of \(P\);
3. a tight triple containing a vertex of \(X\) reverses an edge of the displayed path \(P\).

**Proof.** If an endpoint transfer makes the two component orders more balanced, (1) holds. Otherwise there is \(x\in X\) such that, with \(D=X-\{x\}\), both
\[
D\cup\{p_1\},\qquad D\cup\{p_m\}
\]
are Hamiltonian. If \((V(P)-\{p_1\})\cup\{x\}\) or \((V(P)-\{p_m\})\cup\{x\}\) is Hamiltonian, pair it with the corresponding Hamiltonian five-set to obtain (2). If neither is Hamiltonian, \(x\) cannot be inserted at either end of the displayed path. Testing insertion positions along \(P\), the first unavailable internal insertion gives, by boundary reversal, a tight triple through \(x\) that reverses the corresponding displayed edge. \(\square\)

Thus both central cases reduce to the same ordered objects.

### A prescribed endpoint survives reduction to four vertices

The order-five support alternative reduces to the four-support interface.

**Lemma 9.** Let \(H\) be a minimum counterexample, let \(F\subsetneq V(H)\) be a Hamiltonian five-support, and let \(a\in F\) be prescribed. Then there is a Hamiltonian four-set
\[
K\subset F,\qquad a\in K,
\]
such that \(H-K\) is non-Hamiltonian and has path-cover number two.

**Proof.** Choose a Hamilton path on \(F\). It has two endpoints, so at least one endpoint \(z\) is different from the prescribed vertex \(a\). Delete \(z\). The remaining four vertices inherit a Hamilton path, so
\[
K=F-\{z\}
\]
is Hamiltonian and contains \(a\).

The set \(K\) is proper. Minimum-counterexample calculus gives
\[
\operatorname{pc}(H-K)\le2.
\]
If \(H-K\) were Hamiltonian, a Hamilton path on \(K\) together with one on \(H-K\) would form a two-cover of \(H\), contrary to the choice of \(H\). Hence
\[
\operatorname{pc}(H-K)=2.
\]
\(\square\)

Consequently a Hamiltonian support of order four **or five** carrying displayed endpoint information, with two-coverable complement, may always be replaced by an endpoint-rooted Hamiltonian four-support with the same complement property. Lemma 8 of the preceding Section then converts this four-support directly into a split/leave-and-return disturbance, an external end-edge reversal, or a two-cover.

Thus the order-five support is no longer an independent terminal interface.
