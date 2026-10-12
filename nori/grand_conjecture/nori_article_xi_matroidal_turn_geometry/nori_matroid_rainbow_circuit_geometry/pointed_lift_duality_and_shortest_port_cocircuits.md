# Pointed lift duality and shortest port cocircuits

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
