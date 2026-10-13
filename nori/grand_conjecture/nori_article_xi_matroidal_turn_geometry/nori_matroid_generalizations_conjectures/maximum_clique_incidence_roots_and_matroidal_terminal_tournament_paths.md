# Maximum-clique incidence roots and matroidal terminal-tournament paths

# Intrinsic largest-clique incidence roots and a terminal-tournament path theorem

Let \(M\) be a finite matroid, let \(\Gamma(M)\) be its basis-exchange graph, and let \(\mathscr K(M)\) be the family of cliques of **maximum cardinality** in \(\Gamma(M)\). Construct the canonical bipartite incidence graph
\[
I(M)=\bigl(\mathcal B(M)\sqcup\mathscr K(M),\ \{BK:B\in K\}\bigr).
\]
An incidence side is called *thin* when every vertex on that side has degree two. Whenever \(I(M)\) is the edge-subdivision of a connected simple graph, denote the graph obtained by suppressing its thin side by \(G(M)\). This construction uses only the basis graph and its maximum cliques; it is invariant under matroid isomorphism.

## Theorem 1 (three intrinsic root reconstructions)

For \(n\ge3\) and \(m\ge3\), the following matroids have thin incidence sides and root graphs:
\[
\begin{array}{c|c|c|c}
M&\Gamma(M)&\text{thin side}&G(M)\\ \hline
\bigoplus_{i=1}^n U_{1,2}&Q_n&\mathscr K(M)&Q_n\\
U_{2,n},\ n\ge5&J(n,2)&\mathcal B(M)&K_n\\
U_{1,m}\oplus U_{1,m}&K_m\square K_m&\mathcal B(M)&K_{m,m}.
\end{array}
\]

**Proof.** The first basis graph is the cube \(Q_n\). Because it is triangle-free, its largest cliques are its edges, each incident with two basis vertices. Thus \(I(M)\) is the edge subdivision of \(Q_n\), with the clique side thin.

For \(U_{2,n}\), bases are unordered pairs \(\{a,b\}\) and adjacent when they share a symbol. Its basis graph is \(J(n,2)=L(K_n)\). Every clique of size at least four consists of pairs sharing a single symbol; the other maximal cliques consist of the three edges of a triangle. For \(n\ge5\), the largest cliques are therefore the \(n\) stars
\[
K_a=\{\{a,b\}:b\ne a\},\qquad a\in[n].
\]
Each basis \(\{a,b\}\) lies in precisely \(K_a,K_b\). Suppressing the basis vertices of \(I(M)\) gives \(K_n\).

For \(U_{1,m}\oplus U_{1,m}\), bases are ordered pairs \((i,j)\in[m]^2\), and exchange replaces one coordinate. The basis graph is \(K_m\square K_m\). Its \(2m\) largest cliques are its rows and columns, and each basis lies in one of each. The incidence root is \(K_{m,m}\). \(\square\)

For any **basis-side thin** instance with a simple root \(G(M)\), the edge \(uv\) of \(G(M)\) is the unique basis \(B\) belonging to the two clique vertices \(u,v\). If two edges of \(G(M)\) meet at \(v\), their bases both lie in the clique \(v\), hence are adjacent in \(\Gamma(M)\). Thus every orientation of the corresponding basis-exchange edges induces a tournament on the incident root edges at \(v\). The restriction is canonical under basis-graph isomorphism and permits cyclic local tournaments.

## Theorem 2 (terminal-tournament path transfer)

Suppose \(M\) has a basis-side thin incidence graph with connected simple root \(G=G(M)\). Orient the edges of \(\Gamma(M)\) arbitrarily. Then \(G\) admits a vertex-simple path \(v_1,\dots,v_L\) whose successive root edges are locally increasing at every common vertex:
\[
(v_iv_{i+1})\longrightarrow(v_{i+1}v_{i+2})
\]
in the induced tournament on the edges incident with \(v_{i+1}\), for every \(i\). Moreover
\[
\boxed{\ \frac{\overline d(G)}2\le (L-1)^2\ },\qquad
L\ge 1+\sqrt{\frac{\overline d(G)}2},
\]
where \(\overline d(G)=2|E(G)|/|V(G)|\). In particular, for \(M=U_{2,n}\), every arbitrary reversal-odd boundary \(3\)-tournament admits a monochromatic vertex-simple tight path on at least \(1+\sqrt{(n-1)/2}\) original vertices.

**Proof.** The root's tournament comparisons are induced by the given basis-graph orientation. Let \(L\) be the maximum order of a vertex-simple positively directed path. For each edge \(e\) of \(G\), let \(\ell(e)\) be the maximum order of a positively directed vertex-simple path ending with \(e\), in either direction. Choose a maximizing path and orient \(e\) toward its terminal vertex. Some root vertex \(v\) receives at least \(\overline d(G)/2\) such chosen orientations.

For \(2\le r\le L\), let \(S_r\) be the set of incoming edges \(uv\) with \(\ell(uv)=r\), and put \(s_r=|S_r|\). The tournament induced among the \(s_r\) edges has an edge with at least \((s_r-1)/2\) outneighbors. Choose its witness path of order \(r\) ending \(uv\). Every outneighbor edge \(vw\) with \(w\) outside that witness path would extend it to a positive vertex-simple path of order \(r+1\), contradicting \(\ell(vw)=r\). Apart from the previous vertex \(u\), at most \(r-2\) original vertices are unavailable. Hence
\[
(s_r-1)/2\le r-2,\qquad s_r\le 2r-3.
\]
Summing gives
\[
\frac{\overline d(G)}2\le\deg^-(v)=\sum_{r=2}^{L}s_r
\le\sum_{r=2}^{L}(2r-3)=(L-1)^2.
\]
For \(U_{2,n}\), the reconstruction gives \(G=K_n\) and \(\overline d(G)=n-1\); an arbitrary orientation of each Johnson star encodes an arbitrary reversal-odd middle-vertex tournament. Root vertex-simplicity is the distinct-symbol condition for the corresponding tight path. \(\square\)

