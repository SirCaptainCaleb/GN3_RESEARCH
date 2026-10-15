# Nested positive-prefix carriers and coherent lower-skeleton filling

### Nested positive-cone carriers yield coherent type-A lower-skeleton fillings

Fix \(n\ge4\), \(W=\{v\in\mathbb R^n:\sum v_i=0\}\), and the dual type-A Coxeter sphere \(X\cong S^{n-2}\). A cell \(D_{\mathcal P}\) is indexed by an ordered nontrivial partition \(\mathcal P=B_1|\cdots|B_k\), has dimension \(n-k\), and has vertices the full permutations refining this partition. Reversal \(J\) acts freely on \(X\) by central inversion, so \(X/J\cong\mathbb RP^{n-2}\). On oriented two-planes of \(W\), \(J\) reverses orientation.

For each proper cumulative union \(A_j=B_1\cup\cdots\cup B_j\), \(1\le j<k\), put
\[
T_{A_j}=\mathbf1_{A_j}-\frac{|A_j|}{n}\mathbf1.
\]
Define
\[
K_{\mathcal P}=\{v\in W:\langle v,T_{A_j}\rangle>0\text{ for all }j<k\},
\quad
\mathcal C_{\mathcal P}
=\{\Pi\in\widetilde{\mathrm{Gr}}_2(W):
\Pi\cap K_{\mathcal P}\ne\varnothing\}.
\tag{1}
\]
Here an oriented plane is identified with its underlying subspace for the intersection condition.

**Theorem 1 (monotone and antipodal carriers).** Every \(K_{\mathcal P}\) is a nonempty open convex cone. For every face \(D_{\mathcal Q}\subseteq D_{\mathcal P}\), one has
\[
K_{\mathcal Q}\subseteq K_{\mathcal P},\quad
\mathcal C_{\mathcal Q}\subseteq\mathcal C_{\mathcal P}.
\tag{2}
\]
For the reversed partition, \(K_{\mathcal P^R}=-K_{\mathcal P}\) and \(J(\mathcal C_{\mathcal P})=\mathcal C_{\mathcal P^R}\). Every centered prefix plane of a refining full order lies in \(\mathcal C_{\mathcal P}\), for any pair of prefix ranks \(1\le p<q<n\).

*Proof.* For a full order \(\pi\) refining \(\mathcal P\), write \(Z_p(\pi)=\sum_{h\le p}e_{\pi_h}-(p/n)\mathbf1\). Every \(A_j\) is the first \(|A_j|\) symbols of \(\pi\), and
\[
\langle Z_p(\pi),T_{A_j}\rangle
=\min(p,|A_j|)-\frac{p|A_j|}{n}>0
\]
for every \(1\le p<n\). Thus \(Z_p(\pi)\in K_{\mathcal P}\), which proves nonemptiness and the plane assertion. Refining a partition adds cumulative unions while retaining the old ones, proving (2). Reversing a partition replaces its cumulative unions by complements, and \(T_{V\setminus A}=-T_A\); since a plane meets a cone precisely when it meets the negative cone, the reversal identity follows. QED.

**Theorem 2 (sphere homotopy type).** Each carrier has
\[
\boxed{\mathcal C_{\mathcal P}\simeq S^{n-3}.}
\tag{3}
\]

*Proof.* The spherical convex region \(B=K_{\mathcal P}\cap S(W)\) is contractible: normalized straight-line interpolation toward any fixed vector in \(B\) stays inside \(B\). Let
\[
E=\{(\Pi,v):\Pi\in\mathcal C_{\mathcal P},\
v\in\Pi\cap B\}.
\]
An oriented plane with a chosen unit vector \(v\) is a positively oriented orthonormal two-frame \((v,w)\). Projection \(E\to B\) has fiber \(S(v^\perp)\cong S^{n-3}\), hence \(E\simeq S^{n-3}\).

The other projection \(E\to\mathcal C_{\mathcal P}\) has fiber \(S(\Pi)\cap K_{\mathcal P}\), a nonempty open circular arc, hence contractible. It admits continuous local sections: project a strictly feasible vector into nearby planes. A partition of unity combines them into a continuous global selection because each feasible set \(K_{\mathcal P}\cap\Pi\) is convex and excludes zero. Fiberwise normalized straight-line interpolation contracts each fiber onto the selected unit vector. Thus this projection is a homotopy equivalence, proving (3). QED.

**Theorem 3 (simultaneous lower-skeleton extension).** Let the vertices of \(X\) be labeled by oriented planes
\[
\Psi(\pi)=\operatorname{span}^+\{Z_{p(\pi)}(\pi),Z_{q(\pi)}(\pi)\},
\quad 1\le p(\pi)<q(\pi)<n,
\]
satisfying \(\Psi(\pi^R)=J\Psi(\pi)\). There exists a continuous \(J\)-equivariant extension
\[
\boxed{F:X^{(n-3)}\to\widetilde{\mathrm{Gr}}_2(W)}
\tag{4}
\]
such that on every cell with at least three ordered blocks,
\[
\boxed{F(D_{\mathcal P})\subseteq\mathcal C_{\mathcal P}.}
\tag{5}
\]

