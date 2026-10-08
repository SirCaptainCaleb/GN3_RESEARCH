# A sufficient common-terminal bound

For a vertex \(v\), let
\[
c(v)=|\{e:e\text{ is ascending and }v\text{ is terminal at }e\}|.
\]

## Proposition 6

Suppose \(g\) is nondecreasing and
\[
c(v)\le g(\phi(v))
\]
for every vertex. Then every \(P_\ell^{(3)}\)-free linear \(3\)-graph satisfies
\[
m\le
\left(
\frac{2\ell-3}{3}
+
\frac{g(\ell-1)}6
\right)n. \tag{4}
\]
In particular, \(g(p)=o(p)\) implies the two-thirds leading coefficient.

#### Proof
Every ascending edge has exactly two terminal vertices, so
\[
2A=\sum_v c(v)\le ng(\ell-1).
\]
Substitute this in (2). ∎

Hence full specialness is stronger than necessary: a sublinear common-terminal bound already suffices.
