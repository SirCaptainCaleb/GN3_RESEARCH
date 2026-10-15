# Free Lie algebra and Petrie cycles

# Petrie-cycle pencils, free-Lie incidence, and cubical fillings

The canonical type-\(D_n\) spanning trees of the preceding subsection admit a second description: each chamber is a *book* of antipodally symmetric Petrie cycles, and the books with one fixed central edge form the right-normed free-Lie commutator operator. This supplies signed Jacobi and shuffle cancellations in every switch grade, as well as an explicit cubical two-chain filling the unfiltered sum of every book. All paths and cells in this construction use distinct cube directions.

Throughout, \(n\ge3\), the cube vertices are \(\mathbb F_2^n\), and \(A\) is antipodal inversion. For a full dimension-simple geodesic \(P\), concatenate \(P\) with its antipodal image \(AP\), traversed in the same dimension order. The resulting \(2n\)-cycle \(\mathfrak p(P)\) has each direction twice, and its second half is the antipode of its first. We call it a *Petrie cycle*. It is simple: two different vertices on the first half correspond to nested proper prefixes of one permutation, and no such proper prefix is the complement of another nested prefix. The antipodal second half therefore meets the first only at their common endpoints.

Every Petrie cycle has \(4n\) oriented rooted full-geodesic representatives: choose any of its \(2n\) vertices and either traversal direction, then retain the following \(n\) edges. Consequently the number of undirected Petrie cycles in \(Q_n\) is \(2^{n-2}(n-1)!\).

Fix an undirected cube edge \(e\) of direction \(i\) and choose one orientation \(g\to g\oplus e_i\). Every Petrie cycle through \(e\) has a unique traversal beginning with this oriented edge; its remaining \(n-1\) directions appear in some order \(\pi\). Thus the Petrie cycles through \(e\) are in natural bijection with \(S_{[n]\setminus\{i\}}\) and number \((n-1)!\). This edge-rooted permutation encoding is independent of any coloring.

**Theorem 1 (unimodal chamber books and fourfold root intersection).** Let \(T\) be a canonical type-\(D_n\) chamber tree with ranked directions
\[
i=i_1\prec i_2\prec\cdots\prec i_n
\]
and common central edge \(e\). The distinct Petrie cycles obtained from its full antipodal tree paths are precisely the cycles through \(e\) whose remaining direction permutation first increases and then decreases in the order \(\prec\). Every one of these Petrie cycles occurs as the antipodal completion of precisely four rooted tree paths, and there are
\[
\boxed{|\mathcal B(T)|=2^{n-2}}
\tag{1}
\]
distinct cycles in the book \(\mathcal B(T)\).

*Proof.* Choose the reference endpoint \(g\) of the central edge and the representing root set \(X_g=\{x:x_{i_1}=g_{i_1}\}\). The tree geodesic from \(x\) to \(\bar x\) deletes the directions in which \(x\) differs from \(g\), in decreasing rank, then traverses the central direction \(i_1\), then adds the remaining directions in increasing rank. Root-slide its antipodal Petrie cycle to start with the central oriented edge. The remaining \(n-1\) directions appear in an increasing block followed by a decreasing block. Conversely, for any such unimodal permutation, assign its left-of-maximum entries to the increasing block and its right-of-maximum entries to the decreasing block; assign the maximum to either block. These two assignments yield the same Petrie cycle, and recover tree roots producing it. There are \(2^{n-2}\) unimodal permutations, since every direction except the greatest-ranked remaining direction can be assigned independently to the increasing left block or decreasing right block.

More directly, the preceding canonical root-slide involution toggles the highest-ranked root bit, preserving the Petrie cycle, and reversal gives the two antipodal roots. Hence every cycle in the book has at least four rooted representatives, \(x,x\oplus e_{i_n},\bar x,\bar x\oplus e_{i_n}\). There are no additional representatives: every full tree path contains the unique central edge \(e\) and has the highest-ranked direction \(i_n\) as its first or last step. On a fixed oriented Petrie cycle, among the length-\(n\) consecutive arcs containing \(e\), only two have a direction-\(i_n\) edge as the first or last edge. Reversing the cycle gives two more. Thus there are at most four. \(\square\)

