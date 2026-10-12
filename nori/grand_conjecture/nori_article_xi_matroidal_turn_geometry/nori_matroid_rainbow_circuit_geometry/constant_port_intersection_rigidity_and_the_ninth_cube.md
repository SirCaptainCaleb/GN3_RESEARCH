# Constant port intersection rigidity and the ninth cube

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
