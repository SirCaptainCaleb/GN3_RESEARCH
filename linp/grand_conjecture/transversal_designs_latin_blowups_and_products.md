# Article 7 — Transversal designs, Latin blow-ups, and products

---

## Section — Introduction

<!-- section_id: transversal_designs_latin_blow_ups_and_products_introduction -->

This rehearsal asks whether a dense finite \(P_\ell^{(3)}\)-free component can be enlarged while preserving a favorable ratio between edge density and maximum path length.

A transversal design \(TD(3,q)\) has three vertex classes \(A,B,C\), each of size \(q\), and one triple through every pair of vertices from distinct classes. Equivalently, it is obtained from a proper \(q\)-edge-coloring of \(K_{q,q}\): if the edge \(ab\), with \(a\in A\) and \(b\in B\), has color \(c\in C\), then \(\{a,b,c\}\) is a hyperedge.

---

## Section — Rainbow graph paths lift to linear hypergraph paths

<!-- section_id: transversal_designs_latin_blow_ups_and_products_rainbow_graph_paths_lift_to_linear_hypergraph_paths -->

### Lemma 1

Let
\[
v_0v_1\cdots v_r
\]
be a rainbow path in a properly edge-colored graph \(G\). Replace each graph edge \(v_{i-1}v_i\), of color \(c_i\), by the triple
\[
\{v_{i-1},v_i,c_i\}.
\]
If the color set is disjoint from \(V(G)\), these triples form a linear \(r\)-edge hypergraph path.

#### Proof
Consecutive triples meet in \(v_i\). Nonconsecutive graph edges have disjoint endpoint sets because they lie on a graph path, and their colors are distinct because the path is rainbow. Since colors lie outside \(V(G)\), no color can equal a graph-path vertex. Hence nonconsecutive triples are disjoint. ∎

For \(TD(3,q)\), this representation describes all blocks.

The following graph theorem gives the asymptotic behavior of full transversal designs.

### Theorem 2

Every properly \(q\)-edge-colored \(q\)-regular graph using exactly \(q\) colors contains a rainbow path with
\[
q-o(q)
\]
edges.

Consequently every \(TD(3,q)\) contains a linear path with \(q-o(q)\) edges.

Since a \(TD(3,q)\) has \(3q\) vertices and \(q^2\) hyperedges, its edge density is \(q/3\). If \(\ell_q\) is one more than its maximum path length, then
\[
\frac{|E|/|V|}{\ell_q}
\le
\frac{q/3}{q-o(q)}
=
\frac13+o(1). \tag{1}
\]
Thus full transversal designs cannot yield an asymptotic coefficient above one third.

---

## Section — Blow-ups of a fixed linear triple system

<!-- section_id: transversal_designs_latin_blow_ups_and_products_blow_ups_of_a_fixed_linear_triple_system -->

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

### Theorem 3

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

### Corollary 4

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

---

## Section — Repeated lifts with a common color set

<!-- section_id: transversal_designs_latin_blow_ups_and_products_repeated_lifts_with_a_common_color_set -->

A different construction starts with a properly edge-colored graph \(G\) on \(u\) vertices, with color set \(C\). Take \(r\) disjoint copies of \(V(G)\) but use the same color vertices \(C\) for all copies. Every colored edge \(xy\) of color \(c\) becomes a triple \(\{x,y,c\}\).

Let \(H_r\) be the resulting linear \(3\)-graph.

### Theorem 5

If \(H_r\) is \(P_\ell^{(3)}\)-free for arbitrarily large \(r\), then
\[
\frac{|E(G)|}{u}\le \frac{\lceil\ell/2\rceil}{2}. \tag{6}
\]
Consequently the limiting density of \(H_r\) is at most
\[
\frac{\ell}{4}+O(1).
\]

#### Proof
Form the color-adjacency graph \(C_G\): two colors \(a,b\) are adjacent if some vertex of \(G\) is incident with one edge of color \(a\) and one edge of color \(b\).

Suppose
\[
c_0c_1\cdots c_q
\]
is a simple \(q\)-edge path in \(C_G\). For each \(i\), choose a vertex \(v_i\) of \(G\) incident with an edge of color \(c_{i-1}\) and an edge of color \(c_i\). Realize the two-edge configuration around \(v_i\) in the \(i\)-th copy of \(G\). Listing these two lifted hyperedges for \(i=1,\ldots,q\) produces a linear hypergraph path with \(2q\) edges: consecutive two-edge configurations meet at the common color vertex, distinct copies of \(G\) are disjoint, and the simple color path prevents nonconsecutive reuse of a color.

Thus \(C_G\) has no simple path with \(q\) edges when \(2q\ge\ell\).

