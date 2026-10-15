# Cycle-dominating resource matroids and an improved terminal-extension theorem

# Cycle-dominating resource matroids and a unified tournament-extension bound

Let \(G=(V,E)\) be a finite connected simple graph with at least one edge. Let \(N\) be a matroid on the set \(E\). Assume

1. every vertex star \(E(v)\subseteq E\) is independent in \(N\);
2. every cycle of \(G\) is dependent in \(N\).

The second hypothesis implies that every \(N\)-independent edge set is a forest. In particular, a walk whose traversed edges form an independent family in \(N\) has no repeated vertex. At each \(v\), equip \(E(v)\) with an arbitrary tournament \(T_v\). A path \(v_1,\ldots,v_\ell\) is **admissible** if its successive edges are \(N\)-independent and
\[
(v_{i-1}v_i)\longrightarrow(v_iv_{i+1})\quad \text{in }T_{v_i}
\qquad(2\le i\le \ell-1).
\]
Let \(L\) be the maximum order of an admissible path.

**Theorem 1 (cycle-dominating matroid terminal bound).** Under these two matroid hypotheses,
\[
\boxed{\frac{\bar d(G)}2\le (L-1)^2,\qquad
L\ge 1+\sqrt{\frac{\bar d(G)}2},}
\qquad
\bar d(G)=\frac{2|E|}{|V|}.
\tag{1}
\]

**Proof.** For each root edge \(e\), let \(r(e)\) be the maximum order of an admissible path ending with \(e\) in either direction. Orient \(e\) toward the last vertex of a maximizing path. Some \(v\) receives at least \(\bar d(G)/2\) oriented edges. For \(2\le r\le L\), let
\[
U_r(v)=\{uv:u\to v,\ r(uv)=r\},\qquad q_r=|U_r(v)|.
\]
Select \(uv\in U_r(v)\) dominating at least \((q_r-1)/2\) members of \(U_r(v)\) under \(T_v\). Let \(P\) be an admissible \(r\)-vertex witness ending in \(u,v\), and write \(X=E(P)\), an independent set of rank \(r-1\) in \(N\).

For a dominated edge \(vw\in U_r(v)\setminus\{uv\}\), suppose that \(vw\notin\operatorname{cl}_N(X)\). Then \(X+vw\) is independent. Its edge set is a forest, so \(w\) cannot already belong to \(P\): otherwise \(X+vw\) would contain the cycle formed by the segment of \(P\) from \(w\) to \(v\) and \(vw\), contrary to hypothesis 2. The tournament comparison at \(v\) allows an admissible extension of \(P\) to \(w\), giving a path of order \(r+1\) ending with \(vw\). This contradicts \(r(vw)=r\). Thus **every dominated edge lies in** \(\operatorname{cl}_N(X)\).

Because \(E(v)\) is independent in \(N\), its subset \(E(v)\cap\operatorname{cl}_N(X)\) is independent and therefore has size at most
\[
\operatorname{rk}_N\operatorname{cl}_N(X)=r-1.
\]
One member is \(uv\), so at most \(r-2\) other members of \(U_r(v)\) can be dominated by \(uv\). Hence
\[
\frac{q_r-1}{2}\le r-2,\qquad q_r\le 2r-3.
\]
Summing over \(r\) at the chosen \(v\),
\[
\frac{\bar d(G)}2\le \deg^-(v)
=\sum_{r=2}^{L}q_r
\le\sum_{r=2}^{L}(2r-3)=(L-1)^2.
\]
This proves (1). \(\square\)

The statement strengthens the properly edge-labeled tournament theorem from Article VII whenever the associated color-partition resource matroid has the cycle-dependence property. That theorem counts a repeated vertex and a repeated resource separately, whereas here both obstructions are captured by a single matroid closure.

**Corollary 2 (proper colorings without rainbow cycles).** Let the edges of \(G\) be properly colored with arbitrary labels, and assume every graph cycle repeats at least one label. Give each vertex star an arbitrary tournament. Then there is a vertex-simple, rainbow, locally tournament-increasing path of order at least
\[
1+\sqrt{\bar d(G)/2}.
\tag{2}
\]

