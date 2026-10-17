# Integral saturation and Fourier rigidity of geodesic incidence

Let \(n\ge5\), \(F_n=Q_n/\langle\tau\rangle\), and \(H_n=L(F_n)\). Index the turn edges of \(H_n\) by \(t_{ij}([x])\), where \([x]\in\mathbb F_2^n/\langle\mathbf1\rangle\) is the antipodal orbit of a cube vertex and \(\{i,j\}\) is an unordered pair of distinct directions. Let \(\mathcal G_n\) be the family of length-\(n\) odd-monodromy turn cycles (full antipodal geodesics), each represented by its unsigned \(0/1\) incidence vector \(g_C\in\mathbb Z^{E(H_n)}\). Define the integral geodesic incidence lattice
\[
\Lambda_n=\operatorname{span}_{\mathbb Z}\{g_C:C\in\mathcal G_n\}
\subseteq\mathbb Z^{E(H_n)}.
\tag{1}
\]

**Theorem 1 (Fourier decomposition of all zero-sum turn weights).** Let \(\mathbb K\) be a field of characteristic different from two. A turn weighting \(z:E(H_n)\to\mathbb K\) satisfies
\[
\sum_{t\in C}z(t)=0\qquad\text{for every }C\in\mathcal G_n
\tag{2}
\]
if and only if it has a unique Fourier decomposition
\[
\boxed{z(t_{ij}([x]))=
\sum_{\substack{S\subseteq[n]\\|S|\equiv0\ (2)}}
(-1)^{\sum_{r\in S}x_r}\bigl(b_{i,S}+b_{j,S}\bigr),}
\tag{3}
\]
where the coefficients \(b_{i,S}\in\mathbb K\) satisfy
\[
\boxed{
\begin{cases}
\sum_{i=1}^n b_{i,\varnothing}=0,&S=\varnothing,\\
b_{i,S}=0\text{ for }i\notin S,&S\ne\varnothing.
\end{cases}}
\tag{4}
\]
(The coefficient representation is unique, not merely the resulting weighting.) In particular the space of such zero-sum weightings has dimension
\[
\boxed{\dim_{\mathbb K}\ker\mathcal I_n=
(n-1)+\sum_{\substack{S\ne\varnothing\\|S|\ {\rm even}}}|S|
=n2^{n-2}+n-1,}
\tag{5}
\]
where \(\mathcal I_n\) denotes the matrix with rows \(g_C\).

*Proof.* The group \(V_n=\mathbb F_2^n/\langle\mathbf1\rangle\) of folded cube translations acts regularly on the folded vertex orbits, and its character group consists of \(\chi_S([x])=(-1)^{\sum_{r\in S}x_r}\), indexed by even-cardinality \(S\). Since the characteristic is odd, Fourier inversion holds in \(\mathbb K[V_n]\). Every turn weighting therefore has a unique expansion
\[
z(t_{ij}([x]))=\sum_{S\ {\rm even}}\chi_S([x])a_{ij,S},
\tag{6}
\]
with symmetric pair coefficients \(a_{ij,S}=a_{ji,S}\). A geodesic rooted at \(x\), with direction order \(\pi=(\pi_1,\ldots,\pi_n)\), evaluates the \(S\)-mode as
\[
\chi_S([x])F_S(\pi),\qquad
F_S(\pi)=\sum_{t=1}^n
\varepsilon_t\,a_{\pi_t\pi_{t+1},S},\qquad
\varepsilon_t=\prod_{r=1}^t s_{\pi_r},
\tag{7}
\]
where \(\pi_{n+1}=\pi_1\) and \(s_i=-1\) if \(i\in S\), \(s_i=1\) otherwise. Since \(|S|\) is even, the closing turn is also correctly represented by (7). Varying \(x\) separates all Fourier modes; hence (2) holds if and only if \(F_S(\pi)=0\) for every even \(S\) and every permutation \(\pi\).

Fix an even \(S\), omit the subscript \(S\), and suppose \(F_S(\pi)=0\) for all \(\pi\). Compare two permutations with the same prefix and suffix but consecutive four-direction blocks \((h,i,j,k)\) and \((h,j,i,k)\). The three terms around the swap give
\[
\boxed{
(a_{hi}-a_{hj})+(s_i-s_j)a_{ij}
+s_is_j(a_{jk}-a_{ik})=0
}
\tag{8}
\]
for any four pairwise distinct directions. For fixed \(i,j\) put \(d_h=a_{hi}-a_{hj}\), for \(h\notin\{i,j\}\). Equation (8) becomes
\[
d_h-s_is_jd_k=-(s_i-s_j)a_{ij}
\qquad(h,k\notin\{i,j\},\ h\ne k).
\tag{9}
\]
If \(s_i=s_j\), then \(d_h=d_k\). If \(s_i\ne s_j\), then \(d_h+d_k\) is independent of \(h,k\). Because \(n\ge5\) leaves at least three eligible values of \(h\), the latter equations again force all \(d_h\) to agree. We have proved that for every pair \(i,j\), the difference \(a_{hi}-a_{hj}\) does not depend on \(h\) outside that pair.

