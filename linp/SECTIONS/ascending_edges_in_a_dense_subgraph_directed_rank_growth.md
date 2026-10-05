# Directed rank growth

## Cold composition

There is a complementary global representation. For every ascending edge
\[
e=\{x,u,v\}
\]
with unique entrance \(x\), draw the arcs
\[
x\to u,\qquad x\to v.
\]

## Lemma 9

Along every directed arc \(x\to y\),
\[
\phi(y)\ge\phi(x)+1.
\]
Consequently a directed path of length \(r\) forces a vertex of rank at least \(r\), and therefore forces a linear hypergraph path of length at least \(r\).

#### Proof
If \(e\) has edge rank \(q\), then \(\phi(x)=q-1\), while each terminal vertex has rank at least \(q\). Iteration proves the first assertion. The second follows from the definition of vertex rank. ∎

Thus repeated movement through ascending edges cannot continue indefinitely without increasing rank.

## Metadata

- ID: ascending_edges_in_a_dense_subgraph_directed_rank_growth
- Kind: section
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Composition version: 1
- Composition stale: False

## Development tree

- [Subsection 1 — (untitled)](../SUBSECTIONS/ascending_edges_in_a_dense_subgraph_directed_rank_growth_subsection_a.md) (`ascending_edges_in_a_dense_subgraph_directed_rank_growth_subsection_a`; development v1; composition v1; stale=False)
- [Subsection 2 — Lemma 9](../SUBSECTIONS/ascending_edges_in_a_dense_subgraph_directed_rank_growth_subsection_b.md) (`ascending_edges_in_a_dense_subgraph_directed_rank_growth_subsection_b`; development v1; composition vNone; stale=False)
