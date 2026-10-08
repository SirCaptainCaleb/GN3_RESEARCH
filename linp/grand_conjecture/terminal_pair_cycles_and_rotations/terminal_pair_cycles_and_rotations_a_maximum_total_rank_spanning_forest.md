# A maximum-total-rank spanning forest

Give each graph edge \(uv\in E(T)\) the edge rank of its parent hyperedge. In each component of \(T\), choose a spanning tree of maximum total weight; let \(F\) be the resulting spanning forest.

## Lemma 4

Let \(e\in E(T)\setminus E(F)\), and let \(C_e\) be its fundamental cycle in \(F+e\). Then \(e\) has minimum weight on \(C_e\).

#### Proof
If a tree edge \(f\in C_e\) had smaller weight than \(e\), then replacing \(f\) by \(e\) would produce a spanning tree of larger total weight. ∎

The graph \(T\) has exactly \(\beta(T)\) nonforest edges. Hence Lemma 4 selects one rank-minimal edge on a fundamental cycle for every independent cycle.

These selected graph edges carry additional information in the hypergraph.

## Lemma 5

Let \(e\) and \(f\) be two nonspecial hyperedges whose terminal pairs are adjacent in \(T\) at a common terminal \(v\). If
\[
\phi(f)\ge\phi(e),
\]
then every maximum path with last edge \(f\) and last vertex \(v\) contains a second vertex of \(e\).

#### Proof
Let \(P\) be such a path. If \(P\cap e=\{v\}\), then appending \(e\) after \(P\) gives a path of length \(\phi(f)+1\) with last edge \(e\). Hence
\[
\phi(e)\ge\phi(f)+1,
\]
contrary to the hypothesis. ∎

Combining Lemmas 4 and 5, every nonforest edge \(e\) has two forced second intersections: one associated with each neighboring edge of its fundamental cycle.

This is the structural content of cycle rank. A cycle is not merely an extra graph edge; it prescribes two additional intersections with maximum hypergraph paths.
