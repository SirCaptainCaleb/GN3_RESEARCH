# Vertices of degree above the minimum threshold

## Cold composition

A dense equality case has many vertices whose degree is strictly above the minimum degree.

## Lemma 5

Suppose
\[
|E(H)|=dn
\qquad\text{and}\qquad
\delta(H)\ge d+1.
\]
Let
\[
R=\{v:d_H(v)\ge d+2\}.
\]
Then
\[
|R|\ge 4d-1. \tag{10}
\]
Consequently, every \(q\)-edge path omits at least
\[
4d-2q-2 \tag{11}
\]
vertices of \(R\).

#### Proof
The total degree excess above \(d+1\) is
\[
\sum_v(d_H(v)-(d+1))
=
3dn-(d+1)n
=
(2d-1)n. \tag{12}
\]
Vertices outside \(R\) contribute nothing to (12). By linearity,
\[
d_H(v)\le \frac{n-1}{2}
\]
for every vertex \(v\), because the \(2d_H(v)\) vertices paired with \(v\) in incident hyperedges are all distinct. Hence each vertex of \(R\) contributes at most
\[
\frac{n-1}{2}-(d+1)
=
\frac{n-2d-3}{2}
\]
to (12). Therefore
\[
(2d-1)n
\le
|R|\frac{n-2d-3}{2},
\]
so
\[
|R|
\ge
\frac{2(2d-1)n}{n-2d-3}
>
4d-2.
\]
Since \(|R|\) is integral, (10) follows.

A \(q\)-edge linear \(3\)-uniform path has \(2q+1\) vertices, so it contains at most \(2q+1\) vertices of \(R\). Subtracting from (10) gives (11). ∎

Thus even when \(P\) is nearly spanning relative to the forbidden length, a dense equality case contains many high-degree vertices outside \(P\).

## Metadata

- ID: induction_on_the_complement_of_a_longest_path_vertices_of_degree_above_the_minimum_threshold
- Kind: section
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Composition version: 1
- Composition stale: False

## Development tree

- [Subsection 1 — (untitled)](../SUBSECTIONS/induction_on_the_complement_of_a_longest_path_vertices_of_degree_above_the_minimum_threshold_subsection_a.md) (\`induction_on_the_complement_of_a_longest_path_vertices_of_degree_above_the_minimum_threshold_subsection_a\`; development v1; composition v1; stale=False)
- [Subsection 2 — Lemma 5](../SUBSECTIONS/induction_on_the_complement_of_a_longest_path_vertices_of_degree_above_the_minimum_threshold_subsection_b.md) (\`induction_on_the_complement_of_a_longest_path_vertices_of_degree_above_the_minimum_threshold_subsection_b\`; development v1; composition vNone; stale=True)
