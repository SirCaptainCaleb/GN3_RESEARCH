## Vertex involutions and one-switch rainbow paths

The problem originates in **NORI1** and **reversal-odd boundary 3-tournaments**. We seek the weakest natural graph-theoretic hypotheses that encompass both classes and guarantee long rainbow paths with few binary-label switches. In particular, the binary labeling must remain unrestricted beyond the required involutive reversal; no additional relations between overlapping boundary triples may be assumed.

Let \(G=(V,E)\) be a finite connected simple graph with an ordinary edge coloring \(\lambda:E\to\mathcal C\), a binary edge labeling \(\chi:E\to\{0,1\}\), and a **vertex involution** \(\tau:V(G)\to V(G)\) satisfying
\[
\tau^2=\operatorname{id}_{V(G)},\qquad
\{u,v\}\in E(G)\ \Longleftrightarrow\
\{\tau(u),\tau(v)\}\in E(G).
\]
Thus \(\tau\) is a graph automorphism with domain **the vertices, not the edges**. Throughout Article XIII, the notation \(\tau e\), for \(e=\{u,v\}\), means only the uniquely induced edge \(\{\tau(u),\tau(v)\}\). In particular **there is no independently chosen involution of the edge set**. The reversal-odd condition is
\[
\chi(\{\tau(u),\tau(v)\})=1-\chi(\{u,v\})
\quad\text{for every }\{u,v\}\in E(G).
\]
The ordinary coloring \(\lambda\) is unrestricted under \(\tau\); in particular, \(\lambda(\tau e)\) may differ from \(\lambda(e)\). Put \(k=\hat\delta(G,\lambda)=\min_{v\in V}|\{\lambda(e):e\ni v\}|\). The initial one-switch target asks for a vertex-simple rainbow path of at least \(k\) edges and at most one change in its \(\chi\)-sequence; the counterexamples below refute stronger special cases. Researchers should seek **minimal structural strengthenings applicable to both motivating classes**, and may examine weaker quantitative targets, especially linear-length paths with logarithmically many switches. Conditions must arise from their graph and color-incidence geometry, not extra assumptions on their freely chosen binary labels.

**Theorem XIII.1 (eight-vertex counterexample).** A connected simple graph on eight vertices admits a proper three-edge-coloring \(\lambda\), a fixed-point-free involution \(\tau\) preserving \(\lambda\), and an edge labeling \(\chi\) reversed by \(\tau\), such that every rainbow path of length three has \(\chi\)-word \(010\) or \(101\). Thus \(\hat\delta(G,\lambda)=3\), but the longest rainbow path with at most one \(\chi\)-change has length two.

**Proof.** Take \(V=\{(i,s):i\in\{0,1,2,3\},\,s\in\mathbb F_2\}\). Define \(\varepsilon_{01}=1\) and \(\varepsilon_{ij}=0\) for the other five pairs \(i<j\), and put
\[
E=\{(i,s)(j,s+\varepsilon_{ij}):i<j,\ s\in\mathbb F_2\}.
\]
All sums involving sheet indices or edge labels are in \(\mathbb F_2\). Color the edges over \(01,23\) by \(A\), those over \(02,13\) by \(B\), and those over \(03,12\) by \(C\). Each vertex has one edge of each color. Each of the two sheets induces \(K_4-01\), and the two edges over \(01\) connect the sheets, so \(G\) is connected.

Set \(\gamma_{02}=\gamma_{03}=1\), with \(\gamma_{ij}=0\) for the other four pairs, and define
\[
\chi((i,s)(j,s+\varepsilon_{ij}))=s+\gamma_{ij}\quad(i<j),
\qquad \tau(i,s)=(i,s+1).
\]
The description of an edge with \(i<j\) is unique. Therefore \(\tau\) is a fixed-point-free automorphism preserving \(\lambda\) and complementing \(\chi\).

Project any rainbow three-edge path onto the base \(K_4\). The projected walk does not repeat an edge, as this would repeat a color. If it visits all four base vertices, its first and third edges are disjoint and have the same color in the specified one-factorization. Therefore its projection is a triangle. A base triangle avoiding \(01\) lifts to closed triangles, which cannot be vertex-simple three-edge paths. The remaining base triangles are \(012\) and \(013\). Their lifts are six-cycles because each traverses the single cross-sheet edge \(01\). For \(t\in\{2,3\}\), the three-edge segment
\[
(0,s),(1,s+1),(t,s+1),(0,s+1)
\]
has \(\chi\)-word \((s,s+1,s)\). Extending this segment around its six-cycle yields alternating edge labels throughout. Every rainbow three-edge path consequently has two \(\chi\)-changes.

Only three colors occur, so a rainbow path has at most three edges. Every two-edge path is rainbow and has at most one \(\chi\)-change. Hence the maximum allowable length is two. \(\square\)

##### A transfer from properly edge-colored complete graphs

