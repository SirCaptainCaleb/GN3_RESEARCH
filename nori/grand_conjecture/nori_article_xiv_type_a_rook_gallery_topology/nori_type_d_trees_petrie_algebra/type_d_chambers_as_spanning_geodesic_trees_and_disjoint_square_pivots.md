# Type-D chambers as spanning geodesic trees and disjoint square pivots

# Type-D chambers as spanning geodesic trees and disjoint square pivots

Every open chamber of the type-\(D_n\) arrangement canonically determines a spanning tree of the cube. All rooted Freudenthal maximal simplices containing a point of this chamber are the unique full antipodal paths in that same tree. Adjacent chambers correspond to simultaneous, disjoint square-edge pivots. These facts provide a dimension-simple exchange model, without extra coloring hypotheses.

Fix \(n\ge3\). Write \(t_i=2z_i-1\) for a geometric cube point outside all walls \(t_i=\pm t_j\). A type-\(D_n\) chamber determines an absolute-value order
\[
|t_{i_1}|<|t_{i_2}|<\cdots<|t_{i_n}|
\tag{1}
\]
and the signs of \(t_{i_2},\ldots,t_{i_n}\). The sign of the smallest entry \(t_{i_1}\) may change inside the same chamber. Let \(g\) be a cube vertex agreeing with the signs of \(t_{i_r}\) for \(r\ge2\) (bit one for positive sign) and choose either bit for \(g_{i_1}\). Define a graph \(T_z\) with edge set
\[
\boxed{E(T_z)=\bigcup_{r=1}^n
\left\{\{g\oplus\mathbf1_S,\,
g\oplus\mathbf1_{S\cup\{i_r\}}\}:S\subseteq\{i_1,\ldots,i_{r-1}\}\right\}.}
\tag{2}
\]

**Theorem 1 (common spanning tree and central edge).** The graph \(T_z\) is a spanning tree with \(2^{r-1}\) edges in direction \(i_r\), independent of the choice of \(g_{i_1}\). For every root \(x\), the unique maximal rooted Freudenthal simplex containing \(z\) is the vertex chain of the unique tree path \(x\to\bar x\). Consequently all these paths are complete dimension-simple geodesics, and all contain the same undirected edge
\[
\boxed{e_*=\{g,g\oplus e_{i_1}\}.}
\tag{3}
\]

*Proof.* For a vertex \(v\ne g\), choose the largest rank \(r\) at which \(v\) and \(g\) differ. The edge from \(v\) that flips \(i_r\) belongs to (2) and reduces the number of differing bits by one. Every vertex has one such parent, so the resulting graph connects all vertices to \(g\) without cycles. Formula (2) gives \(2^{r-1}\) edges at rank \(r\). If \(g_{i_1}\) is changed, the choices of \(S\) with and without \(i_1\) are exchanged for every rank \(r>1\), and the rank-one edge remains the same undirected edge. This proves the first assertions.

For a root \(x\), the descending order of the signed distances
\[
d_i^x(z)=\frac{1+(-1)^{x_i}t_i}{2}
\]
is: all directions of rank greater than one where \(x\) differs from \(g\), in descending rank; then \(i_1\); then all greater-ranked directions where \(x\) agrees with \(g\), in ascending rank. The sign of \(t_{i_1}\) does not change this ordering, since \(|t_{i_1}|\) is least. The stated order is also the unique tree path from \(x\) to \(g\), deleting its differing directions in descending rank, followed by the unique tree path from \(g\) to \(\bar x\), adding their complementary directions in ascending rank. The two portions have disjoint dimension sets and use all \(n\) directions once. Thus they form the Freudenthal maximal simplex containing \(z\). Finally, direction \(i_1\) occurs once in every such antipodal path, while (2) contains only one tree edge in that direction. This edge is (3). \(\square\)

