# 

## Composition

(none yet)

## Development

Let
\[
X\mid C\mid D
\]
be a three-cover, with \(X\) Hamiltonian,
\[
C=(c_0,c_1,\ldots ,c_m),
\]
and \(D\ne\varnothing\). Suppose \(X\cup\{c_0\}\) is Hamiltonian.

First note that any deletion cover of \(H-c_0\) must contain an edge with one endpoint in \(X\) and the other in
\[
(C-\{c_0\})\cup D.
\]
Otherwise its two paths would each remain inside one side of this partition, and adjoining \(c_0\) to a Hamilton path on \(X\cup\{c_0\}\) would separate \(H\) into two tight paths.

Suppose now that some Hamilton path on \(X\cup\{c_0\}\) has \(c_0\) as the endpoint adjacent to \(c_1\). Extend this Hamilton path greedily by \(c_1,c_2,\ldots\).

**Lemma 1.** If the greedy extension does not absorb all of \(C\), then at the first failed extension there is a tight triple reversing the terminal edge of the current Hamilton path.

**Proof.** Let \(R\) be the maximal Hamilton path obtained, ending in an edge \((u,c_h)\), and suppose \(c_{h+1}\) is the first vertex that cannot be appended. Then
\[
(u,c_h,c_{h+1})
\]
is non-tight. Boundary reversal gives
\[
(c_{h+1},c_h,u)
\]
tight, which reverses the displayed terminal edge \((u,c_h)\). If every vertex of \(C\) were absorbed, the resulting Hamilton path together with \(D\) would be a two-cover of \(H\). \(\square\)

Thus endpoint realization gives a displayed end-edge reversal. The only alternative is that \(c_0\) is internal in every Hamiltonian order of \(X\cup\{c_0\}\).