**Theorem (rainbow-path deficiency transfer).** Let \(r\geq4\), and let \(\kappa\) be a proper edge coloring of \(K_r\). Write \(L\) for the maximum length of a \(\kappa\)-rainbow simple path. There is a connected simple graph \(G\) on \(r(r+1)\) vertices, a proper edge coloring \(\lambda\), a binary edge labeling \(\chi\), and a fixed-point-free involutive automorphism \(\tau\) such that
\[
\lambda(\tau e)=\lambda(e),\qquad \chi(\tau e)=1-\chi(e),\qquad
\hat\delta(G,\lambda)=2r-2,
\]
and every rainbow simple path with at most one \(\chi\)-change has at most \(2L\) edges. Moreover, there is no rainbow simple cycle of length \(2r-2\) having at most one \(\chi\)-change in any linear indexing of its edges.

**Proof.** Let \(I\) have \(r+1\) elements. Take the graph with vertex set
\[
V(G)=\{(i,j)\in I^2:i\neq j\},
\]
where two distinct vertices are adjacent precisely when their first coordinates agree or their second coordinates agree. Its rows \(R_i=\{(i,j):j\neq i\}\) and columns \(C_i=\{(j,i):j\neq i\}\) are copies of \(K_r\). This graph is connected: given vertices \((i,j)\) and \((a,b)\), choose \(s\in I\setminus\{i,j,a,b\}\), and join them through \((i,s)\) and \((a,s)\), omitting repeated vertices if \(i=a\).

For each \(i\), choose a bijection \(f_i:I\setminus\{i\}\to V(K_r)\). Color the row edges and the corresponding column edges by
\[
\begin{aligned}
\lambda((i,j)(i,j'))&=(i,\kappa(f_i(j)f_i(j'))),\\
\lambda((j,i)(j',i))&=(i,\kappa(f_i(j)f_i(j'))),
\end{aligned}
\qquad (j\neq j',\ i\notin\{j,j'\}),
\]
and give the row edges label \(\chi=0\) and the column edges label \(\chi=1\). The automorphism \(\tau(i,j)=(j,i)\) preserves \(\lambda\) and complements \(\chi\).

At \((i,j)\) the \(r-1\) row-edge colors have first coordinate \(i\), while the \(r-1\) column-edge colors have first coordinate \(j\). Each set consists of distinct colors by properness of \(\kappa\), and the two sets are disjoint because \(i\neq j\). Thus \(\lambda\) is proper and \(\hat\delta(G,\lambda)=2r-2\).

A path with \(\chi\)-word \(0\cdots01\cdots1\), or its reversal, consists of one path inside a row followed by one inside a column. Each rainbow segment has length at most \(L\), proving the path bound.

For cycles, a single-label cycle lies in a \(K_r\) and has length at most \(r<2r-2\). A cycle involving both labels must have an even number of changes when read cyclically. It cannot have two: its row segment and column segment would have two distinct common endpoints, whereas a row and column meet in at most one vertex. Thus a mixed-label cycle has at least four cyclic changes, and every linear indexing has at least three changes. \(\square\)

**Corollary (unbounded minimum color degree).** For every \(d\geq2\), there is such a graph with
\[
\hat\delta(G,\lambda)=2^{d+1}-2,
\qquad
L_{\leq1}(G,\lambda,\chi)\leq 2^{d+1}-4
=\hat\delta(G,\lambda)-2.
\]
The same graph refutes the alternative permitting rainbow paths **or cycles** of length at least the minimum color degree with at most one binary-label change.

**Proof.** Set \(r=2^d\), identify \(V(K_r)\) with \(H=\mathbb F_2^d\), and color an edge \(xy\) by \(\kappa(xy)=x+y\), a nonzero element of \(H\). This is a proper coloring with \(r-1\) colors. A rainbow path of length \(r-1\) would use every nonzero group element as an edge color. Summing its edge colors gives both the sum of its nonzero group elements, which is zero for \(d\geq2\), and the sum of its endpoint coordinates, which is nonzero because the endpoints differ. Hence \(L\leq r-2\), and the transfer theorem applies. \(\square\)

**Example (sharp bound at color degree six).** Take \(r=4\), \(I=\{0,1,2,3,4\}\), and \(H=\mathbb F_2^2=\{0,1,2,3\}\) with XOR addition. For each \(i\), let \(f_i\) map the increasing enumeration of \(I\setminus\{i\}\) onto \(0,1,2,3\). The rainbow path
\[
(0,1),(0,2),(0,3),(1,3),(2,3)
\]
has four edges and \(\chi\)-word \(0011\). It attains the one-switch upper bound \(4\), whereas the minimum color degree is \(6\). The longer path
\[
(0,1),(0,2),(0,3),(1,3),(2,3),(2,0),(2,1)
\]
has six pairwise distinct edge colors
\[
(0,1),(0,3),(3,1),(3,3),(2,2),(2,1)
\]
and \(\chi\)-word \(001100\). Thus this graph contains a rainbow path of length equal to its minimum color degree; the obstruction is its need for two binary-label changes.

##### An infinite family of rainbow-path obstructions

