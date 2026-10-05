# Lemma 2

## Metadata

- ID: ascending_edges_in_a_dense_subgraph_ascending_edges_are_the_incidence_defect_subsection_b
- Parent Section: ascending_edges_in_a_dense_subgraph_ascending_edges_are_the_incidence_defect
- Position: 2
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Cold composition

(none yet)

## Development

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
