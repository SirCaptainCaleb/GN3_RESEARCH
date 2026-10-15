# Color-stable endpoint carriers and mixed-star localization

# Color-position carriers and a high-rank oscillation obstruction

This subsection strengthens the two-end localization of the dimension-simple second-switch method. The labels need not share a terminal **edge**, or even an endpoint color. A color fixed in any path position beyond the second gives a hemispherical carrier. The resulting equivariant extension leaves only parabolic cells with strong color variation across nearly every word position.

Throughout let \(n\ge5\), let \(c:E(Q_n)\to\mathbb F_2\) satisfy antipodal oddness, and provisionally suppose every full antipodal geodesic has at least two switches. The dual type-\(B_n\) Coxeter complex \(X\cong S^{n-1}\) has vertices \(P(x,\pi)\); the signed second-switch labeling is
\[
L(P)=(-1)^{w_1(P)}e_{s_2(P)}
\in \partial\mathcal O\cong S^{n-3},
\qquad
\mathcal O=\operatorname{conv}\{\pm e_2,\ldots,\pm e_{n-1}\}.
\tag{1}
\]
As established earlier, this map is antipodally odd and maps adjacent dual vertices to nonopposite target vertices.

## Anchoring any later word position

**Lemma 1 (fixed-position hemisphere).** Fix \(r\in\{3,\ldots,n\}\) and a family \(\mathcal P\) of complete geodesics whose \(r\)-th edge-color bit is the same \(b\). Then
\[
L(\mathcal P)\subseteq
H_{r,b}:=\partial\mathcal O\cap
\{z:(-1)^b z_{r-1}\ge0\}.
\tag{2}
\]
For any family whose first color is constant \(a\), all labels lie in the target simplex
\[
\Delta_a:=\operatorname{conv}\{(-1)^a e_2,\ldots,(-1)^a e_{n-1}\}.
\tag{3}
\]

*Proof.* If \(s_2(P)=r-1\), the first \(r-1\) comparisons in the word contain two switches, so \(w_1(P)=w_r(P)=b\). Hence a label on the \(e_{r-1}\)-axis has the prescribed sign. Every other label has zero component on that axis. The second assertion follows directly from (1). \(\square\)

**Theorem 2 (equivariant anchored-color carrier).** Let \(X_{\mathrm{anc}}\) be the union of all closed dual Coxeter cells \(D\) for which at least one of the bit positions
\[
\mathcal I=\{1,3,4,\ldots,n\}
\tag{4}
\]
is constant over the complete geodesics represented by the vertices of \(D\). Then \(X_{\mathrm{anc}}\) is an antipodally invariant subcomplex containing the entire dual 1-skeleton. The signed second-switch labeling extends to an equivariant continuous map
\[
F_{\mathrm{anc}}:X_{\mathrm{anc}}\longrightarrow S^{n-3}
\tag{5}
\]
via nested contractible target carriers. It also induces an equivariant augmentation-preserving chain map on the corresponding source chains.

*Proof.* Constancy of a word position is inherited by every face of a dual cell; antipodality complements its bit but preserves constancy. Thus \(X_{\mathrm{anc}}\) is an antipodally invariant subcomplex.

For each \(D\subseteq X_{\mathrm{anc}}\), let \(A_D\subseteq\mathcal I\) be its set of constant positions, with values \(b_r(D)\). Define
\[
C_D=
\begin{cases}
\displaystyle \Delta_{b_1(D)}
\cap\bigcap_{r\in A_D\setminus\{1\}}H_{r,b_r(D)},&1\in A_D,\\[2mm]
\displaystyle\bigcap_{r\in A_D}H_{r,b_r(D)},&1\notin A_D.
\end{cases}
\tag{6}
\]
By Lemma 1, every label of a chamber of \(D\) belongs to \(C_D\), so each carrier is nonempty. If the first bit is fixed, the intersection in (6) is a nonempty face of the simplex \(\Delta_{b_1(D)}\) and hence contractible. Otherwise the intersection contains at least one signed hemispherical constraint. Its intersection with the sphere is also contractible: let
\[
v=\sum_{r\in A_D}(-1)^{b_r(D)}e_{r-1}\ne0.
\]
For any \(z\in C_D\), one has \(z\cdot v\ge0\), so normalized linear interpolation from \(z\) to \(v\) never meets the origin and contracts \(C_D\).

