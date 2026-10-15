# Triangle-square complex and antipodal cohomology

# Triangle-square complex and antipodal cohomology

The preceding subsection identifies unrestricted NORI1 colorings with representatives of the antipodal covering class on the quotient of the cube line graph. Here we show that its local star-triangle and cube-square flatness relations give a *complete two-dimensional topological presentation* of that class.

Let \(n\ge3\), \(H=L(Q_n)\), and let \(\tau\) be the involution induced on its vertices (undirected cube edges) by antipodal translation of \(Q_n\). Construct a finite two-dimensional CW complex \(X_n\) with one-skeleton \(H\) by attaching:

1. A triangular two-cell for every three distinct cube edges incident at one cube vertex (a three-cycle in the line graph).
2. A square two-cell for the cyclic line-graph walk of the four undirected edges surrounding each two-dimensional square face of \(Q_n\).

The involution \(\tau\) permutes all these cells freely. Put \(Y_n=X_n/\tau\).

**Theorem 1 (simple connectivity and canonical double cover).** For every \(n\ge3\), \(X_n\) is simply connected and
\[
\boxed{\pi_1(Y_n)\cong\mathbb Z_2,\qquad
H^1(Y_n;\mathbb F_2)\cong\mathbb F_2.}
\tag{1}
\]
The covering \(X_n\to Y_n\) represents the unique nonzero cohomology class \(\omega\in H^1(Y_n;\mathbb F_2)\).

*Proof.* First attach the star triangles to \(H\), but not yet the cube-square cells. For each cube vertex \(v\), its incident edges form a complete subgraph of \(H\). Filling all its triangles makes that clique simply connected. Adding higher-dimensional simplices on these star cliques does not affect the fundamental group. The resulting union of filled cliques is homotopy equivalent to the original cube graph, viewed with its edges subdivided at their midpoints: each star simplex is contractible, and distinct star simplices intersect in at most one vertex, corresponding to the original edge joining their centers. The incidence pattern is precisely the barycentric subdivision of the cube graph. Hence the original star-triangle complex has fundamental group isomorphic to that of the one-skeleton of \(Q_n\).

The additional square cells kill the boundary loops of every cube two-face. The two-skeleton of the standard cubical cell structure on the solid \(n\)-cube is simply connected, since attaching cells of dimension three or higher does not alter its fundamental group and the full cube is contractible. It follows that adding the square relations to the preceding star-triangle complex kills its whole fundamental group. Thus \(X_n\) is simply connected.

For \(n\ge3\), a cube edge is disjoint from its antipodal mate; no star at a vertex is antipodally fixed, and a two-face lies in a hyperplane fixing at least one bit and so cannot equal its antipodal two-face. Thus the involution is free on all cells and acts freely on \(X_n\). Its quotient is a connected complex with simply connected double cover, hence \(\pi_1(Y_n)=\mathbb Z_2\). Its first mod-two cohomology is \(\operatorname{Hom}(\mathbb Z_2,\mathbb F_2)\), giving (1); the classifying homomorphism of the double cover is nonzero and therefore is its unique generator. \(\square\)

**Theorem 2 (unrestricted NORI1 as all representatives of the unique class).** Let \(a\in C^1(Y_n;\mathbb F_2)\). Then
\[
\boxed{\delta a=0,\quad [a]=\omega\ne0}
\tag{2}
\]
if and only if there is an antipodally odd undirected-edge coloring \(c\) of \(Q_n\) with
\[
\boxed{a([e,f])=c(e)+c(f)}
\tag{3}
\]
for every pair of incident cube edges \(e,f\). The coloring is unique up to global complementation.

*Proof.* Given \(c\), (3) descends to the quotient because antipodality complements both colors. Summing around any star triangle or cube-square cell telescopes to zero, making \(a\) a cocycle. On the quotient of any full antipodal geodesic loop, its value is one, so its cohomology class is \(\omega\).

Conversely lift a nonzero cocycle \(a\) to \(X_n\). By simple connectivity, its class in \(H^1(X_n;\mathbb F_2)\) vanishes, so the lift is the differential of some binary vertex function \(c\) on \(H\). The quotient invariance of the lift implies that \(c(e)+c(\tau e)\) is constant across connected \(H\). Were this constant zero, \(c\) would descend to \(Y_n\), making \(a\) a coboundary, contrary to \([a]=\omega\). Thus the constant is one: \(c\) is an antipodally odd cube-edge coloring. Connectedness of \(H\) shows that primitives differ only by a global constant. \(\square\)

**Corollary 3 (one-crossing generators).** Every complete dimension-simple antipodal geodesic \(P\) induces a simple length-\(n\) cycle \(\gamma_P\) in the one-skeleton of \(Y_n\), using one edge from every cube dimension and representing the nontrivial fundamental-group class. The original NORI1 conjecture is equivalent to:

> Every cellular one-cocycle representing \(\omega\) admits one of these complete-geodesic cycles on which it has support of size one.

*Proof.* The preceding subsection constructs \(\gamma_P\) by appending the antipodal first cube edge to the edge sequence of \(P\), and proves that root slides rotate it. For any cocycle (3), its restriction to \(\gamma_P\) is the ordinary switch-indicator sequence with the antipodal closing comparison. One labeled cycle edge means that after a root slide all internal switches vanish, and conversely a monochromatic full geodesic produces such a cycle. \(\square\)

**Connection with monochromatic antipodal paths.** If a coloring admits an arbitrary monochromatic antipodal cube path (which may repeat dimensions), its edge sequence followed by the antipodal initial edge projects to an essential closed walk of \(Y_n\) on which (3) is one only at the closing step. This is not necessarily one of the distinguished simple basis cycles of Corollary 3. It isolates, in cohomological terms, the gap between the established unrestricted antipodal-path results and the required dimension-simple strengthening.

**Consequence for unification.** The local triangle and square relations are not arbitrary extra axioms: they present the unique nontrivial double-cover class of this intrinsic two-complex. A chirality bit on oriented line-graph links transforms (3) into a reversal-odd turn field. Ordinary boundary tournaments allow arbitrary local triangle curvature, so they cannot be encoded by imposing (2) on every rook fiber. The remaining challenge is to find a common local-incidence topology in which both full classes have faithful chiral realizations and distinguished complete cycles; the current construction supplies that topology rigorously for NORI1 alone.
