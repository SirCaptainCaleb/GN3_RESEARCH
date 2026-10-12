# Sharp square-derivative deficits and terminal holes in odd-dimensional cubes

### Sharp square-derivative deficits and terminal holes

Let \(n\ge3\) be odd. For an antipodally odd coloring \(c\) of undirected edges of \(Q_n\), write \(c_i(x)\) for the color of \(\{x,x^i\}\). Then
\[
c_i(x^i)=c_i(x),\qquad c_i(\bar x)=1+c_i(x).
\tag{1}
\]
All color arithmetic is in \(\mathbb F_2\). Write \(\mu(c)\) for the minimum switch count on a long geodesic of \(Q_n\).

For distinct directions \(i,j\), each \((i,j)\)-square is indexed by a projected vertex \(z\in Q_{[n]\setminus\{i,j\}}\). Its cross-derivatives
\[
d_{ij}(z)=c_i(x)+c_i(x^j),\qquad
d_{ji}(z)=c_j(x)+c_j(x^i)
\tag{2}
\]
are independent of the omitted bits of \(x\). Set
\[
B_{ij}=\{z:(d_{ij}(z),d_{ji}(z))\ne(1,1)\},\quad
D=\sum_{i<j}|B_{ij}|,
\tag{3}
\]
\[
Z_i=\sum_{j\ne i}|\{z:d_{ij}(z)=0\}|,\qquad
K=\sum_{i<j}|\{z:d_{ij}(z)+d_{ji}(z)=1\}|.
\tag{4}
\]

**Theorem 1 (sharp bound and rigidity).** Every coloring satisfying (1) in odd dimension has
\[
Z_i\ge2^{n-2}\ (i\in[n]),\qquad K\ge2^{n-2},\qquad
\boxed{D\ge(n+1)2^{n-3}.}
\tag{5}
\]
The final bound is sharp for every odd \(n\ge3\). Equality holds precisely for colorings
\[
\boxed{c_i(x)=a_i+\sum_{j\notin\{i,p(i)\}}x_j,}
\tag{6}
\]
where \(a_i\in\mathbb F_2\) and the directed partner map \(p\) pairs \(n-1\) coordinates into reciprocal pairs, with the remaining coordinate \(w\) pointing to a member of one pair. Every coloring of form (6) admits a monochromatic long geodesic. Consequently,
\[
\boxed{\mu(c)\ge4\ \Longrightarrow\ D\ge(n+1)2^{n-3}+2.}
\tag{7}
\]

*Proof.* Fix direction \(i\), and regard \(c_i\) as a function of the \(d=n-1\) other bits \(y\), where \(d\) is even. Put
\[
f_i(y)=(-1)^{c_i(y)+\sum_{j\ne i}y_j}.
\tag{8}
\]
Antipodal oddness gives \(f_i(\bar y)=-f_i(y)\), so its mean is zero. The value of \(f_i\) changes along a \(j\)-edge precisely when \(d_{ij}=0\). In the Walsh expansion \(f_i=\sum_S\widehat f_i(S)\chi_S\), Parseval and the elementary directional-edge count give
\[
Z_i=2^{d-1}\sum_{S\ne\varnothing}|S|\widehat f_i(S)^2
\ge2^{d-1}\sum_{S\ne\varnothing}\widehat f_i(S)^2
=2^{n-2}.
\tag{9}
\]
Equality forces Fourier degree one. Since \(f_i^2=1\), writing \(f_i=\sum_j b_j\chi_{\{j\}}\) and comparing the coefficients of \(\chi_{\{j,k\}}\) gives \(b_jb_k=0\) for distinct \(j,k\). Thus \(f_i\) is a signed coordinate character. Reversing (8), equality in (9) is equivalent to
\[
c_i(x)=a_i+\sum_{j\notin\{i,p(i)\}}x_j
\quad\text{for some }p(i)\ne i.
\tag{10}
\]

For the curvature count, fix a direction ordering \(\pi\), and reverse it through \(\binom n2\) adjacent swaps, each unordered pair of directions crossing once. At any root \(x\), the color word for the reversed order is the complemented reversal of the original word, by (1). Their color sums therefore differ by \(n=1\pmod2\). Each adjacent swap changes that sum by \(d_{ij}+d_{ji}\) at the intervening square. Hence an odd number of the squares in the swap sequence have nonzero curvature at every root. Summing over \(2^n\) roots, each square is counted four times: its swapped directions and earlier direction set are fixed, while the two square-coordinate bits of the root vary freely. Therefore \(4K\ge2^n\), proving the middle bound in (5).

A square with derivative pair \((1,1)\) contributes \(0,0,0\) to the counts \((D,\sum_iZ_i,K)\). A square with \((0,0)\) contributes \((1,2,0)\); a square with \((1,0)\) or \((0,1)\) contributes \((1,1,1)\). Thus
\[
2D=\sum_iZ_i+K\ge(n+1)2^{n-2},
\tag{11}
\]
proving the last bound in (5).

