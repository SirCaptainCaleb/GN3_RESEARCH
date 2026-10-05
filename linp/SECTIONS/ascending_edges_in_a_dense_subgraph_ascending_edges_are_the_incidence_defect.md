# Ascending edges are the incidence defect

## Cold composition

## Lemma 1

For every incident pair \(v\in e\),
\[
\phi(e)\le \phi(v)+1.
\]
Equality holds if and only if \(e\) is ascending and \(v\) is its unique entrance.

#### Proof
If \(e\) is special, then \(v\) is terminal at \(e\), so \(\phi(v)\ge\phi(e)\).

Suppose \(e\) is nonspecial with unique entrance \(x\) and edge rank \(q\). Each terminal vertex is the last vertex of a \(q\)-edge path ending in \(e\), and therefore has vertex rank at least \(q\). Deleting \(e\) from a longest path ending in \(e\) shows \(\phi(x)\ge q-1\). Thus \(q\le\phi(v)+1\) at every incidence. Equality can occur only at the unique entrance, and there it is exactly the defining equality for an ascending edge. ∎

## Lemma 2

If \(H\) has \(m\) edges and \(n\) vertices, then
\[
3m-A\le \sum_{v}(2\phi(v)-1). \tag{1}
\]
Consequently, if \(H\) is \(P_\ell^{(3)}\)-free,
\[
3m-A\le (2\ell-3)n. \tag{2}
\]

#### Proof
Fix \(v\) and put \(p=\phi(v)\). Choose a maximum \(p\)-edge path \(P\) with last vertex \(v\). Every incident edge \(e\) with \(\phi(e)\le p\), except possibly the last edge of \(P\), must contain a vertex of \(V(P)\) outside the last edge; otherwise it can be appended to a suitable final segment of \(P\), producing a path longer than \(\phi(e)\). Distinct incident edges give distinct such vertices by linearity. There are \(2p-2\) vertices outside the last edge, so at most \(2p-1\) incident edges have edge rank at most \(p\).

By Lemma 1, the only remaining incident edges are ascending edges whose unique entrance is \(v\). Summing the bound \(2\phi(v)-1\) over all vertices therefore counts every edge three times except that each ascending edge loses exactly its unique-entrance incidence. This proves (1). If \(H\) is \(P_\ell^{(3)}\)-free, then \(\phi(v)\le\ell-1\), which gives (2). ∎

Thus the two-thirds bound follows once \(A=o(\ell n)\).

## Metadata

- ID: ascending_edges_in_a_dense_subgraph_ascending_edges_are_the_incidence_defect
- Kind: section
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Composition version: 1
- Composition stale: False

## Development tree

- [Subsection 1 — Lemma 1](../SUBSECTIONS/ascending_edges_in_a_dense_subgraph_ascending_edges_are_the_incidence_defect_subsection_a.md) (\`ascending_edges_in_a_dense_subgraph_ascending_edges_are_the_incidence_defect_subsection_a\`; development v1; composition v1; stale=False)
- [Subsection 2 — Lemma 2](../SUBSECTIONS/ascending_edges_in_a_dense_subgraph_ascending_edges_are_the_incidence_defect_subsection_b.md) (\`ascending_edges_in_a_dense_subgraph_ascending_edges_are_the_incidence_defect_subsection_b\`; development v1; composition vNone; stale=True)
