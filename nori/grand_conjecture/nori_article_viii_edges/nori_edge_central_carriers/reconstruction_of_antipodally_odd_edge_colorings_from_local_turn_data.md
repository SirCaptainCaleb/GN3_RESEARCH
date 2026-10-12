# Reconstruction of antipodally odd edge colorings from local turn data

Fix \(n\ge3\), and let \(V=\{0,1\}^n\). For each vertex \(v\) and distinct coordinate directions \(i,j\), consider a symmetric binary array \(D=(d_{ij}(v))\), with \(d_{ij}(v)=d_{ji}(v)\). Write \(v^i=v\oplus e_i\) and \(\bar v=v\oplus(1,\ldots,1)\). We impose the following relations:
\[
\begin{array}{ll}
\text{triangle:}&d_{ij}(v)\oplus d_{jk}(v)\oplus d_{ik}(v)=0
\quad(i,j,k\text{ distinct}),\\
\text{square:}&d_{ij}(v)\oplus d_{ij}(v^i)\oplus
d_{ij}(v^j)\oplus d_{ij}(v^{ij})=0,\\
\text{antipodal:}&d_{ij}(\bar v)=d_{ij}(v).
\end{array}\tag{1}
\]
For a root \(x\) and an ordering \(\pi=(p_1,\ldots,p_n)\) of the directions, put
\[
v_s=x\oplus e_{p_1}\oplus\cdots\oplus e_{p_s},
\quad v_n=\bar x,
\]
and define its cyclic turn sum
\[
\Theta_D(x,\pi)=
\sum_{s=1}^{n-1}d_{p_s,p_{s+1}}(v_s)
+d_{p_n,p_1}(\bar x),\tag{2}
\]
where the sum in (2) is over the ordinary integers.

**Theorem 1 (complete reconstruction from incidence disagreements).** Suppose \(D\) satisfies the triangle and square relations of (1). There is an undirected-edge coloring \(c:E(Q_n)\to\{0,1\}\) such that
\[
\boxed{d_{ij}(v)=c_i(v)\oplus c_j(v)
\quad\text{for all }v,\ i\ne j,}\tag{3}
\]
where \(c_i(v)\) is the color of the edge in direction \(i\) incident with \(v\). The coloring is unique up to complementation of all edge colors.

If \(D\) also satisfies the antipodal relation, the reconstructed coloring obeys
\[
c_i(\bar v)=c_i(v)\oplus\varepsilon
\quad\text{for every }v,i,\tag{4}
\]
with one constant \(\varepsilon\in\{0,1\}\). Moreover
\[
\boxed{\Theta_D(x,\pi)\equiv\varepsilon\pmod2
\quad\text{for every root and every ordering}.}\tag{5}
\]
Consequently, \(D\) arises from an antipodally odd edge coloring if and only if it satisfies all three relations of (1) and \(\Theta_D(x,\pi)\) is odd for one (equivalently every) root and ordering. For such an array, the compatible antipodally odd edge colorings are precisely a complementary pair.

*Proof.* Fix a reference direction \(1\), and define vertex functions
\[
r_1(v)=0,\qquad r_i(v)=d_{1i}(v)\quad(i\ne1).\tag{6}
\]
The triangle relation implies \(r_i(v)\oplus r_j(v)=d_{ij}(v)\) for all distinct \(i,j\).

For every direction \(i\), define an edge cochain
\[
a_i(v)=r_i(v)\oplus r_i(v^i).\tag{7}
\]
It has the same value at the two endpoints of an \(i\)-edge. Its sum around any square in directions \(i,j\) equals
\[
\begin{aligned}
&a_i(v)\oplus a_j(v^i)\oplus a_i(v^j)\oplus a_j(v)\\
&\qquad=d_{ij}(v)\oplus d_{ij}(v^i)
\oplus d_{ij}(v^j)\oplus d_{ij}(v^{ij})=0.\tag{8}
\end{aligned}
\]
Thus \(a\) is a gradient on the cube: a binary vertex function \(f\) exists satisfying
\[
f(v)\oplus f(v^i)=a_i(v)\quad\text{for every }v,i.\tag{9}
\]
For completeness, construct \(f(v)\) by summing \(a\) along any path from the zero vertex to \(v\). Backtracking along an edge changes the sum by zero; interchanging two consecutive different coordinate steps changes it by the square sum (8), also zero. Such operations connect any two cube walks with the same endpoints, so the definition is independent of the walk.

Set
\[
c_i(v)=r_i(v)\oplus f(v).\tag{10}
\]
Equations (7) and (9) give \(c_i(v)=c_i(v^i)\), so (10) defines a coloring of undirected edges. Equation (6) and the triangle relation yield
\(c_i(v)\oplus c_j(v)=d_{ij}(v)\), proving existence.

