# Orientation-blind NOR as a neighboring conjectural family

## Metadata

- ID: orientation_blind_repair_and_the_first_nontrivial_dimension
- Parent Section: higher_memory_norine_geodesics
- Position: 5
- Row version: 3
- Development version: 3
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development


There is a natural orientation-blind higher-uniformity family distinct from directed tuple NOR.

Represent an ordered geodesic \(k\)-segment by
\[
(X;v_1,\ldots,v_k),
\qquad
K=\{v_1,\ldots,v_k\}.
\]
A support-orientation-blind coloring ignores the direction-sensitive information internal to the traversed support. One convenient cube formulation allows dependence on the outside base set
\[
B=X\setminus K
\]
while identifying changes of \(X\) inside \(K\).

This family contains the ordinary undirected Norine edge problem when \(k=1\), and it avoids the absolute-rank parity obstruction. It may well satisfy its own one-change theorem.

However, it is not the main directed NOR family because the GN3 \(k=3\) embedding is genuinely directed:
\[
h(u,v,w)
\]
need not equal the color of the reversed triple. Thus the orientation-blind family cannot serve as a common generalization containing GN3.

### First nontrivial dimension

If \(n=k+2\), every binary support-orientation-blind coloring has an antipodal geodesic whose three-window color word changes at most once; antipodal antisymmetry is not needed.

The proof assumes every three-window word is \(010\) or \(101\), varies the two outside coordinates to force independence from \(B\), and reduces to a 2-coloring of the shift graph on ordered \(k\)-tuples. That graph contains an odd cycle, contradiction.

This result should be read as evidence that the orientation-blind family is mathematically viable in its own right, not as a repair of directed NOR.
