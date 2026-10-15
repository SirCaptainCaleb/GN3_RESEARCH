# Affine cube-edge colorings and elimination of rank-one obstructions

# Affine cube-edge colorings: permutation syndromes and elimination of two-dimensional obstructions

Let \(Q_n\) have coordinates in \(\mathbb F_2^n\). Consider arbitrary affine binary colors on its undirected coordinate edges,
\[
c_i(x)=a_i+\sum_{j\ne i}B_{ij}x_j,
\qquad a\in\mathbb F_2^n,\quad B\in\mathbb F_2^{n\times n},\quad B_{ii}=0.
\tag{1}
\]
The formula is independent of the toggled bit \(x_i\), as required for an undirected edge color. The antipodal oddness condition \(c_i(x+\mathbf1)=c_i(x)+1\) is equivalent to
\[
B\mathbf1=\mathbf1.
\tag{2}
\]
The matrix \(B\) is the linear cross-coordinate influence operator of the edge coloring. Write \(V=\mathbb F_2^n/\operatorname{im}B\), and denote the quotient map by \(p:\mathbb F_2^n\to V\).

For a permutation \(\pi=(i_1,\dots,i_n)\), put
\[
v_\pi(i)=\sum_{j\text{ occurring before }i\text{ in }\pi} B_{ij}.
\tag{3}
\]
A geodesic beginning at \(x\) and flipping the coordinates in order \(\pi\) has color word, indexed by its step directions,
\[
c_{\pi}(x)=a+Bx+v_\pi.
\tag{4}
\]
It is monochromatic if and only if
\[
a+v_\pi\in\operatorname{im}B.
\tag{5}
\]
Indeed a constant color-one word can be converted to a color-zero word by replacing its root \(x\) by \(x+\mathbf1\), using (2). The obstruction to a given order is therefore the quotient syndrome \(p(a+v_\pi)\).

**Lemma 1 (cyclic rotation identity).** If \(\pi=(i,i_2,\ldots,i_n)\) and \(\operatorname{rot}\pi=(i_2,\ldots,i_n,i)\), then
\[
v_{\operatorname{rot}\pi}=v_\pi+e_i+Be_i,
\qquad
p(v_{\operatorname{rot}\pi})=p(v_\pi)+p(e_i).
\tag{6}
\]
For every permutation the \(n\) cyclic rotations consequently trace in \(V\) a closed walk whose successive increments are \(p(e_{i_1}),\ldots,p(e_{i_n})\).

*Proof.* Moving the first direction \(i\) to the end changes its own predecessor parity from zero to \(\sum_{j\ne i}B_{ij}=1\). For every other direction \(j\), the presence of \(i\) among its predecessors is removed, changing its parity by \(B_{ji}\). Thus the syndrome difference is \(e_i+Be_i\). The second equation follows by quotienting by \(\operatorname{im}B\), and the cyclic walk follows by iteration. The walk closes because \(\sum_i p(e_i)=p(\mathbf1)=0\) by (2). \(\square\)

**Theorem 2 (affine rank-codimension-two closure).** Suppose (1)--(2) hold and
\[
\boxed{\operatorname{rank}_{\mathbb F_2}B\ge n-2.}
\tag{7}
\]
Then there exist a starting vertex \(x\) and a coordinate permutation \(\pi\) such that the entire antipodal geodesic \(x\to x+\mathbf1\) following \(\pi\) is monochromatic. In particular every antipodally odd affine cube-edge coloring whose cross-influence matrix has nullity at most two satisfies NORI1.

More precisely, for every \(a\), the quotient-syndrome set
\[
\boxed{\{p(v_\pi):\pi\in S_n\}=V}
\tag{8}
\]
whenever \(\dim V\le2\). If \(\dim V=0\), every permutation admits a monochromatic geodesic; for each successful permutation, the number of roots of either prescribed constant color is \(2^{n-\operatorname{rank}B}\), and the roots for opposite colors are antipodal translates.

*Proof.* Let \(t=\dim V=n-\operatorname{rank}B\). The claim is immediate for \(t=0\), since then \(V=0\). If \(t=1\), the classes \(p(e_i)\) span \(V\), so some \(i\) has \(p(e_i)\ne0\). Take any permutation starting with \(i\). Lemma 1 shows that its syndrome and the syndrome of its cyclic rotation differ by the nonzero element of \(V\), and hence together attain all of \(V\).

Now let \(t=2\). Put \(w_i=p(e_i)\in V\cong\mathbb F_2^2\). Their sum vanishes by (2), and they span \(V\), since the \(e_i\) span \(\mathbb F_2^n\). Suppose there are distinct indices \(i,j,h\) with
\[
w_i=w_h=u\ne0,\qquad w_j=v\notin\{0,u\}.
\tag{9}
\]
Choose a permutation beginning \((i,j,h)\). Its first four cyclic-rotation syndromes, by (6), differ from the first by
\[
0,\quad u,\quad u+v,\quad v,
\]
which exhaust \(V\). Thus (8) follows in this case.

It remains to show that (9) can fail only in a special configuration and that this configuration also satisfies (8). Let \(N_u,N_v,N_{u+v}\) be the multiplicities of the three nonzero vectors of \(V\) among the \(w_i\). The identity \(\sum_iw_i=0\) forces
\[
N_u\equiv N_v\equiv N_{u+v}\pmod2.
\tag{10}
\]
Since the \(w_i\) span \(V\), if some nonzero value occurs at least twice and another linearly independent nonzero value occurs, (9) holds. If no such pair exists, (10) implies that the only nonzero \(w_i\) are three distinct values \(u,v,u+v\), each appearing once. Denote their indices by \(i,j,h\) respectively. All other \(w_\ell\) vanish.

