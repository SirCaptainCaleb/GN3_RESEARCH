## Rectified Graphs and Cyclic Path Geometry

### Cubical square curvature and chiral exchange laws

Let \(c\) be any antipodally odd binary undirected-edge coloring of \(Q_n\), and choose an antisymmetric chirality bit \(\chi(i,j)\) on ordered distinct dimensions, so \(\chi(j,i)=1+\chi(i,j)\). For a square face with initial vertex \(x\) and dimensions \(i\ne j\), write
\[
a=c(\{x,x+e_i\}),\quad
b=c(\{x+e_i,x+e_i+e_j\}),\quad
a'=c(\{x,x+e_j\}),\quad
b'=c(\{x+e_j,x+e_i+e_j\}).
\]
Put
\[
\boxed{\kappa_{ij}(x)=a+b+a'+b'.}
\tag{1}
\]
The bit \(\kappa_{ij}\) is attached to the undirected square face and does not depend on the choice of its initial vertex or order of \(i,j\).

**Theorem 1 (chiral turn exchange).** The two ordered turns that run across opposite corners of the square have labels
\[
B_x(i,j)=a+b+\chi(i,j),\qquad
B_x(j,i)=a'+b'+\chi(j,i),
\]
and satisfy
\[
\boxed{B_x(i,j)+B_x(j,i)=1+\kappa_{ij}(x).}
\tag{2}
\]
Thus changing the order of two dimensions complements their local reversal-odd turn bit precisely when the square has zero curvature; it preserves the bit when curvature is one. Moreover \(\kappa_{ij}\) equals the XOR of the two underlying uncorrected switch indicators for the opposite two-step routes.

*Proof.* Add the two equations and use antisymmetry of \(\chi\); the sum of the four edge colors is (1). The two original switch indicators are \(a+b\) and \(a'+b'\), whose sum is \(\kappa_{ij}\). \(\square\)

**Theorem 2 (three-dimensional Bianchi relation).** For pairwise distinct dimensions \(i,j,k\), the six square faces of their three-dimensional subcube obey
\[
\boxed{
\kappa_{ij}(x)+\kappa_{ij}(x+e_k)
+\kappa_{ik}(x)+\kappa_{ik}(x+e_j)
+\kappa_{jk}(x)+\kappa_{jk}(x+e_i)=0.
}
\tag{3}
\]
Further,
\[
\boxed{\kappa_{ij}(\bar x)=\kappa_{ij}(x).}
\tag{4}
\]

*Proof.* Each of the twelve undirected edges of the three-dimensional subcube occurs in precisely two of the six square boundaries. Summing their edge-color sums modulo two therefore gives zero. Under antipodal translation, the four edge colors of a square are all complemented, so their XOR is unchanged. \(\square\)

**Corollary 3 (linear curvature versus monochromatic square defects).** Write \(\delta_{ij}(x)=a+b\) and \(\delta_{ji}(x)=a'+b'\) for the adjacent switch indicators of the two opposite routes across the square. Then
\[
\boxed{\delta_{ij}(x)+\delta_{ji}(x)=\kappa_{ij}(x).}
\tag{5}
\]
Consequently zero square curvature means the two routes have the same switch status (both monochromatic or both mixed), whereas curvature one means precisely one route is monochromatic. Unlike the previously studied nonlinear color-specific square defect, this linear curvature records exchange compatibility of the switch predicate itself, without choosing a preferred color.

**Structural implication.** The curvature \(\kappa\) is the cubical two-coboundary of the underlying edge-color one-cochain \(c\); its Bianchi relation is the cochain identity \(d^2c=0\). The local chiral turn law (2) makes the same curvature govern adjacent dimension exchanges on complete geodesic flags. The identity holds for every unrestricted NORI1 coloring, independent of its geodesic existence status.

A boundary tournament has arbitrary local reversed-triple bits and hence need not have vanishing triangle curvature after subtracting a reference chirality. The challenge for a unified chain argument is therefore to use (2)–(3) where the carrier possesses square exchanges, while permitting unrestricted triangular reversal data in its simplex realization. Requiring all chiral turn cochains to be flat would discard ordinary boundary tournaments.

### The antipodal line-graph cover and one-crossing basis cycles

There is a canonical, reference-free topological meaning for the symmetric part of a NORI1 reversal-odd turn connection. The NORI1 conjecture becomes a one-crossing theorem for distinguished nontrivial cycles in a fixed double cover of a graph. All such cycles are full dimension-simple cube geodesics.

Let \(n\ge3\). Write \(H=L(Q_n)\) for the line graph of the \(n\)-cube: vertices of \(H\) are undirected cube edges, and adjacency means sharing a cube vertex. Cube antipodality induces a free graph involution \(\tau\) on \(H\). No vertex of \(H\) is adjacent to its antipodal image. Thus
\[
\boxed{p:H\longrightarrow Y=H/\tau}
\tag{1}
\]
is a connected regular double covering of finite graphs. Denote its nontrivial covering class by \(\omega\in H^1(Y;\mathbb F_2)\).

**Theorem 1 (NORI1 colorings are representatives of a fixed covering class).** For any antipodally odd undirected cube-edge coloring \(c:V(H)\to\mathbb F_2\), define on every quotient-graph edge represented by adjacent \(e,f\in V(H)\)
\[
\boxed{a_c([e,f])=c(e)+c(f).}
\tag{2}
\]
This is well defined under replacing both \(e,f\) by their antipodes, and represents \(\omega\). Conversely every binary one-cochain \(a\) on \(Y\) with \([a]=\omega\) is \(a_c\) for some antipodally odd coloring \(c\), unique up to complementing all edge colors. Thus the space of unrestricted NORI1 colorings modulo global complementation is canonically the set of all cochain representatives of the same nonzero cohomology class \(\omega\).

*Proof.* Replacing \(e,f\) by \(\tau e,\tau f\) complements both colors, preserving (2). Take any closed walk \(\gamma\) in \(Y\), and lift it to a walk \(e_0,e_1,\ldots,e_m\) in \(H\). The sum of (2) along the lift telescopes to \(c(e_0)+c(e_m)\). This is zero if the lift ends at \(e_0\), and one if it ends at \(\tau e_0\). The resulting evaluation on loops is the monodromy homomorphism of the double cover (1), proving \([a_c]=\omega\). Fix one coloring \(c_0\). For every cochain \(a\) in its cohomology class, there exists a zero-cochain \(f:V(Y)\to\mathbb F_2\) with \(a=a_{c_0}+df\). Put \(c(e)=c_0(e)+f(p(e))\). This is antipodally odd and has \(a_c=a\). If two colorings induce the same \(a\), their difference is a locally constant function on connected \(H\), hence a global constant. \(\square\)

**Theorem 2 (full geodesics are distinguished essential cycles).** Let \(P\) be any full antipodal geodesic in \(Q_n\), with undirected edge sequence \(e_1,e_2,\ldots,e_n\) using every dimension once. Its final edge is incident with the antipodal translate \(\tau e_1\) at its last cube vertex. Therefore
\[
\boxed{e_1\to e_2\to\cdots\to e_n\to\tau e_1}
\tag{3}
\]
is a length-\(n\) path in the line graph, projecting to a closed length-\(n\) cycle \(\gamma_P\) in \(Y\). Its vertices represent \(n\) distinct edge dimensions, so the projected cycle is simple. Its lifted endpoint is \(\tau e_1\), hence
\[
\boxed{\langle\omega,[\gamma_P]\rangle=1.}
\tag{4}
\]
The binary edge labels \(a_c\) around \(\gamma_P\) are the \(n-1\) consecutive internal color-change bits of the geodesic, followed by its antipodally twisted closing color-change bit.

*Proof.* Dimension-simplicity implies the edge dimensions are all distinct, so no two vertices of the projected cycle coincide. The last edge ends at \(\bar x\), where \(\tau e_1\) begins, verifying the closing adjacency. The quotient loop lifts from \(e_1\) to \(\tau e_1\), giving (4). Along its first \(n-1\) edges, (2) is the original adjacent color XOR. Along its final edge, (2) is \(c(e_n)+c(\tau e_1)=1+c(e_n)+c(e_1)\). \(\square\)

**Corollary 3 (topological equivalence of NORI1).** The unrestricted NORI1 conjecture is equivalent to the following one-crossing statement:

> Every \(\mathbb F_2\)-valued one-cochain representing the antipodal covering class \(\omega\) on \(Y=L(Q_n)/\tau\) has at least one distinguished cycle \(\gamma_P\) from (3) on which it is nonzero at only one edge.

*Proof.* The cycle (3) traverses all dimension names once, so its \(n\) possible cyclic starting positions correspond to root slides of complete antipodal geodesics. If its sole labeled edge is chosen as the closing edge, every internal adjacent color comparison is zero, making that root-slid geodesic monochromatic. Conversely a monochromatic full geodesic has no internal changes and, by (4), one closing change. Theorem 1 identifies all NORI1 colorings modulo complement with all cochain representatives of \(\omega\). \(\square\)

**Chiral translation.** An orientation bit \(\chi(e,f)\) on each directed line-graph adjacency, with \(\chi(f,e)=1+\chi(e,f)\) and \(\chi(\tau e,\tau f)=\chi(e,f)\), produces the reversal-odd turn connection
\[
B_c(e,f)=a_c([e,f])+\chi(e,f).
\]
The correction \(B_c+\chi\) is independent of the auxiliary orientation and represents the canonical class \(\omega\). Thus local reversal oddness is a choice of *chiral representation of a nontrivial cover class*, rather than an additional restriction on NORI1 colorings.

**Limit and research objective.** An arbitrary graph double cover with a distinguished family of nontrivial cycles need not have a one-crossing member: sparse signed cycles already yield high crossing counts. The essential additional structure in (3) is that these cycles arise from all full dimension-simple geodesics in the rich cubical face-incidence system. Ordinary reversal-odd boundary tournaments also define arbitrary local chiral data, but their analogue of a fixed covering class has not yet been established. Theorem 2 provides a precise topological target for a future shared one-switch theorem without assuming a separate state-graph construction.

### Triangle-square complex and antipodal cohomology

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

### Rectified graphs and complete path decoding

Rectification gives a natural geometric carrier for both unrestricted original coloring classes. Let \(L(G)\) be the line graph of a simple graph \(G\): its vertices are edges of \(G\), with adjacency whenever the original edges meet.

**Lemma 1 (universal star-alternation).** A line-graph path \(e_1,\ldots,e_m\) whose vertices are distinct comes from a consistently oriented edge-by-edge trail in \(G\) if and only if, for each interior edge \(e_j\), its intersection with \(e_{j-1}\) is the endpoint of \(e_j\) opposite from its intersection with \(e_{j+1}\). The decoded trail is then unique. This is the same local condition for every graph: the incoming and outgoing line-graph edges must meet the two distinct endpoint stars of the interior original edge.

*Proof.* An oriented trail must enter one endpoint of each interior edge and exit the other. Conversely these choices propagate the orientation from its initial edge. \(\square\)

**Theorem 2 (rectified cube).** Let \(Q_n=[-1,1]^n\), \(n\ge3\), and let \(R_n\) be the convex hull of its edge midpoints. Then
\[
\boxed{
R_n=[-1,1]^n\cap\{z:\textstyle\sum_i|z_i|\le n-1\}.
}
\]
Its one-skeleton is \(L(Q_n)\); its two-faces are precisely the star triangles (three cube edges incident at an original cube vertex) and cube-face squares (midpoints of four edges on an original square). Hence the triangle-square complex constructed in the preceding subsection is the two-skeleton of the convex sphere \(\partial R_n\cong S^{n-1}\). Cube antipodality acts as central inversion, so the quotient sphere is \(\mathbb RP^{n-1}\).

*Proof.* The displayed intersection cuts off every cube vertex along the hyperplane through its incident edge midpoints. Its facets are of two kinds: \(z_i=\pm1\), giving copies of \(R_{n-1}\), and \(\sum_i\epsilon_i z_i=n-1\), giving simplices whose vertices are the \(n\) incident edge midpoints at the original cube vertex \(\epsilon\). For \(n=3\) the polytope is the cuboctahedron, with twelve vertices, eight triangles, and six squares, and its graph is the line graph of the cube. Induct on \(n\): all lower-dimensional faces lie in the listed facets. The original-facet recursion yields the cube-square faces, while the cut-off vertex simplices yield all star triangles and adjacency of all pairs of incident cube edges. No other one- or two-faces arise. Central inversion of the original cube preserves this midpoint polytope and is antipodal on its boundary. \(\square\)

**Theorem 3 (rectified simplex).** For a simplex on \(n\ge3\) vertices, its rectification, after rescaling, is the hypersimplex
\[
\boxed{\Delta(2,n)=
\operatorname{conv}\{e_a+e_h:a\ne h\}
=\{z\in[0,1]^n:\sum z_i=2\}.}
\]
Its one-skeleton is the Johnson graph \(J(n,2)=L(K_n)\). An oriented edge
\[
\boxed{\{a,h\}\longrightarrow\{h,c\}}
\]
of the hypersimplex uniquely specifies an ordered triple \((a,h,c)\). Reversing the edge reverses the outer symbols. Therefore **every unrestricted reversal-odd boundary 3-tournament is precisely an arbitrary orientation of the edges of a rectified simplex**.

*Proof.* Hypersimplex vertices sharing the symbol \(h\) lie in the simplex face \(z_h=1\), so their segment is an edge. Vertices corresponding to disjoint pairs cannot be adjacent: their midpoint is also the midpoint of a distinct pairing of the same four symbols. Thus adjacency means sharing one symbol, and the common symbol gives the unique center \(h\). A binary choice on each oriented edge, odd under direction reversal, is the same as independently orienting every undirected Johnson-graph edge. \(\square\)

**Corollary 4 (common complete rectified paths).** A Hamilton order \(v_1,\ldots,v_n\) in the original simplex gives the star-alternating hypersimplex path
\[
\{v_1,v_2\},\{v_2,v_3\},\ldots,\{v_{n-1},v_n\},
\]
whose oriented-edge labels are precisely the tournament's consecutive triple word. A full antipodal cube geodesic similarly yields a star-alternating rectified-cube path of \(n\) vertices, one for each original dimension. Its original edge colors are vertex labels of the rectified cube; taking their chiral-corrected finite difference produces the reversal-odd oriented-edge labels from the preceding subsection. Both families use the same local star-alternation condition, and both retain their original completeness requirements.

**Research direction.** The two unrestricted problems become neighboring degrees of a shared graded incidence setup: NORI1 gives an antipodally odd vertex field on a rectified cube and its reversal-odd turn derivative; boundary tournaments give arbitrary reversal-odd oriented-edge fields on a rectified simplex. Neither arbitrary oriented rectified graphs nor arbitrary projective face-window colorings alone suffice for a low-switch theorem; the complete-path structure and local rank-two relations remain indispensable.

### Systolic cycles characterize complete cube geodesics

Let \(n\ge3\), \(H=L(Q_n)\) be the line graph of the cube, and \(\tau\) the induced antipodal involution on its vertices (original cube edges). The quotient \(Y=H/\tau\) is the one-skeleton of the antipodal quotient of the rectified cube. A closed walk of \(Y\) is essential when its lift to \(H\) starts at an edge \(e\) and ends at \(\tau e\).

**Theorem 1 (distance and equality characterization).** For every cube edge \(e\),
\[
\boxed{\operatorname{dist}_H(e,\tau e)=n.}
\]
Every shortest path in \(H\) from \(e\) to \(\tau e\) is the sequence of \(n\) undirected edges of a full antipodal geodesic of \(Q_n\), followed by the antipodal initial edge.

*Proof.* Let \(e\) have dimension \(i\). Two endpoints of \(e\) and \(\tau e\) have cube distance at least \(n-1\); equality holds when the endpoints agree in dimension \(i\). For any line-graph path \(e=e_0,e_1,\ldots,e_k=\tau e\), let \(v_j=e_{j-1}\cap e_j\) be its consecutive shared cube vertices. Each pair \(v_j,v_{j+1}\) either coincides or is connected by the cube edge \(e_j\). Thus the sequence \(v_1,\ldots,v_k\) contains a cube vertex walk of length at most \(k-1\) between an endpoint of \(e\) and an endpoint of \(\tau e\). Hence \(k\ge n\). A complete geodesic followed by the antipodal first edge gives length \(n\), so equality holds.

If \(k=n\), the intermediate shared vertices must move along an \((n-1)\)-edge shortest cube vertex path; none can coincide. This path uses every dimension other than \(i\) once. Its first vertex is one endpoint of \(e\), and its last vertex is the antipodal mate of the other endpoint of \(e\). Prepending \(e\) from that other endpoint therefore gives an \(n\)-edge full antipodal cube geodesic, and \(e_k=\tau e\) closes its line-graph path. \(\square\)

**Theorem 2 (systolic cycles).** The shortest essential closed walks in \(Y\) have length \(n\). Every such walk is a simple cycle and is the image of a full antipodal cube geodesic; conversely every full antipodal cube geodesic gives an essential cycle of length \(n\).

*Proof.* Every essential loop lifts to a line-graph path from \(e\) to \(\tau e\), so the preceding theorem bounds its length by \(n\). Equality gives a full geodesic. The first \(n\) cube edges use different dimensions, so their images in the quotient line graph are distinct and the projected walk is a simple cycle. \(\square\)

**Corollary 3 (the intrinsic one-crossing conjecture).** An antipodally odd NORI1 edge coloring corresponds, modulo global color complement, to a cellular one-cocycle \(a\) representing the nonzero class of the double cover \(\partial R(Q_n)\to\partial R(Q_n)/\tau\cong\mathbb RP^{n-1}\). The NORI1 conjecture is equivalent to:

> Every representative \(a\) of the nonzero covering class has a **shortest essential cycle** in the rectified quotient graph on which \(a\) is nonzero on only one edge.

*Proof.* The earlier line-graph representation identifies such cocycles with all antipodally odd cube-edge colorings. Their values on the essential cycle are consecutive original edge-color changes, together with one antipodally twisted closing comparison. The unique cochain crossing can be placed at the closing comparison by a root slide precisely when the corresponding full geodesic is monochromatic. \(\square\)

This description captures dimension-simplicity through intrinsic metric systolicity, rather than a separate matroid hypothesis. It does not yet transfer to the boundary-tournament Hamilton galleries: their paths in the Johnson graph of the rectified simplex are not generally shortest. The missing common structure may therefore involve a flag-sensitive notion of essential systolicity, not the ordinary graph metric alone.

### Hamilton orders as longest induced Johnson paths

**Theorem 1 (universal line-graph decoding).** Let \(G\) be any finite simple graph. Induced paths \(e_1,\ldots,e_m\) of \(m\) vertices in \(L(G)\) correspond precisely to vertex-simple paths of \(m\) edges in \(G\), with successive original edges \(e_1,\ldots,e_m\).

*Proof.* Successive edges of a vertex-simple path meet, while nonconsecutive ones are disjoint, so their line-graph vertices form an induced path. Conversely, let \(e_1,\ldots,e_m\) be an induced line-graph path. Each \(e_j\) meets its predecessor and successor at *different* endpoints, since otherwise \(e_{j-1},e_{j+1}\) would meet and form a forbidden chord. Hence the sequence of original edges is consistently traversable as a trail. Any repetition of an original vertex would make nonconsecutive trail edges incident, giving a chord in the line graph. Thus the original trail is vertex-simple. \(\square\)

**Corollary 2 (simplex Hamilton paths are maximum induced paths).** The graph of the rectified simplex \(\Delta(2,n)\) is \(J(n,2)=L(K_n)\). Its longest induced paths have \(n-1\) vertices, and all of them are
\[
\boxed{\{v_1,v_2\},\{v_2,v_3\},\ldots,\{v_{n-1},v_n\}}
\]
for Hamilton orders \(v_1,\ldots,v_n\) of the original simplex. An unrestricted reversal-odd boundary 3-tournament is an arbitrary orientation of the edges of \(J(n,2)\). Consequently its original one-switch conjecture is equivalent to the statement that **every orientation of the Johnson graph has a longest induced path whose directed-edge color word changes at most once**.

*Proof.* By Theorem 1, an induced path of \(m\) Johnson-graph vertices decodes to a simple path of \(m\) edges in \(K_n\), using \(m+1\le n\) vertices; hence \(m\le n-1\). Hamilton paths attain equality, and conversely equality forces Hamiltonicity. An oriented Johnson edge from \(\{a,h\}\) to \(\{h,c\}\) corresponds bijectively to the ordered triple \((a,h,c)\), with direction reversal encoding \(b(c,h,a)=1-b(a,h,c)\). \(\square\)

**Comparison with NORI1.** Every full cube geodesic is also a simple original graph path and hence gives an induced path in its rectified line graph. Its special completeness requirement is, more strongly, characterized by being a **shortest essential cycle** in the antipodal quotient, not by maximum induced-path length. These are intrinsic extremal graph descriptions of the two original complete-path families.

**Limitation.** Arbitrary orientations of all line graphs do not satisfy a one-switch theorem for maximum induced paths. For the original graph \(G=C_N\) with even \(N\ge8\), its line graph is \(C_N\). Alternate the clockwise directed-edge bits. Every maximum induced path uses \(N-1\) consecutive vertices and \(N-2\) edges, whose bits alternate in either traversal direction, forcing \(N-3>1\) switches. Thus the successful Johnson case would rely on additional complete exchange geometry, not merely being a line graph.

### Cyclic variation selection for antipodal and boundary path galleries

The two motivating conjectures have a uniform *orbitwise* description in terms of cyclic binary variation, including their distinct periodicity and observation widths. This separates the elementary root-selection problem from the difficult problem of finding a favorable orbit.

Let \(L\ge2\), let \(\epsilon\in\mathbb F_2\), and take an infinite binary sequence \(a_j\) satisfying the twisted periodicity
\[
a_{j+L}=a_j+\epsilon.
\]
Its adjacent comparison bits
\[
\delta_j=a_j+a_{j+1}
\]
are ordinarily \(L\)-periodic. Write \(D=\sum_{j=0}^{L-1}\delta_j\), as an integer, and for \(1\le m\le L\) consider every length-\(m\) window \(W_t=(a_t,\ldots,a_{t+m-1})\).

**Theorem 1 (twisted cyclic-window switch selection).** For every such sequence,
\[
\boxed{
D\equiv\epsilon\pmod2,\qquad
\min_{0\le t<L}\operatorname{sw}(W_t)
=D-\max_{0\le t<L}\sum_{j=0}^{L-m}\delta_{t+j}.
}
\tag{1}
\]
The omitted comparison block has length \(q=L-m+1\). Therefore an orbit has a window with at most \(r\) switches if and only if it has a cyclic block of \(q\) comparisons containing at least \(D-r\) changes.

*Proof.* The XOR of the \(L\) successive comparisons telescopes to \(a_0+a_L=\epsilon\). Each length-\(m\) window contains \(m-1\) successive comparisons, so it omits \(L-(m-1)=q\) consecutive comparisons from one period. Its switch count is \(D\) minus the number of ones in the complementary block, proving (1). \(\square\)

#### NORI1: antiperiodic cycles, one omitted comparison

For every freely rooted full cube geodesic \(P(x;\pi)\), the canonical root slide
\[
T(x;\pi_1,\ldots,\pi_n)=(x+e_{\pi_1};\pi_2,\ldots,\pi_n,\pi_1)
\]
shifts the true edge-color word by one bit and appends the complement of the first bit. Consequently the orbit's color sequence has \(L=m=n\), twist \(\epsilon=1\), and omitted-block size \(q=1\). Formula (1) becomes
\[
\boxed{D\text{ odd},\qquad
\min_{0\le t<n}\operatorname{sw}(P(T^t(x;\pi)))=D-1.}
\tag{2}
\]
Thus an orbit contains a monochromatic full geodesic if and only if \(D=1\); an at-most-one-switch full geodesic exists on the orbit if and only if \(D=1\) as well. This recovers the cyclic defect criterion of the earlier chiral-turn subsection without reference to a chosen chirality gauge.

#### Boundary tournaments: periodic cycles, three omitted comparisons

