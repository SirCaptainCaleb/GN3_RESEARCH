# Lemma 1 — preserved pre-item development

## Development

Assume the inductive inequality
\[
3m_Y\le \ell |Y|.
\]
Define
\[
D_Y=\ell |Y|-3m_Y.
\]
Then (1) is equivalent to
\[
3e_X\le \binom{|X|}{2}+(\ell-k)|X|+D_Y. \tag{4}
\]

#### Proof
Using (3),
\[
3|E(H)|
=
3m_Y+3e_X.
\]
Hence (1) is equivalent to
\[
3e_X
\le
\ell |X|+\ell |Y|-3m_Y
=
\ell |X|+D_Y. \tag{5}
\]
By (2),
\[
\binom{|X|}{2}
=
\frac{(2k+1)(2k)}2
=
k(2k+1)
=
k|X|.
\]
Therefore
\[
\ell |X|
=
\binom{|X|}{2}+(\ell-k)|X|,
\]
and (5) becomes (4). ∎

When \(k=\ell-1\), the longest possible value in a \(P_\ell^{(3)}\)-free graph, (4) reduces to
\[
3e_X\le \binom{|X|}{2}+|X|+D_Y. \tag{6}
\]

Equation (4) is the entire inductive problem. The first term depends only on unordered pairs of vertices of \(X\); the second records the difference between the forbidden length and the actual longest-path length; the third is the amount by which \(H[Y]\) falls below the inductive extremal bound.
