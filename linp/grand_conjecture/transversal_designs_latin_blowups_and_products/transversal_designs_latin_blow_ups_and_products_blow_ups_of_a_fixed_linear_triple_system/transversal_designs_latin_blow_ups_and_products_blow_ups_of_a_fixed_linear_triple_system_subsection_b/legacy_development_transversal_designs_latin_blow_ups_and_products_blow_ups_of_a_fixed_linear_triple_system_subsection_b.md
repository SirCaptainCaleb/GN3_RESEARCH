# Theorem 3 — preserved pre-item development

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
