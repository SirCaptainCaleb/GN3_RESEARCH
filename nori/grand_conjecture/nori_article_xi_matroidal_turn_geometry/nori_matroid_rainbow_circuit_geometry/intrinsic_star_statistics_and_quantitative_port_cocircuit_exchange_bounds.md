# Intrinsic star statistics and quantitative port-cocircuit exchange bounds

# Intrinsic star statistics and quantitative port–cocircuit exchange bounds

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