**Proof.** Let \(N\) be the partition matroid of edges grouped by label, of capacity one per class. Properness makes each star independent; the absence of rainbow cycles makes every graph cycle dependent in \(N\). Apply Theorem 1. \(\square\)

In particular the result applies to partial cubes, with their canonical edge labels given by the hypercube-coordinate classes: edges sharing a coordinate have the same label, each star has distinct coordinate labels, and every closed walk uses each coordinate an even number of times.

## Intrinsic vector-difference resource quotients

Let \(\phi:V(G)\to\mathbb R^d\) be a map and represent an edge \(uv\) by \(d_{uv}=\phi(v)-\phi(u)\), with any choice of edge direction. Denote by \(N_\phi\) the linear matroid of these columns. Since every oriented graph-cycle sums to zero, every graph cycle is dependent in \(N_\phi\). If the vectors
\[
\{\phi(w)-\phi(v):w\in N_G(v)\}
\]
are linearly independent for each \(v\), then Theorem 1 applies. Equivalently, \(N_\phi\) is a representable quotient of the graphic matroid \(M(G)\), with independent vertex stars.

For the cube \(Q_n\), take \(\phi(x)=x\in\mathbb R^n\). Its edge vectors are \(\pm e_i\) and \(N_\phi\) is the coordinate-partition matroid. Independent edge sequences are precisely coordinate-distinct walks, and hence cube geodesics. Order incident cube edges locally by their arbitrary binary colors, breaking ties to form a tournament. Every admissible path has a weakly increasing color word and at most one switch. Since \(\bar d(Q_n)=n\), Theorem 1 yields

\[
\boxed{\text{a coordinate-distinct at-most-one-switch cube geodesic with at least }
\left\lceil\sqrt{n/2}\right\rceil\text{ edges}.}
\tag{3}
\]
No antipodal coloring hypothesis is required. This improves the general one-switch partial-geodesic constant in the Article VII terminal theorem. The statement is a partial-geodesic theorem; it does not establish a monochromatic antipodal geodesic.

For \(K_n\), take \(\phi(v)=e_v\in\mathbb R^n\). The edge vectors \(e_v-e_u\) represent \(M(K_n)\), since an edge set is independent precisely when it is a forest. Every star is independent. For any reversal-odd boundary coloring \(b(a,v,w)\), orient the tournament at \(v\) from \(av\) to \(vw\) when \(b(a,v,w)=1\). An admissible path is then a monochromatic, vertex-simple tight path, and (1) gives
\[
\boxed{L\ge1+\sqrt{(n-1)/2}.}
\tag{4}
\]

Thus the two witness constraints arise from one natural construction: vertex-difference matroids whose independent sets are forests and whose local stars are independent.

## Canonical spectral construction

There is a representation-free way to obtain these resource matroids from the reconstructed graph. For any connected graph \(G\), let \(A\) be its real symmetric adjacency matrix and let \(\lambda_2\) denote its second largest **distinct** adjacency eigenvalue. Let \(P\) be the orthogonal projection onto the corresponding eigenspace and put
\[
\phi_G(v)=P\mathbf e_v,\qquad
N_{\mathrm{sp}}(G)=N_{\phi_G}.
\tag{5}
\]
The construction is invariant under every automorphism of \(G\): its defining projection is a polynomial in \(A\). It is a linear quotient of the graphic matroid. If each vertex star is independent in \(N_{\mathrm{sp}}(G)\), Theorem 1 applies without selecting a separate resource representation.

**Theorem 3 (spectral recovery of both canonical resources).** For \(n\ge3\),
\[
N_{\mathrm{sp}}(Q_n)=\bigoplus_{i=1}^n U_{1,2^{n-1}}
\quad\text{on the \(n\) direction classes of cube edges},
\tag{6}
\]
and
\[
N_{\mathrm{sp}}(K_n)=M(K_n).
\tag{7}
\]
The cube's \(\lambda_2=n-2\) eigenspace has dimension \(n\), and the complete graph's \(\lambda_2=-1\) eigenspace has dimension \(n-1\). In both graphs the vectors of any vertex star form a basis of the \(\lambda_2\) eigenspace.

