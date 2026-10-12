# Odd-dimensional port cycles: square-derivative rigidity and terminal holes

# Odd-dimensional port cycles: square-derivative rigidity and terminal holes

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