The elementary additive complete-graph lemma now applies: over any field of characteristic different from two, these column-difference conditions imply
\[
\boxed{a_{ij}=b_i+b_j}
\tag{10}
\]
for a unique vector \(b\in\mathbb K^n\). One way to construct \(b\) is to solve \(b_1+b_2=a_{12}\), \(b_1+b_3=a_{13}\), \(b_2+b_3=a_{23}\), and use all the difference conditions to extend to every other vertex; uniqueness follows since \(b_i+b_j=0\) for all \(i\ne j\) forces every \(b_i=0\) when two is invertible.

If \(S\) is nonempty and proper, choose \(i\in S,j\notin S\). With \(s_i=-1,s_j=1\), substituting (10) into (9) gives
\[
2(b_i-b_j)=2(b_i+b_j),
\]
so \(b_j=0\). Every \(j\notin S\) can be paired with some \(i\in S\), proving the support condition in (4). If \(S=[n]\) (possible only for even \(n\)), the support condition is automatic. Conversely, for any nonempty even \(S\) and any \(b\) supported on \(S\), the cyclic sum in (7), with (10), groups by vertex as
\[
F_S(\pi)=\sum_{t=1}^n
(\varepsilon_{t-1}+\varepsilon_t)b_{\pi_t},
\qquad \varepsilon_0=\varepsilon_n.
\tag{11}
\]
Each term with \(\pi_t\in S\) vanishes because \(\varepsilon_t=-\varepsilon_{t-1}\), while every \(b_{\pi_t}\) with \(\pi_t\notin S\) is zero. Thus these \(b\) are all solutions, giving a kernel of dimension \(|S|\).

For \(S=\varnothing\), the same swap calculation gives (10), but \(F_\varnothing(\pi)=2\sum_i b_i\). Since two is invertible, the condition is \(\sum_i b_i=0\), a space of dimension \(n-1\). These classifications prove (3)--(4). Finally each direction \(i\) belongs to \(2^{n-2}\) even subsets, yielding \(\sum_{S\ {\rm even}}|S|=n2^{n-2}\), proving (5). \(\square\)

**Theorem 2 (field-independent geodesic-incidence rank).** For every field \(\mathbb K\), including characteristic two,
\[
\boxed{
\operatorname{rank}_{\mathbb K}\mathcal I_n
=
|E(H_n)|-|V(H_n)|-n+1
=
n(n-2)2^{n-2}-n+1.
}
\tag{12}
\]

*Proof.* For fields of odd characteristic, (5) and \(|E(H_n)|=\binom n2 2^{n-1}\), \(|V(H_n)|=n2^{n-2}\), give the displayed rank by rank-nullity. In characteristic two, the geodesic incidence-row span is \(\mathscr B_n+\langle G\rangle\), where \(\mathscr B_n\) is the binary geodesic-exchange hexagon span and \(G\) is one reference geodesic cycle. Theorem 1 of the preceding geodesic-exchange homology Subsection established
\(\dim_{\mathbb F_2}\mathscr B_n=|E(H_n)|-|V(H_n)|-n\); the reference geodesic lies outside that span because it has monodromy one whereas \(\mathscr B_n\subseteq\ker\alpha\). Thus the binary rank is the same. \(\square\)

**Corollary 3 (saturated integral geodesic lattice).** The lattice \(\Lambda_n\) in (1) is a saturated sublattice of \(\mathbb Z^{E(H_n)}\). Equivalently
\[
\boxed{\mathbb Z^{E(H_n)}/\Lambda_n
\quad\text{has no nonzero torsion}.}
\tag{13}
\]
Every integral turn vector lying in the rational span of the unsigned antipodal-geodesic incidence vectors is therefore an integral linear combination of those incidence vectors.

*Proof.* Apply Smith normal form to the integer matrix \(\mathcal I_n\). Let its nonzero diagonal invariant factors be \(d_1,\ldots,d_r>0\), with \(r\) the rational rank in (12). If a prime \(\ell\) divided any \(d_i\), reduction modulo \(\ell\) would lower the matrix rank below \(r\). But Theorem 2 gives rank \(r\) in every prime characteristic. Hence all nonzero Smith invariant factors equal one, giving (13). \(\square\)

**Corollary 4 (real-valued geodesic weight rigidity).** The Fourier expression (3)--(4) classifies every real turn weighting that has zero integer sum on all full antipodal geodesics. A weighting with constant sum \(K\) on all such geodesics is obtained by adding the uniform weighting \(K/n\) to one of the zero-sum weightings in Theorem 1. This remains a linear statement: restricting the turn weights to \(0/1\) values and imposing the star-triangle parity constraints is a nonlinear restriction not settled by the Fourier classification.

