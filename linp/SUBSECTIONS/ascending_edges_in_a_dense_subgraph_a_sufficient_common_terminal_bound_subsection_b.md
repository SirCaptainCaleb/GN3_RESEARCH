# Proposition 6

## Metadata

- ID: ascending_edges_in_a_dense_subgraph_a_sufficient_common_terminal_bound_subsection_b
- Parent Section: ascending_edges_in_a_dense_subgraph_a_sufficient_common_terminal_bound
- Position: 2
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

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

## Frontier

- Development version when composed: None
- Development version now: 1
