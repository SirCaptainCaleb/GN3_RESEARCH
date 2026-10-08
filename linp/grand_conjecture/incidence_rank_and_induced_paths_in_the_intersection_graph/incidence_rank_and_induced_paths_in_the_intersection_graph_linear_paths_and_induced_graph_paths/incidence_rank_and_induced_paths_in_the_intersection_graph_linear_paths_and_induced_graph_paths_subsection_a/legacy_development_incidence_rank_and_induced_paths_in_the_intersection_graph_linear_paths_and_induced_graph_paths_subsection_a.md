# Lemma 1 — preserved pre-item development

A sequence of distinct hyperedges
\[
e_1,\ldots,e_t
\]
forms a linear hypergraph path if and only if the corresponding vertices form an induced path in \(F\).

#### Proof
If the hyperedges form a linear path, consecutive edges intersect and nonconsecutive edges are disjoint, so their intersection graph is exactly a graph path.

Conversely, assume \(e_1,\ldots,e_t\) form an induced path in \(F\). Proceed by induction on \(t\). By induction, \(e_1,\ldots,e_{t-1}\) can be ordered as a linear hypergraph path. Let
\[
v=e_{t-1}\cap e_t.
\]
Inducedness implies that \(e_t\) is disjoint from every \(e_i\) with \(i\le t-2\). Linearity implies that
\[
e_t\cap e_{t-1}=\{v\}.
\]
Thus \(e_t\setminus\{v\}\) consists of two new vertices, and appending them after \(v\) extends the hypergraph path. ∎

Hence
\[
H\text{ is }P_\ell^{(3)}\text{-free}
\iff
F\text{ is induced-}P_\ell\text{-free}. \tag{3}
\]
