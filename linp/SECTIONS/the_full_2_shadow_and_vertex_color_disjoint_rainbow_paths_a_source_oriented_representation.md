# A source-oriented representation

## Cold composition

A second representation keeps one distinguished vertex of every hyperedge.

For each hyperedge \(T=\{x,y,z\}\), choose one vertex \(\sigma(T)\) as its source. If \(\sigma(T)=x\), draw the directed arcs
\[
x\to y,\qquad x\to z,
\]
and place the graph edge \(yz\) with color \(x\).

Let \(D\) be the resulting digraph and \(J\) the resulting properly edge-colored graph.

For a vertex \(v\), let \(s(v)\) be the number of hyperedges sourced at \(v\), and let \(h(v)\) be the number containing \(v\) as a nonsource vertex.

## Lemma 5

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

## Lemma 6

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

## Metadata

- ID: the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_a_source_oriented_representation
- Kind: section
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Composition version: 1
- Composition stale: False

## Development tree

- [Subsection 1 — (untitled)](../SUBSECTIONS/the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_a_source_oriented_representation_subsection_a.md) (`the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_a_source_oriented_representation_subsection_a`; development v1; composition v1; stale=False)
- [Subsection 2 — Lemma 5](../SUBSECTIONS/the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_a_source_oriented_representation_subsection_b.md) (`the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_a_source_oriented_representation_subsection_b`; development v1; composition v1; stale=False)
- [Subsection 3 — Lemma 6](../SUBSECTIONS/the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_a_source_oriented_representation_subsection_c.md) (`the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_a_source_oriented_representation_subsection_c`; development v1; composition vNone; stale=False)