**Lemma.** Let \(\tau\) be an involutive vertex automorphism of a graph \(G\). There exists a binary edge labeling \(\chi\) satisfying \(\chi(\tau e)=1-\chi(e)\) for all \(e\in E(G)\) if and only if \(\tau\) fixes no edge setwise.

**Proof.** A fixed edge would require \(\chi(e)=1-\chi(e)\). Conversely, when \(\tau\) acts without fixed edges, its edge orbits have size two. Label the two edges in each orbit \(0\) and \(1\). \(\square\)

**Theorem (binary Latin-square obstruction).** For every integer \(d\ge2\) there is a connected simple graph with a proper edge coloring \(\lambda\), binary edge labeling \(\chi\), and involutive automorphism \(\tau\) satisfying
\[
\lambda(\tau e)=\lambda(e),\qquad \chi(\tau e)=1-\chi(e),
\]
whose minimum color degree is \(2^d\), yet which has no rainbow path of length \(2^d\). In particular, Conjecture XIII.1 fails even if its condition on the number of \(\chi\)-changes is omitted.

**Proof.** Put \(A=\mathbb F_2^d\), \(q=|A|=2^d\), and let \(G=K_{q,q}\) have bipartition \(\{L_x:x\in A\}\) and \(\{R_y:y\in A\}\). Define
\[
\lambda(L_xR_y)=x+y.
\]
At every vertex the \(q\) incident edges receive all elements of \(A\) as distinct colors, so \(\hat\delta(G,\lambda)=q\).

Choose a nonzero \(t\in A\) and a linear functional \(h:A\to\mathbb F_2\) with \(h(t)=1\). Define
\[
\tau(L_x)=L_{x+t},\quad \tau(R_y)=R_{y+t},\qquad
\chi(L_xR_y)=h(x).
\]
Translation by \(t\) is an involutive automorphism. For every edge,
\[
\lambda(L_{x+t}R_{y+t})=x+y+2t=x+y,\qquad
\chi(L_{x+t}R_{y+t})=h(x)+1.
\]
Thus all the stipulated symmetries hold.

Suppose \(v_0v_1\cdots v_q\) were a rainbow path with \(q\) edges. Writing \(a(v)\in A\) for the index of either \(L_x\) or \(R_x\), we obtain
\[
a(v_0)+a(v_q)
=\sum_{i=1}^{q}\bigl(a(v_{i-1})+a(v_i)\bigr)
=\sum_{i=1}^{q}\lambda(v_{i-1}v_i)
=\sum_{x\in A}x=0.
\]
The last equality holds because \(d\ge2\). Hence the endpoints have equal indices. Since \(q\) is even, they lie in the same part of \(G\), and consequently \(v_0=v_q\), contrary to vertex-simplicity. There are only \(q\) colors in the graph, so a longer rainbow path is also impossible. \(\square\)

**Remark.** This obstruction distinguishes paths from cycles. When \(d=2\), choose a nonzero \(a\in\ker h\). The cycle
\[
L_0R_0L_aR_tL_0
\]
has colors \(0,a,a+t,t\), all distinct, and all four edges have \(\chi\)-label \(0\). Thus allowing rainbow cycles removes the obstruction in this four-color example.

##### Linear zero-switch paths for proper edge colorings

**Theorem.** Let \(G\) be a finite simple graph with a proper edge coloring \(\lambda\) and minimum degree \(k\geq 1\). For every binary edge labeling \(\chi:E(G)\to\{0,1\}\), there is a vertex-simple \(\lambda\)-rainbow path of at least \(k/8\) edges whose edges share the same \(\chi\)-label.

**Proof.** Write \(n=|V(G)|\), \(m=|E(G)|\). For some \(b\in\{0,1\}\), the spanning subgraph \(H\) comprising the edges with \(\chi=b\) has at least \(m/2\) edges, hence average degree
\[
D=\frac{2|E(H)|}{n}\geq \frac mn=\frac{\overline d(G)}2\geq \frac k2.
\]
There is a nonempty subgraph \(J\subseteq H\) of minimum degree at least \(D/2\). Indeed, if none existed, iterative deletion of vertices of current degree strictly less than \(D/2\) could delete the entire graph, removing fewer than \(nD/2=|E(H)|\) edges in total, an impossibility. Therefore \(\delta(J)\geq k/4\).

Let \(P=v_0v_1\ldots v_\ell\) be a longest vertex-simple \(\lambda\)-rainbow path in \(J\). At most \(\ell\) edges at the terminal vertex \(v_\ell\) lead to earlier vertices of \(P\). Among its edges to vertices outside \(P\), at most \(\ell\) carry colors used by \(P\), since the coloring is proper. Thus \(\deg_J(v_\ell)\leq 2\ell\), since otherwise \(P\) extends by an edge to a new vertex of a new color. Consequently
\[
\ell\geq\frac{\delta(J)}2\geq \frac k8.
\]
Every edge of \(J\) has binary label \(b\), so \(P\) has zero binary-label changes. \(\square\)

The bound requires no symmetry hypothesis on \(\lambda\) or \(\chi\); it also applies when an involutive vertex automorphism reverses \(\chi\) and changes ordinary edge colors.
