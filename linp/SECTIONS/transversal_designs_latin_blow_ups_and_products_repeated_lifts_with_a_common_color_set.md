# Repeated lifts with a common color set

## Body

A different construction starts with a properly edge-colored graph \(G\) on \(u\) vertices, with color set \(C\). Take \(r\) disjoint copies of \(V(G)\) but use the same color vertices \(C\) for all copies. Every colored edge \(xy\) of color \(c\) becomes a triple \(\{x,y,c\}\).

Let \(H_r\) be the resulting linear \(3\)-graph.

## Theorem 5

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

## Metadata

- ID: transversal_designs_latin_blow_ups_and_products_repeated_lifts_with_a_common_color_set
- Kind: section
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted

## Authoring state

- Subsection 1 — crystallized, version 1: (untitled)
- Subsection 2 — HOT, version 1: Theorem 5
