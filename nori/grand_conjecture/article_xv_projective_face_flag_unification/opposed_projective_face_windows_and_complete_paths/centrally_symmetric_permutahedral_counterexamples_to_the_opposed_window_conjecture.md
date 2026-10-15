# Centrally symmetric permutahedral counterexamples to the opposed-window conjecture

# Centrally symmetric permutahedral counterexamples to the opposed-window conjecture

The proposed opposed projective-window one-switch assertion fails even when opposition is geometric central inversion and every observation is a well-defined projective two-face incidence. The obstruction occurs in arbitrarily large dimensions.

**Theorem 1.** For every integer \(d\ge5\) with \(d\equiv1,2\pmod4\), there is a centrally symmetric simple convex \(d\)-polytope \(P\), with its central involution \(J\) on the proper-face flag sphere and induced involution \(\rho\) on \(\mathscr I_2(P)\), and a coloring
\[
c:\mathscr I_2(P)\longrightarrow\mathbb F_2,\qquad
c(\rho I)=1-c(I),
\]
such that every maximal face flag satisfies
\[
\boxed{\operatorname{sw}(\mathsf w_2(\mathcal F))=d-2.}
\]
Thus the minimum switch count equals the largest possible switch count for a word of length \(d-1\). In dimension five the polytope has 720 vertices and every complete flag path has three switches.

We first isolate the coloring mechanism.

**Lemma 2 (bipartite middle-vertex coloring).** Let \(P\) be a centrally symmetric simple \(d\)-polytope whose graph has a bipartition \(\chi:V(P)\to\mathbb F_2\) satisfying \(\chi(-v)=1-\chi(v)\). Suppose no two distinct edges of any two-dimensional face are parallel. Then
\[
c\bigl(F(u,v,w),[v-u],[w-v]\bigr)=\chi(v)
\tag{1}
\]
defines a coloring of projective two-face observations. It is odd under central inversion, and its word alternates along every nonbacktracking graph walk.

*Proof.* In a fixed two-face, the direction line of an edge determines that edge by the nonparallelism assumption. An ordered pair of incident edges determines their common vertex and their ordered two-edge walk. Consequently an observation in (1) determines \(v\), so the assignment is well defined. Central inversion takes that observation to
\[
(-F,[v-u],[w-v]),
\]
whose middle vertex is \(-v\); the coloring is therefore odd. Successive windows have adjacent middle vertices, so their colors differ by the bipartition property. A complete flag path has \(d\) edges and hence \(d-1\) two-step observations, giving \(d-2\) switches. \(\square\)

We construct polytopes satisfying the lemma by perturbing a centrally symmetric permutahedron. All perturbations below are of facet normals, with opposite normals perturbed as opposite pairs.

**Lemma 3 (removing parallel edges within two-faces).** For every \(N\ge4\), the centered permutahedron on \(N\) symbols has arbitrarily small centrally symmetric simple realizations of the same face lattice in which no two distinct edges of a two-face are parallel.

*Proof.* Put \(d=N-1\) and
\[
W=\{z\in\mathbb R^N:\textstyle\sum_i z_i=0\}.
\]
The centered permutahedron is the convex hull of all permutations of
\[
\left(1-\frac{N+1}{2},\ldots,N-\frac{N+1}{2}\right).
\]
Its facet inequalities are
\[
\langle a_S,z\rangle\le h_S,\qquad
a_S=\mathbf1_S-\frac{|S|}{N}\mathbf1,\qquad
h_S=\frac{|S|(N-|S|)}2,
\tag{2}
\]
for nonempty proper \(S\subset[N]\). In particular \(a_{S^c}=-a_S\) and \(h_{S^c}=h_S\).

For completeness, these inequalities describe the displayed convex hull: maximizing a linear functional orders its entries, and summation by parts expresses its value using the corresponding successive subset sums, each bounded by (2). The permutation with the same ordering attains all these bounds. Equality in a facet inequality says that \(S\) receives the largest \(|S|\) entries of a permutation. Hence collections of facets meet precisely when their indexing subsets form a chain. A maximal chain has \(d\) members and determines one permutation vertex. Its normals are independent, so the polytope is simple. Deleting one member of a maximal chain interchanges two consecutive symbols in its vertex order.