**Proof.** For \(Q_n\), the functions \(\chi_i(x)=(-1)^{x_i}\), \(1\le i\le n\), are mutually orthogonal adjacency eigenvectors with eigenvalue \(n-2\); the Boolean-character decomposition gives the remaining eigenvalues \(n-2k\), so they span the eigenspace immediately below \(n\). Identifying that eigenspace with \(\mathbb R^n\), the projection of \(\mathbf e_x\) has coordinates proportional to \((\chi_1(x),\ldots,\chi_n(x))\). For adjacent \(x,x+e_i\), the difference is a nonzero multiple of \(e_i\). Thus its edge-column matroid is the direction-partition matroid; the \(n\) vectors at every vertex form a basis.

For \(K_n\), \(A=J-I\) has the constant eigenspace of eigenvalue \(n-1\) and its orthogonal complement, of eigenvalue \(-1\). Hence \(P=I-\frac1nJ\), and
\[
\phi_G(v)-\phi_G(u)=\mathbf e_v-\mathbf e_u.
\]
These columns represent \(M(K_n)\). Its \(n-1\) incident-edge vectors at any vertex form a basis of the standard zero-sum representation. \(\square\)

Define the **spectral root class** to consist of matroids \(M\) for which the largest-clique incidence graph is a subdivision of a connected simple graph \(G(M)\), the root \(G(M)\) is itself a matroid basis graph, and every root star is independent in \(N_{\mathrm{sp}}(G(M))\). These are intrinsic properties of \(M\). Theorem 3 and the earlier incidence reconstructions place both canonical target families in this class.

The rank-two matroid with three parallel classes of size two, which belongs to the broader root-basis class, does not satisfy the spectral-star condition: its incidence root is \(K_{2,2,2}\), regular of degree \(4\), whereas its second adjacency eigenspace has dimension \(3\), so no four incident spectral differences can be independent. Thus spectral-star independence makes a further structural distinction without referring to the desired path conclusion.

The spectral construction identifies the common resource geometry and proves the bound (1). The full NORI1 conclusion requires a separate rank-saturation mechanism compatible with antipodal color reversal.

## The homogeneous Hamming interpolation

The canonical spectral-resource construction extends simultaneously to all Cartesian powers of complete graphs, providing an intermediate family between the cube and the complete graph.

**Theorem 4 (spectral resource geometry of Hamming graphs).** Let
\[
H(k,q)=\underbrace{K_q\square\cdots\square K_q}_{k\text{ factors}},
\qquad k\ge1,\ q\ge2.
\]
Then \(H(k,q)\) is a connected \(d=k(q-1)\)-regular matroid basis graph, namely the basis graph of \(\bigoplus_{i=1}^k U_{1,q}\). Its second adjacency eigenspace has eigenvalue
\[
\lambda_2=d-q
\]
and dimension \(d\). In a suitable orthogonal coordinate system, its canonical projection \(\phi_{H(k,q)}\) is proportional to
\[
(a_1,\ldots,a_k)\longmapsto
\bigl(\mathbf e_{a_1}-q^{-1}\mathbf1,\ldots,
\mathbf e_{a_k}-q^{-1}\mathbf1\bigr)
\in\bigoplus_{i=1}^k\mathbf1^\perp\subset(\mathbb R^q)^k.
\tag{8}
\]
Every vertex star represents a basis of the \(d\)-dimensional spectral resource matroid.

For each coordinate \(i\), the resource vectors of transitions changing \(a_i=a\) to \(b\) are proportional to \(\mathbf e_b-\mathbf e_a\) in the \(i\)th summand. Thus the canonical resource matroid is the direct sum of \(k\) copies of the type-\(A_{q-1}\) graphic matroid \(M(K_q)\), with parallel copies of each transition \(\{a,b\}\) across the different settings of the other \(k-1\) coordinates. A walk has an independent resource-edge sequence precisely when the transitions within every coordinate form an edge-simple forest in that coordinate's \(K_q\). Such a walk cannot revisit any coordinate value after leaving it, and is a vertex-simple path.

