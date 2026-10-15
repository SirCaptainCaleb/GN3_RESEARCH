# Bi-monochromatic interval exclusion and an equivariant sphere of codimension three

Let \(n\ge5\) and let \(c:E(Q_n)\to\mathbb F_2\) be an arbitrary antipodally odd coloring. For \(a\in\{0,1\}\), let \(P_a(c)\) be the monochromatic geodesic endpoint poset defined earlier in this Article: its elements are oriented endpoint pairs \((u,v)\) with a color-\(a\) geodesic between them, ordered by monochromatic, support-disjoint endpoint extensions. In the universal oriented-interval torus \(X_n\), put
\[
K_a=\Delta P_a(c),\qquad K=K_0\cup K_1,\qquad I=K_0\cap K_1.
\tag{1}
\]
All are simplicial subcomplexes of the same barycentric subdivision. On oriented pairs define
\[
A(u,v)=(\bar u,\bar v),\quad J(u,v)=(v,u),\quad R=AJ.
\tag{2}
\]
The first involution exchanges \(K_0,K_1\), endpoint reversal preserves each, and therefore \(R(K_0)=K_1\), \(R(I)=I\), and \(R(K)=K\). The rank of an endpoint pair is its Hamming distance.

**Theorem 1 (two-color near-spanning closure).** Suppose distinct cube vertices \(u,v\) have Hamming distance \(n-2\), and there exist both a red geodesic and a blue geodesic joining \(u\) to \(v\). Then \(c\) admits a monochromatic full antipodal geodesic.

More generally, if \(d(u,v)=n-k\), \(1\le k\le n-1\), and there are monochromatic geodesics of both colors joining \(u\) to \(v\), then there is a complete antipodal geodesic with at most \(k-1\) switches.

*Proof.* Let \(D\subseteq[n]\) be the set of dimensions in which \(u,v\) differ, and let \(i_1,\dots,i_k\) be an arbitrary ordering of the unused dimensions. Put \(b=c(\{v,v\oplus e_{i_1}\})\). Choose a color-\(b\) geodesic from \(u\) to \(v\), possible by hypothesis, then traverse \(i_1,\dots,i_k\). The resulting path goes from \(u\) to \(\bar u\) and uses every dimension once. Its first \(n-k+1\) edges have color \(b\); only the remaining \(k-1\) edges can introduce switches. For \(k=2\), the full word has at most one switch. The established cyclic root-slide identity transforms every full word with at most one switch into a monochromatic full word (possibly at a different root). \(\square\)

**Corollary 2 (sharp two-color rank exclusions).** Suppose, toward a contradiction, that \(c\) has no monochromatic full antipodal geodesic. Then:
\[
\begin{array}{ll}
\text{(i)}&\text{Every vertex of \(K\) has rank at most \(n-2\).}\\
\text{(ii)}&\text{Every vertex of \(I\) has rank in \(\{2,\dots,n-3\}\).}
\end{array}
\tag{3}
\]
Consequently
\[
\boxed{\dim K\le n-3,\qquad \dim I\le n-5.}
\tag{4}
\]
The rank-one exclusion in (ii) holds for every coloring, because a single undirected cube edge has only one color.

*Proof.* The near-spanning extension lemma of Article XIV says that a monochromatic length-\((n-1)\) geodesic extends to a full monochromatic geodesic: the two unused-direction edges incident with its endpoints form an antipodal pair and have complementary colors. This excludes ranks \(n-1,n\), proving (i). A vertex of \(I\) belongs to both monochromatic endpoint posets and therefore supports both colors of geodesics between the same endpoints. Rank one is impossible, and rank \(n-2\) is excluded by Theorem 1. Rank is strictly increasing along any nonconstant chain of the endpoint poset, so the number of available ranks bounds simplex dimension as in (4). \(\square\)

**Theorem 3 (explicit low-dimensional odd map on the bi-monochromatic intersection).** Under the hypotheses of Corollary 2, there is a simplicial \(R\)-equivariant map
\[
\boxed{\lambda:I\longrightarrow
\partial\operatorname{Crosspolytope}_{n-4}\cong S^{n-5},}
\tag{5}
\]
where \(R\) acts as the antipodal involution on the target.