Choose one representative of each complementary pair \(\{S,S^c\}\), and vary its normal freely in \(W\), assigning the negative variation to its mate. Keep the support numbers \(h_S\) fixed. There is an open neighborhood of the original normals in which the resulting polytope is bounded and has the same labeled face lattice. One way to see this is to take polars: the polar has vertices \(a_S/h_S\) and is simplicial, so sufficiently small perturbations preserve each facet and its strict separation from every remaining vertex. The central pairs remain opposite. Equivalently, every original simple vertex persists as the intersection of its \(d\) supporting hyperplanes, with strict inequalities at all other facets.

Now fix a two-face. It is contained in \(d-2\) facets indexed by a chain \(\mathcal C\). Every edge of this two-face is obtained by adding one facet indexed by a subset \(T\) comparable with all members of \(\mathcal C\). Distinct edges have distinct additional facets. Because \(d\ge3\), the chain \(\mathcal C\) is nonempty.

No complementary pair \(T,T^c\) can both be comparable with a nonempty proper subset \(S\). Indeed, placing both below \(S\) forces \(S=[N]\), placing both above \(S\) forces \(S=\varnothing\), and either mixed placement forces a nonempty set to be contained in its complement. Thus, for any two distinct edges in the two-face, their \(d-2\) common facets and their two additional facets belong to \(d\) distinct complementary facet pairs.

The corresponding \(d\) perturbed normals are therefore independently variable. Their determinant is a nonzero polynomial in the perturbation parameters. The two edges could be parallel only if this determinant vanished: a common edge direction would be orthogonal to all \(d\) normals. There are finitely many two-faces and edge pairs. The union of these determinant zero sets has empty interior, so a sufficiently small central perturbation avoids all of them simultaneously.

This also gives a rational realization if desired: the starting inequalities have rational coefficients in a rational basis of \(W\), and rational perturbations are dense in the open set obtained by excluding the finitely many determinant zero sets. \(\square\)

*Proof of Theorem 1.* Take \(N=d+1\) with \(N\equiv2,3\pmod4\), and choose \(P\) by Lemma 3. Label its vertices by their maximal chains of subsets, equivalently by permutations \(\pi\in S_N\). Its graph joins permutations differing by an adjacent transposition. Therefore
\[
\chi(v_\pi)=\operatorname{inv}(\pi)\pmod2
\tag{3}
\]
is a bipartition.

Central inversion sends every facet indexed by \(S\) to the facet indexed by \(S^c\). Taking complements and reversing a maximal chain reverses its permutation order. Consequently
\[
-v_\pi=v_{\pi^{\mathrm{rev}}},\qquad
\chi(-v_\pi)=\chi(v_\pi)+\binom N2
=\chi(v_\pi)+1\pmod2.
\tag{4}
\]
The face labels and this central action persist under the paired perturbation. Lemma 2 supplies the required coloring.

It remains to verify all opposition hypotheses. Central inversion induces a simplicial involution of the proper-face flag sphere. It is free: a proper face of a centrally symmetric polytope cannot equal its negative, since a supporting functional is positive on that face and negative on its opposite. A setwise invariant flag would fix its face at every rank, which is impossible. Likewise
\[
\rho(F,L_1,L_2)=(-F,L_1,L_2)
\tag{5}
\]
is a fixed-point-free involution of \(\mathscr I_2(P)\), since each two-face is proper. Central inversion commutes with the unique exiting-edge rule defining complete flag paths. Thus the observations of \(J\mathcal F\) are the \(\rho\)-images of those of \(\mathcal F\), in the same position order. All requirements of an opposed projective-window system hold.

Every complete flag path remains vertex-simple and has linearly independent successive displacements, as follows inductively from its successive containing faces. Its observation word nevertheless alternates by Lemma 2. For \(d=5\), \(N=6\), giving \(6!=720\) vertices and \(d-2=3\) switches. The permitted values of \(d\) are unbounded. \(\square\)

**Consequence for the common formulation.** The counterexamples satisfy full path independence, all simple-polytope flag exchanges, geometric antipodality, and projective-incidence descent. The latter condition can become injective on ordered two-edge walks after a central perturbation that preserves the entire labeled face lattice. Thus it imposes no identification capable of excluding the bipartite middle-vertex coloring in these realizations.

More generally, in any centrally symmetric bipartite graph where opposition exchanges the bipartition classes, this coloring descends whenever every observation identifies middle vertices of just one bipartition class. Any universal one-switch principle using these observations must exclude that situation or impose an additional condition that prevents its coloring. The original cube-edge and simplex-turn problems remain unresolved: the present construction concerns centrally opposed two-step observations on perturbed permutahedra, and supplies a refutation of the enlarged assertion of this article.
