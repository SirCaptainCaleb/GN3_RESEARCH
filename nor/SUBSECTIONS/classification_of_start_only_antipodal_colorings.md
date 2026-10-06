# Start-only obstructions in the broader window model

## Metadata

- ID: classification_of_start_only_antipodal_colorings
- Parent Section: higher_memory_norine_geodesics
- Position: 6
- Row version: 2
- Development version: 2
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development


This subsection classifies a specific obstruction in the broader basepoint-dependent cube-window model, not in directed tuple NOR.

Suppose
\[
\chi(X_0,\ldots,X_k)=f(X_0)
\]
depends only on the initial cube vertex. Antipodal reversal forces
\[
f(X\triangle S)=1-f(X)
\]
for every \(S\subseteq V\) of size
\[
d=n-k.
\]

When \(1\le d\le n-1\), such an \(f\) exists iff \(d\) is odd. In that case the only possibilities are
\[
f(X)=|X|\pmod2
\]
and its global complement.

Indeed, comparing two \(d\)-sets differing by one coordinate shows invariance under every two-coordinate flip, hence \(f\) is constant on each rank-parity class. The required \(d\)-flip changes those classes iff \(d\) is odd.

Thus absolute rank parity is the unique start-only obstruction in this enlarged model.

Directed tuple NOR excludes this sector entirely because its color is a function only of the ordered flipped coordinates. This classification is therefore a boundary-of-formulation result, not evidence against \(N_k\).
