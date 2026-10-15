# Primary projective obstruction and root-slide monodromy in dimension-simple Coxeter chains

# Primary projective obstruction and root-slide monodromy in dimension-simple Coxeter chains

This subsection continues the signed-second-switch construction and the acyclic-carrier theorem for two-end-stable parabolic cells (Article XIV, preceding Subsections 18, 22, and 23). Its point is an **all-dimensional obstruction localization**: all lower-dimensional extension problems can be solved, and the first unavoidable failure defines a cohomology class Poincare dual to the same root-slide monodromy that arises in the cube's Coxeter rotation. Unlike a small-rank calculation, the result is uniform in \(n\).

Let \(n\ge4\). Write \(X\) for the dual CW decomposition of the type-\(B_n\) Coxeter complex on \(S^{n-1}\). Its vertices are complete rooted antipodal cube geodesics \(g=(x,\pi)\), and its closed cells are the parabolic residues \(gW_J\), where \(J\subseteq\{0,\ldots,n-1\}\) and \(\dim(gW_J)=|J|\). The central antipodal involution acts freely and cellularly, with quotient \(Y=X/\langle-\rangle\cong\mathbb{RP}^{n-1}\).

Assume hypothetically that an antipodally odd undirected cube-edge coloring has **no** monochromatic full antipodal geodesic. Each complete geodesic then has at least two switches. Let \(w(g)\) be its \(n\)-bit edge word, let \(s_2(g)\in\{2,\ldots,n-1\}\) be the position of its second switch, and define
\[
\ell(g)=(-1)^{w_1(g)}e_{s_2(g)}
\in\partial\mathcal O\cong S^{n-3},\qquad
\mathcal O=\operatorname{conv}\{\pm e_2,\ldots,\pm e_{n-1}\}.
\tag{1}
\]
The adjacent-chamber nonopposition lemma already established in Article XIV gives an antipodally equivariant map on \(X^{(1)}\), sending each dual edge into the target crosspolytope boundary. The two-end-stable extension theorem from the preceding subsection gives an equivariant extension over the subcomplex
\[
X_{\mathrm{good}}=
\bigcup\{gW_J:1\notin J\ \text{or}\ \{0,n-1\}\cap J=\varnothing\}.
\tag{2}
\]
This subcomplex contains \(X^{(1)}\).

**Theorem 1 (primary-obstruction localization).** There is an antipodally equivariant map
\[
F:X_{\mathrm{good}}\cup X^{(n-3)}\longrightarrow S^{n-3}
\tag{3}
\]
agreeing with the signed-second-switch map on vertices and dual edges and agreeing with the previously constructed map on \(X_{\mathrm{good}}\). For each cell \(D=gW_J\) of dimension \(n-2\), let
\[
o(D)=\deg_2\!\left(F|_{\partial D}:\partial D\cong S^{n-3}\longrightarrow S^{n-3}\right).
\tag{4}
\]
This descends to a mod-two cellular \((n-2)\)-cocycle \(o\) on \(Y\), whose cohomology class is
\[
\boxed{[o]=u^{n-2}\ne0\in H^{n-2}(\mathbb{RP}^{n-1};\mathbb F_2),}
\tag{5}
\]
where \(u\) is the degree-one generator. Thus some dimension-\((n-2)\) parabolic residue has a boundary map of odd degree and cannot be filled equivariantly in the proposed target. Moreover every such residue is of one of the following two parabolic types, described by the **two omitted simple generators**:
\[
\boxed{
\begin{array}{ll}
\{0,j\},& 2\le j\le n-2,\\[2pt]
\{i,j\},&2\le i<j\le n-1.
\end{array}}
\tag{6}
\]
There are \(n(n-3)/2\) possible omitted-generator pairs in (6), compared with \(\binom n2\) pairs in total. For \(n=4\), the two types are respectively \(\{0,2\}\) and \(\{2,3\}\).

*Proof.* The target sphere \(S^{n-3}\) is \((n-4)\)-connected. Attaching a \(k\)-cell with \(k\le n-3\) to a partially defined map presents an attaching sphere of dimension \(k-1\le n-4\), so its boundary map extends. The antipodal involution acts freely on the cells, and extensions may be chosen on one cell in each antipodal pair and transported to the partner. Starting from the compatible map on \(X_{\mathrm{good}}\) therefore yields (3) without altering the already defined cells.

