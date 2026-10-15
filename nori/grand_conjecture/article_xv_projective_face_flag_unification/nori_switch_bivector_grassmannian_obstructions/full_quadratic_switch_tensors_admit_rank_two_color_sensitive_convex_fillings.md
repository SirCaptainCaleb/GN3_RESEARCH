# Full quadratic switch tensors admit rank-two color-sensitive convex fillings

### Rank-two convex carriers for the complete quadratic switch tensor

Let \(n\ge6\) and let \(b(x,y,z)\in\mathbb F_2\) be an unrestricted reversal-odd coloring of ordered distinct triples: \(b(z,y,x)=1-b(x,y,z)\). A Hamilton permutation \(\pi\) has color word \(b(\pi_1,\pi_2,\pi_3),\ldots,b(\pi_{n-2},\pi_{n-1},\pi_n)\). Let \(S_\pi\subseteq\{2,\ldots,n-2\}\) denote the prefix ranks at its switches. When \(|S_\pi|\ge2\), define the complete quadratic bivector
\[
\mathcal B(\pi)=\sum_{p<q,\ p,q\in S_\pi}Z_p(\pi)\wedge Z_q(\pi).
\]

**Theorem 1 (color-sensitive rank-two convex filling).** Let \(D\) be any rank-two dual type-A Coxeter cell (commuting square or braid hexagon), and suppose every Hamilton flag in \(D\) has at least two switches. Then there exists a decomposable covector \(\omega=u\wedge v\in\Lambda^2W^*\) such that
\[
\boxed{\omega(\mathcal B(\pi))<0\quad\text{for every flag }\pi\in D.}\tag{1}
\]
Consequently the convex hull of the *full quadratic* bivectors on \(D\) avoids zero, and their normalized positive affine combinations give a continuous filling over \(D\). This strengthens the rank-two convex-carrier result previously proved for first/last switch wedges.

*Proof.* A rank-two Coxeter cell corresponds to an ordered partition of the symbols with either one block of size three (a braid hexagon) or two blocks of size two (a commuting square).

If both terminal blocks have sizes at most two, put \(u\) equal to the average of the entry-extracting covectors on the first block and \(v\) equal to the average on the last block. Every permitted switch prefix rank \(p\) is at least two and at most \(n-2\). Hence each prefix contains the entire first block and none of the last block, and a direct two-by-two determinant gives
\[
(u\wedge v)(Z_p\wedge Z_q)=-\frac{q-p}{n}<0
\quad(p<q).
\tag{2}
\]
Every \(\mathcal B(\pi)\) is a nonempty positive sum of these wedges, so the same separator works for all flags.

The only remaining cases are a braid cell with three symbols in its first block or three symbols in its last block. Reversal reduces to the first case. Write the first block as \(\{a,b,c\}\), with six orders \((x,y,t,d_4,\ldots,d_n)\), where \(t\) is the third of the three variable symbols. Set \(z=d_n\), and choose \(u=\lambda_a e_a^*+\lambda_b e_b^*+\lambda_c e_c^*\), \(v=e_z^*\), with all \(\lambda_t>0\) and \(\sum\lambda_t=1\). For any prefix pair \(2\le p<q\le n-2\),
\[
n(u\wedge v)(Z_p\wedge Z_q)=
\begin{cases}
q\lambda_t-(q-2),&p=2,\\
-(q-p),&p\ge3.
\end{cases}
\tag{3}
\]
When \(2\notin S_\pi\), formula (3) makes \(\omega(\mathcal B(\pi))<0\). Otherwise put \(R_\pi=S_\pi\setminus\{2\}\), which is nonempty. Then
\[
n\omega(\mathcal B(\pi))
=\lambda_t A_\pi-D_\pi,
\quad
A_\pi=\sum_{q\in R_\pi}q,\quad
D_\pi=\sum_{q\in R_\pi}(q-2)+
\sum_{p<q,\ p,q\in R_\pi}(q-p).
\tag{4}
\]
Every ratio \(\theta_\pi=D_\pi/A_\pi\) is at least \(1/3\), and equality occurs only when \(S_\pi=\{2,3\}\); this follows from \((q-2)/q\ge1/3\) for \(q\ge3\), with strictness for \(q>3\), and from positivity of the second sum. Thus it suffices to choose positive \(\lambda_t\) summing to one with
\[
\lambda_t<\theta_t:=\min_{\pi:\,\pi_3=t,\ 2\in S_\pi}\theta_\pi,
\tag{5}
\]
where an empty minimum means \(+\infty\).

We claim at least one of the three \(\theta_t\) is strictly greater than \(1/3\). Suppose not. For each last first-block symbol \(t\), one of the two orders ending in \(t\) has \(S_\pi=\{2,3\}\). In such an order all color comparisons after its third triple window are equalities. The third window has color \(b(t,d_4,d_5)\), whereas the fourth is the common suffix color \(b(d_4,d_5,d_6)=c_0\). Therefore \(b(t,d_4,d_5)=c_0\) for that choice of \(t\), and it has this value for both initial orders ending in \(t\). The other initial order ending in the same \(t\) has no switches after rank three, by the same suffix calculation; since it is also bad, it must switch at both ranks two and three. Hence its first triple has color \(c_0\), just as in the selected order. Repeating for each \(t\in\{a,b,c\}\) shows that all six permutations of the three-symbol initial block have color \(c_0\), contradicting reversal oddness. This proves the claim.

After replacing infinite \(\theta_t\) by the finite upper bound one, the three positive bounds sum to more than one. One can therefore choose positive \(\lambda_t\) with sum one and each strictly below \(\theta_t\). Equations (4)-(5) prove (1) on all six flags. The final-terminal braid follows by reversing all orders. QED.

**Corollary 2 (full-bivector two-skeleton map).** If an unrestricted reversal-odd boundary coloring had no Hamilton order with at most one switch, its complete quadratic switch-bivector labels would extend, by positive affine interpolation, equivariantly over every rank-two cell of the dual type-A Coxeter sphere into the unit sphere of \(\Lambda^2W\). On each cell a color-sensitive decomposable covector strictly separates the entire interpolated image from zero. Opposite cells are filled by the reversed negative images.

**Sharpness with respect to cell dimension.** The tetrahedral parity rank-three construction published earlier in this Article has all 24 flags bad, but two flags with ordered initial pairs complementary within the first four symbols and the same parity bit zero. Both have switch set \(\{2,4\}\), so the *full quadratic* bivectors at those flags equal the extreme bivectors \(Z_2\wedge Z_4\) and its negative. Therefore zero lies in the convex hull already on a rank-three cell. No corresponding universal convex filling assertion holds in rank three.

**Scope.** The positive rank-two result uses the unrestricted reversal-odd triple constraint only in the terminal braid case and keeps all intermediate switch-pair terms. It does not extend convex fillings over rank-three residues, nor does it resolve the one-switch conjecture.
