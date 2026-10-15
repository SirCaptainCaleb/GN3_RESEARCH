# Boundary reversal oddness fills every rank-two switch-wedge residue

### Boundary reversal oddness fills every rank-two switch-wedge residue

Let \(n\ge5\) and let \(b\) be an arbitrary reversal-odd binary coloring of ordered distinct triples. For a Hamilton order \(\pi\) with first and last switch positions \(j<k\), put \(E(\pi)=Z_{j+1}(\pi)\wedge Z_{k+1}(\pi)\).

**Theorem 1 (rank-two convex fillings).** Let \(D\) be any dual type-A Coxeter rank-two cell (commuting square or braid hexagon). If every Hamilton order at its vertices has at least two switches, then
\[
\boxed{0\notin\operatorname{conv}\{E(\pi):\pi\in V(D)\}.}
\tag{1}
\]

*Proof.* The sharp universal carrier theorem handles every commuting square and every braid hexagon other than permutations of the first or last three symbols. Global reversal negates the wedges, so consider the six orders obtained by permuting \(a,b,c\) before a fixed suffix \(d,e,\ldots,z\).

Let \(A=\{a,b,c\}\). On exterior matrices define \(\ell(U)=\sum_{t\in A}U_{t,z}\). For every permitted switch-prefix pair \(2\le p<q\le n-2\),
\[
\boxed{\ell(Z_p\wedge Z_q)=
\frac{p\min(q,3)-q\min(p,3)}n\le0,}
\tag{2}
\]
with equality only for \(p=2,q=3\). Suppose zero belongs to the convex hull in (1). In any zero convex combination, positive weights can occur only on flags with switch-prefix pair \((2,3)\). Their words have the form \((C,1-C,C,C,\ldots,C)\). The associated wedges depend only on the third entry of the first three symbols. Write them \(U_a,U_b,U_c\). They satisfy \(U_a+U_b+U_c=0\) and are pairwise noncollinear. Therefore a zero convex combination needs at least one flag with each third entry.

For \(n\ge6\), the fourth and subsequent color bits are common to all six flags, so the three selected words share a tail color \(C\). Their first triples all have color \(C\). Reversal oddness forbids selecting a triple together with its reverse. The three selected permutations must consequently form one of the two directed three-cycles \((a,b,c),(b,c,a),(c,a,b)\), or its reverse cycle. The other three permutations have first triple color \(1-C\). Since the selected permutations have all three possible third entries, every third and subsequent bit in all six flags is \(C\). Each of the three remaining words therefore has form \((1-C,t,C,C,\ldots,C)\) and hence just one switch, a contradiction.

For \(n=5\), every word has length three. If all six flags had two switches, their words would alternate. Writing \(C_t=b(t,d,e)\), this would force \(b(x,y,t)=C_t\) for every permutation \((x,y,t)\) of \(a,b,c\). Reversal oddness then forces \(C_a+C_b=C_b+C_c=C_c+C_a=1\) in \(\mathbb F_2\), impossible. Thus the final terminal-hexagon case is vacuous. \(\square\)

**Corollary 2 (full equivariant two-skeleton extension).** Suppose \(n\ge6\) and every Hamilton order has at least two switches. On the dual type-A Coxeter sphere \(X\), the labels \(E(\pi)\) extend to an antipodally equivariant continuous map
\[
\boxed{X^{(2)}\longrightarrow\Lambda^2W\setminus\{0\}.}
\tag{3}
\]
Indeed, assign each cell barycenter the arithmetic mean of its flag-vertex labels and interpolate affinely on a common barycentric triangulation of the two-skeleton. Theorem 1 ensures that the entire convex hull of every two-cell misses zero. Opposite flags have negative labels and opposite faces have corresponding averages, yielding equivariance.

**Scope.** The result handles every two-dimensional rank-exchange residue for the unrestricted boundary class under the hypothetical no-good-path condition. It preserves complete Hamilton orders. Higher-dimensional extensions and compression to a target of sufficiently small dimension remain open.