**Remark (the low-dimensional boundary).** The use of at least three auxiliary directions in (9) requires \(n\ge5\). The \(n=4\) incidence rank differs from the formula (12), as recorded in the earlier small-order rank audit. For \(n\ge5\), the present theorem provides an integral strengthening of the binary exchange-homology dimension theorem: no torsion obstruction arises when passing from binary geodesic incidence to the integral lattice of unsigned incidences. It does not imply a small positive integer intersection for every admissible binary coloring, since saturation controls additive relations, not the positivity needed for low-cost cocircuit selection.

**Theorem 5 (direction-potential normal form).** Over any field of characteristic different from two, a turn cochain \(z\) vanishes in sum on every full antipodal-geodesic turn cycle if and only if there exist unique functions
\[
\phi_i:V(F_n)\to\mathbb K,\quad 1\le i\le n,
\tag{14}
\]
and unique constants \(b_i\in\mathbb K\) such that
\[
\boxed{
z(t_{ij}([x]))=\phi_i([x])+\phi_j([x]),\quad
\phi_i([x])+\phi_i([x^i])=2b_i,\quad
\sum_i b_i=0.
}
\tag{15}
\]
For a weighting whose sum on every full antipodal geodesic is a fixed \(K\), the same formula holds with \(\sum_i b_i=K/2\).

*Proof.* In the Fourier decomposition (3)--(4), define
\[
\phi_i([x])=b_{i,\varnothing}+
\sum_{\substack{S\ne\varnothing,\ S\ {\rm even}\\i\in S}}
\chi_S([x])b_{i,S}.
\tag{16}
\]
Each nonconstant Fourier character appearing in \(\phi_i\) changes sign when direction \(i\) is flipped, giving the middle identity in (15); the turn representation (3) gives the first identity, and the trivial Fourier mode gives the final identity. Conversely any function satisfying the middle identity has its nonconstant Fourier coefficients supported on even subsets containing \(i\); the trivial coefficient is \(b_i\). Therefore it has the form (16), and Theorem 1 supplies the zero-sum condition. Uniqueness of the functions \(\phi_i\) follows pointwise from the complete-graph pair equations \(z_{ij}=\phi_i+\phi_j\) because two is invertible and there are at least three directions. For the constant-sum version, subtract the uniform turn cochain \(K/n\) over \(\mathbb R\), or directly telescope as below (the formula \(\sum_i b_i=K/2\) is valid over any field of odd characteristic without dividing by \(n\)).

Indeed, on a geodesic with direction order \(\pi\), the two turns adjacent to the edge in direction \(i=\pi_t\) contribute \(\phi_i([v_{t-1}])+\phi_i([v_t])=2b_i\), where \(v_t=v_{t-1}+e_i\). Every direction occurs once, so the total cyclic turn weight is \(2\sum_i b_i\), proving both necessity and sufficiency of the prescribed sum. \(\square\)

**Corollary 6 (alternate analytic proof of flat-spectrum rigidity).** Suppose \(d\) is the \(0/1\) turn signature of an antipodally odd cube-edge coloring and has the same cyclic turn weight \(K\) on every full antipodal geodesic, with \(n\ge5\). Then \(K=1\).

*Proof.* Theorem 5 supplies a representation \(d(t_{ij}([x]))=\phi_i([x])+\phi_j([x])\). At each folded vertex \([x]\), the turns encode pairwise disagreements between its \(n\) incident cube-edge colors. If at least two incident colors are zero and at least two are one, choose indices \(i,j\) of color zero and \(k,\ell\) of color one. Their turn weights give
\[
d_{ij}+d_{k\ell}-d_{ik}-d_{j\ell}=0+0-1-1=-2,
\]
whereas the same four-term expression in pair potentials \(\phi_i+\phi_j\) is zero. This is a contradiction over the reals. Therefore every cube vertex has at most one incident edge of minority color.

The number of disagreeing turns at each folded vertex is consequently at most \(n-1\). The standard uniform geodesic-turn incidence design yields
\[
K=\mathbb E_C w_d(C)
=\frac{n|\operatorname{supp}(d)|}{|E(H_n)|}
\le\frac{n(n-1)}{\binom n2}=2.
\]
By covering monodromy, every geodesic turn weight is a positive odd integer. Hence the constant \(K\) is one. \(\square\)

The direction-potential representation provides an analytic converse to the discrete pairwise-turn viewpoint: zero-sum geodesic weights are precisely the discrete normal potentials whose variable parts reverse across the associated direction edges. It may be useful for quantitative stability, although the theorem does not establish an unrestricted two-switch bound.

