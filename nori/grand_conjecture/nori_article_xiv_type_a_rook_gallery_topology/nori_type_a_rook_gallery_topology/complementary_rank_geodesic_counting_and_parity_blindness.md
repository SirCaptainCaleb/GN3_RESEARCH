# Complementary-rank geodesic counting and parity blindness

# Complementary-rank geodesic counting and parity blindness

Let \(D=[n]\), \(n\ge2\), and let \(c\) be an arbitrary binary coloring of **undirected** cube edges satisfying \(c(\bar e)=1-c(e)\). For \(x\in\mathbb F_2^n\), \(S\subseteq D\), and \(t\in\mathbb F_2\), let \(A_t(x,S)\) be the number of monochromatic color-\(t\) geodesics starting at \(x\), using precisely the dimensions in \(S\) (each once) and ending at \(x\oplus\mathbf1_S\). Put \(A_t(x,\varnothing)=1\). Paths are counted as ordered dimension sequences.

The recursion is
\[
A_t(x,S)=\sum_{i\in S}\mathbf1_{\{c(\{x,x\oplus e_i\})=t\}}\,
 A_t(x\oplus e_i,S\setminus\{i\})\quad(S\ne\varnothing).
\tag{1}
\]
Reversing a path and then applying the cube antipode gives a color-complementing bijection, and hence
\[
\boxed{A_t(x,S)=A_{1-t}(x\oplus\mathbf1_{D\setminus S},S).}
\tag{2}
\]
In particular \(A_0(x,D)=A_1(x,D)\) at **every** prescribed root.

**Theorem 1 (complementary-rank convolution identity).** For every root \(x\), color \(t\), and rank \(0\le k\le n\),
\[
\boxed{\quad
\sum_{\substack{S\subseteq D\\|S|=k}}
 A_t(x,S)\,A_{1-t}(x,D\setminus S)
 =
 A_t(x,D).
\quad}
\tag{3}
\]
Consequently the sum is independent of \(k\), and the path-existence statement \(A_t(x,D)>0\) is equivalent to the existence of complementary subsets \(S,D\setminus S\) for which both factors in some summand are positive.

*Proof.* Given a color-\(t\) full geodesic \(P\) from \(x\) to \(\bar x\), cut it after the \(k\)-th move. Let \(S\) be the set of dimensions used by its prefix. This prefix is a color-\(t\) geodesic counted by \(A_t(x,S)\). Its suffix, running from \(x\oplus\mathbf1_S\) to \(\bar x\), is color \(t\) with dimension set \(D\setminus S\). Reverse the suffix and take its antipodal image: the result is a color-\((1-t)\) geodesic from \(x\) to \(x\oplus\mathbf1_{D\setminus S}\), counted by \(A_{1-t}(x,D\setminus S)\). Conversely, any such pair of partial geodesics gives a full color-\(t\) geodesic by antipodally reversing the second one and appending it to the first. The dimension sets of the two parts are disjoint, so the concatenation uses every dimension once. These constructions are inverse at the prescribed cut rank \(k\). Thus (3) counts full color-\(t\) geodesics, each once. \(\square\)

**Corollary 2 (layer-by-layer separation under a hypothetical NORI1 counterexample).** If there is no monochromatic full antipodal geodesic at any root, then for every \(x,t,S\),
\[
\boxed{A_t(x,S)\,A_{1-t}(x,D\setminus S)=0.}
\tag{4}
\]
Conversely, (4) for all roots implies the absence of such a geodesic. Thus the proposed dimension-sensitive analogue of Wu–Yang's disjoint component-pair labeling is a **sequence of complementary-support separations at every Boolean rank**, not one equivalence-class partition. Moreover the local update (1) is a rank-increasing implication rather than equality along monochromatic edges. This is where the component-based rook-labeling reduction cannot simply be copied.

