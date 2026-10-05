# Opposite terminal edges and complementary supports

## Metadata

- ID: complementary_path_supports_and_endpoint_involutions_subsection_a
- Parent Section: complementary_path_supports_and_endpoint_involutions
- Position: 1
- Row version: 4
- Development version: 4
- Composition version: 1
- Composition stale: False

## Cold composition

For an ordered pair \(u,v\), let \(\mathcal F_{uv}\) consist of the sets \(X\subseteq V\setminus\{u,v\}\) for which some ordering of \(X\), followed by \(u,v\), is a tight path.

A spanning order with status word \(1^a0^b\) exists if and only if for some \(u\ne v\) there are
\[
X\in\mathcal F_{uv},\qquad Y\in\mathcal F_{vu}
\]
that partition \(V\setminus\{u,v\}\). Indeed, the tight prefix ends with \(u,v\), while reversing the non-tight suffix turns it into a tight path ending with \(v,u\). Conversely, two such paths splice into a spanning order whose first block is tight and second block non-tight.

Thus a one-change order is the same object as two tight paths sharing exactly one ordinary edge, traversed in opposite terminal directions, with complementary remaining supports. The \(0^a1^b\) case is the corresponding initial-edge formulation.

## Development

For an ordered pair \(u,v\), let \(\mathcal F_{uv}\) consist of the sets \(X\subseteq V\setminus\{u,v\}\) for which some ordering of \(X\), followed by \(u,v\), is a tight path.

A spanning order with status word \(1^a0^b\) exists if and only if for some \(u\ne v\) there are
\[
X\in\mathcal F_{uv},\qquad Y\in\mathcal F_{vu}
\]
that partition \(V\setminus\{u,v\}\). Indeed, the tight prefix ends with \(u,v\), while reversing the non-tight suffix turns it into a tight path ending with \(v,u\). Conversely, two such paths splice into a spanning order whose first block is tight and second block non-tight.

Thus a one-change order is the same object as two tight paths sharing exactly one ordinary edge, traversed in opposite terminal directions, with complementary remaining supports. The \(0^a1^b\) case is the corresponding initial-edge formulation.