For uniqueness, suppose \(c'\) has the same incidence disagreements. At every vertex, the values \(c_i'(v)\oplus c_i(v)\) are independent of \(i\); call this value \(b(v)\). As both colorings are constant along each edge in its direction, \(b(v)=b(v^i)\) for every \(i\), hence \(b\) is constant on the connected cube. Therefore \(c'=c\) or \(c'=1-c\).

Assume now the antipodal relation of (1). At vertex \(v\),
\[
[c_i(\bar v)\oplus c_i(v)]\oplus
[c_j(\bar v)\oplus c_j(v)]
=d_{ij}(\bar v)\oplus d_{ij}(v)=0.
\]
So \(\varepsilon(v):=c_i(\bar v)\oplus c_i(v)\) is independent of \(i\). Evaluating at vertices \(v,v^i\), using the \(i\)-edge at each and its antipodal edge, gives \(\varepsilon(v^i)=\varepsilon(v)\). Connectivity implies one constant \(\varepsilon\), proving (4).

Let \(w_1,\ldots,w_n\) be the edge-color word on the geodesic rooted at \(x\) with direction order \(\pi\). Each interior term of (2) equals \(w_s\oplus w_{s+1}\). Its final term equals \(w_n\oplus w_1\oplus\varepsilon\), because the \(p_1\)-edge at \(\bar x\) has color \(w_1\oplus\varepsilon\). The XOR of these \(n\) terms is \(\varepsilon\), proving (5). The stated criterion follows. \(\square\)

**Theorem 2 (intrinsic switch-count and counterexample criterion).** Suppose \(D\) satisfies the four requirements of Theorem 1, including odd cyclic turn parity, and let \(c\) be either reconstructed coloring. Then
\[
\boxed{\displaystyle
\mu(c)=\min_{x,\pi}\Theta_D(x,\pi)-1.}\tag{11}
\]
In particular,
\[
\boxed{
\mu(c)\le2\iff
\Theta_D(x,\pi)\le3
\text{ for some }x,\pi,}\tag{12}
\]
and a hypothetical unrestricted counterexample to the two-switch bound is equivalently an array obeying (1) and oddness for which
\[
\boxed{\Theta_D(x,\pi)\ge5\quad
\text{for every }x,\pi.}\tag{13}
\]
The values of \(\mu(c)\), the set of roots of low-switch geodesics, and their endpoint sets are determined by \(D\).

*Proof.* The number of color changes on the path with root \(x\) and order \(\pi\) is
\[
\sigma_c(x,\pi)=\sum_{s=1}^{n-1}d_{p_s,p_{s+1}}(v_s).\tag{14}
\]
Thus \(\Theta_D(x,\pi)\) is \(\sigma_c(x,\pi)\) plus a binary seam comparison, and it is always odd by Theorem 1. Cyclically rotate the direction order, changing the root from \(x\) to one of the intermediate vertices along the original path. As in the cyclic comparison identity, the resulting color words are successive cyclic shifts of
\[
w_1,\ldots,w_n,1-w_1,\ldots,1-w_n.
\]
The rotations preserve \(\Theta_D\) and respectively omit each of its \(n\) seam comparisons. Since \(\Theta_D\) is odd, at least one comparison is a change, and some rotation has \(\Theta_D-1\) changes.

Conversely, every geodesic has \(\sigma_c\ge\Theta_D-1\), because its seam comparison is at most one. Applying the preceding rotation to a geodesic minimizing \(\Theta_D\) proves (11). Oddness of \(\Theta_D\) yields (12)--(13). Equation (14) proves the statement about roots and endpoints. \(\square\)

**Corollary 3 (size of the unrestricted class).** For \(n\ge3\), the arrays \(D\) satisfying (1) and the oddness condition constitute an affine binary space of dimension
\[
\boxed{n\,2^{n-2}-1.}\tag{15}
\]

*Proof.* The \(n2^{n-1}\) undirected edges of \(Q_n\) form \(n2^{n-2}\) disjoint antipodal pairs. Choosing one edge color per pair determines an antipodally odd coloring, so these colorings form an affine binary space of dimension \(n2^{n-2}\). Their passage to \(D\) is linear with a one-dimensional kernel, namely uniform global color complementation, by Theorem 1. Its image therefore has affine dimension \(n2^{n-2}-1\). \(\square\)

The reconstruction identifies local consistency conditions sufficient to recover all unrestricted edge colorings up to their irrelevant global color phase. In particular, the low-switch problem may be phrased entirely in terms of antipodally even vertex-indexed incidence disagreements, subject to triangle, square and one global oddness constraint. The cyclic comparison and curvature-sensitive exchange inequalities then become inequalities intrinsic to \(D\); any low-switch terminal-alignment argument can be formulated in the same data without committing to a choice of edge-color phase.
