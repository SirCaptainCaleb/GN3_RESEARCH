# Lemma 4 — preserved pre-item development

## Development

The coloring of \(R_t\) is proper, and \(R_t\) contains no rainbow path with \(t\) edges.

#### Proof
If two graph edges incident with \(u\) had the same color \(x\), the corresponding hyperedges would both contain \(u\) and \(x\), contrary to linearity.

Suppose
\[
v_0v_1\cdots v_t
\]
were a rainbow \(t\)-edge path in \(R_t\), with edge \(v_{i-1}v_i\) colored \(x_i\). The associated hyperedges are
\[
e_i=\{x_i,v_{i-1},v_i\}.
\]
The colors \(x_i\) are distinct and have vertex rank below \(t\), whereas every \(v_i\) has vertex rank at least \(t\). Hence no color equals a path vertex. Properness and linearity then imply that
\[
e_1,\ldots,e_t
\]
form a linear \(t\)-edge path. The vertex \(x_t\) is private in the last hyperedge, so the path can be oriented with last vertex \(x_t\). This gives \(\phi(x_t)\ge t\), a contradiction. ∎

There is a useful summation consequence.
