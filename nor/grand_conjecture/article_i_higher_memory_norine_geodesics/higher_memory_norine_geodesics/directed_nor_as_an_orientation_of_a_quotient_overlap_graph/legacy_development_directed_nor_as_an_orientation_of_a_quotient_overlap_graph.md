# Directed sector as an orientation of a quotient overlap graph — preserved pre-item development

## Composition

(none yet)

## Development

## Quotient-overlap orientation model for the directed sector

Fix a coordinate-label arity \(r\ge2\), so this is the translation-invariant directed sector of \(N_{r+1}\). Let \(\mathcal G_{n,r}\) be the graph whose vertices are reversal-orbits
\[
[a_1,\ldots,a_{r-1}]
=
\{(a_1,\ldots,a_{r-1}),(a_{r-1},\ldots,a_1)\}
\]
of injective ordered \((r-1)\)-tuples.

Every reversal-orbit of an injective ordered \(r\)-tuple
\[
t=(a_1,\ldots,a_r)
\]
defines an edge joining
\[
[a_1,\ldots,a_{r-1}]
\quad\text{and}\quad
[a_2,\ldots,a_r].
\]
Using the reversed representative
\[
t^{\mathrm{rev}}=(a_r,\ldots,a_1)
\]
swaps these two endpoints, so the underlying edge is well defined. It is harmless to regard \(\mathcal G_{n,r}\) as a multigraph.

Now let
\[
h(a_1,\ldots,a_r)\in\{0,1\},
\qquad
h(a_r,\ldots,a_1)=1-h(a_1,\ldots,a_r).
\]
Orient the edge represented by \(t\) from
\[
[a_1,\ldots,a_{r-1}]
\longrightarrow
[a_2,\ldots,a_r]
\]
when
\[
h(a_1,\ldots,a_r)=0.
\]
This is well defined: replacing \(t\) by \(t^{\mathrm{rev}}\) swaps the endpoints and complements the color, producing the same edge orientation.

Conversely, every orientation of \(\mathcal G_{n,r}\) determines a reversal-antisymmetric binary coloring of ordered \(r\)-tuples. Thus directed translation-invariant coordinate colorings are exactly orientations of this quotient-overlap graph.

### Coordinate permutations become distinguished paths

For a permutation
\[
\pi=(v_1,\ldots,v_n),
\]
define
\[
z_i=[v_i,\ldots,v_{i+r-2}],
\qquad
1\le i\le n-r+2.
\]
Then
\[
z_1,z_2,\ldots,z_{n-r+2}
\]
is a path in \(\mathcal G_{n,r}\). Its \(i\)-th edge is the reversal-orbit of
\[
(v_i,\ldots,v_{i+r-1}).
\]

Along this distinguished path, the coordinate color is \(0\) exactly when the edge orientation agrees with the traversal direction, and is \(1\) exactly when it opposes the traversal direction.

Therefore the directed-sector target is equivalent to finding a coordinate-permutation path whose edge directions change relative to the traversal at most once.

Equivalently, there is a vertex \(z_j\) of the distinguished path such that every oriented edge of the path points toward \(z_j\), or every oriented edge points away from \(z_j\). Constant words are included by allowing the pivot at an endpoint.

So the directed sector of \(N_{r+1}\) can be restated as follows:

> Every orientation of \(\mathcal G_{n,r}\) contains a coordinate-permutation path that is an oriented in-\(V\) or out-\(V\): its two arms are directed toward one pivot state or away from one pivot state.

### Low-arity specializations

For \(r=2\), reversal-orbits of one-tuples are just the ground vertices and
\[
\mathcal G_{n,2}=K_n.
\]
A directed coordinate coloring is exactly a tournament orientation. A directed Hamilton path gives a constant word.

For \(r=3\), reversal-orbits of ordered pairs are unordered pairs. Hence the vertices of \(\mathcal G_{n,3}\) are the edges of \(K_n\). A triple
\[
(a,b,c)
\]
joins the states \(\{a,b\}\) and \(\{b,c\}\), so
\[
\mathcal G_{n,3}\cong L(K_n).
\]
Thus an arbitrary directed ternary coordinate coloring—hence the directed translation-invariant sector of \(N_4\)—is exactly an arbitrary orientation of the line graph \(L(K_n)\).

A coordinate permutation
\[
(v_1,\ldots,v_n)
\]
corresponds to the edge-sequence
\[
v_1v_2,\ v_2v_3,\ldots,v_{n-1}v_n
\]
of a Hamilton path of \(K_n\). Consequently the directed ternary conjecture is equivalent to:

> Every orientation of \(L(K_n)\) contains the edge-sequence of some Hamilton path of \(K_n\) such that all oriented line-graph edges along that sequence point toward one pivot edge or all point away from one pivot edge.

This also recovers the center-indexed tournament picture: for each \(b\), the clique of line-graph vertices \(\{ab:a\ne b\}\) is oriented as a tournament, and the problem asks to synchronize these star tournaments along one Hamilton path of \(K_n\).

### Why this may help

This formulation removes the binary-word syntax and exposes the target as a path-orientation problem. It suggests path-cover, longest-path, line-graph, and pivot arguments directly, while keeping the global restriction that only paths arising from ground-set permutations are admissible.