For every legal antipodally odd coloring \(c\), the twisted defect \(h_c\) is invariant under reversal and root slides. Hence \(h_c\) is a well-defined nonnegative integer on the Petrie-cycle basis, and every book admits a canonical filtration by switch grade.

Let \(m=n-1\), fix the central edge \(e\), and write \(\mathbb Z\langle x_1,\ldots,x_m\rangle_{\mathrm{mult}}\) for the free abelian group on the \(m!\) associative words using all \(m\) letters once. Identify a word with the Petrie cycle through \(e\) encoded by its direction permutation. Given a rank order \(\rho=(a_1,\ldots,a_m)\), define the **signed book chain**
\[
\boxed{
B(\rho)=[a_1,[a_2,[\cdots,[a_{m-1},a_m]]\cdots]],
}
\tag{2}
\]
using the associative bracket \([u,v]=uv-vu\). Every coefficient in its word expansion is \(0\) or \(\pm1\).

**Theorem 2 (free-Lie incidence and rank).** The support of \(B(\rho)\) is the set of \(2^{m-1}\) Petrie cycles in the chamber book with central edge \(e\) and remaining direction ranking \(\rho\). Write \(D_m\) for the \(\mathbb Z\)-linear operator on all multilinear associative words that sends the word \(a_1\cdots a_m\) to \(B(a_1,\ldots,a_m)\). Then
\[
\boxed{D_m^2=mD_m,\qquad\operatorname{rank}D_m=(m-1)!.}
\tag{3}
\]
These formulas hold integrally, and the rank formula survives reduction modulo two. In characteristic two,
\[
\boxed{D_m^2=
\begin{cases}
D_m,&m\text{ odd},\\
0,&m\text{ even}.
\end{cases}}
\tag{4}
\]
The image is the multilinear component of the free Lie algebra, with the same dimension \((m-1)!\) over every field.

*Proof.* In the expansion of the right-normed bracket, each \(a_j\), inserted in descending order \(j=m-1,m-2,\ldots,1\), goes either to the beginning or the end of the current word. The resulting permutations are precisely those rising to the greatest letter \(a_m\) and then falling; distinct choices give distinct words. The coefficient is \((-1)^q\), where \(q\) is the number of letters placed to the right. This proves the support and its cardinality.

For the quadratic identity, work initially in the free associative Hopf algebra with the primitive coproduct \(\Delta(a)=a\otimes1+1\otimes a\), antipode \(S(a)=-a\), and grading map \(N(w)=|w|w\). In convolution notation put \(D=N*S\). If \(w\) is nonempty and \(a\) a letter, the Hopf identities yield
\[
D(aw)=aD(w)-D(w)a+a\sum w_{(1)}S(w_{(2)})
=[a,D(w)],
\]
since the last sum equals the augmentation of \(w\), which is zero. Also \(D(a)=a\). Thus \(D\) is the right-normed commutator operator (2). Such a commutator is primitive. If \(L\) is homogeneous primitive of degree \(m\), then \(D(L)=N(L)=mL\), because \(\Delta L=L\otimes1+1\otimes L\). Applying this to \(L=D(w)\) proves \(D_m^2=mD_m\) integrally.

Every element of the image is a multilinear Lie polynomial. Conversely, right-normed brackets span the multilinear Lie component. Fix \(a_m\) as a distinguished final letter. Jacobi and the derivation rule \(\operatorname{ad}_{[u,v]}=[\operatorname{ad}_u,\operatorname{ad}_v]\) expand any multilinear Lie bracket as a combination of the \((m-1)!\) right-normed brackets ending in \(a_m\). Those brackets are linearly independent: in the associative expansion of
\([a_{\sigma(1)},[\cdots,[a_{\sigma(m-1)},a_m]\cdots]]\), the only word ending with \(a_m\) is \(a_{\sigma(1)}\cdots a_{\sigma(m-1)}a_m\), with coefficient one. Hence the image dimension is \((m-1)!\), in every characteristic. The characteristic-two statements follow from the integral quadratic identity. \(\square\)

