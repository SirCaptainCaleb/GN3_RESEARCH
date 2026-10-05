# Article 8 — The full 2-shadow and vertex-color-disjoint rainbow paths

## Composition status

- Composition version: 1
- Stale: False
- Composed through revision: 402

## Cold composition

---

## Section — Introduction

<!-- section_id: the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_introduction -->

Let \(H\) be a finite linear \(3\)-graph. Its full \(2\)-shadow is the graph \(G\) on \(V(H)\) obtained by replacing every hyperedge
\[
\{x,y,z\}
\]
by the three graph edges
\[
xy,\quad xz,\quad yz.
\]
Color these three graph edges by
\[
c(xy)=z,\qquad c(xz)=y,\qquad c(yz)=x. \tag{1}
\]

Linearity makes the coloring well defined: a graph edge \(xy\) belongs to at most one hyperedge of \(H\).

The objective is to translate the one-third upper bound into a path problem in this colored graph.

---

## Section — Basic properties of the full shadow

<!-- section_id: the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_basic_properties_of_the_full_shadow -->

### Lemma 1

The coloring (1) is proper. Moreover,
\[
e(G)=3|E(H)| \tag{2}
\]
and, for every vertex \(v\),
\[
d_G(v)=2d_H(v). \tag{3}
\]

#### Proof
If two shadow edges \(xy\) and \(xw\) had the same color \(z\), then the corresponding hyperedges
\[
\{x,y,z\},\qquad \{x,w,z\}
\]
would share the two vertices \(x,z\), contrary to linearity. Thus the coloring is proper.

Every hyperedge contributes its three distinct pairs, and distinct hyperedges share no pair, proving (2).

Every hyperedge through \(v\) contributes exactly the two shadow edges joining \(v\) to its other two vertices. Distinct hyperedges through \(v\) cannot reuse a shadow neighbor, so these \(2d_H(v)\) graph edges are distinct. This proves (3). ∎

The coloring has additional symmetry: if \(c(xy)=z\), then
\[
c(xz)=y,\qquad c(yz)=x. \tag{4}
\]
Thus every hyperedge appears as a triangle whose edge colors are the opposite vertices.

---

## Section — Path translation

<!-- section_id: the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_path_translation -->

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

### Theorem 2

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

### Target theorem

If \(G\) is a properly edge-colored graph satisfying the triangle rule (4) and contains no \(\ell\)-edge path for which all path vertices and edge colors are distinct, then
\[
e(G)\le \ell n. \tag{8}
\]

---

## Section — Separating graph vertices from colors

<!-- section_id: the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_separating_graph_vertices_from_colors -->

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

### Lemma 3

Every rainbow path in \(J\) lifts to a linear hypergraph path of the same length in \(H\).

#### Proof
All path vertices lie in \(A\), while all colors lie in \(B\), so no color equals a path vertex. The rainbow condition makes the colors distinct. A graph path already has distinct path vertices. Hence Theorem 2 applies. ∎

### Proposition 4

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

### Degree bookkeeping across the shadow reduction

The hypergraph degree and the degree in a retained properly edge-colored shadow graph are separate quantities. Equation (3) gives d_G(v)=2d_H(v) only for the full shadow G. After passing to a retained graph J, or to a further graph-side core, a rainbow-path theorem whose hypothesis is stated in terms of minimum graph degree must be applied using the degree in that graph, not d_H. Conversely, a hypergraph-side minimum-degree hypothesis remains available for hypergraph peeling, attachment, or special-edge arguments. The two degree conditions serve different parts of the proof and should be tracked simultaneously rather than identified.

---

## Section — A source-oriented representation

<!-- section_id: the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_a_source_oriented_representation -->

A second representation keeps one distinguished vertex of every hyperedge.

For each hyperedge \(T=\{x,y,z\}\), choose one vertex \(\sigma(T)\) as its source. If \(\sigma(T)=x\), draw the directed arcs
\[
x\to y,\qquad x\to z,
\]
and place the graph edge \(yz\) with color \(x\).

Let \(D\) be the resulting digraph and \(J\) the resulting properly edge-colored graph.

For a vertex \(v\), let \(s(v)\) be the number of hyperedges sourced at \(v\), and let \(h(v)\) be the number containing \(v\) as a nonsource vertex.

### Lemma 5

For every vertex \(v\),
\[
\frac12 d_D^+(v)+d_D^-(v)=d_H(v). \tag{10}
\]

