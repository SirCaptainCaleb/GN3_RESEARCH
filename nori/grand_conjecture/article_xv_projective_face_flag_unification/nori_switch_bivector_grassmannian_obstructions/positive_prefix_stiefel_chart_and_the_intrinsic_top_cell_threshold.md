# Positive-prefix Stiefel chart and the intrinsic top-cell threshold

### Positive-prefix Stiefel charts and the first substantive cell dimension

Let \(W=\{z\in\mathbb R^n:\sum z_i=0\}\), \(n\ge5\). Fix a nonzero vector \(T\in W\) and write \(\mathcal G=\widetilde{\mathrm{Gr}}_2(W)\) for the manifold of oriented two-planes. Define the open transversal plane set
\[
\mathcal U_T=\{\Pi\in\mathcal G:\operatorname{proj}_{\Pi}T\ne0\}.
\]

**Theorem 1 (explicit sphere deformation retract).** There is a natural deformation retraction
\[
\boxed{\mathcal U_T\simeq S(T^\perp)\cong S^{n-3},}\tag{1}
\]
where \(S(T^\perp)\) is identified with the oriented planes containing \(T\). More precisely, each plane \(\Pi\in\mathcal U_T\) has its unique positively oriented orthonormal frame \((e_1,e_2)\) for which
\[
e_1=\frac{\operatorname{proj}_\Pi T}{\|\operatorname{proj}_\Pi T\|},\qquad
e_2\perp T.
\]
The assignment \(\Pi\mapsto e_2\) has contractible fibers, and the frame deformation
\[
e_1(t)=\frac{(1-t)e_1+tT/\|T\|}{\|(1-t)e_1+tT/\|T\|\|},\qquad e_2(t)=e_2,
\]
retracts \(\mathcal U_T\) onto the containing-\(T\) sphere.

*Proof.* The positive \(T\)-projection determines \(e_1\) uniquely, and the orientation then determines \(e_2\). Since \(T\) has no component along \(e_2\), necessarily \(e_2\in T^\perp\). Conversely, given a unit \(e_2\in T^\perp\), every unit \(e_1\in e_2^\perp\) with \(\langle e_1,T\rangle>0\) yields such a plane and frame; the possible \(e_1\) form an open hemisphere. The displayed formula stays inside this hemisphere and keeps \(e_1(t)\perp e_2\), and at \(t=1\) the plane contains \(T\). QED.

**Theorem 2 (every parabolic residue has a positive-prefix transversal).** Let \(\mathcal P=B_1|\cdots|B_k\) be any ordered partition into at least two nonempty blocks, with \(a=|B_1|\). Put
\[
T_{\mathcal P}=\mathbf1_{B_1}-\frac an\mathbf1.
\]
For every full ordering \(\pi\) refining \(\mathcal P\) and every nontrivial centered prefix \(Z_p(\pi)\),
\[
\boxed{\langle T_{\mathcal P},Z_p(\pi)\rangle
=\min(p,a)-ap/n>0.}\tag{2}
\]
Consequently every extreme-switch oriented plane \(\mathrm{span}^{+}(Z_p,Z_q)\), for \(p<q\), belongs to the SAME open set \(\mathcal U_{T_{\mathcal P}}\), regardless of unrestricted coloring or chosen switch ranks.

*Proof.* Every refining full order places precisely the \(a\) members of \(B_1\) first. The dot product is the centered number of them in the first \(p\) positions, giving (2). Since \(a<n\) and \(0<p<n\), the value is positive. A plane containing \(Z_p\) with positive pairing against \(T_{\mathcal P}\) cannot be perpendicular to \(T_{\mathcal P}\). QED.

**Corollary 3 (local Grassmannian obstruction threshold).** For \(n\ge6\), \(\mathcal U_{T_{\mathcal P}}\simeq S^{n-3}\) is \((n-4)\)-connected. Thus any boundary map of a parabolic cell \(D\) of dimension \(k\le n-3\), provided its entire boundary image stays in this fixed \(\mathcal U_{T_{\mathcal P}}\), extends continuously over \(D\) inside \(\mathcal U_{T_{\mathcal P}}\). In particular any rank-three parabolic cell boundary map inside its natural positive-prefix transversal is nullhomotopic when \(n\ge6\).

*Proof.* Its boundary sphere has dimension \(k-1\le n-4\), while \(\pi_j(S^{n-3})=0\) for \(j<n-3\). QED.

**Theorem 4 (why the top-cell straddling obstruction survives).** In dimension \(d=n-2\), the sphere \(\mathcal U_T\simeq S^{n-3}\) itself has nontrivial group \(\pi_{n-3}(\mathcal U_T)\cong\mathbb Z\). The variable-rank two-block switch-plane boundary constructed in the earlier Stiefel obstruction subsection takes values in \(\mathcal U_T\) and has degree \(\pm1\) under the retraction (1). Under inclusion into the full oriented Grassmannian, this integer reduces modulo \(\chi(S^{n-2})\). Thus its image is the nonzero generator of \(\mathbb Z\) when \(n\) is odd, or \(\mathbb Z/2\) when \(n\) is even.

*Proof.* On the relevant top cell the first vector \(x=Z_k\) stays strictly positive against the block vector \(T\), even under the affine boundary interpolation of the two vectors. The retraction identifies its plane boundary class with the unit contraction \(\iota_T(x\wedge y)\), of degree \(\pm1\) by the permutahedral product theorem. The standard Stiefel fibration \(S^{n-3}\to V_2(\mathbb R^{n-1})\to S^{n-2}\) sends its generator to the quotient by the tangent-sphere Euler number, \(\chi(S^{n-2})\), and the frame-to-Grassmannian bundle does not change \(\pi_{n-3}\) for \(n\ge6\). QED.

**Proof-search implication.** The flag planes in ANY individual nontrivial parabolic residue lie in a common natural transversal to a fixed block vector. Therefore a lower-cell Grassmannian obstruction cannot be inferred merely from its vertex labels: any such obstruction must involve how previously chosen boundary fillings leave or wind between these transversal charts. This isolates the global face-gluing problem more precisely. It does not give compatible chart-preserving fillings across all cells simultaneously, nor resolve the two target conjectures.