If \(D'\) is a face of \(D\), every constant position of \(D\) remains constant with the same bit on \(D'\); additional restrictions only shrink the carrier. Thus \(C_{D'}\subseteq C_D\). Antipodality sends all fixed bits to their complements and each carrier to its negative. On dual edges, the known nonopposition theorem supplies the short target crosspolytope edge, and this edge lies inside the chosen carrier (the carriers are spherical intersections of closed convex cones). Inductively extend higher cell boundary maps inside their contractible carriers, selecting a member of each free antipodal cell pair before defining the opposite filling by antipodality. This produces (5) and the associated equivariant chain map. \(\square\)

## Consequences for top-dimensional obstruction cells

**Corollary 3 (every surviving primary cell varies at almost every position).** There is an equivariant extension of the second-switch labeling over
\[
X_{\mathrm{anc}}\cup X^{(n-3)}.
\]
Under the hypothetical absence of a monochromatic antipodal geodesic, at least one dual \((n-2)\)-cell outside \(X_{\mathrm{anc}}\) has nonzero attaching-map degree into \(S^{n-3}\). In particular that cell satisfies:

* its parabolic generator set \(J\) contains \(s_1\) and at least one of \(s_0,s_{n-1}\);
* for **every** position \(r\in\{1,3,\ldots,n\}\), two chamber geodesics in that same cell have different colors in position \(r\).

*Proof.* Fill the anchored cells by Theorem 2. Fill any remaining cells of dimension at most \(n-3\) equivariantly, since \(S^{n-3}\) is \((n-4)\)-connected. If every remaining \((n-2)\)-cell boundary had zero degree, the map would extend equivariantly over \(X^{(n-2)}\). This contradicts the nonzero \((n-2)\)-nd power of the first Stiefel-Whitney class of the double covering \(S^{n-1}\to\mathbb RP^{n-1}\); no equivariant map of that skeleton to \(S^{n-3}\) exists. Thus at least one cell not in \(X_{\mathrm{anc}}\) carries an obstruction. Its lack of constant positions yields the stated simultaneous variability. The parabolic condition follows from the previous two-end localization, since every cell avoiding \(s_1\), or avoiding both \(s_0,s_{n-1}\), already has a first or last fixed edge. \(\square\)

**Theorem 4 (mixed-star localization on root-fixed cells).** Let \(D=gW_J\) be a dual \((n-2)\)-cell with \(s_0\notin J\). If \(D\notin X_{\mathrm{anc}}\), then \(J\) omits precisely \(s_0,s_k\) for some \(2\le k\le n-2\). All its geodesics have a common starting cube vertex \(x\), and their dimension orders consist of permutations of a fixed \(k\)-element initial block \(A\), followed by permutations of its complementary block \(B\). Writing
\[
a_i(x)=c(\{x,x\oplus e_i\}),
\]
both sets
\[
\{a_i(x):i\in A\},\qquad
\{a_i(x):i\in B\}
\]
contain both binary colors. In particular there are at least two red and two blue edges incident to \(x\).

*Proof.* A rank-\((n-2)\) parabolic cell omits two of the \(n\) simple generators. With \(s_0\) missing, the remaining missing generator is \(s_k\). Values \(k=1\) and \(k=n-1\) respectively fix the first and last edge and would put \(D\) in \(X_{\mathrm{anc}}\); hence \(2\le k\le n-2\). The subgroup generated by all swaps except \(s_k\) permutes the first and last dimension blocks independently; \(s_0\) is absent, so the root \(x\) is fixed.

For any full geodesic beginning at \(x\), the first bit equals \(a_{\pi_1}(x)\). Its final edge is antipodal to the edge in direction \(\pi_n\) incident to \(x\), so
\[
w_n(P(x,\pi))=1-a_{\pi_n}(x).
\tag{7}
\]
The first and last dimensions range freely over \(A\) and \(B\), respectively. If either block were monochromatic in the star at \(x\), the first or last word bit would be constant throughout \(D\), contradicting \(D\notin X_{\mathrm{anc}}\). As \(A,B\) are disjoint, the final assertion follows. \(\square\)

**Interpretation.** The unrestricted problem is reduced further to cells with strong simultaneous color variability. A root-fixed primary obstruction must involve two disjoint blocks of dimensions, each with both colors at the same cube root. The remaining cells containing the root-flip generator \(s_0\) require a different analysis: the initial root itself varies, so formula (7) no longer supplies a fixed star vector. These are the most promising location for a support-preserving analogue of Wu–Yang's degenerate-face cancellation. No new coloring restrictions, finite-order reductions, or restricted-family hypotheses are used.