## Interpretation and limitation

Both initial matroids lie in the intrinsic class for which the largest-clique incidence graph is a subdivision of a simple graph. Their thin sides, however, differ. In the rank-two uniform family, bases become *edges* of the root and their overlapping exchanges define arbitrary local tournaments. In the cubical family, largest cliques become *edges* of the root; the original two-color antipodal condition belongs to the root-edge data, with the coordinate classes recoverable from opposite edges of its squares.

Thus Theorem 2 supplies the quantitative square-root mechanism for the boundary family, while the cubical instance instead falls under the properly resource-labeled terminal-path theorem already established in Article VII. The latter provides a coordinate-distinct increasing geodesic of order at least \((5+\sqrt{1+4n})/4\), after locally ordering the two edge colors, but does not yield a full monochromatic antipodal geodesic. The incidence reconstruction is a common intrinsic geometry, not yet a unified full-strength existence conjecture.

The condition alone also does not force one-switch spanning paths: the matroid \(U_{1,3}\oplus U_{1,3}\) lies in the class and has root \(K_{3,3}\); a nine-edge globally ordered tournament instance admits no Hamilton path with at most one change of turn-color (see the scoped research note 'Rook-graph counterexample to incidence-gallery one-switch spanning'). Any stronger common conjecture needs additional intrinsic assumptions encoding the relevant endpoint and resource conditions.

## Theorem 3 (a root-basis filter excluding the rook family)

The property that \(G(M)\) is itself a matroid basis-exchange graph is invariant under matroid isomorphism. It holds in the first two rows of Theorem 1, since \(Q_n=\Gamma(\bigoplus U_{1,2})\) and \(K_n=\Gamma(U_{1,n})\). It fails in the third row for **every** \(m\ge3\): \(K_{m,m}\) cannot be a matroid basis graph.

**Proof.** In a matroid basis graph, suppose bases \(B,D\) are at distance two. Write \(B=S\cup\{a,b\}\) and \(D=S\cup\{c,d\}\), with the four indicated elements distinct. Every common neighbor of \(B\) and \(D\) is among
\[
S\cup\{a,c\},\quad S\cup\{a,d\},\quad
S\cup\{b,c\},\quad S\cup\{b,d\}.
\]
Those four possible common neighbors induce, when all are bases, a \(4\)-cycle: neighboring sets share three of the four displayed exchange elements; opposite sets differ by two. Thus a distance-two pair in a basis graph has at most four common neighbors, and no three of them can be pairwise nonadjacent. In \(K_{m,m}\), any two vertices from one part are at distance two and have \(m\) pairwise nonadjacent common neighbors. For \(m\ge5\), their number alone is impossible; for \(m=3,4\), their independence is impossible. \(\square\)

Consequently the class
\[
\mathcal C_{\mathrm{root}}=
\{M:I(M)\text{ is a simple connected edge subdivision with a thin side,
and }G(M)\text{ is itself a matroid basis graph}\}
\]
is defined from the matroid without reference to either target problem, contains both canonical families, and excludes the entire rook family. Theorems 1–2 remain valid within this refinement. No full-strength one-switch or antipodal-geodesic guarantee for this refined class has been established.

## Theorem 4 (triangle-free matroid basis graphs are cubical)

If the basis-exchange graph of a finite matroid \(M\) is triangle-free, then, up to loops and coloops, \(M\) is a direct sum of copies of \(U_{1,2}\). Conversely, every such direct sum has triangle-free basis graph. In particular, a connected triangle-free basis-exchange graph is a hypercube.

**Proof.** Fix a basis \(B\). For any nonloop \(e\notin B\), its fundamental circuit \(C_B(e)\) must contain precisely one element \(b\in B\): if it contained two distinct basis elements \(b,b'\), then \(B-b+e\) and \(B-b'+e\) would both be bases adjacent to \(B\) and to one another, forming a triangle. Therefore each nonloop element outside \(B\) is parallel to a unique element of \(B\). Every nonloop belongs to one of the parallel classes indexed by \(B\), and \(M\) is the direct sum of rank-one uniform matroids on those classes. A class of three or more elements yields three pairwise adjacent bases by independently choosing one member, again forming a triangle. Each nontrivial parallel class consequently has size two. Conversely, replacing either member in any two-element parallel class independently gives the cube graph. \(\square\)

This classification shows that the triangle-free incidence branch has rigid intrinsic matroid structure. An extension claiming that the cube and the uniform rank-two models share a nontrivial self-dual *basis-vertex* polarity must still confront their distinct automorphism-equivariance properties, as recorded in the canonical-polarity obstruction note.

**A nonuniform member of the refined class.** Let \(M\) be the rank-two matroid on six elements with three parallel classes of size two. Its bases are the two-element sets meeting distinct parallel classes, and its basis graph is \(L(K_{2,2,2})\). Every vertex of \(K_{2,2,2}\) has degree four, so the largest cliques of this line graph are its stars (size four), exceeding its triangle cliques (size three). Consequently the largest-clique incidence root is \(G(M)=K_{2,2,2}\). This root is isomorphic to \(J(4,2)=\Gamma(U_{2,4})\): partition the six two-element subsets of a four-element set into three complementary pairs; precisely the complementary pairs are nonadjacent in \(J(4,2)\). Hence \(M\in\mathcal C_{\mathrm{root}}\), despite being neither a uniform rank-two matroid nor a direct sum of rank-one two-element matroids. This demonstrates that the filter defines a class broader than the two motivating matroids.
