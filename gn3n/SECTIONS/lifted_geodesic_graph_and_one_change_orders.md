# The lifted geodesic graph and one-change orders

**Summary:** The tournament problem is exactly a one-color-change geodesic problem in an antipodally colored graph lying over the cube.

## Statement

A fixed antipodal graph Γ_n remembers the previous and next cube directions. Its pole geodesics are exactly spanning vertex orders, and their edge-color words are the boundary-tournament triple-status words with complementary endpoint colors.

## Cold composition

## The memory-lift graph Γ_n

The staircase triangulation identifies spanning orders with cube geodesics, but the color at one step depends on three successive directions. Introduce a graph \(\Gamma_n\) that stores this two-step memory.

Its vertices are poles \(s,t\) and states
\[
(\sigma,S,u,v),
\]
where \(\sigma\in\{0,1\}\), \(u\ne v\), and \(S\subseteq V\setminus\{u,v\}\). Give the state rank \(|S|+1\), with \(r(s)=0\) and \(r(t)=n\). Join \(s\) to every \((\sigma,\varnothing,u,v)\); join
\[
(\sigma,S,u,v)\longrightarrow(\sigma,S\cup\{u\},v,w)
\]
whenever \(w\notin S\cup\{u,v\}\); and join every rank-\(n-1\) state to \(t\).

Color a source edge by \(\sigma\), an internal edge by \(h(u,v,w)\), and a terminal edge by \(1-\sigma\). The underlying graph depends only on \(n\).

## Antipodal involution and cube projection

Define
\[
A(s)=t,\qquad A(t)=s,
\]
and
\[
A(\sigma,S,u,v)=
(\sigma,V\setminus(S\cup\{u,v\}),v,u).
\]
This is a fixed-point-free graph involution. For an internal edge carrying the triple \(u,v,w\), the antipodal edge, read in increasing-rank direction, carries \(w,v,u\); hence its color is complementary by boundary reversal. Source and terminal edges are likewise paired with complementary colors.

There is also an antipodal graph map to the cube,
\[
p(s)=\varnothing,\qquad p(t)=V,\qquad
p(\sigma,S,u,v)=S\cup\{u\}.
\]
Every \(\Gamma_n\) edge projects to a cube edge and \(p(Ax)=V\setminus p(x)\). Thus \(\Gamma_n\) is a finite memory lift of the cube rather than an unrelated auxiliary graph.

## Pole geodesics are spanning orders

Every edge changes rank by one, so \(d(s,t)\ge n\). For every permutation \(\pi=(v_1,\ldots,v_n)\) and each \(\sigma\), there is a length-\(n\) path
\[
s,\quad
(\sigma,S_i,v_{i+1},v_{i+2})\quad(0\le i\le n-2),\quad
t.
\]
Conversely, every \(s\)-\(t\) geodesic must increase rank at every step, so it chooses each label exactly once and hence determines a unique permutation and copy index.

Therefore the pole geodesics are in bijection with pairs \((\sigma,\pi)\), and their color words are
\[
\sigma,\quad h(v_1,v_2,v_3),\ldots,
h(v_{n-2},v_{n-1},v_n),\quad1-\sigma.
\]

It follows immediately that \(H\) has a spanning order whose consecutive-triple statuses change at most once if and only if \(\Gamma_n\) has a pole geodesic with at most one edge-color change. Deleting the two artificial endpoint colors gives one direction; choosing \(\sigma\) to match the first run gives the other.

## Why geodesicity is essential

For any \(s\)-\(t\) walk \(W\), let \(m_v\) be the number of times its projection uses cube coordinate \(v\). Since the projection joins antipodal cube vertices, every \(m_v\) is odd and
\[
|W|=\sum_{v\in V}m_v
=n+2\sum_{v\in V}\frac{m_v-1}{2}.
\]
Thus the geodesics are exactly the walks with \(m_v=1\) for every \(v\).

This is the key constraint behind the analogy with antipodal path theorems. A theorem producing some one-change antipodal walk is insufficient if it allows repeated coordinates; repetition means repeated original vertices. Likewise, an antipodal theorem whose endpoint pair is allowed to vary is insufficient unless its output can be normalized to the distinguished poles \(s,t\). The desired topology must preserve both pole location and zero detour.

## Metadata

- ID: lifted_geodesic_graph_and_one_change_orders
- Kind: section
- Version: 12
- Math version: 4
- Audit: unaudited
- Refutation: unrefuted
- Composition version: 1
- Composition stale: False

## Development tree

- [Subsection 1 — The memory-lift graph Γ_n](../SUBSECTIONS/lifted_geodesic_graph_and_one_change_orders_subsection_a.md) (`lifted_geodesic_graph_and_one_change_orders_subsection_a`; development v4; composition v1; stale=False)
- [Subsection 2 — Antipodal involution and cube projection](../SUBSECTIONS/lifted_geodesic_graph_and_one_change_orders_subsection_b.md) (`lifted_geodesic_graph_and_one_change_orders_subsection_b`; development v4; composition v1; stale=False)
- [Subsection 3 — Pole geodesics are spanning orders](../SUBSECTIONS/lifted_geodesic_graph_and_one_change_orders_subsection_c.md) (`lifted_geodesic_graph_and_one_change_orders_subsection_c`; development v4; composition v1; stale=False)
- [Subsection 4 — Why geodesicity is essential](../SUBSECTIONS/lifted_geodesic_graph_and_one_change_orders_subsection_d.md) (`lifted_geodesic_graph_and_one_change_orders_subsection_d`; development v3; composition vNone; stale=False)