Because \(p(Be_\ell)=0\) for every \(\ell\), this exceptional configuration gives
\[
B_{i\ell}u+B_{j\ell}v+B_{h\ell}(u+v)=0.
\]
Linear independence of \(u,v\) yields
\[
B_{i\ell}=B_{j\ell}=B_{h\ell}\qquad\text{for every }\ell.
\tag{11}
\]
The three rows \(i,j,h\) of \(B\) coincide. Their diagonal entries vanish, so their entries in the three columns \(i,j,h\) are all zero. By (2), their common row has odd sum; consequently some index \(z\notin\{i,j,h\}\) satisfies
\[
B_{iz}=B_{jz}=B_{hz}=1,\qquad w_z=0.
\tag{12}
\]

Choose \(\pi=(i,z,j,h,\ldots)\). Its first cyclic-rotation syndromes attain the three values
\[
p(v_\pi)+\{0,u,u+v\};
\]
the missing fourth value is \(p(v_\pi)+v\). Swap the adjacent symbols \(z,j\), obtaining \(\pi'=(i,j,z,h,\ldots)\). An adjacent transposition of directions \(j,z\) changes \(v_\pi\) by
\(B_{jz}e_j+B_{zj}e_z\). By (12),
\[
p(v_{\pi'})=p(v_\pi)+w_j=p(v_\pi)+v,
\]
the missing value. Thus the two permutations together with the displayed cyclic rotations exhaust \(V\). This proves (8) for \(t=2\).

Finally, (8) permits choosing \(\pi\) so that \(p(v_\pi)=p(a)\), making (5) hold. The system \(Bx=a+v_\pi\) then has \(2^{n-\operatorname{rank}B}\) roots. Adding \(\mathbf1\) to any solution changes all its edge colors from zero to one by (2), proving the last assertion. \(\square\)

**Corollary 3 (necessary structure of affine counterexamples).** An affine antipodally odd counterexample to NORI1, if one exists, must have
\[
\boxed{\dim\ker B^{\mathsf T}\ge3.}
\tag{13}
\]
Furthermore for any \(B\) satisfying (2), the quotient syndrome of a cyclically rotated permutation changes by a coordinate class \(p(e_i)\). Thus the possible affine obstruction is a simultaneous multi-syndrome obstruction on the permutation exchange geometry; no obstruction of dimension one or two survives arbitrary cyclic rotations and adjacent transpositions.

The theorem is dimension-independent, and imposes no symmetry on \(B\). Its proof uses the same resource-permutation language as the dual-basis galleries of Article XI. It establishes full rank saturation for a broad affine NORI1 class, while leaving nonlinear colorings and affine influence matrices of nullity at least three open.

## 4. Uniform random affine closure probability

Consider the uniform ensemble of affine antipodally odd cube-edge colorings (1): choose each intercept \(a_i\) independently and uniformly, and independently choose each row \(B_{i,*}\) uniformly among binary vectors with \(B_{ii}=0\) and odd Hamming weight. Every admissible affine coloring occurs with equal probability.

**Theorem 4 (random influence rank).** For \(n\ge3\), if \(T=n-\operatorname{rank}B=\dim\ker B^{\mathsf T}\), then
\[
\boxed{\mathbb E(2^T-1)=1-2^{1-n}.}
\tag{14}
\]
Consequently,
\[
\boxed{\Pr(T\ge3)\le\frac{1-2^{1-n}}7<\frac17,}
\tag{15}
\]
and, by Theorem 2, the probability that an affine antipodally odd cube-edge coloring admits a full monochromatic antipodal geodesic is at least
\[
\boxed{1-\frac{1-2^{1-n}}7>\frac67.}
\tag{16}
\]
The conclusion is uniform in the dimension and in the arbitrary intercept vector.

*Proof.* Expand \(2^T-1=\sum_{y\ne0}\mathbf1_{\{y^{\mathsf T}B=0\}}\). Since \(B\mathbf1=\mathbf1\), any left-kernel vector \(y\) has even Hamming weight, so an odd-weight \(y\) contributes zero probability. For an even-weight nonzero \(y\), choose two distinct positions \(i,j\) in its support. A uniform row \(B_{i,*}\) is supported on the odd-parity affine hyperplane with coordinate \(i\) fixed to zero; its translation space is
\[
W_i=\{z:z_i=0,\ z\cdot\mathbf1=0\}.
\]
For \(n\ge3\), the sum \(W_i+W_j\) is the full even-parity hyperplane \(W=\{z:z\cdot\mathbf1=0\}\). Indeed \(W_i^\perp=\langle\mathbf1,e_i\rangle\) and \(W_j^\perp=\langle\mathbf1,e_j\rangle\), whose intersection is \(\langle\mathbf1\rangle\); taking orthogonal complements proves the claim. The sum of the two independent uniform rows is consequently uniform on an even-parity affine coset, which here equals \(W\). Adding the other independently chosen rows in the even support of \(y\) preserves uniformity on \(W\), since their total parity is even. Thus
\[
\Pr(y^{\mathsf T}B=0)=|W|^{-1}=2^{-(n-1)}
\]
for every even-weight nonzero \(y\). There are \(2^{n-1}-1\) such vectors. Summing proves (14). On the event \(T\ge3\), the number \(2^T-1\) is at least seven, so Markov's inequality gives (15). Theorem 2 guarantees the desired geodesic on the complementary event \(T\le2\), proving (16). \(\square\)

The estimate concerns an ensemble of arbitrary affine cross-coordinate influence operators, including nonsymmetric ones. It is independent of the chosen coordinate order and complements the permutation-syndrome closure theorem, which applies deterministically whenever \(T\le2\).
