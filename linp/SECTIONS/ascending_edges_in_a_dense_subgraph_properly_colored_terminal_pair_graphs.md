# Properly colored terminal-pair graphs

## Cold composition

Fix \(t\ge1\). Form a graph \(R_t\) as follows. For every nonspecial edge
\[
e=\{x,u,v\}
\]
whose unique entrance satisfies \(\phi(x)<t\) and whose two terminal vertices satisfy
\[
\phi(u),\phi(v)\ge t,
\]
put the graph edge \(uv\) in \(R_t\) and color it by \(x\).

## Lemma 4

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

## Corollary 5

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

## Metadata

- ID: ascending_edges_in_a_dense_subgraph_properly_colored_terminal_pair_graphs
- Kind: section
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Composition version: 1
- Composition stale: False

## Development tree

- [Subsection 1 — (untitled)](../SUBSECTIONS/ascending_edges_in_a_dense_subgraph_properly_colored_terminal_pair_graphs_subsection_a.md) (\`ascending_edges_in_a_dense_subgraph_properly_colored_terminal_pair_graphs_subsection_a\`; development v1; composition v1; stale=False)
- [Subsection 2 — Lemma 4](../SUBSECTIONS/ascending_edges_in_a_dense_subgraph_properly_colored_terminal_pair_graphs_subsection_b.md) (\`ascending_edges_in_a_dense_subgraph_properly_colored_terminal_pair_graphs_subsection_b\`; development v1; composition v1; stale=False)
- [Subsection 3 — Corollary 5](../SUBSECTIONS/ascending_edges_in_a_dense_subgraph_properly_colored_terminal_pair_graphs_subsection_c.md) (\`ascending_edges_in_a_dense_subgraph_properly_colored_terminal_pair_graphs_subsection_c\`; development v1; composition vNone; stale=True)
