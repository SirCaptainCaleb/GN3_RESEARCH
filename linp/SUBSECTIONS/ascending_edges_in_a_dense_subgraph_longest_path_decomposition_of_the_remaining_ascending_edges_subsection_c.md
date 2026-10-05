# Lemma 8

## Metadata

- ID: ascending_edges_in_a_dense_subgraph_longest_path_decomposition_of_the_remaining_ascending_edges_subsection_c
- Parent Section: ascending_edges_in_a_dense_subgraph_longest_path_decomposition_of_the_remaining_ascending_edges
- Position: 3
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: True

## Cold composition

(none yet)

## Development

Let \(U(v)\) be the class \(U\) edges assigned to \(v\). There is a set \(W(v)\) of vertices with
\[
\phi(w)\ge\phi(v)\qquad (w\in W(v))
\]
such that
\[
|U(v)|\le 2|W(v)|+1. \tag{8}
\]

#### Proof
Let \(e=\{x,u,v\}\in U(v)\), and let \(j(e)\) be the first index for which \(u\in g_{j(e)}\). Since \(x\notin V(P_v)\), the edge \(e\) can replace the suffix immediately after \(g_{j(e)}\), producing a \(\phi(v)\)-edge path with new last vertex
\[
w(e)=g_{j(e)+1}\cap g_{j(e)+2}.
\]
Hence \(\phi(w(e))\ge\phi(v)\).

Different indices \(j\) give different vertices \(w(e)\). By linearity, distinct edges assigned to \(v\) have distinct opposite terminals \(u\). Along a linear path, at most two vertices have their first occurrence in a given \(g_j\) for \(j\ge2\), and at most three do so in \(g_1\). Therefore at most two edges of \(U(v)\) give the same \(j\), apart from one boundary excess. This yields (8). ∎

Lemmas 7 and 8 reduce the unresolved ascending mass to two phenomena:

1. many edges of edge rank \(p-o(p)\) whose unique entrance lies on a maximum \(p\)-edge path;
2. many alternative last vertices of rank at least \(p\), produced from edges whose opposite terminal lies on that path.
