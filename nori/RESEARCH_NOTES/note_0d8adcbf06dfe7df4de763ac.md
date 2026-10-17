# Affine profile surjectivity from forest-supported cokernel exchanges, with unbounded corank

- Stable ID: note_0d8adcbf06dfe7df4de763ac
- Author: unspecified; session provenance retained
- Primary home: subsection:tournament_interleaving_and_functional_dependency_geodesics
- Labels: NORI1, affine, cokernel, forest, acyclic-orientation, dimension-uniform
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11123_1
- Updated session: session_nori_r11123_1
- Disposition: none
- Successor: none

## Related references

- subsection:tournament_interleaving_and_functional_dependency_geodesics
- note:note_b7650be8a633481e699bfc0f

## Research note

## Acyclic-orientation model for affine geodesic profiles

Let \(c_i(x)=\alpha_i+(Ax)_i\) be an affine binary edge coloring of \(Q_n\), with \(A\in M_n(\mathbb F_2)\), \(A_{ii}=0\), \(A\mathbf1=\mathbf1\). Thus the coloring is invariant on each undirected direction edge and is antipodally odd. Put
\[
V=\mathbb F_2^n/\operatorname{im}A,\qquad v_i=[e_i]\in V,\qquad
\gamma_{ij}=A_{ij}v_i+A_{ji}v_j\in V\quad(i\ne j).
\tag{FO1}
\]
Let \(H_A\) be the undirected graph on \([n]\) with edges \(ij\) for which \(\gamma_{ij}\ne0\). For a direction order \(\pi\), define \((r_\pi)_i=\sum_{j\text{ before }i}A_{ij}\), so that the direction-indexed color profile from root \(x\) is
\[
w(x,\pi)=\alpha+Ax+r_\pi.
\tag{FO2}
\]

**Theorem 1 (acyclic-orientation cokernel model).** Fix a reference total order \(\pi_0\) and orient every edge of \(H_A\) from earlier to later under \(\pi_0\). If \(O\) is any acyclic orientation of \(H_A\), let \(I(O)\) be its set of edges oriented opposite to this reference orientation. Then the attainable color-profile set is
\[
\boxed{\mathcal W(c)=
\bigcup_{O\text{ acyclic}}
\left(\alpha+r_{\pi_0}
+\sum_{ij\in I(O)}(A_{ij}e_i+A_{ji}e_j)
+\operatorname{im}A\right).}
\tag{FO3}
\]
In particular its number of profiles depends on \(A\), not on the affine constant \(\alpha\). The unrestricted affine profile-surjectivity question is equivalent to whether the images in \(V\) of the inversion-label sums of acyclic orientations of \(H_A\) exhaust \(V\).

*Proof.* Moving adjacent directions \(i,j\) past one another changes \(r_\pi\) by \(A_{ij}e_i+A_{ji}e_j\). For arbitrary orders \(\pi,\pi_0\), one can sort \(\pi\) into \(\pi_0\) by swapping each reversed pair once (a reduced word for their relative permutation). Thus \([r_\pi]+[r_{\pi_0}]\) is the sum of \(\gamma_{ij}\) over the pairs whose relative order differs. The pairs outside \(H_A\) contribute zero modulo \(\operatorname{im}A\). Restricting a total order to edges of \(H_A\) always gives an acyclic orientation; conversely every acyclic orientation of a finite graph has a total-order extension. Therefore the image of all \(r_\pi\) modulo \(\operatorname{im}A\) is precisely the finite set in (FO3). Equation (FO2) gives the asserted union of cosets. \(\square\)

**Lemma 2 (automatic span of all exchange labels).** Without any acyclicity hypothesis,
\[
\boxed{\sum_{j\ne i}\gamma_{ij}=v_i,\qquad
\operatorname{span}_{\mathbb F_2}\{\gamma_{ij}:ij\in E(H_A)\}=V.}
\tag{FO4}
\]
*Proof.* Since \(\sum_{j\ne i}A_{ij}=1\) and \(\sum_{j\ne i}A_{ji}v_j=[Ae_i]=0\), the first identity follows. The vectors \(v_i\) span \(V\), hence so do the exchange labels. \(\square\)

