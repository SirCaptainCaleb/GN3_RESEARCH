# Rainbow graph paths lift to linear hypergraph paths

## Lemma 1

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

## Theorem 2

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
