# Parabolic fixed-space surplus and equivariant Stiefel fillings

### The parabolic block-count surplus for equivariant oriented-plane fillings

Let \(V=[n]\), \(W=\{z\in\mathbb R^n:\sum_{i\in V}z_i=0\}\), and let
\[
\mathcal P=B_1|\cdots|B_k\qquad(k\ge2)
\]
be an ordered partition into nonempty blocks. The associated dual type-A Coxeter cell \(D_{\mathcal P}\) is the product of permutahedra \(P_{B_1}\times\cdots\times P_{B_k}\), of dimension \(n-k\). Its natural relabeling group is \(G_{\mathcal P}=\prod_i S_{B_i}\). Put
\[
T=\mathbf1_{B_1}-\frac{|B_1|}{n}\mathbf1,\qquad
H_T=T^\perp\cap W.
\]
The oriented-plane transversal \(\mathcal U_T=\{\Pi\in\widetilde{\mathrm{Gr}}_2(W):\operatorname{proj}_\Pi T\ne0\}\) has a \(G_{\mathcal P}\)-equivariant deformation retraction onto \(S(H_T)\): orient the normalized projected vector \(T\) first and take the oriented unit companion perpendicular to \(T\). This is the positive-prefix Stiefel retraction from the preceding Subsection.

**Lemma 1 (fixed-space surplus).** For every subgroup \(K\le G_{\mathcal P}\), let \(r_i(K)\) denote the number of \(K\)-orbits on \(B_i\), and put \(r(K)=\sum_i r_i(K)\). Then
\[
\boxed{\dim D_{\mathcal P}^K=r(K)-k,\qquad
\dim H_T^K=r(K)-2,\qquad
\dim H_T^K-\dim D_{\mathcal P}^K=k-2.}
\tag{1}
\]

*Proof.* For each \(i\), the fixed subspace of the centered permutation representation on \(B_i\) has dimension \(r_i(K)-1\). Since the barycenter is an interior point of every factor permutahedron, its fixed polytope has this same dimension. Summing over factors gives the first identity. The \(K\)-fixed subspace of \(\mathbb R^V\) has dimension \(r(K)\), consisting of vectors constant on each orbit. Imposing zero total sum leaves dimension \(r(K)-1\). The nonzero \(K\)-fixed vector \(T\) imposes one additional independent orthogonality equation, so \(\dim H_T^K=r(K)-2\). Subtraction proves (1). QED.

**Lemma 2 (equivariant cell extension criterion).** Let a finite group \(G\) act linearly on a convex polytope \(D\) and orthogonally on a real representation \(L\). If
\[
\dim L^K\ge\dim D^K+1
\tag{2}
\]
for every subgroup \(K\le G\), then any \(G\)-equivariant map from the vertices of \(D\) into \(S(L)\) extends to a \(G\)-equivariant continuous map \(D\to S(L)\). The conclusion also holds for an equivariant map already prescribed on any invariant subcomplex of an equivariant cell decomposition, provided that subcomplex contains all the prescribed vertices.

*Proof.* Choose a finite equivariant cell subdivision refining the given invariant subcomplex, with every cell stabilizer acting pointwise; this exists for a finite linear group action on a polytope. Extend cell by cell, simultaneously over each \(G\)-orbit of cells. For a \(j\)-cell fixed pointwise by \(K\), its boundary map lands in \(S(L)^K=S(L^K)\), a sphere of dimension \(\dim L^K-1\). Since that cell lies in \(D^K\), one has \(j\le\dim D^K<\dim L^K\). Consequently \(\pi_{j-1}(S(L^K))=0\) for \(j\ge1\); for \(j=0\), the fixed sphere is nonempty. The required extension therefore exists and is propagated by \(G\) to the cell orbit. QED.

**Theorem 3 (all proper multiblock cells have symmetry-compatible plane fillings).** If \(k\ge3\), *every* \(G_{\mathcal P}\)-equivariant nonzero oriented-plane labeling of the vertices of \(D_{\mathcal P}\) with values in \(\mathcal U_T\) extends over the entire cell to a continuous \(G_{\mathcal P}\)-equivariant map \(D_{\mathcal P}\to\mathcal U_T\). In particular, this applies to the first-and-last-switch plane labels of any coloring for which all the flags of the cell have at least two switches, after replacing \(G_{\mathcal P}\) by the stabilizer of the coloring.

*Proof.* By Lemma 1, \(\dim H_T^K-\dim D_{\mathcal P}^K=k-2\ge1\) for every subgroup. Compose the prescribed vertex planes with the \(G_{\mathcal P}\)-equivariant retraction onto \(S(H_T)\), apply Lemma 2, and include that sphere back into \(\mathcal U_T\). To preserve the *original* vertex planes, use the canonical equivariant deformation paths from each given vertex plane to its retraction image as short collars at the vertices, followed by the extension on the complementary cell; equivalently apply the relative equivariant homotopy extension property to this finite invariant vertex set.

