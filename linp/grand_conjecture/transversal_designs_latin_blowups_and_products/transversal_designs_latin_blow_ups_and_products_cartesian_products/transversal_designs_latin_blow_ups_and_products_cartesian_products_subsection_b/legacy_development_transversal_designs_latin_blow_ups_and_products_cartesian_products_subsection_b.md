# Theorem 6 — preserved pre-item development

## Development

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