### Two-sector covariance and a Fourier forcing inequality

**Theorem (zero-frequency and full-parity covariance sectors).** Fix \(n\ge5\) and an arbitrary antipodally odd edge coloring. Put \(E=\binom{[n]}2\), and let \(d_{ij}([x])=[c_i(x)\ne c_j(x)]\) denote the binary projective turn signature. Define
\[
W=\{u\in\mathbb R^E:\ \sum_{j\ne i}u_{\{i,j\}}=0\quad(i\in[n])\},
\qquad P_W:\mathbb R^E\longrightarrow W
\]
as the orthogonal projection. Set \(a_{ij}=\mathbb E_{[x]}d_{ij}([x])\). When \(n\) is even, set also
\[
b_{ij}=\mathbb E_{[x]}(-1)^{|x|}d_{ij}([x]).
\tag{TV1}
\]
The latter is well defined on the antipodal vertex quotient. If \(G(C)\) is the number of bichromatic projective turns on a uniformly sampled complete antipodal-geodesic cycle, then
\[
\boxed{\operatorname{Var}_C G(C)\ \ge\
L_n(c):=\frac2{n-1}\|P_Wa\|_2^2+
\mathbf1_{\{n\ \mathrm{even}\}}\frac2{n-3}\|P_Wb\|_2^2.}
\tag{TV2}
\]
The full-parity term is omitted in odd dimensions.

*Proof.* Sample a folded root \([x]\) and direction permutation \(\pi\) uniformly and independently. Every complete projective geodesic cycle admits equally many rooted ordered descriptions. The translation characters of the folded cube are \(\chi_S([x])=(-1)^{\sum_{i\in S}x_i}\), \(|S|\) even. Expand every \(d_{ij}\) in these characters. Orthogonality separates the variance into its zero-frequency directional-order variance and a sum of nonnegative squares for nonzero frequencies.

For the zero frequency, let \(H(\pi)\in\{0,1\}^E\) be the incidence vector of the Hamiltonian cyclic order \(\pi\) on the direction labels. The corresponding cycle turn sum equals \(H(\pi)\cdot a\). Pair counting yields
\[
\mathbb E_\pi H_eH_f=
\begin{cases}
2/(n-1),&e=f,\\
2/((n-1)(n-2)),&|e\cap f|=1,\\
4/((n-1)(n-2)),&e\cap f=\varnothing.
\end{cases}
\tag{TV3}
\]
The orthogonal decomposition of \(\mathbb R^E\) comprises constant pair weights, star-potential weights \(u_{ij}=\alpha_i+\alpha_j\) with \(\sum_i\alpha_i=0\), and \(W\). Constant weights give a constant Hamiltonian cycle sum; the second space gives zero cycle sum. For \(u\in W\), the sums over pairs adjacent to a specified \(e\) and over pairs disjoint from \(e\) are \(-2u_e\) and \(u_e\), respectively. Thus (TV3) acts on \(W\) by the eigenvalue \(2/(n-1)\), and
\[
\operatorname{Var}_\pi(H(\pi)\cdot a)=\frac2{n-1}\|P_Wa\|_2^2.
\tag{TV4}
\]

If \(n\) is even, the full-parity character \(\chi_{[n]}([x])=(-1)^{|x|}\) changes sign after each traversed dimension. Its directional-order coefficient is \(A(\pi)\cdot b\), where \(A(\pi)\) has alternating signs on the \(n\) edges of the Hamiltonian direction cycle and vanishes elsewhere. At each direction the two incident entries of \(A\) have opposite signs, so \(A(\pi)\in W\). Another pair count gives
\[
\mathbb E_\pi A_eA_f=
\begin{cases}
2/(n-1),&e=f,\\
-2/((n-1)(n-2)),&|e\cap f|=1,\\
4/((n-1)(n-2)(n-3)),&e\cap f=\varnothing.
\end{cases}
\tag{TV5}
\]
For adjacent pairs the signs are opposite. The disjoint entry follows from \(\sum_{e\ni i}A_e=0\) and permutation symmetry. Consequently this Gram operator annihilates the star-potential space and acts on \(W\) by
\[
\frac2{n-1}+\frac4{(n-1)(n-2)}
+\frac4{(n-1)(n-2)(n-3)}=\frac2{n-3}.
\]
Therefore \(\mathbb E_\pi(A(\pi)\cdot b)^2=2\|P_Wb\|_2^2/(n-3)\). Adding the two contributions and discarding the other nonnegative Fourier sectors proves (TV2). \(\square\)