For every vertex \(p=(u,v)\) of \(I\), let \(r(p)=d(u,v)\) and let \(i(p)\) be the least dimension for which \(u_i=v_i\). Define
\[
\boxed{\lambda(p)=(-1)^{u_{i(p)}}e_{r(p)-1},
\qquad 2\le r(p)\le n-3.}
\tag{6}
\]

*Proof.* The unused dimension \(i(p)\) exists since \(r(p)\le n-3\). If \(p\preceq q\) within a simplex of \(I\), their ranks differ unless they coincide. Thus the labels of distinct simplex vertices lie on distinct target axes \(e_1,\dots,e_{n-4}\), so they span a simplex of the crosspolytope boundary. Under \(R(u,v)=(\bar v,\bar u)\), rank and unused dimension set are unchanged, while the common bit at \(i(p)\) is complemented. Therefore \(\lambda(Rp)=-\lambda(p)\), establishing equivariance. \(\square\)

**Theorem 4 (sphere suspension for the entire two-color endpoint complex).** Under the same hypotheses there exists a continuous \(R\)-equivariant map
\[
\boxed{F:K_0\cup K_1\longrightarrow S^{n-4}.}
\tag{7}
\]
In particular the free-involution index of \(K\) is at most \(n-4\), and if \(\alpha=w_1(K\to K/R)\) then
\[
\boxed{\alpha^{n-3}=0\quad\text{in }H^{n-3}(K/R;\mathbb F_2).}
\tag{8}
\]

*Proof.* View \(S^{n-4}\) as the suspension of the equatorial \(S^{n-5}\). The closed upper hemisphere is contractible. Since \(I\subseteq K_0\) is a subcomplex of a finite simplicial complex, the map \(\lambda:I\to S^{n-5}\) extends over \(K_0\) to a continuous map
\[
F_0:K_0\longrightarrow D^{n-4}_{+}\subset S^{n-4}
\]
that restricts to \(\lambda\) on the equator. Such an extension follows by cellular induction into the contractible hemisphere. Define \(F=F_0\) on \(K_0\), and
\[
F(x)=-F_0(Rx),\qquad x\in K_1.
\]
For \(x\in I\), both prescriptions agree because \(\lambda(Rx)=-\lambda(x)\). They therefore glue to a continuous map on \(K\), and by construction \(F(Rx)=-F(x)\). This proves (7). Under the absence of a full monochromatic geodesic, \(R\) has no fixed points on \(K\) by the fixed-center Lefschetz characterization proved previously. The equivariant map descends to \(K/R\to\mathbb RP^{n-4}\), pulling back the universal degree-one class to \(\alpha\). Its \((n-3)\)-rd power vanishes on the target, proving (8). \(\square\)

**An intrinsic obstruction problem.** The free reversal carrier \(M_n\) of Article XV, equivariantly modeled by the punctured torus of the preceding Subsection, has covering class \(\beta\) satisfying \(\beta^{n-1}\ne0\), hence \(\beta^{n-3}\ne0\). If the absence of monochromatic full geodesics supplied any \(R\)-equivariant continuous map
\[
M_n\longrightarrow K,
\tag{9}
\]
then composition with (7) would give an equivariant map \(M_n\to S^{n-4}\), contradicting the nonzero \(\beta^{n-3}\). Thus (9) is a sufficient condition for NORI1, and the missing transfer is now a map to a target **three dimensions below** the ambient carrier's \((n-1)\)-sphere links.

Theorem 4 is a new color-sensitive reduction and does not itself construct (9). The suspension extension is topological: it makes no claim that its image remembers individual geodesic witnesses after projection, whereas the posets \(K_0,K_1\) retain those witnesses intrinsically. In particular, pointwise low-switch Freudenthal coverage is not a prerequisite for (7), avoiding the spanning-tree obstruction proved in the immediately preceding subsection of this Article.
