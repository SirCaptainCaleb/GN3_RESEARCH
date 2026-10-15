# Canonical permutahedral contraction and protected endpoint faces

### Canonical permutahedral contraction, terminal signs, and an equivariant relative field

Write \(W=\{x\in\mathbb R^n:\sum x_i=0\}\), \(n\ge4\), and let \(P_n\subset W\) be the centered permutahedron. For each permutation \(\pi\), its centered prefix vectors are
\[
Z_j(\pi)=\sum_{h\le j}e_{\pi_h}-\frac jn\mathbf1,\qquad 1\le j<n.
\]
Put
\[
\boxed{\rho(\pi)=\sum_{j=1}^{n-1}Z_j(\pi)
=\sum_{j=1}^n\left(\frac{n+1}{2}-j\right)e_{\pi_j},}
\tag{1}
\]
the vertex position vector of \(P_n\). Let \(S_\pi\subseteq\{1,\ldots,n-1\}\) be any set of at least two switch-prefix ranks, and define
\[
\mathcal B(\pi)=\sum_{\substack{r<s\\r,s\in S_\pi}}Z_r(\pi)\wedge Z_s(\pi),\qquad
H(\pi)=\iota_{\rho(\pi)}\mathcal B(\pi)\in\rho(\pi)^\perp.
\tag{2}
\]

**Theorem 1 (canonical positivity without choosing a contraction).** For every \(S_\pi\) with at least two ranks, \(H(\pi)\ne0\). If \(p=\min S_\pi\), \(q=\max S_\pi\), then
\[
\boxed{
\langle H(\pi),Z_k(\pi)\rangle<0\quad(1\le k\le p),\qquad
\langle H(\pi),Z_k(\pi)\rangle>0\quad(q\le k<n).
}
\tag{3}
\]
In particular, \(H_{\pi_1}<0\) and \(H_{\pi_n}<0\).

*Proof.* The Gram kernel \(G(i,j)=\langle Z_i,Z_j\rangle=\min(i,j)-ij/n\) has nonnegative ordered minors
\[
D(i,j;r,s)=\langle Z_i\wedge Z_j,Z_r\wedge Z_s\rangle\ge0
\quad(i<j,\ r<s),
\]
with strict positivity whenever the open intervals \((i,j)\) and \((r,s)\) overlap, as proved in the total-positivity Subsection. Expanding \(H\) using \(\rho=\sum_t Z_t\), for \(k\le p\) all terms \(t\le k\) have disjoint rank intervals and vanish, while all \(t>k\) contribute \(-D(k,t;r,s)\le0\). The contribution \(t=q,(r,s)=(p,q)\) is strictly negative. For \(k\ge q\), all terms \(t\ge k\) vanish, the remaining terms contribute \(D(t,k;r,s)\ge0\), and \(t=p,(r,s)=(p,q)\) is strictly positive. This proves (3) and nonvanishing. Finally \(Z_1=e_{\pi_1}-\mathbf1/n\) and \(Z_{n-1}=\mathbf1/n-e_{\pi_n}\). Since \(H\in W\), (3) at \(k=1,n-1\) yields both terminal entries negative. QED.

**Theorem 2 (even tangent-vector carrier and its global obstruction).** If the switch word is odd under complemented reversal, then
\[
\rho(\pi^R)=-\rho(\pi),\quad
\mathcal B(\pi^R)=-\mathcal B(\pi),\quad
\boxed{H(\pi^R)=H(\pi).}
\tag{4}
\]
Thus (2) gives a nonzero even tangent label at every vertex of \(\partial P_n\cong S^{n-2}\), under the hypothesis of at least two switches at every full ordering. No continuous nowhere-zero extension of these labels to the whole sphere that remains tangent to the radial vector and even under antipodality exists, for any \(n\).

*Proof.* Centered prefix reversal satisfies \(Z_{n-j}(\pi^R)=-Z_j(\pi)\); the switch set reverses and every ordered bivector pair acquires a minus sign, proving (4). Normalize the centrally symmetric boundary of \(P_n\) radially to the unit sphere in \(W\), and put \(d=n-2\). A continuous field \(h(x)\in x^\perp\setminus\{0\}\) with \(h(-x)=h(x)\) would descend to a nowhere-zero section of the rank-\(d\) orthogonal complement bundle \(\gamma^\perp\) of the tautological line \(\gamma\to\mathbb RP^d\). But
\[
w(\gamma^\perp)=(1+\alpha)^{-1}
=1+\alpha+\cdots+\alpha^d,\qquad
w_d(\gamma^\perp)=\alpha^d\ne0,
\tag{5}
\]
contradicting a nonzero section. QED.

**Theorem 3 (automatic zero-free interpolation on protected terminal faces).** Let \(F\) be a parabolic face of \(P_n\) represented by an ordered partition whose first block is \(A\), last block is \(C\), with \(|A|=a\ge1\), \(|C|=c\ge1\). Suppose all full orders \(\pi\) refining the face have at least two switches and
\[
a\le\min S_\pi,\qquad \max S_\pi\le n-c.
\tag{6}
\]
Fix any triangulation of \(F\) using its permutahedral vertices and extend \(H\) and \(\rho\) piecewise affinely to functions \(V(x)\) and \(\rho(x)=x\) on \(F\). Then
\[
\boxed{
h_F(x)=V(x)-\frac{\langle V(x),x\rangle}{\|x\|^2}x\ne0
\quad(x\in F).
}
\tag{7}
\]
These local formulas agree on common faces when obtained from a single triangulation of \(\partial P_n\); reversal sends \(h_F(x)\) to \(h_{F^R}(-x)=h_F(x)\).

*Proof.* The vectors \(Z_a=\mathbf1_A-(a/n)\mathbf1\) and \(Z_{n-c}=-(\mathbf1_C-(c/n)\mathbf1)\) are fixed on all vertices of \(F\). By (3) and (6), \(\sum_{i\in A}H_i<0\) and \(\sum_{i\in C}H_i<0\) for every vertex; thus both remain strictly negative under affine interpolation. But the permutahedral position vector has fixed opposite-sign block sums on \(F\):
\[
\sum_{i\in A}x_i=\frac{a(n-a)}2>0,\qquad
\sum_{i\in C}x_i=-\frac{c(n-c)}2<0.
\]
Consequently \(V(x)\) cannot be proportional to \(x\): a proportionality factor would have to be negative on the first block and positive on the last. Its orthogonal projection in (7) is nonzero. Both projection and interpolation respect reversal by (4), proving the equivariance assertion. QED.

**Corollary 4 (unrestricted boundary and cube support).** Under the hypothetical absence of a Hamilton order with at most one switch, every boundary 3-tournament has switch ranks in \(\{2,\ldots,n-2\}\). Therefore (7) constructs an explicit color-dependent, zero-free, reversal-even tangent section on the subcomplex of permutahedral faces whose first and last blocks each have size at most two. For cube-edge words, the rank range is \(\{1,\ldots,n-1\}\), and the same construction protects all faces with first and last blocks singleton. Its global obstruction remains the nonzero class (5). A cube geodesic with at most one switch can be root-slid to a monochromatic antipodal geodesic.

**Boundary of the result.** Equations (1)-(3) eliminate algebraic genericity and choice of contraction completely. Theorem 3 provides a canonical compatible relative interpolation, but its protected terminal-face subcomplex is not the entire permutahedral sphere. Rank-three tetrahedral parity obstructions can still prevent the naive zero-free extension on other faces; the global conjectures remain unresolved.
