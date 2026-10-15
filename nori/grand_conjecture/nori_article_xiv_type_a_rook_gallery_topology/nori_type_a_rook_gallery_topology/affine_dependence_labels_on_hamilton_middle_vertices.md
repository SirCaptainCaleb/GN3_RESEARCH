# Affine dependence labels on Hamilton middle vertices

# Affine dependence labels on Hamilton middle vertices

A boundary-tournament word transforms under reversal by complemented reversal. A word alone may consequently be fixed by opposition. Placing an affine-dependence certificate on the middle vertices of its Hamilton path converts this symmetry into a free antipodal action on one global type-A target. Shared triple incidences then provide compatible carriers.

Let \(V\) have \(n\ge7\) vertices, and let \(b(a,h,c)\in\mathbb F_2\) satisfy only
\[
b(c,h,a)=1-b(a,h,c).
\]
Suppose provisionally that every Hamilton ordering has at least two switches. Write \(m=n-2\). For a Hamilton ordering \(\pi=(v_1,\ldots,v_n)\), put
\[
s_j(\pi)=(-1)^{b(v_j,v_{j+1},v_{j+2})},\qquad 1\le j\le m.
\]
Use the affine-dependence vector
\[
z(s)=\sum_{\substack{i<j<k\\s_i=s_k=-s_j}}
s_i\bigl((k-j)e_i-(k-i)e_j+(j-i)e_k\bigr).
\tag{1}
\]
As proved in the preceding subsection, \(z(s)\ne0\), every entry has strict sign \(s_j\), both \(\sum_jz_j\) and \(\sum_jjz_j\) vanish, and
\[
z(-\operatorname{rev}s)=-\operatorname{rev}z(s).
\tag{2}
\]

Let
\[
W=\{q\in\mathbb R^V:\sum_{v\in V}q_v=0\},\qquad
Z=\{q\in S(W):q\text{ has at least two zero entries}\}.
\tag{3}
\]
Define the flag label
\[
\boxed{\ell(\pi)=
\frac{\sum_{j=1}^{m}z_j(s(\pi))e_{v_{j+1}}}
{\|z(s(\pi))\|}\in Z.}
\tag{4}
\]

**Theorem 1 (faithful odd flag labeling).** The label (4) is defined on every complete Hamilton ordering and satisfies
\[
\boxed{\ell(\pi^{\mathrm{rev}})=-\ell(\pi).}
\tag{5}
\]
Its two zero entries are the first and last vertices of the ordering. Each middle vertex has strict sign equal to the sign of its triple color.

*Proof.* The distinct middle vertices receive nonzero coefficients, and the sum of those coefficients is zero. This proves membership in \(S(W)\), with zeros at the endpoints. Reversal sends the sign word to \(-\operatorname{rev}s\) and reverses the list of middle vertices. Equation (2) therefore negates the vector in (4), proving (5). \(\square\)

The moving placement on middle vertices is part of the original Hamilton ordering. No additional root or restriction on the boundary tournament is introduced.

**Theorem 2 (the global sparse target).** \(Z\) is an antipodally invariant finite cell complex of dimension \(n-4\), and is \((n-5)\)-connected. It admits an odd continuous map to \(S^{n-4}\).

*Proof.* The type-A root polytope is
\[
R=\operatorname{conv}\{e_u-e_v:u\ne v\}\subset W.
\]
Its boundary is given by \(\sum_{q_v>0}q_v=1\). For disjoint nonempty \(A,B\subseteq V\), the face with positive support in \(A\) and negative support in \(B\) is
\[
\Delta_A\times\Delta_B
\]
of dimension \(|A|+|B|-2\). Radial projection identifies the part with at least two zero entries with the \((n-4)\)-skeleton of \(\partial R\cong S^{n-2}\). This proves the dimension assertion. Attaching the remaining cells cannot change homotopy groups through degree \(n-5\); those groups vanish in the sphere. Hence \(Z\) is \((n-5)\)-connected.

Antipodality exchanges the faces indexed by \((A,B)\) and \((B,A)\). On the barycentric subdivision, choose a sign for one face in each antipodal pair and assign opposite signs to its partner. Label a face of dimension \(r\) by its chosen sign times \(e_{r+1}\). Face-chain dimensions strictly increase, so this extends simplicially to the boundary of the \((n-3)\)-crosspolytope, giving the asserted odd map. \(\square\)

## Carriers from invariant middle-vertex colors

Let \(X\cong S^{n-2}\) be the dual type-A Coxeter cellulation of the simplex flag sphere. Its vertices are Hamilton orders, and its edges exchange adjacent entries. Opposition is reversal of the order.

For a closed dual cell \(D\), let \(A_D\) and \(C_D\) be the sets of vertices that occur first and last, respectively, in its flags. They are disjoint: a proper parabolic residue permutes entries within consecutive position blocks, and its first and last blocks differ. Let
\[
B_D=V\setminus(A_D\cup C_D).
\]
For \(h\in B_D\), its triple color is the color of the unique consecutive triple centered at \(h\) in a given flag. Let \(H_D\subseteq B_D\) consist of those vertices for which this color is constant throughout \(D\), and denote their signs by \(\sigma_h(D)\).

