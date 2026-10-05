# Proposition 4

## Metadata

- ID: the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_separating_graph_vertices_from_colors_subsection_c
- Parent Section: the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_separating_graph_vertices_from_colors
- Position: 3
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

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

## Development

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