An equivariant map into \(S^{n-3}\), viewed as the unit sphere of the sign representation \(\mathbb R^{n-2}\), is a nowhere-zero section over \(Y\) of the rank-\((n-2)\) real vector bundle
\[
E=(n-2)\gamma,
\tag{7}
\]
where \(\gamma\) denotes the tautological real line bundle over \(\mathbb{RP}^{n-1}\). The mod-two primary obstruction to extending that section over the \((n-2)\)-cells is represented by the degree cocycle (4), and its cohomology class is the top Stiefel-Whitney class
\[
w_{n-2}(E)=w_{n-2}((n-2)\gamma)
=u^{n-2},
\tag{8}
\]
because \(w(E)=(1+u)^{n-2}\). The standard cohomology ring \(H^*(\mathbb{RP}^{n-1};\mathbb F_2)=\mathbb F_2[u]/(u^n)\) makes this class nonzero. This proves (5), including the cocycle relation, and forces an odd-degree boundary on at least one cell.

For each cell of \(X_{\mathrm{good}}\), the map already extends across the cell, so its degree obstruction vanishes. Thus any cell with \(o(D)=1\) has \(1\in J\) and at least one of \(0,n-1\) belonging to \(J\). As \(|J|=n-2\), the complement of \(J\) consists of two generator indices. Avoiding the omission of \(1\), and avoiding the simultaneous omission of \(0,n-1\), gives precisely (6). Counting yields \((n-3)+\binom{n-2}{2}=n(n-3)/2\). \(\square\)

**Theorem 2 (obstruction as a projective one-cycle).** The mod-two Poincare dual of the cocycle \(o\) is a cellular one-cycle \(Z_o\) in a dual subdivision of \(Y\), whose homology class is the unique nonzero element of
\[
\boxed{H_1(\mathbb{RP}^{n-1};\mathbb F_2)\cong\mathbb F_2.}
\tag{9}
\]
It is homologous to the loop obtained from **\(n\) Coxeter root slides**, namely the path from any chamber \(g=(x,\pi)\) to \(-g=(\bar x,\pi)\) under
\[
T(x;i_1,\ldots,i_n)=(x\oplus e_{i_1};i_2,\ldots,i_n,i_1),
\quad T^n g=-g,
\tag{10}
\]
after projection to \(Y\).

*Proof.* In the closed \((n-1)\)-manifold \(Y\), cellular Poincare duality sends a mod-two \((n-2)\)-cocycle to a dual one-cycle. By (5),
\[
[Z_o]=u^{n-2}\frown[Y]\ne0
\quad\text{in }H_1(Y;\mathbb F_2).
\tag{11}
\]
A path on \(S^{n-1}\) joining a point to its antipode projects to a loop representing the nontrivial element of the fundamental group and hence of mod-two first homology of \(\mathbb{RP}^{n-1}\). The \(n\) root slides in (10), with each Coxeter multiplication resolved into adjacent chamber edges, provide such a path. Therefore their projected loop and \(Z_o\) represent the same nonzero homology class. \(\square\)

**Interpretation and proof target.** The nonextendibility of the signed-second-switch map is now concentrated in rank-\((n-2)\) residues of the two types (6), and the parity of their boundary degrees globally forms a projective one-cycle with the *same homology class as root-slide half-turn monodromy*. The theorem applies to any hypothetical no-monochromatic-geodesic coloring and relies only on the existing adjacent-chamber lemma, two-end acyclic carriers, and classical obstruction theory. It does **not** rule out such a coloring by itself: the nonzero class (5) is a consequence of the antipodal topology, not a contradiction.

To finish a dimension-simple adaptation of Wu–Yang, it would suffice to prove that the **color-sensitive incidence identities** force this degree cocycle to be null-cohomologous, or show directly that the odd-degree boundary maps of both residual types in (6) admit coherent fillings after a suitable enrichment of the target that does not destroy the dimension bound. Either statement would contradict (5). In the second formulation, the corrections must confront the projective root-slide cycle globally, rather than filling arbitrary local squares in isolation.
