# Article XI — Matroidal Turn Geometry and Rainbow-Circuit Exchange

## Antipodal turn quotients and rainbow-circuit geometry

Let \(n\ge3\), let \(Q_n\) be the \(n\)-dimensional cube, and let \(L=L(Q_n)\) be its line graph. Thus vertices of \(L\) are edges of \(Q_n\), and the edges of \(L\) are pairs of distinct cube edges meeting at one cube vertex. The antipodal involution \(\tau\) of \(Q_n\) induces a free involution on \(L\). Write
\[
H_n=L/\langle\tau\rangle.
\]
The vertices of \(H_n\) are antipodal pairs \([e]=\{e,\tau e\}\) of cube edges. They are partitioned into \(n\) direction classes \(V_1,\ldots,V_n\), according to the coordinate direction of \(e\). The edges of \(H_n\) are antipodal pairs of incident cube-edge pairs. In particular,
\[
|V(H_n)|=n2^{n-2},\qquad
|E(H_n)|=\binom n2 2^{n-1}.\tag{1}
\]
The natural projection \(p:L\to H_n\) is a connected two-sheeted graph covering.

For a closed walk \(C\) in \(H_n\), let \(\alpha(C)\in\mathbb F_2\) be its covering monodromy: \(\alpha(C)=1\) when a lift that begins at \(e\) ends at \(\tau e\), and \(\alpha(C)=0\) otherwise. This defines a nonzero linear functional on the binary cycle space \(Z_1(H_n;\mathbb F_2)\). Fix any edge cochain \(a\in\mathbb F_2^{E(H_n)}\) whose sum on a closed walk \(C\) equals \(\alpha(C)\).

**Theorem 1 (switching-class representation).** Antipodally odd edge colorings \(c:E(Q_n)\to\mathbb F_2\), satisfying \(c(\tau e)=c(e)+1\), induce turn cochains
\[
d([\{e,f\}])=c(e)+c(f),\tag{2}
\]
where \(e,f\) meet at a vertex of \(Q_n\). The set of resulting cochains is precisely
\[
\boxed{\quad a+B^1(H_n;\mathbb F_2)
=\{a+\delta f:f:V(H_n)\to\mathbb F_2\}.\quad}\tag{3}
\]
Equivalently, a turn cochain \(d\) is admissible if and only if
\[
\boxed{\ \sum_{t\in C}d(t)=\alpha(C)
\quad\text{for every cycle }C\text{ of }H_n.\ }\tag{4}
\]
Each admissible \(d\) determines an antipodally odd coloring up to complementation of all edge colors. The affine space (3) has dimension \(n2^{n-2}-1\).

*Proof.* Choose one representative from each antipodal pair of cube edges. Define a reference coloring \(s\) to be zero on these representatives and one on their antipodes. Its incident-edge differences descend to a cochain \(a_s\) on \(H_n\), because complementation of both incident edges preserves their difference. Given a closed turn walk in \(H_n\), lift its edge sequence in \(L\), starting at a cube edge \(e\) and ending at \(\tau^\varepsilon e\). Telescoping the differences of \(s\) along the lifted sequence gives
\[
\sum_{t\in C}a_s(t)=s(e)+s(\tau^\varepsilon e)=\varepsilon=\alpha(C).
\]
Thus \(a_s\) represents the prescribed class, and \(a+a_s\) has zero sum on every cycle. On a connected graph every such cochain is a coboundary, so \(a=a_s+\delta g\) for some vertex function \(g\).

For any other antipodally odd coloring \(c\), the function \(c(e)+s(e)\) is invariant under \(\tau\), hence equals \(f([e])\) for a vertex function on \(H_n\). Consequently
\[
d=a_s+\delta f.
\]
Conversely, every \(f\) gives an antipodally odd coloring \(c(e)=s(e)+f([e])\) and induces \(a_s+\delta f\). Replacing \(f\) by \(f+1\) complements the coloring and leaves \(d\) unchanged; connectedness gives no other kernel. Formula (4) is the standard cycle-space characterization of the affine cut coset (3). Since the coboundary space of a connected graph with \(N\) vertices has dimension \(N-1\), the last assertion follows. \(\square\)

Let \(B\) be the vertex-edge incidence matrix of \(H_n\) over \(\mathbb F_2\). For an admissible turn cochain \(d\), consider the binary matrix
\[
A_d=\begin{pmatrix}B\\d\end{pmatrix},\tag{5}
\]
whose columns are indexed by turns. The vector matroid represented by (5) is the even-cycle matroid associated with the nontrivial covering class \(\alpha\).

**Corollary 2 (a canonical binary matroid).** Every admissible \(d\) gives the same represented binary matroid \(M_n\). Its rank is
\[
\operatorname{rank}M_n=n2^{n-2}.\tag{6}
\]
A binary edge set \(F\subseteq E(H_n)\) is dependent in \(M_n\) precisely when it contains a nonempty binary cycle \(z\) with \(\alpha(z)=0\). In particular, a simple cycle \(C\) of \(H_n\) is independent in \(M_n\) if \(\alpha(C)=1\), and dependent if \(\alpha(C)=0\).

*Proof.* By (3), \(d=a+\delta f=a+f^TB\), so the last row of \(A_d\) differs from that of \(A_a\) by a linear combination of the preceding rows. All matrices \(A_d\) therefore have the same row space and represent the same matroid. The incidence matrix \(B\) has rank \(N-1\), where \(N=|V(H_n)|\). Since \(\alpha\ne0\), the row \(a\) has a nonzero sum on some cycle and does not lie in the row space of \(B\). Hence \(\operatorname{rank}A_a=N\). Finally, a nonzero binary vector \(z\) belongs to the kernel of \(A_d\) if and only if \(Bz=0\) and \(d z=\alpha(z)=0\), giving the dependence characterization. \(\square\)

Call a simple cycle of \(H_n\) **direction-rainbow** if its \(n\) vertices contain one member of each direction class \(V_i\).

**Theorem 3 (rainbow-circuit dichotomy).** Let \(C\) be a direction-rainbow simple cycle of \(H_n\). Precisely one of the following holds:

1. \(\alpha(C)=0\), and \(C\) is obtained by cyclically ordering the \(n\) cube edges incident with one cube vertex and projecting the corresponding turn cycle to \(H_n\).
2. \(\alpha(C)=1\), and \(C\) is obtained by cyclically completing a full antipodal geodesic of \(Q_n\): consecutive edges of the geodesic give the first \(n-1\) turns, and the final turn joins its last edge to the antipode of its first edge.

Conversely, every cyclically ordered cube-edge star and every full antipodal geodesic gives a direction-rainbow cycle of the indicated type. Therefore
\[
\boxed{\begin{aligned}
\{\text{full antipodal geodesic cycles}\}
=\{\text{direction-rainbow graphic circuits }C:
\alpha(C)=1\}.
\end{aligned}}\tag{7}
\]
By Corollary 2, the cycles in (7) are also precisely those direction-rainbow graphic circuits that are independent in \(M_n\).

*Proof.* Traverse \(C\) as a cyclic sequence of its vertices and lift it to a walk
\[
e_1,e_2,\ldots,e_n,e_{n+1}
\quad\text{in }L(Q_n),
\qquad e_{n+1}=\tau^\varepsilon e_1,\tag{8}
\]
where \(\varepsilon=\alpha(C)\). Write \(\pi_i\) for the direction of \(e_i\). The direction-rainbow hypothesis says that \(\pi_1,\ldots,\pi_n\) is a permutation of \(\{1,\ldots,n\}\).

For \(1\le i\le n\), let \(u_i\in Q_n\) be the common cube vertex of the incident edges \(e_i,e_{i+1}\), and define \(u_0=\tau^\varepsilon u_n\). The vertices \(u_{i-1},u_i\) both belong to the cube edge \(e_i\); hence
\[
u_i=u_{i-1}\oplus t_i\,\mathbf e_{\pi_i}
\qquad(t_i\in\mathbb F_2).\tag{9}
\]
Because \(u_n=\tau^\varepsilon u_0\), summing (9) yields
\[
\sum_{i=1}^n t_i\mathbf e_{\pi_i}
=\varepsilon(1,\ldots,1).\tag{10}
\]
Every direction occurs once, so (10) forces \(t_i=\varepsilon\) for all \(i\).

If \(\varepsilon=0\), all \(u_i\) coincide; thus the \(e_i\) are the \(n\) different cube edges incident with one vertex, giving case 1. If \(\varepsilon=1\), every successive pair \(u_{i-1},u_i\) is joined by \(e_i\), and the \(n\) steps traverse every coordinate once. They form a full antipodal geodesic, giving case 2.

Conversely, cyclically ordered edges in one cube vertex star yield a closed turn cycle with trivial covering monodromy. A full antipodal geodesic yields a turn cycle whose last turn joins its last edge to the antipode of its first, so its lifted endpoint is \(\tau e_1\) and its monodromy is one. In either case distinct edge directions make the projected cycle simple and direction-rainbow. The final statement follows from Corollary 2. \(\square\)

**Corollary 4 (matroidal formulation of unrestricted NORI1).** For an admissible turn cochain \(d\), let
\[
\mathcal R_n=\{C\subseteq E(H_n):
C\text{ is a direction-rainbow simple cycle and independent in }M_n\}.
\]
Then
\[
\boxed{\quad \mu(c)=
\min_{C\in\mathcal R_n}\left(\sum_{t\in C}d(t)-1\right).\quad}\tag{11}
\]
Every sum in (11) is odd. In particular, the unrestricted two-switch conclusion in dimension \(n\) is equivalent to
\[
\boxed{
\text{for every }d\in a+B^1(H_n;\mathbb F_2),
\ \text{some }C\in\mathcal R_n\text{ has }\sum_{t\in C}d(t)\le3.
}\tag{12}
\]
The unrestricted monochromatic conclusion is equivalent to the corresponding bound with sum at most one.

*Proof.* By Theorem 3, the members of \(\mathcal R_n\) are the cyclic turn cycles of full antipodal geodesics. Their \(d\)-sums are odd by (4). For any rooted geodesic, its number of switches is the sum on its corresponding turn cycle with the terminal seam comparison omitted, so it is at least the sum minus one. Conversely, cyclically rotating a geodesic and its root allows any turn of the cycle to be chosen as the omitted comparison. An odd sum contains a turn labeled one; omitting that turn achieves the sum minus one. Taking minima proves (11), from which (12) and the monochromatic version follow. \(\square\)

The graphic-matroid circuits of \(H_n\), the binary even-cycle matroid \(M_n\), and the direction partition together characterize the geodesic witness family without a separate port-compatibility condition. Corollary 2 also shows that the even-cycle matroid itself is invariant under all admissible colorings: the coloring-dependent information relevant to switch minimization is the chosen representative \(d\) of the fixed switching class. Thus a matroidal proof of a switch bound must use quantitative properties of its representative's support on the distinguished rainbow circuits, beyond matroid rank or circuit incidence alone.

**Conjecture 5 (three-turn rainbow-circuit property).** For every \(n\ge3\) and every vertex function \(f:V(H_n)\to\mathbb F_2\), the cochain \(d=a+\delta f\) admits a direction-rainbow simple cycle \(C\) with \(\alpha(C)=1\) and
\[
\boxed{\sum_{t\in C}d(t)\le3.}\tag{13}
\]
Here the sum counts those turns assigned the bit one. This conjecture is equivalent, by Corollary 4, to the unrestricted inequality \(\mu(c)\le2\) for antipodally odd cube-edge colorings. Its one-turn strengthening, with the right-hand side of (13) replaced by one, is equivalent to unrestricted NORI1.

Any proof by circuit exchange must control three coupled properties: the direction partition, nontrivial covering monodromy, and the support weight of the turn cochain. The switching-class representation makes the ambient binary matroid independent of the coloring, while the weight \(d\) retains the quantitative difficulty. A proof that uses only rank or matroid independence cannot distinguish the various colorings in this affine switching class.


### Folded-cube cycle-space presentation and antipodal girth

For \(n\ge3\), let \(Q_n\) denote the binary cube with antipodal map \(\tau\), and put \(G_n=Q_n/\langle\tau\rangle\) and \(H_n=L(Q_n)/\langle\tau\rangle\), where \(L\) denotes the line graph. The quotient \(G_n\) is a simple \(n\)-regular graph with \(2^{n-1}\) vertices and \(n2^{n-2}\) edges: two different coordinate directions cannot connect the same antipodal vertex classes for \(n\ge3\).

**Proposition 6 (the folded-cube line graph).** There is a canonical isomorphism
\[
H_n\cong L(G_n).
\tag{1}
\]
Under this isomorphism the two-sheeted covering \(L(Q_n)\to H_n\) is induced by \(Q_n\to G_n\).

*Proof.* Vertices on both sides are pairs of antipodal cube edges. Two pairs are joined precisely when their representatives can meet at a vertex. In \(G_n\) this is incidence of its corresponding edges; simplicity ensures a unique center of incidence. Every turn downstairs lifts uniquely once its first cube edge is chosen, proving the covering assertion. \(\square\)

A star triangle is a triangle formed by three edges incident with one vertex of \(G_n\). A square turn cycle consists of the four successive edges of a square face of \(Q_n\), regarded as four vertices of \(H_n\). Let \(T\) and \(S\) be their respective binary spans in \(Z_1(H_n;\mathbb F_2)\). Write \(\alpha\) for the covering monodromy \(Z_1(H_n;\mathbb F_2)\to\mathbb F_2\).

**Theorem 7 (local generation of even monodromy).** For every \(n\ge3\),
\[
\boxed{\ker\alpha=T+S.}
\tag{2}
\]
The dimensions are
\[
\begin{aligned}
\dim Z_1(H_n)&=n(n-2)2^{n-2}+1,\\
\dim\ker\alpha&=n(n-2)2^{n-2},\\
\dim T&=(n-1)(n-2)2^{n-2},\\
\dim(T+S)/T&=(n-2)2^{n-2}.
\end{aligned}
\tag{3}
\]
In particular, star triangles, square turn cycles, and one antipodal-geodesic cycle span \(Z_1(H_n;\mathbb F_2)\).

*Proof.* Let \(I(G_n)\) be the subdivision graph of \(G_n\), whose vertices are \(V(G_n)\sqcup E(G_n)\). To a turn \(t=\{e,f\}\) at \(v\), assign the incidence chain
\[
\varphi(t)=(e,v)+(v,f).
\tag{4}
\]
This preserves boundaries and induces a linear map \(\varphi:Z_1(H_n)\to Z_1(I(G_n))\cong Z_1(G_n)\). It is onto: every cycle of \(G_n\) lifts to the turn cycle of its successive edges. Its kernel is \(T\). Indeed, different vertex stars use disjoint turn edges, and on each star \(\varphi(z)=0\) means that the turn chain has even degree at every vertex of the clique \(K_n\) of incident edges. The cycle space of a complete graph is generated by its triangles. We therefore have
\[
0\longrightarrow T\longrightarrow Z_1(H_n)
 \xrightarrow{\ \varphi\ }Z_1(G_n)\longrightarrow0,
\tag{5}
\]
with image equal to the whole final space and kernel equal to \(T\).

Let \(\beta:Z_1(G_n)\to\mathbb F_2\) be the monodromy of the cube covering \(Q_n\to G_n\). Tracing contact vertices in a lifted turn walk yields
\(\alpha=\beta\circ\varphi\).

Let \(F\) be the span in \(Z_1(G_n)\) of projected square boundaries of \(Q_n\). We prove \(\ker\beta=F\). Every projected square lifts closed, so \(F\subseteq\ker\beta\). Conversely, express \(z\in\ker\beta\) as a disjoint union of closed trails and connect them by paths used twice to obtain one closed walk \(W\) with incidence vector \(z\) modulo two. Since \(\beta(W)=0\), the walk lifts closed to \(Q_n\). Its binary edge chain lies in the cycle space of the cube, which is spanned by square boundaries: adjacent coordinate steps may be interchanged across squares and immediate backtracks canceled until any closed walk is reduced. Projection gives \(z\in F\). As the turn cycle of a cube square maps under \(\varphi\) to its projected square boundary, \(\varphi(S)=F\). Together with (5), this proves (2).

The \(2^{n-1}\) star cliques are edge-disjoint copies of \(K_n\), each with cycle-space dimension \(\binom{n-1}{2}\). Hence
\(\dim T=2^{n-1}\binom{n-1}{2}\).
The connected graph \(H_n=L(G_n)\) has
\[
|V(H_n)|=n2^{n-2},\qquad
|E(H_n)|=2^{n-1}\binom n2,
\]
giving the first line of (3). A full antipodal geodesic projects to a closed turn cycle whose lift ends at the antipode of its initial edge, so \(\alpha\ne0\). Its kernel consequently has codimension one, giving the remaining lines of (3). The same geodesic cycle adds a generator outside \(\ker\alpha\). \(\square\)

**Corollary 8 (local cochain criterion).** A function \(d:E(H_n)\to\mathbb F_2\) is induced by an antipodally odd binary coloring of cube edges if and only if its sum vanishes on every star triangle and square turn cycle, and its sum equals one on any one specified antipodal-geodesic cycle. The coloring is unique up to global complementation.

*Proof.* Such a coloring makes turn sums equal to covering monodromy, proving necessity. Conversely, Theorem 7 makes the stated conditions equivalent to \(d(z)=\alpha(z)\) for every binary cycle \(z\). The pullback of \(d\) to \(L(Q_n)\) then sums to zero on all cycles and equals the coboundary of a vertex function \(c\), unique up to a constant because \(L(Q_n)\) is connected. Its vertices are cube edges. Invariance of \(d\) under \(\tau\) makes \(c(e)+c(\tau e)\) constant on cube edges; summing around the specified monodromy-one cycle identifies that constant as one. Thus \(c\) is antipodally odd and induces \(d\). \(\square\)

**Theorem 9 (antipodal girth and stability).** If \(C\) is a simple cycle of \(H_n\) with \(\alpha(C)=1\), then
\[
\boxed{|C|\ge n.}
\tag{6}
\]
Equality holds if and only if \(C\) is the cyclic turn cycle of a full antipodal geodesic of \(Q_n\). More quantitatively, let \(|C|=r\), choose a lift of its cyclic edge sequence
\[
e_1,\ldots,e_r,e_{r+1}=\tau e_1,
\]
and let \(u_i\) be the common cube vertex of \(e_i,e_{i+1}\), with \(u_0=\tau u_r\). Write \(s\) for the number of indices with \(u_i=u_{i-1}\), and \(m_j\) for the number of changes \(u_{i-1}\ne u_i\) made in coordinate \(j\). Every \(m_j\) is a positive odd integer, and
\[
\boxed{r-n=s+2\sum_{j=1}^n\frac{m_j-1}{2}.}
\tag{7}
\]

*Proof.* Both \(u_{i-1}\) and \(u_i\) belong to the cube edge \(e_i\). They either coincide or differ only in its direction. Since \(u_r=\tau u_0\), the sequence of contact vertices changes each coordinate an odd number \(m_j\) of times. Therefore \(r=s+\sum_jm_j\), giving (7) and (6). When \(r=n\), the identity forces \(s=0\) and \(m_j=1\) for all \(j\). Thus the lifted edges traverse every direction once from \(u_0\) to \(\tau u_0\), yielding an antipodal geodesic. The converse follows directly by cyclic completion of its turn sequence. \(\square\)

**Corollary 10 (minimal-cycle enumeration).** Both the monodromy-one cycles of length \(n\) and the monodromy-zero direction-rainbow star cycles of length \(n\) number
\[
\boxed{2^{n-2}(n-1)!}
\tag{8}
\]
when cycles are unoriented.

*Proof.* There are \(2^nn!\) directed antipodal geodesics with specified root. Each projected cycle has \(n\) choices of its initial edge-pair, two cyclic orientations, and two lifts, hence \(4n\) preimages. Division gives (8). Independently, every vertex of \(G_n\) supports \((n-1)!/2\) unoriented cyclic orders of its \(n\) incident direction-distinct edges, and \(G_n\) has \(2^{n-1}\) vertices. These star cycles are distinct, giving the same count. \(\square\)

Theorem 9 identifies full antipodal geodesics intrinsically as the shortest cycles with nontrivial covering monodromy. Theorem 7 supplies generators for its monodromy kernel using local triangles and squares. Consequently the turn-weight optimization of Article XI can be formulated over the shortest monodromy-one cycles, with no independent direction-rainbow condition. The support-weight bound needed for unrestricted NORI1 remains open.

### Direction-deleted graphic restrictions and a binary contraction normal form

Let \(n\ge3\), and let \(G_n=Q_n/\langle\tau\rangle\) be the folded cube under antipodal complementation. Put \(H_n=L(G_n)\), with \(V_i\subseteq V(H_n)\) the vertices corresponding to cube-edge pairs of direction \(i\). Let \(M_n\) be the binary matroid on \(E(H_n)\) represented by the vertex-edge incidence matrix \(B\) of \(H_n\), augmented by a row \(a\) recording the monodromy of the cover \(L(Q_n)\to H_n\). In particular, the cycles of \(M_n\) are the even-degree subgraphs of \(H_n\) having zero covering monodromy.

Fix a direction \(s\), set \(U_s=V(H_n)\setminus V_s\), and write \(m=2^{n-2}=|V_s|\).

**Theorem 1 (direction-deleted graphic flat).** There is a canonical isomorphism, after choosing the coordinate-\(s\) zero layer,
\[
H_n[U_s]\cong L(Q_{n-1}).
\tag{1}
\]
The restriction of \(M_n\) to \(E(H_n[U_s])\) is the graphic cycle matroid of \(L(Q_{n-1})\), of rank
\[
(n-1)2^{n-2}-1.
\tag{2}
\]
Moreover, \(E(H_n[U_s])\) is a flat of \(M_n\). Its complement consists of \(2(n-1)m\) turns, partitioned into \(2m\) families of \(n-1\) turns according to the two endpoints of each direction-\(s\) edge of \(G_n\).

*Proof.* Every antipodal vertex pair of \(Q_n\) has a unique representative with coordinate \(s\) equal to zero. Deleting the direction-\(s\) edges from \(G_n\) identifies its remaining graph with \(Q_{n-1}\) on those representatives. Taking line graphs gives (1).

Every closed walk in this direction-deleted graph lifts to a closed walk in the layer \(x_s=0\) of \(Q_n\). Its covering monodromy is zero. Thus the extra row \(a\) of a matrix representing \(M_n\), restricted to \(E(H_n[U_s])\), lies in the cut space of the connected graph \(H_n[U_s]\). The matroid restriction is graphic, with rank \(|U_s|-1=(n-1)2^{n-2}-1\). Every turn outside this restriction has one endpoint in \(V_s\), so its incidence column has a nonzero entry in the corresponding \(V_s\)-row; all columns of the restriction vanish on that row. Such an outside column lies outside their span, proving flatness.

Each vertex \(v\in V_s\) represents an edge \(e_v\) of \(G_n\) in direction \(s\). At each endpoint of \(e_v\), there are \(n-1\) other incident edges, producing \(n-1\) distinct turns incident with \(v\). Since the direction-\(s\) edges of \(G_n\) form a matching, these are all turns outside the restriction. \(\square\)

**Theorem 2 (paired-column contraction).** Let \(T\) be any spanning tree of \(H_n[U_s]\). Contract \(T\) in \(M_n\) and delete the loops arising from \(E(H_n[U_s])\setminus T\). The remaining matroid has rank \(m+1\) and admits over \(\mathbb F_2\) the representation
\[
\boxed{\quad
\{\,e_v^{\,n-1},\ (e_v+z)^{\,n-1}:v\in V_s\,\}
\subseteq\mathbb F_2^{\,V_s}\oplus\mathbb F_2 z .
\quad}
\tag{3}
\]
Here \(e_v^{\,n-1}\) means \(n-1\) parallel copies of the standard vector \(e_v\). The first family represents turns at the endpoint of a selected cube-edge lift with \(s\)-coordinate zero; the second represents turns at its endpoint with \(s\)-coordinate one.

*Proof.* Choose a representative of each antipodal cube-edge pair: for any direction other than \(s\), take its unique edge lying in \(x_s=0\); for every direction-\(s\) pair, choose either one of its two cube edges. Define the reference coloring \(c_0\) to be zero on all selected representatives and one on their antipodes, and let \(a\) be its induced turn cochain on \(H_n\).

A turn between two directions other than \(s\) occurs in the layer \(x_s=0\), giving \(a=0\). A turn involving a direction-\(s\) edge has \(a=0\) when the two incident edges meet at the selected direction-\(s\) representative's endpoint in \(x_s=0\), and \(a=1\) at its endpoint in \(x_s=1\). Indeed, every non-\(s\) edge in the latter layer is antipodal to its selected representative. For the quotient turn, choosing the antipodal lift of both edges leaves their color difference unchanged.

Hence the matrix \(\left(\begin{smallmatrix}B\\a\end{smallmatrix}\right)\) has zero last entry on every edge of \(H_n[U_s]\). Contracting \(T\) identifies all its vertices into one incidence vertex. Deleting the redundant incidence row leaves the \(m\) rows indexed by \(V_s\), together with the monodromy row \(z\). A turn incident with \(v\in V_s\) has incidence vector \(e_v\), with monodromy entry zero or one according to the endpoint family. This gives (3). Every other edge of \(H_n[U_s]\) becomes a loop, since its incidence column belongs to the span of the tree columns and its monodromy entry is zero.

The \(m\) columns \(e_v\), together with any column \(e_v+z\), span \(\mathbb F_2^{m+1}\), proving the rank assertion. \(\square\)

**Corollary 3 (independence and four-element circuits).** Delete parallel copies in (3), and put \(P_v=\{e_v,e_v+z\}\) for every \(v\in V_s\). A set of columns is independent if and only if it contains both members of at most one \(P_v\). For distinct \(v,w\), the four columns of \(P_v\cup P_w\) form a circuit. Consequently \(M_n\) has, for each direction \(s\), a rank-\((2^{n-2}+1)\) minor on \(2^{n-1}\) elements represented by
\[
\begin{pmatrix}
I_m&I_m\\
0&\mathbf1^T
\end{pmatrix}.
\tag{4}
\]

*Proof.* In a linear relation among the columns in (3), the \(e_v\)-coordinate forces the two coefficients from each \(P_v\) to be equal. The \(z\)-coordinate then forces the number of fully selected pairs to be even. A nonzero relation therefore exists if and only if at least two complete pairs occur; any two complete pairs form a minimal relation. Deleting duplicate columns gives (4). \(\square\)

The contraction exhibits the covering monodromy as one shared binary degree of freedom across all direction-\(s\) pairs. The normal form holds for every antipodally odd edge coloring because \(M_n\) is independent of the coloring within its prescribed switching class. Direction-rainbow witnesses and integer turn weights remain additional data in applications to switch minimization.

Let \(n\ge3\), let \(H_n=L(Q_n)/\langle\tau\rangle\), and write \(\alpha\) for the monodromy of the double covering \(L(Q_n)\to H_n\). An antipodally odd edge coloring \(c\) induces a binary turn weight \(d\) by
\[
d([\{e,f\}])=c(e)\oplus c(f)
\]
for cube edges \(e,f\) incident at one vertex. For a cycle \(C\) of \(H_n\), put \(w_d(C)=\sum_{t\in C}d(t)\), with the sum taken in the integers.

Consider a simple cycle \(C\) of length \(r\) with \(\alpha(C)=1\). Lift its cyclically ordered vertices to cube edges
\[
e_1,e_2,\ldots,e_r,e_{r+1}=\tau e_1.
\]
For \(1\le j\le r\), let \(u_j\) be the common endpoint of \(e_j,e_{j+1}\), and put \(u_0=\tau u_r\). Each pair \(u_{j-1},u_j\) consists of endpoints of \(e_j\). Write
\[
s(C)=|\{j:u_{j-1}=u_j\}|,
\qquad
m_i(C)=|\{j:u_{j-1}\ne u_j,\ e_j\text{ has direction }i\}|.
\]
These numbers are invariant under cyclic reindexing, reversal, and antipodal choice of lift. Since \(u_r=\tau u_0\), each \(m_i(C)\) is positive and odd. Hence, writing
\[
q(C)=\sum_{i=1}^n\frac{m_i(C)-1}{2},
\]
we obtain the directional-excess identity
\[
\boxed{|C|=n+s(C)+2q(C).}\tag{1}
\]

**Theorem 1 (monotone contraction of a stationary contact).** If \(s(C)>0\), there is a simple cycle \(C'\) of \(H_n\) such that
\[
\alpha(C')=1,\qquad |C'|=|C|-1,\qquad
s(C')=s(C)-1,\qquad q(C')=q(C),
\tag{2}
\]
and, simultaneously for every admissible turn weight \(d\),
\[
\boxed{w_d(C')\le w_d(C).}\tag{3}
\]
The difference \(w_d(C)-w_d(C')\) is either \(0\) or \(2\).

*Proof.* Choose an index \(j\) with \(u_{j-1}=u_j=v\), and cyclically reindex the lift so that \(2\le j\le r-1\). The three cube edges \(e_{j-1},e_j,e_{j+1}\) are distinct and meet at \(v\). Therefore the two turns
\[
[\{e_{j-1},e_j\}],\quad [\{e_j,e_{j+1}\}]
\]
can be replaced by the single turn \([\{e_{j-1},e_{j+1}\}]\). This removes the vertex \([e_j]\) from \(C\). Since \(C\) is simple and \(r\ge n+1\ge4\), the resulting closed walk \(C'\) is a simple cycle of length \(r-1\). The symmetric difference of the two cycles is a triangle of the clique of turns at \(v\). This triangle has monodromy zero, establishing \(\alpha(C')=\alpha(C)=1\).

The contact vertices of every retained cube edge are unchanged: the two contacts of the removed edge coincide at \(v\). Thus the removed index is the only one counted by \(s\), and the coordinate traversal counts \(m_i\) remain unchanged. This proves (2).

Set \(a=c(e_{j-1})\), \(b=c(e_j)\), and \(z=c(e_{j+1})\). All three colors are compared at the same cube vertex, and
\[
\begin{aligned}
w_d(C)-w_d(C')
&=(a\oplus b)+(b\oplus z)-(a\oplus z)\\
&=2\,\mathbf1_{\{a=z\ne b\}}\ \ge0.
\end{aligned}\tag{4}
\]
The replacement depends only on \(C\), so (3) holds for every antipodally odd edge coloring at once. \(\square\)

**Corollary 2 (moving-cycle normal form).** Every simple cycle \(C\) with \(\alpha(C)=1\) admits a sequence of \(s(C)\) triangle contractions ending at a simple cycle \(C^\circ\) with
\[
\alpha(C^\circ)=1,\quad s(C^\circ)=0,\quad
|C^\circ|=n+2q(C),\quad
w_d(C^\circ)\le w_d(C)
\tag{5}
\]
for every admissible \(d\). Consequently, if \(q(C)=0\), the terminal cycle is a length-\(n\) antipodal-geodesic cycle.

*Proof.* Repeatedly apply Theorem 1. The quantity \(s\) decreases by one at each contraction while \(q\) is preserved. When \(s=0\), (1) gives the length in (5). For \(q=0\), that length is \(n\), and the odd-girth characterization identifies the cycle with a full antipodal geodesic. \(\square\)

**Corollary 3 (weighted stability immediately above odd girth).** For every admissible \(d\),
\[
\boxed{
\min_{\substack{C\text{ simple}\\\alpha(C)=1,\ |C|\le n+1}}w_d(C)
=
\min_{\substack{C\text{ simple}\\\alpha(C)=1,\ |C|=n}}w_d(C).
}\tag{6}
\]
In particular, the minimum \(\mu(c)\) of the number of color changes on a full antipodal geodesic satisfies
\[
\mu(c)=
\min_{\substack{C\text{ simple}\\\alpha(C)=1,\ |C|\le n+1}}
w_d(C)-1.
\tag{7}
\]

*Proof.* Odd girth gives \(|C|\ge n\). If \(|C|=n+1\), identity (1) forces \(s(C)=1\) and \(q(C)=0\), so Theorem 1 supplies a length-\(n\) cycle of no greater weight. The reverse inequality follows by inclusion. Equation (7) then follows from cyclic rotation of a full antipodal geodesic: its cyclic turn weight is odd, and omitting any turn of weight one as the terminal seam yields a rooted geodesic with \(w_d(C)-1\) changes. \(\square\)

**Corollary 4 (the first repeated-direction obstruction).** Let \(C\) have \(\alpha(C)=1\) and \(|C|=n+2\). Either \(s(C)=2,q(C)=0\), in which case \(C\) contracts through a length-\((n+1)\) cycle to a length-\(n\) cycle without increasing any admissible turn weight, or \(s(C)=0,q(C)=1\). In the latter case every contact traverses a cube edge, and its direction sequence traverses one coordinate three times and each other coordinate once.

More generally, if \(\mu(c)\ge4\), every monodromy-one cycle \(C\) with \(w_d(C)\le3\) has \(q(C)\ge1\). Thus a low-weight circuit obstructed from shortening to a geodesic must include repeated coordinate traversal.

*Proof.* The dichotomy at length \(n+2\) follows from \(s+2q=2\), with \(s,q\) nonnegative integers. Apply Corollary 2 in the first case. In the second, \(\sum_i(m_i-1)/2=1\) with all \(m_i\) odd and positive, yielding the asserted direction counts. Finally, if \(q(C)=0\) and \(w_d(C)\le3\), Corollary 2 yields a length-\(n\) cycle of weight at most three, and (7) gives \(\mu(c)\le2\). \(\square\)

The contractions use only triangles within cube-edge stars and work simultaneously for every representative of the admissible switching class. Their scope is determined by the directional excess \(q\). After all stationary contacts are removed, further shortening must address coordinate directions traversed at least three times; such steps need not admit a non-increasing triangle contraction.

Let \(n\ge3\), let \(H=H_n=L(Q_n)/\langle\tau\rangle\), and put \(N=|V(H)|=n2^{n-2}\). Let \(B\in\mathbb F_2^{V(H)\times E(H)}\) be the unoriented vertex-edge incidence matrix over \(\mathbb F_2\). Fix \(a\in\mathbb F_2^{E(H)}\) representing the nontrivial covering-monodromy class \(\alpha\), so that \(a(C)=\alpha(C)\) on all binary cycles of \(H\). Every antipodally odd cube-edge coloring determines a turn cochain \(d=a+\delta f\), where \(\delta f=f^TB\); conversely each such cochain arises from an admissible coloring, unique up to complement. We use \(w_d(F)=\sum_{t\in F}d(t)\) for the *integer* support weight of a set of turns \(F\).

Introduce one distinguished element \(p\) outside \(E(H)\), and represent a binary matroid \(\widehat M_n\) on \(E(H)\cup\{p\}\) by the matrix
\[
\widehat A=
\begin{pmatrix} B&0\\ a&1\end{pmatrix}.
\tag{1}
\]
Write \(D_n=\widehat M_n^*\) for its dual. Deletion of \(p\) from \(\widehat M_n\) gives the even-cycle matroid \(M_n\) of the previous Subsections. Since \(B\) has rank \(N-1\), and the bottom row of (1) is independent of the other rows, \(\operatorname{rank}\widehat M_n=N\), and \(\operatorname{rank}D_n=|E(H)|+1-N\).

**Theorem 1 (port-containing cycles and cocircuits).** The binary cycles of \(D_n\) containing \(p\) are precisely
\[
\boxed{X_d=\operatorname{supp}(d)\cup\{p\},
\qquad d=a+\delta f.}
\tag{2}
\]
The cocircuits of \(D_n\) containing \(p\) are precisely
\[
\boxed{Y_C=C\cup\{p\},\qquad
C\text{ a simple cycle of }H\text{ with }\alpha(C)=1.}
\tag{3}
\]
For every such pair,
\[
\boxed{|X_d\cap Y_C|=1+w_d(C)\equiv0\pmod2.}
\tag{4}
\]
The coloring-dependent support \(X_d\) may be a union of several dual circuits; the statement (2) concerns all binary cycles, not just circuits.

*Proof.* The binary cycle space of the dual of a represented binary matroid is the row space of its representing matrix. The row space of (1) consists of \((\delta f,0)\) and \((a+\delta f,1)\), proving (2). A cocircuit of \(D_n\) is a circuit of \(\widehat M_n\). A set \(F\cup\{p\}\) is dependent in \(\widehat M_n\) precisely when its characteristic vector satisfies \(B\mathbf1_F=0\) and \(a(F)=1\). Decompose the Eulerian binary edge set \(F\) into edge-disjoint graph-theoretic simple cycles. At least one has odd monodromy; therefore minimality forces \(F\) to consist of a single simple odd-monodromy cycle. Conversely, an odd-monodromy simple cycle together with \(p\) is a minimal dependent set: a proper nonempty subset of the simple cycle is never Eulerian. This proves (3). Finally,
\[
|X_d\cap Y_C|=1+\sum_{t\in C}d(t)
\]
and \(d(C)=a(C)+(\delta f)(C)=1\) in \(\mathbb F_2\), establishing (4). \(\square\)

**Theorem 2 (minimum port cocircuits are antipodal geodesics).** Every cocircuit of \(D_n\) containing \(p\) has size at least \(n+1\), and equality occurs precisely for the circuits \(Y_C\) of (3) whose cycle \(C\) is the cyclic turn cycle of a full antipodal geodesic of \(Q_n\):
\[
\boxed{\mathcal Y_n=
\{Y\in\mathcal C^*(D_n):p\in Y,\ |Y|=n+1\}.}
\tag{5}
\]
The cardinality condition in (5), together with the pointed matroid, intrinsically recognizes the geodesic witness family. In particular, no auxiliary direction-rainbow predicate is needed.

*Proof.* The odd-girth theorem proved earlier in Article XI says that every simple cycle \(C\) of \(H\) with \(\alpha(C)=1\) has \(|C|\ge n\), with equality precisely for cyclically completed full antipodal geodesics. For clarity, lift its ordered turn vertices to cube edges \(e_1,\ldots,e_r,e_{r+1}=\tau e_1\). Let \(u_j\) denote the common endpoint of \(e_j,e_{j+1}\), with \(u_0=\tau u_r\). For each \(j\), either \(u_{j-1}=u_j\) or they differ in the direction of \(e_j\). Since \(u_r=\tau u_0\), each of the \(n\) coordinate directions is traversed an odd, hence positive, number of times, giving \(r\ge n\). If \(r=n\), each coordinate is traversed once and no stationary contact occurs, so the edges form a full antipodal geodesic. Conversely, every full antipodal geodesic yields such a length-\(n\) odd-monodromy turn cycle. Apply Theorem 1. \(\square\)

**Corollary 3 (cycle–cocircuit intersection formulation).** Let \(\mu(c)\) be the minimum number of color changes in a full antipodal geodesic for a coloring with turn cochain \(d\). Then
\[
\boxed{\mu(c)=
\min_{Y\in\mathcal Y_n}|X_d\cap Y|-2.}
\tag{6}
\]
Consequently the unrestricted two-switch conjecture is equivalent to the following statement about the fixed pointed binary matroid \((D_n,p)\):
\[
\boxed{\forall X\in Z(D_n)\text{ with }p\in X,\quad
\exists Y\in\mathcal Y_n:\ |X\cap Y|\le4.}
\tag{7}
\]
The stronger unrestricted NORI1 assertion is equivalent to requiring \(|X\cap Y|=2\). All intersections in (7) are even by (4).

*Proof.* Theorem 2 identifies \(Y\setminus\{p\}\) with the cyclic turn cycle of a full antipodal geodesic. The cyclic-rotation identity gives the optimal number of switches among roots of the same cyclic path as \(w_d(Y\setminus\{p\})-1\). By (4) that equals \(|X_d\cap Y|-2\). Take the minimum over all cycles and use (2) to translate the universal quantifier. \(\square\)

We next distinguish dual *circuits* from arbitrary dual cycles. Write \(D=\operatorname{supp}(d)\) and let \(H_0(d)=(V(H),E(H)\setminus D)\). In the cube interpretation, \(H_0(d)\) retains precisely the turns joining edges of the same color.

**Theorem 4 (dual-circuit connectivity criterion).** For every admissible turn cochain \(d\),
\[
\boxed{\quad
X_d=D\cup\{p\}\text{ is a circuit of }D_n
\quad\Longleftrightarrow\quad H_0(d)\text{ is connected}.
\quad}
\tag{8}
\]

*Proof.* By (2), \(X_d\) is a binary cycle of \(D_n\). It is a circuit if and only if it contains no proper nonempty binary cycle. Any nonzero dual cycle contained in \(X_d\) and avoiding \(p\) is of the form \(\operatorname{supp}(\delta g)\) for a nonconstant binary vertex function \(g\) of \(H\). Conversely, if a proper nonzero dual cycle \(X'\subsetneq X_d\) contains \(p\), its disjoint complement \(X_d\setminus X'\) is a nonzero dual cycle avoiding \(p\), again of the form \(\operatorname{supp}(\delta g)\). Thus \(X_d\) is a circuit precisely when there is no nonempty graph cut \(\operatorname{supp}(\delta g)\subseteq D\). Such a cut exists if and only if the graph \(H_0(d)\) is disconnected: one direction takes \(g\) to be a component indicator, and the other observes that a cut contained in \(D\) has no edge joining different \(g\)-classes in \(H_0(d)\). \(\square\)

**Theorem 5 (dual-circuit reduction and even cut penalty).** Let \(d=a+\delta f\) be arbitrary. There exist another admissible turn cochain \(d'\) and a graph cut cochain \(b=\delta g\) such that
\[
\boxed{
d=d'+b\quad\text{over }\mathbb F_2,\qquad
\operatorname{supp}(d')\cap\operatorname{supp}(b)=\varnothing,\qquad
\operatorname{supp}(b)\subseteq\operatorname{supp}(d),
}
\tag{9}
\]
and \(X_{d'}=\operatorname{supp}(d')\cup\{p\}\) is a *circuit* of \(D_n\). Hence the dual-cycle decomposition
\[
\boxed{X_d=X_{d'}\ \dot\cup\
\operatorname{supp}(b)}
\tag{10}
\]
has disjoint supports. For every binary cycle \(C\) of \(H\),
\[
\boxed{w_d(C)=w_{d'}(C)+|\operatorname{supp}(b)\cap C|,
\qquad |\operatorname{supp}(b)\cap C|\equiv0\pmod2.}
\tag{11}
\]

*Proof.* Let the connected components of \(H_0(d)\) be \(K_1,\ldots,K_r\). Contract each \(K_j\) to a vertex, retaining the edges of \(D\) between different components. The resulting multigraph \(J\) is connected because \(H\) is connected. Choose a spanning tree \(T\) of \(J\), bipartition its vertices, and let \(g:V(H)\to\mathbb F_2\) be constant on each \(K_j\), taking opposite values at endpoints of every edge of \(T\). Thus \(b=\delta g\) vanishes on every edge outside \(D\) and equals one on each edge of \(T\). Let \(d'=d+b\). It is admissible because it differs from \(d\) by a cut. Its support is contained in that of \(d\), with the removed edges given by \(\operatorname{supp}(b)\), proving (9). The zero-turn graph \(H_0(d')\) contains every component \(K_j\) and all edges of \(T\); it is connected. Theorem 4 therefore makes \(X_{d'}\) a dual circuit and proves (10). Finally, the supports in (9) are disjoint, giving the integer weight identity in (11), while every cut meets every graph cycle in an even number of edges. \(\square\)

**Limitation and research target.** Theorem 5 is a support-minimizing reduction, but a low-intersection cocircuit for \(X_{d'}\) need not have low intersection with \(X_d\). The added term in (11) can be large. Consequently a proof for port-containing dual *circuits* alone does not establish (7) for arbitrary port-containing dual cycles. A sufficient strengthening would select \(Y\in\mathcal Y_n\) with simultaneous control of
\[
|X_{d'}\cap Y|+|\operatorname{supp}(b)\cap Y|.
\tag{12}
\]
In particular, a zero-cut-penalty witness for each reduction would lift its full intersection bound to the original coloring. The obstruction is now localized to the interaction of minimum port cocircuits with the graph cuts supported on a signature.

Theorem 2 gives an intrinsic matroidal recognition of all geodesic witnesses, Theorem 4 identifies when a coloring support itself becomes a dual circuit, and Theorem 5 decomposes arbitrary colorings into a dual-circuit core and a nonnegative even cut-crossing penalty. These structural statements are valid for every dimension and every admissible coloring.

**Proposition 6 (explicit dual representation and cographic deletion).** Let \(z_1,\ldots,z_r\) be any binary basis of the graphic cycle space \(Z_1(H;\mathbb F_2)\), where \(r=|E(H)|-|V(H)|+1\). Then \(D_n=\widehat M_n^*\) is represented by the binary \(r\times(|E(H)|+1)\) matrix whose \(j\)th row is
\[
\boxed{\bigl(z_j,\alpha(z_j)\bigr).}\tag{13}
\]
Its deletion of the distinguished element is cographic:
\[
\boxed{D_n\setminus p=M(H)^*.}\tag{14}
\]
Thus \(D_n\) is a specified single-element extension of the cographic matroid \(M(H)^*\), and the port column records the covering monodromy on the graphic cycle space.

*Proof.* A vector \((z,t)\) belongs to the kernel of the matrix (1) if and only if \(Bz=0\) and \(a(z)+t=0\). Therefore
\[
\ker\widehat A=\{(z,\alpha(z)):z\in Z_1(H;\mathbb F_2)\}.
\]
The kernel of a binary matrix representing a matroid is the row space of a matrix representing its dual, so the vectors in (13) form a dual representation. Deleting the last column gives the cycle-space basis \(z_1,\ldots,z_r\) of \(H\), which represents the cographic matroid \(M(H)^*\). Equivalently, contracting the column \(p=(0,1)^T\) in (1) removes the monodromy row and leaves the graphic incidence matrix \(B\), and duality exchanges contraction and deletion. \(\square\)

**Geometric interpretation.** Under the covering \(L(Q_n)\to H_n\), the connected components of \(H_0(d)\) are the antipodal orbits of connected monochromatic edge-components upstairs. Theorem 4 therefore translates the dual-circuit condition into a connectivity statement about monochromatic edge components. In Theorem 5 the cut penalty is always even on a geodesic cycle; controlling this penalty jointly with the port-circuit intersection is the additional condition required for a universal low-switch conclusion.

Let \(n\ge3\), and retain the folded-cube line graph \(H=H_n=L(Q_n)/\langle\tau\rangle\), its antipodal monodromy \(\alpha\), and the admissible turn cochain \(d=a+\delta f\). For an edge set or closed walk \(W\) of \(H\), write
\[
w_d(W)=\sum_{\text{traversed turns }t} d(t)
\tag{1}
\]
with integer multiplicity. The parity identity is
\[
w_d(W)\equiv\alpha(W)\pmod2
\tag{2}
\]
for every closed walk \(W\).

Put
\[
H_0(d)=(V(H),\{t:d(t)=0\}).
\]
Let its connected components be \(K_1,\ldots,K_r\). Define the **monochromatic-component quotient** \(J_d\) by contracting every \(K_i\) to one vertex, retaining one edge for each turn \(t\) with \(d(t)=1\). Loops and parallel edges are permitted. Let \(g_{\rm odd}(J_d)\) denote the minimum length of an odd cycle of this multigraph, with a loop counted as a cycle of length one.

**Theorem 1 (odd-girth identity).** For every admissible antipodally odd coloring, in every dimension,
\[
\boxed{\displaystyle
g_{\rm odd}(J_d)=
\min_{\substack{C\subseteq H\text{ a simple cycle}\\
\alpha(C)=1}} w_d(C).}
\tag{3}
\]
In particular, \(J_d\) is nonbipartite and its odd girth is finite and odd.

*Proof.* If \(C\) is a simple cycle with \(\alpha(C)=1\), contract the portions of \(C\) lying in \(H_0(d)\). The result is a closed walk of \(J_d\) of length \(w_d(C)\), which is odd by (2). Any odd closed walk in a multigraph contains an odd cycle of length at most its length. Thus
\[
g_{\rm odd}(J_d)\le w_d(C).
\]

For the reverse inequality, take a shortest odd cycle \(Z\) of \(J_d\). Each of its edges arises from a turn of \(H\) with \(d=1\). At each intervening contracted vertex \(K_i\), join the endpoints of consecutive turns by a path of zero-turn edges inside \(K_i\). This produces a closed walk \(W\) of \(H\) satisfying \(w_d(W)=|Z|\). By (2), \(\alpha(W)=1\). Splitting \(W\) at repeated vertices, and discarding any immediate backtracking, decomposes it into closed subwalks of total weight at most \(|Z|\), at least one of which has nonzero monodromy. Repeating this splitting yields a simple cycle \(C\) with \(\alpha(C)=1\) and \(w_d(C)\le|Z|\). The two inequalities prove (3). The monodromy class is nonzero because an antipodal-geodesic turn cycle has monodromy one, so some such cycle exists; therefore \(J_d\) is not bipartite. \(\square\)

Let \(\mu_{\rm path}(c)\) denote the minimum number of color changes among **arbitrary** paths of \(Q_n\) joining a vertex to its antipode, with no geodesicity requirement. Repeated vertices or edges may be allowed during an intermediate walk: removing a closed detour cannot increase the number of changes of a binary color word, by the triangle inequality for the discrete metric on \(\{0,1\}\).

**Theorem 2 (full antipodal-path duality).** For every antipodally odd coloring,
\[
\boxed{\displaystyle
\mu_{\rm path}(c)=g_{\rm odd}(J_d)-1.}
\tag{4}
\]
In particular, the minimum number of switches on an unrestricted antipodal path is even.

*Proof.* Let \(C\) attain the minimum in (3), with odd weight \(w=w_d(C)\). Lift its cyclic turn sequence to a sequence \(e_1,\ldots,e_m,e_{m+1}=\tau e_1\) of cube edges. If at some cube edge the contact vertices with its predecessor and successor coincide, remove that stationary edge from the turn sequence, replacing two turns in one vertex star by the third side of the corresponding star triangle. The triangle inequality
\[
(c(e_-)\oplus c(e))+(c(e)\oplus c(e_+))
\ge c(e_-)\oplus c(e_+)
\]
shows that each removal does not increase turn weight, and the star triangle has zero monodromy. As established by the stationary-contact contraction theorem earlier in Article XI, repetition ends with a cyclic sequence whose contacts traverse a cube-edge walk from a vertex to its antipode. Its new cyclic turn weight \(w'\) is odd and at most \(w\).

The cyclic sequence of edge colors is antipodally complementary after one traversal. By moving the cut in this cyclic sequence, each comparison in its cyclic turn count can be chosen as the terminal seam of an antipodal walk. As \(w'\) is positive and odd, some turn has weight one. Choosing that turn as the seam yields an antipodal walk with \(w'-1\le w-1\) changes. Erasing self-intersections does not increase the switch count. Thus \(\mu_{\rm path}(c)\le g_{\rm odd}(J_d)-1\).

Conversely, let \(P\) be an antipodal cube-edge path with \(k\) switches. Follow its edge sequence in \(L(Q_n)\). Its last edge is incident with the antipode of the initial vertex, as is the antipode of its first edge; adjoining the latter creates a closed turn walk in \(H\) with monodromy one. If the last edge is already the antipode of the first, no additional turn is needed. The resulting walk has at most \(k+1\) turns of weight one: the original \(k\) switches, plus possibly the terminal seam. Applying the first part of Theorem 1 to this closed walk gives \(g_{\rm odd}(J_d)\le k+1\). Taking a minimizing path proves the reverse inequality. Equation (4) follows; parity of the odd girth makes the minimum even. \(\square\)

**Corollary 3 (monochromatic antipodal paths as quotient loops).** The following statements are equivalent:
1. \(J_d\) has a loop;
2. \(\mu_{\rm path}(c)=0\);
3. some connected monochromatic cube-edge component contains a vertex and its antipode;
4. for some monochromatic cube-edge component \(A\), the vertex sets of \(A\) and its antipodal image \(\tau A\) intersect.

Thus the original, nongeodesic Norine antipodal monochromatic-path statement is equivalent to the assertion that every admissible coloring has a loop in its monochromatic-component quotient. Wu and Yang proved that statement in 2026; the geodesic strengthening remains open.

*Proof.* A loop means \(g_{\rm odd}(J_d)=1\), which is equivalent to (2) by Theorem 2. A monochromatic path between antipodal vertices lies within one monochromatic edge-component, proving equivalence of (2) and (3). Finally, if \(v\in A\cap\tau A\), then both \(v\) and \(\tau v\) lie in \(A\), and conversely any antipodal vertex pair lying in \(A\) yields such an intersection. \(\square\)

Let \(\mu_{\rm geo}(c)\) be the minimum number of switches among full antipodal *geodesics*. By the pointed-matroid theorem of the preceding Subsection,
\[
\mu_{\rm geo}(c)=
\min_{\substack{Y\in\mathcal C^*(D_n)\\
p\in Y,\ |Y|=n+1}} |X_d\cap Y|-2.
\tag{5}
\]

**Corollary 4 (geodesicity penalty).** The difference
\[
\boxed{\displaystyle
\Gamma(c)=\mu_{\rm geo}(c)-\mu_{\rm path}(c)
=\min_{\substack{\alpha(C)=1\\|C|=n}}w_d(C)
-\min_{\alpha(C)=1}w_d(C)
}
\tag{6}
\]
is a nonnegative even integer. An unrestricted two-switch counterexample, if one exists, must exhibit one of two phenomena: either \(g_{\rm odd}(J_d)\ge5\), which would also violate the unrestricted nongeodesic two-switch bound, or \(g_{\rm odd}(J_d)\le3\) but \(\Gamma(c)\ge2\). In the latter case, every low-weight odd-monodromy cycle of weight at most three has positive repeated-coordinate excess \(q(C)\ge1\), by the preceding stationary-contact contraction theorem.

*Proof.* The equality follows from Theorem 2 and the cyclic turn formula (5), and parity gives evenness. If the minimum among length-\(n\) odd cycles is at least five, then either the unrestricted odd girth is at least five or there is an odd cycle of weight at most three. Such a cycle cannot have \(q(C)=0\), since the stationary-contact contraction theorem would then produce a length-\(n\) odd cycle of no greater weight, contradicting the assumed geodesic minimum. \(\square\)

Theorem 2 identifies the shortest odd-cycle problem in the pointed binary matroid with the classical unrestricted antipodal-path problem. Equation (6) isolates the additional geodesicity difficulty as a measurable, even-valued defect. In particular, general matroid circuit-cocircuit principles can guarantee small intersections for unrestricted port cocircuits only insofar as they address the nongeodesic problem; the fixed length condition \(|Y|=n+1\) demands further cube geometry. The component-quotient reduction is valid without assuming any degree balance, sparse curvature, or special coloring structure.

**Theorem 5 (maximum-cut extraction of a dual-circuit core).** Let \(D=\operatorname{supp}(d)\), and let \(J=J_d\) be its connected component quotient, retaining loops. Write \(\operatorname{mc}(J)\) for its maximum cut cardinality, with multiplicities. Among admissible cochains \(d'=d+\delta g\) satisfying \(\operatorname{supp}(d')\subseteq D\),
\[
\boxed{\min |\operatorname{supp}(d')|=|D|-\operatorname{mc}(J).}\tag{7}
\]
Every minimizer has connected zero-turn graph \(H_0(d')\); in particular \(X_{d'}=\operatorname{supp}(d')\cup\{p\}\) is a circuit of the pointed dual matroid. If \(S\) is any maximum cut of \(J\), and \(b_S\) its pullback to \(H\), then
\[
\boxed{\operatorname{supp}(d)=\operatorname{supp}(d')\ \dot\cup\ \operatorname{supp}(b_S)}
\tag{8}
\]
for \(d'=d+b_S\) over \(\mathbb F_2\), and every closed walk \(W\) satisfies
\[
\boxed{w_d(W)=w_{d'}(W)+|\operatorname{supp}(b_S)\cap W|,\quad
|\operatorname{supp}(b_S)\cap W|\equiv0\pmod2.}\tag{9}
\]

*Proof.* The support inclusion \( \operatorname{supp}(d+\delta g)\subseteq D\) holds if and only if \(\delta g\) vanishes on every zero-turn edge. Thus \(g\) is constant on each connected component of \(H_0(d)\), and induces a vertex bipartition of \(J\). Precisely the edges crossing that bipartition are deleted from \(D\). This proves (7) and (8).

We claim that the crossing-edge subgraph of every maximum cut in a connected multigraph \(J\) is connected and spans \(V(J)\). Otherwise take one connected component \(U\) of this crossing-edge subgraph. Every edge between \(U\) and its complement is noncrossing, and at least one exists because \(J\) is connected. Reversing the bipartition on all vertices of \(U\) preserves its previously crossing edges and makes each edge from \(U\) to its complement crossing, increasing the cut size. This is impossible. When \(J\) has one vertex the claim is immediate. Consequently, \(H_0(d')\) contains all original zero-turn components and the edges of a connected spanning crossing subgraph, so it is connected. The dual-circuit connectivity theorem identifies \(X_{d'}\) as a dual circuit. Disjointness in (8) gives the weight identity in (9), and cut-cycle orthogonality gives its evenness. \(\square\)

**Proposition 6 (minimal odd-cycle transversals).** For an admissible turn cochain \(d\) on \(H\), the following are equivalent:

(i) \(X_d=D\cup\{p\}\) is a circuit of the pointed dual;

(ii) \(H_0(d)\) is connected;

(iii) \(D\) is an inclusion-minimal edge set meeting every monodromy-one simple cycle of \(H\);

(iv) each turn \(e\in D\) has a monodromy-one simple-cycle witness \(C_e\) satisfying \(C_e\cap D=\{e\}\).

*Proof.* The dual-circuit criterion gives (i) if and only if (ii). If (ii) holds, join the endpoints of any \(e\in D\) by a simple zero-turn path. Adding \(e\) gives a simple cycle of weight one, hence odd monodromy. This proves (iv), which implies (iii) because each \(C_e\) loses its sole intersection when \(e\) is removed.

If (ii) fails, connectivity of \(H\) supplies \(e\in D\) connecting different zero-turn components. A monodromy-one cycle containing \(e\) cannot contain only one edge of \(D\), since the other edges would then connect the distinct zero-turn components. By parity, it contains at least three edges of \(D\). Thus removing \(e\) from \(D\) leaves every monodromy-one cycle intersected, contradicting (iii). Therefore (iii) implies (ii). \(\square\)

The maximum-cut representative is a minimum-cardinality signature among representatives whose support is contained in \(D\). The decomposition (9) exhibits the nonnegative even crossing penalty on every geodesic cycle. Controlling this penalty simultaneously with the core circuit intersection remains necessary for a universal two-switch proof.

**Corollary 7 (Wu–Yang's theorem gives an unconditional two-intersection cocircuit).** The theorem of Hehui Wu and Ningyuan Yang, *A Chain-Level Borsuk--Ulam Obstruction Proof of Norine's Antipodal-Coloring Conjecture*, arXiv:2607.19276 (July 2026), states that every antipodally odd edge coloring of \(Q_n\), \(n\ge2\), has a monochromatic antipodal path, without a geodesicity requirement. Combining that theorem with Theorems 1 and 2 gives, for every \(n\ge3\) and every admissible turn signature \(d\),
\[
\boxed{g_{\rm odd}(J_d)=1,\qquad \mu_{\rm path}(c)=0.}\tag{10}
\]
Equivalently, every \(H_0(d)\) has a connected component containing both endpoints of some turn with \(d=1\). In the pointed binary dual matroid \(D_n\),
\[
\boxed{\displaystyle
\forall X\in Z(D_n)\ (p\in X),\quad
\exists Y\in\mathcal C^*(D_n)\ (p\in Y):
\ |X\cap Y|=2.}
\tag{11}
\]
There is no bound on \(|Y|\) in (11). The two-switch *geodesic* conjecture is the strengthening that requires \(|Y|=n+1\) and allows the intersection to be at most four.

*Proof.* Apply the Wu--Yang monochromatic antipodal-path theorem, so \(\mu_{\rm path}(c)=0\). Equation (4) gives \(g_{\rm odd}(J_d)=1\). A loop in \(J_d\) is a turn \(e\) with \(d(e)=1\) whose endpoints are joined by a zero-turn path in \(H_0(d)\). Their union contains a simple monodromy-one cycle \(C\) with \(w_d(C)=1\). Theorem 1 of the preceding pointed-lift Subsection makes \(C\cup\{p\}\) a cocircuit \(Y\) of \(D_n\), and its intersection with \(X_d\) has cardinality \(1+w_d(C)=2\). Every port-containing dual cycle equals \(X_d\) for some admissible signature, so the quantifiers follow. \(\square\)

**Corollary 8 (only geodesicity can obstruct the conjecture).** For every admissible coloring,
\[
\boxed{\Gamma(c)=\mu_{\rm geo}(c),}
\tag{12}
\]
and an obstruction to \(\mu_{\rm geo}(c)\le2\), if one exists, must force every monodromy-one turn cycle of weight one to have positive repeated-direction excess \(q(C)\), or it would contract to a length-\(n\) geodesic turn cycle of weight one. More generally, every odd-monodromy cycle of weight at most three in such an obstruction must have \(q(C)\ge1\). These are unrestricted necessary conditions, and the existence of the weight-one cycles is unconditional by Wu--Yang.

The topological theorem in the cited paper does not constrain the lengths of its monochromatic paths. Consequently (11) does not imply the desired minimum-size cocircuit intersection; that restriction is the remaining issue of Article XI.

### Intrinsic star statistics and quantitative port–cocircuit exchange bounds

Let \(n\ge5\), \(G_n=Q_n/\langle\tau\rangle\), and \(H_n=L(G_n)\). Use the pointed binary matroid \(D_n\) with port \(p\) from the preceding Subsection. Let \(X\) be an arbitrary binary cycle of \(D_n\) containing \(p\), and put \(d(t)=\mathbf1_{\{t\in X\}}\) for \(t\in E(H_n)\). Thus \(d=a+\delta f\), where \(a\) represents covering monodromy. Write
\[
\mathcal Y_n=\{Y\in\mathcal C^*(D_n):p\in Y,\ |Y|=n+1\},\quad
I(X)=\min_{Y\in\mathcal Y_n}|X\cap Y|.
\tag{1}
\]
The minimum is even and the optimal antipodal-geodesic switch count is \(I(X)-2\).

For each vertex \(v\) of \(G_n\), its \(n\) incident edges determine a clique \(K_n(v)\) of turns in \(H_n\), with directions \(1,\ldots,n\). Write \(d_{ij}(v)\) for the label on the turn between directions \(i,j\). Since \(d\) sums to zero on star triangles, there is a binary assignment \(s_i(v)\) to the incident directions satisfying
\[
d_{ij}(v)=s_i(v)+s_j(v).
\tag{2}
\]
The assignment is determined up to simultaneous complementation, and therefore
\[
b_X(v)=\min\bigl(\#\{i:s_i(v)=0\},\#\{i:s_i(v)=1\}\bigr)
\tag{3}
\]
is intrinsic to \(X\). In particular, no lift of a cube-edge coloring is needed to evaluate \(b_X(v)\).

Put \(m=\min(k,n-k)\), and define
\[
\lambda_n(k)=
\begin{cases}
0,&m=0,\\
\dfrac{4k(n-k)(m-1)}{n(n-1)(n-2)},&0<m<n/2,\\
\dfrac{4k(n-k)(m-2)}{n(n-1)(n-3)},&m=n/2,
\end{cases}
\quad q_n=\left\lfloor\frac{n-1}{3}\right\rfloor,
\quad\Phi_n(k)=\frac{2k(n-k)}{n-1}-\frac{q_n}{2}\lambda_n(k).
\tag{4}
\]
The last branch of \(\lambda_n\) occurs only in even dimension. For the two opposite corners of a projected coordinate square write \(v^{ij}=v\oplus e_i\oplus e_j\) in \(G_n\), and define
\[
\eta_n(k)=
\begin{cases}
0,&m=0,\\
\dfrac{2(m-1)}{n-2}+
\dfrac{\mathbf1_{\{n\ {\rm even},\,k=n/2\}}}{n-3},&m\ge1;
\end{cases}
\tag{5}
\]
\[
\mathscr K(X)=
\frac1{2^{n-1}n(n-1)}
\sum_{v\in V(G_n)}\ \sum_{i\ne j}
[d_{ij}(v)=1,\ d_{ij}(v^{ij})=0]\,
\eta_n(b_X(v)).
\tag{6}
\]
This is a nonnegative statistic determined by the port-containing cycle \(X\).

**Theorem (intrinsic quantitative port intersection).** Every port-containing binary cycle \(X\) of \(D_n\) satisfies
\[
\boxed{\quad I(X)\le
2+2\left\lfloor
\frac{\displaystyle
\frac1{2^{n-1}}\sum_{v\in V(G_n)}\Phi_n(b_X(v))
-\frac{q_n}{2}\mathscr K(X)-1}{2}
\right\rfloor.\quad}
\tag{7}
\]
Consequently, if \(I(X)\ge6\), then
\[
\boxed{\quad
\frac1{2^{n-1}}\sum_v\Phi_n(b_X(v))
-\frac{q_n}{2}\mathscr K(X)\ge5.\quad}
\tag{8}
\]
The bound holds for arbitrary \(X\) in the affine port-cycle family, irrespective of whether \(X\) is a circuit of \(D_n\).

*Proof.* By the pointed-lift representation, reconstruct an antipodally odd coloring \(c\) of the cube edges whose turn cochain is \(d\). For every vertex \(u\) of \(Q_n\), write \(k_u=\#\{i:c_i(u)=1\}\). Antipodal vertices have complementary incident colors and hence \(k_{\bar u}=n-k_u\); equation (2) implies
\[
\frac1{2^n}\sum_{u\in Q_n}\Phi_n(k_u)
=\frac1{2^{n-1}}\sum_{v\in V(G_n)}\Phi_n(b_X(v)).
\tag{9}
\]
The two-corner comparison \(d_{ij}(u)\), \(d_{ij}(u^{ij})\) is invariant under simultaneous antipodal complementation, so the analogous cube average defining the exchange curvature gain equals (6).

For completeness, the cyclic comparison count on a full geodesic with ordered directions \(p_1,\ldots,p_n\) and colors \(w_1,\ldots,w_n\) is
\[
T(P)=\sum_{r=1}^{n-1}[w_r\ne w_{r+1}]
+[w_n\ne1-w_1].
\tag{10}
\]
It is an odd positive integer. Rotating the root across the first coordinate and moving that direction to the end deletes one of these \(n\) cyclic comparisons; choosing a changed comparison gives a full geodesic with \(T(P)-1\) switches. Uniform sampling over cube roots and full coordinate orders gives
\[
\mathbb ET(P)=\frac1{2^n}\sum_u\frac{2k_u(n-k_u)}{n-1}.
\tag{11}
\]
Indeed each turn sees a uniformly sampled cube vertex and an ordered pair of distinct incident directions.

For a consecutive four-direction block \(h,i,j,\ell\), exchange \(i,j\). If \(v\) is the contact vertex after the \(h\)-step and \(w=v^{ij}\), the resulting change in \(T\) is
\[
\Delta=d_{hj}(v)-d_{hi}(v)
+d_{ij}(v^j)-d_{ij}(v^i)
+d_{i\ell}(w)-d_{j\ell}(w),
\tag{12}
\]
where the right-hand side is in the integers, with binary turn labels interpreted as zero or one. By the parity relation around the square, the middle difference vanishes when \(d_{ij}(v)=d_{ij}(w)\), and otherwise has absolute value one. Conditional averaging over the other two directions gives the four-case estimate
\[
\mathbb E|\Delta|\ge
\frac1{2^n}\sum_u\lambda_n(k_u)+\mathscr K(X).
\tag{13}
\]
Here is the quantitative calculation. If the two corner labels are \((1,1)\), varying \(h\) yields the two outer signs with multiplicities \(a,b\), and the triangle inequality gives a mean at least \(2\min(a,b)/(n-3)\). Averaging over \(\ell\) gives \(g_n(k)=2(m-1)/(n-2)\) for \(m<n/2\), and \(g_n(k)=2(m-2)/(n-3)\) for \(m=n/2\). The probability of a bichromatic ordered pair \(i,j\) at the first corner is \(2k(n-k)/(n(n-1))\), giving \(\lambda_n(k)\). For a pair of corner labels \((1,0)\), the averaged absolute change is at least \(g_n'(k)=2(m-1)/(n-2)\); the pair \((0,1)\) contributes the analogous amount after replacing \(v\) by \(v^{ij}\). Relative to the \((1,1)\) baseline, their combined excess is \(2g_n'(k)-g_n(k)=\eta_n(k)\). The case \((0,0)\) has zero change. This establishes (13).

Choose the \(q_n\) disjoint exchange positions \((2,3),(5,6),\ldots\), with one separating position and a neighbor on both sides. Their effects on \(T\) add independently, since the affected turn positions are disjoint. For each exchange choose the better of the two orders. By the swap involution \(\mathbb E\Delta=0\), and
\[
\mathbb E\min(0,\Delta)=-\tfrac12\mathbb E|\Delta|.
\]
Equations (11)--(13) show that some resulting geodesic has odd \(T\) at most the expression preceding the subtraction of \(1\) inside the floor in (7). Rotating its root deletes one changed comparison, making a full geodesic with at most \(2\lfloor(T_{\rm bound}-1)/2\rfloor\) switches. Finally \(I(X)=\mu(c)+2\), proving (7). If \(I(X)\ge6\), the smallest permissible cyclic turn count is at least five, yielding (8). \(\square\)

**Corollary (ten-dimensional port theorem).** Every port-containing cycle \(X\) of \(D_{10}\) meets some minimum port cocircuit \(Y\) in at most four elements:
\[
\boxed{I(X)\le4\qquad(n=10).}
\tag{14}
\]

*Proof.* Here \(q_{10}=3\), and evaluation of (4) for \(k=0,\ldots,5\) gives
\[
\Phi_{10}(k)=0,\ 2,\ 154/45,\ 259/60,\ 71/15,\ 305/63.
\]
The function is symmetric under \(k\mapsto10-k\), and its maximum \(305/63\) is below five. Since \(\mathscr K(X)\ge0\), (7) gives \(I(X)\le4\). \(\square\)

**Corollary (curvature obstruction in dimension eleven).** Suppose \(n=11\) and every star has \(b_X(v)=5\). Let \(\delta(X)\) be the proportion of projected coordinate squares with
\[
d_{ij}(v)+d_{ij}(v^{ij})=1\pmod2.
\tag{15}
\]
Then
\[
\boxed{\ I(X)\le 2+2\left\lfloor
\frac{58/11-(2/3)\delta(X)-1}{2}\right\rfloor.\ }
\tag{16}
\]
In particular, if \(\delta(X)>9/22\), some \(Y\in\mathcal Y_{11}\) satisfies \(|X\cap Y|\le4\).

*Proof.* Under \(b_X(v)=5\), \(\Phi_{11}=58/11\), \(\eta_{11}=8/9\), and a count over the two opposite corners of each curved square shows \(\mathscr K(X)=4\delta(X)/9\). As \(q_{11}=3\), substitute into (7). \(\square\)

The statistical inputs \(b_X(v)\) and \(\mathscr K(X)\) are computed from incidence with local star triangles and opposite corners of projected squares. Thus the bound is intrinsically a restriction on port-containing cycles of \(D_n\), without a separately chosen cube-edge coloring. In comparison, the cut decomposition of a port cycle into a circuit core and a graphic cut can change these integer statistics; the exchange bound applies directly to the original cycle and avoids any assumption that cut penalties vanish.

### Minimum port-cocircuit profiles and universal coordinate prescription

Let \(n\ge3\). Retain the pointed binary matroid \((D_n,p)\) with ground set \(E(H_n)\cup\{p\}\), where \(H_n=L(Q_n)/\langle\tau\rangle\), and write
\[
\mathcal Y_n=\{Y\in\mathcal C^*(D_n):p\in Y,\ |Y|=n+1\}.
\]
A minimum port cocircuit \(Y\) corresponds to the cyclic turn sequence \(C=Y\setminus\{p\}\) of a full antipodal cube geodesic, with all \(n\) directions occurring once. For a port-containing binary cycle \(X\) of \(D_n\), set \(d(t)=\mathbf1_{\{t\in X\}}\) for turns \(t\).

Choose an orientation of \(C\) and mark a seam following direction \(i_n\). Write \(i_1,\ldots,i_n\) for the successive directions, and \(t_r\) for the turn joining \(i_r\) to \(i_{r+1}\), cyclically. Define the compatible profiles of this marked cocircuit to be the solutions \(w\in\mathbb F_2^n\) of
\[
w_{i_r}+w_{i_{r+1}}=d(t_r)\quad(r<n),\qquad
w_{i_n}+w_{i_1}+1=d(t_n).
\tag{1}
\]
Since \(d(C)=1\), the system has two solutions, related by global complementation. Define \(\mathscr W(X)\) as the union of solutions from all \(Y\in\mathcal Y_n\), orientations and seams.

**Lemma (profile decoding).** The family \(\mathscr W(X)\) equals the family of direction-indexed full-geodesic edge-color vectors for either antipodally odd coloring reconstructed from \(X\). Moving the marked seam across its first direction \(i\) sends a profile \(w\) to \(w+e_i\). The deck involution sends \(w\) to \(w+\mathbf1\).

*Proof.* Lift the ordered turn cycle to cube edges \(e_1,\ldots,e_n,e_{n+1}=\tau e_1\). The first \(n-1\) equations in (1) assert that each incident-edge disagreement equals the turn label. At the closing turn the final edge is compared with the antipode of the initial edge, giving the additional one. The two solutions correspond to the antipodal choices of lifted root, and every geodesic has a marked turn cycle of this form. Rotating the initial direction to the end preserves the other edges and replaces the moved edge by its antipode, changing that profile coordinate by one. \(\square\)

Let \(B_k\) be the assertion that every arbitrary binary coloring of the undirected edges of \(Q_k\) has a spanning antipodal geodesic with at most one change. For \(n>k\) and a fixed set \(S\subseteq[n]\) of \(k\) directions, let \(P_{n,S}\) be
\[
\forall X\in Z(D_n),\ p\in X,\qquad
\{w|_S:w\in\mathscr W(X)\}=\mathbb F_2^S.
\tag{2}
\]

**Theorem (pointed-matroid multifacet bridge).** For every \(k\ge2\), \(n>k\), and \(S\subset[n]\) with \(|S|=k\),
\[
\boxed{B_k\Longleftrightarrow P_{n,S}.}
\tag{3}
\]

*Proof.* Suppose \(B_k\). Reconstruct from any \(X\) an antipodally odd cube coloring \(c\), and fix a desired vector \(t\in\mathbb F_2^S\). Write \(Q_n=Q_S\times Q_D\), with \(D=[n]\setminus S\ne\varnothing\), and fix an exterior vector \(z\). Define the edge coloring of the lower \(S\)-face by \(h_i(u)=c_i(u,z)+t_i\). By \(B_k\), choose an antipodal geodesic in this face with at most one change; reverse it if necessary so its color word is a zero block \(U\) followed by a one block \(V\). If it runs
\[
u_0\xrightarrow{U}u_a\xrightarrow{V}\bar u_0,
\]
begin a full \(Q_n\) geodesic at \((u_a,z)\), traverse \(U\) backwards to \((u_0,z)\), traverse all directions of \(D\), then traverse the reverse of the \(Q_S\)-antipodal image of \(V\) in the upper exterior face. The \(U\) edges have color \(t_i\); the \(V\) edges are global antipodes of the lower one-block edges and likewise have color \(t_i\). This full geodesic gives a profile in \(\mathscr W(X)\) restricting to \(t\).

Conversely suppose \(P_{n,S}\), and let \(h\) be any edge coloring of \(Q_S\). Choose exterior direction \(s\in D\) and a coordinate \(i_0\in S\). Define an antipodally odd coloring of \(Q_n\), using vertices \((u,z)\), by
\[
c_i(u,z)=
\begin{cases}h_i(u),&z_s=0,\\1+h_i(\bar u),&z_s=1,\end{cases}
\ (i\in S);\qquad c_j(u,z)=u_{i_0}\ (j\in D).
\tag{4}
\]
These formulas are invariant under flipping the coordinate of their traversed edge and are complemented by global antipodality. Obtain the associated port cycle \(X\). By \(P_{n,S}\), there is a full geodesic whose \(S\)-edges all have color zero. Reverse it so its unique \(s\)-step runs from \(z_s=0\) to \(z_s=1\). Let \(U,V\) be its \(S\)-direction subsequences before and after the \(s\)-step, ignoring all other exterior steps. The projected \(U\)-edges have \(h\)-color zero, while the \(Q_S\)-antipodal images of the projected \(V\)-edges have \(h\)-color one. Reversing \(U\) and following the reversal of the antipodal image of \(V\) gives a spanning \(Q_S\) geodesic with word \(0^{|U|}1^{|V|}\). Thus \(B_k\) holds. \(\square\)

**Corollary (seven-coordinate marginal universality).** Every port-containing binary cycle \(X\) of \(D_n\) satisfies
\[
\boxed{\{w|_S:w\in\mathscr W(X)\}=\mathbb F_2^S
\qquad\bigl(|S|\le\min(7,n)\bigr).}
\tag{5}
\]
For \(n\le8\), every vector of \(\mathbb F_2^n\) occurs as a profile.

*Proof.* The established geodesic Norin theorem through dimension eight, combined with the Leader–Long implication, gives \(B_k\) for every \(k\le7\). Apply (3). For \(n\le8\), independently toggle the cube-edge color of each coordinate direction according to a prescribed full profile; this preserves antipodal oddness. Apply the proved monochromatic geodesic theorem in that dimension, then undo the direction toggles. The remaining claims follow by projection. \(\square\)

The next theorem controls polynomial relations involving arbitrarily many directions. Its conclusion is independent of the bounded-coordinate marginal property (5).

**Theorem (quadratic independence).** For every port-containing cycle \(X\) and every multilinear polynomial
\[
q(w)=a_0+\sum_i b_iw_i+\sum_{i<j}a_{ij}w_iw_j
\quad\text{over }\mathbb F_2,
\tag{6}
\]
the identity \(q(w)=0\) for all \(w\in\mathscr W(X)\) forces every coefficient to vanish. Equivalently,
\[
\boxed{
\operatorname{span}_{\mathbb F_2}\{(1,(w_i)_i,(w_iw_j)_{i<j}):w\in\mathscr W(X)\}
=\mathbb F_2^{1+n+\binom n2}.}
\tag{7}
\]

*Proof.* Recover a cube-edge coloring \(c\) from \(X\), and suppose \(q\) vanishes. Extend \(a_{ij}=a_{ji}\) and put \(a_{ii}=0\). The root rotation in the profile lemma, applied to a geodesic whose first direction is \(i\), yields
\[
b_i+\sum_{j\ne i}a_{ij}w_j=0.
\tag{8}
\]
Fix either facet perpendicular to direction \(i\). Prepending an \(i\)-edge to any antipodal geodesic of that facet shows that the edge cochain \(\omega_j(x)=a_{ij}c_j(x)\), \(j\ne i\), has constant total sum \(b_i\) on all facet-spanning geodesics.

We use an elementary closed-integral lemma. If an undirected edge weighting of a cube has constant sum on all full antipodal geodesics, every square has weight sum zero, and antipodal edges within that cube have equal weights. Indeed, exchange two successive directions at the start of a geodesic to obtain square closure. Integrating a square-closed weighting gives a vertex potential \(\phi\). Its antipodal difference \(\phi(x)+\phi(\bar x)\) equals the constant geodesic integral. Taking derivatives along edges yields antipodal equality.

Complementing the root of the full geodesic in (8) complements every \(w_j\), so
\[
\sum_{j\ne i}a_{ij}=0.
\tag{9}
\]
Within an \(i\)-facet, its antipode is \(x\mapsto\bar x^i\). The closed-integral lemma and \(c_j(\bar x^i)=1+c_j(x^i)\) imply
\[
a_{ij}=1\ \Longrightarrow\ c_j(x)+c_j(x^i)=1.
\tag{10}
\]
Square closure of the same facet cochain gives, for distinct \(i,j,k\),
\[
a_{ij}\bigl(c_j(x)+c_j(x^k)\bigr)
=a_{ik}\bigl(c_k(x)+c_k(x^j)\bigr).
\tag{11}
\]

Form the graph on \([n]\) with edge \(ij\) when \(a_{ij}=1\). If \(ij,jk\) are edges, (10)--(11) force \(ik\) to be an edge. Its connected components are therefore cliques. Equation (9) implies every clique has odd order. Suppose some component \(B\) has an edge, choose \(j\in B\), and use (10) for \(k\in B\setminus\{j\}\) and (11) for \(k\notin B\). Together with undirectedness in direction \(j\), these coordinate derivatives give
\[
c_j(x)=\gamma_j+\sum_{k\in B\setminus\{j\}}x_k.
\tag{12}
\]
Since \(|B|\) is odd, the sum has an even number of coordinates and is invariant under global complementation, contradicting antipodal oddness of \(c_j\). Hence all \(a_{ij}=0\). Equation (8) forces every \(b_i=0\), and evaluation anywhere forces \(a_0=0\). This proves (7). \(\square\)

**Corollary (profile diversity).** Every port-containing cycle \(X\) satisfies
\[
\boxed{|\mathscr W(X)|\ge
\max\left\{2^{\min(n,7)},\
2\left\lceil\frac{1+n+\binom n2}{2}\right\rceil\right\}.}
\tag{13}
\]
For \(n\le8\) equality \(|\mathscr W(X)|=2^n\) holds.

*Proof.* The first bound follows from (5), and the second from the spanning vectors (7), noting that \(\mathscr W(X)\) is closed under complementation and therefore has even cardinality. The small-dimensional equality follows from the complete-profile conclusion of (5). \(\square\)

All profile information here is recovered from a binary port cycle paired with a *marked* minimum port cocircuit; the seam and antipodal choice retain the endpoint memory lost by taking an unmarked intersection size. The two theorems forbid, respectively, missing low-dimensional coordinate marginals and nonzero quadratic annihilators of the full marked-cocircuit family.

### Connected minimum port cocircuits and their intersection spectrum

Let \(n\ge3\). Write \(G_n=Q_n/\langle\tau\rangle\), \(H_n=L(G_n)\), and let \(D_n\) be the pointed binary matroid with distinguished element \(p\) whose cycles containing \(p\) are \(X_d=\operatorname{supp}(a+\delta f)\cup\{p\}\). Here \(a\) represents the nonzero covering monodromy on \(H_n\). Denote by
\[
\mathcal Y_n=\{Y\in\mathcal C^*(D_n):p\in Y,\ |Y|=n+1\}
\]
the minimum port-containing cocircuits. They are precisely \(Y_C=C\cup\{p\}\), with \(C\) the turn cycle of a full antipodal cube geodesic.

Two elements \(Y,Y'\in\mathcal Y_n\) are *adjacent* when they have representatives that are rooted full antipodal geodesics with the same initial cube vertex and direction orders differing by the interchange of two consecutive directions.

**Theorem 1 (connected bounded exchanges).** The adjacency graph on \(\mathcal Y_n\) is connected. For adjacent \(Y,Y'\),
\[
\boxed{|Y\triangle Y'|\le6,\qquad
p\notin Y\triangle Y',\qquad
Y\triangle Y'\in\ker\alpha\subseteq Z_1(H_n;\mathbb F_2).}
\tag{1}
\]
For every binary cycle \(X\) of \(D_n\) containing \(p\),
\[
\boxed{\bigl||X\cap Y|-|X\cap Y'|\bigr|\le2.}
\tag{2}
\]

*Proof.* Let a rooted full geodesic have direction order \((i_1,\ldots,i_n)\). Exchanging consecutive \(i_j,i_{j+1}\) replaces the two-edge cube-square route between the same endpoints. Its lifted cyclic sequence of turns changes only at the comparisons immediately before, between, and immediately after the two exchanged edges. Thus each of the two projected turn cycles has at most three turn edges absent from the other; the distinguished element \(p\) belongs to both. This proves the support bound in (1).

Both turn cycles have monodromy one. Their symmetric difference is an Eulerian binary edge chain with monodromy zero, proving the remaining assertions of (1).

To prove connectedness, work first with rooted pairs \((x,\pi)\), where \(x\in Q_n\) and \(\pi\in S_n\). Adjacent transpositions connect every pair of direction orders at fixed root. In addition, the operation
\[
(x,(i_1,i_2,\ldots,i_n))
\longmapsto
(x^{i_1},(i_2,\ldots,i_n,i_1))
\tag{3}
\]
preserves the projected cyclic turn cycle: it cyclically moves the root across the first edge and replaces that edge by its antipodal mate. To change a prescribed root \(x\) to \(x^j\), move \(j\) to the first position by adjacent transpositions, apply (3), and then reorder by adjacent transpositions. Single-coordinate root changes connect the entire cube, so any two rooted pairs are connected by such operations. After quotienting out operations (3), only adjacent-transposition moves remain; the graph of projected cycles, equivalently \(\mathcal Y_n\), is connected.

For any port-containing binary cycle \(X\), cycle–cocircuit orthogonality gives \(|X\cap Y|\equiv|X\cap Y'|\equiv0\pmod2\). Moreover, at most three elements leave and at most three enter the cocircuit during an adjacent exchange. The integer intersection counts therefore differ by at most three; their difference is even and hence has magnitude at most two. This proves (2). \(\square\)

**Theorem 2 (gap-free even intersection spectrum).** For every \(n\ge3\) and every binary cycle \(X\) of \(D_n\) containing \(p\), put
\[
I_{\min}(X)=\min_{Y\in\mathcal Y_n}|X\cap Y|,
\qquad
I_{\max}(X)=\max_{Y\in\mathcal Y_n}|X\cap Y|.
\]
Then
\[
\boxed{\{\,|X\cap Y|:Y\in\mathcal Y_n\,\}
=\{I_{\min}(X),I_{\min}(X)+2,\ldots,I_{\max}(X)\}.}
\tag{4}
\]
Equivalently, for an arbitrary antipodally odd coloring, the cyclic turn counts of full antipodal geodesics attain every odd integer between their minimum and maximum; their optimally rotated switch counts attain every even integer between the corresponding endpoints.

*Proof.* Choose cocircuits realizing the minimum and maximum, and join them by an adjacency path given by Theorem 1. All intersection numbers along this path are even and consecutive values differ by at most two. Every intermediate even integer must therefore appear. Conversely every intersection number belongs to the even interval between its extrema. For the coloring interpretation, if \(d=\mathbf1_{X\setminus\{p\}}\), the turn count of a full geodesic with cocircuit \(Y\) is \(|X\cap Y|-1\), and cyclic root rotation deletes a changed comparison to yield \(|X\cap Y|-2\) switches. \(\square\)

**Corollary 3 (interpolation from separate witnesses).** Suppose a port-containing cycle \(X\) has minimum cocircuits \(Y_-\) and \(Y_+\) satisfying
\[
|X\cap Y_-|\le2r,\qquad |X\cap Y_+|\ge2s
\]
for integers \(1\le r\le s\). Then every even integer between \(2r\) and \(2s\) occurs as \(|X\cap Y|\) for some \(Y\in\mathcal Y_n\). In particular, any lower bound on a *maximum* intersection furnished by local star statistics can be combined with a bound on the *minimum* to furnish witnesses at each intermediate switch count.

*Proof.* Apply (4); the two hypotheses put the interval \([2r,2s]\) inside the achieved spectrum. \(\square\)

Theorem 1 makes the minimum-port-cocircuit family a connected exchange system with local differences in the even-monodromy cycle space generated by star triangles and cube-square cycles. Theorem 2 is an unrestricted integer-valued consequence of this geometry; it does not require \(X\) to be a circuit and imposes no balance or affine-coloring hypothesis.

### Extremal port intersections and exterior-square signatures

Fix \(n\ge4\). Let \(D_n\) be the pointed binary matroid with port \(p\), and let \(X\in Z(D_n;\mathbb F_2)\) contain \(p\). Write \(d(t)=\mathbf1_{\{t\in X\}}\) for turns \(t\) of the folded cube line graph \(H_n\). Its shortest port-cocircuit intersection parameter is
\[
I(X)=\min\{|X\cap Y|:Y\in\mathcal C^*(D_n),\ p\in Y,\ |Y|=n+1\}.
\tag{1}
\]
The minimum switch count in full antipodal geodesics of the recovered cube-edge coloring equals \(I(X)-2\). We formulate the finite-face completion constraints of Article X entirely through turn chains and the port-cocircuit intersection parameter.

Let \(F\) be a coordinate face of codimension \(t\), with free-direction set \(D\), exterior-direction set \(T=[n]\setminus D\), and \(1\le|D|,|T|\). For a geodesic \(P=(e_1,\ldots,e_{|D|})\) spanning \(F\), let
\[
A(P)=\{\{[e_j],[e_{j+1}]\}:1\le j<|D|\}\subseteq E(H_n),\qquad
r_X(P)=|A(P)\cap X|.
\tag{2}
\]
Here the projected consecutive edge pairs are turns, and \(r_X(P)\) is their integer support weight. If \(P,Q\) terminate at the same cube vertex \(x\), let \(t_x(P,Q)\in E(H_n)\) be the turn joining their last edges.

**Theorem 1 (port intersection completion and terminal separation).** Let \(P\) span a codimension-\(t\) face, and put \(r=r_X(P)\). Then
\[
\boxed{I(X)\le2+2\left\lfloor\frac{r+t}{2}\right\rfloor.}
\tag{3}
\]
If \(P,Q\) span the same face, end at the same vertex, have \(r_X(P),r_X(Q)\le r\), and \(t_x(P,Q)\in X\), then
\[
\boxed{I(X)\le2+2\left\lfloor\frac{r+t-1}{2}\right\rfloor.}
\tag{4}
\]

*Proof.* The cochain \(d\) reconstructs an antipodally odd edge coloring \(c\), unique up to complementation. Its disagreements between consecutive edges are the labels \(d\), so \(r_X(P)\) is the number of switches along \(P\). Append the \(t\) exterior directions in any order; the resulting path is an antipodal geodesic of \(Q_n\), with at most \(r+t\) switches. The global minimum switch count is even, because cyclic root rotation removes one switch whenever that path has an odd number of switches. It is thus at most \(2\lfloor(r+t)/2\rfloor\). The identity \(I(X)=\mu(c)+2\) gives (3).

For (4), membership \(t_x(P,Q)\in X\) says that the terminal edges of \(P,Q\) have opposite colors. Fix one exterior geodesic \(W\) from \(x\). Its first edge matches the terminal color of one of \(P,Q\); append \(W\) to that path. The seam causes no switch, and the other exterior comparisons contribute at most \(t-1\) switches. Apply the even-minimum reduction and the intersection identity again. \(\square\)

For directions \(i\ne j\) incident at a cube vertex \(y\), write \(d_{ij}([y])\) for the label of their turn in the vertex-star clique of \(H_n=L(G_n)\). All such labels are invariant under replacing \(y\) by its antipode. For \(S\subseteq T\) put \(x^S=x\oplus\sum_{i\in S}e_i\).

**Theorem 2 (forced star-cut pattern on an exterior cube).** Suppose \(P\) spans \(F\), ends at \(x\in F\), and has \(r=r_X(P)\) internal labeled turns. If
\[
\boxed{I(X)\ge r+t+2,}
\tag{5}
\]
then \(r+t\) is even, every completion of \(P\) by an ordering of \(T\) has \(r+t\) switches, and for every \(S\subseteq T\) and distinct \(i,j\in T\),
\[
\boxed{d_{ij}([x^S])=\mathbf1_{\{i\in S\}}+\mathbf1_{\{j\in S\}}\pmod2.}
\tag{6}
\]
In particular, every coordinate square entirely contained in the exterior \(t\)-cube at \(x\) has zero coloring curvature:
\[
\boxed{d_{ij}([x^S])=d_{ij}([x^{S\triangle\{i,j\}}])\qquad
(i,j\in T,\ S\subseteq T).}
\tag{7}
\]

*Proof.* A completion of \(P\) uses each exterior direction once. It has at most \(r+t\) switches, since only \(t\) additional comparisons are introduced. Condition (5), together with \(I(X)-2=\mu(c)\), forces every such completion to have at least \(r+t\) switches. Thus every newly introduced comparison must be a switch. As the minimum of full switch counts is even, \(r+t\) must be even.

Let \(q\in\mathbb F_2\) be the color of the final edge of \(P\). All exterior paths beginning at \(x\) therefore have successive edge colors
\[
1+q,\quad q,\quad1+q,\quad q,\quad\ldots
\tag{8}
\]
in their traversal order. Every exterior cube edge \(\{x^S,x^{S\cup\{i\}}\}\), with \(i\notin S\), occurs as the \((|S|+1)\)-st edge of some such path. Its color is
\[
1+q+|S|\pmod2.
\tag{9}
\]
At a vertex \(x^S\), the exterior direction-\(i\) edge has color \(1+q+|S|\) if \(i\notin S\), and \(q+|S|\) if \(i\in S\). Taking the difference of two such incident edge colors gives (6), independently of the choice of \(q\). Replacing \(S\) by \(S\triangle\{i,j\}\) flips both membership indicators, leaving their sum unchanged; this proves (7). \(\square\)

**Corollary 3 (flat exterior-square exclusions for hypothetical high intersection).** Suppose \(I(X)\ge6\).

(a) Every codimension-two face has no spanning geodesic \(P\) with \(r_X(P)\le1\). If such a face has a spanning geodesic with \(r_X(P)=2\), terminating at \(x\) with exterior directions \(a,b\), then
\[
d_{ab}([x])=d_{ab}([x^{ab}])=0,\qquad
d_{ab}([x^a])=d_{ab}([x^b])=1.
\tag{10}
\]
Consequently its exterior square has zero curvature. No two such low-cost terminal geodesics can have opposite terminal colors, equivalently their terminal-edge turn cannot lie in \(X\).

(b) Every codimension-three face has no monochromatic spanning geodesic. If it has a spanning geodesic with \(r_X(P)=1\) terminating at \(x\), then every exterior vertex star and every exterior square obeys (6)--(7), and no two one-turn terminal geodesics can have their terminal-edge turn in \(X\).

*Proof.* For codimension two, (3) with \(r\le1\) would give \(I(X)\le4\). With \(r=t=2\), Theorem 2 applies because \(I(X)\ge6=r+t+2\), yielding (10). For two such terminal paths, (4) gives \(I(X)\le4\) whenever their final-edge turn lies in \(X\), a contradiction. For codimension three, (3) with \(r=0\) gives \(I(X)\le4\); with \(r=1,t=3\), Theorem 2 gives (6)--(7). The same use of (4) excludes opposite terminal phases. \(\square\)

**Corollary 4 (curvature-positive squares cannot support two-turn terminals).** If \(I(X)\ge6\), fix distinct directions \(a,b\) and a coordinate square \(S\) parallel to them with
\[
d_{ab}([x])\ne d_{ab}([x^{ab}])
\tag{11}
\]
at opposite corners. No geodesic spanning the codimension-two face perpendicular to \(a,b\), terminating at the corresponding corner \(x\), can have only two turns in \(X\).

*Proof.* Such a path would satisfy Corollary 3(a), which forces equality of the two labels in (11). \(\square\)

Equations (6)--(7) transfer the face-completion rigidity of Article X into a phase-free condition on the cycle \(X\): a locally extremal partial turn chain forces the restriction of \(X\) to each exterior star to be the cut separating directions already flipped from directions not yet flipped. Theorem 1 supplies a complementary two-chain certificate for an intersection at most four. These assertions hold for arbitrary port-containing binary cycles, including those which decompose into several dual circuits.

### Odd-dimensional port cycles: square-derivative rigidity and terminal holes

Let \(n\ge5\) be odd, let \((D_n,p)\) be the pointed binary matroid of the antipodal turn quotient \(H_n=L(Q_n)/\langle\tau\rangle\), and let \(X\in Z(D_n)\) contain \(p\). Put \(d(t)=\mathbf1_{\{t\in X\}}\) and
\[
I(X)=\min\{|X\cap Y|:Y\in\mathcal C^*(D_n),\ p\in Y,\ |Y|=n+1\}.
\tag{1}
\]
Every \(X\) in this statement is an admissible turn cochain, so the star triangle sums and the square-turn sums of \(d\) vanish.

For each unordered direction pair \(i,j\), the coordinate squares of \(Q_n\) form \(2^{n-3}\) antipodal pairs. Let \(s\) be such a pair, and choose a representative square with corners \(u,u^i,u^j,u^{ij}\). Define two local derivatives in terms of the port cycle alone:
\[
\partial_jd_i(s)=d_{ij}([u])+d_{ij}([u^j]),\qquad
\partial_id_j(s)=d_{ij}([u])+d_{ij}([u^i])
\quad\text{in }\mathbb F_2.
\tag{2}
\]
Here \([u]\) is the vertex of \(G_n=Q_n/\tau\), and \(d_{ij}([u])\) is the turn between the direction-\(i\) and direction-\(j\) edges incident with \([u]\). Square identities and antipodal invariance show that (2) is independent of the chosen square corner and antipodal representative. Define
\[
\begin{aligned}
\mathfrak B_{ij}(X)&=\{s:(\partial_jd_i(s),\partial_id_j(s))\ne(1,1)\},\\
\mathfrak D(X)&=\sum_{i<j}|\mathfrak B_{ij}(X)|,\\
\mathfrak Z_i(X)&=\sum_{j\ne i}\#\{s\text{ of type }(i,j):\partial_jd_i(s)=0\},\\
\mathfrak K(X)&=\sum_{i<j}\#\{s:\partial_jd_i(s)+\partial_id_j(s)=1\}.
\end{aligned}
\tag{3}
\]
All quantities are intrinsic incidence statistics of \(X\) and the direction-labeled folded cube.

**Theorem (square-derivative deficit and sharp rigidity).** Every port-containing cycle \(X\) satisfies
\[
\boxed{\mathfrak Z_i(X)\ge2^{n-3},\qquad
\mathfrak K(X)\ge2^{n-3},\qquad
\mathfrak D(X)\ge(n+1)2^{n-4}.}
\tag{4}
\]
Equality in the last inequality implies
\[
\boxed{I(X)=2.}
\tag{5}
\]
In particular,
\[
\boxed{\quad I(X)\ge6\ \Longrightarrow\
\mathfrak D(X)\ge(n+1)2^{n-4}+1.\quad}
\tag{6}
\]
The lower bound in (4) is attained for every odd \(n\).

*Proof.* Reconstruct an antipodally odd undirected-edge coloring \(c_i(u)\) from \(X\). If \(\kappa_{ij}(u)\) denotes the color sum around an \((i,j)\)-square, the turn equations give
\[
\partial_jd_i(s)=c_i(u)+c_i(u^j),\qquad
\partial_id_j(s)=c_j(u)+c_j(u^i),
\tag{7}
\]
and \(\kappa_{ij}(s)=\partial_jd_i(s)+\partial_id_j(s)\). These expressions are antipodally invariant.

Fix \(i\), and regard \(c_i\) as a Boolean function of the even number \(n-1\) of coordinates other than \(i\). Put
\[
f_i(y)=(-1)^{c_i(y)+\sum_{j\ne i}y_j}.
\tag{8}
\]
Antipodal oddness of \(c_i\) makes \(f_i(\bar y)=-f_i(y)\), so its constant Walsh coefficient vanishes. The derivative of \(f_i\) along coordinate \(j\) is nonzero precisely when \(\partial_jd_i(s)=0\). Counting all directional edges, using the Walsh expansion and Parseval, yields
\[
2\mathfrak Z_i
=2^{n-2}\sum_{S\ne\varnothing}|S|\widehat f_i(S)^2
\ge2^{n-2}\sum_{S\ne\varnothing}\widehat f_i(S)^2
=2^{n-2},
\tag{9}
\]
proving the first inequality.

Next reverse a complete coordinate order by adjacent transpositions, exchanging each unordered direction pair once. The parity of the sum of edge colors on the reversed geodesic differs from the original by \(n\bmod2=1\), since its word is the complemented reversal. Each exchanged pair contributes the curvature \(\kappa_{ij}(s)\) of the crossed square. Hence every such reversal has an odd number of curved squares. Average over all cube roots: a fixed pair of directions crosses each of its \(2^{n-2}\) cube squares equally often. Thus at least \(2^{n-2}\) cube squares have curvature one in total, or at least \(2^{n-3}\) antipodal pairs of them. This proves the middle inequality of (4).

On each square with derivative pair \((1,1)\), the contributions to \((\mathfrak D,\sum_i\mathfrak Z_i,\mathfrak K)\) are \((0,0,0)\). A square with \((0,0)\) contributes \((1,2,0)\), and one with unequal derivatives contributes \((1,1,1)\). Consequently
\[
2\mathfrak D=\sum_i\mathfrak Z_i+\mathfrak K
\ge(n+1)2^{n-3},
\tag{10}
\]
giving the final inequality in (4).

Suppose equality holds. Equality in (9) for every \(i\) implies \(f_i\) has Walsh degree one. A degree-one function taking values in \(\{\pm1\}\) is a signed coordinate character: squaring its Walsh expansion and comparing cross coefficients shows at most one linear coefficient is nonzero. Hence for each \(i\) there is \(p(i)\ne i\) and \(a_i\in\mathbb F_2\) such that
\[
c_i(u)=a_i+\sum_{j\notin\{i,p(i)\}}u_j.
\tag{11}
\]
Its derivative satisfies
\[
\partial_jd_i(s)=1+[p(i)=j],\qquad
\kappa_{ij}(s)=[p(i)=j]+[p(j)=i].
\tag{12}
\]
The middle inequality of (4) is also an equality, so there is precisely one unordered coordinate pair with nonzero curvature. Since \(p\) has one outgoing arrow from each of the odd number \(n\) of directions, it follows that \(n-1\) directions form reciprocal pairs \(\{u_r,v_r\}\) and one remaining direction \(w\) points to a member of one of these pairs.

We give a monochromatic full geodesic for every coloring (11) of that form. Let \(t_i\) be the position of coordinate \(i\) in the chosen permutation. Choose the permutation with
\[
t_{u_r}+t_{v_r}=1+a_{u_r}+a_{v_r}\pmod2
\tag{13}
\]
for every reciprocal pair. Such a permutation is obtained successively from the remaining odd number of positions: a pair requiring equal parity takes two positions of the majority parity, and one requiring different parity takes one of each; the remaining parity classes continue to differ by one. The final position belongs to \(w\). Write \(S_i\) for the preceding directions and
\[
\eta_i=a_i+(t_i-1)+[p(i)\in S_i].
\tag{14}
\]
Equation (13) gives \(\eta_{u_r}=\eta_{v_r}=:\eta_r\). Choose arbitrary bits \(T,q\), prescribe
\[
u_{u_r}+u_{v_r}=T+q+\eta_r,\quad
u_w=T+\sum_r(u_{u_r}+u_{v_r}),\quad
u_{p(w)}=T+q+\eta_w+u_w.
\tag{15}
\]
These prescriptions are compatible and determine a starting vertex up to free choices. Its total coordinate sum is \(T\). On the edge traversed in direction \(i\), (11), (14), and (15) give
\[
c_i(u^{S_i})=T+u_i+u_{p(i)}+\eta_i=q
\tag{16}
\]
for every direction. This gives a monochromatic antipodal geodesic. By the port-cycle switch identity, \(I(X)=2\), proving (5). A coloring achieving equality is supplied by any partner map of the specified form, proving sharpness. Since \(\mathfrak D\) is integral, (5) implies the strict improvement (6). \(\square\)

The deficit can also be localized to terminal sets of coordinate faces, yielding constraints on port cycles whose every minimum cocircuit has large intersection.

For \(i<j\), identify the four codimension-two faces perpendicular to \(i,j\) with \(Q_{[n]\setminus\{i,j\}}\). Let \(R_{ij}(X)\) be the union of projections of terminals of all face-spanning geodesics having at most two color changes, in all four faces. Here a face-path's changes are determined from \(d\) on its successive turns, so the set is independent of which complementary coloring is reconstructed. Let \(H_{ij}(X)=Q_{n-2}\setminus R_{ij}(X)\). Global antipodality pairs the four faces and preserves their change counts; hence both \(H_{ij}(X)\) and the square-defect set \(\mathfrak B_{ij}(X)\) are invariant under complementation of their projected coordinates. Let \(\mathfrak H_{ij}(X)\) be the quotient of \(H_{ij}(X)\) by this antipodal pairing.

**Theorem (terminal-hole obstruction for large port intersections).** If \(I(X)\ge6\), then
\[
\boxed{\mathfrak B_{ij}(X)\subseteq\mathfrak H_{ij}(X),}
\tag{17}
\]
and
\[
\boxed{\quad
\sum_{i<j}|\mathfrak H_{ij}(X)|
\ge(n+1)2^{n-4}+1,\qquad
\sum_{j\ne i}|\mathfrak H_{ij}(X)|\ge2^{n-3}
\quad(i\in[n]).}
\tag{18}
\]
Therefore
\[
\sum_{i<j}|\mathfrak H_{ij}(X)|\le(n+1)2^{n-4}
\quad\Longrightarrow\quad I(X)\le4.
\tag{19}
\]

*Proof.* The condition \(I(X)\ge6\) means that every full antipodal geodesic has at least four changes. Consider a face-spanning geodesic \(P\) in one of the four \((n-2)\)-faces with at most two changes, ending at corner \(u\), whose projected terminal is \(z\). If \(P\) had at most one change, appending the two exterior directions would produce a full path with at most three changes, a contradiction. Thus \(P\) has two changes. Appending the two exterior directions in either order produces a full path with at most four changes, and therefore both new comparisons must be changes. If \(q\) is the last color of \(P\), both exterior edges incident with \(u\) have color \(1+q\), and the opposite two edges of their square have color \(q\). By (7), its two cross-derivatives are both one. Thus every projected terminal \(z\in R_{ij}(X)\) lies outside the square-defect set, yielding (17). Summing (17), then applying (4) and (6), proves (18). The final implication is the contrapositive of the first bound in (18). \(\square\)

All statistics in (3) and (17) use only the direction-labeled quotient, the incidence vector of \(X\), and marked partial geodesics. They impose local constraints on a port cycle whose minimum cocircuit intersections are all at least six.

Let \(n\ge3\), let \(\tau\) be cube antipodality, and put \(G=Q_n/\langle\tau\rangle\), \(H=L(G)\). Fix an antipodally odd coloring \(c:E(Q_n)\to\mathbb F_2\). Its turn cochain \(d:E(H)\to\mathbb F_2\) assigns the difference of the colors of two incident cube edges. Put \(H_0=(V(H),\{t:d(t)=0\})\). Every turn of \(H\) has a unique center \(v\in V(G)\), and the turns centered at \(v\) form a clique \(K_v\cong K_n\).

Choose a lift \(x\) of \(v\), and partition the \(n\) cube edges incident with \(x\) into their color classes \(A_v^0,A_v^1\). Changing the lift interchanges these classes. Thus \(\lambda_v=|A_v^0||A_v^1|\) is well-defined. Write \(v\) *mixed* if \(\lambda_v>0\). All vertices of the turn clique corresponding to \(A_v^i\) belong to one connected component \(R_v^i\) of \(H_0\), because every turn inside a color class is a zero turn. The two components \(R_v^0,R_v^1\) may coincide.

Define a weighted multigraph \(\Gamma_c\) whose vertices are the connected components of \(H_0\). Each mixed \(v\) contributes one edge joining \(R_v^0\) and \(R_v^1\), of weight \(\lambda_v\), with loops allowed. Thus the \(\lambda_v\) different-color turns at one cube-vertex star form a single weighted edge bundle in \(\Gamma_c\).

**Theorem 1 (star-bundle rigidity).** Let \(b=\delta g\) be a binary cut cochain of \(H\) satisfying \(\operatorname{supp}(b)\subseteq\operatorname{supp}(d)\). Then, for every \(v\in V(G)\),
\[
\boxed{b|_{E(K_v)}=0\quad\text{or}\quad b|_{E(K_v)}=d|_{E(K_v)}.}\tag{1}
\]
Moreover, \(g\) descends to a binary vertex potential \(\bar g\) on \(\Gamma_c\). At a mixed \(v\), the second alternative of (1) holds if and only if \(\bar g(R_v^0)\ne\bar g(R_v^1)\). Conversely, any binary vertex potential on \(\Gamma_c\) determines a cut cochain of \(H\) supported on \(d\). Consequently,
\[
\boxed{|\operatorname{supp}(b)|=
\sum_{\substack{v\ \mathrm{mixed}\\\bar g(R_v^0)\ne\bar g(R_v^1)}}\lambda_v.}\tag{2}
\]
The support-minimizing cochains \(d'=d+b\) with \(\operatorname{supp}(d')\subseteq\operatorname{supp}(d)\) are therefore represented by maximum-weight cuts of \(\Gamma_c\).

*Proof.* The support inclusion forces \(b=0\) on \(H_0\); hence \(g\) is constant on every connected component of \(H_0\) and descends to \(\bar g\). At \(K_v\), it is constant on each of the two local color classes. If those constants agree then \(b\) vanishes on \(K_v\); if they differ then it is one precisely on turns between different color classes, which are the turns where \(d=1\). This proves (1). The converse follows by pulling any \(\bar g\) back to \(V(H)\); all zero turns then have equal endpoint values, so the pulled-back cut is supported on \(d\). The cliques \(K_v\) partition \(E(H)\), and a mixed clique has \(\lambda_v\) nonzero turns. This proves (2) and the weighted-cut statement. \(\square\)

**Theorem 2 (a cut-resistant star bundle).** Every antipodally odd coloring \(c\) admits a mixed vertex \(v\in V(G)\) such that \(R_v^0=R_v^1\). In particular,
\[
\boxed{\lambda_v\ge n-1,\qquad
d'|_{E(K_v)}=d|_{E(K_v)}}
\tag{3}
\]
for every admissible support-decreasing switching \(d'=d+b\). Equivalently, \(\Gamma_c\) has a positive-weight loop, whose whole turn bundle survives every such switching.

*Proof.* By the Wu–Yang theorem on antipodal edge colorings, there is a monochromatic cube path \(P\) from some vertex \(x\) to \(\tau x\). Denote its successive edges by \(e_1,\ldots,e_m\). Their antipodal-pair vertices \([e_1],\ldots,[e_m]\) form a zero-turn path in \(H_0\), so \([e_1]\) and \([e_m]\) lie in the same component. At \(x\), the incident cube edges \(e_1\) and \(\tau e_m\) have opposite colors, while their vertices downstairs are \([e_1]\) and \([e_m]\). Hence the two color classes of the star centered at \([x]\) lie in the same \(H_0\)-component, making its bundle a loop. Since the star has two nonempty classes of cardinalities \(k,n-k\), its weight is \(k(n-k)\ge n-1\). Theorem 1 shows that cuts supported on \(d\) vanish on loops, so this bundle persists in every \(d'\). \(\square\)

**Proposition 3 (a sparse-cut zero-penalty criterion).** Every binary cut \(b\) of \(H\) satisfying
\[
\boxed{|\operatorname{supp}(b)|<(n-1)2^{n-1}}
\tag{4}
\]
is disjoint from some length-\(n\) monodromy-one simple cycle \(C\), corresponding to a full antipodal geodesic. Thus this conclusion applies to every supported cut of Theorem 1 whose crossing weight (2) satisfies (4).

*Proof.* The cube automorphism group acts transitively on turns and preserves the family \(\mathcal R_n\) of length-\(n\) monodromy-one cycles. Every such cycle has \(n\) turns, and \(|E(H)|=\binom n2 2^{n-1}\). Therefore for uniformly sampled \(C\in\mathcal R_n\),
\[
\mathbb E_C|\operatorname{supp}(b)\cap C|
=\frac{n|\operatorname{supp}(b)|}{|E(H)|}
=\frac{2|\operatorname{supp}(b)|}{(n-1)2^{n-1}}<2.
\]
Every graph cut meets every graph cycle in an even number of edges. Hence a nonnegative even-valued random variable with mean below two must attain zero. \(\square\)

The weighted quotient makes support deletion a cut problem on indivisible local switch bundles. Theorem 2 supplies a permanently retained bundle; Proposition 3 gives a checkable sufficient condition for a shortest port cocircuit to incur zero cut penalty.

**Sharpness of (4).** The constant in Proposition 3 cannot be increased for general graph cuts. Fix a coordinate \(s\), and define a vertex potential \(g\) on \(H\) by \(g([e])=1\) when the direction of the cube edge \(e\) is \(s\), and \(g([e])=0\) otherwise. For \(b=\delta g\), every star \(K_v\) contributes \(n-1\) turns to \(\operatorname{supp}(b)\). Since \(G\) has \(2^{n-1}\) vertices,
\[
|\operatorname{supp}(b)|=(n-1)2^{n-1}.
\]
Every length-\(n\) monodromy-one cycle visits every coordinate direction once, so precisely two of its turns cross between the direction-\(s\) vertex and the remaining directions. Thus
\[
|\operatorname{supp}(b)\cap C|=2
\]
for every \(C\in\mathcal R_n\).

### Direction-deleted cocircuit reassembly and rooted phase duality

Let \(m\ge2\), and let \(D_{m+1}\) be the pointed matroid built from the antipodal line-graph cover of \(Q_{m+1}\). Write
\[
I(X)=\min\{|X\cap Y|:Y\in\mathcal C^*(D_{m+1}),\ p\in Y,\ |Y|=m+2\}
\tag{1}
\]
for every port-containing binary cycle \(X\). Every such \(X\) is the turn support of an antipodally odd coloring of the edges of \(Q_{m+1}\), together with the port; the full-geodesic switch minimum is \(I(X)-2\).

Fix one coordinate direction \(s\), identify its zero facet with \(Q_m\), and write \(x^*\) for the antipode within that facet. An arbitrary undirected-edge coloring \(d_i(x)\), \(i\in[m]\), and a function \(h:Q_m\to\mathbb F_2\) satisfying
\[
h(x^*)=1+h(x)
\tag{2}
\]
determine the following antipodally odd coloring of \(Q_{m+1}\):
\[
c_i(x,0)=d_i(x),\qquad
c_i(x,1)=1+d_i(x^*),\quad (i\in[m]),
\qquad c_s(x,z)=h(x).
\tag{3}
\]
Conversely, every antipodally odd cube-edge coloring has this description relative to the selected coordinate. Denote its port-containing cycle by \(X(d,h)\). Geometrically, the direction-deleted turn subgraph is \(L(Q_m)\), a connected subgraph on which the covering monodromy vanishes. The function \(h\) specifies the remaining joining-edge phases.

For each full \(d\)-geodesic \(R\) within \(Q_m\), write \(r(R)\) for its number of color changes and \(s(R)\) for the color of its initial edge.

**Theorem 1 (reassembly formula for minimum port intersections).** For every \(d,h\) satisfying (2),
\[
\boxed{\begin{aligned}
I(X(d,h))=2+\min_{x\in Q_m}\ \min_{R:x\to x^*}\ \Theta(R,h(x)),\\
\Theta(R,p)=
\begin{cases}
r(R),&r(R)\text{ even},\\
r(R)-1+2[s(R)\ne p],&r(R)\text{ odd}.
\end{cases}
\end{aligned}}
\tag{4}
\]
Here every \(R\) spans all \(m\) directions, and both minimizations run over finite sets. The formula is independent of the other joining-edge colors \(h(y)\).

*Proof.* Any full geodesic of \(Q_{m+1}\) traverses the joining direction \(s\) once. Reverse it if needed so this step goes from facet zero to facet one, crossing at the lower-facet vertex \(x\). Reverse the lower portion of the geodesic and reverse the within-facet antipodal image of its upper portion. These two paths concatenate into a full \(d\)-geodesic \(R:x\to x^*\), uniquely split as \(R=UV\). Conversely, any such \(R\), split at any of its vertices, gives a full geodesic of (3), with color word
\[
\operatorname{rev}(w(U)),\quad p,\quad
\overline{\operatorname{rev}(w(V))},
\qquad p=h(x).
\tag{5}
\]
All directions appear once. Thus optimizing over full geodesics is equivalent to optimizing the two seams in (5) over \(R\), its split, and its root \(x\).

Put \(r=r(R)\), \(s=s(R)\), and \(q\) equal to the final color of \(R\). We have \(q=s+(r\bmod2)\) over \(\mathbb F_2\). If the split is interior, write \(j=1\) when it cuts a color change of \(R\), and \(j=0\) otherwise. The number of changes in (5) is
\[
r-j+[s\ne p]+[1+q\ne p].
\tag{6}
\]
If \(r\) is positive and even, the two seam indicators sum to one. Splitting at one of the \(r\) changes attains cost \(r\). If \(r=0\), an endpoint split places all \(m\) facet edges on whichever side gives their constant color agreement with \(p\), attaining cost zero. If \(r\) is odd, the seam indicators are equal and sum to \(2[s\ne p]\); splitting at a change attains \(r-1+2[s\ne p]\). An endpoint split has cost \(r+[s\ne p]\), never smaller. These are the values of \(\Theta\). Finally, the intersection identity \(I=\mu+2\) proves (4). \(\square\)

For an arbitrary coloring \(d\), define its allowable joining phases at \(x\) by
\[
\mathscr H_2(d,x)=
\{p\in\mathbb F_2:\min_{R:x\to x^*}\Theta(R,p)\le2\}.
\tag{7}
\]

**Lemma 2 (phase duality and an antipodal selection principle).** For every arbitrary \(d\),
\[
\boxed{\mathscr H_2(d,x^*)=1+\mathscr H_2(d,x).}
\tag{8}
\]
Furthermore, the following are equivalent:

(i) Every joining phase function \(h\) satisfying (2) gives \(I(X(d,h))\le4\).

(ii) Some \(x\in Q_m\) has \(\mathscr H_2(d,x)=\mathbb F_2\).

*Proof.* Reverse a rooted full \(d\)-geodesic \(R:x\to x^*\). The reversal has the same switch count; its first color is \(s(R)\) for even \(r(R)\), and \(1+s(R)\) for odd \(r(R)\). In either case (4) shows that replacing the root by \(x^*\) and the joining phase \(p\) by \(1+p\) preserves \(\Theta\). This proves (8).

If (ii) holds, every \(h\) assigns at that \(x\) a phase admitted by (7), and (4) supplies a port-cocircuit intersection at most four. Conversely, if no \(x\) admits both phases, choose one representative of each antipodal pair \(\{x,x^*\}\), select \(h(x)\) outside \(\mathscr H_2(d,x)\), and set \(h(x^*)=1+h(x)\). Equation (8) guarantees that both choices lie outside their respective allowable sets. The resulting \(h\) is antipodally odd and (4) gives \(I(X(d,h))>4\), contradicting (i). \(\square\)

**Theorem 3 (rooted criterion for universal short port-cocircuit intersections).** The following assertions are equivalent for every \(m\ge2\):

(a) Every binary cycle \(X\) of \(D_{m+1}\) containing the port satisfies \(I(X)\le4\).

(b) For every arbitrary undirected-edge coloring \(d\) of \(Q_m\), some vertex \(x\in Q_m\) has one of these properties: there is a full \(d\)-geodesic rooted at \(x\) with at most two changes; or there are two full \(d\)-geodesics rooted at \(x\), each with three changes, whose initial edge colors differ.

*Proof.* Formula (4) gives \(\mathscr H_2(d,x)=\mathbb F_2\) whenever a rooted geodesic has zero or two changes. When a rooted geodesic has one change, its two choices of \(p\) give costs zero and two; both are also allowable. If all rooted geodesics have at least three changes, then only those with precisely three changes and matching initial and joining colors have \(\Theta\le2\). Consequently \(\mathscr H_2(d,x)=\mathbb F_2\) holds precisely under the alternatives in (b). Every admissible port cycle is \(X(d,h)\) for some lower-facet coloring and joining function. Apply Lemma 2 and quantify over \(d\). \(\square\)

**Corollary 4 (facet obstructions in a putative high-intersection cycle).** If \(X=X(d,h)\) satisfies \(I(X)\ge6\), then for every choice of the deleted direction and corresponding facet coloring \(d\):

1. No vertex of the facet starts a full \(d\)-geodesic with at most two changes.
2. Whenever a vertex \(x\) starts a full three-change \(d\)-geodesic, all such geodesics have the same initial color, necessarily \(1+h(x)\).
3. No vertex starts three-change \(d\)-geodesics with both initial colors.

*Proof.* If a path as in (1) existed, both joining phases at its root would produce an intersection at most four by (4). If a three-change path had initial color \(h(x)\), formula (4) would again produce an intersection four. Opposite initial phases among two such paths would include \(h(x)\), establishing (2)--(3). The deleted direction was arbitrary. \(\square\)

This characterization transfers the codimension-one reassembly theorem from Article X into the pointed matroid of Article XI. It couples a direction-deleted graphic restriction, an antipodally odd selection of joining phases, and minimum port-cocircuit intersections. The rooted criterion is unrestricted in the dimension, color dependence and choice of the deleted direction.

### Parallel-face port-cocircuit exchange at corresponding terminals

Let \(n\ge4\), \(H_n=L(Q_n)/\langle\tau\rangle\), and let \((D_n,p)\) be the pointed binary matroid of the antipodal turn covering. Fix a port-containing binary cycle \(X\) of \(D_n\), let \(d_X(t)=\mathbf1_{\{t\in X\}}\) for turns \(t\in E(H_n)\), and put
\[
I(X)=\min\{|X\cap Y|:Y\in\mathcal C^*(D_n),\ p\in Y,\ |Y|=n+1\}.
\tag{1}
\]
For a direction-distinct cube path \(P=(e_1,\ldots,e_m)\), define the integer turn weight
\[
r_X(P)=\sum_{j=1}^{m-1}d_X(\{[e_j],[e_{j+1}]\}).
\tag{2}
\]
It equals the number of edge-color changes in \(P\) for either cube coloring recovered from \(X\). The pointed matroid formula says that the minimum switch count over all full antipodal geodesics is \(I(X)-2\). In particular, \(I(X)\) is even.

**Theorem (parallel-face intersection bound).** Fix two directions \(a,b\), a codimension-two face \(F\) in which their coordinates are fixed, and the neighboring face \(F^a\). Suppose \(P\subset F\) and \(Q\subset F^a\) span their faces and terminate at corresponding vertices \(x,x^a\). Write \(r=r_X(P)\) and \(s=r_X(Q)\). Then
\[
\boxed{
I(X)\le2+
\min\left\{
\max\bigl(r,2\lceil s/2\rceil\bigr),\
\max\bigl(s,2\lceil r/2\rceil\bigr)
\right\}.}
\tag{3}
\]
Consequently, a monochromatic face-spanning path matched to a path of at most one change in the adjacent face forces \(I(X)=2\). Two matched face-spanning paths with at most two changes each force \(I(X)\le4\).

*Proof.* Recover an antipodally odd cube-edge coloring \(c\) from \(X\). Write \(\rho,\sigma\) for the final colors of \(P,Q\), respectively. Label the four edges of the exterior square at their terminals:
\[
A=c(xx^a),\quad B=c(xx^b),\quad
C=c(x^ax^{ab}),\quad D=c(x^bx^{ab}).
\tag{4}
\]
Completing either face path by the two possible exterior square routes gives four full antipodal geodesics with respective switch counts
\[
\begin{array}{ll}
r+[\rho\ne A]+[A\ne C],&
r+[\rho\ne B]+[B\ne D],\\
s+[\sigma\ne A]+[A\ne B],&
s+[\sigma\ne C]+[C\ne D].
\end{array}
\tag{5}
\]
For every rooted full geodesic with \(z\) changes, cyclic rotation of the root gives another full geodesic with at most \(2\lfloor z/2\rfloor\) changes. Indeed, when \(z\) is odd, the closing antipodal comparison has value zero, and cutting the cyclic turn word at a changed comparison removes one switch. Thus any bound for a completion in (5) yields the corresponding even bound on \(I(X)-2\).

First prove
\[
I(X)-2\le M:=\max\{r,2\lceil s/2\rceil\}.
\tag{6}
\]
If \(r\) is even and \(M\ge r+2\), either completion of \(P\) has at most \(r+2\le M\) changes. If \(r\) is odd and \(M\ge r+1\), either completion has at most \(r+2\) changes, which is odd; cyclic reduction gives at most \(r+1\le M\). It remains to consider \(M=r\).

If \(r\) is even and both completions of \(P\) failed to yield at most \(r\) after cyclic reduction, each would introduce two new switches. Their square-edge constraints are
\[
A=B=1+\rho,\qquad C=D=\rho.
\tag{7}
\]
One of the two completing routes for \(Q\) then has both edges of color \(\sigma\), so it gives a full geodesic with at most \(s\le2\lceil s/2\rceil\le r\) changes, a contradiction.

If \(r\) is odd, \(2\lceil s/2\rceil\le r-1\). When \(s\le r-2\), any completion of \(Q\) has at most \(s+2\le r\) changes; cyclic reduction gives at most \(r-1\). The remaining case is \(s=r-1\), with \(s\) even. If both completions of \(Q\) failed to yield at most \(r-1\), they would both introduce two switches, forcing
\[
A=C=1+\sigma,\qquad B=D=\sigma.
\tag{8}
\]
One of the two routes completing \(P\) then consists of edges of color \(\rho\), producing \(r\) switches and hence at most \(r-1\) after cyclic reduction, again a contradiction.

This proves (6). Interchanging \(F\) and \(F^a\) proves
\(I(X)-2\le\max\{s,2\lceil r/2\rceil\}\). Taking the smaller bound proves (3). Substituting \((r,s)=(0,0),(0,1)\), or \(r,s\le2\), proves the consequences. \(\square\)

The theorem uses two marked face paths with **corresponding terminal vertices**, an additional geometric condition on top of their individual turn weights. It adds an inter-face intersection certificate to the single-face completion and exterior-star rigidity theorems. Both paths, their turns, and the matching of their terminals can be read from the direction-labeled cube covering, while their switch counts are simply incidences with the port cycle \(X\).

### Equivariant square-derivative galleries for arbitrary port cycles

Let \(n\ge3\), let \(H_n=L(Q_n)/\langle\tau\rangle\), and let \((D_n,p)\) be the pointed binary matroid defined by the antipodal turn cover. Fix any binary cycle \(X\in Z(D_n)\) containing the port \(p\), and write \(d_X\) for its indicator on turns. At a cube vertex \(x\), write \(d^X_{ij}([x])\) for the label of the turn between the edges in directions \(i,j\). For \(i\ne j\), define the square derivative
\[
\partial_j^X(i;x)=d^X_{ij}([x])+d^X_{ij}([x^j])\in\mathbb F_2.
\tag{1}
\]
The star-triangle and square identities for a port cycle make (1) a function of its undirected \((i,j)\)-square, constant on antipodal square pairs. If \(c\) is either reconstructed antipodally odd cube-edge coloring, then
\[
\partial_j^X(i;x)=c_i(x)+c_i(x^j).
\tag{2}
\]
Thus all derivative conditions below are intrinsically determined by \(X\).

Let \(\mathcal T_n\) be the antipodally invariant Freudenthal triangulation of the boundary of the \(n\)-cube. Its maximal simplices are monotone vertex chains through an \((n-1)\)-dimensional coordinate facet, corresponding to geodesics traversing all directions but the fixed one. Write \(\tau\) for complementation of cube vertices.

Fix a family
\[
\mathcal A=((i_\alpha,S_\alpha))_{\alpha=1}^r,
\qquad i_\alpha\in[n],\quad
S_\alpha\subseteq[n]\setminus\{i_\alpha\},\quad
|S_\alpha|\equiv0\pmod2,
\tag{3}
\]
where directions may repeat. Call a maximal simplex of \(\mathcal T_n\) a witness for \(\mathcal A\) if its facet geodesic contains, for each \(\alpha\), a step in some direction \(j\ne i_\alpha\) crossing an \((i_\alpha,j)\)-square with
\[
\partial_j^X(i_\alpha;x)\ne\mathbf1_{\{j\in S_\alpha\}}.
\tag{4}
\]
Let \(\mathcal G_{\mathcal A}(X)\) be the adjacency graph of witnessing maximal simplices, joined when they share a codimension-one simplex. Its vertices and adjacency depend only on \(X\) and the indexed constraints.

**Theorem (simultaneous port-derivative witnesses and invariant galleries).** For every \(X\) and every family (3):

(i) If \(r\le n-1\), the graph \(\mathcal G_{\mathcal A}(X)\) is nonempty.

(ii) If \(r\le n-2\), the graph contains a connected component invariant under \(\tau\).

The bound \(r\le n-2\) for invariant connectedness is sharp in every dimension.

*Proof.* Recover a cube-edge coloring \(c\) from \(X\) and define at every vertex \(x\)
\[
g_\alpha(x)=(-1)^{\,c_{i_\alpha}(x)+\sum_{j\in S_\alpha}x_j}.
\tag{5}
\]
Every \(|S_\alpha|\) is even, and \(c_{i_\alpha}\) is antipodally odd, so \(g_\alpha(\bar x)=-g_\alpha(x)\). Changing the reconstructed coloring by complementation changes all \(g_\alpha\) by a global sign; their zero sets and sign-mixed simplices are unaffected. Moreover \(g_\alpha(x^{i_\alpha})=g_\alpha(x)\), and on a direction-\(j\) edge the sign changes precisely when (4) holds, by (2).

Extend the sign vector \(g=(g_1,\ldots,g_r)\) affinely on every simplex of \(\mathcal T_n\). This produces an odd continuous piecewise-linear map
\[
G:|\mathcal T_n|\cong S^{n-1}\longrightarrow\mathbb R^r.
\tag{6}
\]
If \(r\le n-1\), the Borsuk–Ulam theorem gives a zero of \(G\). The smallest simplex containing that zero has both signs in each coordinate, because zero is a convex combination of its vertex sign vectors. Its containing maximal simplex is therefore a witness for every constraint: along its vertex chain the sign of each \(g_\alpha\) changes on some edge, and such a step has direction different from \(i_\alpha\). This proves (i).

For (ii), we first prove a connected-zero-set principle. If \(F:S^d\to\mathbb R^r\) is an odd piecewise-linear map with \(r\le d-1\), some connected component of \(F^{-1}(0)\) is invariant under the antipodal map. Indeed, its zero set is a finite polyhedron, hence has finitely many connected components. If every component were exchanged with another, assign signs \(+1,-1\) to the paired components, obtaining an odd continuous function \(h:F^{-1}(0)\to\{-1,1\}\). Extend \(h\) continuously to the sphere and antisymmetrize its extension to get an odd function \(H\) that remains \(h\) on the zero set. The odd map \((F,H):S^d\to\mathbb R^{r+1}\) would be nowhere zero, contradicting Borsuk–Ulam because \(r+1\le d\).

Apply this principle to (6), with \(d=n-1\). Let \(Z_0\subseteq G^{-1}(0)\) be a connected \(\tau\)-invariant component. Every maximal simplex meeting \(Z_0\) is a witness, as above. The finite family of their closed intersections with \(Z_0\) covers \(Z_0\) and has connected intersection graph. When two maximal simplices share a zero \(z\), both contain the smallest simplex \(\rho\) containing \(z\). The maximal simplices containing \(\rho\) form a ridge-connected gallery in the triangulated sphere. Every intermediate ridge contains \(\rho\) and hence has both signs in each coordinate; all adjacent maximal simplices are witnesses. Thus all maximal simplices meeting \(Z_0\) belong to one connected component of \(\mathcal G_{\mathcal A}(X)\). Since this collection is invariant under \(\tau\), that component is invariant.

For sharpness, define the antipodally odd edge coloring
\[
c_i(x)=x_{i+1}\quad(i<n),\qquad c_n(x)=x_1.
\tag{7}
\]
Choose \(r=n-1\), with \((i_\alpha,S_\alpha)=(\alpha,\varnothing)\) for \(1\le\alpha<n\). Each constraint is met only by crossing direction \(i_\alpha+1\), so a witnessing facet chain must traverse all directions \(2,\ldots,n\). It therefore lies in one of the two opposite facets \(x_1=0\) or \(x_1=1\). These families have no adjacent maximal simplices, and \(\tau\) exchanges them. The coloring corresponds to a port cycle \(X\), so the threshold is sharp within the pointed-matroid class. \(\square\)

**Corollary (connected derivative-defect galleries under a large port intersection).** Suppose \(n\ge5\) is odd, \(I(X)\ge6\), and \(I\subseteq[n]\) is nonempty with \(|I|\le n-2\). There is a connected \(\tau\)-invariant gallery of facet-spanning geodesics such that for every path in the gallery, and every \(i\in I\), some step in direction \(j\ne i\) crosses a square with
\[
\partial_j^X(i;x)=0
\tag{8}
\]
whose projected corner lies in the terminal-hole set \(\mathfrak H_{ij}(X)\) defined by the codimension-two face-terminal condition.

*Proof.* For each \(i\in I\), use the mask \(S_i=[n]\setminus\{i\}\), whose size \(n-1\) is even. Equation (4) then becomes (8), and the theorem gives the invariant connected gallery. The terminal-hole inclusion for a port cycle with \(I(X)\ge6\) states that a square with derivative zero cannot project to a terminal of a face-spanning path with at most two changes: such a terminal would force both square derivatives to be one. Therefore each square in (8) projects into \(\mathfrak H_{ij}(X)\). \(\square\)

**Corollary (simultaneous opposite derivative values).** If \(n\ge5\) is odd and \(I\subseteq[n]\) satisfies \(2|I|\le n-2\), there is a connected, antipodally invariant gallery of facet-spanning geodesics such that every path in the gallery crosses, for every \(i\in I\), one square with \(\partial_j^X(i)=0\) and another (possibly involving a different direction) with \(\partial_k^X(i)=1\).

*Proof.* For each \(i\in I\), impose both masks \(S=\varnothing\) and \(S=[n]\setminus\{i\}\). They are even, and their requirements (4) force the derivative values one and zero, respectively. Apply the theorem with \(r=2|I|\). \(\square\)

These assertions give a dimension-independent, equivariant connectivity constraint on every port cycle, in addition to the numerical intersection and defect bounds. The gallery witnesses local square derivatives and retains the full facet-path flags. The existence of a minimum port cocircuit with small intersection remains an additional global extraction problem.

### Lifted phase transport and two-intersection splicing certificates

Let \(n\ge4\), \(G_n=Q_n/\langle\tau\rangle\), and \(H_n=L(G_n)\). Let \(X\) be a binary cycle of the pointed matroid \(D_n\) containing \(p\), with turn label \(d=\mathbf1_{X\setminus\{p\}}\). By the monodromy condition, the pullback of \(d\) to the connected graph \(L(Q_n)\) is a coboundary.

For two undirected cube edges \(e,f\), choose any turn path \(\gamma\) from \(e\) to \(f\) in \(L(Q_n)\) and put
\[
\rho_X(e,f)=\sum_{t\in\gamma}d([t])\pmod2.
\tag{1}
\]
Here \([t]\) denotes projection of a cube turn to \(H_n\). The result is independent of \(\gamma\), because every closed turn walk in \(L(Q_n)\) has zero pulled-back \(d\)-sum. Equivalently, if \(c\) is any recovered antipodally odd cube-edge coloring, then
\[
\boxed{\rho_X(e,f)=c(e)+c(f)\pmod2.}
\tag{2}
\]
In particular, \(\rho_X(e,\tau e)=1\), and for incident cube edges \(\rho_X(e,f)\) is their turn label \(d\). Thus \(\rho_X\) expresses relative color phases using the pointed-matroid cycle \(X\), independently of the global color complement.

For a cube geodesic \(P\), let \(A(P)\subseteq E(H_n)\) denote the projected consecutive turns, so that \(|A(P)\cap X|\) is its number of switches. Its edge-color phase on a monochromatic subpath can be compared to another such path by \(\rho_X\) between any one edge of each subpath.

**Lemma 1 (one missing direction).** If a cube geodesic traverses \(n-1\) distinct directions and all its edge turns lie outside \(X\), then some full antipodal cube geodesic has all its turn edges outside \(X\). Equivalently, the minimum shortest-port-cocircuit intersection \(I(X)\) equals two.

*Proof.* Let the \((n-1)\)-edge path run from \(u\) to \(v=\tau u^{\,b}\), missing direction \(b\), and have constant color \(s\). The \(b\)-edges at \(u\) and \(v\) are antipodal and therefore have complementary colors. One has color \(s\). Append it at \(v\) or prepend it at \(u\), choosing the endpoint where agreement occurs; the result is a monochromatic full antipodal geodesic. Its projected turn cycle has one labeled turn, hence its port cocircuit meets \(X\) in two elements. Every port intersection is a positive even integer, so this is minimal. \(\square\)

Fix distinct exterior directions \(a,b\), let \(D=[n]\setminus\{a,b\}\), and let \(F,F^a\) be adjacent \((n-2)\)-faces. For any \(u,x\in F\), let \(u^a,x^a\in F^a\) be the corresponding vertices.

**Theorem 2 (opposite-phase aligned switch certificate).** Suppose \(P\subset F\) and \(Q\subset F^a\) are geodesics spanning their faces, from \(u\) to \(x\) and from \(u^a\) to \(x^a\). Suppose both have precisely one turn in \(X\), at respective vertices \(z\in P\) and \(z^a\in Q\), and the sets \(A,B\) of directions used before and after these switch vertices agree between the two paths. Each set is nonempty; their internal orders may differ. If \(e_P,e_Q\) are their initial edges and
\[
\boxed{\rho_X(e_P,e_Q)=1,}
\tag{3}
\]
then
\[
\boxed{I(X)=2.}
\tag{4}
\]

*Proof.* Recover a coloring \(c\), and write \(s=c(e_P)\). Since \(P,Q\) each have one switch and (3) holds, their two blocks have colors
\[
P:\quad s^{|A|}(1+s)^{|B|},
\qquad
Q:\quad (1+s)^{|A|}s^{|B|}.
\tag{5}
\]
Let \(h=c(zz^a)\). If \(h=s\), the concatenation of the \(A\)-prefix of \(P\), the \(a\)-edge \(zz^a\), and the \(B\)-suffix of \(Q\) is a monochromatic geodesic from \(u\) to \(x^a\). If \(h=1+s\), concatenate the \(A\)-prefix of \(Q\), the reverse \(a\)-edge \(z^az\), and the \(B\)-suffix of \(P\), producing a monochromatic geodesic from \(u^a\) to \(x\). In either case the path uses every direction in \(D\cup\{a\}\) once and omits only \(b\). Apply Lemma 1. \(\square\)

The next certificate needs only monochromatic arms and the geometry of their meeting vertices.

**Theorem 3 (two-arm interface transport).** Let \(P\subset F\) and \(Q\subset F^a\) be spanning geodesics with corresponding initial and terminal vertices as above. Suppose \(w\) is an interior vertex of \(P\), and \(w^a\) is an interior vertex of \(Q\). The following implications hold.

(i) If the prefix \(P[u,w]\) and the suffix \(Q[w^a,x^a]\) have no turns in \(X\), and one edge \(e\) of the first and one edge \(f\) of the second satisfy \(\rho_X(e,f)=0\), then either \(I(X)=2\), or
\[
\boxed{\rho_X(e,ww^a)=1.}
\tag{6}
\]

(ii) If the prefix \(Q[u^a,w^a]\) and suffix \(P[w,x]\) have no turns in \(X\), and their chosen edges \(e',f'\) satisfy \(\rho_X(e',f')=0\), then either \(I(X)=2\), or
\[
\boxed{\rho_X(e',ww^a)=1.}
\tag{7}
\]

If both (i) and (ii) hold and \(\rho_X(e,e')=1\), then \(I(X)=2\).

*Proof.* The coordinate sets traversed by \(P[u,w]\) and \(Q[w^a,x^a]\) are disjoint and cover \(D\), because the two paths have corresponding start and end vertices, and the intermediate vertices are related by the \(a\)-translation. Under the first two hypotheses of (i), these arms have the same constant edge color, say \(s\). If the connecting \(a\)-edge \(ww^a\) had color \(s\), their concatenation would be a monochromatic geodesic using \(D\cup\{a\}\), and Lemma 1 would give \(I(X)=2\). If \(I(X)>2\), the joining edge must have color \(1+s\), which is (6) by (2).

The same argument, interchanging \(P,Q\), proves (ii). If both conclusions were required while \(\rho_X(e,e')=1\), the single joining \(a\)-edge would have to be opposite in color to two edges of opposite colors. This is impossible, so \(I(X)=2\). \(\square\)

**Corollary 4 (phase coherence in a high-intersection cycle).** Assume \(I(X)\ge4\). Two one-turn spanning geodesics on adjacent codimension-two faces with corresponding starting vertices, terminal vertices and switch vertices cannot have opposite initial phases. Likewise, any pair of interface configurations of Theorem 3 whose two monochromatic phases disagree cannot coexist at the same projected vertex.

*Proof.* The first assertion is the contrapositive of Theorem 2. The second is the last assertion of Theorem 3. \(\square\)

The transport \(\rho_X\) is a cocycle primitive on the lifted line graph. It expresses the phase information needed in the adjacent-face splicing theorems of Article VIII directly through the binary cycle \(X\). Theorems 2--3 give checkable geometric certificates forcing a shortest port cocircuit \(Y\) with \(|X\cap Y|=2\), the monochromatic intersection target.

Let (M,p) be a finite pointed binary matroid. Its port cogirth gamma_p(M) is the minimum cardinality of a cocircuit containing p. Let P4(M,p) mean: for every binary cycle X containing p, a port cocircuit Y of cardinality gamma_p(M) satisfies |X intersect Y| at most four. Theorem (contraction inheritance). Suppose T excludes p, M0=M/T, and gamma_p(M)=gamma_p(M0). If M0 satisfies P4, then M satisfies P4. Proof: project X to X0=X intersect (E(M) minus T), which is a binary cycle of M0. Choose a shortest port cocircuit Y of M0 intersecting X0 in at most four elements. Cocircuits of M0 are cocircuits of M disjoint from T, and cogirth equality makes Y shortest in M. Thus |X intersect Y|=|X0 intersect Y| at most four. The same argument works for the bound two. Consequently any pointed binary matroid with a port-cogirth-preserving contraction to the cube matroid D_n inherits the corresponding intersection conjecture, including the monochromatic strengthening.

##### Pointed binary generator construction

Let \((N,t)\) be a simple binary matroid on \(S\cup\{t\}\), where \(S\) spans \(t\). Let \(q\ge4\) be the smallest size of a circuit of \(N\) containing \(t\), and put \(\ell=q-1\). Represent the elements by distinct nonzero vectors \(s\in V=\mathbb F_2^r\) and \(t\in V\). Let \(K=\operatorname{Cay}(V,S)\), joining \(x\) to \(x+s\). Translation \(\tau(x)=x+t\) acts freely on vertices and edges, and \(G=K/\tau\) is simple because \(t\) is neither a generator nor a sum of two generators. Put \(H=L(G)\), with incidence matrix \(B_H\) over \(\mathbb F_2\) and a cochain \(a\) recording the covering monodromy of \(L(K)\to H\). Define the pointed binary matroid
\[
\mathfrak D(N,t)=M\left(\begin{array}{c|c}B_H&0\\a&1\end{array}\right)^*,
\]
where the new final column is the port \(p\). This construction is determined by the pointed matroid \((N,t)\), independently of choices of its binary representation or of the cochain \(a\).

**Theorem (cubical core and port cogirth).** Every such \(\mathfrak D(N,t)\) has port cogirth \(q=\ell+1\) and a contraction onto \(D_\ell\), preserving that port cogirth.


*Proof of the cubical-core theorem.* Choose a shortest circuit \(C\ni t\) of \(N\), and write \(A=C\setminus\{t\}\). Binary circuit dependence yields \(\sum_{s\in A}s=t\), while the \(\ell\) members of \(A\) are independent. For every root \(x\in V\), the induced directions \(A\) on \(x+\operatorname{span}(A)\) form a \(\tau\)-invariant \(Q_\ell\). This cube is induced in \(K\): if \(s\in S\setminus A\) belonged to the span of \(A\), then \(s\) would equal the sum of \(w\ge2\) members of \(A\), giving an expression of \(t\) using only \(\ell-w+1<\ell\) generators. Such an expression contradicts the choice of \(C\).

Therefore the folded cube \(Q_\ell/\tau\) embeds in \(G\), and its line graph \(H_\ell\) is induced in \(H\). Let \(F\) be its set of turns. Restricting the pointed matrix before dualization to \(F\cup\{p\}\), and deleting zero rows, gives the pointed matrix for \(D_\ell^*\): its incidence part is that of \(H_\ell\) and its monodromy row is the canonical cube covering class, up to a cut. Hence
\[
\mathfrak D(N,t)/(E(H)\setminus F)\cong D_\ell.
\]

Every port cocircuit of \(\mathfrak D(N,t)\) has the form \(C_H\cup\{p\}\) with \(C_H\) a simple turn cycle of \(H\) with odd covering monodromy. Lifting its cyclic sequence to \(L(K)\), the consecutive edge-contact vertices yield a walk of at most \(|C_H|\) generator steps from \(u\) to \(u+t\). Any such walk has at least \(\ell\) steps, because \(\ell\) is the shortest generator representation of \(t\). Thus \(|C_H|\ge\ell\). A geodesic inside the invariant \(Q_\ell\) gives an odd-monodromy turn cycle of length \(\ell\). Therefore the port cogirth is \(\ell+1=q\). \(\square\)


### Reversal-odd boundary tournaments as pointed turn matroids

Let \(V\) be a set of \(n\ge5\) vertices. An ordinary boundary 3-tournament is a function
\[
b:V_{\neq}^{3}\longrightarrow\mathbb F_2,\qquad
b(c,b_0,a)=1+b(a,b_0,c),
\tag{1}
\]
where \(V_{\neq}^{3}\) is the set of triples with pairwise distinct entries; \(b_0\) denotes the middle entry, to distinguish it from the function \(b\). The long-path witness is an injective word \(v_1,\ldots,v_m\) for which all \(m-2\) triple values \(b(v_i,v_{i+1},v_{i+2})\) agree.

**Proposition 1 (line-graph orientation).** Boundary 3-tournaments on \(V\) are in bijection with orientations of the ordinary line graph \(L(K_V)\). The edge between \(\{a,b_0\}\) and \(\{b_0,c\}\) is directed from the former to the latter precisely when \(b(a,b_0,c)=0\). A positive tight path corresponds to a directed walk through the successive vertices
\[
\{v_1,v_2\},\{v_2,v_3\},\ldots,\{v_{m-1},v_m\}
\tag{2}
\]
of \(L(K_V)\), with consecutive incidences alternating endpoints of their common \(K_V\)-edge and with the symbols \(v_i\) pairwise distinct.

*Proof.* Every edge of \(L(K_V)\) has a unique middle vertex \(b_0\) of \(K_V\), and is represented by a reversal pair \((a,b_0,c),(c,b_0,a)\). Equation (1) chooses one of the two orientations. Conversely every orientation makes this choice and defines the reversal-odd function. In (2), consecutive edges of \(L(K_V)\) represent the triples \((v_i,v_{i+1},v_{i+2})\). A zero value means the traversal follows the prescribed orientation. The incidence and injectivity conditions are precisely the conditions that this walk comes from an injective word of original vertices. \(\square\)

Define the **triple-overlap graph** \(\widetilde T_V\) to have vertex set \(V_{\neq}^3\), with an undirected edge between
\[
(a,b_0,c)\quad\text{and}\quad(b_0,c,d)
\tag{3}
\]
whenever \(a,b_0,c,d\) are pairwise distinct. Reversal \(J(a,b_0,c)=(c,b_0,a)\) is a fixed-point-free involution of \(\widetilde T_V\), and it maps the edge in (3) to the edge between \((d,c,b_0)\) and \((c,b_0,a)\). Put
\[
T_V=\widetilde T_V/\langle J\rangle,\qquad
\pi:\widetilde T_V\longrightarrow T_V.
\tag{4}
\]

**Lemma 2 (connected double cover).** For \(n\ge5\), \(\widetilde T_V\) and \(T_V\) are connected, and \(\pi\) is a regular two-sheeted graph covering. Their orders are
\[
|V(T_V)|=\frac{(n)_3}{2},\qquad
|E(T_V)|=\frac{(n)_4}{2},\qquad
\deg_{T_V}(x)=2(n-3),
\tag{5}
\]
where \((n)_r=n(n-1)\cdots(n-r+1)\).

*Proof.* A triple \((a,b_0,c)\) has \(n-3\) neighbors of the form \((b_0,c,d)\) and \(n-3\) of the form \((d,a,b_0)\). These are distinct, and no pair consists of reversals of one another: the middle two symbols of the starting triple are distinct. Thus the free involution also acts freely on edges and gives a graph covering; counting vertices and edges gives (5).

For connectivity, fix the middle symbol \(b_0\). Any first entry \(a\) can be changed to \(e\notin\{b_0,c\}\) through
\[
(a,b_0,c)\ --\ (b_0,c,d)\ --\ (e,b_0,c),
\tag{6}
\]
choosing \(d\notin\{a,b_0,c,e\}\), possible because \(n\ge5\). A symmetrical two-step walk changes the last entry while fixing the first and middle entries. These operations connect all ordered triples having the same middle symbol: the graph of ordered pairs of distinct elements of \(V\setminus\{b_0\}\), with changes of one entry, is connected. Finally (3) changes the middle symbol from \(b_0\) to any chosen \(c\ne b_0\) by selecting \(a,d\) distinct from the two. Hence \(\widetilde T_V\) is connected. \(\square\)

Let \(\alpha:Z_1(T_V;\mathbb F_2)\to\mathbb F_2\) denote the covering-monodromy functional: a closed walk has \(\alpha=0\) when its lift closes, and \(\alpha=1\) when its lift ends at the reversed triple. Choose any binary edge cochain \(a\in C^1(T_V;\mathbb F_2)\) representing \(\alpha\). Let \(B\) be the binary vertex-edge incidence matrix of \(T_V\), and introduce a distinguished element \(p\). Set
\[
\widehat A_V=
\begin{pmatrix}B&0\\a&1\end{pmatrix},
\qquad D_V^{\mathrm{BT}}=M(\widehat A_V)^*.
\tag{7}
\]
The pointed binary matroid depends only on \(V\) and the overlap/reversal structure, independently of a tournament coloring.

**Theorem 3 (boundary tournament–port-cycle correspondence).** A boundary tournament \(b\) defines a turn cochain on \(T_V\) by
\[
d_b(\pi\{t,s\})=b(t)+b(s).
\tag{8}
\]
It obeys
\[
\boxed{d_b=a+\delta f,\qquad f\in C^0(T_V;\mathbb F_2),}
\tag{9}
\]
and the binary cycles of \(D_V^{\mathrm{BT}}\) containing \(p\) are precisely
\[
\boxed{X_b=\operatorname{supp}(d_b)\cup\{p\}.}
\tag{10}
\]
Every port-containing binary cycle of \(D_V^{\mathrm{BT}}\) is of this form. The two boundary tournaments inducing a given port cycle are complementary: \(b\) and \(1+b\). Furthermore,
\[
\boxed{
\mathcal C^*(D_V^{\mathrm{BT}})\cap\{Y:p\in Y\}
=\{\,C\cup\{p\}: C\subseteq T_V\text{ a simple cycle with }\alpha(C)=1\,\}.
}
\tag{11}
\]
For such a cocircuit and a port cycle,
\[
\boxed{|X_b\cap(C\cup\{p\})|=1+|\operatorname{supp}(d_b)\cap C|
\quad\text{is a positive even integer}.}
\tag{12}
\]

*Proof.* Because \(b(Jt)=b(t)+1\), the sum \(b(t)+b(s)\) is unchanged on applying \(J\) to an overlap edge, so (8) is well-defined. Lift a closed walk \(C\) of \(T_V\), starting at \(t\). Telescoping (8) along the lift gives \(d_b(C)=b(t)+b(J^{\alpha(C)}t)=\alpha(C)\). Since \(a\) represents the same functional on cycles, \(d_b+a\) annihilates every graphic cycle. The cut-cycle orthogonality of a connected graph implies \(d_b+a=\delta f\).

Conversely any cochain \(d=a+\delta f\) pulls back to a coboundary on the connected graph \(\widetilde T_V\), since its sum on every lifted closed cycle vanishes. Integrate from one triple \(t_0\) to obtain \(b\). Because the covering involution preserves the pullback cochain, \(b(Jt)+b(t)\) is constant on the connected covering graph; evaluating on an odd-monodromy lifted walk gives the constant one. Thus (1) holds. The integration is unique up to a global constant, producing the two complementary colorings.

The row space of (7) is the binary cycle space of its dual and consists of \((\delta f,0)\) and \((a+\delta f,1)\), proving (10). A port-containing circuit of \(M(\widehat A_V)\), equivalently a port-containing cocircuit of \(D_V^{\mathrm{BT}}\), has a graphic Eulerian part with monodromy one. Its minimality forces this part to be a single simple odd-monodromy cycle, proving (11). Finally \(d_b(C)=\alpha(C)=1\), so its integer support weight on \(C\) is odd; adjoining the common port proves (12). \(\square\)

Since \(|V(T_V)|=(n)_3/2\) and \(|E(T_V)|=(n)_4/2\), the dual matroid has rank
\[
\operatorname{rank}D_V^{\mathrm{BT}}
=\frac{(n)_4-(n)_3}{2}+1.
\tag{13}
\]

**Theorem 4 (tight-path decoding).** Let \(3\le m\le n\). For an injective word \(v=(v_1,\ldots,v_m)\), define the forward overlap path \(\gamma_v\) in \(\widetilde T_V\) through
\[
t_i=(v_i,v_{i+1},v_{i+2}),\qquad 1\le i\le m-2,
\tag{14}
\]
and let \(\pi\gamma_v\) denote its projected path in \(T_V\). Then
\[
\boxed{
\sum_{i=1}^{m-3}
[b(v_i,v_{i+1},v_{i+2})\ne b(v_{i+1},v_{i+2},v_{i+3})]
=|\operatorname{supp}(d_b)\cap E(\pi\gamma_v)|.
}
\tag{15}
\]
Consequently \(b\) has a vertex-simple monochromatic tight path on \(m\) original vertices if and only if
\[
\boxed{
\min_{\substack{v_1,\ldots,v_m\in V\\\text{pairwise distinct}}}
|X_b\cap E(\pi\gamma_v)|=0.
}
\tag{16}
\]
The same condition characterizes the existence of a positive tight path, since reversing an injective word complements and reverses its color word.

*Proof.* Each edge of \(\gamma_v\) is the overlap of the consecutive triples in (14). By (8), it is labeled one precisely when their colors differ. Pairwise distinct symbols imply that the projected vertices and edges of \(\gamma_v\) are not repeated, so the right side of (15) counts each transition once. Vanishing means the triple-color word is constant, proving (16). The reversal identity (1) changes a constant-one word into a constant-zero word. \(\square\)

**Proposition 5 (bounded odd-girth).** For every \(n\ge5\), the least size of a port-containing cocircuit of \(D_V^{\mathrm{BT}}\) is seven. Equivalently, the least length of a cycle of \(T_V\) with monodromy one is six.

*Proof.* Choose five distinct symbols \(a,b_0,c,d,e\). The following is a six-edge path in \(\widetilde T_V\):
\[
\begin{split}
(a,b_0,c)&\;--\;(b_0,c,e)\;--\;(d,b_0,c)\;--\;(e,d,b_0)\\
&\;--\;(d,b_0,a)\;--\;(b_0,a,e)\;--\;(c,b_0,a).
\end{split}
\tag{17}
\]
Its endpoints are reversals, and its six intermediate reversal-orbits are distinct. Its projection is therefore a simple six-cycle with monodromy one.

To verify minimality uniformly in \(n\), a path of length at most five from a triple to its reverse uses at most eight symbols: each overlap step retains two existing symbols and introduces at most one. Relabel those symbols into \(\{0,\ldots,7\}\). It is enough to verify in the graph on the \(336\) ordered triples of eight symbols that \((2,1,0)\) lies outside the radius-five ball around \((0,1,2)\). The following exhaustive finite check uses precisely the adjacency definition (3):
\[
\begin{array}{l}
R=\{(0,1,2)\};\\
\text{repeat five times: }\;
R\leftarrow R\cup\bigcup_{(a,b_0,c)\in R}
\{(b_0,c,d),(d,a,b_0):d\notin\{a,b_0,c\}\};\\
(2,1,0)\notin R.
\end{array}
\tag{18}
\]
For reproducibility, the respective distance-layer cardinalities through radius five are \(1,10,55,162,97,10\); a sixth step reaches the reversed triple. This computation covers every possible path of length at most five in any order \(n\), because of the eight-symbol cutoff. Thus the least odd-monodromy cycle has length six, and (11) gives cocircuit size seven. \(\square\)

**Witness distinction.** In the cube case of Article XI, shortest odd-monodromy cycles themselves encode full antipodal geodesics. In the boundary-tournament matroid, port cocircuits of size seven exist uniformly in \(n\), while the long-path target in (16) is a *forward*, symbol-injective overlap path that need not be closed. Accordingly (16) is the pertinent cycle–path zero-intersection problem; the short port cocircuits of (11) encode local reversal monodromy and do not themselves encode long tight paths. This distinction also records both endpoint-seam constraints implicitly in the ordered overlap path: concatenations must preserve directed pair overlaps and the injectivity of the underlying word.

Let \(n\ge5\), let \(c\) be any antipodally odd red--blue coloring of the edges of \(Q_n\), and let \(d=a+\delta f\) denote its binary turn cochain on the folded-cube turn graph \(H_n=L(Q_n/\tau)\). Write \(\mathcal A_n\) for the simple odd-monodromy length-\(n\) cycles (cyclic completions of full antipodal geodesics). Their port cocircuits in the pointed dual matroid \(D_n\) are \(Y_C=C\cup\{p\}\), and the integer cyclic turn weight is \(w_d(C)=\sum_{t\in C}d(t)=|X_d\cap Y_C|-1\), where \(X_d=\operatorname{supp}(d)\cup\{p\}\).

**Theorem 1 (local square-exchange rigidity).** Suppose \(w_d(C)\) has the same integer value for every \(C\in\mathcal A_n\). Then, at every cube vertex, all incident edges have one color except possibly a single edge of the other color. Equivalently, if \(k_v\) of the \(n\) incident edges at \(v\) have color one, then
\[
\boxed{k_v\in\{0,1,n-1,n\}\quad\text{for every }v\in V(Q_n).}\tag{1}
\]

*Proof.* Suppose a vertex \(v\) has at least two incident edges of each color. Choose two distinct coordinate directions \(i,j\) whose edges at \(v\) have different colors. Removing these directions leaves at least one direction \(h_0\) of color zero and one direction \(h_1\) of color one at \(v\). As \(n\ge5\), choose a further direction \(k\notin\{i,j,h_0,h_1\}\).

For each \(h\in\{h_0,h_1\}\), construct a full antipodal geodesic starting at \(v^{h}\) and beginning with coordinate order \((h,i,j,k,\ldots)\), where the remaining unused coordinates appear in any order. Construct a second geodesic with the same start, predecessor and successor but the middle two directions interchanged: \((h,j,i,k,\ldots)\). These two geodesics agree outside the four-edge square swap, including at their cyclic closing seam. Write
\[
\begin{aligned}
P_h&=c_h(v), &A&=c_i(v), &C&=c_j(v),\\
B&=c_j(v^i), &D&=c_i(v^j),&
Q&=c_k(v^{ij}),
\end{aligned}
\]
where \(c_l(z)\) denotes the color of the undirected coordinate-\(l\) edge at \(z\) and \(v^S\) denotes toggling the coordinates in \(S\). Let \(\Delta(x,y)=\mathbf1_{\{x\ne y\}}\). Equality of all cyclic turn weights gives, separately for each \(h\),
\[
\boxed{
\Delta(P_h,A)+\Delta(A,B)+\Delta(B,Q)
=
\Delta(P_h,C)+\Delta(C,D)+\Delta(D,Q).
}\tag{2}
\]
Only the three turns immediately around the exchanged two-edge square segment differ; the cyclic seam and all other turns cancel. Since \(P_{h_0}=0\) and \(P_{h_1}=1\), subtracting the two instances of (2) yields
\[
\Delta(0,A)-\Delta(0,C)=\Delta(1,A)-\Delta(1,C).
\]
For binary \(A,C\), the left side equals \(A-C\) and the right side equals \(C-A\), so \(A=C\). This contradicts the choice of \(i,j\) with different colors. Hence no vertex can have two incident edges of both colors, proving (1). \(\square\)

**Theorem 2 (flat shortest-port intersection spectrum forces two-point intersection).** If the intersection cardinality \(|X_d\cap Y|\) is independent of \(Y\) among all shortest port cocircuits of \(D_n\), then
\[
\boxed{|X_d\cap Y|=2\qquad\text{for every shortest port cocircuit }Y.}\tag{3}
\]
Equivalently, if all antipodal geodesics have the same cyclic turn count, then they all have turn count one and each admits a monochromatic rooted antipodal geodesic after cyclic rotation.

*Proof.* Theorem 1 implies that every star of the folded cube has at most one exceptional edge color. At a quotient vertex, the number of disagreeing turns is \(k_v(n-k_v)\), hence at most \(n-1\). There are \(2^{n-1}\) quotient vertices, each yielding \(\binom n2\) turns. Therefore, with \(E=|E(H_n)|\) and \(D=|\operatorname{supp}(d)|\),
\[
\frac DE\le\frac{n-1}{\binom n2}=\frac2n.
\tag{4}
\]
Each turn of \(H_n\) lies in the same number of length-\(n\) monodromy-one cycles by cube symmetry. Consequently
\[
\mathbb E_{C\in\mathcal A_n}w_d(C)=nD/E\le2.
\tag{5}
\]
By monodromy, \(w_d(C)\) is a positive odd integer for every such cycle. If this value is constant, (5) forces it to be one. The intersection identity \(1+w_d(C)=|X_d\cap Y_C|\) gives (3). Finally cyclic rotation of an odd-monodromy turn cycle allows omission of one changed seam, so a turn count of one yields a rooted geodesic with zero changes. \(\square\)

**Corollary 3 (all-dimensional nonflatness of a counterexample).** For \(n\ge5\), any antipodally odd coloring with no monochromatic full antipodal geodesic has at least two different values of \(|X_d\cap Y|\) among its shortest port cocircuits. By the previously proved gap-free even intersection spectrum, the values differ by an even amount and each intermediate even intersection is attained. In particular, if every shortest port cocircuit intersects \(X_d\) in at least six points, then some such cocircuit has intersection at least eight points.

*Proof.* Otherwise the spectrum is a singleton, and Theorem 2 produces monochromatic geodesics. All intersections are positive even by binary orthogonality, and the connected adjacent-exchange spectrum theorem supplies gap-free interpolation. \(\square\)

**Corollary 4 (two-switch closure through dimension nine).** For every \(2\le n\le9\), every antipodally odd two-edge coloring of \(Q_n\) has a full antipodal geodesic with at most two color changes, equivalently a shortest port cocircuit intersecting its coloring cycle in at most four elements.

*Proof.* For \(n=2,3,4\), the star-density expectation bound below is strictly smaller than five (or apply known elementary low-dimensional results). For \(5\le n\le9\), at any quotient cube vertex with \(k_v\) incident edges of color one, the number of disagreeing turns is \(k_v(n-k_v)\le\lfloor n^2/4\rfloor\), so
\[
\mathbb E_{C\in\mathcal A_n}w_d(C)
=\frac{nD}{E}
\le\frac{n\lfloor n^2/4\rfloor}{\binom n2}.
\tag{6}
\]
For \(2\le n\le8\), the right side is strictly below five; because every weight is odd, one is at most three. For \(n=9\), the right side is five. If every weight were at least five, equality of averages would force *every* geodesic to have weight five. Theorem 2 excludes a constant value of five, since any constant weight must equal one. Thus some geodesic has weight at most three. In all cases, cyclic rotation removes one changed seam, yielding at most two switches. \(\square\)

Theorems 1--2 are unrestricted dimension-independent rigidity statements, not a tractable special-class analysis. Corollary 4 resolves the equality boundary of the sharp global star-incidence bound; the unrestricted two-switch problem in higher dimensions remains open. A possible continuation is a stability version: quantify how many adjacent-square exchanges necessarily change their turn cost when a star contains at least two edges of each color, and combine it with the two-port cocircuit weight enumerators to restrict the fraction of high-weight shortest port cocircuits.

**Corollary 5 (rigidity-sharpened all-dimensional staircase bound).** Every antipodally odd two-edge coloring of \(Q_n\), \(n\ge2\), admits a full antipodal geodesic with at most
\[
\boxed{\displaystyle
2\left\lfloor\frac{n-2}{4}\right\rfloor
}
\tag{7}
\]
color changes. In particular, there is a monochromatic full antipodal geodesic for \(n\le5\), at most two changes for \(6\le n\le9\), and at most four for \(10\le n\le13\). The upper bound is not claimed to be optimal when \(n\ge6\).

*Proof.* For even \(n=2m\ge4\), (6) gives
\[
\mathbb E w_d(C)\le\frac{2m^2}{2m-1}
=m+\frac m{2m-1}<m+1.
\]
Since all weights are positive odd integers, one is at most the greatest odd integer not exceeding \(m\), namely \(2\lfloor(m-1)/2\rfloor+1\). Removing its changed cyclic seam gives at most \(2\lfloor(m-1)/2\rfloor=2\lfloor(n-2)/4\rfloor\) switches.

For odd \(n=2m+1\ge5\), (6) gives \(\mathbb Ew_d(C)\le m+1\). If \(m\) is odd, this upper bound is even, so some odd weight is at most \(m\). If \(m\) is even, the upper bound \(m+1\) is odd. Were all weights at least \(m+1\), equality of the average would force all weights to equal \(m+1\), contradicting Theorem 2 because \(m+1\ge3\). Therefore some weight is at most \(m-1\). The two cases yield the same bound (7) after removing a changed seam. The \(n=2,3\) cases follow directly from (6), whose right side is two. \(\square\)

This counting bound is linear in \(n\), and does not improve the known asymptotic \(O(\sqrt n)\) geodesic-change bound. Its purpose here is the matroidal rigidity mechanism at the equality boundary, not an asymptotic claim.

Let \(n\ge5\), \(F_n=Q_n/\langle\tau\rangle\), and \(H_n=L(F_n)\). Write \(t_{ij}([x])\) for the turn between coordinate directions \(i,j\) at a folded vertex orbit \([x]\). Let \(\alpha\) be the two-cover monodromy and \(\kappa\) the stationary-contact curvature of the earlier two-port construction. The set \(\mathcal G_n\) of full antipodal-geodesic turn cycles consists of the shortest port cocircuits with their ports deleted.

Define the binary exchange span
\[
\mathscr B_n=\operatorname{span}_{\mathbb F_2}
\{C\mathbin\triangle C':C,C'\in\mathcal G_n\}.
\tag{1}
\]
By the connected adjacent-exchange theorem in this Article, \(\mathscr B_n\) is generated by the six-turn cycles
\[
\begin{aligned}
Z_{x;h,i,j,k}={}&t_{hi}([x])+t_{hj}([x])
+t_{ij}([x^i])+t_{ij}([x^j])\\
&+t_{jk}([x^{ij}])+t_{ik}([x^{ij}]),
\end{aligned}\tag{2}
\]
for pairwise distinct directions \(h,i,j,k\). These are the symmetric differences of geodesic cycles before and after an adjacent swap of \(i,j\). The earlier balanced-hexagon theorem shows \(\mathscr B_n\subseteq\ker\alpha\cap\ker\kappa\).

**Theorem 1 (geodesic-exchange homology).** For every \(n\ge5\),
\[
\boxed{\dim(\ker\alpha/\mathscr B_n)=n,\qquad
\dim((\ker\alpha\cap\ker\kappa)/\mathscr B_n)=n-1.}
\tag{3}
\]
In particular,
\[
\boxed{\dim\mathscr B_n=
|E(H_n)|-|V(H_n)|-n=n(n-2)2^{n-2}-n.}
\tag{4}
\]
The dual of \(\ker\alpha/\mathscr B_n\) is naturally the \(n\)-dimensional vector space of antipodally invariant affine Boolean functions
\[
\mathcal A_n=\left\{f(x)=a_0+\sum_{r=1}^n a_rx_r:
\ \sum_{r=1}^n a_r=0\pmod2\right\}.
\tag{5}
\]

*Proof, step one (star-triangle reduction).* The line-graph cycle-space sequence proved earlier in Article XI gives
\[
0\longrightarrow K_n\longrightarrow Z_1(H_n)
\xrightarrow{\varphi}Z_1(F_n)\longrightarrow0,
\tag{6}
\]
where \(K_n\) is the span of all local star triangles
\[
T_{[x];i,j,k}
=t_{ij}([x])+t_{ik}([x])+t_{jk}([x]).
\tag{7}
\]
Write \(\beta\) for monodromy of \(Q_n\to F_n\); then \(\alpha=\beta\circ\varphi\). The cycle space of the cube is generated by coordinate squares. Every monodromy-zero cycle of \(F_n\) lifts to a closed cube cycle and hence is a sum of projected squares, giving that these squares span \(\ker\beta\). Every coordinate square in \(F_n\) is the \(\varphi\)-image of some exchange hexagon (2); select any distinct auxiliary directions \(h,k\) outside the two square directions. Therefore \(\varphi(\mathscr B_n)=\ker\beta\). Every element of \(\ker\alpha\) is congruent modulo \(\mathscr B_n\) to an element of \(K_n\). Thus \(\ker\alpha/\mathscr B_n\) is generated by local star triangles.

*Step two (square relations on folded vertex classes).* Choose distinct \(h,h',i,j\). Since \(n\ge5\), choose a fifth direction \(k\). The difference of two hexagons with the same \(x,i,j,k\) and predecessors \(h,h'\) is
\[
Z_{x;h,i,j,k}+Z_{x;h',i,j,k}
=T_{[x];h,i,j}+T_{[x];h',i,j}.
\tag{8}
\]
It follows that triangles at the same folded vertex \([x]\) with two common directions agree modulo \(\mathscr B_n\). The graph of three-subsets of \([n]\) connected by two-element overlaps is connected, so all star triangles at \([x]\) have one common quotient class, denoted \(T_{[x]}\).

Define the four-turn coordinate square
\[
S_{ij}(x)=t_{ij}([x])+t_{ij}([x^i])
+t_{ij}([x^j])+t_{ij}([x^{ij}]).
\tag{9}
\]
Rearranging the six edges of an exchange hexagon yields the binary identity
\[
Z_{x;h,i,j,k}
=T_{[x];h,i,j}+S_{ij}(x)+T_{[x^{ij}];i,j,k}.
\tag{10}
\]
Thus modulo \(\mathscr B_n\), \(S_{ij}(x)=T_{[x]}+T_{[x^{ij}]}\). Applying (10) with the base point \(x^i\) gives the same square cycle as \(T_{[x^i]}+T_{[x^j]}\). Hence
\[
\boxed{T_{[x]}+T_{[x^i]}+T_{[x^j]}+T_{[x^{ij}]}=0
\quad(i\ne j).}
\tag{11}
\]

The quotient is therefore generated by one formal vertex class for each orbit \([x]\) and subjected to the square relations (11), possibly with further relations. The dual of the formal square-relation quotient consists of antipodally invariant Boolean functions \(f\) with vanishing mixed second derivatives on every coordinate square. Such functions are affine \(f(x)=a_0+\sum_i a_ix_i\); antipodal invariance imposes \(\sum_i a_i=0\). There are \(n\) free coefficients. Consequently
\[
\dim(\ker\alpha/\mathscr B_n)\le n.
\tag{12}
\]

*Step three (all affine functionals survive).* Fix \(f(x)=a_0+L(x)\in\mathcal A_n\), where \(L(x)=\sum_i a_ix_i\). Define a binary turn cochain by
\[
\boxed{\omega_f(t_{ij}([x]))=
a_0+L(x)(1+x_i+x_j).}
\tag{13}
\]
Because \(\sum_i a_i=0\), both \(L(x)\) and \(x_i+x_j\) are invariant under complementation, so \(\omega_f\) is defined on the folded quotient. On a local star triangle,
\[
\boxed{\omega_f(T_{[x];i,j,k})=a_0+L(x)=f(x).}
\tag{14}
\]
For the hexagon (2), put \(u=x_i+x_j\). The contributions of its two turns centered at \(x\) together equal \(uL(x)\); the two centered at \(x^{ij}\) contribute \(uL(x^{ij})\); the remaining two turns centered at \(x^i,x^j\) contribute \(uL(x^i)\) and \(uL(x^j)\). Its six constant terms cancel. Accordingly
\[
\omega_f(Z_{x;h,i,j,k})
=u\bigl[L(x)+L(x^i)+L(x^j)+L(x^{ij})\bigr]=0
\tag{15}
\]
by linearity of \(L\). So every \(\omega_f\) annihilates \(\mathscr B_n\). If such a functional vanished on all of \(\ker\alpha/\mathscr B_n\), then (14) would give \(f(x)=0\) at every cube vertex, implying \(f=0\). Hence the \(n\)-dimensional space \(\mathcal A_n\) injects into the dual of the quotient:
\[
\dim(\ker\alpha/\mathscr B_n)\ge n.
\tag{16}
\]
Together with (12), this proves the first equality in (3) and the dual identification in (5).

The contact-curvature class \(\kappa\) vanishes on all exchange hexagons and evaluates to one on each star triangle. On \(\ker\alpha/\mathscr B_n\), it therefore corresponds to the constant affine function \(f=1\), a nonzero linear functional. Its kernel has codimension one, proving the second equality in (3).

Finally, \(H_n\) is connected, \(\alpha\ne0\), and
\[
|V(H_n)|=n2^{n-2},\qquad
|E(H_n)|=\binom n2\,2^{n-1}.
\]
Therefore \(\dim\ker\alpha=|E(H_n)|-|V(H_n)|\), giving (4). \(\square\)

**Corollary 2 (residual star-triangle classes).** With \(K_n=\ker\varphi\) from (6),
\[
\boxed{\dim K_n/(K_n\cap\mathscr B_n)=n.}
\tag{17}
\]
The surviving star-triangle classes are generated by the vertex-orbit classes \(T_{[x]}\), and their full dual is \(\mathcal A_n\). This follows from \(\varphi(\mathscr B_n)=\ker\beta\) and the second isomorphism theorem.

**Scope and implications.** The fifth-direction argument in (8) is essential to this proof. The formula is not true at \(n=4\), where direct binary elimination gives \(\dim\mathscr B_4=22\), instead of \(28\). Theorem 1 is unrestricted for all \(n\ge5\). It computes the binary homological deficiency of the entire shortest-port cocircuit Coxeter exchange system, not merely the effect of a bounded number of swaps. It does not settle the minimum *integer* color-intersection question: a binary linear relation alone cannot force intersection at most four with a shortest port cocircuit. The residual affine classes provide a new structural object for topological or nonlinear refinements of the matroid approach.

**Theorem 3 (complete binary exchange-charge criterion).** Identify folded-cube vertices with the quotient group \(V_n=\mathbb F_2^n/\langle\mathbf1\rangle\). For a turn edge \(t_{ij}([x])\), define its vertex charge
\[
\xi(t_{ij}([x]))=(1+x_i+x_j)[x]\in V_n,
\tag{18}
\]
and extend \(\xi\) linearly to turn-edge chains. This is well defined: both the factor \(1+x_i+x_j\) and the class \([x]\) are invariant under antipodal complementation. Define the parity charge
\[
\sigma(Z)=|Z|\pmod2
\tag{19}
\]
for a binary turn chain \(Z\).

Then for every \(n\ge5\),
\[
\boxed{\mathscr B_n=
\{Z\in Z_1(H_n;\mathbb F_2):
\alpha(Z)=0,\ \sigma(Z)=0,\ \xi(Z)=0\}.}
\tag{20}
\]
The map
\[
(\sigma,\xi):\ker\alpha\longrightarrow\mathbb F_2\oplus V_n
\tag{21}
\]
is surjective and has kernel \(\mathscr B_n\). Each star triangle centered at \([x]\) has
\[
\boxed{(\sigma(T_{[x];i,j,k}),\xi(T_{[x];i,j,k}))=(1,[x]).}
\tag{22}
\]
Every full antipodal-geodesic turn cycle \(C\in\mathcal G_n\) satisfies
\[
\boxed{\sigma(C)=n\bmod2,\qquad \xi(C)=0.}
\tag{23}
\]

*Proof.* For \(f=a_0+L\in\mathcal A_n\), with \(L(x)=\sum_i a_ix_i\) and \(\sum_i a_i=0\), the cochain in (13) satisfies, on every binary turn chain \(Z\),
\[
\omega_f(Z)=a_0\sigma(Z)+\langle a,\xi(Z)\rangle.
\tag{24}
\]
All binary linear functionals on the quotient group \(V_n=\mathbb F_2^n/\langle\mathbf1\rangle\) are given by even-weight coefficient vectors \(a\). Together with the independent constant coefficient \(a_0\), formula (24) runs through the full dual of \(\mathbb F_2\oplus V_n\). By Theorem 1 the \(\omega_f\) separate the entire quotient \(\ker\alpha/\mathscr B_n\); therefore (21) is an isomorphism on that quotient, yielding surjectivity and (20).

For a star triangle, its three turn-edge parity bits sum to one. The coefficients \(1+x_i+x_j\), \(1+x_i+x_k\), and \(1+x_j+x_k\) sum to one, proving (22).

For the canonical monotone full geodesic rooted at \(0^n\) with direction order \(1,2,\ldots,n\), each interior turn lies at a vertex \(x\) with \(x_i=1\), \(x_j=0\) for its consecutive directions \(i,j\), so its vertex-charge coefficient \(1+x_i+x_j\) is zero. The cyclic closing turn lies at \(\mathbf1\), whose class in \(V_n\) is zero. Hence \(\xi(C)=0\) for this geodesic. The connected geodesic-exchange theorem and \(\xi(\mathscr B_n)=0\) propagate that identity to every \(C\in\mathcal G_n\). Each such cycle has \(n\) turn edges, proving (23). \(\square\)

**Corollary 4 (affine obstruction to shortening an odd-monodromy turn cycle).** Fix any full geodesic cycle \(G\in\mathcal G_n\). For every odd-monodromy simple turn cycle \(C\) of \(H_n\),
\[
\boxed{C\mathbin\triangle G\in\mathscr B_n
\iff \sigma(C)\equiv n\pmod2\ \text{and}\ \xi(C)=0.}
\tag{25}
\]
The criterion is independent of the choice of \(G\). It concerns *binary homology generated by exchange hexagons*, not the existence of a sequence of legal simple-cycle-preserving swaps from \(C\) to \(G\).

**Corollary 5 (complete local pivot charge).** Removing or inserting a stationary edge state by a star-triangle pivot at folded cube vertex \([x]\) changes the charge pair \((\sigma,\xi)\) by
\[
\boxed{(1,[x]).}
\tag{26}
\]
Consequently, if a sequence of such pivots at vertices \([x_1],\ldots,[x_r]\) takes a monodromy-one cycle to a chain homologous through exchange hexagons to a full geodesic, the pivot sites necessarily satisfy
\[
\boxed{r\equiv \sigma(C)+n\pmod2,\qquad
[x_1+\cdots+x_r]=\xi(C)\in V_n.}
\tag{27}
\]
Conversely these two equations suffice for the **binary homology class** of the pivoted chain to equal the geodesic-exchange class; they do not guarantee that every intermediate pivot is geometrically admissible or that the integer turn cost remains small.

*Proof.* A star-triangle pivot changes the binary cycle by adding the corresponding star triangle (7). Apply (22) and the linearity of \(\sigma,\xi\). Summing over all pivots and using (23) yields (27). The converse for binary homology follows from (20). \(\square\)

These identities give an explicit and efficiently computable affine charge for the entire geodesic-exchange complex. The \(n-1\) previously unexplained residual classes are the components of \(\xi\), and the final independent charge is length parity. They supply necessary conditions for path-surgery schemes that preserve the exchange-homology sector. They do not alone impose a low integer cycle--cocycle intersection.

**Theorem 6 (resource-multiplicity formula for affine exchange charge).** Let \(C\) be a simple monodromy-one turn cycle of \(H_n\) with no stationary contacts. Its lifted contact sequence is an antipodal cube-edge walk
\[
v_0=x\xrightarrow{d_1}v_1\xrightarrow{d_2}\cdots
\xrightarrow{d_r}v_r=\bar x,
\tag{28}
\]
with each direction \(i\) traversed \(m_i=1+2u_i\) times, \(u_i\ge0\). Then the affine vertex charge \(\xi\) defined in (18) satisfies
\[
\boxed{\xi(C)=\left[\sum_{i=1}^n u_i e_i\right]
\in\mathbb F_2^n/\langle\mathbf1\rangle.}
\tag{29}
\]
In particular it depends only on the repeated-resource multiplicities modulo four, not on their traversal order or starting vertex.

*Proof.* Let \(o_t=(v_{t-1})_{d_t}\in\mathbb F_2\) be the bit of the direction traversed at step \(t\), at its tail. Put \(o_{r+1}=o_1+1\), because the cyclic closing edge is the antipode of the first edge. For every contact turn, including the closing seam,
\[
1+(v_t)_{d_t}+(v_t)_{d_{t+1}}=o_t+o_{t+1}.
\tag{30}
\]
Summing the charge contributions over the turn cycle, then collecting terms from consecutive contact vertices, gives the identity in \(\mathbb F_2^n\)
\[
\begin{aligned}
\sum_{t=1}^{r}(o_t+o_{t+1})v_t
&=\sum_{t=1}^r o_t(v_t+v_{t-1})+
o_1(v_0+v_r)+v_r\\
&=\sum_{t=1}^r o_t e_{d_t}+o_1\mathbf1+\bar x.
\end{aligned}
\tag{31}
\]
Modulo \(\langle\mathbf1\rangle\), therefore,
\[
\xi(C)=\left[x+\sum_{t=1}^r o_t e_{d_t}\right].
\tag{32}
\]
For a fixed coordinate \(i\), the bit at its tail alternates \(x_i,x_i+1,x_i,\ldots\) along the \(m_i\) traversals of that coordinate. Consequently
\[
\sum_{\{t:d_t=i\}}o_t=x_i+\lfloor m_i/2\rfloor=x_i+u_i
\pmod2,
\tag{33}
\]
because \(m_i\) is odd. Substitute (33) in (32); the starting vertex cancels and yields (29). \(\square\)

**Corollary 7 (stationary-contact charge accounting).** Let \(C\) be any simple odd-monodromy turn cycle. Apply the unique-moving-core theorem to delete its \(s\) stationary edge states, with contact sites \([z_1],\ldots,[z_s]\) in the folded cube. Let the resulting stationary-free core traverse direction \(i\) \(1+2u_i\) times. Then
\[
\boxed{\sigma(C)=n+s\pmod2,\qquad
\xi(C)=\left[\sum_i u_i e_i+\sum_{\ell=1}^s z_\ell\right].}
\tag{34}
\]

*Proof.* The core has \(n+2\sum_i u_i\) turns, of parity \(n\), and its vertex charge is (29). Every removed stationary state is restored by adding a local star triangle, whose charge is \((1,[z_\ell])\) by (22). Summing these charges gives (34). The confluence theorem ensures these contact sites and the core are independent of the contraction order. \(\square\)

**Corollary 8 (nontrivial charge of the first excess layers).** If a stationary-free antipodal walk uses one direction three times and every other direction once, then \(\xi(C)=[e_i]\ne0\). If its two repeated pairs occur in two distinct directions \(i,j\), then \(\xi(C)=[e_i+e_j]\ne0\) for \(n\ge5\). Thus neither type of nongeodesic cycle can be homologous to a geodesic by geodesic-exchange hexagons alone. If one direction is instead traversed five times, its half-excess is two and \(\xi(C)=0\); this removes the affine homology obstruction but does not guarantee a geometrically legal shortening or a bound on coloring cost.

The new charge formula relates the previously calculated \(n-1\) binary homology classes to the auxiliary resource matroid: they measure *half the directional multiplicities* modulo the antipodal all-ones vector. It explains why portless square-exchange cocircuits cannot remove the first repeated-resource defects, while stationary star-triangle pivots change the charge in a controllable way. It does not prove the existence of a bounded-intersection shortest port cocircuit.

**Corollary 9 (fixed-star normal form and complete cycle-space decomposition).** Choose the folded cube vertex orbits
\[
[0],\quad[e_1],\ldots,[e_{n-1}]
\tag{36}
\]
(the omitted direction \(n\) is arbitrary), and choose any fixed triple of distinct directions \(a,b,c\). Let \(T_0=T_{[0];a,b,c}\) and \(T_i=T_{[e_i];a,b,c}\) for \(1\le i<n\). For any fixed full antipodal-geodesic turn cycle \(G\), there are direct-sum decompositions
\[
\boxed{
\ker\alpha=\mathscr B_n\ \oplus\
\operatorname{span}\{T_0,T_1,\ldots,T_{n-1}\},
}
\tag{37}
\]
\[
\boxed{
\ker\alpha\cap\ker\kappa=\mathscr B_n\ \oplus\
\operatorname{span}\{T_i+T_0:1\le i<n\},
}
\tag{38}
\]
and
\[
\boxed{
Z_1(H_n;\mathbb F_2)=\mathscr B_n\ \oplus\
\operatorname{span}\{T_0,\ldots,T_{n-1}\}\ \oplus\
\operatorname{span}\{G\}.
}
\tag{39}
\]
Thus every binary turn cycle is generated by six-turn geodesic-exchange hexagons, at most \(n\) local star triangles at prescribed vertex orbits, and possibly a single fixed antipodal geodesic turn cycle.

*Proof.* By (22), the charge of \(T_0\) is \((1,0)\) and the charge of \(T_i\) is \((1,[e_i])\). The \(n-1\) unit-vector classes \([e_1],\ldots,[e_{n-1}]\) are a basis of \(V_n=\mathbb F_2^n/\langle\mathbf1\rangle\). Consequently the \(n\) displayed star-triangle charges form a basis of \(\mathbb F_2\oplus V_n\). By the surjective charge criterion (20)--(21), they form a linear complement to \(\mathscr B_n\) in \(\ker\alpha\), proving (37). Each \(T_i+T_0\) has zero parity charge and vertex charge \([e_i]\), and the parity charge agrees with contact curvature on \(\ker\alpha\), proving (38). Finally \(\alpha(G)=1\), so \(G\) provides a one-dimensional complement to \(\ker\alpha\) in the full turn-cycle space, proving (39). \(\square\)

**Remark (binary versus geometric generation).** These direct sums are identities of binary cycle spaces. They do not assert that every simple cycle can be transformed to a geodesic through a sequence of individually simple, cost-nonincreasing pivots. Indeed the earlier star-triangle confluence and adjacent-swap plateau counterexamples show that geometric legality and integer turn costs contain information lost in (39). Nevertheless (39) supplies a finite, structurally prescribed generating system for the matroid's cocycle duality and separates the \(n\) resource-charge degrees of freedom from all the locally balanced hexagon exchanges.

**Theorem 10 (minimal parity test for antipodal turn signatures).** Fix \(n\ge5\). Choose star triangles \(T_0\) at \([0]\), and \(T_i\) at \([e_i]\) for \(1\le i<n\), using any fixed triple of distinct incident directions. A binary cochain \(d:E(H_n)\to\mathbb F_2\) is induced by an antipodally odd coloring of cube edges if and only if
\[
\boxed{d(C)=1\ \text{for every full antipodal-geodesic turn cycle }C,
\qquad d(T_i)=0\ (0\le i<n).}\tag{40}
\]
At least \(n\) independent additional linear parity tests are needed if all geodesic parity tests are given.

*Proof.* The direct-sum cycle-space decomposition (39) says that all geodesic turn cycles and these \(n\) star triangles together span \(Z_1(H_n)\). The monodromy cochain \(a\) evaluates to one on each geodesic and zero on every star triangle. Conditions (40) therefore mean that \(d+a\) annihilates the entire graph cycle space, hence is a graph cut \(\delta f\). The affine class \(a+B^1(H_n)\) is the class of turn signatures of antipodally odd cube-edge colorings. The span of all geodesic turn cycles alone has codimension \(n\) in \(Z_1(H_n)\) by Theorem 1; therefore fewer than \(n\) independent supplementary tests cannot suffice. \(\square\)

**Theorem 11 (classification of all geodesic-parity counterfeit signatures).** Let
\[
\mathcal A_n=\left\{f(x)=a_0+\sum_{i=1}^n a_ix_i:\sum_i a_i=0\right\},
\]
and define the previously constructed cochain
\[
\omega_f(t_{ij}([x]))=
a_0+\left(\sum_k a_kx_k\right)(1+x_i+x_j).
\tag{41}
\]
Put \(\eta_f=\omega_f+(n\bmod2)a_0a\), where \(a\) is the monodromy cochain. Then all binary turn cochains passing every full-geodesic parity test are precisely
\[
\boxed{\mathcal P_n=
\{a+\eta_f+\delta g:
f\in\mathcal A_n,\ g:V(H_n)\to\mathbb F_2\}.}
\tag{42}
\]
The affine function \(f\) is unique, the vertex function \(g\) is unique modulo constants, and admissible turn signatures correspond to \(f=0\).

*Proof.* By (23), every full-geodesic cycle \(C\) has parity charge \(\sigma(C)=n\bmod2\) and affine vertex charge \(\xi(C)=0\). Equation (24) therefore gives \(\omega_f(C)=(n\bmod2)a_0\), and the correction in \(\eta_f\) makes \(\eta_f(C)=0\). Each \(a+\eta_f+\delta g\) consequently passes all geodesic parity tests.

On any star triangle centered at \([x]\), equations (14) and monodromy-zero give \((a+\eta_f)(T)=f(x)\). The \(n\) values \(f(0),f(e_1),\ldots,f(e_{n-1})\) determine the antipodally invariant affine function \(f\). For any \(d\) passing the geodesic tests, select \(f\) with these same star values. Then \(d-a-\eta_f\) vanishes on all geodesics and on the chosen \(n\) star triangles, hence is a cut by Theorem 10. This proves (42). Uniqueness of \(f\) follows from its star values, and uniqueness of \(g\) modulo constants follows from connectedness of \(H_n\). \(\square\)

**Consequence.** The \(n\) extra binary degrees of freedom invisible to the full family of geodesic parity tests are completely parametrized by affine antipodally invariant Boolean functions. Every nonzero such function generates a parity counterfeit, detected by one of the specified local star triangles. This is a linear certification theorem, not a bound on the integer number of switches of admissible colorings.

**Theorem 12 (two-star homological repair of every antipodal cycle).** Fix \(n\ge5\), a reference full antipodal-geodesic turn cycle \(G\), and a fixed triple of distinct directions \(a,b,c\). At each folded vertex orbit \([x]\), let \(T_{[x]}=T_{[x];a,b,c}\) be its local star triangle. For any binary turn cycle \(C\) with \(\alpha(C)=1\), put
\[
(\varepsilon,v)=(\sigma(C)+n\bmod2,\ \xi(C))
\in\mathbb F_2\oplus V_n,\quad
V_n=\mathbb F_2^n/\langle\mathbf1\rangle.
\tag{46}
\]
Choose any representative \(x\) of the vertex-orbit vector \(v=[x]\). Then
\[
\boxed{
\begin{cases}
C+G\in\mathscr B_n,&(\varepsilon,v)=(0,0),\\
C+G+T_{[x]}\in\mathscr B_n,&\varepsilon=1,\\
C+G+T_{[x]}+T_{[0]}\in\mathscr B_n,&\varepsilon=0.
\end{cases}}
\tag{47}
\]
In the last case \(v=0\) reduces to the first case, since \(T_{[x]}=T_{[0]}\). Thus **at most two** local star-triangle additions suffice to put *every* odd-monodromy turn cycle into the binary geodesic-exchange class of \(G\). The count cannot in general be reduced to one when \(\varepsilon=0\) and \(v\ne0\), since every single star triangle has odd parity charge.

*Proof.* Both \(C,G\) have monodromy one, so \(Z=C+G\in\ker\alpha\). Theorem 3 gives \((\sigma(Z),\xi(Z))=(\varepsilon,v)\). By (22), the star triangle at \([x]\) has charge \((1,[x])=(1,v)\), while the star triangle at \([0]\) has charge \((1,0)\). When \(\varepsilon=1\), adding \(T_{[x]}\) annihilates both charges. When \(\varepsilon=0\), adding \(T_{[x]}+T_{[0]}\) likewise annihilates both charges. The complete charge criterion (20) says the resulting balanced cycle lies in \(\mathscr B_n\), proving (47). A single star has parity charge one, so it cannot eliminate a nonzero charge of the form \((0,v)\). \(\square\)

**Corollary 13 (resource-defect repair needs at most two formal stars).** For a stationary-free antipodal walk \(C\) with resource traversal multiplicities \(m_i=1+2u_i\), equation (29) gives \(\varepsilon=0\) and \(v=[u_1,\ldots,u_n]\). In this case
\[
\boxed{
C+G+T_{[u]}+T_{[0]}\in\mathscr B_n,\qquad
[u]=\left[\sum_i u_i e_i\right].
}
\tag{48}
\]
If \(v\ne0\), two stars are necessary for such an identity, regardless of the number of repeated directions. For an odd-monodromy turn cycle with an odd number of stationary contacts, the repair uses a single star triangle at the site prescribed by \(\xi(C)\).

**Geometric and quantitative limitation.** Theorem 12 is an identity in the binary cycle space, not a sequence of legal transformations through simple odd-monodromy cycles. The selected star triangles need not meet the input cycle in a location allowing a pivot, and a representation in \(\mathscr B_n\) as a sum of exchange hexagons need not admit cost-nonincreasing simple-cycle swaps. This separates the now-bounded **linear resource charge** from the unresolved **nonlinear accessibility and color cost**. A possible closure principle would strengthen (47) into an admissible splicing theorem with at most two nonlocal star insertions and controlled integer intersection cost. Such a strengthening is conjectural and not implied by the homology theorem.

Let \(n\ge5\), \(F_n=Q_n/\langle\tau\rangle\), and \(H_n=L(F_n)\). Index the turn edges of \(H_n\) by \(t_{ij}([x])\), where \([x]\in\mathbb F_2^n/\langle\mathbf1\rangle\) is the antipodal orbit of a cube vertex and \(\{i,j\}\) is an unordered pair of distinct directions. Let \(\mathcal G_n\) be the family of length-\(n\) odd-monodromy turn cycles (full antipodal geodesics), each represented by its unsigned \(0/1\) incidence vector \(g_C\in\mathbb Z^{E(H_n)}\). Define the integral geodesic incidence lattice
\[
\Lambda_n=\operatorname{span}_{\mathbb Z}\{g_C:C\in\mathcal G_n\}
\subseteq\mathbb Z^{E(H_n)}.
\tag{1}
\]

**Theorem 1 (Fourier decomposition of all zero-sum turn weights).** Let \(\mathbb K\) be a field of characteristic different from two. A turn weighting \(z:E(H_n)\to\mathbb K\) satisfies
\[
\sum_{t\in C}z(t)=0\qquad\text{for every }C\in\mathcal G_n
\tag{2}
\]
if and only if it has a unique Fourier decomposition
\[
\boxed{z(t_{ij}([x]))=
\sum_{\substack{S\subseteq[n]\\|S|\equiv0\ (2)}}
(-1)^{\sum_{r\in S}x_r}\bigl(b_{i,S}+b_{j,S}\bigr),}
\tag{3}
\]
where the coefficients \(b_{i,S}\in\mathbb K\) satisfy
\[
\boxed{
\begin{cases}
\sum_{i=1}^n b_{i,\varnothing}=0,&S=\varnothing,\\
b_{i,S}=0\text{ for }i\notin S,&S\ne\varnothing.
\end{cases}}
\tag{4}
\]
(The coefficient representation is unique, not merely the resulting weighting.) In particular the space of such zero-sum weightings has dimension
\[
\boxed{\dim_{\mathbb K}\ker\mathcal I_n=
(n-1)+\sum_{\substack{S\ne\varnothing\\|S|\ {\rm even}}}|S|
=n2^{n-2}+n-1,}
\tag{5}
\]
where \(\mathcal I_n\) denotes the matrix with rows \(g_C\).

*Proof.* The group \(V_n=\mathbb F_2^n/\langle\mathbf1\rangle\) of folded cube translations acts regularly on the folded vertex orbits, and its character group consists of \(\chi_S([x])=(-1)^{\sum_{r\in S}x_r}\), indexed by even-cardinality \(S\). Since the characteristic is odd, Fourier inversion holds in \(\mathbb K[V_n]\). Every turn weighting therefore has a unique expansion
\[
z(t_{ij}([x]))=\sum_{S\ {\rm even}}\chi_S([x])a_{ij,S},
\tag{6}
\]
with symmetric pair coefficients \(a_{ij,S}=a_{ji,S}\). A geodesic rooted at \(x\), with direction order \(\pi=(\pi_1,\ldots,\pi_n)\), evaluates the \(S\)-mode as
\[
\chi_S([x])F_S(\pi),\qquad
F_S(\pi)=\sum_{t=1}^n
\varepsilon_t\,a_{\pi_t\pi_{t+1},S},\qquad
\varepsilon_t=\prod_{r=1}^t s_{\pi_r},
\tag{7}
\]
where \(\pi_{n+1}=\pi_1\) and \(s_i=-1\) if \(i\in S\), \(s_i=1\) otherwise. Since \(|S|\) is even, the closing turn is also correctly represented by (7). Varying \(x\) separates all Fourier modes; hence (2) holds if and only if \(F_S(\pi)=0\) for every even \(S\) and every permutation \(\pi\).

Fix an even \(S\), omit the subscript \(S\), and suppose \(F_S(\pi)=0\) for all \(\pi\). Compare two permutations with the same prefix and suffix but consecutive four-direction blocks \((h,i,j,k)\) and \((h,j,i,k)\). The three terms around the swap give
\[
\boxed{
(a_{hi}-a_{hj})+(s_i-s_j)a_{ij}
+s_is_j(a_{jk}-a_{ik})=0
}
\tag{8}
\]
for any four pairwise distinct directions. For fixed \(i,j\) put \(d_h=a_{hi}-a_{hj}\), for \(h\notin\{i,j\}\). Equation (8) becomes
\[
d_h-s_is_jd_k=-(s_i-s_j)a_{ij}
\qquad(h,k\notin\{i,j\},\ h\ne k).
\tag{9}
\]
If \(s_i=s_j\), then \(d_h=d_k\). If \(s_i\ne s_j\), then \(d_h+d_k\) is independent of \(h,k\). Because \(n\ge5\) leaves at least three eligible values of \(h\), the latter equations again force all \(d_h\) to agree. We have proved that for every pair \(i,j\), the difference \(a_{hi}-a_{hj}\) does not depend on \(h\) outside that pair.

The elementary additive complete-graph lemma now applies: over any field of characteristic different from two, these column-difference conditions imply
\[
\boxed{a_{ij}=b_i+b_j}
\tag{10}
\]
for a unique vector \(b\in\mathbb K^n\). One way to construct \(b\) is to solve \(b_1+b_2=a_{12}\), \(b_1+b_3=a_{13}\), \(b_2+b_3=a_{23}\), and use all the difference conditions to extend to every other vertex; uniqueness follows since \(b_i+b_j=0\) for all \(i\ne j\) forces every \(b_i=0\) when two is invertible.

If \(S\) is nonempty and proper, choose \(i\in S,j\notin S\). With \(s_i=-1,s_j=1\), substituting (10) into (9) gives
\[
2(b_i-b_j)=2(b_i+b_j),
\]
so \(b_j=0\). Every \(j\notin S\) can be paired with some \(i\in S\), proving the support condition in (4). If \(S=[n]\) (possible only for even \(n\)), the support condition is automatic. Conversely, for any nonempty even \(S\) and any \(b\) supported on \(S\), the cyclic sum in (7), with (10), groups by vertex as
\[
F_S(\pi)=\sum_{t=1}^n
(\varepsilon_{t-1}+\varepsilon_t)b_{\pi_t},
\qquad \varepsilon_0=\varepsilon_n.
\tag{11}
\]
Each term with \(\pi_t\in S\) vanishes because \(\varepsilon_t=-\varepsilon_{t-1}\), while every \(b_{\pi_t}\) with \(\pi_t\notin S\) is zero. Thus these \(b\) are all solutions, giving a kernel of dimension \(|S|\).

For \(S=\varnothing\), the same swap calculation gives (10), but \(F_\varnothing(\pi)=2\sum_i b_i\). Since two is invertible, the condition is \(\sum_i b_i=0\), a space of dimension \(n-1\). These classifications prove (3)--(4). Finally each coordinate \(i\) belongs to \(2^{n-2}\) even subsets, yielding \(\sum_{S\ {\rm even}}|S|=n2^{n-2}\), proving (5). \(\square\)

**Theorem 2 (field-independent geodesic-incidence rank).** For every field \(\mathbb K\), including characteristic two,
\[
\boxed{
\operatorname{rank}_{\mathbb K}\mathcal I_n
=
|E(H_n)|-|V(H_n)|-n+1
=
n(n-2)2^{n-2}-n+1.
}
\tag{12}
\]

*Proof.* For fields of odd characteristic, (5) and \(|E(H_n)|=\binom n2 2^{n-1}\), \(|V(H_n)|=n2^{n-2}\), give the displayed rank by rank-nullity. In characteristic two, the geodesic incidence-row span is \(\mathscr B_n+\langle G\rangle\), where \(\mathscr B_n\) is the binary geodesic-exchange hexagon span and \(G\) is one reference geodesic cycle. Theorem 1 of the preceding geodesic-exchange homology Subsection established
\(\dim_{\mathbb F_2}\mathscr B_n=|E(H_n)|-|V(H_n)|-n\); the reference geodesic lies outside that span because it has monodromy one whereas \(\mathscr B_n\subseteq\ker\alpha\). Thus the binary rank is the same. \(\square\)

**Corollary 3 (saturated integral geodesic lattice).** The lattice \(\Lambda_n\) in (1) is a saturated sublattice of \(\mathbb Z^{E(H_n)}\). Equivalently
\[
\boxed{\mathbb Z^{E(H_n)}/\Lambda_n
\quad\text{has no nonzero torsion}.}
\tag{13}
\]
Every integral turn vector lying in the rational span of the unsigned antipodal-geodesic incidence vectors is therefore an integral linear combination of those incidence vectors.

*Proof.* Apply Smith normal form to the integer matrix \(\mathcal I_n\). Let its nonzero diagonal invariant factors be \(d_1,\ldots,d_r>0\), with \(r\) the rational rank in (12). If a prime \(\ell\) divided any \(d_i\), reduction modulo \(\ell\) would lower the matrix rank below \(r\). But Theorem 2 gives rank \(r\) in every prime characteristic. Hence all nonzero Smith invariant factors equal one, giving (13). \(\square\)

**Corollary 4 (real-valued geodesic weight rigidity).** The Fourier expression (3)--(4) classifies every real turn weighting that has zero integer sum on all full antipodal geodesics. A weighting with constant sum \(K\) on all such geodesics is obtained by adding the uniform weighting \(K/n\) to one of the zero-sum weightings in Theorem 1. This remains a linear statement: restricting the turn weights to \(0/1\) values and imposing the star-triangle parity constraints is a nonlinear restriction not settled by the Fourier classification.

**Remark (the low-dimensional boundary).** The use of at least three auxiliary directions in (9) requires \(n\ge5\). The \(n=4\) incidence rank differs from the formula (12), as recorded in the earlier small-order rank audit. For \(n\ge5\), the present theorem provides an integral strengthening of the binary exchange-homology dimension theorem: no torsion obstruction arises when passing from binary geodesic incidence to the integral lattice of unsigned incidences. It does not imply a small positive integer intersection for every admissible binary coloring, since saturation controls additive relations, not the positivity needed for low-cost cocircuit selection.

**Theorem 5 (coordinate-potential normal form).** Over any field of characteristic different from two, a turn cochain \(z\) vanishes in sum on every full antipodal-geodesic turn cycle if and only if there exist unique functions
\[
\phi_i:V(F_n)\to\mathbb K,\quad 1\le i\le n,
\tag{14}
\]
and unique constants \(b_i\in\mathbb K\) such that
\[
\boxed{
z(t_{ij}([x]))=\phi_i([x])+\phi_j([x]),\quad
\phi_i([x])+\phi_i([x^i])=2b_i,\quad
\sum_i b_i=0.
}
\tag{15}
\]
For a weighting whose sum on every full antipodal geodesic is a fixed \(K\), the same formula holds with \(\sum_i b_i=K/2\).

*Proof.* In the Fourier decomposition (3)--(4), define
\[
\phi_i([x])=b_{i,\varnothing}+
\sum_{\substack{S\ne\varnothing,\ S\ {\rm even}\\i\in S}}
\chi_S([x])b_{i,S}.
\tag{16}
\]
Each nonconstant Fourier character appearing in \(\phi_i\) changes sign when coordinate \(i\) is flipped, giving the middle identity in (15); the turn representation (3) gives the first identity, and the trivial Fourier mode gives the final identity. Conversely any function satisfying the middle identity has its nonconstant Fourier coefficients supported on even subsets containing \(i\); the trivial coefficient is \(b_i\). Therefore it has the form (16), and Theorem 1 supplies the zero-sum condition. Uniqueness of the functions \(\phi_i\) follows pointwise from the complete-graph pair equations \(z_{ij}=\phi_i+\phi_j\) because two is invertible and there are at least three directions. For the constant-sum version, subtract the uniform turn cochain \(K/n\) over \(\mathbb R\), or directly telescope as below (the formula \(\sum_i b_i=K/2\) is valid over any field of odd characteristic without dividing by \(n\)).

Indeed, on a geodesic with direction order \(\pi\), the two turns adjacent to the edge in direction \(i=\pi_t\) contribute \(\phi_i([v_{t-1}])+\phi_i([v_t])=2b_i\), where \(v_t=v_{t-1}+e_i\). Every direction occurs once, so the total cyclic turn weight is \(2\sum_i b_i\), proving both necessity and sufficiency of the prescribed sum. \(\square\)

**Corollary 6 (alternate analytic proof of flat-spectrum rigidity).** Suppose \(d\) is the \(0/1\) turn signature of an antipodally odd cube-edge coloring and has the same cyclic turn weight \(K\) on every full antipodal geodesic, with \(n\ge5\). Then \(K=1\).

*Proof.* Theorem 5 supplies a representation \(d(t_{ij}([x]))=\phi_i([x])+\phi_j([x])\). At each folded vertex \([x]\), the turns encode pairwise disagreements between its \(n\) incident cube-edge colors. If at least two incident colors are zero and at least two are one, choose indices \(i,j\) of color zero and \(k,\ell\) of color one. Their turn weights give
\[
d_{ij}+d_{k\ell}-d_{ik}-d_{j\ell}=0+0-1-1=-2,
\]
whereas the same four-term expression in pair potentials \(\phi_i+\phi_j\) is zero. This is a contradiction over the reals. Therefore every cube vertex has at most one incident edge of minority color.

The number of disagreeing turns at each folded vertex is consequently at most \(n-1\). The standard uniform geodesic-turn incidence design yields
\[
K=\mathbb E_C w_d(C)
=\frac{n|\operatorname{supp}(d)|}{|E(H_n)|}
\le\frac{n(n-1)}{\binom n2}=2.
\]
By covering monodromy, every geodesic turn weight is a positive odd integer. Hence the constant \(K\) is one. \(\square\)

The coordinate-potential representation provides an analytic converse to the discrete pairwise-turn viewpoint: zero-sum geodesic weights are precisely the discrete normal potentials whose variable parts reverse across the associated coordinate edges. It may be useful for quantitative stability, although the theorem does not establish an unrestricted two-switch bound.

## Matroid Generalizations and Short-Port Intersection Conjectures

Let \(M\) be a finite binary matroid and let \(p\in E(M)\) belong to a circuit and a cocircuit. Define the **port cogirth**
\[
g_p(M)=\min\{|Y|:Y\in\mathcal C^*(M),\ p\in Y\},
\]
where \(Z(M)\) denotes the binary cycle space. For an even positive integer \(b\), define the **short-port intersection property** \(P_b(M,p)\) by
\[
\boxed{\forall X\in Z(M)\ (p\in X),\quad
\exists Y\in\mathcal C^*(M):
p\in Y,\ |Y|=g_p(M),\ |X\cap Y|\le b.}\tag{1}
\]
Cycle–cocircuit orthogonality over \(\mathbb F_2\) forces every intersection in (1) to have positive even cardinality.

In Article XI's pointed dual \(D_n\), shortest port cocircuits are the cyclic turn encodings of antipodal geodesics, and every port-containing binary cycle encodes an antipodally odd cube-edge coloring. Thus \(P_4(D_n,p)\) is equivalent to the unrestricted two-switch conjecture, while \(P_2(D_n,p)\) is equivalent to monochromatic NORI1.

**Proposition 1 (small port cogirth).** Every pointed binary matroid with \(g_p(M)\le5\) has \(P_4\). Every pointed binary matroid with \(g_p(M)\le3\) has \(P_2\).

*Proof.* Fix any shortest port cocircuit \(Y\). For every binary cycle \(X\ni p\), the intersection \(X\cap Y\) is nonempty, even, and of size at most \(g_p(M)\). The asserted bounds follow. \(\square\)

**Theorem 2 (port-cogirth-preserving contraction inheritance).** Let \(T\subseteq E(M)\setminus\{p\}\), put \(M_0=M/T\), and assume
\[
g_p(M)=g_p(M_0).\tag{2}
\]
For any positive even \(b\), if \(P_b(M_0,p)\) holds, then \(P_b(M,p)\) holds.

*Proof.* Write \(S=E(M)\setminus T\). Take any binary cycle \(X\in Z(M)\) with \(p\in X\). The restriction \(X_0=X\cap S\) is a binary cycle of \(M/T\), and \(p\in X_0\). Choose by \(P_b(M_0,p)\) a cocircuit \(Y\ni p\) of \(M_0\) satisfying \(|Y|=g_p(M_0)\) and \(|X_0\cap Y|\le b\). Cocircuits of \(M/T\) are precisely the cocircuits of \(M\) disjoint from \(T\). Hence \(Y\) is a cocircuit of \(M\), and (2) makes it shortest among those containing \(p\). Finally \(Y\subseteq S\) gives
\[
|X\cap Y|=|X_0\cap Y|\le b.
\]
\(\square\)

**Corollary 3 (cubical contraction class).** Suppose a pointed binary matroid \(M\) has a contraction \(M/T\cong D_n\), with \(p\notin T\), and \(g_p(M)=n+1\). Then \(P_b(D_n,p)\) implies \(P_b(M,p)\). For \(b=2,4\), the universal \(P_b\) assertion over all such matroids and all \(n\ge3\) is equivalent to the respective cube conjecture, since the class includes \(M=D_n\) with \(T=\varnothing\).

The theorem applies without restrictions on the number of elements, representational rank, or other circuits of \(M\). The port cogirth equality is essential to lifting a *minimum-size* cocircuit from the contraction.

Let \((N,t)\) be a simple binary matroid represented by pairwise distinct nonzero vectors \(S\cup\{t\}\subseteq V=\mathbb F_2^r\), with \(t\) in the span of \(S\). Let
\[
q=\min\{|C|:C\text{ a circuit of }N,\ t\in C\}\ge4,
\qquad \ell=q-1.
\tag{1}
\]
Define \(K=\operatorname{Cay}(V,S)\), the graph with edges \(\{x,x+s\}\) for \(x\in V,s\in S\), and let \(\tau(x)=x+t\). Since \(t\notin S\) and \(t\) is not the sum of two distinct members of \(S\), \(\tau\) acts freely on edges and the quotient \(G=K/\langle\tau\rangle\) is a simple connected graph. Put \(H=L(G)\), and let \(B_H\) denote its binary vertex-edge incidence matrix. The two-sheeted cover \(L(K)\to H\) has a monodromy class represented by an edge cochain \(a\in\mathbb F_2^{E(H)}\). Adjoin a port column \(p\) and define the pointed binary matroid
\[
\boxed{\mathfrak D(N,t)
= M\!\left(\begin{array}{c|c}B_H&0\\a&1\end{array}\right)^*.}
\tag{2}
\]
Changing the cochain representing monodromy adds a cut to \(a\), inducing an elementary row operation in (2). Binary representations of a fixed binary matroid are equivalent under invertible linear changes of coordinates, which induce Cayley-graph isomorphisms. Thus the pointed isomorphism type in (2) depends only on \((N,t)\).

**Theorem 1 (invariant cube core and port cogirth).** The port cogirth of \(\mathfrak D(N,t)\) is \(q\). Moreover, there exists a contraction
\[
\boxed{\mathfrak D(N,t)/T\cong D_\ell,\qquad
g_p(\mathfrak D(N,t))=g_p(D_\ell)=\ell+1=q,}
\tag{3}
\]
where \(D_\ell\) is the pointed dual associated with antipodally odd edge colorings of \(Q_\ell\).

*Proof.* Choose a shortest circuit \(C\ni t\) of \(N\), and put \(A=C\setminus\{t\}\). The \(\ell\) vectors of \(A\) are linearly independent, with sum \(t\). For any \(x\in V\), the edges of \(K\) in directions \(A\) on \(x+\operatorname{span}(A)\) form a cube \(Q_\ell\) invariant under \(\tau\). This cube is induced in \(K\). Indeed, if \(s\in S\setminus A\) were in \(\operatorname{span}(A)\), simplicity would give \(s=\sum_{a\in W}a\) for some \(W\subseteq A\) with \(|W|\ge2\); then
\[
t=s+\sum_{a\in A\setminus W}a
\]
would express \(t\) using \(\ell-|W|+1<\ell\) generators, contradicting (1). Hence its quotient is an induced folded cube inside \(G\), and the associated line graph \(H_\ell\) is an induced subgraph of \(H\). Restrict the matrix preceding dualization in (2) to its turn edges together with \(p\). After deleting zero incidence rows, the restriction is row-equivalent to the pointed matrix defining \(D_\ell^*\), because the restricted covering-monodromy class is that of the antipodal cube covering. Duality exchanges deletion before dualization with contraction afterward. This gives the contraction in (3).

A cocircuit of \(\mathfrak D(N,t)\) containing \(p\) is a circuit of the matrix preceding dualization that contains \(p\). Its deletion of \(p\) is a simple cycle \(C_H\) of \(H\) with odd covering monodromy. Lift the cyclic sequence of line-graph vertices to edges of \(K\) ending at the translate by \(t\) of the first edge. Their successive contact vertices determine a walk in \(K\) from some \(u\) to \(u+t\), using at most \(|C_H|\) generator steps. Every such walk uses at least \(\ell\) steps, since a shortest generator expression for \(t\) has length \(\ell\) by (1). Thus \(|C_H|\ge\ell\). Conversely, a path in the invariant cube using each generator of \(A\) once joins \(u\) to \(u+t\), and cyclic completion of its turn sequence gives an odd-monodromy cycle of \(H\) with length \(\ell\). Therefore the shortest port cocircuit has size \(\ell+1=q\). \(\square\)

**Conjecture 2 (binary-generator short-port intersection).** Every simple pointed binary matroid \((N,t)\) satisfying (1) has
\[
\boxed{P_4(\mathfrak D(N,t),p):\quad
\forall X\in Z(\mathfrak D(N,t)),\ p\in X,\quad
\exists Y\in\mathcal C^*(\mathfrak D(N,t)):
p\in Y,\ |Y|=q,\ |X\cap Y|\le4.}
\tag{4}
\]
The strengthened conjecture \(P_2\) replaces the intersection bound four by two.

**Corollary 3 (equivalence of the generalized conjecture and NORI1).** Conjecture 2 for all \((N,t)\) is equivalent to the unrestricted two-switch edge-coloring conjecture for hypercubes. The \(P_2\) version is equivalent to the unrestricted monochromatic-geodesic conjecture.

*Proof.* By Theorem 1 and the port-cogirth-preserving contraction theorem of the preceding Subsection, the corresponding cube assertion for every dimension \(\ell\ge3\) implies (4) for every \((N,t)\). Conversely, choose \(N=U_{\ell,\ell+1}\), the binary uniform matroid of rank \(\ell\) with one additional element \(t\) equal to the sum of the \(\ell\) basis elements. The Cayley graph is then \(Q_\ell\) and \(\mathfrak D(N,t)=D_\ell\). Applying (4) gives the original assertion in every dimension. The same reasoning applies to \(P_2\). \(\square\)

For a non-cubical instance take \(V=\mathbb F_2^6\) and
\[
S=\{e_1,\ldots,e_6,\ e_1+e_2+e_6\},\qquad
t=e_1+e_2+e_3+e_4+e_5.
\]
There are two shortest five-generator expressions for \(t\), using respectively \(\{e_1,\ldots,e_5\}\) and \(\{e_3,e_4,e_5,e_6,e_1+e_2+e_6\}\). Thus \(\mathfrak D(N,t)\) has distinct invariant-cube cores. The graph \(K\) has 64 vertices of degree seven; \(G\) has 32 vertices and 112 edges; \(H\) has 112 vertices and 672 turns. Consequently \(\mathfrak D(N,t)\) has 673 elements, rank 561, and port cogirth six, while its cogirth-preserving cubical contraction \(D_5\) has 161 elements and rank 121.

This construction gives a matroidal generalization with arbitrary binary dependencies among the generators. The equivalence in Corollary 3 also identifies its current limitation: the sufficient contraction hypothesis already contains the cube's central difficulty. A broader intrinsic characterization that dispenses with cubical contraction, or one that also encodes ordinary reversal-odd boundary tournaments with the same witness principle, remains open.

Let \(n\ge4\) and let \(b(u,v,w)\in\mathbb F_2\), for distinct \(u,v,w\in[n]\), satisfy \(b(w,v,u)=1+b(u,v,w)\). All binary additions below are modulo two, but switch weights are integer sums.

**Theorem 1 (boundary-tournament double cover).** Let \(S_n\) be the undirected graph on ordered pairs \((u,v)\), \(u\ne v\), with an edge between \((u,v)\) and \((v,w)\) whenever \(u,v,w\) are distinct. The involution \(\rho(u,v)=(v,u)\) acts freely on its vertices and edges. There is a connected regular two-sheeted covering
\[
\boxed{S_n\longrightarrow F_n=L(K_n),\qquad (u,v)\mapsto\{u,v\},}
\tag{1}
\]
and
\[
\boxed{H_n^{\mathrm{BT}}=L(S_n)/\langle\rho\rangle\cong L^2(K_n).}
\tag{2}
\]
The boundary tournament \(b\) amounts to an antipodally odd coloring \(c_b\) of the *edges* of \(S_n\): the edge \((u,v)(v,w)\) receives color \(b(u,v,w)\), and
\[
c_b(\rho e)=1+c_b(e).\tag{3}
\]
Furthermore
\[
|V(S_n)|=n(n-1),\quad |E(S_n)|=n(n-1)(n-2),\quad
|E(F_n)|=n\binom{n-1}{2}.\tag{4}
\]

*Proof.* Each undirected edge of \(S_n\) has a unique natural orientation \((u,v)\to(v,w)\). Applying \(\rho\) to this edge produces the edge naturally oriented \((w,v)\to(v,u)\), so (3) is precisely the reversal-oddness of \(b\). Above the vertex \(\{u,v\}\) of \(L(K_n)\) lie two states \((u,v)\) and \((v,u)\). At either state, the neighbors project bijectively to all edges of \(K_n\) incident to \(\{u,v\}\); thus (1) is a regular covering. For four distinct \(u,v,w,z\), the walk
\[
(u,v),(v,w),(z,v),(v,u)
\]
joins the states of a fiber. As \(L(K_n)\) is connected, the cover is connected. Line graphs preserve this covering and its deck quotient, proving (2). Ordered-pair and ordered-triple counting gives (4). \(\square\)

**Theorem 2 (shared pointed binary lift).** For any connected regular two-sheeted graph cover \(\widetilde F\to F\) with deck involution \(\rho\), let \(H=L(F)=L(\widetilde F)/\rho\). Color the edges of \(\widetilde F\) by a function \(c\) with \(c(\rho e)=1+c(e)\). For incident cover edges \(e,f\), define the projected turn cochain
\[
d([\{e,f\}])=c(e)+c(f).\tag{5}
\]
If \(\alpha\) is the covering monodromy on the binary cycle space of \(H\), then the cochains arising in this way comprise the affine coset
\[
\boxed{d\in a+B^1(H;\mathbb F_2),\quad d(C)=\alpha(C)
\text{ for every binary cycle }C,}\tag{6}
\]
where \(a\) represents \(\alpha\). The coloring is reconstructed from \(d\) up to global color complementation. With \(B_H\) the binary incidence matrix, define the pointed binary matroid
\[
\boxed{D(F,\rho)=
M\left(\begin{array}{c|c}B_H&0\\a&1\end{array}\right)^*,}\tag{7}
\]
with distinguished element \(p\). Its binary cycles through \(p\) are \(X_d=\operatorname{supp}(d)\cup\{p\}\), while cocircuits through \(p\) are \(Y_C=C\cup\{p\}\) for odd-monodromy simple cycles \(C\) of \(H\). Their intersections satisfy
\[
|X_d\cap Y_C|=1+\sum_{e\in C}d(e)\equiv0\pmod2.\tag{8}
\]
In particular, boundary tournaments modulo global complementation correspond bijectively to the port-containing cycles of \(D_n^{\mathrm{BT}}=D(F_n,\rho)\), an affine space of dimension
\[
\boxed{n\binom{n-1}{2}-1.}\tag{9}
\]
Taking \(\widetilde F=Q_n\), \(F=Q_n/\langle\tau\rangle\), recovers the pointed cube matroid of Article XI.

*Proof.* Equation (5) is unchanged when both incident edges are acted upon by \(\rho\). A closed walk in \(H\) lifts to a turn walk in \(L(\widetilde F)\) whose final edge is either the initial edge or its deck image; telescoping the color differences gives \(d(C)=\alpha(C)\). Choose a reference odd coloring \(c_0\), selecting one cover edge from each deck pair. Its turn cochain \(a_0\) has these same cycle sums. Hence every admissible \(d\) differs from \(a_0\) by a coboundary \(\delta f\). Lifting \(f\) to a deck-invariant edge function on \(\widetilde F\) produces \(c=c_0+f\); connectedness shows that global complementation is the sole ambiguity. The dual cycle space in (7) is the row space of the displayed matrix. A minimal dependence containing the port comprises the port and one simple cycle on which \(a\) has odd sum. These observations yield (8). Connectedness gives the cut-space dimension \(|V(H)|-1=|E(F)|-1\), proving (9). \(\square\)

**Theorem 3 (the short-port decoding obstruction).** For \(n\ge4\), the port cogirth of \(D_n^{\mathrm{BT}}\) is four:
\[
\boxed{g_p(D_n^{\mathrm{BT}})=4.}\tag{10}
\]
Its shortest port cocircuits correspond to the three-edge stars \(\{va,vb,vc\}\) of the original complete graph \(K_n\), with \(a,b,c,v\) distinct. Consequently *every* port-containing cycle \(X\) and *every* shortest port cocircuit \(Y\) satisfy
\[
\boxed{|X\cap Y|\in\{2,4\}.}\tag{11}
\]
Thus a universal four-intersection theorem for this pointed matroid says nothing about long vertex-simple monochromatic tight paths.

*Proof.* The three-step cover walk
\[
(a,v),(v,b),(c,v),(v,a)=\rho(a,v)
\]
projects to a triangle in \(F_n=L(K_n)\), on vertices \(\{va,vb,vc\}\), with nontrivial monodromy. Its three consecutive cover edges project to a monodromy-one turn triangle in \(H=L(F_n)\), producing a port cocircuit of size four. There are no shorter simple cycles in \(H\), proving (10). Every graph triangle in a line graph \(L(F)\) is either a triangle of edges incident at one vertex of \(F\) (whose lifted turn monodromy is zero), or the three consecutive edges of a triangle of \(F\). Triangles of \(F_n=L(K_n)\) themselves come from either three edges incident at one vertex of \(K_n\), with monodromy one, or the three edges of a triangle of \(K_n\), with monodromy zero: the latter lifts to the closed directed state path \((a,b),(b,c),(c,a),(a,b)\). This classifies the shortest port cocircuits. Binary cycle--cocircuit orthogonality makes their intersections even; since both sets contain \(p\), such an intersection is either two or four. \(\square\)

**Corollary 4 (local tournaments and two-intersection).** The shortest port cocircuit arising from the star \(\{va,vb,vc\}\) has intersection two with \(X_{d_b}\) if the restriction of the middle-local tournament at \(v\) to \(\{a,b,c\}\) is transitive, and intersection four if it is a directed three-cycle. In particular, for every \(n\ge5\), all port-containing cycles \(X\) have a *shortest* port cocircuit \(Y\) with
\[
\boxed{|X\cap Y|=2.}\tag{12}
\]
For \(n=4\), taking every middle-local tournament to be cyclic produces a port cycle whose intersection with every shortest port cocircuit is four.

*Proof.* Order \(a<b<c\) and set \(x=b(a,v,b)\), \(y=b(b,v,c)\), \(z=b(a,v,c)\). The corresponding cyclic turn word lifts from three cover edges colored \(x,1-y,1-z\), and its integer cyclic switch weight is
\[
w=[x=y]+[y\ne z]+[z\ne x].
\]
This equals three precisely when \(x=y\ne z\), the cyclic tournament, and one otherwise. Its port intersection is \(w+1\). Every tournament on at least four vertices contains a transitive triangle: choose a vertex with at least two outneighbors or at least two inneighbors. The local tournament has \(n-1\ge4\) vertices when \(n\ge5\). The cyclic choices at \(n=4\) are permitted independently at each center. \(\square\)

**Theorem 5 (the missing auxiliary graphic matroid).** A vertex tuple \(P=(v_1,\ldots,v_m)\), \(m\ge3\), determines a naturally directed path in \(S_n\) through states
\[
s_i=(v_i,v_{i+1})\quad(1\le i<m),
\]
whose \(m-2\) edges \(e_i=s_i s_{i+1}\) are colored
\(b(v_i,v_{i+1},v_{i+2})\). Let \(t_i\) be the turn of \(H_n^{\mathrm{BT}}\) induced by \(e_i,e_{i+1}\). Then
\[
\boxed{d_b(t_i)=
b(v_i,v_{i+1},v_{i+2})+
b(v_{i+1},v_{i+2},v_{i+3}).}\tag{13}
\]
The tuple \(P\) is vertex-simple precisely when its projected state set
\[
\{\{v_i,v_{i+1}\}:1\le i<m\}
\tag{14}
\]
is independent in the *graphic matroid* \(M(K_n)\), provided the cover path follows the natural orientations of all \(S_n\)-edges. Consequently the maximum length of a positive tight path in \(b\) is the maximum size of a naturally directed \(S_n\)-path whose projected state labels form an independent set in \(M(K_n)\) and whose induced \(H_n^{\mathrm{BT}}\)-turn path has all turn labels zero.

*Proof.* Consecutive edges of the directed state path share the state \((v_{i+1},v_{i+2})\), proving (13). Its projected states are the consecutive edges of the original vertex walk in \(K_n\). A vertex-simple walk is a tree path and its edge set is graphic-independent. Conversely, a repeated original vertex in a nonbacktracking walk, as enforced by the state transitions, creates a closed subwalk of length at least three and hence a graphic cycle. Thus graphic independence is equivalent to vertex simplicity. An all-zero turn word makes all consecutive triple colors agree. If their common color is zero, reversal of the original tuple complements every triple color, yielding a positive tight path of the same length; therefore the maximum for positive words equals the maximum for arbitrary monochromatic words. \(\square\)

**Theorem 6 (shared short-cycle generation).** Let \(\widetilde F\to F\) be any regular connected two-cover, let \(H=L(F)\), and denote the monodromies by \(\beta\) on \(F\) and \(\alpha\) on \(H\). If \(T_H\) is the span of triangles inside vertex-star cliques of \(H\), then the incidence-subdivision turn map yields
\[
0\longrightarrow T_H\longrightarrow Z_1(H;\mathbb F_2)
\xrightarrow{\varphi}Z_1(F;\mathbb F_2)\longrightarrow0,
\qquad \alpha=\beta\circ\varphi.
\tag{15}
\]
In the boundary-tournament case, \(\ker\alpha\) is generated by (a) star triangles of \(H_n^{\mathrm{BT}}\), (b) turn triangles corresponding to three-edge triangles in \(K_n\), and (c) binary sums of two turn triangles corresponding to three-edge stars in \(K_n\). These generators have support cardinality at most six. In the cube case, the kernel is generated by star triangles and square turn cycles, as proved earlier in Article XI.

*Proof.* A turn between two \(F\)-edges incident at \(v\) maps to the sum of their two incident half-edges in the subdivision of \(F\). This gives a surjection of binary cycle spaces from \(H=L(F)\) onto \(F\). The kernel in each incident-edge clique is its graph cycle space, generated by triangles, proving (15). The covering monodromy tracks the lifted contact-vertex walk, so \(\alpha=\beta\circ\varphi\). Apply the same sequence to \(F_n=L(K_n)\). Its cycle space is generated by three-edge stars of \(K_n\) and three-edge triangles of \(K_n\), since the cycle space of \(K_n\) is triangle-generated. The first type has \(\beta=1\) and the second \(\beta=0\), by Theorem 3. Therefore \(\ker\beta\) is generated by the second type and binary sums of pairs of the first type. Lift these elements back through \(\varphi\), adding the star-triangle kernel \(T_H\), to obtain the asserted generators. The cube comparison follows from the previously established square-generation theorem. \(\square\)

**Research consequence.** Cube edge colorings and boundary tournaments share the same functorial pointed binary *line-graph cover lift*, the affine turn cohomology class, and bounded-support generators for its monodromy-zero cycles. But the boundary-tournament four-intersection property is automatic because its port cogirth is four. Long tight paths correspond instead to zero-turn paths satisfying coherent orientation and an independent-set condition in \(M(K_n)\). Accordingly, a common theorem strong enough to advance both problems needs the pointed matroid *decorated with a matroid-constrained path family*, rather than just its collection of shortest port cocircuits. This identifies a structural research direction; it does not assert the unresolved long-path or two-switch conjectures.

A connected two-sheeted cover of graphs induces a cover of their line graphs. Its monodromy cochain, together with a binary incidence matrix and one port column, defines a pointed binary lift matroid. Antisymmetric edge colorings upstairs correspond to port-containing binary cycles downstairs. The central witness problem is to find a resource-constrained path in the covering graph whose projected consecutive turns avoid the support of the selected cycle. The shared incidence representation is the pointed dual of the matrix (B 0; a 1), where B is the vertex-edge incidence matrix of the quotient line graph and a records covering monodromy. Every admissible signature is a+delta(f), and each port-containing binary cycle represents a deck-odd edge coloring up to global complement.

**Theorem (turn signature).** Let H=L(G) and B be its binary vertex-edge incidence matrix. Let a record monodromy of L(tilde G) over H. The pointed binary matroid D is dual to the matrix formed from B with a bottom row a and a new port column whose only nonzero entry is in that bottom row. An antisymmetric edge coloring c upstairs induces the turn signature d(ef)=c(e)+c(f) downstairs, and the corresponding port-containing cycle of D is support(d) together with the port. Every port-containing cycle arises from a cochain \(a+\delta f\). If a path \(P\) of \(\widetilde G\) has consecutive edges \(e_1,\ldots,e_m\) whose projected turns are distinct, denote their set by \(F(P)\). Then
\[
\boxed{\operatorname{sw}_c(P)=|F(P)\cap X_d|.}
\]
*Proof.* Color differences telescope along lifts of cycles of \(H\), giving the covering monodromy. This proves \(d\in a+B^1(H)\); lifting any such cochain constructs an odd coloring unique modulo complement. The port cycles are the row vectors \((a+\delta f,1)\) of the primal matrix. Each projected turn contributes one precisely when its successive edge colors differ. \(\square\)

**Cube instance.** The antipodal two-cover Q_n over its folded quotient gives the pointed dual D_n. Geodesics use every direction once, and zero intersection with the corresponding turn signature means the geodesic is monochromatic.

**Boundary-tournament instance.** Let G=L(K_V). Let S_V have ordered-pair vertices (u,v), with an edge from (u,v) to (v,w) for distinct u,v,w; retain those edges without directions. The map (u,v) to the unordered pair {u,v} is a regular two-cover S_V to L(K_V), with deck involution (u,v) to (v,u). Hence the quotient turn graph is L(L(K_V)). The edge (u,v)-(v,w) represents the ordered triple (u,v,w); its deck translate represents (w,v,u). A reversal-odd boundary tournament is therefore an antisymmetric edge coloring of this covering graph.

An injective word (v_1,...,v_k) of original vertices yields the forward path (v_1,v_2),(v_2,v_3),...,(v_{k-1},v_k) in S_V. Its successive edge colors are precisely the boundary labels b(v_i,v_{i+1},v_{i+2}), and the projected consecutive turns are pairwise distinct. Thus the same zero-intersection condition produces a monochromatic vertex-simple tight path, provided that the selected walk respects the forward-overlap rule and original-vertex injectivity. These conditions are not encoded by a cocircuit of the underlying pointed binary matroid.

**Resource-window extension.** A signed line-cover matroid may be decorated by a finite resource set R and ordered labels omega(e) on covering edges. Each label is a tuple of distinct resources, and omega(tau e) is its reversal. The admissible paths are those whose labels overlap as consecutive windows of a single injective resource word. This path language is not determined by the binary matroid.

**Common witness predicate.** For a marked path P, let F(P) be its projected turn set. Given an integer demand m, define U_m to mean: for every port-containing binary cycle X there exists a marked path P whose resource word has at least m distinct letters and for which F(P) is disjoint from X. Theorem 1 proves that U_m means existence of a monochromatic path using at least m resources.

**Permutation-complete window systems.** Fix n resources and a width k. A window system is called permutation-complete when every permutation of the resources is realized by a marked path (with an allowed starting root), reversing that permutation gives the deck-translated reversal of its edge sequence, and exchanging adjacent resources changes at most k+1 consecutive edge states. The cube is a width-one system, with edge labels equal to coordinate directions. The boundary ordered-pair graph is a width-three system, with edge labels equal to ordered triples of original vertices.

**Conjecture.** Homogeneous complete resource-window covers have the zero-intersection selector property at full resource length for width one and at a positive linear fraction of the resource count for width three, under the further condition that the ordered triple determines its covering edge. Here homogeneous means that the full permutation group on the resources acts through automorphisms of the graph covering, compatibly with the window labels, and that the group acts transitively on feasible directed local turns. The preceding conjecture is an unproved candidate for this more restrictive class; its validity on arbitrary intermediate covers has not been established. In particular, the acting automorphism group may have a root-moving kernel: it must project onto the resource symmetric group and act transitively on local turns, but the resource subgroup alone need not be transitive. Cube translations provide the kernel.

### Polarized matroid basis exchanges, twisted resource galleries, and the unified conjecture

This Subsection strengthens the common signed-cover representation already established in Article XI. Both NORI1 and ordinary reversal-odd boundary 3-tournaments admit the same *kind* of pointed binary matroid, but the boundary model requires a distinguished family of **long, resource-simple, alternating-port cocircuits**, not just shortest port cocircuits. We give axioms, canonical embeddings, a twisted-closing theorem, a seam-weight theorem, a quantitative conjecture, and reproducible finite obstructions.

#### 1. Common basis-exchange geometry

Let \(\Gamma(M)\) be the graph of bases of a matroid \(M\), joining bases related by one exchange.

**Theorem 1.** We have
\[
\boxed{\Gamma(\bigoplus_{i=1}^nU_{1,2})\cong Q_n,\qquad
\Gamma(U_{2,n})\cong J(n,2)=L(K_n).}
\tag{1}
\]
NORI1 colors unoriented edges of the first basis graph, with antipodal edges complementary. An ordinary boundary 3-tournament colors oriented edges of the second basis graph: the oriented exchange \(\{a,b\}\to\{b,c\}\) is the triple \((a,b,c)\), and its reversal obeys
\[
b(c,b,a)=1+b(a,b,c).
\tag{2}
\]

*Proof.* A basis of \(\bigoplus U_{1,2}\) chooses one element of each two-element summand; exchanging that element toggles one binary coordinate. A basis of \(U_{2,n}\) is an unordered pair, and adjacent pairs overlap in one element. Reversing an exchange of overlapping pairs reverses its ordered triple, establishing (2). \(\square\)

A legal boundary turn between two oriented exchanges has the **alternating-port** form
\[
(a,b,c)\longrightarrow(b,c,d),
\tag{3}
\]
with \(a,b,c,d\) pairwise distinct. At the intermediate basis \(\{b,c\}\), the incoming and outgoing ports differ. This property and the freshness of all original vertices are not consequences of arbitrary walk adjacency in a line graph.

#### 2. Five shared axioms

A **polarized exchange-gallery system**, with \(n\) resources and seam width \(q\in\{1,3\}\), consists of the following data.

**A1 (elementary basis-exchange states).** Its primitive colored states are specified oriented or unoriented elementary exchange edges of a matroid basis graph \(\Gamma(M)\). Its transition graph \(\widetilde H\) permits compatible consecutive exchanges, subject to nonbacktracking and alternating-port conditions.

**A2 (resource-simple permutation galleries).** There is an \(n\)-element resource alphabet \(R\). Every permutation of \(R\), perhaps with a starting root, indexes a complete gallery. A legal gallery or subgallery never repeats an original resource. This distinctness is retained when a gallery is decoded to the original model.

**A3 (reversal polarization).** The connected state graph \(\widetilde H\) admits a free involution \(J\), free also on transition edges, yielding a connected two-cover \(\widetilde H\to H=\widetilde H/J\). All state colorings satisfy \(c(Js)=1+c(s)\). If \(B_H\) is the binary graph-incidence matrix and \(a\) represents the covering-monodromy functional, define
\[
\boxed{D=M\begin{pmatrix}B_H&0\\a&1\end{pmatrix}^{*},\qquad
X_c=\operatorname{supp}(a+\delta f)\cup\{p\}.}
\tag{4}
\]
As in the preceding Subsections, the \(X_c\) are precisely the binary cycles of \(D\) containing its distinguished port \(p\), and port cocircuits are simple odd-monodromy cycles of \(H\), adjoined with \(p\).

**A4 (bounded twisted closure).** Each complete gallery on all \(n\) resources has \(n-q\) ordinary transitions and a continuation of \(q\) transitions from its last state to the involute of its initial state. The projected closed walk is a simple monodromy-one cycle of length \(n\). Any shorter \(m\)-resource gallery declared *sealable* has an analogous length-\(m\) simple closing cycle. Denote the associated family of size-\(m+1\) port cocircuits by \(\mathcal F_m\). These need not be shortest among all port cocircuits.

**A5 (local Coxeter exchanges).** Swapping adjacent resource positions changes only boundedly many states and turns, independently of \(n\). Disjoint swaps commute; resource-permutation indices satisfy braid relations; the uncolored family is invariant under relabeling resources.

A1–A5 are shared structural conditions, not a theorem asserting small cycle–cocircuit intersection. In particular, an involution and reversal-oddness alone would permit the higher-face counterexamples in Article I. The requirement that *colored primitive states be elementary one-dimensional exchanges* excludes their canonical higher-face representation, without excluding every conceivable alternative encoding.

**Proposition 2 (the two embeddings).** For \(n\ge6\), both canonical models satisfy A1–A5. In the cube model take \(M=\bigoplus U_{1,2}\), \(\widetilde H=L(Q_n)\), \(J\) induced by antipodal complementation, and \(q=1\). In the boundary model take \(M=U_{2,n}\), the graph on ordered-triple states with alternating-port transitions (3), reversal \(J(a,b,c)=(c,b,a)\), and \(q=3\).

*Proof.* A full cube geodesic has \(n\) edge states and \(n-1\) turns. The last state meets the antipode of the initial state in one further turn. Adjacent direction swaps replace a local square route. For the boundary model, the ordered-triple overlap graph is connected for \(n\ge5\): two steps change either extreme symbol while retaining the middle symbol, and one step can change the middle symbol. Reversal acts freely on the states and their edges. A full injective ordering has \(n-2\) consecutive triple states and \(n-3\) ordinary transitions. The three closing turns are constructed below. Adjacent vertex swaps alter a bounded number of neighboring three-letter windows. Both models admit all resource permutations and all legal polarized state colorings. \(\square\)

The boundary overlap graph here is a restricted alternating-port subgraph of the full line graph of the oriented-pair cover of the preceding boundary-tournament Subsection. That larger pointed matroid has port cogirth four, making four-intersection with a shortest cocircuit automatic but uninformative for long paths. A4 instead remembers the distinguished *long* closing cocircuits.

#### 3. Three-turn closure and long port cocircuits

**Theorem 3 (simple twisted closure).** Let \(v=(v_1,\ldots,v_m)\) be an injective word of length \(m\ge6\) in an ordinary boundary tournament. Set
\[
t_i=(v_i,v_{i+1},v_{i+2})\quad(1\le i\le m-2),\qquad
s_1=(v_{m-1},v_m,v_3),\quad s_2=(v_m,v_3,v_2).
\tag{5}
\]
Then
\[
\boxed{t_1,t_2,\ldots,t_{m-2},s_1,s_2,Jt_1}
\tag{6}
\]
is a state path of length \(m\) from \(t_1\) to \(Jt_1\). Its quotient is a simple cycle \(C_v\) with covering monodromy one, so
\[
\boxed{Y_v=C_v\cup\{p\}\text{ is a port cocircuit of size }m+1.}
\tag{7}
\]
The first \(m-3\) turns compare the original consecutive triple colors; the final three are closing seams.

*Proof.* Adjacent states in (6) overlap in the required ordered pair and use four distinct original vertices, by injectivity and \(m\ge6\). The ordinary states have distinct three-element supports consisting of successive triples of the injective word. The extra supports \(\{v_{m-1},v_m,v_3\}\) and \(\{v_m,v_3,v_2\}\) are distinct from one another and all successive triple supports. Hence their reversal-orbits are distinct from the earlier ones. The final state is \(Jt_1\), so its projection closes the cycle while the lift changes sheets. The cycle is simple and has monodromy one, giving the stated cocircuit by (4). \(\square\)

**Theorem 4 (seam-weight identity and decoding).** For any polarized system satisfying A3–A4, any sealable gallery \(\gamma\) with closing cocircuit \(Y_\gamma\in\mathcal F_m\), and any port cycle \(X_c\), let \(s(\gamma)\) denote the number of changes among the gallery's internal state colors. There exists \(h_\gamma\in\{0,\ldots,q\}\) such that
\[
\boxed{|X_c\cap Y_\gamma|-1=s(\gamma)+h_\gamma,\qquad
|X_c\cap Y_\gamma|\equiv0\pmod2,}
\tag{8}
\]
whence
\[
\boxed{\max(0,|X_c\cap Y_\gamma|-1-q)
\le s(\gamma)\le|X_c\cap Y_\gamma|-1.}
\tag{9}
\]
For the cube \(q=1\), intersection two on a complete gallery guarantees a monochromatic full antipodal geodesic by cyclic root rotation. For the boundary case \(q=3\), intersection at most four along a sealed \(m\)-vertex word guarantees a monochromatic vertex-simple tight subpath of order at least
\[
\boxed{\left\lceil\frac{m-2}{4}\right\rceil+2.}
\tag{10}
\]

*Proof.* The integer turn weight around the closed cycle is the sum of the \(s(\gamma)\) internal comparisons and the \(h_\gamma\le q\) closing comparisons, and the shared port adds one intersection element. Monodromy-one parity makes the intersection even. In the cube, a cyclic turn word with one changed turn can be cut at that change, yielding a full monochromatic geodesic. In the boundary model, at most three internal changes partition the \(m-2\) successive triple colors into at most four constant runs. A largest run contains at least \(\lceil(m-2)/4\rceil\) triples and therefore has two more original vertices, still pairwise distinct. \(\square\)

#### 4. The shared quantitative conjecture

**Conjecture 5 (seam-controlled gallery intersection).** In a homogeneous polarized exchange-gallery system satisfying A1–A5, with \(n\) resources, seam width \(q\in\{1,3\}\), and its decorated pointed matroid \((D,p,\{\mathcal F_m\})\), every binary cycle \(X\in Z(D)\) containing \(p\) meets a distinguished cocircuit \(Y\in\mathcal F_m\) satisfying
\[
\boxed{m\ge\left\lceil n^{\,2/(q+1)}\right\rceil,
\qquad |X\cap Y|\le q+1;}
\tag{11}
\]
for \(q=3\), require also \(m\ge6\).

**Conditional consequence.** This one assertion implies both (i) unrestricted monochromatic NORI1 and (ii) a vertex-simple monochromatic tight path of length \(\Omega(\sqrt n)\) in every ordinary boundary 3-tournament.

*Proof.* For the cube, \(q=1\) forces \(m\ge n\), hence a full gallery; intersection at most two invokes Theorem 4. For a boundary tournament, \(q=3\) forces \(m\ge\sqrt n\); intersection at most four and (10) give the stated simple tight path. \(\square\)

The exponent in (11) is proposed rather than derived. A1–A5 might require a further intrinsic rank or exchange-compatibility hypothesis for (11) to hold across *all* matroids. A refutation of this broader conjecture outside the two canonical systems would locate that missing hypothesis. The distinction between a decorated resource-simple witness family and shortest port cocircuits is essential.

#### 5. Two six-vertex obstructions

Let \(V=\{0,1,2,3,4,5\}\). Index the 60 ordered-triple reversal pairs by increasing middle vertex \(b\), then by lexicographically increasing outer pair \(a<c\) disjoint from \(b\). Define a reversal-odd coloring \(b_M(a,b,c)\) by the corresponding bit of an integer mask \(M\) if \(a<c\), and the complementary bit if \(a>c\).

For every permutation \(v=(v_1,\ldots,v_6)\), construct the six triple states in (6), evaluate their colors \(w_1,\ldots,w_6\), and compute the closing cycle turn weight
\[
W_M(v)=\sum_{i=1}^{5}[w_i\ne w_{i+1}]+[w_6=w_1].
\tag{12}
\]
The equality comparison at the end represents the reversal of the initial triple. The corresponding port intersection is \(W_M(v)+1\).

**Proposition 6 (the two-intersection threshold fails).** For
\[
\boxed{M_1=\mathrm{0x6c08f53c2725f48},}
\tag{13}
\]
the complete enumeration of all 720 full vertex permutations gives the twisted-weight histogram
\[
\boxed{W=1:0,\qquad W=3:360,\qquad W=5:360.}
\tag{14}
\]
Thus no full-resource sealed cocircuit from Theorem 3 intersects the corresponding port cycle in two elements. The cube's two-intersection target does not transfer unchanged to the boundary model.

A second mask
\[
\boxed{M_2=\mathrm{0xc047a05436d6c6e}}
\tag{15}
\]
gives \(W=1:0\), \(W=3:264\), \(W=5:456\), and **no spanning monochromatic tight word** among the 720 permutations. Hence the common conclusion cannot require a full spanning monochromatic boundary path.

*Proof (exhaustive finite verification).* Choose all 60 triple representatives by the indexing convention above. For each of the 720 permutations, calculate the four ordinary consecutive triple colors, then the two closing triple colors from (5). The six colors determine the five ordinary adjacent comparisons and the final equality comparison in (12). Independently count a full monochromatic word when its first four triple colors agree. A Python standard-library implementation enumerating combinations, permutations and these comparisons was executed and returned
\[
\begin{array}{c|ccc|c}
\text{mask}&W=1&W=3&W=5&\text{full monochromatic words}\\\hline
M_1&0&360&360&2\\
M_2&0&264&456&0
\end{array}
\]
with all row totals 720. The 60-bit masks and the completely specified enumeration rule give reproducible finite certificates. \(\square\)

#### 6. Scope and relation to Article XI

The shared object is a **decorated pointed binary matroid arising from a polarized one-dimensional basis-exchange cover**, with an admissible resource-simple path family and bounded twisted closing seams. This formulation simultaneously retains (a) NORI1's full coordinate-distinct geodesics, (b) the boundary model's coherent ordered-triple overlaps and vertex simplicity, (c) adjacent-exchange structure, and (d) the integer turn-intersection identity. The graphic-matroid independence criterion for boundary tight paths proved in the preceding Subsection is an alternative way to enforce original vertex simplicity.

Theorem 1, Proposition 2, Theorems 3–4, and Proposition 6 are established results. Conjecture 5 remains open and must not be presented as a consequence of the axioms. Its proposed seam-dependent intersection threshold and resource scale are justified as a common target by the decoding theorem and the finite obstructions; proving a corresponding general theorem or finding the missing strengthening of A1–A5 is the next research problem.

##### Appendix — executable certificate for Proposition 6

The following standalone Python 3 program verifies all 720 complete words for both finite masks, including reversal oddness, cyclic seam parity, and internal monochromaticity.

```python
"""Exhaustive n=6 boundary-tournament certificates, standard library only."""
from itertools import combinations, permutations
from collections import Counter

N = 6
representatives = [
    (a, b, c)
    for b in range(N)
    for a, c in combinations([u for u in range(N) if u != b], 2)
]
assert len(representatives) == 60
index = {triple: i for i, triple in enumerate(representatives)}

def color(mask, triple):
    a, b, c = triple
    key = (a, b, c) if a < c else (c, b, a)
    return ((mask >> index[key]) & 1) ^ int(a > c)

def enumerate_profiles(mask):
    histogram = Counter()
    for p in permutations(range(N)):
        chain = [(p[i], p[i + 1], p[i + 2]) for i in range(N - 2)]
        chain += [(p[-2], p[-1], p[2]), (p[-1], p[2], p[1])]
        colors = [color(mask, t) for t in chain]
        closed_turns = sum(colors[i] != colors[i + 1] for i in range(N - 1))
        closed_turns += int(colors[-1] == colors[0])
        internal_turns = sum(colors[i] != colors[i + 1] for i in range(N - 3))
        histogram[(closed_turns, internal_turns)] += 1
    assert sum(histogram.values()) == 720
    assert all(k[0] % 2 == 1 for k in histogram)
    return histogram

if __name__ == '__main__':
    A = 0x6C08F53C2725F48
    B = 0xC047A05436D6C6E
    for name, mask in [('No two-point port intersection', A),
                       ('No spanning monochromatic word', B)]:
        h = enumerate_profiles(mask)
        t = Counter({q: sum(c for (turns, internal), c in h.items()
                             if turns == q) for q in (1, 3, 5)})
        print(name, hex(mask), 'closed turns:', dict(t),
              'spanning monochromatic:',
              sum(c for (turns, internal), c in h.items() if internal == 0))
    assert all(t >= 3 for (t, _), _c in enumerate_profiles(A).items())
    assert all(k >= 1 for (_t, k), _c in enumerate_profiles(B).items())
```


### Unified matroid conjectures: common axioms, implications, and obstructions

This Subsection assembles the Article XI exploration of generalized binary matroid intersection properties and the comparison with reversal-odd boundary 3-tournaments. The goal is an abstract theorem implying **both** unrestricted monochromatic NORI1 and a long vertex-simple monochromatic boundary-tournament tight path. It separates established facts from proposed conjectures; none of the proposed universal intersection implications below has been proved.

#### A. The shared pointed line-graph double cover

For any connected regular two-cover \(\widetilde F\to F\) with deck involution \(\rho\), put \(H=L(F)=L(\widetilde F)/\rho\). Let \(B_H\) be the binary incidence matrix and \(a\) a binary cochain representing covering monodromy. The *pointed lift dual*
\[
\boxed{D=M\begin{pmatrix}B_H&0\\a&1\end{pmatrix}^{*}}\tag{1}
\]
has a distinguished element \(p\). Every deck-odd edge coloring of the cover, \(c(\rho e)=1+c(e)\), induces a turn cochain \(d([\{e,f\}])=c(e)+c(f)\) on \(H\), and the allowed signatures comprise the single affine switching class \(a+B^1(H;\mathbb F_2)\). The corresponding binary cycle is \(X_d=\operatorname{supp}(d)\cup\{p\}\). Conversely every port-containing binary cycle determines a coloring up to global complement. Port-containing cocircuits are \(Y_C=C\cup\{p\}\), with \(C\) a simple monodromy-one cycle in \(H\), and
\[
\boxed{|X_d\cap Y_C|=1+\sum_{t\in C}d(t),}\tag{2}
\]
with the sum on the right taken as an integer. These statements are proved in the foundational Subsections.

For the cube take \(\widetilde F=Q_n\), \(F=Q_n/\tau\), and write \(D_n\) for (1). Its shortest port cocircuits have \(|Y|=n+1\) and correspond to full antipodal geodesics. The unrestricted two-switch conjecture says that every port cycle intersects one of these shortest cocircuits in at most four elements. The monochromatic NORI1 conjecture requires intersection two.

For an ordinary boundary tournament take \(\widetilde F=S_n\), the graph of ordered pairs \((u,v)\) with transitions \((u,v)\sim(v,w)\), with deck action \((u,v)\mapsto(v,u)\) and quotient \(F=L(K_n)\). The reversal-odd triple color \(b(u,v,w)=1+b(w,v,u)\) is the deck-odd edge color of that transition. The quotient turn graph is \(H_n^{\rm BT}=L^2(K_n)\), and (1)--(2) yield a pointed binary matroid \(D_n^{\rm BT}\) and a bijection between its port cycles and tournament colorings up to complement.

**Essential asymmetry (theorem):**
\[
\boxed{g_p(D_n)=n+1,\qquad g_p(D_n^{\rm BT})=4.}\tag{3}
\]
In the tournament case the shortest port cocircuits are local star triangles. Every port cycle intersects each in two or four elements, and for \(n\ge5\) a transitive three-vertex local subtournament gives an intersection of two. Therefore an intersection conjecture restricted to *shortest* port cocircuits is automatically satisfied by the tournament and cannot imply long monochromatic tight paths.

#### B. The stronger shared structure: polarized resource galleries

The useful common structure extends beyond the pointed binary matroid itself:

**S1 (polarization).** A connected two-cover of a transition/state graph, with a free involution, a deck-odd coloring of elementary one-dimensional exchange states, and the affine port-cycle correspondence (1).

**S2 (small balanced relations).** The monodromy-zero cycle space of the quotient turn graph is generated by local bounded-support relations. The cube has star triangles and square turns. The tournament has star triangles, triangle turns, and binary sums of paired local triangle turns, with support at most six. These bounds are independent of the size of the underlying instance.

**S3 (resource independence).** Legal witness galleries respect an auxiliary matroid. For the cube, the relevant resource matroid is the partition matroid on coordinate directions; a full antipodal geodesic uses each coordinate once. For boundary tournaments, a coherent state path reads an original vertex word \(v_1,\ldots,v_m\); its projected ordered-pair resources \(\{v_i,v_{i+1}\}\) must be independent in the graphic matroid \(M(K_n)\). Along with the forward-overlap rule, this is equivalent to vertex simplicity.

**S4 (bounded local basis exchanges).** Adjacent transpositions of coordinate directions or of original vertices change only bounded local parts of the corresponding gallery. The exchanges generate connected permutation galleries and satisfy the usual local Coxeter relations, subject to maintaining coherent orientation and resource independence.

**S5 (bounded twisted closing seam).** Sealable galleries can be prolonged to the involute of their first state in \(q\) additional turns, producing marked monodromy-one cycles and cocircuits. On the cube \(q=1\), and the marked full-gallery cocircuits are the *shortest* port cocircuits. In the tournament \(q=3\), and an injective word of \(m\ge6\) vertices has an explicit three-turn closure giving a marked port cocircuit of size \(m+1\), generally much longer than the shortest cocircuit.

The natural setting for S1--S5 is the basis-exchange graph of a matroid together with a reversal polarization. The cube is the basis graph of \(\bigoplus_{i=1}^nU_{1,2}\), whereas \(L(K_n)=J(n,2)\) is the basis graph of \(U_{2,n}\). Their compatible one-dimensional exchanges lead to the two cover constructions. It is the **decorated pointed binary lift plus its independent coherent path language** that might satisfy a common theorem, not the undecorated pointed matroid.

#### C. Abstract intersection conjectures at different strengths

For finite pointed binary \((M,p)\), let \(Z(M)\) be its binary cycle space and
\[
g_p(M)=\min\{|Y|:Y\in\mathcal C^*(M),\ p\in Y\},\quad
\mathcal Y_p=\{Y\in\mathcal C^*(M):p\in Y,\ |Y|=g_p(M)\}.
\tag{4}
\]
Let \(P_b(M,p)\) require, for every port-containing binary cycle \(X\), a *shortest* port cocircuit \(Y\in\mathcal Y_p\) satisfying \(|X\cap Y|\le b\). Let \(\mathrm{PI}_2(M,p)\) be the weaker requirement of intersection two with *some* port cocircuit, which may be long.

**Refuted Conjecture A (abstract short-port amplification).** The proposed implication from binary representability, cographic port deletion, triangle/square generation of the balanced cycle space, connected shortest-cocircuit exchanges with \(|Y\triangle Y'|\le6\), and \(\mathrm{PI}_2(M,p)\) to \(P_4(M,p)\) is false. The weaker-hypothesis version is therefore false as well.

**Balanced-shortcut counterexample.** Start with \(H_6=L(Q_6)/\tau\). The consecutive cube edges \(e_0=\{0,1\}\), \(e_1=\{1,3\}\), \(e_2=\{3,7\}\) define a two-turn path. Add the shortcut \(z=[e_0][e_2]\), with signature equal to the sum along that path, so the new triangle is balanced. The resulting pointed lift dual \(D^+\) satisfies \(D^+/z=D_6\). Thus \(\mathrm{PI}_2\) follows from the established six-dimensional cube theorem, and the old triangle/square generators plus the new triangle generate its balanced cycle space. Its shortest port cocircuits have size six and are indexed by the six orders of the remaining directions \(3,4,5\); their threshold-six exchange graph is connected. An antipodally odd coloring alternating by level on the remaining three-dimensional subcube makes every one of these cocircuits meet its port cycle in six elements. Hence \(P_4(D^+,p)\) fails. The complete construction, proof of the shortest-witness classification, coloring, and finite audit are retained in research note `note_nori_xi_balanced_shortcut_refutes_port_amplification`.

The failure already occurs under a single faithful, port-preserving coextension with a three-element non-port cocircuit certificate. Contraction raises port cogirth from six to seven; the cogirth-preserving contraction theorem remains valid. The shortcut is not a legal cube turn, so this refutes the abstract amplification proposal without refuting the canonical cube or resource-marked boundary conjectures.

For cube \(D_n\), Wu--Yang's 2026 proof of the nongeodesic monochromatic antipodal-path theorem, together with the Article XI odd-girth reduction, establishes \(\mathrm{PI}_2\). The minimum port cocircuits form a connected exchange graph and their even intersection values have no gaps. These are all-dimensional theorems. They do not yet bound the *minimum* intersection by four. The nongeodesic two-intersection witness can have large cocircuit cardinality.

**Conjecture B (seam-controlled marked-gallery intersection).** Let \(\mathscr G\) be a homogeneous polarized basis-exchange-gallery system on \(n\) resources satisfying S1--S5, with seam width \(q\in\{1,3\}\), pointed lift \(D\), and distinguished family \(\mathcal F_m\) of port cocircuits produced by sealable, resource-independent galleries on \(m\) resources. Conjecture that for each \(X\in Z(D)\) containing \(p\), there are \(m\) and \(Y\in\mathcal F_m\) such that
\[
\boxed{m\ge\left\lceil n^{2/(q+1)}\right\rceil,\qquad |X\cap Y|\le q+1,}\tag{5}
\]
with the boundary case additionally taking \(m\ge6\), where the published closing construction applies. The exponent and possible sufficiency of S1--S5 are conjectural. Additional structural rank/exchange hypotheses may be needed.

For such a closing witness the proved seam-count identity is
\[
\boxed{|X\cap Y_\gamma|-1=\operatorname{sw}(\gamma)+h_\gamma,\qquad 0\le h_\gamma\le q.}\tag{6}
\]
If \(q=1\), (5) supplies a full \(n\)-resource cube gallery with cyclic turn weight at most one; cyclic rotation produces a full monochromatic antipodal geodesic, establishing unrestricted NORI1. If \(q=3\), it supplies an injective boundary word with \(m\ge\sqrt n\) vertices and at most three internal changes among its \(m-2\) triple colors. The longest of at most four constant runs then supplies a vertex-simple monochromatic tight path with at least
\[
\boxed{\left\lceil\frac{m-2}{4}\right\rceil+2=\Omega(\sqrt n)}\tag{7}
\]
original vertices. Thus (5) would resolve the two target problems simultaneously. This is a *conditional implication*, not a proof of (5).

**Conjecture C (independence-preserving exchange and rank growth).** Seek a local, color-cost-controlled exchange operation acting on galleries or marked cocircuits that preserves the appropriate auxiliary resource matroid and legal transition language. It should remove repeated-resource excess or increase the independent resource rank without growing \(|X\cap Y|\) beyond the appropriate seam budget. In the cube, the obstacle is an extra coordinate traversal in a low-weight monodromy-one cycle; in the boundary model, the obstacle is extending a zero-turn directed tight path without repeating an original vertex. A sufficiently strong iterative rank-growth or defect-reduction lemma would lead to Conjecture B. The desired operation must be expressed in local basis/circuit language without assuming the sought low-intersection witness.

The direct equivalent research target deletes the disagreeing turns \(\operatorname{supp}(X)\setminus\{p\}\) from the quotient turn graph and asks for a long **resource-independent coherent zero-turn gallery**. The closure formulation (5)--(6) instead allows a bounded number of nonzero turns and extracts a long zero-turn subgallery.

#### D. Noncubical matroids already reached by contraction

Another Subsection of this Section proves a broader class by starting from a simple pointed binary matroid \((N,t)\), with \(t\) spanned by a set of distinct nonzero binary generators \(S\). The Cayley graph \(\operatorname{Cay}(\mathbb F_2^r,S)\), with involution translating by \(t\), produces a pointed signed-cover matroid \(\mathfrak D(N,t)\). If the shortest circuit of \(N\) through \(t\) has size \(q\), the new matroid has port cogirth \(q\) and admits a port-cogirth-preserving contraction onto \(D_{q-1}\). The established contraction-inheritance theorem transfers \(P_b\) for \(b=2,4\) from this cube matroid to \(\mathfrak D(N,t)\). This generalization is equivalent to the all-dimensional cube assertion, since cube matroids occur inside it. It gives noncubical examples, but does not subsume the tournament's long directed path language.

#### E. Counterexamples showing why the decorations matter

The signed odd five-cycle yields a binary pointed dual \(M=U_{1,6}\) with cographic deletion whose ground-set cycle and only cocircuit intersect in six elements; binary/cographic hypotheses alone do not imply \(P_4\). Signed theta examples show that bounded local generators and connected shortest-cocircuit exchanges also do not suffice in the absence of the unrestricted two-intersection premise.

The tope graph \(C_{10}\square Q_k\) admits an antipodally odd edge coloring forcing four changes along every antipodal geodesic for arbitrarily large \(k\). Therefore all antipodal partial cubes, all oriented-matroid tope graphs, and high rank alone form overly broad classes. Pairwise square crossing of coordinate directions was proposed as a possible stronger geometric restriction; its sufficiency is unknown.

For the boundary cover, shortest port cogirth is four, so the four-intersection problem is trivial even though the long monochromatic tight-path problem remains difficult. A published six-vertex mask demonstrates that two-intersection can fail across *all full-length marked boundary closure cocircuits*; a second mask prevents a monochromatic spanning tight word. These rule out stronger seam conjectures requiring two-intersection for every full boundary gallery or a spanning monochromatic boundary path. The four-intersection and square-root resource targets in (5) survive these tests.

Earlier higher-face reversal-odd counterexamples demonstrate that reversal oddness and pointed binary representability alone cannot enforce the required long path. Insistence on elementary one-dimensional exchange states and an independent-resource path language is therefore substantive, although it remains to be tested whether S1--S5 are strong enough outside the canonical models.

#### F. Program for finding the missing shared hypothesis

The main missing property is a **rank-preserving, independence-preserving local splice** compatible with signed monodromy, resource orientation and short local balanced relations. A viable hypothesis must be stated without using the desired global intersection conclusion as an assumption. Search for such a splice through basis-exchange squares, local star triangles, ordered-window exchanges, and their resulting endpoint carriers.

Any replacement for refuted Conjecture A must prevent balanced shortcuts from decoupling minimum witness length from the surviving low-intersection witnesses. Retain geometric/resource legality or a suitable metric condition; small balanced generators and connected shortest exchanges alone do not supply it. Test Conjecture B on other basis-exchange graphs and oriented-matroid systems, always recording port intersection, cocircuit length, independent resource rank, admissible orientation and seam count. Test whether a monotone surgery for repeated cube-coordinate traversals has an analogue that extends boundary paths through fresh vertices. Bounded adjacent-swap exchange and the parity of signed local generators provide the most promising common algebra.

**Epistemic boundary.** The pointed lift representation, affine coset, local-generator facts, shortest-cogirth distinction, seam identity, contraction inheritance and specified counterexamples are established elsewhere in Article XI. Conjecture A is refuted by the balanced-shortcut construction above. Conjectures B and C and the resource bound (5) remain open. The goal is not a matroid theorem already satisfied by the short local tournament cocircuits, but a theorem about a **decorated pointed matroid and its marked matroid-independent gallery family** capable of proving both NORI1 and long boundary-tournament paths.

### A canonical second port: orientation curvature and coherent galleries

Let \(\widetilde F\to F\) be a connected regular two-sheeted cover of finite connected simple graphs with deck involution \(\rho\). Assume \(F\) has a vertex of degree at least three, and put \(H=L(F)=L(\widetilde F)/\rho\). Article XI already defines the binary monodromy cochain \(a\), the pointed dual lift, and the color-dependent turn-signature class. The following new cohomology class is intrinsic to the same cover and distinguishes different *types of path closure*.

**Definition.** Orient the edges of \(\widetilde F\) so that \(\rho\) reverses their orientations. This can always be arranged because the deck action is free on edge orbits. For a quotient turn \(t\in E(H)\), choose incident lifted edges \(e,f\) meeting at a state \(v\). Define
\[
\lambda(t)=0\quad\text{if one edge enters and the other leaves }v,\qquad
\lambda(t)=1\quad\text{if both enter or both leave }v.
\tag{1}
\]
Reversing both orientations under \(\rho\) preserves this label, so \(\lambda\) is a cochain on \(H\).

**Theorem 1 (canonical orientation-curvature class).** Its class \([\lambda]\) modulo the cut space of \(H\) does not depend on which anti-equivariant orientations were chosen. For every star triangle \(T\) in \(H\), corresponding to three edges of \(F\) incident at one vertex,
\[
\boxed{\alpha(T)=0,\qquad\lambda(T)=1.}\tag{2}
\]
Consequently \([\lambda]\) and covering monodromy \([a]\) are independent binary cohomology classes.

*Proof.* Reorienting a deck-orbit of cover edges toggles the sense at every incident turn and therefore adds the vertex cut in \(H\) supported at the orbit corresponding to that vertex of \(H\). All reorientations act by sums of such cuts. A star triangle lifts to three cover edges meeting at one vertex, hence has monodromy zero. If the three incidence senses are \(b_1,b_2,b_3\), its curvature labels are \(1+b_1+b_2\), \(1+b_2+b_3\), and \(1+b_3+b_1\), summing to one over \(\mathbb F_2\). Since the cover is connected, monodromy is nonzero on some cycle, while the star triangle separates \([\lambda]\) from both zero and \([a]\). \(\square\)

**Theorem 2 (stationary-contact parity identity).** Let \(C\) be a simple cycle of \(H\), of length \(r\), and lift it to cover edges \(e_1,\ldots,e_r,e_{r+1}=\rho^\varepsilon e_1\), where \(\varepsilon=\alpha(C)\). Let \(v_i\) be the contact vertex of \(e_i,e_{i+1}\), and \(v_0=\rho^\varepsilon v_r\). Define \(s(C)=|\{i:v_{i-1}=v_i\}|\). Then
\[
\boxed{\lambda(C)\equiv\alpha(C)+s(C)\pmod2.}\tag{3}
\]
In particular a monodromy-one cycle with no stationary contact has curvature one, while a monodromy-one cycle built entirely from coherently directed transitions, all labeled \(\lambda=0\), has an odd number of stationary contacts.

*Proof.* For an oriented cover edge \(e\) and its incident vertex \(v\), set \(h(e,v)=1\) if \(v\) is the head of \(e\) and zero if it is the tail. The turn at \(v_i\) has
\[
\lambda_i=1+h(e_i,v_i)+h(e_{i+1},v_i).
\]
Sum over \(i\). The seam contributes \(\varepsilon\), because the orientation of \(\rho^\varepsilon e_1\) is the reversal of that of \(e_1\) when \(\varepsilon=1\). Each internal cover edge contributes one when its two contact vertices are different, and zero when they coincide. Thus
\[
\lambda(C)\equiv r+\varepsilon+(r-s(C))
\equiv\varepsilon+s(C)\pmod2.
\]
\(\square\)

**Theorem 3 (choice-free two-port lift).** Add distinguished columns \(p,q\), and put
\[
\boxed{\widehat M^{(2)}=
M\left(\begin{array}{c|cc}B_H&0&0\\
a&1&0\\ \lambda&0&1
\end{array}\right).}\tag{4}
\]
With its ordered pair of ports, this represented binary matroid is independent of cochain representatives and of anti-equivariant orientation choices. Its rank is \(|V(H)|+1\). Every simple graph cycle \(C\) gives a circuit
\[
\boxed{C\cup\bigl(\{p\}\text{ if }\alpha(C)=1\bigr)
\cup\bigl(\{q\}\text{ if }\lambda(C)=1\bigr).}\tag{5}
\]
The four signature sectors \((\alpha,\lambda)\in\mathbb F_2^2\) are consequently intrinsic.

*Proof.* Altering either cochain by a cut performs row operations on (4), so it leaves the represented matroid unchanged. The two cohomology classes are independent by Theorem 1, and \(B_H\) has rank \(|V(H)|-1\), giving the rank. The columns of a simple cycle sum to zero in the incidence rows and to \((\alpha(C),\lambda(C))\) in the bottom two rows; adjoining the specified port columns gives a dependence. Every proper nonempty subset of a simple cycle has nonzero incidence boundary, and the port columns are independent, so the dependence is minimal. \(\square\)

**Corollary 4 (cube and boundary paths occupy different phases).** A full antipodal cube geodesic has \((\alpha,\lambda)=(1,1)\) because its lifted consecutive edge contacts are all moving. A naturally directed boundary-tournament gallery from an ordered triple state \(t\) to its reversal \(\rho t\) has \((\alpha,\lambda)=(1,0)\), since all its consecutive directed turns have opposite incidence senses. The spurious minimum-port boundary star triangles have \((\alpha,\lambda)=(1,1)\), and hence lie in the opposite phase from coherent directed tournament galleries. This distinction is preserved by the two-port matroid.

**Theorem 5 (minimum coherent closing length and repeated resources).** In the ordered-pair boundary cover, a naturally directed sequence of triple-edge states beginning with \((a,b,c)\) and ending with its reversal \((c,b,a)\) must contain at least five directed turns. Five suffice, using four distinct original vertices \(a,b,c,d\):
\[
(a,b,c),(b,c,a),(c,a,d),(a,d,c),(d,c,b),(c,b,a).
\tag{6}
\]
Its first five reversal-orbits are distinct, so it yields a simple monodromy-one cycle of length five. Nevertheless the underlying original vertex word
\[
a,b,c,a,d,c,b,a
\tag{7}
\]
repeats vertices, and is not a matroid-independent tight path.

*Proof.* If a directed sequence has \(r\) turns, it reads a word \(x_1,\ldots,x_{r+3}\), each consecutive triple having distinct entries. The twisted terminal constraint reads
\((x_{r+1},x_{r+2},x_{r+3})=(x_3,x_2,x_1)\).
For \(r=2\) it yields the forbidden triple \((x_2,x_3,x_2)\); for \(r=3\) an adjacent equality \(x_4=x_3\); for \(r=4\) a forbidden triple \((x_3,x_4,x_3)\); and \(r=0,1\) are immediately impossible. Hence \(r\ge5\). The sequence (6) supplies the claimed example and its reversal-orbits are pairwise distinct. \(\square\)

**Theorem 6 (the tournament closing seam width three is optimal).** For pairwise distinct \(v_1,\ldots,v_m\), \(m\ge6\), the full tight triple sequence from \((v_1,v_2,v_3)\) to \((v_{m-2},v_{m-1},v_m)\) needs at least three directed transitions to reach the reversal \((v_3,v_2,v_1)\). The three-turn continuation
\[
(v_{m-1},v_m,v_3),\quad
(v_m,v_3,v_2),\quad
(v_3,v_2,v_1)
\tag{8}
\]
attains this minimum.

*Proof.* A one-step continuation would require \((v_{m-1},v_m)=(v_3,v_2)\), impossible by injectivity. A two-step continuation would require \(v_m=v_3\), also impossible. The continuation (8) respects consecutive ordered-pair overlaps and has the simple closing quotient proved in the earlier seam theorem. \(\square\)

**Proposition 7 (two ports are not enough).** In \(H_n^{\rm BT}\), \(n\ge4\), the four successive triple-state orbits represented by
\[
(1,0,2),\ (2,0,3),\ (1,0,3),\ (0,1,3)
\tag{9}
\]
form a simple cycle \(C\) with \((\alpha(C),\lambda(C))=(1,0)\), yet two of its turns are incoherent. Indeed, lift the four states and closing mate as
\[
(1,0,2),\ (3,0,2),\ (3,0,1),\ (0,1,3),\ (2,0,1).
\tag{10}
\]
The first two transitions are head--head and tail--tail respectively, while the other two are head--tail or tail--head. Hence curvature parity vanishes, although these are not all legal directed transitions. Thus the second port is an intrinsic useful refinement, but a valid long-path conjecture still must specify a *coherent directed witness family with an independent resource matroid*.

**Conjectural program.** Refine the pointed-gallery intersection conjecture to a *phase-prescribed two-port* theorem. Select odd-monodromy closed witnesses from the \((1,1)\) phase for full cube geodesics and from the \((1,0)\) phase for coherently directed tournament galleries, subject in both cases to independent resources. Theorem 6 explains why the boundary seam budget is three, rather than an artifact of one arbitrary closing construction. Theorem 5 and Proposition 7 demonstrate that a phase restriction alone still admits short resource-repeating or incoherent cycles. No universal four-intersection or two-intersection selector for the decorated two-port system is presently proved.

**Theorem 8 (seam triangle contraction changes curvature phase).** Let \(C\) be the length-\(m\) monodromy-one turn cycle obtained from a coherent directed twisted closure
\[
e_1\longrightarrow e_2\longrightarrow\cdots\longrightarrow e_m
\longrightarrow \rho e_1
\tag{11}
\]
in an oriented covering graph, with pairwise distinct quotient edge-state orbits, \(m\ge4\). Then the canonical lifted cyclic contact sequence of \(C\) has
\[
\boxed{s(C)=1,\qquad (\alpha(C),\lambda(C))=(1,0).}\tag{12}
\]
The unique stationary contact occurs at the first edge-state \(e_1\), because it is reached from the deck-translated predecessor and departed from through its head. Removing that edge-state by contracting its star triangle produces a simple cycle \(C'\) of \(H\) with
\[
\boxed{|C'|=m-1,\qquad
(\alpha(C'),\lambda(C'))=(1,1),\qquad
w_d(C')\le w_d(C)}
\tag{13}
\]
for every admissible deck-odd turn signature \(d\). The cost difference belongs to \(\{0,2\}\). This move therefore preserves cover monodromy and never increases coloring cost, but it **leaves the coherent-gallery phase**.

*Proof.* Each interior directed edge-state \(e_j\), \(j\ge2\), is contacted at its tail by the preceding directed edge and at its head by the succeeding one, so its contacts differ. The first edge-state \(e_1\) is contacted at its head by \(e_2\), while its other contact is the deck translate of the terminal meeting between \(e_m\) and \(\rho e_1\). Because \(\rho\) reverses the orientation, that translated contact is again the head of \(e_1\). Hence \(s(C)=1\). Theorem 2 gives \(\lambda(C)=1+s(C)=0\).

The edges of \(\widetilde F\) immediately preceding and following \(e_1\), after translating the preceding one to the same sheet, meet at the same vertex. Their three pairwise turns constitute a balanced star triangle. Replace the two consecutive turns through the vertex \([e_1]\) of \(C\) with the third side of that triangle. The resulting graph cycle \(C'\) is simple because the other quotient edge-state orbits were distinct and \(m\ge4\). It has the same monodromy, since the removed star triangle has monodromy zero. The contacts of all remaining lifted edge-states are unchanged, while the unique stationary contact of \(e_1\) is removed, giving \(s(C')=0\) and \(\lambda(C')=1\).

If the lifted edge-state colors in the star triangle are \(x,y,z\in\mathbb F_2\), its turn-cost change is
\[
(x\oplus y)+(y\oplus z)-(x\oplus z)
=2\,\mathbf1_{\{x=z\ne y\}}\in\{0,2\}.
\]
Thus \(w_d(C')\le w_d(C)\) simultaneously for every admissible coloring. \(\square\)

**Exchange warning.** Theorem 8 identifies a structural failure mode of undecorated cocircuit minimization. A cost-nonincreasing contraction of a marked tournament cocircuit may return a shorter cocircuit with the wrong orientation-curvature phase, even before resource independence is considered. A successful unifying exchange theorem must either preserve the prescribed \(\lambda\)-phase and coherent state language, or accompany the shortening by a controlled phase-repair splice. This is a stronger necessary design criterion than preserving only the original monodromy port.

**Theorem 9 (orientation curvature is monodromy plus a cover-independent line-graph class).** There is a canonical cohomology class \([\kappa_F]\in \mathbb F_2^{E(L(F))}/B^1(L(F))\), defined without reference to the covering \(\widetilde F\to F\), such that
\[
\boxed{[\lambda]=[a]+[\kappa_F].}\tag{14}
\]
To define \(\kappa_F\), orient the edges of the *base graph* \(F\) arbitrarily and, for each turn of \(H=L(F)\), set \(\kappa_F(t)=1\) if the two base edges meeting at its center have the same incidence sense, and zero otherwise. Its class is independent of those orientations. For every simple turn cycle \(C\),
\[
\boxed{\kappa_F(C)\equiv s(C)\pmod2.}\tag{15}
\]
Thus the additional binary datum is the universal *stationary-contact curvature of the line graph*, and the orientation-curvature phase of the cover equals this class twisted by monodromy. In the cube target, full geodesic cycles satisfy \((\alpha,\kappa_F)=(1,0)\). In the coherent boundary gallery target, closed directed galleries satisfy \((\alpha,\kappa_F)=(1,1)\). Short boundary star-triangle cycles satisfy \((\alpha,\kappa_F)=(1,0)\).

*Proof.* Reversing the orientation of an edge of \(F\) toggles \(\kappa_F\) on every turn incident with its vertex in \(L(F)\), hence adds a cut. For a lifted turn cycle \(C\), let its successive projected \(F\)-edges be \(f_1,\ldots,f_r,f_{r+1}=f_1\) with common center vertices \(w_i\), \(w_0=w_r\). Writing \(h(f,w)\) for the incidence head-bit of an oriented base edge, the turn label is
\[
\kappa_i=1+h(f_i,w_i)+h(f_{i+1},w_i).
\]
Summation yields
\[
\kappa_F(C)\equiv r+
\sum_{i=1}^r\bigl(h(f_i,w_{i-1})+h(f_i,w_i)\bigr)
\equiv r+(r-s(C))=s(C).
\]
Together with Theorem 2, this gives \(\lambda(C)=\alpha(C)+\kappa_F(C)\) for every cycle \(C\), hence (14) because a cochain annihilating the graph cycle space is a cut. The three model-specific pairs follow from their stationary-contact counts already proved. \(\square\)

**Structural significance.** Equation (14) removes any dependence on an arbitrary orientation upstairs: the two cohomological degrees of freedom are the covering class \([a]\) and an intrinsic characteristic class \([\kappa_F]\) of the base line graph. The common pointed-matroid generalization can therefore be phrased as a graph-cover lift *with its canonical line-graph contact curvature*. This is a cleaner mathematical hypothesis than adding unrelated direction or seam labels, although the counterexamples in Theorems 5 and 7 show that resource independence and coherent orientation remain necessary for long-path decoding.

**Corollary 10 (bipointed cographic deletion and asymmetric witness ports).** Let \(D^{(2)}=(\widehat M^{(2)})^*\) be the dual of the two-port matroid (4). Then
\[
\boxed{D^{(2)}\setminus\{p,q\}\cong M(H)^*,}\tag{16}
\]
a cographic matroid. For each admissible deck-odd turn signature \(d=a+\delta f\), the set
\[
\boxed{X_d=\operatorname{supp}(d)\cup\{p\}}\tag{17}
\]
is a binary cycle of \(D^{(2)}\) that contains \(p\) but not \(q\). For a simple turn cycle \(C\), the associated dual cocircuit is
\[
Y_C=C\cup p^{\alpha(C)}\cup q^{\lambda(C)},\tag{18}
\]
where exponent one means the corresponding port is included. When \(\alpha(C)=1\),
\[
\boxed{|X_d\cap Y_C|=1+w_d(C).}\tag{19}
\]
Therefore full cube-geodesic witnesses are cocircuits containing **both** \(p,q\), while coherent boundary-tournament closure witnesses are cocircuits containing \(p\) and **excluding** \(q\). This port-membership distinction replaces the external terminology of curvature phases with an intrinsic matroid condition.

*Proof.* Contracting both independent unit columns \(p,q\) in the matrix (4) removes the two bottom rows and leaves the graphic incidence representation \(B_H\). Dualizing turns contraction into deletion, proving (16). The rows of (4) generate cycles of \(D^{(2)}\); combining the \(a\)-row with incidence rows produces \((d,1,0)\), proving (17). Formula (18) is Theorem 3 interpreted as a dual cocircuit. Formula (19) follows by counting the common port \(p\) and the support of \(d\) on \(C\). The geometric port memberships were established in Corollary 4. \(\square\)

**Refined unified conjectural form.** Seek a statement for bipointed binary matroids with cographic double deletion, a distinguished coherent resource-independent gallery family, and locally generated balanced relations: every admissible \(p\)-containing, \(q\)-avoiding binary cycle should meet a resource-large marked cocircuit in a bounded even number of elements, with the cocircuit's \(q\)-membership prescribed by the gallery type. The cube asks for *both-port* witnesses of full coordinate rank, whereas the boundary model asks for *\(p\)-only* witnesses of resource rank \(\Omega(\sqrt n)\). The two-port matroid identifies the appropriate cocircuit sectors but does not itself guarantee large resources or small intersection.

Let \(n\ge5\). Write \(S_n\) for the ordered-pair double cover of \(L(K_n)\), with vertices \((u,v)\) and undirected edges labelled by triples \(t=(a,b,c)\), corresponding to \((a,b)-(b,c)\), where the three symbols are distinct. Its deck involution reverses ordered pairs and triple labels. Put
\[
H_{\rm full}=L(S_n)/\langle\rho\rangle\cong L^2(K_n).
\]
The covering \(L(S_n)\to H_{\rm full}\) defines the pointed binary dual \(D_{\rm full}\) of the incidence-plus-monodromy matrix of Article XI.

Declare a turn between triple states **legal** if it has a lift of the form
\[
(a,b,c)\;--\;(b,c,d),\qquad
a,b,c,d\text{ pairwise distinct},
\tag{1}
\]
or the reverse traversal. Let \(F\subseteq E(H_{\rm full})\) be its set of legal turns and \(H_{\rm leg}=(V(H_{\rm full}),F)\). This is the quotient of the alternating-port ordered-triple overlap graph from Article XI. Let \(T=E(H_{\rm full})\setminus F\).

**Theorem 1 (three-turn reconstruction).** Every omitted turn \(e\in T\) has a lifted representative joining two triple states \(t,t'\) that can be joined by a legal-turn path of length at most three in the ordered-triple graph. The projected path \(P_e\subseteq F\) can be chosen such that \(P_e\cup\{e\}\) is a simple cycle of \(H_{\rm full}\) with trivial covering monodromy. In particular,
\[
\boxed{\forall X\in Z(D_{\rm full}),\quad
\mathbf1_X(e)=\sum_{f\in P_e}\mathbf1_X(f)\pmod2,\qquad |P_e|\le3.}
\tag{2}
\]
Equivalently, every \(e\in T\) belongs to a cocircuit \(Y_e\) of \(D_{\rm full}\) avoiding the port and satisfying
\[
\boxed{Y_e\cap T=\{e\},\qquad |Y_e|\le4.}\tag{3}
\]
The bound three in (2) is attained by the forbidden return turns.

*Proof.* Fix the ordered-pair state \((u,v)\) at which the lifted omitted turn meets. Its incident triple states are of two types,
\[
I_w=(w,u,v),\qquad O_z=(u,v,z),
\quad w,z\notin\{u,v\}.
\]
The legal turns at this state are \(I_w--O_z\) with \(w\ne z\). Every omitted turn falls into one of the following cases.

If \(e=I_wI_{w'}\), with \(w\ne w'\), choose \(z\notin\{u,v,w,w'\}\). Then
\(I_w--O_z--I_{w'}\) is a legal two-turn path.

If \(e=O_zO_{z'}\), choose \(w\notin\{u,v,z,z'\}\). Then
\(O_z--I_w--O_{z'}\) is a legal two-turn path.

If \(e=I_wO_w\), choose distinct \(x,y\notin\{u,v,w\}\). Then
\[
I_w--O_x--I_y--O_w
\tag{4}
\]
is a legal three-turn path. These choices exist for \(n\ge5\). In each case the displayed triple states belong to different reversal orbits, so their projections together with \(e\) form a simple cycle. The lifted path followed by the reversed omitted turn closes on the original sheet, hence that cycle has monodromy zero. Its edge set is therefore a non-port circuit of the incidence-plus-monodromy matroid, equivalently a non-port cocircuit of \(D_{\rm full}\). Binary cycle–cocircuit orthogonality yields (2) and (3). \(\square\)

**Theorem 2 (faithful minor and cycle-space isomorphism).** The pointed legal-turn lift matroid \(D_{\rm leg}\) satisfies
\[
\boxed{D_{\rm leg}=D_{\rm full}/T.}\tag{5}
\]
Moreover, restriction to the surviving elements is a linear isomorphism
\[
\boxed{\pi:Z(D_{\rm full})\xrightarrow{\sim}Z(D_{\rm leg}),
\quad X\longmapsto X\cap(F\cup\{p\}).}\tag{6}
\]
In particular, port-containing cycles are in bijection, and the full boundary-tournament coloring modulo global complementation is recoverable from legal-turn data alone. This contraction does **not** preserve port cogirth: in the established range \(n\ge6\), the full-turn pointed matroid has \(g_p=4\), whereas the alternating-port legal-turn pointed matroid has \(g_p=7\).

*Proof.* Restricting the incidence-plus-monodromy matrix for \(H_{\rm full}\) to columns \(F\cup\{p\}\) gives the corresponding matrix for \(H_{\rm leg}\). Matroid duality exchanges this restriction with contraction, proving (5). Projection of binary cycle spaces under contraction is surjective. It is injective by (2): if a cycle restricts to zero on \(F\cup\{p\}\), (2) forces every omitted coordinate to vanish. Thus (6) holds. The differing port cogirth values are the independently proved four-element star cocircuits in the full double-line-graph model and seven-element reversal cocircuits in the alternating-port triple-state model. \(\square\)

For clarity, the vertex sets of \(H_{\rm full}\) and \(H_{\rm leg}\) both have size \(n\binom{n-1}{2}\), while
\[
|E(H_{\rm full})|=\binom n2\binom{2(n-2)}2,\quad
|F|=\frac{n(n-1)(n-2)(n-3)}2,\quad
|T|=\frac{n(n-1)(n-2)^2}2.
\tag{7}
\]
All \(|T|\) omitted coordinates are recoverable using at most three coordinates each, as in Theorem 1.

**Corollary 3 (common bounded-reconstruction axiom).** More generally, let a two-sheeted turn cover be given, and distinguish a spanning legal-turn subgraph \(H'\subseteq H\). Suppose for each excluded turn \(e\) there is a cycle \(C_e\subseteq H\) of trivial covering monodromy, containing \(e\), with \(C_e\setminus\{e\}\subseteq E(H')\) and \(|C_e|\le L+1\). Then contraction onto the legal-turn pointed matroid induces a linear isomorphism of the binary cycle spaces, with every omitted coordinate recoverable by a parity expression of length at most \(L\). The cube has no omitted turns (\(L=0\)); ordinary boundary 3-tournaments satisfy this axiom with \(L=3\).

*Proof.* Each \(C_e\) is a non-port cocircuit of the pointed dual. Orthogonality expresses the deleted coordinate as the parity sum of the remaining coordinates of \(C_e\). These identities establish injectivity of restriction; surjectivity follows from contraction. \(\square\)

The theorem supplies an intrinsic matroidal compatibility requirement missing from arbitrary signed-cover proposals: **legal-turn contraction with bounded non-port cocircuit certificates**. It preserves all color information, but does not by itself prove any long monochromatic resource-simple path. In particular, small port cogirth of the full-turn matroid cannot substitute for the distinguished long port cocircuits of the legal-turn model.

**Sharpness.** For an omitted return turn joining triples (w,u,v) and (u,v,w), the first state has legal neighbors (u,v,x) and (x,w,u), while the second has legal neighbors (v,w,y) and (y,u,v), with x,y outside {u,v,w}. These neighbor sets are disjoint, and the endpoints are not legally adjacent. Their legal-turn distance is three, so the reconstruction bound cannot be reduced to two.

**Theorem 5 (local-port diameter principle).** Let \(\widetilde G\to G\) be a connected regular two-sheeted graph cover with edge-free deck action. At every cover vertex \(v\), let \(A_v\) be a graph on the incident cover edges; an edge of \(A_v\) indicates that the corresponding turn is permitted. Assume the collection \(\{A_v\}\) is equivariant under the deck involution and that each \(A_v\) is connected of diameter at most \(L\). Let \(H_{\rm all}=L(G)\), let \(H_{\rm perm}\) retain only permitted turns, and define their pointed binary line-cover duals \(D_{\rm all}\) and \(D_{\rm perm}\). Then
\[
\boxed{D_{\rm perm}=D_{\rm all}/(E(H_{\rm all})\setminus E(H_{\rm perm})),}
\]
and restriction is a binary linear isomorphism \(Z(D_{\rm all})\cong Z(D_{\rm perm})\). Every omitted turn \(e\) has a non-port cocircuit certificate containing \(e\), containing no other omitted turns, and having at most \(L+1\) elements.

*Proof.* An omitted turn is an incident-edge pair \(s,t\) at some lifted vertex \(v\). Choose a shortest path \(s=s_0,s_1,\ldots,s_k=t\) in the local permitted-turn graph \(A_v\), where \(k\le L\). The path together with the omitted turn is a simple cycle of the full line graph, since the incident edge states are distinct. Its projection remains simple: two distinct edges incident at \(v\) cannot be deck translates, as the translates are incident at the distinct vertex \(\tau v\), and a deck-invariant cover edge is excluded. The projected cycle has monodromy zero because its lift closes. It therefore provides the required non-port cocircuit of \(D_{\rm all}\). Orthogonality reconstructs the omitted coordinate as a parity sum over the \(k\) permitted turns. The matrix for the permitted-turn dual is the restriction of the full primal matrix to permitted columns together with the port. Duality proves the contraction identity, and these reconstruction relations make its binary cycle-space projection injective, hence an isomorphism. \(\square\)

The local graph for cube turns is \(K_n\): every pair of incident coordinate edges is a permitted turn, so no turn is omitted. At an ordered-pair state \((u,v)\) in the boundary cover, the incident triples split into \(r=n-2\) incoming and \(r\) outgoing states, indexed by the remaining symbols. Permitted turns form
\[
\boxed{A_{(u,v)}=K_{r,r}\setminus\{\text{the }r\text{ matched pairs}\}.}
\]
For \(r\ge3\), this graph has diameter three: vertices on the same side have a common neighbor, unmatched opposite vertices are adjacent, and matched opposite vertices have a three-edge path but no shorter path. Thus Theorem 1 is an instance of Theorem 5 with \(L=3\).

**Consequence for generalization.** A common intrinsic hypothesis worth retaining is *bounded-diameter deck-equivariant local-port completion*. It guarantees that the colored pointed matroid can be reduced to permitted turns without information loss. It does not guarantee a long independent-resource path; that stronger selector still requires compatible global path exchange and the auxiliary resource constraints.

**Theorem 6 (quantitative port-cocircuit transport).** Under the hypotheses of Theorem 5, let \(X\in Z(D_{\rm all})\) contain the port, and let \(Y=C\cup\{p\}\) be any port cocircuit of \(D_{\rm all}\). Write \(r=|C|\), let \(t=|C\cap(E(H_{\rm all})\setminus E(H_{\rm perm}))|\), and let
\[
w_X(C)=|C\cap X|.
\]
There exists a port cocircuit \(Y'=C'\cup\{p\}\) of \(D_{\rm perm}\) such that
\[
\boxed{|C'|\le r+(L-1)t,\qquad
|C'\cap \pi(X)|\le w_X(C)+Lt.}\tag{9}
\]
Equivalently, the port intersection satisfies
\[
\boxed{|\pi(X)\cap Y'|\le |X\cap Y|+Lt.}\tag{10}
\]

*Proof.* For each forbidden turn \(e\in C\), take the permitted path \(P_e\) of length at most \(L\) obtained in Theorem 5, with the closed walk \(e+P_e\) of monodromy zero. In the binary cycle space of the graph \(H_{\rm all}\) set
\[
Z=C\mathbin{\triangle}
\mathop{\triangle}_{e\in C\setminus E(H_{\rm perm})}
(\{e\}\mathbin{\triangle}P_e).
\]
All forbidden edges cancel, so \(Z\) is an Eulerian subgraph of \(H_{\rm perm}\). Since the added cycles have zero monodromy and \(C\) has monodromy one, \(Z\) also has monodromy one. Decompose \(Z\) into edge-disjoint simple cycles. An odd number of these have nonzero monodromy, so choose any such cycle \(C'\). It is a legal-turn port cocircuit after adjoining \(p\). The count of edges in \(Z\) is at most \(r-t+Lt\), which bounds \(|C'|\). Likewise
\[
w_X(Z)\le w_X(C\cap E(H_{\rm perm}))
+\sum_{e\text{ forbidden in }C}w_X(P_e)
\le w_X(C)+Lt,
\]
and the chosen constituent satisfies \(w_X(C')\le w_X(Z)\). This proves (9) and (10). \(\square\)

For boundary tournaments, \(L=3\), hence each forbidden full turn costs at most two additional edges and three additional turn disagreements when a cocircuit is transferred into the alternating-port matroid. The estimate alone does not ensure forward orientation, resource simplicity, or long witness length. It instead isolates an actionable obstruction to lifting matroidal intersection bounds: the **forbidden-turn count of the chosen cocircuit**.

**Corollary 7 (parity-improved transport).** The turn-weight estimate in Theorem 6 can be strengthened to
\[
\boxed{|C'\cap\pi(X)|\le w_X(C)+2\lfloor L/2\rfloor\,t,}
\qquad
\boxed{|\pi(X)\cap Y'|\le |X\cap Y|+2\lfloor L/2\rfloor\,t.}
\tag{11}
\]
In particular, the boundary legal-turn contraction with \(L=3\) incurs at most **two**, rather than three, additional color changes per omitted turn of the original cocircuit.

*Proof.* The reconstruction cycle \(\{e\}\cup P_e\) has monodromy zero, so it meets every port-containing binary cycle evenly. Therefore
\[
w_X(P_e)\equiv\mathbf1_X(e)\pmod2.
\]
Because \(w_X(P_e)\le |P_e|\le L\) and \(\mathbf1_X(e)\in\{0,1\}\), the increase
\[
w_X(P_e)-\mathbf1_X(e)
\]
is an even integer no larger than \(2\lfloor L/2\rfloor\). In the proof of Theorem 6, sum these increases over the \(t\) replaced edges before selecting an odd-monodromy cycle constituent. \(\square\)

### Five-cycle turn-density and six-resource port intersections

Let \(b(a,v,c)\in\mathbb F_2\) be an arbitrary ordinary boundary 3-tournament on a vertex set \(V\) of size \(n\ge5\), with \(b(c,v,a)=1+b(a,v,c)\). Let \(\widetilde H_V\) have ordered-triple vertices \((a,v,c)\) and edges from \((a,v,c)\) to \((v,c,d)\) whenever all four symbols are distinct. Reversal \(J(a,v,c)=(c,v,a)\) gives a connected double cover of the quotient graph \(H_V\), whose turn cochain is
\[
d_b([\{t,t'\}])=b(t)+b(t')\in\mathbb F_2.
\tag{1}
\]
Its port cycle in the pointed binary matroid of the preceding Subsections is \(X_b=\operatorname{supp}(d_b)\cup\{p\}\).

**Theorem 1 (hereditary five-cycle turn-density bound).** For every \(n\ge5\),
\[
\boxed{|\operatorname{supp}(d_b)|\le \frac45|E(H_V)|=\frac25(n)_4.}
\tag{2}
\]
The same inequality holds on the graph induced by any subset of at least five original vertices.

*Proof.* For five pairwise distinct vertices \(a,b,c,d,e\), the five ordered-triple states
\[
(a,b,c),(b,c,d),(c,d,e),(d,e,a),(e,a,b)
\tag{3}
\]
form a closed five-cycle in the lifted state graph. The sum of its five turn labels in \(\mathbb F_2\) telescopes to zero. Thus the integer number of changed turns is even and at most four. Averaging over uniformly random ordered quintuples, every directed overlap of four distinct symbols appears equally frequently by the transitive action of the symmetric group, and reversal preserves the turn cochain. Consequently the expected fraction of changed turns in (3) is \(|\operatorname{supp}(d_b)|/|E(H_V)|\le4/5\). Since \(|E(H_V)|=(n)_4/2\), (2) follows. Restricting the argument to any vertex subset proves hereditariness. \(\square\)

For an injective six-vertex word \(v=(v_1,\ldots,v_6)\), the boundary twisted-closure lemma constructs the following state sequence, ending at the reversal of the first state:
\[
\begin{split}
&(v_1,v_2,v_3),(v_2,v_3,v_4),(v_3,v_4,v_5),
(v_4,v_5,v_6),\\
&(v_5,v_6,v_3),(v_6,v_3,v_2),(v_3,v_2,v_1).
\end{split}
\tag{4}
\]
Its projection \(C_v\) is a simple monodromy-one six-cycle. Therefore \(Y_v=C_v\cup\{p\}\) is a *resource-simple marked port cocircuit of size seven*, whether or not it has minimum size in the unrestricted pointed matroid.

**Theorem 2 (all-dimensional six-resource intersection with abundance).** In every ordinary boundary tournament on \(n\ge6\) vertices, for every six-element subset \(S\subseteq V\), at least **36** of the \(6!=720\) permutations \(v\) of \(S\) yield
\[
\boxed{|X_b\cap Y_v|\le4,\qquad |Y_v|=7.}
\tag{5}
\]

*Proof.* Fix \(S\), and choose a permutation \(v\) uniformly. Each of the six turn positions in (4) is individually uniform among the edges of \(H_S\): all involve four distinct original vertices, and the \(S_6\)-action is transitive on their reversal-orbits. Write
\(w(v)=|X_b\cap Y_v|-1=\sum_{t\in C_v}d_b(t)\)
with the sum taken as an integer. By Theorem 1,
\[
\boxed{\mathbb E_v\,w(v)
=6\frac{|\operatorname{supp}(d_b|_{H_S})|}{|E(H_S)|}
\le\frac{24}{5}<5.}
\tag{6}
\]
Odd covering monodromy makes \(w(v)\) odd; six turns restrict \(w(v)\) to \(\{1,3,5\}\). Therefore some \(v\) has \(w(v)\le3\), giving (5). In fact, the total deficit is
\[
\sum_{v\in\mathfrak S(S)}(5-w(v))
\ge720(5-24/5)=144.
\]
Every word with \(w(v)\le3\) contributes at most four to this deficit, and every other contributes zero. Hence there are at least \(144/4=36\) marked four-intersection witnesses. \(\square\)

**Corollary 3 (a uniform finite-range consequence).** The canonical boundary case \(q=3\) of the seam-controlled resource-gallery conjecture, requiring a marked port cocircuit with intersection at most four and \(m\ge\max\{6,\lceil\sqrt n\rceil\}\) distinct original vertices, holds whenever
\[
\boxed{6\le n\le36.}
\tag{7}
\]
Indeed, any six-subset supplies \(m=6\) and Theorem 2 gives the intersection bound.

**Proposition 4 (sharpness of five-cycle averaging).** Take \(V=\{0,1,2,3,4\}\). Index the 30 reversal-orbits of ordered triples by increasing middle entry followed by lexicographically increasing outer pair \(a<c\). Set the color on each representative equal to the corresponding bit of
\[
\boxed{M=\mathrm{0x3ed25058},}
\tag{8}
\]
and color its reversal by the complementary bit. On all \(5!=120\) cyclic five-vertex words, the five-state turn count is four; the density in (2) is therefore \(4/5\). No full five-vertex tight word is monochromatic.

*Proof (complete finite certificate).* The following standard-library program enumerates all 120 words and checks the cyclic switch histogram \(4:120\) and ordinary three-triple-color switch histogram \(1:48,\,2:72\).

    from itertools import permutations, combinations
    V=range(5)
    reps=[(a,b,c) for b in V
          for a,c in combinations([u for u in V if u!=b],2)]
    assert len(reps)==30
    idx={t:i for i,t in enumerate(reps)}
    M=0x3ed25058
    def b(a,v,c):
        t=(a,v,c) if a<c else (c,v,a)
        return ((M>>idx[t])&1)^int(a>c)
    cyclic={0:0,2:0,4:0}
    ordinary={0:0,1:0,2:0}
    for v in permutations(V):
        z=[b(v[i],v[(i+1)%5],v[(i+2)%5]) for i in range(5)]
        cyclic[sum(z[i]!=z[(i+1)%5] for i in range(5))]+=1
        ordinary[sum(z[i]!=z[i+1] for i in range(2))]+=1
    assert cyclic=={0:0,2:0,4:120}
    assert ordinary=={0:0,1:48,2:72}

This example shows that a stronger all-order density bound cannot follow from parity on isolated five-cycles alone. \(\square\)

**Seam-control limitation.** These theorems control the total number of changes around a six-turn twisted cycle, not their placement. At port intersection four, the seam identity
\[
|X_b\cap Y_v|-1=s(v)+h(v)=3
\]
allows \((s,h)=(3,0),(2,1),(1,2),(0,3)\), where \(s\) is the number of original internal turns and \(h\) counts the three closing seams. The following Subsection proves that tail reflection preserves the marked cocircuit and, on six resources, interchanges the internal and seam switch counts. Consequently the present density theorem **does** yield a one-turn path on every induced six-set after this reflection is applied. For longer galleries, the reflection leaves a central-defect interval requiring additional resource-preserving exchange.

### Twisted-cycle reflection and the six-resource one-turn theorem

The preceding Subsection establishes that every induced six-vertex ordinary boundary 3-tournament admits at least 36 marked port cocircuits of size seven with port-cycle intersection at most four. We now prove a *re-rooting symmetry of the marked cocircuit itself* that converts this aggregate intersection bound into a **one-turn path theorem**. The symmetry works at every resource length; in larger dimensions it identifies the central-defect obstruction to the same conversion.

#### Tail reflection of a resource-simple word

Fix \(m\ge6\), and let \(v=(v_1,\ldots,v_m)\) be an injective word on distinct original vertices. Put
\[
R(v)=(v_1,v_2,v_3,v_m,v_{m-1},\ldots,v_4).
\tag{1}
\]
The twisted closing construction associates to \(v\) a lifted state path
\[
\begin{split}
P_v:\quad
&(v_1,v_2,v_3),(v_2,v_3,v_4),\ldots,
(v_{m-2},v_{m-1},v_m),\\
&(v_{m-1},v_m,v_3),(v_m,v_3,v_2),(v_3,v_2,v_1).
\end{split}
\tag{2}
\]
It has \(m\) transition edges, the last state being the reversal \(J\) of the first. Its projection is a simple odd-monodromy cycle \(C_v\) and \(Y_v=C_v\cup\{p\}\) is a distinguished port cocircuit.

**Theorem 1 (twisted-cycle tail-reflection symmetry).** For every injective word \(v\) of length \(m\ge6\), the words \(v\) and \(R(v)\) define the **same** distinguished port cocircuit:
\[
\boxed{C_{R(v)}=C_v,\qquad Y_{R(v)}=Y_v.}
\tag{3}
\]
Their projected cyclic turn-edge sequences are traversed in opposite order. If \(e_1,\ldots,e_m\) are the successive turn edges of the cycle built from (2), then those of \(R(v)\) are
\[
\boxed{e_m,e_{m-1},\ldots,e_1.}
\tag{4}
\]

*Proof.* Write the nonterminal states of (2) as \(t_1,\ldots,t_{m-2},s_1,s_2\), where \(t_i=(v_i,v_{i+1},v_{i+2})\), \(s_1=(v_{m-1},v_m,v_3)\), and \(s_2=(v_m,v_3,v_2)\). Applying the twisted closing construction to (1) yields the lifted state sequence
\[
t_1,\ Js_2,\ Js_1,\ Jt_{m-2},\
Jt_{m-3},\ldots,Jt_2,\ Jt_1.
\tag{5}
\]
Every transition in (5) is the \(J\)-image of one of the transitions of (2), traversed backward. Applying the quotient map identifies each transition with its \(J\)-image, proving (3) and (4). The word \(R(v)\) is injective because it is a permutation of the same resource set; hence the second traversal is a legal boundary tight-path gallery, not merely an abstract reorientation of an inadmissible walk. \(\square\)

#### The terminal-seam exchange identity

For any boundary coloring \(b\), let \(\omega_i=d_b(e_i)\in\{0,1\}\), with the sum of the \(\omega_i\) taken as an integer. The first \(m-3\) edges of (2) are the original tight-path turns, and the final three are closing-seam turns. Define
\[
L=\sum_{i=1}^3\omega_i,\qquad
Z=\sum_{i=4}^{m-3}\omega_i,\qquad
R_0=\sum_{i=m-2}^{m}\omega_i,
\tag{6}
\]
with an empty sum interpreted as zero. Put \(w=\sum_{i=1}^m\omega_i=L+Z+R_0=|X_b\cap Y_v|-1\).

**Theorem 2 (terminal-seam exchange).** The internal and closing switch counts of the two legal words are
\[
\boxed{
s(v)=L+Z,\quad h(v)=R_0,\qquad
s(R(v))=R_0+Z,\quad h(R(v))=L.
}
\tag{7}
\]
In particular,
\[
\boxed{\min\{s(v),s(R(v))\}=Z+\min\{L,R_0\}.}
\tag{8}
\]

*Proof.* The original traversal in Theorem 1 places its internal turn cut immediately after \(e_{m-3}\). The reversed traversal uses the turn order (4); its first \(m-3\) turns comprise old edges \(e_m,\ldots,e_4\), and its last three comprise \(e_3,e_2,e_1\). Counting the nonzero turn labels in these respective intervals gives (7), and taking the minimum gives (8). \(\square\)

When \(w\le3\), the right side of (8) is at most one unless (a) at least two changed turns lie in the central interval \(e_4,\ldots,e_{m-3}\), or (b) there is one central change and one changed turn in each three-edge terminal interval. Thus the sole obstruction to turning **a given low-intersection marked cocircuit** into a one-turn path using its two intrinsic orientations is a central-defect configuration. For \(m=7\) the central interval contains a single edge, so only the balanced pattern \((L,Z,R_0)=(1,1,1)\) remains at weight three.

#### Universal six-resource one-turn theorem

**Theorem 3 (six-vertex one-turn path in every induced six-set).** Every ordinary reversal-odd boundary 3-tournament on \(n\ge6\) vertices has, in **each induced six-element subset** \(S\), a vertex-simple tight path on all six vertices of \(S\) with at most one change among its four ordered-triple colors.

More quantitatively, at least **18** of the 720 orderings of each \(S\) have at most one internal turn.

*Proof.* The preceding five-cycle density theorem produces at least 36 words \(v\) of each six-subset satisfying
\[
w(v)=|X_b\cap Y_v|-1\le3.
\tag{9}
\]
For \(m=6\), the central interval in (6) is empty, so \(Z=0\). Theorem 2 therefore gives
\[
s(v)=L,\qquad s(R(v))=R_0,\qquad
s(v)+s(R(v))=L+R_0=w(v)\le3.
\tag{10}
\]
Since the switch counts are nonnegative integers, at least one of \(v,R(v)\) has at most one internal turn. The map \(v\mapsto R(v)\) is a fixed-point-free involution on the six-vertex permutation set: it fixes the first three symbols and reverses the order of the last three distinct symbols. By Theorem 1, it preserves the set of words satisfying (9). Pairing the at least 36 favorable words under this involution, at least one word per pair is a one-turn word. Hence there are at least \(36/2=18\) such words. \(\square\)

**Corollary 4 (strengthening the canonical \(q=3\) conjecture in the known range).** For all \(6\le n\le36\), every ordinary boundary tournament has a resource-simple gallery on \(m\ge\max\{6,\lceil\sqrt n\rceil\}\) vertices with **at most one internal turn**. The proof chooses \(m=6\) inside an arbitrary induced six-set; it does not assert this bound for \(n>36\).

#### Research consequence

The new reflection shows that the apparent freedom to place switches in the three closing seams is not arbitrary: a single marked cocircuit has two canonical, vertex-simple orientations of the same cycle, and the reflection exchanges its two terminal three-edge intervals. This is a structural property of the boundary gallery language beyond binary matroid orthogonality.

For a marked cocircuit with intersection four, the obstruction to one-turn conversion is now sharply localized to the *central defect* \(Z\) in (6). One can therefore seek a local, resource-preserving adjacent-transposition surgery that reduces \(Z\), or shifts a central changed turn to either terminal interval without increasing the total cyclic weight. A theorem eliminating those central-defect configurations in sufficiently long favorable galleries would strengthen the shared matroid intersection conjecture to produce long one-turn boundary paths. The present theorems prove this mechanism in length six and establish the reflection/central-defect identity in every length; the corresponding growing-length surgery remains open.

### Graphic-nullity extraction from polarized turn galleries

#### 1. A matroid interval-partition lemma

Let \(N\) be a loopless matroid and let \(e_1,\ldots,e_m\) be an ordered sequence of distinct ground-set elements. Parallel resource occurrences are represented by separate parallel elements. Put
\[
\nu=m-r_N(\{e_1,\ldots,e_m\}).
\]

**Lemma 1.** The index interval \([m]\) admits a partition into at most \(\nu+1\) nonempty consecutive intervals, each of whose elements are independent in \(N\).

*Proof.* Traverse the sequence, extending the current independent block whenever possible. If \(e_j\) is dependent on the current block, cut immediately before \(j\) and restart with \(e_j\). The element \(e_j\) lies in the closure of the global prefix \(\{e_1,\ldots,e_{j-1}\}\), so the global rank does not increase at \(j\). Among the \(m\) positions there are precisely \(\nu\) non-rank-increasing indices, since \(N\) is loopless and the first position increases rank. Thus the number of cuts is at most \(\nu\). Each singleton restart is independent by looplessness. \(\square\)

#### 2. Boundary-tournament path defects

Let \(t_1,\ldots,t_m\) be distinct ordered-triple states with legal consecutive transitions: each is either a forward transition
\[
(a,b,c)\longrightarrow(b,c,d),
\]
or a backward transition
\[
(a,b,c)\longrightarrow(d,a,b),
\]
where the four letters displayed in a transition are pairwise distinct. A binary coloring \(c(t_i)\) is arbitrary. Let \(s\) be the number of changes in the state-color word, and let \(h\) be the number of changes between forward and backward transition polarities, with \(h=0\) for \(m\le2\).

Cut at each polarity change, leaving at most \(h+1\) blocks of states. Reverse the order of every backward block. Each resulting block is the sequence of consecutive length-three windows of a word \(w\), of length equal to the number of states plus two. For each occurrence of a consecutive pair of letters in \(w\), use a separately labelled edge of the multigraph on the original resource alphabet. Since the word is a walk, its graphic nullity is
\[
\nu(w)=(|w|-1)-(|\operatorname{supp}(w)|-1)=|w|-|\operatorname{supp}(w)|.
\]
Let \(R\) be the sum of these nullities over all polarity-homogeneous blocks.

**Theorem 2 (lossless defect extraction).** The gallery contains a contiguous state interval of length at least
\[
\boxed{\left\lceil\frac{m}{1+s+h+R}\right\rceil}
\tag{1}
\]
whose states are monochromatic, whose transitions all have the same polarity, and whose decoded resource word has no repeated letter. Consequently, for an ordinary reversal-odd boundary tournament, there is a monochromatic forward vertex-simple tight path on at least
\[
\boxed{2+\left\lceil\frac{m}{1+s+h+R}\right\rceil}
\tag{2}
\]
original vertices.

*Proof.* Within each polarity block, orient its states forward. Greedily append triple windows to a current segment as long as the newly appended last letter is not already among that segment's resource letters. If repetition would occur, cut immediately before the new triple and restart at that triple. The new triple has three distinct letters. Every greedy cut is charged to a non-rank-increasing edge occurrence of the full resource walk, hence at most \(\nu(w)\) cuts are required in that block, by Lemma 1. Across all blocks there are at most \(h+R\) cuts. Additionally cut at the \(s\) color changes, obtaining at most \(1+s+h+R\) nonempty contiguous state segments. Every original state is retained; there is no deduction from the numerator \(m\). The largest segment has at least (1) states. Reversing a backward segment yields a forward triple-window word on the same distinct resources. Under reversal oddness, reversing the complete resource word complements every triple color, so a negative monochromatic word yields a positive one of the same length if needed. \(\square\)

#### 3. Port-cocircuit extraction

Let \(D_{\rm BT}\) be the pointed binary dual of the alternating-port ordered-triple covering graph, and let \(X\in Z(D_{\rm BT})\) contain its port \(p\). Every port cocircuit is \(Y=C\cup\{p\}\), with \(C\) a simple odd-monodromy quotient-state cycle. Put \(r=|C|=|Y|-1\).

Every cyclic root and orientation \(\rho\) of \(C\) lifts to a state walk
\[
t_0,t_1,\ldots,t_r=Jt_0
\]
with \(r\) distinct quotient-state representatives \(t_0,\ldots,t_{r-1}\). Let \(s_\rho\) be the number of color changes among these \(r\) states, and let \(h_\rho,R_\rho\) be the polarity-change and resource-nullity defects of Theorem 2. Put
\[
\Delta(C)=\min_\rho(h_\rho+R_\rho).
\]

**Corollary 3 (defect-weighted port-cocircuit decoding).** Every \(Y\) and \(X\) as above yield a monochromatic vertex-simple tight path on at least
\[
\boxed{
2+\left\lceil\frac{|Y|-1}{|X\cap Y|+\Delta(C)}\right\rceil
}
\tag{3}
\]
original vertices.

*Proof.* The integer intersection \(w=|X\cap Y|-1\) counts all changed turns on the odd-monodromy closed cycle, while the rooted \(r\)-state path omits the closing turn. Hence \(s_\rho\le w\). Choose a root minimizing \(h_\rho+R_\rho\); Theorem 2 supplies a segment of length at least
\[
\left\lceil\frac r{1+s_\rho+h_\rho+R_\rho}\right\rceil
\ge \left\lceil\frac r{|X\cap Y|+\Delta(C)}\right\rceil.
\]
Translate triple-state count into the two additional vertices of its resource word. \(\square\)

The defect \(\Delta(C)\) depends on the directed resource-labelled covering presentation and is not an invariant of the abstract pointed matroid alone. Thus optimizing \(|X\cap Y|\) over all shortest port cocircuits cannot substitute for optimizing over admissible long-path representatives.

#### 4. Parallel cube decoding

Let \(D_n\) denote the pointed matroid for an antipodally odd cube-edge coloring. For any port cocircuit \(Y=C\cup\{p\}\), put \(r=|C|\) and lift a cyclic root of \(C\) to \(r\) colored cube-edge states \(e_0,\ldots,e_{r-1}\), followed by the deck translate of \(e_0\). A consecutive turn specifies which endpoint its two cube-edge states share.

An internal edge state is a **stationary contact** if its preceding and following turns use the same endpoint of that cube edge. Let \(h_\rho\) be the number of such contacts in a rooted lift. Splitting the state sequence at the contacts yields coherent cube walks. For each coherent block, regard each occurrence of a coordinate direction as a different element in a parallel class of the partition matroid having capacity one for every coordinate. Let \(\nu_\rho\) be the sum of the nullities of these coordinate sequences. Let \(s_\rho\) be the number of internal color changes.

**Theorem 4 (common defect extraction).** For either the cube or the boundary covering, every port cocircuit \(Y=C\cup\{p\}\) and every admissible port cycle \(X\) yield a monochromatic resource-simple path of at least
\[
\boxed{\left\lceil\frac{|C|}{1+\min_\rho(s_\rho+h_\rho+\nu_\rho)}\right\rceil}
\tag{4}
\]
colored states. In the cube, this is a geodesic with that many edges; in the boundary model, this is a vertex-simple tight path with that many triple windows, hence two additional original vertices.

*Proof.* For the cube, divide the lifted sequence at stationary contacts to obtain coherent cube walks, with at most \(h_\rho\) cuts. The partition-matroid version of Lemma 1 divides each walk into at most one plus its coordinate-nullity many direction-distinct subwalks. Cuts at the \(s_\rho\) color changes complete a partition into no more than \(1+s_\rho+h_\rho+\nu_\rho\) nonempty monochromatic geodesic segments. The boundary case is Theorem 2, with its graphic resource matroid and transition-polarity defect. Optimize over cyclic roots and orientations. \(\square\)

**Corollary 5 (shortest cube port cocircuit).** If \(Y\) is a shortest port cocircuit of \(D_n\), so \(|C|=n\), then its lift is an antipodal geodesic: the cube-distance lower bound eliminates stationary contacts and repeated directions. Thus \(h_\rho=\nu_\rho=0\). If \(|X\cap Y|=2\), the cyclic turn word has one changed turn; root the cycle at that turn, leaving \(n\) consecutive monochromatic cube edges. This is the monochromatic-geodesic conclusion of NORI1 for that \(X\).

Theorem 4 and Corollary 3 are unconditional extraction statements. They do not establish the existence of a sufficiently long, sufficiently low-defect port cocircuit.

#### 5. Defect-bounded selector target

The pair of canonical systems motivates a pointed signed-cover matroid equipped with an oriented path language and an auxiliary resource matroid. A proposed global selector principle asks for port cocircuits with growing turn length while controlling the sum
\[
\boxed{\text{color intersection}+\text{coherence defect}+\text{resource nullity}.}
\]
Its substantive missing component is an existence theorem producing such cocircuits uniformly in ambient size. The auxiliary data cannot simply be discarded: the marked-cocircuit counterexamples in Article XI show that low intersection without forward coherence and resource simplicity does not produce the desired boundary tight path.

#### 6. Cyclic seam optimization and contact-curvature coupling

The defect extraction of Theorem 4 can be sharpened by treating cyclic roots as choices of an omitted closing turn, rather than bounding the number of internal switches independently.

Let \(Y=C\cup\{p\}\) be any port cocircuit of a signed line-cover dual, let \(r=|C|\), and lift its odd-monodromy cycle to edge states
\[
e_0,e_1,\ldots,e_{r-1},e_r=Je_0.
\]
Indices of projected states and turns are taken modulo \(r\). Write \(\omega_i\in\{0,1\}\) for the color disagreement on the turn \(e_i--e_{i+1}\) and \(w=\sum_i\omega_i=|X\cap Y|-1\). Let \(v_i\) denote the contact vertex of that turn; set \(v_{-1}=Jv_{r-1}\). Define
\[
z_i=\mathbf 1_{\{v_{i-1}=v_i\}},\qquad
\sigma=\sum_{i=0}^{r-1}z_i.
\tag{5}
\]
Thus \(z_i=1\) when the two cyclic contacts of the edge state \(e_i\) use the same endpoint.

**Theorem 6 (cyclic seam-defect identity).** Root the lifted cycle immediately after turn \(i\), omitting that turn from the resulting \(r\)-state path. Let \(s_i\) be its internal color-change count, and \(h_i\) its internal stationary-contact count. Then
\[
\boxed{s_i=w-\omega_i,\qquad
h_i=\sigma-z_i-z_{i+1},}
\tag{6}
\]
and therefore
\[
\boxed{
\min_i(s_i+h_i)
=w+\sigma-\max_i(\omega_i+z_i+z_{i+1}).}
\tag{7}
\]
Consequently
\[
\min_i(s_i+h_i)\le
w+\sigma-
\left\lceil\frac{w+2\sigma}{r}\right\rceil.
\tag{8}
\]
The formula holds in either canonical model. In the ordered-triple covering, the internal stationary-contact count \(h_i\) equals the number of changes between forward and backward transition polarities.

*Proof.* Omitting turn \(i\) deletes its color-change contribution \(\omega_i\) from the cyclic sum \(w\). The rooted state path begins at \(e_{i+1}\) and ends at a deck translate of \(e_i\); its internal states are all the other \(r-2\) cyclic states. Precisely the two endpoint-state stationary indicators \(z_{i+1}\) and \(z_i\) are excluded, proving (6). Taking minima proves (7). Summing the seam benefits over all \(i\) gives \(\sum_i(\omega_i+z_i+z_{i+1})=w+2\sigma\), so their maximum is at least the ceiling of their mean, yielding (8).

For the boundary model, a forward triple-overlap transition traverses the middle covering edge from its tail to its head, while a backward transition traverses it oppositely. At an internal triple state, successive transition polarities agree if and only if the preceding and following contacts use opposite endpoints. Thus a polarity change is equivalent to a stationary contact. \(\square\)

The two-port orientation-curvature construction already present in Article XI records \(\sigma\bmod2\) as the intrinsic line-graph contact-curvature class \(\kappa_G(C)\). Equations (6)–(8) refine that parity-only invariant to an integer contact profile and isolate the role of the closing seam. If \(\nu_i\) is the resource-matroid nullity defect at root \(i\), the sharp denominator supplied by Theorem 4 is
\[
\boxed{1+w+\sigma-\max_i(\omega_i+z_i+z_{i+1}-\nu_i).}
\tag{9}
\]
This equality is a restatement of the optimized color/coherence/nullity defect, but it is useful because the first three contributions to the seam score are local and the global obstruction is concentrated in \(\nu_i\).

#### 7. Trimmed-defect extraction and recovery of the marked-seam bound

In the tournament model, a distinguished twisted-closing cocircuit of length \(m\) contains \(m-2\) forward, resource-simple triple states and two auxiliary seam states. Computing the nullity of the full \(m\)-state lift can charge resource repetitions introduced solely by these seams. The following interval variant removes that avoidable loss.

**Corollary 7 (cyclic-interval selector bound).** Let \(Y=C\cup\{p\}\) be a port cocircuit in either canonical model, and let \(X\) be a port cycle. Choose any cyclic lift and any contiguous interval \(I\) of \(\ell\le |C|\) lifted colored states, with \(\ell\ge1\). Define \(s(I)\), \(h(I)\), and \(\nu(I)\) by the same color, stationary-contact/polarity, and resource-matroid rules as Theorem 4, but counting only the selected interval. Then the instance has a monochromatic resource-simple path with at least
\[
\boxed{
\left\lceil\frac{\ell}{1+s(I)+h(I)+\nu(I)}\right\rceil
}
\tag{10}
\]
colored states. Accordingly one may maximize this quantity over all cyclic roots, orientations, and contiguous intervals of any length.

*Proof.* The chosen interval is itself an admissible state walk, so the partition proof of Theorem 4 applies without change. \(\square\)

**Corollary 8 (the marked boundary seam estimate is retained).** For a twisted closing cycle associated with an injective \(m\)-vertex word \(v\), choose the original \(m-2\) forward triple states and omit the two auxiliary seam states. The selected interval has \(h(I)=\nu(I)=0\), and its internal color changes are at most
\[
w=|X\cap Y|-1.
\]
Therefore it contains a monochromatic vertex-simple tight path on at least
\[
\boxed{2+\left\lceil\frac{m-2}{|X\cap Y|}\right\rceil}
\tag{11}
\]
vertices. In particular intersection at most four implies the earlier bound \(2+\lceil(m-2)/4\rceil\). The full-cycle defect-weighted estimate and the trimmed estimate are complementary: neither should replace the other when optimizing a family of cocircuits.

*Proof.* The original word has distinct resources, and its forward triple states are consecutive windows. No polarity changes or resource dependencies occur inside this interval. Its internal color changes are a subset of the nonzero turn labels of the sealed cycle. Apply (10) and translate state count to vertex count. \(\square\)

This interval formulation suggests a more flexible global selector target: rather than demanding low defect for an entire long port cocircuit, seek a cocircuit that contains a **long low-defect resource interval**. In particular the same criterion incorporates NORI1's full-geodesic interval after removing the unique switched closing seam and the tournament's forward tight subword after discarding its auxiliary closing states.

### Independent port-preserving contractions and fundamental-cocircuit repair

Let \(M\) be a finite binary matroid with a distinguished nonloop \(p\), and let \(T\subseteq E(M)\setminus\{p\}\), with \(S=E(M)\setminus T\). Denote the binary cycle space by \(Z(M)\) and its dual cocycle space by \(Z^*(M)\).

**Theorem 1 (intrinsic faithful-contraction criterion).** Restriction induces a surjective linear map
\[
\pi_T:Z(M)\longrightarrow Z(M/T),\qquad X\longmapsto X\cap S.
\tag{1}
\]
The map is an isomorphism if and only if \(T\) is independent in \(M\). Moreover,
\[
\boxed{T\cup\{p\}\text{ is independent in }M}
\tag{2}
\]
if and only if (1) is an isomorphism and \(p\) remains a nonloop of \(M/T\).

*Proof.* Choose a binary representation \(A\) of \(M\). A cycle of \(M/T\) is a binary dependence of the columns indexed by \(S\) modulo the span of the columns indexed by \(T\). Every such dependence lifts to a cycle of \(M\), proving surjectivity. The kernel comprises cycles of \(M\) supported in \(T\); it is zero precisely when \(T\) contains no circuit, equivalently when \(T\) is independent. Finally \(p\) becomes a loop in \(M/T\) precisely when its representing column lies in the span of the columns of \(T\). In conjunction with independence of \(T\), this is equivalent to dependence of \(T\cup\{p\}\). \(\square\)

**Theorem 2 (port-avoiding fundamental cocircuit certificates).** Assume (2). There is a basis \(B\) of \(M\) containing \(T\cup\{p\}\). For every \(e\in T\), its fundamental cocircuit \(K_e^*\) with respect to \(B\) obeys
\[
\boxed{K_e^*\cap(T\cup\{p\})=\{e\}.}
\tag{3}
\]
Consequently each deleted cycle coordinate is reconstructed by
\[
\boxed{\mathbf1_X(e)=
\sum_{f\in K_e^*\setminus\{e\}}\mathbf1_X(f)\pmod2}
\tag{4}
\]
for every \(X\in Z(M)\). Conversely, if \(p\) is a nonloop and the cocircuits (3) exist for all \(e\in T\), then (2) holds.

*Proof.* Extend the independent set \(T\cup\{p\}\) to a basis \(B\). By definition, \(K_e^*\cap B=\{e\}\), giving (3). Binary cycle–cocircuit orthogonality gives (4). Conversely, if a circuit lies inside \(T\cup\{p\}\), it cannot be \(\{p\}\) because \(p\) is a nonloop. It contains some \(e\in T\), and then its intersection with \(K_e^*\) has size one, contrary to binary orthogonality. Therefore \(T\cup\{p\}\) is independent. \(\square\)

The criterion is an intrinsic property of the pointed matroid and the selected contraction set; it involves neither a graph representation nor a covering. The local-port-diameter theorem of the previous Subsection supplies the stronger **bounded-size** certificates (3) in the two canonical graph-cover models.

**Theorem 3 (intrinsic quantitative port-cocircuit transfer).** Under (2), suppose that cocircuit certificates \(K_e^*\) can be chosen for all \(e\in T\) satisfying (3) and \(|K_e^*|\le L+1\), for an integer \(L\ge1\). For any binary cycle \(X\in Z(M)\) containing \(p\), and any cocircuit \(Y\in\mathcal C^*(M)\) containing \(p\), let \(t=|Y\cap T|\) and put \(X'=\pi_T(X)\). Then there exists a port cocircuit \(Y'\in\mathcal C^*(M/T)\) such that
\[
\boxed{|Y'|\le |Y|+(L-1)t,}
\tag{5}
\]
and
\[
\boxed{|X'\cap Y'|\le
|X\cap Y|+2\left\lfloor\frac L2\right\rfloor t.}
\tag{6}
\]
No graph-cover realization is required for this theorem.

*Proof.* Cocycle vectors form a binary vector space, so take
\[
Z=Y\mathbin{\triangle}
\mathop{\triangle}_{e\in Y\cap T}K_e^*.
\tag{7}
\]
Every \(K_e^*\) meets \(T\) solely in \(e\) and avoids \(p\). Hence \(Z\) is a cocycle avoiding \(T\) and containing \(p\). A binary cocycle decomposes into a disjoint union of cocircuits; at least one constituent \(Y'\) contains \(p\). Since \(Y'\subseteq S\), it is a cocircuit of \(M/T\). Formula (7) replaces \(t\) deleted elements with at most \(Lt\) surviving elements, proving (5).

For the weight bound, put \(v_e=\mathbf1_X(e)\) and \(R_e=K_e^*\setminus\{e\}\). Since \(K_e^*\) is a cocircuit, binary orthogonality gives
\[
|X\cap R_e|\equiv v_e\pmod2.
\tag{8}
\]
Also \(|R_e|\le L\). Consequently
\[
|X\cap R_e|-v_e\le2\lfloor L/2\rfloor.
\tag{9}
\]
Using symmetric-difference subadditivity for the integer overlap weight and summing (9) over the replaced elements gives
\[
|X\cap Z|
\le |X\cap Y|+2\lfloor L/2\rfloor t.
\]
Since \(Y'\subseteq Z\cap S\), and \(X'\) is the restriction of \(X\), (6) follows. \(\square\)

**Corollary 4 (the signed-cover cases).** For the cube all turns are admissible, so take \(T=\varnothing\). For the boundary graph cover, delete inadmissible turns; the local-port completion theorem supplies certificates \(K_e^*\) of size at most four, avoiding \(p\) and meeting \(T\) only at \(e\). Thus \(T\cup\{p\}\) is independent, and (5)–(6) recover the boundary transfer bounds
\[
|Y'|\le |Y|+2t,\qquad
|X'\cap Y'|\le|X\cap Y|+2t.
\]

**Generalization hypothesis.** The combination of (i) a binary pointed matroid, (ii) a port-preserving independent contraction \(T\), (iii) uniformly short fundamental cocircuit certificates, and (iv) a directed resource-independent path language gives an intrinsic matroidal starting point for a common path-selector conjecture. Parts (i)–(iii) provide faithful passage from unrestricted to admissible turns and quantitative control of port cocircuit intersection. Part (iv) is essential for converting the resulting cocircuits to forward, resource-simple witnesses.

#### 4. Bipointed sector cohesion: the missing condition

Theorem 3 transfers cocircuits containing a **single** distinguished port. For two ports \(p,q\), it need not transfer a cocircuit containing both ports, even if \(T\cup\{p,q\}\) is independent: the repaired cocycle can split into cocircuits that separate \(p\) and \(q\). A four-vertex diamond-graph counterexample is retained in the linked research notes.

**Theorem 5 (cocycle-support port-cohesion criterion).** Let \(M\) be any matroid, and let \(Z\in Z^*(M)\) be a nonempty cocycle containing distinct designated elements \(p,q\). There exists a cocircuit \(Y\subseteq Z\) containing both \(p\) and \(q\) if and only if \(p,q\) lie in the same connected component of the restricted dual matroid
\[
\boxed{M^*|Z.}\tag{10}
\]

*Proof.* The cocircuits of \(M\) contained in \(Z\) are precisely the circuits of \(M^*|Z\). In any matroid, two different elements lie in a common connected component if and only if some circuit contains both. Substituting the dual circuits proves the assertion. \(\square\)

**Corollary 6 (conditional two-port quantitative transfer).** Assume \(T\cup\{p,q\}\) is independent and every \(e\in T\) admits a fundamental cocircuit certificate of size at most \(L+1\) meeting \(T\cup\{p,q\}\) solely in \(e\). Let \(Y\) be a cocircuit containing both \(p,q\), and form the repaired cocycle \(Z\) by (7), with \(t=|Y\cap T|\). If \(p,q\) remain in the same connected component of \(M^*|Z\), then there exists a cocircuit \(Y'\) of \(M/T\) containing both \(p,q\) and obeying the same length and integer-overlap bounds (5)–(6).

*Proof.* The fundamental cocircuits avoid both ports, so \(Z\) contains \(p,q\) and avoids \(T\); its size and overlap satisfy the estimates already proved for Theorem 3. Theorem 5 supplies a cocircuit \(Y'\subseteq Z\) containing both ports. It is also a cocircuit of \(M/T\) because it avoids \(T\), and restricting the overlap to \(Y'\) cannot increase it. \(\square\)

Thus a bipointed extension requires **cocycle-support port cohesion**, not merely survival and independence of two ports. This is a natural dual-matroid connectivity condition, and it pinpoints the obstruction to preserving the orientation-curvature cocircuit sector of Article XI under contraction.

### Spanning one-turn galleries and opposite-terminal monochromatic packing

#### 1. The strengthened target replaces the square-root resource bound

For a reversal-odd ordinary boundary 3-tournament, a vertex-simple tight path is an injective ordering \(v=(v_1,\ldots,v_n)\) of all original vertices with ordered triple-color word
\[
b(v_1,v_2,v_3),\ b(v_2,v_3,v_4),\ldots,\ b(v_{n-2},v_{n-1},v_n).
\]
Its **internal turn count** is
\[
s_b(v)=\sum_{i=1}^{n-3}[b(v_i,v_{i+1},v_{i+2})\ne b(v_{i+1},v_{i+2},v_{i+3})].
\tag{1}
\]

**Conjecture 1 (spanning one-turn boundary-tournament conjecture).** Every ordinary reversal-odd boundary 3-tournament on \(n\ge3\) vertices admits an injective ordering of all its vertices with
\[
\boxed{s_b(v)\le1.}
\tag{2}
\]
This is an open assertion, rather than a consequence of the earlier square-root resource-gallery conjecture. The latter would recover only a classical-scale \(\Omega(\sqrt n)\) monochromatic path, obtainable through elementary longest-path endpoint counting; thus it should not be the principal unification target.

For the cube, the corresponding spanning-gallery assertion is the existence of a complete antipodal geodesic whose edge colors change at most once. The antipodally odd cyclic closing seam turns this into the monochromatic NORI1 target. The two resulting quantitative targets are therefore both **spanning, at most one internal turn** (and in the cube equivalently zero internal turns).

#### 2. Marked full-resource port intersection

Let \(D\) be the pointed binary matroid obtained from the connected reversal-overlap state cover, and \(X_b=\operatorname{supp}(d_b)\cup\{p\}\) its port cycle. The three-turn closing theorem for each injective full word \(v\), \(n\ge6\), yields a simple monodromy-one cycle \(C_v\) and cocircuit \(Y_v=C_v\cup\{p\}\). The **marking** is the ordered cyclic decomposition
\[
C_v=I_v\sqcup S_v
\]
into the \(n-3\) original internal turn edges \(I_v\) and the three ordered closing-seam edges \(S_v\). The unmarked cocircuit \(Y_v\) alone does not record which edges are internal.

**Proposition 2 (equivalent full-resource port criterion).** For \(n\ge6\), Conjecture 1 is equivalent, in the canonical boundary matroid, to the following statement:
\[
\boxed{
\forall X\in Z(D),\ p\in X,\quad
\exists\text{ a marked full-resource cocircuit }(Y_v,S_v):
\quad |X\cap(Y_v\setminus(\{p\}\cup S_v))|\le1.
}
\tag{3}
\]
If \(h_v=|X\cap S_v|\in\{0,1,2,3\}\), (3) is also equivalent to
\[
\boxed{|X\cap Y_v|\le h_v+2.}
\tag{4}
\]
For every marked full-resource cocircuit,
\[
|X\cap Y_v|=1+s_b(v)+h_v,\qquad
s_b(v)+h_v\equiv1\pmod2.
\tag{5}
\]
In particular, a witness to (3) automatically has \(|X\cap Y_v|\in\{2,4\}\). The four permitted pairs \((s_b(v),h_v)\) at most one internal turn are
\[
(0,1),\quad (0,3),\quad (1,0),\quad (1,2).
\tag{6}
\]
Conversely, mere unmarked intersection at most four is insufficient, since at intersection four it also permits \((s,h)=(2,1)\) or \((3,0)\).

*Proof.* The cochain \(d_b\) marks an internal turn precisely when two successive triple colors differ. Hence its support on \(I_v\) counts \(s_b(v)\). On the closing seam it counts \(h_v\). Adding the shared port yields (5), and monodromy-one parity makes the nonport weight odd. Equations (3), (4) and (6) follow by inspection. Every port-containing cycle corresponds to a reversal-odd coloring, up to global color complementation, by the covering reconstruction theorem. \(\square\)

**Proposition 3 (cube one-turn equals zero-turn).** In the canonical cube-edge representation, a complete antipodal geodesic with at most one internal change can be cyclically re-rooted to have zero internal changes.

*Proof.* Its cyclic turn word has the \(n-1\) internal transitions plus the unique closing turn, and its parity is odd by antipodal reversal. If at most one internal turn changes, at most two cyclic turns change; oddness forces one. Rotating the cyclic direction order and adjusting the root makes that unique changed turn the closing seam. The remaining complete geodesic is monochromatic. \(\square\)

This identifies one common *marked* invariant: full independent resource rank and at most one internal disagreement. The cube is the width-one, movable-seam case; boundary tournaments have a width-three fixed seam and need an additional endpoint compatibility mechanism.

#### 3. An equivalent two-arm monochromatic packing theorem

For a color \(\varepsilon\in\{0,1\}\) and an ordered pair \(u\ne v\), let \(\mathcal P^\varepsilon_{uv}\) denote the family of vertex-simple \(\varepsilon\)-monochromatic tight paths whose last two vertices are \((u,v)\). We permit the two-vertex path \((u,v)\), on which the triple-color condition is vacuous.

**Theorem 4 (opposite-terminal packing equivalence).** A boundary 3-tournament on \(V\) admits a vertex-simple *spanning tight path with at most one color change* if and only if there exist distinct \(u,v\in V\), a color \(\varepsilon\), and paths
\[
P\in\mathcal P^\varepsilon_{uv},\qquad Q\in\mathcal P^\varepsilon_{vu}
\]
such that
\[
\boxed{V(P)\cap V(Q)=\{u,v\},\qquad V(P)\cup V(Q)=V.}
\tag{7}
\]
In the presence of a nondegenerate change, neither arm need be vacuous. If the spanning path is monochromatic, one may take one arm to be a two-vertex path. Thus the spanning one-turn conjecture is equivalent to a **spanning opposite-terminal monochromatic two-arm packing conjecture**.

*Proof.* Suppose \(W=(w_1,\ldots,w_n)\) is a one-turn spanning path, and its triple colors change between the windows beginning at positions \(i\) and \(i+1\). Put \(u=w_{i+1},v=w_{i+2}\), take \(P=(w_1,\ldots,w_{i+2})\), and let \(Q=(w_n,\ldots,w_{i+1})\), the reversal of the suffix starting at \(u\). If the original first color is \(\varepsilon\), the original suffix is monochromatic \(1-\varepsilon\), so reversal oddness makes \(Q\) monochromatic \(\varepsilon\). Their ends are \((u,v)\) and \((v,u)\), respectively, and injectivity gives (7).

If \(W\) is monochromatic of color \(\eta\), let \(Q\) be its full reversal (color \(1-\eta\)) and \(P=(w_1,w_2)\), a vacuous path declared to have color \(1-\eta\). Their terminal pairs are opposite, their vertex intersection is \(\{w_1,w_2\}\), and they cover \(V\).

Conversely, let \(P=(p_1,\ldots,p_r,u,v)\), \(Q=(q_1,\ldots,q_s,v,u)\) be as in (7), with possible empty prefixes. Reverse \(Q\), and concatenate with \(P\) along their common ordered pair \((u,v)\) to form
\[
W=(p_1,\ldots,p_r,u,v,q_s,\ldots,q_1).
\]
The vertex sets condition makes \(W\) a permutation of \(V\). All triples lying completely in its left portion have color \(\varepsilon\), while those in its right portion are reversals of the triples of \(Q\) and have color \(1-\varepsilon\). There is no additional triple outside these two windows, because the two portions share the full ordered pair. Thus \(W\) has at most one color change. \(\square\)

**Corollary 5 (graphic-matroid interpretation).** Under (7), the union of the underlying \(K_n\)-edges of the two arms, with the common edge \(\{u,v\}\) counted once, forms a Hamiltonian graph path. It is an independent set of rank \(n-1\), hence a *basis* of the graphic matroid \(M(K_n)\), and its graph degree is at most two. Conversely, a same-color opposite-terminal pair of tight paths whose underlying edges form a Hamiltonian path and satisfy (7) decodes to a spanning at-most-one-turn tight path.

The basis condition alone is not sufficient without the oriented terminal compatibility and path-language requirements. Those are precisely the extra decorations absent from an undecorated binary cycle–cocircuit intersection conjecture.

#### 4. An explicit obstruction to nearly monochromatic cyclic Hamiltonian words

We exhibit an ordinary reversal-odd boundary tournament with a spanning one-turn word but no cyclic Hamiltonian word with at most two changes. This rules out the stronger approach of first finding a nearly monochromatic cyclic ordering and cutting it.

Let \(V=\{0,1,2,3,4,5\}\). Index the 60 representatives of reversal classes of ordered triples by increasing middle vertex, followed by lexicographically increasing unordered outer pair \(a<c\) disjoint from the middle vertex. Define the representative color by its indexed bit of
\[
\boxed{M=\mathrm{0x1418d63f482ff8d},}
\tag{8}
\]
and give the reverse triple the complementary color.

**Proposition 6 (cyclic Hamiltonian obstruction).** Among all \(6!=720\) spanning linear words \(v\), the histogram of internal color-change counts is
\[
\boxed{\#(0)=0,\quad \#(1)=108,\quad\#(2)=360,\quad\#(3)=252.}
\tag{9}
\]
For cyclic triple words \(\bigl(b(v_i,v_{i+1},v_{i+2})\bigr)_{i\in\mathbb Z/6\mathbb Z}\), the cyclic change-count histogram is
\[
\boxed{\#(0)=0,\quad\#(2)=0,\quad\#(4)=576,\quad\#(6)=144.}
\tag{10}
\]
In particular, a spanning one-turn path exists, but no cyclic Hamiltonian triple word has at most two changes.

*Proof (finite certificate).* The following Python 3 code visits every permutation and computes both histograms using the 60-bit indexing:
\`\`\`python
from collections import Counter
from itertools import permutations, combinations

V=range(6)
reps=[(a,b,c) for b in V for a,c in
      combinations([x for x in V if x!=b],2)]
assert len(reps)==60
idx={t:i for i,t in enumerate(reps)}
M=0x1418d63f482ff8d
def col(a,b,c):
    rep=(a,b,c) if a<c else (c,b,a)
    return ((M>>idx[rep])&1)^int(a>c)
linear=Counter()
cyclic=Counter()
for v in permutations(V):
    w=[col(*v[i:i+3]) for i in range(4)]
    linear[sum(w[i]!=w[i+1] for i in range(3))]+=1
    z=[col(v[i],v[(i+1)%6],v[(i+2)%6]) for i in range(6)]
    cyclic[sum(z[i]!=z[(i+1)%6] for i in range(6))]+=1
assert linear==Counter({1:108,2:360,3:252})
assert cyclic==Counter({4:576,6:144})
\`\`\`
The enumeration covers all ordered spanning paths and all cyclic orders (with multiplicity six). Reversal oddness is enforced by the color definition, and the assertions reproduce (9)–(10). \(\square\)

#### 5. Revised research program

The principal **proposed unification** should now be the spanning one-internal-turn assertion (3), equivalently the boundary opposite-terminal packing (7) coupled with cube root rotation. The earlier \(m\ge\sqrt n\), \(|X\cap Y|\le4\) marked-gallery conjecture is a strictly weaker auxiliary statement, since its boundary consequences only recover the classical \(\Omega(\sqrt n)\) monochromatic scale. A stronger bare cyclic Hamiltonian assertion is refuted by Proposition 6.

The key missing step is not controlling total cyclic switch weight but aligning two long same-colored *oppositely oriented* terminal arms without repeated original vertices. Any matroidal route must preserve both graphic independence and ordered-pair compatibility; replacing them by cographic port parity or unmarked cocircuit intersection forfeits the spanning problem. The proof objective is an independence-preserving terminal-pair splice that grows the two disjoint arms to total resource rank \(n-1\).

### NORI Article XI — Two-Port Sector Cogirth and Simultaneous Intersection Selectors

**Research status (October 12, 2026):** The sector-girth formulas and the two-cycle identities below are proved. The rank-growing selector is conjectural.

#### Theorem 1: Identical Cogirth in Both Port Sectors

Let \(D^{(2)}\) be the dual of the binary matroid represented by
\[
\begin{pmatrix}
B_H & 0 & 0\\
a & 1 & 0\\
\lambda & 0 & 1
\end{pmatrix},
\]
with distinguished ports \(p,q\), where \(a\) is the two-cover monodromy class and \(\lambda\) its canonical orientation-curvature class.

Define \(g_{pq}\) to be the smallest cocircuit size among cocircuits containing both \(p,q\), and \(g_{p\bar q}\) among those containing \(p\) but not \(q\).

| Family | \(g_{pq}\) | \(g_{p\bar q}\) |
|---|---:|---:|
| Antipodal \(n\)-cube (\(n\ge3\)) | \(n+2\) | \(n+2\) |
| Boundary tournament (\(n\ge4\)) | \(5\) | \(5\) |

**Cube proof.** Every monodromy-one simple turn cycle \(C\) obeys
\[
|C|=n+s(C)+2u(C),
\]
where \(s(C)\) is the number of stationary contacts and \(u(C)\ge0\) is repeated-coordinate excess. Curvature satisfies \(\lambda(C)\equiv 1+s(C)\pmod2\). The both-port sector (\(\lambda=1\)) permits \(s=0\), achieved by an antipodal geodesic of length \(n\); adding both ports gives \(n+2\). The \(p\)-only sector (\(\lambda=0\)) requires odd \(s\), giving turn length at least \(n+1\). At the first internal turn of the standard monotone cube geodesic, insert the incident cube edge in coordinate three; this is a new antipodal edge orbit, producing a simple odd-monodromy turn cycle of length \(n+1\) and precisely one stationary contact. Adding \(p\) gives \(n+2\).

**Boundary proof.** Every monodromy-one triangle in the quotient \(L^2(K_n)\) is a star triangle of curvature one. It produces a both-port cocircuit of size \(3+2=5\). No monodromy-one triangle has curvature zero. The following four-turn cycle has monodromy one and curvature zero:
\[
(1,0,2), (2,0,3), (1,0,3), (0,1,3)
\]
where each triple denotes its reversal orbit. One lift is
\[
(1,0,2),(3,0,2),(3,0,1),(0,1,3),(2,0,1).
\]
The orientation-defect bits are \(1,1,0,0\). Adjoining only \(p\) yields a cocircuit of size \(4+1=5\).

**Consequence.** For every boundary-tournament coloring cycle \(X_d\), every sector-minimum \(p\)-only cocircuit and every sector-minimum both-port cocircuit meets \(X_d\) in **two or four elements** by binary cycle–cocircuit orthogonality. Thus port membership and sector-minimality still cannot enforce a long tight path.

#### Theorem 2: Simultaneous Coloring and Orientation Objectives

An admissible deck-odd coloring determines \(d=a+\delta f\) and a binary cycle
\[
X_d=\operatorname{supp}(d)\cup\{p\}.
\]
The orientation curvature row determines a second binary cycle
\[
X_{\mathrm{or}}=\operatorname{supp}(\lambda)\cup\{q\}.
\]
For a cocircuit \(Y_C=C\cup\{p\}\) from an odd-monodromy, curvature-zero simple turn cycle \(C\),
\[
|X_d\cap Y_C|=1+\sum_{t\in C}d(t),\qquad
|X_{\mathrm{or}}\cap Y_C|=\sum_{t\in C}\lambda(t)
\]
with integer sums.

The second intersection vanishes **if and only if every turn is locally coherently oriented** (one incoming edge, one outgoing edge). This is stronger than the zero-curvature parity condition, which allows two or more incoherent turns.

The previously established identity \([\lambda]=[a]+[\kappa_F]\) implies
\[
[d+\lambda]=[\kappa_F],
\]
so \(X_d\triangle X_{\mathrm{or}}\) has a cover-independent turn-cohomology class, although it includes both ports.

#### Theorem 3: Coherent Directed Closing Criterion

For a simple odd-monodromy cycle \(C\) of \(H=L(F)\), suppose every local orientation defect is zero and \(s(C)=1\). Reindex the cycle at its unique stationary edge and choose the deck sheet so that the stationary contact occurs at that edge's head. Every subsequent edge must then be traversed from tail to head: the opposite-sense condition at its predecessor and successor forces continuity of the prescribed orientation. The lift is a coherently directed state-edge path ending at the deck reversal of its starting state.

Conversely a coherently directed twisted closing walk has zero local orientation defects and its sole stationary contact occurs at the closing seam.

The resource-simple prefix must still be specified separately. In boundary tournaments it requires independent projected \(K_n\)-edge labels in the graphic matroid \(M(K_n)\). A coherently directed closure can repeat original vertices even when its orientation defect is zero.

#### Conjectural Next Step

A unified theorem should select a marked cocircuit \(Y\), for every admissible coloring cycle \(X_d\), with:

1. Bounded color intersection \(|X_d\cap Y|\le q_{\mathrm{seam}}+1\).
2. Zero orientation intersection \(|X_{\mathrm{or}}\cap Y|=0\) in the directed boundary-tournament model.
3. A coherent pre-seam gallery whose projected resources form an independent set of rank at least \(n^{2/(q_{\mathrm{seam}}+1)}\).

The cube uses a full-rank, both-port witness and seam width one. The boundary tournament uses a \(p\)-only coherent witness and seam width three. Proving a rank-increasing, independence-preserving and orientation-defect-preserving exchange/splicing principle is the principal missing step.

**Finite cross-check:** Enumeration of the boundary \(n=4\) quotient turn graph gives 32 triangles (four in monodromy-one/curvature-one sector) and 81 four-cycles (24 in monodromy-one/curvature-zero sector), consistent with the claimed lower bounds. These counts are corroborating checks, not hypotheses of the proofs.


Let \(G\) be a finite simple graph with a connected two-sheeted cover \(\widetilde G\to G\), and let \(H=L(G)\). Write \(\alpha\) for covering monodromy and \(\kappa\) for the intrinsic line-graph contact-curvature class of Article XI. A turn signature \(d\) is a binary cochain whose sum on every star triangle is zero; this includes every color signature \(d=a+\delta f\).

Fix a vertex \(v\) of \(H\), corresponding to an edge \(xy\) of \(G\). The neighbors of \(v\) split into two cliques \(K_x,K_y\), according to whether their corresponding \(G\)-edges meet \(xy\) at \(x\) or at \(y\). A cycle of \(H\) is *moving at \(v\)* when its two neighbors at \(v\) lie in different cliques.

**Theorem 1 (transverse bouquet smoothing).** Let \(C_1,\ldots,C_k\) be simple cycles of \(H\), \(k\ge2\), pairwise vertex-disjoint except at a single common vertex \(v\), and each moving at \(v\). Then one can construct a simple cycle \(C\) of \(H\), on their vertex union with \(v\) possibly omitted, such that
\[
\boxed{|C|=\sum_{i=1}^k|C_i|-2\lfloor k/2\rfloor,}\tag{1}
\]
\[
\boxed{\alpha(C)=\sum_i\alpha(C_i),\qquad
\kappa(C)=\sum_i\kappa(C_i)\pmod2,}\tag{2}
\]
and for every turn signature \(d\),
\[
\boxed{w_d(C)\le\sum_iw_d(C_i).}\tag{3}
\]
The reduction in (3) is an even nonnegative integer.

*Proof.* Write \(a_i\in K_x,b_i\in K_y\) for the neighbors of \(v\) on \(C_i\). Remove \(v\) from each \(C_i\), leaving mutually vertex-disjoint paths \(P_i\) from \(a_i\) to \(b_i\). All their endpoints are distinct.

When \(k\) is even, add the clique edges \(a_1a_2,a_3a_4,\ldots,a_{k-1}a_k\), and \(b_2b_3,b_4b_5,\ldots,b_kb_1\). The resulting graph is one simple cycle, alternating among the \(P_i\), with length \(\sum_i(|C_i|-2)+k\).

When \(k\) is odd, instead add \(a_1a_2,a_3a_4,\ldots,a_{k-2}a_{k-1}\), and \(b_2b_3,b_4b_5,\ldots,b_{k-1}b_k\), and retain the original edges \(va_k\) and \(vb_1\). These pieces again form one simple cycle, now through \(v\), with length \(\sum_i(|C_i|-2)+(k-1)+2\). Both cases give (1).

Each added edge \(a_ia_j\) replaces the pair \(va_i,va_j\) by the third edge of the star triangle \((v,a_i,a_j)\), and similarly on the \(b\)-side. The number of such triangles is \(k\) in the even case, and \(k-1\) in the odd case; it is even in both. Thus the mod-two sum of their indicators, added to the sum of the indicators of \(C_i\), yields \(C\). On every star triangle, covering monodromy is zero and contact curvature is one. Therefore both cohomology signatures in (2) follow.

Finally, on each replaced star triangle the cocycle condition gives \(d(a_ia_j)=d(va_i)\oplus d(va_j)\). Hence its integer turn cost cannot exceed the sum of the two removed turn costs, and the difference is either zero or two. The same argument applies to all paired neighbors in the other clique. All other edges are retained, giving (3). \(\square\)

**Corollary 2 (two-cycle phase addition).** When \(k=2\), the surgery amalgamates two cycles sharing only one moving contact into one cycle of length \(|C_1|+|C_2|-2\), with additive monodromy and contact-curvature phases, and with no greater total color-disagreement weight. In the two-port lift of Article XI, the \((\alpha,\lambda)\) port signatures therefore add. In particular a cycle of phase \((1,0)\) and one of phase \((0,1)\) can give a single cocircuit of phase \((1,1)\), whenever the required transverse shared-state contact holds.

This supplies a phase-coherent local repair mechanism for splitting port sectors under cocircuit contraction. It does not apply when the cycles fail the transverse intersection condition, and it does not enforce a long forward resource-independent gallery.

**Theorem 3 (mixed-contact splice).** Suppose two simple cycles C1,C2 of H=L(G) meet only at v, with C1 moving and C2 stationary there. Then there exists a simple cycle C with length |C1|+|C2|-1, monodromy alpha(C)=alpha(C1)+alpha(C2), contact curvature kappa(C)=kappa(C1)+kappa(C2)+1 modulo two, and cost w_d(C)<=w_d(C1)+w_d(C2) for every admissible turn signature d. The reduction in cost is zero or two.

*Proof.* Let C1 meet v through neighbors a in the x-clique and b in the y-clique, and let C2 meet v through c,d in the x-clique, relabeling endpoints when necessary. Delete v to leave mutually disjoint paths P1 from a to b and P2 from c to d. Replace the two original incident edges va and vd by the clique edge ad, retaining vb and vc. The resulting walk v-b-P1-a-d-P2-c-v is a simple cycle, with the stated length. Its mod-two edge vector is the sum of those for C1,C2 and the star triangle v,a,d. That triangle has monodromy zero and contact curvature one. Its turn colors satisfy d(ad)=d(va) XOR d(vd), so the cost never increases; the improvement is even. QED.

This is a phase-flipping counterpart to the transverse bouquet theorem: a single balanced star-triangle surgery toggles the curvature port while preserving monodromy, whereas the even number of surgeries in a moving bouquet preserves both port phases.

**Theorem 4 (zero-cost one-triangle curvature extension).** Let \(C\) be a simple cycle of the turn graph \(H=L(G)\), with an edge \(va\) lying inside a vertex-star clique of \(H\). Let \(b\) be another vertex of this clique, not in \(V(C)\). Suppose a prescribed admissible binary turn signature \(d\) satisfies
\[
\boxed{d(vb)=0.}\tag{6}
\]
Replace \(va\) in \(C\) by the two-edge detour \(v-b-a\), obtaining \(C'\). Then \(C'\) is a simple cycle with
\[
\boxed{|C'|=|C|+1,\quad
\alpha(C')=\alpha(C),\quad
\kappa(C')=\kappa(C)+1\pmod2,\quad
w_d(C')=w_d(C).}\tag{7}
\]
Equivalently, the orientation-curvature port membership toggles while covering-monodromy port membership and integer color-intersection cost are unchanged.

*Proof.* The vertex \(b\notin V(C)\), so replacing the edge \(va\) with \(v-b-a\) preserves simplicity and increases length by one. The symmetric difference of the edge sets of \(C,C'\) is the star triangle \((v,a,b)\), on which covering monodromy is zero and canonical contact curvature is one. Consequently the two cohomology phases behave as stated. The turn-signature relation on the star triangle gives
\[
d(ab)=d(va)\oplus d(vb)=d(va)
\]
because \(d(vb)=0\). The removed edge \(va\) has the same cost as the new edge \(ab\), while \(vb\) costs zero, proving equality of integer weights. \(\square\)

**Proposition 5 (monochromatic curvature triangles at high-degree stars).** Suppose the base graph \(G\) has degree at least five at a vertex \(x\). For every deck-odd binary coloring of cover edges, the star clique in \(H=L(G)\) corresponding to the edges incident with \(x\) contains a triangle \(T\) with
\[
\boxed{w_d(T)=0,\qquad(\alpha(T),\kappa(T))=(0,1).}\tag{8}
\]

*Proof.* At either lift of \(x\), among its at least five incident edges, at least three have the same color. Their three pairwise turns form a star triangle downstairs. Every turn joins edges of the same color and therefore has zero cost. Star triangles lift to closed triangles, giving monodromy zero, and the intrinsic line-graph curvature evaluates to one on them. \(\square\)

For \(n\ge5\), the folded cube has degree \(n\), and the graph \(L(K_n)\) underlying ordinary boundary tournaments has degree \(2(n-2)\). Hence both canonical models have such zero-cost curvature triangles at every base vertex. **This alone does not guarantee Theorem 4's extension for a prescribed cycle:** an available zero-cost triangle must meet that cycle in the specified way, and the detour vertex must be unused. The distinction prevents conflating abundant local curvature supply with a global phase-switch selector.

**Theorem 6 (free curvature conjugation at a changed turn).** Let \(G\) be a finite simple graph with a connected two-sheeted cover, let \(H=L(G)\), and let \(d\) be a deck-odd turn signature. Let \(C\) be any simple odd-monodromy cycle in \(H\). Assume that at some changed turn \(va\in E(C)\), there is a third vertex \(b\) of the same star clique with \(b\notin V(C)\). Then replacing \(va\) by \(v-b-a\) gives a simple cycle \(C'\) satisfying
\[
\boxed{|C'|=|C|+1,\quad
\alpha(C')=\alpha(C),\quad
\kappa(C')=\kappa(C)+1\pmod2,\quad
w_d(C')=w_d(C).}\tag{9}
\]
In particular, if every base-graph vertex has degree at least \(s+1\) and every star clique meets \(V(C)\) in at most \(s\) vertices, such a companion cycle exists.

*Proof.* Since \(d(C)=\alpha(C)=1\pmod2\), at least one turn edge \(va\) of \(C\) is changed: \(d(va)=1\). The stated unused vertex \(b\) makes the detour simple. The mod-two edge difference is the star triangle \((v,a,b)\), which has monodromy zero and contact curvature one. On that triangle,
\[
d(vb)\oplus d(ba)=d(va)=1.
\]
Thus the two new turn indicators sum to one as ordinary integers, precisely matching the cost of the deleted turn \(va\). For the degree condition, the star clique has at least \(s+1\) vertices, of which at most \(s\) belong to \(C\); hence such an unused \(b\) is available at every changed turn. \(\square\)

**Corollary 7 (unconditional adjacent-sector pairing for cube geodesics).** For every \(n\ge3\), every antipodally odd coloring of cube edges, and every antipodal-geodesic turn cycle \(C\) of length \(n\) in \(H_n=L(Q_n/\tau)\), there is a simple odd-monodromy turn cycle \(C'\) of length \(n+1\) such that
\[
\boxed{w_d(C')=w_d(C),\qquad
(\alpha(C),\kappa(C))=(1,0),\quad
(\alpha(C'),\kappa(C'))=(1,1).}\tag{10}
\]

*Proof.* The folded cube has degree \(n\). The geodesic uses one edge per direction and visits each antipodal vertex pair at most once, except for the identified initial and terminal vertices. Consequently the star clique of any folded-cube vertex contains at most two geodesic edge-state orbits. (At an internal vertex these are its entering and departing edges; at the terminal seam they are the first and last edge orbits.) Apply Theorem 6 with \(s=2\) and \(n\ge3\). The geodesic has no stationary contact, so \(\kappa(C)=0\); the detour toggles that parity. \(\square\)

**Theorem 8 (equality of adjacent two-port minimum spectra).** Let \(\mathcal G_n\) be the odd-monodromy simple turn cycles of length \(n\) in \(H_n\), and let \(\mathcal S_n\) be those of length \(n+1\). For every \(n\ge3\) and every admissible turn signature \(d\),
\[
\boxed{
\min_{C\in\mathcal G_n}w_d(C)
=
\min_{C'\in\mathcal S_n}w_d(C').}\tag{11}
\]
Every member of \(\mathcal G_n\) has \((\alpha,\kappa)=(1,0)\), and every member of \(\mathcal S_n\) has \((\alpha,\kappa)=(1,1)\). Hence the two-port matroid has equal minimum port-cycle intersection weights over these two distinguished consecutive-length cocircuit sectors.

*Proof.* By the established directional-excess formula from Article XI, every odd-monodromy simple turn cycle of length \(r\) satisfies
\[
r=n+s(C)+2q(C),
\]
where \(s(C)\) is its stationary-contact count and \(q(C)\) its nonnegative repeated-direction excess. If \(r=n\), necessarily \(s=q=0\), so the cycle lifts to an antipodal geodesic. If \(r=n+1\), necessarily \(s=1,q=0\). The unique stationary contact admits the established star-triangle contraction, producing a simple odd-monodromy cycle of length \(n\) whose turn weight does not exceed that of the original length-\(n+1\) cycle. Thus the left minimum is no larger than the right one. Conversely Corollary 7 extends every length-\(n\) geodesic cycle to a length-\(n+1\) odd-monodromy cycle at the same cost, giving the reverse inequality. The curvature phases follow from \(\kappa(C)\equiv s(C)\pmod2\). \(\square\)

**Consequence for the conjecture.** In the cube, the monochromatic-geodesic assertion can equivalently be tested in the opposite curvature sector one turn above the port cogirth:
\[
\min_{C'\in\mathcal S_n}w_d(C')=1
\quad\Longleftrightarrow\quad
\min_{C\in\mathcal G_n}w_d(C)=1.
\tag{12}
\]
The additional turn does not weaken this minimization problem. It changes the two-port cocircuit sector while preserving the minimum integer overlap, and may permit alternative geometric or dual-matroid arguments.

**Theorem 9 (equal-weight cube-extension ladder).** For n>=3, every antipodal-geodesic turn cycle C of the folded cube, for every antipodally odd edge coloring and every 0<=t<=n-2, has at least binomial(n-2,t) distinct simple odd-monodromy cycle extensions C_t of length n+t. Their turn weights are all w(C), and their contact curvature is t modulo two. In particular the minimum turn weight among odd-monodromy cycles of length n+t cannot exceed the minimum weight of full geodesic cycles; the adjacent length n+1 case is an equality by Theorem 8.

*Proof.* Covering monodromy is odd on C, so at least one cyclic turn va has color difference one. The vertex va belongs to an incident-edge star clique K_x of the folded cube quotient. At every star the geodesic uses only two edge-state orbits, v and a, leaving n-2 unused clique vertices. Choose any t of those unused states. Order them with all states colored like v followed by all those colored like a. The detour v,b_1,...,b_t,a stays inside K_x and has one color change, just as va did. All inserted vertices were outside C, so the enlarged cycle is simple and retains the same integer turn cost. The symmetric difference with C is the star-clique cycle v,b_1,...,b_t,a,v; it has zero covering monodromy, and its contact curvature is t modulo two, because it triangulates into t star triangles, each with curvature one. The original geodesic has zero contact curvature. Different choices of the t inserted vertices give different enlarged-cycle vertex sets. This proves the binomial lower bound and the asserted weight and phase relations. QED.

**Corollary 10 (stationary-only spectral plateau).** For n>=3, every integer t with 0<=t<=n-2, and every admissible turn signature d, the minimum integer weight of an odd-monodromy simple turn cycle with length n+t and directional excess q=0 equals the minimum weight among antipodal-geodesic turn cycles of length n. Moreover all cycles in the binomial extension family of Theorem 9 have q=0 and stationary-contact count s=t.

*Proof.* The inserted edge states in the star-clique detour of Theorem 9 all have both contact vertices equal to the same cube vertex, so they are stationary; the original n geodesic edge states retain their distinct moving coordinates. Hence s=t and q=0 for every extension, establishing that the left minimum is no greater than the geodesic minimum. Conversely, the monotone stationary-contact contraction theorem already established in the first section of Article XI takes any odd-monodromy cycle with q=0 to a geodesic cycle while never increasing its integer turn weight. Therefore the left minimum is at least the geodesic minimum. QED.

The plateau applies to the q=0 sector only. For t>=2, unrestricted cycles of length n+t may have positive repeated-direction excess, and no equality for that larger family is asserted.

**Theorem 11 (equal-cardinality two-port cocircuit sector exchange).** Let D_n^(2) be the canonical bipointed binary matroid for the n-dimensional cube, with monodromy port p and orientation-curvature port q. Define A_n to be its cocircuits containing p and q of size n+2, and B_n to be its cocircuits containing p but not q of size n+2. For every binary cycle X of D_n^(2) containing p and avoiding q, the two families are nonempty and satisfy

min{|X intersect Y|:Y in A_n}=min{|X intersect Y|:Y in B_n}.

In particular, the unrestricted monochromatic NORI1 conjecture is equivalent to the assertion that for every such X there is a cocircuit Y in B_n with |X intersect Y|=2. This is a size-n+2 cocircuit condition in a single bipointed binary matroid, with port sector (p present, q absent).

*Proof.* By the canonical two-port construction in Article XI, every simple turn cycle C contributes a cocircuit comprising its turn edges and those ports prescribed by (alpha(C),lambda(C)), where lambda=alpha+kappa. An odd-monodromy cycle of length n is a geodesic with stationary count zero, so lambda=1 and its cocircuit belongs to A_n. An odd-monodromy cycle of length n+1 has one stationary contact, so lambda=0 and its cocircuit belongs to B_n. Conversely a cocircuit in either family arises from the indicated turn-cycle length and sector. For X containing p and avoiding q, intersection with either cocircuit is 1+w_d(C). The adjacent-length minimum-spectrum equality of Theorem 8 therefore gives the claimed equality of minimum intersections. Cyclic rotation converts turn weight one in a geodesic cycle to a monochromatic antipodal geodesic, proving the final equivalence. QED.

**Theorem 12 (four-element curvature-port cocircuit pivot).** In the canonical bipointed cube turn matroid D_n^(2), for every star triangle T of H_n the set Q_T=T union {q} is a four-element cocircuit containing curvature port q and not monodromy port p. Let Y=C union {p,q} be any full-geodesic cocircuit. Suppose T contains a changed turn e of C and its third star vertex lies outside C. Then the symmetric difference Y' = Y triangle Q_T is a cocircuit containing p but not q, has the same cardinality n+2 as Y, and for every admissible port cycle X with d(e)=1 satisfies |X intersect Y'|=|X intersect Y|. Conversely, every size-n+2 p-only cocircuit Y' has a unique stationary edge-state, and contraction at that state reverses such a four-element cocircuit pivot, producing a both-port cocircuit Y of size n+2 whose intersection with X does not exceed that of Y'.

*Proof.* A star triangle has monodromy zero and orientation curvature one, so adjoining q yields a cocircuit of the two-port lift. For the forward pivot, Y and Q_T intersect in q and the one old turn e, hence their symmetric difference replaces e by the other two sides of the triangle while deleting q. The third triangle vertex was unused in C, so the turn cycle remains simple. It has one additional turn and the same total cocircuit cardinality. The star turn signature has even parity on T; since d(e)=1, precisely one of its other two sides has label one, hence the X-intersection is unchanged. Conversely, the directional-excess identity forces a size-n+2 p-only cocircuit to have a length-n+1 monodromy-one turn cycle with one stationary contact and no repeated-direction excess. Its stationary state belongs to a unique local star triangle with the two neighboring states; shortcutting via the third side contracts it to a geodesic and adds q. The star-triangle cost inequality guarantees that intersection cannot increase. QED.

This identifies a local q-port cocircuit exchange realizing the adjacent-sector equality, rather than merely a numerical equality of optima.

**Theorem 13 (regular parent map between equal-size cocircuit sectors).** With A_n and B_n as in Theorem 11, for every n>=3 the stationary-contact contraction defines a canonical map pi:B_n -> A_n. Every fiber of pi has cardinality n(n-2), and

|A_n| = 2^(n-2) (n-1)!,     |B_n| = n(n-2) 2^(n-2) (n-1)!.

For a fixed admissible coloring turn cochain d, each B_n-child of a geodesic parent C has integer turn weight either w_d(C) or w_d(C)+2. At least (n-2)w_d(C) of the n(n-2) children retain precisely the parent's turn weight.

*Proof.* The directional-excess identity forces every odd-monodromy cycle of length n+1 to have one stationary contact and no repeated-direction excess. Its stationary edge-state has a unique pair of neighboring states, and replacing its two incident turns by the shortcut uniquely recovers a length-n geodesic cycle. Conversely, a geodesic has n cyclic turn edges, each lying in a folded-cube vertex-star clique containing n edge-state orbits, only two of which belong to that geodesic. Choosing any of the n-2 unused states and inserting it between the endpoints of the selected turn produces a unique simple length-(n+1) odd-monodromy cycle. These n(n-2) extensions are distinct and all contract back to their parent, proving the fiber count.

There are 2^n n! rooted directed full antipodal geodesics in the cube. Each undirected quotient geodesic turn cycle corresponds to 2n choices of oriented starting turn and two deck sheets, or 4n rooted directed geodesics. Hence |A_n|=2^n n!/(4n)=2^(n-2)(n-1)! and the B_n count follows.

For a triangle expansion replacing turn va through a new star state b, the two new turn labels have binary sum d(va). If d(va)=1, one new label is one and the other zero, so the integer weight is preserved for every one of the n-2 choices of b. If d(va)=0, the two new labels agree: their integer sum is either zero or two. Summing the n-2 neutral options for each of the w_d(C) changed turns yields the stated bound. QED.

This yields an uncolored regular cocircuit exchange map and a coloring-dependent lower bound on its cost-preserving outgoing degree. The structure is intrinsic to the canonical two-port representation together with its star-triangle family; ordinary cocircuit elimination alone does not imply such regular fibers.

Let \(H\) be a finite graph equipped with two binary cohomology classes \(\alpha,\lambda\in H^1(H;\mathbb F_2)\). The relevant instance is the two-port line-graph lift of Article XI, in which these classes are covering monodromy and orientation curvature. Put
\[
\sigma(C)=(\alpha(C),\lambda(C))\in\mathbb F_2^2
\]
for any graph cycle \(C\). Let \(w:E(H)\to\mathbb R_{\ge0}\) be any nonnegative edge cost, with \(w(C)=\sum_{e\in C}w(e)\).

**Theorem 1 (two-connector sector completion).** Let \(C_1,C_2\) be vertex-disjoint simple cycles of \(H\). Assume they are joined by two vertex-disjoint paths \(P,Q\), whose interiors avoid both cycles, such that \(P\) connects \(a_1\in C_1\) to \(a_2\in C_2\), \(Q\) connects \(b_1\in C_1\) to \(b_2\in C_2\), and \(a_i\ne b_i\) for \(i=1,2\). Let \(A_i^0,A_i^1\) be the two \(a_i\)-to-\(b_i\) arcs of \(C_i\). For \(\varepsilon,\delta\in\mathbb F_2\), define
\[
\Gamma_{\varepsilon,\delta}=
A_1^\varepsilon\cup P\cup A_2^\delta\cup Q.
\tag{1}
\]
Each \(\Gamma_{\varepsilon,\delta}\) is a simple cycle, and
\[
\boxed{\sigma(\Gamma_{\varepsilon,\delta})
=\sigma(\Gamma_{0,0})+\varepsilon\sigma(C_1)+\delta\sigma(C_2).}
\tag{2}
\]
If \(\sigma(C_1),\sigma(C_2)\) are linearly independent in \(\mathbb F_2^2\), the four simple cycles (1) realize all four possible two-port signature sectors, one in each sector. Every one satisfies
\[
\boxed{|\Gamma_{\varepsilon,\delta}|\le |C_1|+|C_2|+|P|+|Q|,\qquad
w(\Gamma_{\varepsilon,\delta})
\le w(C_1)+w(C_2)+w(P)+w(Q).}
\tag{3}
\]
Consequently, if \(P,Q\) are zero-cost paths, all four sectors are realized by simple cycles whose cost is at most \(w(C_1)+w(C_2)\).

*Proof.* The two arcs of each \(C_i\) meet only at their endpoints, and the connector interiors avoid both cycles and one another. Thus (1) is one simple cycle. In the binary graph cycle space the symmetric difference of its two choices of the first arc is the full cycle \(C_1\), and similarly for the second arc:
\[
\Gamma_{\varepsilon,\delta}
=\Gamma_{0,0}\triangle(\varepsilon C_1)\triangle(\delta C_2).
\]
Applying the two linear cycle functionals gives (2). Independence of the two signature vectors makes the affine map \((\varepsilon,\delta)\mapsto\sigma(\Gamma_{\varepsilon,\delta})\) a bijection of \(\mathbb F_2^2\). For each choice, one uses only one arc from each input cycle and both connecting paths; nonnegativity gives (3). \(\square\)

**Corollary 2 (bipointed cocircuit repair by zero-cost connectors).** Let \(D^{(2)}\) be the dual of the two-port incidence/monodromy/curvature matrix from Article XI. Suppose \(C_1,C_2\) are vertex-disjoint simple turn cycles whose signatures \((\alpha,\lambda)\) are independent. If they admit two disjoint connecting paths of zero turn cost for the prescribed port-containing binary cycle \(X_d\), then for every \(\eta\in\mathbb F_2^2\) there exists a simple cycle \(C_\eta\) with signature \(\eta\) and
\[
w_d(C_\eta)\le w_d(C_1)+w_d(C_2).
\]
In particular \(\eta=(1,1)\) gives a cocircuit \(C_\eta\cup\{p,q\}\) containing both ports, whereas \(\eta=(1,0)\) gives a cocircuit containing \(p\) but avoiding \(q\). For the admissible port cycle \(X_d\), either such cocircuit has intersection \(1+w_d(C_\eta)\).

*Proof.* Apply Theorem 1 with the nonnegative integer cost \(d\). In the two-port representation, a simple turn cycle \(C\) closes to the cocircuit obtained by adjoining \(p\) when \(\alpha(C)=1\) and \(q\) when \(\lambda(C)=1\). The specified port cycle \(X_d\) includes \(p\), excludes \(q\), and records the support of \(d\) on the turn edges. \(\square\)

**Corollary 3 (Menger criterion for zero-cost sector completion).** Let \(H_0(d)\) be the subgraph of zero-cost turns. If one 2-vertex-connected block of \(H_0(d)\) intersects each of two vertex-disjoint simple cycles \(C_1,C_2\) in at least two vertices, and their signatures are independent, then all four port sectors admit the bounded-cost simple-cycle witnesses of Corollary 2.

*Proof.* The vertex form of Menger's theorem, applied inside the 2-connected block to the two disjoint vertex sets given by its intersections with \(C_1,C_2\), yields two vertex-disjoint zero-cost paths connecting the sets. Truncate each at its last point of \(C_1\) and first point of \(C_2\). Their interiors then avoid both cycles and remain mutually disjoint, and their endpoints on each cycle are distinct. Corollary 2 applies. \(\square\)

Theorem 1 does not require graph-cover structure: it is valid for any two binary classes on the cycle space of any graph. In the two-port signed-cover application it supplies a **cost-controlled, phase-prescribed cocircuit selection mechanism** that does not require the two input cycles to intersect. It does not guarantee that a selected simple cycle is resource-independent or coherently directed; those additional path-language restrictions remain central to the shared NORI1/boundary-tournament conjecture.

### Antipodal Boolean-lattice terminal polarity and spanning one-turn paths

The preceding Subsection formulates the spanning one-turn boundary-tournament conjecture as opposite-terminal packing of two same-colored vertex-simple tight paths. Here we introduce a **resource-subset state graph** that carries a canonical complement-reversal involution. The key theorem is a color-reversing anti-isomorphism of its two directed reachability graphs, yielding a single antipodal reachability-intersection formulation that parallels the endpoint-coincidence approaches to NORI1. The proof is valid in all orders and preserves vertex simplicity at every step.

#### 1. The ordered-terminal Boolean-lattice graph

Let \(V\) have \(n\ge3\) vertices, and let \(b:V_{\ne}^3\to\mathbb F_2\) be a reversal-odd boundary coloring:
\[
b(v,u,x)=1+b(x,u,v).
\tag{1}
\]
Define the state set
\[
\mathscr S(V)=\{(A,u,v):\{u,v\}\subseteq A\subseteq V,\ u\ne v\}.
\tag{2}
\]
The first component remembers the set of original vertices used, and the last two components remember the ordered terminal pair. For each color \(\epsilon\in\mathbb F_2\), define an acyclic digraph \(\mathscr D_\epsilon(b)\) on \(\mathscr S(V)\): there is a directed arc
\[
\boxed{(A\setminus\{v\},x,u)\longrightarrow(A,u,v)}
\tag{3}
\]
whenever \(x,u,v\) are distinct members of \(A\) and \(b(x,u,v)=\epsilon\). The arc increases resource-set cardinality by one. The sources are the ordered two-vertex states \((\{u,v\},u,v)\), considered admissible in either color because a two-vertex path has no ordered-triple window.

Let \(\mathscr R_\epsilon\subseteq\mathscr S(V)\) be the union of states reachable from any source in \(\mathscr D_\epsilon(b)\).

**Lemma 1 (terminal-state reachability).** A state \((A,u,v)\) belongs to \(\mathscr R_\epsilon\) if and only if there is a vertex-simple \(\epsilon\)-monochromatic tight path whose vertex set is \(A\) and final ordered pair is \((u,v)\).

*Proof.* A path on two vertices corresponds to a source. Each extension adds a fresh vertex \(v\) to a previously constructed path ending in \((x,u)\), and the new final triple is \((x,u,v)\). The arc rule (3) requires the new triple color to be \(\epsilon\), and the increasing set \(A\) rules out repeated original vertices. Conversely, delete the last vertex of any positive-length witness to recover its predecessor. Induction on \(|A|\) proves the equivalence. \(\square\)

For a fixed ordered pair \((u,v)\), write \(U=V\setminus\{u,v\}\), and let
\[
\mathscr F_{uv}^\epsilon
=\{S\subseteq U:(S\cup\{u,v\},u,v)\in\mathscr R_\epsilon\}.
\tag{4}
\]
Then the recursion is
\[
\boxed{
\mathscr F_{uv}^\epsilon(\varnothing)=1,\qquad
\mathscr F_{uv}^\epsilon(S)=
\bigvee_{x\in S}
\left(
[b(x,u,v)=\epsilon]\land
\mathscr F_{xu}^\epsilon(S\setminus\{x\})
\right)
}
\tag{5}
\]
for \(S\ne\varnothing\), with each \(\mathscr F\) read as a Boolean indicator. The state count is
\[
\boxed{|\mathscr S(V)|=n(n-1)2^{n-2};}
\tag{6}
\]
all values of (5) can be calculated in \(O(n^3 2^n)\) Boolean operations. This is an all-dimensional subset-state representation rather than an enumeration of \(n!\) complete orders.

#### 2. The color-reversing antipodal polarity

Define
\[
\boxed{
\mathcal J(A,u,v)
=\bigl((V\setminus A)\cup\{u,v\},\,v,u\bigr).
}
\tag{7}
\]
This complements the *used* resources other than the terminal pair, retaining the two shared vertices while reversing their order. It satisfies \(\mathcal J^2=1\), has no fixed state, and carries resource-set cardinality \(r\) to \(n-r+2\).

**Theorem 2 (complement-reversal anti-isomorphism).** For every reversal-odd boundary coloring and each \(\epsilon\in\mathbb F_2\), the involution (7) induces a directed-graph anti-isomorphism
\[
\boxed{
\mathcal J:\mathscr D_\epsilon(b)\longrightarrow
\mathscr D_{1-\epsilon}(b)^{\mathrm{op}}.
}
\tag{8}
\]
In other words, whenever \(P\to Q\) is a color-\(\epsilon\) arc, then
\[
\boxed{\mathcal J(Q)\to\mathcal J(P)}
\tag{9}
\]
is a color-\((1-\epsilon)\) arc.

*Proof.* Consider a typical arc (3) with \(b(x,u,v)=\epsilon\). Write \(T=V\setminus A\). Then
\[
\begin{aligned}
\mathcal J(A,u,v)&=(T\cup\{u,v\},v,u),\\
\mathcal J(A\setminus\{v\},x,u)&=(T\cup\{u,v,x\},u,x).
\end{aligned}
\]
The second state is obtained from the first by appending the fresh vertex \(x\) to the terminal pair \((v,u)\). The corresponding new triple is \((v,u,x)\), and by (1)
\[
b(v,u,x)=1+b(x,u,v)=1-\epsilon.
\]
Thus (9) is an arc of \(\mathscr D_{1-\epsilon}(b)\). Applying \(\mathcal J\) again proves the converse and hence (8). \(\square\)

**Corollary 3 (reachability/co-reachability duality).** A state \(s\) lies in \(\mathcal J(\mathscr R_\epsilon)\) precisely when there is a path in \(\mathscr D_{1-\epsilon}(b)\) from \(s\) to some full-resource state \((V,u,v)\). Thus
\[
\boxed{
\mathcal J(\text{color-}\epsilon\text{ source reachability})
=\text{color-}(1-\epsilon)\text{ full-state co-reachability}.
}
\tag{10}
\]

*Proof.* Apply the arc anti-isomorphism to a color-\(\epsilon\) path from a two-vertex source to \(\mathcal J(s)\). Its reverse image starts at \(s\), follows color-\((1-\epsilon)\) arcs, and ends at the image of the two-vertex source, which is a full-resource state. The argument reverses. \(\square\)

#### 3. Antipodal reachability-intersection equivalence

**Theorem 4 (spanning one-turn iff antipodal reachability intersects).** An ordinary reversal-odd boundary 3-tournament admits a spanning vertex-simple tight path with at most one internal color change if and only if
\[
\boxed{
\mathscr R_\epsilon\cap\mathcal J(\mathscr R_\epsilon)
\ne\varnothing
\quad\text{for some }\epsilon\in\mathbb F_2.
}
\tag{11}
\]
Equivalently, for some distinct \(u,v\), a subset \(S\subseteq U=V\setminus\{u,v\}\), and a color \(\epsilon\),
\[
\boxed{
S\in\mathscr F_{uv}^\epsilon,\qquad
U\setminus S\in\mathscr F_{vu}^\epsilon.
}
\tag{12}
\]

*Proof.* The latter condition gives two vertex-simple same-colored tight paths ending at \((u,v)\) and \((v,u)\) whose sets of other vertices are complementary. Reversing the second arm and identifying the shared terminal pair produces a spanning path with at most one change, as proved by the opposite-terminal packing theorem of the preceding Subsection. Conversely, splitting a spanning one-turn path at its color change and reversing its suffix produces these two arms; if the original path is monochromatic, allow the first arm to consist only of its first two vertices. Under the state encoding, the two conditions in (12) say precisely that \(s=(S\cup\{u,v\},u,v)\) and \(\mathcal J(s)\) both belong to \(\mathscr R_\epsilon\), establishing (11). \(\square\)

Thus the principal boundary conjecture can be stated intrinsically as:

**Conjecture 5 (antipodal terminal-reachability intersection).** Every reversal-odd colored ordered-terminal subset-state system (2)–(3) has
\[
\boxed{
\mathscr R_0\cap\mathcal J(\mathscr R_0)\ne\varnothing
\quad\text{or}\quad
\mathscr R_1\cap\mathcal J(\mathscr R_1)\ne\varnothing.
}
\tag{13}
\]
By Theorem 4 this is equivalent to the spanning one-turn boundary-tournament conjecture, not a new independent assumption.

For comparison, the cube's full geodesic is likewise a resource-injective chain in a Boolean subset lattice; its antipodal endpoint construction seeks complementary color-compatible partial chains. The common missing theorem concerns the **reachability geometry under a free antipodal polarity**, rather than bare binary-matroid parity.

#### 4. Sharp complement counting criteria

Let
\[
r_{uv}^{\epsilon}(k)
=\#\{S\in\mathscr F_{uv}^\epsilon:|S|=k\},
\qquad 0\le k\le n-2.
\tag{14}
\]

**Proposition 6 (complementary-layer density suffices).** If there are distinct \(u,v\), \(\epsilon\), and \(k\) with
\[
\boxed{
r_{uv}^{\epsilon}(k)+
r_{vu}^{\epsilon}(n-2-k)>
\binom{n-2}{k},
}
\tag{15}
\]
then the boundary tournament has a spanning at-most-one-turn tight path. Consequently, a hypothetical counterexample to (13) must satisfy **all** the reverse inequalities
\[
\boxed{
r_{uv}^{\epsilon}(k)+
r_{vu}^{\epsilon}(n-2-k)
\le\binom{n-2}{k}
}
\tag{16}
\]
for every ordered pair, color and layer; in particular
\[
|\mathscr F_{uv}^\epsilon|+|\mathscr F_{vu}^\epsilon|
\le2^{n-2}.
\tag{17}
\]

*Proof.* The complement map \(S\mapsto U\setminus S\) bijects the \(k\)-subsets of \(U\) with its \((n-2-k)\)-subsets. If the two cardinalities in (15) exceed the number of complementary pairs, their supports must overlap after complementation. This gives (12). The contrapositives and sum over \(k\) prove (16)–(17). \(\square\)

These counting inequalities are sufficient certificates, not asserted universal density bounds. Establishing an exchange, connectivity, parity or topological principle forcing a violation of (16) for some pair/color/layer would prove the spanning conjecture. A basic accessible-set argument is insufficient: the fixed-terminal reachability families are accessible but need not satisfy greedoid augmentation (a verified five-vertex counterexample is preserved as a research note attached to this Section).

#### 5. Research significance

Theorem 2 introduces a mathematically intrinsic **anti-isomorphism between the two color-specific terminal extension systems**. Together with the resource-set polarity (7), Theorem 4 expresses the full-spanning one-turn assertion as a complement-intersection problem over an ordered-pair bundle of Boolean lattices. Unlike an unmarked cocircuit intersection bound, this representation preserves (i) all original vertices, (ii) the order and orientation of both terminal vertices, (iii) the path's single color-change seam, and (iv) the precise opposite-arm compatibility demanded by the original problem.

The next substantive goal is a global topological or exchange theorem establishing (13) from reversal oddness, perhaps by forcing opposing reachable families to intersect on complementary ranks. The present results provide the encoding, duality, and a transparent target; they do **not** prove the conjectural intersection in general.

### Signed turn adjacency and a dimension-independent disagreement bound

Let \(n\ge6\), and put \(T_n=\{(a,b,c)\in[n]^3:a,b,c\text{ pairwise distinct}\}\). The oriented legal-turn graph has transitions \((a,b,c)\to(b,c,d)\) whenever \(a,b,c,d\) are pairwise distinct. Its reversal involution is \(R(a,b,c)=(c,b,a)\). Write
\[
V_n=\{f:T_n\to\mathbb R:f(Rt)=-f(t)\},\qquad
N_n=\dim V_n=n\binom{n-1}{2}.
\]
Define the operator
\[
(A_nf)(a,b,c)=\sum_{d\notin\{a,b,c\}}
\bigl(f(b,c,d)+f(d,a,b)\bigr).\tag{1}
\]
The two summands enumerate forward and backward legal turns. Reversal exchanges these summands with opposite signs, so \(A_nV_n\subseteq V_n\). Moreover, \(A_n\) is self-adjoint: every forward transition is the backward transition at its other endpoint. Choosing one ordered triple from every reversal pair makes \(A_n\) the signed adjacency matrix of the reversal quotient, of order \(N_n\) and signed degree \(2(n-3)\).

**Theorem 1 (signed-turn spectral identity).** For every \(n\ge6\),
\[
\boxed{A_n(A_n-I)(A_n+2I)\bigl(A_n^2-(n-2)^2I\bigr)=0.}\tag{2}
\]
Consequently,
\[
\boxed{\operatorname{spec}(A_n)\subseteq\{-(n-2),-2,0,1,n-2\},
\qquad A_n\succeq-(n-2)I.}\tag{3}
\]

*Proof.* Fix the initial oriented reversal orbit represented by \(t_0=(1,0,2)\), and let \(e_0\) be its coordinate basis vector in \(V_n\). The action of the symmetric group on the labels commutes with \(A_n\) and acts transitively on oriented reversal-orbit basis vectors up to sign. It therefore suffices to prove that the operator in (2) annihilates \(e_0\).

For any fixed target triple \(t\) whose letters belong to \(\{0,1,2,3,4,5\}\), the coefficient of \(e_t\) in \(A_n^ke_0\), for \(n\ge6\), is a polynomial in \(n\) of degree at most \(k\). Indeed, a contributing walk of length \(k\) introduces at most \(k\) letters outside the three initial labels. Partition its intermediate letters according to equality and according to any equalities with the fixed initial and terminal letters. Each admissible equality pattern contributes \(\pm(n-r)_j\) choices of unused letters, for some fixed integer \(r\) and \(j\le k\), where \((z)_j=z(z-1)\cdots(z-j+1)\). Summing finitely many such patterns gives the claimed polynomial degree bound. The reversal sign of a terminal coordinate depends only on the fixed letters and is independent of \(n\).

The polynomial in the operator on the left of (2) expands to
\[
P_n(A_n)=A_n^5+A_n^4-\bigl((n-2)^2+2\bigr)A_n^3
-(n-2)^2A_n^2+2(n-2)^2A_n.\tag{4}
\]
Every coordinate of \(P_n(A_n)e_0\) thus has degree at most five in \(n\). Since any ordered target triple can, by permuting the labels outside \(\{0,1,2\}\), be represented using at most three further labels, it suffices to check target triples among those six labels. Integer-arithmetic evaluation gives \(P_n(A_n)e_0=0\) for the six values \(n=6,7,8,9,10,11\). A self-contained certificate follows; all entries and operations are integers.

~~~python
from itertools import combinations

def check(n):
    reps = [(a,b,c) for b in range(n)
            for a,c in combinations([v for v in range(n) if v != b], 2)]
    where = {t:i for i,t in enumerate(reps)}
    adjacency = []
    for a,b,c in reps:
        row = []
        for d in range(n):
            if d in (a,b,c):
                continue
            for u,v,w in ((b,c,d),(d,a,b)):
                key = (u,v,w) if u < w else (w,v,u)
                row.append((where[key], 1 if u < w else -1))
        adjacency.append(row)
    def act(x):
        return [sum(s*x[j] for j,s in row) for row in adjacency]
    basis = [0]*len(reps)
    basis[0] = 1  # reps[0] = (1,0,2)
    powers = [basis]
    for _ in range(5):
        powers.append(act(powers[-1]))
    q = (n-2)**2
    return all(powers[5][i] + powers[4][i]
               - (q+2)*powers[3][i] - q*powers[2][i]
               + 2*q*powers[1][i] == 0 for i in range(len(reps)))

assert all(check(n) for n in range(6,12))
~~~

The degree-five polynomial coordinate vanishes at six distinct values, hence vanishes identically. Relabeling proves (2) on the entire space \(V_n\). Self-adjointness then places the spectrum among the roots of \(P_n\), proving (3). \(\square\)

**Theorem 2 (turn-disagreement density).** Let \(b:T_n\to\{0,1\}\) be any reversal-odd coloring, so \(b(c,b,a)=1-b(a,b,c)\). Its legal-turn cochain is
\[
d_b\bigl([(a,b,c)\to(b,c,d)]\bigr)=b(a,b,c)+b(b,c,d)\pmod2.
\]
The reversal quotient has \(E_n=(n)_4/2=N_n(n-3)\) edges. For every \(n\ge6\),
\[
\boxed{\quad
|\operatorname{supp}d_b|\le
\frac{3n-8}{4(n-3)}E_n,
\qquad
\frac{|\operatorname{supp}d_b|}{E_n}\le
\frac34+\frac{1}{4(n-3)}.\quad}\tag{5}
\]
The same statement holds on every restriction to a subset of \(m\ge6\) labels, with \(n\) replaced by \(m\). In particular, (5) improves the five-label parity-cycle bound \(4E_n/5\) when \(n\ge9\), and gives asymptotic disagreement density at most \(3/4\).

*Proof.* Choose one orientation of every reversal pair, and let \(x\in\{\pm1\}^{N_n}\) record \((-1)^{b(t)}\) there. For every quotient turn, its signed-adjacency contribution is \((-1)^{d_b}\). Thus
\[
\frac12x^\top A_nx=\sum_{e\in E(H_n)}(-1)^{d_b(e)}
=E_n-2|\operatorname{supp}d_b|.
\]
By (3), \(x^\top A_nx\ge-(n-2)\|x\|^2=-(n-2)N_n\), giving
\[
|\operatorname{supp}d_b|\le\frac12E_n+\frac14(n-2)N_n
=\frac{3n-8}{4(n-3)}E_n.
\]
Restriction to a subset retains reversal oddness and the legal-turn rule, proving the hereditary assertion. \(\square\)

**Pointed-matroid corollary.** In the cycle--cocycle model of legal turns with added port \(p\), the coloring cycle \(X_b=\operatorname{supp}d_b\cup\{p\}\) obeys
\[
|X_b\setminus\{p\}|\le\frac{3n-8}{4(n-3)}|E(H_n)|.
\]
Equivalently, at least \(\frac{n-4}{4(n-3)}|E(H_n)|\) admissible turns avoid the coloring cycle. This is a global quantitative restriction on the port-cycle sector of the canonical binary covering matroid; the estimate uses neither an edge ordering of the underlying tournament nor a small distinguished class of colorings.

Let \(n\ge3\), let \(H_n=L(Q_n/\tau)\) be the folded-cube turn graph, and let \(d\) be the turn cochain of an arbitrary antipodally odd cube-edge coloring. Write \(D=|\operatorname{supp}(d)|\) and \(E=|E(H_n)|=2^{n-1}\binom n2\).

Let \(\mathcal A_n\) denote the simple odd-monodromy cycles of length \(n\) (antipodal-geodesic cycles), and let \(\mathcal B_n\) denote the simple odd-monodromy cycles of length \(n+1\). Article XI's stationary-contact and two-port exchange theorems give a canonical parent map
\[
\pi:\mathcal B_n\longrightarrow\mathcal A_n
\]
whose fibers have size \(n(n-2)\). It identifies the two families with two equal-cardinality cocircuit sectors of the canonical bipointed binary matroid: both-port cocircuits versus monodromy-only cocircuits. Write \(w_d(C)\) for integer turn cost.

For \(C\in\mathcal A_n\), and for each turn \(e\in C\) of zero disagreement, let \(r_e(C)\) count the unused vertices in its local \(K_n\) star clique whose lifted edge color is opposite to the common color of the two endpoint states of \(e\). Put
\[
R_d(C)=\sum_{\substack{e\in C\\d(e)=0}}r_e(C).
\tag{1}
\]

**Theorem 1 (fiber weight enumerator).** The \(n(n-2)\) children of every \(C\in\mathcal A_n\) have integer turn weights
\[
\boxed{
w_d(C)\ \text{for }n(n-2)-R_d(C)\text{ children},\qquad
w_d(C)+2\ \text{for }R_d(C)\text{ children}.}
\tag{2}
\]
In particular, if
\[
A_d(z)=\sum_{C\in\mathcal A_n}z^{w_d(C)},\quad
B_d(z)=\sum_{C'\in\mathcal B_n}z^{w_d(C')},\quad
R_d(z)=\sum_{C\in\mathcal A_n}R_d(C)z^{w_d(C)},
\]
then the weight-distribution polynomials obey
\[
\boxed{B_d(z)=n(n-2)A_d(z)+(z^2-1)R_d(z).}
\tag{3}
\]

*Proof.* Each child of \(C\) inserts one unused local edge-state at one of its \(n\) cyclic turns, with \(n-2\) possibilities at each turn. For a changed turn, the endpoint colors differ, and either color of the inserted edge-state leaves precisely one changed turn. For an unchanged turn, the endpoint colors agree, and inserting the same color leaves zero changes while inserting the opposite color contributes two. Formula (1) counts precisely the latter choices. The stationary-contact contraction theorem makes the parent unique, so each child is counted once. Summing over parents gives (3). \(\square\)

**Theorem 2 (global fiber conservation).** The number of opposite-sector children that have cost two greater than their parents satisfies
\[
\boxed{
\sum_{C\in\mathcal A_n}R_d(C)
=\frac{(n-2)!(n-2)}2\,D.
}
\tag{4}
\]
Consequently, for a uniformly sampled \(C'\in\mathcal B_n\),
\[
\boxed{
\Pr\bigl[w_d(C')=w_d(\pi(C'))\bigr]
=1-\frac{D}{2E}.
}
\tag{5}
\]
Furthermore,
\[
\boxed{
\Pr\bigl[w_d(C')=w_d(\pi(C'))\bigr]
\ge 1-\frac{\lfloor n^2/4\rfloor}{n(n-1)}.
}
\tag{6}
\]
The lower bound in (6) is attained by antipodally odd edge colorings for every \(n\ge3\).

*Proof.* The automorphism group of the cube acts transitively on the turn edges of \(H_n\). There are
\[
|\mathcal A_n|=2^{n-2}(n-1)!
\]
geodesic cycles, each having \(n\) turns. Since \(|E(H_n)|=n(n-1)2^{n-2}\), every turn edge belongs to
\[
\frac{n|\mathcal A_n|}{|E(H_n)|}=(n-2)!
\tag{7}
\]
geodesic cycles.

At a quotient cube vertex \(v\), the \(n\) incident edge-state colors split into classes of sizes \(k_v,n-k_v\). The number of triples consisting of an **unchanged** pair of star states and a third state of the opposite color is
\[
\binom{k_v}{2}(n-k_v)+\binom{n-k_v}{2}k_v
=\frac{n-2}{2}k_v(n-k_v).
\tag{8}
\]
Every such pair is a turn edge and occurs in \((n-2)!\) geodesic cycles by (7). Summing (8) over all quotient vertices gives (4), since
\[
D=\sum_vk_v(n-k_v)
\tag{9}
\]
counts the changed turn edges. Because
\[
|\mathcal B_n|=n(n-2)|\mathcal A_n|,
\]
dividing (4) by this number yields the bad-child fraction \(D/(2E)\), proving (5). Finally
\[
k_v(n-k_v)\le\lfloor n^2/4\rfloor
\]
at every quotient vertex, and \(H_n\) has \(2^{n-1}\) local star cliques; substitute in (5) to obtain (6).

To prove sharpness in every dimension, label the coordinate directions \(1,\ldots,n\), and pair \((1,2),(3,4),\ldots\). For the first pair assign edge colors \(c_1(x)=x_3\) and \(c_2(x)=1-x_3\). For each subsequent complete pair \((i,i+1)\), assign \(c_i(x)=x_1\), \(c_{i+1}(x)=1-x_1\). If \(n\) is odd, assign the remaining direction \(n\) the color \(c_n(x)=x_1\). Each \(c_i\) is independent of \(x_i\), so it defines an undirected edge coloring. Complementing all cube coordinates reverses every \(c_i\), so the coloring is antipodally odd. Each complete pair supplies one edge of each color at every cube vertex; the unmatched coordinate when \(n\) is odd supplies one additional color. Thus \(k_v\in\{\lfloor n/2\rfloor,\lceil n/2\rceil\}\) for every star, and equality holds in the bound on \(D\) and hence in (6). \(\square\)

**Corollary 3 (first-moment transfer between two-port sectors).** Uniformly over \(\mathcal B_n\) and \(\mathcal A_n\), respectively, the turn costs satisfy
\[
\boxed{
\mathbb E_{\mathcal B_n}w_d
=\frac{n+1}{n}\mathbb E_{\mathcal A_n}w_d,
\qquad
\mathbb E_{\mathcal A_n}w_d=\frac{nD}{E}.
}
\tag{10}
\]
*Proof.* Formula (2) gives
\[
\sum_{C'\in\mathcal B_n}w_d(C')
=n(n-2)\sum_{C\in\mathcal A_n}w_d(C)
+2\sum_{C\in\mathcal A_n}R_d(C).
\]
Use (4), (7), and the family cardinalities. \(\square\)

Theorems 1–2 strengthen the earlier equality of minimum color costs in the two bipointed cocircuit sectors to a polynomial identity and a sharp global conservation law for fiber costs. They do not establish that the common minimum is one: the unresolved NORI1 problem remains the existence of a geodesic-sector cocircuit with two-point intersection.

**Theorem (stationary-child regularity).** For a binary generator Cayley lift with m generators and shortest distinguished representation length ell at least three, the shortest odd-monodromy turn cycles have regular stationary-contact offspring: each has ell(m-2) children one turn longer. Contracting the unique stationary contact recovers a unique geodesic parent. For any deck-odd binary edge coloring, every child has integer turn cost equal to its parent cost or two greater. The number of shortest cycles equals F*2^(r-2)*(ell-1)!, where r is the binary representation rank and F the number of shortest distinguished generator subsets. The statements follow by choosing an invariant ell-dimensional subcube for each shortest generator subset, counting its quotient antipodal geodesics, and inserting one of the m-2 unused edge states at each of ell local turns. A changed turn stays changed after the insertion; an unchanged turn either stays unchanged or splits into two changed turns.
**Theorem 2 (shortest-circuit 2-design conservation).** Let S be a spanning family of m distinct binary generator vectors, t a distinguished vector whose minimum generator expression uses ell>=3 labels, and F the set of such minimum expressions. Assume each pair of distinct generator labels belongs to eta members of F. Put E=2^(r-1)*binomial(m,2) for the quotient line graph turn count, and let D denote the number of changed turns of an admissible deck-odd coloring. For each shortest turn cycle C, let R_d(C) count its stationary children whose integer turn weight is two greater. Then

sum_C R_d(C) = (ell-2)! * eta * (m-2) * D / 2.

If one chooses a stationary child uniformly, its color-turn weight equals that of its geodesic parent with probability

1 - D/(2E),

which is at least 1-floor(m*m/4)/(m*(m-1)).

*Proof.* At a fixed quotient-graph vertex and a fixed pair of distinct generator labels s,s', every shortest representation A containing this pair contributes (ell-2)! shortest cycles through the corresponding local turn. By the pair-design assumption this multiplicity is the same, eta*(ell-2)!, for every turn. At a local clique with k edge states of one color and m-k of the other, the number of unchanged pairs with an opposite-colored third state equals

binomial(k,2)*(m-k)+binomial(m-k,2)*k = (m-2)*k*(m-k)/2.

Summing this quantity over stars and multiplying by eta*(ell-2)! gives the first displayed formula, because D is the sum of k*(m-k) over all local stars. The design double-counting identity eta*binomial(m,2)=|F|*binomial(ell,2) combines with the uniform ell*(m-2) stationary children per parent to reduce the fraction of extra-cost children to D/(2E). The inequality follows from k*(m-k)<=floor(m*m/4). QED.

For an arbitrary, non-design shortest-circuit family, the analogous local formula holds with each generator pair weighted by its incidence multiplicity eta_{s,s'}. The design property is precisely what collapses this weighted incidence statistic to the single global turn count D.

**Example (projective-line binary generator matroids).** For every integer d>=2, let V=F2^(d+1), t=(1,0), and S={(1,u):u in F2^d, u nonzero}, with m=2^d-1. Then every shortest representation of t has length three. The shortest generator triples are precisely {(1,u),(1,v),(1,u+v)} with distinct nonzero u,v; every pair occurs in one triple. Thus they form a Steiner triple system (a 2-(m,3,1) design). The Cayley covering graph is the crown graph K_(2^d,2^d) with its matching deleted, and its quotient by the deck involution is K_(2^d). The number of shortest monodromy-odd turn cycles is (m*(m-1)/6)*2^(d-1)*2. In the Fano-plane case d=3, m=7, there are 56 shortest turn cycles and 840 stationary children; the weight-conservation theorem applies to every reversal-odd coloring of this non-cubical covering graph.

**Weight enumerator identity.** If A_d(z) sums z^(turn weight) over shortest cycles and B_d(z) does so over all one-stationary-contact children, while R_d(C) counts the higher-weight children of parent C, then

B_d(z)=ell*(m-2)*A_d(z)+(z*z-1)*sum_C R_d(C)*z^(w_d(C)).

This follows directly from the stationary-child classification, with children changing weight by zero or two.

**Theorem 3 (adjacent two-port minima for arbitrary generator matroids).** The 2-design hypothesis is not needed to compare shortest cocircuit sectors. Add the second port q corresponding to the orientation-curvature class lambda=alpha+kappa. The shortest cocircuits containing both p,q and the shortest cocircuits containing p but excluding q have equal cardinality ell+2 and equal minimum intersection with every admissible coloring cycle. Their turn-cycle representatives are, respectively, shortest length-ell deck-geodesics and length-(ell+1) cycles with a sole stationary contact. Their equal-size parent/child map has ell*(m-2) children per parent. A stationary child has coloring-intersection equal to its parent's or greater by two.

*Proof.* If a monodromy-odd cycle C has r turn edges and s stationary contacts, the moving contacts form a generator walk representing t, so r-s>=ell. Curvature gives lambda(C)=1+s modulo two. In the both-port sector lambda=1, the minimum r=ell forces s=0. In the p-only sector lambda=0, the minimum r=ell+1 forces s=1. A shortest geodesic has odd cyclic turn weight; at any changed turn inserting an unused local edge state produces a length-(ell+1) p-only cycle without increasing the weight. Conversely the sole stationary contact of any p-only minimum cocircuit can be contracted to a geodesic, decreasing or preserving the weight. The stationary child count and coupling follow from the parent map. QED.


##### Detailed proof of the stationary-child count

A shortest \(\ell\)-generator representation \(A\in\mathcal F\) contains no nonempty dependent subset: deleting such a subset from its binary sum would give a shorter representation of \(t\). Hence its elements are linearly independent, and their translates generate an invariant \(\ell\)-cube \(Q_\ell\subseteq K\), since their sum is \(t\). The cosets of \(\operatorname{span}(A)\) number \(2^{r-\ell}\), and on each the quotient by translation by \(t\) is the folded \(\ell\)-cube. An antipodal geodesic is an ordering of the \(\ell\) directions with a chosen starting vertex, modulo the two deck choices, cyclic starting turn, and reversal. The count per invariant cube is
\[
\frac{2^\ell\ell!}{4\ell}=2^{\ell-2}(\ell-1)!.
\]
Thus every shortest \(A\) contributes \(2^{r-2}(\ell-1)!\) distinct quotient turn cycles. Different \(A\) have different sets of moving generator directions and produce distinct cycles.

For a cycle \(C'\) of length \(\ell+1\) with one stationary contact, remove its stationary state by the star-triangle shortcut. This gives a simple cycle \(C\) of length \(\ell\) with odd monodromy. Its \(\ell\) moving steps represent \(t\), so they use a shortest generator set with no repeated direction; \(C\) is a geodesic cycle. Contracting the sole stationary contact of \(C'\) determines the parent uniquely.

Conversely, in a quotient geodesic \(C\), each visited quotient base vertex is reached at most once, and its incident-edge star meets the turn cycle in the entering and departing edge states only. At each of its \(\ell\) turns, any one of the other \(m-2\) incident edge states gives a fresh line-graph vertex. Inserting that vertex between the two original states yields a simple cycle of length \(\ell+1\), with one stationary contact at the inserted state and no others. Different choices of the turn and the fresh state give different children, and contracting them recovers \(C\). The stationary-child fiber size is therefore \(\ell(m-2)\). This proves the count asserted in Theorem 1.

Let \(\widetilde G\to G\) be a connected regular two-sheeted cover of finite simple graphs, with free deck involution \(\tau\). Assume every vertex of \(G\) has degree at least three and
\[
\delta=\min_{x\in V(\widetilde G)}\operatorname{dist}_{\widetilde G}(x,\tau x)\ge3.
\]
Put \(H=L(G)\), let \(\alpha\in H^1(H;\mathbb F_2)\) be the monodromy class of the induced line-graph cover, let \(\kappa\) be the canonical line-graph contact-curvature class, and put \(\lambda=\alpha+\kappa\). Define the bipointed binary matroid
\[
D^{(2)}=M\!\left(\begin{array}{c|cc}B_H&0&0\\
a&1&0\\\lambda&0&1\end{array}\right)^*,
\]
with distinguished monodromy port \(p\) and curvature port \(q\).

**Theorem 1 (universal deck-displacement sector exchange).** Both the least cocircuit size in the sector containing \(p,q\) and the least cocircuit size in the sector containing \(p\) but avoiding \(q\) equal \(\delta+2\). For every admissible deck-odd coloring, with color cycle \(X_d=\operatorname{supp}(d)\cup\{p\}\),
\[
\boxed{\min_{\substack{Y\in\mathcal C^*(D^{(2)})\\p,q\in Y,\ |Y|=\delta+2}}|X_d\cap Y|
=\min_{\substack{Y\in\mathcal C^*(D^{(2)})\\p\in Y,\ q\notin Y,\ |Y|=\delta+2}}|X_d\cap Y|.}
\tag{1}
\]

*Proof.* Let \(C\) be a simple cycle of \(H\) with monodromy one, of length \(r\), and let \(s(C)\) count stationary contacts of its lifted cyclic edge-state walk. Removing the stationary contacts gives a walk in \(\widetilde G\) from some vertex \(x\) to its deck mate \(\tau x\) using \(r-s(C)\) edges, so
\[
r-s(C)\ge\delta,\qquad \lambda(C)\equiv1+s(C)\pmod2.
\tag{2}
\]
Choose a shortest \(x\)-to-\(\tau x\) path of length \(\delta\), with \(x\) chosen to minimize that distance globally. Its projected edge-state orbits are pairwise distinct: if two path edges were deck mates, their intervening subpath would provide a shorter path joining a vertex to its mate, contrary to the choice of \(\delta\). Its projected base-vertex orbits have no repetitions except the terminal identification, by the same argument and ordinary path simplicity. The \(\delta\) cyclic turns of its edge states therefore give a simple monodromy-one turn cycle of length \(\delta\), without stationary contacts. Its orientation-port phase is \(\lambda=1\), and adjoining \(p,q\) gives a cocircuit of cardinality \(\delta+2\), minimal by (2).

In the sector \(\lambda=0\), equation (2) forces \(s(C)\) odd and at least one; therefore \(r\ge\delta+1\), giving the same size lower bound for a cocircuit with port \(p\) alone. The shortest turn cycle has odd color-turn weight (because its monodromy is one), hence contains a changed turn. That turn belongs to a star clique whose underlying base-graph vertex has degree at least three. Since a shortest deck-geodesic uses only its two consecutive edge states at that base vertex, a third, unused state \(b\) is available. Replacing the changed turn \(va\) by \(v-b-a\) gives a simple cycle of length \(\delta+1\), with the same monodromy, opposite curvature parity, and the same integer turn cost, since the two new binary turn labels sum to one. Its associated p-only cocircuit has size \(\delta+2\).

Conversely, every p-only cocircuit of size \(\delta+2\) has a turn cycle of length \(r=\delta+1\), and by (2) its stationary count is necessarily \(s=1\). Contracting that single stationary contact by the balanced star-triangle shortcut produces a length-\(\delta\) simple odd-monodromy cycle whose integer cost does not exceed the original. This gives both inequalities between the minimum intersection costs and proves (1). \(\square\)

For the antipodal cover \(Q_n\to Q_n/\tau\), \(\delta=n\). For the ordered-pair cover \(S_n\to L(K_n)\) of ordinary boundary 3-tournaments, \(\delta=3\). The latter gives a theorem about short, five-element cocircuits, not a long forward vertex-simple tight-path guarantee.

**Corollary 2 (regular-cover stochastic domination).** If \(G\) is \(m\)-regular, the unique-stationary-contact contraction maps the \(p\)-only cocircuits of size \(\delta+2\) onto the both-port cocircuits of the same size, with \(\delta(m-2)\) children per parent. For a uniformly chosen both-port cocircuit \(A\) and a uniformly chosen \(p\)-only cocircuit \(B\), there is a coupling such that, for every admissible color cycle \(X_d\),
\[
\boxed{|X_d\cap A|\le |X_d\cap B|\le |X_d\cap A|+2.}
\tag{3}
\]
Consequently, for every integer \(u\),
\[
\boxed{\Pr(|X_d\cap A|\le u-2)\le
\Pr(|X_d\cap B|\le u)\le
\Pr(|X_d\cap A|\le u).}
\tag{4}
\]

*Proof.* Every shortest deck-geodesic meets each base-vertex star along its \(\delta\) cyclic turns using two incident edge-state orbits. Each turn has \(m-2\) unused states available for stationary insertion. Each child has a unique parent because it has one stationary contact; uniform sampling of the \(\delta(m-2)\) children per parent therefore gives a uniform parent. Replacing one turn by two turns either preserves the integer disagreement count or increases it by two. Adding the prescribed ports leaves total cocircuit cardinality fixed, proving (3) and (4). \(\square\)

**Necessity of the degree requirement.** For the connected antipodal two-cover \(C_{2\delta}\to C_\delta\), \(\delta\ge3\), the base has degree two. Its line graph is a cycle with one odd-monodromy turn cycle, of length \(\delta\) and no stationary contact. The both-port sector has a size-\(\delta+2\) cocircuit, but the \(p\)-only sector has none. Thus the hypothesis of minimum base degree at least three cannot be removed from Theorem 1.

#### Boundary-tournament two-class conservation

Take the connected ordered-pair cover \(S_n\to L(K_n)\), for \(n\ge4\), and put \(h=n-2\). Its quotient base graph \(G=L(K_n)\) has degree \(2h\). The shortest monodromy-odd turn cycles have length \(\delta=3\). They correspond to the triangles of \(L(K_n)\) formed by three edges of \(K_n\) sharing a common vertex, and their number is
\[
\boxed{N=n\binom{n-1}{3}=\frac{n(n-1)h(h-1)}6.}\tag{5}
\]
The unique-stationary-contact map gives \(3(2h-2)N\) \(p\)-only cocircuits of size five.

At a vertex \(x=\{u,v\}\) of \(G=L(K_n)\), the \(2h\) incident edges split into two classes of size \(h\), according to whether their original \(K_n\) edges meet \(\{u,v\}\) at \(u\) or at \(v\). Fix a lifted star and let \(a_x,b_x\) be the numbers of color-one states in these two classes.

**Theorem 3 (boundary two-class conservation law).** For an arbitrary reversal-odd boundary coloring, the number of stationary-contact children whose integer turn cost is two greater than that of their shortest parent is
\[
\boxed{\sum_{x=\{u,v\}} M_h(a_x,b_x),}\tag{6}
\]
where
\[
\begin{aligned}
M_h(a,b)&=\left[\binom a2+\binom b2\right](2h-a-b)
+\left[\binom{h-a}2+\binom{h-b}2\right](a+b)\\
&=\frac{h-2}{2}(a+b)(2h-a-b)+\frac h2(a-b)^2.
\end{aligned}\tag{7}
\]
Consequently the proportion of cost-preserving children is
\[
\boxed{1-\frac{\sum_xM_h(a_x,b_x)}{3(2h-2)n\binom{n-1}{3}}.}\tag{8}
\]

*Proof.* An odd-monodromy three-cycle of the quotient turn graph corresponds to three original complete-graph edges incident at one vertex. At a fixed base vertex \(x=\{u,v\}\) of \(L(K_n)\), a local turn belongs to such a cycle if and only if its two incident edges arise from original edges meeting the same endpoint of \(\{u,v\}\). For each same-class pair, the third original edge of the triangle is determined, so its incidence multiplicity is one; cross-class pairs have multiplicity zero. For a same-colored class pair, a stationary insertion adds two disagreements precisely when the third inserted edge state is opposite-colored. There are \(a+b\) color-one states and \(2h-a-b\) color-zero states in the whole star. Counting equal-color pairs within each of the two classes, and then their opposite-colored insertion states, yields the first expression in (7). Algebraic expansion gives the second expression. Each such insertion yields a distinct stationary-contact child with a unique parent. Summing over all quotient base vertices gives (6), and dividing by the uniform child count \(3(2h-2)N\) proves (8). \(\square\)

This is an association-class counterpart to the constant pair-incidence formula for cubelike 2-designs. The extra statistic \((a_x-b_x)^2\) records how the two local endpoint-port classes correlate with the coloring. The theorem concerns the full-turn boundary matroid's shortest cocircuits; it does not guarantee a long, coherent, vertex-simple tight path.

Let \(\widetilde G\to G\) be a connected regular two-sheeted cover of finite simple graphs, with deck displacement
\[
\delta=\min_{x\in V(\widetilde G)}\operatorname{dist}(x,\tau x)\ge3.
\]
Put \(H=L(G)\). Every simple cycle \(C\subseteq H\) of odd covering monodromy lifts to a cyclic sequence of edge states \(e_1,\ldots,e_r,e_{r+1}=\tau e_1\), with successive contact vertices \(u_i\), where \(u_0=\tau u_r\). Call \(e_i\) *stationary* when its preceding and following contacts coincide, \(u_{i-1}=u_i\), and *moving* otherwise. A **star-triangle pivot** replaces one edge of \(C\) by the other two edges of a triangle arising from three cover edges meeting at one vertex, or reverses this move, provided the new cycle remains simple and monodromy-odd.

**Theorem 1 (unique moving core and confluence).** For every odd-monodromy simple turn cycle \(C\), removing its stationary edge-state vertices by star-triangle contractions produces a simple odd-monodromy cycle \(C^\circ\) with no stationary contacts. The resulting cycle is independent of the order of these contractions: its cyclic edge-state sequence is obtained by deleting all stationary states from the original sequence. Every contraction preserves the ordered sequence of moving cover edges and their contact endpoints, and never increases integer turn cost for any deck-odd coloring.

*Proof.* If \(e_i\) is stationary, its two neighbors \(e_{i-1},e_{i+1}\) meet \(e_i\) at the same lifted vertex \(v\), so all three cover-edge states meet at \(v\). They define a star triangle in \(H\); shortcutting the two incident turn edges through the third deletes \(e_i\) and preserves simplicity, since \(C\) is simple and its length is at least \(\delta+1\ge4\) whenever a stationary state is present. A star triangle has covering monodromy zero, so odd monodromy survives. The two contact endpoints of every retained state remain unchanged under the shortcut, including at neighboring states. Thus their moving/stationary classifications are unchanged. Every deleted state was stationary before the deletion, and no new stationary state is created; induction proves that all removal orders delete the same set and leave the same cyclic moving-state order. The terminal cycle has at least \(\delta\ge3\) states, so it is a graph cycle. At a star triangle, the inequality \((a\oplus b)+(b\oplus c)\ge(a\oplus c)\) for binary edge-state colors proves the simultaneous nonincrease in integer cost. \(\square\)

**Theorem 2 (star-triangle exchange component theorem).** Form an undirected graph \(\mathscr E\) whose vertices are all simple odd-monodromy turn cycles of \(H\), joining two vertices when their edge-set symmetric difference is one balanced star triangle and both are simple. Then
\[
\boxed{C\text{ and }D\text{ lie in the same component of }\mathscr E
\iff C^\circ=D^\circ.}\tag{1}
\]
Every component has a unique minimum-length cycle, its stationary-free core. The core also minimizes every admissible integer turn cost over that entire component, simultaneously for all deck-odd edge colorings. The directed rewriting system obtained by orienting each pivot toward the shorter cycle is terminating and confluent.

*Proof.* Every stationary state can be deleted by a pivot, so every cycle is connected to its core. Conversely, a one-triangle expansion replaces a turn between states meeting at \(v\) by a two-turn detour through a previously unused edge state incident at \(v\). The inserted state has both contacts at \(v\), while the moving/stationary status and contacts of all original states are unchanged. Consequently both cycles have the same core. Induction along an exchange-graph path proves the forward implication of (1), while contracting both cycles to their common core proves the reverse implication. A stationary-free cycle admits no shortening pivot, every noncore cycle admits at least one, and Theorem 1 proves uniqueness and cost minimality. \(\square\)

**Corollary 3 (cube geodesic components and the directional-excess barrier).** In the folded cube turn graph \(H_n\), let \(q(C)\) denote the repeated-direction excess of Article XI. Star-triangle pivots preserve \(q(C)\) and the cyclic order of all moving coordinate directions. Among the monodromy-one cycles with \(q=0\), the exchange graph \(\mathscr E\) has
\[
\boxed{2^{n-2}(n-1)!}\tag{2}
\]
connected components, one for each antipodal-geodesic turn cycle. Every component is rooted at its distinguished length-\(n\) geodesic; its integer minimum turn cost equals the cost of that geodesic. No sequence of four-element curvature-port star-triangle cocircuit pivots can change the geodesic parent or decrease repeated-direction excess.

*Proof.* By the directional-excess identity, a stationary-free cycle with \(q=0\) has length \(n\) and is an antipodal geodesic. Theorem 2 identifies components with their stationary-free cores. The number of quotient geodesic turn cycles is \(2^{n-2}(n-1)!\), from the rooted directed count \(2^nn!\) divided by the \(4n\) choices of direction, sheet, and cyclic root representing the same turn cycle. Since the list of moving edge states is invariant under star-triangle pivots, so are their coordinate multiplicities and \(q\). \(\square\)

**Corollary 4 (constraint on a matroidal closure proof).** Let \(d\) be the turn cochain of an arbitrary antipodally odd cube-edge coloring. A strategy that starts with a minimum-cost monodromy-one cocircuit and uses only balanced four-element curvature-port cocircuits to simplify it will reach the stationary-free core of the *same moving walk*; it cannot reduce positive directional excess. Likewise, a strategy that starts from a geodesic cocircuit and makes only these local star-triangle pivots can never reach a different geodesic. Therefore any proof of unrestricted NORI1 by cocircuit exchange must additionally use an exchange relation that changes the moving direction word or its resource multiplicities. Adjacent square reroutings provide one candidate, but their turn weights need not decrease, as the strict exchange-local-minimum obstruction recorded in the generalizations research notes demonstrates.

The theorem also applies to the full-turn boundary-tournament cover, where it separates stationary contact removal from the remaining forward-polarity and vertex-injectivity defects.

### Hamilton path-forest overlaps and random boundary pattern universality

Let \(n\ge3\). Give each reversal-pair of distinct ordered triples an independent fair bit and its reverse the complementary bit. For a Hamilton vertex ordering \(\pi\), let \(W_b(\pi)\in\{0,1\}^{n-2}\) be its consecutive triple-color word. The \(n-2\) reversal-orbits along \(\pi\) are distinct, so \(W_b(\pi)\) is uniform.

**Theorem 1 (full-rank pattern second moment).** For any predetermined nonempty set \(A\subseteq\{0,1\}^{n-2}\), let \(Z\) count the Hamilton orders with word in \(A\), and put
\[
p=|A|2^{2-n},\qquad c_n=\frac{(e^2-1)(n-2)}{n(n-1)}.
\]
Then
\[
\boxed{\mathbb EZ=n!p,\quad\operatorname{Var}(Z)\le c_n(\mathbb EZ)^2,\quad
\Pr(Z>0)\ge(1+c_n)^{-1}.}
\tag{1}
\]
Moreover \(\Pr(Z<(1-\delta)\mathbb EZ)\le c_n/\delta^2\) for \(0<\delta<1\).

*Proof.* For two vertex permutations \(\pi,\sigma\), let \(K\) count the reversal-orbits of length-three windows they share. Their two color words together involve \(2(n-2)-K\) independent bits. Counting pairs of allowed words while disregarding compatibility on shared bits gives
\[
\Pr(W_b(\pi)\in A,\ W_b(\sigma)\in A)\le p^2 2^K.
\tag{2}
\]
Fix \(\pi\). Any \(k\) of its consecutive-triple windows contain a path forest of \(s\ge k+1\) edges of \(K_n\), with at most \(k\) nontrivial path components. For \(\sigma\) to contain all the selected triple-orbits, its consecutive adjacency edges must contain this forest. A path forest of \(s\) edges and \(c\) nontrivial components occurs in \(2^c(n-s)!\) permutations: orient each path component, contract it to one block, and permute all blocks. Thus
\[
\mathbb E_\sigma\binom Kk
\le\binom{n-2}k\frac{2^k(n-k-1)!}{n!}
=\frac{2^k(n-k-1)}{k!\,n(n-1)}.
\tag{3}
\]
Using \(2^K=\sum_{k=0}^K\binom Kk\), we obtain
\[
\mathbb E_\sigma 2^K\le1+
\frac{n-2}{n(n-1)}\sum_{k\ge1}\frac{2^k}{k!}
=1+c_n.
\tag{4}
\]
Sum (2) over all ordered permutation pairs to obtain
\(\mathbb E Z^2\le(1+c_n)(\mathbb EZ)^2\).
The variance estimate follows by subtraction, the positivity bound by Cauchy–Schwarz, and the lower-tail bound by Chebyshev. \(\square\)

**Corollary 2 (almost-all spanning one-turn boundary paths).** The number of binary words of length \(n-2\) with at most one color change is \(2(n-2)\). Therefore, if \(Z_{\le1}\) counts full spanning at-most-one-turn vertex-simple tight paths,
\[
\boxed{\mathbb EZ_{\le1}=n!(n-2)2^{3-n},\qquad
\Pr(Z_{\le1}=0)\le\frac{c_n}{1+c_n}=O(n^{-1}).}
\tag{5}
\]
With probability at least \(1-4c_n\), there are at least \(\frac12\mathbb EZ_{\le1}\) such paths. For any single prescribed color word, its realization by some Hamilton order has probability at least \(1/(1+c_n)\). Simultaneous realization of all color words is not claimed.

**Theorem 3 (fixed fractional Hamilton selector obstruction).** Let \(\lambda\) be an arbitrary distribution on Hamilton vertex paths selected independently of the tournament coloring, and let \(\operatorname{sw}_b(\pi)\) count the changes along its triple-color word. Then
\[
\boxed{\mathbb E_b\mathbb E_{\pi\sim\lambda}\operatorname{sw}_b(\pi)=\frac{n-3}{2}.}
\tag{6}
\]
In particular, for \(n\ge6\), some reversal-odd coloring has \(\mathbb E_{\pi\sim\lambda}\operatorname{sw}_b(\pi)>1\).

*Proof.* For any fixed \(\pi\), its two successive triple windows lie in distinct reversal-orbits and their colors are independent fair bits. Each of its \(n-3\) change indicators therefore has expectation \(1/2\). Average first over \(b\), then over \(\lambda\). Some coloring attains at least that mean. \(\square\)

**Graphic-matroid interpretation.** A Hamilton path's \(n-1\) edges form a basis of \(M(K_n)\), with the additional degree-two path condition. Each triple window is a two-edge flag of that basis. Any \(k\) common flags between two Hamilton words require at least \(k+1\) shared graphic basis edges. This additional edge gives the \(O(n^{-1})\) overlap-energy bound. The results are full-resource and all-dimensional, but do not close the worst-case spanning one-turn conjecture. Theorem 3 precludes a coloring-independent fractional basis mixture as a universal average-cost certificate; the missing witness must adapt to the coloring and preserve the integral path constraints.

Let \(n\ge4\), and let \(H_n=L(Q_n/\tau)\) be the folded-cube turn graph. Retain Article XI's monodromy and contact-curvature classes \((\alpha,\kappa)\), and the bipointed dual matroid \(D_n^{(2)}\) with ports \(p,q\), with orientation signature \(\lambda=\alpha+\kappa\). Write \(\mathcal G_n\) for the antipodal-geodesic turn cycles of \(H_n\).

**Theorem 1 (balanced hexagon exchange).** Let \(C\in\mathcal G_n\), and choose two consecutive coordinate directions \(a,b\) in its cyclic direction word. Exchanging their traversal order produces another geodesic turn cycle \(C'\in\mathcal G_n\) with
\[
\boxed{C\mathbin{\triangle}C'=Z,}
\tag{1}
\]
where \(Z\) is a simple six-edge cycle of \(H_n\) with
\[
\boxed{\alpha(Z)=\kappa(Z)=\lambda(Z)=0.}
\tag{2}
\]
Thus \(Z\) itself is a six-element cocircuit of \(D_n^{(2)}\) avoiding both distinguished ports, and the two geodesic cocircuits satisfy
\[
\boxed{(C\cup\{p,q\})\mathbin{\triangle}Z=C'\cup\{p,q\}.}
\tag{3}
\]
For every antipodally odd edge coloring with turn cochain \(d\),
\[
\boxed{w_d(C')-w_d(C)\in\{-2,0,2\}.}
\tag{4}
\]

*Proof.* Root the cyclic geodesic so the exchanged directions occur consecutively, and denote its corresponding four successive edge states (on the cyclic lift) by \(U,A,B,V\). The alternative route around the elementary cube square uses edge states \(B',A'\) instead of \(A,B\), with the same predecessor \(U\) and successor \(V\). Hence the affected turn paths are
\[
U-A-B-V,\qquad U-B'-A'-V.
\]
They are internally vertex-disjoint in \(H_n\). Indeed the edge-state directions of \(A,B\) are distinct and occur only once in a geodesic; the alternative edges \(A',B'\) are different cube edges of those same directions, neither antipodal translates of the original edges nor one another. For \(n\ge4\), the two unchanged neighboring states \(U,V\) are also different. Therefore the symmetric difference of the two geodesic cycles is the simple turn hexagon
\[
Z=U-A-B-V-A'-B'-U.
\]
Both geodesic cycles have covering monodromy one and have no stationary contacts, hence \((\alpha,\kappa)=(1,0)\); their symmetric difference has signatures \((0,0)\). A simple turn cycle with zero monodromy and zero orientation curvature is a circuit of the primal two-port incidence matrix without either port, hence is a cocircuit of \(D_n^{(2)}\). This proves (1)–(3).

Only the three consecutive turn costs along the two displayed paths differ. Since the admissible cochain \(d\) evaluates to zero on the balanced hexagon, the sums on the two three-edge paths have the same parity; each is between zero and three. Their difference must therefore be \(-2,0,\) or \(2\), proving (4). \(\square\)

**Theorem 2 (global connectivity by port-free hexagons).** The graph whose vertices are \(\mathcal G_n\), with edges joining pairs related by the balanced hexagon exchange of Theorem 1, is connected.

*Proof.* Represent a geodesic by a starting cube vertex \(x\in\mathbb F_2^n\) and a permutation \(\pi\) of the coordinate directions, modulo identifying representations of the same cyclic antipodal turn cycle. Adjacent coordinate transpositions generate the full symmetric group, so Theorem 1 connects every two direction orders at a fixed \(x\). Cyclically rerooting one geodesic after its first edge replaces \((x,(i,\pi_2,\ldots,\pi_n))\) by the representation
\[
(x+e_i,(\pi_2,\ldots,\pi_n,i))
\]
of the same turn cycle. Because transpositions can move any chosen coordinate \(i\) to the first position, this identification connects the directions' permutation classes at \(x\) and at \(x+e_i\). The edges \(x\leftrightarrow x+e_i\) generate the whole cube, so all starting vertices and all direction orders lie in one connected exchange graph. \(\square\)

**Corollary 3 (two-generator presentation of the zero-resource-excess exchange geometry).** Let \(\mathcal Z_0\) be the family of monodromy-one simple turn cycles of \(H_n\) with repeated-direction excess \(q(C)=0\). Equip \(\mathcal Z_0\) with two types of allowable symmetric-difference moves:

(i) a balanced star triangle, which toggles the curvature port in the bipointed matroid and inserts or removes one stationary edge state; and

(ii) a balanced turn hexagon as in Theorem 1, applied at a stationary-free geodesic, which changes the cyclic order of two neighboring coordinate directions while preserving both port sectors.

Then the resulting exchange graph on \(\mathcal Z_0\) is connected for every \(n\ge4\).

*Proof.* By the unique-core theorem in the preceding Subsection, every \(C\in\mathcal Z_0\) contracts using moves of type (i) to its unique stationary-free core. Since \(q(C)=0\), that core is a length-\(n\) antipodal geodesic cycle. Theorem 2 connects any two such cores by moves of type (ii). Reversing the star-triangle contractions of a chosen destination cycle then yields a path between any two cycles of \(\mathcal Z_0\). \(\square\)

**Corollary 4 (discrete intermediate-value property).** For any antipodally odd coloring, the set of integer cyclic turn weights attained by antipodal geodesics is an interval of odd integers:
\[
\boxed{\{w_d(C):C\in\mathcal G_n\}=
\{m,m+2,\ldots,M\}}
\tag{5}
\]
for some odd \(m\le M\). This statement does not assert \(m=1\).

*Proof.* The geodesic exchange graph is connected by Theorem 2. Along every exchange edge, the integer weight changes by at most two and preserves odd parity by Theorem 1. A path connecting a minimum-weight and a maximum-weight geodesic must therefore encounter every intermediate odd value. \(\square\)

The spanning one-turn boundary-tournament conjecture involves a different marked gallery language, so these cube-specific exchange generators do not by themselves supply the desired resource-independent directed tournament connector. Moreover, the nonoptimal strict exchange-local minima constructed for \(n\ge9\) in the research notes show why connectivity and the local two-unit cost bound cannot be strengthened to universal monotone descent.

Let \(G\) be a finite connected simple graph with at least two edges, and write \(H=L(G)\). A **turn** of \(G\) is a pair of distinct edges incident with a vertex \(v\); it is an edge of \(H\) and has a uniquely determined center \(v\). For each \(v\in V(G)\), the turns centered at \(v\) form the complete star clique \(K_v\cong K_{\deg_G(v)}\) inside \(H\). Their edge sets partition \(E(H)\).

For \(z\in Z(H)\), the binary cycle space of \(H\), define, for each original edge \(e=uv\in E(G)\),
\[
\Phi_G(z)_e
=\sum_{\substack{h\in E(K_u)\\ h\text{ incident with }e}}z_h
=\sum_{\substack{h\in E(K_v)\\ h\text{ incident with }e}}z_h
\pmod2.
\tag{1}
\]
The two sums agree because the full degree of the vertex \(e\) in the Eulerian turn set \(z\) is even.

**Theorem 1 (canonical line-graph cycle-space sequence).** The map \(\Phi_G\) is a well-defined surjective linear map \(Z(H)\to Z(G)\), and its kernel is the direct sum of the local star-clique cycle spaces:
\[
\boxed{
0\longrightarrow
\bigoplus_{v\in V(G)}Z(K_{\deg_G(v)})
\longrightarrow Z(L(G))
\xrightarrow{\ \Phi_G\ } Z(G)
\longrightarrow0.
}
\tag{2}
\]
In particular, \(\ker\Phi_G\) is generated by the star triangles of \(H\), and
\[
\boxed{\dim\ker\Phi_G
=\sum_{v\in V(G)}\binom{\deg_G(v)-1}{2}.}
\tag{3}
\]

*Proof.* Because \(z\in Z(H)\), the number of turns from \(z\) incident with each vertex \(e\) of \(H\) is even. The incident turns partition according to the two endpoints \(u,v\) of the original edge \(e\), making the two parity sums in (1) equal. At any original vertex \(u\in G\), summing the coefficients \(\Phi_G(z)_e\) over \(e\ni u\) counts every turn in \(K_u\) twice, and hence vanishes over \(\mathbb F_2\). Thus \(\Phi_G(z)\) is Eulerian in \(G\).

Every simple cycle \(e_1,\ldots,e_k\) of \(G\) lifts to the simple turn cycle \((e_1,e_2),\ldots,(e_k,e_1)\) of \(H\). Each original edge state then has one incident turn at each endpoint, so its image under \(\Phi_G\) is the original cycle. Simple cycles generate \(Z(G)\), proving surjectivity.

Now \(\Phi_G(z)=0\) precisely when every edge-state vertex \(e\) has even degree separately in each star clique \(K_u\) containing it. Since the turn edge sets of distinct star cliques are disjoint, this is equivalent to \(z|_{K_u}\in Z(K_u)\) for every original vertex \(u\). The kernel is therefore the asserted direct sum. Each complete-graph cycle space is generated by its triangles and has dimension \(\binom{\deg(u)-1}{2}\), proving (2) and (3). \(\square\)

If \(\widetilde G\to G\) is a connected two-sheeted graph covering with monodromy \(\beta:Z(G)\to\mathbb F_2\), its induced line-graph monodromy satisfies
\[
\boxed{\alpha=\beta\circ\Phi_G\quad\text{on }Z(H).}
\tag{4}
\]
Indeed any lifted turn cycle walks between contact vertices along the original edges counted by \(\Phi_G\), and stationary contacts contribute no moving edge. Hence the cover-sheet change depends only on the projected Eulerian base-graph cycle. Star triangles have zero monodromy and lie in the kernel of \(\Phi_G\).

Equation (2) is a canonical algebraic distinction between **local stationary-contact geometry**, carried by the kernel, and **global moving-walk homology**, carried by \(Z(G)\). It is independent of coloring and applies equally to the cube and ordered-pair boundary-tournament graph covers.

**Theorem 2 (cube triangle-square presentation).** For n>=3, put G_n=Q_n/tau and H_n=L(G_n). Let T denote all local star triangles in H_n and S the turn cycles corresponding to projected coordinate squares of Q_n. Then the binary cycle space of H_n has kernel of covering monodromy alpha equal to span(T union S). Together with any one antipodal-geodesic turn cycle C0, these generators span the entire cycle space. Thus the quotient by the star triangles and projected squares has dimension one, generated by C0.

*Proof.* First, the cycle space of the ordinary cube \(Q_n\) is generated by its coordinate squares. An elementary induction proves this: write \(Q_n\) as two copies of \(Q_{n-1}\) connected by matching edges of the last coordinate. Any Eulerian edge set has an even number of matching edges. Square boundaries involving the last coordinate let one transport those matching-edge incidences along paths within the lower-dimensional cube and eliminate them in pairs. What remains is a sum of Eulerian chains within the two copies of \(Q_{n-1}\), which are generated by squares by induction.

Next, if \(\pi:Q_n\to G_n\) is the two-cover, the image of the pushforward \(\pi_*:Z(Q_n)\to Z(G_n)\) is precisely the kernel of covering monodromy \(\beta\). Every closed lifted cycle has zero monodromy downstairs. Conversely, for an Eulerian base edge set \(z\) with \(\beta(z)=0\), traverse its Eulerian components, joining separate components by auxiliary paths traversed twice. The resulting closed base walk represents \(z\) modulo two and has zero monodromy, so it lifts to a closed walk upstairs. Its mod-two edge vector is a cycle of \(Q_n\) whose pushforward equals \(z\). Hence \(\ker\beta\) is generated by projections of cube squares.

For an even-monodromy turn cycle z, its moving-chain projection has zero base monodromy. It is therefore generated by projected coordinate squares. Subtract the associated turn cycles to land in the kernel of the line-graph projection, which Theorem 1 identifies with the span of star triangles. Conversely every listed generator has zero monodromy. One geodesic turn cycle has odd monodromy and supplies the remaining quotient generator. QED.

Let \(F\) be a connected finite simple graph, and define its *ordered-edge state graph* \(S(F)\) as follows: vertices are oriented edges \((u,v)\) of \(F\), and \((u,v)\) is adjacent to \((v,w)\) whenever \(u,v,w\) are pairwise distinct and \(\{u,v\},\{v,w\}\in E(F)\). The deck involution is reversal \(\tau(u,v)=(v,u)\), and the natural quotient map is
\[
\pi:S(F)\longrightarrow L(F),\qquad
(u,v)\longmapsto\{u,v\}.
\]
It is a regular two-sheeted graph covering; it need not be connected for an arbitrary \(F\). For \(F=K_n\), \(n\ge4\), the cover is connected.

Orient the edges of \(F\) arbitrarily. For each turn \(t\in E(L(F))\) between edges \(e,f\) incident at \(v\), let \(\kappa_F(t)=1\) if their reference orientations have equal incidence senses at \(v\), and let \(\kappa_F(t)=0\) otherwise. As in Article XI, the cohomology class of \(\kappa_F\) is independent of the reference edge orientations.

**Theorem 1 (ordered-edge covering classified by line-graph curvature).** The two-cover \(S(F)\to L(F)\) has covering-transition cochain \(\kappa_F\). In particular,
\[
\boxed{\beta_{S(F)/L(F)}=[\kappa_F]\in H^1(L(F);\mathbb F_2).}\tag{1}
\]

*Proof.* Represent a lifted state of an edge \(e\) by a sheet bit \(\varepsilon\), with zero indicating the chosen reference orientation and one indicating its reversal. Let \(h(e,v)\in\mathbb F_2\) be one if the reference orientation of \(e\) points into \(v\), and zero otherwise. The incidence sense of sheet \(\varepsilon\) at \(v\) is \(h(e,v)+\varepsilon\). Two lifted edge states representing incident edges \(e,f\) are adjacent in \(S(F)\) precisely when one points into their common vertex \(v\) and the other points out. Thus their sheet bits obey
\[
(h(e,v)+\varepsilon)+(h(f,v)+\varepsilon')=1,
\]
or
\[
\boxed{\varepsilon+\varepsilon'=1+h(e,v)+h(f,v)=\kappa_F(t).}
\]
This relation is the transition rule of the two-sheeted covering, proving (1). Reorienting reference edges adds a cut to the transition cochain and leaves its cohomology class unchanged. \(\square\)

**Corollary 2 (boundary monodromy is lower-level contact curvature).** Let \(n\ge4\), put \(F=K_n\), \(G=L(K_n)\), and \(H=L(G)=L^2(K_n)\). The connected double cover used for ordinary reversal-odd boundary tournaments is \(S(K_n)\to G\). Its induced line-graph covering \(L(S(K_n))\to H\) has monodromy
\[
\boxed{\alpha_{\mathrm{BT}}=\kappa_{K_n}\circ\Phi_{L(K_n)}
\quad\text{on }Z(L^2(K_n)),}\tag{2}
\]
where \(\Phi_{L(K_n)}:Z(L^2(K_n))\to Z(L(K_n))\) is the moving-cycle projection from the preceding Subsection.

*Proof.* Apply the naturality of covering monodromy under the moving-cycle projection, \(\alpha=\beta\circ\Phi_G\), from the preceding Theorem. Theorem 1 identifies \(\beta\) with the contact-curvature class \(\kappa_{K_n}\). \(\square\)

The cube and ordinary boundary-tournament pointed matroids thus have a shared signed-line-cover construction but different **origins of the monodromy port**: in the cube it records the global antipodal class of the folded cube; in the boundary construction it is the preceding line graph's local contact-curvature class. This explains the three-turn odd cycles in the boundary model and the dimension-growing odd girth in the cube, without claiming an automatic transfer of long resource-simple witnesses.

**Theorem 3 (three-level cycle-space generation for boundary tournaments).** Let \(n\ge4\), \(F=K_n\), \(G=L(F)\), and \(H=L(G)\). The two line-graph moving-cycle maps form a tower of surjections
\[
\boxed{Z(H)\xrightarrow{\Phi_G}Z(G)\xrightarrow{\Phi_F}Z(F),}\tag{3}
\]
whose kernels are the direct sums of their respective vertex-star clique cycle spaces. Consequently \(Z(H)\) is generated over \(\mathbb F_2\) by three classes:

(i) star triangles of \(H\), centered at the vertices of \(G\);

(ii) lifted turn cycles in \(H\) of star triangles of \(G=L(K_n)\), centered at original vertices of \(K_n\);

(iii) double-lifted turn cycles in \(H\) of ordinary triangles of \(K_n\).

On these three classes, the boundary covering monodromy \(\alpha_{\mathrm{BT}}\) takes the values \(0,1,0\), respectively.

*Proof.* The line-graph cycle-space sequence of the preceding Subsection applies first to \(G\), then to \(F\), giving the two maps and the stated kernels. An arbitrary cycle of \(H\) differs from a lift of its \(\Phi_G\)-image by a sum of type-(i) local star triangles. The \(\Phi_G\)-image in \(Z(G)\) differs from a lift of its image under \(\Phi_F\) by a sum of star triangles of \(G\); lifting those triangles to \(H\) gives type (ii). Finally \(F=K_n\), whose binary cycle space is generated by its ordinary triangles; twice lifting these gives type (iii). This proves spanning.

By Corollary 2, \(\alpha_{\mathrm{BT}}=\kappa_F\circ\Phi_G\). A top-level star triangle has \(\Phi_G=0\), so its monodromy is zero. A lifted type-(ii) triangle maps under \(\Phi_G\) to a star triangle of \(G\), and \(\kappa_F\) evaluates to one on every such triangle by the star-curvature identity. A type-(iii) double-lift projects to a simple cycle of \(F=K_n\), whose consecutive original edges contact distinct endpoints, so its contact-curvature is zero. These give the three claimed monodromy values. \(\square\)

**Corollary 4 (dimension and structural distinction).** The tower gives
\[
\boxed{\dim Z(L^2(K_n))=
\binom n2\binom{2n-5}{2}
+n\binom{n-2}{2}+\binom{n-1}{2}.}\tag{4}
\]
The first summand counts independent top-level star-clique cycles, the second independent lower-level star-clique cycles, and the third the dimension of the underlying complete-graph cycle space. Although the monodromy kernel in either canonical model has codimension one, the distinguished nonzero class is generated locally in the boundary model (a lifted lower-stage star triangle), but is generated by a global antipodal geodesic in the cube model after all star triangles and projected squares are factored out.

This tower is a useful test for prospective intrinsic matroid generalizations: cographic deletion and two-port signature algebra survive both constructions, yet the depth at which their nonzero covering class arises differs. A universal long-path theorem must therefore also control the marked coherent resource-independent galleries rather than merely the shortest cocircuit sector.

### Zero-turn contraction, pointed odd girth, and the cube geodesic distance defect

Let \(\widetilde G\to G\) be a connected regular two-sheeted graph cover, with induced connected turn cover over \(H=L(G)\). Let \(a\in C^1(H;\mathbb F_2)\) represent the covering-monodromy class. The pointed lift dual from Article XI is
\[
D=M\begin{pmatrix}B_H&0\\ a&1\end{pmatrix}^{*},
\tag{1}
\]
with distinguished port \(p\). Any deck-odd coloring gives \(d=a+\delta f\); its associated port-containing binary cycle is \(X_d=\operatorname{supp}(d)\cup\{p\}\).

The dependence on the coloring can be consolidated into a smaller **signed contraction graph**. This gives a full characterization of *unrestricted* port-cocircuit intersection and, in the cube, a metric distance defect whose vanishing is equivalent to NORI1.

#### 1. Zero-turn contraction and pointed odd girth

Define \(H_0(d)=(V(H),\{e:d(e)=0\})\), with all original vertices and only zero-turn edges. Contract each connected component of \(H_0(d)\) to one vertex; retain all edges \(e\) with \(d(e)=1\), including parallel edges and loops. Denote the resulting multigraph by \(K_d\). A loop has odd-girth contribution one. Let \(\operatorname{og}(K_d)\) denote the minimum edge count of an odd cycle, with \(+\infty\) if none exists.

**Theorem 1 (zero-turn odd-girth normal form).** For any deck-odd coloring and its pointed cycle \(X_d\),
\[
\boxed{
\min_{\substack{Y\in\mathcal C^*(D)\\p\in Y}}
|X_d\cap Y|
=1+\operatorname{og}(K_d).
}
\tag{2}
\]
The contracted graph \(K_d\) is nonbipartite (where loops count as odd cycles), so its odd girth is finite. More precisely, the contraction of the *primal* pointed matroid (1) by all zero-turn elements is represented, after elementary row operations, by
\[
\boxed{
\widehat M/H_0(d)\cong
M\begin{pmatrix}B_{K_d}&0\\ \mathbf1&1\end{pmatrix},
}
\tag{3}
\]
where \(\widehat M=D^*\), \(B_{K_d}\) is the incidence matrix of the contracted multigraph, and \(\mathbf1\) assigns one to each retained graph edge. The dual statement is deletion of the zero-turn elements from \(D\).

*Proof.* Replace the bottom row \(a\) in (1) by \(d=a+\delta f\) using vertex-incidence row operations. The columns corresponding to \(d=0\) then have bottom entry zero; contracting them identifies precisely the vertices in each connected component of \(H_0(d)\). The remaining columns represent \(B_{K_d}\) with bottom entry one, and the port still has bottom entry one, proving (3).

By the pointed covering representation, a port-containing cocircuit of \(D\) has the form \(Y_C=C\cup\{p\}\) for a simple cycle \(C\subseteq H\) with monodromy one, and
\[
|X_d\cap Y_C|=1+w_d(C),\qquad
w_d(C)=\sum_{e\in C}d(e),
\tag{4}
\]
where \(w_d\) is an integer. Since \(d\) represents monodromy, \(w_d(C)\) is odd.

Under the component contraction, \(C\) becomes a closed walk in \(K_d\) having \(w_d(C)\) edges: all zero turns have been contracted. Every odd closed walk contains an odd simple cycle, possibly a loop. Consequently
\(\operatorname{og}(K_d)\le w_d(C)\).

Conversely, take a shortest odd cycle of \(K_d\), of length \(g=\operatorname{og}(K_d)\). For each pair of its consecutive retained edges meeting at a contracted vertex, join their original endpoints by a path of zero turns inside the corresponding component of \(H_0(d)\). These zero paths and the \(g\) retained edges assemble a closed walk of \(H\) with odd monodromy and total integer turn weight \(g\). Split this closed walk into simple cycles, discarding paired traversals. Its mod-two turn sum is one, so at least one simple component has odd monodromy and weight at most \(g\). This gives a port cocircuit intersecting \(X_d\) in at most \(1+g\), proving (2).

Finally, if \(K_d\) were bipartite, its constant-one edge cochain would be a cut. Pulling that cut back through the zero-turn components would make \(d\) a cut of \(H\), contradicting the nonzero covering-monodromy class \(a\). Thus \(K_d\) has an odd cycle. \(\square\)

**Corollary 2 (single-disagreement loops).** A port cocircuit \(Y\) with \(|X_d\cap Y|=2\) exists if and only if \(K_d\) has a loop; equivalently, some positive-turn edge \(e=uv\) has both endpoints in the **same** connected component of \(H_0(d)\).

For the folded cube, the established nongeodesic monochromatic-antipodal-path theorem supplies this loop for every antipodally odd coloring. The open geodesic conjecture asks for a loop with a much stronger distance property.

#### 2. The cube zero-turn metric

Let \(n\ge4\), \(G_n=Q_n/\langle\tau\rangle\), \(H_n=L(G_n)\), and \(d\) be any deck-odd cube-edge coloring signature. Let
\[
\mathcal L_d=
\{\,e=uv\in E(H_n): d(e)=1,\ 
u,v\text{ lie in one component of }H_0(d)\,\}.
\tag{5}
\]
These are precisely the positive-turn edges that become loops of \(K_d\). For \(e=uv\in\mathcal L_d\), let \(\operatorname{dist}_{H_0(d)}(u,v)\) be their ordinary shortest-path distance using only zero-turn edges, and put
\[
\boxed{\ell_1(d)=
1+\min_{uv\in\mathcal L_d}
\operatorname{dist}_{H_0(d)}(u,v),}
\tag{6}
\]
taking \(+\infty\) when \(\mathcal L_d\) is empty.

**Theorem 3 (quantized geodesic distance defect).** When \(\mathcal L_d\ne\varnothing\), there exists an integer \(q_d\ge0\) such that
\[
\boxed{\ell_1(d)=n+2q_d.}
\tag{7}
\]
Moreover,
\[
\boxed{
\text{A full monochromatic antipodal geodesic exists}
\iff \ell_1(d)=n
\iff \min_{uv\in\mathcal L_d}\operatorname{dist}_{H_0(d)}(u,v)=n-1.
}
\tag{8}
\]
In particular, a hypothetical coloring refuting NORI1 must satisfy
\[
\boxed{
\operatorname{dist}_{H_0(d)}(u,v)\ge n+1
\quad\text{for EVERY }uv\in\mathcal L_d.
}
\tag{9}
\]

*Proof.* Every \(e=uv\in\mathcal L_d\), together with a shortest zero-turn path from \(u\) to \(v\), forms a simple turn cycle \(C_e\) with \(w_d(C_e)=1\). Thus \(\ell_1(d)\) is the minimum length of a simple odd-monodromy turn cycle containing precisely one positive-turn edge. Every odd-monodromy simple turn cycle in \(H_n\) has length at least \(n\), by the antipodal displacement bound of Article XI.

Choose such a cycle of minimum length, \(C\). If it contains a stationary edge state, the star-triangle shortening theorem permits deleting that state while retaining simplicity and odd monodromy. Its two incident turn labels are binary, and the shortcut label is their XOR. Since \(C\) contains only one positive-turn label, the integer turn cost of the shortened cycle is still one (it cannot be zero, by odd monodromy). This contradicts the minimum choice. Consequently \(C\) has no stationary contacts.

Its lifted edge-state sequence therefore represents a moving cube walk from \(x\) to \(x^*\), of length \(|C|=\ell_1(d)\). Each of the \(n\) coordinate directions appears an **odd positive** number of times in such a walk. Hence the length is \(n+2q_d\) for a nonnegative integer \(q_d\), proving (7).

If \(\ell_1(d)=n\), the lifted walk uses each coordinate once, so it is a full antipodal geodesic. Its cyclic turn word has one nonzero label; choose the root immediately after that turn, making all \(n-1\) internal turns zero. Conversely, a monochromatic full antipodal geodesic has precisely one cyclic nonzero turn (its closing seam, by reversal oddness); its turn cycle has length \(n\), showing \(\ell_1(d)\le n\). The antipodal lower bound forces equality. Formula (6) gives the remaining equivalence, and (7) gives (9) under the negation. \(\square\)

**Corollary 4 (explicit graph algorithm).** For a supplied cube coloring, the existence of a full monochromatic antipodal geodesic can be decided without enumerating \(n!\) coordinate permutations. Form \(H_0(d)\), find its connected components, and for every positive-turn edge \(uv\) internal to a zero component run a shortest-path search from \(u\) to \(v\) in \(H_0(d)\). A shortest path with \(n-1\) edges together with \(uv\) certifies a monochromatic antipodal geodesic. A direct implementation takes
\[
O\bigl(|E(H_n)|(|V(H_n)|+|E(H_n)|)\bigr)
\]
time and linear working space in the explicit turn graph. The method does not decide the all-dimensional conjecture uniformly; it decides the instance given by its complete edge coloring.

#### 3. What the contraction preserves and what it loses

Theorem 1 settles the **unrestricted minimum port-cocircuit intersection** as an odd-girth calculation after zero-turn contraction. But contraction discards both the number of zero turns used between positive turns and the moving-coordinate resources of the lift. A loop of \(K_d\) is therefore not necessarily a geodesic cocircuit: its shortest zero path can contain repeated moving directions, forcing a cycle of length \(n+2q_d\) with \(q_d>0\).

The distinction is now measured by the intrinsic nonnegative integer \(q_d\). Existing unrestricted port-two intersection results guarantee that \(q_d\) is finite for the cube. NORI1 is equivalent to \(q_d=0\). Any general matroid theorem proving that a point-loop of the zero-turn contraction can be **shortened to the covering-displacement distance** under the folded-cube exchange axioms would establish NORI1. The star-triangle shortening theorem removes stationary contacts but preserves moving-direction multiplicities; balanced hexagon exchanges alter the coordinate order but need not reduce the repeated-direction excess. Thus the remaining obstruction is a metric/resource defect, not a deficit of pointed-matroid parity.

#### 4. Intrinsic binary-matroid port-parallelism formulation

The graph contraction above is a special case of a matroid identity that does not assume a graph-cover representation.

**Lemma 5 (port-cocircuit intersection as a dual-minor circuit girth).** Let \(D\) be a finite matroid, \(p\in E(D)\), and \(X\subseteq E(D)\) with \(p\in X\). Put \(S=E(D)\setminus X\) and \(N=D^*/S\). Then
\[
\boxed{
\min_{\substack{Y\in\mathcal C^*(D)\\p\in Y}}
|X\cap Y|
=\min_{\substack{C\in\mathcal C(N)\\p\in C}}|C|.
}
\tag{10}
\]
Either minimum may be infinite if there is no relevant circuit or cocircuit.

*Proof.* Every circuit \(C\) of the contraction \(D^*/S\) lifts to a circuit \(Y\) of \(D^*\) with \(Y\setminus S=C\); this is the circuit description of matroid contraction. Hence the left-hand minimum is at most the right-hand minimum. Conversely, if \(Y\) is a circuit of \(D^*\) containing \(p\), then \(p\) lies in the closure of \(Y\setminus\{p\}\). After contracting \(S\), it still lies in the closure of \((Y\cap X)\setminus\{p\}\) in \(N\). Therefore a circuit \(C\) of \(N\) containing \(p\) exists inside \(Y\cap X\), and \(|C|\le|Y\cap X|\). This proves the reverse inequality. \(\square\)

**Corollary 6 (unrestricted two-intersection is parallelism).** If \(D\) is binary and \(X\in Z(D)\) contains \(p\), then \(p\) is **not a loop** of the contracted dual minor \(N=D^*/(E(D)\setminus X)\). Moreover
\[
\boxed{
\exists Y\in\mathcal C^*(D)\ (p\in Y,\ |X\cap Y|=2)
\iff
p\text{ belongs to a two-element parallel circuit of }N.
}
\tag{11}
\]
In the signed-cover representation, the parallel element is a positive-turn loop of \(K_d\): both its column and the port column of the contracted primal matrix (3) are \((0,\ldots,0,1)^\mathsf T\).

*Proof.* Binary cycle–cocircuit orthogonality forbids any one-element intersection of \(X\) with a cocircuit containing \(p\). Lemma 5 thus forbids a port loop in \(N\) and identifies intersection two with a two-element port circuit of \(N\). In (3), a positive graph loop has zero incidence column and bottom entry one, as does the port, proving the claimed correspondence. \(\square\)

This provides a fully matroid-intrinsic unrestricted two-intersection criterion, independent of shortest-cocircuit size. The remaining cube conjecture additionally asks that a corresponding lifted port cocircuit have size \(n+1\). The contraction minor forgets the lengths of its contracted zero-turn paths; Theorem 3 measures precisely that lost resource-length information by \(q_d\).

#### 5. Graphic-matroid fundamental circuits and a basis-selection form of NORI1

The distance defect of Theorem 3 can also be expressed using **basis exchange inside a graphic matroid**, without referencing a selected path. Let \(M_0=M(H_0(d))\), the cycle matroid of the zero-turn graph, and let \(\mathcal B_0\) be its set of spanning-forest bases. For \(T\in\mathcal B_0\) and a positive edge \(e=uv\in\mathcal L_d\), let \(C_T(e)\) be the unique fundamental circuit of \(e\) relative to \(T\) in the full graphic cycle matroid \(M(H_n)\). Equivalently, \(C_T(e)\) is \(e\) together with the unique tree path connecting its ends.

**Proposition 7 (basis-choice formula for the defect).** For any antipodally odd cube-edge coloring with \(\mathcal L_d\ne\varnothing\),
\[
\boxed{
\ell_1(d)=\min_{\substack{T\in\mathcal B_0\\e\in\mathcal L_d}}
|C_T(e)|,\qquad
q_d=\frac12\left(
\min_{\substack{T\in\mathcal B_0\\e\in\mathcal L_d}}|C_T(e)|-n
\right).
}
\tag{12}
\]
Consequently,
\[
\boxed{\text{NORI1 for this coloring}\iff
\exists\,T\in\mathcal B_0,\ e\in\mathcal L_d:\ |C_T(e)|=n.}
\tag{13}
\]

*Proof.* Every \(T\in\mathcal B_0\) joins the endpoints of every \(e\in\mathcal L_d\) by a zero-turn tree path, so \(|C_T(e)|-1\ge\operatorname{dist}_{H_0(d)}(u,v)\). Conversely, a shortest zero-turn path \(P\) from \(u\) to \(v\) is an independent set of the graphic matroid \(M_0\) and can be extended to a spanning-forest basis \(T\). Because \(T\) contains \(P\), its unique tree path between \(u,v\) is \(P\); thus \(|C_T(e)|=1+|P|\). Minimize over \(e\) and invoke Theorem 3. \(\square\)

This separates the proposed general matroid argument into two logically distinct steps. The unrestricted port intersection theorem supplies **parallelism after contracting all zero turns**, i.e. a positive \(e\) closing inside a zero component. The missing step is a compatible **basis selection** of that zero-turn component in which the mate \(e\) has a fundamental circuit of the covering-displacement length \(n\).

The latter property is stronger than ordinary matroid exchange or binary orthogonality: it compares a fundamental-circuit cardinality with the geometric displacement of the two-cover. Once that cardinality is \(n\), the cube's antipodal parity automatically forces each coordinate resource to occur once, so no further resource-independence hypothesis is needed in the cube model. For boundary tournaments, by contrast, a short port circuit need not use many original vertices, and the independent-resource path language must still be supplied separately.

#### 6. Chordless minimizers and simple moving cycles

The minimum-length one-disagreement cycle has a stronger structural property than the absence of stationary contacts.

**Theorem 8 (one-disagreement chord elimination).** Let \(H\) be a finite simple graph with a binary edge cochain \(d\). Among all simple cycles with integer turn weight
\[
w_d(C)=\sum_{e\in C}d(e)=1,
\]
choose a cycle \(C\) of minimum length. Then \(C\) is an **induced cycle of \(H\)**: there is no edge of \(H\) joining nonconsecutive vertices of \(C\). More generally, every one-disagreement simple cycle admits a sequence of strictly length-decreasing chord eliminations ending at an induced one-disagreement cycle.

*Proof.* Let \(h\) be a chord of a simple cycle \(C\) with \(w_d(C)=1\). The chord splits \(C\) into two strictly shorter simple cycles, using its two complementary arcs. Of the arcs, precisely one contains the unique positive-turn edge of \(C\). If \(d(h)=0\), choose the arc containing that edge; the resulting shorter cycle still has weight one. If \(d(h)=1\), choose the other arc, whose original edges all have cost zero; the chord contributes its unique positive edge. In both cases there is a shorter one-disagreement cycle. Iteration terminates and establishes the result. \(\square\)

**Corollary 9 (simple folded-cube core).** For the cube \(n\ge4\), a minimum-length monodromy-one cycle with one changed turn projects from \(H_n=L(G_n)\) to a **simple odd-monodromy cycle in \(G_n=Q_n/\tau\)**, whose lift is a self-avoiding path between antipodal vertices of \(Q_n\), with no two interior vertices related by the antipodal map. Its length is \(n+2q_d\).

*Proof.* Theorem 8 makes the turn cycle an induced cycle of \(L(G_n)\), of length at least \(n\ge4\). Any induced line-graph cycle of length at least four arises from a simple cycle of the base graph: consecutive edge-state vertices must meet at different endpoints of each base edge, else the preceding and following states are adjacent and create a chord. Moreover the contact vertices cannot repeat, since three or more selected edge states would then lie in the same base-vertex star clique, producing a chord of the induced cycle. Thus the moving walk is a simple base-graph cycle. Its monodromy is one, so its lifted path begins and ends at antipodal vertices, and no two distinct interior vertices project to the same base vertex. The direction-parity argument of Theorem 3 gives its length \(n+2q_d\). \(\square\)

**Example (why chordlessness alone does not close NORI1).** In every dimension \(n\ge4\), the following cube-vertex sequence, written as subsets of \([n]\), is a path from \(\varnothing\) to \([n]\):
\[
\varnothing,\ \{1\},\ \{1,2\},\ \{2\},\ \{2,3\},\
\{1,2,3\},\ \{1,2,3,4\},\ldots,[n].
\tag{14}
\]
Its direction sequence is \(1,2,1,3,1,4,5,\ldots,n\), of length \(n+2\). Its intermediate vertices have pairwise distinct antipodal orbits, so its projection is a simple monodromy-one cycle of length \(n+2\) in \(G_n\), corresponding to an induced turn cycle in \(H_n\). This is a geometric example, not an alleged NORI1 counterexample: prescribing one changed turn on this longer cycle does not rule out a monochromatic geodesic elsewhere.

Thus Theorem 8 removes all chord and stationary-contact defects from the shortest one-positive cocircuit, leaving **simple odd-voltage cycles of excess \(2q_d\)** as the sole geometric obstruction. A successful closure argument must exploit the cube's coordinate-square exchange structure to eliminate that positive excess; graph-theoretic chord shortening by itself is insufficient.

#### 7. Antipodal component-contact graph and port-parallel bundles

Let \(\widetilde G\to G\) be a connected regular two-sheeted graph cover with deck transformation \(\tau\), and let \(c:E(\widetilde G)\to\mathbb F_2\) be deck-odd, so \(c(\tau e)=1+c(e)\). Let \(R\) be the subgraph of color-zero covering edges, omitting isolated vertices; write \(R_1,\ldots,R_s\) for its edge-containing connected components. For a lifted vertex \(x\) incident with a red edge define \(\rho(x)=i\) by \(x\in R_i\), and put \(a_x=\deg_R(x)\), including \(a_x=0\) when no red edge is incident.

Construct the **antipodal component-contact multigraph** \(A_c\) with vertices \(R_1,\ldots,R_s\). For each pair \(\{x,\tau x\}\) with \(a_xa_{\tau x}>0\), place \(a_xa_{\tau x}\) parallel edges between \(R_{\rho(x)}\) and \(R_{\rho(\tau x)}\), allowing loops.

**Theorem 10 (component-contact realization).** Let \(K_d\) be the zero-turn contraction of the quotient line graph \(H=L(G)\) from Theorem 1. There is a canonical multigraph isomorphism
\[
\boxed{K_d\cong A_c.}\tag{15}
\]
In particular \(K_d\) is connected and nonbipartite. The entire contribution of a lifted vertex orbit is a single parallel edge bundle of cardinality
\[
\boxed{a_xa_{\tau x}=a_x(\deg_{\widetilde G}(x)-a_x).}\tag{16}
\]

*Proof.* Lift the zero-turn graph to \(L(\widetilde G)\). Its edges join incident covering edges of the same color, so its connected components are the line graphs of the monochromatic edge components. The deck transformation exchanges colors and pairs \(R_i\) with the color-one component \(\tau R_i\); the quotient zero-turn components are therefore indexed by red components \(R_i\). A positive turn at \(x\) joins a red covering edge at \(x\) to a blue covering edge at \(x\). The latter is the deck image of a red covering edge at \(\tau x\). Its two quotient components are \(R_{\rho(x)}\) and \(R_{\rho(\tau x)}\). Every choice of one red edge at each antipodal endpoint specifies one positive-turn orbit, and no orbit is counted twice since \(x,\tau x\) are one base vertex. This gives \(a_xa_{\tau x}\) parallel edges and exhausts the positive turns. Theorem 1 gives connectedness and nonbipartiteness. Deck oddness implies \(a_{\tau x}=\deg_{\widetilde G}(x)-a_x\). \(\square\)

**Corollary 11 (large parallel bundles).** If the covering graph has minimum degree \(m\ge3\), every edge of \(K_d\) belongs to a parallel bundle containing at least \(m-1\) elements. Every nonloop edge lies in a two-edge cycle; hence \(K_d\) has no bridges.

*Proof.* Both factors in a nonempty bundle are positive integers summing to a degree at least \(m\), so their product is at least \(m-1\). Each bundle consists of edges with the same two endpoints. \(\square\)

**Corollary 12 (loop characterization and port-parallel amplification).** The graph \(K_d\) has a loop if and only if some color-zero edge component \(R_i\) contains an antipodal pair \(x,\tau x\). More precisely, an edge contributed by the vertex orbit \(\{x,\tau x\}\) is a loop if and only if \(\rho(x)=\rho(\tau x)\). Such a vertex orbit contributes at least \(m-1\) distinct loops when the minimum degree is \(m\ge3\). In the primal pointed contraction of Theorem 1, these loop columns are all identical to the port column, so the port has at least \(m-1\) parallel mates.

*Proof.* The edge corresponding to \(\{x,\tau x\}\) is a loop if and only if \(\rho(x)=\rho(\tau x)\). In the contracted incidence-plus-monodromy matrix, a graph loop has zero incidence column and bottom entry one, as does the distinguished port. Apply Corollary 11. \(\square\)

**Lemma 13 (monochromatic antipodal metric).** In the cube cover,
\[
\boxed{
\ell_1(d)=
\min_{\substack{x\in Q_n,\ \varepsilon\in\{0,1\}\\
x,\tau x\text{ joined by an }\varepsilon\text{-colored path}}}
\operatorname{dist}_{G_\varepsilon}(x,\tau x),
}\tag{17}
\]
where \(G_\varepsilon\) is the spanning subgraph of cube edges of color \(\varepsilon\), and the distance is measured inside that monochromatic subgraph.

*Proof.* Any monochromatic antipodal path gives a turn walk of zero internal cost and one positive closing turn, hence an odd-monodromy turn walk of no larger length. Splitting it into simple cycles yields a one-positive simple cycle and proves \(\ell_1(d)\) is no larger than the monochromatic distance. Conversely, Theorem 3 shortens a minimum one-positive turn cycle to a moving stationary-free cycle, which lifts to a monochromatic cube path between antipodal vertices of length \(\ell_1(d)\). \(\square\)

**Proposition 14 (uniform near-short circuits within one loop bundle).** Suppose \(x,\tau x\) belong to the same color-zero component \(R_i\), and put \(L_x=\operatorname{dist}_{R_i}(x,\tau x)\). Every one of the \(a_xa_{\tau x}\) loop elements from the orbit \(\{x,\tau x\}\) belongs to a port cocircuit \(Y\) such that
\[
\boxed{|Y|\le L_x+3,\qquad |X_d\cap Y|=2.}\tag{18}
\]
These cocircuits are distinct for distinct loop edges. Consequently, for a cube coloring whose minimum monochromatic antipodal distance is \(\ell_1(d)=n+2q_d\), at least \(n-1\) distinct port cocircuits have intersection two and size at most \(n+2q_d+3\).

*Proof.* Let \(P\) be a shortest red \(x\)-to-\(\tau x\) path of length \(L_x\). Its edge states form a zero-turn path of length \(L_x-1\). Replace its initial edge by any other red edge incident at \(x\), and its terminal edge by any other red edge incident at \(\tau x\); these replacements add at most one zero turn each. Thus every pair of red incident edges at \(x,\tau x\) is joined by a zero-turn walk of length at most \(L_x+1\) in the quotient state graph. Close it by its associated positive-turn element (one of the loop bundle), and shorten the zero walk to a simple zero path. The result is a simple odd-monodromy cycle of length at most \(L_x+2\) with one positive turn. Adding the port gives (18); its positive-turn element identifies it uniquely. Take an antipodal pair attaining Lemma 13 and apply the cube degree \(m=n\) to obtain the multiplicity assertion. \(\square\)

The contact-graph structure is significantly more restrictive than an arbitrary nonbipartite multigraph: each edge belongs to a large parallel bundle, and a self-contact component yields many port-parallel elements with uniformly bounded circuit-length spread. Nevertheless, a loop is a certificate of monochromatic antipodal **connectivity**, not necessarily of a geodesic. The unresolved geometric condition is \(L_x=n\) for some self-contact, which would force zero directional excess and close NORI1.

#### 8. Eulerian conservation in the antipodal contact minor

Regularity of the covering graph imposes a second global constraint on \(K_d\), beyond the large parallel bundles in Corollary 11.

**Theorem 15 (Eulerian contact conservation).** Suppose \(\widetilde G\to G\) is a connected regular two-cover, \(\widetilde G\) is \(m\)-regular, and \(c(\tau e)=1-c(e)\). Then the contracted antipodal component-contact multigraph \(K_d\) of Theorem 10 is **Eulerian**:
\[
\boxed{\deg_{K_d}(R_i)\equiv0\pmod2\qquad
\text{for every color-zero edge component }R_i.}
\tag{19}
\]
More precisely,
\[
\boxed{
\deg_{K_d}(R_i)
=\sum_{x\in V(R_i)}a_x(m-a_x),\qquad
a_x=\deg_{R_i}(x).
}
\tag{20}
\]
Loops contribute two to the graph degree.

If \(m\) is odd, every *individual local parallel bundle* has even cardinality. If \(m\) is even, a local bundle has odd cardinality precisely when \(a_x\) is odd; the collection of odd-cardinality bundles, considered modulo two on the contact graph, forms an Eulerian subgraph.

*Proof.* A base vertex orbit \(\{x,\tau x\}\) contributes \(a_xa_{\tau x}\) edges between the red components containing \(x\) and \(\tau x\), by Theorem 10. Its contribution to the degree of a red component is \(a_xa_{\tau x}\) for each endpoint \(x\) of that orbit lying in the component; if both antipodal endpoints belong to it, the bundle is a loop and the contribution is counted twice. Summing the contributions over all vertices of \(R_i\) gives (20), since deck oddness and \(m\)-regularity yield \(a_{\tau x}=m-a_x\).

Working modulo two, \(a_x(m-a_x)\equiv(m-1)a_x\), because \(a_x^2\equiv a_x\pmod2\). The degree-sum identity inside \(R_i\) gives \(\sum_{x\in V(R_i)}a_x=2|E(R_i)|\equiv0\pmod2\). Therefore (20) is even, proving (19). For odd \(m\), the positive integers \(a_x\) and \(m-a_x\) have opposite parity and their product is even. For even \(m\), the product has the parity of \(a_x\); the already-proved even-degree condition says the odd-bundle edge set has even degree at every contact-graph vertex. \(\square\)

**Corollary 16 (common Eulerian-port-minor axiom).** The cube cover \(Q_n\to Q_n/\tau\) is \(n\)-regular. The ordered-pair cover used for ordinary boundary 3-tournaments, \(S(K_n)\to L(K_n)\), is \(2(n-2)\)-regular. Thus **both** canonical Article XI signed turn models yield Eulerian zero-turn contractions for every reversal-odd coloring. The cube additionally has even local parallel multiplicities in odd dimensions; the boundary model always lies in the even-degree branch.

In matroid language, the entire positive-turn edge multiset of \(K_d\) is a cycle of its graphic matroid \(M(K_d)\). The parity reduction of local parallel bundles is itself an Eulerian cycle. Consequently a proposed abstract common class may require an Eulerian contact minor, quantitative parallel bundles, and a distinguished port-parallel loop whose lifted fundamental circuit has covering-displacement length. The first two properties are theorems for all regular two-covers; the last is the unresolved NORI1 selector.

**Limitation.** A connected nonbipartite Eulerian multigraph with all nonloop edges in large parallel classes need not have any loops: an odd cycle with each edge replaced by two parallel edges is a counterexample to that implication. Therefore regularity and Eulerian parity alone cannot replace the cube-specific antipodal connectivity theorem, much less guarantee a length-\(n\) loop lift. These restrictions nevertheless exclude most arbitrary pointed binary matroids and supply a useful common structural hypothesis for future matroid generalizations.

#### 9. Global contact-edge parity as a covering-cohomology evaluation

The Eulerian conservation law has a global counterpart. Let \(\beta\in H^1(G;\mathbb F_2)\) denote the monodromy class of a connected regular two-cover \(\widetilde G\to G\), where \(G\) is \(m\)-regular. The number of nonzero-turn edges is
\[
|E(K_d)|=\sum_{v\in V(G)}a_v(m-a_v),
\tag{21}
\]
with \(a_v\) the number of red covering edges incident with either selected lift of \(v\).

**Theorem 17 (covering-cohomology edge-parity identity).** If \(m\) is odd, then \(|E(K_d)|\) is even for every deck-odd coloring. If \(m\) is even, the all-edge set \(E(G)\) is a binary cycle of \(G\), and
\[
\boxed{
|E(K_d)|\equiv
\left\langle\beta,\ E(G)\right\rangle
\pmod2.
}
\tag{22}
\]
Thus for an even-regular quotient, the parity of the total changed-turn set depends only on the covering, **not** on the deck-odd coloring.

*Proof.* Fix one reference lift \(s(v)\) of every base vertex, and represent the covering by a binary edge-voltage cochain \(\alpha\): it is one on a base edge \(uv\) precisely when its lift from \(s(u)\) meets \(\tau s(v)\). Let \(a_v\) count red edges incident with \(s(v)\). Modulo two, \(a_v(m-a_v)\equiv(m-1)a_v\).

For each base edge \(uv\), the deck-odd coloring chooses one of its two covering-edge lifts to be red. If \(\alpha(uv)=0\), this chosen red lift is incident with either both reference endpoints \(s(u),s(v)\) or neither, and contributes zero modulo two to \(\sum_v a_v\). If \(\alpha(uv)=1\), it is incident with precisely one reference endpoint and contributes one, independently of which lift is red. Summing over all base edges gives
\[
\sum_{v\in V(G)}a_v\equiv\sum_{e\in E(G)}\alpha(e)\pmod2.
\]
If \(m\) is odd, the coefficient \(m-1\) vanishes modulo two. If \(m\) is even, the all-edge set is Eulerian; the right-hand sum is the well-defined pairing of covering cohomology with the all-edge cycle, proving (22). \(\square\)

**Corollary 18 (even contact-edge count for both canonical models).** For every antipodally odd \(n\)-cube edge coloring with \(n\ge3\), and for every ordinary reversal-odd boundary 3-tournament on \(n\ge4\) vertices,
\[
\boxed{|E(K_d)|\equiv0\pmod2.}
\tag{23}
\]

*Proof.* If the cube dimension \(n\) is odd, Theorem 17 applies immediately. If \(n\ge4\) is even, choose the sheet of the folded-cube covering whose first coordinate is zero. The voltage is one precisely on quotient edges of direction one; their number is \(2^{n-2}\), which is even. Thus the cohomology pairing in (22) vanishes.

For boundary tournaments the ordered-pair cover \(S(K_n)\to L(K_n)\) has degree \(m=2(n-2)\), and its covering class is the canonical contact-curvature class \(\kappa_{K_n}\), established in the monodromy-tower Subsection. Orient \(K_n\) transitively with vertices \(0,1,\ldots,n-1\). At vertex \(v\) there are \(v\) incoming and \(n-1-v\) outgoing edges, and curvature one occurs on pairs with the same incidence sense. Summing the curvature over all edges of \(L(K_n)\) therefore gives
\[
\sum_{v=0}^{n-1}\left[
\binom v2+\binom{n-1-v}2
\right]
=2\binom n3\equiv0\pmod2.
\]
Apply Theorem 17. \(\square\)

Theorems 15 and 17 identify a pair of common matroidal constraints: the entire positive-turn edge multiset is an Eulerian cycle in the graphic matroid of the contact graph, and it has even cardinality. Equivalently, its evaluation under the constant-one edge functional is zero. These conditions survive arbitrary deck-odd recoloring in both canonical systems. They do not force a length-\(n\) lift of a port-parallel loop; that additional metric selection is the remaining obstruction to NORI1.

#### 10. Endpoint-star tree certificate and rank amplification

The preceding results measure a hypothetical defect \(q_d>0\) by the length of a monochromatic antipodal path. The regular cubical endpoint stars force that metric defect to appear as **graphic rank** in the corresponding monochromatic component.

**Theorem 19 (endpoint-star independent-tree bound).** Let \(c\) be any antipodally odd two-coloring of \(E(Q_n)\), \(n\ge3\), and suppose \(x\) and \(x^*\) belong to one monochromatic component \(R\). Let \(P=(v_0=x,v_1,\ldots,v_L=x^*)\) be a *shortest* monochromatic path between these two endpoints, where \(L\ge n\). Then the union of \(P\) with **all monochromatic edges incident to either endpoint** is a tree having
\[
\boxed{L+n-2\text{ edges and }L+n-1\text{ vertices}.}
\tag{24}
\]
In particular, writing \(M(R)\) for the graphic cycle matroid of the monochromatic component,
\[
\boxed{\operatorname{rank}M(R)=|V(R)|-1\ge L+n-2.}
\tag{25}
\]

*Proof.* If a monochromatic edge joined \(v_0\) to a later path vertex \(v_j\) with \(j\ge2\), replacing the initial \(j\) path edges by this edge would shorten the monochromatic path from \(x\) to \(x^*\), contradicting minimality. The same argument at \(v_L\) shows that its only monochromatic neighbor on \(P\) is \(v_{L-1}\). By deck oddness, the monochromatic endpoint degrees satisfy
\[
\deg_c(x)+\deg_c(x^*)=n,
\]
because each coordinate-direction edge at \(x\) is paired with the oppositely colored edge at \(x^*\). The \(n\) endpoint-neighbor vertices are all distinct for \(n\ge3\): the neighbors of \(x\) and \(x^*\) belong to Hamming layers one and \(n-1\), respectively. Among those \(n\) monochromatic endpoint-neighbor vertices, only \(v_1\) and \(v_{L-1}\) belong to \(P\). Every other endpoint red edge therefore attaches a new leaf to \(P\), and there are \(n-2\) such edges. The resulting union is a tree with the asserted sizes. It is a graphic independent set in \(M(R)\), so the rank inequality follows. \(\square\)

**Corollary 20 (rank cost of cubical geodesic defect).** Let \(\ell_1(c)=n+2q_d\) be the shortest monochromatic antipodal-path length from Theorem 3, and let \(R\) be a monochromatic component containing a pair achieving this length. Then
\[
\boxed{
|V(R)|\ge 2n+2q_d-1,\qquad
\operatorname{rank}M(R)\ge2n+2q_d-2.
}
\tag{26}
\]
Consequently, **if every monochromatic component containing an antipodal pair has fewer than \(2n+1\) vertices, then NORI1 holds for that coloring.** Conversely, a hypothetical counterexample to NORI1 must have every such component of order at least \(2n+1\).

*Proof.* Substitute \(L=n+2q_d\) into Theorem 19; if \(q_d>0\), integrality makes \(q_d\ge1\), giving the threshold. For another self-contact component the same argument uses its own shortest antipodal distance, which is no smaller than \(\ell_1(c)\). \(\square\)

Theorem 19 is a useful graphic-matroid rank constraint on any port-parallel bundle: a self-contact loop with shortest lift of length \(n+2q\) can occur only in a monochromatic component carrying an independent tree of rank at least \(2n+2q-2\). The proof uses the combination of shortest-path chordlessness and complementary antipodal endpoint stars, not binary parity alone.

**Scope.** The rank bound by itself does not force \(q=0\). A partial monochromatic subgraph can contain a length-\(n+2\) antipodal path, both complementary endpoint stars, and no shorter path between its chosen endpoints, with \(2n+1\) vertices. Extending such a partial subgraph to a full deck-odd coloring may create additional monochromatic antipodal geodesics elsewhere. Thus Theorem 19 supplies a rigorous rank barrier for a hypothetical counterexample but not its exclusion.

Let M be a finite binary matroid with distinguished port p, and let X be a binary cycle containing p. Every binary cocycle Y has even intersection with X by binary orthogonality. Define q_X(Y) to be half the intersection cardinality, reduced modulo two.

**Theorem 1 (quadratic intersection refinement).** The function q_X on the binary cocycle space W of M is quadratic. Its polar form is B_X(Y,Z)=|X intersect Y intersect Z| modulo two. This is an alternating bilinear form. If K is the port-free cocycle subspace and its polar restriction has rank 2r, then among all port-containing cocycles the fraction with intersection congruent to two modulo four differs from one half by at most 2^(-r-1). In particular, a positive polar rank forces at least one quarter of port-containing cocycles to have intersection congruent to two modulo four.

*Proof.* The identity |X intersect (Y symmetric-difference Z)|=|X intersect Y|+|X intersect Z|-2|X intersect Y intersect Z| establishes the polarization. Orthogonality makes its diagonal zero. The port-containing cocycles form an affine translate Y0+K. Their quadratic sign sum S=sum_{Z in K}(-1)^{q_X(Y0+Z)} obeys S^2=|K| times the character sum of the quadratic form on the radical of B_X restricted to K. That character sum is either zero or the cardinality of the radical. If the rank is 2r, its radical has codimension 2r, whence |S|<=|K|/2^r. Translating the sign sum into proportions proves the assertion. QED.

**Theorem 2 (local star-cut rank).** Let \(K_m\) be a complete graph with a binary coloring of its vertices, with \(a\) vertices of one color and \(b=m-a\) of the other. Put \(d(e)=1\) on edges joining different colors, and zero otherwise. On its binary graph cycle space \(Z(K_m)\), define
\[
B_d(U,V)=|U\cap V\cap\operatorname{supp}(d)|\pmod2.
\]
If \(a,b>0\), then
\[
\boxed{\operatorname{rank}B_d
=2\left\lfloor\frac{ab-1}{2}\right\rfloor.}\tag{4}
\]
If \(a=0\) or \(b=0\), the rank is zero.

*Proof.* Denote the two color classes by \(A,B\), so the changed-edge set is the cut \(\delta(A)\). A cycle \(U\) belongs to the radical of \(B_d\) precisely when its restriction \(U\cap\delta(A)\) is orthogonal to the entire cycle space of \(K_m\); thus this restriction is a cut of \(K_m\). Any cut supported wholly on the cross edges between \(A\) and \(B\) is either zero or all of \(\delta(A)\), since a vertex-partition cut containing no edge within either complete color class must be constant on each class.

If \(U\cap\delta(A)=0\), then \(U\) is a sum of cycles within \(K_a\) and \(K_b\), giving a radical subspace of dimension \(\binom{a-1}{2}+\binom{b-1}{2}\). A cycle \(U\) with \(U\cap\delta(A)=\delta(A)\) exists if and only if at least one of \(a,b\) is even: when both are odd, parity at each color class prevents completing the cut to an Eulerian set, while if either is even the odd-degree vertices of each color class occur in even numbers and can be paired by internal edges. Thus this second possibility contributes one additional radical dimension when \(ab\) is even.

Subtracting the radical dimension from
\[
\dim Z(K_m)=\binom{m-1}{2}
\]
gives rank \(ab-1\) when \(ab\) is odd and \(ab-2\) when \(ab\) is even, which is (4). \(\square\)

**Theorem 3 (universal modular balance in signed line-graph covers).** Let \(\widetilde G\to G\) be a connected regular two-sheeted graph covering with deck involution, where \(G\) is finite and simple with minimum degree \(m\ge4\). Let \(D\) be its associated pointed binary line-graph lift matroid and \(p\) its distinguished port. Fix any deck-odd edge coloring of \(\widetilde G\), with corresponding port cycle \(X_d\).

For each vertex \(v\in V(G)\), let the incident covering-edge states at either lift of \(v\) split into color classes of sizes \(a_v,b_v\) with \(a_v+b_v=\deg_G(v)\). Define
\[
R(d)=\sum_{\substack{v\in V(G)\\a_vb_v>0}}
2\left\lfloor\frac{a_vb_v-1}{2}\right\rfloor.
\]
Then the polar rank of \(q_{X_d}\) on the port-free binary cocycle space is at least \(R(d)\). In particular,
\[
\boxed{
\frac{|\{Y\in Z^*(D):p\in Y,\ |X_d\cap Y|\equiv2\pmod4\}|}
{|\{Y\in Z^*(D):p\in Y\}|}
\ge \frac12-2^{-R(d)/2-1}.}
\tag{5}
\]
Furthermore \(R(d)\ge2\lfloor(m-2)/2\rfloor\), so the right-hand side is at least
\[
\boxed{\frac12-2^{-\lfloor(m-2)/2\rfloor-1}.}\tag{6}
\]

*Proof.* The turn graph \(H=L(G)\) has one complete star clique at every base vertex, and these cliques have disjoint turn-edge sets. The cycle spaces of these star cliques are subspaces of the port-free cocycle space of \(D\): their turn cycles have zero covering monodromy. The local turn cochain \(d\) is the cut between the two classes of incident covering-edge colors. Theorem 2 therefore gives rank \(2\lfloor(a_vb_v-1)/2\rfloor\) on the corresponding local subspace. Disjoint supports make these subspaces mutually orthogonal for the polar form, giving total rank at least \(R(d)\). Apply Theorem 1 to obtain (5).

If no vertex star had both colors, all incident edges at every covering vertex would have a common color. Since the covering graph is connected, this would force every edge of the cover to have one color, contradicting deck oddness. Thus at least one base vertex has \(a_vb_v>0\). There \(a_vb_v\ge\deg_G(v)-1\ge m-1\); monotonicity of the local rank formula gives \(R(d)\ge2\lfloor(m-2)/2\rfloor\). This proves (6). \(\square\)

For the antipodal \(n\)-cube, \(m=n\) and the bound is \(1/2-2^{-\lfloor(n-2)/2\rfloor-1}\) for every \(n\ge4\). For the full-turn ordinary boundary-tournament double cover, \(m=2(n-2)\), and the bound is \(1/2-2^{-(n-2)}\) for \(n\ge4\).

These are quantitative statements about all port-containing cocycles. Converting them into intersection two with a shortest **port cocircuit** requires an additional length- and simplicity-preserving selection theorem; the modular balance alone does not close NORI1 or the boundary-tournament conjecture.

**Corollary 4 (four-cocycle modular switch).** Suppose a changed turn e belongs to a base star clique of size at least four. Choose two star triangles T1,T2 sharing only e. For any binary cocycle Y containing the distinguished port, the four port-containing cocycles Y, Y triangle T1, Y triangle T2 and Y triangle T1 triangle T2 include both an intersection congruent to two modulo four and an intersection congruent to zero modulo four. Every one differs from Y on at most four turn elements.

*Proof.* Each local triangle has zero covering monodromy and avoids the port, while the quadratic polar pairing of T1,T2 is the color-change indicator d(e)=1. Hence the quadratic intersection form cannot be constant on the four-element affine plane spanned by these triangles. Their symmetric difference has four turn edges. QED.

**Cocircuit extraction caution.** When Y is a geodesic cocircuit and e a changed turn, its two one-triangle extensions are simple stationary-contact cocircuits with unchanged cost, while the double-triangle extension has the opposite quadratic residue but forms a turn subgraph with local degree four at both endpoints of e. It need not be one simple cocircuit. Thus modular freedom at the cocycle level does not imply the shortest simple witness demanded by NORI1.

**Theorem 5 (component quotient cycle-space compression).** If H0 is the subgraph of zero-disagreement turns and J is obtained by contracting its components, restriction from Z(H) to Z(J) is surjective with kernel Z(H0). On the port-free cocycle quotient, the half-intersection quadratic form becomes q(t)=|t|/2 modulo two on the even-cardinality graph cycles t of J, with polar B(t,u)=|t intersect u| modulo two.

*Proof.* Any Eulerian set of changed edges of the quotient J has an even number of incidences at each contracted zero-turn component. Pair the incident endpoints inside that connected component and join each pair with zero-turn paths. Their mod-two sum together with the changed edges is an Eulerian set upstairs, proving the restriction map is surjective. Its kernel contains precisely those Eulerian sets using zero-turn edges alone. Covering monodromy is the parity of the changed edges because the coloring-turn cochain represents the covering class. Therefore the port-free binary cocycle sector projects onto the even-cardinality cycle subspace of J. The definitions of quadratic half-intersection and its polar form depend only on the changed-edge coordinates, proving the identities. QED.

**Corollary 6 (quotient cycle-rank bound).** Let R(d) be the sum of local star-cut polar ranks from Theorem 3. The even-cardinality binary cycle subspace of J has dimension at least R(d). Since J admits a cycle with odd cardinality, dim Z(J)>=R(d)+1. Writing r0 for the number of zero-turn components and D for the changed-turn set yields |D|-r0>=R(d). This constraint does not ensure a shortest port cocircuit with small intersection.

Let \(W\subseteq\mathbb F_2^E\) be any binary linear code containing a vector of odd Hamming weight, with standard overlap pairing
\[
\langle x,y\rangle=|x\cap y|\pmod2.
\]
Put
\[
\beta=\dim W,\quad R=W\cap W^\perp,\quad b=\dim R,\quad
K=\{x\in W:|x|\equiv0\pmod2\}.
\]
Since \(W\) has an odd-weight vector, \(K\) is a hyperplane in \(W\); on \(K\) the overlap pairing is alternating.

**Theorem 1 (bicycle-rank formula for binary codes).** The rank of the alternating pairing restricted to \(K\) is
\[
\boxed{\operatorname{rank}\bigl(\langle\cdot,\cdot\rangle|_K\bigr)
=2\left\lfloor\frac{\beta-b-1}{2}\right\rfloor.}\tag{1}
\]
In particular, no further invariant of the binary code is needed to determine this rank.

*Proof.* Every \(r\in R\) has even weight, since \(\langle r,r\rangle=0\), so \(R\subseteq K\). Pass to \(\overline W=W/R\), whose induced symmetric bilinear pairing is nondegenerate and whose dimension is \(d=\beta-b\). Its diagonal map
\[
\ell(x)=\langle x,x\rangle=|x|\pmod2
\]
is a nonzero linear functional, and \(\overline K=K/R=\ker\ell\) has dimension \(d-1\).

By nondegeneracy there is a unique characteristic vector \(h\in\overline W\) satisfying \(\langle h,x\rangle=\ell(x)\) for every \(x\). A symmetric bilinear form over \(\mathbb F_2\) decomposes orthogonally into one-dimensional odd lines and hyperbolic alternating planes. In such a decomposition, \(h\) is the sum of the unit generators of the odd lines. Therefore
\[
\langle h,h\rangle=\dim\overline W=d\pmod2.
\]
The orthogonal complement of \(\overline K\) in \(\overline W\) is \(\langle h\rangle\). Hence the radical of the restriction to \(\overline K\) is zero if \(d\) is odd, and is \(\langle h\rangle\) of dimension one if \(d\) is even. Its rank is consequently \(d-1\) when \(d\) is odd, or \(d-2\) when \(d\) is even; both equal \(2\lfloor(d-1)/2\rfloor\). Since \(R\) is the radical of the pairing on \(W\), restricting from \(K\) to \(K/R\) does not change rank. Substituting \(d=\beta-b\) proves (1). \(\square\)

The dimension \(b\) is the **bicycle dimension** of the code: it measures the overlap of its linear subspace with its orthogonal complement. Theorem 1 applies to arbitrary binary matroid cycle spaces and not merely to graph-cover representations.

#### Application to the monochromatic-component quotient

Let \(H\) be the turn graph of a connected two-sheeted graph cover, and let \(d\) be an admissible deck-odd turn signature. As in the preceding Subsection, contract the zero-turn connected components of \(H\) to form the connected multigraph \(J=J_d\), whose edges are precisely the changed turns. Because its edge-count parity measures covering monodromy and the latter is nonzero, the graph \(J\) has an odd cycle. Put
\[
\beta(J)=|E(J)|-|V(J)|+1,\qquad
b(J)=\dim\bigl(Z(J)\cap Z(J)^\perp\bigr),
\]
where the orthogonal complement is the cut space of \(J\). Let \(r_d\) be half the polar rank of the quadratic half-intersection form on port-free cocycles of the pointed lift.

**Theorem 2 (Tutte–bicycle formula for port intersection).** With this notation,
\[
\boxed{
2r_d=2\left\lfloor\frac{\beta(J)-b(J)-1}{2}\right\rfloor.}\tag{2}
\]
Equivalently, the port-cocycle quadratic rank is determined by the graph cycle rank and the bicycle dimension of \(J\). By the Rosenstiehl–Read evaluation of the Tutte polynomial,
\[
\boxed{|T_J(-1,-1)|=2^{b(J)},}\tag{3}
\]
and therefore one can recover the polar rank from \(\beta(J)\) and \(T_J(-1,-1)\).

*Proof.* The preceding monochromatic-component quotient theorem identifies the port-free cocycle space, modulo cycles of zero-turn edges, with the even-cardinality subspace \(K\) of \(Z(J)\). Its polar form is precisely the standard binary edge-overlap pairing on \(K\), and the quotient kernel has zero polar pairing against the entire port-free space. Consequently the two polar ranks agree. Apply Theorem 1 to \(W=Z(J)\), which contains odd-weight vectors, with radical dimension \(b(J)\). Equation (3) is the classical Rosenstiehl–Read identity. \(\square\)

**Corollary 3 (three-value modular distribution).** Set
\[
r=\left\lfloor\frac{\beta(J)-b(J)-1}{2}\right\rfloor.
\]
For a uniformly sampled port-containing binary cocycle \(Y\), the probability that
\(|X_d\cap Y|\equiv2\pmod4\) belongs to the three-element set
\[
\boxed{
\left\{\frac12,\quad
\frac12-2^{-r-1},\quad
\frac12+2^{-r-1}\right\}.}\tag{4}
\]
It is not merely bounded by this interval.

*Proof.* In the affine coset of port-containing cocycles, the half-intersection function is quadratic with polar rank \(2r\). Its sign sum is zero when its affine-linear restriction to the radical is nontrivial; otherwise it has absolute value \(2^{-r}\) times the size of the affine coset. This is the standard quadratic Gauss-sum calculation, also proved by squaring the sign sum in the previous Subsection. Dividing by the coset size yields (4). \(\square\)

For a connected graph, the bicycle dimension can also be determined by the nullity of the binary graph Laplacian: \(b(J)=\dim\ker L_J-1\). Consequently the complete modular-distribution bound is computable by binary Gaussian elimination on the monochromatic-component quotient, without enumerating cocircuits or colorings.

#### Intrinsic pointed-matroid restriction theorem

Let \(M\) be a finite binary matroid, let \(p\) be a nonloop element, and let \(X\in Z(M)\) be a binary cycle containing \(p\). Put \(S=X\setminus\{p\}\) and let
\[
N=M|S
\]
be the restriction minor of \(M\) to \(S\). Define the binary bicycle dimension of \(N\) by
\[
b(N)=\dim\bigl(Z(N)\cap Z^*(N)\bigr),
\]
and write \(r(N)\) for the rank of \(N\).

**Theorem 4 (universal pointed intersection-rank formula).** On the port-free cocycle space
\[
K_p=\{Y\in Z^*(M):p\notin Y\},
\]
let
\[
B_X(Y,Z)=|X\cap Y\cap Z|\pmod2.
\]
Then
\[
\boxed{
\operatorname{rank}(B_X|_{K_p})
=2\left\lfloor\frac{r(N)-b(N)-1}{2}\right\rfloor.
}\tag{5}
\]
By the bicycle-space evaluation (Rosenstiehl–Read for graphs, extended to binary matroids by Jaeger, European J. Combin. 10 (1989), 247–255),
\[
\boxed{|T_N(-1,-1)|=2^{b(N)},}\tag{6}
\]
so the polar rank is determined solely by the rank and Tutte polynomial of the restriction minor \(N\). In particular, this quadratic invariant does not require a graph, a line-graph cover, a distinguished cocircuit length, or an admissible resource-path language.

*Proof.* Represent \(M\) over \(\mathbb F_2\) by a matrix \(A\). The binary cocycle space is the row space of \(A\), and coordinate restriction to \(S\) maps it surjectively onto the row space of \(A|S\), which is precisely \(Z^*(N)\). Denote this surjection by \(\rho\).

Because \(X\) is a binary cycle, cycle–cocycle orthogonality gives
\[
\mathbf1_Y(p)=|Y\cap S|\pmod2
\quad\text{for all }Y\in Z^*(M).
\tag{7}
\]
Thus \(\rho(K_p)\) equals the even-cardinality subspace
\[
K=\{z\in Z^*(N):|z|\equiv0\pmod2\}.
\]
Since \(p\) is a nonloop, some cocycle contains \(p\); by (7), \(Z^*(N)\) contains an odd-weight vector, and \(K\) is a hyperplane. The map \(\rho|_{K_p}\) is surjective onto \(K\), and its kernel has zero overlap pairing against every cocycle because all of its coordinates on \(S\) vanish. Therefore the polar rank on \(K_p\) equals the rank of the standard binary overlap form restricted to \(K\).

The full code \(W=Z^*(N)\) has dimension \(\beta=r(N)\), and its orthogonal complement is \(Z(N)\). Its radical hence has dimension \(b(N)\). Apply Theorem 1 to \(W\), giving precisely (5). The identity (6) is the classical bicycle-space evaluation of the Tutte polynomial, which holds for binary matroids. \(\square\)

**Corollary 5 (universal modular spectrum from a restriction minor).** Let
\[
r=\left\lfloor\frac{r(N)-b(N)-1}{2}\right\rfloor.
\]
Among all binary cocycles of \(M\) containing \(p\), the proportion meeting \(X\) in cardinality congruent to two modulo four belongs to
\[
\boxed{\left\{\frac12,\ \frac12-2^{-r-1},\
\frac12+2^{-r-1}\right\}.}\tag{8}
\]

*Proof.* The half-intersection quadratic function on the affine port-containing cocycles factors through the odd-weight coset of \(Z^*(N)\), by (7). Its polarization has rank \(2r\) by Theorem 4; the quadratic Gauss-sum dichotomy from Corollary 3 gives the stated three-value spectrum. \(\square\)

The theorem is a purely pointed-binary-matroid statement and is thus directly suitable for testing candidate intrinsic generalization classes. It also identifies a sharp limitation: modular intersection balance of *all* port-containing cocycles is governed by a restriction minor and need not impose any condition on minimum-size cocircuits or on the resource simplicity of their graph-cover witnesses.

**Corollary 6 (bicycle-corrected cycle-rank inequality).** In any signed line-graph cover with admissible turn cochain \(d\), put \(S=\operatorname{supp}(d)\), let \(r_0\) be the number of zero-turn connected components, and let \(J_d\) be the resulting connected multigraph on those components. If \(R(d)\) denotes the sum of the local star-cut polar ranks from the preceding Subsection, then
\[
\boxed{|S|-r_0\ge b(J_d)+R(d).}\tag{9}
\]
Thus the local quadratic mixing requires not merely global cycle rank but cycle rank *beyond the graph's bicycle space*.

*Proof.* The preceding local star theorem gives a lower bound \(R(d)\) for the polar rank of the port-free cocycle quadratic. By Theorem 2 this rank equals \(2\lfloor(\beta-b-1)/2\rfloor\), where \(\beta=|S|-r_0+1\) and \(b=b(J_d)\). Therefore
\[
R(d)\le 2\left\lfloor\frac{|S|-r_0-b}{2}\right\rfloor
\le |S|-r_0-b,
\]
which is (9). \(\square\)

**Corollary 7 (Laplace–Tutte computational interpretation).** For connected \(J_d\), its binary Laplacian satisfies
\[
b(J_d)=\dim\ker_{\mathbb F_2} L_{J_d}-1.
\]
Hence the quantity on the right side of (9) and the complete three-value modular spectrum can be computed by binary matrix rank calculations on the monochromatic-component quotient. When the number of spanning trees of \(J_d\) is odd, the bicycle dimension is zero; equivalently \(|T_{J_d}(-1,-1)|=1\).

*Proof.* A bicycle is a cut vector \(\partial^Tf\) that also lies in \(\ker\partial\); this is equivalent to \(L_{J_d}f=\partial\partial^Tf=0\). The map \(f\mapsto\partial^Tf\) has one-dimensional kernel for connected \(J_d\), yielding the displayed dimension identity. The matrix-tree theorem over \(\mathbb F_2\) identifies odd spanning-tree count with invertibility of a reduced Laplacian, which is equivalent to one-dimensional kernel of the full Laplacian and thus to \(b(J_d)=0\). \(\square\)

### Discrete Hodge stability and the asymptotically sharp two-thirds turn theorem

Let \(V_n\) denote the real functions on distinct ordered triples satisfying \(f(c,b,a)=-f(a,b,c)\). Use one representative of each reversal pair for the inner product, and write \(N=n\binom{n-1}{2}\), \(E=N(n-3)\). Recall from the preceding signed-adjacency theorem the self-adjoint operator
\[
(Af)(a,b,c)=\sum_{d\notin\{a,b,c\}}[f(b,c,d)+f(d,a,b)]
\]
with spectrum contained in \(\{-(n-2),-2,0,1,n-2\}\), for \(n\ge6\).

**Lemma 1 (minimum eigenspace).** The eigenspace at \(-(n-2)\) is
\[
\mathcal E_-=\{f_s(a,b,c)=s_{ab}-s_{bc}:s_{ab}=s_{ba},\quad
\sum_{b\ne a}s_{ab}=0\ \forall a\}. \tag{1}
\]
It has dimension \(n(n-3)/2\), and is contained in
\[
\mathcal G=\{f:f(a,b,c)=u_b(a)-u_b(c)\}, \tag{2}
\]
the direct sum of gradient spaces on the neighbor sets of the \(n\) centers.

*Proof.* For any \(f\in V_n\), set
\[
U_{ab}=\sum_{d\notin\{a,b\}}f(d,a,b),\quad
H_{ab}=\sum_{d\notin\{a,b\}}f(a,d,b),\quad
W_a=\sum_{c\ne a}U_{ca},
\quad \sigma(a,b,c)=f(a,b,c)+f(b,c,a)+f(c,a,b).
\]
Here \(H_{ba}=-H_{ab}\), \(\sigma\) is alternating, and \(\sum_{b\ne a}U_{ab}=0\). Rearrangement gives
\[
Af=f-\sigma+U_{ab}-U_{cb},\qquad
U(Af)_{ab}=W_a+H_{ab}-(n-2)U_{ba}. \tag{3}
\]
Suppose \(Af=-rf\), with \(r=n-2\). The second equation gives
\(H_{ab}=r(U_{ba}-U_{ab})-W_a\).
Antisymmetry of \(H\) forces \(W_a=-W_b\) for every \(a\ne b\), hence every \(W_a=0\).
From the first equation,
\[
(r+1)f(a,b,c)=\sigma(a,b,c)-U_{ab}+U_{cb}. \tag{4}
\]
Summing (4) over \(f(a,d,b)\), and using the zero row sums of \(U\) and
\(\sum_d\sigma(a,d,b)=-(U_{ab}-U_{ba}-H_{ab})\), yields
\((r+1)H_{ab}=H_{ab}\). Thus \(H=0\), so \(U\) is symmetric. Cyclically summing (4) then gives \((r+1)\sigma=3\sigma\). Since \(n\ge6\), \(\sigma=0\). Equation (4) becomes \(f(a,b,c)=(-U_{ab}+U_{bc})/(n-1)\), establishing (1) with \(s=-U/(n-1)\).
Conversely, the stated symmetric zero-row-sum \(s\) satisfies
\(U_{ab}=-(n-1)s_{ab}\), \(\sigma=0\), and consequently \(Af_s=-(n-2)f_s\) by (3). The \(n\) row-sum constraints on the \(\binom n2\) symmetric edge variables are independent, and \(s\mapsto f_s\) is injective, giving the dimension. \(\square\)

For an antisymmetric edge array \(z_{ac}\) on \(K_m\), write \(\operatorname{div}_a z=\sum_{c\ne a}z_{ac}\) and
\(\gamma_{acd}=z_{ac}+z_{cd}+z_{da}\).

**Lemma 2 (complete-graph Hodge identity).** Orthogonal projection onto the gradients \(z_{ac}=u_a-u_c\) satisfies
\[
(\Pi z)_{ac}=\frac{\operatorname{div}_a z-\operatorname{div}_c z}{m},\qquad
\sum_{\{a,c,d\}}\gamma_{acd}^{\,2}=m\|z-\Pi z\|^2. \tag{5}
\]
*Proof.* Expand the squares:
\(\sum_{\triangle}\gamma^2=m\sum_{\{a,c\}}z_{ac}^2-\sum_a(\operatorname{div}_a z)^2\).
The displayed projection has squared norm \(\frac1m\sum_a(\operatorname{div}_a z)^2\), proving (5). \(\square\)

**Theorem 3 (sharp asymptotic turn density with stability).**
Let \(b(a,b,c)\in\mathbb F_2\) satisfy \(b(c,b,a)=1-b(a,b,c)\). Among the \(E=n(n-1)(n-2)(n-3)/2\) legal-turn reversal orbits let \(D(b)\) be the number on which consecutive triple colors differ. At each center \(v\), interpret \(b(a,v,c)\) as a tournament orientation on the remaining \(n-1\) labels; let \(t_v\) be its number of directed cyclic triangles and \(T(b)=\sum_v t_v\). Then
\[
\boxed{\frac{D(b)}E\le
\frac23+\frac{n-2}{2(n-3)(n-1)}
-\frac{2(n-4)T(b)}{(n-1)E}.} \tag{6}
\]
In particular
\[
\boxed{\frac23\le\max_b\frac{D(b)}E
\le\frac23+\frac{n-2}{2(n-3)(n-1)},}
\qquad
\lim_{n\to\infty}\max_b\frac{D(b)}E=\frac23. \tag{7}
\]
The upper estimates apply to every induced \(m\)-label restriction with \(m\ge6\).

*Proof.* Put \(x(a,b,c)=(-1)^{b(a,b,c)}\). It is reversal-skew and \(\|x\|^2=N\). For every center \(v\), the triangle curl of the \(\{\pm1\}\)-edge array \(x(a,v,c)\) has square \(1\) on a transitive triangle and \(9\) on a cyclic triangle. Applying (5) with \(m=n-1\) separately at all centers yields
\[
\|x-\Pi_{\mathcal G}x\|^2
=\frac1{n-1}\left(n\binom{n-1}{3}+8T(b)\right)
=\frac{n(n-2)(n-3)}6+\frac{8T(b)}{n-1}. \tag{8}
\]
By Lemma 1, \(\mathcal E_-\subseteq\mathcal G\). Every eigenvalue of \(A\) other than \(-(n-2)\) is at least \(-2\). Thus
\[
\langle x,Ax\rangle\ge
-(n-2)N+(n-4)\|x-\Pi_{\mathcal G}x\|^2. \tag{9}
\]
Signed adjacency gives \(\langle x,Ax\rangle=2E-4D(b)\). Substituting (8) into (9) and simplifying proves (6) and the upper bound in (7).

For the matching lower bound, assign independent continuous real labels \(s_{uv}=s_{vu}\) to all edges of \(K_n\), and set
\[
(-1)^{b(a,b,c)}=\operatorname{sgn}(s_{ab}-s_{bc}).
\]
This is reversal-skew. For every legal quadruple \((a,b,c,d)\), the three labels \(s_{ab},s_{bc},s_{cd}\) are independent and identically distributed. The colors of the two overlapping triples differ precisely when the middle label is their minimum or maximum, an event of probability \(2/3\). Hence \(\mathbb E D(b)=2E/3\), so some edge ordering has \(D(b)\ge2E/3\). Finally every restriction retains reversal oddness and the argument applies with its own number of labels. \(\square\)

The stability term in (6) penalizes cyclic triangles in the local tournaments. The upper bound covers all reversal-odd boundary 3-tournaments, while the asymptotically extremal construction belongs to the edge-ordered subclass. The theorem is a global constraint on coloring-cycle support in the pointed binary turn matroid. Extracting a resource-simple long path still requires a cocircuit selector.

**Corollary 5 (abundance of six-resource low-intersection port cocircuits).**
Let \(n\ge6\), and consider the six-resource twisted-cycle construction in the preceding Subsection. For every injective ordered six-vertex word \(v=(v_1,\ldots,v_6)\), let \(Y_v=C_v\cup\{p\}\) be its seven-element marked port cocircuit and put
\[
w(v)=|X_b\cap Y_v|-1.
\]
The six-turn odd-monodromy construction gives \(w(v)\in\{1,3,5\}\). Then the proportion \(q_n(b)\) of injective words satisfying \(|X_b\cap Y_v|\le4\) obeys
\[
\boxed{
q_n(b)\ge
\frac14-\frac{3(n-2)}{4(n-3)(n-1)}
+\frac{3(n-4)T(b)}{(n-1)E_n}.
}\tag{16}
\]
In particular
\[
q_n(b)\ge\frac14-\frac{3(n-2)}{4(n-3)(n-1)}
=\frac14-O(n^{-1}).
\]
At \(n=6\) this recovers the established \(36/720=1/20\) uniform six-resource guarantee; as \(n\to\infty\) it gives a lower bound approaching one quarter of all ordered six-vertex words, independently of the coloring.

*Proof.* Each of the six edges of the marked turn cycle is uniformly distributed over the \(E_n\) legal-turn reversal orbits when \(v\) is uniformly distributed over injective ordered six-tuples. Hence
\[
\mathbb E_v w(v)=6D_n(b)/E_n.
\]
Writing \(q=\Pr(w\le3)\), the parity restriction \(w\in\{1,3,5\}\) gives
\[
\mathbb E_v w(v)\ge q\cdot1+(1-q)\cdot5=5-4q.
\]
Thus \(q\ge(5-6D_n(b)/E_n)/4\). Substitution of the stability bound (11) proves (16). \(\square\)

This is a global marked-cocircuit counting statement; the stronger assertion that every prescribed six-element resource set has at least one such cocircuit follows separately from the five-cycle averaging theorem.

Let \(H\) be a finite connected graph, let \(B_H\) be its binary incidence matrix, and let \(a\in\mathbb F_2^{E(H)}\) represent a nonzero graph cohomology class. Form the pointed binary matroid
\[
D(H,a)=M\!\left(\begin{array}{c|c}B_H&0\\a&1\end{array}\right)^*
\]
with port \(p\). For an admissible signature \(d=a+\delta f\), put
\[
S=\operatorname{supp}(d),
\]
and let \(J_d\) be the multigraph obtained by contracting every connected component of the spanning zero-signature subgraph \(H_0=(V(H),E(H)\setminus S)\). Its labeled edges are precisely the elements of \(S\), including possible loops. Write \(B_J\) for its binary incidence matrix and \(\mathbf1_S\) for the all-ones row on \(S\).

**Theorem 1 (canonical pointed cographic restriction minor).** There are canonical labeled binary-matroid isomorphisms
\[
\boxed{
D(H,a)|(S\cup\{p\})\cong
M\!\left(\begin{array}{c|c}B_J&0\\
\mathbf1_S&1\end{array}\right)^*,}
\tag{1}
\]
and
\[
\boxed{D(H,a)|S\cong M(J_d)^*.}\tag{2}
\]
The first restriction is a pointed parity coextension of the cographic matroid of \(J_d\). It depends only on the monochromatic-component quotient \(J_d\), not on the full turn graph or the chosen representative of the cohomology class.

*Proof.* The binary cocycle space of the dual \(D(H,a)\) is the kernel of its displayed primal representation:
\[
Z^*(D)=\left\{(z,t):B_Hz=0,\ 
t=\langle a,z\rangle\right\}.
\]
Since \(a=d+\delta f\) and every graph cycle is orthogonal to cuts, \(\langle a,z\rangle=\langle d,z\rangle=|z\cap S|\pmod2\). Thus
\[
Z^*(D)=\left\{\bigl(z,|z\cap S|\bmod2\bigr):
z\in Z(H)\right\}.\tag{3}
\]
Coordinate projection from \(Z(H)\) onto \(S\) is surjective onto \(Z(J_d)\), with kernel \(Z(H_0)\). For surjectivity, given an Eulerian set of changed edges of \(J_d\), pair its incident endpoints within each contracted zero-signature component and join each pair by zero-signature paths; the resulting mod-two union is Eulerian in \(H\). Consequently restriction of (3) to \(S\cup\{p\}\) gives
\[
\boxed{
Z^*(D|(S\cup\{p\}))
=\{(w,|w|\bmod2):w\in Z(J_d)\}.}\tag{4}
\]
The right-hand side of (4) is the kernel of the augmented matrix in (1), and hence is the binary cocycle space of its dual. A binary matroid is determined by its cocycle space, proving (1). Deleting the port coordinate from (4) gives \(Z(J_d)\), the cocycle space of the cographic matroid \(M(J_d)^*\), proving (2). \(\square\)

**Corollary 2 (port cocircuits are odd cycles of the quotient).** The cocircuits of \(D(H,a)|(S\cup\{p\})\) containing \(p\) are precisely the sets
\[
\boxed{C\cup\{p\},\quad
C\text{ a simple odd-length cycle of }J_d.}\tag{5}
\]
Loops count as odd cycles of length one. Therefore the shortest port-cocircuit size of the restriction minor is \(1+g_{\mathrm{odd}}(J_d)\).

*Proof.* An odd cycle \(C\) gives a cocycle \(C\cup\{p\}\) by (4). It is support-minimal because no nonzero Eulerian edge set lies in a proper subset of a simple graph cycle. Conversely, a cocycle containing \(p\) projects to an odd-cardinality Eulerian edge set of \(J_d\). Decompose it into edge-disjoint simple cycles. At least one constituent is odd, and the associated cocycle \(C\cup\{p\}\) lies inside the original cocycle. Support minimality therefore forces equality. \(\square\)

The theorem is valid for arbitrary binary graph-cover pointed lifts, including the folded cube and the boundary-tournament full-turn matroid. The restriction minor makes the quotient odd-cycle obstruction intrinsic to the matroid, but—because all unchanged turns have been deleted—it does not retain the length or resource-independence of a lift of an odd cycle to the original graph.

Let \(H\) be a finite connected graph with a nontrivial covering-monodromy cochain \(a\), let
\[
D=M\!\left(\begin{array}{c|c}B_H&0\\a&1\end{array}\right)^*
\]
be the corresponding pointed binary lift with port \(p\), and fix an admissible signature \(d=a+\delta f\). Let \(S=\operatorname{supp}(d)\), \(X_d=S\cup\{p\}\in Z(D)\), and \(H_0=(V(H),E(H)\setminus S)\). Define
\[
\mathscr L(d)=\left\{e=uv\in S:
u,v\text{ belong to the same connected component of }H_0\right\}.
\]
For \(e\in\mathscr L(d)\), write \(\ell_e=\operatorname{dist}_{H_0}(u,v)\), and put \(\ell_*(d)=\min_{e\in\mathscr L(d)}\ell_e\). As usual the minimum of an empty family is infinite.

**Theorem 1 (metric loop-lifting identity).** The minimum cardinality of a port cocircuit intersecting \(X_d\) in two elements is
\[
\boxed{
\min_{\substack{Y\in\mathcal C^*(D)\\
p\in Y,\ |X_d\cap Y|=2}}|Y|
=\ell_*(d)+2.}
\tag{1}
\]
In particular, a two-point-intersection port cocircuit exists if and only if the monochromatic-component quotient \(J_d\) has a loop. Its minimum size is determined by the shortest zero-disagreement path connecting the endpoints of a changed turn that becomes a loop in \(J_d\).

*Proof.* Given \(e=uv\in\mathscr L(d)\), take a shortest \(u\)-to-\(v\) path \(P\) in \(H_0\). Since \(P\) is simple and does not use \(e\), the edge set \(C=P\cup\{e\}\) is a simple cycle in \(H\), with precisely one changed turn. Its covering monodromy is
\[
\alpha(C)=\langle a,C\rangle
=\langle d,C\rangle=1.
\]
Consequently \(Y=C\cup\{p\}\) is a port cocircuit of \(D\) meeting \(X_d\) precisely in \(\{e,p\}\), and \(|Y|=\ell_e+2\).

Conversely, every cocircuit \(Y\) containing \(p\) corresponds to a simple monodromy-one cycle \(C=Y\setminus\{p\}\) of \(H\). If \(|X_d\cap Y|=2\), the cycle \(C\) contains precisely one edge \(e=uv\) from \(S\), and every other edge is in \(H_0\). Thus \(C\setminus\{e\}\) is a zero-turn path joining \(u\) to \(v\), of length at least \(\ell_e\). Therefore \(|Y|\ge\ell_*(d)+2\). Both inequalities establish (1). \(\square\)

For the cube, the existence of at least one such loop follows from the known unrestricted monochromatic antipodal-path theorem (Wu–Yang, 2026), as already recorded in Article XI. The nontrivial question is the distance of the corresponding lifted loop.

#### Cube geodesicity as a zero-turn distance equality

For \(n\ge3\), put \(H_n=L(Q_n/\tau)\) and retain the notation of Theorem 1. Write
\[
g_{p,2}(d)=\min\{|Y|:Y\in\mathcal C^*(D_n),\
p\in Y,\ |X_d\cap Y|=2\}.
\]

**Theorem 2 (even resource-excess distance theorem).** For every antipodally odd edge coloring of \(Q_n\), the minimum \(g_{p,2}(d)\) is finite and satisfies
\[
\boxed{g_{p,2}(d)=n+1+2q_*(d),\qquad
\ell_*(d)=n-1+2q_*(d)}
\tag{2}
\]
for a nonnegative integer \(q_*(d)\). Every minimum-cardinality port cocircuit with two-point intersection is represented by a stationary-free odd-monodromy turn cycle whose lifted moving walk travels each cube coordinate an odd number of times. Its repeated-direction excess is \(q_*(d)\).

In particular, the monochromatic NORI1 conjecture is equivalent to the metric condition
\[
\boxed{
\forall d\text{ admissible on }H_n,\quad
\ell_*(d)=n-1.}\tag{3}
\]
A counterexample, if one exists, must satisfy \(\ell_*(d)\ge n+1\). Equivalently, every changed turn whose endpoints lie in one zero-turn component would have zero-turn distance at least \(n+1\).

*Proof.* The unrestricted monochromatic antipodal-path theorem, together with Article XI's odd-girth duality, guarantees the existence of an odd-monodromy turn cycle of integer turn cost one. Thus Theorem 1 makes \(g_{p,2}(d)\) finite. Choose such a simple cycle \(C\) of the least possible length \(r\).

If \(C\) has a stationary contact, the balanced star-triangle shortcut removes the corresponding stationary edge-state vertex, yields a shorter simple odd-monodromy cycle, and does not increase integer turn cost. The new cost is still a positive odd integer, so it must equal one, contrary to minimality. Therefore \(C\) has no stationary contacts.

Its cyclic edge-state lift is consequently a walk of \(r\) cube edges from a vertex \(x\) to its antipode \(\tau x\). Each coordinate direction occurs an odd number of times; writing its multiplicity as \(1+2k_i\) gives
\[
r=\sum_{i=1}^n(1+2k_i)=n+2\sum_i k_i.
\]
Set \(q_*(d)=\sum_i k_i\). Since \(r=g_{p,2}(d)-1\), Theorem 1 yields (2). If \(q_*=0\), the walk changes each coordinate once and hence is an antipodal geodesic. Its cyclic turn cost is one; place the unique changed turn at the closing seam to obtain a monochromatic full geodesic. Conversely, every monochromatic full antipodal geodesic has a cyclic turn cycle of length \(n\), cost one, and produces \(g_{p,2}\le n+1\). Since the deck displacement is \(n\), no odd-monodromy turn cycle has fewer than \(n\) turns, so equality follows. This proves (3). \(\square\)

**Corollary 3 (a graph-distance sufficient condition).** Suppose a deck-odd cube coloring has at least one changed turn whose endpoints lie in a common zero-turn component of \(H_n\) of graph diameter at most \(n-1\). Then it has a monochromatic antipodal geodesic.

*Proof.* Such a turn has \(\ell_e\le n-1\); Theorem 2 forces \(\ell_*\ge n-1\), so \(\ell_*=n-1\), and (3) applies. \(\square\)

This metric reformulation isolates the full remaining obstruction as the presence of repeated coordinate directions in a shortest zero-turn lift of a changed-turn loop. The pointed cographic restriction minor records which loops exist, while the distances \(\ell_e\) require the zero-turn component geometry discarded by that minor. A universal short-port result therefore needs a hypothesis controlling these **loop-lifting distances**, rather than only its circuit and cocircuit incidence algebra.

Let A be a directed graph whose arcs carry labels in a loopless resource matroid N. Starting from a vertex v and the closure F of an independent resource set, construct a flat-graded automaton with states (v,F). For an arc from v to w labeled e outside F, advance to (w,cl(F union {e})). Every transition increases matroid rank by one. The resulting automaton paths are in bijection with coherent directed walks whose resource labels, together with the initial independent set, remain independent. The automaton is acyclic. This follows immediately from the matroid independence exchange criterion: appending e preserves independence if and only if e is outside the closure of the previously chosen elements.

**Corollary 2 (canonical specializations).** For the cube, take the bidirected Q_n and the free matroid on n coordinate directions; label each cube edge by its direction and begin with the empty flat. From root x a state is (x XOR S,S) with S a subset of directions. Rank n forces every coordinate to be used once, producing an antipodal geodesic.

For ordinary boundary 3-tournaments, take directed ordered-pair states (u,v) and transitions (u,v) to (v,w) for three distinct letters. Use the graphic matroid of K_V. Label each transition by the new resource edge {v,w}, and begin at (u,v) with the flat of {u,v}. After a forward prefix the selected graphic edges form a connected vertex path; its closure contains all edges between previously visited vertices. Thus the next resource {v,w} increases rank if and only if w is new. This automaton recognizes precisely forward vertex-injective tight paths. Reaching graphic rank h means the underlying word uses h+1 original vertices and h-1 ordered triples.

*Proof.* In the cube, free-matroid independence is nonrepetition of coordinate directions. In the boundary model, the graphic closure of a connected tree on a visited vertex set is the set of all complete-graph edges internal to that set. Rank-increasing ordered-pair transitions therefore append a fresh vertex, and the converse holds for every injective tight-path word. QED.

**Theorem 3 (antipodal Boolean reachability criterion for NORI1).** Fix an antipodally odd coloring \(c\) of \(Q_n\) and a root \(x\). Identify its free-resource automaton with the Boolean lattice \(2^{[n]}\), where the directed arc \(S\to S\cup\{i\}\) has the color of the cube edge from \(x+\mathbf1_S\) in direction \(i\). Define
\[
R_x=\{S\subseteq[n]:\text{a color-zero directed path runs from }\varnothing\text{ to }S\}.
\tag{1}
\]
Then, for every \(S\subseteq[n]\), the rooted cube has a geodesic whose edge colors are first zero and then one, with the switch at the vertex \(x+\mathbf1_S\), if and only if
\[
\boxed{S\in R_x\ \text{and}\ [n]\setminus S\in R_x.}\tag{2}
\]
Empty initial or terminal color blocks are allowed. Consequently unrestricted NORI1 is equivalent to
\[
\boxed{\exists x\in Q_n:\ R_x\text{ contains a complementary pair of subsets}.}\tag{3}
\]
A hypothetical NORI1 counterexample would have \(R_x\cap\{[n]\setminus S:S\in R_x\}=\varnothing\) for every root, and hence \(|R_x|\le2^{n-1}\) for every root.

*Proof.* Antipodal oddness makes the arc
\[
S\to S\cup\{i\}
\]
opposite in color to its complemented reverse
\[
[n]\setminus(S\cup\{i\})\to[n]\setminus S.
\]
Therefore reversing and complementing a color-zero path from \(\varnothing\) to \([n]\setminus S\) yields a color-one path from \(S\) to \([n]\). Concatenate with the zero path from \(\varnothing\) to \(S\) to obtain the specified one-switch geodesic. The converse follows by reversing and complementing the color-one suffix. A geodesic with one linear color switch has precisely one cyclic turn disagreement: its closing turn compares the terminal color with the deck complement of the initial color. Cyclically rerooting at the changed turn therefore gives a monochromatic antipodal geodesic. Conversely any monochromatic geodesic, after deck reversal if necessary, is a color-zero geodesic rooted at some \(x\), and gives the complementary pair \(\varnothing,[n]\). Finally a family of subsets avoiding complementary pairs has size at most \(2^{n-1}\), by pairing every subset with its complement. \(\square\)

**Theorem 4 (antipodal cut duality).** For a fixed rooted cube \(x\), let \(R_x\) be as in Theorem 3. The absence of a color-zero-then-color-one antipodal geodesic rooted at \(x\) is equivalent to the existence of a set \(\mathcal U_x\subseteq2^{[n]}\) satisfying all three conditions:
\[
\varnothing\in\mathcal U_x,\qquad
\mathcal U_x\cap\{\bar S:S\in\mathcal U_x\}=\varnothing,\qquad
\text{every outward Boolean-lattice arc of }\mathcal U_x\text{ has color one.}
\tag{4}
\]
Here \(\bar S=[n]\setminus S\). Accordingly, failure of unrestricted NORI1 is equivalent to the existence of such a family \(\mathcal U_x\) for every root \(x\), all arising from the same antipodally odd cube-edge coloring.

*Proof.* If no one-switch geodesic exists from \(x\), Theorem 3 shows that \(R_x\) contains no complementary pair; it contains the empty set, and any outward arc of \(R_x\) must have color one by the definition of color-zero reachability. Thus \(\mathcal U_x=R_x\) works. Conversely, if \(\mathcal U_x\) satisfies (4), no color-zero directed path from the empty set can leave \(\mathcal U_x\), because its first outward arc would have color one. Hence \(R_x\subseteq\mathcal U_x\) and is complement-free, so Theorem 3 excludes the rooted one-switch witness. Apply this for all roots, using Theorem 3's equivalence with global NORI1. \(\square\)

The families in (4) need not be order ideals: directed monochromatic reachability can omit a subset even while reaching some of its supersets by another coordinate order. This is an antipodal-cut certificate, not an ordinary monotone Boolean-lattice ideal.

**Corollary 5 (resource-flat groupoid constraints).** For every root \(x\), the reachability families also satisfy:
\[
\begin{aligned}
&S\in R_x\Longrightarrow S\in R_{x+\mathbf1_S},\\
&S\in R_x,\quad T\in R_{x+\mathbf1_S},\quad S\cap T=\varnothing
\Longrightarrow S\cup T\in R_x .
\end{aligned}
\tag{5}
\]
The first property comes from reversing a color-zero geodesic, and the second from concatenating two coordinate-disjoint color-zero geodesics. Thus the root-indexed antipodal cuts of a hypothetical counterexample cannot be chosen independently: their reachable families obey the symmetric partial-composition laws (5).

The formulation supplies a precise target for Tucker-, Sperner-, or KKM-type arguments. To prove unrestricted NORI1 it suffices to show that no deck-odd cube-edge coloring supports a compatible system of complement-free, color-one-boundary families as in (4) and (5). Theorem 4 does not establish that impossibility.

**Theorem 6 (factorial-free SAT obstruction certificate).** For \(n\ge3\), introduce one Boolean coloring variable per antipodal orbit of cube edges, and one Boolean membership variable \(r_{x,S}\) for every cube root \(x\) and coordinate subset \(S\subseteq[n]\). Let \(\gamma_{x,S,i}\) denote the color-one Boolean expression of the edge from \(x+\mathbf1_S\) in unused coordinate direction \(i\). Consider the clauses
\[
\begin{array}{ll}
r_{x,\varnothing},&\text{all }x,\\
\neg r_{x,S}\vee\gamma_{x,S,i}\vee r_{x,S\cup\{i\}},&
\text{all }x,S,i\notin S,\\
\neg r_{x,S}\vee\neg r_{x,\bar S},&
\text{all }x,\text{ one representative per complement pair }S,\bar S.
\end{array}
\tag{6}
\]
This formula is satisfiable if and only if an antipodally odd coloring of \(Q_n\) exists with no monochromatic antipodal geodesic. Its size is
\[
\boxed{n2^{n-2}+4^n\text{ variables},\qquad
(n+1)2^{2n-1}+2^n\text{ clauses}.}\tag{7}
\]

*Proof.* The coloring variables determine one deck-odd coloring by giving opposite colors to paired antipodal edges. For each root, the first two clause families make \(U_x=\{S:r_{x,S}=1\}\) contain the empty subset and be closed under every color-zero forward transition. The third clause family makes it free of complementary pairs. By Theorem 4 this excludes a NORI1 witness. Conversely, if a counterexample coloring exists, take \(U_x\) to be the true zero-reachable family \(R_x\). Theorem 4 guarantees every clause. There are \(n2^{n-2}\) edge orbits and \(4^n\) root-subset memberships; the forward transitions number \(n2^{2n-1}\), complement pairs \(2^{2n-1}\), and initial-root clauses \(2^n\). \(\square\)

**Corollary 7 (resource-groupoid strengthening).** Adding
\[
r_{x,S}\Longrightarrow r_{x+\mathbf1_S,S},\qquad
r_{x,S}\wedge r_{x+\mathbf1_S,T}
\Longrightarrow r_{x,S\cup T}\quad(S\cap T=\varnothing)
\tag{8}
\]
does not change satisfiability. Indeed the true reachable sets satisfy these implications by path reversal and disjoint-resource concatenation, so they still witness the converse direction.

This gives a finite resource-sensitive dual certificate of a potential counterexample, with a clause count growing as \(O(n4^n)\) instead of the factorial number of rooted geodesics. It is not a uniform proof of unsatisfiability.

**Corollary 8 (antipodal root reduction).** In Theorem 6 the rooted membership variables and clauses may be imposed only for a transversal \(T\) of antipodal vertex pairs. The smaller formula is satisfiable if and only if a counterexample coloring exists. Its size is
\[
\boxed{n2^{n-2}+2^{2n-1}\text{ Boolean variables},\qquad
(n+1)2^{2n-2}+2^{n-1}\text{ clauses}.}\tag{9}
\]
For \(n=7\), this is 224 coloring variables, 8192 rooted variables, and 32,832 clauses before symmetry constraints.

*Proof.* Any counterexample coloring has complement-free true reachable families at every root, so restrict to \(T\). Conversely, if a monochromatic antipodal geodesic existed, reversing it and translating by the deck involution would give geodesics of both colors rooted at both antipodal endpoints. One endpoint lies in \(T\), and its color-zero path forces both the empty set and its complement into that root's SAT membership family, contradicting the complementary-pair clauses. Thus the restricted formula excludes all counterexample witnesses if unsatisfiable. Halving the roots halves the reachability variables and clauses. \(\square\)

This is an equivalent finite-dimensional decision procedure, not a uniform proof over all dimensions.

### Edge-order synchronization and stability of extremal boundary colorings

Let \(n\ge6\), and let \(V_n\) consist of real functions \(x(a,b,c)=-x(c,b,a)\) on ordered triples of distinct labels. Its dimension is \(N=n(n-1)(n-2)/2\). The legal-turn reversal quotient has \(E=N(n-3)\) edges. For sign-valued \(x\), let \(D(x)\) count disagreeing turns. Recall the signed adjacency operator
\[
(Ax)(a,b,c)=\sum_{d\notin\{a,b,c\}}[x(b,c,d)+x(d,a,b)]
\]
with spectrum contained in \(\{-(n-2),-2,0,1,n-2\}\). Its smallest eigenspace is
\[
\mathcal E_-=\{f_s(a,b,c)=s_{ab}-s_{bc}:s_{ab}=s_{ba},\ \sum_{b\ne a}s_{ab}=0\}.
\]
Let \(\mathcal G=\{f:f(a,b,c)=u_b(a)-u_b(c)\}\) be the direct sum of local gradient spaces; then \(\mathcal E_-\subseteq\mathcal G\).

**Theorem 1 (canonical symmetric edge potential).** For \(x\in V_n\) define
\[
d_b(a)=\sum_{c\notin\{a,b\}}x(a,b,c),\quad
h_{ab}=d_b(a)+d_a(b),\quad H_a=\sum_{b\ne a}h_{ab}.
\]
The symmetric weights
\[
\boxed{s_{ab}=\frac1{2(n-1)}
\left(h_{ab}-\frac{H_a+H_b}{n-2}\right)}
\tag{1}
\]
have zero row sums and determine the orthogonal projection
\(\Pi_-x=f_s\) onto \(\mathcal E_-\). The nonnegative global synchronization defect
\[
\Gamma(x)=\|\Pi_{\mathcal G}x-\Pi_-x\|^2
\]
has the explicit expression
\[
\boxed{\Gamma(x)=
\frac1{n-1}\sum_b\sum_{a\ne b}d_b(a)^2-
\frac1{2(n-1)}\sum_{a<b}
\left(h_{ab}-\frac{H_a+H_b}{n-2}\right)^2.}
\tag{2}
\]

*Proof.* Reversal skewness gives \(\sum_{a\ne b}d_b(a)=0\), hence \(\sum_aH_a=0\). Formula (1) has zero row sums. For any symmetric zero-row-sum array \(t\), define \(f_t(a,b,c)=t_{ab}-t_{bc}\). Expanding over outer pairs yields
\[
\langle x,f_t\rangle=\sum_{a<b}h_{ab}t_{ab},\qquad
\langle f_s,f_t\rangle=2(n-1)\sum_{a<b}s_{ab}t_{ab}.
\]
Their difference is zero because \(h_{ab}-2(n-1)s_{ab}=(H_a+H_b)/(n-2)\) is orthogonal to \(t\). This proves the projection claim. The local gradient projection has coordinates \((d_b(a)-d_b(c))/(n-1)\) and squared norm \((n-1)^{-1}\sum_{a\ne b}d_b(a)^2\). The norm of \(f_s\) is \(2(n-1)\sum_{a<b}s_{ab}^2\). Subtraction of the nested projection norms proves (2). \(\square\)

For each center \(b\), orient its tournament of outer labels by \(x(a,b,c)\), and let \(t_b\) count directed cyclic triangles, \(T(x)=\sum_b t_b\).

**Theorem 2 (joint curvature and synchronization penalty).** Every sign-valued reversal-skew \(x\) obeys
\[
\boxed{\frac{D(x)}E\le
\frac23+\frac{n-2}{2(n-3)(n-1)}
-\frac{2(n-4)T(x)}{(n-1)E}
-\frac{(n-4)\Gamma(x)}{4E}.}
\tag{3}
\]
*Proof.* The complete-graph Hodge identity yields
\(\|x-\Pi_{\mathcal G}x\|^2=n(n-2)(n-3)/6+8T(x)/(n-1)\).
Nested orthogonal projections add \(\Gamma(x)\) to this squared distance. The spectral gap between \(-(n-2)\) and the remaining eigenvalues, which are at least \(-2\), gives
\[
\langle x,Ax\rangle\ge-(n-2)N+
(n-4)\|x-\Pi_-x\|^2.
\]
Use \(\langle x,Ax\rangle=2E-4D(x)\) and simplify. \(\square\)

**Lemma 3 (elementary tournament stability).** A tournament on \(m\ge3\) vertices with \(t\) cyclic triangles can be made transitive by reversing at most \(8m^2(t/m^3)^{1/3}\) arcs, with zero changes when \(t=0\).

*Proof.* List vertices in increasing outdegree \(d_0\le\cdots\le d_{m-1}\). Counting transitive triples by their source gives
\(\sum_i i^2-\sum_i d_i^2=2t\).
For each \(k\), the \(k\) lowest-degree vertices have at least \(\binom{k}{2}\) internal wins, so \(\sum_{i<k}(d_i-i)\ge0\). Summation by parts against increasing \(d_i\) yields \(\sum_i(i-d_i)d_i\ge0\), hence
\[
\sum_i(i-d_i)^2\le2t. \tag{4}
\]
An inversion in the score order is an arc \(i\to j\) with \(i<j\). It belongs to at least \(d_j-d_i+1\) cyclic triangles, as follows by comparing the two endpoint outdegrees and partitioning their other neighbors into four orientation types.

Set \(\delta=t/m^3\), \(\eta=\delta^{1/3}\), \(\theta=\delta^{1/2}\), assuming \(t>0\). At most \(2t/(\eta^2m^2)\) vertices have \(|d_i-i|>\eta m\), so at most \(2t/(\eta^2m)\) inversion arcs touch such vertices. Among the remaining vertices, at most \((\theta+2\eta)m^2\) pairs have rank separation at most \((\theta+2\eta)m\). Every other inverted arc has outdegree gap greater than \(\theta m\), hence participates in at least \(\theta m\) cyclic triangles. Since each cyclic triangle has three arcs, there are at most \(3t/(\theta m)\) such inversions. The total is at most
\[
m^2\big(\theta+2\eta+2\delta/\eta^2+3\delta/\theta\big)
=m^2(4\delta^{1/3}+4\delta^{1/2})
\le8m^2\delta^{1/3}.
\]
Reversing the inversions gives a transitive order. \(\square\)


**Theorem 4 (near-extremal stability toward edge orderings).** Define
\[
\varepsilon=\max\{0,\,2/3-D(x)/E\},\qquad
z=\varepsilon+\frac{n-2}{2(n-3)(n-1)}.
\]
There exist pairwise distinct symmetric edge weights \(s_{ab}=s_{ba}\) such that the comparison coloring \(x_s(a,b,c)=\operatorname{sgn}(s_{ab}-s_{bc})\) differs from \(x\) on at most \(O(Nz^{1/9})\) reversal classes of triples, with an absolute implied constant. Consequently \(D(x_n)/E_n\ge2/3-o(1)\) forces agreement with an edge-ordered boundary coloring on \(1-o(1)\) of all triple classes.

*Proof.* The nonnegative penalties in (3) give
\[
\frac{2(n-4)T}{(n-1)E}+\frac{(n-4)\Gamma}{4E}\le z.
\]
Writing \(m=n-1\), we have \(T/(nm^3)\le3z/10\) and \(\Gamma/N\le6z\). Apply Lemma 3 to the \(n\) local tournaments. Jensen's inequality supplies a reversal-skew coloring \(y\), whose local tournaments are all transitive, with \(R\) altered triple classes satisfying
\[
R/N\le \frac{16m}{m-1}(T/(nm^3))^{1/3}
\le20z^{1/3}. \tag{5}
\]
Take the symmetric potential \(s\) computed by (1), so \(\Pi_-x=f_s\). Projection contractivity, \(\|x-y\|^2=4R\), and the definition of \(\Gamma\) give
\[
\|\Pi_{\mathcal G}y-f_s\|^2\le8R+2\Gamma. \tag{6}
\]
The signed outdegree scores of a transitive tournament on \(m\) vertices are \(-(m-1),-(m-3),\ldots,m-1\). Consequently the local gradient projection \((\Pi_{\mathcal G}y)(a,b,c)\) has the same sign as \(y(a,b,c)\) and magnitude \(2|i-j|/m\), where \(i,j\) are their local ranks.

For any \(0<\theta<1\), the fraction of outer pairs with rank separation smaller than \(\theta m\) is at most \(2m\theta/(m-1)\). Every other pair at which \(y\) and the sign of \(f_s\) disagree contributes at least \(4\theta^2\) to (6). Perturb the finitely many symmetric weights generically by sufficiently small amounts to eliminate ties while preserving all strict comparisons. Thus
\[
\frac{\operatorname{dist}(x,x_s)}N
\le\frac RN+\frac{2m}{m-1}\theta+
\frac{8R+2\Gamma}{4\theta^2N}. \tag{7}
\]
Taking \(\theta=z^{1/9}\) when \(z<1\), and applying (5) and the preceding bounds, proves the assertion. For \(z\ge1\) the bound is immediate after enlarging its absolute constant. \(\square\)

The theorem concerns unrestricted reversal-odd boundary tournaments; the edge-ordered subclass emerges quantitatively in the near-extremal density regime. Transferring long vertex-simple paths across exceptional triples requires a separate robustness argument.


### NORI Article XI — precise Smith form for boundary-tournament tight windows

**Theorem (proved, n >= 5).** Let T_n be the reversal-orbits of distinct ordered triples (a,b,c)~(c,b,a), N=n(n-1)(n-2)/2. Let h_pi be the 0/1 incidence vector of the n-2 consecutive triple windows in any Hamiltonian word pi. Then

  span_Z{h_pi: pi in S_n}
    = {z in Z^N: sum(z) = 0 mod (n-2)}.

Thus Z^N/span_Z{h_pi} = Z/(n-2), and the Smith normal form has N-1 ones and one n-2. This proves the earlier Smith-form conjecture, not merely the n=5,6,7 computations.

**Local swaps.** If a Hamiltonian word ends u,a,b,c, exchanging b,c gives the identity for an annihilating triple weighting w_{abc}=w_{cba}:

  w_{uab}+w_{abc}-w_{uac}-w_{acb}=0. (E)

For characteristic different from two, fix middle symbol a. Equation (E) says the differences of the symmetric matrix M_a(u,b)=w_{uab} between columns b,c do not depend on row u. The standard complete-graph additive lemma (solve three pair equations and extend by column differences) gives M_a(u,b)=s_a(u)+s_a(b). Set P_ab=s_a(b)+s_b(a). Substitution in E shows P_ab-P_ac=s_c(b)-s_b(c), independent of a, so another application of the lemma gives P_ab=gamma_a+gamma_b. Adding/subtracting these two identities gives s_a(b)=gamma_b, hence w_{abc}=gamma_a+gamma_c.

The Hamiltonian sum is 2 sum gamma_i minus the gamma values at the four end positions. Swapping an interior-position label with an end-position label forces all gamma_i equal. So w is constant, and the word constraint is (n-2)w=0. This proves the claimed annihilator dimension for all fields of odd characteristic and for characteristic zero.

For characteristic two, each relation (E) is a four-cycle in F=L(K_n) with vertices ua,ab,bc,ac. These squares generate the even-length subspace of Z_1(F;F2): the cycle space is generated by star triangles (three K_n edges at a vertex) and edge triangles (three K_n edges forming a triangle). An E square is the symmetric difference of an edge triangle on ab,ac,bc and a star triangle on ua,ab,ac. Two K_n edge triangles sharing an original K_n edge are congruent via the same star triangle; the adjacency graph of K_n triangles is connected. Thus all generating triangles are congruent modulo E squares, and their common odd parity proves the square span is precisely the even-cycle subspace.

Therefore every F2 annihilating weighting of (E) has the form
  w_{abc}=u_{ab}+u_{bc}+z,
a cut cochain on F plus a constant. Summing over a Hamiltonian word telescopes the cut, yielding u_{v1v2}+u_{v(n-1)vn}+(n-2)z=0. Any two disjoint edges of K_n can be the first and last. For two edges sharing a vertex, a third edge disjoint from both exists since n>=5; comparing these pairs forces their u-values equal. Connectivity of L(K_n) forces u constant. Thus w=z constant and (n-2)z=0. Hence over *every* field the annihilator has dimension one precise when its characteristic divides n-2; otherwise it is zero.

**Integral step.** The Hamiltonian incidence matrix has full rational rank, so C=Z^N/L is finite. In every characteristic its corank is <=1, making C cyclic. For each prime dividing |C|, the unique modular annihilator is the all-one cochain, nonzero on every basis vector e_t; therefore every e_t generates C. S_n acts on C by relabeling. Since Aut(C) is abelian, conjugate transpositions induce the same automorphism. A transposition of two labels outside a fixed triple exists (n>=5) and fixes the generator e_t; it therefore acts trivially. Thus all transpositions, hence all permutations, act trivially, and every e_t is the same element e of C. Each Hamiltonian row has n-2 windows, giving (n-2)e=0. Conversely total coordinate sum modulo n-2 gives a surjection C -> Z/(n-2). Hence C is precise Z/(n-2).

**Significance.** The cube's geodesic unsigned incidence lattice was proved saturated for n>=5. The boundary-tournament Hamiltonian triple-window lattice has precisely one length-based torsion factor n-2, and no other hidden integrality defects. The theorem concerns unsigned triple-window incidence, not the entire pointed two-port cocircuit incidence matrix. It does not yield positivity, a monochromatic tight path, or unrestricted NORI1; the nonlinear low-cost gallery selector remains open.


#### Signed Hamiltonian tight-window incidence: complete Smith form

Choose one oriented representative of every reversal class \(t=[a,b,c]=[c,b,a]\). Each Hamiltonian word \(\pi\) determines a signed incidence vector \(s_\pi\in\mathbb Z^{\mathcal T_n}\), in which a triple window contributes \(+1\) if it agrees with the chosen orientation of its reversal orbit, and \(-1\) if it is reversed. Write \(\Lambda_n^\pm=\operatorname{span}_{\mathbb Z}\{s_\pi\}\).

**Theorem 2 (signed Smith form).** For all \(n\ge5\),
\[
\boxed{\mathbb Z^{\mathcal T_n}/\Lambda_n^\pm\cong
\begin{cases}
0,&n\ \text{odd},\\
\mathbb Z/2\mathbb Z,&n\ \text{even}.
\end{cases}}
\]
Thus the signed Hamiltonian incidence matrix has full rational column rank. All nonzero Smith invariant factors are one in odd orders, and there is a single factor two in even orders.

*Proof.* We first compute its linear annihilator over fields. For characteristic different from two, represent an annihilating weighting by \(z_{abc}=-z_{cba}\). The terminal adjacent-swap comparison gives, for pairwise distinct \(u,a,b,c\),
\[
z_{uab}+z_{abc}-z_{uac}-z_{acb}=0.\tag{S}
\]
Interpret triple reversal orbits as oriented edges of \(F=L(K_n)\), where \((u,a,b)\) is the edge from \(\{u,a\}\) to \(\{a,b\}\).

Fix \(a\) and put \(M_a(u,b)=z_{uab}\); this is antisymmetric in \(u,b\). The relation (S) says \(M_a(u,b)-M_a(u,c)\) is independent of \(u\) outside \(\{a,b,c\}\). It follows that the triangular circulation
\[
T_a(u,b,c)=M_a(u,b)+M_a(b,c)+M_a(c,u)
\]
does not change if any one of the three arguments is replaced by a fourth distinct label. Comparing such replacements on four labels shows \(T_a(u,b,c)=-T_a(u,b,c)\); since the field characteristic is not two, \(T_a=0\). Thus there are potentials \(r_a(b)\) with
\[
z_{uab}=r_a(b)-r_a(u).
\]
Substituting this form in (S), the skew function \(P_{ab}=r_a(b)-r_b(a)\) has zero triangular circulation on \(K_n\); hence \(P_{ab}=\gamma_b-\gamma_a\) for some \(\gamma\). The potentials
\[
v_{\{a,b\}}=r_a(b)+\gamma_a
\]
are symmetric, since \(r_a(b)-r_b(a)=\gamma_b-\gamma_a\), and yield
\[
\boxed{z_{uab}=v_{\{a,b\}}-v_{\{u,a\}}.}
\]
This is a graph coboundary on \(F\). In a Hamiltonian tight-window sequence it telescopes to the potential of the final unordered edge minus that of the initial unordered edge. Any two disjoint \(K_n\) edges can occur as these endpoints. If two edges intersect, a third edge disjoint from both exists for \(n\ge5\), so comparison through that edge forces their potentials to agree as well. Therefore every \(v_{\{a,b\}}\) is equal and \(z=0\). The signed incidence matrix has full column rank over every field of characteristic other than two.

Over characteristic two, the orientation signs disappear. The unsigned Smith-form theorem above says that its nullity is zero when \(n\) is odd and one when \(n\) is even; in the latter case the unique annihilator is the constant triple-orbit weighting.

The integral cokernel \(C^\pm=\mathbb Z^{\mathcal T_n}/\Lambda_n^\pm\) is finite because of rational full column rank. It has no odd-primary torsion and its reduction modulo two has dimension zero for odd \(n\), one for even \(n\). Therefore it is trivial for odd \(n\) and a cyclic \(2\)-group for even \(n\). In the even case, each coordinate class \(e_t\) generates \(C^\pm\), since the unique modular annihilator is constant and nonzero at every triple orbit.

Relabeling gives an action of \(S_n\) on the cokernel. Since a cyclic group has abelian automorphism group, conjugate transpositions induce the same automorphism. For any fixed oriented triple, two unused labels exist when \(n\ge5\). Their transposition fixes its generating coordinate class and must act as identity. Thus every transposition acts trivially. But exchanging the first and third labels of a triple sends its signed coordinate class \(e_t\) to \(-e_t\). Consequently \(2e_t=0\), so the cokernel has exponent two. It is nonzero in even orders by its mod-two deficiency; hence \(C^\pm=\mathbb Z/2\mathbb Z\). \(\square\)

**Scope.** These two Smith-form results concern unsigned and reversal-signed Hamiltonian triple-window incidences. They are not statements about all pointed dual-matroid cocircuits. The unsigned length congruence and residual signed parity describe linear integer obstructions; they do not produce nonnegative path representations, low-switch geodesics, or long monochromatic boundary-tournament tight paths.

#### Nonnegative cones and the missing connectivity constraints

The integral lattice identities above admit a sharp positivity analysis.

**Theorem 3 (the signed Hamiltonian semigroup has no convex restriction).** Let
\[
\mathsf S_n^\pm=\left\{\sum_{\pi\in S_n}m_\pi s_\pi:
m_\pi\in\mathbb Z_{\ge0}\right\}
\]
be the nonnegative integral semigroup generated by the signed Hamiltonian triple-window incidence vectors. For every \(n\ge5\),
\[
\boxed{
\mathsf S_n^\pm=\Lambda_n^\pm
=\begin{cases}
\mathbb Z^{\mathcal T_n},&n\text{ odd},\\
\{z\in\mathbb Z^{\mathcal T_n}:\sum_tz_t\equiv0\pmod2\},
&n\text{ even}.
\end{cases}}
\tag{16}
\]
The real cone generated by these signed vectors is the entire real space \(\mathbb R^{\mathcal T_n}\).

*Proof.* Reversing a Hamiltonian vertex word reverses all of its triple windows, so
\[
s_{\pi^R}=-s_\pi.
\]
Every integer linear combination of signed path vectors can therefore be rewritten as a nonnegative integer combination, by replacing a negatively weighted path with its reversal. Hence the signed semigroup equals its generated integer lattice. The signed Smith theorem gives this lattice as the entire space in odd orders and a subgroup of index two in even orders. For even \(n\), each signed row has even coordinate sum, and the parity-even subgroup itself has index two, identifying the lattice. Full rational column rank and the availability of both \(s_\pi\) and \(-s_\pi\) make the real cone equal to the whole space. \(\square\)

This theorem warns against treating nonnegative coefficients in a **signed** incidence expansion as a positive witness: reversal provides a negative representative for every path, so the semigroup has no pointed-cone geometry. The relevant convex constraints must instead retain orientation-specific feasibility or use unsigned incidences.

For unsigned windows let
\[
P_n=\operatorname{conv}\{h_\pi:\pi\in S_n\}
\subseteq\mathbb R^{\mathcal T_n},
\tag{17}
\]
and define the middle-resource projection
\[
(Mz)_v=\sum_{\substack{a,c\in[n]\setminus\{v\}\\a<c}}
z_{[a,v,c]},\qquad v\in[n].
\tag{18}
\]

**Theorem 4 (uniform-matroid base projection).** For \(n\ge5\),
\[
\boxed{
M(P_n)=\left\{y\in[0,1]^n:
\sum_{v=1}^n y_v=n-2\right\}
=B(U_{n-2,n}),
}
\tag{19}
\]
the base polytope of the uniform matroid of rank \(n-2\).

*Proof.* A Hamiltonian word uses each vertex as a middle vertex of a triple window precisely when that vertex is neither its first nor its last label. Hence
\[
Mh_\pi=\mathbf1-e_{v_1}-e_{v_n}.
\]
Every unordered pair of possible endpoints occurs in a Hamiltonian word, so the images of path vectors are all \(0/1\) vectors with \(n-2\) ones. Their convex hull is the hypersimplex \(B(U_{n-2,n})\). \(\square\)

The base-polytope projection captures the resource independence used by Hamiltonian words, but it does not capture their connectedness.

**Theorem 5 (cut inequalities and disconnected lattice certificates).** For every nonempty proper vertex set \(S\subsetneq[n]\), define
\[
q_S([a,b,c])=
\mathbf1\bigl(\{a,b\}\in\delta_{K_n}(S)
\text{ or }\{b,c\}\in\delta_{K_n}(S)\bigr).
\tag{20}
\]
Every unsigned Hamiltonian path-incidence vector satisfies
\[
\boxed{\langle q_S,h_\pi\rangle\ge1,}
\tag{21}
\]
and therefore so does every \(z\in P_n\). For every \(n\ge6\), however, there exists a \(0/1\) vector \(z\in\mathbb Z^{\mathcal T_n}\) satisfying all of the following:
\[
\boxed{
\begin{gathered}
z\ge0,\quad\sum_tz_t=n-2,\quad
z\in\Lambda_n,\quad
Mz=\mathbf1-e_u-e_v\in B(U_{n-2,n}),\\
\langle q_S,z\rangle=0\text{ for some nontrivial }S.
\end{gathered}}
\tag{22}
\]
In particular, the complete Smith congruence plus nonnegativity and the uniform-matroid resource-base constraints are insufficient to characterize a Hamiltonian path or its convex hull.

*Proof.* Every Hamiltonian word visits vertices in both \(S\) and its complement, so at least one of its consecutive \(K_n\) edges crosses \(\delta(S)\). That edge belongs to at least one of the \(n-2\) consecutive triple windows, proving (21).

For (22), partition the vertex set into \(S\dot\cup S^c\) with \(|S|,|S^c|\ge3\). Choose one omitted middle vertex \(u\in S\) and \(v\in S^c\). For every other center \(b\), choose distinct \(a,c\) from the same side as \(b\) and different from \(b\); put a single one in the coordinate \([a,b,c]\), with all other coordinates zero. Different centers give different triple-orbit coordinates, so the resulting \(z\) is \(0/1\), has \(n-2\) ones, and has middle-resource projection \(\mathbf1-e_u-e_v\). The unsigned Smith theorem puts it in \(\Lambda_n\), because its coordinate sum equals \(n-2\). But no chosen triple crosses the partition, giving \(\langle q_S,z\rangle=0\), contrary to (21). \(\square\)

**Implication for the unification program.** The two lattice theorems eliminate divisibility ambiguity but do not replace coherent resource-independent path geometry. Signed cones are non-pointed because reversal negates generators; unsigned convex path incidence has additional global connectivity inequalities invisible to both the Smith lattice and its uniform-matroid middle-resource projection. A common matroidal low-switch selector must preserve **graphic connectivity across cuts**, in addition to linear incidence and resource independence. The new conclusions are polyhedral obstructions to a proposed shortcut, not proofs of the unrestricted cube or boundary-tournament existence conjectures.

### Antipodal cut-pair separation and four-sector cocycle geometry

The component-contact minor records the intersections of monochromatic components with their deck images. Here we recover additional information lost under zero-turn contraction: the *boundaries of a monochromatic component and its deck image are disjoint graphic-matroid cocycles*. This yields a canonical four-sector quotient with prescribed boundary colors, and a matroid-intersection characterization of which vertex sets can occur as monochromatic components under a deck-odd coloring.

Let \(G\) be a finite connected graph with a fixed-point-free involution \(\tau\) that acts freely on edges, and let \(c:E(G)\to\mathbb F_2\) obey \(c(\tau e)=1+c(e)\). The antipodal cube \(Q_n\), \(n\ge3\), is the principal example. The graph cuts \(\delta_G(S)\) form the cocycle space of the graphic matroid \(M(G)\).

#### 1. Disjoint antipodal cut cocycles

**Theorem 1 (component-cut disjointness).** Let \(R\subseteq V(G)\) be the vertex set of one connected color-zero component, excluding isolated zero-degree vertices. Then
\[
\boxed{\delta_G(R)\subseteq c^{-1}(1),\qquad
\delta_G(\tau R)=\tau\delta_G(R)\subseteq c^{-1}(0),}
\tag{1}
\]
and therefore
\[
\boxed{\delta_G(R)\cap\delta_G(\tau R)=\varnothing.}
\tag{2}
\]

*Proof.* An edge leaving a full color-zero connected component cannot itself have color zero, since its exterior endpoint would belong to the same component. Thus \(\delta_G(R)\) is blue. Applying \(\tau\) converts those edges to red and gives the boundary of \(\tau R\), proving (1) and (2). \(\square\)

**Corollary 2 (antipodal cocycle pair).** The two graphic-matroid cocycles \(\delta_G(R)\) and \(\delta_G(\tau R)\) have disjoint supports, are exchanged by \(\tau\), and have the same cardinality. Their union is the cocycle
\[
\boxed{
\delta_G(R)\sqcup\delta_G(\tau R)
=\delta_G(R\mathbin{\triangle}\tau R).
}
\tag{3}
\]
If \(R\) contains an antipodal pair, then \(R\cap\tau R\ne\varnothing\), and this pair of separated cuts coexists with a port-parallel loop in the pointed component-contact minor.

*Proof.* Binary cut addition obeys \(\delta(A)\triangle\delta(B)=\delta(A\triangle B)\). The supports are disjoint by (2), and \(\tau\) exchanges them. \(\square\)

#### 2. Canonical four-sector geometry

Define a partition of \(V(G)\):
\[
\boxed{
I=R\cap\tau R,\quad
A=R\setminus\tau R,\quad
B=\tau R\setminus R=\tau A,\quad
O=V(G)\setminus(R\cup\tau R).
}
\tag{4}
\]
The sectors \(I,O\) are \(\tau\)-invariant; \(\tau\) exchanges \(A\) and \(B\).

**Theorem 3 (four-sector forbidden diagonals and forced colors).** No edge joins \(I\) to \(O\), and no edge joins \(A\) to \(B\):
\[
\boxed{E_G(I,O)=E_G(A,B)=\varnothing.}
\tag{5}
\]
Every edge between distinct sectors belongs to one of the four other cross-sector classes. Its color is forced:
\[
\boxed{
c(E_G(I,A))=0,\quad
c(E_G(B,O))=0,\quad
c(E_G(I,B))=1,\quad
c(E_G(A,O))=1.
}
\tag{6}
\]
Edges contained within an individual sector are not assigned a color by (5)–(6).

*Proof.* An edge between \(I\) and \(O\) crosses both boundaries \(\delta(R)\) and \(\delta(\tau R)\); so does an edge between \(A\) and \(B\). Theorem 1 forbids such edges. An \(I\)-to-\(A\) edge crosses \(\delta(\tau R)\), hence is red. An \(I\)-to-\(B\) edge crosses \(\delta(R)\), hence is blue. The other two cases are symmetric and give (6). \(\square\)

Equivalently, the sector label defines a \(\tau\)-equivariant graph map to a four-cycle with cyclic sectors \(I,A,O,B\), allowing stationary steps, and with the two opposite diagonals forbidden. Red and blue boundary edges alternate around this four-cycle. The quotient is a global compatibility constraint between the color-zero component \(R\), the color-one component \(\tau R\), and their interface \(I\), not merely a statement about one component in isolation.

#### 3. Which sets can be monochromatic components?

Let \(G\) be any finite connected graph with a fixed-point-free involution acting freely on edges, as at the start of this Subsection. A deck edge orbit is the two-element pair \(\{e,\tau e\}\). For a vertex set \(R\), let \(G_R=G[R]\) be its induced graph. The edge orbits partition \(E(G_R)\) into classes of size one or two. Let \(P_\tau(R)\) be the partition matroid on \(E(G_R)\) permitting at most one selected edge from each antipodal orbit. Let \(M(G_R)\) be the graphic cycle matroid of the induced graph.

**Theorem 4 (graphic–partition matroid component characterization).** For a nonempty \(R\subseteq V(G)\), there exists a deck-odd edge coloring of the full covering graph for which \(R\) is precisely one connected red component if and only if
\[
\boxed{
\delta_G(R)\cap\tau\delta_G(R)=\varnothing
}
\tag{7}
\]
and
\[
\boxed{
\max\{|T|:T\in\mathcal I(M(G_R))\cap\mathcal I(P_\tau(R))\}
=|R|-1.
}
\tag{8}
\]
The second condition says that \(G_R\) has a spanning tree containing no antipodal pair of edges.

*Proof.* For necessity, let \(R\) be a red component of a deck-odd coloring. Condition (7) is Theorem 1. Choose a red spanning tree of \(R\). It is independent in \(M(G_R)\), has \(|R|-1\) edges, and cannot contain both members of an antipodal edge pair because they have complementary colors. Thus (8) holds.

For sufficiency, choose a spanning tree \(T\subseteq E(G_R)\) meeting each edge orbit at most once. For each orbit that meets \(\delta(R)\), color its unique boundary member blue and its antipode red; this prescription is consistent because (7) forbids both orbit members from lying in \(\delta(R)\). On every still-uncolored edge orbit meeting \(T\), declare its member in \(T\) red and its antipode blue; there is no conflict because the orbit contains at most one tree edge, and any tree edge whose antipode was a boundary edge has already been colored red. Color the remaining orbits arbitrarily with complementary bits. All boundary edges of \(R\) are blue, so no red path exits \(R\); every edge of \(T\) is red, so \(R\) is red connected. Hence \(R\) is one full red component. \(\square\)

**Corollary 5 (intrinsic partition-cut test).** Condition (8) holds if and only if for every partition
\(\mathcal P=\{R_1,\ldots,R_k\}\) of the vertex set \(R\) into \(k\ge2\) nonempty parts,
\[
\boxed{
\#\left\{\text{antipodal edge orbits containing an edge of }
G_R\text{ crossing }\mathcal P\right\}\ge k-1.
}
\tag{9}
\]
Thus (7) together with (9) gives a criterion expressed entirely by **disjoint antipodal graphic cocycles and edge-orbit matroid rank**, without quantification over edge colorings.

*Proof.* Apply the matroid-intersection min–max theorem to \(M(G_R)\) and \(P_\tau(R)\). For any edge subset \(F\subseteq E(G_R)\), the graphic rank is \(|R|-\kappa(F)\), where \(\kappa(F)\) is the number of connected components of \((R,F)\). The partition rank on \(E(G_R)\setminus F\) is the number of antipodal edge orbits represented there. Therefore the intersection has a common independent set of size \(|R|-1\) precisely when, for all \(F\),
\[
\#\{\text{orbits represented in }E(G_R)\setminus F\}
\ge\kappa(F)-1.
\]
The crossing edges of the component partition of \(F\) lie outside \(F\), so (9) implies the inequalities. Conversely, for an arbitrary partition \(\mathcal P\), take \(F\) to contain all edges internal to its parts. The remaining edges are its crossing edges and \(\kappa(F)\ge k\), proving (9). \(\square\)

#### 4. Consequences for the spanning-geodesic selector

For a cube coloring \(c\), take a red component \(R\) containing an antipodal pair. The component is subject simultaneously to (i) the graphic-rank amplification bound from the preceding Subsection, (ii) the antipodal cocycle separation (7), and (iii) the orbit-rainbow connectivity condition (8). The induced four-sector partition constrains every edge leaving \(R\) and every edge leaving its antipodal blue mate \(\tau R\).

These conditions provide an intrinsic matroidal class of admissible **monochromatic component supports**, not merely of signed turn graphs. Nevertheless, they characterize which supports are possible under *some* deck-odd coloring, not which edges inside such a support are red under a previously fixed coloring. A vertex-simple antipodal geodesic lying in \(Q_n[R]\) need not be red. Therefore the characterization alone does not establish NORI1.

The next closure problem is to combine the two-cut sector geometry with resource-simple fundamental-circuit exchange. It would suffice to prove that in every admissible fixed coloring, some self-antipodal red component contains a **red** shortest antipodal path. Disjoint graphic cocycle pairs and the partition-cut criterion are additional constraints that any purported counterexample must satisfy; in isolation they do not imply the desired distance equality.

#### 5. Shared specialization to both canonical systems

**Corollary 6 (common component-support structure).** Theorems 1–4 and Corollary 5 apply to both canonical Article XI graph coverings:

(i) the \(n\)-regular antipodal cube cover \(Q_n\to Q_n/\tau\), whose covering edges are cube edges; and

(ii) the \(2(n-2)\)-regular ordered-pair cover \(S(K_n)\to L(K_n)\) used for ordinary reversal-odd boundary 3-tournaments, whose covering edges are ordered triples \((a,b,c)\), with deck reversal \((c,b,a)\).

For both systems, every monochromatic component \(R\) and its opposite-colored deck image \(\tau R\) determine disjoint antipodal cut cocycles and the same four-sector constraints. A candidate monochromatic component support is realizable by a deck-odd coloring if and only if its antipodal cut pair is disjoint and its induced graph has an edge-orbit-rainbow spanning tree, equivalently the partition-cut inequalities (9).

*Proof.* In either cover, the deck involution acts freely on vertices and edges and complements edge-state colors. The proofs above use only those conditions and the graphic–partition matroid intersection theorem. \(\square\)

In the boundary model, the vertices of \(S(K_n)\) are ordered pairs of original vertices. Thus red connectivity of an ordered-pair component does not ensure a forward vertex-simple tight path. The shared cocycle and component-realizability structures are independent of, but compatible with, the additional original-resource matroid required for the spanning one-turn conjecture.

Let \(Q_n\) be the \(n\)-cube, \(n\ge3\), \(\tau(x)=x+\mathbf1_{[n]}\), and \(H_n=L(Q_n/\tau)\), whose \(n2^{n-2}\) vertices correspond to antipodal orbits of cube edges. Fix any order \(\pi=(1,\ldots,n)\) of coordinate directions. For a starting vertex \(x\), let \(C_x^\pi\subseteq H_n\) be the simple length-\(n\) turn cycle of the antipodal geodesic starting at \(x\) and visiting coordinates in order \(\pi\).

**Theorem 1 (geodesic vertex-disjoint packing).** For even \(n\ge4\), choose one representative \(x\) from each antipodal pair of even-parity cube vertices. The family of cycles \(C_x^\pi\), indexed by those \(2^{n-2}\) roots, partitions \(V(H_n)\) into pairwise vertex-disjoint cycles of length \(n\). In particular it is a 2-factor of \(H_n\), all of whose components are shortest odd-monodromy turn cycles.

For odd \(n\ge3\), choose every even-parity cube vertex \(x\) whose first two coordinates are zero. The resulting \(2^{n-3}\) cycles \(C_x^\pi\) are pairwise vertex-disjoint.

*Proof.* Along a fixed order \(\pi\), the state corresponding to direction \(i\) on the path from \(x\) is the cube edge starting at \(x\) translated by the fixed preceding-coordinate prefix. Suppose the projected edge states in direction \(i\) from roots \(x,y\) coincide. Two unoriented cube edges lie in the same antipodal orbit precisely when one is the other, its endpoint reversal, its antipodal translate, or the endpoint reversal of that translate. Translating away the common coordinate prefix gives
\[
\boxed{y\in\{x,\ x+e_i,\ \tau x,\ \tau x+e_i\}.}\tag{1}
\]
For even \(n\), both selected roots have even parity, excluding \(x+e_i\) and \(\tau x+e_i\). The two remaining possibilities are the same selected root or its antipode, and the latter is excluded by choosing one representative from each pair. Thus the cycles are vertex-disjoint. Their number times \(n\) equals \(|V(H_n)|\), proving the partition assertion.

For odd \(n\), \(x+e_i\) and \(\tau x\) have odd parity, so neither is selected. The point \(\tau x+e_i\) has at least one of its first two coordinates equal to one, whether \(i\) belongs to those two directions or not. Since all selected roots have both coordinates zero, this final possibility is also excluded. Their number is \(2^{n-3}\), proving the second assertion. \(\square\)

**Corollary 2 (pointed-cocircuit sunflower).** Let \(D_n\) be the pointed binary turn matroid and \(p\) its distinguished port. Each cycle \(C_x^\pi\) determines a shortest port cocircuit \(Y_x=E(C_x^\pi)\cup\{p\}\). The family of such cocircuits satisfies
\[
\boxed{Y_x\cap Y_y=\{p\}\quad(x\ne y),}\tag{2}
\]
and has cardinality \(2^{n-2}\) when \(n\) is even, and \(2^{n-3}\) when \(n\) is odd.

*Proof.* Disjoint turn-cycle vertex sets give disjoint turn-edge sets, while each port cocircuit contains \(p\). \(\square\)

**Theorem 3 (exponential-probability monochromatic NORI1).** Color each antipodal orbit of cube edges independently with an unbiased bit, giving its antipodal mate the complementary bit. Then the probability that the coloring has a monochromatic full antipodal geodesic obeys
\[
\boxed{
\Pr(\mathrm{NORI1\ witness})
\ge
\begin{cases}
1-\left(1-\dfrac{n}{2^{n-1}}\right)^{2^{n-2}}
\ge1-e^{-n/2},&n\text{ even},\\[6pt]
1-\left(1-\dfrac{n}{2^{n-1}}\right)^{2^{n-3}}
\ge1-e^{-n/4},&n\text{ odd}.
\end{cases}}\tag{3}
\]

*Proof.* For one fixed antipodal-geodesic turn cycle, the \(n\) cube-edge states belong to distinct antipodal edge orbits. Their edge colors are therefore independent unbiased bits. The cyclic comparison of consecutive states uses the deck complement of the first bit at the closing seam. The cyclic number of disagreements is one precisely when the linear color word is constant, or changes once between two constant blocks. There are \(2\) constant words and \(2(n-1)\) one-change words, among \(2^n\) equally likely words. Thus
\[
\Pr(w_d(C)=1)=\frac{2n}{2^n}=\frac{n}{2^{n-1}}.
\]
A cycle of cyclic turn weight one can be rerooted at its changed turn to give a monochromatic full antipodal geodesic. By Theorem 1, the cycles in the selected packing have disjoint edge-state orbit sets. Thus their weight-one events are independent. The complement of the event that at least one succeeds has probability \((1-n/2^{n-1})^k\), where \(k\) is the size of the packing. Substituting the two values of \(k\) gives (3); the exponential estimates follow from \(1-z\le e^{-z}\). \(\square\)

**Proposition 4 (why the full 2-factor is restricted to even dimension).** For odd \(n\), the turn graph \(H_n\) cannot have a partition of its vertices into antipodal-geodesic turn cycles, regardless of coordinate ordering.

*Proof.* Such a partition would cover every edge of the folded cube \(G_n=Q_n/\tau\) by edge-disjoint closed geodesic walks. Each component is a graph cycle, so their union would give every vertex of \(G_n\) even degree. But \(G_n\) is \(n\)-regular with \(n\) odd. This is impossible. \(\square\)

The two-factor theorem produces many independently testable shortest port cocircuits, and the probability bound quantifies how unlikely a counterexample is under an unbiased deck-odd coloring. It does not prove the worst-case conjecture: an adversarial coloring could make all members of one packing have at least three disagreements. Relations between different packings, rather than independence within a single packing, would be needed for a deterministic closure.

Let \(N\) be a finite loopless matroid of rank \(r\), let \(I_0\) be an independent set spanning the **anchor flat** \(F_0=\operatorname{cl}_N(I_0)\), and let \(B_1,B_2\) be independent resource sets containing \(I_0\). Put \(F_i=\operatorname{cl}_N(B_i)\).

**Theorem 1 (modular complementary-flat gluing).** If
\[
\boxed{
F_1\wedge F_2=F_0,\qquad
F_1\vee F_2=E(N),\qquad
r(F_1)+r(F_2)=r(F_0)+r(N),}
\tag{1}
\]
then
\[
\boxed{B_1\cap B_2=I_0,\qquad B_1\cup B_2\text{ is a basis of }N.}\tag{2}
\]
Conversely, if \(B_1\cap B_2=I_0\) and \(B_1\cup B_2\) is a basis, all three relations in (1) hold. Thus (1) characterizes pairs of **complementary modular flats over \(F_0\)** whose bases glue to one full resource basis.

*Proof.* Since \(B_i\) is independent and contains a basis \(I_0\) of \(F_0\), it cannot contain any further element of \(F_0\). A common element of \(B_1,B_2\) belongs to \(F_1\cap F_2=F_0\); hence their intersection is \(I_0\). The union therefore has cardinality
\[
|B_1\cup B_2|=r(F_1)+r(F_2)-r(F_0)=r(N).
\]
It spans \(F_1\vee F_2=E(N)\). A spanning set of size \(r(N)\) is a basis, proving (2).

Conversely, assume \(B_1\cap B_2=I_0\) and their union is a basis. Their closures jointly span \(N\), so \(F_1\vee F_2=E(N)\). The basis cardinality gives \(r(F_1)+r(F_2)-r(F_0)=r(N)\). By submodularity,
\[
r(F_1\cap F_2)\le r(F_1)+r(F_2)-r(F_1\vee F_2)=r(F_0).
\]
But \(F_0\subseteq F_1\cap F_2\), so their ranks agree; since both are flats, \(F_1\cap F_2=F_0\). All conditions in (1) follow. \(\square\)

**Theorem 2 (colored opposite-terminal gluing).** Suppose \(B_1,B_2\) arise from two same-colored coherent paths in a deck-reversal-odd path system, and their distinguished terminal states are opposite and compatible: reversing and deck-translating the second path can be concatenated with the first along the shared anchor, without introducing any additional turn. If their resource flats satisfy (1), the concatenated path uses a full basis of resources and has at most one color change.

*Proof.* The reversal-deck operation complements the colors of the second arm. By terminal compatibility the two arms concatenate into one coherent path, with no extra interior transition beyond their joining seam. Theorem 1 says their combined resource set, counting the anchor once, is a full independent basis. Each arm was monochromatic, and the transformed second arm has the opposite color, so the concatenation has at most one color change. \(\square\)

The compatibility hypothesis in Theorem 2 is essential: complementary matroid flats alone do not encode the order in which directed path states can be joined. The theorem isolates resource-basis gluing as a modular-flat property and forward coherence as a separate signed-cover condition.

**Corollary 4 (boundary graphic flats form a Boolean sublattice).** Fix an unordered pair {u,v} and put A=V without {u,v}. Among flats of the graphic matroid M(K_V), consider only F_S=E(K_{S union {u,v}}), for S subset A. They are a Boolean sublattice: F_S meet F_T=F_(S intersect T), F_S join F_T=F_(S union T), with rank r(F_S)=|S|+1. Every pair is modular. The flat F_empty is the common anchor edge {u,v}, and F_A is the full resource flat. Therefore two terminal arms have complementary modular flats if and only if their sets of visited vertices outside {u,v} are complementary subsets of A.

**Theorem 5 (opposite-terminal complementary-family criterion).** For an ordinary reversal-odd boundary 3-tournament on \(V\), fix distinct \(u,v\) and a color \(\varepsilon\). Put \(A=V\setminus\{u,v\}\), and define
\[
\mathcal R^\varepsilon_{uv}
=\{S\subseteq A:\text{there is a vertex-simple monochromatic }\varepsilon
\text{ tight path ending at }(u,v)
\text{ whose vertex set is }S\cup\{u,v\}\}.
\tag{4}
\]
The vacuous two-vertex path is allowed. Then the boundary tournament has a spanning tight path with at most one internal color change if and only if
\[
\boxed{
\exists u\ne v,\ \varepsilon,\ S\subseteq A:
S\in\mathcal R^\varepsilon_{uv},\quad
A\setminus S\in\mathcal R^\varepsilon_{vu}.}
\tag{5}
\]
Consequently, if the spanning one-turn conjecture fails for a coloring, then for every unordered pair \(\{u,v\}\) and both colors \(\varepsilon\),
\[
\boxed{
|\mathcal R^\varepsilon_{uv}|+
|\mathcal R^\varepsilon_{vu}|\le2^{n-2}.}\tag{6}
\]

*Proof.* The resource footprints of the two paths in (5) have original vertex sets meeting only at \(u,v\) and covering \(V\). Their terminal ordered pairs are opposite and their triple colors coincide. The opposite-terminal packing theorem in Article XI (or Theorem 2 above) joins them into a vertex-simple spanning path with at most one color change. Conversely, any such path splits at its color-change seam into two same-colored terminal arms after reversal of the suffix; for a monochromatic word take one arm to be the vacuous two-vertex path. Their outside vertex sets are complementary, proving (5). In the absence of any such witness, \(\mathcal R^\varepsilon_{uv}\) and the complement image \(\{A\setminus T:T\in\mathcal R^\varepsilon_{vu}\}\) are disjoint subsets of \(2^A\). Since complementation is a bijection, their cardinalities sum to at most \(2^{|A|}=2^{n-2}\). \(\square\)

**Comparison with the cube.** In the free-matroid cube automaton, NORI1 is equivalent to a complementary pair inside one rooted color-zero reachable family \(R_x\subseteq2^{[n]}\); failure imposes \(|R_x|\le2^{n-1}\) for every root. In the boundary system the same Boolean-complement obstruction acts *between* the two opposite-terminal families \(\mathcal R^\varepsilon_{uv}\) and \(\mathcal R^\varepsilon_{vu}\). The shared proposed proof principle is therefore a **complementary reachable-flat intersection theorem** for compatible monochromatic arms, rather than an unrestricted short-cocircuit intersection theorem. The counting bounds are necessary conditions for failure, not proofs that failure is impossible.

### Global antipodal graphic-flat covers and rainbow spanning-forest chambers

The preceding four-sector theorem describes one monochromatic component and its opposite-colored deck image. The following characterization instead controls the **entire partition of the covering graph into monochromatic components at once**. Its hypotheses and conclusions are intrinsic to a graphic matroid, an edge-free involutive automorphism, and the corresponding partition matroid on deck edge orbits. It applies to both the cube and the ordered-pair cover of ordinary boundary 3-tournaments.

Let \(G=(V,E)\) be a finite connected graph with a fixed-point-free involutive automorphism \(\tau\) acting freely on edges, and let \(M=M(G)\) be its graphic cycle matroid. For a partition \(\Pi\) of \(V\) into nonempty parts, define its graphic flat
\[
\boxed{
F_\Pi=\{uv\in E:u,v\text{ lie in the same part of }\Pi\}.
}
\tag{1}
\]
This is a flat of \(M\); its rank is \(r_M(F_\Pi)=|V|-|\Pi|\). The deck image \(\tau F_\Pi\) is the flat for the partition \(\tau\Pi\).

Call a forest \(T\subseteq F_\Pi\) **orbit-rainbow** if it contains at most one element from each two-element edge orbit \(\{e,\tau e\}\). Call it a **spanning forest of \(\Pi\)** if the connected components of \((V,T)\) are precisely the parts of \(\Pi\).

#### 1. Global flat-cover characterization

**Theorem 1 (antipodal flat-cover realization).** The partition \(\Pi\) is the partition of all vertices into color-zero connected components of some deck-odd edge coloring \(c:E(G)\to\mathbb F_2\) if and only if both conditions hold:
\[
\boxed{F_\Pi\cup\tau F_\Pi=E(G),}
\tag{2}
\]
and
\[
\boxed{\text{there exists an orbit-rainbow spanning forest }T
\text{ of }\Pi.}
\tag{3}
\]
Equivalently, with \(P_\tau\) the orbit partition matroid on \(E\),
\[
\boxed{
\max\{|T|:T\subseteq F_\Pi,\ 
T\in\mathcal I(M)\cap\mathcal I(P_\tau)\}
=r_M(F_\Pi)=|V|-|\Pi|.
}
\tag{4}
\]

*Proof.* Suppose \(c\) is deck-odd with red component partition \(\Pi\). Choose a spanning forest \(T\) in the red-edge subgraph. Every red edge has both endpoints in the same red component, so it belongs to \(F_\Pi\). The deck image of every blue edge is red and therefore lies in \(F_\Pi\), so every blue edge lies in \(\tau F_\Pi\). Thus \(E=F_\Pi\cup\tau F_\Pi\). The red forest \(T\) is independent in \(M\) and cannot contain both members of a deck edge orbit, since their colors are opposite; it spans all parts of \(\Pi\), proving (3).

Conversely, suppose (2) and (3). For each edge orbit \(\{e,\tau e\}\), at least one member belongs to \(F_\Pi\). If the orbit meets \(T\), declare its unique tree edge red and its mate blue. Otherwise select any member of the orbit lying in \(F_\Pi\) to be red, and its mate blue. These prescriptions are consistent because \(T\) is orbit-rainbow. They define a deck-odd coloring in which **every red edge lies in** \(F_\Pi\) and **every tree edge lies among the red edges**. Therefore no red edge joins two different parts of \(\Pi\), while \(T\) red-connects each part. The red component partition is \(\Pi\). \(\square\)

**Corollary 2 (all-component cut separation).** If \(\Pi\) is realizable, no graph edge simultaneously crosses a part boundary of \(\Pi\) and the corresponding boundary of \(\tau\Pi\). In other words, for every \(e=uv\),
\[
\boxed{
u\not\sim_\Pi v\ \Longrightarrow\ \tau u\sim_\Pi\tau v.
}
\tag{5}
\]
Here \(\sim_\Pi\) means belonging to the same part. For a specified red component \(R\in\Pi\), this implies the disjoint cocycles \(\delta(R)\cap\tau\delta(R)=\varnothing\) of the preceding Subsection.

*Proof.* Equation (2) says every edge is internal to \(\Pi\) or internal to \(\tau\Pi\). The two formulations are equivalent. If an edge leaves \(R\), it crosses \(\Pi\), so its deck image is internal to \(\Pi\), and cannot leave the corresponding deck image component. \(\square\)

This is stronger organizational information than imposing antipodal boundary separation on one red component at a time: it specifies a pair of **graphic-matroid flats that cover all covering edges simultaneously**.

#### 2. A global matroid-intersection cut test

**Theorem 3 (refinement-partition criterion).** Given a vertex partition \(\Pi\), the orbit-rainbow forest condition (3) is equivalent to the following inequalities. For every partition \(\mathcal Q\) of \(V\) that refines \(\Pi\),
\[
\boxed{
\#\bigl\{\{e,\tau e\}:
e\in F_\Pi\text{ joins distinct parts of }\mathcal Q\bigr\}
\ge |\mathcal Q|-|\Pi|.
}
\tag{6}
\]
Thus a proposed component partition is realizable precisely when its two antipodal graphic flats cover \(E\) and all inequalities (6) hold.

*Proof.* If an orbit-rainbow spanning forest \(T\) exists, then contracting each part of \(\mathcal Q\) within its containing \(\Pi\)-part requires at least \(|\mathcal Q|-|\Pi|\) forest edges crossing \(\mathcal Q\). Those forest edges belong to different deck orbits, proving (6).

For sufficiency, apply the matroid-intersection min–max theorem to the restrictions of \(M\) and \(P_\tau\) to \(F_\Pi\). For any \(A\subseteq F_\Pi\), let \(\mathcal Q\) be the partition of \(V\) into connected components of \((V,A)\). It refines \(\Pi\), with
\[
r_M(A)=|V|-|\mathcal Q|,\quad
r_M(F_\Pi)=|V|-|\Pi|.
\]
Every edge of \(F_\Pi\) crossing \(\mathcal Q\) lies in \(F_\Pi\setminus A\). Thus (6) gives
\[
r_{P_\tau}(F_\Pi\setminus A)
\ge|\mathcal Q|-|\Pi|
=r_M(F_\Pi)-r_M(A).
\]
This is the matroid-intersection min–max criterion for a common independent subset of \(F_\Pi\) of size \(r_M(F_\Pi)\). Such a common independent set is the required orbit-rainbow spanning forest of \(\Pi\). \(\square\)

#### 3. Boolean chambers of compatible colorings

For fixed \(\Pi\) satisfying (2) and any orbit-rainbow spanning forest \(T\) of \(\Pi\), let
\[
\mathcal O_{\rm amb}(\Pi)
=\{\{e,\tau e\}: e,\tau e\in F_\Pi\}
\tag{7}
\]
be the set of **ambiguous edge orbits**, whose two members are both internal to red components. Let \(\mathcal O(T)\) be the edge orbits represented by \(T\).

**Proposition 4 (basis chambers).** The family of all deck-odd colorings in which \(T\) is red and no red edge leaves a part of \(\Pi\) is an affine Boolean cube of dimension
\[
\boxed{
|\mathcal O_{\rm amb}(\Pi)\setminus\mathcal O(T)|.
}
\tag{8}
\]
In every such coloring, each edge in \(F_\Pi\setminus\tau F_\Pi\) is **forced red**, each edge in \(\tau F_\Pi\setminus F_\Pi\) is **forced blue**, and the remaining choices occur independently on the ambiguous orbits not constrained by \(T\). Every compatible coloring with red component partition \(\Pi\) belongs to at least one of these spanning-forest chambers.

*Proof.* For a deck orbit with only one member in \(F_\Pi\), that member must be red so red edges cannot leave the components; the other member is blue. For an orbit with both members in \(F_\Pi\), either orientation is permitted unless the orbit meets \(T\), in which case its tree member is forced red. The choices on distinct unconstrained orbits are independent. Each resulting coloring contains \(T\) and has red edges only in \(F_\Pi\), so its red components are the parts of \(\Pi\). Conversely, any coloring giving \(\Pi\) has a red spanning forest \(T\), belongs to the associated chamber, and meets the stated conditions. \(\square\)

**Corollary 5 (a forced-edge geodesic certificate).** In the antipodal cube, suppose a realizable partition \(\Pi\) has a monochromatic antipodal geodesic using only edges from the forced-red set \(F_\Pi\setminus\tau F_\Pi\). Then **every** deck-odd coloring with red component partition \(\Pi\) satisfies NORI1.

*Proof.* The edges of such a geodesic are red by Proposition 4 for every compatible coloring, so the path is a monochromatic full antipodal geodesic. \(\square\)

The certificate is sufficient, not asserted to hold in every realizable partition. In particular, when \(F_\Pi=E\), the forced-red set is empty, and the certificate does not apply.

#### 4. Relationship to both canonical pointed matroids

In the cube, the graphic matroid is \(M(Q_n)\) and \(\tau\) is coordinate complementation. In the ordinary boundary-tournament covering, use \(M(S(K_n))\), whose edge states are reversal-paired ordered triples. Both have the same full component-partition characterization (2), (4) and the refinement cut test (6).

This theorem coordinates *all* monochromatic components across the two sheets of their regular covering, beyond the Eulerian zero-turn contact graph and the local four-sector pair for a single component. It also exposes the coloring choices not fixed by component connectivity as independent ambiguous edge-orbit variables. Nevertheless, it does not alone prove the deterministic spanning-path targets. In the cube, geodesicity must still be certified by a red resource-simple antipodal path in at least one component; in the boundary model, the original-vertex graphic-resource independence and forward ordered-pair coherence remain additional requirements. The global flat-cover constraints give an intrinsic common class within which a future geodesic or one-turn selector theorem must operate.

#### 5. Global cycle-rank conservation

The flat-cover theorem gives a common partition-based representation; regularity imposes an additional **global graphic-matroid nullity budget** that cannot be detected inside a single component.

**Theorem 6 (fixed red cycle-rank budget).** Let \(G\) be a finite \(d\)-regular graph on \(N\) vertices with a free vertex-and-edge involution \(\tau\), and let \(c\) be any deck-odd edge coloring. Let \(\Pi_c\) be its partition into color-zero connected components, including isolated vertices, with \(\kappa=|\Pi_c|\). Then the nullity of its color-zero edge set in the graphic matroid \(M(G)\) is
\[
\boxed{
\dim Z(G_{\rm red})
=|E_{\rm red}|-r_M(E_{\rm red})
=\frac{(d-4)N}{4}+\kappa.
}
\tag{9}
\]
In particular,
\[
\boxed{
\sum_{R\in\Pi_c}
\left(|E_{\rm red}(R)|-|R|+1\right)
=\frac{(d-4)N}{4}+\kappa.
}
\tag{10}
\]

*Proof.* The covering graph has \(dN/2\) edges. Since every antipodal edge orbit consists of one red and one blue edge, \(|E_{\rm red}|=dN/4\), independently of the coloring. The graphic rank of the red subgraph is \(N-\kappa\), because its connected components are the parts of \(\Pi_c\), including isolated vertices. Subtracting rank from edge count proves (9); summing the component cyclomatic numbers proves (10). \(\square\)

**Corollary 7 (the two canonical budgets).** For an antipodally odd edge coloring of \(Q_n\), whose \(2^n\) vertices have degree \(n\),
\[
\boxed{\dim Z((Q_n)_{\rm red})=(n-4)2^{n-2}+\kappa.}
\tag{11}
\]
For an ordinary reversal-odd boundary coloring on the ordered-pair covering graph \(S(K_n)\), which has \(N=n(n-1)\) vertices and degree \(d=2(n-2)\),
\[
\boxed{
\dim Z((S(K_n))_{\rm red})
=\frac{n(n-1)(n-4)}2+\kappa.
}
\tag{12}
\]

The budget is global: it does **not** assert that every self-antipodal red component contains a red circuit. Research-note constructions in Q4–Q6 exhibit self-antipodal components that are trees, including one with a two-unit geodesicity defect. Such tree components contribute zero to (10), forcing the total cycle-rank budget to reside elsewhere. This is a rigorous indication that a successful matroid closure argument may need to compare distinct monochromatic components and their graphic cycles through the shared antipodal flat-cover constraints, rather than optimizing only one port-loop component.