**Theorem 3 (forest criterion and polynomial-time construction).** If \(H_A\) is a forest, then
\[
\boxed{\mathcal W(c)=\mathbb F_2^n}
\tag{FO5}
\]
for every affine constant \(\alpha\). Given any desired profile \(w\), a full antipodal geodesic with profile \(w\) can be constructed by Gaussian elimination and topological sorting in polynomial time.

*Proof.* A forest has no directed cycles under any orientation, so every subset \(T\subseteq E(H_A)\) can be realized as the reversed-edge set \(I(O)\) of some acyclic orientation \(O\). Thus (FO3) realizes every subset sum of \(\gamma_{ij}\). By (FO4) those sums cover \(V\), giving (FO5). Constructively, solve in \(V\) for coefficients \(t_{ij}\) such that \(\sum t_{ij}\gamma_{ij}=[w+\alpha+r_{\pi_0}]\). Reverse the reference orientation on the selected forest edges and topologically sort the resulting directed forest, obtaining an order \(\pi\). Equations (FO3)-(FO4) then ensure \(w+\alpha+r_\pi\in\operatorname{im}A\), so solve \(Ax=w+\alpha+r_\pi\) by Gaussian elimination. Equation (FO2) proves that the resulting geodesic has profile \(w\). \(\square\)

**Corollary 4 (odd-degree forest dependency graphs).** If \(T\) is any forest in which every vertex has odd degree, let \(A\) be its binary adjacency matrix. The legal antipodally odd coloring
\[
c_i(x)=\alpha_i+\sum_{j:\{i,j\}\in E(T)}x_j
\]
has complete direction-indexed color-profile support, for every \(\alpha\). Indeed \(A_{ii}=0\), \(A\mathbf1=\mathbf1\), and \(\gamma_{ij}=0\) outside \(E(T)\); hence \(H_A\subseteq T\).

**Corollary 5 (simultaneously unbounded cokernel and nonunary dependence).** For any odd \(h\ge3\), let \(T_h\) have vertices consisting of a hub \(o\), branch vertices \(b_1,\ldots,b_h\), and two private leaves \(a_j,d_j\) for each branch. Its edges are \(ob_j,b_ja_j,b_jd_j\). Then \(n=3h+1\), every vertex has odd degree, the binary adjacency matrix \(A_h\) has rank \(2h\), and its cokernel has dimension \(h+1\). The hub and all \(h\) branch vertices have at least three readers, so the number of nonunary direction rules is \(h+1\). By Corollary 4 every direction-indexed profile occurs, even though both the cokernel dimension and number of nonunary rows diverge with \(n\).

*Rank proof.* Each leaf column is \(e_{b_j}\), so the leaf columns span the \(h\)-dimensional branch subspace. The column of branch vertex \(b_j\) is \(e_o+e_{a_j}+e_{d_j}\). These \(h\) columns are independent modulo the branch subspace, because their disjoint private-leaf supports are nonzero. The hub column is \(\sum_{j=1}^h e_{b_j}\) and is already in the branch subspace. Hence \(\operatorname{rank}A_h=2h\). The number of branch readers is three; the hub degree \(h\) is odd, so all row sums equal one. \(\square\)

**Audit.** A Gaussian-elimination and topological-sort implementation constructed geodesics with prescribed independently randomized color profiles in the \(T_h\) families for \(h=3,5,7,9\) (dimensions \(10,16,22,28\)); 200 target profiles were tested per instance. The computed ranks were \(6,10,14,18\), respectively, agreeing with \(2h\). Separately, all 32,768 legal affine five-direction dependency matrices were checked for full profile support, as were 10,000 sampled legal affine six-direction matrices. These finite checks support, but do not establish, surjectivity for arbitrary affine matrices; only the forest theorem and its corollaries are proved.

*Scope.* The acyclic-orientation description (FO3) is valid for all legal affine colorings, not just forests. In general a cyclic exchange-support graph need not admit arbitrary choices of inverted edges; the full affine profile-surjectivity conjecture remains open beyond established classes. The forest theorem does not assert the unrestricted nonlinear NORI1 conjecture.
