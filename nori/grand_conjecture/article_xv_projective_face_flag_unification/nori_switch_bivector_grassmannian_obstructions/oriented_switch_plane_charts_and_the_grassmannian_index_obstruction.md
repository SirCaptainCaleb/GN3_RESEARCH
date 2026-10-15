# Oriented switch-plane charts and the Grassmannian index obstruction

### Oriented switch-plane charts and the Grassmannian index obstruction

Let \(W=\{z\in\mathbb R^n:\sum z_i=0\}\), \(n\ge5\), and let \(\mathcal G=\widetilde{\mathrm{Gr}}_2(W)\) be the space of oriented two-planes, with its free orientation-reversing involution \(J\). A full centered color word with first and last switch-prefix ranks \(p<q\) determines the oriented plane \(\Psi=(\mathrm{span}\{Z_p,Z_q\}, Z_p\wedge Z_q)\). This is defined whenever there are two switches. Under the complemented-reversal law for either original problem, \(\Psi(Rg)=J\Psi(g)\).

**Lemma 1 (decomposable separating charts).** For independent covectors \(u,v\in W^*\), the subset of oriented planes \(\Pi\) with positive Pluecker evaluation \((u\wedge v)(\Pi)>0\) is contractible, homeomorphic to \(\mathbb R^{2(n-3)}\). The negative subset is also contractible.

*Proof.* Split \(W=H\oplus\ker(u,v)\), with \(H\) two-dimensional and the covectors independent on \(H\). Each such plane is the graph of a unique linear map \(H\to\ker(u,v)\), with the orientation determined by its projection to \(H\). This is a vector-space chart. \(\square\)

**Theorem 2 (boundary rank-two Grassmannian charts).** For every unrestricted reversal-odd boundary triple coloring, every rank-two dual type-A Coxeter cell whose Hamilton flags all have at least two switches has its flag planes \(\Psi\) contained in one contractible chart from Lemma 1.

*Proof.* For each commuting square or braid residue whose first and last ordered blocks have size at most two, the previous universal convex-carrier theorem gives a negative decomposable separator \(e_a^*\wedge e_c^*\), with \(a\) in the first block and \(c\) in the last.

A terminal braid residue with a variable first three-symbol set \(A=\{a,b,c\}\) needs a weighted separator. Fix the final symbol \(z\), choose positive weights \(\lambda_t\) on \(A\) summing to one, and put \(u=\sum_{t\in A}\lambda_t e_t^*\). If the first and last switch-prefix ranks are \(p<q\), then \((u\wedge e_z^*)(Z_p\wedge Z_q)=(p-q)/n<0\) when \(p\ge3\). When \(p=2\), write \(t\) for the third symbol of the first three, and calculate
\[
\boxed{(u\wedge e_z^*)(Z_2\wedge Z_q)
=\frac{q\lambda_t-(q-2)}n.}\tag{1}
\]
For \(q=3\), negativity requires \(\lambda_t<1/3\); for \(q\ge4\), it suffices that \(\lambda_t<1/2\). The terminal-braid theorem from the preceding Subsection proves that, if all six flags have at least two switches, the pair \((p,q)=(2,3)\) cannot occur with each of the three possible third symbols. Thus at most two weights must be below \(1/3\), while the others need only be below \(1/2\). These strict bounds admit positive weights totaling one because their upper bounds sum to at least \(1/3+1/3+1/2>1\). Equation (1) then makes \(u\wedge e_z^*\) negative on all six planes. Reversing all Hamilton orders handles a final-three-symbol braid residue. For \(n=5\), the bad-hexagon hypothesis is already impossible by the previous theorem. \(\square\)

**Corollary 3 (equivariant two-skeleton realization).** Under the hypothetical absence of a one-switch Hamilton order for a reversal-odd boundary coloring on \(n\ge6\) vertices, the flag-plane assignment \(\Psi\) extends equivariantly over the full two-skeleton of the dual type-A Coxeter sphere with target \(\mathcal G\).

*Proof.* The oriented two-plane Grassmannian is simply connected for \(\dim W\ge4\), as follows from the standard fibration \(SO(2)\times SO(n-3)\to SO(n-1)\to\mathcal G\). Choose paths on involutive pairs of dual edges and use simple connectivity to fill each two-cell, choosing fillings in opposite pairs. Theorem 2 strengthens this abstract extension by providing a contractible color-sensitive chart for the vertices of every two-cell. \(\square\)

**Theorem 4 (an infinite Grassmannian cohomological obstruction).** Suppose \(m=2^r\ge4\). On the unoriented Grassmannian \(\operatorname{Gr}_2(\mathbb R^m)\), the orientation-cover class \(\omega=w_1(\gamma_2)\) satisfies
\[
\boxed{\omega^{m-1}=0.}\tag{2}
\]
Consequently, for \(n=m+1\), no antipodally equivariant map exists from the type-A Coxeter sphere \(S^{n-2}\) into \(\widetilde{\operatorname{Gr}}_2(\mathbb R^{n-1})\). Likewise, no equivariant map exists from the free punctured affine reversal carrier \(M_n\) constructed earlier in this Article into that oriented Grassmannian.

*Proof.* Set \(x=w_1(\gamma_2)\), \(y=w_2(\gamma_2)\), and expand the formal inverse \((1+xt+yt^2)^{-1}=\sum_{j\ge0}h_jt^j\). The orthogonal complement of the tautological bundle has rank \(m-2\), so the Whitney sum relation gives \(h_{m-1}=0\). Over \(\mathbb F_2\),
\[
h_j=\sum_{k=0}^{\lfloor j/2\rfloor}
\binom{j-k}{k}x^{j-2k}y^k.
\]
For \(j=m-1=2^r-1\), all terms with \(k\ge1\) vanish modulo two. Indeed the binary digits of \(j-k\) and \(k\) are complementary, so Lucas's criterion makes \(\binom{j-k}{k}\) even. Therefore \(h_{m-1}=x^{m-1}\), proving (2).

The type-A sphere quotient is \(\mathbb RP^{m-1}\), whose covering class \(\alpha\) has \(\alpha^{m-1}\ne0\). A hypothetical equivariant map would induce a quotient map pulling \(\omega\) back to \(\alpha\), contradicting (2). The quotient of \(M_n\) contains projective boundary components \(\mathbb RP^m\) on which its covering class has nonzero \((m-1)\)-st power, giving the same contradiction. \(\square\)

The Grassmannian cohomology presentation is classical; see https://link.springer.com/article/10.1007/s00209-024-03556-y.

**Research consequence.** The oriented switch-plane target is common to both original full-path questions. At dimensions \(n=2^r+1\), its covering class has insufficient index for an equivariant map from either source. For unrestricted boundary tournaments, the no-good-path assumption already supplies an equivariant map on the entire two-skeleton. The next obstruction lies in extending over three-dimensional cells, where \(\pi_2(\mathcal G)\) can carry nonzero classes. For cubes, the terminal braid counterexample still prevents a purely local universal chart. The global extensions, and the original existence conjectures, remain open.