Equality in (11) forces equality in (9) for every \(i\) and equality in the curvature bound. Hence (10) holds for every direction. In that case,
\[
d_{ij}+d_{ji}=[p(i)=j]+[p(j)=i]
\tag{12}
\]
is constant over all \((i,j)\)-squares. Since \(K=2^{n-2}\), there is precisely one unordered direction pair with a nonreciprocal partner relation. The directed graph of \(p\) has one outgoing arc at each vertex; all but one arcs belong to reciprocal pairs. Its structure is therefore the paired map with one unmatched vertex described in the theorem. Conversely, that map has \(Z_i=2^{n-2}\) for all \(i\), and one direction pair of nonzero curvature, so it attains (5).

We prove monochromaticity for every equality coloring, allowing arbitrary constants \(a_i\). Write the reciprocal pairs as \(\{u_r,v_r\}\), \(1\le r\le m=(n-1)/2\), with unmatched vertex \(w\). Choose a permutation of directions, with position \(t_i\) for direction \(i\), such that
\[
t_{u_r}+t_{v_r}=1+a_{u_r}+a_{v_r}\pmod2.
\tag{13}
\]
This permutation exists by assigning the pairs successively to positions of the required parities. Among any odd number of unused positions, one parity class has one more position than the other. For a required same-parity pair, use two positions of the larger class; for a required opposite-parity pair, use one position of each class. The remaining classes again differ by one, and the final unused position is assigned to \(w\).

Let \(S_i\) be the directions preceding \(i\) in this permutation and set
\[
\eta_i=a_i+(t_i-1)+[p(i)\in S_i].
\tag{14}
\]
Equation (13) ensures \(\eta_{u_r}=\eta_{v_r}=:\eta_r\). Choose arbitrary bits \(T,q\). Prescribe the root-coordinate pair sums
\[
s_r=x_{u_r}+x_{v_r}=T+q+\eta_r,
\tag{15}
\]
set \(x_w=T+\sum_rs_r\), and set \(x_{p(w)}=T+q+\eta_w+x_w\). Complete the remaining root bits so that all prescribed pair sums hold; the conditions are compatible since \(p(w)\) belongs to one reciprocal pair. These assignments give \(\sum_i x_i=T\). At the step traversing direction \(i\), equation (6) now yields
\[
c_i(x^{S_i})
=T+x_i+x_{p(i)}+\eta_i=q
\tag{16}
\]
for each paired direction by (15), and also for \(w\) by its prescribed coordinate. Thus the full path is monochromatic.

Antipodal complementation preserves both cross-derivatives of every square, and pairs the projected vertices \(z,\bar z\). Since \(n-2\ge1\), those vertices differ, and \(D\) is even. Any coloring with \(\mu(c)\ge4\) lies outside the equality family by the preceding construction, giving the strict even-integer bound (7). \(\square\)

**Theorem 2 (global terminal-hole obstruction).** Assume \(n\ge5\) odd. For each pair \(i<j\), consider the four codimension-two faces obtained by fixing bits \(i,j\), and project their long-geodesic terminals with at most two switches onto the common \(Q_{n-2}\). Let \(H_{ij}\) be the complement of the union of these four projected terminal sets. If \(\mu(c)\ge4\), then
\[
\boxed{B_{ij}\subseteq H_{ij}\quad(i<j),}
\tag{17}
\]
\[
\boxed{\sum_{i<j}|H_{ij}|\ge(n+1)2^{n-3}+2,\qquad
\sum_{j\ne i}|H_{ij}|\ge2^{n-2}\quad(i\in[n]).}
\tag{18}
\]
Furthermore, fix a direction \(i\) and identify the direction-\(i\) edges of \(Q_n\) with vertices of \(Q_{n-1}\). Along every long geodesic of this edge-position cube, an odd number of crossed edges have \(d_{ij}=0\), where \(j\) is the crossed direction. Each corresponding \((i,j)\)-square belongs to \(H_{ij}\) under projection.

*Proof.* Suppose a projection \(z\) is the terminal of a long geodesic \(P\) with at most two switches in one of the four \((n-2)\)-faces. Write \(x\) for its terminal corner and \(q\) for its last color. When \(\mu(c)\ge4\), \(P\) must have two switches: appending both exterior directions to a path with at most one switch would produce at most three switches, implying \(\mu(c)\le2\) by the evenness of \(\mu(c)\). Append the two exterior directions to \(P\) in either order. Each full geodesic has at most four switches and therefore must have four. Both added comparisons must be switches. The two square edges leaving \(x\) have color \(1+q\), and the two entering its opposite corner have color \(q\). It follows that \(d_{ij}(z)=d_{ji}(z)=1\). This proves (17). The bounds (18) follow from (17), (5), (7), and the definition of \(Z_i\).

For the last assertion, a long geodesic in the edge-position cube joins \(y\) to \(\bar y\) and has \(n-1\) edges. The sum of its crossed derivatives is \(c_i(y)+c_i(\bar y)=1\). Since \(n-1\) is even, an odd number of these derivatives vanish. Each vanishing derivative marks a square belonging to \(B_{ij}\subseteq H_{ij}\). \(\square\)

**Corollary (a two-switch certificate).** In odd dimension \(n\ge5\), the inequality
\[
\sum_{i<j}|H_{ij}|\le(n+1)2^{n-3}+1
\tag{19}
\]
implies \(\mu(c)\le2\).

The directional constraint applies to every antipodal geodesic in each edge-position cube and couples the four-face terminal sets across all exterior direction pairs. No antipodal symmetry is assumed for the edge coloring restricted to an individual face.
