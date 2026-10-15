# Primary-cell antipodal separation and obstruction parity

# Antipodal separation of local edge data and the global degree obstruction

Let \(n\ge5\), \(X\cong S^{n-1}\) be the dual type-\(B_n\) Coxeter cell complex, and write \(s_0,\ldots,s_{n-1}\) for its simple chamber changes. For a dual cell \(D=gW_J\), let \(E(D)\) be the set of undirected cube edges traversed by all rooted full antipodal geodesics corresponding to its chamber vertices. Write \(\bar E(D)=\{\bar e:e\in E(D)\}\).

## Primary-cell separation

**Theorem 1 (no antipodal edge pairs inside a primary cell).** For every dual Coxeter cell \(D=gW_J\) of dimension \(n-2\),
\[
E(D)\cap\bar E(D)=\varnothing.
\tag{1}
\]
Consequently any function \(h:E(D)\to\mathbb F_2\) extends to an antipodally odd coloring of all undirected cube edges. Thus antipodal oddness itself imposes no constraints within the family of complete geodesics carried by an individual primary obstruction cell; their only intra-cell constraints are shared-edge identifications.

*Proof.* There are \(n\) simple generators, so \(J\) omits two generators. We distinguish whether \(s_0\) is omitted.

If \(0\notin J\), the initial cube vertex \(x\) is fixed. The other omitted generator is some \(s_k\), \(1\le k\le n-1\). Every order is a concatenation of two nonempty dimension blocks \(A,B\), with \(A\) preceding \(B\) in every order and the entries within each block permuted independently. On every edge traversed in a dimension of \(A\), the bits in all dimensions of \(B\) still equal their starting values at \(x\). On every edge in a dimension of \(B\), the bits in all dimensions of \(A\) have already been flipped and therefore equal the complementary starting values at \(x\). Since antipodal edges have the same dimension but opposite bits in *all other* dimensions, neither an \(A\)-edge nor a \(B\)-edge can have its antipodal mate in \(E(D)\).

If \(0\in J\), the two omitted generators are \(s_a,s_b\), with \(1\le a<b\le n-1\). The dimension order is partitioned into three nonempty consecutive blocks \(A,B,C\), with these blocks occupying positions \(1,\ldots,a\), \(a+1,\ldots,b\), and \(b+1,\ldots,n\). The parabolic group permits arbitrary permutation and initial-root sign changes on dimensions of \(A\), but the initial bits in \(B\cup C\) remain fixed throughout the cell. On an edge in \(A\), all \(B\)-bits remain at their common initial values; on an edge in \(B\), all \(C\)-bits remain at their common initial values; on an edge in \(C\), all \(B\)-bits have their common complemented initial values. Because the comparison block used in each case is nonempty and disjoint from the direction of the edge, the antipodal mate of that edge cannot occur elsewhere within \(E(D)\). This proves (1).

Given \(h\) on \(E(D)\), color the antipodal mates \(\bar e\) with \(1-h(e)\), and choose complementary values independently on every remaining antipodal edge orbit. Equation (1) makes the extension well defined. \(\square\)

**Interpretation.** The result holds for both the root-fixed and root-changing primary cells, including the mixed-star cells remaining after the all-position color-anchor theorem. It does not say that arbitrary assignments are compatible with the *global no-monochromatic-geodesic hypothesis*: the extension can create monochromatic full geodesics in other cells. In particular, any final cancellation proof must exploit relations across different parabolic cells or global consequences of that hypothesis. Applying antipodal oddness within a single primary cell cannot supply a missing local parity equation.

## An odd global obstruction parity

Retain the hypothetical assumption that *no* monochromatic antipodal geodesic exists. Then the signed second-switch label on complete geodesic chambers is defined, odd, and nonopposite on adjacent chambers. The color-anchor construction extends it equivariantly over the subcomplex \(X_{\mathrm{anc}}\) of cells with a common first color or a common later-position color, and over the entire \((n-3)\)-skeleton. Denote such an extension by \(F\), with target \(S^{n-3}\). Write \(\bar X=X/(\pm1)\cong\mathbb RP^{n-1}\).

For a dual \((n-2)\)-cell \(D\), define its mod-two attaching degree
\[
o_F(D)=\deg_2\bigl(F|_{\partial D}:\partial D\cong S^{n-3}\to S^{n-3}\bigr)\in\mathbb F_2.
\tag{2}
\]
It is well defined on an antipodal cell orbit, as orientation does not affect degree modulo two. On an anchored cell, \(F\) already extends over \(D\), so \(o_F(D)=0\).

**Theorem 2 (global obstruction parity).** Let
\[
Z=\sum_{[D]}\epsilon_D[D]
\]
be any cellular \((n-2)\)-cycle representing the nonzero class of
\[
H_{n-2}(\bar X;\mathbb F_2)\cong\mathbb F_2.
\]
Then
\[
\boxed{
\sum_{\substack{[D]\ {\rm unanchored}\\\dim D=n-2}}
\epsilon_D\,o_F(D)=1\pmod2.
}
\tag{3}
\]
Thus the obstruction is not merely supported on some exceptional cells: its **total contribution over an appropriate projective homology cycle is odd**.

*Proof.* The primary obstruction to extending an equivariant map from the \((n-3)\)-skeleton of the antipodal sphere \(S^{n-1}\) into \(S^{n-3}\) reduces modulo two to
\[
w_1^{n-2}\in H^{n-2}(\mathbb RP^{n-1};\mathbb F_2),
\tag{4}
\]
where \(w_1\) is the first Stiefel–Whitney class of the antipodal double covering. It is the nonzero generator in degree \(n-2\), since the cohomology ring is \(\mathbb F_2[w_1]/(w_1^n)\). The cellular cocycle representing this primary obstruction assigns to each \((n-2)\)-cell the attaching-map degree (2). Evaluation on the nonzero homology class \([Z]\) is therefore one. Anchored cells contribute zero, yielding (3). \(\square\)

## A precise Wu–Yang-type proof obligation

Equation (3) supplies a quantitative chain target. To contradict the hypothetical absence of a monochromatic full geodesic, it suffices to construct a color-sensitive pairing or mod-two boundary identity showing that the total number of degree-contributing exceptional cells in a projective generator \(Z\), counted with their coefficients, is even. Such a pairing must involve **more than one primary cell**: Theorem 1 shows that the antipodal edge-color relation is invisible within each cell on its own.

One possible chain-level route is to choose compatible subdivisions and evaluate each degree by counting preimages of the interior of a fixed top-dimensional crosspolytope facet. The needed argument would pair those preimages globally through shared-edge and full-rank dimension-exchange relations, analogous to Wu–Yang's dependent-radial cancellation. No such global pairing is established here; (3) is a necessary topological obstruction, not a proof of NORI1.