**Corollary (dimension-uniform monochromatic-geodesic criterion).** Let \(B_n=2\lfloor(n-1)/2\rfloor+1\), \(\mu=\mathbb EG=2\sum_{i<j}a_{ij}/(n-1)\), and \(p_1=\Pr(G=1)\). Then
\[
\boxed{
p_1\ge \max\left\{0,\
\frac{L_n(c)-(\mu-3)(B_n-\mu)}{2(B_n-1)}
\right\}.
}
\tag{TV6}
\]
In particular, \(L_n(c)>(\mu-3)(B_n-\mu)\) forces a monochromatic full antipodal geodesic.

*Proof.* Since \(G\in\{1,3,\ldots,B_n\}\), the polynomial \((G-3)(B_n-G)\) is nonnegative for \(G\ge3\), and equals \(-2(B_n-1)\) for \(G=1\). Hence
\[
\operatorname{Var}G\le(\mu-3)(B_n-\mu)+2(B_n-1)p_1.
\]
Use (TV2) and the equivalence between a one-turn projective cycle and a monochromatic full antipodal geodesic. \(\square\)

**Balanced-star simplification.** If \(n\) is even and \(c\) is vertex-balanced, then at every \([x]\), \(\sum_{j\ne i}d_{ij}([x])=n/2\). Consequently \(P_Wb=b\) and \(P_Wa\) has entries \(a_{ij}-n/[2(n-1)]\), so
\[
L_n(c)=\frac2{n-1}\sum_{i<j}
\left(a_{ij}-\frac{n}{2(n-1)}\right)^2+
\frac2{n-3}\sum_{i<j}b_{ij}^2.
\tag{TV7}
\]

**Example (two-sector forcing in a balanced six-cube).** With dimensions \(0,\ldots,5\), define
\[
\begin{array}{lll}
c_0=x_2\oplus x_3\oplus x_4,&c_1=1\oplus c_0,&
c_2=x_0\oplus x_1\oplus x_5,\\
c_3=1\oplus c_2,&c_4=x_0,&c_5=1\oplus c_4.
\end{array}
\tag{TV8}
\]
Each rule ignores its own dimension and changes under antipodal inversion; each displayed complementary pair gives one incident edge of each color, so the coloring is legal and vertex-balanced. Its averages \(a_{ij}\) are one on the three designated pairs \(\{0,1\},\{2,3\},\{4,5\}\), and one half elsewhere. Thus \(\mu=18/5\) and \(\|P_Wa\|^2=3/5\). The parity vector \(b\) is supported on the four pairs between \(\{0,1\}\) and \(\{2,3\}\), with entries \(\pm1/2\) and zero direction sums. Thus \(P_Wb=b\), \(\|P_Wb\|^2=1\), and
\[
\boxed{
L_6(c)=\frac{2}{5}\frac35+\frac23=\frac{68}{75}
>\frac{21}{25}=(\mu-3)(5-\mu).
}
\tag{TV9}
\]
Formula (TV6) implies \(p_1\ge1/120\), yielding at least \(16\) one-turn cycles among the \(1920\) full-geodesic projective cycles. The first-moment threshold \(\mu\le3\) does not apply to this coloring. The new certificate detects a global parity correlation through the original edge colors.

The inequality (TV6) supplies a sufficient condition for unrestricted legal colorings. Establishing its strict inequality for all colorings remains open.


**Sharp limitation of the two selected Fourier sectors.** The two terms in (TV2) can vanish simultaneously in every dimension \(n\ge5\), even for legal colorings with many one-turn cycles. Take the cyclic affine reader coloring \(c_i(x)=x_{i+1\bmod n}\). Its turn signature is
\[
d_{ij}([x])=\frac{1-(-1)^{x_{i+1}+x_{j+1}}}{2}.
\]
For all distinct \(i,j\), \(a_{ij}=1/2\), so \(P_Wa=0\). If \(n\) is even and \(n\ge6\), each \(d_{ij}\) has Walsh frequencies only of sizes zero and two, whence \(b=0\) as well. Thus \(L_n(c)=0\). Nevertheless the reader matrix is an invertible cyclic permutation matrix, so for every direction order the root-to-color-word map is a bijection. There are \(2n!\) monochromatic rooted ordered geodesics, or \(n!/2\) projective one-turn cycles. Consequently any universal argument from (TV2) must incorporate further Fourier sectors or a constraint coupling those sectors. This example does not diminish the forcing implication (TV6).


### Root-Walsh positivity and three-character forcing

Let \(n\ge5\), \(H=\mathbb F_2^n/\langle\mathbf1\rangle\), and let \(\pi=(\pi_1,\ldots,\pi_n)\) be a direction order. Let \(G_\pi([x])\) count bichromatic projective turns of its complete geodesic cycle rooted at \([x]\). Write \(\chi_S([x])=(-1)^{\sum_{i\in S}x_i}\) for each even subset \(S\subseteq[n]\) and
\[
\widehat G_\pi(S)=\mathbb E_{[x]\in H}\chi_S([x])G_\pi([x]).
\tag{RP1}
\]
These are original-color data: if \(d_{ij}([x])=[c_i(x)\ne c_j(x)]\), \(\widehat d_{ij}(S)=\mathbb E_{[x]}\chi_S([x])d_{ij}([x])\), \(P_t=\{\pi_1,\ldots,\pi_t\}\), \(P_0=\varnothing\), and \(\pi_0=\pi_n\), then
\[
\widehat G_\pi(S)=\sum_{t=0}^{n-1}(-1)^{|S\cap P_t|}\widehat d_{\pi_t,\pi_{t+1}}(S).
\tag{RP2}
\]

