# A sufficient common-terminal bound

## Cold composition

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

## Metadata

- ID: ascending_edges_in_a_dense_subgraph_a_sufficient_common_terminal_bound
- Kind: section
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Composition version: 1
- Composition stale: False

## Development tree

- [Subsection 1 — (untitled)](../SUBSECTIONS/ascending_edges_in_a_dense_subgraph_a_sufficient_common_terminal_bound_subsection_a.md) (`ascending_edges_in_a_dense_subgraph_a_sufficient_common_terminal_bound_subsection_a`; development v1; composition v1; stale=False)
- [Subsection 2 — Proposition 6](../SUBSECTIONS/ascending_edges_in_a_dense_subgraph_a_sufficient_common_terminal_bound_subsection_b.md) (`ascending_edges_in_a_dense_subgraph_a_sufficient_common_terminal_bound_subsection_b`; development v1; composition vNone; stale=True)
