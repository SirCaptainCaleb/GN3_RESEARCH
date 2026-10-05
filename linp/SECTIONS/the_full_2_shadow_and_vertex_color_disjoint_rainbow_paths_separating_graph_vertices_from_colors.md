# Separating graph vertices from colors

## Composition

There is a simpler reduction that forces color-vertex disjointness by construction, at the cost of a factor two.

Choose a partition
\[
V(H)=A\sqcup B.
\]
Retain only shadow edges \(xy\) with
\[
x,y\in A
\qquad\text{and}\qquad
c(xy)\in B.
\]
Call the resulting properly edge-colored graph \(J\).

## Lemma 3

Every rainbow path in \(J\) lifts to a linear hypergraph path of the same length in \(H\).

#### Proof
All path vertices lie in \(A\), while all colors lie in \(B\), so no color equals a path vertex. The rainbow condition makes the colors distinct. A graph path already has distinct path vertices. Hence Theorem 2 applies. ∎

## Proposition 4

Suppose there is a constant \(\alpha>0\) and an absolute constant \(C\) such that every properly edge-colored graph of average degree \(d\) contains a rainbow path with at least
\[
\alpha d-C
\]
edges. Then every \(P_\ell^{(3)}\)-free linear \(3\)-graph satisfies
\[
|E(H)|
\le
\frac{2(\ell+C)}{3\alpha}\,n. \tag{9}
\]

#### Proof
Choose \(A,B\) by placing each vertex independently into either class with probability \(1/2\). A hyperedge contributes exactly one retained shadow edge precisely when two of its vertices lie in \(A\) and the third lies in \(B\), which occurs with probability \(3/8\). Therefore
\[
\mathbb E\,e(J)=\frac38|E(H)|.
\]
Also
\[
\mathbb E|A|=\frac n2.
\]

Since \(H\) is \(P_\ell^{(3)}\)-free, Lemma 3 implies that \(J\) has no rainbow \(\ell\)-edge path. By the assumed graph theorem,
\[
\alpha\,\frac{2e(J)}{|A|}-C<\ell,
\]
so
\[
e(J)\le \frac{\ell+C}{2\alpha}|A|.
\]
Taking expectations gives
\[
\frac38|E(H)|
\le
\frac{\ell+C}{2\alpha}\frac n2,
\]
which is (9). ∎

Even the ideal value \(\alpha=1\) gives only the two-thirds coefficient. Therefore the one-third problem cannot be solved by discarding the triangle rule (4) and applying a general rainbow-path theorem.

## Degree bookkeeping across the shadow reduction

The hypergraph degree and the degree in a retained properly edge-colored shadow graph are separate quantities. Equation (3) gives d_G(v)=2d_H(v) only for the full shadow G. After passing to a retained graph J, or to a further graph-side core, a rainbow-path theorem whose hypothesis is stated in terms of minimum graph degree must be applied using the degree in that graph, not d_H. Conversely, a hypergraph-side minimum-degree hypothesis remains available for hypergraph peeling, attachment, or special-edge arguments. The two degree conditions serve different parts of the proof and should be tracked simultaneously rather than identified.

## Metadata

- ID: the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_separating_graph_vertices_from_colors
- Kind: section
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Composition version: 1
- Composition stale: False

## Development tree

- [Subsection 1 — (untitled)](../SUBSECTIONS/the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_separating_graph_vertices_from_colors_subsection_a.md) (`the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_separating_graph_vertices_from_colors_subsection_a`; development v1; composition v1; stale=False)
- [Subsection 2 — Lemma 3](../SUBSECTIONS/the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_separating_graph_vertices_from_colors_subsection_b.md) (`the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_separating_graph_vertices_from_colors_subsection_b`; development v1; composition v1; stale=False)
- [Subsection 3 — Proposition 4](../SUBSECTIONS/the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_separating_graph_vertices_from_colors_subsection_c.md) (`the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_separating_graph_vertices_from_colors_subsection_c`; development v1; composition v1; stale=False)
- [Subsection 4 — Degree bookkeeping across the shadow reduction](../SUBSECTIONS/the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_separating_graph_vertices_from_colors_subsection_d.md) (`the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_separating_graph_vertices_from_colors_subsection_d`; development v1; composition vNone; stale=False)
