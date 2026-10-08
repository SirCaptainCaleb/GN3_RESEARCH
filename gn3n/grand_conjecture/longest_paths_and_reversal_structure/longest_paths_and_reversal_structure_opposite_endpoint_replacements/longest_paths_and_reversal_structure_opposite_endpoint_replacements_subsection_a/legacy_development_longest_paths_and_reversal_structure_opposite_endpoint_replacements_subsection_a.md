#  — preserved pre-item development

## Development

Let \(x,y\notin V(A)\). Suppose \(L\) is a Hamilton path on
\[
(V(A)-\{a_0\})\cup\{x\}
\]
and \(R\) is a Hamilton path on
\[
(V(A)-\{a_{\lambda-1}\})\cup\{y\},
\]
and both preserve the order inherited from \(A\). Assume \(\lambda\ge6\).

**Lemma 7.** The support
\[
(V(A)-\{a_0,a_{\lambda-1}\})\cup\{x,y\}
\]
is Hamiltonian.

**Proof.** Since \(A\cup\{x\}\) is not Hamiltonian, \(x\) can occupy only one of the first two positions relative to \(a_1,\ldots ,a_{\lambda-1}\); otherwise prepending \(a_0\) extends \(A\). Thus
\[
L=(x,a_1,\ldots ,a_{\lambda-1})
\]
or
\[
L=(a_1,x,a_2,\ldots ,a_{\lambda-1}).
\]
Similarly,
\[
R=(a_0,\ldots ,a_{\lambda-2},y)
\]
or
\[
R=(a_0,\ldots ,a_{\lambda-3},y,a_{\lambda-2}).
\]
Delete the old endpoints and combine the corresponding left and right forms. Every consecutive triple is inherited from \(L\), \(R\), or the middle of \(A\), so the resulting order is Hamiltonian. \(\square\)

Thus a difficult pair of opposite endpoint replacements must change the inherited order. Comparing deletion covers at \(a_0\) and \(a_{\lambda-1}\), one obtains either a reversed surviving edge of \(A\), different support partitions on the common double deletion, or an order disagreement on a common support.