**Theorem 2 (bijection with type-D chambers).** The map from type-\(D_n\) chambers to trees (2) is injective. Its image consists of
\[
\boxed{2^{n-1}n!}
\tag{4}
\]
distinct spanning trees, naturally indexed by a total order of dimensions and the sign choices at all but the smallest rank.

*Proof.* In the tree, each direction appears a distinct number of times, namely \(1,2,4,\ldots,2^{n-1}\). These counts recover the total rank order \(i_1,\ldots,i_n\). The unique first-rank edge (3) fixes the vertex bits in every other direction and therefore recovers the higher-rank signs. Those data specify one type-\(D_n\) chamber. There are \(n!\) choices of order and \(2^{n-1}\) higher-rank sign assignments. \(\square\)

**Theorem 3 (disjoint square-pivot law).** Suppose two type-\(D_n\) chambers are adjacent across a wall that interchanges consecutive absolute-value ranks \(r,r+1\), occupied by directions \(i,j\). Put \(L=\{i_1,\ldots,i_{r-1}\}\), and choose the same \(g\) for both chamber trees, agreeing with all signs on the wall. The two spanning trees differ only on the \(2^{r-1}\) vertex-disjoint cubical squares
\[
F_S=\{g\oplus\mathbf1_{S\cup U}:U\subseteq\{i,j\}\},
\quad S\subseteq L,
\tag{5}
\]
with higher-ranked bits fixed. Both trees contain the two square edges from \(g\oplus\mathbf1_S\) into its one-bit extensions. The first tree connects the doubly flipped vertex to the vertex reached by flipping \(i\), whereas the second connects it to the vertex reached by flipping \(j\):
\[
\boxed{
\{g\oplus\mathbf1_{S\cup\{i\}},g\oplus\mathbf1_{S\cup\{i,j\}}\}
\ \longleftrightarrow\
\{g\oplus\mathbf1_{S\cup\{j\}},g\oplus\mathbf1_{S\cup\{i,j\}}\}.}
\tag{6}
\]
Thus a rank-\(r\) chamber exchange is a batch of \(2^{r-1}\) independent spanning-tree edge pivots along squares. For \(r=1\) it changes the unique common central edge by one square pivot; for \(r>1\) that edge is preserved.

*Proof.* Across a generic type-\(D_n\) wall, signs are unchanged and the relative ranks of \(i,j\) are the only order change. Every other direction has the same smaller-ranked set, so its tree edges in (2) remain fixed. On a square \(F_S\), the two singly flipped vertices have parent \(g\oplus\mathbf1_S\) in both trees. The doubly flipped vertex has as parent the singly flipped vertex in the lower-ranked direction, giving (6). There are \(2^{r-1}\) choices of the lower-ranked subset \(S\); their squares are disjoint because the assignments to the lower ranks differ. These account for every changed edge. Swapping one of the two edges (6) for the other is the standard four-cycle spanning-tree exchange. The first-rank edge changes only if rank one is among the exchanged ranks. \(\square\)

**Corollary 4 (intrinsic dimension-simple exchange geometry).** Every type-\(D_n\) chamber carries a complete book of full antipodal geodesics, all sharing one edge, and every chamber-wall move is generated by disjoint cubical square exchanges. Each witness in every book traverses every dimension once.

*Proof.* This combines Theorems 1 and 3; dimension-simplicity follows from the path description in Theorem 1. \(\square\)

**Implication for Wu--Yang.** The common refinement can now be treated as the space of canonical spanning geodesic trees. A rank-two wall modifies the family of complete path certificates through a controlled set of disjoint square moves; this retains the identity of each dimension traversed. Switch-filtered Freudenthal chains and the previously computed quadratic square defects can be compared directly between adjacent tree books. The separate spanning-tree obstruction proves that an individual book may have only highly switching paths, so the unresolved task is a global equivariant cancellation across books. This construction uses only the native type-\(D_n\) and cube geometries, without new coloring restrictions.

