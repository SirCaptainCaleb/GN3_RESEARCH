# Boundary tournaments and doubled line-graph matroids

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