**Theorem (Walsh Gram forcing and quantitative root bound).** Fix any \(q\)-element set \(\mathscr A\) of even subsets. Form the real symmetric matrix
\[
K_{\pi,\mathscr A}(S,R)
=\widehat G_\pi(S\triangle R)-3\mathbf1_{S=R}.
\tag{RP3}
\]
If the original legal coloring has no monochromatic full antipodal geodesic, then \(K_{\pi,\mathscr A}\succeq0\) for every \(\pi,\mathscr A\). For an arbitrary legal coloring, writing \(p_\pi=\Pr_{[x]\in H}(G_\pi([x])=1)\), one has
\[
\boxed{p_\pi\ge\max\{0,-\lambda_{\min}(K_{\pi,\mathscr A})/(2q)\}.}
\tag{RP4}
\]
*Proof.* For real coefficients \(v_S\), character multiplication gives
\[
v^\top K_{\pi,\mathscr A}v=
\mathbb E_{[x]}(G_\pi([x])-3)
\left(\sum_{S\in\mathscr A}v_S\chi_S([x])\right)^2.
\tag{RP5}
\]
In the no-witness case \(G_\pi\ge3\) everywhere, giving positivity. In general \(G_\pi\) is an odd positive integer, so its negative contribution is confined to \(G_\pi=1\), where \(G_\pi-3=-2\). By Cauchy--Schwarz, the squared character sum is at most \(q\sum_Sv_S^2\). Thus (RP5) is at least \(-2qp_\pi\|v\|^2\); the Rayleigh minimum proves (RP4). \(\square\)

**Corollary (cubic compatibility inequality).** For linearly independent even subsets \(S,R\), let \(m=\widehat G_\pi(\varnothing)-3\), \(a=\widehat G_\pi(S)\), \(b=\widehat G_\pi(R)\), \(d=\widehat G_\pi(S\triangle R)\). A witness-free coloring must satisfy
\[
\boxed{m^3-m(a^2+b^2+d^2)+2abd\ge0,}
\tag{RP6}
\]
as well as \(m\ge0\) and \(m^2\ge a^2,b^2,d^2\). These are the principal-minor conditions of the matrix \(\begin{psmallmatrix}m&a&b\\a&m&d\\b&d&m\end{psmallmatrix}\). A negative determinant gives a monochromatic-geodesic certificate computable through (RP2).

**Example (seven-cube undetected by the full second-moment variance bound).** Let \(c_i(x)=x_{i+1\bmod7}\) and \(\pi=(0,1,\ldots,6)\). The rooted color word is \(w=(x_1,x_2,\ldots,x_6,1+x_0)\); hence
\[
G_\pi(x)=\frac72-\frac12\sum_{t=1}^{6}(-1)^{w_t+w_{t+1}}
+\frac12(-1)^{w_7+w_1}.
\tag{RP7}
\]
With \(S=\{1,2\}\), \(R=\{3,4\}\), one obtains
\[
(m,a,b,d)=(1/2,-1/2,-1/2,0),\qquad \det K=-1/8.
\]
The least eigenvalue is \((1-\sqrt2)/2\), so (RP4) certifies \(p_\pi\ge(\sqrt2-1)/12\); enumeration gives \(p_\pi=7/64\). Across all projective supports, the grade distribution is \(\Pr(G=1,3,5,7)=(7,35,21,1)/64\). Consequently \(\mu=7/2\) and \(\operatorname{Var}G=7/4=(\mu-3)(7-\mu)\), so the preceding complete second-moment bound alone cannot force a witness. The three-character inequality detects relative Walsh signs unavailable to the global variance.


