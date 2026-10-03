# Blow-ups of a fixed linear triple system

## Body

Let \(T\) be a fixed linear \(3\)-graph with \(v\) vertices and \(m\) edges. Replace every vertex \(x\in V(T)\) by a class \(X_x\) of \(q\) vertices. For each hyperedge \(\{x,y,z\}\in E(T)\), place an arbitrary \(TD(3,q)\) on
\[
X_x\cup X_y\cup X_z.
\]
Call the resulting hypergraph \(T(q)\). Then
\[
|V(T(q))|=qv,
\qquad
|E(T(q))|=q^2m. \tag{2}
\]

A cycle in \(T\) produces a long path in every such blow-up, independently of the chosen Latin squares.

## Theorem 3

Suppose \(T\) contains a linear cycle with \(s\) edges. Then every blow-up \(T(q)\) described above contains a linear path with
\[
sq-o(q) \tag{3}
\]
edges.

#### Proof
Write the base cycle as
\[
E_1,\ldots,E_s.
\]
Let
\[
X_0,\ldots,X_{s-1}
\]
be the classes corresponding to its successive joints, and let
\[
P_1,\ldots,P_s
\]
be the classes corresponding to its private vertices.

Label
\[
X_0=\{a_0,\ldots,a_{q-1}\}
\]
cyclically. For a fixed index \(t\), seek an \(s\)-edge lifted path from \(a_t\) to \(a_{t+1}\) following the base cycle. Once one vertex is chosen in each intermediate joint class
\[
X_1,\ldots,X_{s-1},
\]
the Latin-square relations on the \(s\) base edges determine the corresponding private vertices. Hence each prescribed pair \(a_t,a_{t+1}\) has exactly
\[
q^{s-1}
\]
lifted realizations.

Each realization uses one vertex in each of the \(s-1\) intermediate joint classes and one vertex in each of the \(s\) private classes, altogether \(2s-1\) internal vertices. Fixing one internal vertex removes one degree of freedom, so it lies in \(O(q^{s-2})\) realizations for a fixed prescribed pair. Fixing two internal vertices leaves at most \(O(q^{s-3})\) realizations.

Choose \(h=(1-o(1))q\) successive pairs
\[
(a_0,a_1),\ldots,(a_{h-1},a_h).
\]
Consider the \(2s\)-uniform auxiliary hypergraph whose vertices consist of these \(h\) prescribed pairs and the internal vertices of the blow-up, and whose hyperedges are the possible lifted realizations. The prescribed-pair degrees are \(q^{s-1}\); the internal degrees are asymptotically of the same order after restriction to \(h=(1-o(1))q\) pairs; and all pair-codegrees are \(o(q^{s-1})\).

We use the following fixed-uniformity matching principle: if an \(r\)-uniform hypergraph has vertex degrees \((1+o(1))D\), with \(D\to\infty\), and every pair of vertices has codegree \(o(D)\), then it has a matching covering all but an \(o(1)\)-fraction of its vertices. Applied to the auxiliary hypergraph above, this selects mutually internally disjoint realizations for all but \(o(q)\) prescribed pairs. The remaining \(o(q)\) pairs may be repaired greedily: each has \(\Theta(q^{s-1})\) realizations, while the already used \(o(q)\) internal vertices exclude only \(o(q^{s-1})\) of them.

We thus obtain one internally disjoint lifted \(s\)-edge path from \(a_t\) to \(a_{t+1}\) for every \(0\le t<h\). Concatenating these paths yields a single linear path with
\[
sh=sq-o(q)
\]
edges. ∎

## Corollary 4

Let \(s(T)\) be the maximum number of edges in a linear cycle of \(T\). Then every arbitrary Latin blow-up of \(T\) has normalized density at most
\[
\frac{m}{v\,s(T)}+o(1). \tag{4}
\]

#### Proof
By Theorem 3, the maximum path length of \(T(q)\) is at least
\[
s(T)q-o(q).
\]
Using (2),
\[
\frac{|E(T(q))|/|V(T(q))|}{s(T)q-o(q)}
=
\frac{mq/v}{s(T)q-o(q)}
=
\frac{m}{v\,s(T)}+o(1).
\]
∎

Therefore an arbitrary Latin blow-up can exceed the one-third scale only if its base hypergraph satisfies
\[
s(T)<\frac{3m}{v}. \tag{5}
\]

This converts the amplification problem into a finite structural problem about the density and circumference of the base hypergraph.

## Metadata

- ID: transversal_designs_latin_blow_ups_and_products_blow_ups_of_a_fixed_linear_triple_system
- Kind: line
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted

## Authoring state

- Chunk 1 — crystallized, version 1: (untitled)
- Chunk 2 — crystallized, version 1: Theorem 3
- Chunk 3 — HOT, version 1: Corollary 4