**Theorem 3 (signed Jacobi and shuffle coherence in every switch grade).** For each fixed central edge \(e\), and each switch grade \(r\ge0\), let \(\Pi_r\) project the Petrie-cycle basis onto the cycles with \(h_c=r\), where \(c\) is any legal antipodally odd edge coloring. Then:

(i) Exchanging the two greatest-ranked remaining directions negates the integral signed book:
\[
\boxed{\Pi_r B(\rho,a,b)=-\Pi_r B(\rho,b,a).}
\tag{5}
\]

(ii) If \(a,b,d\) are three greatest-ranked remaining directions, with all lower ranks fixed in the same order \(\rho\), then
\[
\boxed{
\Pi_r B(\rho,a,b,d)
+\Pi_r B(\rho,b,d,a)
+\Pi_r B(\rho,d,a,b)=0.
}
\tag{6}
\]

(iii) For two nonempty disjoint ordered words \(u,v\) whose letters partition the remaining directions, the signed sum of the coefficients of \(B(\rho)\) over their order-preserving shuffles is zero:
\[
\boxed{\sum_{\pi\in u\shuffle v}[\,\pi\,]B(\rho)=0.}
\tag{7}
\]

*Proof.* The innermost commutator changes sign upon swapping its entries, giving (5). The Jacobi identity
\([a,[b,d]]+[b,[d,a]]+[d,[a,b]]=0\), valid in the free associative algebra, remains valid inside any fixed outer sequence of brackets, giving (6). Both identities hold as integral equalities of Petrie-cycle incidence vectors. Applying the linear projection \(\Pi_r\) preserves the equalities for every coloring.

For (iii), a free-Lie commutator of primitive generators is primitive. In the coproduct of a multilinear associative word, the coefficient of \(u\otimes v\) is the sum over the order-preserving shuffles of \(u\) and \(v\). Since the coproduct of \(B(\rho)\) contains only \(B(\rho)\otimes1+1\otimes B(\rho)\), that coefficient vanishes when both \(u,v\) are nonempty. \(\square\)

Theorem 3 gives a complete set of algebraic coherence relations within each fixed-edge pencil: the only linear relations among the signed right-normed book vectors are those entailed by antisymmetry and Jacobi. Indeed these identities rewrite every right-normed bracket into the \((m-1)!\) normal forms ending in one fixed letter, and Theorem 2 proves those forms independent.

We next record a different, geometric cancellation involving **unsigned** book cycles, with \(\mathbb F_2\) coefficients. Let \(E_i\) denote the sum of all cube edges in direction \(i\), and let \(Q_{ij}\) be the sum of all square faces with free directions \(i,j\).

**Theorem 4 (explicit geometric filling of every unsigned chamber book).** If \(i_{n-1},i_n\) are the two greatest-ranked directions of \(T\), and \([C]\) denotes the \(\mathbb F_2\) one-chain supported on the edges of a full Petrie cycle \(C\), then
\[
\boxed{
\sum_{C\in\mathcal B(T)}[C]
=E_{i_{n-1}}+E_{i_n}
=\partial Q_{i_{n-1},i_n}.
}
\tag{8}
\]
After taking the antipodal quotient \(Y_n=\partial I^n/A\), let \(\bar C\) be the resulting \(n\)-edge projective Petrie loop and let \(\bar Q_{ij}\) be the sum of the orbits of square faces in directions \(i,j\). Then
\[
\boxed{
\sum_{C\in\mathcal B(T)}[\bar C]
=\partial\bar Q_{i_{n-1},i_n}
\quad\text{in }C_1(Y_n;\mathbb F_2).
}
\tag{9}
\]
The filling uses only dimension-distinct two-faces, and is independent of the coloring.

