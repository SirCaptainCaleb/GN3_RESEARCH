# Universal variable prefix degree on two-block cells

### Unit degree survives arbitrary variation of the two switch ranks

Let \(P_m\) denote the centered permutahedron of full orders on \(m\) symbols, and let \(Z_k(\pi)=\sum_{j\le k}e_{\pi_j}-(k/m)\mathbf1\) for \(1\le k<m\).

**Lemma 1 (variable-prefix sphere degree).** For every function \(k:S_m\to\{1,\ldots,m-1\}\), the boundary vertex labeling \(\pi\mapsto Z_{k(\pi)}(\pi)\) has a zero-free simplicial affine extension over \(\partial P_m\). Its radial normalization has degree \(\pm1\), independently of the function \(k\).

*Proof.* On any proper face of \(P_m\), all orders begin with the elements of a fixed nonempty proper first block \(S\), in some order. For every \(1\le k<m\) and every order on this face,
\[
\sum_{i\in S}(Z_k(\pi))_i=\min(k,|S|)-\frac{k|S|}{m}>0.
\tag{1}
\]
Thus convex hulls of the labels of any boundary face avoid zero. Moreover the straight-line homotopy at vertices from the variable labels to the centered permutahedron vertex vectors stays in this same strict halfspace on each face. The latter radial boundary map has degree one up to orientation. QED.

**Theorem 2 (variable-rank straddling unit degree).** Let \(V=A\sqcup B\), with \(a=|A|\ge2\), \(b=|B|\ge2\), and let \(D=P_a\times P_b\) be the top dual Coxeter cell of Hamilton orders listing \(A\) before \(B\). For each \(\pi\in D^{(0)}\), independently select integers
\[
1\le k(\pi)\le a-1,\qquad 1\le\ell(\pi)\le b-1.
\]
Put \(T=\sum_{i\in A}e_i-(a/(a+b))\mathbf1\), and let
\[
F(\pi)=\iota_T\left(Z_{k(\pi)}(\pi)\wedge Z_{a+\ell(\pi)}(\pi)\right)
\in W\cap T^\perp\cong\mathbb R^{a+b-2}.
\]
For any vertex triangulation of \(\partial D\), the affine extension of \(F\) is nowhere zero and its radial normalization has degree \(\pm1\), *regardless of the chosen functions \(k,\ell\)*.

*Proof.* Decompose \(W\cap T^\perp=W_A\oplus W_B\), with dimensions \(a-1,b-1\), and write \(u_k(\pi)\in W_A\) and \(v_\ell(\pi)\in W_B\) for the centered prefix indicators inside their blocks. Then
\[
F(\pi)=\|T\|^2\left(\frac{k(\pi)}a v_{\ell(\pi)}(\pi)
-\frac{b-\ell(\pi)}b u_{k(\pi)}(\pi)\right).
\tag{2}
\]
Each boundary facet of \(D\) is either \(H_A\times P_b\) or \(P_a\times H_B\), where \(H_A,H_B\) are permutahedral facets. In the first case, if \(S\subsetneq A\) is the first block defining \(H_A\), then for every flag of that facet,
\[
\sum_{i\in S}F_i
=-\|T\|^2\frac{b-\ell(\pi)}b
\left(\min(k(\pi),|S|)-\frac{k(\pi)|S|}{a}\right)<0.
\tag{3}
\]
In the second case, the corresponding sum on the first block \(R\subsetneq B\) is
\[
\sum_{i\in R}F_i
=\|T\|^2\frac{k(\pi)}a
\left(\min(\ell(\pi),|R|)-\frac{\ell(\pi)|R|}{b}\right)>0.
\tag{4}
\]
Every boundary simplex lies in a facet, so (3) or (4) places its vertex labels in a common strict halfspace. Affine interpolation therefore never vanishes. These same inequalities persist through a straight-line homotopy from the variable-rank labels to labels with fixed arbitrary ranks \(k_0,\ell_0\). The fixed-rank product map has degree \(\pm1\) by the permutahedral prefix degree theorem and multiplicativity of Brouwer degree. Hence so does the variable-rank map. QED.

**Corollary 3 (color-sensitive formulation).** In an unrestricted reversal-odd boundary 3-tournament, suppose every Hamilton ordering in one two-block cell \(D(A|B)\) has at least one color switch whose centered prefix rank lies strictly inside \(A\) and at least one color switch whose prefix rank lies strictly inside \(B\). Then the extreme-switch bivector labeling on that cell, after contraction by its centered block vector, has canonical boundary degree \(\pm1\), even when the first and last switch ranks vary from order to order.

**Scope.** The hypotheses involve only where color switches occur relative to a bipartition, not their positions within either block. Unlike the fixed-rank construction, the theorem applies in all dimensions. It does not claim that every globally all-bad coloring possesses such a straddling top cell, and it does not itself provide a globally compatible selection of fillings on different cells.