*Proof.* Induct on cell dimension, beginning with the vertex labels, which lie in their carriers by Theorem 1. Suppose a cell \(D_{\mathcal P}\) has dimension \(d=n-k\le n-3\), and every proper face \(D_{\mathcal Q}\) has been filled in its carrier. By (2), the assembled boundary map lies entirely in \(\mathcal C_{\mathcal P}\). By (3), this carrier is \((n-4)\)-connected. The attaching sphere has dimension \(d-1\le n-4\), so its map is nullhomotopic and extends over \(D_{\mathcal P}\) within that carrier. Since ordered nontrivial partitions and their reversals are distinct, the cells occur in free reversal pairs. Choose the extension on one cell of each pair and transport it by target orientation reversal onto its opposite cell. This produces (4)-(5), with the same continuous map on every shared face. QED.

For the two-block cells, dimension \(n-2\), the carrier is the positive-prefix Stiefel transversal \(\mathcal U_{T_A}\simeq S^{n-3}\). The attaching boundary sphere has dimension \(n-3\), so its map carries an integer degree, which need not vanish.

**Theorem 4 (unavoidable top-carrier obstruction in every dimension).** No continuous \(J\)-equivariant map \(F:X\to\widetilde{\mathrm{Gr}}_2(W)\) can satisfy \(F(D_{\mathcal P})\subseteq\mathcal C_{\mathcal P}\) for all cells, including the two-block top cells. Therefore, for every lower-skeleton map supplied by Theorem 3, at least one two-block cell has nonzero integral boundary degree in its carrier.

*Proof.* Suppose a map \(F\) satisfying all carrier conditions existed. At every point \(x\), belonging to the relative interior of a unique cell \(D_{\mathcal P(x)}\), the plane \(F(x)\) contains a vector strictly positive on all the prefix normals of \(\mathcal P(x)\). We can choose these vectors continuously. Indeed near a point \(x_0\) in a face \(D_{\mathcal Q}\), every nearby cell is a coface of \(D_{\mathcal Q}\), whose cone contains \(K_{\mathcal Q}\). Choose \(v_0\in F(x_0)\cap K_{\mathcal Q}\); projecting \(v_0\) into nearby planes \(F(x)\) retains strict positivity on the finitely many prefix normals of \(\mathcal Q\), hence gives a local feasible section. A partition of unity patches these sections continuously, since the feasible vectors in a given plane form an open convex cone avoiding zero. Normalize, obtaining \(v(x)\).

The reversal identities of Theorem 1 imply that \(F(Jx)\) is the same unoriented plane and its feasible cone is the negative of the cone at \(x\). Hence both \(v(x)\) and \(-v(Jx)\) lie in the same convex cone in that plane. Their sum cannot vanish. Accordingly
\[
u(x)=\frac{v(x)-v(Jx)}{\|v(x)-v(Jx)\|}
\]
is a continuous odd map \(u:X\cong S^{n-2}\to S(W)\cong S^{n-2}\), lying in \(F(x)\). Let \(w(x)\) be the unit vector in \(F(x)\), perpendicular to \(u(x)\), completing \(u(x)\) to the prescribed plane orientation. Reversal changes both the first vector and the plane orientation, so
\[
u(Jx)=-u(x),\qquad w(Jx)=w(x),\qquad u(x)\perp w(x).
\tag{6}
\]

Put \(d=n-2\). The odd map \(u:S^d\to S^d\) descends to \(\bar u:\mathbb RP^d\to\mathbb RP^d\), and \(\bar u^*\alpha=\alpha\) for the degree-one mod-two cohomology generator \(\alpha\). The even orthogonal vector \(w\) descends to a nowhere-zero section of \(\bar u^*(\gamma^\perp)\), the rank-\(d\) complement bundle of the tautological line over \(\mathbb RP^d\). Yet
\[
w_d\bigl(\bar u^*(\gamma^\perp)\bigr)
=\bar u^*(\alpha^d)
=\alpha^d\ne0.
\tag{7}
\]
This top Stiefel-Whitney obstruction prohibits a nowhere-zero section. Contradiction.

If every top-cell boundary map had degree zero in its carrier \(\mathcal C_{A|A^c}\simeq S^{n-3}\), each would extend over its ball within that carrier. Extending one cell from each reversal pair and transporting by \(J\) would produce the forbidden global map. Thus some top degree is nonzero. QED.

**Application to the two unrestricted coloring problems.** Under a hypothetical counterexample to the boundary one-switch conjecture, every Hamilton order has at least two switches and the first/last-switch plane assignment meets the hypotheses of Theorem 3. Under a hypothetical counterexample to NORI1, every rooted dimension-simple antipodal geodesic has at least two switches: one switch would give a monochromatic root slide on the same antipodally odd Petrie cycle. At a fixed root, reversal of the dimension order complements and reverses its color word, giving the same odd plane labeling. Thus both settings admit the coherent carrier-controlled extension through the full \((n-3)\)-skeleton, and both have at least one unavoidable two-block top-carrier obstruction in every dimension.

This localizes the surviving problem to the degrees of two-block attaching maps. It does not prove that the coloring constraints force those degrees to vanish, and therefore does not resolve either original conjecture.
