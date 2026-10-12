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
