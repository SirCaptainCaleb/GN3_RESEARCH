# Path translation

## Cold composition

Let
\[
x_0x_1\cdots x_k
\]
be a graph path in \(G\), and write
\[
c_i=c(x_{i-1}x_i).
\]
The corresponding hyperedges are
\[
e_i=\{x_{i-1},x_i,c_i\}. \tag{5}
\]

## Theorem 2

The hyperedges \(e_1,\ldots,e_k\) form a linear hypergraph path if and only if
\[
x_0,\ldots,x_k,c_1,\ldots,c_k \tag{6}
\]
are all distinct.

#### Proof
Assume first that the vertices in (6) are all distinct. Consecutive hyperedges \(e_i,e_{i+1}\) meet in \(x_i\). If nonconsecutive \(e_i,e_j\) intersected, their common vertex would have to be either a repeated graph-path vertex, a repeated color, or a color equal to a nonincident graph-path vertex. Each possibility contradicts (6). Hence the hyperedges form a linear path.

Conversely, suppose \(e_1,\ldots,e_k\) form a linear path. A \(k\)-edge linear \(3\)-uniform path has exactly \(2k+1\) vertices. The list (6) has \(k+1+k=2k+1\) entries and contains every vertex of the hypergraph path by (5). Therefore the entries in (6) are all distinct. ∎

Thus
\[
H\text{ is }P_\ell^{(3)}\text{-free}
\]
if and only if its full shadow contains no \(\ell\)-edge graph path whose graph vertices and edge colors are mutually distinct.

By (2), the desired upper bound
\[
|E(H)|\le \frac{\ell}{3}n \tag{7}
\]
is equivalent to the following colored-graph statement.

## Target theorem

If \(G\) is a properly edge-colored graph satisfying the triangle rule (4) and contains no \(\ell\)-edge path for which all path vertices and edge colors are distinct, then
\[
e(G)\le \ell n. \tag{8}
\]

## Metadata

- ID: the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_path_translation
- Kind: section
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Composition version: 1
- Composition stale: False

## Development tree

- [Subsection 1 — (untitled)](../SUBSECTIONS/the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_path_translation_subsection_a.md) (`the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_path_translation_subsection_a`; development v1; composition v1; stale=False)
- [Subsection 2 — Theorem 2](../SUBSECTIONS/the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_path_translation_subsection_b.md) (`the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_path_translation_subsection_b`; development v1; composition v1; stale=False)
- [Subsection 3 — Target theorem](../SUBSECTIONS/the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_path_translation_subsection_c.md) (`the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_path_translation_subsection_c`; development v1; composition vNone; stale=False)