Let \(n\ge4\) and let \(b(a,h,c)\) be an arbitrary reversal-odd boundary tournament. For a cyclic vertex order \((v_0,\ldots,v_{n-1})\), set
\[
a_j=b(v_j,v_{j+1},v_{j+2}),\quad j\in\mathbb Z/n\mathbb Z.
\tag{3}
\]
Every Hamilton order obtained by cyclic rotation reads \(m=n-2\) consecutive entries \(a_t,\ldots,a_{t+n-3}\). Thus \(L=n,\epsilon=0\), and \(q=3\). Let \(\delta_j=a_j+a_{j+1}\), and let \(D=\sum_j\delta_j\). Theorem 1 yields
\[
\boxed{
D\text{ even},\qquad
\min_{\text{cyclic rotations}}\operatorname{sw}
=D-\max_t(\delta_t+\delta_{t+1}+\delta_{t+2}).
}
\tag{4}
\]

**Corollary 2 (complete orbitwise boundary one-switch criterion).** A cyclic vertex order has a rotation giving an at-most-one-switch Hamilton tight path if and only if one of the following holds:
\[
\boxed{
D\le2,\qquad\text{or}\qquad
D=4\ \text{and three successive cyclic comparisons are all one.}
}
\tag{5}
\]
No cyclic order with \(D\ge6\) has an at-most-one-switch Hamilton path among its rotations. Reversing the cyclic order preserves \(D\) and condition (5).

*Proof.* Since \(D\) is even, \(D=0\) gives all monochromatic windows. For \(D=2\), some three-comparison block contains at least one change, so (4) gives at most one. If \(D=4\), equation (4) gives at most one precisely when the maximum three-comparison block has all three changes. If \(D\ge6\), even omitting three changes leaves at least three. Reversing the order complements and reverses the cyclic triple-color word by reversal oddness, which reverses the cyclic comparison vector and preserves its total and its runs of length three. \(\square\)

**Corollary 3 (a sharp reduction of the unrestricted boundary conjecture).** The unrestricted boundary-tournament one-switch conjecture is equivalent to the following cyclic variation-selection assertion:

> For every reversal-odd binary coloring of ordered distinct triples, there is a cyclic ordering of all vertices whose cyclic triple-color comparison word satisfies (5).

This is an equivalent reformulation, not a proven existence claim. It reduces the desired bound to finding a cycle with either at most two transitions or four transitions containing a run of three consecutive changes. The second alternative must be retained; merely conjecturing the existence of a cycle with \(D\le2\) is a strictly stronger problem.

**Structural point.** Equation (1) is one common root-selection theorem, not a disjunction of two classes. The original systems differ only in intrinsic twist \(\epsilon\), orbit length \(L\), and observation width \(m\): NORI1 has \((\epsilon,L-m)=(1,0)\), while ordinary boundary tournaments have \((0,2)\). In both cases the unresolved mathematics is *inter-orbit selection*: using rank-two face exchanges, projective incidence, or equivariant topology to force an orbit of sufficiently low variation.

#### Deletion of switches and minimal obstructions

Let \(H\) be a finite graph whose vertices are the objects read by path color words, and let \(R\) be a fixed-point-free involution of its vertex set which preserves adjacency. A permitted coloring is a function \(c:V(H)\to\mathbb F_2\) with \(c(Rv)=1+c(v)\). Write \(D(c)=\{uv\in E(H):c(u)\ne c(v)\}\). We allow a retained transition set \(S\subseteq D(c)\), without requiring equality. Throughout, transitions used by a complete path are distinct, including after identification under \(R\) when that identification is used.

**Theorem 4 (intrinsic description of the deletion-closed family).** For any set \(S\subseteq E(H)\), there exists a permitted coloring with \(S\subseteq D(c)\) if and only if
\[
K(S)=\bigl(V(H),\,S\cup\{\{v,Rv\}:v\in V(H)\}\bigr)
\]
is bipartite. If transitions are retained in \(R\)-orbits, replace \(S\) in this formula by the union of their lifts. Every connected component of \(K(S)\) has two possible colorings, independently of the other components.

*Proof.* Every edge displayed in \(K(S)\) requires its two endpoint bits to differ. A proper binary vertex coloring satisfies all these requirements, and the opposition edges give the required identity under \(R\). Conversely every permitted completion of \(S\) is a proper binary coloring of \(K(S)\). The usual alternating coloring along paths proves that such a coloring exists precisely when there is no odd cycle. In each connected bipartite component the coloring is determined by one vertex bit. \(\square\)

For cubes with \(n\ge3\), take \(H=L(Q_n)\), with cube edges as its vertices and cube antipodality as \(R\). For boundary tournaments on at least four vertices, the vertices of \(H\) are ordered distinct triples; its edges are the unordered pairs
\[
\{(a,b,c),(b,c,d)\},
\]
where \(a,b,c,d\) are distinct, and \(R(a,b,c)=(c,b,a)\). Thus an edge of \(H\) is a comparison of consecutive triple windows. In both models the original switch sets are \(R\)-invariant. A complete path uses each transition orbit at most once: on a cube path its turns occur at distinct antipodal vertex classes; in a Hamilton order distinct consecutive four-vertex windows cannot coincide up to reversal.

Theorem 4 gives an intrinsic hereditary condition for switch deletion. In particular, omitting a transition from \(S\) imposes no equality constraint on its endpoint colors.

**Proposition 5 (critical witnesses and the common threshold).** Let \(\mathcal P\) be a finite family of complete paths and let \(T(P)\) denote the set of transition orbits used by \(P\). If \(S\) is inclusion-minimal subject to
\[
|S\cap T(P)|\ge r+1\qquad(P\in\mathcal P),
\]
then for each \(s\in S\) there is a path \(P_s\) such that
\[
s\in T(P_s),\qquad |S\cap T(P_s)|=r+1.
\]
A counterexample to either motivating conjecture yields such a set with \(r=1\), satisfying the bipartiteness condition of Theorem 4.

*Proof.* By minimality some complete path has at most \(r\) retained transitions after deleting \(s\). Restoring \(s\) changes its count by at most one, whereas the original count is at least \(r+1\). Thus the path contains \(s\) and has count \(r+1\).

A boundary counterexample has at least two switches on every Hamilton order by definition. A cube coloring with no monochromatic full geodesic also has at least two switches on every full geodesic: the root-slide formula (2) turns any at-most-one-switch geodesic into a monochromatic one. Choose a minimal subset of transition orbits retaining this lower bound. Its lift is contained in the original switch set and hence satisfies Theorem 4. Conversely any such bipartite retained obstruction extends to a permitted coloring; that coloring has at least two switches on every complete path. \(\square\)

The reduction for cubes uses the one-switch threshold before deleting transitions. Root sliding need not turn a retained one-switch path into a retained zero-switch path after deletion.

##### All rotations of a critical witness

The next lemma uses cyclic comparison positions without assuming they arise from a binary word. Fix integers \(r\ge0\) and \(q\ge1\). Let \(\mathcal C\) be a family of cycles of length greater than \(q\), each with distinct transition identifiers in cyclic order. A complete path consists of a cycle with a block of \(q\) consecutive transitions omitted. Let \(S\) be a set of identifiers. For a cycle \(C\), put
\[
d_S(C)=|S\cap C|,\qquad
M_S(C)=\max_{\substack{B\subset C\\B\text{ a cyclic }q\text{-block}}}|S\cap B|.
\]
The least retained count among its complete paths is \(d_S(C)-M_S(C)\).

**Theorem 6 (bounded cyclic witnesses).** Suppose \(S\) is inclusion-minimal with every complete path having at least \(r+1\) retained transitions. Each \(s\in S\) belongs to a cycle \(C_s\) and has an omitted block \(B_s\) avoiding \(s\), such that
\[
|S\cap(C_s\setminus B_s)|=r+1,\qquad
r+2\le d_S(C_s)\le r+q+1.
\]
Moreover every \(q\)-block \(B\) in this cycle satisfies
\[
|S\cap B|\le d_S(C_s)-(r+1),
\]
with equality for \(B_s\).

*Proof.* Proposition 5 supplies a complete witness containing \(s\), hence a cycle and omitted block avoiding \(s\). Its total retained count is \(r+1+|S\cap B_s|\), proving the upper bound. Every rotation is a complete path, so the displayed block inequality follows. Since the cycle contains a retained transition, some \(q\)-block contains at least one, and the inequality gives the lower bound. \(\square\)

**Corollary 7 (cube witnesses).** A hypothetical NORI1 counterexample has an antipodally invariant retained set \(S\), whose lift satisfies Theorem 4, with the following properties:

1. Every projective Petrie cycle contains at least three members of \(S\).
2. Every \(s\in S\) lies on a projective Petrie cycle containing precisely three members of \(S\).

These two properties are equivalent to minimality among retained sets for which every full geodesic has at least two retained transitions.

*Proof.* The projective Petrie cycle has \(n\) turns; its root slides omit each single turn in succession. Thus the least retained path count is \(\max\{0,d_S(C)-1\}\). Theorem 6 with \(q=1,r=1\) gives three retained turns on each critical witness cycle. Conversely a cycle with three retained turns becomes a cycle with two after deleting any one of them, and omitting one of the remaining two gives a complete path with one retained transition. \(\square\)

**Corollary 8 (boundary witness classification).** A hypothetical boundary counterexample has a reversal-invariant retained set satisfying Theorem 4. Each retained transition \(s\) has a cyclic Hamilton witness of one of these forms:

- Three retained positions, with cyclic distances between successive retained positions at least three.
- Four retained positions, with no block of three consecutive retained positions, and a three-position block avoiding \(s\) that contains two retained positions.
- Five retained positions, with a block of three consecutive retained positions avoiding \(s\).

These are the complete possibilities for a cycle to certify that deleting \(s\) destroys the lower bound of two on some rotation, while all rotations originally satisfy that bound.

*Proof.* Hamilton orders omit three cyclic comparisons, so apply Theorem 6 with \(q=3,r=1\). The total \(d\) is three, four, or five. If \(d=3\), every three-position block contains at most one retained position, which is equivalent to the spacing condition; a block containing one of the other retained positions avoids \(s\). If \(d=4\), every block has at most two retained positions, and the witness block must have two and avoid \(s\). If \(d=5\), the lower bound on every rotation is automatic, and a witness block has three retained positions and avoids \(s\). These conditions are also sufficient, by restoring the omitted block and counting the two retained positions outside it. \(\square\)

In particular the first boundary case requires at least nine vertices. Neither the odd cube count nor the even boundary count of the original switch word can be imposed on a retained set after deletion.

##### Exchange inequalities and odd-cycle certificates

**Theorem 9 (replacement demand).** Let \(S\) meet every complete path in at least \(k\) transitions, and let \(P\) be a complete path meeting it in precisely \(k\). For every complete path \(Q\),
\[
|S\cap(T(Q)\setminus T(P))|
\ \ge\
|S\cap(T(P)\setminus T(Q))|.
\]
Equality makes \(Q\) another path meeting \(S\) in precisely \(k\). The same statement holds for any family of cycles with a uniform lower bound \(k\), in particular the three-turn cube witnesses of Corollary 7.

*Proof.* Subtract the counts on \(P\) and \(Q\). Their common transitions cancel, and the resulting difference is nonnegative. \(\square\)

This inequality retains the complete-path constraint in every exchange. An adjacent dimension exchange changes at most three turn positions of a cube path or projective Petrie cycle. An adjacent vertex exchange changes at most five comparison positions of a boundary Hamilton path. Thus removing \(a\) retained transitions in one such exchange requires at least \(a\) of at most three, respectively five, replacement transitions to be retained. The bounds remain valid for deleted sets; they do not use the parity of a completed color word.

**Corollary 10 (bipartite exclusion in an exchange).** Suppose \(F\subseteq S\) is known, and form \(K(F)\) as in Theorem 4. A transition whose endpoints are joined by an even-length path in \(K(F)\) cannot belong to \(S\). Consequently, in an exchange from Theorem 9 that removes \(a\) retained transitions, at least \(a\) replacement transitions must avoid this exclusion. If fewer than \(a\) do so, the assumed obstruction has no permitted completion. If precisely \(a\) do so, every one of them is forced into \(S\).

*Proof.* Adding an edge between the endpoints of an even-length path gives an odd closed walk and hence an odd cycle. This contradicts bipartiteness of \(K(S)\). Apply this exclusion to the replacement demand. \(\square\)

For an orbit transition the exclusion may be tested on either lift; opposition edges ensure that the tests agree. Repeatedly adjoining forced transitions to \(F\) can therefore yield an odd-cycle certificate of inconsistency. This is a sufficient contradiction mechanism. A theorem forcing it to terminate in an odd cycle for every critical obstruction in either path geometry remains open.

The conclusions above reduce both original problems to exclusion of bipartite critical transition sets with complete two-transition path witnesses. Cube root slides strengthen those witnesses to three-transition Petrie cycles, while Hamilton rotations restrict them to the three configurations of Corollary 8. Establishing a global exchange argument from these constrained witnesses is the remaining existence step.


#### Hereditary containers and the structure of tight witnesses

The containing transition set may be fixed before any deletion. If \(\mathcal B\) is any collection of transition sets, its downward closure
\[
\mathcal D(\mathcal B)=\{S:S\subseteq B\text{ for some }B\in\mathcal B\}
\]
is hereditary. For any complete-path family, the assertion that every \(S\in\mathcal D(\mathcal B)\) has a path of retained count at most one is equivalent to the same assertion restricted to \(B\in\mathcal B\). Indeed a favorable path for the containing set remains favorable after deletion; conversely the containing sets themselves belong to the downward closure. Critical witness arguments therefore require no symmetry or coloring condition beyond membership in the chosen hereditary class.

##### An oddness-free cube formulation

For a cube \(Q_n\), let \(S\) be a set of its unoriented two-edge turns. Regard \(S\) as an edge set in the line graph \(L(Q_n)\), and let \(\sigma_S(P)\) count the turns of a geodesic \(P\) belonging to \(S\).

**Theorem 11 (bipartite turn reformulation).** The following all-dimensional assertions are equivalent:

1. Every antipodally odd binary cube-edge coloring has a monochromatic full antipodal geodesic.
2. Every binary cube-edge coloring has a full antipodal geodesic with at most one color change.
3. For every \(n\) and every \(S\subseteq E(L(Q_n))\) such that the graph \((V(L(Q_n)),S)\) is bipartite, some full antipodal geodesic \(P\) satisfies \(\sigma_S(P)\le1\).

The equivalence of the first two assertions is the established Leader–Long dimension-shift equivalence, recorded previously in the project's doubling treatment. The third is its hereditary switch formulation.

*Proof.* A binary cube-edge coloring is a binary vertex coloring of \(L(Q_n)\). Its switch set is a cut in that line graph. A set \(S\) is contained in such a cut if and only if \((V(L(Q_n)),S)\) is bipartite, by assigning either side of each bipartite component color zero. Thus assertion 2 supplies the favorable path in assertion 3. Assertion 3 applied to the full switch set gives assertion 2.

For completeness, write \(A_n\) and \(B_n\) for assertions 1 and 2 in dimension \(n\). Then \(B_n\) implies \(A_n\): if an antipodally odd coloring has a one-change geodesic, write it as \(L:x\to y\) of color \(a\), followed by \(R:y\to\bar x\) of color \(1-a\). The concatenation
\[
L^{-1}:y\to x,\qquad \bar R^{-1}:x\to\bar y
\]
is monochromatic of color \(a\) and uses each dimension once. A path already monochromatic requires no change.

Conversely, for an arbitrary coloring \(c\) on \(Q_n\), construct a coloring \(C\) on \(Q_n\times\{0,1\}\) by giving the lower copy of an edge \(e\) color \(c(e)\), the upper copy color \(1-c(\bar e)\), and the vertical edge at \(x\) color \(x_1\). This is an antipodally odd coloring. Under \(A_{n+1}\), take a monochromatic full geodesic and orient it so its vertical crossing is from layer zero to layer one. Its lower portion \(L:x\to y\) and upper portion \(R:y\to\bar x\) use complementary dimension sets. If the common color is \(a\), then \(L^{-1}\) is colored \(a\) in the original cube, whereas the antipodal image of the upper portion, reversed, is colored \(1-a\). Their concatenation goes from \(y\) to \(\bar y\), uses each original dimension once, and has at most one change. Hence \(A_{n+1}\) implies \(B_n\), proving the all-dimensional equivalence. The one-dimensional assertion \(B_1\) is immediate. \(\square\)

Here bipartiteness is imposed on the retained turn set alone; there are no opposition edges. Deletion is ordinary single-turn deletion. If assertion 3 fails, an inclusion-minimal failing set is bipartite and every retained turn belongs to a full geodesic with precisely two retained turns. This reformulation removes antipodal oddness from the switch hypothesis while preserving equivalence to the full NORI1 problem.

The three-turn Petrie conclusion of Corollary 7 concerns antipodally invariant transition-orbit sets. It is a separate, stronger conclusion available in that symmetric formulation; it is not asserted for arbitrary sets from Theorem 11.

##### Uncrossing two-switch witnesses

Let \(S\) be any retained transition set for which every complete path has at least two retained transitions. Call a complete path *tight* in this paragraph when it has precisely two retained transitions. The adjective refers only to equality in this lower bound; for boundary tournaments the underlying paths are also tight paths in the usual hypergraph sense.

**Theorem 12 (prefix agreement under admissible tail exchange).** Suppose two tight complete paths \(P,Q\) share an observation at which both exchanges of their suffixes give admissible complete paths, with no new comparison at the join. Let \(a\) and \(b\) be their retained counts before the common observation, including comparisons ending at it. Then
\[
a=b.
\]
Both exchanged paths are tight. The conclusion depends only on the path family and \(S\); no binary coloring or opposition relation is needed.

*Proof.* The two hybrid paths have retained counts
\[
a+(2-b),\qquad b+(2-a).
\]
Each is at least two. The first inequality gives \(a\ge b\), and the second gives \(b\ge a\). Thus both counts are two. \(\square\)

The common observation and completeness conditions can be expressed directly in the two geometries.

**Corollary 13 (coherent prefix levels on cube witnesses).** Fix a root \(x\) in \(Q_n\). Orient each cube edge away from \(x\), according to increasing Hamming distance. Let \(E_x\) be the set of edges occurring on two-switch full geodesics rooted at \(x\). For every \(e\in E_x\), the number of retained turns before and through the observation \(e\) is independent of the chosen two-switch geodesic containing it. Denote it by
\[
h_x(e)\in\{0,1,2\}.
\]
If consecutive edges \(e,f\) occur on such a geodesic, then
\[
h_x(f)-h_x(e)=\mathbf1_{\{\{e,f\}\in S\}}.
\]
Initial edges have level zero and terminal edges level two. Any full rooted geodesic each of whose consecutive turns occurs on some two-switch rooted geodesic has precisely two retained turns.

If \(S\) is antipodally invariant, then \(E_x\) is antipodally invariant and
\[
h_x(\bar e)=2-h_x(e).
\]

*Proof.* Two full geodesics from \(x\) containing the same edge traverse it in the same direction. Their dimension sets before that edge agree: they are the dimensions in which its initial vertex differs from \(x\). Exchanging their suffixes at the common edge therefore preserves every dimension precisely once. No new comparison is created because the edge observation itself is shared. Theorem 12 proves independence of \(h_x\), and the increment formula follows on each witness.

For a full geodesic assembled from witness turns, the increment formula telescopes. Its first edge occurs as a first edge on every rooted geodesic containing it, so has level zero; its last edge has level two. The retained count is consequently two.

When \(S\) is antipodally invariant, reversing a full geodesic and complementing all its vertices gives another full geodesic from the same root \(x\), with the same retained count. The prefix ending at \(\bar e\) in the transformed path corresponds to the suffix beginning at \(e\) in the original. Those two counts sum to two. \(\square\)

Thus the union of rooted witnesses has three coherent edge regions. Each retained turn on a witness crosses from level zero to one, or from level one to two. In the symmetric formulation, antipodality exchanges these two kinds of crossings.

**Corollary 14 (coherent prefix levels on Hamilton witnesses).** Let \(V\) be the vertex set of a boundary path problem with an arbitrary retained comparison set \(S\). For a prefix of a two-switch Hamilton order, retain its used vertex set \(U\) and its final ordered triple \(t\). The prefix switch count is determined by \((U,t)\), independently of the witness order. In particular two witnesses with the same used set and final ordered triple can exchange their suffixes, producing two further two-switch Hamilton orders.

*Proof.* Both suffixes use precisely the vertices of \(V\setminus U\). The common final triple supplies the same preceding observation for the first comparison of either suffix. Both exchanges therefore preserve distinct vertices and create no new comparison. Apply Theorem 12. \(\square\)

Repeated admissible tail exchanges preserve the prefix levels and generate further complete witnesses. These conclusions use the support required by geodesicity or Hamilton completeness explicitly. Equality of terminal observations alone is sufficient for rooted cube witnesses, because the root determines their used dimensions; for Hamilton witnesses the used vertex set remains necessary.

##### The graph of two-switch witness pairs

For a retained set \(S\), define a graph \(W_S\) on vertex set \(S\) by
\[
st\in E(W_S)
\quad\Longleftrightarrow\quad
S\cap T(P)=\{s,t\}
\text{ for some complete path }P.
\]
Criticality says that \(W_S\) has no isolated vertices. Rotational closure supplies stronger conclusions.

**Theorem 15 (certified witness triangles on the cube).** In the antipodally invariant critical cube formulation of Corollary 7, every vertex and every edge of \(W_S\) lies in a triangle supplied by a projective Petrie cycle containing precisely three retained turns.

*Proof.* For any tight geodesic \(P\), its projective Petrie cycle \(C\) has all the turns of \(P\) and one closing turn. Thus \(|S\cap C|\le3\). Every cycle has at least three retained turns by Corollary 7, so its count is three. Root slides can omit each of these three turns in succession, producing all three pairs as two-switch complete witnesses. Every edge of \(W_S\) therefore lies in the corresponding triangle. Criticality covers every vertex by an edge. \(\square\)

The triangle vertices are switches, not colored observations. This assertion imposes no odd-cycle contradiction on the transition constraint graph from Theorem 4.

**Theorem 16 (boundary rotational witness graphs).** Let \(C\) be a cyclic Hamilton order whose every rotation has retained count at least two, and suppose some rotation has count two. Define \(W_C\) on the retained positions in \(C\), with an edge for each retained pair left by a two-switch rotation. Then:

1. If \(C\) has three retained positions, \(W_C=K_3\).
2. If \(C\) has four retained positions, \(W_C\) is bipartite.
3. If \(C\) has five retained positions and the cycle has length greater than five, the nonisolated part of \(W_C\) is a path with one, two, or three edges.
4. If the cycle has length five and all its positions are retained, \(W_C=C_5\).

These exhaust the possibilities.

*Proof.* Theorem 6 restricts the number of retained positions to three, four, or five.

For three, the spacing condition ensures that a three-position block can omit any one retained position while leaving the other two, giving \(K_3\).

For four, let \(J_C\) be the graph on the four retained positions joining a pair when both can be contained in a three-position cyclic block. No such block contains three retained positions. Consequently \(W_C\) has the edge complementary to each edge of \(J_C\), where complementation means taking the other two vertices among the four. The degree of \(J_C\) is at most two: the possible neighbors of a marked position have offsets \(-2,-1,1,2\), and choosing any three of these would produce three consecutive marked positions, which is forbidden. A triangle in \(W_C\) would correspond to three edges of \(J_C\) with a common endpoint, contrary to that degree bound. A graph on four vertices is nonbipartite only if it contains a triangle. Hence \(W_C\) is bipartite.

For five on a longer cycle, an unretained position exists, so the retained positions split into runs. A two-switch rotation must omit a block of three consecutive retained positions. Since there are only five retained positions in total, at most one run has length at least three. If its length is three, four, or five, its consecutive triple blocks leave respectively one, two, or three distinct retained pairs. Naming a length-five run \(a,b,c,d,e\), these pairs are \(de,ae,ab\), which form a three-edge path; shortening the run gives the shorter paths. Remaining retained positions are isolated where applicable.