#### Proof
Every hyperedge through \(v\) places \(v\) in exactly one of two roles. If \(v\) is the source, it contributes one to \(s(v)\); otherwise it contributes one to \(h(v)\). Hence
\[
s(v)+h(v)=d_H(v).
\]
Each source hyperedge contributes two distinct outgoing arcs, so
\[
d_D^+(v)=2s(v).
\]
Each nonsource occurrence corresponds to exactly one incoming arc, so
\[
d_D^-(v)=h(v).
\]
Substitution gives (10). ∎

Longest directed paths force complementary degree information at their ends.

### Lemma 6

Let
\[
v_0v_1\cdots v_p
\]
be a longest directed path in \(D\). If \(d_H(v)\ge d\) for every vertex, then
\[
h(v_p)\ge d-\frac p2 \tag{11}
\]
and
\[
s(v_0)\ge d-p. \tag{12}
\]

#### Proof
Every out-neighbor of \(v_p\) lies on the directed path, otherwise the path extends. Hence
\[
d_D^+(v_p)\le p,
\]
so
\[
s(v_p)\le p/2.
\]
Since \(s(v_p)+h(v_p)=d_H(v_p)\ge d\), this gives (11).

Now consider a graph edge \(v_0x\) of \(J\) with color \(u\). The parent hyperedge is sourced at \(u\), so \(D\) contains the arc
\[
u\to v_0.
\]
If \(u\notin\{v_0,\ldots,v_p\}\), this arc extends the directed path at its beginning, contradicting maximality. Hence every color on an edge of \(J\) incident with \(v_0\) belongs to the directed path. Properness makes these colors distinct, so
\[
h(v_0)=d_J(v_0)\le p.
\]
Therefore
\[
s(v_0)=d_H(v_0)-h(v_0)\ge d-p.
\]
∎

This representation yields a directed-path versus rainbow-path dichotomy, but the resulting quantitative bounds remain far from (8). Its role is to show that concentrated source reuse cannot be ignored.

---

## Section — Repeated colors are a genuine obstruction

<!-- section_id: the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_repeated_colors_are_a_genuine_obstruction -->

An ordinary long path in the full shadow need not contain a long linear hypergraph path.

### Proposition 7

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

---

## Section — The remaining theorem

<!-- section_id: the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_the_remaining_theorem -->

The full-shadow approach is reduced to Target theorem (8).

A proof must distinguish between two regimes.

If a long graph path uses mostly distinct colors and few colors coincide with nonincident path vertices, then Theorem 2 nearly gives the required hypergraph path directly.

If a small set of colors occurs many times, the triangle rule (4) implies that these colors are actual hypergraph vertices incident with many corresponding pairs. One must use the other two edges of the colored triangles to find a different path with more distinct colors.

### Open problem

Prove that every properly edge-colored graph satisfying the triangle rule (4) and
\[
e(G)>\ell n
\]
contains an \(\ell\)-edge path
\[
x_0x_1\cdots x_\ell
\]
such that the \(2\ell+1\) vertices
\[
x_0,\ldots,x_\ell,
c(x_0x_1),\ldots,c(x_{\ell-1}x_\ell)
\]
are all distinct.

By Theorem 2 and (2), this statement is exactly the one-third upper bound.

General rainbow-path theorems cannot supply it because Proposition 4 loses a factor two, and ordinary graph-path extraction cannot supply it because of Proposition 7. The remaining argument must use the symmetric triangle structure of the full shadow to control repeated colors.

## Contained Sections

- 1. [Introduction](../SECTIONS/the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_introduction.md) (`the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_introduction`; composition v1; stale=False)
- 2. [Basic properties of the full shadow](../SECTIONS/the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_basic_properties_of_the_full_shadow.md) (`the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_basic_properties_of_the_full_shadow`; composition v1; stale=False)
- 3. [Path translation](../SECTIONS/the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_path_translation.md) (`the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_path_translation`; composition v1; stale=False)
- 4. [Separating graph vertices from colors](../SECTIONS/the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_separating_graph_vertices_from_colors.md) (`the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_separating_graph_vertices_from_colors`; composition v1; stale=False)
- 5. [A source-oriented representation](../SECTIONS/the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_a_source_oriented_representation.md) (`the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_a_source_oriented_representation`; composition v1; stale=False)
- 6. [Repeated colors are a genuine obstruction](../SECTIONS/the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_repeated_colors_are_a_genuine_obstruction.md) (`the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_repeated_colors_are_a_genuine_obstruction`; composition v1; stale=False)
- 7. [The remaining theorem](../SECTIONS/the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_the_remaining_theorem.md) (`the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_the_remaining_theorem`; composition v1; stale=False)
