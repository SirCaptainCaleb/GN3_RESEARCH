# Connectedness iff greedy boundary zero-free and dual equivariant rigidity

### Greedy matroid degree: connectivity is the sharp zero-free threshold

Let \(E\) have \(m\ge2\) elements, \(W_E=\{x\in\mathbb R^E:\sum x_e=0\}\), and \(P_E\subset W_E\) the centered permutahedron, with vertices \(\pi\) indexed by orders of \(E\). For any matroid \(M\) on \(E\), write \(B_M(\pi)\) for its lexicographic greedy basis, \(p_M=|\mathcal B(M)|^{-1}\sum_{B\in\mathcal B(M)}\mathbf1_B\), and \(g_M(\pi)=\mathbf1_{B_M(\pi)}-p_M\).

**Theorem 1 (connectivity criterion).** For any triangulation of the permutahedral boundary using its vertices, extend the vertex labels \(g_M\) affinely over simplices. The resulting boundary map avoids zero if and only if \(M\) is connected. When connected, its normalized map has degree \(\pm1\). When disconnected, for *every* such triangulation the map vanishes on the ordered-component face of \(P_E\).

*Proof.* If \(M\) is connected, then for every nonempty proper \(S\subset E\) the matroid inequality
\[
r_M(S)+r_M(E\setminus S)>r_M(E)
\]
implies \(p_M(S)<r_M(S)\): extend a basis of the complement to a basis of \(M\), obtaining one whose intersection with \(S\) has fewer than \(r_M(S)\) members, while no basis exceeds \(r_M(S)\). On a face indexed by an ordered partition whose first block is \(S\), greedily scanning any compatible permutation selects \(r_M(S)\) elements of \(S\). Hence the linear functional \(\sum_{e\in S}x_e\) takes the strictly positive value \(r_M(S)-p_M(S)\) on every prescribed vertex label of that face. Affine extension is zero-free there. The same halfspace contains the standard centered permutahedron vertices. Straight-line interpolation to the identity embedding is therefore zero-free on the entire boundary and preserves degree \(\pm1\).

Conversely suppose \(M=\bigoplus_{i=1}^q M_i\), \(q\ge2\), is the direct sum of its connected matroid components \(C_1,\ldots,C_q\). Consider the proper face \(F=C_1|\cdots|C_q\) of the permutahedron. Geometrically \(F\cong\prod_{i=1}^q P_{C_i}\), a ball of dimension \(m-q\). Greedy basis selection and basis barycenters split componentwise. Therefore the vertex labels on \(F\) lie in
\[
L=\bigoplus_{i=1}^q W_{C_i},\qquad\dim L=m-q=\dim F.
\]
On any proper boundary face \(H\) of \(F\), at least one component permutahedron has a proper first block \(S\subsetneq C_i\), so that component contributes the positive supporting functional \(r_{M_i}(S)-p_{M_i}(S)>0\). The affine boundary map on \(\partial F\) avoids zero and is straight-line homotopic there to the centered product-polytope embedding \(F\hookrightarrow L\). It consequently has degree \(\pm1\). Any continuous extension from \(F\) to \(L\) must attain zero, else its normalized boundary map would extend over the ball. In particular every affine triangulation extension of \(g_M\) has a zero on the proper face \(F\subset\partial P_E\). Singleton components cause no difficulty: their factors have dimension zero and their summands are zero. QED.

**Theorem 2 (equivariant rigidity of variable connected-matroid assignments).** Assign an independently chosen connected matroid \(M_\pi\) on \(E\) to every full order \(\pi\), subject only to
\[
M_{\pi^R}=M_\pi^*.
\]
Then the greedy labeling \(g(\pi)=g_{M_\pi}(\pi)\) extends to a zero-free, reversal-odd map on \(\partial P_E\). More strongly, every such labeling is *equivariantly homotopic* to the standard centered permutahedron boundary embedding. Thus its ordinary degree is odd, and its equivariant homotopy class is independent of all matroid choices.

*Proof.* Greedy duality gives \(g_{M^*}(\pi^R)=-g_M(\pi)\). The centrally inverted standard permutahedral vertex vector \(u_\pi\) also satisfies \(u_{\pi^R}=-u_\pi\). For each face with first block \(S\), the connectedness argument above places \(g_{M_\pi}(\pi)\) and \(u_\pi\) in one strict positive halfspace simultaneously, for every vertex \(\pi\) of that face. Thus the affine straight-line homotopy \((1-t)g+t u\) is zero-free on every boundary simplex and is reversal-equivariant throughout. Its endpoint is the identity boundary embedding, proving the assertion. QED.

**Consequence for the unification program.** Duality and connected greedy-basis carriers supply the correct antipodal behavior automatically, but carry no color-sensitive homotopy information when connectivity is retained at every flag. A useful contradiction via this carrier must force a loss of matroid connectivity, a change in target dimension, or additional cross-face constraints not reducible to independent greedy selections. Theorem 1 gives a precise geometric signature of a connectivity failure: a zero already on the ordered-component face, rather than a mysterious high-dimensional top-cell obstruction.
