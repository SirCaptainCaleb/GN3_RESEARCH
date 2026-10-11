# Ordered-pair antipodal edge model: a three-step connectivity obstruction

- Stable ID: note_ordered_pair_antipodal_graph_bridge_and_decoding_obstruction_20261011
- Author: unspecified; session provenance retained
- Primary home: article:nori_article_ix_unification
- Labels: obstruction, proved, topological_approach
- Lifecycle: active
- Epistemic status: proved
- Current version: 5
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6176_2
- Updated session: session_nori_r6202_2
- Disposition: none
- Successor: none

## Related references

- article:nori_article_vii_seven_coordinate
- article:nori_article_viii_edges
- article:nori_article_ix_unification

## Research note

Let \(V\) have \(n\ge3\) vertices and let \(b(a,v,c)\in\mathbb F_2\), for pairwise distinct \(a,v,c\), satisfy \(b(c,v,a)=1-b(a,v,c)\). Define the **ordered-pair graph** \(H_V\) with vertex set \(V^{\underline2}=\{(a,v):a\ne v\}\) and an undirected edge \(\{(a,v),(v,c)\}\) for every ordered triple of distinct vertices. Give this edge color \(b(a,v,c)\), and put \(\tau(a,v)=(v,a)\).

**Proposition (faithful odd-edge representation).** The assignment \(b\mapsto c_b\) is a bijection from boundary 3-tournaments on \(V\) to edge colorings of \(H_V\) obeying \(c_b(\tau e)=1-c_b(e)\).

**Proof.** An edge of \(H_V\) determines its ordered triple uniquely: if both orientations furnished the displayed overlap, then \(a=c\), contrary to distinctness. Its image under \(\tau\) is \(\{(c,v),(v,a)\}\), so the antipodal-edge equation is precisely \(b(c,v,a)=1-b(a,v,c)\). Conversely every edge has this form. \(\square\)

**Theorem (antipodal graph connectivity with no tight-path witness).** For every \(n\ge5\) and every boundary 3-tournament \(b\), the edge-colored graph \(H_V\) contains a monochromatic three-edge path from some \(w\) to \(\tau w\). This conclusion can be witnessed entirely by triples with one common middle vertex, and the resulting three-edge path changes direction in the ordered-pair transition digraph.

**Proof.** Fix \(v\in V\). The values \(b(a,v,c)\) orient the complete graph on \(V\setminus\{v\}\), with an arrow \(a\to c\) when \(b(a,v,c)=0\). Since \(|V\setminus\{v\}|\ge4\), this tournament has a transitive triple: some vertex has at least two outneighbors, and the edge between those outneighbors completes a transitive triple. Name it \(u\to a\to w\), with \(u\to w\). Then
\[
(a,v),\quad(v,w),\quad(u,v),\quad(v,a)
\]
is a path of three differently positioned edges of \(H_V\), with colors respectively
\[
b(a,v,w)=0,\qquad b(u,v,w)=0,\qquad b(u,v,a)=0.
\]
Its endpoint is \(\tau(a,v)\). In the natural transition digraph, the first edge is traversed forward, the second backward, and the third forward. The implied original-vertex sequence revisits \(v\), so the graph path cannot be decoded as a vertex-simple tight path. \(\square\)

**Scope.** Cube-edge NORI1 and boundary 3-tournaments both admit representations as antipodally odd edge colorings of graphs with free involutions: \(Q_n\) with coordinate complementation, and \(H_V\) with reversal of ordered pairs. However, the existence of an undirected monochromatic path connecting involution-paired vertices in \(H_V\) is automatic for \(n\ge5\) and has no forced vertex-simple tight-path decoding. Any shared topological carrier must retain the directed transition orientation and used-vertex support for tournament paths; pair-state connectivity alone loses both.

**Quantitative strengthening.** For each \(n\ge5\), at least
\[
 \frac{n(n-1)(n-2)(n-4)}4
\]
distinct monochromatic three-edge paths in \(H_V\) join a state to its reversed state, counting paths with their colors and ordered vertices. Moreover, every transitive triple in a local comparison tournament gives two such paths, of opposite colors, with the same pair of endpoints.

**Proof.** For a transitive local triple \(u\to a\to w\), \(u\to w\), the preceding proof gives the color-zero path
\[
(a,v),(v,w),(u,v),(v,a).
\]
The color-one path
\[
(a,v),(v,u),(w,v),(v,a)
\]
has edge colors \(b(a,v,u)=b(w,v,u)=b(w,v,a)=1\). Different choices of the local middle vertex \(v\) or of the transitive triple yield different ordered paths. In a tournament on \(m=n-1\) vertices, the number of transitive triples equals \(\sum_u\binom{d^+(u)}2\), which by convexity is at least
\[
 m\binom{(m-1)/2}{2}=\frac{m(m-1)(m-3)}8.
\]
Summing over \(n\) local tournaments and counting both color paths gives the stated bound. \(\square\)

Thus even simultaneous red and blue antipodal connectivity on \(\Omega(n^4)\) short witnesses is automatic in this pair-graph model, while those certificates traverse a comparison transition backward. This sharpens the obstruction to transferring graph-level antipodal reachability into simple directed tight paths.

**Linear-length obstruction.** For every \(n\ge5\), each of the two color subgraphs of \(H_V\) contains a simple path of at least
\[
 \left\lceil\frac{n-2}{4}\right\rceil
\]
edges whose every edge represents a triple with the same middle vertex \(v\). Every such path of length at least two necessarily reverses direction between consecutive transitions in the directed ordered-pair graph.

**Proof.** Fix \(v\). Put \(m=n-1\), \(L=\{(a,v):a\ne v\}\), \(R=\{(v,a):a\ne v\}\), and retain only the \(H_V\)-edges between \(L\) and \(R\) arising from triples centered at \(v\). For every unordered pair \(\{a,c\}\subseteq V\setminus\{v\}\), precisely one of \(\{(a,v),(v,c)\}\) and \(\{(c,v),(v,a)\}\) is color zero; the other is color one. Consequently each color graph on \(L\cup R\) has \(\binom m2\) edges and \(2m\) vertices, with average degree \((m-1)/2\).

Any finite graph of average degree \(d\) contains a nonempty subgraph of minimum degree at least \(d/2\): iteratively removing vertices with degree below \(d/2\) cannot delete all vertices, since otherwise fewer than \(d|V|/2=|E|\) edges would be removed. A longest simple path in such a subgraph has at least its minimum degree many edges, because all neighbors of either endpoint lie on that path. This yields \(\lceil(m-1)/4\rceil=\lceil(n-2)/4\rceil\) edges of each color.

Every retained edge joins \(L\) to \(R\) and, as a forward ordered-pair transition, points \(L\to R\). An undirected walk using two consecutive retained edges therefore traverses one forward and the next backward, or vice versa. Hence none of these paths of length at least two decodes to a directed tight path. \(\square\)

This shows that even linear-length monochromatic paths, with all edges distinct and with antipodally paired edge colors, can be forced by single-middle local tournament comparisons and have no corresponding directed tight-path witness.
