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