**Corollary (four-character XOR closure and conditional-root forcing).** Let \(S,R\) be linearly independent even subsets, and put \(\mu_\pi=\widehat G_\pi(\varnothing)\), \(a=\widehat G_\pi(S)\), \(b=\widehat G_\pi(R)\), \(d=\widehat G_\pi(S\triangle R)\). For \(\epsilon,\eta\in\{\pm1\}\), let \(H_{\epsilon,\eta}=\{[x]\in H:\chi_S([x])=\epsilon,\ \chi_R([x])=\eta\}\). Then
\[
\boxed{\mathbb E[G_\pi\mid H_{\epsilon,\eta}]
=\mu_\pi+\epsilon a+\eta b+\epsilon\eta d.}
\tag{RP8}
\]
If this quantity is less than \(3\) for some choice of signs, the coloring contains a monochromatic full geodesic. More quantitatively,
\[
\boxed{
\Pr(G_\pi=1\mid H_{\epsilon,\eta})
\ge\max\left\{0,\frac{3-\mu_\pi-\epsilon a-\eta b-\epsilon\eta d}{2}\right\}.
}
\tag{RP9}
\]
*Proof.* The indicator of the conditioning coset is \(\frac14(1+\epsilon\chi_S)(1+\eta\chi_R)\), whose expectation is \(1/4\). Expanding its product with \(G_\pi\) proves (RP8). Since every projective turn grade lies in \(\{1,3,5,\ldots\}\), its conditional expectation is at least \(3-2\Pr(G_\pi=1\mid H_{\epsilon,\eta})\), giving (RP9). Equivalently, the four values in (RP8) minus three are the four eigenvalues of the full XOR-closed \(4\times4\) Fourier matrix indexed by \(\{\varnothing,S,R,S\triangle R\}\). \(\square\)

**Example (strict three-character positivity and successful four-character closure).** A reproducible nonlinear vertex-balanced coloring of \(Q_7\), encoded by seven 32-bit hexadecimal exterior-edge tables, is recorded with its complete integer verification in research note `note_be85d81b3c8929b59cfbffef`. For every direction order and every three-character family, all principal shifted-root-Walsh Gram matrices are positive definite. In particular, the minimum of their \(3\times3\) determinants is \(25/512\). Yet for the order \(\pi=(0,1,2,4,6,5,3)\), and \(S=\{0,6\}\), \(R=\{1,3\}\), the unnormalized four-character Gram eigenvalues are \(72,72,-8,96\), with denominator \(64\). The coset \(\chi_S=-1,\chi_R=+1\) consists of the folded roots \(x_0=1\), \(x_1=x_3\) (choose representatives with \(x_6=0\)). Its turn-grade histogram is \(G=1:3,\ G=3:11,\ G=5:2\), so its conditional mean is \(23/8\), agreeing with (RP8). This supplies an original-color witness certificate after all three-character tests fail.

### Highest-order Fourier sectors in odd dimensions

For odd \(n\ge5\), define \(S_z=[n]\setminus\{z\}\), and write
\[
b_{ij}^{(z)}=\mathbb E_{[x]}(-1)^{\sum_{k\in S_z}x_k}
\mathbf1_{\{c_i(x)\ne c_j(x)\}},
\qquad
R^{(z)}_{ij}=b_{ij}^{(z)}-b_{zi}^{(z)}-b_{zj}^{(z)}\quad(i,j\ne z).
\tag{H1}
\]
Let \(P_z\) denote the orthogonal projection onto edge weights of \(K_{n-1}\), on vertex set \([n]\setminus\{z\}\), whose sums at each vertex vanish. Retain \(a_{ij}=\mathbb E_{[x]}d_{ij}([x])\), the projection \(P_W\) onto zero-vertex-sum pair weights on \(K_n\), and \(G(O)=T_c(O)/2\).

**Theorem (co-singleton turn covariance).** For every legal antipodally odd coloring, without further hypotheses,
\[
\boxed{\operatorname{Var}_O G(O)\ge
L_n^{\rm odd}:=\frac2{n-1}\|P_Wa\|^2+
\sum_{z=1}^n\left[
\frac{2}{(n-1)(n-2)}\|R^{(z)}\|^2+
\frac{2(n-3)}{(n-1)(n-4)}\|P_zR^{(z)}\|^2
\right].}
\tag{H2}
\]
With \(\mu=\mathbb E_OG(O)\), the witnessing-support fraction satisfies
\[
\boxed{\Pr_O(G(O)=1)\ge
\max\left\{0,\frac{L_n^{\rm odd}-(\mu-3)(n-\mu)}{2(n-1)}\right\}.}
\tag{H3}
\]

*Proof.* We first establish the needed finite symmetric-group identity. Let \(N\ge4\) be even, let \(R_{ij}\) be arbitrary real pair weights, and sample a uniformly random order \(u=(u_1,\ldots,u_N)\). Put \(A_R(u)=\sum_{j=1}^{N-1}(-1)^jR_{u_j,u_{j+1}}\). If \(Z_e(u)\) is the signed indicator of consecutive pair \(e\), then
\[
\mathbb EZ_eZ_f=
\begin{cases}
2/N,&e=f,\\
-2/[N(N-1)],&|e\cap f|=1,\\
4/[N(N-1)(N-3)],&e\cap f=\varnothing.
\end{cases}
\tag{H4}
\]
Indeed, a specified pair is consecutive with probability \(2/N\); two pairs sharing a label are successive, with opposite signs, with probability \(2/[N(N-1)]\). The disjoint case follows by permutation symmetry, \(\sum_eZ_e=-1\), and \(\mathbb EZ_e=-2/[N(N-1)]\).

