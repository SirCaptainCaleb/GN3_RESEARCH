# The special-edge inequality

## Body

Form the snake digraph of \(H\): for every edge \(e\) and every vertex \(v\in e\) with
\[
\phi(e,v)=\phi(e),
\]
include the incidence \((e,v)\). A special edge contributes three such incidences; a nonspecial edge contributes exactly two.

## Lemma 1

For every vertex \(v\),
\[
d^-_{\mathrm{snake}}(v)\le 2\phi(v)-1. \tag{1}
\]

#### Proof
Put \(p=\phi(v)\) and choose a \(p\)-edge path
\[
P=(g_1,\ldots,g_p)
\]
with last vertex \(v\). Consider an edge \(f\ni v\) for which \(v\) is terminal at \(f\). If \(f\ne g_p\), then \(f\) must contain a vertex of
\[
V(P)\setminus g_p.
\]
Otherwise \(P\) can be continued through \(f\), contradicting the maximality of \(p\). Distinct such edges use distinct vertices of \(V(P)\setminus g_p\), since two edges already share \(v\) and cannot share another vertex. There are \(2p-2\) such vertices, and \(g_p\) itself contributes one further edge. ∎

## Corollary 2

\[
2m+s\le \sum_v(2\phi(v)-1)\le (2\ell-3)n. \tag{2}
\]

#### Proof
Summing (1), every special edge contributes \(3\) and every nonspecial edge contributes \(2\). Since there are \(s\) special edges,
\[
\sum_v d^-_{\mathrm{snake}}(v)=3s+2(m-s)=2m+s.
\]
The second inequality follows from \(\phi(v)\le\ell-1\). ∎

Thus any lower bound on \(s\) immediately improves the general coefficient.

## Metadata

- ID: terminal_pair_cycles_and_rotations_the_special_edge_inequality
- Kind: line
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted

## Authoring state

- Chunk 1 — crystallized, version 1: (untitled)
- Chunk 2 — crystallized, version 1: Lemma 1
- Chunk 3 — HOT, version 1: Corollary 2
