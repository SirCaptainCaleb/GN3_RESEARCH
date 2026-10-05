# Repeated colors are a genuine obstruction

## Cold composition

An ordinary long path in the full shadow need not contain a long linear hypergraph path.

## Proposition 7

For every \(t\), there is a linear \(3\)-graph whose full shadow contains the graph path
\[
x_0x_1\cdots x_t
\]
but every linear hypergraph path has at most four edges.

#### Proof
Take distinct vertices
\[
x_0,\ldots,x_t,z,w.
\]
For \(1\le i\le t\), define
\[
e_i=
\begin{cases}
\{x_{i-1},x_i,z\},&i\text{ odd},\\
\{x_{i-1},x_i,w\},&i\text{ even}.
\end{cases}
\tag{13}
\]
The system is linear. Consecutive edges meet in the corresponding \(x_i\) and use different vertices \(z,w\). Two nonconsecutive odd edges meet only in \(z\); two nonconsecutive even edges meet only in \(w\); nonconsecutive edges of opposite parity are disjoint.

The full shadow contains every graph edge \(x_{i-1}x_i\), giving the displayed graph path. Its edge colors alternate \(z,w\).

Any linear hypergraph path can contain at most two odd-indexed edges, because three such edges would include two nonconsecutive path edges both containing \(z\). If two odd-indexed edges occur, they must be consecutive in the hypergraph path. The same argument applies to the even-indexed edges through \(w\). Therefore every linear path has at most four edges. ∎

Thus no positive proportion of an arbitrary ordinary shadow path can be extracted without using the colors.

The same example explains the precise difficulty in Theorem 2: the graph vertices \(x_i\) are all distinct, but the colors repeat heavily.

## Metadata

- ID: the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_repeated_colors_are_a_genuine_obstruction
- Kind: section
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Composition version: 1
- Composition stale: False

## Development tree

- [Subsection 1 — (untitled)](../SUBSECTIONS/the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_repeated_colors_are_a_genuine_obstruction_subsection_a.md) (`the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_repeated_colors_are_a_genuine_obstruction_subsection_a`; development v1; composition v1; stale=False)
- [Subsection 2 — Proposition 7](../SUBSECTIONS/the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_repeated_colors_are_a_genuine_obstruction_subsection_b.md) (`the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_repeated_colors_are_a_genuine_obstruction_subsection_b`; development v1; composition vNone; stale=True)