**Theorem 3 (parity blindness of the simple arm pairing).** In the square-zero polynomial algebra
\[
\mathcal A=\mathbb Z[z_1,\ldots,z_n]/(z_1^2,\ldots,z_n^2),
\qquad
P_t^x(\mathbf z)=\sum_{S\subseteq D}A_t(x,S)\prod_{i\in S}z_i,
\tag{5}
\]
the top-degree coefficient satisfies
\[
\boxed{[z_D]P_t^xP_{1-t}^x=(n+1)A_t(x,D).}
\tag{6}
\]
When \(n\) is odd, this coefficient vanishes modulo two for every coloring, even when monochromatic full geodesics exist. More strongly, for **every even** \(n=2m\ge4\), there exists an antipodally odd coloring with monochromatic full geodesics but
\[
A_0(x,D)\equiv A_1(x,D)\equiv0\pmod2
\quad\text{for every root }x;
\tag{7}
\]
in particular all complementary-rank coefficients in (3) also vanish modulo two for all roots and all ranks.

*Proof.* The square-zero relations imply that the coefficient of \(z_D\) in a product comes only from disjoint dimension sets whose union is \(D\). Summing (3) over all ranks gives (6). Odd \(n\) makes \(n+1\) even.

For the even-dimensional example, define the color of a dimension-\(i\) undirected edge with endpoint \(y\) by
\[
c_i(y)=\sum_{j\ne i}y_j\pmod2.
\tag{8}
\]
This is independent of the choice of endpoint because it ignores bit \(i\). Since \(n-1\) is odd, complementing every bit flips the color. Along a full geodesic with root \(x\) and dimension order \(\pi\), the \(k\)-th edge color is
\[
w_k=|x|+x_{\pi_k}+(k-1)\pmod2.
\tag{9}
\]
Thus \(w_k=w_{k+1}\) if and only if \(x_{\pi_k}\ne x_{\pi_{k+1}}\). A monochromatic full geodesic exists from \(x\) if and only if the root bits \(x_{\pi_1},\ldots,x_{\pi_n}\) alternate. For \(n=2m\), this is possible if and only if \(|x|=m\). At such a root, there are \(2(m!)^2\) alternating permutations: two alternating binary patterns, with \(m!\) assignments of dimensions of each bit. The color-complementing reversal-antipode bijection (2) at \(S=D\) splits them evenly between the two colors, giving
\[
\boxed{A_0(x,D)=A_1(x,D)=(m!)^2\ \text{when }|x|=m,}
\tag{10}
\]
and both counts zero at every other root. Since \(m\ge2\), all counts in (10) are even, proving (7). Equation (3) then yields the asserted parity vanishing at every individual rank. \(\square\)

**Implication for adapting Wu–Yang (arXiv:2607.19276, Sections 2 and 5).** The source Freudenthal simplices already describe dimension-simple monotone paths. Wu–Yang's proof obtains its ordinary rook labeling by passing through unrestricted connected components, which forgets whether the connecting monochromatic paths reuse dimensions. Equations (1)–(4) offer a rank-sensitive replacement for the component separation, and (3) supplies a cut-compatible counting law. However, the counterexample (8)–(10) shows that reducing these nonnegative integer path counts modulo two can annihilate every full-geodesic witness at every root. Therefore a modified chain argument cannot use just the mod-two scalar coefficient of the symmetric two-arm enumerator as its existence detector. It must retain dimension-set supports, asymmetric path order data, or finer geometric information before taking a mod-two obstruction.

**Relation to companion work.** The common-terminal two-arm polynomial for boundary tournaments in Article XI also has a symmetric-arm characteristic-two cancellation. Here the rank-resolved convolution (3) and the even-dimensional family (8) are specific to antipodally odd *edge* colorings and use their reversal-plus-antipode bijection. This makes the obstruction to direct binary counting visible on both sides of the intended unification. Neither theorem proves the NORI1 existence conjecture; it identifies a faithful dimension-simple calculation and a limitation of its parity compression.

## Signed path-orbit incidence and incompatible monochromatic geodesics

Let \(c\) range over legal antipodally odd binary edge colorings of \(Q_n\). Choose one reference edge in each of the \(m=n2^{n-2}\) antipodal orbits of undirected edges, so each coloring is specified by independent binary bits \(z_o\). A full antipodal geodesic \(P\) uses one orbit per direction. Its direction-\(i\) edge in orbit \(o\) has color \(z_o\oplus s_{P,o}\), where \(s_{P,o}\) records which member of that orbit occurs.

