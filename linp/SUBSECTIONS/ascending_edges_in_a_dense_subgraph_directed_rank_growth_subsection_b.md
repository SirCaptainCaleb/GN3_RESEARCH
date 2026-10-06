# Lemma 9

## Metadata

- ID: ascending_edges_in_a_dense_subgraph_directed_rank_growth_subsection_b
- Parent Section: ascending_edges_in_a_dense_subgraph_directed_rank_growth
- Position: 2
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Along every directed arc \(x\to y\),
\[
\phi(y)\ge\phi(x)+1.
\]
Consequently a directed path of length \(r\) forces a vertex of rank at least \(r\), and therefore forces a linear hypergraph path of length at least \(r\).

#### Proof
If \(e\) has edge rank \(q\), then \(\phi(x)=q-1\), while each terminal vertex has rank at least \(q\). Iteration proves the first assertion. The second follows from the definition of vertex rank. ∎

Thus repeated movement through ascending edges cannot continue indefinitely without increasing rank.

## Frontier

- Development version when composed: None
- Development version now: 1