Define
\[
\boxed{
\mathcal C_D=
\bigcup_{\substack{a\in A_D\\c\in C_D}}
\{q\in S(W):q_a=q_c=0,\ 
\sigma_h(D)q_h\ge0\text{ for every }h\in H_D\}.
}
\tag{6}
\]
Every label of \(D\) belongs to this subset of \(Z\). If \(D'\) is a face of \(D\), its endpoint sets shrink, its invariant middle-vertex set grows, and the inherited signs agree. Hence
\[
\mathcal C_{D'}\subseteq\mathcal C_D.
\tag{7}
\]
Opposition negates these carriers.

**Theorem 3 (contractible carriers and the complete one-skeleton).** Carrier (6) is contractible whenever \(H_D\) contains vertices of both colors. It is also contractible for every dual edge. Consequently (4) extends equivariantly over the subcomplex consisting of all dual edges and all closed dual cells with invariant middle vertices of both colors.

*Proof.* Suppose \(h,k\in H_D\) have opposite signs. The vector
\[
v=\sigma_h(D)(e_h-e_k)/\sqrt2
\]
belongs to every piece of the union (6). It satisfies the sign inequalities, with positive prescribed sign at \(h\), and vanishes at every candidate endpoint. Thus \(-v\) is excluded from the carrier. Normalized linear interpolation to \(v\) contracts each piece and, using the same \(v\) for all pieces, the whole union.

Now let \(D\) be an edge. Exchanging adjacent positions affects at most four consecutive triple windows. Since \(m=n-2\ge5\), at least one triple is unchanged, and its middle vertex belongs to \(H_D\). If both colors occur in \(H_D\), the preceding contraction applies.

Otherwise all \(\sigma_h(D)\) equal a sign \(\sigma\). We claim \(B_D\setminus H_D\ne\varnothing\). For an interior exchange, the endpoints stay fixed, so \(B_D\) is the set of all middle vertices. If every such vertex had the same invariant color, both words would be constant. For an exchange involving an endpoint, \(B_D\) comprises all middle vertices except the first or last one, respectively. If all of them had the same invariant color, each complete word would have at most one switch. Both alternatives contradict the hypothesis. This proves the claim.

Choose \(h\in H_D\) and \(k\in B_D\setminus H_D\). The vector \(v=\sigma(e_h-e_k)/\sqrt2\) again belongs to every piece of (6); all other constrained entries are zero. Its negative violates the constraint at \(h\). The same interpolation contracts the carrier.

Having invariant vertices of both colors is inherited by cell faces. Together with the whole one-skeleton, these cells therefore form an opposition-invariant subcomplex. Equations (7) and (5) give a nested equivariant acyclic carrier. Extend the prescribed vertex labels inductively over cells inside their contractible carriers, using antipodal cell pairs. \(\square\)

The edge argument uses the unchanged **ordered triple**, rather than word symmetry alone. It applies to every unrestricted reversal-odd boundary tournament.

**Corollary 4 (a boundary primary obstruction).** The map extends equivariantly over the union of that subcomplex with \(X^{(n-4)}\). After composition with the odd map \(Z\to S^{n-4}\) from Theorem 2, its degree obstruction on the \((n-3)\)-cells represents
\[
\boxed{u^{n-3}\ne0
\in H^{n-3}(\mathbb RP^{n-2};\mathbb F_2).}
\tag{8}
\]
Some degree-contributing cell therefore has no pair of invariant middle vertices with opposite colors.

*Proof.* Connectivity of \(Z\) permits filling every remaining cell through dimension \(n-4\), while retaining the existing carrier map. Composition gives an odd map to \(S^{n-4}\) on this domain. Its primary mod-two obstruction is the top Stiefel-Whitney class of \((n-3)\gamma\), namely \(u^{n-3}\). The quotient of the type-A opposition sphere is \(\mathbb RP^{n-2}\), where this class is nonzero. Every cell with opposite-colored invariant middle vertices is already filled, proving the localization. \(\square\)

**Relation to the cube construction.** Both constructions begin with the same positive affine dependence of a complete color word with at least two switches. Cube antipodality negates its fixed position vector. Boundary reversal negates the vector after placement on the ordering's middle vertices. Both give a fixed free target with dimension below the corresponding complete-path sphere and compatible color-sensitive fillings on source cells. They retain dimension-simple cube geodesics and vertex-simple Hamilton paths in the source.

The remaining obligations are the unfilled primary cells: full positional variation for the cube construction, and the absence of two opposite-colored invariant centers for the boundary construction. The results establish labels and coherent portions of the chain maps for both unrestricted models; neither gives the final cancellation of the primary obstruction.
