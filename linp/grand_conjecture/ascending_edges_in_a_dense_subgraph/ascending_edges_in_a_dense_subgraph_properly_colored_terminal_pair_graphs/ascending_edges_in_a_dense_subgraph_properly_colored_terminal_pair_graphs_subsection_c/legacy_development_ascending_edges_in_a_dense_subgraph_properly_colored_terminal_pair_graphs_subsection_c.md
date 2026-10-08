# Corollary 5 — preserved pre-item development

For a nonspecial edge \(e\), let \(a(e)\) be the vertex rank of its unique entrance and let
\[
p(e)=\min\{\phi(u),\phi(v)\}
\]
for its two terminal vertices. Then the edges with \(a(e)<p(e)\) satisfy
\[
\sum_e\left(\frac1{a(e)}-\frac1{p(e)}\right)=O(n\log\ell) \tag{3}
\]
in every \(P_\ell^{(3)}\)-free linear \(3\)-graph.

#### Proof
An edge with entrance rank \(a\) and minimum terminal rank \(p>a\) occurs in \(R_t\) precisely for
\[
a<t\le p.
\]
Therefore
\[
\frac1a-\frac1p
=
\sum_{t=a+1}^{p}\frac1{t(t-1)}.
\]
Summing over the edges and reversing the order of summation gives
\[
\sum_e\left(\frac1{a(e)}-\frac1{p(e)}\right)
=
\sum_{t\ge2}\frac{|E(R_t)|}{t(t-1)}.
\]
A rainbow-path extremal bound for properly colored graphs with no rainbow \(t\)-edge path gives \(|E(R_t)|=O(tn)\). Since \(t\le\ell-1\), the right-hand side is \(O(n\log\ell)\). ∎

Thus edges with a substantial entrance-to-terminal rank gap have bounded total harmonic mass. The unresolved contribution must concentrate near equal ranks.