On a five-cycle with all positions retained, omitting a cyclic block of three leaves two consecutive positions. The five possible pairs form \(C_5\). \(\square\)

Theorem 16 requires no binary parity condition and therefore includes the pentagon case. In the original completed boundary coloring, a five-cycle cannot have all five comparisons switched because a periodic binary word has even cyclic variation. An arbitrary hereditary container need not enforce that restriction.

Theorems 12–16 supply structure beyond individual private witnesses: coherent switch counts at admissible joins, closure under complete-path recombination, and certified small witness-pair graphs. A proof of existence must still compare prefix levels across different supports or roots, or derive a contradiction from the containing set and these witness configurations. No such global comparison is established here.


#### Coupling deletion witnesses

Retain the antipodally invariant cube formulation: \(S\) is a set of projective turn orbits, contained in the switch set of some antipodally odd cube-edge coloring, and every full geodesic has retained count at least two. Assume \(S\) is inclusion-minimal for this lower bound. A full geodesic uses any given turn orbit at most once.

**Proposition 17 (complete description after one deletion).** For every \(s\in S\), put \(S_s=S\setminus\{s\}\). Then
\[
\min_P\sigma_{S_s}(P)=1.
\]
Its one-switch geodesics are precisely the original two-switch geodesics containing \(s\). Their projective Petrie cycles contain three original retained turns, one of which is \(s\). After deletion those cycles have two retained turns. Among the \(n\) cyclic cuts of each such projective cycle, precisely two have retained count one; the other \(n-2\) have count two.

*Proof.* Deleting \(s\) reduces the count on any complete path by at most one, so every path still has count at least one. Criticality supplies one of count one. If a path has count one after deletion, its original count is at least two and differs by at most one, so its original count is two and it contains \(s\). The converse is immediate. Theorem 15 identifies its original cyclic count as three. Removing \(s\) leaves two active cyclic comparisons. A cut omits one comparison, giving count one precisely when that comparison is one of the remaining two. \(\square\)

Thus the two optimal rotations after deletion supply two cuts of the same two-switch period. Coupling them to other witnesses requires comparisons between their supports or roots.

##### Deletion fixes the position of a switch at shared prefixes

The following statement does not require a coloring or an opposition relation. It applies to cube turns, boundary comparisons, or another complete-path family with the stated exchange property.

**Theorem 18 (uniform intersections at shared prefixes).** Let \(k\ge1\), and let \(S\) be a transition set for which every complete path has retained count at least \(k\). Suppose no complete path repeats a transition identifier. Fix prefix data \(q\) such that any two complete paths through \(q\) may exchange their suffixes in both directions, preserving completeness and creating no new comparison. Consider all paths through \(q\) having retained count \(k\).

Their prefix count has one common value \(h(q)\). For each retained transition \(s\) used by any such path, whether \(s\) occurs in the prefix is independent of the chosen path through \(q\) containing \(s\). Write this indicator as \(b_q(s)\in\{0,1\}\). Every retained \(k\)-set \(A\) realized by a path through \(q\) satisfies
\[
\boxed{\sum_{s\in A}b_q(s)=h(q).}
\]
In particular, all realized \(k\)-sets meet the subset \(\{s:b_q(s)=1\}\) in the same number of elements.

*Proof.* If two paths have prefix counts \(a,b\), their exchanged paths have counts \(a+k-b\) and \(b+k-a\). Both are at least \(k\), so \(a=b\). This defines \(h(q)\).

Fix \(s\), and restrict to paths through \(q\) using \(s\). After deleting \(s\), all these paths have count \(k-1\). Every complete path has count at least \(k-1\), because no path repeats \(s\). Applying the same tail-exchange argument to \(S\setminus\{s\}\), the deleted prefix count has a common value \(h_s(q)\). Therefore
\[
b_q(s)=h(q)-h_s(q)
\]
is independent of the path and equals the indicator that its prefix used \(s\). Summing these indicators on a path proves the displayed formula. \(\square\)

For cube geodesics, fix a root and take \(q\) to be an edge observation. The root determines its orientation and the dimensions used before it. For Hamilton orders, take \(q=(U,t)\), where \(U\) is the used vertex set and \(t\) the final ordered triple. These are the exchange data verified in Corollaries 13–14.

**Corollary 19 (bipartite witness pairs at a middle observation).** In the case \(k=2\), let \(W_q\) be the graph on retained switches occurring in two-switch complete paths through \(q\), with an edge for each pair realized by such a path. If \(h(q)=1\), then
\[
\boxed{W_q\text{ is bipartite},}
\]
with the sides given by \(b_q(s)=0\) and \(b_q(s)=1\).

Consequently, witnesses for the pairs
\[
\{s_0,s_1\},\ \{s_1,s_2\},\ \ldots,\
\{s_{2r},s_0\}
\]
cannot all share compatible prefix data at which each path has one retained switch before the join. In particular, the three pairs of a certified witness triangle cannot all have a common compatible middle observation.

*Proof.* Theorem 18 gives \(b_q(s)+b_q(t)=1\) on every witness edge. This is a proper binary vertex coloring of \(W_q\). Around an odd cycle the roles would alternate and return to their complement, which is impossible. \(\square\)

This is a coupling criterion on the switch witnesses themselves. It applies to every hereditary containing-set hypothesis. Criticality is used to ensure that every switch has witnesses; the exclusion at a common prefix follows from the lower bound and admissible recombination.

##### Two antipodally odd binary labels after deletion

Fix a cube root \(x\). Let \(E_x^s\) be the edges occurring in the one-switch \(S_s\)-geodesics from \(x\), equivalently in the original two-switch geodesics from \(x\) containing \(s\). Define
\[
u_x^s(e)=\text{the }S_s\text{-prefix count through }e,
\qquad
b_x^s(e)=\text{the indicator that }s\text{ has occurred through }e.
\]

**Theorem 20 (binary labels and antipodal complementation).** Both functions are well defined on \(E_x^s\), have values in \(\{0,1\}\), and satisfy
\[
h_x(e)=u_x^s(e)+b_x^s(e),
\]
where \(h_x\) is the original two-switch prefix level. Moreover \(E_x^s\) is antipodally invariant, and
\[
\boxed{
u_x^s(\bar e)=1-u_x^s(e),\qquad
b_x^s(\bar e)=1-b_x^s(e).
}
\]
Along any consecutive edge pair appearing in one of these witnesses, \(b_x^s\) changes precisely at \(s\), and \(u_x^s\) changes precisely at the other retained switch. Their disagreement set is the middle edge region \(h_x=1\).

*Proof.* Proposition 17 gives the family of one-switch paths. Theorem 18 with \(k=2\) proves that their deleted prefix counts and indicators of \(s\) are well defined at each shared edge. Both are zero or one, and their sum is the original prefix count.

Reverse a witness and complement all its vertices. Antipodal invariance of \(S_s\) makes this another one-switch geodesic from \(x\), and it still contains \(s\) in the original set. The prefix count through \(\bar e\) in the transformed path is the suffix count after \(e\) in the original path, so its deleted count is \(1-u_x^s(e)\). The original path uses \(s\) once, and the transformed prefix contains it precisely when the original suffix does, giving \(1-b_x^s(e)\). The increment statements follow by counting on each witness. Finally two binary values have sum one precisely when they differ. \(\square\)

The retained set need not itself be the switch set of a binary coloring. Nevertheless, each critical deletion canonically produces two antipodally odd binary labels on its witness domain. One label records the deleted transition, and the other records its witness partner. At a compatible middle edge these labels determine the consistent switch roles of Corollary 19.

##### A component condition for coupling rooted witnesses

Let \(E_x\) be the union of all two-switch rooted geodesic edges. Form a graph \(J_x\) on \(E_x\), retaining the adjacency \(\{e,f\}\) precisely when that turn belongs to \(S\) and occurs consecutively on some two-switch geodesic from \(x\). This graph records only retained transitions, while preserving their rooted complete-path certificates.

**Proposition 21 (paired retained-transition components).** If \(S\) is contained in a NORI1 switch set, no connected component of \(J_x\) contains both \(e\) and \(\bar e\). Equivalently, antipodality pairs the connected components of \(J_x\) without fixing a component.

*Proof.* By Corollary 13, the integer prefix level \(h_x\) changes by one across every edge of \(J_x\). Hence \(h_x\bmod2\) is a proper binary coloring of \(J_x\). Antipodality sends \(h_x(e)\) to \(2-h_x(e)\), preserving this parity.

Let \(c\) be any antipodally odd cube-edge coloring whose switch set contains \(S\). On every edge of \(J_x\), both \(c\) and \(h_x\bmod2\) change, so their sum is constant on each connected component. Were \(e\) and \(\bar e\) in the same component, this constant would have equal values at them. Antipodality complements \(c\) and preserves \(h_x\bmod2\), making those values different. This is a contradiction.

The graph \(J_x\) is antipodally invariant by the witness reversal used in Corollary 13. A component is fixed by antipodality precisely when it contains an antipodal vertex pair, proving the equivalent statement. \(\square\)

This gives another sufficient contradiction certificate: a chain of retained transitions, each lying in a rooted two-switch witness, that joins an edge observation to its antipode. It uses ordinary connectivity only to contradict the containing coloring; the constituent transitions retain their complete geodesic certificates.

The other switch-matroid treatment identifies legal signature changes on the folded line graph with its binary cut space, whose minimal nonzero supports are cographic circuits. This describes changes of a completed coloring. The deletion arguments here concern subsets of a fixed containing signature; Theorems 18–20 remain valid before a completion is chosen. Coupling must therefore supply either a compatible middle observation for an odd cycle of witness pairs, or an antipodally invariant component forbidden by Proposition 21, or another contradiction using the containing set. Criticality alone has not yet been shown to force any of these global configurations.


#### Root transport, independent arms, and cographic bond moves

The deletion witnesses admit a factorization into independent geodesic arms. This makes root transport a finite-dimensional comparison of two minimum switch counts and gives a family of legal bond moves.

Let \(s=([v],\{i,j\})\in S\) be a retained projective turn. Fix a lift \(v\), and a root \(x\) for which
\[
D=\{d:x_d\ne v_d\}
\]
contains \(i\) and excludes \(j\). A full geodesic from \(x\) containing this lift of \(s\) arrives at \(v\) in direction \(i\) and leaves in direction \(j\). Define
\[
\begin{aligned}
p_s(x,v)&=\min\{\sigma_S(A):
 A:x\to v\text{ uses }D,\text{ with final direction }i\},\\
q_s(x,v)&=\min\{\sigma_S(B):
 B:v\to\bar x\text{ uses }[n]\setminus D,\text{ with first direction }j\}.
\end{aligned}
\]
The costs here count only the internal turns of each arm. No turn at the join \(v\) is included. Both families of arms are nonempty. For the other eligible roots interchange the names \(i,j\). Eligibility is the affine condition
\[
x_i+x_j=1+v_i+v_j\pmod2.
\]

**Theorem 22 (arm factorization and opposite branches).** Suppose every full geodesic has retained count at least two. Then
\[
p_s(x,v)+q_s(x,v)\ge1.
\]
There is a two-switch geodesic from \(x\) through this lift of \(s\) if and only if \(p_s(x,v)+q_s(x,v)=1\). In that case the family of all such geodesics is the Cartesian product of the minimizing prefix-arm family and the minimizing suffix-arm family.

If \(S\) is antipodally invariant, then
\[
p_s(x,\bar v)=q_s(x,v),\qquad
q_s(x,\bar v)=p_s(x,v).
\]
The families through \(v\) and \(\bar v\) are internally vertex-disjoint: their only possible common vertices are \(x,\bar x\). Within one branch all two-switch witnesses encounter \(s\) in the same position among their retained switches; in the other branch that position is reversed.

*Proof.* Any prefix arm \(A\) and suffix arm \(B\) use complementary dimension sets. Their concatenation is therefore a full geodesic, with cost
\[
\sigma_S(A)+1+\sigma_S(B),
\]
since the joining turn is \(s\). The two minima can be attained independently, proving the lower bound and the criterion. If their sum is one, a two-switch concatenation must attain both minima, and every pair of minimizing arms gives such a concatenation.

Antipodal reversal converts a suffix through \(v\) to a prefix through \(\bar v\) from the same root, and conversely, proving the two identities. For disjointness, identify cube vertices with their flip sets from \(x\). A chain through \(v\) consists of sets comparable with \(D\); a chain through \(\bar v\) consists of sets comparable with \([n]\setminus D\). Since these two sets are disjoint and both nonempty, a set comparable with both is either empty or all of \([n]\). Thus the paths have no common internal vertex. Finally \((p_s,q_s)\) is either \((0,1)\) or \((1,0)\), determining whether \(s\) is the first or second retained turn; antipodal reversal swaps these types. \(\square\)

In particular, the two branches created by a fixed critical deletion do not need to be coupled through a common middle edge. The arm factorization instead describes how their roots and dimension sets can change.

##### Opposite arm types supplied by each critical cycle

**Theorem 23 (root transport along the intervening arc).** Let a projective Petrie cycle contain precisely the three retained turns \(s,a,b\). Choose a lift \(v\) of the center of \(s\), and orient a half-cycle from \(v\) to \(\bar v\). Its dimension order is
\[
(j,d_1,\ldots,d_{n-2},i).
\]
Let \(x\) and \(y\) be the centers of the lifted turns \(a,b\), in that order along this half-cycle. Then \(x,y\) lie in the same \((n-2)\)-face of root choices, fixing
\[
x_i=y_i=v_i,\qquad x_j=y_j=1-v_j.
\]
At the lift \(v\), their arm types are
\[
(p_s(x,v),q_s(x,v))=(0,1),\qquad
(p_s(y,v),q_s(y,v))=(1,0).
\]
Along the segment from \(x\) to \(y\) inherited from the half-cycle, every intermediate root \(z\) satisfies
\[
(p_s(z,v),q_s(z,v))
\in\{(0,1),(1,0),(1,1)\}.
\]
The connecting segment uses only the exterior dimensions \(d_1,\ldots,d_{n-2}\), each once, and has no retained internal turn.

*Proof.* The centers \(x,y\) occur after the first move \(j\) and before the last move \(i\), establishing the fixed root bits. Rotating the complete path to start at \(x\) omits the turn \(a\); its two retained turns are \(b\) and the lift of \(s\) at \(\bar v\), in that order. Antipodal reversal gives a path from the same root through \(v\) on which \(s\) is first. It therefore supplies a zero-cost prefix and a one-cost suffix. Theorem 22 proves that their minima are \((0,1)\). Rotating to \(y\) omits \(b\) and reverses the retained order, giving \((1,0)\) at \(v\).

At any root strictly between these two centers, the inherited rotated path encounters one retained turn on each side of the lift of \(s\). Antipodal reversal therefore supplies arms of cost one on each side of \(v\). The minima are each at most one, while Theorem 22 excludes \((0,0)\). Finally the segment between \(x,y\) contains neither \(s\) nor the endpoint turns \(a,b\) internally, so all its internal retained turn indicators are zero. \(\square\)

Thus every critical cycle supplies opposite arm types in one connected cube of eligible roots. The intermediate type \((1,1)\) accounts for loss of two-switch witnesses during transport; the inherited paths then have three retained switches.

##### A common connector produces a whole witness family

**Theorem 24 (zero-cost arms joined by a zero-cost connector).** Let \(x,y\) be eligible roots for the same lift \(v\), and suppose their flip sets from \(v\) satisfy
\[
D_x\subsetneq D_y,
\qquad
K=D_y\setminus D_x\subseteq[n]\setminus\{i,j\}.
\]
Let \(R:x\to y\) be a geodesic using \(K\) with no retained internal turn. Suppose \(p_s(x,v)=0\) and \(q_s(y,v)=0\).

For every zero-cost prefix \(A:x\to v\) ending in the incoming direction of \(s\), and every zero-cost suffix \(B:v\to\bar y\) starting in its outgoing direction, the concatenation
\[
P=A^{-1}\,R\,\bar B^{-1}
\]
is a full antipodal geodesic from \(v\) to \(\bar v\). It has precisely two retained turns, at the two ends of \(R\). Its projective cyclic completion has precisely those two retained turns and \(s\).

*Proof.* The three segments use, respectively,
\[
D_x,\qquad K,\qquad[n]\setminus D_y,
\]
which partition \([n]\). They concatenate at \(x,y\) and hence form a full geodesic. Antipodal invariance makes \(\bar B^{-1}\) zero-cost. All three segments have zero internal retained count; the only possible retained turns are their two joins. The global lower bound of two therefore forces both joining turns to belong to \(S\). The first direction of \(P\) is the incoming direction of \(s\), and its last is the outgoing direction, so its cyclic closing turn is \(s\). \(\square\)

Theorem 23 supplies the hypotheses of Theorem 24 for every critical three-turn cycle. The connector can be fixed while all zero-cost arms vary independently. When \(R\) has length one, the two forced turns occur at opposite ends of one cube edge.

##### A cographic bond lowers the completed variation

Write \(G=Q_n/A\) and \(H=L(G)\), where vertices of \(H\) are projective cube-edge orbits. For the fixed connector \(R\) from Theorem 24, let \(U\subseteq V(H)\) consist of its edge orbits, and put
\[
\mathcal B_R=\delta_H(U).
\]

