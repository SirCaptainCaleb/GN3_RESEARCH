# Lemma 6

## Metadata

- ID: the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_a_source_oriented_representation_subsection_c
- Parent Section: the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_a_source_oriented_representation
- Position: 3
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

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