At a vertex \(v\in V(G)\), proper coloring gives \(d_G(v)\) distinct incident colors. They form a clique \(K_{d_G(v)}\) in \(C_G\), which contains a path with \(d_G(v)-1\) edges. Therefore
\[
2(d_G(v)-1)<\ell,
\]
and hence
\[
d_G(v)\le \lceil\ell/2\rceil.
\]
Averaging gives (6).

Finally
\[
|V(H_r)|=ru+|C|,
\qquad
|E(H_r)|=r|E(G)|,
\]
so the density tends to \(|E(G)|/u\) as \(r\to\infty\). ∎

Hence repeated use of a fixed color set is asymptotically weaker than the one-third construction.

A one-factorization lift of \(K_N\) is a special case. A sufficiently large properly edge-colored complete graph contains a rainbow path with \(N-2\) edges, and by Lemma 1 this produces a linear path of length \(N-2\) in the corresponding hypergraph. Thus the small exceptional one-factorization examples do not scale.

---

## Section — Cartesian products

<!-- section_id: transversal_designs_latin_blow_ups_and_products_cartesian_products -->

For linear \(3\)-graphs \(H\) and \(K\), define their Cartesian product on \(V(H)\times V(K)\) by taking edges of the forms
\[
e\times\{y\}\qquad(e\in E(H),\ y\in V(K))
\]
and
\[
\{x\}\times f\qquad(x\in V(H),\ f\in E(K)).
\]

### Theorem 6

If \(H\) contains a linear path with \(a\) edges and \(K\) contains one with \(b\) edges, then \(H\square K\) contains a linear path with
\[
(a+1)(b+1)-1 \tag{7}
\]
edges.

#### Proof
Let
\[
E_1,\ldots,E_a
\]
be a path in \(H\), with distinct endpoint vertices \(p,q\), and let
\[
F_1,\ldots,F_b
\]
be a path in \(K\). Choose successive path vertices
\[
y_0,y_1,\ldots,y_b
\]
so that \(y_{i-1},y_i\in F_i\).

For each \(i=0,\ldots,b\), place a copy of the \(H\)-path in the fibre over \(y_i\), reversing its orientation on alternate fibres. Between the copies over \(y_{i-1}\) and \(y_i\), insert the edge
\[
\{s_i\}\times F_i,
\]
where \(s_i\) alternates between \(p\) and \(q\).

There are \((b+1)a\) edges inside the \(H\)-fibres and \(b\) connecting edges, giving (7). Consecutive pieces meet in exactly the prescribed vertex. Distinct fibres are disjoint. A connecting edge meets only the terminal edge of either neighboring fibre path, and nonconsecutive connecting edges are disjoint because either their \(H\)-coordinates differ or the corresponding \(K\)-edges are nonconsecutive. Hence the displayed sequence is a linear path. ∎

### Corollary 7

Let \(H\) have \(n\) vertices, \(m\) edges, and maximum path length \(L\). Its \(t\)-fold Cartesian power has density
\[
t\frac mn
\]
and maximum path length at least
\[
(L+1)^t-1.
\]
Consequently its normalized density at the first forbidden path length tends to \(0\) as \(t\to\infty\).

#### Proof
The \(t\)-fold power has \(n^t\) vertices and \(tmn^{t-1}\) edges. Iterate Theorem 6. Then
\[
\frac{tm/n}{(L+1)^t}\to0.
\]
∎

Thus Cartesian powers cannot amplify a finite exceptional component into an asymptotically stronger construction.

---

## Section — The remaining construction problems

<!-- section_id: transversal_designs_latin_blow_ups_and_products_the_remaining_construction_problems -->

The preceding theorems leave two mathematically distinct possibilities.

### Open problem A

Find a finite linear \(3\)-graph \(T\) with \(v\) vertices, \(m\) edges, and linear circumference \(s(T)\) satisfying
\[
s(T)<\frac{3m}{v}, \tag{8}
\]
and construct blow-ups for which the longest path has length only
\[
s(T)q+o(q).
\]

Theorem 3 shows that \(s(T)q-o(q)\) is unavoidable; the problem is whether all other paths can also be kept at that scale.

### Open problem B

Construct a partial or nonregular transversal system with nearly quadratic many triples in its three classes but without the long rainbow paths forced by full transversal designs.

Such a construction must lose few edges while destroying a linear proportion of the compatible lifted paths. Independent full Latin squares cannot do this by Theorem 3, and repeated use of a common fixed color set cannot do it by Theorem 5.

The unresolved lower-bound problem in this family is therefore not to choose a different Latin square inside the same regular construction, but to change the global incidence structure so that the large family of internally disjoint lifted paths no longer exists.