**Theorem 5 (one adjacent exchange per root; global Lipschitz switch energy).** Let \(\mathcal T,\mathcal T'\) be adjacent type-\(D_n\) chamber trees, related by exchanging consecutive absolute-value ranks occupied by dimensions \(i,j\), and use the common reference corner \(g\) from Theorem 3. For every cube root \(x\), let \(P_x(\mathcal T)\) denote the unique antipodal tree geodesic.

(i) If \((x_i\oplus g_i)\ne(x_j\oplus g_j)\), then
\[
\boxed{P_x(\mathcal T')=P_x(\mathcal T).}
\tag{8}
\]
If these two bits agree, the two paths differ by a single exchange of the adjacent dimension occurrences \(i,j\). In particular their other dimensions occur in the same positions and the differing two-edge routes traverse one square from Theorem 3. For each wall precisely \(2^{n-1}\) rooted paths, or \(2^{n-2}\) unoriented antipodal paths, are changed.

(ii) Let \(c\) be any legal antipodally odd binary coloring, and for a complete geodesic with edge word \(w=(w_1,\ldots,w_n)\) define the antiperiodic switch defect
\[
h_c(P)=\frac12\left(\sum_{k=1}^{n-1}[w_k\ne w_{k+1}]
+[w_n=w_1]-1\right).
\tag{9}
\]
Then for each root \(x\),
\[
\boxed{|h_c(P_x(\mathcal T'))-h_c(P_x(\mathcal T))|\le1.}
\tag{10}
\]
Consequently the intrinsic, root-free chamber energy
\[
\boxed{\mu_c(\mathcal T)=\min_{x\in Q_n}h_c(P_x(\mathcal T))}
\tag{11}
\]
is 1-Lipschitz on the type-\(D_n\) chamber adjacency graph:
\[
\boxed{|\mu_c(\mathcal T')-\mu_c(\mathcal T)|\le1.}
\tag{12}
\]
Moreover the unrestricted NORI1 conjecture is equivalent to \(\min_{\mathcal T}\mu_c(\mathcal T)=0\).

*Proof.* In the tree description of Theorem 1, each path first deletes the dimensions in which \(x\) differs from \(g\), in decreasing rank, then adds the complementary dimensions in increasing rank. When \(i,j\) lie on opposite sides of this division, exchanging their consecutive ranks leaves the full dimension order unchanged. When they lie on the same side, their relative order reverses at consecutive positions and all remaining dimension positions agree. Hence (i) follows. The equality condition on the two bits holds for half of the \(2^n\) roots. Antipodal roots give the same geometric path with reversed orientation, so the number of unoriented changed paths is half as large.

For (ii), an adjacent dimension exchange at fixed root changes only two adjacent edge colors; the other edges are unaffected. With antiperiodic closing comparison, the relevant three comparisons have the same parity before and after the exchange and their counts differ by \(0\) or \(\pm2\). This is the uniform twisted switch exchange law proved earlier in Article XIV. Dividing by two gives (10); the unchanged-path case gives zero. The minimum of functions whose values move by at most one also moves by at most one, proving (12). Every full rooted geodesic is the maximal simplex of some rooted Freudenthal triangulation, and its interior contains a generic point of some type-\(D_n\) chamber. By Theorem 1, its complete path belongs to that chamber's tree. Conversely every tree path is a valid full geodesic. The root-slide criterion proved earlier identifies \(h=0\) with existence of a monochromatic complete geodesic. Thus the last equivalence follows. \(\square\)

**Corollary 6 (sharp high-energy chamber in every dimension).** For every \(n\ge3\) there is a legal antipodally odd coloring and a type-\(D_n\) chamber tree \(\mathcal T\) such that
\[
\boxed{h_c(P_x(\mathcal T))=
\mu_c(\mathcal T)=\left\lfloor\frac{n-1}{2}\right\rfloor
\quad\text{for every }x.}
\tag{13}
\]
This is the largest possible value of \(h_c(P)\) for any full geodesic in dimension \(n\).

*Proof.* Use the canonical recursive tree coloring from the preceding spanning-tree obstruction subsection. For odd \(n\), every path through its chosen chamber has the alternating edge word with \(n-1\) ordinary switches; the twisted seam contributes one and (9) gives \(h=(n-1)/2\). For even \(n\), every such word is alternating, possibly with its first or last bit flipped by the necessary antipodal-odd correction. An unmodified alternating word has \(n-1\) ordinary switches and twisted seam zero; an endpoint-modified word has \(n-2\) ordinary switches and twisted seam one. Both give \(h=(n-2)/2\). Since an antiperiodic cyclic comparison count is odd and at most \(n\), or at most \(n-1\) when \(n\) is even, no larger \(h\) is possible. \(\square\)

**Proof-search implication.** Passing from rooted type-\(B_n\) flags to type-\(D_n\) chamber trees yields a globally root-minimized switch energy with a uniform one-step variation bound, while preserving every dimension-simple witness. This repairs the unbounded root-flip Lipschitz failure recorded in Article XV at the level of the chamber selection variable. It does not force a chamber of energy zero: the high-energy example in Corollary 6 shows that local minimization or bounded variation by itself does not yield NORI1. A successful topological argument would need to use the coloring-sensitive square-pivot comparisons together with the equivariant topology of the full chamber complex.

**Theorem 7 (canonical root-slide pairing within a chamber book).** Let \(\mathcal T\) be a type-\(D_n\) chamber tree, \(n\ge3\), with ranked directions \(i_1,\ldots,i_n\) and reference vertex \(g\). Choose one root from each antipodal pair by
\[
X_g=\{x\in Q_n:x_{i_1}=g_{i_1}\}.
\]
Put \(j=i_n\), the largest-ranked direction. The involution
\[
\boxed{J:X_g\longrightarrow X_g,\qquad J(x)=x\oplus e_j}
\tag{14}
\]
is fixed-point-free. For each \(x\in X_g\), the two unoriented antipodal tree paths represented by \(P_x(\mathcal T)\) and \(P_{Jx}(\mathcal T)\) are related by a single cyclic root slide across their dimension-\(j\) edge (or the inverse slide). In particular, for every legal antipodally odd coloring,
\[
\boxed{h_c(P_x(\mathcal T))=h_c(P_{Jx}(\mathcal T)).}
\tag{15}
\]

*Proof.* Since \(j\ne i_1\), toggling bit \(j\) preserves \(X_g\), and \(J\) has no fixed root. Suppose first \(x_j=g_j\). The tree path \(P_x\) uses direction \(j\) in its final step, because it is the greatest-ranked direction not differing from \(g\) at the start. The path \(P_{Jx}\) uses the same direction in its first step, because it is the greatest-ranked direction differing from \(g\). After its first step, \(P_{Jx}\) is at \(x\), and the remaining \(n-1\) steps coincide with the initial \(n-1\) steps of \(P_x\). The last edge of \(P_x\) is the antipodal mate of the first edge of \(P_{Jx}\). Hence \(P_x\) is the one-step root slide of \(P_{Jx}\). If \(x_j\ne g_j\), reverse the roles. The color word of a root slide is obtained by moving the initial bit to the end and complementing it. The antiperiodic comparison count and the defect \(h\) are invariant under this operation, proving (15). \(\square\)

**Corollary 8 (even multiplicity of every switch grade).** For every legal coloring \(c\), every type-\(D_n\) chamber tree \(\mathcal T\), and every \(r\ge0\),
\[
\boxed{
\#\{\text{unoriented full antipodal paths in }\mathcal T:
h_c(P)=r\}\equiv0\pmod2.
}
\tag{16}
\]
More generally the sum over the book of any binary path statistic invariant under reversal and root slides is zero modulo two.

*Proof.* Each unoriented full antipodal tree path has the two roots \(x,\bar x\), of which precisely one lies in \(X_g\). The fixed-point-free involution \(J\) pairs these representatives, and Theorem 7 preserves \(h\). For a reversal- and root-slide-invariant statistic, the two paired values agree, so they cancel over \(\mathbb F_2\). \(\square\)

**Consequence for the chain obstruction.** A raw mod-two count of complete paths of any fixed switch grade, performed inside one type-\(D_n\) chamber book, vanishes identically. Thus a Wu--Yang construction must retain more than unweighted chamber-by-chamber path counts: it may use root-sensitive chain orientation, a quotient by the canonical root-slide pairing, incidence across neighboring books, or the higher filtered square corrections. The pairing holds for every unrestricted legal coloring and preserves dimension-simpleness throughout.

**Theorem 9 (highest-rank wall preserves the root-slide orbit spectrum).** Let \(\mathcal T,\mathcal T'\) be adjacent type-\(D_n\) chamber trees, \(n\ge3\), differing by exchange of their greatest-ranked dimensions \(i=i_{n-1},j=i_n\). Let \([P]_{\rm cyc}\) denote the class of a complete antipodal geodesic under cyclic root slides and path reversal. Then
\[
\boxed{
\{[P]_{\rm cyc}:P\text{ an unoriented full path of }\mathcal T\}
=
\{[P]_{\rm cyc}:P\text{ an unoriented full path of }\mathcal T'\}
}
\tag{17}
\]
as multisets. The equality is geometric and does not depend on the coloring.

*Proof.* The smallest-ranked direction and its reference bit are unchanged across the wall. The common representative root set \(X_g\) from Theorem 7 indexes each book's unoriented paths. Partition \(X_g\) into four-root sets by fixing all bits except \(i,j\); denote their relative \(i,j\) bits by \(00,01,10,11\).

Theorem 5(i) shows that roots \(01\) and \(10\), whose two bits differ, have identical full vertex paths in the two books. Call their root-slide orbits \(A,B\), respectively. In the first book the greatest-ranked direction is \(j\), so the canonical root-slide pairing of Theorem 7 toggles \(j\). Thus the path at \(00\) belongs to orbit \(A\) together with the path at \(01\), and the path at \(11\) belongs to orbit \(B\) together with the path at \(10\). The four-root contribution is the multiset \(\{A,A,B,B\}\).

In the second book the greatest-ranked direction is \(i\), so Theorem 7 instead toggles \(i\). The path at \(11\) has orbit \(A\), paired with unchanged root \(01\); the path at \(00\) has orbit \(B\), paired with unchanged root \(10\). Its four-root contribution is again \(\{A,A,B,B\}\). Summing over all four-root sets proves (17). \(\square\)

**Corollary 10 (highest-wall spectral rigidity).** For any legal antipodally odd coloring \(c\), any switch grade \(r\ge0\), and adjacent trees in Theorem 9,
\[
\boxed{
\#\{P\in\mathcal T:h_c(P)=r\}
=\#\{P\in\mathcal T':h_c(P)=r\},
\qquad
\mu_c(\mathcal T)=\mu_c(\mathcal T').
}
\tag{18}
\]
Every statistic invariant under root slides and reversal has the same distribution across these two books.

*Proof.* The twisted switch defect is constant on cyclic root-slide classes and under reversal, by the established odd-color root-slide identity. Theorem 9 preserves the full orbit multiset. \(\square\)

**Implication for chain constructions.** The 1-Lipschitz root-free chamber energy is constant across the Coxeter walls that exchange the two greatest-ranked dimensions. These walls can be identified when searching for low-switch cyclic path orbits. The other rank exchanges retain color-sensitive square defects. Theorem 9 is a support-preserving global path-orbit cancellation valid for every unrestricted legal cube coloring, and supplies more information than parity of unweighted path counts.