*Proof.* In the tree of Theorem 1, take an edge \(e(r,S)\) of rank \(r\), whose upper endpoint differs from the reference vertex in the rank-\(r\) direction and in a subset \(S\) of smaller-ranked directions. The rooted path \(P_x(T)\) traverses this edge if and only if the corresponding endpoint is a prefix, under the rank order, of either \(x\oplus g\) or its complement. There are \(2^{n-r}\) choices of each kind and the two kinds are disjoint, so the number of rooted tree paths using \(e(r,S)\) is
\[
2^{n-r+1}.
\tag{10}
\]
For \(r<n\), the antipodal mate of \(e(r,S)\) does not belong to the tree: it differs from the reference bits in every greater-ranked direction. If the full Petrie cycle of a tree path contains \(e(r,S)\), all four rooted tree-path representatives of that cycle must use this edge rather than its antipodal mate. Theorem 1 therefore gives
\[
\#\{C\in\mathcal B(T):e(r,S)\in C\}=2^{n-r-1}
\quad(r<n).
\tag{11}
\]
For \(r=n\), both the edge and its antipodal mate belong to the tree, and each contributing Petrie cycle has two rooted paths using either one. Equation (10) then gives one Petrie cycle through every highest-ranked edge.

Thus for ranks \(r\le n-2\), every tree edge and its antipodal mate occur in an even number of cycles and cancel in the \(\mathbb F_2\) sum. At rank \(n-1\) every tree edge and its antipode occur once; together these are all cube edges in direction \(i_{n-1}\). At rank \(n\), every cube edge already lies in the tree and occurs once in the cycle sum. No other edge can occur, because every Petrie cycle is a tree geodesic together with its antipodal image. This proves the first equality of (8).

Each square in directions \(i,j\) contributes two edges of direction \(i\) and two of direction \(j\); the collection of all such squares partitions the edges of those two directions. Therefore \(\partial Q_{ij}=E_i+E_j\), proving the second equality. All chains are invariant under antipodal inversion. The transfer map from quotient chains to their complete antipodal lifts is injective over \(\mathbb F_2\), and carries the two sides of (9) to the corresponding sides of (8). This proves (9). \(\square\)

**Theorem 5 (dimension-simple cubical coherence).** For every nonempty set \(S\subseteq[n]\), let \(Q_S\) denote the sum over \(\mathbb F_2\) of all cubical faces with free direction set \(S\), of dimension \(|S|\). Then
\[
\boxed{\partial Q_S=\sum_{i\in S}Q_{S\setminus\{i\}}.}
\tag{12}
\]
For \(|S|<n\), the same identity holds after passage to the antipodal quotient. In particular for three distinct directions
\[
\boxed{Q_{ij}+Q_{ik}+Q_{jk}=\partial Q_{ijk}.}
\tag{13}
\]
Thus the two-chain fillings (8) enjoy explicit three-cube coherence, with no repeated direction.

*Proof.* Every \((|S|-1)\)-face with free directions \(S\setminus\{i\}\) is a facet of precisely one face in the collection \(Q_S\), after fixing its other bits. Every facet of a member of \(Q_S\) appears in one of these collections, proving (12) by direct incidence counting. For proper \(S\), antipodal inversion pairs the faces without fixed faces, and the same transfer-injectivity argument proves the quotient identity. Formula (13) is the \(|S|=3\) case. \(\square\)

**Research consequences and scope.** The book geometry now has two mutually reinforcing pieces of coherence: signed free-Lie Jacobi and shuffle identities within every central-edge pencil, valid after arbitrary coloring-dependent switch-grade projection; and unsigned cubical square and three-cube fillings for complete books. Across a chamber wall exchanging ranks \(r\ge2\), the central edge stays fixed, so the first mechanism applies. Across rank \(r=1\), the central edge changes, and the two free-Lie pencils use different permutation bases: their interaction requires a new comparison beyond the identities above. The geometric filling (8) depends only on the two greatest-ranked directions and therefore is unchanged across any wall that preserves this unordered pair, including a central-edge wall in dimension \(n\ge4\). This gives unfiltered root-changing coherence, but not a filtered lift. The outstanding problem is to construct a support-preserving and antipodally compatible comparison of grade-zero Lie-pencil chains across changes of the central edge, with its higher cubical coherence, and deduce a topological obstruction forcing a monochromatic Petrie half-cycle. Neither unrestricted NORI1 nor the boundary Hamilton conjecture is resolved here.

