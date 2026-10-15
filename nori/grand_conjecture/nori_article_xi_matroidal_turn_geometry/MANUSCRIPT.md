# Article XI — Matroidal Turn Geometry and Rainbow-Circuit Exchange

## Antipodal Turn Quotients and Rainbow-Circuit Geometry

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

## Polarized Matroid Galleries and Port-Cocircuit Geometry

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

This Subsection assembles the Article XI exploration of generalized binary matroid intersection properties and the comparison with reversal-odd boundary 3-tournaments. The full-strength goal is an abstract theorem implying **both** unrestricted monochromatic NORI1 and the boundary one-change Hamiltonian conjecture: a vertex-simple tight path through all original vertices, with at most one change among its consecutive triple colors. A long monochromatic boundary tight path is only an established weaker consequence. It separates established facts from proposed conjectures; none of the proposed universal intersection implications below has been proved.

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
original vertices. Thus (5) would establish NORI1 and a weaker monochromatic boundary square-root theorem, not the full one-change Hamiltonian boundary conjecture; the latter needs rank \(n-1\) and a one-switch tight triple-color word. This is a *conditional implication*, not a proof of (5).

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

##### Spectral lower bound for unrestricted boundary switches

The signed adjacency spectrum of the reversal quotient, established in the preceding spectral Subsection, gives a lower as well as an upper bound on switched turns. Let \(N=n(n-1)(n-2)/2\), \(E=N(n-3)\), and \(S_b\) be the switch support of any reversal-odd triple coloring.

**Theorem 1 (two-sided hereditary density).** For every \(n\ge6\),
\[
\boxed{\frac{n-4}{4(n-3)}\le \frac{|S_b|}{E}\le\frac{3n-8}{4(n-3)}.}
\]
The same inequalities apply on every \(m\)-symbol restriction for \(m\ge6\).

*Proof.* The self-adjoint signed adjacency matrix \(A\) obeys \(-(n-2)I\preceq A\preceq(n-2)I\), by the previously established annihilating polynomial. For a reversal-odd sign vector \(x\in\{\pm1\}^{N}\),
\[
\tfrac12x^\top Ax=E-2|S_b|,\qquad x^\top x=N.
\]
The two Rayleigh bounds give \(E/2-(n-2)N/4\le |S_b|\le E/2+(n-2)N/4\). Substitute \(E=(n-3)N\). Restriction retains reversal oddness. QED.

**Theorem 2 (cyclic-orientation construction).** For every \(n\ge5\), there is a reversal-odd boundary coloring with switched-turn fraction \(1/3\).

*Proof.* Fix a cyclic ordering of the symbols, and color an ordered triple by its clockwise orientation. Reversing the two outside entries complements its color. Two overlapping triples \(abc\) and \(bcd\) disagree precisely when the distinct exterior symbols \(a,d\) lie on opposite arcs of the circle from \(b\) to \(c\). Among the relative circular configurations of four distinct labeled points this occurs with probability \(1/3\). Uniformity of the directed overlapping turns therefore gives switched fraction \(1/3\). QED.

**Theorem 3 (sharp cube comparison).** The minimum switch fraction over all legal antipodally odd cube-edge colorings is \(1/n\), whereas the minimum boundary fraction belongs to \([\, (n-4)/(4(n-3)),\,1/3\,]\) for \(n\ge6\).

*Proof.* Every projective dimension-simple Petrie cycle has an odd, hence positive, number of switches. All such cycles have \(n\) turns and all quotient turns occur with equal multiplicity, so cube switch fraction is at least \(1/n\). To attain this, choose distinct directions \(a,b\) and set \(c_a(x)=x_b\), \(c_d(x)=x_a\) for every \(d\ne a\). This coloring is well-defined on undirected edges and is antipodally odd. At a projective cube vertex, the number of bichromatic turns is \(n-1\) when \(x_a\ne x_b\), and zero otherwise. Half of the projective vertices satisfy the inequality, so the switch support has size \((n-1)2^{n-2}\), while the entire quotient turn graph has \(n(n-1)2^{n-2}\) edges. Their ratio is \(1/n\). The boundary inequalities are Theorems 1-2. QED.

**Corollary (first-moment barrier).** A uniformly random Hamilton order of any reversal-odd boundary tournament has expected switch count at least \((n-4)/4\), since it contains \(n-3\) overlap transitions sampled uniformly across quotient turns. This applies even to globally support-minimizing odd colorings, and grows linearly with \(n\). Thus a proof of the one-switch conjecture must exploit favorable-path structure beyond the global first moment or cographic support minimization.

The contrast is intrinsic to the different covering incidence graphs: their common odd cohomology description does not imply comparable minimum representative densities.

## Graphic and Boundary-Tournament Exchange Geometry

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

#### Complete local-exchange generation for signed Hamiltonian windows

Keep \(n\ge5\), and write \(s_\pi\in\mathbb Z^{\mathcal T_n}\) for the signed triple-window incidence vector of a Hamiltonian word \(\pi\). Let
\[
E_n^\pm=\operatorname{span}_{\mathbb Z}
\{s_\pi-s_{\pi'}:\ \pi'\text{ is obtained from }\pi
\text{ by one adjacent transposition}\}.
\tag{23}
\]

**Theorem 6 (all signed adjacent-swap differences generate the parity lattice).** For every \(n\ge5\),
\[
\boxed{
E_n^\pm=
\left\{z\in\mathbb Z^{\mathcal T_n}:
\sum_t z_t\equiv0\pmod2\right\}.
}
\tag{24}
\]
Equivalently, the integer matrix of all signed adjacent-swap differences has full rational column rank and a Smith normal form with \(|\mathcal T_n|-1\) unit factors and one factor two. This holds in both odd and even orders.

*Proof.* Adjacent transpositions generate the connected Cayley graph of the permutation group, so \(E_n^\pm\) also equals the lattice of all pairwise differences \(s_\pi-s_\sigma\).

First classify annihilators over fields. Let \(z\) be a linear functional vanishing on these differences. Then \(\langle z,s_\pi\rangle=K\) is constant over all Hamiltonian words \(\pi\). Comparing terminal adjacent swaps gives the same four-cycle relation (S) used in Theorem 2.

For a field of characteristic different from two, Theorem 2's local-potential argument turns any solution of (S) into an oriented graph cut
\[
z_{uab}=v_{\{a,b\}}-v_{\{u,a\}}
\]
on \(F=L(K_n)\). Its Hamiltonian sum is the potential of the final unordered edge minus that of the first. Since any ordered pair of disjoint original \(K_n\)-edges occurs as these endpoints, constant value \(K\) forces all potentials to agree (compare through a third edge disjoint from any intersecting pair), giving \(z=0\). Thus the swap-difference matrix has full rank over every field of characteristic different from two, including \(\mathbb Q\).

In characteristic two, the unsigned four-cycle classification from Theorem 1 applies: every solution of (S) is
\[
z_{abc}=u_{\{a,b\}}+u_{\{b,c\}}+\zeta.
\]
Its Hamiltonian evaluation is
\[
u_{\{v_1,v_2\}}+u_{\{v_{n-1},v_n\}}+(n-2)\zeta=K.
\]
Constancy over arbitrary disjoint endpoint pairs again forces \(u\) to be constant. Hence the only annihilating weightings are the constant triple-orbit cochains \(z_{abc}=\zeta\), a one-dimensional space over \(\mathbb F_2\). Therefore the integral cokernel
\[
C=\mathbb Z^{\mathcal T_n}/E_n^\pm
\]
is finite with no odd-primary torsion, and \(\dim_{\mathbb F_2}(C/2C)=1\). It is a nonzero cyclic 2-group. Its unique nonzero modular annihilator is the all-one cochain, which evaluates to one on every coordinate vector, so every standard coordinate class \(e_t\) generates \(C\).

The symmetric group acts on \(C\) by relabeling oriented triples. Every transposition is conjugate, while automorphisms of a cyclic group commute. A transposition of two labels outside a fixed triple fixes its coordinate generator, so it acts trivially; hence every transposition acts trivially. But transposing the first and last labels of the fixed triple reverses its orientation and sends \(e_t\) to \(-e_t\). Thus \(2e_t=0\), forcing \(C\cong\mathbb Z/2\mathbb Z\).

Every signed Hamiltonian incidence vector has coordinate sum congruent to \(n-2\pmod2\), independent of its orientation signs. Accordingly every difference \(s_\pi-s_\sigma\) has even coordinate sum. The even-sum lattice has index two in \(\mathbb Z^{\mathcal T_n}\), as does \(E_n^\pm\); inclusion implies equality and proves (24). \(\square\)

**Corollary 7 (difference-only versus full signed path lattices).** For \(n\ge5\),
\[
\boxed{
\Lambda_n^\pm/E_n^\pm\cong
\begin{cases}
\mathbb Z/2\mathbb Z,&n\text{ odd},\\
0,&n\text{ even}.
\end{cases}}
\tag{25}
\]
Thus in even orders the entire signed Hamiltonian path incidence lattice is generated by adjacent-swap differences. In odd orders a single signed Hamiltonian path vector supplies the remaining parity-odd class.

*Proof.* Combine Theorem 6 with Theorem 2 and note that the coordinate sum of each signed Hamiltonian incidence vector has parity \(n-2\). \(\square\)

**Interpretation for the matroidal unification project.** The signed Hamiltonian *resource-incidence* exchange system is integrally complete up to a single unavoidable parity class; it has no residual affine resource charge analogous to the \(n-1\)-dimensional charge space of cube geodesic six-turn exchanges. Yet this does not imply low color cost or long monochromatic tight paths. Differences between signed Hamiltonian vectors are formal integer relations, and their all-dimensional generation need not yield a sequence of legal, monotone-cost, resource-independent galleries. The remaining common problem is nonlinear **accessibility and positivity**, not generation of the integral incidence lattice.

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

### Boundary tournaments, antipodal graphic-flat matroids, and resource-basis packing

We verify that *every* ordinary reversal-odd boundary 3-tournament produces the antipodal graphic-flat and edge-orbit partition-matroid structure of Article XI. We also establish a distinction between the **basis-exchange quotient** and its covering graph, and reduce the spanning one-turn conjecture to the existence of a two-arm basis of the **separate** original-vertex graphic matroid.

#### 1. Cover and matroid construction

For \(n\ge4\), define \(\mathscr S_n\) to have vertices \((a,b)\), \(a\ne b\), and undirected edges
\[
\boxed{\{(a,b),(b,c)\}\quad(a,b,c\text{ distinct}).}
\tag{1}
\]
Each covering edge is indexed by its ordered triple \((a,b,c)\). Reversal \(\tau(a,b)=(b,a)\) exchanges the edges of \((a,b,c)\) and \((c,b,a)\). Thus
\[
\boxed{\mathscr S_n/\tau\cong L(K_n)=\Gamma(U_{2,n}),}
\tag{2}
\]
with a connected regular two-cover \(\mathscr S_n\to L(K_n)\). The cover is \(2(n-2)\)-regular, has \(N=n(n-1)\) vertices, and has \(N(n-2)\) edges.

Write \(\mathsf G_n=M(\mathscr S_n)\) for its graphic cycle matroid. Let \(\mathsf P_n\) be the partition matroid on covering edges with one two-element part \(\{e,\tau e\}\) per triple reversal-orbit, each of capacity one. Its rank is \(N(n-2)/2\).

**Theorem 1 (unrestricted boundary representation).** Reversal-odd boundary 3-tournaments are in bijection with the bases \(B\) of \(\mathsf P_n\): their zero-colored covering edges. For any such \(B\), let \(\Pi_B\) be the partition into connected components of \((V(\mathscr S_n),B)\) and let \(F_B=\operatorname{cl}_{\mathsf G_n}(B)\). Then
\[
\boxed{
F_B\cup\tau F_B=E(\mathscr S_n),\qquad
r_{\mathsf G_n}(B)=N-|\Pi_B|,
}
\tag{3}
\]
and
\[
\boxed{
|B|-r_{\mathsf G_n}(B)
=\frac{n(n-1)(n-4)}2+|\Pi_B|.
}
\tag{4}
\]
Conversely, a partition \(\Pi\) is the full zero-colored component partition of some reversal-odd boundary coloring if and only if its graphic flat \(F_\Pi\) covers \(E(\mathscr S_n)\) together with \(\tau F_\Pi\), and \(F_\Pi\) contains an orbit-rainbow spanning forest. By the graphic–partition matroid intersection theorem, the latter is equivalent to the refinement-partition cut inequalities already proved in the global flat-cover Subsection.

*Proof.* Each reversal-odd coloring selects one edge from every reversal-orbit as zero-colored; that is a basis of the orbit partition matroid, and every such basis gives a coloring. Every zero edge lies in its connected component, and the reversal of any one-colored edge is a zero edge, which proves the flat covering. The graphic rank is \(N\) minus the number of connected components, giving (3) and (4). The converse is the all-cover flat and rainbow-forest characterization from the preceding Subsection, applied to \(\mathscr S_n\). \(\square\)

It follows that **all** the shared antipodal cut, Eulerian contact-graph, global even-edge and graphic-flat results of Article XI apply to every boundary coloring. The pointed binary matroid from the induced cover of the turn graph \(L(L(K_n))\) is a second, compatible construction. No special coloring subclass is needed.

#### 2. The covering graph itself is not generally a basis graph

**Theorem 2 (basis-graph obstruction in unbounded orders).** The graph \(\mathscr S_n\) is not the basis-exchange graph of any matroid when \(n=4\) or \(n\ge8\).

*Proof.* Choose distinct original symbols \(a,b,c\) and vertices \(u=(a,b)\), \(v=(a,c)\) in \(\mathscr S_n\). They are not adjacent, and their common neighbors are
\[
\boxed{N(u)\cap N(v)=\{(x,a):x\notin\{a,b,c\}\}.}
\tag{5}
\]
Thus these two vertices are at distance two and possess \(n-3\) common neighbors. In every matroid basis graph, two vertices at distance two correspond to bases differing by two elements in each direction. All common neighbors exchange one of two elements for one of two others, giving at most four possibilities. Symmetric basis exchange supplies at least two distinct common neighbors. The number \(n-3\) violates the lower bound for \(n=4\) and the upper bound for \(n\ge8\). \(\square\)

Therefore the relevant **basis graph** is the quotient \(\Gamma(U_{2,n})=L(K_n)\); the covering graph has its own *graphic matroid*. Identifying these two layers would lead to an invalid universal basis-exchange argument.

#### 3. A second graphic matroid supplies the Hamilton resource constraint

The original-vertex resource matroid is
\[
\boxed{\mathsf R_n=M(K_n),}
\tag{6}
\]
distinct from \(\mathsf G_n=M(\mathscr S_n)\). A forward tight word \(P=(v_1,\ldots,v_k)\) is a directed-overlap path \((v_1,v_2)\to(v_2,v_3)\to\cdots\) in the covering graph, with resource edges
\[
E(P)=\{\{v_i,v_{i+1}\}:1\le i<k\}.
\tag{7}
\]
Starting from one original edge, requiring each appended resource edge to increase graphic rank in \(\mathsf R_n\) forces every appended original vertex to be new. An undirected same-color path in \(\mathscr S_n\) need not be a legal forward tight path because it may switch the overlap direction and revisit original vertices. Thus covering-graph connectivity, even between reversal-related oriented pairs, does not alone produce the desired tournament path.

**Theorem 3 (opposite-terminal basis packing).** Let \(P,Q\) be vertex-simple \(\varepsilon\)-monochromatic forward tight paths for the same color, ending in ordered pairs \((u,v)\) and \((v,u)\) respectively. A two-vertex arm is allowed. Then
\[
\boxed{
E(P)\cup E(Q)\in\mathcal I(\mathsf R_n)
\iff
V(P)\cap V(Q)=\{u,v\}.
}
\tag{8}
\]
Consequently,
\[
\boxed{
\text{A spanning one-turn boundary tight path exists}
\iff
\exists\,u,v,\varepsilon,P,Q:
E(P)\cup E(Q)\in\mathcal B(\mathsf R_n).
}
\tag{9}
\]
In this formulation, graphic independence automatically enforces disjoint interiors and the Hamilton path degree bound.

*Proof.* Delete the shared last edge \(\{u,v\}\). The remaining edges of \(P\) form one path attached to \(u\), and those of \(Q\) another path attached to \(v\). If the paths have no common additional vertex, their union with \(\{u,v\}\) is a simple path, hence graphic-independent. If they meet at some other original vertex, choose the first common meeting point from the two rooted ends. The two initial subpaths from \(u\) and \(v\), together with \(\{u,v\}\), form a graph cycle; hence their union is graphic-dependent. This proves (8). If the independent union is a graphic basis, its simple path contains all \(n\) original vertices. Reverse \(Q\), which reverses all its triple colors under boundary oddness, and splice it to \(P\) at the terminal pair to obtain a spanning path with at most one color change. Conversely, split a spanning one-turn path at its switch, reverse its second arm and use the two same-colored arms. When the path is monochromatic, use a vacuous two-vertex arm and the full reversed path. \(\square\)

The criterion (9) is the natural **integral matroid basis-packing target**. The difficult part is finding the two forward, color-compatible arms; their families do not satisfy ordinary greedoid augmentation in general, as shown by earlier Article XI research-note counterexamples. Generic matroid intersection on the covering graph \(\mathsf G_n\) is therefore insufficient without the directed resource-language constraint.

#### 4. Why a cube-specific port-loop axiom must be excluded

The cube's pointed contact graph always has a port-parallel loop by the known existence of a monochromatic antipodal path. The corresponding loop property fails for boundary tournaments: on four original vertices, the reversal-odd coloring with representative mask \(\mathrm{0x555}\), indexed by increasing middle symbol and then lexicographic outer pair \(a<c\), has a red covering graph consisting of four disjoint oriented three-cycles, one on each three-element original-vertex subset. No component contains both \((a,b)\) and \((b,a)\). The contact graph is \(K_4\) with four parallel copies of every edge. It is Eulerian, nonbipartite, even-sized, and loop-free. Hence its shortest unrestricted port intersection is four, rather than two. This example and an exhaustive enumeration of the 4096 order-four colorings are retained as a research note.

The **shared** matroid class is therefore the antipodal graph-cover, graphic-flat, orbit-partition, and pointed-binary construction. The **distinct admissible selectors** are (i) a displacement-minimal lifted fundamental circuit for the cube and (ii) an opposite-terminal union that is a basis of \(\mathsf R_n=M(K_n)\) for boundary tournaments. A unification theorem must preserve this second level of independent resources rather than replacing it by port parallelism.

#### 5. A pulled-back original-resource matroid on covering transitions

Fix the initial ordered pair \((u,v)\). For each covering edge
\[
e_{abc}=\{(a,b),(b,c)\}\in E(\mathscr S_n),
\]
label its original resource by \(\lambda(e_{abc})=\{b,c\}\in E(K_n)\). This is well-defined because an undirected covering edge has a unique ordered-triple index. Define the parallel-extension pullback matroid
\[
\boxed{\mathsf N_{uv}=\lambda^*(M(K_n)/\{u,v\})}
\tag{10}
\]
on the same covering-transition ground set as \(\mathsf G_n=M(\mathscr S_n)\). Thus \(A\subseteq E(\mathscr S_n)\) is independent in \(\mathsf N_{uv}\) if the resource labels \(\lambda(A)\) are distinct and
\[
\{\{u,v\}\}\cup\lambda(A)\in\mathcal I(M(K_n)).
\tag{11}
\]

**Theorem 4 (resource independence of coherent forward words).** A coherent forward covering-state path starting at \((u,v)\) with no repeated covering edge decodes to an injective original-vertex word if and only if its edge set is independent in \(\mathsf N_{uv}\). When these conditions hold, its edge set is also independent in the covering graphic matroid \(\mathsf G_n\).

*Proof.* The initial original edge \(\{u,v\}\) followed by the labels of the successive forward covering edges is the entire original edge sequence of the decoded word. An injective word traces a graph path with pairwise distinct original resource labels, so (11) holds. Conversely, revisiting an original vertex yields a closed nonbacktracking segment, because consecutive triples use three distinct original vertices. That segment either repeats a resource edge or contains a graph cycle, contradicting the label distinctness or original graphic independence in (11). For an injective word, its oriented-pair covering states are distinct, so the covering edges form a graph path and are independent in \(\mathsf G_n\). \(\square\)

**Proposition 5 (plain matroid intersection does not enforce coherent paths).** On five original vertices there exists a reversal-odd boundary coloring whose red covering edge set contains a common independent set of size \(n-2=3\) in \(\mathsf G_5\) and \(\mathsf N_{01}\), yet no red or blue spanning tight path exists.

*Proof.* Use the representative bit mask \(\mathrm{0x3ed25058}\), with representatives ordered by increasing middle vertex followed by increasing outer pair \(a<c\). The full \(5!=120\) word enumeration in the five-cycle sharpness Subsection establishes that all spanning words have at least one turn, so no monochromatic spanning word exists. Nevertheless, the three covering edges indexed by
\[
\boxed{(0,1,3),\ (0,1,4),\ (0,2,3)}
\tag{12}
\]
are red. They form a covering graph forest (two share only state \((0,1)\), and the third is disjoint). Their original resource labels are \(\{1,3\},\{1,4\},\{2,3\}\). Adding the initial resource \(\{0,1\}\) gives a spanning tree of \(K_5\). Hence the three covering edges are independent in both matroids, attaining resource rank \(3\), but they are not a single forward coherent state path. \(\square\)

This yields two graphic-derived matroids on the same boundary covering-edge set, plus the antipodal orbit partition matroid that parametrizes all reversal-odd colorings. Theorem 4 proves resource independence is an ordinary matroid constraint on directed forward paths. Proposition 5 shows a common independent set of full resource rank need not be a forward path: its **directed adjacency and route connectedness** must be retained as a separate admissibility condition. Thus a matroid-based spanning one-turn proof needs an exchange principle compatible with the coherent directed path language, not plain matroid intersection alone.

#### 6. Near-complete resource support in every boundary coloring

There is a strong universal abundance theorem for the original-resource labels of a **fixed** color, independent of any randomization or exchange choices.

Fix one color \(\varepsilon\), and let \(B_\varepsilon\) consist of covering edges of that color. Using the resource labeling \(\lambda(e_{abc})=\{b,c\}\), put
\[
\boxed{
\Lambda_\varepsilon=\lambda(B_\varepsilon)
\subseteq E(K_n).
}
\tag{13}
\]

**Theorem 6 (missing resources form a matching).** For every ordinary reversal-odd boundary 3-tournament on \(n\ge3\) vertices, and for each \(\varepsilon\in\{0,1\}\),
\[
\boxed{
E(K_n)\setminus\Lambda_\varepsilon
\text{ is a matching}.
}
\tag{14}
\]
In particular,
\[
\boxed{
|\Lambda_\varepsilon|\ge\binom n2-\left\lfloor\frac n2\right\rfloor,
\qquad r_{M(K_n)}(\Lambda_\varepsilon)=n-1.
}
\tag{15}
\]
Thus every fixed color appears on a collection of forward covering transitions whose **original-resource labels already span the full graphic resource matroid**.

*Proof.* For each middle vertex \(b\), restrict the boundary coloring to the ordered triples \((a,b,c)\) with \(a,c\ne b\). Reversal oddness makes the color-\(\varepsilon\) triples into the arcs of a tournament \(T_b^\varepsilon\) on \(V\setminus\{b\}\), oriented \(a\to c\) when \(b(a,b,c)=\varepsilon\). The resource edge \(\{b,c\}\) occurs as \(\lambda(e_{abc})\) for some color-\(\varepsilon\) triple with middle \(b\) if and only if \(c\) has positive indegree in \(T_b^\varepsilon\).

Suppose two missing resource edges \(\{b,c\}\) and \(\{b,d\}\) share the same vertex \(b\). Their absence implies both \(c\) and \(d\) have indegree zero in \(T_b^\varepsilon\). But a tournament has at most one vertex of indegree zero, because the edge between any two proposed sources must enter one of them. This is impossible. Hence the missing-edge graph has maximum degree at most one, proving (14). The stated cardinality bound follows. The complement of a matching in \(K_n\) is connected for \(n\ge3\); its graphic rank is \(n-1\). \(\square\)

**Corollary 7 (two forced outgoing fans).** If a resource edge \(\{b,c\}\) is absent from \(\Lambda_\varepsilon\), then for every \(a\notin\{b,c\}\),
\[
\boxed{
b(c,b,a)=\varepsilon,\qquad b(b,c,a)=\varepsilon.
}
\tag{16}
\]
Equivalently, both ordered-pair states \((c,b)\) and \((b,c)\) have all \(n-2\) possible **outgoing forward transitions** of color \(\varepsilon\).

*Proof.* Absence of resource \(\{b,c\}\) means each triple \((a,b,c)\) and \((a,c,b)\) has the opposite color \(1-\varepsilon\). Reverse both triples and apply reversal oddness. \(\square\)

The matching bound is attainable: the missing resource sets for the five-vertex mask \(\mathrm{0x3ed25058}\) in Proposition 5 are the two disjoint edges \(\{1,2\}\) and \(\{3,4\}\). More generally the independent local tournament choices at each middle vertex permit any prescribed matching as the missing color-\(\varepsilon\) resource support for \(n\ge4\): make the designated partner a zero-indegree source at each matched vertex, and choose source-free local tournaments at unmatched vertices.

This theorem clarifies why ordinary graphic rank arguments on \(\mathsf R_n\) alone cannot settle the spanning conjecture. Every color already has an almost-complete **resource support graph**, and therefore abundant spanning trees. The obstruction must occur in the directed overlap constraints coupling **successive** resource edges, not in the ability to select independent resources individually. The forced outgoing fans (16) may supply useful local rerouting operations for an eventual rank-preserving opposite-terminal exchange theorem.

#### 7. Missing resource edges are forced color-change gates

The outgoing-fan phenomenon in Corollary 7 has a dual incoming constraint. Let \(e=\{b,c\}\) be an original resource edge absent from the color-\(\varepsilon\) support \(\Lambda_\varepsilon\).

**Theorem 8 (forced phase gate at a missing resource).** For every \(a\notin\{b,c\}\),
\[
\boxed{
\begin{aligned}
b(a,b,c)&=1-\varepsilon,&
b(b,c,a)&=\varepsilon,\\
b(a,c,b)&=1-\varepsilon,&
b(c,b,a)&=\varepsilon.
\end{aligned}}
\tag{17}
\]
Consequently **every** coherent forward tight path that passes through either ordered-pair state \((b,c)\) or \((c,b)\) as an interior state makes a color change from \(1-\varepsilon\) to \(\varepsilon\) at that state. All incoming transitions to either state have color \(1-\varepsilon\), and all outgoing transitions have color \(\varepsilon\).

*Proof.* The first and third displayed triples have resource label \(\{b,c\}\) in the color-\(\varepsilon\) resource map. Since this label is absent, both triples have color \(1-\varepsilon\). The second and fourth triples are their reversal pairs, so reversal oddness forces color \(\varepsilon\). The incoming and outgoing transition description follows from the ordered-pair covering graph. \(\square\)

**Corollary 9 (forced-gate packing restriction).** Let \(F_\varepsilon=E(K_n)\setminus\Lambda_\varepsilon\), a matching by Theorem 6. In any spanning tight word with at most one internal color change, there is at most one consecutive original pair from \(F_\varepsilon\) occurring as an interior ordered-pair state; if such a pair occurs, the unique change is from \(1-\varepsilon\) to \(\varepsilon\) at that pair. A monochromatic spanning tight word cannot contain any missing-resource pair as an interior state. The endpoints of the word may contain such a pair without triggering an internal comparison.

Theorem 8 converts a missing resource into a **deterministic two-color switching interface**. In particular, instead of treating missing labels solely as rank defects, a proposed spanning one-turn proof may use one as its intended seam and seek two independent monochromatic arms attaching on opposite sides. The missing edges themselves form a matching, so there can be no overlapping gate constraints based at the same original vertex. This is a structural lead, not a completed spanning one-turn theorem.

#### 8. A common full-rank resource-cocircuit axiom for cube and boundary models

The resource-support theorem has a direct counterpart in NORI1 and therefore supplies another **intrinsic hypothesis shared by the two canonical models**.

Let \(\mathsf R\) denote the original-resource matroid of a polarized exchange-gallery system and \(\Lambda_\varepsilon\) the set of resource labels occurring on primitive states or forward transitions of color \(\varepsilon\). Consider the matroid property
\[
\boxed{
r_{\mathsf R}(\Lambda_0)
=r_{\mathsf R}(\Lambda_1)
=r(\mathsf R).
}
\tag{18}
\]
Equivalently, **each color support meets every cocircuit of the original-resource matroid**. This equivalence is standard: a set spans a matroid if and only if it intersects every cocircuit.

**Theorem 10 (common cocircuit-hitting resource supports).** Both canonical Article XI models satisfy (18) for every permitted reversal-odd coloring, with the following refinements.

(a) For the antipodal \(n\)-cube, \(\mathsf R\) is the free matroid on the \(n\) coordinate directions. Each color occurs on precisely \(2^{n-2}\) edges of each coordinate direction, for \(n\ge2\). In particular, \(\Lambda_0=\Lambda_1=[n]\), and each color meets every singleton cocircuit.

(b) For the ordinary boundary 3-tournament, \(\mathsf R=M(K_n)\), and for every nonempty proper \(S\subset[n]\),
\[
\boxed{
|\Lambda_\varepsilon\cap\delta_{K_n}(S)|
\ge |S|(n-|S|)-\min(|S|,n-|S|).
}
\tag{19}
\]
Consequently the resource-support graph \(([n],\Lambda_\varepsilon)\) is \((n-2)\)-edge-connected for every \(n\ge3\), and it contains a Hamilton cycle whenever \(n\ge4\).

*Proof.* For (a), the \(2^{n-1}\) cube edges of any coordinate direction split into \(2^{n-2}\) antipodal edge pairs, and reversal oddness selects one edge of each color in each pair. For (b), Theorem 6 says the missing resource-edge graph is a matching. At most \(\min(|S|,n-|S|)\) edges of that matching cross a cut \(\delta(S)\), proving (19). Its minimum over nontrivial \(S\) is at least \(n-2\) for \(n\ge3\), giving the edge-connectivity bound. Since the support graph has minimum degree at least \(n-2\ge n/2\) for \(n\ge4\), Dirac's Hamilton-cycle theorem applies. \(\square\)

The common full-rank cocircuit-hitting condition (18) is a natural addition to the proposed abstract class of **polarized resource-exchange matroids**. It is an all-color, all-dimensional restriction stronger than merely saying that the uncolored gallery system admits every resource permutation. But it is still not a path selector: the five-vertex counterexample in Proposition 5 has almost-complete full-rank red resource support and even a Hamilton resource cycle, without any coherent monochromatic spanning tight path. A closure proof must exploit **how** these abundant resource labels are realized by adjacent colored covering transitions.

#### 9. Matroid base-packing abundance for each color

The cocircuit-hitting theorem also yields a quantitative **spanning-basis packing** result for the color-specific resource supports. This survives in arbitrarily large order and can be useful for future exchange arguments that must avoid a bounded set of resource labels.

**Theorem 11 (boundary spanning-tree packing).** For an ordinary reversal-odd boundary 3-tournament on \(n\ge4\) vertices, let \(B_\varepsilon\) be the colored covering edges and let \(\Lambda_\varepsilon=\lambda(B_\varepsilon)\). Then \(\Lambda_\varepsilon\) contains at least
\[
\boxed{k_n=\left\lfloor\frac{n-2}{2}\right\rfloor}
\tag{20}
\]
pairwise edge-disjoint spanning trees of \(K_n\). Equivalently, the pullback resource matroid
\[
\lambda^*M(K_n)
\]
on the covering-transition ground set contains \(k_n\) pairwise disjoint bases comprised entirely of color-\(\varepsilon\) transitions.

*Proof.* By Theorem 10(b), the resource-support graph \(([n],\Lambda_\varepsilon)\) is \((n-2)\)-edge-connected, hence \(2k_n\)-edge-connected. For every partition of its vertex set into \(t\ge2\) nonempty parts, each part has at least \(2k_n\) crossing incidences. Counting edges crossing between parts twice gives at least \(k_n t\ge k_n(t-1)\) such edges. The Nash-Williams–Tutte spanning-tree packing criterion therefore supplies \(k_n\) edge-disjoint spanning trees. For each tree edge choose one color-\(\varepsilon\) covering transition with that resource label. Since the trees have disjoint resource-edge sets, these choices give disjoint bases of the parallel-extension pullback matroid. \(\square\)

**Proposition 12 (cube analogue).** For the antipodally odd \(n\)-cube, \(n\ge2\), let \(\lambda\) label each colored cube edge by its coordinate direction and let \(\mathsf R\) be the free matroid on \([n]\). For either fixed color, the parallel-extension pullback \(\lambda^*\mathsf R\) on the cube-edge set contains
\[
\boxed{2^{n-2}}
\tag{21}
\]
pairwise disjoint full-rank bases, and no larger number is possible.

*Proof.* In each direction there are precisely \(2^{n-2}\) edges of each color, by Theorem 10(a). A basis of the parallel-extension free matroid chooses one edge in every direction. Pair the direction-\(i\) edges arbitrarily with the indices \(1,\ldots,2^{n-2}\); selecting the edges with the same index across all directions gives \(2^{n-2}\) disjoint bases. Conversely every such basis consumes one colored edge of each direction, and only \(2^{n-2}\) are available. \(\square\)

Hence **both canonical models have many single-color full-rank resource bases**, in addition to the covering graphic-flat and pointed binary matroid structure. The quantitative base-packing property is still weaker than the spanning-path conjectures, because independent resource representatives chosen from different covering states need not be geometrically adjacent or coherently directed. The challenge is to turn this substantial matroid-rank redundancy into a **coherent basis-path selector** using covering monodromy and the antipodal path language.

#### 10. Common two-color resource bases and the rarity of forced gates

The preceding full-rank and base-packing statements concern each color separately. The two colors also share a substantial **common** graphic resource support, even in worst-case tournaments.

Let \(F_\varepsilon=E(K_n)\setminus\Lambda_\varepsilon\) denote the color-\(\varepsilon\) missing-resource matching, and define
\[
\boxed{
H_b=([n],\Lambda_0\cap\Lambda_1)
=K_n-(F_0\cup F_1).
}
\tag{22}
\]

**Theorem 13 (simultaneous full rank and Hamiltonian common support).** For every ordinary reversal-odd boundary tournament:
\[
\boxed{
F_0\cap F_1=\varnothing,\quad
\Delta(F_0\cup F_1)\le2,\quad
\delta(H_b)\ge n-3.
}
\tag{23}
\]
Consequently, for \(n\ge5\),
\[
\boxed{r_{M(K_n)}(\Lambda_0\cap\Lambda_1)=n-1;}
\tag{24}
\]
for \(n\ge6\), \(H_b\) has a Hamiltonian cycle; and for \(n\ge7\), \(H_b\) is Hamilton-connected.

*Proof.* A resource edge \(\{u,v\}\) cannot be absent from both color supports, since each ordered triple entering the state \((u,v)\) has one of the two colors and would represent that same resource edge. Thus \(F_0\cap F_1=\varnothing\). By Theorem 6 each \(F_\varepsilon\) is a matching, so their union has maximum degree at most two, proving (23). For \(n\ge5\), each component of \(H_b\) contains at least \(\delta(H_b)+1\ge n-2\) vertices. Two components would require at least \(2(n-2)>n\) vertices, impossible; thus \(H_b\) is connected and its original graphic resource rank is \(n-1\). For \(n\ge6\), \(\delta(H_b)\ge n-3\ge n/2\), so Dirac's theorem gives a Hamiltonian cycle. For \(n\ge7\), every pair of nonadjacent vertices has degree sum at least \(2(n-3)\ge n+1\); Ore's Hamilton-connectedness theorem gives a Hamilton path between any prescribed pair of vertices. \(\square\)

The common-support graph omits a graph of maximum degree two whose components are isolated vertices, alternating paths, and even alternating cycles (the two omitted matchings alternate in any nontrivial cycle). In particular, **the same original resource basis can be represented by transitions of either color**, though the two representations need not be coherently adjacent or have compatible roots.

**Corollary 14 (any designated gate can occupy the unique unsupported position).** Let \(n\ge7\), and let \(e=\{u,v\}\in F_0\cup F_1\) be any missing-resource edge. There exists a Hamiltonian vertex order \(w\) containing \(u,v\) consecutively in an *interior* position, such that
\[
\boxed{
E(w)\setminus\{e\}\subseteq\Lambda_0\cap\Lambda_1.
}
\tag{25}
\]

*Proof.* By Theorem 13, the common-support graph \(H_b\) has a Hamiltonian path with prescribed endpoints \(u,v\). Adding the missing edge \(e=uv\) closes this path into a Hamiltonian cycle in which \(e\) is the sole edge outside \(H_b\). Delete a cycle edge not incident with \(e\) to obtain a spanning Hamiltonian path in which \(e\) is an interior resource edge and all other resource edges belong to both color supports. \(\square\)

This is a **resource-geometric**, not a colored-forward-path, statement: the color-\(\varepsilon\) representative of each common resource edge may occur at a completely different ordered-pair state. The theorem shows that the *placement* of a forced switching gate is never obstructed by ordinary graphic basis availability in orders \(n\ge7\). Forward path coherence remains the difficulty.

**Proposition 15 (forced gates are exponentially rare under random coloring).** Under the uniform probability measure on reversal-odd boundary 3-tournaments,
\[
\boxed{
\mathbb E|F_\varepsilon|
=\binom n2\,2^{-2(n-2)},\qquad
\Pr(F_0\cup F_1\ne\varnothing)
\le n(n-1)\,2^{-2(n-2)}.
}
\tag{26}
\]
In particular, with probability \(1-O(n^2 4^{-n})\), the **two** resource supports both equal the entire edge set \(E(K_n)\); no forced switching gate exists.

*Proof.* For a given edge \(\{u,v\}\), its absence from \(\Lambda_\varepsilon\) requires that all \(n-2\) ordered triples entering \((u,v)\) have color \(1-\varepsilon\), and likewise all \(n-2\) triples entering \((v,u)\). These are \(2(n-2)\) distinct reversal-pair bits: the first group has middle vertex \(u\), the second middle vertex \(v\), and no pair is the reversal of another in the same group or across groups. They are independent fair bits, so the absence event has probability \(2^{-2(n-2)}\). Sum over the \(\binom n2\) possible edges and use Markov's inequality and a union bound over both colors to obtain (26). \(\square\)

**Research limitation and next target.** The missing-resource matching and its phase gates are valuable *conditional* rerouting devices, but Proposition 15 rules out any universal proof that requires at least one missing resource: nearly all colorings have none. The stronger shared full-rank property (24) remains available even then. The natural missing theorem is therefore a **coherent basis-path synchronization principle**, converting the two full-color representatives of a common resource basis into oppositely rooted monochromatic arms whose union is independent, with at most one phase seam. Neither ordinary graphic matroid intersection nor uncolored Hamiltonicity implies that synchronization, as the preceding finite obstructions demonstrate.

### Conflict-graph purification and robust transfer of monotone paths

Let \(V\) be an \(n\)-element set, \(n\ge3\). A *boundary coloring* is a map \(b:V_{\ne}^3\to\{0,1\}\) satisfying \(b(c,v,a)=1-b(a,v,c)\). Let \(\prec\) be a total ordering of \(E(K_V)\), and let
\[
b_\prec(a,v,c)=\mathbf 1_{\{av\prec vc\}}.
\]
Reversing a triple complements this value. Denote by
\[
m=m(b,\prec)=\bigl|\{\{(a,v,c),(c,v,a)\}:b(a,v,c)\ne b_\prec(a,v,c)\}\bigr|
\]
the number of erroneous reversal classes of ordered triples. Every such class represents an unordered pair of incident edges of \(K_V\).

**Theorem 1 (conflict-graph purification).** There is a spanning graph \(G\subseteq K_V\) satisfying
\[
\boxed{\quad
\frac{2|E(G)|}{n}\ \ge\
d_{n,m}:=\frac{n-1}{1+\frac{4m}{n(n-1)}} ,
\quad} \tag{1}
\]
such that for every ordered triple \((a,v,c)\) of distinct vertices with \(av,vc\in E(G)\),
\[
\boxed{b(a,v,c)=b_\prec(a,v,c).} \tag{2}
\]
Consequently, every path of strictly increasing edge labels in \(G\) is a vertex-simple monochromatic tight path of color \(1\) in \(b\). The same holds for decreasing edge labels, of color \(0\).

*Proof.* Form the conflict graph \(J\) with vertex set \(E(K_V)\). Join two vertices \(av,vc\in E(K_V)\) whenever their comparison is erroneous, namely when \(b(a,v,c)\ne b_\prec(a,v,c)\). The reversal identity makes this condition independent of ordering the pair. Thus
\[
|V(J)|=Q:=\binom n2,\qquad |E(J)|=m.
\]
For any finite graph \(J\), its independence number satisfies the Caro–Wei bound
\[
\alpha(J)\ge\sum_{e\in V(J)}\frac{1}{1+\deg_J(e)}
\ge\frac{Q^2}{Q+2m}. \tag{3}
\]
For completeness, randomly order \(V(J)\) and retain each vertex earlier than all its neighbors; the retained vertices are pairwise nonadjacent, and each is retained with probability \(1/(1+\deg_J(e))\). Taking expectations proves the first inequality; Cauchy–Schwarz proves the second.

Choose an independent vertex set \(F\subseteq V(J)\) attaining the lower bound (3), and take \(G=(V,F)\). Independence states precisely that no two incident edges of \(G\) give an erroneous triple, proving (2). Since \(Q=n(n-1)/2\), the lower bound (3) gives
\[
\frac{2|F|}{n}\ge\frac{2Q^2}{n(Q+2m)}
=\frac{n-1}{1+4m/[n(n-1)]},
\]
which proves (1). For a strictly increasing path \(v_0v_1\cdots v_\ell\) in \(G\), every consecutive pair of its edges has the comparison color \(1\) in \(b_\prec\), hence by (2) in \(b\). Since it is a graph path, the vertices are distinct. \(\square\)

Define the *altitude* \(f(G)\) to be the minimum, over all total orders of \(E(G)\), of the greatest length in edges of an increasing vertex-simple path. Then Theorem 1 immediately gives \(L(b)\ge f(G)\), where \(L(b)\) is the maximum number of edges in a monochromatic vertex-simple tight path. To quantify this, use the published theorem of Bucić, Kwan, Pokrovskiy, Sudakov, Tran and Wagner, *Nearly-linear monotone paths in edge-ordered graphs*, Israel J. Math. **238** (2020), 663–685, Theorem 1.2: for an \(n\)-vertex graph of average degree \(d\ge2\),
\[
f(G)\ge \frac{d}{2^{C\sqrt{\log_2 d\,\log_2\log_2 n}}} \tag{4}
\]
for an absolute constant \(C\). The classical lower bound of Rödl gives \(f(G)\ge c\sqrt d\) for a universal \(c>0\).

**Corollary 2 (robust monotone-path transfer).** Let \(d_{n,m}\) be given by (1). Whenever \(d_{n,m}\ge2\),
\[
\boxed{
L(b)\ge \max\left\{
c\sqrt{d_{n,m}},
\ \frac{d_{n,m}}{2^{C\sqrt{\log_2 d_{n,m}\,\log_2\log_2 n}}}
\right\}.} \tag{5}
\]
In particular, as \(n\to\infty\):

(a) If \(m=o(n^2)\), then \(L(b)\ge n^{1-o(1)}\).

(b) If \(m=O(n^{2+\delta})\) for fixed \(0<\delta<1\), then \(L(b)\ge n^{1-\delta-o(1)}\).

(c) If \(m=o(n^3)\), then \(L(b)\to\infty\), quantitatively \(L(b)=\Omega(\sqrt{\min\{n,n^3/m\}})\) when \(m>0\). In the equivalent normalized notation \(m=\eta n^3\), this is \(\Omega(\min\{\sqrt n,\eta^{-1/2}\})\). The zero-error case is covered by (a).

*Proof.* Both bounds of (5) apply to the purified graph from Theorem 1; each increasing path transfers by (2). Under (a), \(d_{n,m}=n(1-o(1))\). Under (b), \(d_{n,m}=\Omega(n^{1-\delta})\). The denominator of the second expression of (5) is \(n^{o(1)}\) whenever \(d_{n,m}\) is a positive power of \(n\), proving (a) and (b). Under (c), (1) implies \(d_{n,m}=\Omega(\min\{n,n^3/m\})\to\infty\), and the first expression in (5) applies. \(\square\)

**Corollary 3 (spectrally near-extremal boundary colorings).** Suppose \(b\) has legal-turn disagreement density \(D(b)/E_n\), and put
\[
z=\max\{0,2/3-D(b)/E_n\}+\frac{n-2}{2(n-3)(n-1)}.
\]
The preceding edge-order synchronization theorem supplies an ordering \(\prec\) for which
\[
m(b,\prec)\le C_0 n(n-1)(n-2)z^{1/9}
\]
for an absolute constant \(C_0\). Applying Theorem 1 gives a comparison-faithful graph of average degree at least
\[
\boxed{d\ge\frac{n-1}{1+4C_0(n-2)z^{1/9}}.} \tag{6}
\]
Corollary 2 now applies with this lower bound. In particular, a polynomially small synchronization error \(m=O(n^{2+\delta})\) yields a monochromatic path of length \(n^{1-\delta-o(1)}\).

The case \(m=o(n^3)\) gives an unbounded path but does not itself imply a path of length \(n^{1-o(1)}\). A stronger transfer would have to exploit path-wise avoidance of errors while retaining many adjacent edges of the ordered complete graph. The conflict-free subgraph in Theorem 1 is a graph-theoretic comparison certificate; the path's original-vertex simplicity is preserved by its graphic-matroid independence.

### Random smoothing and the failure of global edge-order purification

Let \(V\) be a set of \(n\) vertices, \(n\ge3\). A reversal-odd coloring is a map \(b_0:V_{\ne}^3\to\{0,1\}\) satisfying \(b_0(c,v,a)=1-b_0(a,v,c)\). Fix \(0<\rho\le1/2\). Independently for each reversal class \(\{(a,v,c),(c,v,a)\}\), choose a Bernoulli random variable \(Z_{\{a,v,c\}}\) of parameter \(\rho\), and define
\[
b(a,v,c)=b_0(a,v,c)\oplus Z_{\{a,v,c\}}.
\tag{1}
\]
Thus \(b\) is again reversal-odd.

**Theorem 1 (near-spanning paths after independent perturbation).**
Fix an ordered pair \(u,v\) of distinct vertices, a color \(\epsilon\in\{0,1\}\), and \(0<\delta<1\). Put
\[
r=\left\lceil \rho^{-1}\log(n/\delta)\right\rceil .
\]
If \(r\le n-2\), then with probability at least \(1-\delta\), the coloring \(b\) admits a vertex-simple \(\epsilon\)-monochromatic tight path beginning with \(u,v\), using at least \(n-r\) vertices. In particular, when \(\rho n/\log n\to\infty\), with probability tending to one every ordered starting pair and each prescribed color admits such a path on \(n-O(\rho^{-1}\log n)\) vertices.

*Proof.* Build a sequence \(v_1=u,v_2=v,\ldots\) by greedily appending any unused \(w\) for which \(b(v_{i-1},v_i,w)=\epsilon\). To decide whether the next extension exists, reveal the colors of the triples \((v_{i-1},v_i,w)\) for unused \(w\). Every one of their reversal classes has middle vertex \(v_i\). The vertices \(v_i\) used as centers at successive stages are distinct, hence none of these classes has been queried at an earlier stage. Conditional on the complete past of the algorithm, the new bits are independent and each has probability at least \(\rho\) of yielding the desired color, whatever the deterministic values of \(b_0\). If \(k\) vertices remain unused, the conditional probability of failure is at most
\[
(1-\rho)^k\le e^{-\rho k}.
\]
Before \(n-r\) vertices have been used, \(k\ge r\), and there are at most \(n\) opportunities to fail. A union bound gives probability of failure at most \(ne^{-\rho r}\le\delta\). For the uniform assertion choose \(r=\lceil6\rho^{-1}\log n\rceil\), giving failure probability at most \(n^{-5}\) for each of fewer than \(2n^2\) starting-pair/color choices. A final union bound completes the proof. \(\square\)

A spanning subgraph \(G\subseteq K_V\) is called *comparison-orderable for \(b\)* if some strict total ordering of \(E(G)\) induces \(b(a,v,c)\) on every pair of incident edges \(av,vc\in E(G)\). Such a graph has a transitive induced subtournament on \(N_G(v)\) for every vertex \(v\): its local arc \(a\to c\) is defined by \(b(a,v,c)\), and a single ordering of the incident edges at \(v\) determines all its arcs.

**Lemma 2 (edge-disjoint triangle packing).** For any integer \(d\ge3\), the complete graph \(K_d\) contains at least \(d(d-1)/18\) triangles with pairwise disjoint edge sets.

*Proof.* Greedily select a triangle and remove every triangle sharing one of its three edges. Each selection removes at most \(3(d-2)\) triangles, while \(K_d\) originally contains \(\binom d3\) triangles. At least \(\binom d3/[3(d-2)]=d(d-1)/18\) selections are possible. \(\square\)

**Theorem 3 (uniform obstruction to comparison-orderable subgraphs).**
For every deterministic baseline \(b_0\), with probability tending to one as \(n\to\infty\), every comparison-orderable spanning subgraph \(G\subseteq K_V\), even allowing its edge ordering to depend on \(b\) and \(G\), satisfies
\[
\boxed{\quad
\Delta(G)<\left\lceil\frac{200\log n}{\rho}\right\rceil
\quad\text{whenever the right side is at most }n-1.\quad}
\tag{2}
\]
Consequently all such \(G\) satisfy
\[
\boxed{\quad |E(G)|=O\!\left(\frac{n\log n}{\rho}\right). \quad}
\tag{3}
\]
The implicit constant is absolute, independent of \(b_0\).

*Proof.* Fix a center \(v\) and a \(d\)-set \(S\subseteq V\setminus\{v\}\), where \(d=\lceil200(\log n)/\rho\rceil\le n-1\). For a triple \(\{a,c,e\}\subseteq S\), the restriction of the tournament \(b(\cdot,v,\cdot)\) to those three vertices is cyclic with probability at least \(\rho/4\). Indeed, if it is transitive in \(b_0\), flipping just the comparison between the first and last vertices in its transitive order produces a directed cycle, with probability \(\rho(1-\rho)^2\ge\rho/4\). If it is initially cyclic, keeping all three comparisons unchanged has probability \((1-\rho)^3\ge1/8\ge\rho/4\).

Choose the edge-disjoint triangle packing of Lemma 2 on \(S\). The corresponding cyclic-triangle events involve disjoint comparison variables and are therefore independent. Since there are at least \(d(d-1)/18\) such triangles,
\[
\Pr\bigl(b(\cdot,v,\cdot)|_S\text{ is transitive}\bigr)
\le\left(1-\frac{\rho}{4}\right)^{d(d-1)/18}
\le \exp\left(-\frac{\rho d(d-1)}{72}\right).
\]
The probability that some \(v\) and \(d\)-set \(S\) have a transitive induced local tournament is at most
\[
n\binom{n-1}{d}\exp\left(-\frac{\rho d(d-1)}{72}\right)
\le n\exp\left(d\log n-\frac{\rho d(d-1)}{72}\right)=o(1).
\tag{4}
\]
The last relation follows from \(d\ge200(\log n)/\rho\). On the complementary event, no comparison-orderable graph can have a vertex of degree at least \(d\), since that vertex's neighbor set contains such a transitive \(d\)-set. This proves (2). If \(d>n-1\), (3) is trivial from \(|E(G)|\le\binom n2\); otherwise use the degree bound. \(\square\)

**Corollary 4 (near-extremal coloring with almost-spanning paths but no dense orderable subgraph).**
There exist reversal-odd boundary colorings \(b_n\) on \(n\) vertices for which simultaneously
\[
\boxed{\frac{D(b_n)}{E_n}\ge \frac23-O(n^{-1/3}),}\tag{5}
\]
every ordered pair and both colors initiate a monochromatic tight path on \(n-O(n^{1/3}\log n)\) vertices, and every comparison-orderable subgraph \(G\subseteq K_n\) satisfies
\[
\boxed{|E(G)|=O(n^{4/3}\log n),\qquad
\Delta(G)=O(n^{1/3}\log n).}\tag{6}
\]
Here \(D(b)\) counts disagreeing edges of the legal-turn reversal quotient and \(E_n=n(n-1)(n-2)(n-3)/2\).

*Proof.* Randomly assign distinct real labels to \(E(K_n)\), and let \(b_0\) compare consecutive edge labels. Each legal turn \((a,b,c,d)\) involves three distinct edges with independent labels, so the probability of a changed comparison is \(2/3\). By averaging, there exists a deterministic edge order with \(D(b_0)/E_n\ge2/3\). Perturb this \(b_0\) as in (1) with \(\rho=n^{-1/3}\).

The two reversal classes involved in each legal turn are distinct, so their flips are independent. Write \(h=2\rho(1-\rho)\). The perturbed turn disagrees with probability \(h+(1-2h)d_0\), where \(d_0\in\{0,1\}\) is its original disagreement bit. Since \(1-2h=(1-2\rho)^2\ge0\),
\[
\frac{\mathbb E D(b)}{E_n}
=h+(1-2h)\frac{D(b_0)}{E_n}
\ge\frac23-\frac h3\ge\frac23-\frac23\rho.
\tag{7}
\]
There are \(N_n=n\binom{n-1}{2}\) independently perturbed reversal classes, and changing one flip changes \(D\) by at most \(2(n-3)\). The bounded-differences inequality therefore gives, for any \(t>0\),
\[
\Pr\left(\frac{D(b)}{E_n}<\frac{\mathbb E D(b)}{E_n}-t\right)
\le \exp(-t^2N_n/2).
\tag{8}
\]
Taking \(t=\rho\) proves (5) with probability tending to one. Theorem 1, with \(\delta=n^{-5}\) and a union bound over all starting ordered pairs and colors, gives the claimed paths. Theorem 3 gives (6). All three events occur simultaneously with probability tending to one, proving existence. \(\square\)

The contrast is structural: even when an unrestricted boundary coloring is arbitrarily close in normalized disagreement density to the extremal value \(2/3\), and supports near-spanning monochromatic paths, a subgraph on which *any* total edge ordering realizes all its local comparisons may have only \(O(n^{4/3}\log n)\) edges. Resource-simple paths can navigate mutually incompatible comparisons globally, so an exchange theorem seeking long paths must retain only the comparisons used by the evolving witness rather than insist upon one global edge-order representation.

**Theorem 5 (near-geodesic smoothing of antipodally odd cube colorings).**
Let \(Q_n\) be the \(n\)-dimensional cube, let \(c_0:E(Q_n)\to\{0,1\}\) satisfy \(c_0(\tau e)=1-c_0(e)\), where \(\tau\) is antipodal reversal, and fix a root vertex \(x\) and color \(\epsilon\). Independently for each antipodal pair of cube edges \(\{e,\tau e\}\), flip both assigned colors with probability \(\rho\), where \(0<\rho\le1/2\). Put \(r=\lceil\rho^{-1}\log(n/\delta)\rceil\) for \(0<\delta<1\). If \(2\le r\le n-1\), with probability at least \(1-\delta\) there is an \(\epsilon\)-monochromatic path beginning at \(x\) that uses \(n-r\) distinct coordinate directions, and hence is a geodesic of length \(n-r\). If \(\rho n/\log n\to\infty\), such a path has length \(n-o(n)\) with probability tending to one, for each prescribed root and color.

*Proof.* Identify vertices relative to \(x\) with subsets \(S\subseteq[n]\), and regard the directed edge \(e(S,i)\) from \(x^S\) to \(x^{S\cup\{i\}}\), \(i\notin S\), as a possible increasing-resource move. Greedily select an unused coordinate \(i\) whenever \(c(e(S,i))=\epsilon\). We show that, as long as \(|S|\le n-2\), all candidate antipodal edge orbits at the current step are distinct and have never been queried at an earlier step.

Indeed, let \(T\subsetneq S\) be a previously visited coordinate set, and let \(e(T,j)\) have been queried at that step. The current edge \(e(S,i)\) cannot equal \(e(T,j)\), since these two edges have different lower endpoints. If \(e(S,i)=\tau e(T,j)\), comparison of the endpoints with their ranks in the Boolean lattice gives
\[
S=[n]\setminus(T\cup\{j\}),\qquad
S\cup\{i\}=[n]\setminus T.
\]
Thus \(i=j\) and \(S\cap T=\varnothing\). Since \(T\subseteq S\), we have \(T=\varnothing\), and then \(S=[n]\setminus\{i\}\), contradicting \(|S|\le n-2\). Distinct current candidate coordinates also represent distinct antipodal edge orbits. This proves freshness until the final coordinate.

Consequently, conditional on all previously queried colors, when \(k=n-|S|\ge2\) unused coordinates remain, the candidate colors are independent, each with probability at least \(\rho\) of equaling \(\epsilon\). The conditional chance that all \(k\) extensions fail is at most \(e^{-\rho k}\). Until length \(n-r\) has been reached, at least \(r\ge2\) coordinates remain. At most \(n\) stages are tested, so the total failure probability is at most \(ne^{-\rho r}\le\delta\). Each selected coordinate is used once, so the resulting path is a geodesic. \(\square\)

**Common probabilistic mechanism.** Theorem 1 and Theorem 5 both exploit a graded extension system in which each extension consumes a new resource and its local candidates belong to noise variables unexposed at previous stages. For boundary tournaments the new resource is the next terminal vertex, giving a previously unused middle vertex for every new triple comparison. For cube geodesics the new resource is the next coordinate, and antipodal edge-orbit collisions are excluded until the final step by the Boolean-lattice complement relation. This common mechanism gives near-full-length single-color paths under independent perturbations, while the deterministic problem demands a zero-defect selection under arbitrary signatures; the cube theorem makes no claim about extending the last \(r\) coordinates in the prescribed color.


### Three-matroid Hamiltonian galleries and bounded-cost block reversal

Let \(n\ge4\) and let \(b(a,v,c)\in\{0,1\}\) be a reversal-odd boundary 3-tournament:
\[
b(c,v,a)=1-b(a,v,c)
\]
for pairwise distinct letters. For an injective word \(P=(v_1,\ldots,v_m)\), write its triple-color sequence \(c_P(i)=b(v_i,v_{i+1},v_{i+2})\), and let \(\mathrm{sw}(P)=\sum_{i=1}^{m-3}\mathbf1_{\{c_P(i)\ne c_P(i+1)\}}\).

**Theorem 1 (Hamiltonian words as three-matroid common independent sets).** Let \(A=\{(u,v):u,v\in[n],u\ne v\}\) be the directed arcs of the complete graph. On this common ground set define the graphic matroid \(M_{\rm gr}\) of \(K_n\), treating both directions of an undirected edge as parallel elements; the indegree partition matroid \(M_{\rm in}\), allowing at most one arc entering each vertex; and the outdegree partition matroid \(M_{\rm out}\), allowing at most one arc leaving each vertex. The common independent sets of cardinality \(n-1\) are precisely the directed Hamiltonian paths:
\[
\boxed{\{B\subseteq A:|B|=n-1,\ B\in\mathcal I(M_{\rm gr})\cap\mathcal I(M_{\rm in})\cap\mathcal I(M_{\rm out})\}.}
\tag{1}
\]

*Proof.* A graphic-independent set of \(n-1\) arcs has an underlying spanning tree in \(K_n\). The two partition matroid bounds give each vertex total degree at most two. Every degree-two spanning tree is an undirected Hamiltonian path. Its internal vertices each have one incoming and one outgoing arc, ensuring a consistently directed Hamiltonian path. Conversely such a path satisfies all three conditions. \(\square\)

**Proposition 2 (a single matroid does not encode the paths).** For every \(n\ge4\), the undirected edge sets of Hamiltonian paths of \(K_n\) do not form the bases of any matroid on \(E(K_n)\).

*Proof.* Let \(P=(0,1,2,3,\ldots,n-1)\) and \(Q=(0,2,1,3,\ldots,n-1)\). The differences between their edge sets are
\[
E(P)\setminus E(Q)=\{\{0,1\},\{2,3\}\},\quad
E(Q)\setminus E(P)=\{\{0,2\},\{1,3\}\}.
\]
Remove \(e=\{0,1\}\) from \(P\). Adding \(\{0,2\}\) gives degree three at vertex 2 and is not a path. Adding \(\{1,3\}\) creates triangle \(1,2,3,1\) and leaves vertex 0 isolated. No element of \(E(Q)\setminus E(P)\) provides the required basis exchange, so the axiom fails. \(\square\)

**Theorem 3 (uniformly bounded cost for nonlocal block reversal).** For any injective word \(P=(v_1,\ldots,v_m)\), \(m\ge4\), and any \(1\le a<b\le m\), let \(P^{[a,b]}\) be obtained by reversing the contiguous block \(v_a,\ldots,v_b\). Then
\[
\boxed{\bigl|\mathrm{sw}(P^{[a,b]})-\mathrm{sw}(P)\bigr|\le6.}
\tag{2}
\]
The bound is independent of \(m\) and the number of reversed vertices. For Hamiltonian words the operation preserves all three matroid independence conditions from Theorem 1, and modifies at most two edges of the underlying undirected Hamiltonian spanning tree.

*Proof.* Every triple window fully inside the reversed block becomes, after reindexing, the reversal of its corresponding former triple. Reversal-oddness complements every such color while reversing their order. Comparing consecutive triple colors strictly within this block therefore yields the same number of changes before and after reversal. Triple windows fully outside the block are unchanged. Only windows crossing its boundaries can change nontrivially: their possible start indices are \(a-2,a-1\) on the left and \(b-1,b\) on the right. Each pair of boundary-crossing windows belongs to at most three switch comparisons; every other comparison is either unchanged or belongs to the reversed-and-complemented interior, where the total is preserved. Thus no more than six switch indicators can change, proving (2).

Reversing a block preserves the vertex set and injectivity of the word, so the resulting Hamiltonian path is again a common independent set of cardinality \(n-1\). At the undirected graph level, every interior edge of the reversed block remains present. Only the two external boundary edges, if present, are replaced:
\[
\{v_{a-1},v_a\}\mapsto\{v_{a-1},v_b\},\qquad
\{v_b,v_{b+1}\}\mapsto\{v_a,v_{b+1}\}.
\]
Thus at most two graphic-basis edges change. \(\square\)

**Proposition 4 (the constant six is sharp).** For \(n=14\), consider
\[
P=(0,1,2,3,4,5,6,7,8,9,10,11,12,13)
\]
and the block reversal of positions 8 through 11 (one-based),
\[
P'=(0,1,2,3,4,5,6,10,9,8,7,11,12,13).
\]
The following triple-color words are simultaneously realizable by a reversal-odd tournament:
\[
c_P=011000000000,\qquad c_{P'}=011001011010.
\tag{3}
\]
Every triple reversal-orbit occurring in both words receives consistent complementary labels upon orientation reversal; assign colors on all other triple orbits freely. The two words have switch counts two and eight. Hence equality is achieved in (2). \(\square\)

**Corollary 5 (connected nonlocal gallery with bounded edge and cost changes).** The graph of directed Hamiltonian paths joined by contiguous-block reversals is connected. Any two such words can be joined by at most \(n-1\) reversals, each changing at most two underlying graphic-basis edges and at most six color switches.

*Proof.* Reversing an adjacent pair swaps two consecutive symbols, and adjacent transpositions generate all permutations. For the quantitative bound, repeatedly locate the desired next symbol of a target word and reverse the block from its current position to the current target position, fixing one additional prefix symbol at each step. At most \(n-1\) reversals suffice. Apply Theorem 3 to each operation. \(\square\)

**Implications and limitations.** This is an admissibility-preserving *nonlocal* exchange on Hamiltonian paths, with a dimension-independent cost Lipschitz constant. It differs from formal binary hexagon reductions or signed-incidence lattice generation because every intermediate object is a connected, resource-simple directed path. The theorem does not guarantee a descending reversal from each nonoptimal Hamiltonian path; it gives no universal upper bound on the minimum switch count. Arbitrary antipodally odd cube-edge colorings do not acquire the same block-reversal property on proper coordinate subcubes: complementarity is imposed only by the full antipodal involution. A future shared theorem needs the analogous globally legal move in each model, not an unqualified transfer of this tournament-specific operation.

A prospective approach is to combine the nonlocal reversal graph with cut-connectivity constraints and a low-cost witness principle. The difficult remaining step is to prove that this connected family must contain a path with a long constant-color run, rather than merely controlling how much one move can change the cost.

## Matroidal Reachability and Long-Path Bounds

Fix an antipodally odd binary edge coloring \(c\) of \(Q_n\), a root \(x\), and identify the directed resource-flat automaton with the Boolean lattice \(2^{[n]}\). Write \(\bar S=[n]\setminus S\). For the rooted edge \(S\to S\cup\{i\}\), deck oddness takes the form
\[
c_x(S,S+i)=1-c_x(\overline{S+i},\bar S).
\tag{1}
\]
Let \(U\subseteq2^{[n]}\) contain \(\varnothing\), avoid complementary pairs, and be forward-closed under color-zero arcs. Such a family is the dual reachability-cut certificate from the preceding flat-automaton Subsection.

**Theorem 1 (antipodal frontier separation).** No directed Boolean-lattice edge runs from \(U\) to its antipodal image \(\bar U=\{\bar T:T\in U\}\). Equivalently, there do not exist \(S,T\in U\) such that
\[
\boxed{S\cap T=\varnothing,\qquad |S|+|T|=n-1.}\tag{2}
\]

*Proof.* Suppose \(S\in U\) and \(S+i=\bar T\in\bar U\), with \(i\notin S\). Since \(U\cap\bar U=\varnothing\), this edge leaves \(U\), so its color is one. Reflection under complementation reverses this directed Boolean edge, producing
\[
T=\overline{S+i}\longrightarrow\bar S.
\]
Its initial point \(T\) lies in \(U\), while its terminal point \(\bar S\) lies in \(\bar U\), hence it also leaves \(U\) and must have color one. But the two reflected cube edges are antipodal and must have opposite colors by (1). Contradiction. A directed edge \(S\to\bar T\) exists if and only if \(S\cap T=\varnothing\) and \(|S|+|T|=n-1\), proving the equivalence. \(\square\)

**Theorem 2 (cross-level Hall inequalities).** Put \(U_s=U\cap\binom{[n]}s\). If \(s+t=n-1\) with \(s\ne t\), then
\[
\boxed{\frac{|U_s|}{\binom ns}+
\frac{|U_t|}{\binom nt}\le1.}\tag{3}
\]
In particular, since \(U_0=\{\varnothing\}\), it follows that \(U_{n-1}=\varnothing\).

*Proof.* Consider the bipartite disjointness graph between all \(s\)-subsets and all \(t\)-subsets. It is biregular: each \(s\)-set has \(n-s=t+1\) disjoint \(t\)-neighbors, and each \(t\)-set has \(n-t=s+1\) disjoint \(s\)-neighbors. Theorem 1 says that every neighbor of a member of \(U_s\) lies outside \(U_t\). Counting these edges by their two ends gives
\[
(t+1)|U_s|\le(s+1)(\binom nt-|U_t|).
\]
Use \((t+1)\binom ns=(s+1)\binom nt\) to obtain (3). Taking \(s=0,t=n-1\) proves the final statement. \(\square\)

**Corollary 3 (odd-dimensional Erdős–Ko–Rado obstruction).** For \(n=2k+1\), \(k\ge1\), the reachable middle family \(U_k\) is pairwise intersecting. Consequently,
\[
\boxed{|U_k|\le\binom{2k}{k-1}.}\tag{4}
\]
For \(k\ge2\), equality in the Erdős–Ko–Rado inequality forces \(U_k\) to be a full star (all \(k\)-subsets containing one distinguished coordinate).

*Proof.* Two disjoint \(k\)-sets would violate (2), since \(2k=n-1\). Apply the classical Erdős–Ko–Rado theorem to the intersecting \(k\)-uniform family on \(2k+1>2k\) elements. Its equality characterization for \(k\ge2\) gives the star structure. \(\square\)

**Consequence for NORI1.** In a hypothetical counterexample, the true color-zero reachable set \(R_x\) meets the hypotheses for every cube root \(x\). Thus (2)–(4) impose additional cross-rank constraints simultaneously on all rooted reachability families. The inequalities apply only under the complement-free hypothesis: colorings with a monochromatic full geodesic may violate them. They strengthen the SAT counterexample certificate, but do not independently prove that the certificate is impossible.

**Corollary 4 (near-complete monochromatic geodesics suffice).** For any \(n\ge3\), the following statements are equivalent under antipodally odd undirected cube-edge coloring:

(i) there exists a monochromatic full antipodal \(n\)-edge geodesic;

(ii) there exists a monochromatic geodesic of \(n-1\) edges, using all but one coordinate direction;

(iii) some rooted color-zero resource reachability family contains a subset of cardinality \(n-1\).

*Proof.* (i) implies (ii) by truncation. To see (ii) implies (i), take its two endpoints \(a,b\), which differ in all directions except \(j\). Appending the edge in direction \(j\) from either end gives an antipodal \(n\)-edge geodesic. These two extension edges are antipodal translates of one another and therefore have opposite colors. One of them has the color of the original \((n-1)\)-edge path, yielding a monochromatic full geodesic. For (iii), a rooted color-zero path using \(n-1\) resources is such a geodesic; conversely any monochromatic \((n-1)\)-edge geodesic can be deck-translated if needed to give a color-zero witness. \(\square\)

This shows that, in the free-coordinate matroid model, it would already suffice to force rank \(n-1\) in the color-zero flat automaton for **one** root, rather than force two complementary reachable flats directly. In a hypothetical counterexample, the accessible rank of every rooted color-zero automaton is at most \(n-2\), consistent with the conclusion \(U_{n-1}=\varnothing\) of Theorem 2.

**Corollary 5 (cross-level SAT strengthening).** The factorial-free counterexample SAT formulation in the flat-automaton Subsection can be strengthened, without changing satisfiability, by adding binary clauses
\[
\boxed{\neg r_{x,S}\vee\neg r_{x,T}
\quad\text{for every root }x,\ S\cap T=\varnothing,\ 
|S|+|T|=n-1.}\tag{5}
\]
These clauses are logical consequences of the original color-edge closure, antipodal oddness, and complementary exclusion constraints. In particular the clauses \(r_{x,\varnothing}\) force all membership variables \(r_{x,T}\) of cardinality \(n-1\) to be false.

*Proof.* Any satisfying assignment defines a complement-free outward color-zero-closed family \(U_x=\{S:r_{x,S}=1\}\). Apply Theorem 1 separately to each root. \(\square\)

For odd \(n=2k+1\), the clause family includes disjointness constraints between all reachable \(k\)-sets. By Corollary 3 these induce the Erdős–Ko–Rado bound \( |U_{x,k}|\le\binom{2k}{k-1}\). This gives a small, intrinsic collection of resource-level constraints that can be propagated by SAT or cutting-plane solvers. No large-dimensional conclusion is inferred from solver timeouts.

**Corollary 6 (Hilton–Milner stability of a hypothetical counterexample).** Suppose \(n=2k+1\) with \(k\ge2\), and suppose the antipodally odd coloring has no monochromatic antipodal geodesic. Then at every root \(x\), the middle-level reachable family
\[
\mathcal F_x=R_x\cap\binom{[n]}k
\]
obeys the following alternative:
\[
\boxed{
\bigcap_{S\in\mathcal F_x}S\ne\varnothing
\quad\text{or}\quad
|\mathcal F_x|\le\binom{2k}{k-1}-k+1.}
\tag{6}
\]
In particular, for \(Q_7\), if a counterexample had at least fourteen reachable triples at some root, all those triples would necessarily contain one common coordinate. If it had fifteen, they would form a full star on that coordinate.

*Proof.* By Corollary 3, \(\mathcal F_x\) is an intersecting \(k\)-uniform family on \(2k+1\) elements. If its total intersection is empty, the classical Hilton–Milner stability theorem for nontrivial intersecting families bounds its size by
\[
\binom{n-1}{k-1}-\binom{n-k-1}{k-1}+1
=\binom{2k}{k-1}-k+1.
\]
Otherwise it has a shared coordinate. The \(Q_7\) thresholds are \(15-3+1=13\) and the EKR maximum \(15\). \(\square\)

**Prospective proof route.** The missing global step can be sharpened to a root-coupling problem: if a hypothetical counterexample has many reachable rank-\(k\) flats, their common coordinate is nearly forced. One could seek a contradiction between the resulting root-dependent central-coordinate assignments, reversal symmetry, and the composition law
\[
S\in R_x,\quad T\in R_{x+\mathbf1_S},\quad S\cap T=\varnothing
\Longrightarrow S\cup T\in R_x.
\]
Theorem 1 and the Hilton–Milner bound are unconditional restrictions on the hypothetical counterexample, but do not establish the needed global counting lower bound.

### Common-terminal monochromatic arm bases and rooted Boolean complement intersection

The spanning at-most-one-turn conjecture for ordinary reversal-odd boundary 3-tournaments has a simpler equivalent form than opposite-ordered-pair terminal packing. It asks for two same-colored tight paths ending at the **same original vertex**, using complementary sets of other vertices. Their union is a basis of a doubled graphic matroid. No matching penultimate ordered pairs or prescribed bridging-triple color is required.

Fix a reversal-odd boundary coloring \(b(a,v,c)\in\mathbb F_2\) on a set \(V\) of order \(n\ge3\). Admit one-vertex and two-vertex tight paths as vacuously monochromatic in either color.

**Theorem 1 (single-terminal two-arm characterization).** The following assertions are equivalent:

(i) Some injective ordering \(W\) of all \(V\) has at most one change among its successive ordered-triple colors.

(ii) There are a vertex \(v\), a color \(\varepsilon\), and two vertex-simple \(\varepsilon\)-monochromatic tight paths \(P,Q\), **both ending at \(v\)**, with
\[
\boxed{V(P)\cap V(Q)=\{v\},\qquad V(P)\cup V(Q)=V.}
\tag{1}
\]

*Proof.* For (ii), write \(P=(p_1,\ldots,p_r,v)\), \(Q=(q_1,\ldots,q_s,v)\) and concatenate
\[
W=(p_1,\ldots,p_r,v,q_s,\ldots,q_1).
\]
This word is injective and spanning. All triples wholly inside \(P\) have color \(\varepsilon\), and all triples wholly inside the reverse of \(Q\) have color \(1-\varepsilon\). There is only one additional junction triple \((p_r,v,q_s)\), which has one of those two colors. Thus the full color word has at most one change. If either arm is a single vertex, the concatenation is the other monochromatic path.

Conversely, if the one change of \(W=(w_1,\ldots,w_n)\) occurs between its triple windows starting at indices \(i\) and \(i+1\), take \(v=w_{i+2}\), let \(P=(w_1,\ldots,w_{i+2})\), and take \(Q=(w_n,\ldots,w_{i+2})\), the reverse of the suffix beginning at \(v\). If the initial triple color is \(\varepsilon\), then \(P\) has all triple colors \(\varepsilon\), whereas the original suffix has triple colors \(1-\varepsilon\); reversal makes all triples of \(Q\) color \(\varepsilon\). Their vertex sets partition \(V\) around \(v\). The alternative pivot \(v=w_{i+1}\) works as well, giving **two adjacent seam-pivot choices**. If \(W\) is monochromatic, take \(P=W\) and \(Q=(w_n)\). \(\square\)

#### Parallel-extension graphic matroid

Let \(2K_n\) be the multigraph obtained by duplicating every edge of \(K_n\), giving each original edge a \(P\)-copy and a \(Q\)-copy, and let
\[
\boxed{\mathsf R_n^{(2)}=M(2K_n).}
\tag{2}
\]
For a path \(P\), write \(E_P(P)\) for its consecutive-original-vertex edges in the \(P\)-copy, and similarly \(E_Q(Q)\).

**Theorem 2 (rooted two-arm basis-packing equivalence).** If \(P,Q\) are vertex-simple tight words ending at the same original vertex \(v\), then
\[
\boxed{
E_P(P)\cup E_Q(Q)\in\mathcal I(\mathsf R_n^{(2)})
\iff
V(P)\cap V(Q)=\{v\}.
}
\tag{3}
\]
Such a union is a basis if and only if the two arms also cover \(V\). Hence the spanning one-turn conjecture is equivalent to the existence of a **same-color common-terminal arm pair whose union is a basis of the rank-\((n-1)\) graphic matroid \(\mathsf R_n^{(2)}\)**.

*Proof.* Each arm is a simple graph path. If their vertex sets meet only at \(v\), their doubled-edge union is a tree. Otherwise the two paths from \(v\) to any other common vertex form a graphic cycle, with doubled shared edges contributing two-element parallel cycles when necessary. Thus graphic independence is equivalent to intersection only at \(v\). An independent connected graph whose arms cover all \(n\) vertices has \(n-1\) edges, hence is a graphic-matroid basis; conversely a graphic basis requires all \(n\) vertices. Apply Theorem 1. \(\square\)

The parallel copies matter: in the simple graphic matroid \(M(K_n)\), two identical suffix edges collapse set-theoretically and might falsely appear independent. In \(M(2K_n)\) their repetition is a graphic two-cycle, so the basis condition alone enforces disjointness away from the root.

#### Rooted Boolean-lattice complement formulation

For each \(v\in V\) and color \(\varepsilon\), define
\[
\boxed{
\mathcal A_v^\varepsilon=
\{S\subseteq V\setminus\{v\}:
\exists\text{ an injective }\varepsilon\text{-monochromatic tight word}\\
\text{on }S\cup\{v\}\text{ ending at }v\}.
}
\tag{4}
\]
The singleton path \((v)\) witnesses the empty set, and all singleton subsets are witnessed by two-vertex paths. The complete family is the union of reachability states from the ordered-terminal resource automaton after forgetting the penultimate vertex.

**Theorem 3 (rooted complementary reachability).** A boundary tournament has a spanning at-most-one-turn tight path if and only if
\[
\boxed{
\exists\,v\in V,\ \varepsilon\in\mathbb F_2,\ S\subseteq V\setminus\{v\}:
\quad
S,\ (V\setminus\{v\})\setminus S\in\mathcal A_v^\varepsilon.
}
\tag{5}
\]

*Proof.* Two complementary reachable subsets give two same-color arms ending at \(v\) whose only shared original vertex is \(v\), and their union covers \(V\). Theorem 1 glues them into a one-turn spanning word. Conversely the two-arm decomposition in Theorem 1 yields precisely these complementary resource subsets. \(\square\)

**Corollary 4 (a sufficient rooted-majority criterion).** If some \(v,\varepsilon\) satisfies
\[
\boxed{|\mathcal A_v^\varepsilon|>2^{n-2},}
\tag{6}
\]
then a spanning one-turn tight path exists, by pigeonholing the \(2^{n-1}\) subsets into \(2^{n-2}\) complementary pairs. This inequality is a proposed proof route, **not** an established universal lower bound.

#### Unification with NORI1

The cube's free-resource automaton already gives rooted color-zero reachability families \(R_x\subseteq2^{[n]}\), and Article XI proves NORI1 equivalent to the existence of a root \(x\) for which
\[
\boxed{\exists S:\quad S,\ [n]\setminus S\in R_x.}
\tag{7}
\]
Theorem 3 now places the ordinary boundary spanning one-turn conjecture in **the identical formal rooted complement-pair template**, but on original-vertex subsets \(V\setminus\{v\}\). The resource independence of two boundary arms is captured by the parallel-extension graphic matroid \(\mathsf R_n^{(2)}\), while cube coordinate resource independence is captured by the free matroid. This removes the two-vertex seam-matching constraint from the boundary selector and makes the common open question precise: **under which shared intrinsic polarized-exchange axioms must a rooted monochromatic reachable-set family intersect its Boolean complement image?**

These results are equivalences and sufficient criteria, not a proof of the required complementary intersection in every coloring.

#### 5. Computational obstruction to the majority shortcut

The sufficient majority condition (6) is **not a universal consequence** of boundary reversal oddness. A reproducible order-eight reversal-odd coloring, stored in the research note *Eight-vertex obstruction to rooted-majority reachability*, has
\[
\boxed{\max_{v,\varepsilon}|\mathcal A_v^\varepsilon|=64=2^{8-2},}
\tag{8}
\]
with no root-color family larger than half the Boolean lattice. Yet it has the spanning one-turn tight word
\[
\boxed{(0,1,3,4,5,6,2,7),}
\tag{9}
\]
whose triple colors are \((0,0,0,1,1,1)\).

The complete representative-bit mask, the 16 rooted family sizes, and an independent standard-library enumeration certificate are preserved in that research note. The equivalence in Theorem 3 remains valid; this finite obstruction rules out only a proof relying on **strict rooted cardinality majority**. A universal theorem must force complementary reachability by more structural means, such as a linked exchange between the two monochromatic arms or a topological/intersection property stronger than set cardinality.

#### 6. The rooted path-basis polynomial and an integer counting identity

The same-terminal equivalence admits an all-dimensional **enumerative** refinement. It expresses the number of spanning at-most-one-turn words as a full-rank coefficient of squared monochromatic path-generating polynomials, and exposes a systematic characteristic-two cancellation in the corresponding doubled graphic-matroid basis count.

For each \(v\in V\) and \(\varepsilon\in\{0,1\}\), define the ordinary commuting-variable polynomial
\[
\boxed{
P_v^\varepsilon(\mathbf x)
=\sum_{\substack{P\text{ vertex-simple }\varepsilon\text{-monochromatic}\\
                   \text{tight word ending at }v}}
\prod_{u\in V(P)\setminus\{v\}}x_u.
}
\tag{10}
\]
Include singleton and two-vertex words, which are vacuously monochromatic in each color. The coefficient
\[
a_v^\varepsilon(S)=[x_S]P_v^\varepsilon
\]
is the number of monochromatic rooted paths using precisely \(S\cup\{v\}\). Thus the support of \(P_v^\varepsilon\) is the rooted family \(\mathcal A_v^\varepsilon\) defined above. Let \(H_0(b)\) and \(H_1(b)\) denote the respective numbers of ordered spanning tight words having zero and precisely one internal color change.

**Theorem 5 (rooted full-rank path-pair identity).** For every ordinary reversal-odd boundary coloring on \(n\ge3\) vertices,
\[
\boxed{
\sum_{v\in V}\sum_{\varepsilon=0}^1
\left[x_{V\setminus\{v\}}\right]
\bigl(P_v^\varepsilon(\mathbf x)\bigr)^2
=4H_0(b)+2H_1(b).
}
\tag{11}
\]
Equivalently, with \(U_v=V\setminus\{v\}\),
\[
\boxed{
\sum_{v,\varepsilon}\ \sum_{S\subseteq U_v}
a_v^\varepsilon(S)a_v^\varepsilon(U_v\setminus S)
=4H_0(b)+2H_1(b).
}
\tag{12}
\]

*Proof.* Each summand on the left counts an **ordered pair** of same-colored monochromatic tight words \(P,Q\) ending at one vertex \(v\), with disjoint other-vertex sets that together exhaust \(V\). Their union is a doubled-graphic-matroid basis by Theorem 2. Theorem 1 glues the ordered pair to the spanning word \(W=P+\operatorname{reverse}(Q)\), which has at most one internal color change.

Conversely, fix a spanning word \(W=(w_1,\ldots,w_n)\). A decomposition at a pivot \(v=w_j\) is forced by the word: \(P=(w_1,\ldots,w_j)\), \(Q=(w_n,\ldots,w_j)\). They have a common monochromatic color \(\varepsilon\) precisely when the prefix triples before the bridging position \(j-1\) all have color \(\varepsilon\), and the suffix triples after that bridging position all have color \(1-\varepsilon\).

If \(W\) has precisely one turn between the triple windows starting at positions \(i\) and \(i+1\), then there are precisely **two** admissible pivots \(j=i+1,i+2\), each with color \(\varepsilon\) equal to the initial run color. Thus \(W\) occurs twice on the left.

If \(W\) is monochromatic of color \(\eta\), two admissible pivots \(j=n-1,n\) use common arm color \(\eta\), while two pivots \(j=1,2\) use common arm color \(1-\eta\) (the short arm is vacuously monochromatic). Thus \(W\) occurs four times, including when \(n=3\), where the coincident middle pivot is counted once in each of the two different colors. Words with at least two changes admit no decomposition, since the only omitted crossing triple cannot suppress both changes. Summing multiplicities proves (11) and (12). \(\square\)

**Corollary 6 (basis-polynomial positivity certificate).** The spanning one-turn conjecture for a fixed boundary coloring is equivalent to strict positivity of the coefficient sum in (11). Each nonzero contributing monomial pair is a feasible full-rank basis in the doubled graphic matroid \(\mathsf R_n^{(2)}\), with both arms constrained to be monochromatic directed tight paths.

**Corollary 7 (parity cancellation).** For every \(v,\varepsilon\), and every \(n\ge2\),
\[
\boxed{
\left[x_{U_v}\right](P_v^\varepsilon)^2\equiv0\pmod2.
}
\tag{13}
\]
This holds regardless of the coloring and regardless of whether any complementary arm pair exists.

*Proof.* The coefficient is
\(\sum_{S\subseteq U_v}a(S)a(U_v\setminus S)\).
As \(U_v\ne\varnothing\), complementation has no fixed subset. Terms come in equal pairs indexed by \(S\) and \(U_v\setminus S\), so the sum is even. \(\square\)

Thus a direct **modulo-two full-rank coefficient** of the symmetric two-arm basis enumerator vanishes identically and cannot certify the desired intersection. This is consistent with, but conceptually distinct from, the binary pointed-matroid cycle–cocycle orthogonality: it reflects the exchange involution swapping the two arms. A proof using algebraic counting must retain asymmetry between the arms, richer integer coefficients, or geometric information about the reachability supports. The identity itself is an integral enumerative theorem, not an existence proof.

#### 7. Canonical phase choice at the root and a symmetric-matrix cancellation

The local tournament at a shared terminal vertex is not an additional feasibility constraint for two-arm gluing; it canonically selects **which of the two reversed Hamilton orders places the bridge on the first color run**.

**Proposition 8 (unique bridge-phase orientation).** Fix \(\varepsilon,v\), and let \(P,Q\) be two distinct vertex-simple color-\(\varepsilon\) tight words ending at \(v\), with disjoint nonterminal vertex sets, and suppose both arms have length at least two. Let \(u,w\) be their penultimate vertices. Then \(u\ne w\), and precisely one of the two Hamilton orders
\[
\boxed{P+\operatorname{rev}(Q),\qquad Q+\operatorname{rev}(P)}
\tag{14}
\]
has the joining triple of color \(\varepsilon\); the other has its joining triple of color \(1-\varepsilon\).

*Proof.* The two joining triples are \((u,v,w)\) and \((w,v,u)\), whose colors are complementary by reversal oddness. All remaining triples lie in the monochromatic first arm or the reversed second arm. The claimed phase choice follows. \(\square\)

Thus the orientation at a local tournament vertex is responsible for **selecting** the color-change position, but does not prevent the one-turn spanning path once the doubled-graphic-matroid basis pair exists. In particular, trying to impose a preselected junction color on *both* splicing orientations would introduce an unnecessary restriction.

For nontrivial arms define terminal refined polynomials
\[
P_{u,v}^{\varepsilon}(\mathbf x)=
\sum_{\substack{P\ \varepsilon\text{-monochromatic}\\
\operatorname{last2}(P)=(u,v)}}
\prod_{a\in V(P)\setminus\{v\}}x_a.
\tag{15}
\]
They give a local matrix representation of the full-rank complementary coefficient. Write
\(A^{\varepsilon}_v(u,w)=\mathbf1_{\{b(u,v,w)=\varepsilon\}}\) for distinct \(u,w\).
Then
\[
A_v^\varepsilon(u,w)+A_v^\varepsilon(w,u)=1,
\tag{16}
\]
and, because commuting polynomials multiply symmetrically,
\[
\boxed{
\sum_{u\ne w}
A_v^\varepsilon(u,w)
P_{u,v}^{\varepsilon}P_{w,v}^{\varepsilon}
=
\frac12\sum_{u\ne w}
P_{u,v}^{\varepsilon}P_{w,v}^{\varepsilon}.
}
\tag{17}
\]
All coefficients on the right are even before the division by two, by pairing \((u,w)\) and \((w,u)\). Taking the full-resource coefficient counts the unordered compatible rooted basis pairs with both arms nontrivial, each with its canonical bridge-color orientation. The remaining pairs involving a singleton arm contribute separately and correspond to monochromatic spanning paths.

Equation (17) shows the **skew-symmetric part of the local tournament adjacency matrix cancels** in this symmetric two-arm enumerator. Any future parity or Pfaffian argument must break the arm-swap symmetry before summing, rather than expect the local skew part to survive a symmetric quadratic form. This reinforces the integer-vs-binary distinction in Corollary 7 and points toward asymmetric terminal-root weights or a signed **two-arm linkage invariant** as a possible algebraic route.

### Random Hamiltonian absorption via transversal matroids

Let \(b_0\) be an arbitrary reversal-odd coloring of distinct ordered triples from an \(n\)-element vertex set \(V\). Independently for each reversal pair of triples, flip both colors with probability \(\rho\in(0,1/2]\), producing \(b\).

**Theorem 1 (noise-forced Hamiltonian tight paths).** If
\[
\boxed{\rho_n^3 n/\log n\to\infty,}\tag{1}
\]
then uniformly in \(b_0\), with probability \(1-o(1)\) **every** prescribed initial ordered pair \((u,v)\) and prescribed color \(\epsilon\in\{0,1\}\) extend to an \(\epsilon\)-monochromatic vertex-simple tight Hamiltonian path.

The key deterministic construction is governed by a transversal matroid.

**Lemma 2 (separated-slot absorption).** Suppose \(P=(v_1,\ldots,v_\ell)\) is an injective \(\epsilon\)-monochromatic tight path and \(U=V\setminus V(P)\). Let \(I\subseteq\{2,\ldots,\ell-2\}\) be gap indices at pairwise distance at least five. Form a bipartite graph \(B\) with left vertices \(U\) and right vertices \(I\); declare \(z\in U\) adjacent to \(i\in I\) when
\[
b(v_{i-1},v_i,z)=b(v_i,z,v_{i+1})
=b(z,v_{i+1},v_{i+2})=\epsilon.\tag{2}
\]
If \(B\) has a matching saturating \(U\), then the original coloring has an \(\epsilon\)-monochromatic tight Hamiltonian path beginning with \((v_1,v_2)\).

*Proof.* For each matched pair \((z,i)\), insert \(z\) between \(v_i,v_{i+1}\). The insertion removes the two original triple windows meeting that gap and replaces them by the three windows in (2), all of the required color. Because selected gaps are separated by at least five positions, the changes at different gaps are disjoint. The resulting word uses all vertices once and retains its first two vertices. Matchable subsets of \(U\) are the independent sets of the transversal matroid determined by \(B\). \(\square\)

*Proof of Theorem 1.* Fix \(u,v,\epsilon\). Set
\[
t=\lceil12\rho^{-1}\log n\rceil,\qquad r=2t.
\]
Condition (1) implies \(t\log n=o(n)\), hence \(r=o(n)\). Beginning with \((u,v)\), repeatedly choose uniformly at random \(t\) of the unused vertices, expose the triples obtained by appending each candidate, and append one candidate with color \(\epsilon\), continuing until \(r\) vertices remain. At each step every newly queried reversal class has the current terminal vertex as its middle vertex. That vertex has never been the middle vertex of an earlier extension query, since the growing path is injective. Therefore the candidate colors are fresh independent random variables, each equal to \(\epsilon\) with probability at least \(\rho\). The chance that a step has no acceptable candidate is at most \((1-\rho)^t\le n^{-12}\). A union bound over fewer than \(n\) steps shows that, except with probability at most \(n^{-11}\), this process produces a monochromatic path \(P\) of length \(\ell=n-r\).

For each \(z\in V\), let \(Q_z\) be the number of stages whose random query set included \(z\). When \(k\) vertices are still unused, the conditional probability of such inclusion is at most \(t/k\), even given the entire earlier construction. Once \(z\) has been appended, its subsequent inclusion probability is zero. Therefore the moment-generating bound for adapted indicators gives
\[
\mathbb E e^{Q_z}
\le \exp\!\left((e-1)t\sum_{k=r+1}^{n-2}k^{-1}\right)
\le \exp((e-1)t(1+\log n)).
\]
By Markov's inequality,
\[
\Pr[Q_z>4t(1+\log n)]
\le\exp(-(5-e)t(1+\log n)).
\]
A union bound gives, with probability \(1-o(n^{-10})\),
\[
\boxed{\max_{z\in V}Q_z\le4t(1+\log n)=o(n).}\tag{3}
\]

Choose \(I=\{2,7,12,\ldots\}\cap\{2,\ldots,\ell-2\}\), so \(K=|I|=(1/5+o(1))n\). For any missing \(z\in U\), consider the three insertion comparisons at gap \(i\). The comparison centered at \(z\) has never been exposed, because \(z\) was never a terminal path vertex. The last comparison, centered at \(v_{i+1}\), also has not been exposed: when \(v_{i+1}\) was terminal during construction, every tested triple had \(v_i\) as one outer vertex, while \((z,v_{i+1},v_{i+2})\) has two different outer vertices. Only the first comparison, centered at \(v_i\), might have been exposed. This occurs at no more than \(Q_z\) gaps. Thus at least \(K-Q_z\) gap comparisons are fully fresh for each missing \(z\).

The reversal classes in the three comparisons for distinct eligible pairs \((z,i)\in U\times I\) are all different: the five-position gap spacing separates centers \(v_i,v_{i+1}\), the missing vertices \(z\) lie outside \(P\), and the remaining outer pairs identify the missing vertex and its gap. Conditional on the complete construction history, all eligible compatibility indicators are independent and have success probability at least \(\rho^3\).

We verify Hall's condition by a union bound. Let \(A\subseteq U\) be nonempty, with \(a=|A|\), and \(C\subseteq I\) have cardinality \(a-1\). If (3) holds, then for each \(z\in A\), at least
\[
K-Q_z-|C|\ge n/10
\]
gaps outside \(C\) retain three fresh comparisons, for all sufficiently large \(n\), since both \(r\) and the bound in (3) are \(o(n)\). The probability that no compatible edge joins \(A\) to \(I\setminus C\) is at most \(e^{-\rho^3 a n/10}\). The number of pairs \(A,C\) of these cardinalities is bounded by
\(\binom ra\binom K{a-1}\le n^{2a}\). Hence
\[
\Pr[\exists A\subseteq U:|N_B(A)|<|A|\mid\text{construction}]
\le\sum_{a=1}^{r}\exp\!\left(a(2\log n-\rho^3n/10)\right)
=n^{-\omega(1)}.\tag{4}
\]
By Hall's theorem, with overwhelming probability the bipartite compatibility graph has a matching saturating \(U\). Lemma 2 inserts every leftover vertex while preserving the complete monochromatic path. The error probabilities from the greedy stage, the exposure estimate, and Hall's estimate sum to \(o(n^{-3})\), allowing a final union bound over both colors and fewer than \(n^2\) ordered initial pairs. \(\square\)

**Scope and interpretation.** This proves a three-window, resource-preserving absorption theorem for ordinary boundary 3-tournaments and identifies its intrinsic transversal-matroid independence condition. The random perturbation assumption supplies the necessary compatible slots. It substantially strengthens near-spanning random smoothing, but it does not establish a deterministic spanning monochromatic path for arbitrary boundary colorings. For cube-edge colorings, inserting an unused coordinate at an interior position changes the edges along the entire remaining suffix, so an additional cubical exchange argument would be required for a parallel Hamiltonian result.

### Rooted random cube geodesics and permutation overlap moments

Fix a cube vertex \(x\), a prescribed color \(\epsilon\), and an arbitrary antipodally odd coloring \(c_0\) of \(Q_n\). Independently flip both colors in each antipodal edge orbit with probability \(\rho\in(0,1/2]\), producing \(c\).

**Theorem (optimal rootwise noise threshold).** If \(n\rho\to\infty\), the probability that there is an \(\epsilon\)-monochromatic geodesic from \(x\) to \(\tau x\) tends to one, uniformly over \(c_0\). Put \(h=3e(\rho^{-1}-1)/n\). If \(h<1\), the failure probability is at most \(h\). The growth assumption \(n\rho\to\infty\) is necessary for the uniform fixed-root, fixed-color assertion.

**Lemma (shared-edge moment).** Fix a coordinate permutation \(\pi\), take \(\sigma\in S_n\) uniformly, and let \(s\) be the number of cube edges common to the two root-to-antipode geodesics. For every \(z\ge1\),
\[
\mathbb E z^s\le\sum_{t=0}^n\frac{[3(z-1)]^t}{(n)_t}
\le\sum_{t=0}^n\left(\frac{3e(z-1)}n\right)^t.
\tag{1}
\]

*Proof.* Relabel so that \(\pi=(1,\ldots,n)\). The edge at rank \(k\) is common precisely when the first \(k\) symbols of \(\sigma\) are \([k]\) and its next symbol is \(k+1\). This is a singleton component of its direct-sum permutation decomposition. Prescribing \(t\) such positions divides the other \(n-t\) entries into \(t+1\) consecutive blocks of sizes \(a_0,\ldots,a_t\). The number of compatible permutations is \(\prod_j a_j!\). Expanding \(z^s=(1+z-1)^s\) gives
\[
\mathbb E z^s=\frac1{n!}\sum_{t=0}^n(z-1)^t
\sum_{\substack{a_0+\cdots+a_t=n-t\\a_j\ge0}}\prod_j a_j!.
\]
For all \(m\ge0\), \(\sum_{j=0}^m j!(m-j)!=m!\sum_j\binom mj^{-1}\le3m!\), since the two extreme reciprocals are one and each interior reciprocal is at most \(1/m\). Convolution induction bounds the inner sum by \(3^t(n-t)!\), giving the first inequality. The inequality \((n)_t\ge(n/e)^t\), obtained by comparing the geometric means of the largest \(t\) integers among \(1,\ldots,n\) with \((n!)^{1/n}\ge n/e\), proves the second. \(\square\)

*Proof of the theorem.* Let \(A_\pi\) be the event that the path of coordinate permutation \(\pi\) is all color \(\epsilon\), and \(q_\pi=\Pr(A_\pi)\). A geodesic uses each direction once, so its edges lie in distinct antipodal orbits, and \(q_\pi=\prod_{f\in P_\pi}p_f\), where \(p_f=\Pr(c(f)=\epsilon)\in[\rho,1-\rho]\). Define
\[
Z=\sum_{\pi\in S_n}\frac{\mathbf1_{A_\pi}}{q_\pi};
\qquad\mathbb EZ=n!.
\]
For two geodesics \(P_\pi,P_\sigma\), their simultaneous all-\(\epsilon\) event has probability zero if an edge of one is antipodal to an edge of the other. Otherwise all orbit variables are independent except for common edges, each contributing a joint-to-product factor \(1/p_f\le1/\rho\). Consequently
\[
\frac{\mathbb EZ^2}{(\mathbb EZ)^2}
\le\mathbb E_{\pi,\sigma}\rho^{-|E(P_\pi)\cap E(P_\sigma)|}
\le\sum_{t=0}^n h^t\le(1-h)^{-1}.
\]
The second-moment inequality gives \(\Pr(Z>0)\ge1-h\), proving the quantitative claim and the limit. Conversely choose the initial coloring with all \(n\) edges at \(x\) colored \(1-\epsilon\), completing antipodal pairs consistently. With probability \((1-\rho)^n\), none of these root edges flips, so no \(\epsilon\)-monochromatic path starts at \(x\). This failure probability stays positive whenever \(n\rho\) is bounded. \(\square\)

The result concerns full geodesics under noise, and is uniform over the baseline coloring. The deterministic NORI1 conjecture remains open.

**Corollary (coordinate-face smoothing).** Let \(F\) be an \(m\)-dimensional coordinate face of \(Q_n\), \(2\le m\le n\), and fix \(x\in F\) and a color \(\epsilon\). Independently flip the colors on full-cube antipodal edge pairs with probability \(\rho\). Then, uniformly in the initial antipodally odd coloring,
\[
\Pr(\text{no \(\epsilon\)-monochromatic geodesic in \(F\) between opposite face corners})
\le\frac{3e(\rho^{-1}-1)}m
\]
whenever the right side is below one. In particular, the failure probability is \(o(1)\) if \(m\rho\to\infty\).

*Proof.* A face geodesic uses each of its \(m\) free coordinates once, and hence meets distinct full-cube antipodal edge orbits. If \(F\) is proper, the full-cube antipodal translate of any edge of \(F\) lies outside \(F\), so two face geodesics can share an orbit only by using the same edge. In the full-face case, opposite edges between different geodesics produce incompatible prescribed-color events and contribute zero to their joint probability. Thus the weighted second-moment calculation and the permutation singleton-block bound of the theorem apply in either case, with \(m\) in place of \(n\). \(\square\)

**Lemma (opposite-chain edge exclusion).** Let \(P_\pi\) be the root-to-antipode coordinate geodesic given by a permutation \(\pi=(i_1,\ldots,i_n)\), and let \(P_{\pi^R}\) use its reverse permutation. Every root-to-antipode coordinate geodesic \(P_\sigma\) shares an edge with at most one of \(P_\pi,P_{\pi^R}\).

*Proof.* In resource-set coordinates relative to the root, the first path has edges between its consecutive prefix sets
\[
A_k=\{i_1,\ldots,i_k\},\qquad 0\le k\le n,
\]
whereas the second has edges between consecutive suffix sets
\[
B_j=\{i_{n-j+1},\ldots,i_n\},\qquad 0\le j\le n.
\]
If a monotone resource chain contained an edge \(A_k\to A_{k+1}\) followed by an edge \(B_j\to B_{j+1}\), its sets would satisfy \(A_{k+1}\subseteq B_j\). But \(i_1\in A_{k+1}\) and \(i_1\notin B_j\), since \(j\le n-1\). If the suffix edge occurred first, the chain would require \(B_{j+1}\subseteq A_k\), contradicted by \(i_n\in B_{j+1}\) and \(i_n\notin A_k\). These exhaust the possible orders. \(\square\)

**Theorem (full edge-color profile universality).** Under the hypotheses of the rootwise smoothing theorem, fix an arbitrary predetermined word \(w=(w_1,\ldots,w_n)\in\{0,1\}^n\) and a root \(x\). There is a root-to-antipode geodesic whose consecutive edge colors form \(w\), with failure probability at most
\[
\boxed{\frac{2h}{1+h},\qquad
h=\frac{3e(\rho^{-1}-1)}n<1.}
\]
In particular this probability tends to one uniformly in the baseline coloring and prescribed word whenever \(n\rho\to\infty\). The growth condition is necessary for a uniform fixed-root, fixed-word assertion.

*Proof.* For every \(\pi\in S_n\), let \(A_\pi\) be the event that the sequence of colors along \(P_\pi\) is \(w\), let \(q_\pi=\Pr(A_\pi)>0\), and set \(Z=\sum_\pi\mathbf1_{A_\pi}/q_\pi\). Since each coordinate is used once, a single path visits distinct antipodal noise-variable orbits and \(\mathbb EZ=n!\).

A pair of paths may share a noise orbit through a common cube edge or through antipodal partner edges. When the two demands on a shared orbit conflict, their joint success probability is zero; otherwise that orbit contributes a joint-to-product factor at most \(\rho^{-1}\). Let \(K_+(\pi,\sigma)\) count edges common to \(P_\pi,P_\sigma\), and let \(K_-(\pi,\sigma)\) count edges common to \(P_{\pi^R},P_\sigma\). The antipodal image of the edge set of \(P_\pi\) is the edge set of \(P_{\pi^R}\), so \(K_++K_-\) counts shared noise orbits. By the opposite-chain exclusion lemma, \(K_+K_-=0\). Therefore, for \(z\ge1\),
\[
\begin{aligned}
\mathbb E_{\pi,\sigma}z^{K_++K_-}
&=1+\mathbb E(z^{K_+}-1)+\mathbb E(z^{K_-}-1)\\
&=2\mathbb E_{\pi,\sigma}z^{K_+}-1.
\end{aligned}
\]
The two overlap counts have identical marginal distributions under uniform permutations. Apply the singleton-block moment bound with \(z=\rho^{-1}\) to obtain
\[
\frac{\mathbb EZ^2}{(\mathbb EZ)^2}
\le2(1-h)^{-1}-1=\frac{1+h}{1-h}.
\]
Cauchy--Schwarz now yields \(\Pr(Z>0)\ge(1-h)/(1+h)\), proving the failure estimate. For necessity, prescribe the first edge color \(w_1\) and choose the initial coloring with all \(n\) root-incident edges of color \(1-w_1\). The probability that none flips is \((1-\rho)^n\), bounded away from zero when \(n\rho\) stays bounded. \(\square\)

On a proper \(m\)-face, no two of its edges lie in the same full-cube antipodal orbit. Hence the face corollary also holds for every prescribed length-\(m\) color word with its original failure bound \(3e(\rho^{-1}-1)/m\). The new theorem establishes a common fixed-pattern smoothing principle with the rooted boundary Hamiltonian-window theorem.

### Rooted Hamiltonian windows and the sharp random perturbation threshold

Let \(V\) be an \(n\)-element set, \(n\ge4\), and let \(b_0:V_{\ne}^3\to\mathbb F_2\) satisfy \(b_0(c,v,a)=1-b_0(a,v,c)\). Independently flip both colors in each reversal orbit of ordered triples with probability \(\rho\in(0,1/2]\), obtaining \(b\). For an injective word \(P=(v_1,\dots,v_n)\), its windows are the ordered triples \((v_i,v_{i+1},v_{i+2})\), \(1\le i\le n-2\).

**Theorem 1 (optimal rooted Hamiltonian pattern universality).** Fix any ordered pair \((u,v)\) of distinct vertices and any predetermined binary word \(a=(a_1,\ldots,a_{n-2})\). Put
\[
h_n=\frac{e(1+2e)(\rho^{-1}-1)}{n-2}.
\]
If \(h_n<1\), then, uniformly over \(b_0\),
\[
\boxed{\Pr\bigl(\text{no Hamiltonian tight path starting with \(u,v\) has color word \(a\)}\bigr)\le h_n.}\tag{1}
\]
Consequently \(\rho_n n\to\infty\) implies that each preselected color word is realized from \((u,v)\) with probability \(1-o(1)\), uniformly in the word. Simultaneous realization of all color words is not asserted. Conversely, the assumption \(\rho_n n\to\infty\) is necessary for this assertion to hold uniformly over all baseline colorings.

The key input is a factorial-moment inequality for overlapping length-three windows.

**Lemma 2 (fixed-prefix window overlap).** Fix a permutation \(\pi=(1,\ldots,n)\), and choose \(\sigma\) uniformly among permutations beginning with \(1,2\). Let \(K(\pi,\sigma)\) count the reversal orbits of length-three windows appearing in both \(\pi\) and \(\sigma\). For \(z\ge1\), set \(y=z-1\). Then
\[
\boxed{\mathbb E_\sigma z^{K(\pi,\sigma)}
\le\sum_{t=0}^{n-2}\left(\frac{e(1+2e)y}{n-2}\right)^t.}\tag{2}
\]

*Proof.* Put \(N=n-2\). For a nonempty set \(S\subseteq[N]\), with \(|S|=t\), write \(c\) for its number of maximal runs of consecutive integers. Each selected triple window at rank \(i\) requires its two undirected path edges \(\{i,i+1\},\{i+1,i+2\}\) to occur as adjacent pairs in \(\sigma\). Their union is a path forest with \(t+c\) edges. Add the edge \(\{1,2\}\), which is already the prescribed first edge of \(\sigma\).

If \(1\in S\), the added edge is already present; the resulting forest has \(m=t+c\) edges and at most \(c\) nontrivial components. If \(1\notin S\), it has \(m=t+c+1\) edges and at most \(c+1\) components. For a forest with \(m\) edges and \(r\) nontrivial path components, one of which contains the required initial ordered edge \((1,2)\), the number of permutations beginning \(1,2\) that contain every forest edge as a consecutive adjacency is at most \(2^{r-1}(n-m-1)!\): the initial component has its order and position prescribed, each other path component admits two orientations, and the remaining blocks can be permuted. Dividing by the total \((n-2)!\) gives
\[
\Pr(S\text{ is contained in the common-window indices})\le
\begin{cases}
2^{c-1}/(N)_{t+c-1},&1\in S,\\
2^c/(N)_{t+c},&1\notin S,
\end{cases}\tag{3}
\]
where \((N)_j=N(N-1)\cdots(N-j+1)\). The bound holds because every shared triple imposes its two underlying path adjacencies.

The number of \(t\)-subsets of \([N]\) with \(c\) runs and containing \(1\) is
\[
\binom{t-1}{c-1}\binom{N-t}{c-1},
\]
and the number avoiding \(1\) is
\[
\binom{t-1}{c-1}\binom{N-t}{c}.
\]
Use \((N)_j\ge(N/e)^j\), \(\binom{N-t}{j}\le N^j/j!\), and \(1/j!\le1\). The sum of probabilities in (3) over all \(t\)-subsets is at most
\[
\begin{aligned}
&\left(\frac eN\right)^t
\sum_{c=1}^t\binom{t-1}{c-1}
\left(\frac{(2e)^{c-1}}{(c-1)!}
+\frac{(2e)^c}{c!}\right)\\
&\hspace{30mm}\le
\left(\frac eN\right)^t(1+2e)^t.\tag{4}
\end{aligned}
\]
Finally expand \(z^K=(1+y)^K=\sum_{S\subseteq\mathrm{CommonWindows}}y^{|S|}\), average, and insert (4), proving (2). \(\square\)

*Proof of Theorem 1.* Let \(\mathcal P\) be the \((n-2)!\) permutations of \(V\) starting with \(u,v\). Let \(A_P\) be the event that the consecutive triple-color word of \(P\) equals \(a\), and let \(q_P=\Pr(A_P)>0\). Their reversal orbits are distinct because their middle vertices are distinct, so
\[
q_P=\prod_{t\in\mathrm{Windows}(P)}p_t,\qquad p_t\in[\rho,1-\rho].
\]
Define
\[
Z=\sum_{P\in\mathcal P}\frac{\mathbf1_{A_P}}{q_P},
\qquad \mathbb E Z=(n-2)!.
\]
If two words \(P,Q\) require opposing colors on the same reversal orbit, their joint all-\(\epsilon\) event has probability zero. Otherwise independence of distinct orbit-noise variables shows that the ratio \(\Pr(A_P\cap A_Q)/(q_Pq_Q)\) is a product of \(p_t^{-1}\le\rho^{-1}\) over their shared window orbits. Hence
\[
\frac{\mathbb EZ^2}{(\mathbb EZ)^2}
\le\mathbb E_{P,Q}\rho^{-K(P,Q)}
\le\sum_{t=0}^{n-2}h_n^t
\le(1-h_n)^{-1}.
\]
By Cauchy--Schwarz, \(\Pr(Z>0)\ge(\mathbb EZ)^2/\mathbb EZ^2\ge1-h_n\), giving (1).

For necessity, choose \(b_0(u,v,w)=1-a_1\) for every \(w\in V\setminus\{u,v\}\), assign the reverse triples their complementary color, and fill the remaining reversal orbits arbitrarily. With probability \((1-\rho)^{n-2}\), no triple \((u,v,w)\) is flipped, and no Hamiltonian tight path starting with \(u,v\) can realize \(a\). This failure probability stays bounded away from zero if \(n\rho\) remains bounded. \(\square\)

**Common witness-overlap principle.** The theorem and the rootwise cube-geodesic theorem of the preceding Subsection both use a family of full-resource paths, with a distinct independent noise variable for each edge or window constraint within a path. For any such finite family \(\mathcal W\), let \(q_W>0\) be the probability that \(W\) satisfies its prescribed monochromatic constraints, and let \(K(W,W')\) count shared unoriented noise-variable orbits. With \(Z=\sum_W\mathbf1_{\{W\text{ succeeds}\}}/q_W\), the same argument gives
\[
\boxed{
\Pr(Z>0)\ge
\left(\mathbb E_{W,W'}\rho^{-K(W,W')}\right)^{-1}.}\tag{5}
\]
Oppositely oriented shared constraints make joint success impossible and only strengthen the estimate. In both canonical applications, the overlap sets form subforests of underlying path bases; their factorial moments decay sufficiently rapidly to produce the common optimal rootwise smoothing condition \(n\rho\to\infty\).

The theorem concerns independent random perturbations of arbitrary reversal-odd colorings and applies to each prescribed window pattern, including monochromatic, one-switch, and alternating words. It strengthens the earlier transversal-matroid absorption theorem, which supplies simultaneous guarantees for all ordered starting pairs under a larger perturbation rate. Neither theorem establishes a deterministic boundary-tournament selector or unrestricted NORI1.

### Two-resource Hamiltonian recognition and monochromatic forest rank

Let \(n\ge4\), let \(V=[n]\), and let \(\mathcal T_n\) denote reversal-orbits \([a,b,c]=[c,b,a]\) of ordered triples with pairwise distinct entries. As established in the boundary-cover construction, \(\mathcal T_n\) is the edge set of the line graph \(L(K_n)\): the turn \([a,b,c]\) joins its two **edge states** \(ab=\{a,b\}\) and \(bc=\{b,c\}\) and has **middle label** \(b\).

For a subset \(T\subseteq\mathcal T_n\), let \(J_T\) be the subgraph of \(L(K_n)\) with edge set \(T\), discarding isolated state vertices. Write \(S(T)\subseteq E(K_n)\) for its vertex support, i.e. the union of the two state edges activated by each triple. We say that \(T\) is **resource-feasible** if

* no two selected triples have the same middle label (independence in the middle-label partition matroid), and
* \(S(T)\) is independent in the graphic matroid \(M(K_n)\).

These conditions are intrinsic to the two resource systems, without presupposing a path or its orientation.

**Theorem 1 (automatic path-forest structure).** Every nonempty resource-feasible \(T\) has \(J_T\) equal to a vertex-disjoint union of \(c\ge1\) simple paths (each with at least one edge). Each such component lifts, in either direction, to a vertex-simple path in \(K_n\), and its line-graph edges are precisely the selected consecutive triple reversal-orbits of that path. If \(m=|T|\), then
\[
\boxed{|S(T)|=m+c\le n-1,\qquad c\le n-1-m.}\tag{1}
\]

*Proof.* A line-graph state \(e=\{a,b\}\) is incident with selected turns centered at \(a\) or \(b\). At most one selected turn has each middle label, so the degree of \(e\) in \(J_T\) is at most two. If a component of \(J_T\) were a cycle with turns centered at \(b_1,\ldots,b_r\), then consecutive turn centers would be distinct and its state edges would be \(\{b_1,b_2\},\{b_2,b_3\},\ldots,\{b_r,b_1\}\), forming a cycle in the underlying graph \(S(T)\), contrary to graphic independence. Thus \(J_T\) is a disjoint union of paths.

For one such path with state vertices \(e_1,\ldots,e_{\ell+1}\) and successive turn centers \(b_1,\ldots,b_\ell\), the middle-label independence gives \(b_i\ne b_{i+1}\), hence each intermediate state \(e_{i+1}\) has endpoints \(b_i,b_{i+1}\). Taking the other endpoints of the first and last states gives an edge trail in \(K_n\). As its state edges belong to the forest \(S(T)\), no original vertex repeats: otherwise the trail would contain a graph cycle. It is therefore a simple path whose consecutive triple windows are the selected turns. Summing \(\ell+1\) state vertices over its \(c\) disjoint line-graph components gives \(|S(T)|=|T|+c\). Graphic independence bounds this by \(n-1\), proving (1). \(\square\)

**Corollary 2 (complete Hamiltonian window recognition).** A \(0/1\) set \(T\subseteq\mathcal T_n\) is the family of consecutive triple reversal-orbits of a Hamiltonian vertex word if and only if
\[
\boxed{|T|=n-2,\quad\text{its middle labels are distinct},\quad
S(T)\in\mathcal I(M(K_n)).}\tag{2}
\]
No separate global cut-connectivity condition is needed at this integral maximal cardinality.

*Proof.* Necessity follows from a Hamiltonian word: the middle labels are its \(n-2\) internal vertices, and its \(n-1\) consecutive \(K_n\) edges form a spanning tree. For sufficiency, Theorem 1 gives \(n-2+c=|S(T)|\le n-1\), so \(c=1\). Thus \(J_T\) is one simple path on \(n-1\) edge states. Its lift is a simple \(K_n\) path with \(n-1\) edges, hence Hamiltonian. \(\square\)

This proves that a *full-rank* middle-partition selection with graphic-independent state support automatically satisfies the connectivity and incidence requirements absent from the bare Smith lattice and uniform-matroid base polytope. Both resource tests are necessary: several selected turns of the same center can form a line-graph star despite an underlying forest, while a repeated original vertex gives a graphic circuit despite distinct middle labels.

**Theorem 3 (complete single-turn augmentation test).** Let \(T\ne\varnothing\) be resource-feasible with \(|T|<n-2\), and let \(B=(V,S(T))\) be its underlying forest. There exists \(t\notin T\) such that \(T\cup\{t\}\) remains resource-feasible if and only if at least one of the following holds:

1. \(B\) is disconnected on \(V\); or
2. \(B\) is a spanning tree having a vertex \(b\) of degree at least two which is not yet used as the middle label of any turn in \(T\).

*Proof.* If \(B\) is disconnected, choose a leaf \(b\) in a nontrivial tree component, and let \(ab\in S(T)\) be its incident edge. Since \(\deg_B(b)=1\), no selected turn is centered at \(b\). Choose \(c\) in another component. The new turn \([a,b,c]\) has unused middle label \(b\), and its activated edge \(bc\) joins two forest components; adding it preserves graphic independence.

If \(B\) is a spanning tree and \(b\) is an unused center with two incident tree edges \(ab,bc\), the turn \([a,b,c]\) adds no new state edge to \(S(T)\), preserves middle-label independence, and is not already selected. It therefore augments \(T\).

Conversely, when \(B\) is a spanning tree no new underlying \(K_n\) edge can be activated without creating a cycle. Any added turn must use two edges already in \(B\), so its center must have tree degree at least two; distinct middle labels require it to be unused. \(\square\)

**Corollary 4 (failure of ordinary matroid augmentation).** The hereditary family of resource-feasible turn sets does not satisfy the matroid augmentation axiom. For every \(n\ge5\), consider the two simple \(K_n\) paths
\[
P_1=(0,1,2),\qquad P_2=(3,2,4,5,\ldots,n-1)
\]
and let \(T\) be the union of their respective triple-window orbit sets. Its middle centers are \(1,2,4,5,\ldots,n-2\), all distinct, and its state-edge support is the spanning tree
\[
01,\ 12,\ 23,\ 24,\ 45,\ 56,\ldots,(n-2)(n-1).
\]
It has \(n-3\) selected turns. The unused centers are precisely the three leaves \(0,3,n-1\), so by Theorem 3 it admits no single-turn augmentation, even though Hamiltonian triple sets of cardinality \(n-2\) exist. In dimension five the obstruction is simply \(T=\{[0,1,2],[3,2,4]\}\).

We next quantify how much of a resource-feasible turn forest can survive in one Hamiltonian vertex word. For a reversal-odd boundary coloring \(b\), let \(\operatorname{sw}_b(P)\) be the number of color changes between successive triple windows of a simple word \(P\). Reversing the word complements and reverses the triple-color sequence, so its switch count is unchanged. Accordingly every component of \(J_T\) has an unambiguous switch count \(s_b(Q)\), independent of which direction is used to read its corresponding simple \(K_n\) path.

**Theorem 5 (cost-controlled forest-to-Hamiltonian completion).** Let \(T\ne\varnothing\) be resource-feasible with \(m=|T|=n-2-\delta\), \(\delta\ge0\), and components \(Q_1,\ldots,Q_c\) of \(J_T\). There is a Hamiltonian vertex word \(P\) satisfying
\[
\boxed{\operatorname{sw}_b(P)
\le\sum_{i=1}^{c}s_b(Q_i)+6\delta.}\tag{3}
\]
Moreover, if each component is monochromatic (possibly with different colors before choosing its direction), there is a Hamiltonian word \(P\) with
\[
\boxed{\operatorname{sw}_b(P)\le4\delta.}\tag{4}
\]
The construction uses at most \(2\delta+1\) surviving vertex-disjoint path pieces; at least \(m-3\delta\) original turn windows remain as internal windows of those pieces, with a negative bound interpreted as vacuous.

*Proof.* Let \(h\) be the number of nontrivial connected components of the \(K_n\) forest \(B=(V,S(T))\), and let \(u\) count isolated vertices of \(B\). By Theorem 1, each line-graph component \(Q_i\) lifts to a simple \(K_n\) path \(P_i\), and the sum of the numbers of vertex occurrences across these \(c\) paths is \(m+2c\). The forest \(B\) has \(|S(T)|=m+c\) edges and \(m+c+h\) nonisolated vertices, so the number of repeated vertex occurrences among \(P_1,\ldots,P_c\), beyond one occurrence per original vertex, is
\[
r=(m+2c)-(m+c+h)=c-h.\tag{5}
\]
Assign every original vertex occurring in the paths to one owning occurrence and delete its other \(r\) occurrences. Deleting a vertex from a path word splits it into at most two contiguous subwords, increasing the number of pieces by at most one. After these deletions all surviving subwords are vertex-disjoint, and adding the \(u\) missing vertices as singleton words produces at most
\[
q\le c+r+u=2c-h+u=n-m+c-2h\tag{6}
\]
pieces which together use every original vertex precisely once. The bound \(m+c\le n-1\), combined with \(h\ge1\), gives \(c\le\delta+1\) and
\[
\boxed{q\le2\delta+1.}\tag{7}
\]
Each removed vertex occurrence belongs to at most three original triple windows, so at least \(m-3r\ge m-3\delta\) selected turn windows survive within the pieces.

Orient each remaining piece consistently with its original \(P_i\), and concatenate all \(q\) pieces arbitrarily into a Hamiltonian word. A triple window wholly contained inside one piece retains its original color and any switch between consecutive such windows was already counted in \(\sum_i s_b(Q_i)\). Only windows crossing a piece boundary are new; at most two triple windows cross any given boundary. Every new switch comparison is incident to one of these crossing windows, and for each boundary at most three comparisons need to be counted. Thus at most \(3(q-1)\) new changes arise. This proves
\(\operatorname{sw}_b(P)\le\sum_i s_b(Q_i)+3(q-1)
\le\sum_i s_b(Q_i)+6\delta\), establishing (3).

If each original component \(Q_i\) has constant color, reverse individual paths before trimming them so all internal triple windows of all pieces have the same prescribed color \(\epsilon\); reversal-oddness makes this possible. All triple windows not crossing a join then have color \(\epsilon\). The crossing-window indices form a union of at most \(q-1\) intervals, each of length at most two. Any assignment of the other color to positions in a union of such intervals creates at most \(q-1\) maximal runs of non-\(\epsilon\) colors: an interval of length at most two can add at most one such run. Every run contributes at most two color changes. Hence \(\operatorname{sw}_b(P)\le2(q-1)\le4\delta\), proving (4). \(\square\)

**Theorem 6 (constant-factor matroidal rank-deficiency principle).** For every reversal-odd boundary 3-tournament \(b\), define
\[
R(b)=\max\{|T|: T\subseteq\mathcal T_n
\text{ resource-feasible, and each path component of }J_T
\text{ has constant triple color}\},
\]
and set
\[
\delta(b)=n-2-R(b),\qquad
\mu(b)=\min_{\pi\in S_n}\operatorname{sw}_b(\pi).
\]
Then for every \(n\ge4\),
\[
\boxed{\delta(b)\le\mu(b)\le4\delta(b).}\tag{8}
\]

*Proof.* Take a Hamiltonian word attaining \(s=\mu(b)\) switches and delete the right-hand triple window at each switch of its triple-color sequence. At most \(s\) windows are removed; the remaining selected turns form a resource-feasible subset of its original Hamiltonian line-graph path, and every surviving component has constant color. Thus \(R(b)\ge n-2-s\), or \(\delta(b)\le\mu(b)\).

Conversely, choose a maximizing \(T\) of size \(R(b)=n-2-\delta(b)\). By Theorem 5's monochromatic completion (4), there is a Hamiltonian word with at most \(4\delta(b)\) changes. Minimizing over all words yields \(\mu(b)\le4\delta(b)\). \(\square\)

**Interpretation.** The Hamiltonian switch minimization problem is, up to a universal factor four, equivalent to maximizing the rank of a *monochromatic forest of graphic-independent triple turns with distinct centers*. The two independence systems are necessary, but their intersection on the turn ground set is not itself a matroid: Theorem 3 supplies an obstruction to single-element augmentation. A promising stronger approach is to seek a **multi-exchange augmenting principle** for this resource system under the monochromatic-component constraint. An increase in \(R(b)\) immediately reduces the quantitative ceiling (8), and finding \(R(b)\ge n-2-o(\sqrt n)\) would produce a Hamiltonian word with \(o(\sqrt n)\) switches and hence a monochromatic tight subpath of length \(\omega(\sqrt n)\). This remains conjectural. The new theorems do not settle an unrestricted long-monochromatic-path conjecture, but reduce its asymptotic strengthening to a near-basis rank statement in a structured matroidal path-forest system.

**Independent finite check.** Enumerating every subset of \(n-2\) turn orbits and applying the two independence tests gives, in dimensions \(n=4,5,6\), respectively \(12,60,360\) feasible sets and no non-Hamiltonian sets. These counts agree with the \(n!/2\) unoriented Hamiltonian words; the proofs are dimension-independent and do not rely on the enumeration.

#### A legal, cost-controlled augmenting exchange

Orient each edge of the turn graph \(L(K_n)\) according to the reversal-odd coloring \(b\). The turn from edge-state \(ab\) to \(bc\) is oriented in that direction when \(b(a,b,c)=1\), and the other direction otherwise.

**Lemma 7 (local orientation energy).** For any resource-feasible turn set \(T\), put \(d_b(e,T)=1\) if an edge-state \(e\in S(T)\) has two selected turns that both point into it or both point out of it, and zero otherwise. Then
\[
\boxed{K_b(T)=\sum_{e\in S(T)}d_b(e,T)
=\sum_{Q\text{ component of }J_T}\operatorname{sw}_b(Q).}\tag{9}
\]
*Proof.* Along a component path, consecutive triple colors differ precisely when both corresponding directed turn edges have the same incoming or outgoing incidence at their common state. Reversal of the path complements and reverses its color word, preserving this count. \(\square\)

**Theorem 8 (one-for-two augmentation with at most three new switches).** For \(n\ge5\), every nonempty resource-feasible \(T\) with \(|T|<n-2\) can be replaced by a resource-feasible \(T'\) satisfying
\[
\boxed{|T'|=|T|+1,\quad |T\setminus T'|\le1,\quad
|T'\setminus T|\le2,\quad K_b(T')\le K_b(T)+3.}\tag{10}
\]
The result holds for every reversal-odd boundary coloring \(b\).

*Proof.* Write \(B=(V,S(T))\) for the original-vertex forest. If \(B\) is disconnected, choose a leaf \(u\) in a nontrivial tree component, its neighbor \(a\), and a vertex \(w\) in another component. Add the turn \([a,u,w]\). This joins forest components through the new state-edge \(uw\), uses a fresh middle label \(u\), and creates at most one local orientation defect at the old edge-state \(au\).

If \(B\) is spanning and has an unused middle label \(u\) with tree degree at least two, add the turn between two tree edges incident with \(u\). State support is unchanged, middle independence persists, and at most two orientation defects are created, because neither of the two involved line-graph states had degree exceeding one.

Otherwise \(B\) is a spanning tree whose unused middle labels are all leaves. Since \(|T|<n-2\), the tree has a branching vertex \(v\) of degree at least three: if it were a Hamiltonian path, all its internal vertices would already be selected middle labels, giving \(|T|\ge n-2\). The unique turn centered at \(v\) involves two of its incident edges. Choose a third tree edge \(vc\), absent from that turn. This state-edge must belong to the unique turn \(t_c\) centered at \(c\), so \(c\) is an internal tree vertex and the line-graph degree of state \(vc\) is one.

Choose a leaf \(u\) in the branch of \(B-v\) containing \(c\), and a leaf \(w\) in another branch. Write \(a\) for the tree neighbor of \(u\) and \(d\) for that of \(w\). The edge \(vc\) belongs to the tree path from \(u\) to \(w\), away from their leaf edges. Define
\[
\boxed{T'=(T\setminus\{t_c\})\cup\{[a,u,w],[u,w,d]\}.}\tag{11}
\]
Both inserted centers \(u,w\) were previously unused. Deleting \(t_c\) removes state \(vc\), since no other selected turn uses it. Consequently
\[
S(T')\subseteq(S(T)\setminus\{vc\})\cup\{uw\}.\tag{12}
\]
The latter set is a tree: the new chord \(uw\) creates a fundamental cycle in \(B\), and \(vc\) lies on that cycle. Thus graphic independence holds, and the new middle labels are distinct. We removed one turn and inserted two, so the selected rank grew by one.

Removing \(t_c\) creates no orientation defect. Before inserting the two new turns, the old states \(au,dw\) each have line-graph degree at most one, because the leaves \(u,w\) were unused centers; the new state \(uw\) has degree zero. The two new turns can create at most one defect at each of \(au,dw,uw\), hence at most three in total. This proves the theorem. \(\square\)

**Corollary 9 (factor-three comparison).** With the maximum monochromatic feasible-forest rank \(R(b)\), rank deficit \(\delta(b)=n-2-R(b)\), and minimum Hamiltonian switch count \(\mu(b)\) defined earlier, every \(n\ge5\) satisfies
\[
\boxed{\delta(b)\le\mu(b)\le3\delta(b).}\tag{13}
\]
*Proof.* The lower inequality is Theorem 6: from an \(s\)-switch Hamiltonian word delete the right-hand triple at each switch, retaining at least \(n-2-s\) turns partitioned into monochromatic components. For the upper inequality, start from an optimal monochromatic feasible forest \(T\), with \(K_b(T)=0\). Apply Theorem 8 a total of \(\delta(b)\) times. The final turn set has \(n-2\) edges and is Hamiltonian by Corollary 2. Its cost rose by at most three per augmentation, giving \(\mu(b)\le3\delta(b)\). \(\square\)

**Corollary 10 (cost-stable full-rank extension).** Iterating the theorem \(n-2-|T|\) times extends any nonempty feasible set to a Hamiltonian turn set, deleting at most one and adding at most two turns per step, and gives
\[
\boxed{K_b(T_*)\le K_b(T)+3(n-2-|T|).}\tag{14}
\]

This proves a legal, rank-increasing and dimension-independent cost-Lipschitz exchange theorem for the two-resource gallery. Its bound does not force successive cost increases to cancel. The remaining open objective is to obtain a stronger color-compatible augmentation principle that keeps the final cost sublinear or bounded.

### Two-color Kneser stability and sharp middle-rank reachability bounds

#### 1. Uniform two-color Kneser upper bound

Let \(n=2k+1\), \(k\ge2\), and let \(\mathcal F\subseteq\binom{[n]}k\) be a vertex family whose induced disjointness graph in the Kneser graph \(KG(n,k)\) is bipartite.

**Theorem 1 (two-color Kneser bound).** Every such family satisfies
\[
\boxed{
|\mathcal F|\le
\max\left\{
\binom{2k}{k-1}+\binom{2k-1}{k-1},
\quad
2\binom{2k}{k-1}-2(k-1)
\right\}.
}
\tag{1}
\]
In particular the upper bound is \(7\) when \(n=5\), and \(26\) when \(n=7\).

*Proof.* A proper bipartition writes \(\mathcal F=\mathcal A\sqcup\mathcal B\), where \(\mathcal A\) and \(\mathcal B\) are disjoint intersecting families of \(k\)-subsets.

If \(\mathcal A\) has a common coordinate \(i\), it lies in the full star \(\mathcal S_i=\{S:i\in S\}\). Of the members of \(\mathcal B\), those also containing \(i\) lie in this star; those avoiding \(i\) form an intersecting family of \(k\)-subsets on \(2k\) points. Erdős–Ko–Rado bounds the latter by \(\binom{2k-1}{k-1}\). Thus
\[
|\mathcal F|\le|\mathcal S_i|+
|\{B\in\mathcal B:i\notin B\}|
\le\binom{2k}{k-1}+\binom{2k-1}{k-1}.
\]
The same argument applies with the classes reversed.

If neither color class has a common coordinate, the Hilton–Milner theorem bounds each by
\[
\binom{2k}{k-1}-\binom{k}{k-1}+1
=\binom{2k}{k-1}-k+1.
\]
Adding the two bounds proves (1). For empty classes, applying Erdős–Ko–Rado or Hilton–Milner to the nonempty class is no weaker. \(\square\)

**Corollary 2 (NORI1 middle-layer obstruction).** Let \(c\) be an antipodally odd undirected cube-edge coloring, and let \(R_x^\varepsilon\) be the coordinate subsets reachable from root \(x\) by a monochromatic geodesic of color \(\varepsilon\). If the coloring has no full monochromatic antipodal geodesic, then for every root \(x\),
\[
\mathcal F_x=(R_x^0\cup R_x^1)\cap\binom{[n]}k
\]
obeys (1). In particular \(|\mathcal F_x|\le7\) for \(Q_5\), and \(|\mathcal F_x|\le26\) for \(Q_7\).

*Proof.* Article VII's color-free reachability odd-cycle theorem shows that, absent a full monochromatic antipodal geodesic, the induced Kneser disjointness graph on \(\mathcal F_x\) must be bipartite: an edge joins two disjoint \(k\)-sets covering all but one coordinate, and two same-colored monochromatic arms at such endpoints would produce a monochromatic near-full geodesic, which extends to a full one by antipodal oddness. Every support incident to a disjointness edge then has a uniquely forced witness color, giving a proper bipartition. Apply Theorem 1. \(\square\)

The bound is necessary for a counterexample, not sufficient for a witness: a single rooted family may attain equality without any monochromatic geodesic of length \(n-1\) from that root.

#### 2. Sharpness and rigidity for dimensions five and seven

For \(n=5\), the union of the full stars of two distinct coordinates among two-element subsets has seven distinct members. Its disjointness graph is bipartite, assigning each support to one of the two stars, so the bound seven is sharp for the abstract Kneser problem.

For \(n=7\), partition the seven labels into a three-element set \(T\) and four-element set \(Q\), and fix \(q\in Q\). Put
\[
\begin{aligned}
\mathcal A&=\{S\in\tbinom{[7]}3:|S\cap T|\ge2\},\\
\mathcal B&=\{S\in\tbinom{[7]}3:q\in S,\ 
S\cap(Q\setminus\{q\})\ne\varnothing\}\cup\{Q\setminus\{q\}\}.
\end{aligned}
\tag{2}
\]
These are disjoint intersecting families, each of cardinality thirteen. Therefore their union realizes the upper bound twenty-six.

**Theorem 3 (classification of sharp seven-point Kneser families).** Every induced-bipartite family \(\mathcal F\subseteq\binom{[7]}3\) of size twenty-six admits a bipartition into two disjoint thirteen-element nontrivial intersecting families. Up to relabeling, there are precisely two possibilities:
\[
\begin{array}{ll}
\text{(I)}&J(T)\sqcup J(U),\quad T\cap U=\varnothing;\\
\text{(II)}&H(c;T)\sqcup J([7]\setminus(T\cup\{c\})),
\end{array}
\tag{3}
\]
where
\[
J(T)=\{S\in\tbinom{[7]}3:|S\cap T|\ge2\},\qquad
H(c;T)=\{T\}\cup\{\{c,a,b\}:\{a,b\}\cap T\ne\varnothing\},
\]
with \(|T|=3\) and \(c\notin T\). There are seventy labeled unordered pairs of type (I) and one hundred forty of type (II), for a total of
\[
\boxed{210\text{ labeled extremal pairs, in two permutation orbits}.}
\tag{4}
\]

*Proof.* The common-coordinate case in Theorem 1 gives at most \(15+10=25\), so a twenty-six-member family must have two nontrivial intersecting color classes. Hilton–Milner bounds each by thirteen, hence each attains equality.

The equality classification for nontrivial intersecting triple families on seven labels has two forms: the triangle-majority family \(J(T)\), or the canonical Hilton–Milner family \(H(c;T)\). Both have thirteen members, and there are respectively \(\binom73=35\) and \(7\binom63=140\) labeled families.

Two majority families \(J(T),J(U)\) are disjoint precisely when the indexing triples \(T,U\) are disjoint. Indeed, if \(T\cap U\ne\varnothing\), choose two points of \(T\) and two of \(U\), using their shared point so that the resulting three-element set has at least two in each. Conversely, no three-set can contain two elements from each of disjoint three-sets. Thus the number of unordered disjoint majority pairs is \(\binom73\binom43/2=70\).

A canonical family \(H(c;T)\) is disjoint from a majority family \(J(U)\) precisely when \(U=[7]\setminus(T\cup\{c\})\). If \(U\) avoids the four-point set \(T\cup\{c\}\), members of \(H(c;T)\) contain at most one point of \(U\). Conversely, if \(U\) contains two points of \(T\), it lies with a suitable third point in \(J(U)\cap H(c;T)\); if \(U\) contains \(c\) and any point of \(T\), choose a triple containing both and a further point of \(U\); the remaining configurations likewise supply a triple of \(H(c;T)\) with two members of \(U\). Hence there is one disjoint majority family for each of the \(140\) canonical families.

Two canonical families cannot be disjoint. If their centers coincide, a triple containing the center and meeting both exceptional triples belongs to both. If their centers \(c,d\) differ, a triple \(\{c,d,a\}\) belongs to both provided \(\{d,a\}\) meets the first exceptional triple and \(\{c,a\}\) meets the second. Such \(a\) exists unless both exceptional triples are disjoint and exclude both centers, which is impossible for distinct \(c,d\) on seven labels. This proves the two types and their counts. \(\square\)

The sharp configuration classification describes a **single root's** Kneser layer only. It does not imply the global existence of a counterexample to NORI1.

Let \(G=(V,E)\) be a finite simple graph with at least one edge, and let \(N\) be a matroid on \(E\). Assume
\[
\tag{1}
\mathcal I(N)\subseteq\mathcal I(M(G)),\qquad
\delta_G(v)\in\mathcal I(N)\quad(v\in V),
\]
where \(M(G)\) is the graphic matroid and \(\delta_G(v)\) is the star at \(v\). At each vertex \(v\), prescribe an arbitrary tournament \(T_v\) on \(\delta_G(v)\). A vertex word \(P=(v_1,\ldots,v_\ell)\) is an *independent tournament path* when its consecutive edges are pairwise distinct, their set is independent in \(N\), and
\[
v_{i-1}v_i\longrightarrow v_iv_{i+1}\quad\text{in }T_{v_i}
\qquad(2\le i<\ell).
\]
Condition (1) implies that an independent tournament path has distinct vertices. Indeed, a closed subwalk with pairwise distinct edges contains a graph cycle, contradicting independence in \(N\).

**Theorem (matroid terminal-growth bound).** Let \(L\) be the maximum number of vertices in an independent tournament path, and let \(\bar d=2|E|/|V|\). Then
\[
\boxed{\quad\frac{\bar d}{2}\le(L-1)^2,\qquad
L\ge1+\sqrt{\frac{\bar d}{2}}.\quad}\tag{2}
\]
The bound holds for arbitrary matroids \(N\), including nonrepresentable matroids.

*Proof.* For every \(e=uv\in E\), let \(r(e)\) be the maximum order of an independent tournament path ending in either \(u,v\) or \(v,u\). Orient \(e\) toward the last vertex of one maximizing path. Some vertex \(v\) receives at least \(\bar d/2\) oriented edges. For \(2\le r\le L\), write \(D_r(v)\) for the incoming edges with \(r(e)=r\), and let \(q=|D_r(v)|\).

For \(q>0\), choose \(e=uv\in D_r(v)\) which beats at least \((q-1)/2\) other members of \(D_r(v)\) in \(T_v\). Let \(P\) be an independent tournament path of order \(r\) ending in \(u,v\), and put \(A=E(P)\). Then \(r_N(A)=r-1\). If \(f=vw\in D_r(v)\) is beaten by \(e\) and \(f\notin\operatorname{cl}_N(A)\), the word obtained by appending \(w\) to \(P\) has independent edge set \(A\cup\{f\}\). By (1), this set is a forest; consequently \(w\) is new to \(P\). The tournament comparison at \(v\) is legal, so the new word is an independent tournament path of order \(r+1\), contradicting \(r(f)=r\).

Thus every member of \(D_r(v)\) beaten by \(e\) belongs to \(\operatorname{cl}_N(A)\). Since \(\delta_G(v)\) is independent in \(N\),
\[
\bigl|\delta_G(v)\cap\operatorname{cl}_N(A)\bigr|
\le r_N(A)=r-1.
\]
One of these edges is \(e\). Hence \((q-1)/2\le r-2\), giving \(q\le2r-3\). Summing over terminal ranks yields
\[
\frac{\bar d}{2}\le d^-(v)
=\sum_{r=2}^{L}|D_r(v)|
\le\sum_{r=2}^{L}(2r-3)
=(L-1)^2.
\]
This proves (2). \(\square\)

**Transitive refinement.** If every \(T_v\) is transitive, then
\[
\boxed{\quad \bar d\le L(L-1),\qquad
L-1\ge\frac{\sqrt{1+4\bar d}-1}{2}.\quad}\tag{3}
\]

*Proof.* In the preceding proof, the tournament induced on \(D_r(v)\) has a vertex beating all \(q-1\) others. Thus \(q-1\le r-2\), so \(q\le r-1\). Summing gives
\[
\bar d/2\le\sum_{r=2}^{L}(r-1)=L(L-1)/2.
\]
Solving this quadratic proves (3). \(\square\)

**Corollary 1 (ordinary reversal-odd boundary tournaments).** Let \(b(a,v,c)\in\{0,1\}\) satisfy \(b(c,v,a)=1-b(a,v,c)\) on distinct triples from an \(n\)-element set. Take \(G=K_n\), \(N=M(K_n)\), and orient the local tournament \(T_v\) by
\[
av\longrightarrow vc\quad\Longleftrightarrow\quad b(a,v,c)=1.
\]
Every independent tournament path is a vertex-simple monochromatic tight path of color one, and conversely. Thus there is such a path on at least
\[
\boxed{1+\sqrt{(n-1)/2}}\tag{4}
\]
vertices, with integer rounding understood.

*Proof.* Every vertex star of \(K_n\) is a forest, hence independent in its graphic matroid. The condition on \(b\) says precisely that the comparisons at each vertex form a tournament. Along an independent tournament path every triple color is one; ordinary graph paths have independent edge sets in \(M(K_n)\). Apply the theorem with \(\bar d=n-1\). \(\square\)

**Corollary 2 (cube geodesics with at most one switch).** For every binary coloring \(c\) of the edges of \(Q_n\), there exists a coordinate-distinct geodesic of length at least
\[
\boxed{\left\lceil\frac{\sqrt{4n+1}-1}{2}\right\rceil}\tag{5}
\]
whose edge-color word is weakly increasing. In particular it has at most one color change, and this applies to every NORI1 coloring.

*Proof.* On \(E(Q_n)\), let \(N\) be the partition matroid with capacity one in each parallel-coordinate class. Its independent edge sets use each direction at most once, hence contain no graph cycle. At each cube vertex, the \(n\) incident edges use distinct directions, so the whole star is independent. Order each local star with all color-zero edges preceding color-one edges, resolving ties arbitrarily, and let \(T_v\) be the resulting transitive tournament. A path independent in \(N\) uses distinct coordinate directions and is therefore a geodesic. Along every admissible path, the colors are weakly increasing. The chosen local tournaments are transitive, so apply (3) with \(\bar d=n\). \(\square\)

The common mechanism is a rank obstruction to extending a maximum terminal path: a rank-\((r-1)\) flat meets an independent vertex star in at most \(r-1\) edges. In the boundary model, the resource matroid is graphic. In the cube model, it is a coordinate partition matroid subordinate in independence to the graphic matroid of the cube. This supplies one intrinsic matroidal proof of the square-root scale in both models and improves the weaker proper-label cube estimate obtained by separately charging repeated vertices and directions. The passage from a partial low-switch cube geodesic to a full monochromatic antipodal geodesic remains open; (1) alone does not encode antipodal color polarization.

### Fundamental-circuit pivots, dual-basis sweeps, and faithful ordered exchanges

Let \(M\) be a finite loopless matroid on \(E\), and let \(\Gamma(M)\) denote its basis-exchange graph. For an oriented edge \(B\to B'=B-a+e\), let \(C_M(e,B)\) be the fundamental circuit of \(e\) with respect to \(B\). The circuit contains \(a,e\), since replacing \(a\) by \(e\) gives a basis.

**Theorem 1 (canonical pivot of a small fundamental circuit).** Suppose every circuit of \(M\) has cardinality at most three. Each oriented basis exchange \(B\to B-a+e\) admits a unique intrinsic label of one of the following types:
\[
\begin{array}{ll}
\text{parallel exchange:}& C_M(e,B)=\{a,e\};\\
\text{triangular exchange:}& C_M(e,B)=\{a,b,e\},\quad
b\in B\cap B'.
\end{array}
\tag{1}
\]
In the triangular case the ordered triple \((a,b,e)\) is determined by the oriented exchange and the matroid. Reversing the exchange changes it to \((e,b,a)\). The labels are preserved by every matroid isomorphism.

*Proof.* The element \(e\) is outside \(B\), and a fundamental circuit contains \(e\) together with at least one element of \(B\). Because \(B-a+e\) is independent, \(a\) is in this circuit. The size bound gives the two displayed possibilities; in the size-three case the third element \(b\) belongs to \(B\setminus\{a\}=B\cap B'\). Fundamental circuits are unique. For the reverse exchange \(B'\to B\), the fundamental circuit of \(a\) with respect to \(B'\) is the same circuit: its removal of \(e\) restores the basis, and its removal of \(b\) also yields a basis by the fundamental-circuit exchange criterion. The description is matroid-theoretic and therefore commutes with isomorphisms. \(\square\)

The theorem identifies the local middle element of a boundary triple as a *fundamental-circuit pivot*. It also identifies a cubical coordinate exchange with a two-element fundamental circuit. No auxiliary ordering of the retained basis elements is used in either case.

**Theorem 2 (faithfulness rigidity for uniform sliding windows).** Fix \(1\le r<n\). Map an injective ordered \((r+1)\)-tuple
\[
(a,x_1,\ldots,x_{r-1},e)
\]
to the oriented basis exchange
\[
\{a,x_1,\ldots,x_{r-1}\}
\longrightarrow
\{x_1,\ldots,x_{r-1},e\}
\tag{2}
\]
of \(U_{r,n}\). Every oriented edge of \(\Gamma(U_{r,n})=J(n,r)\) has precisely \((r-1)!\) preimages. Hence an oriented exchange determines its ordered sliding window if and only if \(r\le2\).

For \(r=2\), arbitrary reversal-odd boundary 3-tournaments on \([n]\) are in bijection with orientations of \(J(n,2)\): orient the edge
\[
\{a,b\}\longrightarrow\{b,e\}
\]
when \(b(a,b,e)=1\). Every orientation of \(J(n,2)\) arises. For \(r\ge3\), some reversal-odd ordered-\((r+1)\)-window colorings cannot descend to orientations of the basis-exchange graph.

*Proof.* The ordered source and target bases in (2) recover \(a\) as their deleted element, \(e\) as their inserted element, and the unordered set \(X=B\cap B'\) of their \(r-1\) retained elements. The preimages are precisely the permutations of \(X\). This gives the factorial and the characterization \(r\le2\). When \(r=2\), the sole retained element is \(b\), and reversing the graph edge reverses \((a,b,e)\). Thus the reversal-odd identity specifies one orientation of each undirected graph edge with no further compatibility conditions. When \(r\ge3\), choose two different permutations of \(X\) and give their windows different binary colors; assign the complementary colors to their reversed windows, then fill the remaining reversal orbits arbitrarily. The coloring is reversal-odd but assigns different colors to the same directed exchange, so it does not descend. \(\square\)

**Theorem 3 (dual-basis permutation sweeps).** In both canonical models the colored states along a complete path admit distinct intrinsic resource labels forming one basis of the dual matroid.

(i) Let \(M=\bigoplus_{i=1}^kU_{1,2}\). Every dual basis \(D\) has complementary primal basis \(B=E\setminus D\). For each permutation \(d_1,\ldots,d_k\) of \(D\), let \(B_j\) arise from \(B_{j-1}\) by exchanging its element parallel to \(d_j\) for \(d_j\). Then
\[
B=B_0,B_1,\ldots,B_k=D
\tag{3}
\]
is an antipodal geodesic of the \(k\)-cube. Its \(k=r(M^*)\) exchange edges have distinct two-element-circuit labels indexed by \(D\); every antipodal geodesic from \(B\) is obtained from one such permutation.

(ii) Let \(M=U_{2,n}\), \(n\ge3\). Every dual basis \(D\) has complementary primal basis \(\{s,t\}\). For each permutation \(d_1,\ldots,d_{n-2}\) of \(D\), the word
\[
(s,d_1,\ldots,d_{n-2},t)
\tag{4}
\]
defines a path in \(J(n,2)\) through its consecutive unordered pairs. Its \(n-2=r(M^*)\) oriented exchanges are labeled, in order, by the distinct triangular-circuit pivots \(d_1,\ldots,d_{n-2}\). Conversely, the original-element Hamiltonian tight words with endpoints \(s,t\) are precisely (4).

In both instances, the reversal operation on complete paths acts on the corresponding color words by
\[
w\longmapsto\overline{\operatorname{rev}(w)}.
\tag{5}
\]

*Proof.* The complement of a primal basis is a dual basis. In (i), each \(d_j\) belongs to a different parallel pair, so all exchanges are legal and no pair is toggled twice. A path from \(B\) to \(E\setminus B\) has length at least \(k\), and equality forces every pair to be toggled once. In (ii), consecutive unordered pairs of the displayed word intersect in the single middle element; every pair is a basis and every original vertex appears once. The ordered-triple labels are its successive windows, whose middle elements are precisely the members of \(D\). Conversely, a Hamiltonian tight word determines its two endpoints and the order of its interior elements. The reversal of a boundary word reverses and complements each triple label by reversal oddness. For the cube, reverse the geodesic and apply the canonical complementation map to every basis; the antipodal odd edge rule complements the reversed sequence of edge colors. This proves (5). \(\square\)

**Corollary 4 (the common resource parameter).** The natural number of primitive colored states of a complete gallery is
\[
\boxed{r(M^*)=|E(M)|-r(M)}
\tag{6}
\]
in both canonical models: \(k\) for the cube and \(n-2\) for the boundary tournament. The canonical exchange label is an inserted element in (i) and a retained fundamental-circuit pivot in (ii). For uniform rank \(r\ge3\), the underlying oriented basis-exchange graph alone loses \((r-1)!\)-fold ordered-window information.

This identifies a common matroidal resource budget and a choice-free source of its local exchange labels. It leaves two additional ingredients to a path-existence theorem: a compatible global polarity of colored exchange states, and a rank-increasing exchange rule that preserves a coherent path with distinct resources. In the cube the antipode acts on bases; in uniform rank two, reversal acts on directed exchanges. The two actions have different domains, and the colored signed-cover matroid requires the additional gallery information developed elsewhere in Article XI.

Let \(M\) be a finite matroid of rank \(r\ge1\) on a ground set \(E\), with \(N=|E|\). Write \(\mathcal B(M)\) for its bases and \(\mathcal I_{r-1}(M)\) for its independent \((r-1)\)-sets. For each \(1\le j\le N-r\), choose an arbitrary binary coloring \(\beta_j\) of the oriented edges of the basis-exchange graph, satisfying
\[
\beta_j(B',B)=1-\beta_j(B,B')\qquad(B,B'\text{ adjacent}).\tag{1}
\]
A **sliding-window gallery** of order \(m\) is an injective word \(v_1,\ldots,v_m\), \(m\ge r\), for which each consecutive \(r\)-set
\[
B_i=\{v_i,\ldots,v_{i+r-1}\},\qquad1\le i\le m-r+1,
\]
is a basis. The gallery is **positive** if \(\beta_i(B_i,B_{i+1})=1\) for \(1\le i\le m-r\). The stage colorings \(\beta_i\) may vary independently.

**Theorem (terminal-set growth).** Let \(L\) be the maximum order of a positive sliding-window gallery. Then
\[
\boxed{|\mathcal B(M)|\le|\mathcal I_{r-1}(M)|(L-r+1)^2,\qquad
L\ge r-1+\sqrt{\frac{|\mathcal B(M)|}{|\mathcal I_{r-1}(M)|}}.}\tag{2}
\]
The conclusion requires neither representability nor simplicity nor an edge ordering.

*Proof.* Every basis supports a gallery of order \(r\), with no colored transitions. For each basis \(B\), let \(\ell(B)\) be the maximum order of a positive gallery terminating with the \(r\)-set \(B\). Choose such a gallery with final word \(x,s_1,\ldots,s_{r-1}\), and assign \(B\) to the independent set \(S=\{s_1,\ldots,s_{r-1}\}\). 

Fix an independent \((r-1)\)-set \(S\), an integer \(s\in\{r,\ldots,L\}\), and put
\[
U_{S,s}=\{x\notin S:S\cup\{x\}\text{ was assigned to }S,\ \ell(S\cup\{x\})=s\},\qquad q=|U_{S,s}|.
\]
If \(s=N\), then \(q\le N-r+1\le 2(s-r)+1\), so (3) follows immediately. Suppose henceforth that \(s<N\). The bases \(S\cup\{x\}\), \(x\in U_{S,s}\), form a complete exchange clique. Equation (1) makes \(\beta_{s-r+1}\) a tournament on this clique. Choose \(x\) having at least \((q-1)/2\) outgoing comparisons of color one. The selected \(s\)-element gallery for \(S\cup\{x\}\) ends in \(x,s_1,\ldots,s_{r-1}\). If an outgoing neighbor \(y\in U_{S,s}\) did not already occur in the gallery, appending \(y\) would preserve distinctness, add the valid basis window \(S\cup\{y\}\), and fulfill the prescribed positive stage comparison. This would give \(\ell(S\cup\{y\})\ge s+1\), a contradiction. Thus all favorable neighbors occur among the earlier \(s-r\) vertices, and
\[
(q-1)/2\le s-r,\qquad |U_{S,s}|\le2(s-r)+1.\tag{3}
\]
The number of bases assigned to \(S\) is at most
\[
\sum_{s=r}^{L}(2(s-r)+1)=(L-r+1)^2.
\]
Summing over all \(S\in\mathcal I_{r-1}(M)\) gives (2). \(\square\)

**Corollary 1 (uniform matroids of every rank).** For \(1\le r<n\), every reversal-odd coloring of oriented exchanges of \(U_{r,n}\) admits a positive injective sliding-window gallery with
\[
\boxed{L\ge r-1+\sqrt{\frac{n-r+1}{r}}.}\tag{4}
\]
The assertion remains valid for independently chosen reversal-odd colorings at every stage.

*Proof.* In \(U_{r,n}\), all \(r\)-sets are bases and all \((r-1)\)-sets are independent, so
\[
|\mathcal B|/|\mathcal I_{r-1}|=\binom nr/\binom n{r-1}=(n-r+1)/r.
\]
Apply (2). \(\square\)

When \(r=2\), \(S=\{b\}\) and the oriented exchange \(S\cup\{a\}\to S\cup\{c\}\) is the ordered triple \((a,b,c)\). Thus (4) is \(L\ge1+\sqrt{(n-1)/2}\), recovering the Devine--Milans terminal-pair theorem for every ordinary reversal-odd boundary 3-tournament. Its stage-dependent version recovers the layered terminal-pair extension in Article VII. For every fixed \(r\), (4) is a square-root lower bound with distinct original resources. The complete exchange clique above a codimension-one independent set is the shared local mechanism.

**Corollary 2 (cubical specialization and its limitation).** Let \(M_n=\bigoplus_{i=1}^nU_{1,2}\), so its basis graph is \(Q_n\). Designate one element in each parallel pair as zero, and let \(\varepsilon(B)\) count the other selected elements modulo two. For an arbitrary undirected-edge coloring \(c\) of \(Q_n\), define the stage-dependent oriented coloring
\[
\boxed{\beta_j(B,B')=c(\{B,B'\})+\varepsilon(B)+(j-1)\pmod2.}\tag{5}
\]
Every positive sliding-window gallery for (5) induces a monochromatic cube geodesic, using \(m-n\) different directions if the gallery has order \(m\).

*Proof.* Each basis window of length \(n\) chooses one element of every parallel pair. When the window shifts, its entering element must be the parallel mate of the departing element. The injective word therefore exchanges every pair at most once, so the basis windows trace a geodesic. Every basis exchange changes \(\varepsilon\) by one, giving \(\beta_j(B',B)=1-\beta_j(B,B')\). Along the gallery, \(\varepsilon(B_j)=\varepsilon(B_1)+(j-1)\), whence
\[
\beta_j(B_j,B_{j+1})=c(\{B_j,B_{j+1}\})+\varepsilon(B_1).
\]
Positivity makes the traversed cube edges monochromatic. \(\square\)

For this cubical matroid, however,
\[
\frac{|\mathcal B(M_n)|}{|\mathcal I_{n-1}(M_n)|}
=\frac{2^n}{n2^{n-1}}=\frac2n.\tag{6}
\]
Therefore (2) offers no guaranteed positive exchange beyond the initial basis window, whereas a full antipodal geodesic requires gallery order \(2n\). In contrast, the ratio for \(U_{2,n}\) is \((n-1)/2\). The terminal-set method gives a common witness predicate and proves the tournament square-root estimate, while (6) pinpoints its inability to force the spanning cubical witness. A unified spanning theorem must supply an additional global exchange or antipodal-splicing principle beyond the terminal-set tournament comparison.

**Corollary 3 (parallel-factor law for terminal capacity).** For a loopless partition matroid \(M=\bigoplus_{j=1}^tU_{r_j,m_j}\) with \(r_j\ge1\), the terminal-set ratio in (2) obeys
\[
\boxed{\frac{|\mathcal B(M)|}{|\mathcal I_{r-1}(M)|}
=\left(\sum_{j=1}^{t}\frac{r_j}{m_j-r_j+1}\right)^{-1}.}\tag{7}
\]
*Proof.* An independent \((r-1)\)-set is obtained by choosing \(r_j-1\) elements in one summand \(j\) and bases in all others. Therefore
\[
|\mathcal I_{r-1}(M)|
=\sum_j \binom{m_j}{r_j-1}\prod_{\ell\ne j}\binom{m_\ell}{r_\ell}.
\]
Divide by \(|\mathcal B(M)|=\prod_\ell\binom{m_\ell}{r_\ell}\), and use \(\binom{m_j}{r_j-1}/\binom{m_j}{r_j}=r_j/(m_j-r_j+1)\). \(\square\)

The reciprocal terminal capacity is additive under direct sums. Thus the uniform rank-two model has one large rank-one contraction fiber, producing a square-root gain, whereas the cubical model has \(n\) small contraction fibers whose reciprocal contributions add to \(n/2\). This formula expresses quantitatively why terminal-fiber growth by itself cannot recover the cube's full antipodal geodesic.

### Intrinsic largest-clique incidence roots and a terminal-tournament path theorem

Let \(M\) be a finite matroid, let \(\Gamma(M)\) be its basis-exchange graph, and let \(\mathscr K(M)\) be the family of cliques of **maximum cardinality** in \(\Gamma(M)\). Construct the canonical bipartite incidence graph
\[
I(M)=\bigl(\mathcal B(M)\sqcup\mathscr K(M),\ \{BK:B\in K\}\bigr).
\]
An incidence side is called *thin* when every vertex on that side has degree two. Whenever \(I(M)\) is the edge-subdivision of a connected simple graph, denote the graph obtained by suppressing its thin side by \(G(M)\). This construction uses only the basis graph and its maximum cliques; it is invariant under matroid isomorphism.

#### Theorem 1 (three intrinsic root reconstructions)

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

#### Theorem 2 (terminal-tournament path transfer)

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

#### Interpretation and limitation

Both initial matroids lie in the intrinsic class for which the largest-clique incidence graph is a subdivision of a simple graph. Their thin sides, however, differ. In the rank-two uniform family, bases become *edges* of the root and their overlapping exchanges define arbitrary local tournaments. In the cubical family, largest cliques become *edges* of the root; the original two-color antipodal condition belongs to the root-edge data, with the coordinate classes recoverable from opposite edges of its squares.

Thus Theorem 2 supplies the quantitative square-root mechanism for the boundary family, while the cubical instance instead falls under the properly resource-labeled terminal-path theorem already established in Article VII. The latter provides a coordinate-distinct increasing geodesic of order at least \((5+\sqrt{1+4n})/4\), after locally ordering the two edge colors, but does not yield a full monochromatic antipodal geodesic. The incidence reconstruction is a common intrinsic geometry, not yet a unified full-strength existence conjecture.

The condition alone also does not force one-switch spanning paths: the matroid \(U_{1,3}\oplus U_{1,3}\) lies in the class and has root \(K_{3,3}\); a nine-edge globally ordered tournament instance admits no Hamilton path with at most one change of turn-color (see the scoped research note 'Rook-graph counterexample to incidence-gallery one-switch spanning'). Any stronger common conjecture needs additional intrinsic assumptions encoding the relevant endpoint and resource conditions.

#### Theorem 3 (a root-basis filter excluding the rook family)

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

#### Theorem 4 (triangle-free matroid basis graphs are cubical)

If the basis-exchange graph of a finite matroid \(M\) is triangle-free, then, up to loops and coloops, \(M\) is a direct sum of copies of \(U_{1,2}\). Conversely, every such direct sum has triangle-free basis graph. In particular, a connected triangle-free basis-exchange graph is a hypercube.

**Proof.** Fix a basis \(B\). For any nonloop \(e\notin B\), its fundamental circuit \(C_B(e)\) must contain precisely one element \(b\in B\): if it contained two distinct basis elements \(b,b'\), then \(B-b+e\) and \(B-b'+e\) would both be bases adjacent to \(B\) and to one another, forming a triangle. Therefore each nonloop element outside \(B\) is parallel to a unique element of \(B\). Every nonloop belongs to one of the parallel classes indexed by \(B\), and \(M\) is the direct sum of rank-one uniform matroids on those classes. A class of three or more elements yields three pairwise adjacent bases by independently choosing one member, again forming a triangle. Each nontrivial parallel class consequently has size two. Conversely, replacing either member in any two-element parallel class independently gives the cube graph. \(\square\)

This classification shows that the triangle-free incidence branch has rigid intrinsic matroid structure. An extension claiming that the cube and the uniform rank-two models share a nontrivial self-dual *basis-vertex* polarity must still confront their distinct automorphism-equivariance properties, as recorded in the canonical-polarity obstruction note.

**A nonuniform member of the refined class.** Let \(M\) be the rank-two matroid on six elements with three parallel classes of size two. Its bases are the two-element sets meeting distinct parallel classes, and its basis graph is \(L(K_{2,2,2})\). Every vertex of \(K_{2,2,2}\) has degree four, so the largest cliques of this line graph are its stars (size four), exceeding its triangle cliques (size three). Consequently the largest-clique incidence root is \(G(M)=K_{2,2,2}\). This root is isomorphic to \(J(4,2)=\Gamma(U_{2,4})\): partition the six two-element subsets of a four-element set into three complementary pairs; precisely the complementary pairs are nonadjacent in \(J(4,2)\). Hence \(M\in\mathcal C_{\mathrm{root}}\), despite being neither a uniform rank-two matroid nor a direct sum of rank-one two-element matroids. This demonstrates that the filter defines a class broader than the two motivating matroids.

Let \(M=\bigoplus_{j=1}^{t}U_{r_j,m_j}\) be a loopless partition matroid decomposed into its connected matroid components, with \(1\le r_j<m_j\) or \(r_j=m_j=1\) (singleton coloops). Let its component ground sets be \(E_j\), and put \(r=\sum_jr_j\), \(N=\sum_jm_j\). A **resource-simple sliding-window gallery** of order \(m\) is an injective word \(w_1,\ldots,w_m\), \(m\ge r\), such that every consecutive length-\(r\) set \(B_i=\{w_i,\ldots,w_{i+r-1}\}\) is a basis. Its exchanged basis arcs are \(B_i\to B_{i+1}\).

**Theorem (periodic component strands).** A word of distinct ground elements with a basis as its initial length-\(r\) window is a resource-simple sliding-window gallery if and only if
\[
\boxed{w_i\text{ and }w_{i+r}\text{ belong to the same connected component of }M}
\quad(1\le i\le m-r).\tag{1}
\]
Thus every gallery decomposes into \(r\) strands indexed by positions modulo \(r\); each strand stays inside one connected component. Conversely every such component schedule can be realized by choosing distinct elements in the prescribed components, subject only to their cardinalities.

*Proof.* The \(i\)-th basis window contains \(r_j\) elements of block \(E_j\) for every \(j\). The next window deletes \(w_i\) and inserts \(w_{i+r}\). Since all block counts must be preserved, both belong to the same block. This proves necessity. Conversely, if the entering and departing elements always belong to the same block, each transition preserves the block counts \(r_j\). By induction every length-\(r\) window is a basis, proving sufficiency. Distinctness gives a resource-simple gallery. \(\square\)

**Theorem (resource-capacity formula).** Fix a nonnegative integer \(q\), the proposed number of successive basis exchanges, and write
\[
q=ar+s,\qquad a\ge0,\quad 0\le s<r.
\]
A resource-simple sliding-window gallery with \(q\) exchanges (word order \(r+q\)) exists if and only if both
\[
\boxed{m_j\ge(a+1)r_j\text{ for every }j,}\tag{2}
\]
and
\[
\boxed{\sum_{j=1}^{t}\min\{r_j,m_j-(a+1)r_j\}\ge s.}\tag{3}
\]
In particular, these conditions compute the maximum uncolored resource-simple gallery length for every partition matroid in all ranks.

*Proof.* Choose the initial length-\(r\) block schedule with \(r_j\) positions labeled \(j\). By (1) the block schedule repeats with period \(r\). In the first \(r+q=(a+1)r+s\) positions, each block \(j\) occurs \((a+1)r_j+t_j\) times, where \(t_j\) is the number of labels \(j\) among the first \(s\) positions of the initial period. We have \(0\le t_j\le r_j\), \(\sum_jt_j=s\). Distinct resources can be chosen if and only if \((a+1)r_j+t_j\le m_j\) for each \(j\). Such integers \(t_j\) exist precisely under (2) and (3). Indeed, (3) says the available nonnegative prefix capacities \(\min\{r_j,m_j-(a+1)r_j\}\) can be allocated to total \(s\); after choosing the \(t_j\), arrange the first \(s\) positions accordingly, fill the remaining \(r-s\) positions to reach initial counts \(r_j\), and populate the strands by distinct resources. \(\square\)

**Corollary (criterion for a full-resource word).** A resource-simple sliding-window gallery using every nonloop element of \(M\) exists if and only if, writing \(h=\lfloor N/r\rfloor\),
\[
\boxed{h r_j\le m_j\le(h+1)r_j\quad\text{for every }j.}\tag{4}
\]
*Proof.* Apply (2)--(3) with \(q=N-r=(h-1)r+(N-hr)\). The excess capacities \(u_j=m_j-h r_j\) sum to \(s=N-hr<r\). Feasibility requires \(u_j\ge0\) and \(\sum\min(r_j,u_j)\ge\sum u_j\), equivalently \(0\le u_j\le r_j\). \(\square\)

**Canonical cases.** For \(M=\bigoplus_{i=1}^nU_{1,2}\), one strand corresponds to each parallel pair and contains at most two elements. Consequently any maximal uncolored gallery has length \(2n\): its first \(n\) entries choose one representative from each pair, and its final \(n\) entries are the corresponding mates in the same order. The basis windows form a coordinate-distinct antipodal cube geodesic. For \(M=U_{2,n}\), all positions share one component; every injective word of length at least two is a gallery, giving ordinary vertex-simple tight paths of a boundary 3-tournament. More generally, for \(M=U_{r,n}\) the same one-component rule gives vertex-simple length-\(r\) window galleries.

**Geometric implication.** The periodic component-strand rule is a common intrinsic gallery geometry underlying both canonical models. Its capacity theorem separates **combinatorial admissibility** (which positions and resources may occur) from the **color feasibility** treated by terminal-set tournament growth. In particular, full-resource uncolored galleries exist for both models; their color existence problems have qualitatively different strength. The all-dimensional mixed example \(Q_k\square K_3\) constructed in the associated obstruction note satisfies (4), while its deck-odd reversal-odd coloring prohibits positive galleries of \(r\) exchanges. This proves that the periodicity and capacity axioms alone cannot supply the desired colored diameter bound.

### Cycle-dominating resource matroids and a unified tournament-extension bound

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

#### Intrinsic vector-difference resource quotients

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

#### Canonical spectral construction

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

#### The homogeneous Hamming interpolation

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

Let \(M\) be a finite matroid obtained as a direct sum of nontrivial uniform matroids
\[
M=\bigoplus_{j=1}^{t}U_{r_j,m_j},\qquad 1\le r_j<m_j,
\]
and let \(G=\Gamma(M)\) be its basis-exchange graph. Thus
\[
G=\mathop{\square}_{j=1}^{t}J(m_j,r_j),\qquad
d=\deg(G)=\sum_{j=1}^{t}r_j(m_j-r_j).
\]
Let \(A_G\) be its adjacency matrix, \(P_2\) the orthogonal projection onto the eigenspace \(W_2\) of its second largest distinct adjacency eigenvalue, and \(N_{\rm sp}(G)\) the linear matroid on graph edges \(uv\) represented by \(P_2({\bf e}_u-{\bf e}_v)\).

**Theorem (spectral-star rigidity).** The following are equivalent:

(i) The edge vectors in every vertex star of \(G\) are independent in \(N_{\rm sp}(G)\).

(ii) There is an integer \(q\ge2\) such that every summand has \(m_j=q\) and \(r_j\in\{1,q-1\}\).

(iii) \(G\cong H(t,q)=K_q^{\square t}\) for some \(q\ge2\).

Under these conditions,
\[
\dim W_2=d=t(q-1),\qquad
\operatorname{rk}N_{\rm sp}(G)=d;
\]
each vertex star is a basis of \(N_{\rm sp}(G)\), and \(N_{\rm sp}(G)\) has minimum possible rank among matroids on \(E(G)\) in which all vertex stars are independent.

*Proof.* The adjacency spectrum of a Johnson graph \(J(m,r)\), for \(1\le r<m\), consists of the distinct eigenvalues
\[
\theta_\ell=(r-\ell)(m-r-\ell)-\ell,\qquad 0\le\ell\le\min(r,m-r),
\]
with the second one \(\theta_1=r(m-r)-m\) of multiplicity \(m-1\). Thus its spectral gap between the largest and second-largest adjacency eigenvalues is \(m\).

The adjacency operator of a Cartesian product is the sum of the lifted factor adjacency operators. Put \(m_*=\min_jm_j\). The second-largest eigenvalue of \(G\) is therefore \(d-m_*\), and its multiplicity is
\[
D=\dim W_2=\sum_{\{j:m_j=m_*\}}(m_j-1).\tag{1}
\]
For every \(j\),
\[
r_j(m_j-r_j)\ge m_j-1,\tag{2}
\]
with equality if and only if \(r_j=1\) or \(r_j=m_j-1\). As each summand is nontrivial, (1)--(2) give \(d\ge D\), and equality holds if and only if all \(m_j=m_*\) and each rank is \(1\) or \(m_*-1\). Since the \(d\) incident edge vectors at a vertex lie in the \(D\)-dimensional space \(W_2\), condition (i) requires \(d\le D\). Hence (i) implies (ii).

Under (ii), every Johnson factor is \(J(q,1)\cong J(q,q-1)\cong K_q\), proving (iii). Conversely, every Johnson graph \(J(m,r)\), \(1\le r<m\), has triangle-connected edge set (the graph whose vertices are its edges and whose adjacencies join two edges belonging to one triangle is connected), unless it consists of a single edge. Indeed, two exchanges at the same basis are joined by a sequence of triangle moves that alternately hold the entering or departing element fixed; the line graph of the complete bipartite fundamental exchange graph \(K_{r,m-r}\) is connected. Connectedness of \(J(m,r)\) then joins the triangle chains across bases. In a Cartesian product, the edges of every triangle lie in one factor, so a triangle-connected Johnson factor cannot split across distinct Cartesian factors. Therefore if (iii) holds, each Johnson factor is one complete factor \(K_q\), and hence \(r_j\in\{1,m_j-1\}\) and \(m_j=q\).

To prove (iii) implies (i), identify the second eigenspace of \(H(t,q)\) with \(\bigoplus_{j=1}^t{\bf1}^{\perp}\subseteq(\mathbb R^q)^t\). The projected difference vector for an edge changing symbol \(a\) to \(b\) in factor \(j\) is, up to a common nonzero scalar, \({\bf e}_b-{\bf e}_a\) in the \(j\)-th summand and zero elsewhere. At any vertex, the \(q-1\) incident vectors in factor \(j\) form a basis of that summand. All incident vectors are therefore a basis of \(W_2\). Connectedness ensures that the projected differences of graph edges span all of \(W_2\), because edge differences span the coordinate hyperplane perpendicular to the all-ones vector, which contains \(W_2\). Hence the edge-column matroid has rank \(d\).

Finally, any matroid on \(E(G)\) with an independent vertex star has rank at least \(d\). The spectral resource matroid attains this lower bound. \(\square\)

**Corollary (intrinsic minimal resource geometry of the canonical roots).** For \(Q_n=H(n,2)\), the minimal-rank spectral resource matroid is the partition matroid on coordinate-direction edge classes, of rank \(n\). For \(K_n=H(1,n)\), it is the graphic matroid \(M(K_n)\), of rank \(n-1\). In both cases, every vertex star is a resource basis. These are two specializations of the same automorphism-invariant spectral projection, with the resource rank equal to the graph degree.

**Scope.** The theorem classifies the spectral-star condition *within partition-matroid basis graphs*. It does not classify all matroid basis graphs satisfying that condition. Its two extremal cases are the root graphs naturally associated with the NORI1 cube and the boundary 3-tournament Johnson basis graph, respectively: the boundary root is \(K_n\), recovered as the line-graph root of \(J(n,2)\) for \(n\ge4\). It provides a structural class and a minimum-rank resource representation but does not force full-rank positively oriented paths.

**Corollary (functorial polarization threshold).** Let \(X=V(H(t,q))\) with the natural action of \(\operatorname{Aut}(H(t,q))=S_q\wr S_t\). If \(q\ge3\), every equivariant self-map \(X\to X\) is the identity. If \(q=2\), the equivariant self-maps are the identity and simultaneous coordinate complementation.

*Proof.* The automorphism group acts transitively. An equivariant map is determined by the image of the all-zero vertex, which must be fixed by its stabilizer. For \(q\ge3\), the stabilizer contains an independent \(S_{q-1}\) permutation group on the unused alphabet symbols in every factor, and therefore fixes only the all-zero vertex. For \(q=2\), the stabilizer permutes the \(t\) factors and fixes the two constant binary words; the two resulting equivariant maps are identity and complementation. \(\square\)

Thus the canonical fixed-point-free antipode of \(Q_t\) disappears immediately upon passing to the next homogeneous Hamming interpolation \(H(t,3)\). Any formulation encompassing arbitrary complete-graph roots must locate its reversal structure on oriented exchange flags or another derived carrier.

Let \(G=(V,E)\) be a finite simple graph. Let \(\mathsf R\) be a matroid of rank \(d\), represented by nonzero vectors \(\{a_\ell:\ell\in\Lambda\}\) over a field \(\mathbb F\). Suppose the edges of \(G\) carry labels \(\lambda:E\to\Lambda\) and there is an injective vertex potential \(\phi:V\to\mathbb F^N\), where the vectors \(a_\ell\) also lie in \(\mathbb F^N\), with the following properties:

1. For every oriented edge \(uv\), \(\phi(v)-\phi(u)\) is a nonzero scalar multiple of \(a_{\lambda(uv)}\).
2. At every vertex \(v\), the \(d\) labels on its incident edges form a basis of \(\mathsf R\).

The second condition makes \(G\) \(d\)-regular. We call this the **basis-star condition**. In this Subsection, a path is resource-independent if its edge-label multiset contains no repetitions and is independent in \(\mathsf R\). Equip each vertex \(v\) with an arbitrary tournament \(T_v\) on the edges incident with \(v\). A resource-independent path \(v_1,\ldots,v_\ell\) is admissible if \(v_{i-1}v_i\to v_iv_{i+1}\) in \(T_{v_i}\) at every internal vertex. The tournament data are entirely unrestricted.

**Lemma 1 (independent resources enforce vertex simplicity).** Every resource-independent walk in \(G\) is vertex-simple. Furthermore, two resource-independent walks terminating at the same vertex, whose combined edge-label multiset is independent, have no common vertex other than their terminal vertex.

*Proof.* A nonempty closed subwalk whose labels are independent would give, by telescoping the potential \(\phi\), a nontrivial linear relation among their representing vectors: every traversed edge contributes a nonzero scalar and no label occurs twice. This is impossible. Therefore an independent-resource walk has no repeated vertex. If two walks with a common terminal \(t\) met again at \(z\ne t\), their subwalks from \(t\) to \(z\) would give two representations of \(\phi(z)-\phi(t)\). Subtracting these expressions would produce a nontrivial dependence among their combined distinct labels. Hence their intersection consists only of \(t\). \(\square\)

**Theorem 2 (basis-star terminal-edge theorem).** In the preceding setting, there is an admissible resource-independent path with \(L\) vertices satisfying
\[
\boxed{\quad d/2\le (L-1)^2,\qquad L\ge 1+\sqrt{d/2}.\quad} \tag{1}
\]

*Proof.* For an undirected edge \(e\), let \(h(e)\) be the greatest order of an admissible resource-independent path with \(e\) as its last edge, in either orientation. A two-vertex path is admissible, so \(2\le h(e)\le d+1\). Orient \(e\) toward the terminal vertex of a path attaining \(h(e)\), resolving ties arbitrarily. Since \(G\) is \(d\)-regular, the average indegree in the resulting orientation is \(d/2\); choose a vertex \(v\) with at least this indegree.

For \(2\le k\le L:=\max_e h(e)\), let \(U_k\) consist of the edges oriented toward \(v\) for which \(h(e)=k\), and put \(q=|U_k|\). If \(q=0\) there is nothing to prove. The tournament on \(U_k\) has an edge \(uv\) beating at least \((q-1)/2\) other members \(vw\) of \(U_k\). By the choice of the orientation, there is an admissible resource-independent path \(P=(v_1,\ldots,v_{k-2},u,v)\) attaining \(h(uv)=k\).

Write \(S\) for the span of the \(k-1\) representing vectors corresponding to the labels of the edges of \(P\). Suppose that a beaten edge \(vw\in U_k\) has \(a_{\lambda(vw)}\notin S\). Then \(P\) followed by \(vw\) has independent labels, and it obeys the required tournament comparison at \(v\). Lemma 1 guarantees that the resulting walk has distinct vertices. It is therefore an admissible resource-independent \((k+1)\)-vertex path ending in \(vw\), contrary to \(h(vw)=k\).

Every edge of \(U_k\) beaten by \(uv\) consequently has its representing vector in \(S\). The vectors labeling the full star at \(v\) constitute a basis of \(\mathsf R\); at most \(\dim S=k-1\) of them can lie in \(S\). One of these vectors labels the incoming edge \(uv\), which does not beat itself. Therefore at most \(k-2\) other star edges can be beaten, and
\[
(q-1)/2\le k-2,\qquad q\le 2k-3.
\]
Summing over all terminal orders,
\[
d/2\le\deg^-(v)=\sum_{k=2}^{L}|U_k|
\le\sum_{k=2}^{L}(2k-3)=(L-1)^2.
\]
This proves (1). \(\square\)

The proof uses the matroid span to control both possible failures of extension: a repeated label and a repeated vertex. The vertex-potential identity in Lemma 1 makes the second failure automatically dependent on the first. This removes the second obstruction term in the proper-edge-label terminal theorem of Article VII, while allowing labels to recur at different vertices.

##### Canonical realization on products of simplices

Let \(M=\bigoplus_{j=1}^t U_{r_j,E_j}\), where \(1\le r_j<|E_j|=:m_j\). Its connected-component partition is intrinsic to \(M\). Define the componentwise rank-one reduction
\[
M^\flat=\bigoplus_{j=1}^t U_{1,E_j},
\qquad
G_M=\Gamma(M^\flat)\cong \mathop{\square}_{j=1}^t K_{m_j}.
\tag{2}
\]
The vertices of \(G_M\) are tuples \(x=(x_1,\ldots,x_t)\), with \(x_j\in E_j\); an edge changes one component coordinate from \(a\) to \(b\).

Let
\[
\mathsf R_M=\bigoplus_{j=1}^t M(K_{E_j}),\qquad
d=\operatorname{rk}(\mathsf R_M)=\sum_{j=1}^t(m_j-1).
\tag{3}
\]
Represent the edge \(ab\) in the \(j\)-th clique by \(e_b-e_a\in\mathbb R^{E_j}\), and write \(\lambda(xy)=(j,\{a,b\})\) for the edge label when \(x,y\) differ in component \(j\). The vertex potential
\[
\phi(x)=\bigoplus_{j=1}^t e_{x_j}\in\bigoplus_{j=1}^t\mathbb R^{E_j}
\tag{4}
\]
is injective. Its derivative along \(xy\) is the root \(e_b-e_a\) with the appropriate orientation. At \(x\), the root vectors of its \(m_j-1\) incident edges in coordinate \(j\) are
\[
\{e_b-e_{x_j}:b\in E_j\setminus\{x_j\}\}.
\tag{5}
\]
These form a basis of the type-\(A_{m_j-1}\) root space. Taking their union over the different components gives a basis of \(\mathsf R_M\).

**Proposition (coordinatewise simple-path criterion).** Let
\[
G=\mathop{\square}_{j=1}^t K_{m_j},\qquad
R=\bigoplus_{j=1}^t M(K_{m_j}),
\]
with the canonical labels \(\lambda(xy)=(j,\{a,b\})\) on steps changing coordinate \(j\) from \(a\) to \(b\). For any finite walk \(P=(x^0,\ldots,x^\ell)\) in \(G\), let \(P_j\) be the sequence of coordinate-\(j\) values obtained from \(x_j^0,\ldots,x_j^\ell\) by suppressing consecutive repeats. Then the following are equivalent:

(a) the multiset of all step labels along \(P\) is independent in \(R\);

(b) for every \(j\), the entries of \(P_j\) are pairwise distinct.

Under either condition, \(P\) is a vertex-simple path and \(\ell\le\operatorname{rk}(R)=\sum_j(m_j-1)\). Equality holds if and only if \(P_j\) is a Hamiltonian path in the complete graph \(K_{m_j}\) for every coordinate \(j\).

*Proof.* The labels contributed by coordinate \(j\) are the consecutive edges of the walk \(P_j\) in \(K_{m_j}\). A multiset of edges is independent in the graphic matroid if and only if it has no repeated edge and its underlying graph is a forest. A walk using only edges of a forest, each at most once, cannot revisit a vertex: a segment between successive visits would be a nonempty closed trail, necessarily containing either a repeated edge or a cycle. Conversely, a walk with pairwise distinct vertices forms a simple path, whose edges are independent in the graphic matroid. Since \(R\) is the direct sum of its factor matroids, applying this equivalence in every coordinate proves (a)\(\Leftrightarrow\)(b).

If \(x^p=x^q\) for \(p<q\), some coordinate changes between those two times, and its suppressed coordinate sequence revisits its initial value, contradicting (b). Hence \(P\) is vertex-simple. In coordinate \(j\), pairwise distinct entries imply at most \(m_j-1\) changes. Summing gives \(\ell\le\sum_j(m_j-1)\). Equality holds precisely when every coordinate changes \(m_j-1\) times and thus visits all its \(m_j\) symbols. \(\square\)

**Canonical interpretations.** When all \(m_j=2\), a full-rank independent gallery changes each binary coordinate once; it is a cube antipodal geodesic. When \(t=1\) and \(m_1=n\), a full-rank independent gallery is a Hamiltonian vertex word in \(K_n\), and its successive two-edge windows are the ordered triples of the boundary tournament. For general \(t\), a full-rank gallery is a path whose projections onto every clique factor are Hamiltonian paths, with the factor moves interleaved arbitrarily. This is a common *geometric* witness language derived from the intrinsic direct-sum graphic-root matroid. Color-compatible existence is the additional problem.


**Corollary 3 (uniform Hamming-graph theorem).** For every Cartesian product of nontrivial cliques \(G=\square_{j=1}^t K_{m_j}\), endowed with arbitrary local tournaments on its incident edges, there is a vertex-simple tournament-admissible path whose labels are independent in \(\bigoplus_j M(K_{m_j})\) and which has at least
\[
\boxed{1+\sqrt{\tfrac12\sum_j(m_j-1)}} \tag{6}
\]
vertices.

This establishes one intrinsic root-matroid extension theorem for all rank-one partition-matroid basis graphs. The source matroid ranks \(r_j\) determine additional color-carrier geometry but play no role in the root-basis terminal inequality.

##### Both canonical source models

For \(M_{\rm cub}=\bigoplus_{i=1}^nU_{1,2}\), the reduction \(M_{\rm cub}^\flat=M_{\rm cub}\) has \(G_M=Q_n\) and \(\mathsf R_M\cong U_{n,n}\). Given any coloring of undirected cube edges, order the edges incident with each cube vertex first by increasing color and then by an arbitrary tie-break. Each local tournament is transitive. An admissible path has independent direction labels and therefore is a geodesic; its edge-color word is weakly increasing. Theorem 2 supplies a geodesic of at least
\[
\boxed{\sqrt{n/2}}\tag{7}
\]
edges and at most one color change. This applies, in particular, to every NORI1 antipodally odd coloring. It strengthens the partial-geodesic bound obtained by applying the proper-label estimate of Article VII directly.

For \(M_{\rm bd}=U_{2,n}\), the reduction is \(U_{1,n}\), so \(G_M=K_n\), \(\mathsf R_M=M(K_n)\), and
\[
\Gamma(M_{\rm bd})=J(n,2)=L(G_M).
\tag{8}
\]
Let \(b(a,v,c)\in\{0,1\}\) be an arbitrary reversal-odd boundary coloring. At vertex \(v\) of \(K_n\), orient the local comparison \(av\to vc\) precisely when \(b(a,v,c)=1\). Reversal oddness makes this a tournament. Theorem 2 produces a vertex-simple path of order at least
\[
\boxed{1+\sqrt{(n-1)/2}}\tag{9}
\]
on which every consecutive triple has color one. Reversal gives an equally long color-zero path. In this model the independent-root predicate is the original-vertex graphic independence: a simple tight path uses a forest of consecutive original edges.

Thus the same rank \(d\), the same star-basis hypothesis, and the same terminal-edge proof explain both square-root bounds. In the cube the resulting geodesic is only partial; neither Theorem 2 nor Corollary 3 promotes it to a monochromatic full antipodal geodesic. Such a promotion would require the global antipodal coloring law and the additional square-exchange geometry.

##### Two-arm resource bases

The potential argument also supplies a common geometric gluing rule. Let \(P,Q\) be two paths ending at a common vertex \(t\), and suppose the multiset of labels of their combined edges is a basis of \(\mathsf R\). Lemma 1 makes their union a simple path, obtained by concatenating \(P\) with the reversal of \(Q\). For the two canonical color-carrier grades this has a common binary conclusion:

- For undirected edge colors, two same-colored monochromatic arms concatenate to a monochromatic path. On the cube, full root rank \(n\) forces every coordinate to occur once, hence the other endpoints are antipodes.
- For reversal-odd colors on oriented two-edge windows, two same-colored monochromatic arms concatenate to a path with at most one color change among successive windows. Windows in the reversed arm have the complementary color, and the one junction window can only extend one of these two color runs. On \(K_n\), full root rank \(n-1\) forces a Hamiltonian tight word.

Conversely, a full monochromatic cube geodesic splits into two monochromatic arms with a basis union. The common-terminal two-arm theorem elsewhere in Article XI establishes the converse for boundary Hamiltonian words with at most one change, including its junction cases. In this way a single resource-basis packing predicate expresses both spanning conclusions; its universal existence remains conjectural. Theorem 2 supplies quantitative rank-growth toward that predicate without assuming it.

##### Linear monochromatic paths from edge-density and root independence

The root-potential hypotheses strengthen the standard greedy rainbow-path argument for a properly edge-labelled graph. In particular, the independent-star property suffices without requiring the star to span all of \(\mathsf R\).

**Lemma 4 (minimum degree forces independent-root path length).** Suppose \(G\) has an injective vertex potential and a root representation as above, and the edge labels incident with each vertex are independent in \(\mathsf R\). Every nonempty edge-subgraph \(H\subseteq G\) of minimum degree \(\delta(H)\) contains a resource-independent path of at least \(\delta(H)\) edges.

*Proof.* Choose a resource-independent path \(P=(v_0,\ldots,v_\ell)\) in \(H\) with maximal length, and let \(S\) be the linear span of its \(\ell\) resource vectors. If an edge \(v_\ell w\) of \(H\) has label outside \(S\), then adding it preserves resource independence. Moreover \(w\) is new: for any \(w=v_i\) already on \(P\), the vector \(\phi(w)-\phi(v_\ell)\) is a linear combination of the root vectors labeling the terminal subpath of \(P\), hence the label of \(v_\ell w\) lies in \(S\). Thus maximality forces every \(H\)-edge incident with \(v_\ell\) to have its label in \(S\). The independent-star condition bounds their number by \(\dim S=\ell\). Therefore \(\ell\ge \deg_H(v_\ell)\ge\delta(H)\). \(\square\)

**Theorem 5 (density-to-resource-rank bound).** Under the conditions of Lemma 4, every nonempty edge-subgraph \(H=(V,E_H)\subseteq G\), including isolated vertices in \(V\), contains a resource-independent path of length at least
\[
\boxed{\left\lceil\frac{|E_H|}{|V|}\right\rceil .}\tag{10}
\]

*Proof.* Put \(a=|E_H|/|V|>0\). Iteratively delete a vertex whose degree in the remaining subgraph is strictly smaller than \(a\), if one exists. All vertices cannot be deleted: charge every edge to its endpoint deleted first. Were every vertex deleted, fewer than \(a|V|=|E_H|\) edge incidences would be charged, while each original edge is charged once. Hence a nonempty subgraph \(K\subseteq H\) survives with \(\delta(K)\ge a\). Lemma 4 gives a resource-independent path of at least \(\delta(K)\) edges, at least the ceiling in (10). \(\square\)

**Theorem 6 (free-resource rank potential).** Assume in addition that \(\mathsf R\) is free, and fix any total order on its edge-label ground set \(\Lambda\). For any edge-subgraph \(H=(V,E_H)\) with proper edge labelling and the same injective root potential, let \(L_H(v)\) be the greatest length of a path ending at \(v\) whose resource labels occur in strictly increasing order. Then
\[
\boxed{\sum_{v\in V} L_H(v)\ge 2|E_H|.}\tag{11}
\]
In particular \(H\) contains a resource-independent path of length at least \(2|E_H|/|V|\).

*Proof.* We argue by induction on \(|E_H|\). The assertion is immediate when \(E_H=\varnothing\). Choose an edge \(e=xy\) with maximal label and put \(H'=H-e\). By properness, the label of every last edge in a strictly increasing path of \(H'\) ending at \(x\) or \(y\) is smaller than \(\lambda(e)\): no other edge at either endpoint has this label. Since \(\mathsf R\) is free, appending \(e\) to either such path preserves resource independence; injectivity of the vertex potential ensures the new endpoint has not been visited. Write \(a=L_{H'}(x)\) and \(b=L_{H'}(y)\). If \(a=b\), appending \(e\) increases both endpoint maxima by at least one, and their sum increases by at least two. If, say, \(a\ge b+1\), appending \(e\) to a maximizing path ending at \(x\) increases the maximum at \(y\) by at least \(a+1-b\ge2\). In every case the sum of all endpoint maxima increases by at least two when \(e\) is restored. The induction hypothesis proves (11). \(\square\)

The argument is the increasing-geodesic potential method of Leader and Long, *Long geodesics in subgraphs of the cube*, extended here to any faithful free-resource voltage graph with proper labelling. The representation-theoretic role of freeness is explicit: a newly largest label has no circuit dependence on previously used labels. The potential hypothesis makes an attempted endpoint repetition a consequence of precisely such a circuit.

**Corollary 7 (sharp known density bound for cube edge colors).** Every two-coloring of \(E(Q_n)\) has a monochromatic coordinate-distinct geodesic of length at least \(\lceil n/2\rceil\). For an antipodally odd coloring, each of the two colors admits such a geodesic.

*Proof.* The coordinate-root matroid \(U_{n,n}\) is free, the coordinate edge labelling is proper, and its natural vertex potential is injective. The cube has \(n2^{n-1}\) edges. Under any two-coloring, a color occurs on at least \(n2^{n-2}\) edges. Apply Theorem 6 with \(|V|=2^n\). Under antipodal oddness, each edge-color class contains \(n2^{n-2}\) edges, so the argument applies to both classes. \(\square\)

The first conclusion is the Leader--Long monochromatic-geodesic corollary, recovered through Theorem 6; the both-color formulation follows from antipodal balance. This result supersedes the weaker density-to-rank bound \(\lceil n/4\rceil\) that Theorem 5 supplies in the cube. Theorem 5 retains its independent significance for represented resource matroids with circuits.

**Proposition 8 (triangle obstruction to free-resource induction).** The induction proving (11) fails in general for graphic resource matroids, even on \(K_3\). Give the three edges the increasing order \(ab<bc<ac\) and use the incidence-root representation of \(M(K_3)\). In \(H'=K_3-ac\), a maximal increasing path ending at \(c\) is \(a,b,c\), using resources \(ab,bc\). The remaining largest root \(ac\) lies in their span and its addition would close a triangle and repeat \(a\). Restoring \(ac\) raises the sum of the three endpoint maxima by only one, whereas the free-resource proof requires an increment of two.

*Proof.* The incidence identity \(e_c-e_a=(e_b-e_a)+(e_c-e_b)\) is the graphic circuit relation. The lengths of maximal increasing paths ending at \(a,b,c\), respectively, are \((1,1,2)\) in \(H'\). In \(H\) they are \((2,1,2)\): the additional increasing path \(b,c,a\) increases the maximum at \(a\) by one, while the dependent edge cannot extend the two-edge path ending at \(c\). Thus the sum increases from four to five. \(\square\)

This circuit obstruction is independent of the second complication in ordinary boundary tournaments: arbitrary reversal-odd boundary data prescribe different local tournaments, which need not be restrictions of one globally ordered root set. The former prevents automatic independent extension; the latter prevents applying the global increasing-path induction. The root-basis terminal theorem permits both and retains the common square-root conclusion.

The different grades of the two original coloring systems also matter. In a cube, a monochromatic *edge* set is a dense graph whose average degree can be used in Theorem 6. In a boundary tournament, color is assigned to consecutive *turns*, and a color class does not determine an undirected edge-subgraph of comparable density. Together, freeness of the resource matroid and the carrier grade explain why a linear monochromatic *partial* cube geodesic is accessible by this method, whereas the common local-tournament proof only gives the square-root boundary estimate. A full monochromatic antipodal cube geodesic still requires the global opposition condition and additional exchange geometry.

Let \(M\) be a finite matroid on \(E\), and let \(\Gamma(M)\) be its basis-exchange graph. For a basis \(B\), the **fundamental exchange graph** \(F_B\) is the bipartite graph on \(B\sqcup(E\setminus B)\), with edge \(be\) precisely when \(B-b+e\) is a basis. Loops and coloops become isolated vertices; the remaining connected components correspond to the connected matroid components.

Define the canonical basis-incidence embedding
\[
\Phi:\mathcal B(M)\longrightarrow\mathbb R^E,\qquad
\Phi(B)=\sum_{b\in B}{\bf e}_b.
\]
An exchange edge \(B\to B-b+e\) has difference vector \({\bf e}_e-{\bf e}_b\).

**Theorem (exchange-forest rigidity).** The following conditions are equivalent.

(i) For every basis \(B\), the exchange-difference vectors of the edges incident with \(B\) are linearly independent.

(ii) For every basis \(B\), the fundamental exchange graph \(F_B\) is a forest.

(iii) Every connected component of \(M\) is a loop, a coloop, a uniform rank-one matroid \(U_{1,m}\), or its dual \(U_{m-1,m}\).

In particular, the canonical basis-incidence resource matroid has independent stars throughout the basis-exchange graph precisely for direct sums of rank-one or corank-one uniform matroids.

*Proof.* The difference vectors \({\bf e}_e-{\bf e}_b\) at a basis \(B\) are the oriented vertex-edge incidence columns of \(F_B\), viewed in \(\mathbb R^E\). Incidence columns are independent if and only if the corresponding graph has no cycle, so (i) and (ii) are equivalent.

We prove (ii) implies (iii). Suppose an induced path
\[
b_1-e_1-b_2-e_2\tag{1}
\]
occurs in \(F_B\), with \(b_1,b_2\in B\) and \(e_1,e_2\notin B\). Thus
\[
B-b_1+e_1,\quad B-b_2+e_1,\quad B-b_2+e_2
\]
are bases, whereas \(B-b_1+e_2\) is dependent. Put \(A=B\setminus\{b_1,b_2\}\), and contract \(A\). In the rank-two matroid \(M/A\), the pair \(\{b_2,e_2\}\) is dependent, while \(\{b_1,e_2\}\) and \(\{b_2,e_1\}\) are bases. Therefore \(b_2\) and \(e_2\) are nonloops in the same parallel class, and \(\{e_1,e_2\}\) is a basis. Lifting to \(M\) shows
\[
B-\{b_1,b_2\}+\{e_1,e_2\}\ \text{is a basis}.\tag{2}
\]

Pivot from \(B\) to the adjacent basis \(B'=B-b_2+e_1\). The four substitutions
\[
B'-b_1+b_2,\quad B'-e_1+b_2,\quad
B'-e_1+e_2,\quad B'-b_1+e_2
\]
are all bases, by the hypotheses and (2). Hence \(F_{B'}\) contains a four-cycle on bipartition \(\{b_1,e_1\}\sqcup\{b_2,e_2\}\), contradicting (ii). Thus **no** fundamental exchange graph can contain an induced four-vertex path.

We next recall why the connected components of \(F_B\) correspond to those of \(M\). Let \(S_1,\ldots,S_h\) be the vertex sets of the components of \(F_B\), and let \(B_j=B\cap S_j\). Every \(e\in S_j\setminus B_j\) belongs to the closure of \(B_j\), since its fundamental circuit relative to \(B\) is contained in \(S_j\). Therefore \(\operatorname{rk}_M(S_j)=|B_j|\). As \(\sum_j|B_j|=\operatorname{rk}(M)\), the rank-additivity criterion implies \(M=\bigoplus_jM|S_j\). Conversely each matroid direct-sum component induces no fundamental exchanges with other components. Thus a connected, nontrivial component of \(M\) yields a connected \(F_B\).

By (ii), each such graph is a tree, and by the preceding pivot argument it contains no induced four-vertex path. A connected tree with no four-vertex path is a star. Since the star spans every element of its connected matroid component, one side of its bipartition has a single vertex. Thus that component has rank one or corank one. A connected rank-one matroid is \(U_{1,m}\), and a connected corank-one matroid is its dual \(U_{m-1,m}\). Loops and coloops are harmless singleton components. This proves (iii).

Conversely, for \(U_{1,m}\) the graph \(F_B\) is \(K_{1,m-1}\), and for \(U_{m-1,m}\) it is \(K_{m-1,1}\). Direct sums give disjoint unions of these stars and isolated vertices, which are forests. Hence (iii) implies (ii). \(\square\)

**Application to the two canonical root graphs.** The basis graph \(Q_n\) of \(\bigoplus^nU_{1,2}\) has a canonical embedding \(\Phi\) whose incident differences are independent: its resources are the \(n\) parallel classes of coordinate directions. The original basis graph \(J(n,2)\) of \(U_{2,n}\), \(n\ge4\), fails this condition because \(F_B=K_{2,n-2}\) has cycles. Its intrinsic line-graph root \(K_n=\Gamma(U_{1,n})\), however, satisfies the condition, and its exchange-difference vectors represent the graphic matroid \(M(K_n)\). Thus the passage from the boundary model's Johnson basis graph to its complete-graph root is mathematically necessary for this common independent-star resource mechanism.

The theorem is an ordinary-matroid obstruction to using canonical basis-indicator gradients directly in both problems, and provides a structural reason for examining a derived root graph equipped with a graphic or spectral resource matroid.

**Theorem (transitive-star terminal bound).** Let \(G\) be a connected finite simple graph of average degree \(d\), and \(N\) a matroid on \(E(G)\) in which every vertex star is independent and every graph cycle is dependent. At each vertex equip the incident edges with a transitive tournament. An admissible path has an \(N\)-independent edge set and respects the tournaments at successive edges. If \(L\) is the maximum number of vertices of an admissible path, then
\[
\boxed{d\le L(L-1).}
\]
**Proof.** For each edge \(e\), choose a longest admissible path ending with \(e\) in either direction, orient \(e\) toward its witness terminal, and let \(r(e)\) be its witness order. Some vertex \(v\) receives at least \(d/2\) edges. Let \(U_r\) be the incoming edges with \(r(e)=r\). The transitive tournament on \(U_r\) has an edge \(uv\) beating all others. Let \(P\) be its \(r\)-vertex witness and \(X=E(P)\), independent of rank \(r-1\). Any other \(vw\in U_r\) outside \(\operatorname{cl}_N(X)\) extends \(P\): independence of \(X+vw\) precludes a repeated vertex because every graph cycle is \(N\)-dependent, and the terminal comparison is favorable. This contradicts \(r(vw)=r\). Thus \(U_r\subseteq E(v)\cap\operatorname{cl}_N(X)\). As the star is independent, \(|U_r|\le r-1\). Summing gives \(d/2\le\sum_{r=2}^L(r-1)=L(L-1)/2\). \(\square\)

**Corollary (binary cube-edge colors).** Every binary coloring of \(E(Q_n)\) has a coordinate-distinct geodesic with at most one color change and at least
\[
\boxed{\left\lceil(\sqrt{4n+1}-1)/2\right\rceil}
\]
edges. Use the coordinate-partition resource matroid and order each star by edge color, breaking ties arbitrarily. Every admissible path has distinct coordinates and a weakly increasing color word; the cube has average degree \(n\). Antipodal oddness is not needed.

**Corollary (locally transitive boundary tournaments).** If the comparison tournament at each middle vertex of a reversal-odd boundary \(3\)-tournament is transitive, there is a monochromatic vertex-simple tight path with at least \(1+(\sqrt{4n-3}-1)/2\) vertices. Use \(G=K_n\), \(N=M(K_n)\), and \(d=n-1\). The local orders may be mutually inconsistent.

**Interpolation.** If every induced subtournament on \(q\) edges of any star has a vertex beating at least \(\alpha(q-1)\) others, \(1/2\le\alpha\le1\), the same proof gives \(d/2\le (L-1)+(L-1)(L-2)/(2\alpha)\), since \(\alpha(|U_r|-1)\le r-2\). It specializes to the arbitrary-tournament bound at \(\alpha=1/2\) and the theorem at \(\alpha=1\).

An \(n\)-edge one-switch geodesic in the antipodally odd cube would settle NORI1 by odd-change rotation; the result here supplies a longer partial path.

Let \(G=(V,E)\) be a finite connected simple graph and let \(N\) be a matroid on \(E\) such that
\[
\text{each vertex star }E(v)\text{ is independent in }N,
\qquad
\text{every graph cycle is dependent in }N.\tag{1}
\]
Let \(c:E\to\mathbb F_2\) be an arbitrary edge coloring. Give each nonbacktracking oriented two-edge walk \((u,v,w)\), with \(u\ne w\), a bit \(b(u,v,w)\). Assume
\[
b(u,v,w)=c(uv)+c(vw)\pmod2\qquad\text{if }uw\notin E,\tag{2}
\]
and
\[
b(u,v,w)+b(w,v,u)=1\pmod2\qquad\text{if }uw\in E.\tag{3}
\]
Thus a turn with nonadjacent outside vertices tests agreement of its incident edge colors, whereas a turn belonging to a triangle has an arbitrarily oriented comparison. The two conditions are equivalent to a reversal law
\[
b(u,v,w)+b(w,v,u)=\mathbf1_{\{uw\in E\}},
\]
together with the potential condition (2) on nontriangular turns.

Call a vertex-simple path \(P=(v_0,\ldots,v_\ell)\) **accepted** if \(\{v_{i-1}v_i:1\le i\le\ell\}\) is independent in \(N\) and \(b(v_{i-1},v_i,v_{i+1})=0\) for every internal turn.

**Theorem (two-color triangular-turn terminal bound).** Under (1)--(3), there exists an accepted path of at least
\[
\boxed{\ell\ge\frac12\sqrt{\bar d(G)},\qquad \bar d(G)=\frac{2|E|}{|V|}}\tag{4}
\]
edges. Its edge set can be chosen monochromatic under \(c\).

*Proof.* Partition \(E=E_0\sqcup E_1\) by the edge coloring \(c\). At least one color class, say \(E_s\), has at least \(|E|/2\) edges. Hence the spanning monochromatic subgraph \(G_s=(V,E_s)\) has average degree at least \(\bar d(G)/2\). Some nontrivial connected component \(H\) of \(G_s\) has average degree at least \(\bar d(G)/2\).

For every vertex \(v\in V(H)\), define a tournament on the incident edges of \(H\). Given two incident edges \(uv\), \(vw\), if \(u,w\) are adjacent in \(G\), orient their tournament comparison from \(uv\) to \(vw\) when \(b(u,v,w)=0\), and in the opposite direction otherwise. Condition (3) ensures that one orientation is accepted. If \(u,w\) are nonadjacent in \(G\), both edges have color \(s\), so (2) gives
\[
b(u,v,w)=c(uv)+c(vw)=0,
\]
and the reversed turn also has value zero. Either orientation may be chosen in the tournament. Thus **every forward comparison of these vertex-star tournaments is an accepted turn**.

The restriction \(N|E(H)\) has independent vertex stars and dependent graph cycles, by (1). Apply the cycle-dominating resource-matroid terminal-path theorem to \(H\) with the constructed local tournaments. It gives a path with \(N\)-independent edge set, all its turns accepted, and at least
\[
\sqrt{\bar d(H)/2}\ge\sqrt{\bar d(G)/4}
\]
edges. Since the path lies in \(H\subseteq G_s\), all its edges also have color \(s\). \(\square\)

**Corollary (common spectral-root bound).** Let \(G=H(k,q)=K_q^{\square k}\), \(k\ge1,q\ge2\), and let \(N=N_{\rm sp}(G)\) be its canonical second-adjacency-eigenspace edge-difference matroid. Then (1) holds, \(\bar d(G)=k(q-1)\), and every turn system (2)--(3) admits an accepted \(N\)-independent path of at least
\[
\boxed{\frac12\sqrt{k(q-1)}}\tag{5}
\]
edges.

*Proof.* The second-eigenspace difference vectors are supported within individual Cartesian factors, representing a direct sum of \(k\) copies of \(M(K_q)\). The vectors in every vertex star form a basis of \(N\). Graph cycles are dependent because their oriented edge differences telescope to zero. The graph is \(k(q-1)\)-regular. Apply (4). \(\square\)

**Canonical specializations.** For \(G=Q_n=H(n,2)\), every nonbacktracking turn has nonadjacent outside vertices, so the turn condition (2) reduces to \(b(u,v,w)=c(uv)+c(vw)\). An accepted resource-independent path is a monochromatic coordinate-distinct cube geodesic. Consequently **every** binary coloring of the edges of \(Q_n\), without any antipodal condition, admits such a geodesic of at least \(\frac12\sqrt n\) edges.

For \(G=K_n=H(1,n)\), every turn has adjacent outside vertices; (3) is the reversal-odd boundary 3-tournament rule, and condition (2) is vacuous. Here the auxiliary edge coloring \(c\) may be chosen constant. Applying the terminal-path theorem directly to the full \(K_n\) recovers the stronger boundary estimate
\[
\ell\ge\sqrt{(n-1)/2}.\tag{6}
\]
The spectral resource matroid is \(M(K_n)\), so independence is equivalent to vertex simplicity along a path.

These instances share a single accepted-turn predicate, a single star-independent cycle-dominating resource matroid hypothesis, and a common terminal-set counting proof. To force the full \(n\)-edge cubical geodesic, an additional global condition must strengthen the square-root estimate (5).

Let \(D_F(u,v)\) be the greatest length of a vertex-simple path from \(u\) to \(v\) in a finite graph \(F\), with \(D_F(v,v)=0\) and \(D_F(u,v)=-\infty\) for vertices in different connected components. For connected \(F\), write
\[
S_F(z)=\sum_{v\in V(F)}D_F(z,v),\qquad
W_D(F)=\sum_{\{u,v\}\subseteq V(F)}D_F(u,v).
\]

**Lemma 1 (rooted detour bound).** For every connected graph \(F\) with \(m\) edges and root \(z\),
\[
\boxed{S_F(z)\ge m.}\tag{1}
\]
*Proof.* Run undirected depth-first search rooted at \(z\), obtaining a rooted tree \(T\). Every edge of \(F\) connects a vertex to an ancestor in \(T\). Assign the edge to its deeper endpoint \(v\). The number of edges so assigned is at most the depth \(d_T(z,v)\), because different assigned edges reach different ancestors of \(v\). Therefore
\[
m\le\sum_vd_T(z,v)\le\sum_vD_F(z,v)=S_F(z).
\]
Each tree path is a simple path of \(F\). \(\square\)

**Lemma 2 (one-vertex gluing).** Let connected graphs \(A,B\) meet at a single vertex \(z\), with no other connections, and have respective orders \(a,b\) and sizes \(m_A,m_B\). Then
\[
W_D(A\cup B)=W_D(A)+W_D(B)+(b-1)S_A(z)+(a-1)S_B(z).\tag{2}
\]
If each summand satisfies \(W_D(A)\ge(a-1)m_A\) and \(W_D(B)\ge(b-1)m_B\), then their union \(F\), of order \(a+b-1\) and size \(m_A+m_B\), satisfies
\[
\boxed{W_D(F)\ge(|V(F)|-1)|E(F)|.}\tag{3}
\]
*Proof.* A simple path between vertices in \(A\) cannot leave \(A\), because its return would repeat \(z\). For \(u\in A-\{z\}\), \(v\in B-\{z\}\), the longest simple \(u\)-to-\(v\) path concatenates a longest \(u\)-to-\(z\) path in \(A\) with a longest \(z\)-to-\(v\) path in \(B\). Thus \(D_F(u,v)=D_A(u,z)+D_B(z,v)\); summing the three pair types gives (2). Lemma 1 supplies \(S_A(z)\ge m_A\) and \(S_B(z)\ge m_B\). Substitution gives
\[
W_D(F)\ge(a-1)m_A+(b-1)m_B+(b-1)m_A+(a-1)m_B=(a+b-2)(m_A+m_B).
\]
\(\square\)

**Theorem 3 (natural detour-index classes).** Every block graph, every cactus graph, and every outerplanar graph \(F\) satisfies \(W_D(C)\ge(|V(C)|-1)|E(C)|\) in each connected component \(C\).

*Proof.* A complete graph \(K_s\) has \(D(u,v)=s-1\) for every distinct pair, giving equality \(W_D(K_s)=(s-1)\binom{s}{2}\). On a cycle \(C_s\), the longer arc between any pair is a simple path of length at least \(s/2\); for \(s\ge4\),
\[
W_D(C_s)\ge\tbinom{s}{2}\frac{s}{2}\ge s(s-1),
\]
and for \(s=3\) the cycle is a clique. Lemma 2 propagates the bound through cut vertices, proving the claims for block graphs (all blocks cliques) and cactus graphs (all blocks cycles or bridges).

For outerplanar graphs it suffices to consider a two-connected block of order \(s\). Such a block has a Hamiltonian outer-face boundary and at most \(2s-3\) edges. When \(s\ge6\), its cycle already guarantees
\[
W_D(F)\ge\tbinom{s}{2}\frac{s}{2}\ge(s-1)(2s-3)\ge(s-1)|E(F)|.
\]
For \(s=5\), the cycle provides detours of length at least three for all ten unordered pairs, so \(W_D(F)\ge30>4(2s-3)=28\). For \(s=4\), the four-cycle has detour index \(16>3(2s-3)=15\). For \(s=3\), the block is \(K_3\). Lemma 2 concludes the proof. \(\square\)

**Theorem 4 (detour-index criterion for arbitrary endpoint weights).** Suppose every connected component \(C\) of a graph \(F\) of order \(s\ge2\) satisfies \(W_D(C)\ge(s-1)|E(C)|\). Then, for every real weight function \(w:V(F)\to\mathbb R\),
\[
\boxed{
\sum_{v\in V(F)}\max_{u\in V(F)}
\bigl(w(u)+D_F(u,v)\bigr)\ge\sum_{v\in V(F)}w(v)+2|E(F)|.
}\tag{4}
\]
*Proof.* For each nontrivial component \(C\) independently choose a uniform random derangement \(\pi_C\). The image \(\pi_C(v)\) is uniformly distributed over the other \(s-1\) vertices. Thus
\[
\mathbb E\sum_{v\in C}D_C(\pi_C(v),v)
=\frac{2W_D(C)}{s-1}\ge 2|E(C)|.
\]
Set \(\pi(v)=v\) for isolated vertices. Some component-preserving permutation \(\pi\) has \(\sum_vD_F(\pi(v),v)\ge2|E(F)|\). For arbitrary weights, the left side of (4) is at least
\[
\sum_v \bigl(w(\pi(v))+D_F(\pi(v),v)\bigr)
=\sum_v w(v)+\sum_vD_F(\pi(v),v),
\]
as required. \(\square\)

**Theorem 5 (matroidal Hamming-product density theorem).** Let
\[
G=\mathop{\square}_{j=1}^{t}K_{m_j},\quad
R=\bigoplus_{j=1}^{t} M(K_{m_j}),
\]
and label an edge changing coordinate \(j\) from symbol \(a\) to \(b\) by the graphic root resource \((j,\{a,b\})\). Let \(H\) be any edge-subgraph of \(G\), retaining all vertices. Assume that every graph of \(H\)-edges within every one-coordinate fiber satisfies the componentwise detour-index criterion of Theorem 4. Then \(H\) has a simple path with an \(R\)-independent set of edge labels and length at least
\[
\boxed{\left\lceil\frac{2|E(H)|}{|V(G)|}\right\rceil.}\tag{5}
\]
This holds whenever the fiber graphs are block graphs or outerplanar graphs.

*Proof.* Fix factor order \(1,\ldots,t\). Let \(L_0(x)=0\), and inductively let \(L_j(x)\) be the greatest length of a path of \(H\) ending at \(x\) that uses only factors \(1,\ldots,j\), in nondecreasing factor order, traversing within each factor a single simple path among that factor's symbols. Each such path has \(R\)-independent labels: in each factor the traversed roots form a simple graph path, a forest in \(M(K_{m_j})\), and distinct factors belong to different direct summands. These paths are vertex-simple because their potential \(\phi(x)=\oplus_i e_{x_i}\) is injective and a repeated vertex would produce a dependence among traversed root vectors.

Fix a \(j\)-coordinate fiber \(F\). Any preceding path using only the first \(j-1\) factors keeps coordinate \(j\) fixed at some \(u\). Extending it by a simple path along fiber \(F\) from \(u\) to \(v\) retains root independence and vertex simplicity. Hence the dynamic-programming recurrence is
\[
L_j(v)=\max_{u\in V(F)}\{L_{j-1}(u)+D_F(u,v)\}.\tag{6}
\]
Apply (4) to the weights \(L_{j-1}\) in every such fiber. Sum the resulting inequalities over fibers and successively over \(j\):
\[
\sum_{x\in V(G)}L_t(x)\ge 2|E(H)|.
\]
Some terminal \(x\) therefore has \(L_t(x)\ge 2|E(H)|/|V(G)|\); integrality proves (5). \(\square\)

**Corollary 6 (canonical models).** All edge-subgraphs of \(Q_n=(K_2)^{\square n}\) satisfy the hypothesis of Theorem 5, since their one-coordinate fibers are isolated vertices or \(K_2\). The conclusion recovers the Leader--Long density theorem for coordinate-distinct cube geodesics and yields monochromatic paths of at least \(n/2\) edges in each color for antipodally odd colorings. The other canonical source model \(U_{2,n}\) has rank-one reduction \(U_{1,n}\), with basis graph \(K_n\) and resource matroid \(M(K_n)\): here the full graph's fiber is a clique, so the theorem guarantees a graphic-independent length-\((n-1)\) path. Boundary coloring resides instead on oriented two-edge windows, so the earlier root-basis tournament path theorem controls its unrestricted monochromatic \(\Omega(\sqrt n)\) paths.

**Remaining conjecture.** It remains to show whether \(W_D(F)\ge(|V(F)|-1)|E(F)|\) holds for every finite connected graph. The preceding results reduce any counterexample to a two-connected graph and prove the conjecture on natural families independent of either NORI construction. The full monochromatic antipodal cube geodesic requires further use of its global color-reversal polarity.

##### Rooted strengthening and reduction to two-connected blocks

The preceding detour-index theorem has a stronger rooted version on these graph families. For a connected graph \(F\), define
\[
\Delta_F(z)=S_F(z)-2|E(F)|+\deg_F(z).
\]
The proposed unrestricted **rooted detour inequality** is \(\Delta_F(z)\ge0\) for every root \(z\).

**Lemma 8 (rooted inequality is preserved by one-sums).** Suppose connected graphs \(A,B\) meet in one cut vertex \(q\), and \(\Delta_A(x)\ge0\) and \(\Delta_B(y)\ge0\) for every respective root \(x,y\). Then \(\Delta_{A\cup B}(z)\ge0\) for every root \(z\) of their union.

*Proof.* At the shared root, \(S_{A\cup B}(q)=S_A(q)+S_B(q)\), and both edge counts and degrees add, so \(\Delta_{A\cup B}(q)=\Delta_A(q)+\Delta_B(q)\ge0\). For a root \(z\in A-\{q\}\), maximal simple paths from \(z\) to \(B-\{q\}\) pass through \(q\). Hence
\[
S_{A\cup B}(z)=S_A(z)+S_B(q)+(b-1)D_A(z,q),
\]
where \(b=|V(B)|\). Since \(\deg_{A\cup B}(z)=\deg_A(z)\), this gives
\[
\Delta_{A\cup B}(z)=\Delta_A(z)+\Delta_B(q)+(b-1)D_A(z,q)-\deg_B(q)\ge0.
\]
Here \(D_A(z,q)\ge1\) and \(\deg_B(q)\le b-1\). The other case is symmetric. \(\square\)

**Theorem 9 (rooted inequality for outerplanar, cactus, and block graphs).** Every graph belonging to any of these three classes satisfies, in each connected component and for every root \(z\),
\[
\boxed{\sum_{v\in V(F)}D_F(z,v)\ge2|E(F)|-\deg_F(z).}\tag{8}
\]

*Proof.* For a clique \(K_s\), every root-to-other-vertex detour has length \(s-1\), so \(S(z)=(s-1)^2=2\binom{s}{2}-(s-1)\). For a cycle \(C_s\), its two neighbors of \(z\) can each be reached around the opposite arc in \(s-1\) edges. Thus \(S(z)\ge 2(s-1)=2|E(C_s)|-\deg(z)\). Lemma 8 settles block graphs and cacti.

For a two-connected outerplanar graph \(F\) of order \(s\), the Hamiltonian outer-face cycle provides two root-to-neighbor detours of length \(s-1\), and each of the remaining \(s-3\) vertices is reachable along the longer of two cycle arcs, giving a detour of length at least \(s/2\). Therefore
\[
S_F(z)\ge 2(s-1)+(s-3)\frac{s}{2}
=\frac{s^2+s-4}{2}.
\]
For \(s\ge4\), this is at least \(4s-8\), since the difference is \((s-3)(s-4)/2\). Outerplanarity gives \(m\le2s-3\), and two-connectivity gives \(\deg_F(z)\ge2\), so
\[
2m-\deg_F(z)\le4s-8\le S_F(z).
\]
For \(s=3\), the block is \(K_3\). Lemma 8 extends the result from blocks to all outerplanar graphs. \(\square\)

**Corollary 10 (rooted inequality implies the conjectural unrestricted weighted theorem).** If the rooted inequality (8) holds for every connected graph \(F\), then the detour-index inequality \(W_D(F)\ge(|V(F)|-1)|E(F)|\), and hence Theorems 4--5 without fiber restrictions, follow.

*Proof.* Summing (8) over all \(n\) choices of root gives
\[
2W_D(F)=\sum_z S_F(z)\ge 2n|E(F)|-\sum_z\deg_F(z)
=2(n-1)|E(F)|.
\]
Apply the derangement argument of Theorem 4 to deduce the unrestricted weighted inequality. \(\square\)

The rooted inequality is presently a **conjecture** outside the proved graph families. Lemma 8 reduces its search for counterexamples to two-connected blocks. The rooted and unrooted assertions have been tested on all connected labeled graphs of order at most six and on samples of seven-vertex graphs, without yielding a counterexample; such finite checks are diagnostic only.

##### Complete bipartite and complete split blocks

Two families with arbitrarily large non-outerplanar two-connected blocks also satisfy the rooted inequality, with explicit slack.

**Theorem 11 (complete bipartite blocks).** Let \(F=K_{a,b}\), where \(1\le a\le b\). For a root \(z\) in the part of size \(a\),
\[
\boxed{S_F(z)-(2|E(F)|-\deg_F(z))=2(a-1)^2.}\tag{9}
\]
For a root \(z\) in the part of size \(b\),
\[
\boxed{S_F(z)-(2|E(F)|-\deg_F(z))=
\begin{cases}
2(a-1)^2,&b=a,\\
2a(a-1),&b>a.
\end{cases}}\tag{10}
\]
In particular every complete bipartite graph satisfies the rooted detour inequality.

*Proof.* A simple path in a bipartite graph alternates the two parts. The greatest possible length of a path from a vertex of the smaller part to a vertex of the other part is \(2a-1\); between two vertices of the smaller part it is \(2(a-1)\). Between two vertices of the larger part it is \(2a\) when \(b>a\), and \(2(a-1)\) when \(b=a\). These maxima are attained by alternating paths using the allowed number of vertices in each part. Thus, for a root in the smaller part,
\[
S_F(z)=2(a-1)^2+b(2a-1),\quad
2|E(F)|-\deg(z)=2ab-b=b(2a-1),
\]
giving (9). For a root in the larger part and \(b>a\),
\[
S_F(z)=2a(b-1)+a(2a-1),\quad
2|E(F)|-\deg(z)=2ab-a.
\]
Subtracting yields \(2a(a-1)\). When \(a=b\), the two parts are symmetric and (9) applies. \(\square\)

**Theorem 12 (complete split blocks).** Let \(F=K_s\vee\overline{K_t}\), with \(s\ge1\) clique vertices and \(t\ge1\) independent vertices. Write \(C\) for the clique part and \(I\) for the independent part. For \(z\in C\),
\[
\boxed{S_F(z)-(2|E(F)|-\deg(z))=
\begin{cases}
t(t-1),&t\le s-1,\\
(s-1)^2,&t\ge s.
\end{cases}}\tag{11}
\]
For \(z\in I\),
\[
\boxed{S_F(z)-(2|E(F)|-\deg(z))=
\begin{cases}
(t-1)^2,&t\le s,\\
s(s-1),&t\ge s+1.
\end{cases}}\tag{12}
\]
In particular every complete split graph satisfies the rooted detour inequality.

*Proof.* Let \(L_{CC},L_{CI},L_{II}\) be the greatest simple-path lengths between two distinct vertices of the indicated types. In a path, independent vertices must be separated by clique vertices. Conversely any ordering of the required clique and independent vertices respecting that separation is a path in the join. Consequently
\[
L_{CC}=s+\min(t,s-1)-1,\quad
L_{CI}=s+\min(t,s)-1,\quad
L_{II}=s+\min(t,s+1)-1.
\]
(The \(CC\) and \(II\) expressions are used only if those endpoint types occur.) Therefore
\[
S_F(z)=
\begin{cases}
(s-1)L_{CC}+tL_{CI},& z\in C,\\
sL_{CI}+(t-1)L_{II},& z\in I.
\end{cases}
\]
The graph has \(m=\binom{s}{2}+st\) edges, a clique vertex has degree \(s-1+t\), and an independent vertex has degree \(s\). Substituting the three displayed path-length formulas and simplifying in the two threshold ranges gives (11) and (12). Every right-hand side is nonnegative. \(\square\)

**Corollary 13 (high-treewidth fiber family).** The rooted inequality (8), the detour-index hypothesis of Theorem 4, and the weighted endpoint inequality (4) hold on every connected graph whose blocks belong to the union of the following classes: outerplanar graphs, complete bipartite graphs, and complete split graphs. Consequently Theorem 5 holds for arbitrary Hamming-product edge-subgraphs all of whose one-coordinate fiber components have blocks of these types.

*Proof.* Theorems 9, 11, and 12 establish the rooted bound on each block, and Lemma 8 propagates it through the block-cut tree. Summing over roots and applying Theorem 4 establishes the weighted inequality. Theorem 5 then applies fiberwise. \(\square\)

These new block families include two-connected graphs of arbitrarily large treewidth (complete bipartite graphs with both part sizes increasing, and dense complete split graphs). They extend the preceding result beyond sparse planar exchange geometries. The stronger unrestricted rooted inequality remains open.

##### Dominant independent parts and complete multipartite graphs

We extend the rooted-detour inequality to graphs containing a complete bipartite spanning subgraph with a sufficiently large independent side, and thence to all complete multipartite graphs. The proofs use the preceding complete-bipartite slack formulas and the classical Ore Hamiltonian-connectedness theorem.

**Theorem 14 (stability under filling the smaller side of a biclique).** Let \(a\ge b\ge1\) be integers. Let \(A,B\) be disjoint vertex sets of cardinalities \(a,b\). Define
\[
G=\overline{K_a}\vee H,
\]
where \(H\) is an arbitrary simple graph on \(B\); thus \(A\) is independent and all \(ab\) edges between \(A,B\) belong to \(G\). Then for every root \(z\in V(G)\),
\[
\boxed{S_G(z)\ge 2|E(G)|-\deg_G(z).}\tag{13}
\]
For \(b\ge2\), a uniform lower bound for the rooted slack is
\[
\Delta_G(z):=S_G(z)-2|E(G)|+\deg_G(z)
\ge(b-1)(b-2).
\tag{14}
\]

*Proof.* Let \(G_0=K_{a,b}\subseteq G\), and let \(e=|E(H)|\le\binom b2\). Since adding edges does not reduce any longest simple-path length, \(S_G(z)\ge S_{G_0}(z)\). Also
\[
|E(G)|=ab+e,\qquad
\deg_G(z)=\deg_{G_0}(z)+\deg_H(z),
\]
where \(\deg_H(z)=0\) for \(z\in A\). Therefore
\[
\Delta_G(z)\ge\Delta_{G_0}(z)-2e+\deg_H(z)
\ge\Delta_{G_0}(z)-2e.
\tag{15}
\]
The complete-bipartite formulas in Theorem 11 give \(\Delta_{G_0}(z)\ge 2(b-1)^2\) for every root: the smaller part of \(K_{a,b}\) has order \(b\), and the displayed root slack on either side has this lower bound. Thus
\[
\Delta_G(z)\ge2(b-1)^2-b(b-1)=(b-1)(b-2)\ge0
\]
when \(b\ge2\). If \(b=1\), the only possible \(H\) has no edges and \(G=K_{a,1}\), already covered by Theorem 11. \(\square\)

The theorem allows an arbitrary pattern of up to \(\binom b2\) internal edges on \(B\), independent of whether the resulting graph is chordal, planar, or multipartite. The hypothesis is intrinsic: \(G\) contains an independent set of size at least half its order, every vertex of which is adjacent to every vertex outside that set.

**Theorem 15 (all complete multipartite graphs).** Every connected complete multipartite graph \(G=K_{a_1,\ldots,a_t}\) satisfies the rooted-detour inequality (13) for every root.

*Proof.* Let \(n=\sum_i a_i\) and \(a=\max_i a_i\). If \(a\ge n/2\), choose a part \(A\) of order \(a\) and let \(B=V(G)\setminus A\) have size \(b=n-a\le a\). All edges between \(A\) and \(B\) occur and \(A\) is independent. Theorem 14 applies, regardless of the internal multipartite graph on \(B\).

Now suppose \(a<n/2\). Since \(a\) is integral, \(a\le(n-1)/2\). Every nonadjacent pair \(u,v\) belongs to one common part of cardinality \(s\le a\), so
\[
\deg_G(u)+\deg_G(v)=2(n-s)\ge n+1.
\]
By Ore's Hamiltonian-connectedness theorem (Ore's degree-sum criterion for Hamiltonian-connected graphs, as recalled in Gould–Yu, *On hamiltonian-connected graphs*, J. Graph Theory 18 (1994), 841–860), \(G\) has a Hamiltonian path between every pair of distinct vertices. Hence \(D_G(z,v)=n-1\) for every \(v\ne z\), and
\[
S_G(z)=(n-1)^2\ge\sum_{v\ne z}\deg_G(v)=2|E(G)|-\deg_G(z),
\]
since every degree is at most \(n-1\). For orders \(n\le2\) the claim follows by direct inspection. \(\square\)

**Corollary 16 (weighted detours and Hamming products).** The weighted endpoint inequality (4) holds for every graph whose connected components are complete multipartite, or whose blocks are complete multipartite, outerplanar, complete bipartite, or complete split graphs. The matroidal Hamming-product density theorem (Theorem 5) therefore applies whenever all one-coordinate fiber components have blocks from this enlarged list.

*Proof.* Theorem 15 and Lemma 8 verify the rooted inequality through one-sum gluing. Summation over roots yields the detour-index inequality; Theorem 4 supplies arbitrary endpoint weights, which Theorem 5 propagates factor by factor. \(\square\)

The complete-multipartite result covers high-connectivity and arbitrarily large graphic circuits without requiring a bounded treewidth or chordal graph structure. It leaves the unrestricted rooted-detour and vertex-deletion conjectures open.


##### Augmentation from a Hamiltonian-connected core

**Theorem 17 (sharp vertex-deletion inequality).** Let \(G\) be connected and \(H=G-v\) Hamiltonian-connected. Write \(N=|V(H)|\), \(K=N_G(v)\), and \(k=|K|\). Then for every \(z\in V(H)\),
\[
\boxed{S_G(z)-S_H(z)\ge 2k-\mathbf1_{\{z\in K\}}.}\tag{16}
\]
Consequently the rooted-detour inequality holds at every root of \(G\).

*Proof.* For \(N=1\) the graph is \(K_2\). Suppose \(N\ge2\). If \(K=\{z\}\), then \(D_G(z,v)=1=2k-\mathbf1_{\{z\in K\}}\) and every old endpoint detour can only increase. In every other case there is a neighbor \(u\in K-\{z\}\). A Hamiltonian \(z\)-to-\(u\) path in \(H\), followed by \(uv\), shows \(D_G(z,v)=N\). Every existing endpoint \(w\ne z\) has \(D_H(z,w)=N-1\), and its new detour length is either \(N-1\) or \(N\). The latter occurs whenever a Hamiltonian \(z\)-to-\(w\) path in \(H\) has two consecutive vertices in \(K\): insert \(v\) between them.

If \(2k-\mathbf1_{\{z\in K\}}\le N\), the newly available endpoint \(v\) supplies the claimed increase. If \(k>\lceil N/2\rceil\), any Hamiltonian path in \(H\) has two consecutive vertices in \(K\), since at most \(\lceil N/2\rceil\) positions of a path can be chosen without consecutive positions. All \(N-1\) old endpoints therefore gain one, and \(S_G(z)-S_H(z)=2N-1\ge2k-\mathbf1_{\{z\in K\}}\). The sole remaining possibility is \(N=2m-1\), \(k=m\), \(z\notin K\). Choose \(w\in K\) and a Hamiltonian \(z\)-to-\(w\) path in \(H\). An alternating placement of \(m\) marked \(K\)-vertices among \(2m-1\) positions with no adjacent marks must start with a marked position; since \(z\notin K\), a consecutive \(K\)-pair must occur. Inserting \(v\) gives a gain of one at endpoint \(w\), producing the required increment \(N+1=2m=2k\). This proves (16).

Because \(H\) is Hamiltonian-connected, \(S_H(z)=(N-1)^2\ge 2|E(H)|-\deg_H(z)\); adding (16) proves the rooted inequality on \(H\)'s vertices. At root \(v\) there are two cases. If \(k\ge2\), for each \(w\in H\) choose \(u\in K-\{w\}\), traverse a Hamiltonian \(u\)-to-\(w\) path of \(H\) after the initial edge \(vu\), and obtain \(D_G(v,w)=N\). Thus \(S_G(v)=N^2\ge 2|E(H)|+k=2|E(G)|-\deg_G(v)\). If \(k=1\), let \(u\) be the sole neighbor; then
\[
S_G(v)=N+S_H(u)=N+(N-1)^2
\ge2|E(H)|+1=2|E(G)|-\deg_G(v).
\]
This completes the proof. \(\square\)

The result is an unconditional one-vertex extension theorem for *arbitrary attachment neighborhoods*, provided the core is Hamiltonian-connected. Its proof isolates the failure mechanism for general vertex deletion: the desired detour increment is available by inserting a vertex between adjacent neighbors on a long endpoint path. It remains open whether an aggregate version of this argument works for arbitrary connected deletion cores.


Let \(G=H(k,3)=K_3^{\square k}\), \(k\ge1\), with canonical edge-resource matroid \(N=N_{\mathrm{sp}}(G)\cong\bigoplus_{j=1}^kM(K_3)\). Let \(c:E(G)\to\mathbb F_2\) and let \(b(u,v,w)\) label ordered two-edge turns under the intrinsic rules
\[
b(u,v,w)+b(w,v,u)=\mathbf1_{\{uw\in E(G)\}}\pmod2,\qquad
b(u,v,w)=c(uv)+c(vw)\quad\text{if }uw\notin E(G).\tag{1}
\]
A path is **accepted** if all internal \(b\)-turns are zero and its edge resources are independent in \(N\).

A **coordinate triangle** arises by fixing all but one coordinate. If its three edges are monochromatic, its three unoriented two-edge walks have one accepted orientation apiece. These orientations induce a tournament on their endpoint pairs. Call the triangle **defective** if this tournament is transitive; let \(B\) be the total number of defective coordinate triangles.

**Theorem (ternary turn conservation).** There exists an accepted monochromatic \(N\)-independent path of length
\[
\boxed{\ell\ge\left\lceil k-\frac{B}{2\cdot3^k}\right\rceil\ge\left\lceil\frac{5k}{6}\right\rceil.}\tag{2}
\]
Consequently the Hamming-root factor-count conjecture \(\ell\ge k\) holds for all \(k\le5\); it also holds for arbitrary \(k\) whenever no coordinate triangle is defective. In particular, it holds whenever every coordinate triangle is bichromatic.

*Proof.* Let \(F\) be any subgraph of a coordinate \(K_3\) whose edges have one fixed color. Let \(D_F(u,v)\) denote the greatest length of an accepted simple \(u\)-to-\(v\) path within \(F\), taking \(D_F(u,u)=0\) and \(-\infty\) for unreachable pairs. Every single edge is accepted. Put \(\delta(F)=1\) if \(F=K_3\) and its accepted two-step endpoint tournament is transitive; put \(\delta(F)=0\) otherwise.

**Local permutation lemma.** There exists a permutation \(\pi\) of the three vertices of \(F\), using only reachable source-target pairs, for which
\[
\sum_v D_F(\pi(v),v)\ge 2|E(F)|-\delta(F).\tag{3}
\]
For zero edges choose the identity; for one edge transpose its endpoints to obtain total length two. For two edges \(F=a-b-c\), reversal oddness on its triangular turn accepts one of \(a-b-c\), \(c-b-a\). If the former is accepted, use the cyclic source-target assignment \(a\to c,\ c\to b,\ b\to a\), giving total length \(2+1+1=4\); reverse it in the other case. For three edges, each ordered pair has a direct path of length one, and one orientation of each two-edge path is accepted. These longer path orientations constitute a tournament on three vertices. Its cyclic case admits a cyclic permutation with three length-two paths, total six. Its transitive case admits a cyclic permutation with two forward arcs of length two and one reverse arc of length one, total five. This establishes (3).

For any real weight function \(w\) on the three vertices, put \(T_F(w)(v)=\max_u\{w(u)+D_F(u,v)\}\). The permutation lemma implies
\[
\sum_v T_F(w)(v)\ge\sum_v w(v)+2|E(F)|-\delta(F),\tag{4}
\]
because \(\sum_vw(\pi(v))=\sum_vw(v)\).

Now choose one edge color \(s\). Process coordinates in order \(1,\ldots,k\), and define \(L_j(x)\) as the largest length of a color-\(s\) accepted path ending at \(x\), whose coordinate indices are nondecreasing and whose successive moves within one coordinate visit distinct symbols. Set \(L_0(x)=0\). For each \(j\)-coordinate triangle fiber, with color-\(s\) edge subgraph \(F\), the dynamic-programming recurrence is
\[
L_j(v)=\max_u\{L_{j-1}(u)+D_F(u,v)\}.\tag{5}
\]
The concatenated path is accepted: turns internal to one coordinate segment are accepted by definition of \(D_F\); turns joining different factors have nonadjacent outer vertices, and their label is \(s+s=0\) by (1). Its edge-resource family is independent because within each coordinate factor it is a simple path in the root \(K_3\), hence a forest in the corresponding direct-sum factor \(M(K_3)\). Nondecreasing factor order also makes the full vertex path simple.

Apply (4) to weights \(L_{j-1}\) in every fiber of coordinate \(j\), and sum over the \(3^{k-1}\) fibers. Then
\[
\sum_{x\in V(G)}L_j(x)\ge\sum_xL_{j-1}(x)+2|E_s^{(j)}|-B_s^{(j)},
\]
where \(E_s^{(j)}\) comprises the color-\(s\) edges of the \(j\)-factor and \(B_s^{(j)}\) its defective monochromatic triangles. Summing across coordinates gives
\[
\sum_x L_k^{(s)}(x)\ge 2|E_s|-B_s.\tag{6}
\]
Summing (6) over the two colors gives
\[
\sum_x\bigl(L_k^{(0)}(x)+L_k^{(1)}(x)\bigr)
\ge 2|E(G)|-B=2k3^k-B.
\]
Thus some color and some terminal vertex satisfy
\[
L_k^{(s)}(x)\ge k-\frac B{2\cdot3^k}.
\]
There are \(k3^{k-1}\) coordinate triangles, so \(B\le k3^{k-1}\), and (2) follows. For \(k\le5\), \(\lceil5k/6\rceil=k\); if \(B=0\), the first inequality gives \(\ell\ge k\). \(\square\)

**Interpretation.** The local weighted transfer contribution equals \(2|E(F)|\) except for a transitive monochromatic coordinate triangle, which can lose one unit. Every other fiber, including a bichromatic triangle, conserves the full weighted transfer budget. This gives the first linear-in-\(k\) bound for arbitrary polarized ternary Hamming systems, establishes the full factor-count guarantee in dimensions \(k\le5\), and reduces the unrestricted ternary gap to controlling global compensation for transitive monochromatic triangles. The binary endpoint remains the NORI1 antipodal spanning problem.

**Corollary (critical six-factor rigidity).** If a triangular-turn system on \(H(6,3)\) has no accepted monochromatic resource-independent path of length six, then (i) all \(6\cdot3^5=2\cdot3^6\) coordinate triangles are defective, hence monochromatic with transitive accepted-turn tournaments; (ii) there are \(3^6\) defective triangles of each color; and (iii) for every permutation \(\sigma\) of the six factor indices, each color \(s\), and each terminal vertex \(x\), the longest accepted color-\(s\) path whose coordinate segments occur in order \(\sigma\) and do not revisit a symbol within one segment has length five.

*Proof.* Put \(V=3^6\). The bound (2) forces \(B\ge2V\) if no length-six path exists, while the total number of coordinate triangles equals \(2V\). Thus every coordinate triangle is defective. Let \(B_s\) count the defective triangles of color \(s\). Every edge of color \(s\) lies in one of these monochromatic coordinate triangles, so \(|E_s|=3B_s\). The transfer inequality (6) gives
\[
\sum_x L_6^{(s)}(x)\ge2|E_s|-B_s=5B_s.
\]
Since every terminal length is at most five, the sum is at most \(5V\), hence \(B_s\le V\). As \(B_0+B_1=2V\), equality holds: \(B_0=B_1=V\). Therefore \(\sum_xL_6^{(s)}(x)\ge5V\) while each summand is at most five, so every \(L_6^{(s)}(x)=5\). The dynamic-programming proof is invariant under permutations of the coordinate order, giving the terminal conclusion for every \(\sigma\). \(\square\)

This isolates the equality case: a perfectly balanced system of transitive monochromatic coordinate triangles with flat five-edge terminal profiles under all \(6!\) factor orders.

**Lemma (forced predecessor profile in the critical case).** In the hypothetical six-factor counterexample of the preceding corollary, fix any order of factors, its final factor \(j\), and a coordinate-\(j\) fiber. If the fiber is monochromatic in color \(s\), then the three values of \(L_5^{(s)}\) just before processing that fiber are, in some order,
\[
\boxed{(3,3,4),}\tag{7}
\]
with the value four located at the sink of the fiber's accepted two-step endpoint tournament. For the other color, whose fiber edge subgraph is empty, all three predecessor values are five.

*Proof.* By the corollary, for both colors and every terminal vertex, \(L_6^{(s)}=5\). Equality also holds in every summed local transfer inequality (4): the two colors' total transfer lower bounds sum to the maximum possible \(10\cdot3^6\), and each of their terminal outputs is at most five. Thus on a defective color-\(s\) triangle, with input weights \(w\), the transfer output \(T_F(w)\) is the constant vector \((5,5,5)\) and \(\sum w=10\).

Relabel the triangle so its accepted length-two endpoint tournament is transitive \(a\to b\), \(a\to c\), \(b\to c\). Every direct edge has length one; the accepted length-two arcs have length two. Therefore
\[
T_F(w)(a)=\max\{w_a,w_b+1,w_c+1\},\quad
T_F(w)(b)=\max\{w_b,w_a+2,w_c+1\},\quad
T_F(w)(c)=\max\{w_c,w_a+2,w_b+2\}.
\]
To reach output five at \(a\), some predecessor other than \(a\) must have weight four (the possibility \(w_a=5\) would force the output at \(b\) to be at least seven). Weight four at \(b\) would force output at \(c\) to be at least six. Hence \(w_c=4\). The output constraints at \(b,c\) give \(w_a,w_b\le3\), and the sum \(\sum w=10\) forces \(w_a=w_b=3\). When the fiber has no edges of color \(1-s\), its transfer map is the identity, so the opposite-color predecessor vector is \((5,5,5)\). \(\square\)

Thus a six-factor counterexample would force a specific \((3,3,4)\) profile around every last-factor monochromatic triangle, in every permutation of the six factors.

## Hamming Gallery Polarities and Twisted Transport

### Permutation galleries, unimodular transport, and endpoint degrees

Let \(H(k,q)=K_q^{\square k}\) with \(k\ge1,q\ge2\), and \(N_{\rm sp}\) its canonical spectral-resource matroid on graph edges. Fix a root \(x\), let \(d=k(q-1)\), and put
\[
D_x=\{(i,b): i\in[k],\ b\in[q]\setminus\{x_i\}\},
\qquad |D_x|=d.
\]
Orient a root edge by the direction of traversal. Its spectral difference vector is \(e_b-e_a\) in coordinate summand \(i\) when that coordinate changes from \(a\) to \(b\).

**Theorem 1 (full-rank gallery permutation correspondence).** Every \(N_{\rm sp}\)-independent path of length \(d\) beginning at \(x\) is obtained uniquely from a permutation \(\pi=(t_1,\ldots,t_d)\) of \(D_x\): for \(t_j=(i,b)\), replace the current \(i\)-th coordinate value by \(b\). Every such permutation yields a resource-independent path.

**Proof.** Resource independence means the transitions in each coordinate form a forest in the graphic matroid \(M(K_q)\). Since the coordinate transitions form a trail, they cannot revisit a coordinate symbol. Rank saturation forces \(q-1\) transitions in each coordinate, so the successive visited symbols are a permutation of the \(q-1\) symbols other than \(x_i\). Interleaving the \(k\) coordinate sequences gives a permutation of \(D_x\). Conversely a permutation of \(D_x\) gives a simple coordinate path in each complete-graph factor, hence a forest, and the resource vectors for different factors occupy direct-sum subspaces. The entire set of \(d\) edge vectors is therefore independent. \(\square\)

**Corollary 2 (diametral endpoints and uniform fibers).** Every full-rank path from \(x\) finishes at some \(y\) differing from \(x\) in all \(k\) coordinates. Every such \(y\) occurs, and the number of full-rank paths with prescribed directed endpoints \(x,y\) is
\[
\boxed{\frac{d!}{(q-1)^k}}.
\tag{1}
\]
In particular there are \(d!\) full-rank paths from \(x\), distributed uniformly among the \((q-1)^k\) diametral endpoints.

**Proof.** In each coordinate the prescribed terminal symbol is the last visited among \(q-1\) tokens. Choose the orders of the \(q-2\) remaining tokens in \((q-2)!\) ways, and interleave the \(k\) ordered coordinate sequences in \(d!/((q-1)!)^k\) ways. Their product is (1). \(\square\)

In the cube endpoint \(H(n,2)=Q_n\), this is the familiar \(n!\) antipodal geodesics between fixed endpoints. At \(H(1,n)=K_n\) the count becomes \((n-2)!\) Hamilton paths between prescribed distinct vertices.

**Theorem 3 (unimodular triangular change of basis).** Let \(w_{i,b}=e_b-e_{x_i}\), for \((i,b)\in D_x\), be the root-star basis of the spectral resource space. For \(\pi=(t_1,\ldots,t_d)\), write \(u_j\) for the vector of its \(j\)-th oriented path edge, and \(p(j)<j\) for the previous occurrence of the coordinate of \(t_j\), if one exists. Then
\[
u_j=w_{t_j}-w_{t_{p(j)}} ,
\]
where the second term is zero if \(p(j)\) does not exist. The matrix with columns \(u_j\) in the ordered basis \((w_{t_1},\ldots,w_{t_d})\) is unitriangular. Consequently, relative to any fixed ordering of the root-star basis,
\[
\boxed{\det(u_1,\ldots,u_d)=\operatorname{sgn}(\pi).}
\tag{2}
\]
Adjacent token swaps reverse this determinant, thereby connecting resource-basis orientation to the permutohedral exchange graph.

**Proof.** The changed coordinate goes from the value visited at its previous occurrence (or \(x_i\) for its first occurrence) to the newly named symbol. Subtracting their root-star vectors gives the identity above. The new token contributes diagonal coefficient one and any previous token contributes a coefficient in an earlier row. Hence the matrix is unitriangular, and the remaining determinant sign is the sign of the ordering permutation. \(\square\)

**Proposition 4 (signed endpoint enumeration).** Fix \(x\) and a diametral endpoint \(y\). The signed sum \(\sum_{\pi:x\to y}\operatorname{sgn}(\pi)\) is zero for \(q\ge4\), and also for \(q=2,k\ge2\). For \(q=3\), its absolute value is \(k!\), with the sign depending on the reference token order.

**Proof.** When \(q\ge4\), each factor has at least two nonterminal tokens. Interchange two chosen nonterminal tokens from one factor in the permutation word. The endpoint stays fixed, and the determinant changes sign; this is a sign-reversing fixed-point-free involution. For \(q=2,k\ge2\), each factor has one token, and every permutation has the same endpoint. Transpose the positions of two fixed tokens to pair signs.

For \(q=3\), the prescribed endpoint leaves a pair of ordered tokens in each coordinate. Every endpoint gallery is a shuffle of these \(k\) ordered pairs. Partition the \(2k\) word positions into adjacent slots \((1,2),(3,4),\ldots,(2k-1,2k)\). For a shuffle in which one slot contains tokens from different coordinates, choose the first such slot and swap its two tokens. This is a fixed-point-free sign-reversing involution, preserving each coordinate's internal token order. The surviving shuffles have every slot occupied by the two tokens of the same coordinate in their prescribed order. There are \(k!\) such shuffles. Permuting two complete slots makes four elementary transpositions, so all survivors have the same sign. The signed sum thus has absolute value \(k!\). \(\square\)

**Interpretation.** The cube and rank-two uniform endpoints have a common permutation-gallery and unimodular resource orientation algebra. The untwisted signed degree cancels at both endpoints for growing rank; the ternary Hamming interpolation retains a nonzero integer signed endpoint enumerator. This alone does not force any color-coherent gallery. Any determinant-degree attempt for arbitrary cube antipodal coloring must incorporate the coloring, root transport, or a signed-cover twist.

### Polarized Hamming turn geometry and the displacement conjecture

Let \(M=\bigoplus_{i=1}^{k}U_{r_i,E_i}\), with \(m_i:=|E_i|\ge2\) and \(1\le r_i<m_i\). The summand ground sets are the intrinsic connected components of \(M\). Define
\[
M^\flat=\bigoplus_iU_{1,E_i},\quad
G=\Gamma(M^\flat)=\square_iK_{E_i},\quad
N=\bigoplus_i M(K_{E_i}),\quad
d=\operatorname{rk}(N)=\sum_i(m_i-1).
\tag{1}
\]
An edge changing symbol \(a\) to \(b\) in factor \(i\) carries resource \((i,\{a,b\})\), represented by \(e_b-e_a\) in the \(i\)-th summand. The potential \(\Phi(x)=\bigoplus_i e_{x_i}\) is injective; its edge differences realize \(N\). Consequently every star of \(G\) is an \(N\)-basis, and every graph cycle is \(N\)-dependent.

A **factorwise polarity** \(\tau\) is either the identity, or a product of fixed-point-free involutions \(\tau_i:E_i\to E_i\) on all factors, with \(k\ge2\) in the latter case. Put \(\chi_\tau=0\) in the identity case and \(1\) otherwise. Equivalently, \(\chi_\tau\) is the canonical faithful character of \(\langle\tau\rangle\) into \(\mathbb F_2\), including the trivial group. Let \(c:E(G)\to\mathbb F_2\) color undirected edges and satisfy
\[
c(\tau e)=c(e)+\chi_\tau.
\tag{2}
\]
For each nonbacktracking turn \((u,v,w)\), prescribe a bit \(b(u,v,w)\) according to the **triangle-curvature rule**
\[
\boxed{
\begin{cases}
b(u,v,w)+b(w,v,u)=1,&uw\in E(G),\\
b(u,v,w)=c(uv)+c(vw),&uw\notin E(G).
\end{cases}}
\tag{3}
\]
The triangular case is an unrestricted tournament comparison; the other case tests edge-color agreement. For products of cliques, a turn is triangular precisely when its two steps change one factor. Both clauses are invariant under isomorphisms of the matroid with its chosen polarity.

Call a path \(P=(v_0,\ldots,v_\ell)\) an **accepted gallery** when its edge resources are \(N\)-independent, its graph edges have a common \(c\)-color, and every interior turn has bit \(b=0\). Matroid independence entails vertex simplicity because a closed subwalk yields an \(N\)-dependent cycle. The witness predicate is uniform across all members of this class.

**Theorem 1 (common rank-growth bound).** Every preceding geometry has an accepted gallery with
\[
\ell\ge\left\lceil\tfrac12\sqrt d\right\rceil .
\tag{4}
\]

*Proof.* One \(c\)-color class spans at least half the edges of the \(d\)-regular graph \(G\). Its spanning subgraph \(H\) has average degree at least \(d/2\). At every vertex of \(H\), put a tournament on the incident edges: for a pair forming a triangular turn, favor the bit-zero direction, which is unique by (3); for a nontriangular turn, both bit values are zero because both edges have the same color, so choose either direction. Restrict \(N\) to the edges of \(H\). Vertex stars remain independent, and all cycles of \(H\) remain dependent. The cycle-dominating resource-matroid terminal theorem of Article XI provides an \(N\)-independent path respecting these tournaments and containing at least \(\sqrt{\bar d(H)/2}\ge\sqrt d/2\) edges. Its turns have bit zero and its edges share one color. Taking the ceiling proves the claim. \(\square\)

The **polar displacement** is the intrinsic quantity
\[
\rho(G,\tau):=\min_x d_G(x,\tau x)=k\chi_\tau.
\tag{5}
\]

**Conjecture U (polarized Hamming displacement).** Every preceding geometry admits an accepted gallery with
\[
\boxed{\ell\ge \max\left\{
\left\lceil\tfrac12\sqrt{\operatorname{rk}N}\right\rceil,\,
\rho(G,\tau)\right\}.}
\tag{6}
\]
This is one quantitative conjecture over a continuous family of root-exchange geometries. It uses the same resource-independence, color-consistency, and turn-admissibility witness in every instance.

**Theorem 2 (NORI1 equivalence).** Conjecture U over the entire polarized Hamming class holds if and only if NORI1 holds for every admissible dimension.

*Proof that U implies NORI1.* For \(M=\bigoplus_{i=1}^nU_{1,2}\), \(G=Q_n\), \(N\) is the coordinate-partition resource matroid of rank \(n\), and \(\tau\) toggles all \(n\) factors. An arbitrary antipodally odd coloring of undirected cube edges satisfies (2), while all nonbacktracking turns are nontriangular and (3) becomes \(b(u,v,w)=c(uv)+c(vw)\). Thus accepted galleries are monochromatic coordinate-distinct geodesics. Equation (6) forces \(n\) edges. Independence then forces each coordinate to appear once, so the endpoints are antipodal.

*Proof that NORI1 implies U.* For identity polarity, Theorem 1 proves (6). Suppose \(\tau=\prod_i\tau_i\) is nontrivial. Choose any \(a_i\in E_i\) and consider the induced cube
\[
Q(a)=\prod_i\{a_i,\tau_i(a_i)\}\subseteq G.
\tag{7}
\]
It is invariant under \(\tau\), and \(\tau\) acts on it as cube complementation. By (2), the restriction of \(c\) is antipodally odd. NORI1 supplies a monochromatic geodesic of \(k\) edges within this cube. Each step changes a different factor, so its \(N\)-resources lie in different direct summands and are independent. Every turn changes two factors; hence its outside endpoints are nonadjacent in \(G\) and its bit is zero by (3). It is an accepted gallery of length \(k=\rho(G,\tau)\). Theorem 1 separately gives a gallery of length at least \(\lceil\sqrt d/2\rceil\). Taking the longer witness establishes (6). \(\square\)

**Corollary 3 (both original models).** The cube model \(M=\bigoplus U_{1,2}\), with its canonical nontrivial polarity, yields a full monochromatic antipodal geodesic by U. For the boundary model \(M=U_{2,n}\), the root is \(G=K_n\), \(N=M(K_n)\), \(d=n-1\), and \(\tau=\mathrm{id}\). Choose \(c\equiv0\). All turns are triangular, so any reversal-odd boundary coloring \(b(a,v,w)\) satisfies (3). Accepted galleries are vertex-simple bit-zero tight paths. Theorem 1 gives at least \(1+\lceil\sqrt{n-1}/2\rceil\) original vertices, and the unpartitioned terminal bound in Article XI improves this to \(1+\sqrt{(n-1)/2}\). Reversing the original vertex word gives the opposite color.

**Corollary 4 (even-alphabet antipodal extension).** Assuming NORI1, for any \(k\ge2\), any even \(m_i\ge2\), any factorwise fixed-point-free \(\tau\), and any edge coloring of \(\square_iK_{m_i}\) with \(c(\tau e)=1-c(e)\), there is a monochromatic path of \(k\) edges from some \(x\) to \(\tau x\), using every factor once. No triangle-turn comparison restricts this witness. This follows from the invariant cube (7).

**Proposition 5 (polarity is invisible locally).** In a nontrivially polarized product, fix \(x\) and \(R\) with \(2R<k\). Any arbitrary coloring of the edges induced by the radius-\(R\) ball about \(x\) extends to a global coloring satisfying (2).

*Proof.* If an edge \(e\) and \(\tau e\) both lay within that ball, some vertex \(y\) and its image \(\tau y\) would both be within distance \(R\) of \(x\). This contradicts \(k=d_G(y,\tau y)\le2R\). The edge action is free, since \(\tau\) changes every factor and \(k\ge2\), so each edge orbit has size two. Choose the prescribed bit on the unique orbit representative lying in the ball, put its complement on the translated edge, and fill all other orbits arbitrarily. \(\square\)

Theorem 1 is a uniform local rank-growth mechanism common to both examples. Theorem 2 shows that promoting this mechanism to full polar displacement is equivalent to the unresolved NORI1 assertion. The freedom in triangular turns and the forced color-potential rule on commuting-factor turns arise from the same graph's intrinsic local geometry. The current implication from NORI1 to U uses an invariant cube slice, leaving open a direct rank-saturation proof that interacts with all factors without restricting to that slice.

Let \(G=H(k,q)=K_q^{\square k}\), \(k\ge1,q\ge2\), with canonical spectral edge-resource matroid
\[
N_{\rm sp}(G)\cong\bigoplus_{j=1}^kM(K_q).
\]
Let \((b,c)\) be an arbitrary triangular-turn system:
\[
b(u,v,w)+b(w,v,u)=\mathbf1_{\{uw\in E(G)\}},\qquad b(u,v,w)=c(uv)+c(vw)\quad(uw\notin E(G)),\tag{1}
\]
with binary arithmetic. A path is **accepted** when all turns have label zero and the traversed edge resources are independent in \(N_{\rm sp}(G)\).

**Theorem (uniform linear factor bound).** Every system (1) admits an accepted monochromatic path with
\[
\boxed{\ell\ge\left\lceil\frac{k}{2}\right\rceil.}\tag{2}
\]
In combination with the cycle-dominating resource-matroid terminal theorem, this gives
\[
\boxed{\ell\ge\max\left\{\left\lceil\frac{k}{2}\right\rceil,\left\lceil\frac12\sqrt{k(q-1)}\right\rceil\right\}.}\tag{3}
\]
No antipodal condition, representability assumption beyond the canonical spectral resource, or restriction on triangle-turn orientations is required.

*Proof.* Fix one edge color \(s\). Process factors in the order \(1,\ldots,k\). Define \(L_j(x)\) as the maximum length of a color-\(s\) path ending at \(x\) that uses at most one edge from each factor \(1,\ldots,j\), with factor indices strictly increasing. Put \(L_0(x)=0\). A transition between different factors is nontriangular and has turn label \(s+s=0\); no turn inside a factor occurs. Consequently every such path is accepted. The use of each factor at most once guarantees independence in the direct-sum graphic resource matroid.

For a \(j\)-coordinate fiber, let \(F\) be the subgraph of \(K_q\) consisting of its color-\(s\) edges, and let \(w\) be the weights \(L_{j-1}\) at its \(q\) vertices. The new terminal weights are
\[
T_F(w)(v)=\max\bigl\{w(v),\max_{u:\,uv\in E(F)}(w(u)+1)\bigr\}.\tag{4}
\]
Put \(\delta_v=T_F(w)(v)-w(v)\ge0\). For each edge \(uv\in E(F)\), the inequalities \(T_F(w)(u)\ge w(v)+1\) and \(T_F(w)(v)\ge w(u)+1\) imply
\[
\delta_u+\delta_v\ge2.
\]
Summing over edges, and using \(\deg_F(v)\le q-1\), yields
\[
2|E(F)|\le\sum_v\deg_F(v)\delta_v\le(q-1)\sum_v\delta_v.
\]
Thus
\[
\sum_vT_F(w)(v)\ge\sum_vw(v)+\frac{2|E(F)|}{q-1}.\tag{5}
\]
Sum (5) over all \(j\)-coordinate fibers and then \(j=1,\ldots,k\):
\[
\sum_{x\in V(G)}L_k(x)\ge\frac{2|E_s|}{q-1}.\tag{6}
\]
Since the regular graph \(G\) has \(q^k\) vertices and \(k(q-1)q^k/2\) edges, one color class contains at least \(k(q-1)q^k/4\) edges. For that color, (6) shows some terminal \(x\) satisfies
\[
L_k(x)\ge\frac{2|E_s|}{(q-1)q^k}\ge\frac{k}{2}.
\]
Integrality proves (2); combining with the previously established root-resource square-root bound proves (3). \(\square\)

**Strengthening for nonhomogeneous Hamming products.** The same argument applies to
\[
G=\square_{j=1}^kK_{q_j},\qquad q_j\ge2,
\]
with root resources \(\bigoplus_jM(K_{q_j})\), because each \(j\)-fiber contributes \(2|E_s^{(j)}|/(q_j-1)\). Summing over the two color classes, the total normalized contribution is
\[
\frac1{|V(G)|}\sum_{j=1}^k\frac{2|E(G)^{(j)}|}{q_j-1}
=\sum_{j=1}^k1=k.
\]
Hence some color has a path of length at least \(\lceil k/2\rceil\), for any factor sizes, under the same intrinsic nontriangular potential condition.

**Relation to the central conjecture.** The theorem explains why the factor-count scale \(k\) is available independently of the spectral degree \(k(q-1)\): each Cartesian factor supplies one unit of aggregate weighted terminal growth across both colors. It proves half the proposed spanning factor-count guarantee uniformly, while the ternary turn-conservation theorem improves the coefficient to \(5/6\) for \(q=3\) and isolates its remaining loss to transitive monochromatic coordinate triangles.

### Linear resource-independent path growth from square-flat turns

Let \(H(k,q)=K_q^{\square k}\), \(k\ge1,q\ge2\), and let \(N_{\rm sp}\) be its canonical spectral resource matroid of rank \(d=k(q-1)\). Let \(b(u,v,w)\in\mathbb F_2\) be defined on all nonbacktracking ordered turns, satisfying the mixed triangle/square axioms:

(i) if \(uw\in E(H)\), then \(b(u,v,w)+b(w,v,u)=1\);

(ii) there is one global edge coloring \(c:E(H)\to\mathbb F_2\) such that \(b(u,v,w)=c(uv)+c(vw)\) whenever \(uw\notin E(H)\).

A zero-turn path has \(b=0\) at every internal turn, and it is resource-independent when its edge vectors are independent in \(N_{\rm sp}\). The involution hypothesis at the cubical endpoint, when applicable, can be imposed additionally; it is unnecessary here.

**Theorem 1 (factor-count linear guarantee).** Every such mixed triangle/square turn system contains a zero-turn \(N_{\rm sp}\)-independent path with at least
\[
\boxed{\ell\ge \lceil k/2\rceil}
\tag{1}
\]
edges. The bound is uniform in \(q\) and valid for arbitrary triangular reversal-odd comparisons.

**Proof.** Choose any two symbols in each \(K_q\) factor and let \(C\subseteq H(k,q)\) be the induced copy of the hypercube \(Q_k\) on their \(2^k\) product vertices. Every two successive edges of a geodesic in \(C\) change distinct Cartesian factors. Therefore the two outer vertices of every such turn differ in two factors and are nonadjacent in the full Hamming graph. By (ii) its turn label is the sum of the colors of the two edges.

The restriction of \(c\) to \(C\) gives a binary edge coloring of \(Q_k\). Of its two monochromatic subgraphs, at least one has average degree at least \(k/2\), because \(Q_k\) is \(k\)-regular and the edge sets partition its edges. By the Leader–Long long-geodesic theorem (Imre Leader and Eoin Long, *Long geodesics in subgraphs of the cube*, Discrete Mathematics 326 (2014), 29–33), any subgraph of a hypercube of average degree \(a\) contains a graph geodesic of at least \(a\) edges. Hence the denser color subgraph of \(C\) contains a monochromatic geodesic with at least \(\lceil k/2\rceil\) edges.

Such a geodesic changes each cube coordinate at most once. Its consecutive edge colors coincide; by (ii), all its turn labels are zero. The spectral resource vectors of its edges lie in distinct coordinate summands and are linearly independent. Thus it is an accepted zero-turn \(N_{\rm sp}\)-independent path of the required length. \(\square\)

In conjunction with the general mixed-turn terminal bound previously proved in Article XI, of order \(\sqrt{k(q-1)}\), this yields complementary, simultaneous guarantees of linear growth in factor count and square-root growth in resource rank:
\[
\ell_{\max}\ge \max\!\left\{\lceil k/2\rceil,\ \tfrac12\sqrt{k(q-1)}\right\}.
\tag{2}
\]
Formula (2) is a lower-bound combination; the stronger proposed unified conjecture asks for \(\ell\ge k\) in addition to the square-root term. The remaining gap is therefore a factor at most two in the factor-count branch.

**Lemma 2 (matroidal minimum-degree growth).** Let \(G\) be a finite simple graph with a matroid \(N\) on \(E(G)\) such that each vertex star is independent in \(N\) and every graph cycle is dependent in \(N\). If a subgraph \(F\subseteq G\) has minimum degree \(\delta\), then from every vertex of \(F\) there is an \(N\)-independent simple path with at least \(\delta\) edges.

**Proof.** Start at any vertex. If the current path has \(r<\delta\) edges, its edge set \(X\) is independent of rank \(r\). At the terminal vertex \(v\), the incident \(F\)-edges are independent in \(N\), so at most \(r\) of them can belong to \(\operatorname{cl}_N(X)\). Thus some incident edge \(e=vw\) is outside the closure, and \(X+e\) remains independent. If \(w\) were an earlier vertex of the path, \(X+e\) would contain a graph cycle and therefore be dependent, a contradiction. Hence the path can be extended. Continue until it has at least \(\delta\) edges. \(\square\)

**Corollary 3 (self-contained density bound).** Under the hypotheses of Lemma 2, every subgraph \(F\subseteq G\) of average degree \(a\) contains an \(N\)-independent simple path of length at least \(a/2\). Moreover, for every two-color edge coloring of a \(d\)-regular graph \(G\) under these hypotheses, some monochromatic \(N\)-independent path has length at least \(d/4\).

**Proof.** Iteratively delete vertices of current degree below \(a/2\). Such deletions strictly increase the average degree of the remaining nonempty graph, so a nonempty subgraph with minimum degree at least \(a/2\) remains. Apply Lemma 2. For a two-coloring, one color subgraph has average degree at least \(d/2\); apply the first assertion to it. \(\square\)

This corollary supplies a self-contained weaker version of (1), namely \(\ell\ge k/4\) on any induced \(Q_k\), without invoking the sharper Leader–Long theorem.

**Scope and asymmetry.** The rank-\(k\) root cube witness in Theorem 1 uses only cross-factor square-flat turns. Consequently it survives completely arbitrary and non-edge-orderable triangular comparisons. At the boundary endpoint \(k=1\), however, it supplies just one edge and does not replace the square-root boundary-tournament theorem. The mixed turn system combines the flat edge-potential geometry responsible for linear-in-\(k\) growth with freely oriented triangular comparisons responsible for the separate \(\sqrt{d}\) tournament bound.

### Edge-free coordinatewise polarities and the maximal Hamming reduction

Let \(G=\square_{i=1}^kK_{E_i}\), with \(|E_i|\ge2\). Let \(\tau=\prod_i\tau_i\) be any coordinatewise involution of \(G\), allowing fixed symbols in the individual factors. Define
\[
J(\tau)=\{i:\operatorname{Fix}(\tau_i)=\varnothing\},
\qquad h(\tau)=|J(\tau)|.
\tag{1}
\]
A nontrivial binary edge polarity is an undirected-edge coloring \(c\) satisfying \(c(\tau e)=1-c(e)\).

**Theorem 1 (edge-freeness and displacement).** For a nonidentity coordinatewise involution \(\tau\), the following are equivalent:

(i) \(\tau\) fixes no undirected edge of \(G\);

(ii) \(h(\tau)\ge2\);

(iii) there exists a binary edge polarity \(c\) with \(c(\tau e)=1-c(e)\).

Furthermore, for every coordinatewise involution, including the identity,
\[
\boxed{\min_{x\in V(G)} d_G(x,\tau x)=h(\tau).}
\tag{2}
\]

*Proof.* Every factor indexed by \(J(\tau)\) changes its symbol at every vertex, while every factor outside \(J(\tau)\) has at least one fixed symbol. A shortest Hamming path from \(x\) to \(\tau x\) changes precisely the factors on which \(x_i\ne\tau_i x_i\). Choosing fixed symbols in the other factors gives (2).

Assume \(h(\tau)\ge2\). An edge \(e\) changes one coordinate \(j\), leaving every other coordinate constant. At least one factor in \(J(\tau)\setminus\{j\}\) changes its constant symbol under \(\tau\); thus \(\tau e\ne e\), proving (i).

Conversely, assume \(h(\tau)\le1\) and \(\tau\) is nonidentity. Choose a component \(j\) in which \(\tau_j\) exchanges two distinct symbols \(a,b\); if \(h(\tau)=1\), take the sole fixed-point-free component for \(j\). For every \(i\ne j\), choose a fixed symbol of \(\tau_i\), possible by the definition of \(h\). Then the edge whose changing coordinate \(j\) joins \(a\) to \(b\), with all other coordinates fixed, is stabilized setwise by \(\tau\). Hence (i) implies (ii). An edge-stabilizing involution cannot support an odd binary edge polarity since it would require \(c(e)=1-c(e)\). If all edge orbits have size two, assign one arbitrary bit per orbit and its complement to the other edge, producing such a coloring. This proves the equivalence. \(\square\)

**Theorem 2 (NORI1 gives full intrinsic displacement).** Suppose \(\tau\) is nonidentity and \(h(\tau)\ge2\). Let \(c\) be any edge polarity of \(G\) and \(b\) any turn system obeying the triangle-curvature rule
\[
b(u,v,w)+b(w,v,u)=1\quad(uw\in E(G)),
\qquad b(u,v,w)=c(uv)+c(vw)\quad(uw\notin E(G)).
\tag{3}
\]
Assuming NORI1, there is a monochromatic accepted gallery \(P\) from \(x\) to \(\tau x\) of length \(h(\tau)\). Its edge labels are independent in the canonical resource matroid
\(N=\bigoplus_i M(K_{E_i})\).

*Proof.* For every \(i\in J(\tau)\) choose a symbol \(a_i\), and in every component outside \(J(\tau)\) choose a fixed symbol \(f_i=\tau_i(f_i)\). The induced subgraph
\[
Q=\prod_{i\in J(\tau)}\{a_i,\tau_i(a_i)\}
 \times\prod_{i\notin J(\tau)}\{f_i\}
\tag{4}
\]
is an \(h(\tau)\)-cube invariant under \(\tau\), whose restricted involution is its antipode. The restriction of \(c\) to \(Q\) is therefore antipodally odd. NORI1 supplies a monochromatic geodesic \(P\) joining antipodal vertices of \(Q\). The gallery changes every active component once, using pairwise different direct summands of \(N\), so its resource labels are independent. Consecutive steps change different factors, making the endpoints of their turn nonadjacent in the ambient Hamming graph. The second rule in (3) makes the bit of every interior turn zero. Since \(Q\) is induced, \(P\) is a path of \(G\) and its endpoints are \(x,\tau x\). Its length is \(h(\tau)\), which equals the minimum displacement by Theorem 1. \(\square\)

**Corollary 3 (largest coordinatewise polarized class).** Let \(\mathcal H\) consist of all pairs \((M,\tau)\) where \(M=\bigoplus_iU_{r_i,E_i}\) is a partition matroid and \(\tau\) acts coordinatewise on its intrinsic rank-one reduction, subject to either \(\tau=\mathrm{id}\) or \(h(\tau)\ge2\). Equip these pairs with undirected colors and the turn rule (3), imposing \(c(\tau e)=c(e)+\chi_\tau\), where \(\chi_\tau=0\) for the identity and \(1\) otherwise. Every member has an accepted gallery of length at least \(\lceil\sqrt{\operatorname{rk}N}/2\rceil\), by the cycle-dominating resource-matroid terminal theorem. The single strengthened assertion
\[
\boxed{\ell\ge\max\left\{
\left\lceil\tfrac12\sqrt{\operatorname{rk}N}\right\rceil,\,
\min_x d_G(x,\tau x)\right\}
\tag{5}
\]
for an accepted gallery in every member of \(\mathcal H\) is equivalent to NORI1.

*Proof.* The uniform rank-growth theorem in the preceding Article XI Hamming Subsection applies unchanged to \(\mathcal H\); its proof does not require nontrivial polarity. In the nontrivial case Theorem 2 supplies an independent witness of length equal to the second term of (5). The longer of these two witnesses proves (5) assuming NORI1. Conversely take \(M=\bigoplus_{i=1}^n U_{1,2}\) with its antipodal involution. Then the second term of (5) is \(n\), and an accepted gallery of \(n\) edges is a monochromatic antipodal cube geodesic. Thus (5) entails NORI1. \(\square\)

Theorem 1 establishes why this class is maximal among coordinatewise involutions admitting an odd coloring on undirected edges: every excluded nonidentity involution stabilizes an edge and admits no such coloring. Theorem 2 extends the antipodal cube transfer to Hamming products with odd-sized factors, arbitrary mixed component ranks, and fixed symbols in some factors; only the \(h(\tau)\) forced-moving components enter the invariant cube. This extension retains the same graphic resource matroid and the same local turn law that yield unrestricted boundary-tournament square-root paths when \(\tau\) is the identity.

### Canonical central polarity of partition-matroid Hamming roots

Let \(M=\bigoplus_{i\in I}U_{r_i,E_i}\), with \(1\le r_i<|E_i|\). The connected-component decomposition is intrinsic to \(M\). Define the rank-one reduction and its root graph
\[
M^\flat=\bigoplus_{i\in I}U_{1,E_i},
\qquad G_M=\Gamma(M^\flat)=\square_{i\in I}K_{E_i}.
\tag{1}
\]
Put \(I_2=\{i:|E_i|=2\}\), \(s=|I_2|\). On every two-element ground set the exchange of its elements is a choice-free involution. Let
\[
\eta_M(x)_i=
\begin{cases}
E_i\setminus\{x_i\},&i\in I_2,\\
x_i,&i\notin I_2.
\end{cases}
\tag{2}
\]
Here \(x=(x_i)\) is a basis of \(M^\flat\), and in the first case the complement is understood as its unique member. The map \(\eta_M\) depends only on \(M\).

**Theorem 1 (center of the root-matroid automorphism group).** If \(s=0\), the center of \(\operatorname{Aut}(M^\flat)\) is trivial. If \(s\ge1\), it has order two and is generated by \(\eta_M\). Thus the unique possible nonidentity root automorphism commuting with all automorphisms of \(M^\flat\) is simultaneous exchange of every two-element component.

*Proof.* For every \(m\ge2\), let \(k_m\) denote the number of components of size \(m\). The action on the ground set identifies
\[
\operatorname{Aut}(M^\flat)
=\prod_{m\ge2}\left(S_m^{k_m}\rtimes S_{k_m}\right)
\tag{3}
\]
(the factor for \(k_m=0\) is omitted). A central element must normalize and centralize the independent symmetric groups acting within individual components. Conjugation carries the subgroup supported on a component \(i\) to the subgroup supported on its image; commuting with all such subgroups forces each component to be preserved individually. The restriction to a component of size \(m\) must then lie in \(Z(S_m)\), which is trivial for \(m\ge3\) and is \(S_2\) when \(m=2\). Finally, centrality with respect to permutations of equally sized components forces all two-element components to be flipped together or none to be flipped. Both choices commute with every automorphism. Thus the claimed center consists of \(\mathrm{id}\) and \(\eta_M\) when \(s\ge1\), and only \(\mathrm{id}\) otherwise. \(\square\)

**Theorem 2 (maximal canonical odd-coloring domain).** If \(s\ge1\), the canonical involution \(\eta_M\) has graph displacement
\[
d_{G_M}(x,\eta_M x)=s\qquad\text{for every }x.
\tag{4}
\]
It acts without fixed undirected graph edges if and only if \(s\ge2\). Consequently a binary edge coloring satisfying
\[
c(\eta_M e)=1-c(e)
\tag{5}
\]
exists if and only if \(s\ge2\).

*Proof.* Formula (2) changes the coordinate on each of the \(s\) two-element factors and fixes all others, giving (4). If \(s=1\), fix arbitrary coordinates in the other factors and take the edge that changes the unique two-element factor; it is preserved as an undirected edge by \(\eta_M\). If \(s\ge2\), every graph edge changes just one factor, while \(\eta_M\) flips at least one other factor; hence the edge moves to a different edge. The edge-orbit action then consists of two-element orbits, and assigning complementary colors to their two members gives (5). A fixed edge would require its color to equal its complement, which is impossible. \(\square\)

Define the **canonical polarized partition class**
\[
\mathcal C_{\rm can}=
\{M=\bigoplus_iU_{r_i,E_i}:s(M)=0\text{ or }s(M)\ge2\},
\tag{6}
\]
and put \(\tau_M=\eta_M\) for \(s\ge2\), and \(\tau_M=\mathrm{id}\) for \(s=0\). This polarization is canonically determined by the undecorated matroid \(M\); no symbols, matchings, preferred bases, or external involutions are chosen. The excluded case \(s=1\) is precisely the case when the only nonidentity central involution would stabilize an undirected edge. Equip the root graph with the canonical graphic resource matroid
\[
N_M=\bigoplus_i M(K_{E_i})
\tag{7}
\]
and the mixed turn law: on triangular turns, reversal exchanges bit zero and bit one, while on nontriangular turns the bit is the sum of the two incident graph-edge colors. A witness is a monochromatic path with independent \(N_M\)-resources and all turn bits zero.

**Corollary 3 (undecorated common class and quantitative conjecture).** Both \(M_{\rm cub}=\bigoplus_{i=1}^nU_{1,2}\) for \(n\ge2\) and \(M_{\rm bd}=U_{2,n}\) for \(n\ge3\) lie in \(\mathcal C_{\rm can}\). In the former, \((G_M,\tau_M)=(Q_n,\text{complement})\); in the latter, \((G_M,\tau_M)=(K_n,\mathrm{id})\). The resource rank is
\(d=\sum_i(|E_i|-1)\).
On this class the single strengthened path assertion
\[
\boxed{\ell\ge\max\left\{
\left\lceil\tfrac12\sqrt d\right\rceil,\ s(M)
\right\}}
\tag{8}
\]
for a monochromatic resource-independent accepted gallery is equivalent to NORI1.

*Proof.* The universal \(\lceil\sqrt d/2\rceil\) lower bound follows from the cycle-dominating resource-matroid terminal theorem, as in the preceding polarized Hamming Subsection. In the cube model the canonical polarity is complement and \(s=d=n\), so (8) gives a full monochromatic antipodal geodesic. For the reverse implication, assume NORI1. When \(s=0\) the terminal theorem proves (8). When \(s\ge2\), fix one symbol in each factor of size at least three and retain both symbols of each two-element factor. The induced \(s\)-cube is invariant under \(\eta_M\), which acts as the antipode there. The restricted edge coloring is odd. NORI1 yields a monochromatic geodesic changing every two-element factor once; it has independent root-graphic resources and all its turns are nontriangular, so the turn bits vanish. This yields a gallery of length \(s\). Take the longer of this witness and the terminal-theorem witness to obtain (8). In the boundary model \(s=0,d=n-1\), the root is \(K_n\), and the triangular turn law realizes every ordinary reversal-odd boundary tournament, giving the common square-root bound. \(\square\)

**Interpretation.** Simultaneous binary-factor complementation is the unique nontrivial symmetry canonically available from the root-matroid automorphism group. Arbitrary pairings in factors of size at least four lead to legitimate *chosen* polarizations but cannot be obtained as automorphism-equivariant operations on those factors. The canonical class (6) therefore answers the intrinsic-polarization objection for the partition-matroid Hamming family. The rank-saturation term of (8) remains equivalent to NORI1; the shared resource-rank growth mechanism is proved independently.

### Affine cube-edge colorings: permutation syndromes and elimination of two-dimensional obstructions

Let \(Q_n\) have coordinates in \(\mathbb F_2^n\). Consider arbitrary affine binary colors on its undirected coordinate edges,
\[
c_i(x)=a_i+\sum_{j\ne i}B_{ij}x_j,
\qquad a\in\mathbb F_2^n,\quad B\in\mathbb F_2^{n\times n},\quad B_{ii}=0.
\tag{1}
\]
The formula is independent of the toggled bit \(x_i\), as required for an undirected edge color. The antipodal oddness condition \(c_i(x+\mathbf1)=c_i(x)+1\) is equivalent to
\[
B\mathbf1=\mathbf1.
\tag{2}
\]
The matrix \(B\) is the linear cross-coordinate influence operator of the edge coloring. Write \(V=\mathbb F_2^n/\operatorname{im}B\), and denote the quotient map by \(p:\mathbb F_2^n\to V\).

For a permutation \(\pi=(i_1,\dots,i_n)\), put
\[
v_\pi(i)=\sum_{j\text{ occurring before }i\text{ in }\pi} B_{ij}.
\tag{3}
\]
A geodesic beginning at \(x\) and flipping the coordinates in order \(\pi\) has color word, indexed by its step directions,
\[
c_{\pi}(x)=a+Bx+v_\pi.
\tag{4}
\]
It is monochromatic if and only if
\[
a+v_\pi\in\operatorname{im}B.
\tag{5}
\]
Indeed a constant color-one word can be converted to a color-zero word by replacing its root \(x\) by \(x+\mathbf1\), using (2). The obstruction to a given order is therefore the quotient syndrome \(p(a+v_\pi)\).

**Lemma 1 (cyclic rotation identity).** If \(\pi=(i,i_2,\ldots,i_n)\) and \(\operatorname{rot}\pi=(i_2,\ldots,i_n,i)\), then
\[
v_{\operatorname{rot}\pi}=v_\pi+e_i+Be_i,
\qquad
p(v_{\operatorname{rot}\pi})=p(v_\pi)+p(e_i).
\tag{6}
\]
For every permutation the \(n\) cyclic rotations consequently trace in \(V\) a closed walk whose successive increments are \(p(e_{i_1}),\ldots,p(e_{i_n})\).

*Proof.* Moving the first direction \(i\) to the end changes its own predecessor parity from zero to \(\sum_{j\ne i}B_{ij}=1\). For every other direction \(j\), the presence of \(i\) among its predecessors is removed, changing its parity by \(B_{ji}\). Thus the syndrome difference is \(e_i+Be_i\). The second equation follows by quotienting by \(\operatorname{im}B\), and the cyclic walk follows by iteration. The walk closes because \(\sum_i p(e_i)=p(\mathbf1)=0\) by (2). \(\square\)

**Theorem 2 (affine rank-codimension-two closure).** Suppose (1)--(2) hold and
\[
\boxed{\operatorname{rank}_{\mathbb F_2}B\ge n-2.}
\tag{7}
\]
Then there exist a starting vertex \(x\) and a coordinate permutation \(\pi\) such that the entire antipodal geodesic \(x\to x+\mathbf1\) following \(\pi\) is monochromatic. In particular every antipodally odd affine cube-edge coloring whose cross-influence matrix has nullity at most two satisfies NORI1.

More precisely, for every \(a\), the quotient-syndrome set
\[
\boxed{\{p(v_\pi):\pi\in S_n\}=V}
\tag{8}
\]
whenever \(\dim V\le2\). If \(\dim V=0\), every permutation admits a monochromatic geodesic; for each successful permutation, the number of roots of either prescribed constant color is \(2^{n-\operatorname{rank}B}\), and the roots for opposite colors are antipodal translates.

*Proof.* Let \(t=\dim V=n-\operatorname{rank}B\). The claim is immediate for \(t=0\), since then \(V=0\). If \(t=1\), the classes \(p(e_i)\) span \(V\), so some \(i\) has \(p(e_i)\ne0\). Take any permutation starting with \(i\). Lemma 1 shows that its syndrome and the syndrome of its cyclic rotation differ by the nonzero element of \(V\), and hence together attain all of \(V\).

Now let \(t=2\). Put \(w_i=p(e_i)\in V\cong\mathbb F_2^2\). Their sum vanishes by (2), and they span \(V\), since the \(e_i\) span \(\mathbb F_2^n\). Suppose there are distinct indices \(i,j,h\) with
\[
w_i=w_h=u\ne0,\qquad w_j=v\notin\{0,u\}.
\tag{9}
\]
Choose a permutation beginning \((i,j,h)\). Its first four cyclic-rotation syndromes, by (6), differ from the first by
\[
0,\quad u,\quad u+v,\quad v,
\]
which exhaust \(V\). Thus (8) follows in this case.

It remains to show that (9) can fail only in a special configuration and that this configuration also satisfies (8). Let \(N_u,N_v,N_{u+v}\) be the multiplicities of the three nonzero vectors of \(V\) among the \(w_i\). The identity \(\sum_iw_i=0\) forces
\[
N_u\equiv N_v\equiv N_{u+v}\pmod2.
\tag{10}
\]
Since the \(w_i\) span \(V\), if some nonzero value occurs at least twice and another linearly independent nonzero value occurs, (9) holds. If no such pair exists, (10) implies that the only nonzero \(w_i\) are three distinct values \(u,v,u+v\), each appearing once. Denote their indices by \(i,j,h\) respectively. All other \(w_\ell\) vanish.

Because \(p(Be_\ell)=0\) for every \(\ell\), this exceptional configuration gives
\[
B_{i\ell}u+B_{j\ell}v+B_{h\ell}(u+v)=0.
\]
Linear independence of \(u,v\) yields
\[
B_{i\ell}=B_{j\ell}=B_{h\ell}\qquad\text{for every }\ell.
\tag{11}
\]
The three rows \(i,j,h\) of \(B\) coincide. Their diagonal entries vanish, so their entries in the three columns \(i,j,h\) are all zero. By (2), their common row has odd sum; consequently some index \(z\notin\{i,j,h\}\) satisfies
\[
B_{iz}=B_{jz}=B_{hz}=1,\qquad w_z=0.
\tag{12}
\]

Choose \(\pi=(i,z,j,h,\ldots)\). Its first cyclic-rotation syndromes attain the three values
\[
p(v_\pi)+\{0,u,u+v\};
\]
the missing fourth value is \(p(v_\pi)+v\). Swap the adjacent symbols \(z,j\), obtaining \(\pi'=(i,j,z,h,\ldots)\). An adjacent transposition of directions \(j,z\) changes \(v_\pi\) by
\(B_{jz}e_j+B_{zj}e_z\). By (12),
\[
p(v_{\pi'})=p(v_\pi)+w_j=p(v_\pi)+v,
\]
the missing value. Thus the two permutations together with the displayed cyclic rotations exhaust \(V\). This proves (8) for \(t=2\).

Finally, (8) permits choosing \(\pi\) so that \(p(v_\pi)=p(a)\), making (5) hold. The system \(Bx=a+v_\pi\) then has \(2^{n-\operatorname{rank}B}\) roots. Adding \(\mathbf1\) to any solution changes all its edge colors from zero to one by (2), proving the last assertion. \(\square\)

**Corollary 3 (necessary structure of affine counterexamples).** An affine antipodally odd counterexample to NORI1, if one exists, must have
\[
\boxed{\dim\ker B^{\mathsf T}\ge3.}
\tag{13}
\]
Furthermore for any \(B\) satisfying (2), the quotient syndrome of a cyclically rotated permutation changes by a coordinate class \(p(e_i)\). Thus the possible affine obstruction is a simultaneous multi-syndrome obstruction on the permutation exchange geometry; no obstruction of dimension one or two survives arbitrary cyclic rotations and adjacent transpositions.

The theorem is dimension-independent, and imposes no symmetry on \(B\). Its proof uses the same resource-permutation language as the dual-basis galleries of Article XI. It establishes full rank saturation for a broad affine NORI1 class, while leaving nonlinear colorings and affine influence matrices of nullity at least three open.

#### 4. Uniform random affine closure probability

Consider the uniform ensemble of affine antipodally odd cube-edge colorings (1): choose each intercept \(a_i\) independently and uniformly, and independently choose each row \(B_{i,*}\) uniformly among binary vectors with \(B_{ii}=0\) and odd Hamming weight. Every admissible affine coloring occurs with equal probability.

**Theorem 4 (random influence rank).** For \(n\ge3\), if \(T=n-\operatorname{rank}B=\dim\ker B^{\mathsf T}\), then
\[
\boxed{\mathbb E(2^T-1)=1-2^{1-n}.}
\tag{14}
\]
Consequently,
\[
\boxed{\Pr(T\ge3)\le\frac{1-2^{1-n}}7<\frac17,}
\tag{15}
\]
and, by Theorem 2, the probability that an affine antipodally odd cube-edge coloring admits a full monochromatic antipodal geodesic is at least
\[
\boxed{1-\frac{1-2^{1-n}}7>\frac67.}
\tag{16}
\]
The conclusion is uniform in the dimension and in the arbitrary intercept vector.

*Proof.* Expand \(2^T-1=\sum_{y\ne0}\mathbf1_{\{y^{\mathsf T}B=0\}}\). Since \(B\mathbf1=\mathbf1\), any left-kernel vector \(y\) has even Hamming weight, so an odd-weight \(y\) contributes zero probability. For an even-weight nonzero \(y\), choose two distinct positions \(i,j\) in its support. A uniform row \(B_{i,*}\) is supported on the odd-parity affine hyperplane with coordinate \(i\) fixed to zero; its translation space is
\[
W_i=\{z:z_i=0,\ z\cdot\mathbf1=0\}.
\]
For \(n\ge3\), the sum \(W_i+W_j\) is the full even-parity hyperplane \(W=\{z:z\cdot\mathbf1=0\}\). Indeed \(W_i^\perp=\langle\mathbf1,e_i\rangle\) and \(W_j^\perp=\langle\mathbf1,e_j\rangle\), whose intersection is \(\langle\mathbf1\rangle\); taking orthogonal complements proves the claim. The sum of the two independent uniform rows is consequently uniform on an even-parity affine coset, which here equals \(W\). Adding the other independently chosen rows in the even support of \(y\) preserves uniformity on \(W\), since their total parity is even. Thus
\[
\Pr(y^{\mathsf T}B=0)=|W|^{-1}=2^{-(n-1)}
\]
for every even-weight nonzero \(y\). There are \(2^{n-1}-1\) such vectors. Summing proves (14). On the event \(T\ge3\), the number \(2^T-1\) is at least seven, so Markov's inequality gives (15). Theorem 2 guarantees the desired geodesic on the complementary event \(T\le2\), proving (16). \(\square\)

The estimate concerns an ensemble of arbitrary affine cross-coordinate influence operators, including nonsymmetric ones. It is independent of the chosen coordinate order and complements the permutation-syndrome closure theorem, which applies deterministically whenever \(T\le2\).

### Affine root-syndrome gallery transport and corank-one closure

Let \(n\ge2\), \(M\in\mathbb F_2^{n\times n}\) have zero diagonal and \(M\mathbf1=\mathbf1\), and color the undirected coordinate-\(i\) edges of \(Q_n\) by
\[
c_i(x)=a_i+\sum_jM_{ij}x_j.
\tag{1}
\]
The row-oddness condition \(M\mathbf1=\mathbf1\) is the antipodal-odd coloring law. For a coordinate permutation \(\pi\in S_n\), put
\[
t_i(\pi)=\sum_{\pi^{-1}(j)<\pi^{-1}(i)}M_{ij}.
\tag{2}
\]
Let \(R=\operatorname{im}M\), \(q=n-\operatorname{rk}M\), and \(\Phi(\pi)=t(\pi)+R\in\mathbb F_2^n/R\).

**Theorem 1 (root criterion).** A monochromatic full geodesic with coordinate order \(\pi\) exists if and only if \(\Phi(\pi)=a+R\). For each qualifying \(\pi\), there are \(2^{q+1}\) directed monochromatic geodesics with that order, counted over both colors and all roots. Swapping two consecutive directions \(i,j\) changes the quotient syndrome by
\[
\boxed{\Phi(\pi')-\Phi(\pi)=\Delta_{ij}+R,\qquad
\Delta_{ij}=M_{ij}e_i+M_{ji}e_j.}
\tag{3}
\]

**Proof.** The edge traversed in direction \(i\) from root \(x\), after visiting the earlier directions, has color \(a_i+(Mx)_i+t_i(\pi)\). Hence the full word is constant \(s\) if and only if \(Mx=a+t(\pi)+s\mathbf1\). Since \(\mathbf1=M\mathbf1\in R\), existence is independent of \(s\) and is equivalent to the quotient criterion. Each solvable equation has \(2^q\) solutions \(x\) for either \(s\). Adjacent exchange modifies only the two preceding-direction sums for \(i,j\), giving (3). \(\square\)

**Theorem 2 (universal quotient span and balanced characters).** For every matrix satisfying (1),
\[
\boxed{R+\operatorname{span}\{\Delta_{ij}:i<j\}=\mathbb F_2^n.}
\tag{4}
\]
Consequently the affine span of \(\Phi(S_n)\) is the entire quotient. Moreover, every nonzero linear character of \(\mathbb F_2^n/R\) takes each of its values on at least \((n-1)!\) permutations.

**Proof.** A vector \(z\) annihilating both \(R\) and all the \(\Delta_{ij}\) obeys \(M^Tz=0\) and \(z_iM_{ij}+z_jM_{ji}=0\) for all \(i\ne j\). Fixing \(i\) and summing the latter relations over \(j\ne i\) gives
\[
0=z_i\sum_jM_{ij}+\sum_jM_{ji}z_j=z_i+(M^Tz)_i=z_i.
\]
Thus \(z=0\), proving (4). Every \(\Delta_{ij}\) appears as a difference of \(\Phi\)-values on two permutations in which \(i,j\) are adjacent, giving the affine-span assertion.

For nonzero \(z\in\ker M^T\), (4) ensures some \(i,j\) satisfy \(z\cdot\Delta_{ij}=1\). There are \((n-1)!\) permutations containing \(i,j\) consecutively in that order and the same number containing \(j,i\) consecutively. Swapping the two entries pairs them and flips the value of \(z\cdot\Phi\). Thus each character value occurs at least \((n-1)!\) times. \(\square\)

**Corollary 3 (unrestricted nonsymmetric affine closure in corank at most one).** If \(\operatorname{rk}M\ge n-1\), then for every choice of \(a\), the coloring (1) admits a monochromatic full antipodal geodesic. There are \(2n!\) directed such geodesics when \(\operatorname{rk}M=n\), and at least \(4(n-1)!\) when \(\operatorname{rk}M=n-1\).

**Proof.** If \(q=0\), the quotient is trivial and every order qualifies. If \(q=1\), Theorem 2 forces both elements of the quotient to be attained and guarantees at least \((n-1)!\) permutations in either class. Apply Theorem 1. \(\square\)

**Proposed affine quotient-surjectivity conjecture.** Every zero-diagonal row-odd binary matrix satisfies
\[
\Phi(S_n)=\mathbb F_2^n/\operatorname{im}M.
\tag{5}
\]
Its proof would settle all antipodally odd *affine* cube-edge colorings. Full affine span from Theorem 2 is a necessary step but does not alone imply (5) when \(q\ge2\). The general nonlinear NORI1 conjecture remains separate.

**Falsification check.** Direct exhaustive enumeration of all row-odd zero-diagonal matrices at dimensions \(3,4,5\) found no counterexample to (5): respectively \(8,256,32768\) matrices. The largest observed coranks were respectively \(1,2,3\). No computation is used in the proofs.

**Relationship to prior work.** The manuscript's forest-coupling theorem gives rooted switch bounds for sparse symmetric \(M\). The results here apply to arbitrary nonsymmetric matrices of corank at most one and establish an unrestricted-dimensional gallery-exchange span statement for every affine antipodally odd interaction matrix.

#### Theorem 4 (corank-two affine NORI1 closure)

Under the assumptions of Theorem 1, if
\[
\boxed{\operatorname{rk}_{\mathbb F_2}M\ge n-2,}
\tag{11}
\]
then **every** choice of \(a\) yields a monochromatic full antipodal geodesic. When \(\operatorname{rk}M=n-2\), there are at least \(16\) directed monochromatic full geodesics. Thus affine root-syndrome surjectivity (5) holds for quotient dimensions \(q=0,1,2\), with no symmetry condition on \(M\).

**Lemma 4.1 (cyclic gallery transport).** Let \(\pi=(i_1,\ldots,i_n)\) and let \(\rho\pi=(i_2,\ldots,i_n,i_1)\). In \(Q=\mathbb F_2^n/\operatorname{im}M\), write \(g_i=e_i+\operatorname{im}M\). Then
\[
\boxed{\Phi(\rho\pi)=\Phi(\pi)+g_{i_1}.}
\tag{12}
\]
Successive cyclic rotations visit the cosets
\[
\Phi(\pi),\quad\Phi(\pi)+g_{i_1},\quad
\Phi(\pi)+g_{i_1}+g_{i_2},\quad\ldots.
\tag{13}
\]

**Proof.** Moving \(i_1\) from first to last reverses its order relative to every other direction. Its own coordinate of \(t\) changes by \(\sum_{j\ne i_1}M_{i_1j}=1\), while coordinate \(j\ne i_1\) changes by \(M_{j i_1}\). Thus
\[
t(\rho\pi)+t(\pi)=e_{i_1}+Me_{i_1},
\]
whose quotient class is \(g_{i_1}\). Iteration proves (13). \(\square\)

**Proof of Theorem 4.** The cases \(q=0,1\) are Corollary 3, so suppose \(q=2\). The \(n\) vectors \(g_i\in Q=\mathbb F_2^2\) span \(Q\) and satisfy \(\sum_i g_i=\mathbf1+\operatorname{im}M=0\).

First suppose some nonzero class \(u\in Q\) occurs as \(g_i=g_{i'}=u\) at two distinct coordinates, and some other coordinate has class \(v\notin\{0,u\}\). Take a permutation beginning with \(i,j,i'\), where \(g_j=v\). By (13), four successive cyclic rotations have syndrome classes
\[
z,\quad z+u,\quad z+u+v,\quad z+v.
\]
They are the four elements of \(Q\). Therefore \(\Phi(S_n)=Q\).

Otherwise, because the \(g_i\) span \(Q\) and sum to zero, the only nonzero \(g_i\)'s consist of **three distinct nonzero classes appearing once each**. Denote the corresponding coordinates by \(a,b,c\), and let \(S=\{a,b,c\}\). Every \(e_u\) with \(u\notin S\) lies in \(R=\operatorname{im}M\), and \(e_a+e_b+e_c\in R\). These \(n-2\) vectors are independent, so
\[
R=\operatorname{span}\{e_u:u\notin S\}
+\operatorname{span}\{e_a+e_b+e_c\}.
\tag{14}
\]
Every column \(Me_j\) lies in \(R\); restriction of such a column to the coordinates \(a,b,c\) therefore has either \(000\) or \(111\). Consequently rows \(a,b,c\) of \(M\) are identical; denote their common row by \(w\). The zero diagonal gives \(w_a=w_b=w_c=0\). Since the row sum is odd, some \(u\notin S\) satisfies \(w_u=1\).

Choose permutations beginning with the four-letter blocks
\[
(a,b,c,u),\qquad (a,u,b,c),\qquad
(b,u,a,c),\qquad (c,u,a,b),
\]
and place all other coordinates afterward, in any common order. For their syndrome vectors \(t(\pi)\), the entries at \(a,b,c\) are respectively
\[
000,\qquad 011,\qquad 101,\qquad 110.
\]
Indeed, within \(S\) the common row \(w\) vanishes, all other outside coordinates come after the block, and the sole preceding \(w\)-active coordinate inside the block is \(u\). By (14), the four triples represent the four quotient classes. Hence \(\Phi(S_n)=Q\) also in this case.

For any \(a+R\), therefore, a qualifying permutation exists. Reversing a qualifying permutation gives another: because \(M\mathbf1=\mathbf1\), formula (2) gives \(t(\operatorname{rev}\pi)=t(\pi)+\mathbf1\), and \(\mathbf1\in R\). The two permutations are distinct for \(n\ge3\). Each supplies \(2^{q+1}=8\) directed full monochromatic geodesics by Theorem 1, giving the lower bound \(16\). \(\square\)

**Scope.** This handles affine antipodally odd cube-edge colorings whenever the binary interaction matrix has corank at most two. It strengthens the corank-one case without assuming symmetry or a sparse interaction graph. The first unresolved affine quotient dimension is \(q=3\).

#### Theorem 5 (fixed-support rank-defect control)

The following holds even for a zero-diagonal affine matrix \(M\) without the row-oddness condition. Write \(q=n-\operatorname{rk}M\). There is a set \(I\subseteq[n]\) of cardinality \(q\), depending only on \(M\), with this property: **for every prescribed permutation \(\pi\)** there is a root \(x\) for which all edges of its full geodesic in directions outside \(I\) have color zero. Its color-one counterpart on those directions exists whenever \(M\mathbf1=\mathbf1\). In particular, some full antipodal geodesic has at most \(q\) color changes:
\[
\boxed{\mu(c)\le n-\operatorname{rk}M.}
\tag{15}
\]

**Proof.** Choose \(I\) such that the coordinate cosets \(\{e_i+R:i\in I\}\) form a basis of \(\mathbb F_2^n/R\), with \(R=\operatorname{im}M\). Then every coset has one representative supported on \(I\). For any \(\pi\), choose that representative \(w\) for the coset \(a+t(\pi)+R\). Solve \(Mx=a+t(\pi)+w\). Formula (4) of Theorem 1 says the associated edge-color vector is \(w\), vanishing outside \(I\). If \(M\mathbf1=\mathbf1\), replace \(x\) by \(x+\mathbf1\) to complement the colors. Finally choose \(\pi\) to traverse every direction outside \(I\) first and the \(q\) directions in \(I\) last. Its word is \(0^{n-q}w_I\), which changes color at most \(q\) times. \(\square\)

For \(q=1\) and antipodal oddness, the ordinary odd-change rotation of the full path converts the resulting at-most-one-switch path into a monochromatic full path. Theorem 4 strengthens this conclusion to the larger class \(q=2\).

#### Theorem 6 (binary cut transport and a Gray-code saturation criterion)

For any subset \(S\subseteq[n]\), let \(\mathbf1_S\) be its indicator vector. Moving a consecutive initial block whose coordinate set is \(S\) to the end of the permutation, preserving the internal order of both blocks, changes its syndrome by
\[
\boxed{\Phi(\text{block rotated }\pi)-\Phi(\pi)=\mathbf1_S+R.}
\tag{16}
\]
Indeed the cross-block swaps contribute
\[
\sum_{i\in S,j\notin S}\Delta_{ij}
=\mathbf1_S+M\mathbf1_S
\]
because each full transposition star obeys
\(\sum_{j\ne i}\Delta_{ij}=e_i+Me_i\) and the internal pairs cancel twice. Reduction modulo \(R\) proves (16).

More generally, suppose the projected coordinate vectors \(g_i=e_i+R\) contain a quotient basis \(h_1,\ldots,h_q\) with at least \(2^{q-j}\) distinct coordinate representatives of \(h_j\) for every \(j=1,\ldots,q\). Then \(\Phi:S_n\to\mathbb F_2^n/R\) is surjective, and every affine antipodally odd coloring with this matrix \(M\) has a monochromatic full geodesic.

**Proof.** The standard reflected binary Gray sequence on \(\mathbb F_2^q\) visits all \(2^q\) vectors, starting at zero, using \(2^{q-j}\) steps in basis direction \(h_j\). Choose distinct coordinates representing those steps and place them first in a coordinate permutation, ordered as in this Gray sequence; place the remaining coordinates afterward. By Lemma 4.1, consecutive cyclic rotations traverse its successive quotient prefix sums. They visit all \(2^q\) quotient syndromes, proving surjectivity and then the existence assertion by Theorem 1. \(\square\)

The cut identity (16) is the affine root-transport analogue of the cycle–cocycle relation: the sum of local pair exchanges across a coordinate cut equals its indicator modulo the root-change image. The Gray-code condition is a sufficient structural criterion, while Theorem 4 proves the entire corank-two family without a repetition hypothesis.

#### Theorem 7 (all rank-two antipodally odd affine interactions admit monochromatic full paths)

Suppose \(M_{ii}=0\), \(M\mathbf1=\mathbf1\), and
\[
\boxed{\operatorname{rk}_{\mathbb F_2}M=2.}
\tag{17}
\]
Then for every constant vector \(a\), the affine coloring \(c_i(x)=a_i+(Mx)_i\) admits a monochromatic antipodal geodesic. Moreover, there exist two fixed coordinate directions \(u,t\), depending only on \(M\), such that for every \(a\) a monochromatic full geodesic begins at one of the four roots \(0,e_u,e_t,e_u+e_t\).

**Proof.** Because all rows of \(M\) have odd parity, and the two-dimensional row space contains only two odd-parity vectors, there are precisely two distinct row types \(v,w\). Let \(A\) be the nonempty set of row indices of type \(v\) and \(B\) those of type \(w\), partitioning \([n]\). The zero diagonal forces \(v_i=0\) for \(i\in A\) and \(w_j=0\) for \(j\in B\). Therefore
\[
U=\operatorname{supp}v\subseteq B,\qquad
T=\operatorname{supp}w\subseteq A,
\]
and both \(|U|\) and \(|T|\) are odd. For any \(u\in U\) and \(t\in T\), the columns of \(M\) satisfy
\[
Me_u=\mathbf1_A,\qquad Me_t=\mathbf1_B.
\tag{18}
\]
Hence the root-change image is \(R=\operatorname{span}\{\mathbf1_A,\mathbf1_B\}\).

Choose bits \(\alpha,\beta\), and define target labels \(h_i=a_i+\alpha\) on \(A\) and \(h_j=a_j+\beta\) on \(B\). Because \(|T|\) is odd, one can choose \(\alpha\) so that
\[
|T_0|:=|\{i\in T:h_i=0\}|\quad\text{is even};
\]
because \(|U|\) is odd, choose \(\beta\) so that
\[
|U_0|:=|\{j\in U:h_j=0\}|\quad\text{is odd}.
\]
Write \(T_1=T\setminus T_0\), \(U_1=U\setminus U_0\). Construct a coordinate permutation whose active-coordinate blocks occur in the order
\[
\boxed{T_0,\quad U_0,\quad T_1,\quad U_1.}
\tag{19}
\]
Every \(i\in T_0\) encounters zero earlier members of \(U\), so \(t_i(\pi)=0=h_i\). Every \(j\in U_0\) encounters \(|T_0|\) earlier members of \(T\), an even number, so \(t_j(\pi)=0=h_j\). Every \(i\in T_1\) encounters \(|U_0|\) earlier members of \(U\), an odd number, so \(t_i(\pi)=1=h_i\). Every \(j\in U_1\) encounters all \(|T|\) earlier members of \(T\), also odd, so \(t_j(\pi)=1=h_j\).

For \(i\in A\setminus T\), the same formula \(t_i(\pi)=|\{u\in U:u\text{ precedes }i\}|\pmod2\) applies. Insert such an inactive coordinate at the very beginning if \(h_i=0\), and at the very end if \(h_i=1\). For \(j\in B\setminus U\), insert it at the beginning if \(h_j=0\) and at the end if \(h_j=1\). Their insertion does not change any active parity, since inactive \(A\)-vertices are absent from \(T\) and inactive \(B\)-vertices are absent from \(U\). All target equalities \(t_i(\pi)=h_i\) are therefore realized.

Thus
\[
a+t(\pi)=\alpha\mathbf1_A+\beta\mathbf1_B
=M(\alpha e_u+\beta e_t).
\]
Choose root \(x=\alpha e_u+\beta e_t\). The edge-color formula (4) yields
\[
a+Mx+t(\pi)=0,
\]
so the full path from \(x\) in direction order \(\pi\) is monochromatic. The possible roots form the stated four-element set. \(\square\)

**Corollary (affine gap reduced to intermediate ranks).** A zero-diagonal row-odd binary matrix has rank at least two: if it had rank one, all nonzero odd rows would coincide, and the zero diagonal would force their common row to vanish. Combining Theorems 4 and 7, every antipodally odd affine cube-edge coloring is solved when
\[
\operatorname{rk}M=2\quad\text{or}\quad \operatorname{rk}M\ge n-2.
\]
The first potentially unresolved interaction ranks are \(3\le\operatorname{rk}M\le n-3\), beginning at dimension \(n=6\). In particular all affine antipodally odd cube-edge colorings in dimensions \(n\le5\) are covered by theorems in this subsection.

**Structural interpretation.** A rank-two odd interaction matrix forces a bipartite two-row-type dependence system. The four-block permutation (19) is an explicit resource-basis gallery that solves the root syndrome. It complements the high-rank quotient approach and applies in arbitrarily large dimensions with corank \(n-2\).

### Triangle–square rigidity of canonical Hamming resource matroids

Let \(G=\square_{i=1}^k K_{E_i}\) be a finite Cartesian product of nontrivial complete graphs, with \(|E_i|=m_i\ge2\). Write \(A_i\subseteq E(G)\) for the graph edges changing coordinate \(i\), and \(d=\sum_i(m_i-1)\). A **Cartesian square** is a four-cycle obtained by changing two different coordinates, and a **fiber triangle** is a three-cycle obtained by changing one coordinate. A matroid \(N\) on the graph-edge ground set \(E(G)\) is said to have **local resource compatibility** if:

(S) every graph vertex star \(\delta_G(x)\) is independent in \(N\);

(T) every fiber triangle is dependent in \(N\);

(P) the two opposite graph edges of each Cartesian square are parallel elements of \(N\).

These axioms refer only to the graph's intrinsic local geometry and the circuit/independence structure of \(N\). No representation, spectral projection, orientation, or edge coloring is assumed.

For the product \(G\), define \(R(G)\) to be the matroid on \(E(G)\) obtained by giving each edge \(e\in A_i\), joining symbols \(a,b\in E_i\), the graphic resource label \((i,\{a,b\})\). On the set of distinct labels the matroid is
\[
R_0(G)=\bigoplus_{i=1}^k M(K_{E_i});
\tag{1}
\]
the matroid \(R(G)\) is its parallel extension in which different graph edges with a common label are parallel.

**Theorem 1 (local resource rigidity).** A matroid \(N\) on \(E(G)\) satisfies (S), (T), and (P) if and only if
\[
\boxed{N=R(G).}
\tag{2}
\]
In particular, the three local matroid axioms determine the complete independence system, and
\[
\boxed{\operatorname{rk}N=\sum_{i=1}^k(m_i-1)=\deg G.}
\tag{3}
\]
Every graph cycle is then \(N\)-dependent, and every resource-independent graph walk has distinct vertices.

*Proof.* Fix a vertex \(o=(o_1,\ldots,o_k)\) of \(G\). For each factor \(i\), let \(B_i\) be the \(m_i-1\) edges incident with \(o\) that change coordinate \(i\), and put \(B=\bigcup_i B_i=\delta_G(o)\). By (S), \(B\) is independent.

First consider an arbitrary edge of type \(i\), changing the two symbols \(a,b\in E_i\), in a fiber whose other coordinates need not agree with those of \(o\). Change those other coordinates one at a time until the fiber coincides with the fiber of \(o\). At every change the edge is opposite a corresponding edge in a Cartesian square. By (P), its resource element is parallel to the corresponding element in the next fiber. Hence it is parallel to the edge \(e^i_{ab}\) of type \(i\) in the reference fiber through \(o\).

If \(a=o_i\) or \(b=o_i\), the element \(e^i_{ab}\) belongs to \(B_i\). Otherwise the edges \(e^i_{o_i a}, e^i_{o_i b},e^i_{ab}\) form a fiber triangle. By (T) its three elements are dependent, and by (S) each pair is independent since any pair shares a graph vertex. Thus the triangle is a three-element circuit, giving
\[
e^i_{ab}\in\operatorname{cl}_N
\{e^i_{o_i a},e^i_{o_i b}\}
\subseteq\operatorname{cl}_N(B_i).
\tag{4}
\]
Together with opposite-edge parallel transport this proves
\[
A_i\subseteq\operatorname{cl}_N(B_i)
\qquad\text{for every }i.
\tag{5}
\]
The \(B_i\)'s are disjoint subsets of the independent set \(B\), so \(r_N(A_i)=|B_i|=m_i-1\), while \(B\) spans all of \(E(G)\). Therefore
\[
r_N(E(G))=|B|=\sum_i r_N(A_i).
\tag{6}
\]
Rank additivity across the partition \(E(G)=\bigsqcup_i A_i\) implies
\[
N=\bigoplus_i N|A_i.
\tag{7}
\]

It remains to determine the single-factor restriction. By (P), all copies of a given edge \(\{a,b\}\) in distinct fibers are parallel, and every such parallel class contains the reference-fiber edge \(e^i_{ab}\). Consider the induced restriction \(N_i\) to the reference-fiber edges of \(K_{E_i}\). Every vertex star in \(K_{E_i}\) is independent by (S), and every triangle is a three-element circuit by (S) and (T).

We claim that \(N_i=M(K_{E_i})\). Every graph spanning tree \(T\) of \(K_{E_i}\) can be turned into the star at \(o_i\) through successive **triangle pivots** that preserve matroid span. Root \(T\) at \(o_i\). Whenever a vertex \(v\) has depth at least two, let \(u\) be its parent and \(p\) the parent of \(u\). Replace the tree edge \(uv\) by the complete-graph edge \(pv\). The result is another spanning tree with smaller total depth, and the triangle \(pu,uv,pv\) is a three-element circuit. Because \(pu\) remains in the tree, the outgoing and incoming edges lie in each other's closure together with \(pu\), so the two spanning-tree edge sets have the same closure and rank. Repeating the operation eventually yields the star at \(o_i\), which is independent of rank \(m_i-1\). Thus **every spanning tree has rank \(m_i-1\) and is independent**, and every graph forest, being extendible to a spanning tree, is independent in \(N_i\).

Conversely, take any graph cycle \(C\) of \(K_{E_i}\), with vertex set \(S\), and choose \(z\in S\). Its star edges \(\{zv:v\in S\setminus\{z\}\}\) form an independent family of \(|S|-1\) elements. Every edge \(uv\) of the cycle not incident with \(z\) belongs to the closure of \(zu,zv\) by the triangular circuit; edges incident with \(z\) already belong to the star. Hence the \(|S|\) edges of \(C\) have rank at most \(|S|-1\), so \(C\) is dependent. Consequently the independent sets of \(N_i\) are precisely the graph forests, proving \(N_i=M(K_{E_i})\).

Equations (7) and the parallel-class description now give \(N=R(G)\). Conversely, in \(R(G)\) every graph vertex star uses distinct edges of the factor-graphic root stars, and their union is independent in the direct sum; any triangle in a factor is a graphic cycle; and opposite Cartesian-square edges share the same factor and unordered pair of symbols, hence are parallel. Thus \(R(G)\) satisfies (S), (T), and (P), proving (2).

Finally every closed graph walk projects in every coordinate to a closed walk of the corresponding complete graph. If the original walk is nonempty, some coordinate projection is nontrivial; its multiset of graphic resource labels contains a repeated edge or a cycle, and so is dependent. The original edge set is dependent in \(R(G)\). In particular a resource-independent walk cannot repeat a vertex. \(\square\)

**Corollary 2 (intrinsic matroidal unification).** For
\[
M_{\rm cub}=\bigoplus_{i=1}^nU_{1,2},
\qquad M_{\rm bd}=U_{2,n},
\tag{8}
\]
the connected-component rank-one reduction \(M^\flat\) and its basis graph \(G=\Gamma(M^\flat)\) recover the two canonical root graphs \(Q_n\) and \(K_n\). Theorem 1 uniquely determines their resource matroids from vertex-star independence, triangle dependence, and Cartesian-square parallelism:
\[
R(Q_n)=\text{coordinate-direction partition matroid on cube edges},
\quad
R(K_n)=M(K_n).
\tag{9}
\]
Thus both resource-independence notions have a common choice-free characterization using ordinary matroid circuits and the local graph structure. The turn bits and global involution are additional data that remain necessary for the colored path assertion.

**Proposition 3 (logical sharpness of the three axioms).** Each hypothesis (S), (T), and (P) is needed for uniqueness.

- Without (S), take \(G=K_3\), and put the rank-one uniform matroid \(U_{1,3}\) on its graph edges. Its triangle is dependent, and (P) is vacuous, while the canonical resource is \(M(K_3)=U_{2,3}\).
- Without (T), take \(G=K_3\) and the free rank-three matroid on its graph edges. Every star is independent and (P) is vacuous, but the canonical triangle circuit disappears.
- Without (P), take \(G=Q_2=C_4\) and \(N=U_{2,4}\) on its four graph edges. Every two-edge star is independent, and (T) is vacuous; the four-cycle is dependent, but opposite edges are independent rather than parallel. The canonical resource instead is \(U_{1,2}\oplus U_{1,2}\).

These examples also show that star independence and graph-cycle dependence alone do not determine the cube resource matroid: the commuting-square condition (P) carries essential information.

**Interpretation.** The rank-one reduction of the source matroid supplies the common Hamming root geometry. Theorem 1 recovers the full resource matroid solely from its local triangle/square behavior, with no spectral or vector choice. Independent-star terminal arguments therefore have a canonical combinatorial foundation in both source models. The missing step toward the full NORI1 statement is a global antipodal rank-saturation argument for arbitrary edge colorings; Theorem 1 isolates its resource geometry from the unconstrained coloring problem.

### Commuting-turn cohomology and intrinsic antipodal holonomy

Let \(G=\square_{i=1}^k K_{E_i}\), where \(k\ge2\) and \(|E_i|\ge2\). The **commuting-turn graph** \(T(G)\) is the following ordinary undirected graph:
- its vertices are the graph edges \(e\in E(G)\);
- \(e,f\) are adjacent in \(T(G)\) if they are distinct incident edges of \(G\) which change *different* Cartesian coordinates.

Equivalently, their ordered two-edge turn \((u,v,w)\) has nonadjacent outside endpoints \(u,w\). A binary value on each edge of \(T(G)\) is thus an assignment to the underlying *unoriented* commuting turns of \(G\).

**Lemma 1 (connectivity).** If \(k\ge2\), the graph \(T(G)\) is connected.

*Proof.* The line graph \(L(G)\) is connected since \(G\) is connected. Every adjacency \(ef\) in \(L(G)\) between edges of different Cartesian factors is also an edge of \(T(G)\). If \(e,f\) are incident at \(v\) and change the same factor \(i\), choose any edge \(g\) incident at \(v\) changing a different factor \(j\ne i\). Then \(e,g,f\) is a two-edge walk in \(T(G)\). Thus every line-graph adjacency can be replaced by a \(T(G)\)-walk of length at most two, proving connectivity. \(\square\)

**Theorem 2 (choice-free reconstruction of edge colors from commuting turns).** Let \(B:E(T(G))\to\mathbb F_2\). The following are equivalent:

(i) for every cycle \(C\) of \(T(G)\), \(\sum_{t\in C}B(t)=0\);

(ii) there exists \(c:E(G)\to\mathbb F_2\) such that
\[
B(\{e,f\})=c(e)+c(f)
\quad\text{for every }\{e,f\}\in E(T(G)).
\tag{1}
\]

When these conditions hold, \(c\) is unique up to simultaneous complementation on all edges of \(G\). In particular, for any graph edges \(e,f\), the quantity
\[
\delta_B(e,f)=\sum_{t\in P}B(t)
\tag{2}
\]
is independent of the choice of \(T(G)\)-path \(P:e\leadsto f\), and satisfies \(\delta_B(e,f)=c(e)+c(f)\).

*Proof.* Under (ii), the sum around every cycle telescopes to zero. Conversely, fix \(e_0\in E(G)=V(T(G))\), set \(c(e_0)=0\), and for any \(e\) define \(c(e)\) to be the sum of \(B\) along a \(T(G)\)-path from \(e_0\) to \(e\). Condition (i) makes this path independent, and adding the values at adjacent vertices gives (1). If \(c'\) also satisfies (1), then \(c+c'\) is constant along every edge of the connected graph \(T(G)\), so it is globally constant. Equation (2) follows from the same telescoping argument. \(\square\)

Let \(\tau\) be any involutive automorphism of \(G\) preserving the Cartesian factor directions, such as the canonical central polarity determined by the two-element components of a partition matroid. It acts on \(T(G)\). Say \(B\) is \(\tau\)-invariant if \(B(\tau t)=B(t)\).

**Theorem 3 (intrinsic oddness as a path integral).** Suppose \(B\) satisfies Theorem 2 and is \(\tau\)-invariant. Then there exists one bit \(\omega_\tau(B)\in\mathbb F_2\), independent of the graph edge \(e\), such that
\[
\boxed{\omega_\tau(B)=\delta_B(e,\tau e)
=c(e)+c(\tau e).}
\tag{3}
\]
It is independent of the choice of the reconstructed edge coloring \(c\). In particular,
\[
\boxed{\omega_\tau(B)=1
\quad\Longleftrightarrow\quad
c(\tau e)=1-c(e)\ \text{for all }e\in E(G).}
\tag{4}
\]

*Proof.* Let \(h(e)=c(e)+c(\tau e)\). For adjacent \(e,f\) in \(T(G)\),
\[
h(e)+h(f)
=B(\{e,f\})+B(\{\tau e,\tau f\})=0
\]
by invariance. Connectivity of \(T(G)\) makes \(h\) constant. By Theorem 2 this constant equals the path integral \(\delta_B(e,\tau e)\). Replacing \(c\) by \(c+1\) leaves \(h\) unchanged. The equivalence (4) follows. \(\square\)

For a nontrivial canonical polarity \(\eta\) involving at least two two-element factors, \(\eta\) acts freely on \(E(G)\). The class \(\omega_\eta(B)=1\) is therefore possible: assign arbitrary complementary colors on the two-member orbits of \(\eta\), and construct \(B\) using (1). Formula (3) recovers the familiar nontrivial deck parity entirely from commuting-turn data, without introducing a separate chosen edge coloring.

#### A graph-and-matroid intrinsic turn system

For \(k\ge2\), equip every ordered nonbacktracking turn \((u,v,w)\) with a bit \(b(u,v,w)\) subject to:

(C1) if \(u,w\) are nonadjacent, then \(b(u,v,w)=b(w,v,u)\); these common values form \(B:E(T(G))\to\mathbb F_2\) satisfying the cycle condition of Theorem 2;

(C2) if \(u,w\) are adjacent, then \(b(u,v,w)+b(w,v,u)=1\), with no other restrictions on these triangular comparisons;

(C3) when the canonical polarity \(\eta\) is nontrivial, \(B\) is \(\eta\)-invariant and \(\omega_\eta(B)=1\).

Define an **accepted resource gallery** to be a path \(P=(v_0,\ldots,v_\ell)\) whose graph edges are independent in the uniquely determined triangle–square resource matroid \(R(G)\) of the preceding Article XI Subsection and for which, at every internal vertex, both
\[
b(v_{j-1},v_j,v_{j+1})=0,\qquad
\delta_B(v_{j-1}v_j,v_jv_{j+1})=0.
\tag{5}
\]
The second constraint is intrinsic by Theorem 2. On nontriangular turns, the two constraints coincide.

For the one-factor case \(G=K_m\), the commuting-turn graph has no edges. Use instead the intrinsic triangular rule \(b(a,v,c)+b(c,v,a)=1\) and define an accepted gallery using the first constraint of (5) alone. This is the boundary-tournament specialization and involves no edge-color potential.

**Corollary 4 (faithful decoding of the canonical examples).**

(a) For \(M=\bigoplus_{i=1}^nU_{1,2}\), \(n\ge2\), its rank-one root is \(G=Q_n\) and its canonical polarity is cube complementation. Every nonbacktracking turn is commuting, so the turn bit is \(\delta_B(e,f)\). A turn system satisfying (C1)--(C3) is equivalent, up to simultaneous exchange of the color names, to an arbitrary antipodally odd binary coloring of undirected cube edges. The accepted resource galleries are its monochromatic coordinate-distinct geodesics. In particular, a gallery of length \(n\) is a monochromatic antipodal geodesic.

(b) For \(M=U_{2,n}\), \(n\ge3\), the root is \(G=K_n\), and the canonical polarity is the identity. Every nonbacktracking turn is triangular. The turn rule is precisely an arbitrary reversal-odd boundary 3-tournament on distinct ordered triples, and the accepted resource galleries are its monochromatic vertex-simple tight paths.

*Proof.* Part (a) follows from Theorems 2--3 and the triangle–square rigidity characterization \(R(Q_n)\) as the coordinate-direction partition matroid. Part (b) follows from the absence of commuting turns in a complete graph and \(R(K_n)=M(K_n)\), whose independent paths are precisely the vertex-simple paths in the original complete graph. \(\square\)

**Corollary 5 (a turn-only unified conjecture).** Let \(\mathcal C_{\rm can}\) be the intrinsic partition-matroid class whose number \(s\) of two-element connected components satisfies \(s=0\) or \(s\ge2\). Let \(G=\Gamma(M^\flat)\), \(k\) be its Cartesian-factor count, and \(d=\operatorname{rk}R(G)\). Use the turn-only systems (C1)--(C3) for \(k\ge2\) and the unrestricted triangular turn system for \(k=1\). The single quantitative conjecture
\[
\boxed{
L\ge\max\left\{
\left\lceil\frac{k}{2}\right\rceil,
\left\lceil\frac{\sqrt d}{2}\right\rceil,
s
\right\}
}
\tag{6}
\]
for an accepted resource gallery is equivalent to NORI1.

*Proof.* The factor-count bound \(\lceil k/2\rceil\) is already established for arbitrary edge colors on Hamming products by the monochromatic factorwise transfer theorem in Article XI. The resource-rank bound \(\lceil\sqrt d/2\rceil\) is established by the cycle-dominating resource-matroid terminal theorem. Both apply to the reconstructed \(c\) by Theorem 2, and for \(k=1\) the rank theorem applies directly to the unrestricted local tournament. If \(s\ge2\), the canonical polarity acts by simultaneous complementation of all binary factors and fixes the remaining factors. Under NORI1, restrict the reconstructed odd coloring to a cube obtained by retaining those binary factors and fixing the others. A monochromatic \(s\)-edge antipodal geodesic on that slice is resource-independent and accepted, giving the third bound. Conversely the pure cube case has \(k=s=d=n\), so (6) forces a monochromatic antipodal geodesic and hence NORI1. \(\square\)

The reconstructed color bit is a gauge choice: changing it globally affects none of the turn data, holonomy, or accepted galleries. Thus both the resource matroid and the antipodal color law can be specified using intrinsic circuit geometry and a binary turn cocycle. The nontrivial remaining mathematical task is the full-rank path-existence theorem for such unrestricted polarized turn systems.

#### Dimension of the intrinsic odd-holonomy space

**Theorem 6 (two cosets of invariant commuting-turn cuts).** Let \(\tau\) be a fixed-point-free involution on the vertices of the connected graph \(T(G)\), induced by a factor-preserving graph involution of \(G\). Put \(2m=|V(T(G))|=|E(G)|\), and let \(\mathcal B^\tau\) be the vector space of \(\tau\)-invariant edge functions \(B:E(T(G))\to\mathbb F_2\) whose sum around every graph cycle vanishes. Then
\[
\boxed{\dim_{\mathbb F_2}\mathcal B^\tau=m.}
\tag{7}
\]
The map \(B\mapsto\omega_\tau(B)\) is a surjective linear functional on this space. Its two fibers have
\[
\boxed{|\{B\in\mathcal B^\tau:\omega_\tau(B)=\epsilon\}|
=2^{m-1}\quad(\epsilon\in\mathbb F_2).}
\tag{8}
\]
In particular, antipodally odd edge colorings modulo simultaneous exchange of the two colors correspond bijectively to the nonzero-holonomy fiber.

*Proof.* By Theorem 2, the cycle-zero cochains on \(T(G)\) are precisely the image of the graph coboundary map \(d:C^0(T(G);\mathbb F_2)\to C^1(T(G);\mathbb F_2)\), whose kernel consists of the two constant vertex functions. By Theorem 3, \(dc\) is \(\tau\)-invariant precisely when \(c+\tau c=\alpha\mathbf1\) for some \(\alpha\in\mathbb F_2\), and then \(\omega_\tau(dc)=\alpha\). On each of the \(m\) two-element vertex orbits of \(\tau\), choose the value of \(c\) at one representative freely; the other value is forced to be \(c+\alpha\). Thus all such potentials \(c\), allowing either \(\alpha\), form an \((m+1)\)-dimensional vector space. Quotienting by the one-dimensional constant kernel of \(d\) gives dimension \(m\), proving (7). Both values of \(\alpha\) occur (choose representative values all zero, and then choose either value of \(\alpha\)), so \(\omega_\tau\) is surjective, with kernel of dimension \(m-1\). This proves (8). \(\square\)

For the canonical cube \(Q_n\), \(n\ge2\), the commuting-turn graph has \(|E(Q_n)|=n2^{n-1}\) vertices and its antipodal involution pairs them freely, so \(m=n2^{n-2}\). Thus the entire unrestricted space of antipodally odd edge colorings, modulo exchanging the colors, is a single nonzero-holonomy coset of cardinality \(2^{n2^{n-2}-1}\). No regularity restriction is imposed on the colorings.

### Universal twisted-gallery switch enumeration and degree mixing

Let \(n\ge2\) and let \(c:E(Q_n)\to\mathbb F_2\) be any undirected edge coloring satisfying \(c(\bar e)=1-c(e)\). For the \(T=2^n n!\) rooted directed full geodesics \((x,\pi)\), let \(S_j\) count those with \(j\) changes in their length-\(n\) edge-color word. There is no affine or other regularity assumption.

**Theorem 1 (switch spectrum under rooted rotations).** For \(2r+1\le n\),
\[
\boxed{(2r+1)S_{2r+1}=(n-2r-1)S_{2r}.}\tag{1}
\]
In particular
\[
\boxed{S_1=(n-1)S_0.}\tag{2}
\]
More strongly, there are integers \(A_{2r+1}\ge0\) such that
\[
\boxed{S_{2r}=2(2r+1)A_{2r+1},\quad
S_{2r+1}=2(n-2r-1)A_{2r+1}.}\tag{3}
\]

**Proof.** If a path \(P=(x;i_1,\dots,i_n)\) has color word \(w=(w_1,\dots,w_n)\), its rooted cyclic rotation
\[
R(P)=(x^{i_1};i_2,\dots,i_n,i_1)
\]
has color word
\[
\boxed{w(R(P))=(w_2,\dots,w_n,1-w_1).}\tag{4}
\]
The last new edge is antipodal to the original first edge. The action \(R\) has orbit size \(2n\): before \(n\) steps the coordinate permutation has not returned, and after \(n\) steps the root becomes its antipode. The associated length-\(2n\) circular word is \(w_1,\dots,w_n,1-w_1,\dots,1-w_n\). Define its half-circle change count
\[
k(P)=\sum_{i=1}^{n-1}[w_i\ne w_{i+1}]+[w_n\ne1-w_1].
\]
It is odd, because its transitions change the initial bit to its complement. It is invariant under \(R\). In an orbit with \(k=2r+1\), every rooted linear word omits one of the \(n\) comparisons of a twisted half-circle. If the omitted comparison is a change, the linear word has \(k-1=2r\) changes; otherwise it has \(k=2r+1\). Over all \(2n\) rotations, \(2k\) omit a change and \(2(n-k)\) omit an equality. Thus each orbit contributes \(2(2r+1)\) paths of type \(2r\) and \(2(n-2r-1)\) paths of type \(2r+1\). Summation gives (1)--(3). \(\square\)

**Theorem 2 (local color mixing determines the first cyclic moment).** Put \(a(v)=\deg_{c=0}(v)\), the number of zero-color edges incident with vertex \(v\). For uniformly random rooted full geodesic \(P\),
\[
\boxed{\mathbb E k(P)=\frac{2}{2^n(n-1)}
\sum_{v\in Q_n}a(v)(n-a(v)).}\tag{5}
\]

**Proof.** Each of the \(n-1\) internal transitions of the full geodesic is an ordered pair of distinct directions at a uniformly random cube vertex. The closing comparison is between the final edge and the antipodal image of the initial edge at the terminal vertex; its vertex and ordered direction pair have the same uniform law. At a vertex \(v\), the proportion of mixed-color ordered edge pairs is
\[
\frac{2a(v)(n-a(v))}{n(n-1)}.
\]
Summing the \(n\) cyclic comparisons and averaging proves (5). \(\square\)

**Corollary 3 (quantitative existence criterion).** For every antipodally odd coloring,
\[
\boxed{S_0\ge2^{n-1}(n-1)!\,
\max\left\{0,\ 3-\frac{2}{2^n(n-1)}
\sum_v a(v)(n-a(v))\right\}.}\tag{6}
\]
In particular, if the mean of \(a(v)(n-a(v))\) over cube vertices is less than \(3(n-1)/2\), a monochromatic antipodal geodesic exists.

**Proof.** Let \(p\) be the fraction of rotation orbits with \(k=1\). All other odd switch counts are at least three, hence \(\mathbb E k\ge p+3(1-p)\) and \(p\ge(3-\mathbb E k)/2\). Each orbit has \(2n\) rooted paths; a \(k=1\) orbit has two monochromatic paths, and no other orbit has any. Thus \(S_0=(T/n)p=2^n(n-1)!p\). Substitute (5). \(\square\)

**Corollary 4 (sharp low-dimensional witness multiplicities).** Every antipodally odd coloring has
\[
\boxed{S_0(Q_3)\ge8,\qquad S_0(Q_4)\ge16.}\tag{7}
\]
Both bounds are attained. In \(Q_4\), equality holds if and only if each vertex has two edges of each color.

**Proof.** For \(n=3\), integer \(a\) satisfies \(a(3-a)\le2\), so \(\mathbb E k\le2\); (6) gives \(S_0\ge8\). The coloring
\[
c_1=x_2,\quad c_2=x_1,\quad c_3=1+x_1
\]
is antipodally odd, and both colors occur at every vertex, making \(\mathbb E k=2\). Since the twisted count \(k\in\{1,3\}\), the proof of (6) gives \(S_0=8\).

For \(n=4\), \(a(4-a)\le4\) gives \(\mathbb E k\le8/3\), and (6) yields \(S_0\ge16\). The coloring
\[
c_1=x_2,\quad c_2=x_1,\quad c_3=1+x_2,\quad c_4=1+x_1
\]
is antipodally odd and has two colors of each type in every vertex star. Its cyclic counts likewise belong to \(\{1,3\}\), so it attains \(S_0=16\). Conversely, equality \(S_0=16\) forces the mean in (5) to be \(8/3\); hence every vertex maximizes \(a(4-a)\), meaning \(a(v)=2\) for all \(v\). \(\square\)

**Corollary 5 (rigidity of a putative \(Q_5\) counterexample).** If an antipodally odd coloring of \(Q_5\) had no monochromatic antipodal geodesic, then every vertex would have two or three edges of color zero, and **every** rooted full geodesic would have cyclic switch number \(k=3\). Its ordinary switch word would always have two or three changes, with \(3S_3=2S_2\).

**Proof.** Since \(a(5-a)\le6\), (5) gives \(\mathbb E k\le3\). If \(S_0=0\), Theorem 1 excludes any \(k=1\) rotation orbit, so \(k\ge3\) everywhere. Equality of the upper and lower means forces \(a(v)\in\{2,3\}\) at every vertex and \(k=3\) throughout. Equation (1) for \(r=1\) completes the statement. \(\square\)

**Scope.** These theorems hold for *every* legal antipodally odd cube-edge coloring, unlike affine-subclass results. The odd-switch rotation is established elsewhere in Article XI; Theorem 1 upgrades it to full integer-valued switch-spectrum relations, and Theorem 2 connects those counts to a simple vertex-degree observable. The sharp multiplicity bound settles dimensions 3 and 4 by a new count and yields explicit sufficient conditions in all dimensions. For large \(n\), the first-moment threshold is not sufficient near balanced vertex stars: one would need further moments or square-turn correlations to force \(k=1\). No unrestricted NORI1 proof follows from the displayed bounds alone.

#### Theorem 6 (rank-one antipodal completion and facet enumeration)

Let \(M_{n-1}(c)\) denote the number of **directed** monochromatic geodesics of length \(n-1\) in \(Q_n\), counted with their initial vertices and their ordered sets of \(n-1\) distinct coordinate directions. Then
\[
\boxed{M_{n-1}(c)=2S_0(c),\qquad
S_1(c)=\frac{n-1}{2}M_{n-1}(c).}
\tag{10}
\]
Moreover, writing \(F_{j,0}=\{x\in Q_n:x_j=0\}\), and letting \(B(F_{j,0})\) count all monochromatic directed full geodesics within the \((n-1)\)-dimensional face \(F_{j,0}\) under the inherited coloring, one has
\[
\boxed{S_0(c)=\sum_{j=1}^n B(F_{j,0}).}
\tag{11}
\]

**Proof.** Let \(P\) be a monochromatic geodesic of length \(n-1\), from \(x\) to \(y\), missing direction \(j\). Then \(y=\bar x^{j}\). The \(j\)-edge at the start, \(xx^{j}\), and the \(j\)-edge at the end, \(yy^{j}\), are antipodal images of each other. By the oddness condition, their colors are opposite. Precisely one of them agrees with the common color of \(P\), allowing one and only one monochromatic full-geodesic extension by adding direction \(j\) at the appropriate end. Conversely, deleting the first or the last edge of any monochromatic full geodesic produces two different directed \((n-1)\)-edge monochromatic geodesics, each of which is uniquely extended back to the original full geodesic. This is a two-to-one correspondence, proving the first identity in (10). The second identity follows from (2).

Every \((n-1)\)-edge cube geodesic lies in precisely one coordinate facet, determined by its omitted direction \(j\) and the fixed \(j\)-bit of its vertices. The cube antipode maps the facet \(F_{j,0}\) bijectively to its opposite facet \(F_{j,1}\), reversing all edge colors; hence their monochromatic spanning-geodesic counts coincide. Therefore
\[
M_{n-1}(c)=\sum_{j=1}^n \bigl(B(F_{j,0})+B(F_{j,1})\bigr)
=2\sum_{j=1}^n B(F_{j,0}).
\]
Combine with \(M_{n-1}(c)=2S_0(c)\) to obtain (11). \(\square\)

This count identity makes precise the distinction between **partial witness growth** and **rank saturation**. An \((n-1)\)-resource monochromatic path extends automatically, thanks to the antipodal pair of final resource ports. However, a path of only \(\sqrt n\), \(n/2\), or \(n-2\) independent resources need not have such an antipodal pair at its endpoints. An unrestricted proof via the common matroid terminal theorem must therefore either grow witnesses up to rank \(n-1\) or find an analogue of the complementary-endport completion mechanism at larger resource defect. The reversal-odd boundary tournament does not automatically possess this two-end extension rule, so the possible unification must encode different seam arities without discarding the resource constraints.

#### Theorem 7 (second-moment certificate for arbitrary antipodally odd colorings)

Let \(n\ge3\), let \(K\) be the largest odd integer at most \(n\), and regard \(k(P)\in\{1,3,\ldots,K\}\) as a random variable over uniformly chosen rooted full geodesics. Put \(m_1=\mathbb E k\), \(m_2=\mathbb E k^2\). Then
\[
\boxed{
S_0\ge
2^{n-1}(n-1)!\,
\max\left\{0,\frac{m_2-(K+3)m_1+3K}{K-1}\right\}.}
\tag{12}
\]
This is a second-moment certificate independent of any affine or regularity condition.

**Proof.** The polynomial \(g(k)=(k-3)(K-k)\) vanishes at \(k=3,K\), is nonnegative at every admissible odd \(k\ge3\), and has \(g(1)=-2(K-1)\). If \(p\) is the fraction of rotation orbits with \(k=1\), it follows that
\[
\mathbb E g(k)\ge -2(K-1)p.
\]
But \(-\mathbb E g(k)=m_2-(K+3)m_1+3K\). As proved in Corollary 3, \(S_0=2^n(n-1)!p\). The inequality follows. \(\square\)

**Corollary 8 (a variance characterization of the balanced \(Q_5\) case).** Suppose \(n=5\) and every vertex star has zero-color degree two or three. Then \(m_1=3\), and
\[
\boxed{S_0(c)=96\,\operatorname{Var}(k).}
\tag{13}
\]
Consequently in this balanced-star regime, a monochromatic antipodal geodesic exists if and only if the cyclic switch number is not constant over the rooted full geodesics.

**Proof.** By (5), balanced stars give \(m_1=3\). The cyclic switch count can be \(1,3,5\). Its probabilities at 1 and 5 are equal because their contributions to \(m_1-3\) are opposite. If that common probability is \(p\), then \(\operatorname{Var}(k)=4p+4p=8p\), while \(S_0=2^5\cdot4!p=768p\). Therefore \(S_0=96\operatorname{Var}(k)\). \(\square\)

This suggests a possible unrestricted strategy beyond average-degree bounds: estimate cyclic-switch variance (or suitable higher positive polynomial moments) from square-turn correlations and rooted gallery exchanges. The first moment depends only on the vertex color degrees; the second moment detects correlations across turns and may remain informative when all vertex stars are perfectly balanced. Formula (13) is a sharp manifestation in dimension five. It is not, by itself, a proof that such variance must be positive in every balanced coloring.

### Cyclic switch calculus for cube galleries and arbitrary boundary tournaments

#### A binary local system and its cut identity

Let \(m\ge3\), \(h\in\{1,\ldots,m\}\), and \(w_i\in\mathbb F_2\), indexed by integers, satisfy
\[
w_{i+m}=w_i+\eta,\qquad\eta\in\mathbb F_2.
\]
Put \(d_i=w_i+w_{i+1}\pmod2\), and let \(D=\sum_{i=0}^{m-1}d_i\) be an integer sum. Then \(d\) is \(m\)-periodic and
\[
D\equiv\eta\pmod2.
\]
A retained switch-window with seam width \(h\) has cost
\[
J_s=D-\sum_{j=s}^{s+h-1}d_j.
\]
**Lemma 1 (cyclic cut transfer).** The cut costs obey
\[
\boxed{\sum_{s=0}^{m-1}J_s=(m-h)D,\qquad
\sum_{s=0}^{m-1}z^{J_s}
=\sum_{s=0}^{m-1}z^{D-\sum_{j=s}^{s+h-1}d_j}.}
\]
In particular, a cut with cost at most one exists if and only if one block of \(h\) consecutive comparisons contains at least \(D-1\) changes.

*Proof.* The switch sequence is periodic because the twist cancels when taking adjacent differences. Its cyclic XOR telescopes to \(\eta\), proving parity. Each comparison belongs to \(h\) deleted blocks and \(m-h\) retained blocks, proving the sum formula. The generating-function identity is termwise. \(\square\)

#### Cubical odd-monodromy specialization

Let \(c:E(Q_n)\to\mathbb F_2\) be arbitrary except for \(c(\bar e)=1-c(e)\). Moving the first step of a rooted full geodesic to its end, while shifting the root over that edge, transforms its color word by
\[
(w_0,\ldots,w_{n-1})\mapsto(w_1,\ldots,w_{n-1},1-w_0).
\]
Therefore \(m=n,\eta=1,h=1\). A rooted rotation orbit has \(2n\) members and contains two lifts of each cyclic cut. If its odd cyclic switch count is \(D\), the orbit has \(2D\) paths with \(D-1\) ordinary switches and \(2(n-D)\) paths with \(D\) switches. The universal switch-spectrum identity from the preceding subsection follows. The presence of a monochromatic full geodesic is equivalent to existence of a rooted cyclic gallery with \(D=1\).

#### Boundary even-monodromy specialization

Let \(V\) be an \(n\)-vertex set, \(n\ge4\), and let \(b(a,v,c)\) be an arbitrary reversal-odd boundary coloring:
\[
b(c,v,a)=1-b(a,v,c).
\]
Take any oriented Hamiltonian cycle \(C=(v_0,\ldots,v_{n-1})\), modulo rotations but not reversal, and define, with subscripts modulo \(n\),
\[
t_i=b(v_{i-1},v_i,v_{i+1}),\qquad
d_i=t_i+t_{i+1}\pmod2,\qquad D(C)=\sum_i d_i.
\]
The word \(t\) is \(n\)-periodic, so \(D(C)\) is even. Open the cycle into the Hamiltonian path
\(P_s=(v_s,v_{s+1},\ldots,v_{s+n-1})\).
The path's turn colors are \(t_{s+1},\ldots,t_{s+n-2}\); their switch count is
\[
\boxed{\sigma(P_s)=D(C)-(d_{s-2}+d_{s-1}+d_s).}
\tag{1}
\]
Thus the seam width is \(h=3\), rather than the cubical \(h=1\).

**Theorem 2 (boundary Hamiltonian cycle-window theorem).** Each oriented Hamiltonian cycle supplies \(n\) distinct Hamiltonian paths, and
\[
\boxed{\sum_{s=0}^{n-1}\sigma(P_s)=(n-3)D(C).}
\tag{2}
\]
The number of cyclic cuts with at most one switch equals the number of cyclic length-three blocks of \(d(C)\) containing at least \(D(C)-1\) ones. Hence:

- For \(D(C)=0\), all \(n\) cuts give monochromatic Hamiltonian paths.
- For \(D(C)=2\), at least four cuts give Hamiltonian paths with at most one switch.
- For \(D(C)=4\), some cut works if and only if three consecutive entries of \(d(C)\) are one.
- For \(D(C)\ge6\), no cyclic cut works.

The spanning one-switch Hamiltonian boundary conjecture is consequently equivalent to the existence of a Hamiltonian cycle with \(D(C)\le2\), or one with \(D(C)=4\) and three consecutive changes.

*Proof.* Each permutation of the \(n\) original vertices opens a unique oriented Hamiltonian cycle, obtained by appending its closing edge. Formula (1) omits three consecutive circular comparisons and retains the \(n-3\) internal comparisons. Apply Lemma 1 to obtain (2) and the cut condition. Since \(D\) is even, the four listed cases exhaust the possibilities. For \(D=2\), each of the two changed comparisons belongs to three deleted three-blocks; their combined set contains at least four different blocks. At \(D=4\), deleting at least three changed comparisons requires an all-one three-block; at \(D\ge6\), three deletions cannot leave fewer than three changes. \(\square\)

**Corollary 3 (unconditional spanning one-switch path on five vertices).** Every binary coloring of ordered triples on \(n\le5\) distinct vertices, even without reversal oddness, has a Hamiltonian vertex ordering whose consecutive triple-color word has at most one switch.

*Proof.* For \(n\le4\) there are at most two successive triple colors. At \(n=5\), any cyclic binary five-term turn word has \(D\in\{0,2,4\}\). The first two cases are covered by Theorem 2. In the last case, the cyclic comparison word has four ones and one zero, and therefore three consecutive ones. Theorem 2 applies. \(\square\)

**Theorem 4 (boundary quartet-discrepancy moment).** Let
\[
\beta(b)=\frac1{n(n-1)(n-2)(n-3)}
\sum_{\substack{a,u,v,d\in V\\\mathrm{distinct}}}
\mathbf1_{\{b(a,u,v)\ne b(u,v,d)\}}.
\]
For uniform oriented Hamiltonian cycle \(C\) and uniform Hamiltonian path \(P\),
\[
\boxed{\mathbb E D(C)=n\beta(b),\qquad
\mathbb E\sigma(P)=(n-3)\beta(b).}
\tag{3}
\]
In particular, if \(\beta(b)<4/n\), there is a Hamiltonian path with at most one switch.

*Proof.* Four consecutive vertices in a uniformly random oriented Hamiltonian cycle form a uniformly random ordered quadruple of distinct vertices. Thus each cyclic turn comparison changes color with probability \(\beta(b)\), giving the first equality. Averaging (2) over cycles, whose cuts partition the permutations, gives the second. If the mean cyclic count is below four, some cycle has even count zero or two; apply Theorem 2. \(\square\)

#### Mathematical distinction

Both models encode the turn defects of full-resource galleries as cyclic \(\mathbb F_2\)-differences. An existence witness is a cut whose deleted seam contains nearly all defects. This is a shared statement valid for all legal colorings; no affinity, local transitivity, or special edge order is involved.

The cube has odd monodromy and a one-comparison seam; the boundary has even monodromy and a three-comparison seam. For the former, existence is governed solely by the smallest cyclic change count \(D=1\). For the latter, the relative positions of up to four cyclic changes also matter. Consequently a proof of the boundary conjecture must control clustering or reductions of cyclic turn defects, not just their total. The results give a common analytic mechanism but do not assert that a general unifying existence theorem has been proved.

#### 5. Quantized local exchange curvature

**Lemma 5 (adjacent-exchange Lipschitz bounds).** On the graph of full-resource galleries related by transposing adjacent steps, the cyclic switch count \(D\) changes as follows:

(a) For arbitrary antipodally odd cubical edge colors, transposing two consecutive directions changes \(D\) by an even integer of absolute value at most two.

(b) For arbitrary boundary triple colors, transposing two consecutive vertices in a cyclic Hamiltonian ordering changes \(D\) by an even integer of absolute value at most four.

Both statements hold without assuming the target conjectures.

**Proof.** The cyclic switch count of a binary color word is the number of unequal adjacent colors, including the twisted closing comparison in (a) and the periodic closing comparison in (b). In both cases its parity is preserved under gallery transpositions: odd in (a), even in (b).

In (a), exchanging two consecutive coordinate steps replaces two edges of a single coordinate square; all the other path edges stay unchanged. Thus only two neighboring entries of the length-\(n\) edge-color word can change, affecting at most three consecutive cyclic comparisons. The integer difference of switch counts is even, so its magnitude is at most two.

In (b), swapping two consecutive vertices in the Hamiltonian cycle changes only the four consecutive triple colors whose centers are the swapped vertices or their two immediate neighbors. All other turn colors are unchanged. Therefore at most five cyclic comparisons are affected. The integer difference is even, hence of magnitude at most four. \(\square\)

**Variational consequence.** A gallery minimizing the cyclic switch count is automatically stable under every adjacent exchange. In the cube its local energy increments belong to \(\{0,2\}\), and for boundary Hamiltonian cycles they belong to \(\{0,2,4\}\). To prove the target from such a minimum, one must show that an odd local minimum with \(D\ge3\) (cube), respectively a boundary local minimum outside the \(D\le2\)/clustered-\(D=4\) extraction classes, is impossible or can be escaped by a coordinated sequence of zero-cost exchanges. The support bounds make this a finite-neighborhood curvature problem, not a solution in themselves.


#### Switch signatures as the prescribed covering class

**Theorem 6 (odd vertex labels versus switch cohomology).** Let \(H\) be a finite graph with a fixed-point-free involution \(R\) on vertices and edges, let \(G=H/R\), and let \(\alpha=w_1(H\to G)\in H^1(G;\mathbb F_2)\). An edge signature \(s:E(G)\to\mathbb F_2\) arises from an odd vertex coloring \(c(Rv)=1+c(v)\) by
\[
s([uv])=c(u)+c(v)
\]
if and only if
\[
\boxed{[s]=\alpha.}\tag{6}
\]
For connected \(G\), the coloring is unique up to simultaneous complementation; in general it has one binary choice on each quotient component.

*Proof.* Select one lift \(\widetilde v\) of each quotient vertex. Put \(\eta(vw)=0\) if the lift of \(vw\) from \(\widetilde v\) reaches \(\widetilde w\), and \(\eta(vw)=1\) if it reaches \(R\widetilde w\). This cochain represents \(\alpha\). Writing \(b(v)=c(\widetilde v)\), oddness gives \(s(vw)=\eta(vw)+b(v)+b(w)\), so \([s]=\alpha\). Conversely, if \(s+\eta=\delta b\), assign \(c(\widetilde v)=b(v)\) and \(c(R\widetilde v)=1+b(v)\). These assignments induce \(s\) on every edge orbit. Any two potential choices differ by a locally constant function on \(G\). \(\square\)

**Corollary 7 (legal perturbations are graph cuts).** Two legal signatures on \(G\) differ by a coboundary \(\delta f\), i.e. by toggling all signature edges crossing a vertex cut. Changing just one switch while leaving all others unchanged is legal precisely when the selected edge of \(G\) is a bridge.

*Proof.* Theorem 6 says both signatures lie in the same affine coset \(\alpha+B^1(G;\mathbb F_2)\). A one-edge indicator is a graph coboundary if and only if that edge lies on no graph cycle. \(\square\)

**Theorem 8 (common switch-only encoding for both unrestricted gallery problems).** There are native graphs \(H_\square,H_\partial\) on which the two original reversal-odd bit colorings become odd vertex colorings, and the switches become representatives of the corresponding covering class.

For NORI1, take \(H_\square=L(Q_n)\), whose vertices are cube edges and whose adjacencies are incident pairs of distinct cube edges. Antipodal inversion acts freely. The quotient \(G_\square=L(Q_n)/A\cong L(Q_n/A)\) has vertices representing antipodal pairs of cube edges and edges representing projective turns. The NORI1 conclusion is equivalent to: every edge signature on \(G_\square\) in the class \(\alpha_\square\) admits a dimension-simple projective Petrie loop with precisely **one** active turn.

For ordinary reversal-odd boundary 3-tournaments, take \(H_\partial\) whose vertices are ordered triples \((a,b,c)\) of distinct symbols, with an undirected edge joining \((a,b,c)\) to \((b,c,d)\) for every ordered quadruple of distinct symbols. The involution \(R(a,b,c)=(c,b,a)\) preserves adjacency and reverses transition orientations. The quotient \(G_\partial=H_\partial/R\) has one edge for each reversal-orbit of four-symbol transitions. Every unrestricted odd triple coloring becomes an odd vertex coloring of \(H_\partial\). The boundary conclusion is equivalent to: every signature representing \(\alpha_\partial\) admits a vertex-simple Hamilton triple-overlap path with **at most one** active transition.

Neither \(G_\square\) nor \(G_\partial\) has bridges. In \(G_\square\), each turn belongs to a triangle formed by three edges incident at one projective cube vertex, since \(n\ge3\). In \(G_\partial\), every transition belongs to the four-cycle obtained by rotating its four distinct symbols:
\[
(a,b,c)\to(b,c,d)\to(c,d,a)\to(d,a,b)\to(a,b,c).
\]
Its quotient remains a cycle. Thus no single-switch deletion is legal in either unrestricted class.

*Proof.* Apply Theorem 6 to the graphs and involutions defined above. Cube edge bits become vertex bits of the line graph and their changes occur on turn edges. The closed projective Petrie path represents a nontrivial lift and has an odd number of changes; one change is equivalent, by cyclic root sliding, to a monochromatic antipodal half-geodesic. Consecutive ordered triples of a Hamilton vertex order trace a path in \(H_\partial\), and its changes are the transition signature. The graph-cycle assertions prove the bridge claim. \(\square\)

**Research consequence.** This is one common structural encoding of the two full unrestricted coloring classes; it does **not** yet prove one substantive shared path-existence theorem. Their distinguished complete path families differ. It does correct the natural switch-criticality induction: legal perturbations are whole graph cuts, not deletion of arbitrary isolated turns. The signed-graph class \(\alpha+B^1\), together with the prescribed dimension-simple or vertex-simple path family, is the proper object for cut-critical investigations.
