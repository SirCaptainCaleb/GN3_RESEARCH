# Optimal Hamiltonian ordering of direction disagreements: a dimension-uniform NORI1 certificate

- Stable ID: note_nori_optimal_order_disagreement_20261016
- Author: unspecified; session provenance retained
- Primary home: subsection:global_petrie_switch_moment_and_local_turn_counting
- Labels: NORI1, dimension-uniform, color-switches, metric, root-slide, Hamiltonian-ordering
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r10487_1
- Updated session: session_nori_r10487_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

Let \(n\ge2\), and let \(c\) be any antipodally odd binary edge coloring of \(Q_n\), with edge rule \(c_i(x)\) ignoring \(x_i\). For distinct dimensions \(i,j\), put
\[
d_c(i,j)=2^{-n}\sum_{x\in Q_n}[c_i(x)\ne c_j(x)].
\]
This is the Hamming pseudometric on the \(n\) Boolean direction rules. Define its minimum Hamiltonian path weight
\[
L(c)=\min_{\pi\in S_n}\sum_{k=1}^{n-1}d_c(\pi_k,\pi_{k+1}).
\]

**Theorem (optimal-order disagreement certificate).** The minimum number \(\mu(c)\) of ordinary color switches over all full antipodal geodesics satisfies
\[
\boxed{\mu(c)\le\lfloor L(c)\rfloor.}
\]
Consequently, \(L(c)<2\) implies a monochromatic full antipodal geodesic. Any counterexample to NORI1 must have \(L(c)\ge2\). If a minimum spanning tree of the metric \(d_c\) has weight less than one, NORI1 holds for \(c\).

*Proof.* Fix an order \(\pi=(\pi_1,\ldots,\pi_n)\) and choose the initial vertex \(X\) uniformly from \(Q_n\). Immediately before the \((k+1)\)-st edge, the path vertex is \(Y_k=X+e_{\pi_1}+\cdots+e_{\pi_k}\), which is uniform on \(Q_n\). The consecutive edge colors meeting at \(Y_k\) are \(c_{\pi_k}(Y_k)\) and \(c_{\pi_{k+1}}(Y_k)\); the color of an undirected \(\pi_k\)-edge is unchanged by toggling its own bit. Therefore the expected switch count of this rooted full geodesic is
\[
\mathbb E_X[\operatorname{sw}(P(X,\pi))]
=\sum_{k=1}^{n-1}d_c(\pi_k,\pi_{k+1}).
\]
Some root has switch count at most the floor of this expectation. Minimize over \(\pi\), proving the first inequality.

If the resulting path has at most one switch, write its color word, after a possible global color interchange, as \(0^a1^{n-a}\). Follow it by its antipodal translate in the same direction order. Antipodal oddness makes the second color word \(1^a0^{n-a}\). The resulting \(2n\)-edge closed dimension-periodic walk contains \(n\) consecutive edges of color one, and these use every dimension once, giving the desired geodesic. The constant-word cases are immediate. Finally \(d_c\) satisfies the triangle inequality; doubling a spanning tree, shortcutting repeated vertices, and deleting a closing edge gives a Hamiltonian path of weight at most twice the tree weight. Thus tree weight less than one implies \(L(c)<2\). \(\square\)

**Strict improvement over indiscriminate-order averaging.** Fix \(r\ge5\) and partition the \(2r\) dimensions into \(A,B\), each of size \(r\). Choose any three dimensions of \(B\) and let \(g(x_B)\) be their parity; choose any three dimensions of \(A\) and let \(h(x_A)\) be their parity. Set \(c_i(x)=g(x_B)\) for all \(i\in A\) and \(c_j(x)=h(x_A)\) for all \(j\in B\). This coloring is antipodally odd, and every direction rule is nonunary. The pseudometric vanishes within each block and equals \(1/2\) across the blocks; hence \(L(c)=1/2\) and the theorem applies. In contrast, a uniformly random dimension order has mean disagreement length \(r/2\ge5/2\), since its expected number of adjacencies across the two blocks is \(r\). Thus averaging over all orders does not yield the at-most-one-switch conclusion, whereas optimizing the order does.

**Limit of the certificate.** For the legal cyclic-reader coloring \(c_i(x)=x_{i+1\pmod n}\), all pairwise disagreements equal \(1/2\). Hence \(L(c)=(n-1)/2\), which is at least two for \(n\ge5\). These colorings nonetheless admit monochromatic full geodesics. Therefore the metric criterion is sufficient and its threshold does not establish unrestricted NORI1. The theorem applies to arbitrary numbers of nonlinear direction rules; no complexity restriction enters its proof.