For centered-prefix switch planes, the positivity identity
\[
\langle T,Z_p(\pi)\rangle=\min(p,|B_1|)-p|B_1|/n>0
\]
holds for every full order \(\pi\) refining \(\mathcal P\) and every \(1\le p<n\). Thus any oriented plane spanned by two distinct switch prefixes belongs to \(\mathcal U_T\), irrespective of the coloring. Under any relabeling symmetry of the entire coloring, the switch-plane labeling is equivariant. QED.

**Theorem 4 (sharpness at two blocks).** For \(k=2\), the surplus in (1) vanishes identically. In particular for the full block symmetry \(G_{\mathcal P}\), the fixed cell \(D_{\mathcal P}^{G_{\mathcal P}}\) is a point whereas the fixed target sphere \(S(H_T)^{G_{\mathcal P}}\) is empty. Hence there exist equivariant nonzero vertex plane labelings which admit no equivariant extension over the two-block cell. Independently, the previously established variable-rank straddling-switch constructions have boundary maps of degree \(\pm1\) in \(S(H_T)\), exhibiting nonextendibility for prescribed natural boundary interpolations. Thus \(k=3\) is the precise threshold for unconditional parabolic-equivariant filling.

*Proof.* For \(K=G_{\mathcal P}\), each ordered block is one orbit, so \(r(K)=k=2\). Lemma 1 gives \(\dim D^K=0\) and \(\dim H_T^K=0\). Vertex stabilizers are trivial under the natural blockwise relabeling action, so choose a base vertex plane in \(\mathcal U_T\) and propagate it to every vertex by the group; this gives a valid equivariant nonzero labeling. An extension would have to map the cell barycenter, fixed by the whole group, into \(\mathcal U_T^G\), which is empty by its sphere retraction and the fixed-plane frame description. QED.

**Proposition 5 (off-residue triples remove the tetrahedral Klein symmetry).** Let \(A\) be a four-element variable block in a boundary 3-tournament, and let \(z\notin A\) be any outside symbol fixed by relabeling \(A\). The colors of the unused triples \((a,z,c)\), \(a,c\in A\), define an ordinary tournament on \(A\). Its symmetry stabilizer inside \(S_A\) has odd order, hence is either trivial or cyclic of order three. Define skew signs \(\varepsilon_{ac}=(-1)^{b(a,z,c)}=-\varepsilon_{ca}\) and score vector
\[
s_a=\sum_{c\in A\setminus\{a\}}\varepsilon_{ac}.
\]
Every entry \(s_a\) is odd, so \(s=(s_a)_{a\in A}\in W_A\setminus\{0\}\). The assignment is equivariant under relabeling and changes sign under global complementation of the triple colors. In particular the Klein four-group cannot stabilize the full coloring neighborhood.

If, for a rank-three tetrahedral cell, the vertex tensors are contained in \(L=\Lambda^2(\mathbb RT\oplus W_A)\setminus\{0\}\), and the boundary rank-two filling is equivariant under the stabilizer of the full coloring neighborhood, then it extends equivariantly inside \(L\setminus\{0\}\), despite the Klein-group fixed-point obstruction for the restricted cell data.

*Proof.* An involution of four symbols swaps some pair \(a,c\), taking \((a,z,c)\) to its reversal. Invariance would contradict \(b(c,z,a)=1-b(a,z,c)\). An even-order subgroup contains an involution, so a stabilizer has odd order; the only possible odd orders of subgroups of \(S_4\) are one and three. The score assertions follow from summing three signs and antisymmetry. For the filling statement, the trivial stabilizer presents no obstruction because \(L\setminus\{0\}\simeq S^5\) is 2-connected and the rank-three cell is a three-ball. If the stabilizer is \(C_3\), its fixed locus in the tetrahedral permutahedron is a line segment, while \(L^{C_3}\) has dimension two: the real four-symbol standard representation decomposes under \(C_3\) as one fixed line plus one rotation plane, and \(L\) has one fixed line in each of \(T\wedge W_A\) and \(\Lambda^2W_A\). Therefore the fixed target sphere is \(S^1\), connected, permitting extension along the fixed interval. All remaining cell orbits have trivial stabilizer, and extend because \(\pi_0,\pi_1,\pi_2(S^5)=0\). This extends the boundary map equivariantly. QED.

**Boundary of the result.** These are *individual-cell* extension theorems. The extensions obtained independently for neighboring cells need not agree on their common faces, because their associated positive-prefix transversal vectors \(T\) differ. Nothing here constructs the globally coherent odd Grassmannian map that the original conjectures would rule out; it isolates the obstruction in intercell compatibility and in the top two-block residues, rather than in the isolated rank-three parity configuration.
