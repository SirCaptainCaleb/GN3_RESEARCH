# Cartesian products

## Cold composition

For linear \(3\)-graphs \(H\) and \(K\), define their Cartesian product on \(V(H)\times V(K)\) by taking edges of the forms
\[
e\times\{y\}\qquad(e\in E(H),\ y\in V(K))
\]
and
\[
\{x\}\times f\qquad(x\in V(H),\ f\in E(K)).
\]

## Theorem 6

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

## Corollary 7

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

## Metadata

- ID: transversal_designs_latin_blow_ups_and_products_cartesian_products
- Kind: section
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Composition version: 1
- Composition stale: False

## Development tree

- [Subsection 1 — (untitled)](../SUBSECTIONS/transversal_designs_latin_blow_ups_and_products_cartesian_products_subsection_a.md) (`transversal_designs_latin_blow_ups_and_products_cartesian_products_subsection_a`; development v1; composition v1; stale=False)
- [Subsection 2 — Theorem 6](../SUBSECTIONS/transversal_designs_latin_blow_ups_and_products_cartesian_products_subsection_b.md) (`transversal_designs_latin_blow_ups_and_products_cartesian_products_subsection_b`; development v1; composition v1; stale=False)
- [Subsection 3 — Corollary 7](../SUBSECTIONS/transversal_designs_latin_blow_ups_and_products_cartesian_products_subsection_c.md) (`transversal_designs_latin_blow_ups_and_products_cartesian_products_subsection_c`; development v1; composition vNone; stale=True)
