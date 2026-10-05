# Lemma 1

## Metadata

- ID: terminal_pair_cycles_and_rotations_the_special_edge_inequality_subsection_b
- Parent Section: terminal_pair_cycles_and_rotations_the_special_edge_inequality
- Position: 2
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Cold composition

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

## Development

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