For pair weights \(R\) with all vertex sums zero, the sums over pairs adjacent to and disjoint from a fixed pair \(e\) are \(-2R_e\) and \(R_e\). Hence (H4) acts on this subspace by
\[
\lambda_{\rm cycle}=\frac{2(N^2-2N-1)}{N(N-1)(N-3)}.
\]
On pair-additive weights \(R_{ij}=v_i+v_j\), the alternating sum telescopes to \(-v_{u_1}-v_{u_N}\). On constant and zero-sum vertex potentials its eigenvalue is \(2/[N(N-1)]\). Pair-additive and zero-vertex-sum weights form an orthogonal decomposition, so
\[
\boxed{\mathbb E_uA_R(u)^2=
\frac2{N(N-1)}\|R\|^2+
\frac{2(N-2)}{N(N-3)}\|P_{W_N}R\|^2.}
\tag{H5}
\]

Now sample a folded cube root and a direction order independently and uniformly. The resulting projective support is uniform. Fourier expansion over even Walsh characters gives the variance decomposition into the zero-frequency directional-order variance, plus the mean squares of each nonzero Fourier frequency. The former equals \(2\|P_Wa\|^2/(n-1)\).

At frequency \(S_z\), cyclically rotate the direction order to begin with \(z\). This preserves the squared Fourier coefficient. Since the character is unchanged across direction \(z\) and changes sign across every other direction, if \(u\) is the uniformly random order of the remaining \(N=n-1\) directions, the Fourier coefficient becomes
\[
b_{z,u_1}^{(z)}+b_{z,u_N}^{(z)}
+\sum_{j=1}^{N-1}(-1)^jb_{u_j,u_{j+1}}^{(z)}
=\sum_{j=1}^{N-1}(-1)^jR^{(z)}_{u_j,u_{j+1}}.
\tag{H6}
\]
The equality uses
\(\sum_{j=1}^{N-1}(-1)^j(v_{u_j}+v_{u_{j+1}})=-v_{u_1}-v_{u_N}\).
The \(n\) frequencies \(S_z\) are distinct and nonempty. Apply (H5) to each and retain their nonnegative contributions to obtain (H2).

Finally, \(G\in\{1,3,\ldots,n\}\) and \((G-3)(n-G)\ge-2(n-1)\mathbf1_{\{G=1\}}\). Therefore
\(\operatorname{Var}G\le(\mu-3)(n-\mu)+2(n-1)\Pr(G=1)\),
which together with (H2) proves (H3). \(\square\)

**Projection evaluation.** For pair weights \(R\) on \(K_N\), put \(t_i=\sum_{j\ne i}R_{ij}\). The incidence Gram \((N-2)I+J\) gives
\[
\|P_{W_N}R\|^2=\sum_{i<j}R_{ij}^2-
\frac{\sum_i t_i^2}{N-2}+
\frac{(\sum_i t_i)^2}{(N-2)(2N-2)}.
\tag{H7}
\]

**Seven-dimensional forcing example.** Over \(\mathbb F_2\), index directions \(0,\ldots,6\) and set
\[
\begin{aligned}
c_0&=1+x_1+x_5+x_6,&c_1&=1+x_0+x_3+x_4,\\
c_2&=1+x_4,&c_3&=1+x_1+x_5+x_6,\\
c_4&=x_1+x_2+x_3+x_5+x_6,&c_5&=1+x_4,\\
c_6&=x_0+x_2+x_4.
\end{aligned}
\tag{H8}
\]
Each rule ignores its own bit and changes under global complementation. The mean grade is \(\mu=19/6\). The zero-frequency energy is \(11/90\), while the co-singleton contributions for \(z=0,2,3\) are respectively \(2/15,47/180,43/180\), with all remaining contributions zero. Thus
\[
L_7^{\rm odd}=\frac{34}{45}>\frac{23}{36}=(\mu-3)(7-\mu).
\tag{H9}
\]
The theorem certifies a witnessing-support fraction at least \(7/720\), or \(224\) among the \(23040\) projective supports. The earlier zero-frequency bound \(11/90\) does not force a witness in this coloring. Enumeration gives the histogram \(G=1:4200,\ G=3:13000,\ G=5:5560,\ G=7:280\), whose variance is \(67/36\).

A standard-library rational verifier checks (H5) by enumeration for \(N=4,6,8\), validates all edge-color conditions in (H8), and enumerates the seven-cube support histogram. It is preserved at \`nori/certificates/nori_odd_topmode_verifier.py\` (GitHub commit \`b188ad321996e021b7c1f71d2531d7efa92ac571\`).
