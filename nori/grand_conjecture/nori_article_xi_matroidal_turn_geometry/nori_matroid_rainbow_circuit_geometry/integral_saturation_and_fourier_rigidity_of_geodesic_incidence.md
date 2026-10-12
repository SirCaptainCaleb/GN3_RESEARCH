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

For \(S=\varnothing\), the same swap calculation gives (10), but \(F_\varnothing(\pi)=2\sum_i b_i\). Since two is invertible, the condition is \(\sum_i b_i=0\), a space of dimension \(n-1\). These classifications prove (3)--(4). Finally each coordinate \(i\) belongs to \(2^{n-2}\) even subsets, yielding \(\sum_{S\ {\rm even}}|S|=n2^{n-2}\), proving (5). \(\square\)

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

**Theorem 5 (coordinate-potential normal form).** Over any field of characteristic different from two, a turn cochain \(z\) vanishes in sum on every full antipodal-geodesic turn cycle if and only if there exist unique functions
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
Each nonconstant Fourier character appearing in \(\phi_i\) changes sign when coordinate \(i\) is flipped, giving the middle identity in (15); the turn representation (3) gives the first identity, and the trivial Fourier mode gives the final identity. Conversely any function satisfying the middle identity has its nonconstant Fourier coefficients supported on even subsets containing \(i\); the trivial coefficient is \(b_i\). Therefore it has the form (16), and Theorem 1 supplies the zero-sum condition. Uniqueness of the functions \(\phi_i\) follows pointwise from the complete-graph pair equations \(z_{ij}=\phi_i+\phi_j\) because two is invertible and there are at least three directions. For the constant-sum version, subtract the uniform turn cochain \(K/n\) over \(\mathbb R\), or directly telescope as below (the formula \(\sum_i b_i=K/2\) is valid over any field of odd characteristic without dividing by \(n\)).

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

The coordinate-potential representation provides an analytic converse to the discrete pairwise-turn viewpoint: zero-sum geodesic weights are precisely the discrete normal potentials whose variable parts reverse across the associated coordinate edges. It may be useful for quantitative stability, although the theorem does not establish an unrestricted two-switch bound.
