# The antipodal line-graph cover and weighted rainbow circuits

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
