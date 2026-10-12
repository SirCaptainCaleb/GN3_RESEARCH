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

**Conjecture A (abstract short-port amplification).** If \(M\setminus p\) is cographic, its balanced cycle space admits bounded-size generators, its shortest port cocircuits form a connected bounded-exchange graph, and \(\mathrm{PI}_2(M,p)\) holds, then \(P_4(M,p)\) holds. A specific earlier proposal required local generators of size three or four and \(|Y\triangle Y'|\le6\) along edges of the exchange graph. The bolder version drops local generation and exchange connectivity and assumes only binary representability, cographic deletion and \(\mathrm{PI}_2\). Both formulations remain open; neither can by itself encode the boundary long-path target.

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

Test Conjecture A on small noncubical signed-graphic lifts that satisfy \(\mathrm{PI}_2\), not merely lifts with short generating cycles. Test Conjecture B on other basis-exchange graphs and oriented-matroid systems, always recording port intersection, cocircuit length, independent resource rank, admissible orientation and seam count. Test whether a monotone surgery for repeated cube-coordinate traversals has an analogue that extends boundary paths through fresh vertices. Bounded adjacent-swap exchange and the parity of signed local generators provide the most promising common algebra.

**Epistemic boundary.** The pointed lift representation, affine coset, local-generator facts, shortest-cogirth distinction, seam identity, contraction inheritance and specified counterexamples are established elsewhere in Article XI. Conjectures A--C and the resource bound (5) are open. The goal is not a matroid theorem already satisfied by the short local tournament cocircuits, but a theorem about a **decorated pointed matroid and its marked matroid-independent gallery family** capable of proving both NORI1 and long boundary-tournament paths.

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