Moreover, through any specified initial vertex there exists an independent path with \(d\) edges, saturating the resource rank.

**Proof.** The eigenvalues of the \(K_q\) adjacency matrix on the constant and zero-sum spaces are respectively \(q-1\) and \(-1\), with multiplicities \(1\) and \(q-1\). The adjacency matrix of their Cartesian product is the sum of the adjacency operators on the \(k\) factors. Its leading eigenvalue is \(d\); replacing the constant space in precisely one factor by its zero-sum space produces the next eigenvalue \(d-q\), with total multiplicity \(k(q-1)=d\). Orthogonal projection of a vertex delta function to this eigenspace gives (8), up to a common nonzero normalization. An edge changes one coordinate, so its gradient is a single type-\(A_{q-1}\) root in one factor; all other blocks vanish. This proves the resource-matroid decomposition.

At a vertex \(a\), the \(q-1\) vectors \(\mathbf e_b-\mathbf e_{a_i}\) as \(b\) runs over the other symbols form a basis of the zero-sum space in factor \(i\). Over all coordinates they form a basis of the full spectral eigenspace. An independent edge sequence cannot contain a closed cycle among the transitions in any coordinate. The successive coordinate values form a trail in \(K_q\); a repeated coordinate value would produce a cycle in that trail. For rank saturation, fix any order of the \(k\) coordinates and, one coordinate at a time, change its value through all \(q\) symbols without repetition. The resulting \(k(q-1)\) transitions form a forest in each coordinate factor and are independent. \(\square\)

At the two extremes,
\[
H(n,2)=Q_n,\qquad H(1,n)=K_n,
\]
and their spectral resource matroids specialize respectively to coordinate independence and graphic independence. Theorem 1 therefore gives the uniform quantitative bound
\[
L\ge 1+\sqrt{k(q-1)/2}
\tag{9}
\]
for arbitrary local tournaments on every homogeneous Hamming graph, with spectral-resource-independent paths. The endpoint examples recover the cube one-switch partial-geodesic result (under local color ordering) and the ordinary boundary-tournament square-root result (under reversal-odd turn ordering).

The intermediate family is a statement about *resource-root graphs*; it does not assert that every \(H(k,q)\) appears as the maximum-clique incidence root of an input matroid \(M\) from the previous section. Its usefulness is that the two extremal resource matroids are specializations of the same automorphism-invariant spectral construction, with a common full-rank uncolored path geometry.

**Proposition 5 (spectral antipodes occur only at the cubical endpoint).** For \(k\ge1\), \(q\ge2\), the convex hull of the spectral vertex embedding \(\phi_{H(k,q)}(V)\) is centrally symmetric if and only if \(q=2\). When \(q=2\), its central reflection is the hypercube complement map \(a\mapsto\bar a\); when \(k=1\) and \(q>2\), the root is a simplex and has no centrally induced vertex antipode.

**Proof.** Formula (8) identifies the spectral convex hull, up to a common dilation, with a Cartesian product of \(k\) centered \((q-1)\)-simplices. For \(q=2\), each simplex is a segment, and their product is centrally symmetric. For \(q>2\), project onto any coordinate summand. A centrally symmetric convex body has centrally symmetric linear images, whereas the simplex with vertices \(\mathbf e_a-q^{-1}\mathbf1\), \(a\in[q]\), has no central symmetry: its centroid is the only possible center and the negative of \(\mathbf e_a-q^{-1}\mathbf1\) is not another vertex when \(q>2\). Hence the product is not centrally symmetric. \(\square\)

This proposition localizes a necessary distinction in the polarization problem: the spectral map produces the cube's vertex antipode intrinsically, while in the complete-graph endpoint the reversal-odd operation must be imposed on oriented exchanges or turns. In either case reversal of an oriented edge changes its spectral resource vector by a sign, but that common linear sign involution does not itself impose the original two-color constraints.