**Theorem 6 (root-changing wall reduction to one lower Lie arity).** For \(n\ge4\), fix distinct directions \(i,j\), a vertex \(g\), and an order \(K\) on the remaining \(n-2\) directions. Let \(B_{i|j,K}\), \(B_{j|i,K}\) be signed chamber-book chains, in the free abelian group on undirected cube Petrie cycles, for chamber rankings \((i,j,K)\) and \((j,i,K)\). Put \(C(g;w)\) for the cycle generated by a full dimension word \(w\) from \(g\). Then
\[
\boxed{
B_{i|j,K}+(-1)^nB_{j|i,K}
=\sum_{\sigma\in\mathcal U(K)}\epsilon_K(\sigma)
\left\{C(g;i,j,\sigma)+(-1)^nC(g;j,i,\sigma)\right\}.
}
\tag{14}
\]
This is an integral identity of dimension-simple complete cycles and persists under the projection onto any prescribed switch grade.

*Proof.* In the first book, the smallest remaining letter \(j\) appears at the beginning or the end of each unimodal word. Separating these possibilities yields
\(B_{i|j,K}=\sum_\sigma\epsilon_K(\sigma)
(C(g;i,j,\sigma)-C(g;i,\sigma,j))\).
Likewise,
\(B_{j|i,K}=\sum_\sigma\epsilon_K(\sigma)
(C(g;j,i,\sigma)-C(g;j,\sigma,i))\).
Reversing the full direction word from \(g\) preserves its undirected Petrie cycle:
\(C(g;i,\sigma,j)=C(g;j,\operatorname{rev}\sigma,i)\).
The Lie coefficients of a word on \(n-2\) letters transform under reversal by the factor \((-1)^{n-3}=-(-1)^n\). Thus the terms with the smaller letter at the end cancel in the displayed combination, leaving (14). Projection by switch grade is linear on the global cycle basis. \(\square\)

**Theorem 7 (dimension and unfiltered cubical shadow).** With \(g,i,j\) fixed, the span of the signed wall defects in (14) over all orders \(K\) has rank \((n-3)!\) over \(\mathbb Z\), and the same dimension over \(\mathbb F_2\). Let \(\mathcal E\) take a Petrie cycle to its projective one-chain over \(\mathbb F_2\). Then each pair of cycles in braces in (14) has image equal to the boundary of the projective square with initial vertex \(g\) and directions \(i,j\), independently of \(\sigma\). Therefore
\[
\boxed{\mathcal E\bigl(B_{i|j,K}+(-1)^nB_{j|i,K}\bigr)=0.}
\tag{15}
\]

*Proof.* The two sets of cycles \(C(g;i,j,\sigma)\) and \(C(g;j,i,\sigma)\) are disjoint: the first contains the edge from \(g\) in direction \(i\) but not that in direction \(j\), whereas the second has the converse property. For each set, the full \(\sigma\) can be recovered by walking from the indicated edge at \(g\). Consequently the map from the free word module on \(K\) to the free Petrie-cycle module, taking \(\sigma\) to the signed pair in braces, is injective integrally and modulo two. Theorem 2 identifies the image rank of the lower-arity Dynkin operator as \((n-3)!\). Swapping the first two dimension steps replaces one length-two geodesic across an \(ij\)-square with the other; the antipodal cycle completions differ by that square boundary together with its antipodal mate. This becomes one projective square boundary, proving the first chain assertion. Summing with Lie coefficients annihilates this fixed boundary, since the coefficients of any nontrivial iterated commutator have sum zero. \(\square\)

The first signed moment of the *filtered* discrepancy in Theorem 6 is computed in the subsequent subsection, *Lie endpoint compression for filtered root wall variation*. At higher switch moments the full residual word may contribute, so the unfiltered cancellation (15) is not a grade-zero proof.