For any finite nonempty family \(\mathcal P\) of full geodesics, construct a signed bipartite incidence graph \(B(\mathcal P)\) with left vertices the paths \(P\), right vertices the edge orbits \(o\) they use, and edge label \(s_{P,o}\). Write \(v\) for its number of orbit vertices and \(k\) for its number of connected components.

**Theorem (signed-incidence realization and probability).** The paths in \(\mathcal P\) can all be monochromatic (not necessarily in the same color) in a legal coloring if and only if the binary sum of incidence labels is zero around every cycle of \(B(\mathcal P)\). Moreover,
\[
\boxed{
\mathbb P_c[\text{all }P\in\mathcal P\text{ monochromatic}]
=\begin{cases}
2^{k-v},&\text{all incidence cycles have even label sum},\\
0,&\text{otherwise}.
\end{cases}}\tag{SI1}
\]
In the positive case the satisfying colorings form an affine subspace of \(\mathbb F_2^m\) of dimension \(m-v+k\).

*Proof.* Introduce an unknown color \(t_P\) for each selected path. Its monochromaticity is equivalent to
\[
z_o\oplus t_P=s_{P,o}\quad\text{for every incidence }P-o.
\]
Summing these equations around an incidence cycle yields the stated necessary condition. Conversely, in each connected component of the incidence graph choose one variable freely, then propagate the equations along a spanning tree. The equations on remaining edges hold precisely when all fundamental cycles have even label sum. Thus one binary degree of freedom survives per connected component, and the \(m-v\) unused orbit-color bits are unconstrained. There are \(2^{m-v+k}\) satisfying colorings among the \(2^m\) legal colorings, proving (SI1). \(\square\)

**Corollary (two-path overlap law).** Let two full geodesics \(P,Q\) have \(t\) shared antipodal edge-orbits. If \(t\le1\), their monochromaticity events are independent, with joint probability \(2^{2-2n}\). If \(t\ge2\), write \(d_o=s_{P,o}\oplus s_{Q,o}\) at each common orbit. If the \(d_o\) disagree then the joint probability is zero; if they agree then it equals \(2^{t+1-2n}\). Hence sharing at least two orbits creates either positive correlation or incompatibility. This follows directly by applying (SI1) to the union of two star incidence graphs.

**Theorem (frustrated triple of full geodesics in every dimension).** For any \(n\ge3\), put \(E=(3,4,\ldots,n-1)\) and consider the three full geodesics from the zero vertex with direction orders
\[
\boxed{P=(0,1,2,E),\qquad Q=(0,2,E,1),\qquad R=(1,0,2,E).}\tag{SI2}
\]
Any two of these can be monochromatic simultaneously in some legal coloring, but no legal coloring can make all three monochromatic.

*Proof.* Paths \(P,Q\) use the same first edge, forcing equal monochromatic colors if both succeed. Paths \(P,R\) reach \(e_0\oplus e_1\) after their first two moves, and share the remaining edges (directions \(2,E\)), also forcing equal colors. The final direction-one edge of \(Q\), from \(\mathbf1\oplus e_1\) to \(\mathbf1\), is antipodal to the first edge of \(R\), from \(0\) to \(e_1\). It forces opposite colors. These three requirements contradict one another.

For pairwise realizability, \(P,Q\) have just one common edge orbit (their first edge), and \(Q,R\) have just one (the opposite end edges). Their respective incidence graphs have no cycles. Paths \(P,R\) share all the same edges from direction two onward, and have no further common edge orbit; every resulting incidence cycle has even label sum. Hence each pair is individually realizable by the preceding theorem. \(\square\)

The pairwise probabilities in (SI2) are
\[
\boxed{
\mathbb P(M_PM_Q=1)=2^{2-2n},\quad
\mathbb P(M_PM_R=1)=2^{-n-1},\quad
\mathbb P(M_QM_R=1)=2^{2-2n},\quad
\mathbb P(M_PM_QM_R=1)=0.}\tag{SI3}
\]
The orbit incidence counts were independently verified by a signed disjoint-set algorithm for every \(3\le n\le10\).

This supplies a dimension-uniform signed-graphic description of joint full-geodesic events and a minimal three-path failure of pairwise compatibility. It does not prove unrestricted NORI1, which asks for at least one monochromatic path in each legal coloring.
