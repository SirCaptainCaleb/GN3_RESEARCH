# Lemma 5

## Composition

(none yet)

## Development

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
