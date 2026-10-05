# Lemma 1

## Metadata

- ID: ascending_edges_in_a_dense_subgraph_ascending_edges_are_the_incidence_defect_subsection_a
- Parent Section: ascending_edges_in_a_dense_subgraph_ascending_edges_are_the_incidence_defect
- Position: 1
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

For every incident pair \(v\in e\),
\[
\phi(e)\le \phi(v)+1.
\]
Equality holds if and only if \(e\) is ascending and \(v\) is its unique entrance.

#### Proof
If \(e\) is special, then \(v\) is terminal at \(e\), so \(\phi(v)\ge\phi(e)\).

Suppose \(e\) is nonspecial with unique entrance \(x\) and edge rank \(q\). Each terminal vertex is the last vertex of a \(q\)-edge path ending in \(e\), and therefore has vertex rank at least \(q\). Deleting \(e\) from a longest path ending in \(e\) shows \(\phi(x)\ge q-1\). Thus \(q\le\phi(v)+1\) at every incidence. Equality can occur only at the unique entrance, and there it is exactly the defining equality for an ascending edge. ∎

## Development

For every incident pair \(v\in e\),
\[
\phi(e)\le \phi(v)+1.
\]
Equality holds if and only if \(e\) is ascending and \(v\) is its unique entrance.

#### Proof
If \(e\) is special, then \(v\) is terminal at \(e\), so \(\phi(v)\ge\phi(e)\).

Suppose \(e\) is nonspecial with unique entrance \(x\) and edge rank \(q\). Each terminal vertex is the last vertex of a \(q\)-edge path ending in \(e\), and therefore has vertex rank at least \(q\). Deleting \(e\) from a longest path ending in \(e\) shows \(\phi(x)\ge q-1\). Thus \(q\le\phi(v)+1\) at every incidence. Equality can occur only at the unique entrance, and there it is exactly the defining equality for an ascending edge. ∎