**Theorem 25 (bond descent on the connector witness family).** Let \(1\le\ell=|E(R)|\le n-2\). Then \(\mathcal B_R\) is a bond of \(H\), hence a circuit of its cographic matroid, and
\[
\boxed{|\mathcal B_R|=2\ell(n-2)+2.}
\]
Let \(c\) be any antipodally odd coloring whose switch set contains \(S\). Flip the colors of all cube-edge orbits in \(U\), obtaining another antipodally odd coloring \(c'\). On every projective Petrie cycle \(C\) supplied by Theorem 24,
\[
\boxed{D_{c'}(C)=D_c(C)-2.}
\]
Thus one legal bond move decreases completed cyclic variation simultaneously throughout this Cartesian product of zero-cost arm choices.

*Proof.* The projective connector edge orbits induce a path with \(\ell\) vertices in \(H\): nonconsecutive connector edges cannot share an endpoint, and their lifts cannot meet antipodally because the connector has length less than \(n\). Hence \(H[U]\) is connected and has \(\ell-1\) edges.

To see that \(H[V(H)\setminus U]\) is connected, remove the \(\ell\) connector edges from \(G\). The folded cube contains a spanning \((n-1)\)-cube, obtained by choosing one representative with a fixed vertex bit and using the other \(n-1\) dimensions. A \(d\)-cube remains connected after deletion of fewer than \(d\) edges; its edge connectivity is \(d\), as follows by induction from its two \((d-1)\)-cube halves and their perfect matching. Since \(\ell\le n-2\), the spanning cube remains connected after the removals. Consequently \(G\setminus E(R)\) and its line graph are connected. Both shores of \(\delta_H(U)\) therefore induce connected graphs, making it a bond.

Every vertex of \(H\) has degree \(2(n-1)\). Subtracting twice the \(\ell-1\) internal edges of \(H[U]\) gives
\[
|\delta_H(U)|=2\ell(n-1)-2(\ell-1)=2\ell(n-2)+2.
\]

Flipping the orbit colors in \(U\) toggles precisely the comparisons in \(\delta_H(U)\), which is the legal cut-space move identified by the cographic switch-change theorem. On each cycle in the witness family, the connector is one contiguous block of edge observations. No observation in either arm belongs to \(U\), because its dimension is outside \(K\). The bond therefore meets this cycle in precisely its two connector-end turns. Both are retained and hence are switches of the containing coloring \(c\); the flip changes both from one to zero and leaves every other cyclic comparison unchanged. This proves the decrease by two. \(\square\)

If \(D_c(C)=3+2r\), the moved coloring has cyclic count \(1+2r\), and its best rotation has \(2r\) color changes. In particular, \(r=0\) gives a monochromatic full geodesic for the moved coloring. This is a legal variation-descent statement; a conclusion for the original coloring still requires controlling restoration of the connector colors or coupling this descent with another witness family.

The root-arm analysis therefore ties the hereditary criticality argument to the existing cographic matroid through a specified bond and a batch of complete geodesic witnesses. A single-cycle argument permits a \((1,1)\) transport region; the linked research note gives a realizable example. The global critical witness distribution remains the additional ingredient needed for a universal existence theorem.


#### Global sensitivity of a connector bond

The bond in Theorem 25 has controlled effects even on Petrie cycles outside its certified witness family. The control comes from dimension simplicity, rather than from the size of the bond.

**Theorem 26 (connector intersection rigidity and sharp run bound).** Let \(R\) be any cube geodesic of length \(1\le\ell\le n-2\), and let \(U\) be its projective edge observations. For a projective Petrie cycle \(C\), mark the edges of \(R\) whose orbits belong to \(C\). The resulting binary word has no occurrence of \(101\). Its runs of ones are precisely the connected portions of \(C\cap U\) in the observation cycle. Consequently, if \(r_R(C)\) denotes their number,
\[
\boxed{r_R(C)\le\left\lceil\frac{\ell}{3}\right\rceil.}
\]
The bound is attained for every permitted \(\ell\).

*Proof.* Suppose \(C\) contains the outer edges of three consecutive connector edges, in dimensions \(a,b,c\). Delete those outer edges from \(C\). The two remaining arcs use neither \(a\) nor \(c\). Their endpoints must therefore be paired so that their projective differences have representatives avoiding both dimensions. A cross pairing of an inner connector endpoint with the opposite outer endpoint has difference \(a+b\) or \(b+c\); its complement contains the other forbidden dimension. Such pairings are impossible. Hence the two inner endpoints are paired. Their difference is \(b\), whereas its complement contains both \(a,c\). Dimension simplicity forces their connecting arc to be the single \(b\)-edge. The middle connector edge therefore belongs to \(C\), excluding \(101\).

The induced graph \(H[U]\) is the connector observation path, as established in Theorem 25. Consecutive selected connector edges are consecutive observations of \(C\), since they meet at their common cube vertex. Conversely, observations from different runs cannot be adjacent in \(C\), since they are not adjacent in \(H[U]\). Thus the two run counts agree. Between runs there are at least two zero entries, so \(r\) runs require at least \(r+2(r-1)=3r-2\) entries. This proves the bound.

For sharpness take \(R\) to be the first \(\ell\) edges of the full geodesic with dimension order \(1,\ldots,n\). Put \(r=\lceil\ell/3\rceil\). Starting at the same root, interchange dimensions at positions \(2,3\), then \(5,6\), and so on through the first \(r-1\) such pairs. Each interchange replaces precisely those two cube edges and returns to the same vertex after the pair. The unchanged connector edges have \(r\) runs, separated by the replaced pairs; their projective orbits do not acquire additional coincidences. Indeed every observation retains its direction, and each replaced edge differs from the original edge of that direction in one other vertex bit, rather than in all \(n-1\) other vertex bits. The completed Petrie cycle attains the bound. \(\square\)

**Corollary 27 (global switch-grade sensitivity).** For an antipodally odd coloring define its Petrie grade by
\[
g_c(C)=\frac{D_c(C)-1}{2}.
\]
Flip the edge orbits of a connector \(R\), obtaining \(c'\). Let \(a_R(C)\) count the original switched comparisons in \(\delta_H(U)\cap C\). Then
\[
\boxed{g_{c'}(C)-g_c(C)=r_R(C)-a_R(C),\qquad
|g_{c'}(C)-g_c(C)|\le\left\lceil\frac{\ell}{3}\right\rceil.}
\]
In particular every connector of length at most three induces a legal move changing every Petrie grade by at most one. On the complete witness family of Theorem 24 the grade decreases by one.

*Proof.* Each observation run has two boundary comparisons, giving \(|\delta_H(U)\cap C|=2r_R(C)\). Toggling these comparisons changes \(D_c(C)\) by \(2r_R(C)-2a_R(C)\). Since \(0\le a_R(C)\le2r_R(C)\), Theorem 26 gives the bound. On a certified cycle there is one run and both boundary comparisons are switches. \(\square\)

**Corollary 28 (short connector choice at a critical cycle).** Every three-turn retained witness cycle has a connector bond which decreases its completed grade by one, together with its associated independent-arm witness family, and satisfies
\[
|g_{c'}(C')-g_c(C')|
\le
\left\lceil\frac{\lfloor n/3\rfloor}{3}\right\rceil
\]
for every Petrie cycle \(C'\).

*Proof.* The three edge distances between consecutive retained turn centers are positive integers summing to \(n\). Choose the shortest, of length \(\ell\le\lfloor n/3\rfloor\), as the connector. Use the third retained turn as \(s\) in Theorems 23–25. Corollary 27 supplies the global bound. \(\square\)

These bounds quantify the compensation required outside a descending witness family. They permit increases on other cycles, so a simultaneous descent principle remains to be proved.

#### Shared one-switch Fourier law for both complete-path problems

Fix \(m\ge2\), and write a binary color word as spins \(t_j=(-1)^{w_j}\). Let \(G_m(t)\) be the indicator that the word has at most one adjacent color change.

**Theorem (universal Fourier formula).**
\[
G_m(t)=2^{-m}\sum_{k=0}^{m-1}\left[
\prod_{j<k}(1-t_j)\prod_{j\ge k}(1+t_j)
+\prod_{j<k}(1+t_j)\prod_{j\ge k}(1-t_j)\right].
\tag{UF1}
\]
Its coefficient at the squarefree monomial \(\prod_{j\in S}t_j\) is zero for odd \(|S|\), and for even \(|S|\) equals
\[
\boxed{2^{1-m}\sum_{k=0}^{m-1}(-1)^{|S\cap\{0,\ldots,k-1\}|}.}
\tag{UF2}
\]
Consequently \(\deg G_m\le d_m=2\lfloor(m-1)/2\rfloor\).

*Proof.* The first summand at \(k=0\) lists the two constant words, and the summands indexed \(1\le k<m\) list the two complementary two-block words with a single switch at \(k\). Each listed word occurs once, and no other word occurs. This proves (UF1). In its multilinear expansion, each complementary pair cancels on odd-degree monomials. For even \(S\), the common monomial sign in the \(k\)-th pair is \((-1)^{|S\cap[0,k)|}\), proving (UF2). If \(m\) is odd, degree \(m\) vanishes by parity. For even \(m\), the degree-\(m\) coefficient is proportional to \(\sum_{k=0}^{m-1}(-1)^k=0\). The largest remaining possible degree is \(d_m\). \(\square\)

**Theorem (common restoration identity).** Let \(\Omega\) carry a free involution \(J\), and let legal colorings satisfy \(c(Jo)=1-c(o)\). Suppose every member \(P\) of a family \(\mathscr P\) reads \(m\) observations from distinct \(J\)-orbits. Put
\[
H(c)=\sum_{P\in\mathscr P}G_m((-1)^{w(P)_0},\ldots,(-1)^{w(P)_{m-1}}).
\]
As a function of one independent spin per observation orbit, \(H\) has Fourier degree at most \(d_m\). For any \(r>d_m\) distinct orbits \(q_1,\ldots,q_r\), and writing \(c^U\) for the legal coloring with orbits indexed by \(U\) flipped,
\[
\boxed{\sum_{U\subseteq[r]}(-1)^{r-|U|}H(c^U)=0.}
\tag{UF3}
\]

*Proof.* Distinct observation orbits on each path make (UF1) a multilinear polynomial in distinct global variables, up to fixed signs from the choice of lifts. The degree bound survives summation. Iterated Boolean finite differences in more than \(d_m\) variables annihilate every monomial, giving (UF3). \(\square\)

**NORI1 encoding.** Take \(\Omega=E(Q_n)\), \(J(e)=\bar e\), and all undirected antipodal geodesics, each reading \(m=n\) distinct direction orbits. Root sliding converts an at-most-one-switch word into a monochromatic geodesic. If \(F_n(c)\) counts monochromatic-zero unoriented antipodal geodesics, then
\[
\boxed{H_{Q_n}(c)=2nF_n(c).}
\tag{UF4}
\]
Indeed each projective Petrie cycle of twisted variation one has \(2n\) full geodesic windows, all with at most one switch, and one monochromatic-zero window. A cycle with higher odd variation has neither.

**Boundary-tournament encoding.** Take \(\Omega\) to be ordered triples of distinct vertices, \(J(abc)=cba\), and \(\mathscr P=S_n\), the Hamilton vertex orders. Their \(m=n-2\) consecutive triple windows have distinct middle vertices, preserved by reversal, so they lie in distinct \(J\)-orbits. Consequently
\[
\boxed{H_{\mathrm{BT},n}(c)=\sum_{\pi\in S_n}G_{n-2}(w(\pi)),\quad
\deg H_{\mathrm{BT},n}\le d_{n-2},}
\tag{UF5}
\]
and (UF3) governs its legal triple-pair recolorings. Both original existence problems are therefore nonvanishing assertions for the *same one-switch polynomial* on two path-incidence systems.

**Switch-bound distinction and closure scope.** The at-most-two-switch indicator need not share this degree drop: on four bits, its top Fourier coefficient is \(-1/8\), because its only excluded words are \(0101\) and \(1010\). This distinguishes the former higher-face two-switch objective algebraically. The common Fourier law remains an incidence-blind necessary structure; an unrestricted nonvanishing theorem requires further hypotheses linking overlapping paths, thereby excluding the higher-face obstructions.

##### Even-repair compensation at a zero of the path-count polynomial

**Corollary (cross-orbit compensation).** In the setting of the shared low-degree theorem, suppose \(H(c)=0\). Take any \(r>d_m\) distinct observation orbits \(R=\{q_1,\ldots,q_r\}\). Then
\[
\boxed{
\sum_{\substack{U\subseteq R\\|U|\ {\rm even}\\|U|\ge2}}H(c^U)
=
\sum_{\substack{U\subseteq R\\|U|\ {\rm odd}}}H(c^U)
\ge\sum_{q\in R}H(c^{\{q\}}).
}
\tag{UF7}
\]
Consequently if at least one singleton flip in \(R\) creates a favorable complete path, some even-cardinality collection of at least two flips in \(R\) also creates one. Moreover at least one such collection has path-count at least
\[
\frac{\sum_{q\in R}H(c^{\{q\}})}{2^{r-1}-1}.
\tag{UF8}
\]

*Proof.* Equation (UF3) states that the sum over even \(U\) equals the sum over odd \(U\), irrespective of the parity of \(r\). The empty even subset contributes \(H(c)=0\), and every other path count is nonnegative. The odd sum includes all singleton subsets, proving (UF7). There are \(2^{r-1}-1\) nonempty even subsets. Averaging gives (UF8). \(\square\)

For NORI1 one may select \(r=n-1\) distinct edge orbits when \(n\) is even, or \(r=n\) when \(n\) is odd; choosing distinct directions avoids automatic same-direction affinity. For boundary tournaments the same statement holds with \(r>d_{n-2}\) distinct ordered-triple reversal orbits. This gives a shared higher-order compensation mechanism among legal repairs. It does not prescribe which even subset heals, nor guarantee a two-pair repair: the cancellation may be distributed among larger subsets.

#### Quadratic Fourier overlap law for boundary 3-tournaments

Let \(n\ge5\), \(m=n-2\). An ordinary boundary 3-tournament colors ordered triples of distinct vertices, with \(c(c,b,a)=1-c(a,b,c)\). Choose a representative from each reversal pair of triples \(q\) and let \(s_q=(-1)^{c(q)}\). The number
\[
H_n(c)=\sum_{\pi\in S_n}\mathbf1\{\text{the }m\text{ consecutive triple colors along }\pi
\text{ have at most one switch}\}
\]
is a multilinear polynomial in these independent spins. Its Fourier degree is at most \(2\lfloor(m-1)/2\rfloor\).

Two reversal pairs \(q,r\) form a *four-chain* if they admit orientations \((a,b,c),(b,c,d)\) on four distinct original vertices. They form a *five-chain* if they admit orientations \((a,b,c),(c,d,e)\) on five distinct original vertices. Either chain comes with the signed product \(\varepsilon_{q,r}\) of the two orientation signs relative to the selected representatives. Simultaneous reversal of the entire chain negates both signs, so their product is well defined.

**Theorem (signed two-triple kernel).** The constant coefficient of \(H_n\) is \(n!m/2^{m-1}\), its odd Fourier degrees vanish, and the quadratic coefficient of two distinct reversal orbits is
\[
\boxed{
\widehat H_n(\{q,r\})=
\begin{cases}
\varepsilon_{q,r}\,2^{2-m}(m-1)(m-2)(n-4)!,&\text{four-chain},\\
\varepsilon_{q,r}\,2^{2-m}(m-2)(m-4)(n-5)!,&\text{five-chain},\\
0,&\text{all other pairs}.
\end{cases}}
\tag{BTK1}
\]
The two chain cases have different numbers of shared original vertices and are mutually exclusive. In particular, disjoint triple supports have zero quadratic coefficient.

*Proof.* The universal one-change word indicator has constant Fourier coefficient \(m/2^{m-1}\) and two-position coefficient
\(2^{1-m}(m-2(q-p))\) at positions \(p<q\). Sum these over the \(n!\) Hamilton vertex orders; odd degrees cancel under global color complementation.

Two triple windows in one Hamilton order overlap in two original vertices if their starting positions differ by one, in one endpoint if those positions differ by two, and in none if they differ by at least three. Hence two reversal orbits sharing two vertices can co-occur only if they form a four-chain. Each such chain has \(m-1\) possible starting positions and \((n-4)!\) orders of the remaining vertices. Its reversed chain has the same spin-product sign. The gap-one coefficient \(2^{1-m}(m-2)\) times this twofold count yields the first case.

Two orbits sharing a single original vertex can co-occur only when that vertex is an endpoint of both triples, giving a five-chain at position gap two. There are \(m-2\) starting positions, \((n-5)!\) residual permutations, and two reversed chain orientations with the same spin-product sign. The gap-two coefficient is \(2^{1-m}(m-4)\), giving the second case.

Two different reversal orbits supported on the same three vertices cannot both appear in a Hamilton order, since two distinct overlapping windows use at least four vertices. Incompatible one- or two-vertex overlaps likewise cannot co-occur. For disjoint triple supports, at every permitted pair of positions all four independently chosen triple orientations have equal multiplicity, and their spin-product signs sum to zero. This proves the remaining case. \(\square\)

**Corollary (six-vertex polynomial).** At \(n=6\) the word length is \(m=4\). The five-chain coefficient is zero and the polynomial has degree at most two. With \(t_{abc}=(-1)^{c(a,b,c)}=-t_{cba}\),
\[
\boxed{H_6(c)=360+\frac32\sum_{\substack{a,b,c,d\\\text{pairwise distinct}}}t_{abc}t_{bcd}.}
\tag{BTK2}
\]
Each four-chain pair appears in the ordered quadruple sum twice, via reversal. For \(n=5,6,7,8\), the unsigned four-chain coefficients are \(1,3,9,30\), respectively, and the five-chain coefficients are \(-1/2,0,3/4,3\), before their orientation signs. Independent exhaustive enumeration of Hamilton orders through eight vertices verifies these values and the zero cases.

**Interpretation.** This gives the boundary-tournament counterpart of the cube's factorial quadratic Fourier kernel. Both arise from the same one-change word polynomial. The cube kernel measures signed Hamming separation between direction-distinct edges; the boundary kernel records the four-vertex and five-vertex overlaps of ordered triple windows. The resulting support difference is a constraint on any shared positive-certificate strategy. Higher even Fourier degrees remain when the word length exceeds four.


#### Two usage-class completion and the missing interleaving clauses

The shared one-switch polynomial and the restoration fans have a Boolean counterpart retaining complete-path incidence. It gives a precise closure target and clarifies the role of Article XIV's local joining-square constraints.

**Theorem (two-class avoidance is 2-SAT).** Let complete paths read at most one observation orbit from each of two selected usage classes. Fix all other orbit colors, and let the selected colors vary freely, respecting the involution's coloring relation. For any specified success predicate on full color words, the legal completions avoiding successful complete paths are the solutions of a 2-CNF formula.

*Proof.* A given path depends on at most two adjustable Boolean variables. List its successful assignments, at most four. Forbid each such assignment with a clause asserting that at least one accessed variable differs. The clause has at most two Boolean tests. A successful path with no adjustable variables gives an empty clause; one adjustable variable gives a unary clause. Conjoining over complete paths is equivalent to avoidance. \(\square\)

**Cube specialization.** Select two distinct directions \(a,b\) of \(Q_n\), \(n\ge3\), and fix a legal antipodally odd coloring of all other directions. Give the antipodal edge orbits of direction \(a\) variables \(X_e\), and those of direction \(b\) variables \(Y_f\), choosing one lift of each as representative.

For a full geodesic, its \(n-2\) fixed observations must all have a common color \(t\) to permit a monochromatic completion. When they do, let its two adjustable colors be \(X_e+\epsilon_e\) and \(Y_f+\epsilon_f\), where the lift signs \(\epsilon_e,\epsilon_f\) are fixed. Its avoidance clause is
\[
\boxed{
(X_e\ne t+\epsilon_e)\ \lor\
(Y_f\ne t+\epsilon_f).
}
\tag{TC1}
\]
If the fixed observations have both colors, that path gives no clause. The resulting formula \(\Psi_{a,b}\) has only binary clauses between the two direction classes. A completion is a NORI1 counterexample precisely when it satisfies \(\Psi_{a,b}\).

Therefore NORI1 is equivalent to universal unsatisfiability of these formulas for every legal partial coloring. In implication-graph language this requires a signed variable and its negation to lie in one strongly connected component. The underlying variable classes alternate along every implication path.

**Boundary specialization.** Select two middle symbols \(a,b\) of an ordinary reversal-odd boundary tournament, and vary the reversal-orbit colors of triples centered at those symbols. A Hamilton ordering reads at most one triple from each selected class. Apply the theorem with the success predicate “at most one switch.” Its avoidance formula has clause width at most two; unary and empty clauses can occur because a selected symbol may be an endpoint of the ordering. Universal unsatisfiability is equivalent to the full boundary one-switch conjecture.

These are complete-incidence reductions. The usage-class property alone does not prove unsatisfiability: the geometry of the path-generated clauses remains essential.

##### What the two-polarity folding contributes

Let \(f\) be a hypothetical least-dimensional odd cube counterexample. For two omitted dimensions \(a,b\), the preceding dimension's NORI1 theorem gives paired roots in every arbitrary opposing face coloring, by the folding equivalence of Article XIV.

At a given corner \(u\), a face certificate of polarity \(t\) excludes a color-\(t\) monochromatic two-step route across its residual \(\{a,b\}\)-square. Thus every such route gives a clause forbidding \(tt\). A paired face root supplies both clauses, requiring the two route colors to differ.

This implies the following four-corner rule:
- A residual square of curvature one has no corner whose parallel complementary face is paired at that root.
- A flat gate permits paired face roots only at its two opposing gate corners. Its adjacent corners have monochromatic diagonal routes and therefore cannot be paired.
- A stripe has bichromatic diagonal routes at all four corners.
- A monochromatic residual square has no paired face root at any corner.

*Proof.* The face-certificate gluing is the two-polarity folding construction. Curvature one means the two diagonal routes from any corner have different color parities, so one is monochromatic. A gate's adjacent-corner diagonals are monochromatic; a stripe's diagonals are all bichromatic. \(\square\)

These clauses concern paths in which \(a,b\) are consecutive. They form only a subformula of \(\Psi_{a,b}\); interleaved placements generate additional clauses.

**Proposition (consecutive-direction avoidance can remain satisfiable in every dimension).** Fix \(n\ge3\), choose \(j\notin\{a,b\}\), and put
\[
\boxed{
c_a(x)=x_j,\qquad c_b(x)=1-x_j,\qquad
c_i(x)=x_a\quad(i\notin\{a,b\}).
}
\tag{TC2}
\]
This coloring is legal and antipodally odd. No monochromatic full geodesic has \(a,b\) consecutive. Nevertheless it has a monochromatic-zero full geodesic.

*Proof.* Without a \(j\)-step between \(a,b\), their colors are opposite, so a monochromatic path cannot traverse them consecutively. Start with \(x_a=1,x_j=0\) and traverse \(a,j,b\), followed by all remaining directions. The first edge is zero, flipping \(a\) makes every fixed-direction color zero, and the \(j\)-step changes \(x_j\) to one, making the \(b\)-edge zero. All remaining colors are zero. \(\square\)

Thus a contradiction obtained solely from residual-square gates cannot be universal. The missing clauses can already be supplied by a third interleaving direction. This agrees with Article XIV's need for full dimension-simple exchange geometry and higher coherence.

##### Four-clause inconsistent kernels

**Theorem (two robust orientation paths force a four-clause contradiction).** Fix a partial odd coloring with free directions \(a,b\). In the \(a=0\) facet, suppose a root \(z\) has one full path order of each monotone orientation which succeeds for either value of the color of its traversed \(b\)-edge. All other colors on those paths are fixed. Let \(Y_0,Y_1\) be the two adjustable \(b\)-edge colors read by these orders, and let \(X\) be the color of the \(a\)-bridge over \(z\), after choosing the representative sign accordingly.

Then the full completion formula contains the four clauses
\[
\boxed{
(X\lor Y_0),\quad(X\lor\neg Y_0),\quad
(\neg X\lor Y_1),\quad(\neg X\lor\neg Y_1).
}
\tag{TC3}
\]
They form an inconsistent kernel. Equivalently, they give implication paths
\[
\boxed{\neg X\longrightarrow Y_0\longrightarrow X,
\qquad X\longrightarrow Y_1\longrightarrow\neg X.}
\]

*Proof.* For \(t=0,1\), use the robust facet order of word \(t^*(1-t)^*\). For either value \(q=0,1\) of its \(b\)-edge, split the path at its monotone seam and apply the odd bridge gluing. If the bridge color is \(X=t\), the result is a monochromatic color-\(t\) full geodesic in the original cube. Its two adjustable observations are precisely \(X\) and \(Y_t\); when the \(b\)-step lies in the antipodally moved suffix, its lift sign changes, but its original variable requirement remains \(Y_t=q\).

Avoiding these two paths requires
\[
(X\ne t)\lor(Y_t\ne0),\qquad
(X\ne t)\lor(Y_t\ne1).
\]
For \(t=0,1\) these are the displayed four clauses. The first two force \(X=1\), and the second two force \(X=0\). \(\square\)

**Corollary (common-reader fixed directions force full completion inconsistency).** Fix \(a,b\), and suppose every other direction has color
\[
\boxed{c_i(x)=x_a+\eta_i,\qquad \eta_i\in\mathbb F_2.}
\tag{TC4}
\]
The free directions \(a,b\) may have arbitrary legal antipodally odd colors depending on all permitted bits. Every completion has a monochromatic full geodesic. More strongly, its completion formula has a four-clause inconsistent kernel for every lower-facet root.

*Proof.* On \(a=0\), all directions other than \(b\) have constant colors \(\eta_i\). From any root, traverse the zero-colored directions, then \(b\), then the one-colored directions. This order is nondecreasing for either color of the \(b\)-edge. The order taking the one-colored directions, then \(b\), then the zero-colored directions is nonincreasing for either color. Apply the theorem. \(\square\)

An alternative proof compresses the two offset groups into macro-directions within antipodally stable cosets, reducing to an odd cube of dimension at most four and expanding its monochromatic path. The four-clause proof identifies the contradictory implication kernel directly and uses no finite-dimensional existence input.

An independent completion check found zero full-avoidance solutions among all 16 legal compressed \(Q_3\) completions and all 256 legal compressed \(Q_4\) completions with these prescribed fixed directions. Their consecutive-direction relaxations had respectively two and four solutions. The all-dimensional proof is the four-clause construction.

**Assessment and next closure task.** Article XV now gives critical repairs, directional selector incompatibility, and full completion clauses. Article XIV provides faithful root/order geometry, paired-face gate clauses, curvature-strip constraints, and a sharp chain-tower obstruction calculus. The tower nonvanishing and universal contradictory implication cycle remain unproved.

The four-clause kernel shows how to close a completion formula through interleaving paths. Its robust fixed root is a sufficient certificate; it is unavailable in general, as the one-direction completion Subsection's adaptive-root example demonstrates. The next structural task is therefore to link clauses at different roots into the same pair of opposite implication paths, using criticality and the direction-changing incidence geometry. Local gates supply only part of the formula, and a high topological index cannot be inferred merely from their presence.

#### Critical repair intervals and terminal implication blocks

The preceding completion reduction lets us state the consequence of hereditary repair criticality without assuming that it already supplies an inconsistent implication cycle. The distinction between legal orbit recolorings and deletion of retained switches remains important.

Let \(c^0\) be a legal coloring and \(D\) a finite set of observation orbits. For \(S\subseteq D\), write \(c^S\) for the coloring obtained by flipping the orbits in \(S\). Assume
\[
c^D\text{ has no successful complete path},\qquad
c^S\text{ has one whenever }S\subsetneq D.
\tag{CR1}
\]
This is an inclusion-minimal bad interval based at \(c^0\). Such an interval can be selected from a hypothetical bad coloring and any good legal reference: minimize the bad subsets of their difference set.

Choose two usage classes and let \(V\subseteq D\) be the orbits in those classes. Keep all other orbits in their \(c^D\) state. Put \(p_u=1\) when orbit \(u\in V\) is kept in that state and \(p_u=0\) when it is repaired toward \(c^0\). The two-class avoidance formula \(\Phi_V\) has the unique satisfying assignment
\[
\boxed{p_u=1\quad(u\in V).}
\tag{CR2}
\]
Indeed every other assignment corresponds to a proper subset of \(D\). This statement uses only hereditary interval criticality and the two-usage property.

**Theorem (terminal-block characterization of criticality).** A 2-CNF formula satisfied by its all-one assignment has that assignment as its sole model if and only if the following condition holds.

After removing tautologies and repeated Boolean tests, its clauses have the forms
\[
p_u,\qquad p_u\lor p_v,\qquad p_u\lor\neg p_v.
\tag{CR3}
\]
Make a directed graph on the variables by placing an arc \(u\to v\) for every mixed clause \(p_u\lor\neg p_v\). Call \(u\) anchored if \(p_u\) is a unary clause, and mark the pair \(\{u,v\}\) for each positive clause \(p_u\lor p_v\). Then every sink strongly connected component contains an anchor or contains both ends of a marked pair.

*Proof.* A set \(T\) of variables changed to zero satisfies all mixed clauses precisely when it is closed under the directed arcs. It satisfies the remaining clauses precisely when it contains no anchor and contains no marked pair in full.

If a sink component has neither kind of obstruction, changing that component to zero gives another model. Conversely, every nonempty arc-closed set contains a sink component of the whole graph: follow outgoing arcs in the finite condensation graph, which remains inside the set. Under the stated condition that component contains an anchor or a marked pair, so the proposed zero set violates a clause. Hence no nonempty zero set is allowed. \(\square\)

**Corollary (one-sided implication certificates).** Under (CR1), every \(u\in V\) has an implication path
\[
\boxed{\neg p_u\longrightarrow p_u.}
\tag{CR4}
\]
A certificate can be chosen using at most \(2|V|-1\) clause implications.

*Proof.* Follow deletion arcs from \(u\) to a sink component. For a mixed clause \(p_i\lor\neg p_j\), the signed implication graph contains \(\neg p_i\to\neg p_j\) and \(p_j\to p_i\). If the sink has an anchor \(i\), choose a path from \(u\) to \(i\), use the unary implication \(\neg p_i\to p_i\), and reverse the path in positive signs.

Otherwise choose a marked pair \(\{i,j\}\) within the sink. There are directed paths from \(u\) to both \(i\) and \(j\). Use the first path in negative signs, the positive-clause implication \(\neg p_i\to p_j\), and the second path backwards in positive signs. Simple paths have at most \(|V|-1\) arcs each, giving the bound. \(\square\)

##### Full-geodesic meaning of the terminal blocks

For the cube, take success to mean a monochromatic full antipodal geodesic. The three clause types have direct witness meanings.

A unary anchor is a full geodesic that becomes monochromatic after repairing one orbit; its other selected-direction orbit is fixed outside \(V\). A mixed clause \(p_u\lor\neg p_v\) records a geodesic becoming monochromatic when \(u\) is repaired and \(v\) is retained. A positive clause \(p_u\lor p_v\) records a geodesic becoming monochromatic when both \(u,v\) are repaired. All its other observations already have the target color.

Thus a terminal component without anchors contains a two-repair witness and chains of one-repair witnesses returning between its repaired orbits. When \(V\) consists of two direction classes, every binary clause joins the classes and every deletion-arc path alternates between them. In particular an unanchored sink has at least two vertices and a directed alternating cycle.

The path supplying a mixed clause has one exceptional edge in the original coloring. In a NORI1 counterexample that edge must be internal: an endpoint exception gives an at-most-one-switch full word and hence a monochromatic root slide. The two-repair witness has two exceptional edges in the original coloring. Its existence does not prescribe their adjacency or the compatibility of its direction order with the one-repair witness orders.

For boundary tournaments, the same terminal-block theorem applies to the at-most-one-switch avoidance formula. Its witness meanings refer to repaired observations making the full word successful, rather than necessarily making it monochromatic.

##### Why a return block is not yet a contradiction

**Proposition (criticality and two-class incidence permit arbitrarily long consistent return blocks).** For any even \(r\ge2\), alternate variables \(p_0,\ldots,p_{r-1}\) between two classes and consider
\[
\boxed{
\bigwedge_{i=0}^{r-1}(p_i\lor\neg p_{i+1\bmod r})
\ \land\ (p_0\lor p_1).
}
\tag{CR5}
\]
All clauses join different classes. The formula has no anchors and its sole model is the all-one assignment.

*Proof.* The mixed clauses give one directed cycle. Their implication requirements force every variable to have the same value. The positive clause excludes the all-zero value. \(\square\)

Every nonempty deletion therefore restores a successful assignment pattern for some clause, and every variable participates in a one-deletion witness pattern. Nonetheless the original assignment satisfies the formula. This is an obstruction to a graph-only closure argument, not a claimed realization by cube geodesics or Hamilton orders.

In a consistent critical interval, (CR4) cannot be accompanied by \(p_u\to\neg p_u\): that would contradict its all-one model. Consequently criticality provides the first half of the desired inconsistent cycle, while complete-path geometry must force the other half.

**Revised closure task.** Select an unanchored terminal block, its internal two-repair path, and the alternating chains of one-repair paths. Use their full direction orders, antipodal lifts, and interleaving exchanges to produce a reverse signed implication or a monochromatic path before repair. Anchored blocks require coupling their one-repair paths to other roots instead. Article XIV's joining-square clauses constrain those exchanges but do not by themselves exclude (CR5); its higher chain obstruction also still requires a nonvanishing argument.

This reduction makes the needed coupling finite and dimension-independent in form. It proves neither universal inconsistency nor a switch-matroid exchange axiom. Independent enumeration checked the terminal-block criterion against all 4096 three-variable formulas assembled from the clause types (CR3); the proof above does not rely on that check.


##### Endpoint saturation removes a class of binary clauses

Antipodal root sliding gives a clause operation beyond the abstract terminal-block theorem.

**Lemma (endpoint sign saturation).** In the cube's full two-direction completion formula, suppose a clause comes from a full path whose free \(a\)-edge is its first or last edge. Write its mono-completion requirement as \(X=\alpha,\ Y=\beta\). Then the formula also contains the clause with requirement \(X=1-\alpha,\ Y=\beta\). These two clauses together impose the unary constraint \(Y\ne\beta\).

*Proof.* If the path starts with its \(a\)-edge, slide the root one step forward. The new full path removes that first edge and appends its antipodal mate. Its other \(n-1\) edges remain the same, in the same order, and the new \(a\)-edge has the complemented color. The fixed observations retain their common target color, and the \(b\)-edge retains its color. The representative variable for the \(a\)-orbit is unchanged while its required value is complemented. If the \(a\)-edge is last, use the reverse root slide.

The avoidance clauses are
\[
(X\ne\alpha)\lor(Y\ne\beta),\qquad
(X\ne1-\alpha)\lor(Y\ne\beta).
\]
Their conjunction is equivalent to \(Y\ne\beta\). \(\square\)

**Corollary (internal-edge completion core).** The full avoidance formula can be written as
\[
\boxed{\Psi_{a,b}\equiv U_{a,b}\land I_{a,b},}
\tag{CR6}
\]
where \(U_{a,b}\) is a conjunction of unary constraints generated by paths having at least one selected-direction edge at an endpoint, and \(I_{a,b}\) uses paths whose two selected-direction edges are both internal.

*Proof.* Pair each endpoint path with its root slide. Every resulting unary constraint is entailed by the endpoint-path formula, and every endpoint clause is entailed by the corresponding unary constraint. Paths with mixed fixed observations give no clause on either side. Retain all remaining clauses. \(\square\)

If the endpoint constraints force opposite values of one variable, completion closes immediately. Otherwise propagate them through the internal clauses. A surviving unanchored terminal block in a critical repair interval is then generated by internal/internal witnesses. Its two-repair witness and alternating one-repair chains must be coupled in that interior geometry.

This is stronger than observing that a critical defect cannot sit at an endpoint: it removes every clause having either free observation at an endpoint. For \(n=3\) there is no internal/internal path, so the full formula is equivalent to unary constraints alone. For \(n\ge4\), interior interleavings remain. Article XIV's face-gate information constrains consecutive internal placements, while (TC2) continues to show why the full interleaving system must be retained.


##### A five-clause closure through two different readers

The endpoint reduction yields a second bounded certificate, without the common-reader hypothesis (TC4).

**Theorem (two uniform reader groups admit arbitrary nonlinear hubs).** Partition the remaining directions into nonempty sets \(J,K\), and prescribe
\[
\boxed{
c_j(x)=1-x_a\quad(j\in J),\qquad
c_k(x)=1-x_b\quad(k\in K).
}
\tag{CR7}
\]
Allow arbitrary legal antipodally odd colors in directions \(a,b\). Every completion has a monochromatic full geodesic. Its full completion formula has an inconsistent kernel of at most five clauses.

*Proof.* Fix any direction-\(a\) edge and let \(B\) be its \(b\)-bit. Construct a full path of order
\[
J,\ a,\ K,\ b
\]
passing through that prescribed edge. Choose its initial \(a\)-bit to be \(B\); choose all other initial bits so that the prescribed edge is read after the \(J\)-steps. Every \(J\)-edge then has color \(1-B\), and every \(K\)-edge has color \(1-B\), since \(b\) has not yet been traversed. The \(b\)-edge is last. Endpoint sign saturation forces the prescribed \(a\)-edge to avoid color \(1-B\). Thus every completion avoiding monochromatic full paths must satisfy
\[
c_a(x)=x_b.
\]
The symmetric construction with order \(K,b,J,a\), and initial \(b\)-bit equal to the prescribed \(b\)-edge's \(a\)-bit, forces
\[
c_b(x)=x_a.
\]

These forced colors already give a monochromatic-zero full path. Start with \(x_a=1,x_b=0\), traverse \(J,a,b,K\), and use any orders within the two groups. Before \(a\), the \(J\)-colors are zero; the \(a\)-color is \(x_b=0\); crossing \(a\) makes the \(b\)-color \(x_a=0\); crossing \(b\) makes all \(K\)-colors zero.

To obtain the bounded kernel, retain this internal path's clause and the two endpoint path pairs forcing its \(a\)- and \(b\)-observations. With representative signs chosen so those observations are \(X,Y\), the five clauses have the form
\[
\boxed{
(\neg X\lor Z),\quad(\neg X\lor\neg Z),\quad
(\neg Y\lor W),\quad(\neg Y\lor\neg W),\quad
(X\lor Y).
}
\tag{CR8}
\]
The first two force \(X=0\), the next two force \(Y=0\), and the last excludes that assignment. Variable coincidences can only shorten the certificate. \(\square\)

**Proposition (the endpoint relaxation can be consistent in every dimension \(n\ge4\)).** In (CR7), set
\[
c_a(x)=x_b,\qquad c_b(x)=x_a.
\tag{CR9}
\]
Every monochromatic full geodesic has one of the orders
\[
\boxed{J,a,b,K\qquad\text{or}\qquad K,b,a,J,}
\tag{CR10}
\]
with arbitrary orders within the groups. Hence both selected directions are internal, and the endpoint-only formula is satisfied by (CR9).

*Proof.* Suppose a monochromatic path of color \(t\) traverses \(a\) before \(b\). Its \(a\)-color forces the initial \(b\)-bit to be \(t\); its later \(b\)-color forces the initial \(a\)-bit to be \(1-t\). A \(J\)-edge has color \(t\) only before \(a\), and a \(K\)-edge has color \(t\) only after \(b\). This gives the first order. The opposite relative order gives the second. Since \(J,K\) are nonempty, neither selected direction is an endpoint. \(\square\)

This provides a dimension-uniform model of the closure step: endpoint paths at different roots force colors, and a full internal path couples those forces. The four-clause common-reader certificate and the five-clause two-reader certificate therefore realize two distinct ways to contradict the completion formula. Arbitrary fixed colorings need not admit either certificate; their remaining internal implication blocks still require a general coupling theorem.


#### Bridge-variable resolution couples the two implication reductions

The one-direction paired-root formula and the two-direction odd-cube formula are linked by eliminating a complete class of bridge variables. This supplies a dimension-uniform correspondence between their implication certificates.

Fix arbitrary colors on all directions of \(Q_d\) except direction \(i\), whose edge colors are variables \(X\). Write \(f_X\) for this ordinary facet coloring. Form its odd bridge extension on \(Q_{d+1}\): the lower facet has \(f_X\), the upper facet has edge color \(1-f_X(\bar e)\), and the joining edge above \(u\) has color \(h(u)\), with \(h(\bar u)=1-h(u)\). Choose one representative \(u\) from each antipodal root pair and write \(Y_u=h(u)\).

For a full nondecreasing facet path \(P\) starting at \(u\), let \(L_P(X)\) be its success predicate. Since it uses one direction-\(i\) edge, this predicate is false, true, or a one-variable Boolean test. Put
\[
A_u(X)=\bigvee_{P\text{ full nondecreasing from }u}L_P(X).
\]

**Lemma (bridge-port identity).** A monochromatic full path crosses the bridge above \(u\) precisely when the facet admits a full path from \(u\) of orientation \(h(u)^*(1-h(u))^*\).

*Proof.* For a facet path of that orientation, split at its monotone seam. Reverse the initial segment, traverse the bridge at \(u\), and use the antipodally translated reversed final segment in the upper facet. Its edges all have the bridge's color and its endpoints are antipodal.

Conversely, cut a monochromatic full path at its unique bridge. Reversing its lower horizontal segment and then applying antipodal translation and reversal to its upper segment produces a full facet path from the bridge root. The first segment has color \(h(u)\), the second color \(1-h(u)\). Paths starting in the upper facet give the same conclusion after reversal. \(\square\)

Reversal of an ordinary full facet path exchanges nondecreasing paths from \(\bar u\) with nonincreasing paths from \(u\). Thus the odd completion formula has the equivalent root-pair factorization
\[
\boxed{
\Psi(X,Y)=
\bigwedge_{[u]}
\left[(Y_u\lor\neg A_u(X))
\land(\neg Y_u\lor\neg A_{\bar u}(X))\right].
}
\tag{BR1}
\]
Expanding each \(\neg A\) produces the full two-class clauses associated with the corresponding complete paths.

**Theorem (bridge elimination is paired-root avoidance).** Eliminating all bridge variables gives
\[
\boxed{
\exists Y\,\Psi(X,Y)
\ \Longleftrightarrow\
\bigwedge_{[u]}(\neg A_u(X)\lor\neg A_{\bar u}(X))
\ \Longleftrightarrow\
P(f_X)=\varnothing.
}
\tag{BR2}
\]
After expansion, the middle formula is the one-direction paired-root 2-CNF.

*Proof.* For one root pair, some \(Y_u\) satisfies its two factors if and only if \(A_u,A_{\bar u}\) are not both true. The bridge variables for different root pairs are independent. Both predicates true mean that the same root has opposite monotone witnesses, by reversal. Expanding the middle factor over every pair of successful-path predicates gives
\[
\neg L_P(X)\lor\neg L_Q(X),
\]
where \(P\) starts at \(u\) and \(Q\) starts at \(\bar u\), both nondecreasing. Reverse \(Q\) to recover the ordinary paired-root clause at \(u\). \(\square\)

**Corollary (two-step lifting of every resolved implication).** Suppose a paired-root clause comes from success predicates \(L_P,L_Q\) at the antipodal roots \(u,\bar u\). Its two bridge clauses are
\[
(Y_u\lor\neg L_P),\qquad
(\neg Y_u\lor\neg L_Q).
\]
The resolved implication \(L_P\to\neg L_Q\) lifts to
\[
\boxed{L_P\longrightarrow Y_u\longrightarrow\neg L_Q,}
\tag{BR3}
\]
and the reverse implication lifts through \(\neg Y_u\). Consequently a contradictory implication cycle in the facet formula gives one in the odd-cube formula with at most twice as many steps. Constant success predicates give the corresponding unary or empty clauses.

This correspondence permits the root pair to change at every resolved implication. It therefore requires neither a universally robust root nor a shared direction order across the certificate. In a critical repair interval, the bounded one-sided forcing paths already obtained can be interpreted as chains of paired-root witness clauses and lifted through their individual bridge ports. The missing reverse forcing path remains a geometric obligation.

**Assessment alongside the current updates.** The tree interfaces allow two orders at a shared root; the cyclic overlap results sometimes construct one order for both colorings. Bridge resolution retains the more general two-order structure. The affine twin reduction and rank-three verification close their stated matrix class, while the general paired-root implication formula remains unresolved. The current proof target is a contradictory resolved chain in that formula, using antipodal reversal and full-order exchange to couple different root pairs.

Independent direct enumeration checked the bridge-port identity for 36 unrelated ordinary facet colorings and odd extensions in facet dimensions three and four. The proof and the Boolean elimination above apply in every dimension.


#### Non-reader support thresholds from rooted-tree and two-hub closure

The current proof tools imply a stronger necessary condition on an arbitrary NORI1 counterexample than the one-unrestricted-direction theorem alone gives. This is a support reduction valid for unrestricted dependency graphs and arbitrarily large cube dimension.

Call a direction of an ordinary cube coloring a partial-reader direction when its edge-color function is constant or is \(a_i+x_{r(i)}\), \(r(i)\ne i\). A legal odd coloring has no constant direction, so its reader directions are precisely the signed one-bit readers.

**Lemma (one unrestricted ordinary direction).** Let \(f\) color the edges of \(Q_d\). Suppose all but at most one direction are partial readers. If \(k\) is the number of its nontrivial dependency strongly connected components, then
\[
\boxed{|P(f)|\ge2^{d-k}\ge2^{\lceil d/2\rceil}.}
\tag{NS1}
\]

*Proof.* Every partial-reader direction has dependency indegree at most one. Thus every nontrivial strongly connected component has at most one internal branching target. The unique-predecessor graph lemma identifies each such component as a directed cycle or an outward rooted tree with feedback into its root. The rooted-tree feedback theorem makes every fixed-outer fiber at least three quarters favorable. Paired-root fiber gluing contributes a factor \(2^{s-1}\) when a component has \(s\ge2\) directions, and a factor two for a singleton. Multiply over the condensation graph to obtain \(2^{d-k}\). Nontrivial components have at least two vertices, so \(k\le\lfloor d/2\rfloor\). \(\square\)

**Lemma (two unrestricted ordinary directions; computer-assisted).** If all but at most two directions of \(f\) are partial readers, then \(P(f)\ne\varnothing\).

*Proof.* Every component has at most two internal branching targets. Components with at most one are removed using (NS1)'s fiber argument. For a terminal component with two branching targets, the unique-predecessor forest compression reduces each fixed-outer fiber to a two-hub star. Its hub functions may be arbitrary. The published two-hub finite certificate proves that every fiber is at least nine sixteenths favorable. Two such favorable sets intersect after antipodal complementation in at least \(2^{s-3}\) roots. The sink-component gluing lemma therefore removes that component as well. Induct over the condensation graph.

This uses the computer-assisted two-hub majority theorem. The paired-root bound used in the argument is valid; its numerical sharpness is not needed. \(\square\)

**Theorem (two unrestricted odd directions; analytic).** A legal antipodally odd coloring of \(Q_n\), \(n\ge2\), has a monochromatic full antipodal geodesic whenever all but at most two directions are signed one-bit readers. Moreover,
\[
\boxed{F_n(c)\ge2^{\lceil(n-1)/2\rceil-1},}
\tag{NS2}
\]
where \(F_n\) counts unoriented monochromatic-zero full geodesics.

*Proof.* Choose an unrestricted direction \(h\), or any direction if all are readers, and restrict to its lower facet. A reader pointing to \(h\) becomes constant. All other reader directions remain partial readers, and the facet has at most one unrestricted direction. Apply (NS1). The odd bridge-splice theorem gives a monochromatic-zero full path from each antipodal pair of paired facet roots, choosing the unique zero bridge in that pair. Different pairs give different crossing edges. Hence \(F_n(c)\ge|P(f)|/2\), proving (NS2). \(\square\)

**Theorem (three unrestricted odd directions; computer-assisted).** A legal odd coloring with all but at most three directions signed one-bit readers has a monochromatic full antipodal geodesic.

*Proof.* Restrict along one unrestricted direction. Its ordinary facet has at most two unrestricted directions, and the preceding two-target lemma gives paired roots. Apply the free-bridge equivalence. The only computer-assisted input is the existing sharp favorable-root theorem for two-hub stars. \(\square\)

##### Consequences for the critical implication search

Let \(s_i(x)=(-1)^{c_i(x)}\) be the direction spin, regarded as an odd Boolean function on the other \(n-1\) bits. Define
\[
E(c)=\left\{i:\sum_{|T|\ge3}\widehat s_i(T)^2>0\right\}.
\]
Oddness removes even Walsh degrees. A Boolean function supported only on singleton Walsh characters is a signed single character, since the degree-two coefficients of its square force all but one linear coefficient to vanish. Thus \(E(c)\) is precisely the set of non-reader directions.

**Corollary (four-direction obstruction threshold).** Every hypothetical NORI1 counterexample satisfies
\[
\boxed{|E(c)|\ge4.}
\tag{NS3}
\]
The threshold three is analytic; excluding three non-reader directions uses the two-hub finite certificate.

Equivalently, arbitrary legal recolorings confined to any three direction classes of any one-reader odd coloring preserve a monochromatic full geodesic. The number of recolored antipodal edge orbits within those classes is unrestricted. A critical bad interval based at a reader coloring must therefore use at least four direction classes.

In the full two-direction formula \(\Psi_{a,b}\), a signed-reader background forces universal inconsistency analytically. A background with at most one additional non-reader direction forces universal inconsistency through the computer-assisted theorem. Any satisfiable two-direction completion formula must consequently have at least two non-reader directions among its fixed observations.

These conclusions strengthen the earlier four- and five-clause families: the controlling reader graph can be arbitrary, with many cycles, incoming trees, and readers pointing to either selected direction. A robust fixed root and a constant-size inconsistent kernel are not assumed.

##### Updated path toward closure

The general formula remains unsolved. The proved elimination rules remove singleton, cyclic, rooted-tree, and two-target terminal components. A least-dimensional paired-root obstruction therefore contains a terminal component with at least three internal branching targets. The remaining task is a cross-fiber intersection certificate for such a component, compatible with two different hub tables at the outside seam vertices.

A strict favorable-root majority cannot be the universal certificate: a product of three sharp three-dimensional stars has favorable fraction \((3/4)^3=27/64\) and nevertheless has paired roots. The safe-check and crossed-factor theorems already provide intersections below the majority threshold when suitable root constraints are present. The next closure attempt should extract analogous compatible root constraints from the critical repair witnesses in the three-target component, then use bridge resolution to assemble the resulting root-changing implications.

This is the current proof plan: retain the hereditary repair interval, localize its unresolved implications to a multi-target terminal fiber, and couple its witness orders through root constraints that survive a change of fiber. The new support threshold records how much feedback such an obstruction must contain before that step is needed.


**Independent support-threshold check.** A separate subset-reachability evaluator verified (NS1) for 80 partial-reader colorings with one arbitrary direction in dimensions three through six, including constant directions and multiple dependency components. It computed the dependency components from essential inputs and checked the bound (2^{d-k}) against directly obtained paired-root sets. The support-threshold theorems rest on the analytic component arguments and the stated two-hub certificate, rather than on this sample.


#### Dimension induction with boundary parity and interior seams

A dimension induction on paired roots must retain where the deleted direction can be inserted. The lower-dimensional existence statement by itself supplies no control of that insertion port. The following general endpoint criterion identifies one part of the induction that does close.

Let \(f\) be an ordinary edge coloring of \(Q_{d+1}\), split across direction \(h\). Denote its facet colorings by \(g_0,g_1\), and write \(H(y)\) for the edge color in direction \(h\) above the remaining-bit root \(y\). The function \(H\) is arbitrary. Set
\[
C=A_0(g_1)\cap A_1(g_0).
\]

**Theorem (even boundary pair closes an inductive step).** If \(y\in C\) and
\[
\boxed{H(y)=H(\bar y),}
\tag{DI1}
\]
then \(f\) has a paired root. Both witnesses can put direction \(h\) at an endpoint.

*Proof.* If both values are zero, start at \((y,0)\). For the nondecreasing path, cross the zero \(h\)-edge first and then use the \(g_1\) nondecreasing path from \(y\). For the nonincreasing path, use the \(g_0\) nonincreasing path and then cross the zero \(h\)-edge at its endpoint \(\bar y\). The two full words are monotone.

If both values are one, reversal gives \(\bar y\in A_0(g_0)\cap A_1(g_1)\). Start at \((\bar y,0)\). Use the \(g_0\) nondecreasing path followed by its terminal one-colored \(h\)-edge, and the initial one-colored \(h\)-edge followed by the \(g_1\) nonincreasing path. \(\square\)

**Corollary (boundary oddness on cross-favorable roots).** In any paired-root-free ordinary coloring,
\[
\boxed{y\in C\Longrightarrow H(y)\ne H(\bar y).}
\tag{DI2}
\]
Thus an attempted endpoint induction leaves a specified odd boundary profile over its cross-root set.

**Example (interior insertion is necessary even with complete facet profiles).** Take three directions \(a,b,h\) with
\[
f_a=0,\qquad f_b=1,\qquad f_h=x_a.
\tag{DI3}
\]
Both \(h\)-facets have every root paired, and \(C\) is their whole root set. Their horizontal full paths have no monochromatic word. The joining values \(H(y),H(\bar y)\) are opposite.

No root has both orientations witnessed with \(h\) at an endpoint. For a root with initial \(x_a=0\), an endpoint-\(h\) path cannot be nonincreasing: \(h\) first has color zero before the required one-colored \(b\)-edge, and \(h\) last has color one after the required zero-colored \(a\)-edge. With initial \(x_a=1\), the nondecreasing endpoint case fails for the reversed reasons.

Every root of the full cube is nevertheless paired. The orders \(a,h,b\) and \(b,h,a\) produce opposite monotone words from every root. Thus the lifting construction needs an interior seam even when the two smaller paired-root profiles are complete.

##### Structural return from the induction attempt

The new adjacent-face result in Article XIV makes the residual boundary condition much stronger in an odd cube. For omitted directions \(a,b\), let \(g_{\alpha\beta}\) be the codimension-two face colorings. If a root belongs to
\[
A_0(g_{01})\cap A_1(g_{00})
\]
or its reverse-orientation counterpart, the residual joining square must be a stripe in a bad coloring. Both transverse direction derivatives vanish there and the two incident direction colors differ.

At a gate, an adjacent face root supports neither orientation. In particular every vertex of Article XIV's monochromatic face corridor becomes a completely empty root in each neighboring translated face. The rooted-tree rootwise coverage theorem therefore constrains those neighboring fibers at the prescribed corridor vertices, rather than only supplying paired roots somewhere else.

The induction has consequently reached a usable obstruction: cross-root ports carry stripe constraints; gate ports force empty adjacent profiles. Critical repair witnesses can be tested against both conditions. A closing exchange must carry a witness through an interior seam, preserve its direction set, and either create a nonstripe cross-root port or assemble opposite implication paths through several bridge ports.

The local cross-interface graph of Article XIV records the first possibility: an odd cycle among its direction pairs produces a monochromatic full path. Full two-direction completion retains the interleaving clauses needed for the second. Neither universal odd-cycle production nor universal opposite-path coupling has been proved.

**Current strategy.** Continue the hereditary repair induction using full direction orders and seam positions. Whenever a proposed witness transport crosses a gate, apply the empty-root rule to the neighboring face; whenever it creates opposite face polarities, apply the stripe rule. The earlier endpoint transport obstruction shows why these positions must remain in the inductive state. This returns the closure search to structural analysis at the first point where the smaller certificates fail to align.


#### Sharp antiperiodic first-harmonic criterion for NORI1

Inspired by Mykkeltveit's de Bruijn cycle-transversal theorem (Toolkit id \`literature_mykkeltveit_de_bruijn_fourier_cycle_transversal\`), we use a complex first Fourier harmonic, distinct from the Boolean Fourier polynomial (UF1)--(UF3).

Write \(\zeta=e^{\pi i/n}\), \(s_j=(-1)^{w_j}\), and
\[
F_n(w)=\sum_{j=0}^{n-1}s_j\zeta^j,\qquad M_n=\csc(\pi/(2n)).
\tag{AF1}
\]
Here \(n\ge2\). The antiperiodic extension \(s_{j+n}=-s_j\) has first length-\(2n\) Fourier coefficient \(2F_n(w)\).

**Theorem (sharp Fourier inequality).**
\[
\boxed{|F_n(w)|\le M_n,}
\tag{AF2}
\]
with equality iff \(w\) has at most one adjacent color change.

*Proof.* The antiperiodic shift \(T(s_0,\ldots,s_{n-1})=(s_1,\ldots,s_{n-1},-s_0)\) satisfies \(F_n(Ts)=\zeta^{-1}F_n(s)\). Iterating \(T\) sends each zero- or one-change word to a constant word, and
\[
\left|\sum_{j=0}^{n-1}\zeta^j\right|=2/|1-\zeta|=M_n.
\]
For arbitrary \(s,\theta\),
\[
\operatorname{Re}(e^{-i\theta}F_n(s))
=\sum_j s_j\cos(j\pi/n-\theta)
\le\sum_j|\cos(j\pi/n-\theta)|. \tag{AF3}
\]
The sampled angles span less than a semicircle, so signs of the cosines change at most once. Choosing either sign at a zero sample produces a zero- or one-change word \(u\), and the right-hand side is
\(\operatorname{Re}(e^{-i\theta}F_n(u))\le |F_n(u)|=M_n\). Optimizing over \(\theta\) proves (AF2). Under equality, \(s\) agrees with the signs of the cosines on every nonzero sample; at most one sample vanishes, and either sign there leaves at most one change. \(\square\)

**Theorem (sharp harmonic attainment is NORI1).** Let \(c\) be an antipodally odd coloring of the undirected edges of \(Q_n\). For a vertex \(x\) and direction permutation \(\pi\), denote the color word of the complete geodesic by \(w(x,\pi)\). Then
\[
\boxed{\text{a monochromatic antipodal geodesic exists}
\quad\Longleftrightarrow\quad
\max_{x,\pi}|F_n(w(x,\pi))|=M_n.}\tag{AF4}
\]

*Proof.* The root slide
\(\mathcal T(x,\pi)=(x+e_{\pi_1},(\pi_2,\ldots,\pi_n,\pi_1))\)
acts on the color word by
\[
w(\mathcal T(x,\pi))=(w_1,\ldots,w_{n-1},1-w_0), \tag{AF5}
\]
using the antipodal-odd color of the moved edge. This is precisely \(T\) on the spins and preserves \(|F_n|\). If \(w\) has a single change after position \(k\), then \(k\) root slides produce a constant word: the old final block is followed by the complement of the old first block. The converse is immediate, and (AF2) supplies the equivalence. \(\square\)

**Corollary (Fourier phase section).** Each rooted-geodesic root-slide orbit has \(2n\) states: \(\mathcal T^n(x,\pi)=(\bar x,\pi)\), and \(\mathcal T^{2n}(x,\pi)=(x,\pi)\). If \(F_n(w(x,\pi))\ne0\), there is a unique state in its orbit such that
\[
\operatorname{Im}F_n(w(x,\pi))\le0<
\operatorname{Im}\bigl(\zeta^{-1}F_n(w(x,\pi))\bigr). \tag{AF6}
\]
The \(2n\) complex phases form a regular \(2n\)-gon, and one step crosses from the closed lower half-plane to the open upper half-plane. For zero-harmonic orbits choose a representative by a fixed total order. The resulting canonical set has
\[
\boxed{2^{n-1}(n-1)!} \tag{AF7}
\]
rooted paths, and the maximum in (AF4) is unchanged when restricted to that set.

**Scope and obstruction to a direct de Bruijn transfer.** The section (AF6) intersects all root-slide orbits; it is not known to meet every directed cycle in the larger adjacent-exchange graph. The de Bruijn argument depends on every nonrotation transition adding a real scalar to its Fourier mode. For a cube path, swapping adjacent directions at positions \(j,j+1\) changes the harmonic by
\[
\Delta F_n=\zeta^j\bigl((s'_j-s_j)+\zeta(s'_{j+1}-s_{j+1})\bigr). \tag{AF8}
\]
The change need not lie on a common real line. A closure theorem would therefore need a new color-sensitive exchange constraint or a proof that the sharp maximum (AF2) is forced by the available paths; neither follows from the phase section.


#### Rank-two quadratic objective common to NORI1 and boundary tight paths

For a legal length-\(m\) complete path \(P\) with color spins \(s_0(P),\ldots,s_{m-1}(P)\), define
\[
Q_m(P)=\left|\sum_{j=0}^{m-1}s_j(P)e^{\pi i j/m}\right|^2
=m+2\sum_{0\le i<j<m}\cos\!\left(\frac{\pi(j-i)}m\right)s_i(P)s_j(P).
\tag{QF1}
\]
The Gram matrix is \(C_{ij}=\cos(\pi(i-j)/m)=\cos(\pi i/m)\cos(\pi j/m)+\sin(\pi i/m)\sin(\pi j/m)\), hence positive semidefinite of rank two for \(m\ge2\).

**Corollary (common quadratic witness).** Every binary color word satisfies
\[
Q_m(P)\le\csc^2(\pi/(2m)),
\tag{QF2}
\]
with equality if and only if the word has at most one change. This follows from the antiperiodic first-harmonic theorem (AF2).

For NORI1 on \(Q_n\), with \(m=n\), existence of a monochromatic full geodesic is equivalent to a legal rooted full path attaining (QF2), because a one-change extremizer root-slides to a monochromatic path. For ordinary boundary tournaments, when the goal is a full tight path with at most one binary color change, existence of the desired path is likewise equivalent to attainment of (QF2) by one of its legal tight paths. The two applications share the same extremal objective but have different legal path systems and exchange constraints.

The objective (QF1) has degree two in the observed color spins. The *indicator* of attaining its maximum remains higher degree in general, as in the preexisting Boolean Fourier formula (UF1)--(UF3). Thus (QF1) is a low-rank numerical reformulation, not a degree-two expression for the one-change indicator. A common proof still needs structural information forcing extremal attainment in both classes.


#### Sharp second-best harmonic energy and spin-flip ascent

Retain \(F_m(s)=\sum_{j=0}^{m-1}s_j e^{\pi i j/m}\), \(Q_m(s)=|F_m(s)|^2\), \(M_m=\csc(\pi/(2m))\).

**Lemma (unrestricted strict ascent).** For \(m\ge3\), if a spin word \(s\) has two or more adjacent changes, a single spin flip strictly raises \(Q_m\).

*Proof.* If \(F_m(s)=0\), flipping any spin increases \(Q_m\) from zero to four. Otherwise choose \(\theta=\arg F_m(s)\). On the sampled semicircle, signs of \(\cos(j\pi/m-\theta)\) change at most once. Since \(s\) has at least two changes, there is a \(j\) with \(s_j\cos(j\pi/m-\theta)<0\). Flipping spin \(j\) changes the Fourier vector by \(-2s_je^{\pi i j/m}\); consequently
\[
Q_m(s^{(j)})-Q_m(s)
=4-4|F_m(s)|s_j\cos(j\pi/m-\theta)>4. \tag{SG1}
\]
\(\square\)

**Theorem (sharp spectral gap).** For \(m\ge3\), if a word has two or more adjacent changes, then
\[
\boxed{
Q_m(s)\le \csc^2(\pi/(2m))-8\cos(\pi/m).
} \tag{SG2}
\]
Equality is attained by \(s=(+,-,+,\ldots,+)\) and its antiperiodic rotations.

*Proof.* Maximize \(Q_m\) over the finite set of words with at least two changes. The strict-ascent lemma supplies a one-spin flip that increases \(Q_m\); by the selected word's maximality among nonextremizers, that flip must yield a zero- or one-change word. Antiperiodic rotation and spin negation preserve the energy and move any zero- or one-change word to the all-plus word. Thus we need examine a word obtained from all-plus by changing one spin in an interior position \(1\le j\le m-2\).

Put \(a=\pi/(2m)\) and \(\zeta=e^{2ia}\). Since \(\sum_{t=0}^{m-1}\zeta^t=M_m e^{i(m-1)a}\),
\[
Q_m(s)=\left|\sum_{t=0}^{m-1}\zeta^t-2\zeta^j\right|^2
=M_m^2+4-4M_m\cos((2j-m+1)a).
\]
The right side is largest at \(j=1\) or \(m-2\), with cosine \(\sin(3a)\). Using \(M_m\sin a=1\) and \(\sin(3a)=3\sin a-4\sin^3 a\),
\[
Q_m(s)\le M_m^2+4-4M_m\sin(3a)
=M_m^2-8+16\sin^2 a=M_m^2-8\cos(\pi/m).
\]
The displayed example attains equality. \(\square\)

**Corollary (quantitative NORI and boundary witness threshold).** If a legal complete path \(P\) of length \(m\ge3\) has
\[
Q_m(P)>\csc^2(\pi/(2m))-8\cos(\pi/m),
\]
then its color word has at most one change. For an antipodally odd NORI1 coloring, root sliding then produces a monochromatic full geodesic; for an ordinary boundary tight-path instance, it yields the required one-change witness.

**Scope.** The ascent lemma applies to arbitrary binary words. Flipping a single edge observation is generally not realizable by changing a rooted geodesic while preserving the coloring and dimension-simple constraint. A closure theorem still needs a legal path-exchange mechanism that approaches or crosses the sharp threshold.


#### Balanced realization of a Petrie cycle and all its immediate exchanges

Perfect vertex balance leaves the complete color data of one projective Petrie cycle and its immediate square exchanges freely prescribable. The construction below makes this freedom compatible, in arbitrarily large dimension, with realization of every binary full-geodesic profile.

Number the directions \(0,\ldots,n-1\), let \(n=2m\ge8\), and fix the standard full geodesic
\[
v_j=\sum_{t<j}e_t,\qquad P=(v_0,\ldots,v_n).
\]
Extend it by \(v_{j+n}=\bar v_j\); its directions repeat modulo \(n\). Denote its projective Petrie cycle by \(C\). For each \(j\) modulo \(n\), its adjacent exchange replaces the two steps in directions \(j,k\), where \(k=j+1\pmod n\), by the other side of their square:
\[
v_j\longrightarrow v_j+e_k\longrightarrow v_{j+2}.
\tag{BR1}
\]
For \(j=n-1\), this uses the first edge of the antipodal copy of \(P\).

**Theorem (balanced square-neighborhood realization).** Prescribe arbitrary colors for the \(n\) successive edge orbits of \(C\), and arbitrary ordered color pairs for all \(n\) alternate two-edge routes (BR1). There is an antipodally odd vertex-balanced coloring realizing all these prescriptions. It can be obtained from a fixed balanced unary coloring by changing at most \(24n\) cube edges.

*Proof.* Pair direction \(i\) with \(i+m\), for \(0\le i<m\). Seek rules of the form
\[
\boxed{c_i(x)=f_i(x|_{[n]\setminus\{i,i+m\}}),\qquad
c_{i+m}(x)=1-c_i(x),}\tag{BR2}
\]
where each \(f_i\) is antipodally odd on its \(n-2\) input bits. These rules ignore their own edge directions and give precisely \(m\) edges of each color at every vertex.

For each underlying function \(f_i\), the prescribed original edges in its two directions have input states
\[
A_i=v_i|_{[n]\setminus\{i,i+m\}},\qquad
B_i=v_{i+m}|_{[n]\setminus\{i,i+m\}}.
\]
Their Hamming distance is \(m-1\), and their distances to each other's antipodes are also \(m-1\). In either direction, the two alternate-square edges have input states differing from the corresponding original state in the preceding or following direction bit. At the cyclic seam, take the antipodal representative before making this comparison. Those two bits are distinct and belong to the input set.

Thus the six prescribed projective input states for \(f_i\) lie in radius-one neighborhoods of \(A_i,B_i\), with antipodal representatives allowed. The four centers \(A_i,\bar A_i,B_i,\bar B_i\) have pairwise distances at least \(m-1\ge3\). Their radius-one neighborhoods are disjoint. Within each of the two relevant neighborhoods the center and its two specified neighbors are distinct. All six input states are consequently distinct even after antipodal identification. Their values may be assigned independently; the direction \(i+m\) prescriptions are converted to \(f_i\)-values by complementing their requested colors. Assign complementary values at the six antipodal input states.

Complete each \(f_i\) using the default unary rule
\[
f_i^*(x)=x_{i+1}.
\tag{BR3}
\]
The reader \(i+1\) belongs to its input set. Both the prescribed input set and its values respect complementation, so using (BR3) elsewhere gives an odd Boolean function. This proves legality and balance.

At most twelve input states per \(f_i\) differ from the default. Each input state represents two undirected edges in each of its two paired directions. Hence at most \(4\cdot12m=24n\) cube edges change. \(\square\)

##### Full profile support survives every such local prescription

**Theorem (simultaneous full support).** For every even \(n=2m\ge18\), the completion in (BR2)--(BR3), for *any* of the prescribed square-neighborhood data above, realizes every binary direction-indexed color profile:
\[
\boxed{\mathcal W(c)=\mathbb F_2^n.}\tag{BR4}
\]

*Proof.* All rules of the default coloring \(c^*\) are unary. The established all-dimensional one-reader theorem, followed by whole-direction color reversals and antipodal translation, realizes any specified binary profile on a default full geodesic with some direction order \(\pi\). Every default rule reads one of the bits in
\[
J=\{1,\ldots,m\}.
\]
Therefore the remaining \(m\) initial bits
\[
F=\{0,m+1,\ldots,2m-1\}
\]
may be varied freely, keeping \(\pi\) and the initial \(J\)-bits fixed, without changing this profile.

Choose those free initial bits uniformly. Every paired set \(\{i,i+m\}\) contains precisely one bit from \(F\). At any specified step in either paired direction, the input state of \(f_i\) is therefore uniform on an affine subcube of dimension \(m-1\). Its probability of hitting the set of at most twelve modified input states is at most \(12/2^{m-1}\). A union bound over the \(2m\) steps gives
\[
\Pr(\text{some traversed edge uses a modified input})
\le\frac{24m}{2^{m-1}}<1
\qquad(m\ge9).
\tag{BR5}
\]
Choose free bits avoiding every modified input. The resulting geodesic retains its prescribed default profile in \(c\). Repeat the argument for each target profile; its root and order are allowed to vary. This proves (BR4). \(\square\)

The result concerns one global construction in every stated dimension. It retains arbitrary local square data while guaranteeing all \(2^n\) profiles elsewhere.

##### Strict grade-three islands in the balanced exchange gallery

For a projective Petrie cycle, let \(g(C)\) be its completed odd turn grade. Form the gallery whose vertices are these cycles and whose edges are adjacent direction exchanges at any root slide. The sublevel gallery at three is the induced graph on \(g\le3\).

**Theorem (balanced grade-three exchange islands).** For every even \(n\ge10\), there exists a legal vertex-balanced coloring and a projective Petrie cycle \(C\) with
\[
\boxed{g(C)=3,\qquad g(C')=5
\quad\text{for every immediate adjacent-exchange neighbor }C'.}
\tag{BR6}
\]
For every even \(n\ge18\), the coloring can simultaneously satisfy (BR4), and hence have monochromatic full antipodal geodesics. Thus its grade-three sublevel gallery contains an isolated grade-three vertex alongside grade-one vertices.

*Proof.* Let
\[
a=b=\lfloor n/3\rfloor,\qquad d=n-a-b,
\]
and prescribe on \(P\) the word \(0^a1^b0^d\). Its completed comparison word \(\delta\) has three ones, with successive cyclic gaps \(a,b,d\), all at least three. Every consecutive triple
\[
(\delta_{j-1},\delta_j,\delta_{j+1})
\]
therefore contains at most one one.

Choose the alternate two-edge color word at exchange \(j\) to differ from the *old positional word* by \((\alpha_j,\beta_j)\), according to
\[
\begin{array}{c|c}
(\delta_{j-1},\delta_j,\delta_{j+1})&(\alpha_j,\beta_j)\\ \hline
(1,0,0)&(0,1)\\
(0,1,0)&(1,1)\\
(0,0,1)\ \text{or}\ (0,0,0)&(1,0).
\end{array}
\tag{BR7}
\]
The positions in this table are word positions after the exchange, rather than direction-indexed colors. At the cyclic seam use \(b_{j+n}=1-b_j\), where \(b\) is the prescribed color word.

Changing those two observations toggles their three incident turn bits by
\[
(\alpha_j,\ \alpha_j+\beta_j,\ \beta_j).
\tag{BR8}
\]
In every row of (BR7), the total turn count rises by two. All other turns stay unchanged, so every exchanged cycle has grade five. The square-neighborhood realization theorem implements all these choices simultaneously in a balanced legal coloring. When \(n\ge18\), its specified default completion has full profile support by (BR4). \(\square\)

**Explicit successful ten-dimensional instance.** Apply the deterministic completion (BR3) and table (BR7) to \(n=10\) and the word \(0001110000\). Besides its isolated grade-three cycle, it has a full zero geodesic with initial support
\[
\{0,3,4,6,8\}
\]
and direction order
\[
(7,8,0,4,1,3,5,9,2,6).
\tag{BR9}
\]
Direct evaluation of the rules defined above gives ten zeros. Thus a globally successful balanced coloring already supplies the obstruction in dimension ten.

**Verification.** Independent evaluation of (BR7) and the completed rules in dimensions \(10,12,14,20\) gave grade three for the prescribed cycle and grade five for each of its cyclic adjacent exchanges. Arbitrary prescribed original words and alternate color pairs were also checked for input consistency in 100 trials each in dimensions \(8,10,12,18\). Balance and oddness were checked exhaustively in the ten-dimensional instance. The dimension-uniform proofs use input-state separation, the union bound, and the three-bit identity (BR8), independently of these checks.

**Implication for a Minty-style closure proof.** A grade-three cycle may require a first step through grade five before any adjacent-exchange route can reach a successful cycle. Root slides and reversal preserve its grade and stay in the same projective cycle. Consequently an approach confined to nonincreasing grade, even allowing neutral exchanges, faces the obstruction (BR6). A local argument using a single cycle, its immediate exchanges, and balance also faces unrestricted realization of all those local data by (BR2). A closure argument must use compatibility across larger families of cycles, a higher-grade intermediate state, or a walk relaxation with an additional global objective. The unrestricted NORI1 conjecture remains open.


##### Mesoscopic exchange-ball indistinguishability under full profile saturation

A cycle in the **projective square-exchange gallery** is a simple antipodal-quotient Petrie cycle traversing all cube directions once. Two cycles are adjacent when an exchange of successive direction steps replaces one two-edge square route with the other (including the cyclic seam). Let \(\mathcal B_R(C)\) be the radius-\(R\) ball of cycles around a chosen cycle \(C\) in this gallery, with no restriction on intermediate turn grades.

Write \(E_{\mathrm{orb}}(\mathcal B_R(C))\) for the set of antipodal undirected-edge orbits traversed by at least one cycle in the ball.

**Lemma (gallery-ball edge exposure).** In every dimension \(n\ge3\),
\[
\boxed{
|E_{\mathrm{orb}}(\mathcal B_R(C))|
\le n+2\sum_{j=1}^{R}n^j.
}\tag{BE1}
\]
*Proof.* Every cycle uses \(n\) distinct edge orbits, and a single adjacent exchange changes at most two of them. The gallery has degree at most \(n\), since there are \(n\) cyclic adjacent pairs of directions. Choose a breadth-first tree of the ball from \(C\). There are at most \(n^j\) vertices at distance \(j\). On adjoining each tree vertex, at most two edge orbits not present in its parent are added. This proves (BE1). \(\square\)

Recall the exponentially robust legal full-profile and chronological-word packing theorem (RPC1): for any fixed \(A>6e\) and all sufficiently large \(n\), there exists a legal coloring \(d\) of \(Q_n\) possessing, for **each** binary direction-profile target and each chronological-word target, at least
\[
K_n=\lfloor\gamma_A2^{\lfloor n/2\rfloor}\rfloor
\]
pairwise antipodal-edge-orbit-disjoint full geodesics. Thus any modification of fewer than \(K_n\) edge-orbit color variables preserves full profile and chronological-word surjectivity.

**Theorem (mesoscopic exchange-ball cloning).** Let \(c\) be **any** legal antipodally odd coloring of \(Q_n\), \(C\) any projective direction-rainbow Petrie cycle, and \(R\ge0\) an integer satisfying
\[
\boxed{n+2\sum_{j=1}^{R}n^j<K_n.}\tag{BE2}
\]
Then there exists another legal antipodally odd coloring \(\widetilde c\) of the *same* \(Q_n\) such that

(i) every edge color on every projective cycle in \(\mathcal B_R(C)\) is unchanged: \(\widetilde c(e)=c(e)\) on all their represented edge orbits;

(ii) every cycle of the ball retains its projective turn grade, and every exchange relation and color pattern entirely within this ball is unchanged;

(iii) \(\widetilde c\) realizes **every** direction-indexed full-geodesic color profile and **every** temporal \(n\)-letter color word, and in particular has a monochromatic full antipodal geodesic.

*Proof.* Pick any robust coloring \(d\) supplied by (RPC1). Let \(E=E_{\mathrm{orb}}(\mathcal B_R(C))\), with \(|E|<K_n\) by the lemma. On every orbit in \(E\), replace the value of \(d\) by the prescribed value of \(c\), and on its antipodal partner replace the value by its complement. Leave \(d\) unchanged on all other edge orbits. The prescribed pattern is consistent because \(c\) is legal. Thus \(\widetilde c\) remains antipodally odd, undirected, and agrees with \(c\) on all edges traversed by cycles in the ball. This proves (i)--(ii). The recoloring changes fewer than \(K_n\) antipodal orbit variables, so for each target binary profile and word, at least one of the \(K_n\) orbit-disjoint witnessing geodesics of \(d\) is untouched. Therefore every target remains attained, proving (iii). \(\square\)

**Corollary (growing-radius indistinguishability).** Fix any \(\varepsilon\in(0,\tfrac12)\). For all sufficiently large \(n\), condition (BE2) holds for
\[
\boxed{
0\le R\le
\left\lfloor(\tfrac12-\varepsilon)\frac{n\log2}{\log n}\right\rfloor-3.
}\tag{BE3}
\]
Consequently every possible colored exchange-ball pattern around an arbitrary legal cycle, even through radius of order \(n/\log n\), can be replicated without change inside a globally successful coloring with full profile and chronological-word support.

*Proof.* For \(n\ge2\), \(n+2\sum_{j=1}^Rn^j\le4n^{R+1}\). Under (BE3), this is \(O(2^{(1/2-\varepsilon)n})\), while \(K_n\ge\gamma_A 2^{n/2-O(1)}-1\). Hence (BE2) holds for large \(n\). \(\square\)

**Scope and methodological consequence.** The theorem is a *realization and indistinguishability* result, not a refutation of NORI1. It applies even if the source coloring \(c\) were hypothetically bad; only the preserved region is copied, while the many distant edges may change. It strengthens the radius-one balanced neighborhood realization (BR2)--(BR4) in a different direction: arbitrary initial legal colorings and a growing exchange radius, with full target saturation guaranteed in the completion, but **without** requiring the completion to remain vertex-balanced. In particular, any proposed criterion that identifies the *global* absence of a one-turn cycle from solely the finite colored data of an \(R\)-ball around one selected Petrie cycle, with \(R\) as in (BE3), cannot be valid. Closure must use global exchange information, or properties involving more than this local ball; an isolated grade-three critical cycle by itself is consistent with many faraway monochromatic witnesses.



##### Cartesian amplification of exchange distance from three-turn cycles to one-turn witnesses

Let \(\mathcal G(c)\) be the projective full-geodesic square-exchange gallery of a legal antipodally odd coloring \(c\). Its vertices are direction-rainbow Petrie cycles in the antipodal quotient cube, and its edges are cyclic adjacent direction swaps. Write \(\mathcal G_1(c)\) for its cycles of completed turn grade one and
\[
d_\square(C,\mathcal G_1(c))
=\min_{C'\in\mathcal G_1(c)}\{\text{square exchanges along a gallery walk }C\to C'\},
\]
with value \(+\infty\) if no such cycle exists. This distance does **not** bound the grades along intermediate cycles.

**Lemma (factor projection is nonexpansive in the sum metric).** Let \(c=c^{(1)}\boxtimes\cdots\boxtimes c^{(m)}\) be an independent Cartesian product of legal colorings. Every projective full-geodesic cycle \(C\) of the product has well-defined factor projections \(C_j\in\mathcal G(c^{(j)})\), obtained by retaining only steps in factor \(j\). For a single square exchange \(C\to C'\), either every factor projection is unchanged, or there is a unique factor \(j\) in which \(C_j,C'_j\) are square-exchange neighbors. In particular,
\[
\boxed{
\sum_{j=1}^m d_{\square,j}(C_j,C'_j)\le1
}\tag{BE4}
\]
and for any two product cycles \(C,D\),
\[
\boxed{
d_\square(C,D)\ge\sum_{j=1}^m d_{\square,j}(C_j,D_j).
}\tag{BE5}
\]

*Proof.* Choose any rooted representative of the product cycle and restrict its root bits and temporal direction order to each Cartesian factor. Interleaving steps in other factors does not affect colors or vertices of the projected factor path. Cyclic shifts of the global representative restrict to cyclic shifts of each factor representative, and global antipodal translation restricts to its factor analogues, so the projected projective cycles are well defined. A swap of two consecutive global directions belonging to distinct factors does not alter either factor's relative order or rooted edge sequence, and hence fixes every projected cycle. A swap involving two directions of one factor changes only their relative order in that factor; they are cyclically adjacent there, so this produces at most one factor square-exchange step. This proves (BE4). Summing (BE4) along any gallery walk and applying the triangle inequality in each factor gives (BE5). \(\square\)

**Theorem (tensor lower bound on escape-to-one-turn distance).** For the above independent product and every full product cycle \(C\),
\[
\boxed{
d_\square(C,\mathcal G_1(c))
\ \ge\
\sum_{j=1}^m d_{\square,j}(C_j,\mathcal G_1(c^{(j)})).
}\tag{BE6}
\]
*Proof.* A one-turn projective product cycle admits a full representative with monochromatic temporal word: cyclically move its root across the unique projective turn. Projecting this monochromatic full geodesic onto every factor gives a monochromatic full geodesic in that factor. Thus each factor projection of a grade-one product cycle lies in the corresponding \(\mathcal G_1(c^{(j)})\). Apply (BE5) to a shortest gallery walk from \(C\) to any grade-one product cycle, and minimize its factor distances. \(\square\)

**Theorem (linear-depth grade-three traps despite universal profile support).** For every integer \(m\ge1\), there is a **vertex-balanced legal antipodally odd** coloring \(c_m\) on
\[
\boxed{Q_{18m}}\tag{BE7}
\]
that realizes every binary full-geodesic direction-indexed color profile and every projective color degree permitted by its factor witnesses, contains monochromatic full antipodal geodesics, and contains a projective direction-rainbow cycle \(C_m\) of grade three with
\[
\boxed{
d_\square(C_m,\mathcal G_1(c_m))\ge2m=\frac{n}{9}.
}\tag{BE8}
\]

*Proof.* The established balanced local-square realization theorem (BR6), together with its full-profile completion (BR4), supplies a legal vertex-balanced coloring \(b\) on \(Q_{18}\) whose standard full geodesic has chronological color word \(0^6 1^6 0^6\). Its projective cycle \(C_*\) has grade three, and **every** adjacent square-exchange neighbor has grade five. Therefore \(d_\square(C_*,\mathcal G_1(b))\ge2\). The same coloring has full direction-profile support by (BR4), hence possesses monochromatic full geodesics.

Take the independent product \(c_m=b^{\boxtimes m}\). It is legal, antipodally odd, and vertex-balanced, and its direction-profile support is the Cartesian product of the full supports of the \(m\) factors, hence the full binary cube of size \(18m\). Interleave the chosen factor geodesics *run by run*: first all six-edge zero prefixes, then all six-edge one middles, finally all six-edge zero suffixes. This is a full product geodesic with word
\[
0^{6m}1^{6m}0^{6m},
\]
so its projective cycle \(C_m\) has grade three. Every projected factor cycle is \(C_*\), and (BE6) yields
\[
d_\square(C_m,\mathcal G_1(c_m))
\ge\sum_{j=1}^m d_\square(C_*,\mathcal G_1(b))
\ge2m.
\]
Monochromatic product full geodesics exist by concatenating monochromatic factor geodesics of the same color, using antipodal translation where necessary. \(\square\)

**Implications and boundary.** The coloring family is globally successful, even profile-universal and vertex-balanced, yet an arbitrarily chosen three-turn projective cycle can be linearly far in the unrestricted square-exchange graph from *every* one-turn witness. Intermediate grades are completely unrestricted in (BE8), so permitting uphill excursions alone does not yield a bounded-length repair. This substantially strengthens the one-step grade-five island phenomenon (BR6). It refutes a universal \(o(n)\)-exchange repair principle from an arbitrary grade-three witness. It does **not** rule out a proof using a different strategically selected witness, a global extremization criterion, or a nonlocal operation affecting several Cartesian factors simultaneously.



##### Connectivity and a quadratic diameter bound for the ungraded Petrie gallery

The square-exchange gallery has a purely combinatorial connectivity property, independent of the edge coloring. To avoid identifying the two orientations of a cycle, work first with **oriented** projective direction-rainbow Petrie cycles; the unoriented gallery is their quotient.

**Theorem (ungraded gallery diameter).** For every \(n\ge2\), the oriented projective full-geodesic square-exchange gallery is connected, with diameter at most
\[
\boxed{(n-1)(2n-3)+\binom{n-1}{2}.}\tag{BE9}
\]
Consequently the same bound holds for its unoriented quotient.

*Proof.* Distinguish direction zero. An oriented projective Petrie cycle can be represented uniquely by a root \(x\) with bit \(x_0=0\) and a full direction order
\[
(0,\pi_1,\ldots,\pi_{n-1}),
\]
with all \(\pi_j\) distinct and in \(\{1,\ldots,n-1\}\). Indeed cyclic root rotation moves its unique direction-zero edge to the first position, while its antipodal mate gives the complementary root, of which precisely one has bit zero equal to zero.

Swapping two adjacent entries among \(\pi_1,\ldots,\pi_{n-1}\) is an allowed square exchange and does not alter \(x\). Thus the tail can be arbitrarily permuted in at most \(\binom{n-1}{2}\) exchanges.

To toggle any selected root bit \(i>0\), first move direction \(i\) to the front of the tail by at most \(n-2\) adjacent swaps. The order begins \((0,i,\ldots)\). Exchange the leading directions, producing \((i,0,\ldots)\), and cyclically slide the root through the new first \(i\)-edge until the order begins with direction zero again. This changes the canonical root to \(x+e_i\); bit zero remains zero. The resulting tail has moved \(i\) to its end. Restore the original tail order using at most \(n-2\) adjacent swaps. The total cost of toggling root bit \(i\) while preserving the desired tail is at most \(2n-3\).

Thus any two canonical roots can be connected by changing at most \(n-1\) bits, using at most \((n-1)(2n-3)\) moves. Afterward reorder the tail to the desired permutation in at most \(\binom{n-1}{2}\) moves. This proves connectivity and (BE9). Passing to the unoriented quotient cannot increase distances. \(\square\)

**Corollary (what an unrestricted exchange-to-one-turn assertion means).** For any legal coloring \(c\), the existence of a gallery walk from one (equivalently every) projective three-turn cycle to some projective one-turn cycle, with no restriction on its intermediate grades or its length, is *equivalent to the existence of a one-turn cycle itself*, provided a three-turn cycle is present. The gallery walk then exists for every coloring solely by the connectivity theorem. In the one-defect normalization (GD4), obtaining the desired one-turn endpoint would settle NORI1; connectivity supplies no additional color-based existence information.

*Proof.* If a one-turn cycle exists, the connectivity theorem joins it to every starting cycle. Conversely any walk ending at one-turn exhibits such a cycle. A one-turn projective cycle corresponds by cyclic root rotation to a monochromatic full antipodal geodesic. \(\square\)

Together with the linear-distance trap (BE8), this establishes that a useful exchange proof must involve **more** than abstract connectivity and an unspecified uphill detour. It may control a structural potential, restrict a strategically extremized starting witness, exploit correlated collections of cycles, or give a color-based reason that a one-turn endpoint must exist. Even the bound (BE9) on gallery diameter holds in hypothetical counterexamples and therefore has no NORI1-closing force by itself.



##### Audited eighteen-cube escape distance five; linear amplification

Take the deterministic balanced legal coloring b on Q_18 of (BR2)--(BR7), with original projective Petrie cycle C_* supported on the standard direction order 0,1,...,17 and chronological word 0^6 1^6 0^6. The completed coloring uses the two-bit-paired rules of (BR2), the BR7 alternate square prescriptions and the default unary rule (BR3); it realizes every direction-profile by (BR4).

**Computer-assisted finite lemma (certified escape depth).**
\[
\boxed{d_\square(C_*,\mathcal G_1(b))=5.}\tag{BE10}
\]

*Finite proof certificate.* Represent every oriented projective cycle canonically by its first direction zero and a root with bit zero equal to zero. Generate each of its 18 square-exchange neighbors by rotating to one cyclic adjacent pair, swapping the two directions, then returning to canonical form. Evaluate the resulting direction-order path with the deterministic BR2--BR3 coloring. Its odd projective grade is its internal switch count plus one if its final and initial edge colors agree. Exhaustive breadth-first enumeration yields the following size and grade counts on the successive distance layers:
\[
\begin{array}{c|r|rrrrrrr}
R&\#&g=1&g=3&g=5&g=7&g=9&g=11&g=13\\
0&1&0&1&0&0&0&0&0\\
1&18&0&0&18&0&0&0&0\\
2&171&0&15&25&131&0&0&0\\
3&1140&0&42&263&343&492&0&0\\
4&5985&0&182&954&2051&1792&1006&0\\
5&26334&2&666&3647&8003&8517&4422&1077
\end{array}\tag{BE11}
\]
No grade-one cycle lies within four exchanges. The sequence of cyclic exchange indices (zero-based)
\[
\boxed{6,\ 5,\ 9,\ 8,\ 10}\tag{BE12}
\]
changes the original grade three through grades 5,3,5,3,1, and ends at the full direction order
\[
(0,1,2,3,4,7,5,6,10,8,11,9,12,13,14,15,16,17),
\]
whose temporal edge-color word is all zeros. This proves the upper and lower distance bounds. The layer counts and path were independently checked by a deterministic self-contained Python audit (petrie_grade18_exchange_audit.py), using only bit arithmetic, set-based breadth-first enumeration, and assertions. It also verifies edge-direction invariance, antipodal oddness, and balance in the stated rule system. The computer-assisted component is solely the finite enumeration (BE11), not the product induction.

**Theorem (linear-depth successful balanced three-turn cycles).** For every integer h>=1, let N=18h. There exists a legal vertex-balanced antipodally odd coloring c_h of Q_N realizing *every* binary direction-indexed full-geodesic profile, with monochromatic full geodesics, and with a projective grade-three cycle C_h such that
\[
\boxed{d_\square(C_h,\mathcal G_1(c_h))
\ge5h=\frac{5N}{18}.}\tag{BE13}
\]
No upper bound on turn grades along the exchange walk is imposed.

*Proof.* Let c_h be the independent h-fold Cartesian power b^{\boxtimes h}. It is legal, balanced and full-profile-universal, by factor product rules and (BR4). Choose in every factor a copy of C_* and interleave its three chronological runs, first all six-edge zero prefixes, then all six-edge one middles, then all six-edge zero suffixes. The product full path has word 0^{6h}1^{6h}0^{6h}, hence its projective cycle C_h has grade three and projects to C_* in every factor. Every global square exchange changes the projected projective cycle in at most one factor (BE4)--(BE6). Since any global grade-one witness must project to a grade-one factor cycle, its distance from C_h is at least the sum of factor distances, namely 5h. A monochromatic full product geodesic exists by concatenating same-color monochromatic geodesics of the factors. \(\square\)

The finite certificate strengthens the symbolic exchange-distance bound 1/9 from (BE8) to 5/18. It proves a *global* linear obstacle to repairing an arbitrarily selected three-turn witness through adjacent square exchanges, even when intermediate grades are unrestricted and the coloring itself is successful and profile-universal. It does not refute NORI1.


##### Paired-turn non-isolation and its sharp balanced converse

Let C be a projective direction-rainbow Petrie cycle of a legal antipodally odd coloring, represented by a temporal edge word 0^a 1 0^b, with a,b>=1.

**Theorem (two unavoidable nonascending exchanges).** Swapping the exceptional one-colored edge with either its immediately preceding or following zero-colored edge gives a projective Petrie cycle of grade at most three. If the coloring has no grade-one cycle, both neighbors have grade three. For n>=4 these are distinct neighbors, so a singleton-defect grade-three cycle cannot be isolated in the grade-three sublevel gallery of a hypothetical NORI1 counterexample.

*Proof.* Projectively complete the edge-color word with the antiperiodic rule. A swap changes two adjacent edge-color observations and affects only their three surrounding turn bits; the change of turn count is even. In each of the two swaps next to the singleton defect, the three-turn window initially contains at least the two switched turns surrounding that defect. If its count is two, the replacement window retains an even count, hence at most two; if its count is three, the replacement count is odd, hence at most three. All outside turns stay unchanged. Therefore the grade cannot increase beyond three. Positive odd grades below four are one and three. The two transpositions are different for n>=4. \(\square\)

**Theorem (balanced sharpness).** In every even dimension n=2m>=18 there is a legal vertex-balanced coloring with full profile support W(c)=F_2^n and a one-exception Petrie cycle C of word
\[
0^{m-1}\,1\,0^m,
\]
with precisely two grade-three immediate exchange neighbors, no grade-one immediate neighbor, and grade five at all its remaining n-2 neighbors.

*Proof.* In the balanced local-square realization theorem (BR2)--(BR5), prescribe the indicated original word. The two cyclic adjacent swaps touching its lone one-colored edge originally replace pairs 01 and 10. Prescribe alternate color pair 11 in each case; because the outer edges are zero, this preserves the local count of two turns and gives grade three. The three cyclic switched turns are otherwise separated by gaps at least three. Every remaining swap therefore sees at most one original turn in its three-turn window; use the alternate-pair prescription (BR7) to increase the number of turns by two, producing grade five. All n local prescriptions are jointly realizable by the balanced construction (BR2), and in n>=18 its default completion retains full profile support (BR4), including monochromatic full geodesics. \(\square\)

Thus the two nonascending square exchanges forced by a singleton defect are the strongest purely first-neighborhood conclusion possible, even in perfectly balanced globally successful profile-universal colorings. They do not alone yield a one-turn witness.



##### Linear-depth single-defect Petrie traps via three separated directional anchors

Write \(H_2(\alpha)=-\alpha\log_2\alpha-(1-\alpha)\log_2(1-\alpha)\), and fix a constant \(0<\alpha<1/4\) with \(H_2(\alpha)<1/2\), for instance \(\alpha=1/10\). Let \(R=\lfloor\alpha n\rfloor\).

**Theorem (linear-radius singleton-defect exchange traps).** For every sufficiently large \(n\), there exists a legal antipodally odd coloring \(c\) of \(Q_n\) attaining every direction-indexed full-geodesic binary color profile and every chronological color word, with a projective Petrie cycle \(C\) whose representative full path has a single color-one edge and
\[
\boxed{d_\square(C,\mathcal G_1(c))>R.}\tag{AT3}
\]
In particular, the coloring is globally successful although no projective cycle obtainable from this singleton-defect \(C\) in at most \(\lfloor n/10\rfloor\) adjacent square exchanges has grade one.

*Proof.* Fix the standard oriented projective cycle \(C\) rooted at the zero vector with direction order \(0,1,\ldots,n-1\). Choose three marked directions
\[
p=\lfloor n/4\rfloor,\quad q=\lfloor n/2\rfloor,\quad r=\lfloor3n/4\rfloor.
\]
They occur in the canonical cyclic order \(0,p,q,r\), with successive gaps of order \(n/4\). Prescribe on the original path the word having a single color-one edge in direction \(q\), every other edge being color zero.

An oriented projective cycle has a canonical lift whose first step is in direction zero and whose starting root has bit zero equal to zero. Among cycles obtained from \(C\) by at most \(R\) cyclic adjacent exchanges, the four marked directions \(0,p,q,r\) retain their cyclic order: changing their order would require first bringing two originally separated marked directions into cyclic adjacency, requiring at least the number of intervening directions, which is larger than \(R\) for all sufficiently large \(n\). Hence **every** canonical full path in the exchange ball uses the marked directions in the linear order \(p,q,r\).

For each \(i\in\{p,q,r\}\), consider all direction-\(i\) edge orbits visited by cycles in this ball. The projective direction-\(i\) edge orbits form a folded \((n-1)\)-cube. One square exchange changes the used direction-\(i\) orbit, if at all, by one transverse step. Therefore the number of visited orbits in that direction is at most
\[
B_{n-1}(R)=\sum_{j=0}^R\binom{n-1}{j}.
\tag{AT4}
\]
Prescribe color zero on **every encountered direction-\(p\) and direction-\(r\) edge**, and color one on **every encountered direction-\(q\) edge**, always evaluated on the canonical representative. These prescriptions are simultaneously consistent with antipodal oddness: all three marked directions are nonzero, and every canonical lift uses them after direction zero, so both endpoints of each encountered marked-direction edge have bit zero equal to one. Its antipodal mate has bit zero equal to zero and can never be an observed canonical representative of that direction. Thus the same antipodal edge orbit cannot receive conflicting prescribed colors. On the remaining \(n-3\) original C-orbits, prescribe color zero as well; all these original orbits have distinct directions, and their mates receive the complementary values. The total number of prescribed edge-orbit variables is at most
\[
\boxed{3B_{n-1}(R)+n.}\tag{AT5}
\]

Every canonical path of every cycle in the ball uses a direction-\(p\) edge of color zero, later a direction-\(q\) edge of color one, and still later a direction-\(r\) edge of color zero. Its temporal word therefore has **at least two internal color changes**, so its positive odd projective turn grade is at least three. In particular **no grade-one cycle is present anywhere in the ball**. This argument uses an ordered three-color pattern, not just the presence of both colors.

By the established exponentially robust legal profile-and-word packing theorem (RPC1), for any fixed \(A>6e\), in every sufficiently large dimension there exists a legal coloring \(d\) having at least \(K_n=\lfloor\gamma_A2^{\lfloor n/2\rfloor}\rfloor\) pairwise antipodal-edge-orbit-disjoint geodesic witnesses of **every** direction profile and **every** temporal color word. Since \(H_2(\alpha)<1/2\),
\[
3B_{n-1}(\lfloor\alpha n\rfloor)+n
\le 2^{(H_2(\alpha)+o(1))n}<K_n
\]
for all sufficiently large n. Modify fewer than \(K_n\) orbit variables of \(d\) to implement all the above finite local prescriptions. Each target still has at least one untouched geodesic witness, so the resulting legal coloring \(c\) attains every direction profile and every temporal word. On the other hand, its entire radius-\(R\) exchange ball about the prescribed singleton-defect C contains no grade-one cycle. This proves the theorem. \(\square\)

**Theorem (balanced amplification).** For every sufficiently large \(n\), the complementary paired lift \(L(c)\) is a legal, perfectly vertex-balanced coloring on \(Q_N\), \(N=2n\), with full direction-profile support and monochromatic full geodesics. It contains a singleton-defect projective Petrie cycle \(C^+\) satisfying
\[
\boxed{d_\square(C^+,\mathcal G_1(L(c)))>\lfloor N/20\rfloor.}\tag{AT6}
\]

*Proof.* Use old rules \(L(c)_i(x,z)=c_i(x)\) and paired new rules \(L(c)_{n+i}(x,z)=1+c_i(x)\). Every old/new pair contributes one edge of each color at every vertex, so this is a legal balanced coloring. The full-profile cylinder property (SM3) preserves profile universality.

For the original singleton-defect path P rooted at x, put every new direction n+i with \(c_i(x)=1\) before P and every new direction with \(c_i(x)=0\) after P. Such new edges are zero: before P their color is \(1+c_i(x)=0\), and after P it is \(1+c_i(\bar x)=c_i(x)=0\). Thus the lifted full path has the same single defect and projects to C.

Project any full projective cycle of the lifted cube onto its old directions. The result is a projective full cycle in the original cube. A square exchange involving two old steps projects to at most one cyclic adjacent square exchange; an exchange involving a new step does not change the old projected cycle because old rules ignore all new bits. Thus projection does not increase gallery distance. Every lifted grade-one cycle has a monochromatic full representative, whose projection is a monochromatic full path of the original coloring, and therefore projects to an old grade-one cycle. Applying (AT3) yields (AT6). \(\square\)

**Audit and consequence.** The preliminary approach of coloring all off-C local edges blue was insufficient: a mixed binary temporal word may have just one switch and give projective grade one. The proof above replaces it by **three ordered anchored directions of colors 0,1,0**. That stronger condition guarantees the needed two internal changes throughout the ball, and the projection argument proves a linear-depth singleton-defect trap even under vertex balance and profile universality. Hence a proposed NORI1 proof cannot rely on a sublinear number of adjacent direction exchanges from an arbitrarily chosen one-defect witness; global selection or nonlocal moves remain necessary.


##### Linear-radius exchange-ball cloning for arbitrary legal colorings

The direction-orbit exposure bound (AT4) improves the earlier crude branching-tree estimate (BE1), independently of whether the distinguished cycle has a singleton defect.

**Theorem (linear-radius full-neighborhood indistinguishability).** Fix \(0<\alpha<1/2\) with \(H_2(\alpha)<1/2\), such as \(\alpha=1/10\), and put \(R=\lfloor\alpha n\rfloor\). For every sufficiently large \(n\), every legal antipodally odd coloring \(c\) of \(Q_n\), and every projective direction-rainbow Petrie cycle \(C\), there exists a second legal coloring \(\widetilde c\) of the same cube such that:

(i) every undirected edge color on every projective Petrie cycle within \(R\) adjacent square exchanges of \(C\) agrees with \(c\), including the complementary antipodal mate values;

(ii) all those cycles retain their projective grades, all neighbor relations, and all local color patterns inside the ball;

(iii) \(\widetilde c\) realizes every binary direction-indexed full-geodesic profile and every chronological full-geodesic word. In particular, \(\widetilde c\) has monochromatic full antipodal geodesics.

*Proof.* Let \(E_{\rm orb}(\mathcal B_R(C))\) be the union of the antipodal edge orbits used by cycles in the gallery ball. For each direction i, its edge orbits form a folded \((n-1)\)-cube; exchanging adjacent directions i,j replaces its direction-i edge orbit by the neighboring parallel orbit across j. Hence the direction-i orbit stays within the folded Hamming ball of radius R about the orbit on C. Such a ball has at most \(\sum_{j=0}^R\binom{n-1}{j}\) members, so
\[
\boxed{
|E_{\rm orb}(\mathcal B_R(C))|
\le n\sum_{j=0}^R\binom{n-1}{j}
\le2^{(H_2(\alpha)+o(1))n}.
}\tag{BE14}
\]
For a fixed \(A>6e\), the established robust packing result (RPC1) gives a legal coloring \(d\) of \(Q_n\) having \(K_n=\lfloor\gamma_A2^{\lfloor n/2\rfloor}\rfloor\) pairwise antipodal-edge-orbit-disjoint witnesses for *every* direction profile and every chronological word. For sufficiently large n the bound (BE14) is smaller than \(K_n\), since \(H_2(\alpha)<1/2\). On every edge orbit in \(E_{\rm orb}(\mathcal B_R(C))\), overwrite \(d\)'s color with the corresponding color of the original legal coloring \(c\), and set its mate to the complementary color. This is consistent because c is legal and uses fewer than \(K_n\) orbit modifications. The resulting coloring \(\widetilde c\) agrees with c on the entire R-ball. For any target profile or chronological word, at most \(K_n-1\) of its \(K_n\) orbit-disjoint witnesses are affected, leaving at least one untouched. Thus \(\widetilde c\) is simultaneously profile-universal and word-universal, proving every claim. \(\square\)

The entropy equation \(H_2(\alpha)=1/2\) has its smaller solution near \(0.1100\). Thus the theorem permits every fixed linear-radius fraction below this value, a substantial strengthening of (BE3), which permitted only order \(n/\log n\). This result does **not** preserve vertex balance for arbitrary input c, but the singleton-defect specialization (AT6) does produce balanced, full-profile-universal examples with linear exchange-depth.

**Interpretation.** No property determined solely by the colored projective square-exchange ball of radius \(\lfloor0.1n\rfloor\) around one fixed witness cycle can certify global failure of NORI1. Whatever locally compatible pattern is present around that cycle can also be embedded, unchanged through this linear radius, in a legal coloring with full profile and word support. Any exchange-based closure proof must compare globally selected witnesses, exploit nonlocal moves, or use relations involving multiple distant exchange neighborhoods.


##### Deterministic quarter-dimension singleton-defect exchange traps

The robust packing theorem is not needed to build singleton-defect traps with a linear exchange barrier. A unary default coloring provides a larger radius and preserves full direction-profile support by a free-root argument.

**Theorem (quarter-dimension trap).** For every sufficiently large integer \(m\), put \(n=4m\). There is a legal antipodally odd coloring \(c\) of \(Q_n\) with
\[
\boxed{\mathcal W(c)=\mathbb F_2^n,}\tag{AT7}
\]
and a projective direction-rainbow Petrie cycle \(C\) represented by a full geodesic of temporal word
\[
0^{2m}\,1\,0^{2m-1}
\]
such that
\[
\boxed{d_\square(C,\mathcal G_1(c))\ge m=n/4.}\tag{AT8}
\]
The bound permits all intermediate turn grades. In particular the coloring itself has monochromatic full antipodal geodesics, but the designated single-defect cycle needs at least \(n/4\) adjacent square exchanges to reach any one-turn cycle.

*Proof.* Use the standard direction order \(0,1,\ldots,n-1\) from the zero root for the distinguished cycle C. Mark four cyclic directions
\[
0,\quad p=m,\quad q=2m,\quad r=3m.
\]
Any cyclic adjacent transposition sequence of fewer than m exchanges preserves the cyclic order of these four marked directions: initially each pair of successive marked directions has \(m-1\) unmarked directions between it, so at least m swaps are needed to transpose two marked directions. Thus in the canonical representative (starting with direction zero), every cycle within \(m-1\) exchanges traverses p, then q, then r in that order.

Begin with the unary legal odd coloring
\[
\boxed{d_0(x)=x_1,\qquad d_i(x)=x_0\quad(1\le i<n).}\tag{AT9}
\]
Its full direction-profile support is all \(\mathbb F_2^n\), with a large family of witnesses for each target profile. Indeed, given target \(w\), start with bit \(x_0=0\), order all nonzero directions i with \(w_i=0\) before direction zero and all those with \(w_i=1\) after it, and choose starting bit
\[
x_1=w_0+\mathbf1_{\{1\text{ placed before }0\}}\pmod2.
\]
This gives color w_i on every direction i, while the remaining \(n-2\) starting bits are unconstrained.

Let \(\mathcal B_{m-1}(C)\) be the projective square-exchange ball. For every direction-p and direction-r edge orbit encountered by any canonical representative in this ball, change the color of its encountered edge to zero and that of its antipodal mate to one. These changes are consistent: a canonical representative has initial bit zero equal to zero and takes direction zero first, so every subsequent edge in any nonzero direction has bit zero equal to one at both endpoints. An antipodal mate has bit zero equal to zero and is never an observed canonical edge in that direction. Leave all encountered direction-q edges at the default color one. Finally change to zero the colors of each original C-edge in the other nonzero directions, which are default-one; direction zero is already zero at the original root. The resulting legal odd coloring c has the advertised singleton word along C.

By the folded direction-orbit estimate (AT4), each of the two modified marked directions contributes at most
\[
B_{n-1}(m-1)=\sum_{j=0}^{m-1}\binom{n-1}{j}
\]
changed edge-orbit variables, and the remaining original-C adjustments contribute at most n. Thus the modification set \(\mathscr M\) satisfies
\[
\boxed{|\mathscr M|\le 2B_{n-1}(m-1)+n.}\tag{AT10}
\]

Now fix any prescribed full direction-profile target w, and choose the unary-default geodesic order and its bits \(x_0,x_1\) as above. Vary independently the other \(n-2\) starting bits. For each nonzero direction i, its traversed undirected edge orbit is uniform on a family of at least \(2^{n-3}\) distinct antipodal edge orbits: the n-3 free bits other than i determine distinct orbits, since bit zero is fixed at this step. Hence the probability that the selected default witness traverses any one modified orbit of direction i is at most \(2^{-(n-3)}\). Direction-zero edges were not modified. By the union bound,
\[
\Pr\{\text{some used orbit lies in }\mathscr M\}
\le\frac{2B_{n-1}(m-1)+n}{2^{n-3}}=o(1).
\tag{AT11}
\]
The last equality follows from the standard entropy estimate
\(B_{n-1}(m-1)\le2^{(H_2(1/4)+o(1))n}\)
and \(H_2(1/4)<1\). For every sufficiently large n, choose free starting bits avoiding all altered orbits. That geodesic still realizes the target profile w in the modified coloring c. As w was arbitrary, (AT7) follows.

Finally, every cycle \(C'\) within at most \(m-1\) adjacent exchanges of C retains the cyclic marked-direction order \(0,p,q,r\). Its canonical full path meets a direction-p edge of color zero, then a direction-q edge of color one, then a direction-r edge of color zero, by the corresponding orbit prescriptions. It therefore has at least two internal switches, and its positive odd projective grade is at least three. There is no grade-one cycle within that radius, proving (AT8). \(\square\)

**Corollary (balanced one-eighth-dimension trap).** For every sufficiently large m there exists a perfectly vertex-balanced legal antipodally odd coloring of \(Q_N\), \(N=8m\), with full binary direction-profile support, monochromatic full geodesics, and a single-defect projective cycle C^+ for which
\[
\boxed{d_\square(C^+,\mathcal G_1)\ge m=N/8.}\tag{AT12}
\]

*Proof.* Apply the complementary paired lift to the coloring c of the theorem. Each old/new direction pair contributes one incident edge of each color, establishing balance. The established profile-cylinder identity (SM3) preserves full profile support. Lift the singleton-defect full geodesic by inserting each new direction \(n+i\) before it if \(c_i(x)=1\) at the old root x, or after it if \(c_i(x)=0\). Both choices give a zero-colored new edge because the new rule is \(1+c_i\) and c is antipodally odd. The lifted cycle therefore still has one defect and projects onto C.

Projection of a lifted projective cycle to the old directions is a projective full cycle of c. Adjacent square exchange projects to at most one old adjacent square exchange (zero if one exchanged direction is new). A one-turn lifted cycle admits a monochromatic representative, which projects to a monochromatic full old geodesic and hence an old one-turn cycle. Thus its gallery distance from the lifted initial cycle is at least the old distance \(m\). \(\square\)

**Interpretation.** The three-direction anchor method (AT3)--(AT6) is strengthened to a deterministic quarter-dimension distance barrier, without probabilistic smoothing: the unary star (AT9) retains n-2 free initial bits for every target profile, enough to avoid all altered orbits in two marked direction classes. The balanced lift retains a one-eighth-dimension obstruction. Thus even a singleton-defect projective cycle in a completely profile-universal, vertex-balanced and globally successful legal coloring can lie linearly far from all one-turn cycles. This does not rule out a closure argument that chooses a specially extremized witness or performs exchanges beyond adjacent direction swaps.


### Lipschitz variation under exchanges and an unbounded root seam

The twisted cyclic-variation invariant \(D\) of the preceding subsection depends only on the canonical flag-rotation orbit, not on the root selected within the orbit. Its behavior under individual Coxeter rank exchanges makes the key distinction between the two motivating geometries precise: exchanges preserving the starting cube root are local in \(D\), but the exchange changing that root can alter \(D\) by an amount linear in dimension.

For an antipodally odd cube-edge coloring, set
\[
D(x,\pi)=\sum_{j=1}^{n-1}\mathbf1_{\{w_j\ne w_{j+1}\}}
+\mathbf1_{\{w_n=w_1\}},
\tag{1}
\]
where \(w\) is the full-geodesic edge-color word. The last summand is the comparison of \(w_n\) with the complement of \(w_1\). The total \(D\) is odd and unchanged by the flag rotation \(T\).

For an ordinary boundary tournament and a cyclic ordering \(\pi=(v_0,\ldots,v_{n-1})\), put \(a_j=b(v_j,v_{j+1},v_{j+2})\) with cyclic indices and
\[
D_{\rm bdry}(\pi)=\sum_{j\in\mathbb Z/n\mathbb Z}
\mathbf1_{\{a_j\ne a_{j+1}\}}.
\tag{2}
\]
It is even and invariant under cyclic rotation and reversal of the vertex order.

**Theorem 1 (local rank-exchange bounds).**
(a) Exchanging two consecutive dimensions in a cube geodesic while retaining its root changes the cyclic invariant (1) by at most two:
\[
\boxed{|D(x,\pi)-D(x,\pi\circ s_i)|\le2,\qquad 1\le i<n.}
\tag{3}
\]
(b) Exchanging two consecutive vertices of a boundary cyclic order changes (2) by at most four:
\[
\boxed{|D_{\rm bdry}(\pi)-D_{\rm bdry}(\pi\circ s_i)|\le4.}
\tag{4}
\]

*Proof.* For (a), a transposition of adjacent dimensions affects only the corresponding two consecutive original cube edges: the root and all earlier edges agree, and after both exchanged steps the paths arrive at the same cube vertex and follow the same suffix. Thus the two binary \(n\)-words differ in at most two consecutive positions. Only the three comparisons meeting this pair can change, counting the antipodal closing comparison as cyclic. Since both total comparison counts are odd, their difference is even, so it has magnitude at most two.

For (b), switching two adjacent elements of a cyclic vertex order changes only those cyclic triples containing either exchanged element. There are four possible starting positions, consecutive around the cyclic index set. Only the five comparisons incident with these four entries can change. Both cyclic variation counts are even, so their difference is even and hence has magnitude at most four. \(\square\)

**Theorem 2 (sharp linear obstruction at the cube root flip).** For every \(n\ge3\) there is an antipodally odd undirected-edge coloring of \(Q_n\) and two *adjacent type-B Coxeter chambers*
\[
g=(0;1,2,\ldots,n),\qquad
h=(e_1;1,2,\ldots,n)
\tag{5}
\]
whose root-slide orbits have cyclic variation values
\[
\boxed{
D(g)=1,\qquad
D(h)=
\begin{cases}
n,&n\text{ odd},\\
n-1,&n\text{ even}.
\end{cases}}
\tag{6}
\]
The difference is \(n-1\) for odd \(n\) and \(n-2\) for even \(n\), the largest difference compatible with odd cyclic-variation parity. In particular, no dimension-independent Lipschitz bound on \(D\) holds over all adjacent type-B chamber pairs.

*Proof.* Let \(A\) be the complete geodesic from \(0\) using dimensions \(1,2,\ldots,n\), and let \(B\) be the complete geodesic from \(e_1\) using the same dimension order. The initial undirected edge of both is \(\{0,e_1\}\). For each \(j\ge2\), the dimension-\(j\) edge of \(A\) lies in the face \(x_1=1\), while that of \(B\) lies in \(x_1=0\), so the two edges differ. Neither is the antipodal image of the other: since \(n\ge3\), choose a dimension \(k\notin\{1,j\}\). At their \(j\)-th edges, paths \(A\) and \(B\) have the same bit \(x_k\), whereas antipodal edges must have opposite bits \(x_k\). The pairs of paths therefore have no common antipodal edge orbit except their shared initial edge. Distinct positions also have different edge dimensions, so no additional antipodal orbit coincidences arise.

We may consequently prescribe the colors of all edges of \(A\) to be zero and prescribe the colors of the \(j\)-th edges of \(B\) to be \(j-1\bmod2\). The prescriptions agree on the common initial edge and have no conflicts with antipodal oddness. Extend the coloring arbitrarily to the remaining antipodal edge orbits. Then
\[
w(A)=0^n,\qquad
w(B)=(0,1,0,1,\ldots).
\]
The antiperiodic cyclic comparison count of \(0^n\) is one. The alternating word has a change at every internal comparison. Its twisted closing comparison is one for odd \(n\) and zero for even \(n\), yielding (6). Since the chambers differ only by the type-B rank-zero flip across their shared initial edge, they are adjacent. \(\square\)

**Consequences for a common proof.** The exchange bounds (3)–(4) suggest minimizing \(D\) on the graph of rotation orbits rather than on all rooted flags. But Theorem 2 isolates an obstruction specific to gluing the cube's fixed-root type-A fibers: the single rank-zero exchange can leap from an orbit with a monochromatic geodesic to an orbit whose every root-slide has nearly the largest possible switch count. Therefore a proof that treats every adjacent flag exchange as a bounded local energy perturbation cannot work. The missing mechanism must correlate the many root-changing exchanges globally, or use a topological chain construction whose cancellations do not rely on local variation monotonicity.

##### Prismatic vertex figures and triangle-square port transport

The two rectified carriers from this Article have identical vertex figures in equal dimension. Their polygonal two-faces distinguish the two coloring geometries, while products of simplices provide a common triangle-square transport law and a complete-path shift formula.

**Theorem 1 (prismatic vertex figures).** Let \(d\ge3\). Every vertex figure of the midpoint rectification \(R_d\) of the \(d\)-cube and of the hypersimplex \(H_d=\Delta(2,d+1)\) is
\[
\boxed{\Delta^{d-2}\times\Delta^1.}\tag{1}
\]
Its vertices form two \((d-1)\)-element cliques connected by a perfect matching.

*Proof.* In \(R_d=[-1,1]^d\cap\{z:\sum_i|z_i|\le d-1\}\), choose the edge-midpoint vertex \(v=(0,1,\ldots,1)\). In its tangent cone put \(t=z_1\), \(u_j=1-z_j\) for \(j\ge2\). The inequalities near \(v\) are \(u_j\ge0\), \(|t|\le\sum_{j\ge2}u_j\). The cone section \(\sum_{j\ge2}u_j=1\) is the product of the simplex \(\{u\ge0,\sum u=1\}\) and \([-1,1]\).

For the hypersimplex, at its vertex \(e_a+e_b\), write \(z_a=1-\alpha\), \(z_b=1-\beta\), \(z_c=u_c\) for \(c\notin\{a,b\}\). The tangent inequalities are \(\alpha,\beta,u_c\ge0\) and \(\alpha+\beta=\sum_cu_c\). Intersecting with \(\sum_cu_c=1\) gives a simplex on the \(d-1\) remaining symbols times the segment \(\alpha+\beta=1\). These sections give the two vertex figures. \(\square\)

**Theorem 2 (polygon types encoded on the prism).** In the vertex figure (1), edges within either simplex layer correspond to triangular two-faces in both rectifications. The matching edges correspond to quadrilateral two-faces in \(R_d\), and triangular two-faces in \(H_d\).

*Proof.* The \(2(d-1)\) neighbors of a rectified-cube vertex representing a cube edge \(uv\) are the other \(d-1\) edges at \(u\) and at \(v\). Two from the same endpoint together with \(uv\) form a triangle inside the simplex obtained by rectifying that cube vertex. The matched pair from the two endpoints, in another cube dimension \(j\), lies with \(uv\) in the rectified square face spanning these two dimensions. For \(H_d\), a vertex \(\{a,b\}\) has neighbors \(\{a,c\}\) and \(\{b,c\}\). Within-layer neighbor pairs form triangles in the simplex face fixing \(a\) or \(b\); the matched pair \(\{a,c\},\{b,c\}\), together with \(\{a,b\}\), also forms a triangle. Every two-face of \(\Delta(2,d+1)\) is triangular, since fixing facet entries to zero or one until three entries remain produces a two-dimensional hypersimplex on three symbols. \(\square\)

###### Canonical transport through triangles and induced squares

Put \(P=\prod_{i=1}^r\Delta^{q_i-1}\), \(q_i\ge2\), of dimension \(d=\sum_i(q_i-1)\). Its graph is the Cartesian product \(G(P)=\square_i K_{q_i}\).

**Theorem 3 (port matching).** Every oriented edge \(xy\) of \(G(P)\) carries a canonical bijection
\[
\boxed{\Theta_{xy}:N(x)\setminus\{y\}\longrightarrow N(y)\setminus\{x\}.}\tag{2}
\]
If \(xy\) changes factor \(i\) from symbol \(a\) to symbol \(b\), the matching is given by:
(i) a neighbor \(z\) of \(x\) obtained by changing factor \(i\) from \(a\) to \(c\notin\{a,b\}\) matches \(z\) itself, closing a triangle \(xyz\);
(ii) a neighbor \(z\) obtained by changing another factor \(j\) matches the vertex obtained from \(y\) by making that same change of factor \(j\), closing an induced square. These are respectively \(q_i-2\) triangle pairs and \(d-q_i+1\) square pairs. Also \(\Theta_{yx}=\Theta_{xy}^{-1}\).

*Proof.* Every graph neighbor changes one factor. When that factor is \(i\), the new symbol \(c\) is also adjacent to \(b\), producing the stated triangle. When it is \(j\ne i\), changes in factors \(i,j\) commute, giving the unique opposite corner of their Cartesian square. Both assignments reverse upon interchanging \(x,y\), and exhaust the \(d-1\) outgoing edges other than \(xy\). Their cardinalities are the stated counts. \(\square\)

A product of segments has only square pairs; a single simplex has only triangle pairs. Mixed products have both types, providing one intrinsic family for the two local exchange laws.

###### Full-path dynamics in the same family

Every complete face-graded path in \(P\) corresponds to a cyclic listing \(A_i=(a_{i,0},\ldots,a_{i,q_i-1})\) of all symbols of each factor, and an interleaving word \(\sigma\) containing symbol \(i\) precisely \(q_i-1\) times. Starting with symbol \(a_{i,0}\) in each factor, its successive occurrences in \(\sigma\) advance along the corresponding \(A_i\). This is the product-flag factorization proved earlier in this Article.

**Theorem 4 (rotor description of the Petrie shift).** If \(\sigma=i\sigma'\), the universal full-path rank-flip shift satisfies
\[
\boxed{T(A_1,\ldots,A_r;i\sigma')
=(A_1,\ldots,\operatorname{rot}(A_i),\ldots,A_r;\sigma'i).}\tag{3}
\]
Let \(N_i(t)\) count symbol \(i\) in the first \(t\) letters of the periodic repetition of \(\sigma\). Then \(T^t\) rotates \(\sigma\) by \(t\) positions and \(A_i\) by \(N_i(t)\) positions. If \(p\) is the least positive rotation period of \(\sigma\), and \(m_i\) counts symbol \(i\) in its first \(p\) positions, then
\[
\boxed{|\mathrm{Orb}_T|=p\,\mathrm{lcm}_{1\le i\le r}
\left(\frac{q_i}{\gcd(q_i,m_i)}\right).}\tag{4}
\]
For a simplex this yields its Hamilton-order rotation period \(q_1\); for a \(d\)-cube it yields the full antipodal root-slide period \(2d\).

*Proof.* Dropping the first move of \(\sigma\) advances the root one step in factor \(i\). It leaves the remaining \(d-1\) moves in the original order. Rotating \(A_i\) makes the former initial factor symbol the new last symbol, supplying the one additional final step. This gives a complete face-graded walk with the required common suffix; uniqueness of the rank-flip shift proves (3). Iteration proves the count \(N_i(t)\). Returning to the same shuffle requires \(t=kp\); it then rotates \(A_i\) by \(km_i\) positions. All factor lists return precisely when \(q_i\mid km_i\) for every \(i\), whose least positive solution is \(k=\mathrm{lcm}_i(q_i/\gcd(q_i,m_i))\). \(\square\)

**Mathematical scope.** The common prism links, triangle-square port matching, and skew-product shift hold throughout the product-of-simplices family and preserve the original complete-path witnesses at its two extremes. The opposing color fields still have different observational degrees: unrestricted cube edge colors are antipodally odd vertex fields on a rectification, whereas unrestricted boundary triples are arbitrary reversal-odd oriented-edge fields. Theorem 2 shows why polygon lengths and incidence descent must remain visible in a color-sensitive argument. No mixed-product one-switch assertion is established here. The permutahedral counterexamples in this Article rule out promoting the local prismatic geometry alone to a universal one-switch condition.

**Proposition 5 (universal polygonal port matching).** Let \(P\) be any simple convex \(d\)-polytope, \(d\ge2\), with graph \(G\). Every oriented edge \(xy\) admits a canonical bijection \(\Theta_{xy}:N(x)\setminus\{y\}\to N(y)\setminus\{x\}\): for an edge \(xz\ne xy\), take the unique two-face \(F\) containing both \(xy\) and \(xz\), and let \(\Theta_{xy}(z)\) be the other neighbor of \(y\) on the boundary of \(F\). These maps are inverse under reversal. The corresponding polygonal residue has three vertices precisely when \(z=\Theta_{xy}(z)\), four precisely when \(x,z,\Theta_{xy}(z),y\) form an induced square, and otherwise five or more vertices.

*Proof.* The vertex figure of a simple \(d\)-polytope is a \((d-1)\)-simplex. Its edges correspond bijectively to the two-faces containing a given pair of incident original edges. In particular the \(d-1\) other edges at \(x\) correspond bijectively to the \(d-1\) two-faces containing \(xy\). The same two-faces correspond to the \(d-1\) other edges at \(y\), yielding the bijection and its reversal law. The polygon lengths give the final assertions. \(\square\)

Theorem 3 is the triangle-square specialization of Proposition 5. **In particular, the existence of a prismatic port matching alone does not exclude the permutahedral counterexamples from this Article:** they have the same local matching mechanism, with longer polygonal residues. This identifies the two-face length decoration, rather than the bare port matching, as necessary information for any strengthening along this route.
