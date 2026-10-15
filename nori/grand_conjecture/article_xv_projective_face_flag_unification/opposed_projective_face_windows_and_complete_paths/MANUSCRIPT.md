## Projective Face Flags and Intrinsic Monodromy

### Introduction: one-switch paths through opposed face flags

#### The mathematical objective

Two unresolved problems motivate a common intrinsic path-selection problem. The proposed extension to all opposed projective-window systems is refuted below by centrally symmetric permutahedral counterexamples.

**NORI1.** Color every undirected edge of the \(d\)-cube \(Q_d\) by an arbitrary binary function \(c\) satisfying \(c(\bar e)=1-c(e)\), where the bar complements all vertex bits. Conjecturally a full antipodal geodesic, traversing each dimension once, is monochromatic. A path of length \(d\) with at most one color change already suffices: sliding its root past the unique switch uses the antipodal oddness to produce a monochromatic full geodesic. The root and dimension order must both remain unrestricted.

**Ordinary boundary 3-tournaments.** Let \(V\) have \(d+1\) vertices and let \(b(a,h,c)\in\mathbb F_2\) be specified independently for every ordered triple of distinct vertices, subject only to \(b(c,h,a)=1-b(a,h,c)\). Conjecturally there is a permutation \(v_0,\ldots,v_d\) of *all* the vertices whose consecutive triple word \(b(v_0,v_1,v_2),\ldots,b(v_{d-2},v_{d-1},v_d)\) has at most one switch.

Neither a short nonspanning path nor an arbitrary path in an auxiliary state graph is an adequate witness. An earlier Coxeter-coset reformulation in Article XIV recovers both problems but its conjecture explicitly chooses the type-A and type-B cases; it therefore does not identify the desired common structural hypotheses.

#### Complete paths from faces

A simple \(d\)-dimensional convex polytope \(P\) has maximal proper face flags \(F_0\subset\cdots\subset F_{d-1}\subset P\), with \(\dim F_i=i\). Starting at \(v_0=F_0\), traverse at rank \(i\) the unique edge of \(F_i\) that leaves \(F_{i-1}\) at \(v_{i-1}\). This constructs a canonical path \(v_0,\ldots,v_d\). Its successive displacement vectors are linearly independent: the first \(i+1\) vertices affinely span \(F_i\). Conversely every such face-graded basis path reconstructs its maximal flag.

For a simplex, these are all Hamilton vertex orderings. For a cube, these are all freely rooted full antipodal geodesics. In every simple polytope, complete-path witnesses are therefore encoded by the maximal simplices of the barycentrically subdivided boundary sphere. This is the essential dimension-simplicity condition required in a chain-level proof.

#### Intrinsic observations of one or two steps

For an edge \(E=uv\), define the first-order observation \(\Xi_1=(E,[v-u])\), where \([a]=\mathbb Ra\) is an unoriented vector line.

For a nonbacktracking two-edge walk \(u,v,w\), its edges lie in one two-dimensional face \(F(u,v,w)\) of a simple polytope. Define its second-order *projective face observation*
\[
\boxed{\Xi_2(u,v,w)=\bigl(F(u,v,w),[v-u],[w-v]\bigr).}
\]
Let \(\mathscr I_k(P)\) be the set of such observations, \(k=1,2\). A coloring \(c:\mathscr I_k(P)\to\mathbb F_2\) descends to the specified local incidence: observations representing the same face and ordered unoriented directions share one color. A maximal face flag \(\mathcal F\) yields an observation word \(\mathsf w_k(\mathcal F)\) of length \(d+1-k\).

For cubes at \(k=1\), this is the entire unrestricted undirected-edge coloring problem. For simplices at \(k=2\), an ordered triple \((a,h,c)\) is recovered from its supporting triangular face and its two ordered edge direction lines; reversing the triple exchanges the lines. This retains every ordinary reversal-odd tournament coloring, not merely cyclically symmetric or globally representable subclasses.

#### Opposition and the proposed common conjecture

Call \((P,k,J,\rho)\) an *opposed projective-window system* when \(P\) is a simple \(d\)-polytope, \(k\in\{1,2\}\), \(J\) is a free simplicial involution of the proper-face flag sphere, and \(\rho\) is a fixed-point-free involution of \(\mathscr I_k(P)\) such that the observation word on \(J\mathcal F\) is obtained from that on \(\mathcal F\) by applying \(\rho\) to every incidence, with either the original order of positions or its reversal. In particular, a \(\rho\)-odd coloring, \(c(\rho I)=1-c(I)\), has a complementary word on opposite flags, possibly reversed.

**Original opposed-window one-switch assertion (refuted).** Every such system with \(d\ge k\), and every \(\rho\)-odd coloring of its projective local incidences, admits a maximal face flag \(\mathcal F\) satisfying
\[
\boxed{\operatorname{sw}\bigl(\mathsf w_k(\mathcal F)\bigr)\le1.}
\]

For cube one-edge data, choose geometric central inversion for \(J\) and for \(\rho\) on edges. For simplex two-edge data, choose complement of proper nonempty vertex subsets for \(J\) and turn reversal for \(\rho\). These specializations recover both targets without mentioning either reflection family in the hypotheses. The enlarged assertion fails on other opposed systems.

**Status and proof obligations.** The face-flag path theorem, projective-incidence encoding, rank-flip rotation, and these two specializations are proved and developed in subsequent subsections. The universal one-switch assertion is false. The subsection “Centrally symmetric permutahedral counterexamples to the opposed-window conjecture” proves that for every \(d\ge5\) with \(d\equiv1,2\pmod4\), an opposed system satisfying all the stated hypotheses has \(d-2\) switches on every complete path. Its coloring descends to projective two-face observations. The original NORI1 and boundary-tournament targets remain open; a revised common statement requires further intrinsic hypotheses. Mere antipodality, a spherical flag carrier, and path-basis completeness are individually insufficient. In particular, changing colors on different paths representing the same projective two-face observation admits alternating-parity obstructions, so local incidence descent cannot be omitted.

The remaining proof search seeks an adaptation of the Wu–Yang chain-level Borsuk–Ulam obstruction from general monochromatic antipodal paths to complete face-flag paths. The obstacle is constructing equivariant color-sensitive fillings over rank exchanges while retaining both full-path decoding and the local observation identifications. This article tests that obstruction directly.

### Simple-polytope flags and complete basis paths

Let \(P\subset\mathbb R^d\) be a full-dimensional simple convex polytope. A maximal face flag is \(F_0\subset F_1\subset\cdots\subset F_d=P\), where \(\dim F_j=j\). Put \(v_0=F_0\). For \(j\ge1\), define \(v_j\) as the other endpoint of the unique edge incident with \(v_{j-1}\) that lies in \(F_j\) and leaves \(F_{j-1}\).

**Theorem 1 (complete paths from flags).** The construction produces a vertex-simple \(d\)-edge walk \(v_0,\ldots,v_d\) satisfying
\[
\operatorname{aff}\{v_0,\ldots,v_j\}=\operatorname{aff}F_j.
\]
Its displacement vectors form a basis of \(\mathbb R^d\). Moreover, the correspondence is a bijection between maximal face flags and *face-graded basis paths*, namely graph paths whose first \(j+1\) vertices lie in a \(j\)-face and whose displacements are linearly independent.

*Proof.* Each face \(F_j\) is a simple \(j\)-polytope and \(F_{j-1}\) its facet. At the vertex \(v_{j-1}\) there are \(j\) incident edges within \(F_j\), of which \(j-1\) lie in \(F_{j-1}\). The remaining edge exists uniquely and ends at \(v_j\notin F_{j-1}\). Induction proves the asserted affine spans and the independence of moves. Conversely, the \(j+1\) affinely independent prefix vertices determine a unique containing \(j\)-face: distinct faces of dimension \(j\) intersect in lower dimension. These faces give the flag and its exiting-edge rule recovers the original walk. \(\square\)

**Corollary 2 (two natural cases).** When \(P\) is a \(d\)-simplex, each maximal flag inserts one previously unused vertex, and the induced walk is an arbitrary Hamilton ordering of all \(d+1\) vertices. When \(P=[0,1]^d\), each flag starts at an arbitrary vertex \(x\), frees one previously fixed dimension at every step, and induces the antipodal geodesic from \(x\) to \(\bar x\) traversing all \(d\) dimensions. Every witness in either original class corresponds to a flag. Thus vertex-simpleness and dimension-simpleness are both enforced intrinsically by the same face-graded basis condition.

**Theorem 3 (spherical face-flag carriers).** The order complex of the nonempty proper faces of \(P\) is the barycentric subdivision of \(\partial P\), hence a sphere \(S^{d-1}\). Its maximal simplices are face flags and consequently encode complete basis paths whenever \(P\) is simple. For cubes, central inversion of faces acts antipodally on this sphere. For simplices, face complementation \(S\mapsto V\setminus S\) defines a free simplicial antipodal involution of the type-A Coxeter sphere.

*Proof.* The proper-face order complex is the barycentric subdivision by definition. In a simplex with vertex set \(V\), map each proper nonempty face \(S\) to the ray spanned by
\[
z_S=\mathbf1_S-\frac{|S|}{|V|}\mathbf1
\]
in \(W=\{z:\sum_{v\in V}z_v=0\}\). Chains of subsets yield the standard braid-arrangement triangulation of \(S(W)\). Since \(z_{V\setminus S}=-z_S\), complementation is antipodal. The cube assertion follows from central symmetry of its boundary. \(\square\)

This unified geometric carrier applies to every simple polytope, including products of simplices and permutahedra. It builds maximal-path completeness into the top-dimensional simplices and supplies the same kind of sphere used by chain-level obstruction arguments.

**Open selection problem.** The boundary coloring lives on ordered two-step path windows and is odd under reversal; the cube coloring lives on undirected one-step windows and is odd under central antipodality. A common color-sensitive conjecture needs intrinsic local incidence descent and suitable opposition on the flag observations. Theorems 1–3 settle the common path geometry, without claiming a one-switch color selection theorem.

### Projective face windows and intrinsic flag monodromy

Let \(P\subset\mathbb R^d\) be a simple convex polytope. For a nonbacktracking two-edge graph walk \(u,v,w\), the two incident edges at \(v\) lie in a unique two-dimensional face \(F(u,v,w)\). Let \([a]=\mathbb Ra\) be the unoriented line of a nonzero vector \(a\). Define the intrinsic incidence sets
\[
\mathscr I_1(P)=\{(E,[v-u]):E=uv\text{ an edge of }P\},
\tag{1}
\]
\[
\mathscr I_2(P)=\{
(F(u,v,w),[v-u],[w-v]):u,v,w\text{ nonbacktracking graph walk}
\}.
\tag{2}
\]
The order of the two direction lines in (2) is retained. Multiple two-edge walks can give one member of \(\mathscr I_2(P)\). For a maximal face flag \(\mathcal F\), its canonical complete basis walk \(v_0,\ldots,v_d\) supplies the color word
\[
\mathsf w_k(\mathcal F)=
\bigl(c(\Xi_k(v_j,\ldots,v_{j+k}))\bigr)_{j=0}^{d-k},
\qquad c:\mathscr I_k(P)\to\mathbb F_2,\quad k\in\{1,2\}.
\tag{3}
\]

**Theorem 1 (faithful local-incidence realization).**
(a) For the \(d\)-cube \(P=[0,1]^d\) and \(k=1\), (1) is canonically the undirected edge set, and (3) runs through all full antipodal geodesic edge-color words as the maximal flag varies. Under central inversion, \((E,[v-u])\) maps to its opposite edge with the same direction line. Thus all odd incidence colorings are the unrestricted NORI1 colorings.

(b) For a \(d\)-simplex with vertices \(e_a\), \(a\in V\), \(|V|=d+1\), and \(k=2\), the correspondence
\[
\boxed{(a,h,c)\longmapsto
(\operatorname{conv}\{e_a,e_h,e_c\},[e_h-e_a],[e_c-e_h])}
\tag{4}
\]
is a bijection between ordered triples of distinct vertices and \(\mathscr I_2(P)\). The words (3) are all Hamilton tight-path triple words. The natural incidence involution
\[
\rho(F,L_1,L_2)=(F,L_2,L_1)
\tag{5}
\]
corresponds to triple reversal. Thus every binary coloring odd under (5) is an arbitrary ordinary reversal-odd boundary 3-tournament.

*Proof.* For the cube, an edge and its direction line determine an undirected edge, and a maximal face flag selects every dimension once from an arbitrary root. For the simplex, distinct edges have distinct unoriented direction lines. Two edges of one triangular face share a unique middle vertex, and the order of their lines specifies the first and last vertex. This reconstructs the triple from (4); reversing the triple interchanges its two lines. Every Hamilton vertex ordering is the canonical walk of a maximal face flag. \(\square\)

**Theorem 2 (intrinsic flag rotation).** For every simple \(d\)-polytope, let \(r_j\), \(0\le j<d\), change only the \(j\)-face of a maximal flag to the other \(j\)-face between its adjacent ranks, using the bottom and top elements as usual. These operations are involutions satisfying
\[
r_ir_j=r_jr_i\quad(|i-j|\ge2).
\tag{6}
\]
Their product \(T=r_0r_1\cdots r_{d-1}\), acting successively on the right, has the following effects:
\[
\begin{aligned}
\text{simplex: }&(v_0,\ldots,v_d)\longmapsto(v_1,\ldots,v_d,v_0),\\
\text{cube: }&(x;i_1,\ldots,i_d)\longmapsto
(x\oplus e_{i_1};i_2,\ldots,i_d,i_1).
\end{aligned}
\tag{7}
\]

*Proof.* Thinness of rank-two intervals in a convex face lattice gives a unique alternative intermediate face at each rank, and changes at nonadjacent ranks commute. For a simplex, \(r_j\) exchanges the entries in positions \(j,j+1\) of its vertex order, hence the product rotates the first entry to the end. For the cube, \(r_0\) moves the root across the first edge, while \(r_j\) for \(j\ge1\) swaps the \(j\)-th and \((j+1)\)-st freed dimensions. Their successive application gives (7). \(\square\)

The previously specified Coxeter-parabolic stabilizers now arise from the incidence definitions: a simplex's first oriented two-edge observation is invariant under \(r_j\) for \(j\ge3\), while a cube's first undirected edge observation is invariant under \(r_0\) and \(r_j\) for \(j\ge2\). The common flag rotation is a product of canonical rank exchanges, independent of the reflection type.

**Opposition covariance and the proposed extension.** On the simplex's proper-face flag sphere, the complement involution reverses each maximal flag order and turns (4) into its reverse; the color word becomes complemented and reversed. On the cube's flag sphere, central inversion preserves the dimension order while complementing every edge color. More generally, call \((P,k,J,\rho)\) an *opposed projective-window system* when \(P\) is simple, \(k\in\{1,2\}\), \(J\) is a free involution of its flag sphere, \(\rho\) a free involution on \(\mathscr I_k(P)\), and applying \(J\) to a flag transforms its ordered windows by \(\rho\) with a fixed identity or reversed position order.

**Original unified assertion (refuted by the permutahedral construction below).** In every opposed projective-window system, every binary coloring \(c:\mathscr I_k(P)\to\mathbb F_2\) satisfying \(c(\rho I)=1-c(I)\) has a maximal face flag \(\mathcal F\) with
\[
\operatorname{sw}(\mathsf w_k(\mathcal F))\le1.
\tag{8}
\]
Theorem 1 shows that (8) would imply both unrestricted motivating conjectures, with no specific reflection group in its hypotheses. It also contains other simple polytopes, including centrally symmetric products and permutahedra when their incidence opposition is free. Theorem 2 gives a common exchange structure. The universal assertion (8) is false: the subsequent permutahedral counterexample theorem constructs opposed systems in arbitrarily large dimensions whose every complete path has an alternating observation word. The face-flag geometry and the two faithful specializations remain valid. A revised universal theorem requires an additional intrinsic condition.

### Universal Petrie shift on maximal face flags

A maximal face flag of a simple polytope defines a complete affine-basis walk. Its rank-flip product has a stronger universal property than the individual cube and simplex formulas: **it shifts the canonical walk forward by one edge**. This supplies the common transport identity needed for a cyclic variation or topological proof.

Let \(P\) be a simple convex \(d\)-polytope with flag
\[
\mathcal F:\quad F_0\subset F_1\subset\cdots\subset F_d=P,\qquad \dim F_i=i,
\]
and let \(v_0,\ldots,v_d\) be its canonical basis path. Let \(r_i\) exchange the \(i\)-face in a maximal flag with the other \(i\)-face in its rank-two interval, \(0\le i\le d-1\). Write \(T=r_0r_1\cdots r_{d-1}\), meaning successive application of the indicated flips.

**Theorem 1 (universal one-step flag transport).** The canonical path of \(T\mathcal F\) begins with
\[
\boxed{\quad v_1,v_2,\ldots,v_d.\quad}
\tag{1}
\]
It has one additional last vertex \(v_{d+1}\), uniquely determined by its final face flag. More precisely, after applying \(r_0,\ldots,r_j\) to \(\mathcal F\), the newly selected \(i\)-face for every \(i\le j\) is the unique \(i\)-face \(G_i\) satisfying
\[
v_1,\ldots,v_{i+1}\in G_i,
\quad
\operatorname{aff}G_i=\operatorname{aff}\{v_1,\ldots,v_{i+1}\},
\tag{2}
\]
while the faces of rank above \(j\) remain unchanged.

*Proof.* For \(j=0\), \(r_0\) changes \(F_0=\{v_0\}\) to the other endpoint \(v_1\) of \(F_1\); thus \(G_0=\{v_1\}\). Assume the assertion through rank \(j-1\). Then the intermediate flag contains
\[
G_{j-1}\subset F_j\subset F_{j+1},
\]
with \(v_1,\ldots,v_j\in G_{j-1}\) and \(v_{j+1}\in F_{j+1}\setminus F_j\). At the vertex \(v_j\in G_{j-1}\), the path edge \(v_jv_{j+1}\) lies in \(F_{j+1}\) and leaves its facet \(F_j\). Inside the simple \((j+1)\)-face \(F_{j+1}\), there are precisely two \(j\)-faces containing the \((j-1)\)-face \(G_{j-1}\): one is \(F_j\), and the other \(G_j\) contains the edge \(v_jv_{j+1}\). Thus \(G_j\) contains all the previously selected vertices \(v_1,\ldots,v_j\) and also \(v_{j+1}\). Since these \(j+1\) vertices are affinely independent, they span \(G_j\). Applying \(r_j\) replaces \(F_j\) by \(G_j\), proving the induction.

After all flips, the flag begins \(G_0\subset\cdots\subset G_{d-1}\subset P\). Its canonical path must follow \(v_1\to v_2\to\cdots\to v_d\): at each rank, the next listed vertex is on the unique edge exiting the preceding face. This proves (1). \(\square\)

**Corollary 2 (universal local-word shift).** Let \(k\in\{1,2\}\), let \(c:\mathscr I_k(P)\to\mathbb F_2\) be any coloring, and set \(m=d+1-k\). For the projective-incidence word
\[
\mathsf w_k(\mathcal F)=(w_0,w_1,\ldots,w_{m-1})
\]
one has
\[
\boxed{\quad
\mathsf w_k(T\mathcal F)
=(w_1,w_2,\ldots,w_{m-1},w_{\rm new}).
\quad}
\tag{3}
\]
No symmetry or parity hypothesis on the coloring is required.

*Proof.* The two canonical walks share the \(d\)-edge tail \(v_1,\ldots,v_d\) by Theorem 1; therefore their \(k\)-step observations agree on each of the first \(m-1\) overlapping windows. The last window in \(T\mathcal F\) is new. \(\square\)

**Corollary 3 (cyclic switch representation for all simple polytopes).** Fix a \(T\)-orbit of maximal flags of length \(L\). There is a cyclic binary sequence \(a_0,\ldots,a_{L-1}\) such that the color word of \(T^s\mathcal F\) is the consecutive \(m\)-term window
\[
(a_s,a_{s+1},\ldots,a_{s+m-1})
\tag{4}
\]
with indices modulo \(L\). Define the cyclic comparisons \(d_i=\mathbf1_{\{a_i\ne a_{i+1}\}}\) and \(D=\sum_{i=0}^{L-1}d_i\). Then
\[
\boxed{\quad
\min_{0\le s<L}\operatorname{sw}(\mathsf w_k(T^s\mathcal F))
=\min_s\sum_{j=0}^{m-2}d_{s+j}
\le \left\lfloor\frac{m-1}{L}D\right\rfloor.
\quad}
\tag{5}
\]

*Proof.* Repeated use of (3) constructs the sequence \(a_i\) and proves (4). The flag returns after \(L\) shifts, so the sequence is cyclic. Each comparison \(d_i\) occurs in precisely \(m-1\) of the \(L\) window switch sums, counted with multiplicity. Their average is \((m-1)D/L\); the minimum is at most its floor. \(\square\)

**Theorem 4 (specialization of opposition monodromy).** On the simplex, \(T\) cyclically shifts a Hamilton vertex order and has order \(d+1\) on each flag orbit. Complementation \(J\) of face subsets reverses the vertex order, so \(JTJ=T^{-1}\). On the cube, \(T\) is the one-step geodesic root slide; \(T^d\) is central complementation and \(T^{2d}=1\) on flags. Thus the original boundary periodic word and the NORI1 antiperiodic half-cycle word are instances of (4), with different relations between \(T\) and opposition.

*Proof.* The specializations of the rank-flip formula were established in the preceding Subsection. In the simplex, reversing a vertex permutation conjugates cyclic rotation to its inverse. In the cube, after \(d\) slides every dimension has been flipped once and the dimension order returns; after another \(d\) slides the original root returns. \(\square\)

**Research consequence.** The cyclic-rotation operation previously introduced separately for NORI1 and boundary tournaments is intrinsic to *every* simple-polytope flag geometry. This is stronger than merely arranging two classes in a common Coxeter notation. The remaining one-switch problem is to use antipodal odd projective-incidence color descent and interaction of different \(T\)-orbits to force a low-variation orbit. Equation (5) alone is insufficient: arbitrary cyclic binary sequences can have high variation.

### Exchange completeness and product factorization of flags

The universal one-step shift is not the only structure available in an arbitrary simple polytope. Its full face incidence gives a strong extension property for local paths, and products admit a factorization into independent full paths and shuffles.

Let \(P\) be a simple convex \(d\)-polytope and let \(\mathcal F(P)\) be its maximal face flags, identified with canonical affine-basis walks.

**Theorem 1 (any two incident edges extend to a complete flag).** Let \(d\ge2\). For every pair of distinct edges \(uv\), \(vw\) incident at a common vertex \(v\), there is a maximal face flag whose canonical walk begins
\[
\boxed{\quad u\longrightarrow v\longrightarrow w.\quad}
\tag{1}
\]
Thus every ordered nonbacktracking two-edge walk of \(G(P)\) occurs as the first two steps of a complete basis path.

*Proof.* At a vertex of a simple polytope, every pair of incident edges lies in a unique two-dimensional face \(F\). Start the desired flag with \(F_0=\{u\}\subset F_1=uv\subset F_2=F\). Since \(F\) is a polygon, its unique edge at \(v\) other than \(uv\) is \(vw\). Extend the partial face chain to a maximal chain through \(P\), which is possible in any finite graded face lattice. The canonical path begins with (1), as claimed. \(\square\)

**Corollary 2 (unconditional first-switch avoidance).** If \(d\ge3\), every binary coloring of the undirected edges of \(P\) has a complete face-flag path whose first two edges have the same color. No antipodal symmetry is needed.

*Proof.* At any vertex \(v\), there are \(d\ge3\) incident edges. Two have the same color by the pigeonhole principle. Order these edges as \(uv\), \(vw\) and apply Theorem 1. \(\square\)

When \(d=3\), the complete path has three edges, so its first two equal bits imply at most one switch over the entire path. Consequently every binary edge coloring of every simple three-dimensional polytope has a one-switch complete face-flag path, even in the absence of an opposition involution.

This local extension property is a structural distinction from a sparse cycle of affinely independent basis paths: in the full simple-polytope graph, all choices of two incident edges are realized by complete flags. It rules out globally alternating complete edge-color words, and is the elementary input behind stronger switch-selection attempts in higher ranks.

**Theorem 3 (factorization of complete flags in products).** Let \(P,Q\) be simple convex polytopes of dimensions \(p,q\). Maximal face flags of the \((p+q)\)-polytope \(P\times Q\) are in canonical bijection with triples
\[
\boxed{
(\mathcal F_P,\mathcal F_Q,\sigma),\qquad
\mathcal F_P\in\mathcal F(P),\quad
\mathcal F_Q\in\mathcal F(Q),
}
\tag{2}
\]
where \(\sigma\) is a shuffle of \(p\) symbols \(P\) and \(q\) symbols \(Q\), retaining the internal order within each factor. Under this correspondence, the canonical complete basis path of the product flag is the corresponding interleaving of the factor paths, moving in precisely one factor at each step.

*Proof.* Every nonempty face of \(P\times Q\) is \(A\times B\) with \(A\) a face of \(P\) and \(B\) a face of \(Q\), and its dimension is \(\dim A+\dim B\). In a maximal product flag, each rank increase raises the dimension of precisely one factor by one. Recording which factor increases gives the shuffle \(\sigma\); deleting repeated factor faces leaves independent maximal flags of \(P\) and \(Q\). Conversely, any two factor flags and a shuffle determine a maximal product flag by advancing the chosen factor at each rank.

An edge of the product is either an edge of \(P\) times a vertex of \(Q\), or vice versa. The unique edge leaving a product face \(A\times B\) in the next enlarged product face is the unique exiting edge in whichever factor advances, with the other factor's current vertex fixed. Thus the canonical product walk is the indicated interleaving. Its moves form a basis because the factor moves form bases of complementary direct-sum spaces. \(\square\)

**Corollary 4 (a natural enlarged geometric class).** If \(P,Q\) have central involutions mapping their face lattices freely, then \(P\times Q\) has the free central involution \((x,y)\mapsto(\tau_Px,\tau_Qy)\) on its flag sphere and an induced free involution on first-order edge incidences. Hence products of centrally symmetric simple polytopes supply opposed first-order projective-window systems. In particular, the conjecture covers arbitrary products of centrally symmetric polygons, segments, and other centrally symmetric simple factors, rather than being restricted to cubes.

*Proof.* The product of the central face automorphisms carries each proper face \(A\times B\) to \(\tau_P(A)\times\tau_Q(B)\). A nonempty proper face of a centrally symmetric full-dimensional polytope cannot equal its antipodal image: a supporting hyperplane of such a face lies strictly away from the central interior point, while its antipodal hyperplane has opposite support value. Thus no proper face is fixed; the induced flag action is free. The image of a proper edge under central inversion is another edge, never the same edge. The corresponding map on undirected first-order projective incidences is therefore free and transforms each complete flag's word by applying the incidence involution without changing its position order. \(\square\)

Theorem 3 explains why products are a serious test for the common conjecture: they have abundant complete basis paths formed by all shuffles, yet their face incidence is richer than either a single simplex or a cube. The one-switch existence assertion on arbitrary products with arbitrary odd colorings remains open.

### Polygonal rank-two monodromy and exchange seams

The universal flag shift \(T=r_0r_1\cdots r_{d-1}\) holds for every simple polytope. However, the local effect of a rank-one exchange depends on the size of the containing two-dimensional face. This is relevant to color-sensitive chain fillings.

Let \(P\) be a simple \(d\)-polytope, \(d\ge2\), and let \(\mathcal F\) be a maximal flag whose initial two-face \(F_2\) is a polygon with \(p\ge3\) vertices. Label its vertices cyclically \(u_0,u_1,\ldots,u_{p-1}\), such that the canonical complete path of \(\mathcal F\) begins \(u_0,u_1,u_2\).

**Theorem 1 (rank-one exchange and the square criterion).** Let \(r_1\) change only the first edge face \(F_1=u_0u_1\), retaining the initial root \(u_0\) and the containing two-face \(F_2\). The canonical path of \(r_1\mathcal F\) begins
\[
\boxed{\quad u_0,u_{p-1},u_{p-2}.\quad}
\tag{1}
\]
The two complete paths have a common vertex after their second steps if and only if \(p=4\). When \(p=4\), the two initial two-edge routes are the opposite routes across a quadrilateral and rejoin at \(u_2\), so their entire suffix from that vertex onward coincides.

*Proof.* Since \(F_2\) is a polygon, the two edges incident with \(u_0\) in \(F_2\) are \(u_0u_1\) and \(u_0u_{p-1}\). The flip \(r_1\) replaces the former by the latter. At the new first endpoint \(u_{p-1}\), the unique edge within \(F_2\) leaving \(u_0u_{p-1}\) is \(u_{p-1}u_{p-2}\); this gives (1). The second-step endpoints agree precisely when \(u_2=u_{p-2}\), namely \(p=4\). If the endpoints agree, the unchanged higher-rank faces and uniquely determined exiting edges give the same remaining suffix. \(\square\)

**Theorem 2 (polygonal rank-two monodromy).** Restrict attention to the rank-two residue of flags with a fixed first two-face \(F_2\). The product \(r_0r_1\) cyclically shifts the initial vertex and its directed boundary edge by one position, giving
\[
\boxed{\quad (r_0r_1)^p=1\quad}
\tag{2}
\]
on this residue, with least positive period \(p\).

*Proof.* The two flips affect only the initial vertex and edge. Applying \(r_0\) changes \(u_i\) to \(u_{i+1}\) along the selected edge \(u_iu_{i+1}\). Applying \(r_1\) then selects the other edge at \(u_{i+1}\) within \(F_2\), namely \(u_{i+1}u_{i+2}\). Thus each application advances the directed edge once around the polygon. It returns after \(p\) steps and no earlier. \(\square\)

**Corollary 3 (limitation of a direct square filling).** Any attempted chain map that glues two complete paths related by a single \(r_1\) exchange at their common endpoint after two steps, while preserving the remaining suffix, works on quadrilateral rank-two faces and fails on other polygonal rank-two faces. A common color-sensitive one-switch proof across arbitrary simple polytopes must therefore use the intrinsic polygonal dihedral monodromy (2), or a stronger global carrier, instead of identifying all rank-two exchanges with cubical commuting squares.

Triangles and squares appear here as the first two values of the natural parameter \(p\), not as alternative classes inserted into the conjecture. The mathematical task is to develop coherent equivariant chain fillings over all rank-two \(2p\)-flag residues that respect projective-incidence coloring and attach compatibly in higher-dimensional cells. Theorem 2 supplies the underlying residue cycles; the required color-sensitive chain assignment remains open.

### The universal Bockstein obstruction to equivariant rank-two fillings

Let \(X\) be a finite regular cell decomposition of \(S^m\), \(m\ge2\), with a free cellular involution \(J\), and let \(Y=X/J\). Let \(\alpha\in H^1(Y;\mathbb F_2)\) classify the double cover \(X\to Y\). This setup includes the dual face-flag spheres of the cube and simplex under their geometric opposition involutions.

**Theorem 1 (integral winding class).** Suppose that
\[
f:X^{(1)}\to S^1,\qquad f(Jx)=-f(x)
\tag{1}
\]
is an odd continuous map defined on the one-skeleton. Its quotient \(\bar f:Y^{(1)}\to\mathbb RP^1\cong S^1\) determines an integer cellular one-cochain \(u\) on \(Y\) whose modulo-two class on the one-skeleton is \(\alpha\). Define
\[
\boxed{\omega(D)=\frac{(\delta u)(D)}2\in\mathbb Z}
\tag{2}
\]
for each oriented two-cell \(D\) of \(Y\). Then \(\omega\) is an integral two-cocycle with
\[
\boxed{[\omega]=\beta(\alpha)\ne0\quad\text{in }H^2(Y;\mathbb Z),}
\tag{3}
\]
where \(\beta\) is the connecting homomorphism for \(0\to\mathbb Z\xrightarrow{\times2}\mathbb Z\to\mathbb F_2\to0\). The value \(\omega(D)\) is the winding number of the map (1) along the boundary of either lift of \(D\) in \(X\). In particular some dual two-cell has nonzero winding: no odd extension of (1) to all of \(X^{(2)}\) exists.

*Proof.* The double covering \(S^1\to\mathbb RP^1\) pulled back along \(\bar f\) is the restriction of \(X\to Y\) to the one-skeleton. Cellular approximation of \(\bar f\) on this graph gives an integral edge-degree one-cochain \(u\). Its reduction modulo two is the covering cocycle \(\alpha\) there. Since the latter extends as a cocycle on \(Y\), the integral coboundary \(\delta u\) is even on every two-cell. Hence (2) is integral, and \(\delta\omega=0\). The degree of \(\bar f\) on the attaching circle of \(D\) is \((\delta u)(D)\); it is twice the degree of its lift under \(f\) because the target map \(S^1\to\mathbb RP^1\) is a two-fold covering. This proves the winding assertion. The cochain construction of the integral Bockstein identifies \([\omega]\) with \(\beta(\alpha)\).

The sphere \(X\) is simply connected for \(m\ge2\), so \(\pi_1(Y)\cong\mathbb Z_2\). Therefore \(H^1(Y;\mathbb Z)=\operatorname{Hom}(\mathbb Z_2,\mathbb Z)=0\), whereas \(\alpha\ne0\). The Bockstein long sequence makes \(\beta\) injective at \(H^1(Y;\mathbb F_2)\); thus (3) is nonzero. If all two-cell windings vanished, \(\omega\) would be zero, contradicting (3). Changing target edge paths by additional full turns changes \(u\) by twice an integral one-cochain and changes \(\omega\) by its coboundary; the class (3) is unchanged. \(\square\)

**Theorem 2 (higher first-obstruction skeleton).** For every \(0\le k<m\), there is no odd continuous map
\[
\boxed{X^{(k+1)}\longrightarrow S^k.}
\tag{4}
\]
Thus an odd map already constructed on the \(k\)-skeleton must fail extension on some \((k+1)\)-cell.

*Proof.* The mod-two cohomology ring of the quotient of a sphere by a free involution is
\[
H^*(Y;\mathbb F_2)=\mathbb F_2[\alpha]/(\alpha^{m+1}).
\tag{5}
\]
This follows from the standard covering/Gysin sequence (or the classifying-space spectral sequence). In particular \(\alpha^{k+1}\ne0\). Restriction to \(Y^{(k+1)}\) retains this nonzero class: adding higher-dimensional cells can only impose further relations in degree \(k+1\). If (4) existed, it would yield a quotient map \(Y^{(k+1)}\to\mathbb RP^k\) pulling the universal double-cover class back to \(\alpha\). But the \((k+1)\)-st power of the class in \(H^1(\mathbb RP^k;\mathbb F_2)\) is zero, contrary to \(\alpha^{k+1}\ne0\). \(\square\)

**NORI1 application.** Suppose an antipodally odd cube-edge coloring had no monochromatic full antipodal geodesic. Then every complete-path color word would have at least two switches. The signed-second-switch construction from Article XIV gives an odd map on the dual type-B Coxeter one-skeleton, with target \(S^{n-3}\), because labels of adjacent complete flags are nonopposite. Theorem 2 forces an extension obstruction on the dual \((n-2)\)-skeleton. At \(n=4\), Theorem 1 says that the target circle has a nonzero winding around the boundary of some rank-two dual cell. The accompanying Article XV note gives a valid cube-edge coloring with winding \(+1\) on the initial eight-flag dihedral residue; it does not assert absence of monochromatic geodesics elsewhere.

**Research consequence.** Dihedral winding defects are not independent local choices. They assemble into the nonzero class (3), which cannot be annihilated simply by rerouting target edges equivariantly. A proof of the monochromatic full-path conjecture through this method must show that the *colored local incidence* supplies additional chain-level cancellations inconsistent with the nonzero obstruction class whenever no favorable complete path exists. In the ordinary boundary-tournament case, a separate starting difficulty remains: opposite complete flags can carry identical self-complement-reversed words, preventing every word-only odd label. The common chain construction must retain flag information as well as switch data.

### Centrally symmetric permutahedral counterexamples to the opposed-window conjecture

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


### Extreme-switch selectors and central-rank localization

Let \(P\) be a simple \(d\)-polytope, \(d\ge3\), and \(K\) the order complex of its proper nonempty faces. Then \(K\cong S^{d-1}\). Let \(X\) be its dual cell complex; its vertices are maximal face flags \(g=(F_0\subset\cdots\subset F_{d-1})\), and a dual edge of rank \(i\) exchanges \(F_i\). Write \(G=K^{(1)}\), the graph joining every comparable pair of proper faces.

Suppose \(g\) carries a binary complete-path word \(w(g)=(w_1,\ldots,w_m)\) with at least two switches. Let a free simplicial opposition \(J\) on \(K\) transform the words by complementation, either in place or after reversal. Require **rank coherence**: \(J\) carries the rank-\(j\) face in the flag to the rank assigned to switch position \(j\) after the word opposition. For the cube with edge windows, \(m=d\), both index maps are identity; for the simplex with ordered triple windows, \(m=d-1\), both send \(j\mapsto d-1-j\). This is a structural compatibility property, not an assumption that every arbitrary opposed polytope automatically satisfies it.

**Theorem 1 (an antipodal graph-valued selector).** Let \(a(g)\) and \(b(g)\) be the first and last switch indices of \(w(g)\). Then
\[
\boxed{L(g)=\operatorname{midpoint}\,[F_{a(g)},F_{b(g)}]\in G}
\tag{1}
\]
is well defined and satisfies \(L(Jg)=JL(g)\).

*Proof.* The indices are distinct and lie between \(1\) and \(m-1\), so the corresponding proper faces are nested and span an edge of \(K\). Complementation preserves every switch position; complemented reversal sends position \(j\) to \(m-j\) and exchanges the first and last switches. Rank coherence makes the unordered pair of chosen faces transform by \(J\), proving equivariance. For the simplex this holds even when the two opposed flags have identical binary words: their selected face vertices differ. \(\square\)

Choose a \(J\)-stable set \(R\) consisting of one central face rank, or two adjacent central ranks. For cubes, any one rank is stable. For simplices with \(d\) odd, choose \(R=\{(d-1)/2\}\); for simplices with \(d\) even, choose \(R=\{d/2-1,d/2\}\). Associate to each flag its *anchor* \(A(g)\in G\): the vertex \(F_r\) if \(R=\{r\}\), or the midpoint of \([F_r,F_{r+1}]\) if \(R=\{r,r+1\}\). Then \(A(Jg)=JA(g)\).

Let \(X_{\neg R}\) comprise all closed dual cells whose variable face ranks avoid \(R\). It is an opposition-invariant subcomplex, and every flag incident with one of its cells has the same anchor.

**Theorem 2 (equivariant anchored extension).** The selector (1) extends continuously and equivariantly to
\[
\boxed{L_R:X_{\neg R}\longrightarrow G.}
\tag{2}
\]

*Proof.* For each maximal flag \(g\), choose a path \(\gamma_g\) in \(G\) from \(L(g)\) to \(A(g)\), entirely inside the one-skeleton of the maximal simplex of \(K\) represented by \(g\). Such a path exists because all of the flag's proper faces are nested and pairwise adjacent in \(G\). Since opposition freely permutes maximal flags, choose paths on one representative of each antipodal pair and impose \(\gamma_{Jg}=J\gamma_g\).

For a directed dual edge \(g\to h\) changing a rank outside \(R\), the anchor is unchanged: \(A(g)=A(h)\). Define the image of the edge as \(\gamma_g\gamma_h^{-1}\). This is a path joining the prescribed vertex labels and is equivariant. Around a dual two-cell avoiding \(R\), these paths concatenate as \(\gamma_{g_0}\gamma_{g_1}^{-1}\gamma_{g_1}\gamma_{g_2}^{-1}\cdots\gamma_{g_q}\gamma_{g_0}^{-1}\), which freely reduces to the empty path. Hence the boundary admits a filling in the graph. Choose compatible fillings over antipodal cell pairs. For cells of dimension at least three, the higher homotopy groups of a graph vanish, allowing extension over each further cell, again in antipodal pairs. \(\square\)

**Theorem 3 (the unfilled cells must carry a topological obstruction).** No equivariant map from the full two-skeleton \(X^{(2)}\) to \(G\) exists. Hence, starting from (2), the only remaining obstruction to a full graph-valued map lies among dual edges and two-cells involving at least one rank in \(R\).

*Proof.* The covering class \(\alpha\in H^1(X/J;\mathbb F_2)\) of the free involution on the sphere satisfies \(\alpha^2\ne0\), also on the quotient two-skeleton. An equivariant map \(X^{(2)}\to G\) would induce a map into the one-dimensional quotient graph \(G/J\) that pulls back its covering class to \(\alpha\). The square of the class on \(G/J\) vanishes because the graph has no second cohomology. This contradicts \(\alpha^2\ne0\). \(\square\)

**Status.** Theorems 1–3 are unconditional structural statements once every flag has two switches. They apply to unrestricted NORI1 cube-edge colorings and unrestricted reversal-odd boundary tournaments. They do not establish a one-switch witness: central-rank exchange cells remain unfilled. The new proof target is to exploit the common projective-incidence descent to rule out the required central-rank obstruction under a hypothetical absence of favorable complete paths. Unlike the signed-second-switch method, this approach has a **one-dimensional equivariant target** and reduces the first obstruction to **rank-two residues in every ambient dimension**.

### Root-slide holonomy for reversal-odd cube turns

Fix \(n\ge3\), an antipodally odd undirected cube-edge coloring \(c(\bar e)=1-c(e)\), and a chirality \(\chi(i,j)\in\mathbb F_2\) on pairs of distinct dimensions with \(\chi(j,i)=1+\chi(i,j)\). For a full cube geodesic from \(x\) with dimension order \(\pi=(\pi_1,\ldots,\pi_n)\), write its edge colors \(w_1,\ldots,w_n\) and define
\[
b_j=w_j+w_{j+1}+\chi(\pi_j,\pi_{j+1})\quad(1\le j<n).
\]
The \(b_j\) are locally reversal-odd turn labels: reversing an ordered turn exchanges its two dimensions and complements \(\chi\), while its edge-color XOR is unchanged. Antipodal translation complements both edge colors and hence preserves \(b_j\).

Let \(\pi_{n+1}=\pi_1\). Define the cyclic chirality
\[
K(\pi)=\sum_{j=1}^n\chi(\pi_j,\pi_{j+1})
\]
and append the closing bit
\[
\boxed{b_n=1+K(\pi)+\sum_{j=1}^{n-1}b_j.}
\]

**Theorem 1 (cyclic chiral root-slide theorem).** The canonical flag shift
\[
T(x;\pi_1,\ldots,\pi_n)=(x+e_{\pi_1};\pi_2,\ldots,\pi_n,\pi_1)
\]
rotates the augmented turn word \((b_1,\ldots,b_n)\) cyclically. Every such augmented turn word obeys
\[
\boxed{\sum_{j=1}^n b_j=1+K(\pi).}
\]
After \(n\) slides the root is antipodal, and the entire turn word returns.

*Proof.* Under \(T\) the undirected edge-color word changes from \((w_1,\ldots,w_n)\) to \((w_2,\ldots,w_n,1+w_1)\). The first \(n-2\) new turns are \(b_2,\ldots,b_{n-1}\), while the last is
\[
w_n+(1+w_1)+\chi(\pi_n,\pi_1)
=1+\sum_{j=1}^{n-1}b_j+K(\pi)=b_n.
\]
Since \(K\) is invariant under cyclic permutation of \(\pi\), the closing-bit rule gives the next rotation too. After \(n\) slides, each dimension has been toggled once; the antipodal edge-color complementation cancels in every turn XOR. \(\square\)

**Corollary 2 (quantitative switch-defect criterion).** Put
\[
\delta_j=b_j+\chi(\pi_j,\pi_{j+1}) \quad(1\le j\le n),
\]
interpreting the last pair cyclically, and let \(D\) be the integer number of ones in this cyclic defect vector. Then
\[
\boxed{\sum_j\delta_j=1,\qquad
\min_{0\le k<n}\operatorname{sw}(P(T^k(x;\pi)))=D-1.}
\]
In particular \(D\) is odd, and the orbit contains a monochromatic full geodesic if and only if \(D=1\). One-switch and zero-switch existence are equivalent on each root-slide orbit.

*Proof.* For \(j<n\), \(\delta_j=w_j+w_{j+1}\); the closing defect is \(\delta_n=1+w_n+w_1\). Their binary sum is one. Sliding rotates these defects and places any selected defect at the omitted seam. Thus the least internal switch count is \(D-\max_j\delta_j=D-1\). \(\square\)

**Theorem 3 (fixed-root type-A opposition).** For each fixed cube root \(x\), all dimension orders form the chambers of a type-\(A_{n-1}\) Coxeter sphere. The order-reversal involution \(\pi\mapsto\pi^{\mathrm{rev}}\) is its antipode, and
\[
\boxed{b(x;\pi^{\mathrm{rev}})=\mathbf1-\operatorname{rev} b(x;\pi).}
\]
This is the same complemented-reversal law obeyed by the triple-color words of ordinary reversal-odd boundary tournaments on Hamilton paths.

*Proof.* Reversing a complete geodesic and applying cube antipodality gives the same root and reversed dimension order; its edge-color word is complemented reversal of the original. Adjacent edge-color changes are therefore reversed without complementation. The antisymmetry of \(\chi\) adds the one-bit complement at each reversed turn, yielding the displayed identity. Order reversal is the longest-element opposition of the type-A Coxeter complex. \(\square\)

**Scope.** This is a faithful local-reversal-odd encoding of unrestricted NORI1, not a proof that an orbit with \(D=1\) exists. The cube also has gluing edges between these fixed-root type-A spheres, and the reversal involution does not preserve that gluing in the standard type-B complex. Root selection remains the outstanding compatibility problem.

### Dihedral full-path symmetry and the root-gluing obstruction

The two motivating problems have a common *dihedral* action on their complete paths. It is more extensive than the simple flag rotation, and it is faithful to the original color words. Its limitation is topological: the reflection action preserves the type-A chamber structure at each fixed root of the cube, but not the type-B adjacency that joins different roots.

**Theorem 1 (cube dihedral gallery action).** For every \(n\ge3\), let \(\mathcal G_n=\{(x;\pi):x\in\mathbb F_2^n,\ \pi\in S_n\}\) be the full cube-geodesic flags. Define
\[
T(x;\pi_1,\ldots,\pi_n)
=(x+e_{\pi_1};\pi_2,\ldots,\pi_n,\pi_1),
\qquad
R(x;\pi)=(x;\pi^{\rm rev}).
\]
Then
\[
\boxed{T^{2n}=R^2=1,\quad T^n(x;\pi)=(\bar x;\pi),\quad RTR=T^{-1}.}
\tag{1}
\]
For any antipodally odd undirected-edge coloring, if \(w(g)=(w_1,\ldots,w_n)\) is the true edge-color word of \(g\), then
\[
\boxed{
w(Tg)=(w_2,\ldots,w_n,1+w_1),\qquad
w(Rg)=(1+w_n,\ldots,1+w_1).
}
\tag{2}
\]

*Proof.* After \(n\) root slides the geodesic has used every dimension once as its first dimension, and the order returns, giving \(T^n=(x\mapsto\bar x)\) and \(T^{2n}=1\). Reversal of a complete geodesic followed by antipodal translation starts at its original root and uses the reverse dimension order, giving the second word relation. The first follows because its final edge is the antipodal translate of the initial edge. Direct calculation shows
\[
RTR(x;\pi)
=(x+e_{\pi_n};\pi_n,\pi_1,\ldots,\pi_{n-1})=T^{-1}(x;\pi).
\]
\(\square\)

**Theorem 2 (boundary-tournament dihedral gallery action).** On Hamilton vertex orders \(\pi=(v_1,\ldots,v_n)\), put \(T\pi=(v_2,\ldots,v_n,v_1)\) and \(R\pi=(v_n,\ldots,v_1)\). Then
\[
\boxed{T^n=R^2=1,\quad RTR=T^{-1}.}
\tag{3}
\]
For an arbitrary reversal-odd boundary triple coloring \(b\), define the cyclic triple array
\[
a_j=b(v_j,v_{j+1},v_{j+2}),\quad j\in\mathbb Z/n\mathbb Z.
\]
Every full Hamilton path flag in the cyclic orbit reads \(n-2\) consecutive entries of this array. \(T\) rotates the array, and \(R\) complements it and reverses its circular order, with an index shift.

*Proof.* The dihedral relations follow from operations on an ordered cycle. Cyclically rotating a vertex order rotates all consecutive cyclic triples. Reversing the order sends every ordered triple to its reverse, which changes its color by one, and reverses the cyclic sequence. \(\square\)

**Corollary 3 (opposed fixed-root type-A fibers versus root gluing).** For fixed \(x\), the \(n!\) cube flags \((x;\pi)\) form the chamber set of a type-\(A_{n-1}\) Coxeter sphere. \(R\) acts as its simplicial antipode. Swapping neighboring dimensions is a type-A chamber adjacency, and \(R\) conjugates the swap in position \(i\) to the swap in position \(n-i\).

However, \(R\) does not act simplicially on the ordinary type-B Coxeter sphere incorporating all cube roots. A type-B chamber edge may change the root across the *first* dimension without changing \(\pi\):
\[
(x;\pi)\sim(x+e_{\pi_1};\pi).
\]
Under \(R\), this becomes a root change across dimension \(\pi_1\), which is now *last* in the reversed order; those chambers are not adjacent in the type-B Coxeter complex.

Thus the required symmetry already exists on the full gallery set and on each type-A root fiber, but it is incompatible with the standard gluing between root fibers. A common topological proof could seek an alternative gluing that makes the dihedral reflection continuous without forfeiting the rank-preserving full-geodesic certificates. Simply declaring \(R\) antipodal on the type-B sphere is invalid.

**Scope.** Dihedral gallery symmetry and complemented reversal do not alone imply a low-switch complete path: unrestricted turn colorings and sparse gallery systems give obstructions. The new point is the shared *faithful* symmetry and the identification of the residual obstruction as coherence of fiber gluing rather than of word parity.

##### Tetrahedral parity obstruction for the complete quadratic switch tensor

**Theorem 1 (four-point cancellation).** For each \(n\ge6\), there is an unrestricted reversal-odd boundary triple coloring and a rank-three Coxeter cell \(D\cong P_4\) whose 24 Hamilton flags all have at least two switches, yet the convex hull of their **complete quadratic switch bivectors** contains zero. More strongly, each of the six Klein-four orbits of four flags has bivectors summing to zero.

*Proof.* Let \(A=\{1,2,3,4\}\) be the variable first block, and fix the remaining symbols in a suffix beginning \(e,f\). For any distinct \(a,b,c\in A\), let \(t(a,b,c)\) be the parity of \((a,b,c,d)\), where \(d\) is the omitted fourth member. Set \(b(a,b,c)=t(a,b,c)\). Cyclically rotating four symbols changes parity, and reversing the first and third positions changes parity. Prescribe \(b(c,d,e)=1\) whenever \(c,d\in A\) are the last two symbols of a first-block order, and \(b(d,e,f)=0\) for \(d\in A\). Set subsequent colors on the fixed suffix to zero. These prescriptions are consistent with reversal oddness and extend to all unused ordered triples.

Thus every full order \(\pi=(a,b,c,d,e,f,\ldots)\) in \(D\) has consecutive triple-color word \((t,1-t,1,0,0,\ldots)\). Its switch-prefix ranks are \(\{2,4\}\) for \(t=0\), or \(\{2,3,4\}\) for \(t=1\). Consequently
\[
\mathcal B(\pi)=
\begin{cases}
Z_2\wedge Z_4,& t=0,\\
Z_2\wedge Z_3+Z_2\wedge Z_4+Z_3\wedge Z_4,&t=1.
\end{cases}
\tag{1}
\]
Let \(T=Z_4=\mathbf1_A-(4/n)\mathbf1\) and let \(W_A\) consist of vectors supported on \(A\) whose entries sum to zero. All vectors \(Z_2,Z_3,Z_4\) lie in \(U=\mathbb RT\oplus W_A\).

Consider the Klein four-group \(K=\{1,(12)(34),(13)(24),(14)(23)\}\) acting on \(A\). As a real \(K\)-module, \(W_A\) splits into the three distinct nontrivial one-dimensional characters. Therefore
\[
\Lambda^2 U=T\wedge W_A\oplus\Lambda^2W_A
\]
is a sum of six nontrivial one-dimensional \(K\)-modules, and \((\Lambda^2 U)^K=\{0\}\). Hence the group average \(\frac14\sum_{h\in K}hX\) vanishes for every \(X\in\Lambda^2U\).

Each \(h\) is even, preserving parity \(t\). The tensor formula (1) is equivariant under relabeling the four symbols, so \(\mathcal B(h\pi)=h\mathcal B(\pi)\). Thus
\[
\boxed{\frac14\sum_{h\in K}\mathcal B(h\pi)=0.}
\tag{2}
\]
All four coefficients are positive and all four flags have at least two switches. The same conclusion survives every linear map on bivectors, including generic critical contractions. QED.

**Theorem 2 (symmetry-forced zero and external escape).** There is no continuous \(K\)-equivariant map \(D\to\Lambda^2U\setminus\{0\}\). However, if at least two suffix symbols \(e,f\) exist, any nonvanishing \(K\)-equivariant boundary map \(\partial D\to\Lambda^2 U\setminus\{0\}\) extends to a nonvanishing \(K\)-equivariant map \(D\to\Lambda^2W\setminus\{0\}\) that uses a bivector involving the suffix.

*Proof.* The barycenter of \(D=P_4\) is fixed by \(K\). A \(K\)-equivariant map into \(\Lambda^2U\) must send this barycenter into the fixed subspace, which is zero. For the extension, choose \(L=T\wedge(e_e-e_f)\in\Lambda^2W\), a nonzero \(K\)-fixed bivector perpendicular to \(\Lambda^2U\). Cone the boundary map radially to \(L\) at the barycenter. Every interior value is \((1-s)L+sX\), with \(X\in\Lambda^2U\setminus\{0\}\), and is nonzero by orthogonality. The cone is equivariant. QED.

**Proposition 3 (forced global symmetry breaking).** The triple-color data encountered on the 24 flags of \(D\) is \(K\)-invariant, but no globally reversal-odd triple coloring can be \(K\)-invariant on all ordered triples.

*Proof.* The encountered colors are either the four-symbol parity, invariant under even permutations, or the constant mixed-triple prescriptions. But for distinct \(a,c\in A\), a double transposition \(h=(a\,c)(a'\,c')\in K\), where \(\{a',c'\}=A\setminus\{a,c\}\), sends the unused ordered triple \((a,e,c)\) to its reversal \((c,e,a)\). A globally invariant coloring would give equal bits, contradicting reversal oddness. QED.

**Implication.** The full quadratic tensor improves rank-two convex fillings but does not remove the rank-three convex obstruction. No nonlinear *equivariant* filling confined to the local four-symbol tensor module can remove it, either. The extra ambient directions and off-cell coloring constraints are mathematically necessary ingredients for a symmetric filling mechanism; the results do not resolve the global one-switch conjecture.

##### Canonical permutahedral contraction, terminal signs, and an equivariant relative field

Write \(W=\{x\in\mathbb R^n:\sum x_i=0\}\), \(n\ge4\), and let \(P_n\subset W\) be the centered permutahedron. For each permutation \(\pi\), its centered prefix vectors are
\[
Z_j(\pi)=\sum_{h\le j}e_{\pi_h}-\frac jn\mathbf1,\qquad 1\le j<n.
\]
Put
\[
\boxed{\rho(\pi)=\sum_{j=1}^{n-1}Z_j(\pi)
=\sum_{j=1}^n\left(\frac{n+1}{2}-j\right)e_{\pi_j},}
\tag{1}
\]
the vertex position vector of \(P_n\). Let \(S_\pi\subseteq\{1,\ldots,n-1\}\) be any set of at least two switch-prefix ranks, and define
\[
\mathcal B(\pi)=\sum_{\substack{r<s\\r,s\in S_\pi}}Z_r(\pi)\wedge Z_s(\pi),\qquad
H(\pi)=\iota_{\rho(\pi)}\mathcal B(\pi)\in\rho(\pi)^\perp.
\tag{2}
\]

**Theorem 1 (canonical positivity without choosing a contraction).** For every \(S_\pi\) with at least two ranks, \(H(\pi)\ne0\). If \(p=\min S_\pi\), \(q=\max S_\pi\), then
\[
\boxed{
\langle H(\pi),Z_k(\pi)\rangle<0\quad(1\le k\le p),\qquad
\langle H(\pi),Z_k(\pi)\rangle>0\quad(q\le k<n).
}
\tag{3}
\]
In particular, \(H_{\pi_1}<0\) and \(H_{\pi_n}<0\).

*Proof.* The Gram kernel \(G(i,j)=\langle Z_i,Z_j\rangle=\min(i,j)-ij/n\) has nonnegative ordered minors
\[
D(i,j;r,s)=\langle Z_i\wedge Z_j,Z_r\wedge Z_s\rangle\ge0
\quad(i<j,\ r<s),
\]
with strict positivity whenever the open intervals \((i,j)\) and \((r,s)\) overlap, as proved in the total-positivity Subsection. Expanding \(H\) using \(\rho=\sum_t Z_t\), for \(k\le p\) all terms \(t\le k\) have disjoint rank intervals and vanish, while all \(t>k\) contribute \(-D(k,t;r,s)\le0\). The contribution \(t=q,(r,s)=(p,q)\) is strictly negative. For \(k\ge q\), all terms \(t\ge k\) vanish, the remaining terms contribute \(D(t,k;r,s)\ge0\), and \(t=p,(r,s)=(p,q)\) is strictly positive. This proves (3) and nonvanishing. Finally \(Z_1=e_{\pi_1}-\mathbf1/n\) and \(Z_{n-1}=\mathbf1/n-e_{\pi_n}\). Since \(H\in W\), (3) at \(k=1,n-1\) yields both terminal entries negative. QED.

**Theorem 2 (even tangent-vector carrier and its global obstruction).** If the switch word is odd under complemented reversal, then
\[
\rho(\pi^R)=-\rho(\pi),\quad
\mathcal B(\pi^R)=-\mathcal B(\pi),\quad
\boxed{H(\pi^R)=H(\pi).}
\tag{4}
\]
Thus (2) gives a nonzero even tangent label at every vertex of \(\partial P_n\cong S^{n-2}\), under the hypothesis of at least two switches at every full ordering. No continuous nowhere-zero extension of these labels to the whole sphere that remains tangent to the radial vector and even under antipodality exists, for any \(n\).

*Proof.* Centered prefix reversal satisfies \(Z_{n-j}(\pi^R)=-Z_j(\pi)\); the switch set reverses and every ordered bivector pair acquires a minus sign, proving (4). Normalize the centrally symmetric boundary of \(P_n\) radially to the unit sphere in \(W\), and put \(d=n-2\). A continuous field \(h(x)\in x^\perp\setminus\{0\}\) with \(h(-x)=h(x)\) would descend to a nowhere-zero section of the rank-\(d\) orthogonal complement bundle \(\gamma^\perp\) of the tautological line \(\gamma\to\mathbb RP^d\). But
\[
w(\gamma^\perp)=(1+\alpha)^{-1}
=1+\alpha+\cdots+\alpha^d,\qquad
w_d(\gamma^\perp)=\alpha^d\ne0,
\tag{5}
\]
contradicting a nonzero section. QED.

**Theorem 3 (automatic zero-free interpolation on protected terminal faces).** Let \(F\) be a parabolic face of \(P_n\) represented by an ordered partition whose first block is \(A\), last block is \(C\), with \(|A|=a\ge1\), \(|C|=c\ge1\). Suppose all full orders \(\pi\) refining the face have at least two switches and
\[
a\le\min S_\pi,\qquad \max S_\pi\le n-c.
\tag{6}
\]
Fix any triangulation of \(F\) using its permutahedral vertices and extend \(H\) and \(\rho\) piecewise affinely to functions \(V(x)\) and \(\rho(x)=x\) on \(F\). Then
\[
\boxed{
h_F(x)=V(x)-\frac{\langle V(x),x\rangle}{\|x\|^2}x\ne0
\quad(x\in F).
}
\tag{7}
\]
These local formulas agree on common faces when obtained from a single triangulation of \(\partial P_n\); reversal sends \(h_F(x)\) to \(h_{F^R}(-x)=h_F(x)\).

*Proof.* The vectors \(Z_a=\mathbf1_A-(a/n)\mathbf1\) and \(Z_{n-c}=-(\mathbf1_C-(c/n)\mathbf1)\) are fixed on all vertices of \(F\). By (3) and (6), \(\sum_{i\in A}H_i<0\) and \(\sum_{i\in C}H_i<0\) for every vertex; thus both remain strictly negative under affine interpolation. But the permutahedral position vector has fixed opposite-sign block sums on \(F\):
\[
\sum_{i\in A}x_i=\frac{a(n-a)}2>0,\qquad
\sum_{i\in C}x_i=-\frac{c(n-c)}2<0.
\]
Consequently \(V(x)\) cannot be proportional to \(x\): a proportionality factor would have to be negative on the first block and positive on the last. Its orthogonal projection in (7) is nonzero. Both projection and interpolation respect reversal by (4), proving the equivariance assertion. QED.

**Corollary 4 (unrestricted boundary and cube support).** Under the hypothetical absence of a Hamilton order with at most one switch, every boundary 3-tournament has switch ranks in \(\{2,\ldots,n-2\}\). Therefore (7) constructs an explicit color-dependent, zero-free, reversal-even tangent section on the subcomplex of permutahedral faces whose first and last blocks each have size at most two. For cube-edge words, the rank range is \(\{1,\ldots,n-1\}\), and the same construction protects all faces with first and last blocks singleton. Its global obstruction remains the nonzero class (5). A cube geodesic with at most one switch can be root-slid to a monochromatic antipodal geodesic.

**Boundary of the result.** Equations (1)-(3) eliminate algebraic genericity and choice of contraction completely. Theorem 3 provides a canonical compatible relative interpolation, but its protected terminal-face subcomplex is not the entire permutahedral sphere. Rank-three tetrahedral parity obstructions can still prevent the naive zero-free extension on other faces; the global conjectures remain unresolved.

##### Exterior tournament scores resolve a local tetrahedral symmetry obstruction

**Theorem 1.** Let A be a set of even size m, and let e,f be distinct symbols outside A. For any reversal-odd triple coloring b, set
s_e(a)=sum over c in A excluding a of (-1)^{b(a,e,c)}.
Then s_e has entry sum zero, every entry is an odd nonzero integer, and ||s_e||^2 >= m. Furthermore the bivector L=s_e wedge (e_e-e_f) is nonzero and perpendicular to the space of bivectors generated by T and W_A, with T=1_A-(m/n)1 and W_A the zero-sum A-supported subspace.

*Proof.* The reversal rule makes the signs for (a,e,c) antisymmetric under interchanging a,c, so the entry sum is zero. Each entry has m-1 odd summands, hence is an odd integer. The nonzero wedge and orthogonality follow because e_e-e_f is nonzero and belongs to the orthogonal complement of span(T,W_A).

**Theorem 2.** Consider the four-symbol first-block tetrahedral parity example, with at least two fixed suffix symbols. The full quadratic switch bivectors of all 24 flags belong to Lambda^2(span(T,W_A)). Their affine interpolations on every rank-two boundary face avoid zero, by the rank-two convex-carrier theorem. Let B(y) denote this continuous nonvanishing boundary interpolation on the permutahedral three-ball D. Then for any off-cell triple colors the formula
F((1-t)o+ty)=(1-t)L+t B(y),
where o is the center, y lies in the boundary, and 0<=t<=1, defines a continuous nowhere-zero map from D into the full ambient bivector space agreeing with B on the boundary. Indeed the two summands lie in orthogonal linear subspaces, and at least one is nonzero. The formula is natural under relabeling A together with the selected ordered exterior symbols.

**Proposition 3.** For an odd-size A the signed score may vanish (regular tournaments furnish examples). The tournaments defined by (a,e,c) for distinct exterior symbols e and f can be chosen independently, so legal colorings can have s_e=s_f or s_e=-s_f. Consequently no nonvanishing transition between choices of the exterior score follows from reversal oddness alone.

This supplies a color-derived escape direction for the tetrahedral parity obstruction and identifies the remaining lack of gluing coherence across different exterior channels. It neither asserts nor proves the one-switch or zero-switch conjectures.

**Theorem 4 (coherent interpolation of all exterior score channels).** Let E=(e1,...,er), r>=2, list exterior symbols in their cell order. Put T=1_A-(|A|/n)1, v=e_e1-e_er, and let s_e be the nonzero signed tournament score for each e. For every point lambda in the probability simplex on E, put

L(lambda)=[sum_e lambda_e s_e+(1-sum_e lambda_e^2)T] wedge v.

This map never vanishes, agrees with s_e wedge v at simplex vertex e, and restricts compatibly to every simplex face. Indeed the W_A and RT parts of its first factor are orthogonal; at vertices the W_A term is a nonzero score, elsewhere the RT term is nonzero. The first factor is perpendicular to nonzero v. Under reversal of the exterior list, v changes sign, while the score sum and quadratic symmetric coefficient remain unchanged upon reversing the weights. Therefore L is reversal odd.

**Corollary 5 (parametric parity-cell filling).** On the tetrahedral parity cell D, the bivectors L(lambda) lie perpendicular to the entire local tensor space Lambda^2U. Thus F((1-t)o+ty,lambda)=(1-t)L(lambda)+t B_boundary(y) is a nowhere-zero extension on D times the exterior choice simplex, agrees with the previously fixed boundary filling, and is compatible with all simplex faces. Contrary to naive linear interpolation, opposite exterior scores cause no zero. This does not yet resolve matching across different moving blocks or unrestricted rank-three residues.

##### The parabolic block-count surplus for equivariant oriented-plane fillings

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

##### Parabolic saturation of affine root syndromes

Let \(B\in\mathbb F_2^{n\times n}\) have zero diagonal and satisfy \(B\mathbf1=\mathbf1\). Color undirected direction-\(i\) edges of \(Q_n\) by \(c_i(x)=a_i+(Bx)_i\). Put \(V=\mathbb F_2^n/\operatorname{im}B\), \(q=\dim V\), and define the root syndrome of a full order \(\pi\) by
\[
\Phi(\pi)=\left[\left(\sum_{j\text{ before }i}B_{ij}\right)_{i=1}^n\right]\in V.
\]
A full geodesic of constant color exists with this direction order if and only if \(\Phi(\pi)=[a]\).

**Theorem 1 (additivity over parabolic products).** Fix an ordered partition \(\mathcal P=C_1|\cdots|C_s\). Let \(D_h\subset V\) be the differences in syndrome obtained by varying the permutation inside \(C_h\), relative to a fixed reference order. Then
\[
\boxed{\Phi(\{\pi:\pi\text{ refines }\mathcal P\})
=\Phi(\pi_0)+D_1+\cdots+D_s.}
\tag{1}
\]
Consequently the parabolic product cell certifies a monochromatic full geodesic for every affine offset \(a\) whenever \(D_1+\cdots+D_s=V\).

*Proof.* The predecessor sum for an element of block \(C_h\) splits into contributions from all earlier blocks, fixed by the partition, and its predecessors inside \(C_h\), which vary only with that block. Changes from different blocks have disjoint row supports and add independently, giving (1). QED.

Write \(\Delta_{ij}=B_{ij}e_i+B_{ji}e_j\). By the adjacent-exchange syndrome formula, swapping consecutive directions \(i,j\) changes \(\Phi\) by \([\Delta_{ij}]\).

**Theorem 2 (commuting exchange cube).** Suppose \(q\) mutually vertex-disjoint unordered pairs \(\{i_h,j_h\}\) have projected exchange vectors \([\Delta_{i_hj_h}]\) forming a basis of \(V\). Then every offset \(a\) admits a monochromatic full antipodal geodesic. The \(2^q\) orders obtained by swapping these pairs independently, each pair kept consecutive, enumerate \(V\) bijectively under \(\Phi\).

*Proof.* Use the selected pairs as size-two blocks of a parabolic partition, with all remaining symbols as singleton blocks. The syndrome changes independently by the \(q\) basis vectors, so the \(2^q\) syndromes cover \(V\). QED.

**Theorem 3 (one cyclic root slide completes the cube).** It suffices to find an index \(k\) and \(q-1\) mutually disjoint pairs avoiding \(k\), for which
\[
\boxed{[e_k],\ [\Delta_{i_1j_1}],\ldots,[\Delta_{i_{q-1}j_{q-1}}]}
\tag{2}
\]
form a basis of \(V\). Then every affine offset admits a monochromatic full geodesic. Specifically, \(2^{q-1}\) independent pair-swap orders starting with \(k\), together with their cyclic rotations moving the initial \(k\) to the end, have all \(2^q\) possible syndromes.

*Proof.* The pair-swap orders cover one affine hyperplane in \(V\). Moving the first symbol \(k\) to the end changes the predecessor sum by \(e_k+Be_k\), since \(B\mathbf1=\mathbf1\); its quotient syndrome changes by \([e_k]\). This translates the first affine hyperplane to its disjoint complement, as required. QED.

**Example 4 (strict strength of the root-slide criterion).** Let \(n=6\), and specify the six row masks of \(B\), with binary bit \(j\) giving entry \(B_{ij}\), by
\[
(22,21,2,2,1,1).
\]
The matrix has zero diagonal, odd row sums and rank three. In the quotient, the nonzero pair-exchange syndromes are
\[
[\Delta_{02}]=1,\quad [\Delta_{04}]=[\Delta_{05}]=17,\quad
[\Delta_{12}]=[\Delta_{13}]=5,\quad[\Delta_{14}]=1.
\]
All remaining pair-exchange syndromes vanish. The nonzero exchange graph has no matching of three edges, so Theorem 2 cannot be applied. Nevertheless, \(k=2\), the pairs \(\{0,4\},\{1,3\}\), and the three vectors
\[
[e_2]=4,\qquad[\Delta_{04}]=17,\qquad[\Delta_{13}]=5
\]
satisfy (2). The eight orders obtained by swapping pairs \(04,13\) within \((2,0,4,1,3,5)\) and optionally moving the leading 2 to the end have syndrome representatives
\[
\{0,1,4,5,16,17,20,21\}=V.
\]
Thus the cyclic root slide closes an instance missed by the commuting matching.

**Interpretation.** These are dimension-simple gallery saturation criteria for arbitrary corank, with no restriction on the affine constants. They complement the known unconditional corank-at-most-two affine NORI1 result, but do not imply that every affine matrix possesses either certificate; the high-corank and nonlinear cases remain open.

**Theorem 5 (corank-three braid and root-slide saturation).** Let \(\dim V=3\). Choose \(k\) with \(w_k=[e_k]\ne0\) and three distinct directions \(i,j,h\ne k\). In \(\bar V=V/\langle w_k\rangle\cong\mathbb F_2^2\), put
\[
u=[\Delta_{ij}],\quad v=[\Delta_{ih}],\quad w=[\Delta_{jh}]
\quad\text{modulo }\langle w_k\rangle.
\]
If these vectors span \(\bar V\) and
\[
\boxed{u+v+w\ne0,}
\tag{3}
\]
then the six full orders starting with \(k\), followed by the six permutations of the braid block \(i,j,h\), then all remaining directions in one fixed order, together with their cyclic rotations moving \(k\) to the end, enumerate every syndrome in \(V\). Hence every affine offset has a monochromatic full antipodal geodesic.

*Proof.* Relative to ordering \(i,j,h\), the six braid permutations change the quotient syndrome by
\[
\{0,u,w,u+v,v+w,u+v+w\}.
\tag{4}
\]
These are sums of the three pair-inversion changes, each independent of the surrounding order. In a two-dimensional binary space, if \(u,v,w\) span, the set (4) contains all four values if and only if \(u+v+w\ne0\). Indeed, when their sum is zero, the three vectors are the distinct nonzero elements and (4) contains only \(\{0,u,w\}\). In every remaining spanning configuration (4) contains the fourth value as well. Root-sliding \(k\) to the end translates every syndrome by the independent class \(w_k\), supplying both lifts of all four values and exhausting \(V\). QED.

**Example 6 (braid closure with no nonzero independent matching).** Let \(n=6\) and take the binary influence matrix whose six row masks are
\[
(4,28,25,4,4,4).
\]
It has zero diagonal, odd row sums, and rank three. Its quotient has representatives with \([e_0]=1\); its nonzero projected exchange vectors are
\[
[\Delta_{02}]=1,\quad[\Delta_{23}]=8,\quad
[\Delta_{24}]=16,\quad[\Delta_{25}]=25,
\]
and every other pair-exchange vector vanishes. In particular, all nonzero exchanges share direction \(2\), so no two nonzero pairs can be disjoint. The earlier commuting-swap theorems cannot apply.

For \(k=0\) and braid triple \(\{2,3,4\}\), the quotient \(\bar V=V/\langle1\rangle\) has \(u=8,v=16,w=0\). These span \(\bar V\) and have sum \(24\ne0\). The six unrotated braid orders attain four distinct syndromes \(\{1,9,17,25\}\); sliding the leading \(0\) to the end adds one, giving \(\{0,8,16,24\}\). All eight syndromes therefore occur.

This establishes a strict hierarchy of dimension-simple certificates: commuting exchanges, one cyclic slide plus commuting exchanges, and a braid hexagon plus a cyclic slide. It is a general sufficient result for corank-three affine colorings, not a complete affine classification.

##### Nested positive-cone carriers yield coherent type-A lower-skeleton fillings

Fix \(n\ge4\), \(W=\{v\in\mathbb R^n:\sum v_i=0\}\), and the dual type-A Coxeter sphere \(X\cong S^{n-2}\). A cell \(D_{\mathcal P}\) is indexed by an ordered nontrivial partition \(\mathcal P=B_1|\cdots|B_k\), has dimension \(n-k\), and has vertices the full permutations refining this partition. Reversal \(J\) acts freely on \(X\) by central inversion, so \(X/J\cong\mathbb RP^{n-2}\). On oriented two-planes of \(W\), \(J\) reverses orientation.

For each proper cumulative union \(A_j=B_1\cup\cdots\cup B_j\), \(1\le j<k\), put
\[
T_{A_j}=\mathbf1_{A_j}-\frac{|A_j|}{n}\mathbf1.
\]
Define
\[
K_{\mathcal P}=\{v\in W:\langle v,T_{A_j}\rangle>0\text{ for all }j<k\},
\quad
\mathcal C_{\mathcal P}
=\{\Pi\in\widetilde{\mathrm{Gr}}_2(W):
\Pi\cap K_{\mathcal P}\ne\varnothing\}.
\tag{1}
\]
Here an oriented plane is identified with its underlying subspace for the intersection condition.

**Theorem 1 (monotone and antipodal carriers).** Every \(K_{\mathcal P}\) is a nonempty open convex cone. For every face \(D_{\mathcal Q}\subseteq D_{\mathcal P}\), one has
\[
K_{\mathcal Q}\subseteq K_{\mathcal P},\quad
\mathcal C_{\mathcal Q}\subseteq\mathcal C_{\mathcal P}.
\tag{2}
\]
For the reversed partition, \(K_{\mathcal P^R}=-K_{\mathcal P}\) and \(J(\mathcal C_{\mathcal P})=\mathcal C_{\mathcal P^R}\). Every centered prefix plane of a refining full order lies in \(\mathcal C_{\mathcal P}\), for any pair of prefix ranks \(1\le p<q<n\).

*Proof.* For a full order \(\pi\) refining \(\mathcal P\), write \(Z_p(\pi)=\sum_{h\le p}e_{\pi_h}-(p/n)\mathbf1\). Every \(A_j\) is the first \(|A_j|\) symbols of \(\pi\), and
\[
\langle Z_p(\pi),T_{A_j}\rangle
=\min(p,|A_j|)-\frac{p|A_j|}{n}>0
\]
for every \(1\le p<n\). Thus \(Z_p(\pi)\in K_{\mathcal P}\), which proves nonemptiness and the plane assertion. Refining a partition adds cumulative unions while retaining the old ones, proving (2). Reversing a partition replaces its cumulative unions by complements, and \(T_{V\setminus A}=-T_A\); since a plane meets a cone precisely when it meets the negative cone, the reversal identity follows. QED.

**Theorem 2 (sphere homotopy type).** Each carrier has
\[
\boxed{\mathcal C_{\mathcal P}\simeq S^{n-3}.}
\tag{3}
\]

*Proof.* The spherical convex region \(B=K_{\mathcal P}\cap S(W)\) is contractible: normalized straight-line interpolation toward any fixed vector in \(B\) stays inside \(B\). Let
\[
E=\{(\Pi,v):\Pi\in\mathcal C_{\mathcal P},\
v\in\Pi\cap B\}.
\]
An oriented plane with a chosen unit vector \(v\) is a positively oriented orthonormal two-frame \((v,w)\). Projection \(E\to B\) has fiber \(S(v^\perp)\cong S^{n-3}\), hence \(E\simeq S^{n-3}\).

The other projection \(E\to\mathcal C_{\mathcal P}\) has fiber \(S(\Pi)\cap K_{\mathcal P}\), a nonempty open circular arc, hence contractible. It admits continuous local sections: project a strictly feasible vector into nearby planes. A partition of unity combines them into a continuous global selection because each feasible set \(K_{\mathcal P}\cap\Pi\) is convex and excludes zero. Fiberwise normalized straight-line interpolation contracts each fiber onto the selected unit vector. Thus this projection is a homotopy equivalence, proving (3). QED.

**Theorem 3 (simultaneous lower-skeleton extension).** Let the vertices of \(X\) be labeled by oriented planes
\[
\Psi(\pi)=\operatorname{span}^+\{Z_{p(\pi)}(\pi),Z_{q(\pi)}(\pi)\},
\quad 1\le p(\pi)<q(\pi)<n,
\]
satisfying \(\Psi(\pi^R)=J\Psi(\pi)\). There exists a continuous \(J\)-equivariant extension
\[
\boxed{F:X^{(n-3)}\to\widetilde{\mathrm{Gr}}_2(W)}
\tag{4}
\]
such that on every cell with at least three ordered blocks,
\[
\boxed{F(D_{\mathcal P})\subseteq\mathcal C_{\mathcal P}.}
\tag{5}
\]

*Proof.* Induct on cell dimension, beginning with the vertex labels, which lie in their carriers by Theorem 1. Suppose a cell \(D_{\mathcal P}\) has dimension \(d=n-k\le n-3\), and every proper face \(D_{\mathcal Q}\) has been filled in its carrier. By (2), the assembled boundary map lies entirely in \(\mathcal C_{\mathcal P}\). By (3), this carrier is \((n-4)\)-connected. The attaching sphere has dimension \(d-1\le n-4\), so its map is nullhomotopic and extends over \(D_{\mathcal P}\) within that carrier. Since ordered nontrivial partitions and their reversals are distinct, the cells occur in free reversal pairs. Choose the extension on one cell of each pair and transport it by target orientation reversal onto its opposite cell. This produces (4)-(5), with the same continuous map on every shared face. QED.

For the two-block cells, dimension \(n-2\), the carrier is the positive-prefix Stiefel transversal \(\mathcal U_{T_A}\simeq S^{n-3}\). The attaching boundary sphere has dimension \(n-3\), so its map carries an integer degree, which need not vanish.

**Theorem 4 (unavoidable top-carrier obstruction in every dimension).** No continuous \(J\)-equivariant map \(F:X\to\widetilde{\mathrm{Gr}}_2(W)\) can satisfy \(F(D_{\mathcal P})\subseteq\mathcal C_{\mathcal P}\) for all cells, including the two-block top cells. Therefore, for every lower-skeleton map supplied by Theorem 3, at least one two-block cell has nonzero integral boundary degree in its carrier.

*Proof.* Suppose a map \(F\) satisfying all carrier conditions existed. At every point \(x\), belonging to the relative interior of a unique cell \(D_{\mathcal P(x)}\), the plane \(F(x)\) contains a vector strictly positive on all the prefix normals of \(\mathcal P(x)\). We can choose these vectors continuously. Indeed near a point \(x_0\) in a face \(D_{\mathcal Q}\), every nearby cell is a coface of \(D_{\mathcal Q}\), whose cone contains \(K_{\mathcal Q}\). Choose \(v_0\in F(x_0)\cap K_{\mathcal Q}\); projecting \(v_0\) into nearby planes \(F(x)\) retains strict positivity on the finitely many prefix normals of \(\mathcal Q\), hence gives a local feasible section. A partition of unity patches these sections continuously, since the feasible vectors in a given plane form an open convex cone avoiding zero. Normalize, obtaining \(v(x)\).

The reversal identities of Theorem 1 imply that \(F(Jx)\) is the same unoriented plane and its feasible cone is the negative of the cone at \(x\). Hence both \(v(x)\) and \(-v(Jx)\) lie in the same convex cone in that plane. Their sum cannot vanish. Accordingly
\[
u(x)=\frac{v(x)-v(Jx)}{\|v(x)-v(Jx)\|}
\]
is a continuous odd map \(u:X\cong S^{n-2}\to S(W)\cong S^{n-2}\), lying in \(F(x)\). Let \(w(x)\) be the unit vector in \(F(x)\), perpendicular to \(u(x)\), completing \(u(x)\) to the prescribed plane orientation. Reversal changes both the first vector and the plane orientation, so
\[
u(Jx)=-u(x),\qquad w(Jx)=w(x),\qquad u(x)\perp w(x).
\tag{6}
\]

Put \(d=n-2\). The odd map \(u:S^d\to S^d\) descends to \(\bar u:\mathbb RP^d\to\mathbb RP^d\), and \(\bar u^*\alpha=\alpha\) for the degree-one mod-two cohomology generator \(\alpha\). The even orthogonal vector \(w\) descends to a nowhere-zero section of \(\bar u^*(\gamma^\perp)\), the rank-\(d\) complement bundle of the tautological line over \(\mathbb RP^d\). Yet
\[
w_d\bigl(\bar u^*(\gamma^\perp)\bigr)
=\bar u^*(\alpha^d)
=\alpha^d\ne0.
\tag{7}
\]
This top Stiefel-Whitney obstruction prohibits a nowhere-zero section. Contradiction.

If every top-cell boundary map had degree zero in its carrier \(\mathcal C_{A|A^c}\simeq S^{n-3}\), each would extend over its ball within that carrier. Extending one cell from each reversal pair and transporting by \(J\) would produce the forbidden global map. Thus some top degree is nonzero. QED.

**Application to the two unrestricted coloring problems.** Under a hypothetical counterexample to the boundary one-switch conjecture, every Hamilton order has at least two switches and the first/last-switch plane assignment meets the hypotheses of Theorem 3. Under a hypothetical counterexample to NORI1, every rooted dimension-simple antipodal geodesic has at least two switches: one switch would give a monochromatic root slide on the same antipodally odd Petrie cycle. At a fixed root, reversal of the dimension order complements and reverses its color word, giving the same odd plane labeling. Thus both settings admit the coherent carrier-controlled extension through the full \((n-3)\)-skeleton, and both have at least one unavoidable two-block top-carrier obstruction in every dimension.

This localizes the surviving problem to the degrees of two-block attaching maps. It does not prove that the coloring constraints force those degrees to vanish, and therefore does not resolve either original conjecture.

##### Gauge-critical switch cochains and clustered near-good paths

The shared antipodal incidence-cover theorem represents both unrestricted colorings by a switch cochain \(\sigma\) in the prescribed cohomology class \(\alpha\in H^1(H;\mathbb F_2)\) of a connected two-cover \(T\to H=T/J\). The cube case has \(T=L(Q_n)\), where vertices represent cube edges and \(J\) acts antipodally. The boundary-tournament case has \(T=O_n\), where vertices are ordered distinct triples, adjacent if they overlap in two successive symbols, and \(J(abc)=cba\). An admissible complete path never visits both lifts of one quotient vertex: otherwise a cube dimension or a tournament symbol would repeat.

**Theorem 1 (isolated switch deletion is not integrable).** Every quotient edge of either incidence graph \(H\) lies on a cycle. Thus deleting only one switch from a legal switch assignment changes its cohomology class and cannot arise from another legal reversal-odd coloring.

*Proof.* A cube transition between incident edges belongs to the four-edge cycle around a cube square; it projects to a cycle in the quotient line graph (for \(n=2\), two parallel quotient edges form a cycle). An ordered-triple transition \(abc\sim bcd\) belongs to \(abc\sim bcd\sim cda\sim dab\sim abc\), disjoint from its reversed cycle and projecting to a cycle. Hence the quotient graph has no bridges. A single-edge cochain has nonzero integral on a cycle containing that edge, and so cannot be a coboundary. Adding it changes the prescribed class \(\alpha\). QED.

**Theorem 2 (legal gauge cuts and critical witnesses).** Flipping a binary color simultaneously at \(v\) and \(Jv\), leaving other elementary states unchanged, is legal. It modifies the quotient switch cochain by the star coboundary \(\delta\mathbf1_{\{[v]\}}\). Such moves generate all legal representatives of \(\alpha\), modulo overall color complementation.

Fix a switch bound \(t\ge0\). Suppose a coloring minimizes \(|S|\), the support size of its quotient switch cochain, among colorings for which all admissible complete paths have more than \(t\) switches. For any \(U\subseteq V(H)\) satisfying
\[
|S\cap\delta U|>\tfrac12|\delta U|,
\tag{1}
\]
there must be a complete path \(P\) whose switch data in the original coloring satisfies
\[
\boxed{2|S\cap E(P)\cap\delta U|\ \ge\
|S\cap E(P)|+|E(P)\cap\delta U|-t.}
\tag{2}
\]

*Proof.* Two reversal-odd colorings differ by a \(J\)-invariant zero-cochain, which descends to \(H\), so every legal change is a quotient coboundary. Flipping the lifts of \(U\) replaces \(S\) by \(S\triangle\delta U\), reducing the support by (1). By minimizing among bad colorings, the new coloring has some full path \(P\) with at most \(t\) switches. The new switch count along \(P\) equals \(|S\cap E(P)|+|E(P)\cap\delta U|-2|S\cap E(P)\cap\delta U|\), proving (2). QED.

**Corollary 3 (clustered local witnesses).** Suppose a quotient vertex \(z\) has more than half of its incident comparisons marked as switches in such a support-minimal bad coloring. The original coloring has a full path of one of two types:
(i) a path with \(t+1\) switches, including a switch at the path endpoint \(z\);
(ii) a path with \(t+1\) or \(t+2\) switches, including two consecutive switches incident to the internal state \(z\). The case \(t+1\) in (ii) requires \(t\ge1\).

*Proof.* Apply Theorem 2 to \(U=\{z\}\). A complete path visits that quotient state at most once, hence toggling \(z\) alters at most one comparison when \(z\) is an endpoint, or at most two consecutive comparisons when it is internal. Only removal of one switched endpoint comparison or both switched internal comparisons can lower the original count to at most \(t\), producing the stated alternatives. QED.

For NORI1 (\(t=0\)), the witness is a one-switch full geodesic with its switch at an endpoint, or a two-switch full geodesic with adjacent switches around one state. For the boundary one-switch target (\(t=1\)), it is a two-switch Hamilton order with one endpoint switch, or a two-/three-switch Hamilton order with two adjacent switches. The state degrees are \(2(n-1)\) and \(2(n-3)\), so the strict majority thresholds are \(n-1\) and \(n-3\).

**Interpretation.** Critical switch sets must be treated as cohomologically constrained path multitransversals. Isolated switch deletion violates integrability; the legitimate local operations are vertex-star gauges and general cuts. Formula (2) supplies a shared necessary condition that distributes nearly favorable complete paths across any cut with a strict majority of switches. This sharpens the proposed induction-on-switch-count framework without proving either conjecture.

**Theorem 4 (linear versus bounded monodromy length).** In the antipodally folded cube line graph \(H_Q=L(Q_n)/J\), \(n\ge2\), the shortest loop with nonzero double-cover monodromy has length \(n\). In the reversal quotient \(H_B=O_n/R\) of the ordered triple-overlap graph on \(n\ge5\) symbols, such a loop has length at most six.

*Proof.* In any connected graph double cover \(T\to T/J\), the shortest nontrivial-monodromy loop has length \(\min_v d_T(v,Jv)\). For cube edges \(e=\{x,x\oplus e_i\}\) and \(Je=\{\bar x,\bar x\oplus e_i\}\), the closest pair of endpoints has Hamming distance \(n-1\). The distance of distinct edges in the line graph is one more than the minimum distance of their endpoints, giving \(d_{L(Q_n)}(e,Je)=n\). For five distinct symbols \(a,b,c,d,e\), the path
\[
abc\sim bcd\sim cda\sim dae\sim aec\sim ecb\sim cba
\]
uses six valid triple-overlap transitions and ends at the reversal of its first state. Its projected loop has nontrivial monodromy and length six. QED.

**Limitation.** The common switch cohomology class does not retain the full-length condition: cube monodromy loops must grow with dimension, but tournament triple-overlap monodromy loops can use only five symbols in any dimension. The Hamilton vertex-usage and cube dimension-usage restrictions must therefore remain visible in any shared unification.

#### Antipodal edge-pair restoration and universal internal pivots

Let \(n\ge2\), let \(\tau\) complement cube vertices, and call an undirected-edge coloring \(c\) legal when \(c(\tau e)=1-c(e)\). Define \(c^{[e]}\) by reversing colors on the two edges \(e,\tau e\). Say that a coloring is *good* if some antipodal geodesic is monochromatic, and *bad* otherwise.

**Lemma (one-change surgery).** If a legal coloring has an antipodal geodesic with at most one color change, it is good.

*Proof.* For a geodesic \(a\to v\to\tau a\) consisting of a color-zero segment followed by a color-one segment, reverse the first segment to run \(v\to a\). Reverse and apply \(\tau\) to the second, obtaining a color-zero segment \(a\to\tau v\). Their concatenation is monochromatic, joins antipodes, and uses each direction once. The opposite color order is symmetric; a constant color word already suffices. \(\square\)

**Theorem (universal internal pivot for a critical antipodal pair).** Suppose \(c\) is legal and bad, while \(d=c^{[e]}\) is good. For each \(b\in\mathbb F_2\), write \(f_b\) for the unique member of \(\{e,\tau e\}\) colored \(b\) by \(d\). Every color-\(b\) monochromatic antipodal geodesic in \(d\) contains \(f_b\) strictly internally. Both colors have such geodesics.

*Proof.* Antipodal complementation maps any monochromatic geodesic to one of the opposite color. Fix a color-\(b\) geodesic \(P\). It uses the direction of \(e\) once and so cannot contain both members of the flipped pair. It also cannot contain the member colored \(1-b\) by \(d\). If \(P\) avoided \(f_b\), then it would still be monochromatic in \(c\), contrary to badness. If \(f_b\) were first or last, the coloring \(c\) would give \(P\) a single color change; the lemma would again contradict badness. Hence \(f_b\) occurs internally in every such \(P\). \(\square\)

**Corollary (critical good–bad boundary).** If a bad legal coloring exists, then there is a good legal coloring \(d\) and a pair \(\{e,\tau e\}\) with the preceding internal-pivot property for both colors.

*Proof.* Legal colorings form a connected hypercube under flips of antipodal edge pairs. A good legal coloring exists: color a selected full geodesic zero, its edge-disjoint antipodal image one, and extend over the remaining edge pairs. Along any pair-flip sequence from this good coloring to a bad one, take the first good-to-bad transition and apply the theorem. \(\square\)

Consequently NORI1 would follow from the *internal-bottleneck exclusion*: every good legal coloring \(d\), for each edge \(f\) of color \(b\), admits some color-\(b\) monochromatic antipodal geodesic that avoids \(f\) or has \(f\) at an endpoint. This is a sufficient condition and is not established here. The argument uses undirected cube-edge colors; it asserts no transfer to boundary tournaments.

#### Boolean restoration fans and internal bottlenecks

Fix direction \(i\) of a legal antipodally odd edge coloring of \(Q_{m+1}\). Identify its lower facet with \(Q_m\), with unrestricted coloring \(g\); the upper horizontal coloring is its complemented antipodal image. Let \(S\) be the set of lower endpoints of zero-colored \(i\)-edges. Legality makes \(S\) a selector of antipodal vertex pairs. Put
\[
A(g)=\{y:\exists\text{ a full }y\to\bar y\text{ geodesic with word }0^*1^*\},\qquad P(g)=A(g)\cap\bar A(g),
\]
and let \(M(g)\) denote roots of monochromatic full geodesics.

**Theorem (restoration fan).** A zero-colored antipodal geodesic crossing the \(i\)-edge above \(y\) exists precisely for \(y\in S\cap A(g)\). Such a geodesic can have that edge first or last precisely when \(y\in S\cap M(g)\). In particular the entire legal coloring is good if and only if \(S\cap A(g)\ne\varnothing\).

If the coloring is bad, then \(P(g)=M(g)=\varnothing\) and \(S\cap A(g)=\varnothing\). Of all antipodal edge-pair flips in direction \(i\), precisely \(|A(g)|\) single flips heal it. Denote this set of healing flips by \(H_i\). For any collection \(F\) of flips in direction \(i\), the resulting coloring is good if and only if \(F\cap H_i\ne\varnothing\). Every member of \(F\cap H_i\) contributes a monochromatic full geodesic crossing its distinct restored \(i\)-edge. For a single healing flip, all monochromatic full geodesics in the repaired coloring use the changed pair strictly internally.

*Proof.* Orient a zero-colored full geodesic from the lower to upper facet and let it cross above \(y\). Reverse its lower zero arm and antipodally complement the reversal of its upper zero arm. These form a \(0^*1^*\) full geodesic from \(y\) to \(\bar y\) in the lower facet. Conversely, split any such lower-facet path at the change, reverse its zero arm, cross vertically, and append the antipodal image of the reversed one arm. The two arms use disjoint directions. A vertical endpoint corresponds to an empty arm and thus a constant word. Antipodal symmetry handles paths of the other color. If the legal coloring is bad, the selector avoids \(A(g)\). An antipodal pair wholly inside \(A(g)\) would meet every selector, hence \(P(g)=\varnothing\). Monochromatic full geodesics place both their endpoints in \(A(g)\), hence \(M(g)=\varnothing\). Every member \(y\in A(g)\) is presently excluded from \(S\), while its antipode is selected. Its pair flip introduces precisely that favorable bridge; independent flips of other pairs cannot affect it. This proves the healing formula and the multi-flip statement. With only one healing pair, it is the sole available favorable bridge; since \(M(g)\) is empty, its use is internal. \(\square\)

**Proposition (internal-bottleneck profile).** Within the bridge colorings above a fixed arbitrary \(g\), a good coloring can possess an \(i\)-edge strictly internal to every monochromatic full geodesic of its color if and only if either (i) \(P(g)=\varnothing\) and \(A(g)\ne\varnothing\), or (ii) \(P(g)\) is one antipodal vertex pair and \(g\) has no monochromatic full geodesic.

*Proof.* A common internal zero-edge means there is a selector \(S\) with \(S\cap A(g)=\{y\}\) and \(y\notin M(g)\). Every antipodal pair contained in \(A(g)\) forces a member into the intersection, so there are at most one such pair. If none exists, select one \(y\in A(g)\) and avoid all remaining favorable members; \(M(g)\subseteq P(g)\) ensures the pivot is internal. If there is one such pair, select one of its members and avoid the others. A monochromatic full geodesic, if present, has both endpoints in that unique pair, and conversely its absence makes the chosen witness strictly mixed. Two or more paired-root orbits prohibit a singleton intersection. \(\square\)

This locates the additional obligation in the proposed universal internal-pivot exclusion: paired-root existence alone does not ensure it. The stronger exclusion would also require a monochromatic antipodal geodesic whenever the paired-root set consists of a single antipodal pair.
#### Weighted restoration and a bridge generating polynomial

Fix a direction of \(Q_{m+1}\), put an arbitrary two-coloring \(g\) on its lower \(Q_m\)-facet, and put the antipodally complemented coloring on the upper facet. Let \(S\) choose one vertex from each antipodal pair \(\{y,\bar y\}\). Give the vertical edge above \(y\) color zero if and only if \(y\in S\). Write \(C(g,S)\) for the resulting legal coloring, and
\[
W_g(y)=\#\{y=v_0,\ldots,v_m=\bar y:
\text{each direction is used once and the color word lies in }0^*1^*\}.
\]
Let \(N_b(c)\) count unoriented monochromatic antipodal geodesics of color \(b\). Antipodal complementation gives \(N_0(c)=N_1(c)\).

**Theorem (weighted bridge enumeration).** For every \(g,S\),
\[
\boxed{N_0(C(g,S))=\sum_{y\in S} W_g(y).}\tag{WB1}
\]
Consequently, with the product over antipodal vertex pairs in the lower facet,
\[
\boxed{\sum_{S}t^{N_0(C(g,S))}
 =\prod_{\{y,\bar y\}}\bigl(t^{W_g(y)}+t^{W_g(\bar y)}\bigr).}\tag{WB2}
\]
The minimum over legal bridge assignments equals
\[
\boxed{\min_S N_0(C(g,S))
=\sum_{\{y,\bar y\}}\min\{W_g(y),W_g(\bar y)\},}\tag{WB3}
\]
and the maximum has \(\max\) in place of \(\min\). Under independent uniformly random selector choices,
\[
\mathbb E_S N_0=\frac12\sum_y W_g(y),\qquad
\operatorname{Var}_S N_0=\frac14\sum_{\{y,\bar y\}}(W_g(y)-W_g(\bar y))^2.
\tag{WB4}
\]

*Proof.* Orient an unoriented monochromatic-zero full geodesic from the lower facet to the upper facet. It crosses one vertical edge above \(y\in S\). Reverse its lower zero arm, obtaining a zero path starting at \(y\). Reverse and antipodally complement its upper zero arm, obtaining a one path ending at \(\bar y\). They concatenate to a full \(0^*1^*\) geodesic rooted at \(y\). Conversely split any such lower-facet geodesic at the zero/one division, reverse the zero arm, cross above \(y\), and append the antipodally complemented reversal of the one arm upstairs. These constructions are inverse. Constant words use the division at the beginning or end, as appropriate. This proves (WB1). Every antipodal bridge pair makes an independent binary choice of one of its two weights. Multiplying the two-term factors gives (WB2); optimizing each choice gives (WB3). The expectation and variance of an independent choice between weights \(a,b\) are \((a+b)/2\) and \((a-b)^2/4\); summation gives (WB4). \(\square\)

**Corollary (additive repair multiplicity).** If \(C(g,S)\) is bad, then \(W_g(y)=0\) for every \(y\in S\). Let \(F\) be any collection of antipodal vertical edge pairs to flip, and identify a flipped pair by its currently unselected root \(y\). Then
\[
\boxed{N_0(C(g,S)^F)=\sum_{y\in F}W_g(y).}\tag{WB5}
\]
Each summand counts full paths whose sole one-colored edge in the original bad coloring is the edge restored at \(y\). By the one-change surgery lemma this edge is internal. Thus the healing neighbors of a bad coloring carry additive, integer path multiplicities, not just a binary repair indicator.

**Common structure and closure limitation.** Both NORI1 and ordinary boundary tournaments have a free involution on local colored observations and a partition into usage classes such that a complete path reads at most one observation from each class: cube directions in NORI1 and the middle symbol of ordered triples in tournaments. Thus complete-path color-word indicator polynomials are separately affine in the coloring variables of each usage class. The cube identity (WB1) is stronger because its fixed-direction observations separate into two opposite facets. Higher-face counterexamples also retain separate affinity, so it alone cannot force the desired path. The outstanding mathematical step is a nonvanishing relation across *different* usage classes, imposed by their joint local incidence geometry.
#### Counterexamples nearest to a perfect cube coloring

Reference distance supplies a different criticality criterion. It is available for any hypothetical NORI1 counterexample, and places no local majority condition on the switch signature.

Fix distinct dimensions \(a,b\) in \(Q_n\), \(n\ge3\). For an edge in direction \(d\), define
\[
(c_0)_d(x)=
\begin{cases}
x_b,&d=a,\\
x_a,&d\ne a.
\end{cases}
\]
This is well-defined on unoriented edges and antipodally odd. It has one switched comparison on every projective Petrie cycle: turns not involving \(a\) compare equal bits, while the two turns at the ends of the unique \(a\)-edge have complementary switch bits \(x_a+x_b\). Thus every Petrie cycle has a monochromatic rotation under \(c_0\).

Write \(V\) for the \(n2^{n-2}\) projective cube-edge observations. Every legal coloring has the form
\[
c_U=c_0+\mathbf1_U,\qquad U\subseteq V,
\]
where both lifts of an observation are flipped. Call \(c_U\) bad if it has no monochromatic full geodesic.

**Theorem 5 (minimum reference distance forces clustered witnesses).** If a bad coloring exists, choose one minimizing \(|U|\). Every proper subset of \(U\) gives a good coloring. More generally, flipping any set \(Q\subseteq V\) satisfying
\[
2|Q\cap U|>|Q|
\]
gives a good coloring.

For each \(e\in U\), there is a full geodesic \(P_e\) on which \(e\) is internal and is the sole edge whose original color differs from the other edge colors. Those other edges all have color \(c_0(e)\). Consequently the original geodesic has two adjacent switches around \(e\), and its projective completion \(C_e\) has three switched comparisons.

*Proof.* A proper subset has smaller reference distance, as does \(U\triangle Q\) under the displayed inequality. Minimality makes both colorings good. In particular restore the observation \(e\) to its reference color and choose a monochromatic full geodesic in the restored coloring. It must contain \(e\), since otherwise it was already monochromatic. Its common color is \(c_0(e)\). In the original coloring only \(e\) on this path has the opposite color.

If \(e\) were an endpoint observation, the original path would have one switch. The antipodal root-slide formula then yields a monochromatic full geodesic in the original coloring, contradicting badness. Thus \(e\) is internal and its two adjacent comparisons are switches. The cyclic completion has the two internal switches plus at most one closing switch; its total is odd and at least three in a bad coloring. Its total is therefore three. \(\square\)

This reduction covers the unrestricted existence problem: any counterexample supplies a counterexample with these witnesses at every changed observation. It does not assert that every bad coloring has this stronger property.

**Proposition 6 (anchored interval structure of each witness).** Cut the observation cycle \(C_e\) at its unique reference switch. In this linear order of its \(n\) observations,
\[
U\cap V(C_e)=I\ \dot\cup\ \{e\},
\]
where \(I\) is a prefix or suffix, possibly empty. If \(I\) is nonempty, at least one unselected observation separates \(e\) from \(I\). If \(I\) is empty, \(e\) is neither endpoint of the linear order.

*Proof.* The reference color word is constant along the chosen linear order. The restored coloring \(c_{U\setminus\{e\}}\) has cyclic variation one on \(C_e\), because the path used in Theorem 5 is monochromatic. Hence the membership word of \(U\setminus\{e\}\) along this order has at most one internal transition. Its ones form a prefix or suffix, including the empty or full possibilities. The full possibility is excluded because \(e\) is not selected after restoration.

If adding \(e\) merely extends that interval, the original membership word still has at most one transition and the original completed variation is one. The same occurs when the interval is empty and \(e\) is an endpoint. Each would contradict badness. This proves both remaining restrictions. \(\square\)

**Proposition 7 (switch compensation under subset repair).** Let \(R\) be a nonempty subset of the minimum-distance set \(U\). Some Petrie cycle \(C\) has variation one after restoring \(R\). Let \(t\) be its unique switched comparison in the restored coloring, and let \(r\) count the cyclic runs of observations in \(R\cap V(C)\). Then
\[
D_{c_U}(C)=
\begin{cases}
2r+1,&t\notin\delta_H(R),\\
2r-1,&t\in\delta_H(R).
\end{cases}
\]
The first case requires \(r\ge1\), and the second requires \(r\ge2\). The original switch set on \(C\) is the symmetric difference of its repair-boundary comparisons with \(\{t\}\).

*Proof.* The repaired coloring is good by Theorem 5, so choose the completion of a monochromatic full geodesic. Its switch set consists of \(\{t\}\). Repair toggles the \(2r\) boundary comparisons of the selected observation runs. Taking the symmetric difference proves the formulas. The original variation is at least three, giving the two lower bounds. The selected observations cannot be empty or the whole cycle, since either gives no boundary comparisons and would leave original variation one. \(\square\)

For a singleton repair the second case is impossible. Thus the two adjacent original switches are forced by completed parity as well as by the monochromatic path witness.

**Corollary 8 (many grade-one cycles in the reduced obstruction).** Let \(Z_1(c_U)\) count distinct projective Petrie cycles with three switched comparisons. For \(n\ge4\),
\[
Z_1(c_U)\ge\frac{|U|}{2}\ge2^{n-3}.
\]

*Proof.* Every observation of \(U\) is healed by its singleton restoration on a grade-one cycle, by Theorem 5. A cycle with three marked comparisons can heal an observation only when both comparisons adjacent to that observation are marked. On an observation cycle of length at least four, three marked comparisons supply at most two such observations. Counting the witness incidences gives \(|U|\le2Z_1(c_U)\).

Furthermore \(U\) meets every Petrie cycle: one disjoint from \(U\) would retain reference variation one. Cube symmetry makes the number of Petrie cycles through each observation constant. Each cycle has \(n\) observations, so double counting incidences with this transversal gives \(|U|\ge |V|/n=2^{n-2}\). \(\square\)

The strict transversal bound established in “Dimension-simple Petrie presentation of the full projective cycle space” further strengthens this to \(Z_1(c_U)>2^{n-3}\). That refinement uses the classification of equality transversals.

##### Coupling reference minimality to connector bonds

**Corollary 9 (short reference-improving connectors force a second descent witness).** Let \(c_U\) be the minimum-distance bad coloring above. Let \(Q\) be the projective observations of a geodesic connector of length at most three, with length also at most \(n-2\), and suppose \(2|Q\cap U|>|Q|\). Flipping \(Q\) produces a good coloring. There is an original grade-one Petrie cycle \(C\) such that \(Q\cap V(C)\) is a single nonempty proper observation interval, and both of its boundary comparisons are original switches.

*Proof.* Reference minimality makes the moved coloring good. Choose a cycle whose moved grade is zero. The connector sensitivity theorem in “Cyclic variation selection for antipodal and boundary path galleries” bounds every grade change by one. Original badness makes the original grade at least one, so it is precisely one and decreases by one. The connector intersection has at most one run. It must have one run, and the identity
\[
g_{\mathrm{moved}}(C)-g_{c_U}(C)=r_Q(C)-a_Q(C)
\]
then forces both boundary comparisons to be original switches. \(\square\)

Thus a short connector certified by retained criticality can lower its independent-arm family; when it also improves reference distance, minimality forces a completed grade-one witness somewhere in the Petrie family. Coupling these two witness families, or ruling out their required compensation, remains the unresolved step.
#### Connected zero-switch skeletons and the cographic deletion matroid

Let \(p:T\to H\) be either of the connected incidence double covers of Article XV, and let \(\eta\in C^1(H;\mathbb F_2)\) be a legal switch cochain, representing \(w_1(p)\), with support \(S\). Write \(Z=(V(H),E(H)\setminus S)\), and let \(V_1,\ldots,V_c\) denote its connected components. Form a multigraph \(F\) by contracting the \(V_i\) in \(H\), retaining the switched intercomponent edges as links and any switched intracomponent edges as loops.

**Theorem 10 (all legal deletions are cocircuit cuts).** For every \(D\subseteq S\), the following statements are equivalent:
(i) toggling every switch in \(D\) to nonswitch, without adding switches elsewhere, is realizable by another legal odd coloring;
(ii) \(\mathbf1_D=\delta_H f\) for a quotient-vertex function \(f:V(H)\to\mathbb F_2\);
(iii) \(D=\delta_H U\), where \(U\) is a union of connected components of \(Z\);
(iv) \(D\) is the inverse image of a cut of \(F\).

The legal deletion masks form the binary cut space of \(F\), with dimension \(c-1\). Their inclusion-minimal nonempty members are the **bonds**, or graphic-matroid cocircuits, of \(F\). The least size of a nonempty legal deletion is \(\lambda(F)\), the edge-connectivity of \(F\), with no nonempty deletion when \(c=1\).

*Proof.* Removing \(D\) changes \(\eta\) to \(\eta+\mathbf1_D\). Both switch cochains represent \(w_1(p)\) if and only if their difference \(\mathbf1_D\) is a coboundary, proving (i)\(\Leftrightarrow\)(ii). Every graph coboundary is a cut \(\delta_H U\). Requiring \(\delta_H U\subseteq S\) means no nonswitch edge crosses the partition \(U|U^c\), so \(U\) is a union of connected components of \(Z\). This proves equivalence with (iii), and contracting those components proves equivalence with (iv). The graph \(F\) is connected because \(H\) is connected. Standard graphic matroid theory gives the dimension, bond characterization and minimum cut size. QED.

**Corollary 11 (connected monochromatic normal form).** The switch set \(S\) is inclusion-minimal among all legal supports representing \(w_1(p)\) if and only if \(Z\) is connected. Every legal coloring is gauge equivalent to one whose zero-switch graph is connected: choose a spanning tree in \(H\) and apply vertex color-pair flips that cancel every switch along it.

*Proof.* A disconnected \(Z\) gives a nonempty cut \(D\subseteq S\) by Theorem 10; conversely a connected \(Z\) forbids such a cut, so no proper support subset is legal. A gauge potential may be integrated along any spanning tree to make its edges all nonswitching, giving the claimed representative. QED.

**Corollary 12 (monochromatic elementary-state components).** The two induced color-class graphs upstairs in \(T\) are both isomorphic, via \(p\), to the zero-switch quotient graph \(Z\). Hence \(Z\) is connected if and only if both of those color-class graphs are connected.

*Proof.* Above every quotient vertex there is one elementary state of each color. An edge of \(Z\) lifts to an adjacency of states having equal colors, and no switched comparison joins two same-color states. The restrictions of \(p\) identify the two color-class graphs separately with \(Z\). QED.

**Short-cycle deletion certificate.** By the local integration theorem, condition (ii) is equivalent to the vanishing of the parity of \(D\) on every required local motif and on the one covering-odd loop: for cubes these are incidence triangles and cubical squares; for boundary triples at least six symbols these are alternating crown squares and directed sliding quadrilaterals and pentagons, with the crown six-cycles also included at five symbols.

**Limitation.** Inclusion-minimality here is among *all legal odd colorings*, not only bad colorings without favorable complete paths. A gauge-equivalent coloring may acquire such a path. Therefore the theorem identifies the matroid of permissible deletions for any proposed switch-critical induction, but does not assert that a hypothetical minimum bad coloring has connected \(Z\).

#### Quotient frustration index and monotone reduction to a connected skeleton

Retain the zero-switch component contraction \(q:H\to F\) from Theorem 10, with all the original switched edges represented in \(F\). Write \(\mathbf1_F\) for the cochain taking value one on every edge of \(F\), including loops.

**Theorem 13 (signed quotient and unavoidable odd cycle).** The canonical covering class satisfies
\[
\boxed{w_1(p)=q^*[\mathbf1_F].}
\tag{15}
\]
Consequently the connected component multigraph \(F\) is nonbipartite, where a loop counts as an odd cycle.

*Proof.* Along any closed walk in \(H\), the original switch cochain \(\eta\) counts each switched edge and ignores each zero-switch edge. Contracting the zero-switch components gives a closed walk in \(F\), whose edge-length parity is the same. This proves (15). The covering class is nonzero since the incidence double cover is connected. If \(F\) were bipartite, \(\mathbf1_F\) would be the cut cochain of its bipartition, hence cohomologically zero, contradicting (15). QED.

**Theorem 14 (maximum-cut optimization of all monotone deletions).** Let \(F\) have \(m\) edges counted with multiplicity and loops. Starting from the given legal coloring, the largest number of switches that can be deleted without creating any new switch is \(\operatorname{MaxCut}(F)\). The smallest remaining number of switches reachable by such monotone deletion is therefore
\[
\boxed{m-\operatorname{MaxCut}(F),}
\tag{16}
\]
the frustration index (minimum edge-bipartization number) of the all-negative signed multigraph \(F\). Every maximum-cut deletion produces a connected zero-switch graph, so its support is inclusion-minimal among *all* legal signatures.

*Proof.* Every monotone legal deletion is, by Theorem 10, a quotient cut \(\delta_F U\); it removes \(|\delta_F U|\) switches and changes no other comparisons. Maximizing the number removed is precisely the maximum-cut problem, proving (16).

To show connectivity, let \(K\) be the spanning subgraph of \(F\) consisting of the edges crossing a fixed maximum cut. Suppose \(K\) is disconnected. Since \(F\) is connected, some edge of \(F\) joins distinct components of \(K\). Such an edge cannot cross the cut, for every crossing edge belongs to \(K\). Flip the cut side of all vertices in one connected component of \(K\). Every crossing edge of \(K\) remains crossing, since both of its ends lie in that component or neither does; every edge joining that component to another was previously noncrossing and now becomes crossing. At least one such edge exists, so the cut size strictly increases, contradicting maximality. Thus \(K\) is connected. The new zero-switch graph is the union of the previous zero-switch components with the crossing edges of \(K\); its contraction is \(K\), so it is connected. By Corollary 11 the remaining signature is inclusion-minimal. QED.

**Implication for criticality.** The matroid of deletion masks has a global optimization interpretation: the entire set of legal monotone deletions is the cut space of \(F\), minimal clusters are its bonds, and the maximal total deletion is a maximum cut. The residual switch count is positive because \(F\) is nonbipartite. For a coloring selected as a minimum-size counterexample *among bad colorings*, these deletions need not remain bad; their resulting favorable full paths are precisely the witnesses constrained by the earlier critical-cut inequality.

#### Root-slide sharpening of critical cut witnesses for NORI1

Let \(H=L(Q_n)/J\) be the antipodally folded cube-edge incidence graph, with the canonical switch cochain \(\eta\) of an odd coloring \(c\). Let \(D=\delta_H U\) be a cut whose support lies inside the switches \(S=\operatorname{supp}\eta\). Deleting \(D\) produces a legal odd coloring \(c'\), obtained from \(c\) by complementing the colors of the two antipodal edge states over every quotient vertex of \(U\).

**Lemma 15 (one-switch root-slide elimination).** A full antipodal dimension-simple geodesic with one interior color switch yields a monochromatic full antipodal geodesic for the same coloring.

*Proof.* Write the direction order \(\pi=(i_1,\ldots,i_n)\) and its color word as \(b,\ldots,b,1-b,\ldots,1-b\), changing after position \(j\), where \(1\le j<n\). Let \(y\) be the vertex reached after those first \(j\) steps. The new full dimension order \((i_{j+1},\ldots,i_n,i_1,\ldots,i_j)\), starting from \(y\), traverses the final \(n-j\) edges of the former path and then antipodal copies of its first \(j\) edges. Those copied edges have color \(1-b\) by oddness, so the whole new path is monochromatic. All dimensions are used once. QED.

**Theorem 16 (two-crossing necessity for every legal monotone deletion).** Suppose \(c\) is a hypothetical NORI1 counterexample. Let \(D\subseteq S\) be any nonempty legal deletion cut and let \(c'\) be obtained by deleting it. If \(P\) is a monochromatic full geodesic of \(c'\), then
\[
\boxed{|D\cap E_{\mathrm{turn}}(P)|\ge2,}
\tag{17}
\]
where the intersection counts consecutive elementary-state comparisons along \(P\). Equivalently, the binary gauge membership of the \(n\) consecutive cube-edge states along \(P\) must change at least twice.

*Proof.* Since \(D\subseteq S\), deleting it changes the comparison bit at precisely those turns in \(D\), and nowhere else. The color word of \(P\) in \(c'\) is constant, so the number of switches on the same path in \(c\) is \(|D\cap E_{\mathrm{turn}}(P)|\). If this number is zero, \(P\) is monochromatic for \(c\), a contradiction. If it is one, Lemma 15 supplies a monochromatic root-slide of \(P\) for \(c\), also a contradiction. QED.

**Theorem 17 (the interior-defect witness in a support-minimal bad coloring).** Suppose a hypothetical NORI1 counterexample \(c\) minimizes the total support size \(|S|\) among all bad legal odd colorings. If a quotient elementary-state vertex \(z\in V(H)\) has more than half of its incident comparisons switched, then there is a complete antipodal geodesic \(P\) under \(c\) whose color word is constant except for one **interior** edge with the opposite color, and that exceptional edge represents \(z\). Consequently \(P\) has two consecutive switches in the linear word and its projective Petrie cycle has three switches in total.

*Proof.* Flipping the antipodal elementary-edge pair corresponding to \(z\) modifies the switch support by its vertex-star cut \(\delta\{z\}\). The strict-majority hypothesis makes the support smaller, so by minimal bad-support choice the flipped coloring \(c'\) admits a monochromatic full geodesic \(P\). A full dimension-simple geodesic traverses each quotient elementary state at most once (each dimension occurs once). Thus the vertex gauge at \(z\) changes the color of at most one edge on \(P\), and changes at most two successive comparisons. If that edge is absent, or occurs at either endpoint, \(P\) has zero or one switch for the original coloring \(c\), contradicting Lemma 15 and badness. Therefore the flipped elementary edge occurs strictly inside \(P\); under \(c\) its color differs from that of all other edges of \(P\), producing two neighboring switches.

The projective Petrie cycle formed by the complete path has an additional closure comparison, joining its last edge to the antipodal copy of its first. Since the two endpoint colors of \(P\) in \(c\) are equal, this closure comparison switches, giving three cyclic switches. QED.

**Corollary 18 (local minimality or three-switch Petrie obstruction).** A support-minimal hypothetical NORI1 counterexample has one of two properties: either every quotient elementary-state vertex has switched degree at most half its total degree, or it has a dimension-simple Petrie cycle with precisely three switches, two consecutive and enclosing a single exceptional elementary edge. This dichotomy holds independently of dimension and does not require choosing a special small subcube.

**Boundary distinction.** The root-slide lemma depends on antipodal cube geometry and is unavailable for general boundary ordered-triple colorings. Their one-switch target has the ordinary star-flip witness classification from the preceding part of this Subsection. Therefore the two-crossing principle is a strengthened cube-specific consequence of the common cographic deletion framework, not an assertion that every one-switch boundary Hamilton word can be made monochromatic by cyclic rotation.

#### Free bridge colors and a closure route through paired roots

The reference family can be enlarged by freeing one whole dimension. This strengthens repair criticality from one favorable path to a coupled pair in an ordinary cube.

Write \(Q_{d+1}=Q_d\times\{0,1\}\), and let \(f:E(Q_d)\to\mathbb F_2\) be arbitrary. Color a lower edge \(e\) by \(f(e)\) and an upper edge \(e\) by \(1-f(\bar e)\). Color the vertical edge at \(z\in Q_d\) by \(h(z)\), where \(h(\bar z)=1-h(z)\). The resulting edge coloring \(C(f,h)\) is antipodally odd.

For \(b\in\{0,1\}\), let \(A_b(f)\) be the set of roots \(z\) admitting a full geodesic to \(\bar z\) with color word
\[
b^k(1-b)^{d-k}\qquad(0\le k\le d).
\]
Empty blocks are allowed, so a monochromatic path qualifies for both values of \(b\). Reversal gives \(A_1(f)=\overline{A_0(f)}\). Call a root in \(A_0(f)\cap A_1(f)\) a paired root.

**Theorem 19 (universal bridge criterion and fixed-dimension equivalence).** The coloring \(C(f,h)\) has a monochromatic full geodesic if and only if
\[
h(z)=b\quad\text{for some }z\in A_b(f).
\]
Consequently the following are equivalent:
(i) every legal bridge assignment \(h\) gives a monochromatic full geodesic;
(ii) \(f\) has a paired root.
In particular, NORI1 in dimension \(d+1\) is equivalent to the assertion that every binary edge coloring of \(Q_d\) has a paired root.

*Proof.* A full geodesic uses precisely one vertical edge. Orient it from the lower to the upper layer, and suppose this crossing occurs at \(z\), with color \(b=h(z)\). Let \(x\) be its lower starting root. Its lower arm \(x\to z\) has color \(b\). Antipodal reflection of its upper arm gives a lower path \(z'\!:=\bar z\to x\) of color \(1-b\). Reverse both arms and concatenate them as \(z\to x\to\bar z\). They use complementary dimension sets, giving the required word. Reversing this construction proves the converse.

The permitted bridge-color set at \(z\) is therefore \(\{b:z\in A_b(f)\}\). At \(\bar z\) this set is its bitwise complement. If a paired root exists, every choice of its bridge color is permitted. If none exists, choose a bridge color outside the permitted set independently at one vertex from each antipodal pair, and extend by oddness. The complementary-set identity makes both choices forbidden, so this legal \(h\) gives no monochromatic full geodesic.

Finally every antipodally odd coloring of \(Q_{d+1}\) is of the displayed form: its lower layer determines \(f\), its upper layer follows by oddness, and its vertical colors determine \(h\). This proves the fixed-dimension equivalence. \(\square\)

**Lemma 20 (a free-direction perfect reference family).** For every legal \(h\), the coloring \(C(0,h)\) has completed switch count one on every Petrie cycle. Thus all vertical colors can be chosen freely within the perfect reference family.

*Proof.* Root the full geodesic immediately before its vertical edge and cross upward. The vertical edge has color \(h(z)\), and all subsequent upper horizontal edges have color one. The linear comparisons contribute \(1-h(z)\). The closing comparison joins the last upper edge, of color one, to the antipodal vertical edge, of color \(1-h(z)\), contributing \(h(z)\). Their sum is one. \(\square\)

The edge orbits where \(C(f,h)\) differs from \(C(0,h)\) correspond precisely to the one-colored edges of \(f\); no vertical edge is changed. Hence minimum distance from this enlarged family is minimum one-edge count for a coloring without a paired root.

**Theorem 21 (bridge-independent critical repairs).** Suppose NORI1 fails in dimension \(d+1\). Choose \(f\) without a paired root minimizing
\[
m=|\{e:f(e)=1\}|.
\]
For every nonempty subset \(R\) of its one-colored edges, changing all edges of \(R\) to zero yields a coloring \(f_R\) with a paired root. Equivalently, every bridge assignment \(h\) makes \(C(f_R,h)\) good.

*Proof.* Theorem 19 converts a counterexample into a coloring without a paired root. A nonempty repair lowers \(m\), so minimality supplies a paired root. Apply the universal bridge criterion. \(\square\)

This quantifier is stronger than choosing a monochromatic witness after one fixed bridge assignment. The two opposite path orientations occur at one common root, using the same repaired horizontal coloring.

**Proposition 22 (normal form of a singleton critical repair).** Let \(e\) be one-colored in the minimum coloring of Theorem 21, and choose a paired root \(z\) of \(f_e\). At least one of its two orientation witnesses fails when \(e\) is restored to one. One may choose the witnesses so that one of the following holds:

1. A full geodesic from \(z\) is zero-colored in \(f_e\) and has \(e\) as its sole one-colored edge in \(f\). If \(e\) is internal, both orientation witnesses can be chosen as this same path, and both fail after restoration.
2. There is no zero-colored full geodesic from \(z\) in \(f_e\). Precisely one witness contains \(e\); the other avoids it and already supplies the opposite orientation in \(f\).

If both initially chosen witnesses fail upon restoration, the first alternative holds with \(e\) internal.

*Proof.* A pair surviving restoration would make \(z\) paired in \(f\), contradicting its choice. Thus a failing witness contains \(e\). If a zero-colored full geodesic exists from \(z\) in \(f_e\), it contains \(e\), since \(f\) has no monochromatic full geodesic: such a path would make its root paired. This gives alternative 1, including its internal-edge assertion.

Otherwise choose witnesses \(P_0,P_1\) of the two types. If both contain \(e\), both read it as zero. Every path from the same root traverses a given cube edge in the same orientation and with the same set of preceding dimensions. Splice the zero prefix of \(P_0\), through \(e\), with the zero suffix of \(P_1\), after \(e\). Their dimension sets partition \([d]\), giving a zero-colored full geodesic in \(f_e\), a contradiction. Hence precisely the failing witness contains \(e\), proving alternative 2.

For the final assertion, restoring a zero entry in a \(0^*1^*\) word destroys that form only if another zero occurs later. Restoring a zero entry in a \(1^*0^*\) word destroys that form only if another zero occurs earlier. Thus failure of both witnesses forces the common edge \(e\) to be internal. The same splice proves the first alternative. \(\square\)

##### Locating the remaining obstruction in directed zero arms

For a root \(z\), direct every edge away from \(z\) by increasing Hamming distance. Let \(F_z(f)\) be the vertices reachable from \(z\) by zero-colored directed paths, and let \(B_z(f)\) be the vertices from which \(\bar z\) is reachable by zero-colored directed paths. Directed paths use each dimension at most once.

**Proposition 23 (zero-arm separation and repair factorization).** In a coloring without paired roots,
\[
F_z(f)\cap B_z(f)=\varnothing\qquad\text{for every }z.
\]
For a repaired edge oriented \(u\to v\), let \(R_0(v)\) be the vertices reachable from \(v\) by original zero-colored directed paths, and let \(L_0(u)\) be the vertices that can reach \(u\) by such paths. Then
\[
F_z(f_e)=F_z(f)\cup
\begin{cases}
R_0(v),&u\in F_z(f),\\
\varnothing,&u\notin F_z(f),
\end{cases}
\]
and
\[
B_z(f_e)=B_z(f)\cup
\begin{cases}
L_0(u),&v\in B_z(f),\\
\varnothing,&v\notin B_z(f).
\end{cases}
\]
In particular, if both opposite orientation types are newly created at \(z\), then \(u\in F_z(f)\), \(v\in B_z(f)\), and repair joins these original zero arms into a zero-colored full geodesic.

*Proof.* A vertex in both sets splices two zero paths into a full zero geodesic, whose root is paired. A new zero path after repair must use \(e\) once. Its prefix ending at \(u\) and its suffix starting at \(v\) use original zero edges. Conversely any such concatenation is directed, and therefore dimension-simple; this proves the formulas.

A newly created \(0^*1^*\) witness must use \(e\) in its zero prefix, since a path avoiding \(e\) survives restoration. Hence \(u\in F_z(f)\). A newly created \(1^*0^*\) witness similarly forces \(v\in B_z(f)\). Joining those arms across \(e\) gives the final conclusion. \(\square\)

**Closure target.** By Theorems 19 and 21, it suffices to exclude a binary cube-edge coloring with disjoint sets \(A_0,A_1\) for which every one-edge repair creates a paired root. Propositions 22–23 divide its critical witnesses into isolated-edge exceptions and a new orientation coupled to an existing opposite orientation. A successful exchange argument must force compatible original zero arms or a surviving opposite path pair at one root. The directed support keeps every splice dimension-simple.

The bridge criterion and its direct doubled-cube interpretation were exhaustively compared for all \(2\), \(16\), and \(4096\) edge colorings of \(Q_1,Q_2,Q_3\), including every legal bridge assignment. The general statements above are proved by the arm decomposition; the universal paired-root assertion remains the closure step.


#### Counting counterexample bridge fibers via antipodal root profiles

Use the universal bridge family \(C(f,h)\) of Theorem 19: arbitrary horizontal coloring \(f\) of \(Q_d\), upper-layer antipodal complement, and vertical bits \(h(\bar z)=1-h(z)\). Let \(A_0(f)\) be the roots admitting a complete \(0^*1^*\) geodesic in \(f\). Reversing a full path gives \(A_1(f)=\bar A_0(f)\).

For each antipodal root pair \(P=\{z,\bar z\}\), put \(a(P)=|P\cap A_0(f)|\in\{0,1,2\}\), and let \(N_j\) count pairs with \(a(P)=j\).

**Theorem 24 (bridge-fiber enumeration).** Of the \(2^{2^{d-1}}\) legal assignments of vertical bridge colors, the number producing a cube coloring with no monochromatic full antipodal geodesic is
\[
\boxed{
\#\{h:C(f,h)\text{ is bad}\}=
\begin{cases}
0,&N_2>0,\\
2^{N_0},&N_2=0.
\end{cases}}
\tag{18}
\]
If \(N_2=0\), this count equals \(2^{2^{d-1}-|A_0(f)|}\).

*Proof.* For a representative \(z\) of each antipodal root pair, Theorem 19 permits a favorable full geodesic through its bridge whenever
\[
h(z)\in B_z=\{0:z\in A_0(f)\}\cup\{1:\bar z\in A_0(f)\}.
\]
The set \(B_z\) has size \(a(P)\). If \(a(P)=2\), either legal bridge bit gives a favorable path, eliminating all bad assignments. If \(a(P)=1\), precisely one bit choice forbids a favorable path through that root pair. If \(a(P)=0\), both bit choices forbid it. The bridge bits on different antipodal pairs are independent, so multiplying their numbers of forbidden choices gives the displayed count. If no pair contains two members of \(A_0\), each element of \(A_0\) belongs to a different antipodal pair, proving \(N_1=|A_0|\) and \(N_0=2^{d-1}-|A_0|\). QED.

**Corollary 25 (probability and root-density reformulation).** For uniformly random legal bridge bits \(h\), the probability that \(C(f,h)\) is bad is zero when \(A_0(f)\) contains an antipodal pair, and otherwise
\[
\boxed{\Pr_h[C(f,h)\text{ bad}]=2^{-|A_0(f)|}.}
\]
Thus a hypothetical lower-dimensional coloring with no paired root and larger \(A_0\) creates fewer bad bridge assignments; one with every antipodal pair meeting \(A_0\) on one side gives only one bad assignment. This is a counting refinement of the paired-root criterion, not a proof that a paired root must exist.

#### Root-profile barriers and the middle ranks of a critical pair

The paired-root route requires the paths' color arms and dimension supports. Two simpler closure proposals, based on root density and neighboring root labels, have explicit obstructions.

**Theorem 26 (complete root profile of the parity-reader coloring).** Let \(d=2r\ge2\), and color a direction-\(i\) edge by
\[
f_i(x)=\sum_{j\ne i}x_j\pmod2.
\]
Writing \(|x|\) for Hamming weight, its root sets are
\[
\boxed{
A_0(f)=\{x:|x|=r\text{ or }r+(-1)^r\},\qquad
A_1(f)=\{x:|x|=r\text{ or }r-(-1)^r\}.
}
\]
Their intersection is precisely the middle layer. Hence
\[
|A_0|=\binom{2r}{r}+\binom{2r}{r+1},\qquad
|A_0\cap A_1|=\binom{2r}{r}.
\]
Both densities tend to zero as \(r\) grows. In particular \(|A_0|<2^{d-1}\) for every even \(d\ge8\).

*Proof.* For a dimension order \(\pi\) rooted at \(x\), let \(p=|x|\bmod2\). Its edge-color word is
\[
a_t=p+(t-1)+x_{\pi_t}\pmod2,\qquad1\le t\le d.
\]
To obtain \(0^k1^{d-k}\), the ordered root bits must therefore read \(p+(t-1)\) before the switch and its complement afterwards. If \(k\) is even, both blocks have even length, and precisely \(r\) root bits are one. If \(k\) is odd, both blocks have odd length and each begins with bit \(p\). Thus the weight is \(r-1\) when \(p=0\) and \(r+1\) when \(p=1\). Consistency with the parity of the root weight leaves precisely \(r+(-1)^r\). Conversely, any root with one of these weights supplies the required bit sequence by ordering its zero-bit and one-bit dimensions appropriately. This proves \(A_0\); antipodal reversal proves \(A_1\).

The two binomial densities tend to zero by the central-binomial estimate. More explicitly, put \(s_r=2^{-2r}(\binom{2r}{r}+\binom{2r}{r+1})\). Then \(s_4=126/256<1/2\) and \(s_{r+1}/s_r=(2r+3)/(2r+4)<1\), proving the final assertion. \(\square\)

This is the atomic-stationary family classified in the incidence-cocycle subsection, now with its complete paired-root profile. It has paired roots and monochromatic full paths while most roots eventually have neither one-switch orientation. A universal positive-density lower bound for paired roots, or a greater-than-half bound for \(A_0\), cannot establish closure.

**Lemma 27 (constant-direction extension of root profiles).** Extend any coloring \(f\) of \(Q_d\) to \(Q_{d+k}\) by making its old edge colors independent of the new bits and coloring every new direction by a fixed bit \(c\). Then
\[
A_b(f^{\mathrm{ext}})=A_b(f)\times Q_k\qquad(b=0,1).
\]

*Proof.* Projecting a full geodesic to its old directions deletes entries from its color word, preserving each of the forms \(0^*1^*\) and \(1^*0^*\). Conversely, insert the new constant-colored directions into the appropriate constant block of any old witness, including at an endpoint if that block was empty. This gives a full witness from every root in the corresponding fiber. \(\square\)

**Proposition 28 (adjacent exclusive orientations in every dimension at least four).** For every \(d\ge4\), there is a binary edge coloring with adjacent roots
\[
z\in A_0\setminus A_1,\qquad w\in A_1\setminus A_0.
\]

*Proof.* Begin in \(Q_4\) with the parity-reader coloring of Theorem 26, using bit indices \(0,1,2,3\). Change just the edge \(\{e_0,e_0+e_1\}\) from one to zero. Take \(z=0\) and \(w=e_1\).

At \(z\), every unmodified dimension order has word \(0101\). A full path uses the changed edge precisely when its first two dimensions are \(0,1\), in that order; its new word is \(0001\). Thus \(z\in A_0\setminus A_1\).

Originally \(w\), of weight one, belongs to \(A_1\setminus A_0\) by Theorem 26. A full path from \(w\) uses the changed edge precisely when its first two dimensions are again \(0,1\). Its new word is \(1010\), which creates no \(0^*1^*\) witness. The dimension order \((2,1,0,3)\) avoids that edge and retains word \(1110\), so \(w\in A_1\setminus A_0\). The two roots are adjacent. Apply Lemma 27 for every larger dimension. \(\square\)

This example has many paired roots elsewhere. Its role is to exclude a local rule that adjacent exclusive opposite orientations must already yield a pair at one of those two roots. A closure argument must retain the path witnesses.

**Proposition 29 (separation throughout the middle ranks of a critical repair).** Let \(f\) be the minimum obstruction of Theorem 21. Suppose repairing \(e\) creates a paired root \(z\), with no zero-colored full geodesic from \(z\) in \(f_e\). Let the two witnesses have words
\[
P_0:0^{k_0}1^{d-k_0},\qquad
P_1:1^{k_1}0^{d-k_1}.
\]
Then \(1\le k_0,k_1<d\). At every rank
\[
\min(k_0,k_1)\le t\le\max(k_0,k_1),
\]
their vertices are different. Precisely one witness uses \(e\), and restoring it destroys that witness's orientation.

*Proof.* A one-colored full geodesic in \(f_e\) would also be one-colored in \(f\), since repair only changes one to zero; this would give a paired root in \(f\). By hypothesis there is no zero-colored full geodesic from \(z\). Thus both color blocks in each witness are nonempty.

Suppose the two paths share a vertex of rank \(t\). If \(k_1\le t\le k_0\), splice the zero prefix of \(P_0\) to the zero suffix of \(P_1\). If \(k_0\le t\le k_1\), splice the one prefix of \(P_1\) to the one suffix of \(P_0\). Each splice uses complementary dimension sets, so it gives a monochromatic full geodesic from \(z\). Both possibilities were excluded. Proposition 22 supplies the last assertion. \(\square\)

The critical paired witnesses therefore carry a separated interval of Boolean ranks, together with the single edge whose restoration breaks one orientation and an opposite companion path that avoids it. An intersection at a rank with \(k_0\le t\le k_1\) would give an original one-colored full geodesic and contradict the obstruction. An intersection in the opposite rank order gives a zero-colored repaired geodesic and reduces to the isolated-edge case. The root-profile barriers above show why this requires arm and support data rather than only the roots' labels or their cardinalities.



#### Rooted monotone-witness intersection and a spectral closure target

The universal bridge criterion in Theorem 19 converts NORI1 for \(Q_{d+1}\) into a paired-root assertion for an *arbitrary* binary coloring \(f\) of \(Q_d\). This section records a positive integral intersection formula, its Walsh spectral form, and a calibration showing why root density or the first two aggregate moments cannot be a proof invariant.

For a root \(z\), let
\[
P_f(z)=\#\{\pi\in S_d:
\text{the full path from }z\text{ in dimension order }\pi
\text{ has word }0^*1^*\}.
\]
Define
\[
\mathcal I(f)=\sum_{\{z,\bar z\}}P_f(z)P_f(\bar z),
\tag{19}
\]
with the sum over unordered antipodal vertex pairs. Reversing a \(0^*1^*\) full path from \(\bar z\) gives a \(1^*0^*\) full path from \(z\). Consequently
\[
\boxed{\mathcal I(f)>0
\quad\Longleftrightarrow\quad
f\text{ has a paired root}.}
\tag{20}
\]
This is the integral intersection number that the closure route must force to be positive.

**Theorem 30 (antipodal Walsh intersection identity).** Write the normalized Walsh coefficients
\[
\widehat P_f(S)=2^{-d}\sum_{z\in Q_d}
P_f(z)(-1)^{\sum_{i\in S}z_i}.
\]
Then
\[
\boxed{\mathcal I(f)=2^{d-1}
\left(
\sum_{|S|\text{ even}}\widehat P_f(S)^2
-
\sum_{|S|\text{ odd}}\widehat P_f(S)^2
\right).}
\tag{21}
\]
Thus the universal paired-root assertion, and hence NORI1 one dimension higher, is equivalent to strict dominance of the even Walsh energy of the *rooted monotone-witness count* over its odd Walsh energy for every arbitrary \(f\).

*Proof.* The Walsh characters diagonalize the antipodal translation \(z\mapsto\bar z\), with eigenvalue \((-1)^{|S|}\). Parseval applied to the inner product of \(P_f(z)\) and \(P_f(\bar z)\) gives
\[
2^{-d}\sum_zP_f(z)P_f(\bar z)
=\sum_S(-1)^{|S|}\widehat P_f(S)^2.
\]
The unordered antipodal sum in (19) is half the full sum. This proves (21); the positivity criterion (20) proves the equivalence. \(\square\)

The crude sufficient condition \(\operatorname{Var}_zP_f(z)<(\mathbb E_zP_f(z))^2\) would follow by keeping only the constant Walsh term and discarding the positive even nonconstant terms. It is *not* universally valid, even when many paired roots exist.

**Theorem 31 (full rooted multiplicity for the parity-reader coloring).** Let \(d=2r\ge2\), and let
\[
f_i(x)=\sum_{j\ne i}x_j\pmod2.
\]
Put \(q_r=(r+1)(r!)^2\). Then
\[
\boxed{
P_f(z)=
\begin{cases}
q_r,&|z|=r\text{ or }r+(-1)^r,\\
0,&\text{otherwise}.
\end{cases}}
\tag{22}
\]
Therefore
\[
\boxed{
\mathcal I(f)=\frac12\binom{2r}{r}q_r^2>0.}
\tag{23}
\]
If \(p_r=2^{-2r}\bigl(\binom{2r}{r}+\binom{2r}{r+1}\bigr)\) is the fraction of roots having \(P_f(z)>0\), then
\[
\boxed{
\frac{\operatorname{Var}P_f}{(\mathbb EP_f)^2}
=\frac{1-p_r}{p_r}\longrightarrow\infty.
}
\tag{24}
\]

*Proof.* Along an order \(\pi\), the edge colors from a root of weight \(w\), with parity \(p=w\bmod2\), are
\(a_t=p+(t-1)+z_{\pi_t}\pmod2\). To obtain a prescribed monotone word \(0^k1^{d-k}\), the root bits in that permutation must be \(p+(t-1)\) for \(t\le k\) and \(p+t\) for \(t>k\). For an even cut \(k\), the required bit string has weight \(r\), with \(r+1\) possible even cuts. For an odd cut, it has weight \(r-1\) if \(p=0\) and weight \(r+1\) if \(p=1\), giving the permitted other weight \(r+(-1)^r\), with \(r\) possible cuts. Each prescribed bit string of root weight \(w\) occurs under \(w!(d-w)!\) permutations. Therefore \(P_f=(r+1)(r!)^2\) on the middle layer and
\(P_f=r(r+1)!(r-1)!=(r+1)(r!)^2\) on the other permitted layer. Every other root has no witness.

The antipode preserves weight \(r\) and interchanges the other permitted weight with the excluded weight \(r-(-1)^r\). Thus only the \(\binom{2r}{r}/2\) antipodal middle-layer pairs contribute to (19), giving (23). Since \(P_f\) is \(q_r\) times the indicator of a set of density \(p_r\), its squared coefficient of variation is \((1-p_r)/p_r\). The central-binomial estimate gives \(p_r\to0\), proving (24). \(\square\)

**Proposition 32 (unweighted paired-path parity is not a recoloring invariant).** Already for arbitrary binary colorings of \(Q_4\), \(\mathcal I(f)\bmod2\) can change after recoloring. For all-zero \(f\), every root has \(P_f(z)=24\), giving \(\mathcal I(f)=4608\), even. If only the three edges
\[
\{0000,0001\},\quad
\{0000,0010\},\quad
\{0100,0101\}
\tag{25}
\]
have bit one (with bit positions read from the least significant end), direct enumeration of the 24 dimension orders at each root gives
\[
(P_f(0),\ldots,P_f(15))
=(10,16,17,18,14,16,19,18,18,19,21,20,18,22,22,22)
\]
and hence
\[
\boxed{\mathcal I(f)=2571,\quad\text{odd}.}
\tag{26}
\]
Thus a direct mod-two degree based only on unweighted path-pair counts cannot be preserved by arbitrary edge recoloring, even though both colorings have abundant paired roots. A successful topological intersection proof must use supported chains, refined orientations, or a different equivariant index.

**Closure objective.** The bridge criterion reduces the conjecture to proving strict positivity in (21) for every coloring \(f\). The parity-reader family shows that a proof cannot rely on any fixed positive density of good roots or on \(\operatorname{Var}P_f<(\mathbb EP_f)^2\); the nonconstant *even* Walsh levels are essential. The critical-repair separation of Proposition 29 supplies geometric information not represented by the raw overlap (19). A possible next proof is a supported chain lift of this overlap whose nonzero index survives edge recoloring and whose intersections splice into dimension-simple paired roots.



#### Transfer determinants for one-edge critical repairs

The preceding spectral overlap formula counts paired-root witnesses globally. We now obtain an edge-local factorization of its underlying rooted monotone path counts. It is valid for every arbitrary edge coloring of \(Q_d\), not merely those satisfying an antipodal relation, and uses only dimension-simple directed paths.

Fix a root \(z\) and orient each cube edge from smaller to larger Hamming distance from \(z\). For vertices \(u,v\), let \(F_{0,z}(u)\) and \(F_{01,z}(u)\) count directed paths from \(z\) to \(u\) whose color words are respectively all zero and \(0^*1^*\). Let \(B_{1,z}(v)\) and \(B_{01,z}(v)\) count directed paths from \(v\) to \(\bar z\) whose words are all one and \(0^*1^*\). Empty paths count once. Define \(F_{1,z},F_{10,z},B_{0,z},B_{10,z}\) similarly for the other word orientation.

**Theorem 33 (signed transfer determinants).** Let \(e=uv\) be an edge of color one, oriented \(u\to v\) away from \(z\), and let \(f_e\) be the coloring obtained by changing only \(e\) to zero. With \(P_f(z)\) the number of rooted \(0^*1^*\) full geodesics and \(Q_f(z)\) the number of \(1^*0^*\) geodesics, one has
\[
\boxed{
P_{f_e}(z)-P_f(z)=
F_{0,z}(u)B_{01,z}(v)
-F_{01,z}(u)B_{1,z}(v),
}
\tag{27}
\]
\[
\boxed{
Q_{f_e}(z)-Q_f(z)=
F_{10,z}(u)B_{0,z}(v)
-F_{1,z}(u)B_{10,z}(v).
}
\tag{28}
\]
The right side of (27) is the determinant of the two path-count vectors
\((F_{0,z}(u),F_{01,z}(u))\) and \((B_{1,z}(v),B_{01,z}(v))\), with the latter's entries ordered as displayed.

*Proof.* All rooted geodesics avoiding \(e\) contribute identically before and after repair. A full geodesic using \(e\) in the original coloring, with \(f(e)=1\), has a \(0^*1^*\) word if and only if its prefix up to \(u\) is \(0^*1^*\) and its suffix after \(v\) is entirely one. Such paths are counted by \(F_{01,z}(u)B_{1,z}(v)\). In the repaired coloring, \(e\) has color zero, so the entire prefix up to \(u\) must be all zero and the suffix after \(v\) may be \(0^*1^*\), giving \(F_{0,z}(u)B_{01,z}(v)\). Every such concatenation is a dimension-simple full geodesic because all pieces increase Hamming distance from \(z\); their traversed dimension sets are disjoint. Subtracting yields (27). The same argument for \(1^*0^*\) words gives (28): the original one-colored edge requires an all-one prefix and a \(1^*0^*\) suffix, whereas after repair the prefix may be \(1^*0^*\) and the suffix must be all zero. \(\square\)

**Corollary 34 (critical empty-root repair and monochromatic arm splice).** Suppose \(P_f(z)=Q_f(z)=0\), but a single repair \(f_e\) makes both positive at \(z\). Then, orienting \(e=u\to v\) away from \(z\),
\[
\boxed{F_{0,z}(u)>0,\qquad B_{0,z}(v)>0.}
\tag{29}
\]
Thus \(f_e\) has a monochromatic zero full geodesic from \(z\) passing through \(e\). In particular, if a critical repair \(e\) produces a paired root but no repaired zero geodesic, that root had at least one monotone orientation already before repair.

*Proof.* Since \(P_f(z)=0\), equation (27) and the positivity of \(P_{f_e}(z)\) imply
\(F_{0,z}(u)B_{01,z}(v)>0\), so its first factor is positive. Similarly (28), \(Q_f(z)=0\), and \(Q_{f_e}(z)>0\) imply \(F_{10,z}(u)B_{0,z}(v)>0\), so its second factor is positive. Concatenate the original all-zero prefix ending at \(u\), the repaired zero edge \(uv\), and the original all-zero suffix from \(v\) to \(\bar z\). All pieces are directed away from \(z\), so each dimension is used once. \(\square\)

**Lemma 35 (the path-count influence kernel).** For any edge \(e\) in direction \(i\), every root \(z\) gives an orientation \(u\to v\) of \(e\) away from \(z\), with \(k=d_{Q_d}(z,u)\). Precisely
\[
\boxed{k!(d-1-k)!}
\tag{30}
\]
complete dimension-simple rooted geodesics from \(z\) contain \(e\). Hence
\[
\boxed{|P_{f_e}(z)-P_f(z)|\le k!(d-1-k)!},
\tag{31}
\]
and summing the influence envelope over all roots gives
\[
\boxed{\sum_{z\in Q_d} k_z!(d-1-k_z)!=2d!.}
\tag{32}
\]

*Proof.* To use \(e\) in a full geodesic from \(z\), the path must first traverse the \(k\) dimensions on which \(z\) and \(u\) differ, then direction \(i\), then the other \(d-1-k\) dimensions. The two outer blocks may be ordered arbitrarily, proving (30). Recoloring \(e\) cannot affect paths avoiding it, giving (31). For a fixed edge and each \(k\), precisely \(2\binom{d-1}{k}\) roots have nearer endpoint distance \(k\). Sum (30) over these roots to obtain \(2\sum_{k=0}^{d-1}(d-1)!=2d!\). \(\square\)

**Closure significance.** In the minimal-one-edge obstruction of Theorem 21, every one-colored edge \(e\) must create a paired root when deleted. Equations (27)--(28) now express the creation of each missing orientation as strict positivity of a **signed rank-two prefix/suffix determinant**. Corollary 34 isolates the only two kinds of critical repair: a new zero full geodesic across \(e\), or a newly repaired orientation paired with an orientation already present in the original coloring. A proof of the unrestricted paired-root lemma would follow from a global coherence/cancellation identity forcing a contradiction among these determinants over all critical edges. Unlike unweighted root-pair parity, the determinants retain direction support and the relative location of the two color blocks; establishing their square-exchange and antipodal coherence is the remaining substantive task.



#### Two-state transfer algebra and curvature-twisted square coherence

The rooted transfer determinants above arise from a two-state path automaton. Its rank-two finite differences obey an explicit square-exchange law that keeps every intermediate path dimension-simple.

For a color bit \(b\in\{0,1\}\), put
\[
T_0=\begin{pmatrix}1&0\\0&0\end{pmatrix},
\quad T_1=\begin{pmatrix}0&0\\1&1\end{pmatrix},
\quad B=T_0-T_1=
\begin{pmatrix}1&0\\-1&-1\end{pmatrix}.
\tag{33}
\]
If the successive bits of a directed path are \(b_1,\ldots,b_k\), the scalar
\[
\boxed{(1,1)T_{b_k}\cdots T_{b_1}(1,0)^T}
\tag{34}
\]
equals one precisely when the path word has type \(0^*1^*\), and zero otherwise. In particular
\[
\boxed{T_0^2=T_0,\quad T_1^2=T_1,\quad
T_0T_1=0,\quad B^2=I.}
\tag{35}
\]
The difference of the zero-edge and one-edge transition operators is an involution.

Fix a root \(z\), orient every cube edge away from \(z\), and write \(a\preceq_z b\) when \(b\) is reachable from \(a\) by such a directed path. Define \(\mathscr T_f(a,b)\) as the sum of \(T_{b_k}\cdots T_{b_1}\) over every dimension-simple directed path \(a\to b\), and set \(\mathscr T_f(a,a)=I\). The number of full \(0^*1^*\) geodesics from \(z\) is
\[
P_f(z)=(1,1)\mathscr T_f(z,\bar z)(1,0)^T.
\]

**Theorem 36 (factorized first variation).** For a directed edge \(e=u\to v\), let \(D_e\) denote the formal difference between setting its bit to zero and setting it to one, holding all other edge bits fixed. Then
\[
\boxed{D_e\mathscr T_f(z,\bar z)
=\mathscr T_f(v,\bar z)\,B\,\mathscr T_f(z,u).}
\tag{36}
\]

*Proof.* All paths avoiding \(e\) cancel. Any path containing \(e\) uniquely decomposes into a prefix \(z\to u\), edge \(e\), and suffix \(v\to\bar z\). Its matrix product is suffix times edge times prefix, and the two transition matrices differ by \(B\). Every concatenation is still dimension-simple because its Hamming-distance rank strictly increases. Summing independently over the prefix and suffix families proves (36). \(\square\)

**Theorem 37 (curvature-twisted second variation on every square).** Let \(F\) be any cube square, with bottom \(u\), top \(w\), and intermediate vertices \(v_i=u\oplus e_i,v_j=u\oplus e_j\) under the ordering directed away from \(z\). Denote its two ascending routes by
\[
a=(u,v_i),\ b=(v_i,w),\qquad
a'=(u,v_j),\ b'=(v_j,w).
\]
The *formal* second variations satisfy
\[
\boxed{D_aD_b\mathscr T_f(z,\bar z)
=D_{a'}D_{b'}\mathscr T_f(z,\bar z)
=\mathscr T_f(w,\bar z)\mathscr T_f(z,u).}
\tag{37}
\]
Let \(\Delta_e\) instead denote toggling the original bit of \(e\). Then
\[
\boxed{
\Delta_a\Delta_b P_f(z)
=(-1)^{\kappa_f(F)}\Delta_{a'}\Delta_{b'}P_f(z),
\qquad
\kappa_f(F)=f(a)+f(b)+f(a')+f(b')\pmod2.
}
\tag{38}
\]
The two second variations have the same nonnegative magnitude
\[
\boxed{
K_z(F)=(1,1)\mathscr T_f(w,\bar z)
\mathscr T_f(z,u)(1,0)^T.
}
\tag{39}
\]
Every identity holds for arbitrary cube-edge colorings and every root, with no antipodal hypothesis.

*Proof.* A directed full geodesic containing both edges of a given route must traverse those edges consecutively: after entering the intermediate vertex it cannot return there. The rest of the path consists of an independent prefix \(z\to u\) and suffix \(w\to\bar z\). Two formal bit differences insert \(B^2=I\) between the outer matrix sums, giving the last expression of (37). The alternate square route has the same start, end, prefix and suffix, so gives the same expression. Applying the accepting row and initial column vector yields (39), which is nonnegative since the transfer matrices have nonnegative entries.

For original bit \(b_e\), toggling rather than setting gives
\(\Delta_e=(2b_e-1)D_e\). The two-bit toggle multiplier on one route is therefore \((2b_a-1)(2b_b-1)=(-1)^{b_a+b_b}\). Comparing it with the alternate route gives the ratio \((-1)^{\kappa_f(F)}\), proving (38). \(\square\)

**Corollary 38 (rooted rank-two consistency).** The integer \(K_z(F)\) counts complete dimension-simple geodesics whose colored prefix before \(u\) and colored suffix after \(w\), concatenated while omitting the square's two edge bits, form a \(0^*1^*\) word. It is independent of the two square routes and all four square edge bits. The sole sign discrepancy between the two edge-pair toggle variations is the ordinary square curvature. Since \(\kappa_f=\delta f\), the sign twist obeys the three-cube identity \(\delta\kappa_f=0\). This verifies coherence of the *local signs*, not a root-changing equivariant homotopy.

**Remaining closure task.** The bridge theorem reduces NORI1 to paired-root existence for arbitrary lower-cube colorings. The preceding first-variation determinant describes the repair of each missing path orientation, while Theorem 37 provides the signed rank-two compatibility of those repairs along cubical squares. The missing step is to assemble these rooted matrices with antipodal root reversal into a global chain operation having nonzero Smith-transfer index. Unlike unweighted path-pair parity, the matrices retain both direction support and the two color phases.



#### Antipodal anti-involution and quantitative bridge witness counts

The two-state transfer algebra above has a natural reverse-complement symmetry. Combining it with the universal free-bridge construction of Theorem 19 yields the full number of monochromatic witnesses for every bridge assignment, not just a yes/no criterion.

Keep
\[
T_0=\begin{pmatrix}1&0\\0&0\end{pmatrix},
\qquad T_1=\begin{pmatrix}0&0\\1&1\end{pmatrix}.
\]
Define
\[
R=\begin{pmatrix}0&1\\1&-1\end{pmatrix},
\quad
R^{-1}=\begin{pmatrix}1&1\\1&0\end{pmatrix},
\qquad \Theta(M)=R M^T R^{-1}.
\tag{41}
\]

**Theorem 39 (reverse-complement duality of monotone transfer).** The map \(\Theta\) is an involutive anti-automorphism of the two-state matrix algebra, and
\[
\boxed{\Theta(T_0)=T_1,\quad \Theta(T_1)=T_0,\quad
\Theta(T_0-T_1)=-(T_0-T_1).}
\tag{42}
\]
For any binary word \(w\), writing \(w^\sharp\) for its reverse followed by bitwise complementation,
\[
\boxed{T(w^\sharp)=\Theta(T(w)).}
\tag{43}
\]
For any arbitrary coloring \(f\) of \(Q_d\), let \(1-f\) complement all its edge bits. Then its full transfer matrices obey
\[
\boxed{
\mathscr T_{1-f}(\bar z,z)
=\Theta(\mathscr T_f(z,\bar z)).
}
\tag{44}
\]
For an antipodally odd coloring \(c\) of \(Q_d\), its rooted transfer matrix is fixed under \(\Theta\):
\[
\boxed{\Theta(\mathscr T_c(z,\bar z))
=\mathscr T_c(z,\bar z).}
\tag{45}
\]
The sign reversal of \(B=T_0-T_1\) under \(\Theta\), together with \(B^2=I\), gives an algebraic explanation for the odd first variation and even square second variation.

*Proof.* Direct multiplication gives the three relations in (42). The symmetry \(R^T=R\) and \(R^{-T}=R^{-1}\) implies that \(\Theta^2\) is the identity, while transposition reverses product order. Applying \(\Theta\) to the matrix product of a word therefore reverses its order and exchanges the two colors, proving (43). Reversing a directed geodesic from \(z\) to \(\bar z\) produces a directed geodesic from \(\bar z\) to \(z\); complementing the coloring complements each edge bit. This is a bijection of all full dimension orders, proving (44). If \(c(Ae)=1-c(e)\), the coloring \(1-c\) is the antipodal pullback of \(c\), and inversion identifies the two corresponding full path families. This gives (45). \(\square\)

Fix an *arbitrary* coloring \(f\) of \(Q_d\). Let \(P_f(z)\) be its rooted \(0^*1^*\) full-geodesic count as defined above; by path reversal, the rooted \(1^*0^*\) count is \(P_f(\bar z)\). For an odd bridge assignment \(h(\bar z)=1-h(z)\), form the antipodally odd coloring \(C(f,h)\) of \(Q_{d+1}\) from Theorem 19. Let \(X_f(h)\) count **oriented monochromatic full geodesics directed from the lower face to the upper face** (each such path crosses a vertical bridge once).

**Theorem 40 (full quantitative bridge formula).** Choose a representative \(z_P\) from each antipodal root pair \(P=\{z,\bar z\}\). Then
\[
\boxed{
X_f(h)=2\sum_{P}
\begin{cases}
P_f(z_P),&h(z_P)=0,\\
P_f(\bar z_P),&h(z_P)=1.
\end{cases}}
\tag{46}
\]
In particular,
\[
\boxed{
\min_hX_f(h)=2\sum_P\min(P_f(z),P_f(\bar z)),
}
\tag{47}
\]
\[
\boxed{
\max_hX_f(h)=2\sum_P\max(P_f(z),P_f(\bar z)).
}
\tag{48}
\]
If \(h\) is chosen uniformly among all legal odd bridge assignments, then
\[
\boxed{
\mathbb E_hX_f(h)=\sum_{z\in Q_d}P_f(z),\qquad
\operatorname{Var}_hX_f(h)=
\sum_P(P_f(z)-P_f(\bar z))^2.
}
\tag{49}
\]
Furthermore, with \(\mathcal I(f)=\sum_PP_f(z)P_f(\bar z)\), the uniform lower bound
\[
\boxed{\min_hX_f(h)\ge\frac{2}{d!}\mathcal I(f)}
\tag{50}
\]
holds. Therefore the universal bridge condition is equivalent to the strict positivity of the minimum in (47), or of the Walsh overlap in (21).

*Proof.* Orient a monochromatic full geodesic from the lower cube face to the upper face and let \(z\) be the lower endpoint of its vertical bridge, with bit \(b=h(z)\). As in Theorem 19, reversing its lower horizontal arm and reflecting its upper horizontal arm gives a full directed geodesic of \(f\) from \(z\) to \(\bar z\) whose color word is \(b^* (1-b)^*\). Conversely this construction is reversible and uniquely reconstructs the lower-to-upper monochromatic geodesic, including its split position. The number of such paths using the bridge at \(z\) is therefore \(P_f(z)\) when \(b=0\), and \(P_f(\bar z)\) when \(b=1\).

Now pair \(z\) and \(\bar z\). If \(h(z)=0\), then \(h(\bar z)=1\), and the respective contributions at the two bridge endpoints are both \(P_f(z)\); if \(h(z)=1\), they are both \(P_f(\bar z)\). Summing proves (46). Distinct antipodal root pairs carry independent bridge choices, giving (47)--(48). For a pair with values \(a,b\), its random contribution is \(2a\) or \(2b\) with equal probabilities, having mean \(a+b\) and variance \((a-b)^2\). Independence proves (49).

Finally \(0\le P_f(z)\le d!\), so \(\min(a,b)\ge ab/d!\) for every pair. Summing in (47) proves (50). \(\square\)

**Corollary 41 (rooted \(L^1\) closure formulation).** The universal paired-root lemma, hence NORI1 in dimension \(d+1\), is equivalent to the strict inequality
\[
\boxed{
\sum_{z\in Q_d}P_f(z)>
\sum_{\{z,\bar z\}}
|P_f(z)-P_f(\bar z)|
\quad\text{for every arbitrary }f.
}
\tag{51}
\]
Both sides are intrinsic to monotone full geodesics in the lower cube. Unlike a density-greater-than-one-half proposal, (51) remains meaningful for the sparse parity-reader root profiles of Theorem 31.

*Proof.* Equations (47) and (49) give
\[
\min_hX_f(h)=
\sum_zP_f(z)-\sum_P|P_f(z)-P_f(\bar z)|.
\]
It is positive precisely when some antipodal root pair has two positive rooted path counts, by (47). Apply the bridge equivalence of Theorem 19. \(\square\)

**Proof-search implication.** The two-state path matrices now supply an explicit involutive antipodal duality and a curvature-twisted square second-variation identity. The quantitative bridge formula converts their rooted counts into a minimax intersection inequality (51). The remaining full proof would establish (51) for arbitrary lower-cube colorings, preferably by a supported equivariant chain index preserved under single-edge recolorings. The unweighted parity counterexample in Proposition 32 explains why a direct mod-two count is inadequate, while the transfer involution and square relation identify the additional algebraic structure available for such an index.


#### Root-reversal duality and antipodal seam certificates

The two-state transfer algebra has a support-preserving duality under root reversal and color complementation. It also suggests a geometric certificate in which the opposite path orientations have antipodal switch vertices.

**Theorem 42 (transfer duality under reversal).** Put
\[
J=\begin{pmatrix}1&1\\1&0\end{pmatrix},\qquad
K=JB=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]
For each bit \(b\),
\[
\boxed{T_b^T J=J T_{1-b},\qquad B^T J=-JB.}
\]
If \(a\preceq_z b\), and the reverse interval is ordered away from \(\bar z\), then
\[
\boxed{\mathscr T_f(b,a)^T J
       =J\mathscr T_{1-f}(a,b).}
\]
Thus this duality reverses each geodesic's dimension order and preserves its dimension support. The full-root scalar identity is
\[
P_f(\bar z)=P_{1-f}(z)=Q_f(z).
\]

*Proof.* Multiply the two displayed transition matrices to verify the local identity. For a path with bits \(b_1,\ldots,b_k\), the reversed transfer product is \(T_{b_1}\cdots T_{b_k}\). Transposing and moving \(J\) through its factors gives \(J T_{1-b_k}\cdots T_{1-b_1}\), the complemented forward product. Reversal is a bijection on the interval's directed geodesics, so sum the identity over those paths. Finally \(J(1,0)^T=(1,1)^T\), which converts the terminal scalar on the reversed interval into the accepting scalar on the complemented interval. \(\square\)

**Corollary 43 (positive-cone form of a critical determinant).** For an edge \(u\to v\), put
\[
p=\mathscr T_f(z,u)(1,0)^T,\qquad
q=J^{-1}\mathscr T_f(v,\bar z)^T(1,1)^T.
\]
Both vectors have nonnegative integer entries, and
\[
\boxed{D_e P_f(z)=q^T Kp=p_0q_1-p_1q_0.}
\]
More explicitly, \(p_0\) counts zero prefixes and \(p_1\) counts prefixes with a monotone word ending in one. The entry \(q_0\) counts one suffixes, while \(q_1\) counts monotone suffixes with an initial zero. The entries at empty intervals are defined by the matrix formula.

*Proof.* Every nonempty accepted word is all zero, all one, or of type \(0^+1^+\), with transfer matrix respectively \(T_0,T_1,T_1T_0\). Thus an interval transfer sum has form
\[
\begin{pmatrix}Z&0\\H+O&O\end{pmatrix},
\]
where \(Z,O,H\) count these three kinds of words. This proves the prefix description, while application of \(J^{-1}\) gives suffix vector \((O,Z+H)^T\). Empty intervals give \(p=(1,0)^T\) or \(q=(1,0)^T\), directly. The factorized first variation from Theorem 36 is
\[
(1,1)\mathscr T_f(v,\bar z)B\mathscr T_f(z,u)(1,0)^T
=q^T JBp,
\]
proving the determinant. \(\square\)

The matrix \(J\) has determinant \(-1\), so its symmetric form is indefinite. The duality gives an algebraic compatibility of root reversal with supported transfers. A global supported homotopy and a nonzero index remain to be established.

##### A quadrilateral certificate with antipodal switches

For any cube vertices \(a,b\), let \(Z_f(a,b)\) and \(O_f(a,b)\) count respectively zero-colored and one-colored geodesics using precisely the dimensions on which \(a,b\) differ. Empty paths count once. Define
\[
\mathcal R_f(z)=
\sum_{w\in Q_d}
Z_f(z,w)O_f(w,\bar z)
O_f(z,\bar w)Z_f(\bar w,\bar z).
\]
Let \(S(f)=\{z:\mathcal R_f(z)>0\}\).

**Theorem 44 (antipodal seam equivalence).** A root belongs to \(S(f)\) precisely when its two opposite-orientation witnesses can have switch vertices \(w,\bar w\), respectively. Therefore
\[
\boxed{S(f)\subseteq P(f),\qquad S(f)=\bar S(f).}
\]
A positive summand specifies a monochromatic geodesic quadrilateral: zero arms join \(z\) to \(w\) and \(\bar w\) to \(\bar z\), while one arms join \(w\) to \(\bar z\) and \(z\) to \(\bar w\). If neither color block is empty, its union is a simple \(2d\)-cycle; each of its two diagonals joins antipodal vertices.

*Proof.* Put \(U=\{i:z_i\ne w_i\}\). The zero arms use \(U\), and the one arms use \(U^c\). Concatenating the indicated zero and one arms gives a full \(0^*1^*\) path from \(z\); concatenating the one and zero arms gives a full \(1^*0^*\) path from the same root, with complementary switch vertices. Conversely such paths supply the four factors of a positive summand. Antipodal reversal of both witnesses preserves this condition, proving symmetry.

The two zero arms occupy opposite parallel \(U\)-faces, and the two one arms occupy opposite parallel \(U^c\)-faces. Any two adjacent arms meet only at their prescribed corner, because their varying dimension sets are disjoint. Opposite arms lie in disjoint faces. This proves the simple-cycle statement when both blocks are nonempty. \(\square\)

**Theorem 45 (antipodal seam preservation under a free new direction).** Extend \(f\) from \(Q_d\) to \(Q_d\times Q_1\) by keeping every old-direction edge color independent of the new bit, and assigning arbitrary colors \(h(x)\) to the new-direction edges. Then
\[
\boxed{S(f^{\mathrm{ext}})=S(f)\times Q_1.}
\]

*Proof.* Projection of an extended certificate erases the new direction from both witnesses. The resulting words retain their opposite monotone orientations, and their switch vertices remain antipodal after projection. Hence every extended root projects into \(S(f)\).

For the converse take a certificate with corners \(z,w,\bar z,\bar w\), and start in either new layer. Suppose each of the two zero arms has a corner where \(h=0\). Insert the new edge at one such corner of each zero arm. This puts the new direction in the zero dimension block, while the old one arms remain in their prescribed layers. The two new switch vertices are antipodal, so this gives an extended certificate.

If that condition fails, both corners of one zero arm have \(h=1\): either \(h(z)=h(w)=1\), or \(h(\bar w)=h(\bar z)=1\). Each of the two opposite one arms therefore has a corner where \(h=1\). Insert the new edge at these corners instead, putting the new direction in the one dimension block. Again the switch vertices are antipodal. This four-corner argument also covers an empty color block. \(\square\)

**Corollary 46 (Cartesian seam factorization).** For independent Cartesian factors,
\[
\boxed{S(f\boxtimes g)=S(f)\times S(g).}
\]

*Proof.* Project the two witnesses and their antipodal seams into each factor for one inclusion. Conversely concatenate the factors' zero prefixes, then their one suffixes, to make the first witness; concatenate their one prefixes, then zero suffixes, to make the other. Their switch vertices are the product of the first seams and its antipode. Every dimension is used once. \(\square\)

##### A local limitation of seam normalization

**Proposition 47 (a paired root can lack antipodal seams).** In \(Q_3\), color precisely the edges indexed by
\[
(x,i)\in\{(0,1),(0,2),(1,1),(1,2),(2,2)\}
\]
one, where \(x\) is the integer encoding of the endpoint with bit \(i\) zero; all other edges have color zero. Then \(z=1\) is paired and belongs to \(P(f)\setminus S(f)\).

*Proof.* In lexicographic dimension-permutation order, the six words from \(z=1\) are
\[
011,\ 010,\ 101,\ 100,\ 100,\ 100.
\]
The only \(0^*1^*\) switch vertex is \(0\). The \(1^*0^*\) switch vertices are \(3,5\). The antipode of \(0\) is \(7\), so none of these two opposite witnesses has an antipodal seam partner. The root is paired because both orientations occur. \(\square\)

**Closure proposal and status.** The assertion \(S(f)\ne\varnothing\) for every binary cube-edge coloring would imply the paired-root theorem and NORI1 one dimension higher. Theorems 45--46 show that this stronger certificate respects free-direction insertion and Cartesian decomposition. Proposition 47 shows that deriving it from a paired witness requires control of rerooting. The unrestricted certificate assertion and its implication from ordinary paired-root existence are unproved.

For validation, all \(1920\) distinct quadrilateral and monochromatic certificates in \(Q_4\) were encoded as Boolean forbidden-pattern inequalities on its \(32\) edge bits. The integer feasibility solver reported the joint avoidance system infeasible. This is a finite computational consistency check of the stronger proposal, rather than an all-dimensional proof.


#### Restoring an endpoint defect in an antipodal quadrilateral

An antipodal seam certificate permits restoration to be coupled with rerooting. This gives a contradiction rule stronger than the arbitrary paired-root repair classification.

**Theorem 48 (endpoint restoration forces an original paired root).** Let \(f\) have no paired root, let \(e\) have color one, and let \(f_e\) change its color to zero. Suppose \(f_e\) has a nondegenerate antipodal geodesic quadrilateral, with zero dimension block \(U\) and one dimension block \(U^c\), both nonempty. Then \(e\) lies strictly inside one of its zero arms. In particular
\[
\boxed{3\le |U|\le d-1.}
\]

*Proof.* If the quadrilateral avoided \(e\), it would already certify a paired root in \(f\). Since \(e\) has repaired color zero, it belongs to a zero arm. The two zero arms lie in disjoint parallel \(U\)-faces, so only one contains \(e\). All other arms retain their colors after restoration.

Name the affected zero arm \(z\to w\); the other is \(\bar w\to\bar z\), and the one arms are \(z\to\bar w\) and \(w\to\bar z\). Put \(k=|U|\).

If \(e\) is the final edge of \(z\to w\), its original word is \(0^{k-1}1\). Append the one arm \(w\to\bar z\), obtaining an original \(0^*1^*\) full geodesic from \(z\). The unaffected one arm \(z\to\bar w\), followed by the unaffected zero arm, gives the opposite orientation from the same root. Thus \(z\) was paired.

If \(e\) is the first edge, reverse the affected arm. From \(w\) its original word is \(0^{k-1}1\); append the one arm \(z\to\bar w\) to obtain \(0^*1^*\). The one arm \(w\to\bar z\), followed by the reverse of the unaffected zero arm, gives \(1^*0^*\) from \(w\). Thus \(w\) was paired. The same argument applies to the other zero arm after relabeling the corners. Both endpoint cases contradict the hypothesis. An internal edge requires \(k\ge3\), and nondegeneracy gives \(k\le d-1\). \(\square\)

**Corollary 49 (an empty antipodal root pair in the affected face).** Under Theorem 48, let the affected zero arm run from \(z\) to \(w\), and let \(H\) be its \(U\)-face. In the original restricted coloring \(f|_H\), neither \(z\) nor \(w\) admits either monotone orientation to the other. Repair makes them joined by a zero-colored full \(H\)-geodesic. Moreover, every zero-colored \(z\)-to-\(w\) geodesic in \(f_e|_H\) must contain \(e\) internally.

*Proof.* An original \(0^*1^*\) geodesic from \(z\) to \(w\), followed by the unaffected one arm to \(\bar z\), would give that orientation at the full root \(z\). Its unaffected opposite witness would then make \(z\) paired in \(f\). An original \(0^*1^*\) geodesic from \(w\) to \(z\) gives the same contradiction at \(w\). Reversal excludes the other orientation at each face root.

Repair supplies the prescribed zero arm. Any repaired zero arm avoiding \(e\) would yield an original quadrilateral; any with \(e\) at an endpoint would contradict Theorem 48. This proves the last assertion. \(\square\)

**Inductive closure implication.** Choose a hypothetical paired-root counterexample in the least dimension, and then minimize its one-edge count. Every repaired coloring has a paired root. If a repair supplies a nondegenerate antipodal seam certificate, Theorem 48 confines its defect to a proper face of at least three dimensions. That face has an empty antipodal pair at the certificate's corners by Corollary 49, while the least-dimension hypothesis supplies paired roots elsewhere in the same face. Thus closure can proceed by transporting a lower-dimensional paired root to the quadrilateral interface, or by showing that a critical repair must admit an endpoint-defect certificate. These transport assertions remain unproved.



#### Reciprocal doubling gives a unimodular self-dual positive transfer module

The positive \(q\)-deformation of rooted monotone-geodesic transfer introduces reciprocal parameters \(q\) and \(q^{-1}\) under reversal-complementation. A two-state bilinear duality cannot identify these at one fixed \(q\ne1\), but a four-state direct-sum module does. Importantly the doubled model has **entrywise nonnegative** transition matrices and an **integral unimodular** reversal pairing, with no need to invert \(q\) in its coefficients.

Let
\[
T_0=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
T_1=\begin{pmatrix}0&0\\1&1\end{pmatrix},\quad
R=\begin{pmatrix}0&1\\1&-1\end{pmatrix},
\quad S=R^{-1}=\begin{pmatrix}1&1\\1&0\end{pmatrix}.
\]
For an indeterminate \(q\) (or any positive real specialization), define four-state operators
\[
V_0(q)=\operatorname{diag}(qT_0,T_0),\quad
V_1(q)=\operatorname{diag}(T_1,qT_1),\quad
\mathcal J=\begin{pmatrix}0&S\\S&0\end{pmatrix}.
\tag{52}
\]
The first channel is the weighted automaton \(U_b(q)\); the second is the automaton \(q U_b(q^{-1})\), so a length-\(k\) path has channel matrices \(U_q(P)\) and \(q^kU_{q^{-1}}(P)\). No negative powers of \(q\) occur in the four-state edge operators.

**Theorem (fixed-parameter reciprocal bilinear duality).** Over \(\mathbb Z[q]\),
\[
\boxed{V_b(q)^T\mathcal J=\mathcal J V_{1-b}(q)
\quad(b=0,1).}
\tag{53}
\]
The matrix \(\mathcal J\) is symmetric, nondegenerate and unimodular, with determinant \(1\), and has real signature \((2,2)\). Writing \(D(q)=V_0(q)-V_1(q)\), one has
\[
\boxed{D(q)^T\mathcal J=-\mathcal J D(q),\qquad
(D(q)^k)^T\mathcal J=(-1)^k\mathcal J D(q)^k.}
\tag{54}
\]
For any full dimension-simple path \(P\) with bit word \(w\), if \(w^\sharp\) is the reversal of its bitwise complement, then
\[
\boxed{V(w)^T\mathcal J=\mathcal J V(w^\sharp),}
\tag{55}
\]
where \(V(w)=V_{w_{|w|}}\cdots V_{w_1}\). Thus root reversal with antipodal color complementation is represented by **one fixed unimodular bilinear pairing** on a four-state module.

*Proof.* The two-state reciprocity identity \(U_b(q)^TS=qS U_{1-b}(q^{-1})\) follows from \(T_b^TS=S T_{1-b}\). The off-diagonal blocks of \(V_b^T\mathcal J\) are therefore \(U_b(q)^TS\) and \(qU_b(q^{-1})^TS\), respectively equal to the off-diagonal blocks of \(\mathcal J V_{1-b}\), proving (53). The determinant of \(S\) is \(-1\), and \(\det\mathcal J=\det(S)^2=1\). The symmetric off-diagonal form has equal positive and negative inertia. Subtract (53) for the two colors to obtain the first identity of (54); raise it to successive powers for the second. Applying (53) to each factor of the transfer product, with transpose reversing factor order, proves (55). \(\square\)

**Proposition (two-state and positive-metric obstructions).** For \(q\ne1\), there is no invertible two-by-two matrix \(J\) with
\[
U_0(q)^T J=J U_1(q),\quad U_1(q)^T J=J U_0(q).
\tag{56}
\]
Nor can the doubled operators in (52) satisfy the corresponding exchange relation for a positive-definite real symmetric \(J\), for any \(q>0\).

*Proof.* An invertible two-state \(J\) in (56) would make \(U_0(q)^T\) similar to \(U_1(q)\), whose traces are \(q\) and \(1\), forcing \(q=1\). For any dimension and a positive-definite \(J\), the adjoint relation gives \(V_1=J^{-1}V_0^TJ\). But \(V_0V_1=0\), since \(T_0T_1=0\) in both blocks. Therefore \(V_0J^{-1}V_0^TJ=0\). Multiplying by \(J^{-1}\) and taking the associated positive quadratic form forces \(V_0=0\), a contradiction. \(\square\)

**Scope for equivariant chains.** The four-state model reconciles positive transfer operators with *integral* reversal duality at fixed \(q\). Its skew-adjoint color difference gives coherent odd/even signs under all-rank face variations. Nevertheless the bilinear pairing is necessarily indefinite. Its existence supplies a compatible local coefficient system, not a nonvanishing global Smith index. Moreover reduction of path-count coefficients modulo two may cancel all witnesses at a root (for example, an all-zero \(d\)-cube has \(d!\) accepted full paths, an even number for \(d\ge2\)). A support-sensitive chain lift must retain individual path incidences or higher cells rather than relying on the parity of the scalar transfer sum.



#### Faithful path tags versus square-flat scalar transport

The reciprocal four-state module is self-dual, but characteristic-two scalar path summation may cancel all existing witnesses. The following gives a rigorous obstruction and a minimal higher-chain replacement.

Fix a root \(z\) of \(Q_d\), \(d\ge2\), and put an independent commuting indeterminate \(t_e\) on each undirected cube edge. Work over \(\mathcal R=\mathbb F_2[q,\{t_e\}]\). For an arbitrary coloring \(f\), define
\[
\boxed{\mathscr P_{f,q}(z;\mathbf t)
=\sum_{\substack{\pi\in S_d\\f(P(z,\pi))=0^k1^{d-k}}}
q^k\prod_{e\in P(z,\pi)}t_e.}
\tag{57}
\]

**Theorem 50 (faithful support and paired-root polynomial).** For every \(f,z\), the polynomial \(\mathscr P_{f,q}(z;\mathbf t)\) is nonzero if and only if a full \(0^*1^*\) geodesic from \(z\) exists. If \(r_{\{z,\bar z\}}\) are distinct indeterminates indexed by antipodal root pairs, then
\[
\boxed{\mathscr I_{f,q}=
\sum_{\{z,\bar z\}}r_{\{z,\bar z\}}
\mathscr P_{f,q}(z;\mathbf t)
\mathscr P_{f,q}(\bar z;\mathbf t)}
\tag{58}
\]
is nonzero if and only if a paired root exists.

*Proof.* Two different full geodesics from a fixed root have different edge sets: a simple path edge set and its initial vertex determine its entire order. Their tagged monomials therefore differ, so their sum cannot cancel in \(\mathcal R\). This proves the first assertion. The polynomial ring has no zero divisors, so a product of the two root polynomials is nonzero precisely when both are nonzero. Distinct variables \(r_{\{z,\bar z\}}\) prevent cancellation between different antipodal pairs. \(\square\)

**Theorem 51 (flat scalar tags necessarily lose support).** Let \(\mathcal K\) be any commutative ring of characteristic two with edge weights \(w_e\), satisfying on every directed square
\[
\boxed{w_{uv_i}w_{v_iw}=w_{uv_j}w_{v_jw}.}
\tag{59}
\]
Every full root-to-antiroot geodesic has the same weight \(W\). In the all-zero coloring its weighted monotone count is
\[
\boxed{\sum_{\pi\in S_d}q^d\prod_{e\in P(z,\pi)}w_e
=d!\,q^d W=0.}
\tag{60}
\]
Thus scalar multiplicative square-flatness is incompatible with detecting every rooted witness by nonvanishing of a characteristic-two transfer count.

*Proof.* Adjacent transpositions generate \(S_d\). Each replaces one square route by its other route, leaving prefix and suffix unchanged; (59) preserves its product weight. Therefore all full path products agree. The integer \(d!\) is even for \(d\ge2\), so the sum vanishes although all geodesics are admissible. \(\square\)

Let \(\mathscr U_{f,q}^{\mathbf t}(a,b)\) be the two-state matrix transfer weighted by the monomial \(\prod_{e\in P}t_e\) along each directed dimension-simple path \(P:a\to b\). For a monotone route \(\rho\) through a \(k\)-face \(F=[u,w]\), put \(t_\rho=\prod_{e\in\rho}t_e\) and \(B_q=U_0(q)-U_1(q)\).

**Theorem 52 (tagged higher-face exchange defect).** The formal color differences along \(\rho\) obey
\[
\boxed{D_\rho\mathscr U_{f,q}^{\mathbf t}(z,\bar z)
=t_\rho\,
\mathscr U_{f,q}^{\mathbf t}(w,\bar z)
B_q^k\mathscr U_{f,q}^{\mathbf t}(z,u).}
\tag{61}
\]
For any two routes \(\rho,\rho'\) across the same face, their difference is
\[
\boxed{(t_\rho-t_{\rho'})
\mathscr U_{f,q}^{\mathbf t}(w,\bar z)
B_q^k\mathscr U_{f,q}^{\mathbf t}(z,u).}
\tag{62}
\]

*Proof.* Taking formal differences removes paths avoiding any prescribed route edge. Every remaining path is the concatenation of a prefix, the full prescribed route, and a suffix. The route matrices become \(B_q^k\), while its tag monomial factors as \(t_\rho\). Prefix and suffix sums multiply as displayed. Subtract the formulas for the two routes. \(\square\)

**Closure implication.** Independent path tags are support-faithful, but they replace scalar square equality by the nonzero difference \(t_\rho-t_{\rho'}\). A viable dimension-simple equivariant construction must retain **higher square-exchange chains whose boundary is this difference**, not collapse them to scalar equalities. The natural uncolored framework is the permutohedron of full dimension orders, with neighboring vertices related by adjacent swaps and two-faces encoding commutation and braid relations. Whether the colored accepted-path carriers inside this framework have the necessary antipodal Smith index remains unproved.


#### Localizing restoration defects after dimension removal

The endpoint restoration theorem forces both opposite corners of the affected zero face to admit neither monotone orientation. The repaired zero arm nevertheless gives a full geodesic with a single one-colored edge in the original face. These two facts constrain which dependencies can contain that edge.

**Theorem 53 (a defect cannot lie in a root-universally removable block).** Let \(g\) color \(Q_k\), let a root \(z\) admit neither \(0^*1^*\) nor \(1^*0^*\), and suppose a full geodesic from \(z\) has precisely one one-colored edge \(e\). Split the directions into \(A,B\), with every \(A\)-edge color independent of the \(B\)-bits. Suppose every fixed-\(A\) fiber on \(B\) has all roots favorable. Then the direction of \(e\) lies in \(A\).

*Proof.* If it lay in \(B\), projection of the exceptional path onto \(A\) would give a zero-colored full outer geodesic from \(z_A\). Traverse this path first, then a favorable \(B\)-geodesic from \(z_B\) in the terminal fiber. The resulting full word has type \(0^*1^*\), contradicting the root hypothesis. All outer colors are preserved because they are independent of \(B\). \(\square\)

In particular the defect direction survives every successive sink deletion in the directed dependency graph. A sink variable affects no other direction's edge color; its one-dimensional fibers are root-universally favorable. Favorability of each orientation at the projected root is preserved by insertion at its phase change.

**Theorem 54 (the surviving defect requires branching in its component).** Under Theorem 53's root and path hypotheses, strip all sink directions and let \(C\) be the interaction component of the surviving defect direction. Then:

1. The projected root in \(C\) admits neither monotone orientation.
2. The projected exceptional path has its sole one-colored edge strictly internally in \(C\).
3. The interaction graph on \(C\) is not a star.
4. Some direction in \(C\) has at least two incoming dependency arcs.

Consequently these restrictions hold inside every affected face of a nondegenerate critical-repair quadrilateral.

*Proof.* Sink insertion preserves both orientation sets after projection, while Theorem 53 prevents removal of the defect. In the retained cube, the coloring factors over its interaction components. Projection of the exceptional path onto every component other than \(C\) gives a zero-colored full geodesic. If the root in \(C\) admitted either orientation, combine that witness with these zero factor paths, placing the additional zeros before the one block for \(0^*1^*\), or after it for \(1^*0^*\). This would give the corresponding orientation in the retained cube, and hence at the original root. Thus assertion 1 holds. The exceptional path projects to a one-edge exception in \(C\); an endpoint exception would itself have a monotone word, proving assertion 2.

Every root of a star-interaction coloring admits at least one orientation: traverse the hub first, read its color \(b\), and sort the remaining leaf steps from color \(b\) toward color \(1-b\). Their colors depend only on the now-fixed hub bit. This contradicts assertion 1 and proves assertion 3.

Suppose all indegrees in \(C\) were at most one. The sink-stripped graph has outdegree at least one everywhere. Its total indegree and outdegree agree, forcing both degrees to equal one at every vertex of \(C\). The weakly connected component is therefore a directed cycle. Each edge-color function has form \(a_i+x_{p(i)}\), where \(p(i)\) is its cycle predecessor.

At a root \(y\), put \(b_i=a_i+y_{p(i)}\). Nonconstant \(b_i\) orient the cycle precedence constraints for a zero-colored path acyclically, giving a monochromatic zero full geodesic. If all \(b_i=0\), a reverse cyclic dimension order gives word \(0^{|C|-1}1\). If all \(b_i=1\), a forward cyclic order gives \(10^{|C|-1}\). Thus every root admits an orientation, contradicting assertion 1. This proves assertion 4. \(\square\)

The hypothesis is stronger than merely having an empty root: it includes a full path with one isolated color exception. The defect must remain in the retained dependency system, and the branching obstruction is localized to its own factor. This prevents removal of the exceptional direction by the existing all-root fiber reductions.

A scoped counterexample recorded as research note \(\texttt{note_0ef014a49eca70c6785725e2}\) shows that the surviving interaction graph can still be an undirected path. In that example, two overlapping three-direction constraints force a rise and a descent in every order at the selected root, while one order has only an internal single-edge exception. Hence cycle-freeness of the interaction graph alone cannot transport a paired root to the quadrilateral corner.

**Closure assessment.** The recent repair-fan theorem identifies all free bridge flips within one direction; the variable-matching and star-fiber results give structural rules for gluing across selected terminal blocks. Theorems 53--54 confine a restoration defect beyond the root-universal removal rules. The remaining step must couple a paired root elsewhere in this surviving component to the outside one-colored arms, or force an endpoint certificate. Existence of paired roots in a proper face supplies the starting witness; preserving the outside arm colors during root transport remains unproved.


#### Rooted-tree exclusion at the restoration corners

The rootwise rooted-tree theorem in “Cartesian factorization of paired roots and interaction-prime reduction” strengthens the local obstruction in Theorem 54.

**Corollary 55 (two branching targets in a strongly connected defect factor).** Let \(C\) be the surviving defect factor of Theorem 54. Its coloring cannot have an outward rooted-tree dependency structure with arbitrary feedback into its root, including inactive parent links. If the directed dependency graph on \(C\) is strongly connected, it has at least two distinct vertices of indegree at least two.

*Proof.* At every prescribed root of a rooted-tree feedback coloring, traverse the hub first and then monochromatically traverse the components obtained by cutting inactive parent links. Ordering those components by color gives a full path with at most one switch. The root in \(C\) admits neither orientation by Theorem 54, excluding this structure.

A strongly connected dependency graph with at most one branching target is a directed cycle or an outward rooted tree with additional arrows entering its root. Every nonhub color function then has one active predecessor, hence the required affine one-bit form. The rootwise theorem applies, giving the contradiction. \(\square\)

This sharpens the earlier requirement of one branching direction whenever the defect factor is strongly connected. For a factor with several strongly connected components, coupling their root-specific orientations remains an additional obligation. The tree-face counterexample in note \(\texttt{note_0ef014a49eca70c6785725e2}\) has several branching targets and is consistent with this stronger restriction.


#### A causal obstruction to transporting the prescribed empty root

The strong-connectivity qualification in Corollary 55 has a dimension-uniform obstruction. For every \(r\ge2\), use cycle bits \(y_0,\ldots,y_{r-1}\) and two more directions \(u,v\), and color
\[
f_i=y_{i-1}\quad(0\le i<r,\ \text{indices modulo }r),\qquad
f_u=(1-v)\left(1-\prod_i y_i\right),\qquad f_v=1-u.
\]
Its directed dependency graph has a source cycle on the \(y\)-directions, a terminal two-cycle \(u\leftrightarrow v\), and arrows from the source into \(u\). The sole branching target of the whole graph is \(u\). Every individual feedback component is covered by the cyclic-core or rooted-tree theorem.

At the prescribed root \((\mathbf0,0,0)\), every full path has both a rise and a descent. The cycle subsequence supplies a rise. If \(v\) precedes \(u\), their colors are one and zero. If \(u\) precedes \(v\), the latter color is zero; either \(u\) is one, supplying a descent, or all cycle bits were already one at \(u\), and an earlier one-colored cycle edge precedes this zero. Yet reverse cyclic order followed by \(u,v\) has word
\[
\boxed{0^{r-1}100,}
\]
with one strictly internal exceptional edge. Its antipodal endpoint also admits neither orientation.

The full root profile is
\[
A_0=\{(y,u,v):y\ne\mathbf1,\ (u,v)\ne(0,0)\},\qquad
A_1=\{(y,u,v):y\ne\mathbf0,\ (u,v)\ne(1,1)\},
\]
so
\[
\boxed{|P|=2^{r+1}-4.}
\]
The proof and complete profile are recorded in note \(\texttt{note_0868fc3b9c03299a5e19a9b8}\). This family proves that a single-defect path at an empty prescribed root can traverse a dependency system whose components are all globally reducible, with only one branching target in their union.

**Implication for closure.** Restoring the defect produces a zero path between the required corners, while component reductions supply paired roots at other locations. Any closure argument using these reductions must preserve compatibility with the outside one-colored arms during the change of root. The additional quadrilateral arm conditions remain available: the family above establishes the local transport obstruction, and does not assert that it extends to a paired-root-free full coloring.


#### Audit and a path toward closure

The hub-first rooted-tree theorem, the affected-face endpoint exclusion, and the causal obstruction family remain valid in their stated scopes. Two graph-lemma hypotheses have been corrected in the companion interaction-reduction Subsection: the unique-predecessor forest conclusion requires a nonempty set of branching targets, and a singleton strongly connected graph needs its own case. A directed cycle supplies the counterexample to the forest assertion when that set is empty. The two-hub compression applications already satisfy the required nonempty-set hypothesis.

The following limits are part of the mathematical status:
- Corollary 55 requires strong connectivity of the surviving defect factor. The causal family proves the corresponding weak-connectivity extension false.
- A paired root in a repaired coloring supplies no established antipodal quadrilateral certificate. Certificate availability remains an additional unproved assertion.
- The causal family is a counterexample to prescribed-root transport from the stated local hypotheses; its paired-root count is positive. Extension to a critical full quadrilateral with compatible outside arms is unproved.

**Written closure route.** Start with an ordinary coloring without paired roots minimizing its one-edge count. Every nonempty restoration of one-edges creates a paired root. The singleton repair classification splits the witness into a repaired zero full path or a newly repaired orientation paired with an old opposite orientation. The first remaining task is to obtain antipodally aligned seams, or to run the exchange argument directly on both orientation paths without such alignment.

When a repair supplies a nondegenerate quadrilateral, fix its other three monochromatic arms. In the affected face consider all full corner-to-corner paths with one one-colored edge. Every such path produces the same type of marked quadrilateral after repairing its exceptional edge, because all other arms lie outside this affected face. An endpoint exception contradicts original paired-root absence. Minimize the defect's rank, or maximize it, among these paths. The next lemma gives forced square constraints at both extremes.

The proposed finishing step is to combine these constraints with the opposite zero arm and the two one arms: produce an endpoint exception, reduce the affected zero block, or create an original paired root. Each successful alternative contradicts a minimum marked obstruction. This finishing step and initial seam alignment remain unproved; the local root-transport counterexamples show why all four arms must participate.

**Lemma 56 (incoming and outgoing fans at extremal defect positions).** Let \(g\) color a cube face \(H\), with opposite roots \(z,w\). Suppose no full \(z\)-to-\(w\) path has a monotone color word, and some full path has precisely one one-colored edge. Let \(\mathcal E\) be all such one-defect paths.

For a path in \(\mathcal E\) whose defect rank is smallest possible, write its two steps immediately before and through the defect as
\[
a\xrightarrow[\ 0\ ]{i}b\xrightarrow[\ 1\ ]{j}v.
\]
Then the alternative square edge
\[
\boxed{a\oplus e_j\xrightarrow[\ 1\ ]{i}v}
\]
has color one. More generally, keep the defect \(b\to v\) and its zero suffix fixed. For every direction \(i\) which can be last on a zero geodesic from \(z\) to \(b\), the edge into \(v\) in direction \(i\) has color one. Together with the defect itself these form an incoming one-colored fan of size at least two.

For a path whose defect rank is largest possible, write the defect and its next step as
\[
b\xrightarrow[\ 1\ ]{j}v\xrightarrow[\ 0\ ]{i}c.
\]
Then
\[
\boxed{b\xrightarrow[\ 1\ ]{i}b\oplus e_i}
\]
has color one. Keeping the zero prefix and defect fixed, every possible first direction of a zero suffix from \(v\) gives such a one-colored edge out of \(b\), again forming a fan of size at least two.

*Proof.* An exceptional edge cannot be first or last, since its path would have a monotone word.

In the first square suppose the alternative final edge had color zero. If the alternative first edge were zero, the swapped full path would be monochromatic zero. If it were one, the swapped full path would still have one defect, one rank earlier. Both conclusions contradict the hypotheses. Thus the alternative final edge is one. Any other zero prefix ending at \(b\) can replace the original prefix while retaining its defect rank and zero suffix, proving the full fan assertion.

In the second square suppose the alternative first edge had color zero. If its following edge were zero, the swapped path would be monochromatic zero. If it were one, the defect would move one rank later. Both are excluded. Replacement by any zero suffix proves the outgoing fan assertion. \(\square\)

**Application to critical quadrilaterals.** The affected corners admit neither monotone orientation by the empty-face corollary. The family \(\mathcal E\) is nonempty by restoration, so Lemma 56 applies there. It constrains edges outside the selected witness, while allowing the repaired defect edge to vary. The earliest and latest fans can occur on different paths; no common path attaining both extremes is asserted.

The square constraints were additionally checked on all one-defect paths in the causal obstruction family for cycle lengths two through five. The proof is dimension-independent.


**Proposition 57 (complete local defect immobility in the causal family).** In the causal obstruction family with \(r\) cycle directions and additional directions \(u,v\), every full one-defect path from \((\mathbf0,0,0)\) has word
\[
\boxed{0^{r-1}100.}
\]
There are precisely \(r\) such dimension orders. Thus the earliest and latest defect ranks both equal \(r\), and no exchange sequence retaining one defect within this face can move it to an endpoint.

*Proof.* Every full cycle traversal from its all-zero root has at least one one-colored step. A full one-defect path must therefore have zero-colored \(u\) and \(v\) steps. The zero \(v\) step requires \(u\) to precede \(v\). At that earlier \(u\) step the bit \(v\) is still zero, so a zero \(u\) step requires all cycle bits to be one. Consequently all cycle steps precede \(u\), which precedes \(v\).

For a cycle traversal to have only one one-colored step, all other directions must precede their cycle predecessors. Choosing the exceptional direction breaks the cyclic precedence system into a total chain. Its unique order is reverse cyclic order, ending at the exceptional direction. There is one such order for each of the \(r\) choices. Appending \(u,v\) proves the word and count. \(\square\)

The causal family still has paired roots elsewhere. Proposition 57 proves that the affected-face hypotheses alone cannot support an endpoint-mobility theorem. Lemma 56 supplies necessary fans; obtaining a contradiction requires the additional full-coloring hypothesis and its exterior arm geometry.


#### Coupling opposite zero arms through transverse geodesic cuts

The unaffected zero arm constrains entire transverse fibers, rather than only the chosen exceptional path.

Use the marked quadrilateral notation of the endpoint restoration theorem. The original coloring \(f\) has no paired root. Its affected arm \(P:z\to w\) uses the direction block \(U\), has one one-colored edge, and otherwise is zero. Its opposite arm \(Q:\bar w\to\bar z\) is zero. Put \(V=U^c\), \(k=|U|\), and \(m=|V|\ge1\).

A subset \(T\subseteq U\) is **compatible** when it is a prefix direction set both of \(P\) and of \(Q\). More generally, allow \(P\) to vary over all one-defect full paths in its face and \(Q\) over all zero full paths in the opposite face. Write \(\mathcal C\) for the union of compatible subsets. For \(T\in\mathcal C\), let
\[
p_T=z\oplus\mathbf1_T,\qquad
q_T=\bar w\oplus\mathbf1_T.
\]
These vertices differ precisely in \(V\), and determine a transverse \(V\)-face.

**Theorem 58 (transverse zero-path exclusion).** No transverse face indexed by \(T\in\mathcal C\) contains a zero-colored full \(p_T\)-to-\(q_T\) geodesic. Its one-colored edges contain a directed geodesic cut separating those two vertices.

*Proof.* Choose the corresponding arm orders, and let the exceptional edge of \(P\) have rank \(r\). Put \(t=|T|\). If \(t<r\), concatenate the zero prefix of \(P\), a supposed zero transverse geodesic, and the zero suffix of \(Q\). This is a zero-colored full geodesic from \(z\) to \(\bar z\).

If \(t\ge r\), concatenate the reverse of the zero suffix of \(P\), the transverse geodesic, and the reverse of the zero prefix of \(Q\). This gives a zero-colored full geodesic from \(w\) to \(\bar w\). Both contradict paired-root absence. Prefix-set compatibility ensures that the two \(U\)-arms use complementary direction sets.

Orient the transverse face away from \(p_T\), and let \(Z_T\) be its vertices reachable from \(p_T\) along zero-colored directed paths. Then \(p_T\in Z_T\), \(q_T\notin Z_T\), and every directed edge leaving \(Z_T\) has color one. Every full directed geodesic crosses this cut. \(\square\)

**Lemma 59 (smallest rooted geodesic blockers).** In \(Q_m\), a set of edges meeting every full geodesic between one prescribed antipodal pair has size at least \(m\). For \(m\ge3\), equality requires the set to consist of all \(m\) edges incident with one of the prescribed endpoints.

*Proof.* Give a uniformly chosen full direction order to the prescribed starting root. A directed edge from rank \(s\) to rank \(s+1\) is traversed with probability
\[
\frac{s!(m-s-1)!}{m!}
=\frac1{m\binom{m-1}{s}}\le\frac1m.
\]
A blocker has expected intersection size at least one, yielding the lower bound.

For \(m\ge3\), every interior edge has probability strictly below \(1/m\). A blocker of size \(m\) must therefore use only first or last edges. Let \(I\) be its first-edge directions and \(J\) its last-edge directions. Every possible pair of distinct first and last directions must be covered: for all \(i\ne j\), either \(i\in I\) or \(j\in J\).

If \(I\ne[m]\), each missing \(i\) forces all \(j\ne i\) into \(J\). Two missing first directions would force \(J=[m]\), so a mixed blocker could omit only one first direction. It would then have at least \(m-1\) first edges and \(m-1\) last edges, exceeding \(m\) when \(m\ge3\). Thus all edges are first, or all are last. \(\square\)

**Corollary 60 (disjoint transverse cuts and endpoint fans).** Each compatible transverse fiber contains at least \(m\) one-colored edges. Distinct compatible subsets give edge-disjoint fibers. If one has precisely \(m\) one-colored edges and \(m\ge3\), they form a full one-colored endpoint star. When \(m=1\), its single transverse bridge is one.

If the two arm orders agree, all \(k+1\) prefix subsets are compatible, so the transverse fibers contribute at least \(m(k+1)\) distinct one-colored edges. The exceptional edge lies in a \(U\)-direction and contributes an additional edge. The structural conclusion is the family of directed one-colored cuts; the count records their disjointness.

The theorem uses both opposite zero arms and the full-coloring obstruction. It does not require their orders to agree. It converts the other arm into constraints on edges beyond the selected witness and the internal square fans.

#### Critical direction exchanges force incompatible bridge selectors

The bridge-independent repair theorem also provides a coupling which does not assume a quadrilateral certificate.

For an ordinary cube coloring \(f\), let \(A_0(f)\) be its favorable-root set. Let \(\mathcal B(f)\) consist of all antipodally odd bridge functions \(h\) for which the odd extension \(C(f,h)\) is bad. Equivalently, its zero-bridge selector avoids \(A_0(f)\). When \(P(f)=\varnothing\), the set \(\mathcal B(f)\) is a nonempty Boolean subcube: a favorable root fixes the bridge choice in its antipodal pair, and a pair with neither favorable member leaves that bit free.

**Theorem 61 (selector incompatibility under a directional exchange).** Suppose \(P(f)=\varnothing\), and changing one one-colored edge \(e\) to zero produces a coloring with a paired root. Let \(g\) differ from \(f\) only on edges in the direction of \(e\), including the change at \(e\). The other edges in that direction may change either way.

Then
\[
\boxed{\mathcal B(f)\cap\mathcal B(g)=\varnothing.}
\]
Consequently either \(g\) has a paired root, or there is a root \(x\) with
\[
\boxed{x\in A_0(f)\cap A_1(g).}
\]

*Proof.* Fix \(h\in\mathcal B(f)\). The original odd extension \(C(f,h)\) is bad, while \(C(f_e,h)\) is good by bridge-independent repair. Thus the antipodal edge-pair flip corresponding to \(e\) is a healing flip in its direction. The restoration fan theorem says that any collection of pair flips in that direction containing this flip remains good. The extension \(C(g,h)\) therefore is good, proving disjointness.

If \(g\) has no paired root, both bad-selector subcubes are nonempty. Two Boolean subcubes are disjoint only when some bit is fixed to opposite values. Here that bit indexes an antipodal root pair. Hence one of its members \(x\) lies in \(A_0(f)\), while \(\bar x\) lies in \(A_0(g)\). Reversal gives \(x\in A_1(g)\). \(\square\)

**Corollary 62 (a separating root for balanced minimum-obstruction exchanges).** In the minimum-one-edge obstruction of the bridge-independent repair theorem, any same-direction exchange which turns at least one original one edge to zero either creates a paired root or yields the crossed witnesses of Theorem 61. In particular this applies to a balanced swap of a one edge and a zero edge.

Two distinct minimum-one-edge obstructions which differ only in one direction have disjoint bad-selector subcubes. Equal one-edge counts force their difference to contain a one-to-zero change, so Theorem 61 applies.

**Quantifier qualification.** Paired-root absence means that some bridge assignments are bad. It does not mean that every bridge assignment is bad. Theorem 61 therefore proves disjoint bad-selector sets and crossed witnesses, rather than unconditional paired-root persistence under arbitrary same-direction additions.

**Progress toward the written closure route.** The transverse cut theorem forces exterior constraints using the unaffected zero arm. The selector theorem produces a common root carrying opposite favorable orientations in two directionally related colorings. The remaining task is to couple the cut or crossed witnesses to an original paired certificate while preserving all direction uses. This has not been proved. The crossed-witness alternative avoids assuming initial quadrilateral availability and provides a second route for that missing alignment step.

#### Two-lift induction and edge-pair avoidance across an unread direction

Let \(n\ge3\) and let \(c\) be a legal antipodally odd coloring of the undirected edges of \(Q_n=Q_{n-1}\times\{0,1\}\). Denote the last direction by \(j\), and suppose every edge color in the other \(n-1\) directions is independent of the \(j\)-bit. Let \(g\) denote that common horizontal coloring. Antipodal oddness of \(c\) implies that \(g\) itself is antipodally odd. Write \(h(y)\) for the color of the vertical edge above \(y\); then \(h(\bar y)=1-h(y)\). Let \(F_d\) count unoriented monochromatic-zero full antipodal geodesics.

**Theorem (two-lift monochromatic induction).** Every unoriented monochromatic-zero full geodesic \(P\) of \(g\), between roots \(y,\bar y\), gives two distinct monochromatic-zero full geodesics of \(c\). Choose the unique endpoint \(z\in\{y,\bar y\}\) with \(h(z)=0\). Orient \(P\) from \(z\) to \(\bar z\). The two lifts start at \((z,0)\) and \((z,1)\), respectively, traverse the zero-colored vertical edge at \(z\), and then traverse \(P\) in the opposite horizontal layers. Thus
\[
\boxed{F_n(c)\ge2F_{n-1}(g).}
\tag{LI1}
\]

*Proof.* Since the horizontal colors are independent of the layer, the described paths use each cube direction once and have every edge color zero. Their horizontal edges lie in different layers, so the unoriented full paths are distinct. Removing the unique vertical edge from either lift recovers \(P\); hence paths derived from distinct lower geodesics do not coincide, proving the inequality. \(\square\)

**Theorem (pair-avoidance lifting).** Assume \(g\) has at least one monochromatic-zero antipodal full geodesic. For every *horizontal* antipodal edge orbit \(q\) of \(Q_n\), at least one monochromatic-zero full geodesic of \(c\) avoids \(q\). If \(g\) has monochromatic-zero full geodesics with at least two different antipodal endpoint pairs, then the same avoidance holds for *every* antipodal edge orbit, including vertical ones. In particular, any single legal antipodal-pair recoloring of \(c\) preserves a monochromatic full antipodal geodesic.

*Proof.* Fix a monochromatic-zero lower geodesic \(P\) and its two lifts from the preceding theorem. A horizontal orbit of \(Q_n\) consists of an edge \(e\) in one horizontal layer and the antipodal edge \(\bar e\) in the other. The lower coloring \(g\) assigns opposite colors to \(e,\bar e\). Thus the zero-colored path \(P\) cannot contain both. Since its two lifts traverse the same lower horizontal edge sequence in different layers, at most one lift can encounter the given horizontal orbit. The other avoids it.

For a vertical orbit, each lifted path derived from \(P\) uses the vertical edge above \(z\), where \(z\) is the unique endpoint of \(P\) satisfying \(h(z)=0\). If two lower geodesics have different antipodal endpoint pairs, their selected vertical edges belong to different antipodal orbits. Consequently one of their lifts avoids any prescribed vertical orbit. A path avoiding a recolored orbit is unaffected by its flip and remains monochromatic. \(\square\)

**Restoration consequence.** A critical good coloring in the pair-restoration lemma cannot possess an unread direction whose induced facet has two monochromatic-zero endpoint pairs: the lifting theorem produces a monochromatic full geodesic avoiding the purported compulsory internal pivot, no matter which direction contains that pivot. The functional-reader root census supplies the required two endpoint pairs whenever its lower facet has dimension at least three; this gives an alternate route to the dimension-four one-pair robustness theorem without requiring the exceptional vertical color function itself to have the one-reader form.

**Scope.** This is a nontrivial all-dimensional closure transfer for every legal odd coloring with an unread direction, provided the lower-dimensional odd coloring has a monochromatic full geodesic. It does not settle the minimum-dimensional case in which every direction influences at least one other direction.

#### Three exceptional directions, the two-hub bridge, and facetwise obstruction rigidity

The recent computer-assisted two-hub paired-root theorem combines with the unrestricted bridge criterion to close a further all-dimensional class of odd cube-edge colorings. It also forces a simultaneous structural obstruction in every facet of a minimum-dimensional counterexample.

Call a direction \(i\) of a legal antipodally odd cube coloring *simple* if its edge colors have the form \(c_i(x)=a_i+x_{r(i)}\), where \(r(i)\ne i\). A nonsimple direction is *exceptional*. Every legal edge-color function depending on at most one other bit is simple: global antipodal oddness excludes constant functions, and a nonconstant Boolean function of one bit is a signed reader.

For an arbitrary edge coloring \(g\) of \(Q_m\), its directed influence graph has an arc \(j\to i\) when changing bit \(j\) can change the color of a direction-\(i\) edge. A direction function that is constant or reads only one bit has indegree at most one. Thus a coloring with at most \(k\) other direction functions has at most \(k\) vertices of indegree at least two, both globally and within any strongly connected component.

**Lemma (two-exception paired-root bound, from the two-hub SCC theorem).** If an arbitrary edge coloring \(g\) of \(Q_m\) has at most two direction functions that are neither constant nor signed one-bit readers, then
\[
\boxed{|P(g)|\ge\max\{2,\;2^{\lceil m/2\rceil-2}\}.}
\tag{TE1}
\]
Here \(P(g)\) consists of roots admitting both monotone color-word orientations. This lemma uses the computer-assisted two-hub favorable-root theorem published in “A coupled-hub obstruction to independent leaf elimination.”

*Proof.* Every dependency SCC has at most two vertices with internal indegree greater than one. The two-hub SCC gluing theorem gives a paired-root multiplicative factor at least \(2^{b-1}\) for any nontrivial component of size \(b\) with at most one branching target, and at least \(2^{b-3}\) if it has two; a singleton gives factor \(2\). Let \(t\) count nontrivial SCCs and let \(\delta=1\) if a component with two branching targets occurs, zero otherwise. Since only two exceptional functions exist, at most one SCC can have two branching targets. Multiplying the factors gives
\[
|P(g)|\ge2^{m-t-2\delta}
\ge2^{m-\lfloor m/2\rfloor-2}
=2^{\lceil m/2\rceil-2}.
\]
The paired-root set is antipodally symmetric and nonempty, so it also has at least two vertices. \(\square\)

**Theorem (NORI1 with at most three exceptional directions).** Every legal antipodally odd edge coloring \(c\) of \(Q_n\), \(n\ge2\), with at most three exceptional direction functions admits a monochromatic full antipodal geodesic. Its number \(F_n(c)\) of unoriented monochromatic-zero full antipodal geodesics satisfies the all-dimensional estimate
\[
\boxed{F_n(c)\ge\max\{1,\;2^{\lceil(n-1)/2\rceil-3}\}.}
\tag{TE2}
\]

*Proof.* If there is an exceptional direction \(h\), choose it. Otherwise choose any direction. Restrict the other direction-edge color functions to the lower \(h\)-facet, obtaining an arbitrary coloring \(g\) of \(Q_{n-1}\). Every globally simple direction restricts to either a constant function, if it reads \(h\), or a signed one-bit reader. Of the exceptional directions, at most two remain after deleting \(h\). Thus \(g\) meets the lemma's hypotheses, and \(P(g)\) has the bound (TE1). For each antipodal vertex pair contained in \(P(g)\), the odd colors on its two \(h\)-bridges select a color-zero crossing above one favorable root. The universal bridge-splice bijection turns this into a monochromatic-zero full geodesic. Crossings from distinct root pairs are different, so
\[
F_n(c)\ge |P(g)|/2
\ge\max\{1,2^{\lceil(n-1)/2\rceil-3}\}.
\]
\(\square\)

**Corollary (four exceptional directions are necessary).** In any hypothetical legal odd coloring without a monochromatic antipodal full geodesic, at least four distinct direction functions are nonsimple. In Walsh language, at least four direction spins have nonzero Fourier mass on odd levels at least three. This strengthens the earlier two-direction support obstruction using the computer-assisted two-hub theorem.

**Theorem (facetwise three-branching obstruction at minimum dimension).** Assume \(c\) is a bad legal coloring of \(Q_n\) with minimum possible \(n\). For every direction \(h\), let \(g_h\) denote its coloring induced on the facet \(x_h=0\). Then \(P(g_h)=\varnothing\), and **every terminal strongly connected component** of the directed influence graph of \(g_h\) has at least three distinct vertices with internal indegree at least two. In particular it contains at least four directions and is not a directed simple cycle.

*Proof.* If some \(g_h\) had a paired root, the universal bridge criterion would give a monochromatic full geodesic for \(c\), a contradiction. By the converse half of the same criterion, a paired-root-free arbitrary coloring of \(Q_d\) has an odd extension without a monochromatic full geodesic on \(Q_{d+1}\). Since \(c\) is minimum-dimensional, no coloring of a cube of dimension less than \(n-1\) is paired-root-free.

Let \(B\) be any terminal SCC of the influence graph of \(g_h\). If it has at most two branching targets, the established fiberwise two-hub gluing theorem removes \(B\) and shows
\[
|P(g_h)|\ge \rho_B\,|P(g_h|_{Q_{[n]\setminus(\{h\}\cup B)}})|,
\quad \rho_B>0.
\]
The left side is zero, so the smaller induced coloring would have no paired root. Its odd bridge extension would be a bad legal cube coloring of dimension \(n-|B|<n\), contradicting minimality. Thus every terminal SCC has at least three branching targets. Every SCC on at most three directions is reducible by the published small-SCC theorem, so the component has size at least four. \(\square\)

**Closure target.** If a minimum-dimensional bad coloring has only four exceptional directions, the theorem forces a coupled feedback configuration in every facet: deleting any one exceptional direction must leave a terminal SCC containing the other three, each still internally dependent on at least two direction bits. The constraint is imposed simultaneously for all deletion choices, rather than merely on the original influence digraph. A closing proof could attempt to show that these four facetwise feedback structures cannot coexist with antipodal oddness and the square-exchange identities. The present argument does not exclude their coexistence.

#### The apex two-hub criterion and vertex-deletion feedback rigidity

For a legal odd edge coloring \(c\) of \(Q_n\), let \(D(c)\) be its directed influence graph on the dimension set: \(j\to i\) means that the direction-\(i\) edge color can change when bit \(j\) is toggled. For an induced digraph \(H\), call an SCC *two-hub reducible* when at most two of its vertices have internal indegree at least two.

**Theorem (apex two-hub NORI1 closure).** Suppose there is a direction \(h\) such that every strongly connected component of the graph \(D(c)-h\) is two-hub reducible. Then \(c\) has a monochromatic antipodal full geodesic. This conclusion allows arbitrarily many nonlinear direction functions and does not bound the ambient dimension.

*Proof.* Let \(g_h\) be the edge coloring induced on the facet \(x_h=0\). Its directed influence graph \(D(g_h)\) is a subgraph of \(D(c)-h\): fixing one bit cannot introduce a dependence on another bit that did not occur in the full coloring. Every SCC of a subgraph lies inside some SCC of the original digraph, and its internal indegree cannot increase. Hence every SCC of \(D(g_h)\) is two-hub reducible. The published two-hub SCC paired-root theorem, whose central nine-sixteenths estimate is computer-assisted, gives \(P(g_h)\ne\varnothing\). The universal antipodal bridge criterion then gives a monochromatic antipodal full geodesic in \(c\), independently of the direction-\(h\) edge colors. \(\square\)

**Corollary (vertex-deletion resilient feedback is necessary).** In every hypothetical bad legal coloring and for every direction \(h\), the induced graph \(D(c)-h\) must contain a strongly connected component with at least three vertices of internal indegree at least two. This is an all-direction graph condition imposed before examining the detailed color values on a facet. A bad coloring cannot have a dimension whose deletion separates all internally branching feedback into one- or two-target SCCs.

**Corollary (four-exception persistence).** Suppose a bad legal coloring has precisely four exceptional direction functions, and write \(H\) for their set. Then for every \(h\in H\), all three vertices of \(H\setminus\{h\}\) belong to a single SCC of \(D(c)-h\), and each has internal indegree at least two within that SCC. The corresponding three functions must also retain at least two active internal bit-dependencies when restricted to the facet \(x_h=0\).

*Proof.* All globally simple direction functions have indegree one. After deleting \(h\), only the three remaining exceptional directions can have internal indegree at least two. The preceding corollary therefore forces all three to be in one SCC with internal indegree at least two. Since \(P(g_h)=\varnothing\), the contrapositive of the two-hub SCC paired-root theorem gives some SCC of \(D(g_h)\) containing at least three branching vertices. Only the three remaining exceptional directions can have such indegrees; hence all three occur in this one SCC and retain the specified internal dependencies. The SCC need not be terminal unless the bad coloring has minimum possible dimension. \(\square\)

**Toward proof closure.** The first unresolved bad configuration must be robust under deletion of every individual dimension: three branching targets must remain strongly feedback-connected somewhere after each deletion. When there are four exceptional directions this demands a common three-target feedback skeleton in every exceptional facet. This offers a global structural alternative to direct path enumeration: analyze the compatibility of the resulting vertex-deletion-resistant influence digraphs with antipodal oddness and with the square-derivative relations of their Boolean edge-color functions. No contradiction for the general skeleton is claimed here.

#### Terminal-component elimination and global strong connectivity of minimal obstructions

For a legal antipodally odd coloring \(c\) of the undirected edges of \(Q_n\), let \(D(c)\) be its directed influence graph: \(j\to i\) if the color of a direction-\(i\) edge depends on bit \(j\). Edges point from a bit toward a function reading that bit.

**Theorem (inductive terminal-component elimination).** Suppose NORI1 holds in every dimension below \(n\). If \(D(c)\) is not strongly connected, then \(c\) has a monochromatic antipodal full geodesic. Consequently every counterexample of minimum dimension has a strongly connected influence digraph.

*Proof.* Choose a proper terminal SCC \(B\) of \(D(c)\), and put \(A=[n]\setminus B\ne\varnothing\). No influence arc leaves \(B\) toward \(A\), so all \(A\)-direction edge colors are independent of the \(B\)-bits. Their common restriction \(c_A\) is odd under antipodal inversion of \(Q_A\):
\[
c_{A,i}(\bar x_A)=c_i(\bar x_A,\bar z_B)
=1-c_i(x_A,z_B)=1-c_{A,i}(x_A).
\]
Thus \(|A|\ge2\), since a one-dimensional cube admits no legal antipodally odd undirected-edge coloring: its only edge is fixed by inversion.

By lower-dimensional NORI1, \(c_A\) has a monochromatic-zero full antipodal geodesic \(P_A:x_A\to\bar x_A\). Fix the \(A\)-bits at \(\bar x_A\), giving an arbitrary coloring \(g_B\) of \(Q_B\). Since \(|B|\le n-2\), the dimension \(|B|+1\) falls under the induction hypothesis. The universal paired-root bridge equivalence therefore guarantees \(P(g_B)\ne\varnothing\), and in particular a full geodesic \(P_B:z_B\to\bar z_B\) with word \(0^*1^*\).

Traverse \(P_A\) at fixed \(B\)-bits \(z_B\), then \(P_B\) at fixed \(A\)-bits \(\bar x_A\). This is a complete antipodal geodesic, because the two paths use disjoint direction sets and together use all directions. The first block is all zero, since its edge colors are independent of \(B\)-bits; the second block has word \(0^*1^*\). The concatenation therefore has at most one color change. The established one-change root-slide surgery for legal odd colorings produces a monochromatic full antipodal geodesic. \(\square\)

**Corollary (global and deletion-level rigidity).** In a minimum-dimensional bad legal odd coloring, (i) the entire directed influence graph is strongly connected; (ii) for every removed direction \(h\), the unrestricted coloring on the lower \(h\)-facet has no paired root; (iii) every terminal SCC of each such facet influence graph contains at least three internal branching targets, by the published computer-assisted two-hub theorem and minimum-dimensionality. These conditions are simultaneous, imposed by the same legal coloring.

**Limitation of graph-only closure.** A fully connected feedback graph can satisfy all of the corresponding indegree and deletion-survival requirements. For instance \(c_i(x)=\sum_{j\ne i}x_j\pmod2\) in dimension four is legal and has a complete bidirected influence graph. Every three-direction facet restriction retains a complete feedback triangle with internal indegree two, while the coloring is good by the affine full-rank theorem. An eventual contradiction must use numerical color or path-incidence relations, not strong graph connectivity alone.

The theorem gives an unrestricted-dimensional induction step: any first obstruction is a single strongly connected influence core, rather than a collection of terminal components. It sharpens the earlier connected-interaction-graph reduction.

#### Minimal obstruction is a canonical hub-star kernel

Let \(c\) be a legal antipodally odd edge coloring of \(Q_n\). A direction is *simple* if its color is \(a_i+x_{p(i)}\), with \(p(i)\ne i\); let \(H\) contain the other directions, and put \(k=|H|\). Antipodal oddness forces every edge-color function to read at least one bit, and any odd Boolean function reading at most two bits is a signed one-bit reader.

**Compression lemma.** If the directed influence graph is strongly connected, all simple vertices lie in outward rooted trees whose parents eventually reach \(H\). For each branch \(B\) beginning at a child of hub \(h(B)\), let \(a(B)\) be the offset in its leading-edge color \(a(B)+x_{h(B)}\). Group branches by the pair \((h(B),a(B))\), giving \(r\le2k\) nonempty classes \(S_j\) partitioning the simple vertices. For each coset representative \(y\) of the span of their indicator vectors, the compressed coloring \(c_y\) on \(Q_{k+r}\) has hub-edge colors
\[
(c_y)_h(u,s)=c_h\left(u,y+\sum_js_j\mathbf1_{S_j}\right)
\]
and macro-leaf colors \((c_y)_j(u,s)=a(S_j)+u_{h(S_j)}\). This coloring is legal odd, and every monochromatic full antipodal geodesic in it lifts to one in \(c\).

*Proof.* A directed cycle of simple vertices cannot have an incoming arrow from a hub or another vertex, because every simple vertex has only one incoming arrow. Strong connectivity excludes such a cycle, so the unique-predecessor simple graph consists of hub-rooted trees. The compressed antipode complements every represented original bit because the type classes partition all simple bits; hence all compressed colors satisfy oddness. To expand a macro-leaf step of color \(t\), traverse each branch in its class without changing the controlling hub bit. Every leading edge has color \(t\). For descendant \(i\), the requirement \(a_i+x_{p(i)}=t\) prescribes one parent-child precedence relation. An orientation of a tree is acyclic, so these comparisons have a total-order extension, giving a complete all-\(t\) traversal of the branch. After every branch is traversed, the macro class has been flipped, and the next hub step reads the represented original state. Expansion uses every original direction once, respects all colors, and joins antipodes. \(\square\)

**Theorem (minimal hub-star kernel).** If \(c\) is a counterexample of minimum dimension \(n\), then the directed influence graph is strongly connected and every simple direction reads a hub directly. For each hub there is at most one simple leaf colored \(x_h\) and at most one colored \(1+x_h\). Hence
\[
\boxed{n\le3k,\qquad k\ge\max\{4,\lceil n/3\rceil\}.}
\]
*Proof.* Strong connectivity follows from the terminal-SCC induction theorem. If any type class \(S_j\) contained more than one simple direction, then its compressed legal odd coloring would have dimension \(k+r<n\). Minimality makes the compressed coloring good, and the compression lemma lifts its monochromatic full antipodal geodesic to \(c\), a contradiction. Hence every class contains one simple direction, and all branches have size one. There are at most two classes per hub, yielding \(n-k\le2k\). The previously published three-exception closure establishes \(k\ge4\). \(\square\)

Thus a first obstruction with four hubs must occur in a legal odd canonical star with at most twelve directions. This is a proven inductive reduction; it leaves the four-hub kernel existence question open.

#### Favorable roots in every bit facet: the simple-bridge induction target

Let \(g\) be an arbitrary binary coloring of the undirected edges of \(Q_m\). Write
\[
A(g)=\{x:\exists\text{ a full antipodal geodesic rooted at }x
\text{ with word }0^*1^*\}.
\]
Define the *facet-hitting property* \(\mathrm{FH}_m\): for every \(g\), every bit position \(j\), and each \(b\in\mathbb F_2\),
\[
\boxed{A(g)\cap\{x:x_j=b\}\ne\varnothing.}
\tag{FH1}
\]
This remains conjectural in unrestricted dimension.

**Theorem (equivalence to odd colorings with a simple bridge).** For every \(m\ge1\), \(\mathrm{FH}_m\) is equivalent to the statement that every legal antipodally odd coloring of \(Q_{m+1}\) whose edge color in at least one direction \(h\) is a signed single-bit reader \(c_h(y)=a+y_j\), \(j\ne h\), admits a monochromatic antipodal geodesic.

*Proof.* Cut the odd colored \((m+1)\)-cube across \(h\). The lower horizontal facet has an unrestricted coloring \(g\), and the upper facet is its antipodally complemented image. The zero-colored bridge selector is the bit facet \(S=\{y:y_j=a\}\). The established bridge-splice bijection says that a monochromatic antipodal geodesic exists if and only if \(S\cap A(g)\ne\varnothing\). Thus (FH1) proves the stated one-reader-bridge closure.

Conversely, for any \(g,j,b\), give a larger cube its lower horizontal coloring \(g\), its upper horizontal coloring the antipodally complemented image of \(g\), and bridge color \(y_j+b\). This is legal odd and has a simple bridge direction. If it is good, the bridge-splice criterion gives a favorable root of \(g\) in the bit facet \(y_j=b\). This is (FH1). \(\square\)

**Theorem (induction reduces the facet-hitting conjecture to strongly connected influence cores).** Suppose \(\mathrm{FH}_d\) holds for all \(d<m\). If the directed influence graph of an arbitrary coloring \(g\) of \(Q_m\) is not strongly connected, then \(g\) satisfies (FH1) for every \(j,b\).

*Proof.* Choose a proper source SCC \(U\) in the influence graph, and put \(V=[m]\setminus U\). No influence arrow enters \(U\) from \(V\), so all \(U\)-direction edge colors are independent of the \(V\)-bits. Their induced coloring \(g_U\) is arbitrary. Fix a desired starting bit \(x_j=b\).

If \(j\in U\), the induction hypothesis supplies a favorable full \(U\)-geodesic from a root with \(j\)-bit \(b\). If \(j\in V\), it supplies any favorable full \(U\)-geodesic. Let \(y\) be the vertex of \(Q_U\) at the zero-to-one division of that path. Fix the \(U\)-bits at \(y\), giving an arbitrary colored \(V\)-cube \(g_{V,y}\). The induction hypothesis supplies a favorable full \(V\)-geodesic, with starting \(j\)-bit \(b\) if \(j\in V\), or any starting root otherwise.

Insert the \(V\)-geodesic at the color-change division of the \(U\)-geodesic. All \(U\)-direction colors remain unchanged because they are independent of \(V\)-bits, while the \(V\)-geodesic is evaluated at fixed \(U\)-bits \(y\). The concatenated word remains \(0^*1^*\), and the full geodesic begins with \(j\)-bit \(b\). Thus (FH1) holds. \(\square\)

**Corollary (conditional closure improvement).** If \(\mathrm{FH}_m\) holds in every dimension, then no bad legal odd coloring has a simple direction. In combination with the canonical hub-star theorem above, a minimum bad coloring would have **every direction exceptional** (no simple leaves). If (FH1) ever fails, the bridge construction furnishes a bad odd coloring with a simple direction in the next dimension. The theorem does not decide which possibility occurs.

**Finite checks and proof status.** A binary integer feasibility formulation can test failure of (FH1): introduce one edge-color bit for each undirected cube edge and, for every dimension order rooted in the selected bit facet, require at least one adjacent color descent \(1\to0\). Auxiliary binary bits mark candidate descents and are constrained above by the color of the first edge and by the complement of the second. Infeasibility is equivalent to (FH1). This formulation was solved as infeasible in dimensions four and five using SciPy/HiGHS; these are computational checks, not a general proof or a published independently checkable certificate. The cross-facet seam geometry for strongly connected unrestricted colorings remains the missing step.


#### Empty corridors, component polarization, and localization of paired repairs

The empty-corridor rule must retain the source of the root's failure. An empty full root can arise from incompatible one-sided orientations in independent components, even though every component root supports an orientation. A one-edge paired repair imposes a stronger local condition.

Let \(f=\prod_{\nu=1}^r f_\nu\) be the Cartesian factorization by weak components of its direction-interaction graph. At a root \(x=(x_\nu)\), define its component profile by membership in \(A_0(f_\nu),A_1(f_\nu)\). Paired-root and favorable-root factorization give
\[
A_t(f)=\prod_\nu A_t(f_\nu),\qquad
P(f)=\prod_\nu P(f_\nu).
\]
Call a root *locally empty* in component \(\nu\) when \(x_\nu\) admits neither orientation there. When every component root admits an orientation, the full root is empty precisely when one component is favorable only nondecreasingly and another only nonincreasingly.

**Theorem (an empty antipodal corridor in a reader coloring).** In every dimension \(n\ge6\), there is a legal odd one-reader coloring having a full antipodal geodesic all of whose vertices admit neither monotone orientation.

*Proof.* Use three independent two-direction blocks, with reciprocal readers
\[
f_{2j}=x_{2j+1},\qquad f_{2j+1}=x_{2j}\quad(j=0,1,2).
\]
A block root, encoded by its first bit plus twice its second, has profiles
\[
A_0=\{0,1,2\},\qquad A_1=\{1,2,3\}.
\]
Thus root zero is upward-only, root three downward-only, and roots one and two paired.

Start at full root \(60\), whose three block roots are \((0,3,3)\), and traverse order
\[
\boxed{(2,3,0,1,4,5).}
\tag{EC1}
\]
Its vertex sequence is
\[
\boxed{60,56,48,49,51,35,3.}
\]
First the second block moves \(3\to2\to0\), while the first remains upward-only and the third downward-only. Then the first moves \(0\to1\to3\), while the second is upward-only and the third downward-only. Finally the third moves \(3\to2\to0\), while the first is downward-only and the second upward-only. Every vertex therefore has both one-sided profile types among its factors and is empty. The order flips every direction once and \(3=60\oplus63\).

For larger dimensions add leaf directions \(i\ge6\) with color \(x_0\), leaving every old direction independent of the new bits. The one-way leaf insertion lemma gives
\[
A_t(f^+)=A_t(f)\times\mathbb F_2\quad(t=0,1):
\]
insertion at the appropriate monotone seam proves inclusion, and deleting the added step from a favorable path proves the reverse inclusion because old edge colors remain unchanged. Hence the empty-root set is the old empty-root set times the new bit cube. Traverse all added directions at the initial empty old root and then follow (EC1). This is an empty-root full antipodal geodesic, and every edge-color function remains a legal signed reader. \(\square\)

This shows that empty-corridor exclusion requires more information than reader structure or componentwise paired-root existence. The gate geometry and critical repair ports supply the additional constraints.

**Proposition (two covered components cannot support an empty antipodal path).** Suppose \(f\) has at most two Cartesian factors, and every root of each factor admits at least one orientation. Then no cube path lying entirely in empty roots can join antipodal vertices.

*Proof.* With one factor no root is empty. With two factors an empty root has profiles upward-only/downward-only or downward-only/upward-only. A cube edge changes bits in only one factor, so it cannot connect the two profile combinations while retaining emptiness. Antipodal inversion exchanges upward and downward profiles in each factor by path reversal. Therefore antipodal empty roots lie in different components of the induced empty-root graph. \(\square\)

##### A repaired empty root has an empty component

**Lemma (two new orientations through one edge splice monochromatically).** Suppose an ordinary coloring \(f'\) differs from \(f\) on one edge \(e\). If a root \(x\) is empty in \(f\) and paired in \(f'\), then \(f'\) has a monochromatic full geodesic from \(x\) through \(e\).

*Proof.* Both new monotone witnesses must traverse \(e\); a witness avoiding it would already give an orientation in \(f\). Their traversal direction on \(e\) is the same, because the starting bit of its direction is fixed and is flipped only once. Their prefixes ending at its far endpoint use the same direction set, determined by the displacement from \(x\) to that endpoint.

If the repaired edge has color zero, splice the nondecreasing witness's zero prefix through \(e\) to the nonincreasing witness's zero suffix after \(e\). If it has color one, splice the nonincreasing one's one prefix to the nondecreasing one's one suffix. The shared prefix-direction set ensures no direction is repeated or omitted. \(\square\)

**Theorem (localization of a one-edge paired repair at an empty root).** Let \(B\) be the original Cartesian component containing the direction of \(e\). Under the preceding lemma's hypotheses,
\[
\boxed{x_B\notin A_0(f_B)\cup A_1(f_B).}
\tag{EC2}
\]
For some color \(t\), every other component supports a monochromatic full color-\(t\) geodesic from its starting root \(x_\nu\).

*Proof.* In \(f\), the spliced path has all edges of one color \(t\) except \(e\). Its projection to every component other than \(B\) is a monochromatic full geodesic in the original coloring. Its projection to \(B\) contains the sole exception.

If \(x_B\) admitted either monotone orientation in \(f_B\), use that full \(B\)-path and insert every unaffected monochromatic component path at its color-change division, in the phase matching \(t\). Original component independence preserves all edge colors. This gives a full monotone path in \(f\) from \(x\), contrary to emptiness. Hence (EC2) holds. \(\square\)

The repaired coloring may acquire new dependencies on other components; the theorem uses only the original factorization and the original colors along the spliced path.

**Corollary (polarization-only empty roots resist a one-edge paired repair).** When every original component root admits at least one orientation, changing one arbitrary edge cannot turn an empty full root into a paired root. In particular no vertex of (EC1) can be healed in this way.

**Coupling to Article XIV.** A gate corridor forces neighboring face roots to be empty. If a critical one-edge repair produces paired witnesses at one of those roots, (EC2) locates a component that is itself empty there, and every unaffected factor must provide a common-color monochromatic path. The repair therefore resolves a local feedback obstruction at that prescribed root. Independent components with opposing one-sided orientations can supply an empty corridor, but cannot supply such a paired repair.

This separates two structural sources of the corridor and narrows the missing induction: transport the critical witness into its locally empty component, preserving its seam and direction set, and then apply the rooted feedback exclusions or cross-profile stripe rule. The original causal transport obstruction still prevents an automatic passage to a different favorable root.

**Independent checks.** The block profiles and all seven vertices of (EC1) were directly evaluated. The repair-splice theorem follows from the shared displacement direction set and does not use enumeration.

#### Zero/one crossing gates for a prescribed root facet

Let \(f_0,f_1\) be arbitrary binary colorings on two horizontal copies of \(Q_m\), and let \(h(z)\) color the joining edge above \(z\in Q_m\). Define \(Z\) as the sites above which a full geodesic from some lower-layer root can cross with an all-zero lower horizontal prefix and a \(0^*1^*\) upper horizontal suffix. Define \(O\) as the sites permitting a lower \(0^*1^*\) prefix and an all-one upper suffix. The two segments together traverse each horizontal direction once; empty segments are allowed. The gate sets depend on \(f_0,f_1\) only.

**Theorem (crossing-gate completion face).** The assembled coloring has no \(0^*1^*\) full antipodal geodesic starting in its lower root facet precisely when
\[
\boxed{h(z)=1\ (z\in Z),\qquad h(z)=0\ (z\in O).}
\tag{BG1}
\]
These bridge assignments exist precisely if \(Z\cap O=\varnothing\); their number is then \(2^{2^m-|Z\cup O|}\).

*Proof.* With a zero bridge, a favorable word must have only zeros before the bridge and a nondecreasing word afterward. With a one bridge, it must have a nondecreasing prefix and only ones afterward. Thus favorable paths are present at the indicated gate sites precisely for the respective bridge bit. Avoiding every such path forces the opposite bit. Conflict occurs at an intersection site; otherwise one independent bridge bit is fixed per site of the union. \(\square\)

**Lemma (endpoint gates).** If \(A(f)\) denotes roots of full \(0^*1^*\) geodesics, then
\[
\boxed{A(f_1)\subseteq Z,\qquad\overline{A(f_0)}\subseteq O.}
\tag{BG2}
\]
Hence a coloring with no favorable root in the lower facet must have
\[
\boxed{A(f_1)\cap\overline{A(f_0)}=\varnothing,\qquad
|A(f_0)|+|A(f_1)|\le2^m.}
\tag{BG3}
\]
*Proof.* A favorable upper full geodesic rooted at \(z\) may follow a zero bridge first. A favorable lower full geodesic rooted at \(\bar z\) may precede a one bridge last. These yield the inclusions, and the gate theorem gives the separation. \(\square\)

**Corollary (both root facets covered for every bridge assignment).** If
\[
\boxed{A(f_1)\cap\overline{A(f_0)}\ne\varnothing,}
\tag{BG4}
\]
then each of the two root facets has a favorable full antipodal geodesic, whatever \(h\) is. This holds, in particular, when \(|A(f_0)|+|A(f_1)|>2^m\).

*Proof.* A vertex in the intersection supplies both gate colors; hence a favorable path from the lower layer exists for either choice of its bridge bit. Interchanging layers sends the intersection into its antipodal image \(\overline{A(f_1)}\cap A(f_0)\), proving the upper-layer claim. The cardinality condition forces intersection by inclusion-exclusion. \(\square\)

**Corollary (two independent two-hub facet colorings).** If each horizontal coloring is a two-hub star with arbitrary nonlinear hub functions and signed one-bit leaf readers, then the published computer-assisted theorem gives \(|A(f_b)|\ge(9/16)2^m\) in each layer. Their combined favorable-root counts exceed \(2^m\). Therefore both root facets remain favorable for every vertical edge-color assignment, even if the two layers have unrelated hub functions, offsets, and reader patterns.

This gives the crossing-site interpretation of the general one-direction completion Boolean-face theorem published separately. The bit-facet hitting conjecture is equivalent to demanding \(Z\cap O\ne\varnothing\) for every pair of unrestricted horizontal colorings. Any obstruction has the cross-facet separation (BG3); a closing argument must then force internally crossing gate witnesses. Formula (BG1) was checked on 100 randomly generated four-cube horizontal interfaces and 45 vertical assignments per interface.

#### Cross-coloring condensation and apex facet coverage

Let \(f,g\) be arbitrary binary edge colorings of \(Q_m\). Assume a common directed influence supergraph \(D\) contains every arc \(j\to i\) along which either color of direction \(i\) depends on bit \(j\). Suppose each strongly connected component of \(D\) has at most two vertices with internal indegree greater than one.

**Theorem (opposed favorable roots of distinct colorings).** The favorable root sets for \(0^*1^*\) complete geodesics satisfy
\[
\boxed{A(f)\cap\overline{A(g)}\ne\varnothing.}
\tag{CC1}
\]

*Proof.* Induct on the dimension. Choose a terminal strongly connected component \(B\) of \(D\), and write \(U=[m]\setminus B\). Because no arc goes from \(B\) to \(U\), the colors of \(U\)-direction edges in both colorings are independent of \(B\)-bits. Their restrictions \(f_U,g_U\) share influence supergraph \(D[U]\); by induction choose favorable full \(U\)-paths from antipodal starting roots \(x,\bar x\).

Let \(u,v\) be the zero-to-one seam vertices of these two paths. The induced \(B\)-fiber colorings \(f_{B,u},g_{B,v}\) have their internal dependency arcs contained in \(D[B]\). The existing component theorems give a strict favorable-root majority in *each* fiber, uniformly over all outside bit assignments: density one for a singleton SCC; at least \(1-2^{-|B|}\) for a simple reader cycle and its inactive-edge subgraphs; at least \(3/4\) for a one-branching-target rooted feedback component; and at least \(9/16\) for a two-branching-target component, by the computer-assisted two-hub theorem and its inactive-parent extension. In every case both fiber favorable sets exceed half the cube, so
\[
A(f_{B,u})\cap\overline{A(g_{B,v})}\ne\varnothing.
\]
Choose a root \(z\) in this intersection. Insert the favorable \(f\)-fiber path rooted at \(z\) into the \(f_U\)-seam \(u\), and the favorable \(g\)-fiber path rooted at \(\bar z\) into the independent \(g_U\)-seam \(v\). The outer edge colors do not depend on \(B\)-bits, so both insertions preserve their respective \(0^*1^*\) words and traverse each direction once. The resulting favorable paths begin at antipodal roots \((x,z)\) and \((\bar x,\bar z)\). \(\square\)

**Theorem (two-hub apex facet coverage without oddness).** Let \(F\) be an unrestricted edge coloring of \(Q_{m+1}\), and suppose a direction \(j\) can be deleted from its influence graph so that every remaining SCC has at most two vertices of internal indegree greater than one. Then **each** of the two bit facets \(x_j=0\) and \(x_j=1\) contains a starting root of a full \(0^*1^*\) geodesic, independently of how the direction-\(j\) edges are colored.

*Proof.* The horizontal colorings \(f_0,f_1\) of the two \(j\)-facets share the common influence supergraph \(D(F)-j\). The preceding theorem gives \(A(f_1)\cap\overline{A(f_0)}\ne\varnothing\). The crossing-gate theorem (BG4) then yields favorable complete paths from both starting facets for every assignment to the joining edges. \(\square\)

**Corollary (three exceptional directions).** An arbitrary cube coloring with at most three edge-direction functions other than constants or signed one-bit readers has favorable roots in both bit facets of **every exceptional direction**. For any such direction \(j\), deletion leaves at most two potentially branching vertices in the common influence graph. This applies in unbounded dimension and does not assume antipodal oddness.

**Necessary obstruction.** A counterexample to bit-facet hitting at a particular direction \(j\) must have some SCC in the influence graph after deleting \(j\) with at least three distinct vertices of internal indegree at least two. This is a condition on the horizontal dependencies alone, stronger than requiring global influence connectivity.

The new proof is the cross-coloring seam induction: the computer-assisted ingredient is the published \(9/16\) two-hub favorable-root bound, not the induction itself. Independent direct path enumeration verified the cross-favorable conclusion on 100 randomly sampled pairs of independent two-hub colorings in each of dimensions four, five and six.

#### Opposed-root multiplicity and flat square derivatives

For a directed influence graph \(D\) whose SCCs each have at most two vertices of internal indegree greater than one, assign a factor
\[
\lambda(B)=
\begin{cases}
2,&|B|=1,\\
2^{|B|}-2,&B\text{ is a directed cycle},\\
2^{|B|-1},&B\text{ has one branching target},\\
2^{|B|-3},&B\text{ has two branching targets}.
\end{cases}
\]
The terminal-component induction proving opposed favorable-root existence also proves the quantitative bound
\[
\boxed{|A(f)\cap\overline{A(g)}|
\ge\prod_{B\in\operatorname{SCC}(D)}\lambda(B)>0.}
\tag{CD1}
\]
Indeed each opposed favorable root of the outer coloring has at least \(\lambda(B)\) inner choices: the respective fiber favorable sets have densities one, at least \(1-2^{-|B|}\), at least \(3/4\), or at least \(9/16\) in these four component classes. Inclusion-exclusion yields the factors. The two-hub factor depends on the previously published computer-assisted theorem.

Now fix a legal antipodally odd coloring \(c\) of \(Q_n\), with distinct directions \(h,j\). Restrict to the facet \(x_h=0\), and then cut across \(j\), yielding arbitrary colorings \(f_{00},f_{01}\) of \(Q_{n-2}\). Put
\[
L_{h,j}=A(f_{01})\cap\overline{A(f_{00})},
\qquad
\partial_hc_j(z)=c_j(z,h=0)+c_j(z,h=1)\pmod2.
\]

**Theorem (cross-witness derivative vanishing).** If \(c\) has no monochromatic full antipodal geodesic, then
\[
\boxed{L_{h,j}\subseteq\{z:\partial_hc_j(z)=0\}.}
\tag{CD2}
\]
Moreover \(\partial_hc_j(\bar z)=\partial_hc_j(z)\), so it also vanishes on the antipodal image of \(L_{h,j}\).

*Proof.* The bridge equivalence makes the facet coloring at \(h=0\) paired-root-free. Take \(z\in L_{h,j}\). If its two vertical direction-\(j\) edges above \(z,\bar z\) within that facet had equal colors, the endpoint construction yields paired favorable roots. When both edges are zero, cross them first from the antipodal roots \((z,0)\) and \((\bar z,1)\), then follow the favorable upper and lower paths rooted at \(z,\bar z\). When both are one, use the favorable horizontal paths first from antipodal roots \((\bar z,0)\) and \((z,1)\), then cross the edges last. Both cases contradict paired-root-freeness. Therefore
\(c_j(z,h=0)+c_j(\bar z,h=0)=1\).
Global antipodal oddness gives
\(c_j(\bar z,h=0)=1+c_j(z,h=1)\), so \(\partial_hc_j(z)=0\). Complementing all remaining input bits shows the derivative is antipodally even. \(\square\)

**Corollary (four-hub uniform-coupling exclusion).** Suppose a legal odd coloring has at most four nonsimple direction functions. If two distinct nonsimple directions \(h,j\) satisfy \(\partial_hc_j\equiv1\), then the coloring has a monochromatic full antipodal geodesic.

*Proof.* If it were bad, deleting \(h,j\) would leave at most two branching direction functions, so the common-influence root bound (CD1) would give \(L_{h,j}\ne\varnothing\). The preceding theorem would then force \(\partial_hc_j=0\) at a member of this set, a contradiction. \(\square\)

In particular, a hypothetical four-hub minimal obstruction has, for every ordered pair of different hubs \(h,j\), the quantitative restriction
\[
\boxed{
|\{z:\partial_hc_j(z)=0\}|
\ge\prod_{B\in\operatorname{SCC}(D(c)-\{h,j\})}\lambda(B)>0.
}
\tag{CD3}
\]
Every present hub-to-hub dependency must therefore switch its activity with other input bits; no such edge can be a uniform affine coupling. A closure argument should force a nonzero square derivative at one of the opposed favorable-root sites, contradicting (CD2).

##### A five-cube warning: active derivatives can avoid every cross-witness site

The preceding square-flatness theorem is a necessary condition for a **bad** coloring. Its converse cannot be obtained from antipodal oddness alone: an active derivative need not intersect the opposed favorable-root witness set. The following small construction makes this precise.

Use directions \((h,j,a,b,t)\) of \(Q_5\), and let \(p=x_a+x_b+x_t\pmod2\). Define
\[
\boxed{
\begin{aligned}
c_h(x)&=x_a,\\
c_j(x)&=p+\mathbf1_{\{x_a=x_b=x_t=1-x_h\}}\pmod2,\\
c_a(x)&=1+x_b,\qquad c_b(x)=1+x_a,\qquad c_t(x)=x_h.
\end{aligned}}
\tag{W1}
\]
Each edge-color function is independent of its own direction bit. The three-bit parity \(p\) changes under antipodal inversion, while the indicator in \(c_j\) remains invariant; all other functions are signed readers. Thus \(c\) is legal antipodally odd.

On the facet \(h=0\), the two subfacets \(j=0\) and \(j=1\) have the same horizontal three-cube coloring
\[
f_a=1+x_b,\qquad f_b=1+x_a,\qquad f_t=0.
\]
With the three-bit root encoding \(z=x_a+2x_b+4x_t\), its favorable-root set is
\[
A(f)=\{1,2,3,5,6,7\}.
\]
Consequently the opposed witness set is
\[
\boxed{L_{h,j}=A(f)\cap\overline{A(f)}=\{1,2,5,6\}.}
\tag{W2}
\]
On the other hand
\[
\boxed{\{z:\partial_hc_j(z)=1\}=\{0,7\}.}
\tag{W3}
\]
The derivative is nonzero but its active sites avoid the entire opposed witness set. Nonetheless this coloring is good: starting from the cube vertex \(x=4\) (only \(x_a=1\)), the direction order \(h,j,a,b,t\) has color word \(11111\).

The favorable-root sets, derivative support, legal oddness, and displayed monochromatic path were independently checked by finite enumeration. This example rules out the unconditional statement that every active square derivative must meet the opposed favorable-root set. A closing argument based on (CD2) must exploit counterexample minimality, gauge criticality, or additional simultaneous constraints across hub pairs; square oddness and active influence alone are insufficient.

#### Leaf-root surjectivity and a nonlinear hub-coupling closure class

**Lemma (prescribed constant-block roots).** Let \(f,g\) be binary edge colorings of the same \(Q_m\), with a common directed influence supergraph \(D\) whose strongly connected components each contain at most two vertices of internal indegree greater than one. Let \(S\) be a set of directions whose edge colors are constant in each of the two colorings, possibly with different constants. Then for every starting assignment \(u\in\mathbb F_2^S\) there is a root
\[
\boxed{x\in A(f)\cap\overline{A(g)},\quad x_S=u.}
\tag{LS1}
\]
The number of such roots is at least \(\prod_{B\in\operatorname{SCC}(D[[m]\setminus S])}\lambda(B)\), with the component factors established in (CD1).

*Proof.* The constant-colored \(S\)-directions admit a full \(0^*1^*\) geodesic from *every* root, obtained by listing all zero directions before all one directions. In \(f\) choose such a path from \(u\), and in \(g\) choose one from \(\bar u\). Let their zero-to-one seams occur at \(S\)-vertices \(v_f,v_g\). The induced colorings on \(T=[m]\setminus S\) at these two seam assignments share the influence supergraph \(D[T]\), hence by the quantitative cross-coloring condensation theorem have at least the displayed number of opposed favorable-root choices \(z,\bar z\). Insert the two \(T\)-geodesics at their respective \(S\)-seams. Since the \(S\)-edge colors are constant, the resulting complete paths preserve the nondecreasing color words and start at antipodal roots \((u,z),(\bar u,\bar z)\). \(\square\)

**Theorem (closure for leaf-supported hub derivatives).** Suppose a legal odd coloring \(c\) of \(Q_n\) has at most four nonsimple direction functions. Choose two distinct nonsimple directions \(h,j\). Let \(S_{h,j}\) consist of simple directions whose edge colors read only \(h\) or only \(j\):
\[
c_s(x)=a_s+x_h\quad\text{or}\quad c_s(x)=a_s+x_j.
\]
Assume the Boolean square derivative
\[
\partial_h c_j(z)=c_j(z,h=0)+c_j(z,h=1)
\]
depends only on the bits of \(S_{h,j}\). If \(\partial_hc_j\) is nonzero at any input, then
\[
\boxed{c\text{ possesses a monochromatic antipodal full geodesic}.}
\tag{LS2}
\]

*Proof.* Suppose \(c\) were bad. Delete direction \(h\), fix its bit to zero, then split the resulting facet along \(j\) into colorings \(f_{00},f_{01}\) on the remaining \(n-2\) directions. Every direction of \(S_{h,j}\) becomes constant-colored in both horizontal colorings, because its only reader is a fixed deleted bit. At most two nonsimple direction functions remain, so the common influence graph after deleting \(h,j\) has no SCC with more than two branching vertices.

Apply (LS1) to \(f=f_{01}\), \(g=f_{00}\). For every assignment \(u\) of the bits in \(S_{h,j}\), the opposed favorable-root set
\(L_{h,j}=A(f_{01})\cap\overline{A(f_{00})}\)
contains a root with that assignment. The previously proved square-flatness theorem (CD2) says \(\partial_hc_j\) vanishes at every such root whenever \(c\) is bad. Because its value depends only on \(u\), it must vanish for all assignments, contradicting the hypothesis that it is nonzero somewhere. \(\square\)

This strengthens the uniform active-coupling exclusion: a four-hub obstruction cannot have a nonzero hub-to-hub interaction whose activity is controlled solely by simple leaf bits attached to the two participating hubs, even when that control function is nonlinear. In a canonical minimal hub-star kernel, any present feedback arc between distinct hubs must have activity depending on a bit outside those two hubs' simple leaf sets. The result is dimension-uniform but does not rule out interactions controlled by other hubs or their leaf bits.
\n\n## Finite hub kernel certification\n\nThe four-hub canonical stars in dimensions seven through ten were tested with exhaustive Boolean solvers. All nine leaf-pattern instances were unsatisfiable. Thus the first bad four-hub kernel, if any, occurs in dimension eleven or twelve. Complete generators and checks are preserved in the local research artifacts.\n
Reproduction: sat_hub_slots.py checks hub-step orders with leaf slots; sat_hub_kernel.py checks full direction orders. The n=7 and n=8 results agree in both constructions. Further n=9 and n=10 runs each return unsatisfiable.


#### Arc-disjoint feedback necessary in every odd cube obstruction

For a binary edge coloring \(f\) of a cube, let \(D(f)\) have an arrow \(i\to j\) if direction-\(j\) edge colors may depend on bit \(i\).

**Lemma (acyclic root saturation).** If \(D(f)\) is acyclic, every starting root has a full antipodal geodesic with color word \(0^*1^*\). Traverse unused zero-colored edges until none remain. All remaining colors are then one. Repeatedly traverse a sink in the induced influence graph on unused directions: its bit is not read by any other unused direction, so their colors remain one. This gives the desired full path from the arbitrary starting root.

**Theorem (arc-complement cycle condition).** If a legal antipodally odd coloring \(c\) of \(Q_n\) is bad, then for every influence arc \(h\to j\) in \(D(c)\), the digraph \(D(c)-\{h,j\}\) contains a directed cycle.

*Proof.* Suppose the complement of an arc is acyclic. Fix the \(h\)-bit zero, and split this facet into its two \(j\)-layers. Each resulting horizontal edge coloring has acyclic influence graph and therefore has a favorable full path from every root. Hence their opposed favorable-root witness set is the entire remaining vertex cube. The square-flatness theorem previously proved in this Subsection says that badness forces \(\partial_hc_j\) to vanish at every such root. Thus \(\partial_hc_j\equiv0\), contradicting the assumed influence arc. \(\square\)

**Corollary (arc endpoint sets do not meet every cycle).** In a bad legal odd coloring, the endpoints of any influence arc fail to form a directed feedback vertex set: at least one directed cycle survives their deletion.

*Proof.* This is the preceding arc-complement cycle condition. A surviving cycle avoids the two endpoints; its vertices may meet other vertices of a cycle containing the selected arc. A conclusion about vertex-disjoint cycle packing requires an additional argument.

#### Two-vertex feedback elimination by a monochromatic hub connector

Let \(D(c)\) be the directed influence graph of a legal antipodally odd undirected-edge coloring of \(Q_n\). A *feedback vertex set* \(H\) is a set of dimensions whose deletion makes the induced digraph acyclic.

**Theorem (two-vertex feedback closure).** If \(D(c)\) has a feedback vertex set of size at most two, then \(c\) has a monochromatic full antipodal geodesic. Consequently every minimum-dimensional bad legal coloring has directed feedback vertex number at least three.

*Proof.* If \(D(c)\) is acyclic, the all-root acyclic greedy theorem gives a full \(0^*1^*\) geodesic, converted to monochromatic by root-slide surgery. If a feedback vertex set is a singleton \(h\), choose any influence arc incident with \(h\). Removing that arc's endpoints also removes \(h\), leaving an acyclic digraph; the arc-complement cycle theorem immediately gives a monochromatic geodesic.

Now let \(H=\{h,j\}\) be a feedback vertex set, with nonempty acyclic complement \(S\). If an influence arc joins \(h\) and \(j\) in either direction, deleting these two endpoints leaves an acyclic graph, and the arc-complement theorem applies.

Suppose neither hub reads the other. Their edge-color functions therefore depend only on the \(S\)-bits, say \(b_h(z),b_j(z)\), and satisfy \(b_h(\bar z)=1+b_h(z)\) and similarly for \(b_j\).

If they agree at some \(z\), they also agree with the opposite color at \(\bar z\). Hence choose a site where both hub edges are zero. Traverse \(h,j\) first at that site; the two edges have color zero and do not affect one another's colors. In the resulting fixed hub layer, the \(S\)-direction influence graph is acyclic. Its all-root theorem provides a favorable full \(S\)-geodesic starting at \(z\). Concatenation has word \(0^*1^*\).

It remains to suppose \(b_j(z)=1+b_h(z)\) for every \(z\). The odd function \(b=b_h\) is nonconstant on \(S\); choose a direction \(s\in S\) and a site \(z\) where \(b(z\oplus e_s)=1+b(z)\). Put \(t=b(z)\). Fix the other \(S\)-bits at \(z\). If the direction-\(s\) edge color takes the value \(t\) at some choice of the two hub bits, choose the initial hub bits so that, after traversing \(h\), its value is \(t\). Then the three-step block
\[
\boxed{h,\ s,\ j}
\]
is monochromatic of color \(t\): the first hub edge has color \(t\), the middle edge was chosen color \(t\), and the final hub edge has color \(1+b(z\oplus e_s)=t\). If no hub-bit choice gives color \(t\) on the \(s\)-edge at this fixed \(S\)-site, its color is identically \(1+t\) on all four hub-bit assignments. In this case the three-step block
\[
\boxed{j,\ s,\ h}
\]
is monochromatic of color \(1+t\). The first edge has color \(1+t\), the middle edge has that fixed color, and the last edge has color \(b(z\oplus e_s)=1+t\).

Thus some complete traversal of the three directions \(C=\{h,j,s\}\), at the fixed other \(S\)-bits, is monochromatic of a color \(q\). Put \(T=S\setminus\{s\}\), whose induced influence graph is acyclic. If \(q=0\), traverse this block first and then, at the resulting fixed \(C\)-state, use the all-root acyclic theorem to traverse every direction of \(T\) with word \(0^*1^*\). If \(q=1\), first traverse all \(T\)-directions with a favorable full geodesic ending at the prescribed \(T\)-site \(z_T\), with the \(C\)-bits fixed at the block's starting values, and then traverse the monochromatic-one block. Either concatenation traverses every direction once and has word \(0^*1^*\). Root-slide surgery finishes the proof. \(\square\)

**Inductive significance.** A hypothetical minimal counterexample must have directed feedback vertex number at least three, even if many nonhub directions have arbitrary nonlinear functions and high internal indegrees. The two-hub argument uses only the acyclic greedy lemma, antipodal oddness, and a three-step monochromatic connector; it does not invoke the finite two-hub certificate. A natural next target is to construct analogous bounded-length connectors from three feedback directions and an acyclic exterior.


#### Prescribed roots on acyclic source blocks and feedback-dependent activity

Write \(A_0(f)\) for roots admitting a full path with word \(0^*1^*\), and \(A_1(f)\) for roots admitting a full path with word \(1^*0^*\).

**Lemma (source-block cross gluing).** Let \(f,g\) be ordinary binary edge colorings on \(Q_{S\cup T}\). Suppose their common influence supergraph has no arrow from \(T\) into \(S\), and its restriction to \(S\) is acyclic. For each pair of assignments \(v,w\in\mathbb F_2^S\), suppose the two induced \(T\)-colorings satisfy
\[
|A_0(f_{T,v})\cap A_1(g_{T,w})|\ge \kappa>0.
\]
Then, for every prescribed assignment \(u\in\mathbb F_2^S\),
\[
\boxed{|\{x\in A_0(f)\cap A_1(g):x_S=u\}|\ge\kappa.}
\tag{AS1}
\]

*Proof.* The acyclic root-saturation lemma, applied also after interchanging the colors, gives an increasing full \(S\)-path for \(f\) and a decreasing full \(S\)-path for \(g\), both starting at \(u\). Let \(v,w\) be their respective change-of-color seams. Choose any cross root \(z\) for \(f_{T,v},g_{T,w}\). Insert the increasing and decreasing \(T\)-paths at the corresponding seams. The \(S\)-edge colors do not depend on the \(T\)-bits, so both inserted paths preserve the required color words. They start at the same full root \((u,z)\). Distinct choices of \(z\) give distinct roots. Empty blocks and paths with a single color are included by allowing endpoint seams. \(\square\)

The hypothesis on the \(T\)-fibers is available from each of the following established modules: the common directed influence theorem with at most two internal branching targets per strongly connected component; the universal cross-favorability theorem for a common linear-forest interaction graph; or the Hall theorem for two independently functional colorings. The last module does not require the two fiber colorings to have the same reader map. This source-block statement prescribes exterior source bits, and therefore does not assert the endpoint prescription that fails for general path-local pairs.

**Theorem (acyclic-source activity exclusion).** Let \(c\) be a legal antipodally odd coloring, and choose distinct directions \(h,j\). In the residual influence digraph \(D(c)-\{h,j\}\), let \(S\) be a source-closed acyclic set and put \(T=[n]\setminus(\{h,j\}\cup S)\). Assume that every pair of \(T\)-fibers of the two horizontal colorings \(f_{01},f_{00}\) satisfies one of the cross-favorability modules above. If the nonzero Boolean derivative \(\partial_hc_j\) depends only on bits in \(S\), then \(c\) has a monochromatic full antipodal geodesic.

*Proof.* If \(c\) were bad, square flatness (CD2) would force \(\partial_hc_j=0\) on
\[
L_{h,j}=A_0(f_{01})\cap A_1(f_{00}).
\]
By (AS1), this set contains a root over every assignment of the \(S\)-bits. A derivative depending only on those bits must consequently vanish everywhere, contrary to the hypothesis. \(\square\)

More generally, badness forces at least \(\kappa\) zeros of the derivative in every prescribed \(S\)-fiber. This replaces the constant-block conclusion (LS1) by an arbitrarily large acyclic source block, including directed source trees with nonlinear direction functions.

**Corollary (activity must use surviving feedback descendants).** Let \(S\) comprise all vertices of \(D(c)-\{h,j\}\) which are not reachable from a directed cycle. This set is source-closed and acyclic: an arrow into it from a cycle descendant would make its target a cycle descendant, and a cycle inside it would contradict its definition. Under the same fiber hypotheses, if \(c\) is bad and \(h\to j\) is an influence arc, then some \(v\in T\) satisfies
\[
\boxed{\partial_v\partial_hc_j\not\equiv0.}
\tag{AS2}
\]
Indeed, the influence arc makes \(\partial_hc_j\) nonzero. If all its derivatives in \(T\) vanished, it would depend only on \(S\), contradicting the preceding theorem. The bit \(v\) need only be downstream of a surviving directed cycle; it need not lie on the cycle itself.

In particular, the fiber hypothesis holds when \(c\) has at most four nonsimple direction functions and \(h,j\) are two of them. Deleting these two directions leaves at most two possible branching targets, and restriction to \(T\) cannot add others. Thus every active hub-to-hub derivative in a bad four-hub coloring must have a nonzero mixed derivative with a bit downstream of residual feedback.

**Path toward closure.** The arc-complement condition supplies surviving feedback; (AS2) now requires that feedback to control the activity of each participating coupling. A closing argument must show that these mixed-derivative requirements either expose a square at a cross-favorable root or admit a feedback-reducing monochromatic connector. Neither conclusion follows from the projection lemma alone. In particular, it does not supply arbitrary prescribed roots in the residual feedback block, and it does not upgrade cycle survival to vertex-disjoint cycle packing.


#### Switch-component intersection lemma

Let \(f:Q_m\to\mathbb F_2\) be antipodally odd. Let \(\Gamma_f\) be the subgraph of cube edges across which \(f\) changes.

**Theorem.** Every other antipodally odd function \(g\) changes on some edge of \(\Gamma_f\) if and only if \(\Gamma_f\) contains a connected component preserved by antipodal complementation.

*Proof.* If a component contains \(z\) and \(\bar z\), every odd \(g\) takes opposite values there. Along a connecting path in that component, \(g\) must change, giving a common switch. Conversely, if no component is antipodally invariant, pair up the components as \(C,\bar C\) and make \(g\) constant zero on one and constant one on its mate. This defines an odd \(g\) with no switches along any edge of \(\Gamma_f\). \(\square\)

If \(z,\bar z\) belong to one component \(C\), every odd \(g\) has at least \(\lambda_C(z,\bar z)\) common-switch edges with \(f\), where \(\lambda_C\) is the minimum edge-cut size between the two vertices. Each path between them must cross a \(g\)-switch edge, and all edges of \(C\) are already \(f\)-switches.


#### Synchronized feedback switch closes NORI1

Let \(H\sqcup S\) partition directions of a legal odd cube-edge coloring. Assume the induced influence graph on \(S\) is acyclic, and no hub direction reads another hub's bit. Thus its hub-edge color functions \(b_h(z)\) depend only on \(z\in Q_S\).

**Theorem.** If some edge \(z,z\oplus e_s\) in \(Q_S\) switches every hub color,
\[
\boxed{b_h(z\oplus e_s)=1+b_h(z)\quad(h\in H),}
\]
the full coloring has a monochromatic antipodal geodesic.

*Proof.* Choose a desired bit \(t\). Traverse before direction \(s\) all hubs colored \(t\) at \(z\), and after \(s\) the hubs colored \(1+t\) at \(z\). Their colors at their respective steps are all \(t\), because every hub flips its color across \(s\) and none reads another hub bit. Varying the starting hub bits can realize any hub-bit assignment when step \(s\) is taken. If its edge color can equal \(t\), the entire hub-and-\(s\) block is monochromatic \(t\). Otherwise that edge color is identically \(1+t\) for all hub assignments at \(z\); choose the opposite desired bit and repeat to obtain a monochromatic block of color \(1+t\).

The remaining directions \(T=S\setminus\{s\}\) have acyclic influence graph. For a zero-colored block, traverse the block first and follow it by an all-root favorable full \(T\)-geodesic. For a one-colored block, take an all-root favorable \(T\)-geodesic ending at the selected \(T\)-site, then append the block. Both constructions yield a complete path with word \(0^*1^*\). The odd root-slide lemma makes it monochromatic. \(\square\)

**Corollary.** If every hub except perhaps one reads either an odd Boolean function \(f:Q_S\to\mathbb F_2\) or its complement, and the switch graph of \(f\) has a component containing antipodal vertices, the full coloring is good. Indeed the remaining odd hub function must switch with \(f\) on some edge by the preceding switch-component theorem. On that edge all hub colors switch together, and the theorem applies. This is an all-dimensional closure class with any number of feedback directions.


##### Parity limitation of switch-component transport

**Lemma.** Let \(m\) be even and \(f:Q_m\to\mathbb F_2\) be antipodally odd. Then no connected component of its switch graph contains antipodal vertices.

*Proof.* Each edge of the switch graph changes \(f\), so any switch-only path from \(z\) to \(\bar z\) must have odd length, since \(f(\bar z)=1+f(z)\). But every cube path between antipodes has length congruent to \(m\) modulo two, and \(m\) is even. Contradiction. \(\square\)

This also has a constructive dual proof. Let \(p(z)=\sum_{s=1}^m z_s\pmod2\), which is antipodally even for even \(m\). Given any odd \(f\), put \(g=f+p\). Then \(g\) is also odd, while every cube edge changes \(p\), so
\[
\partial_sg(z)=1+\partial_sf(z).
\]
Consequently no edge changes both \(f\) and \(g\). Thus the switch-component criterion can enforce a common switch only in odd dimension.

Dependence on all input bits does not replace the missing parity condition. For instance, in dimension five take \(f(x)=x_1+p(x_2,x_3,x_4,x_5)\), where \(p\) indicates the antipodal pair \(0000,1111\) in its four-bit input. The function \(f\) is odd and depends on every input bit, yet its switch-edge components occur in disjoint antipodal pairs. Therefore the robust closing property is antipodal connectivity of the switch graph, not merely full bit sensitivity.

#### Global switch-packing rigidity and antipodal component duality

Fix \(m\ge2\). For an antipodally odd Boolean function \(f:Q_m\to\mathbb F_2\), let \(E(f)\) contain those cube edges across which \(f\) changes.

**Lemma (odd switch isoperimetry).** For \(\phi=(-1)^f\), with normalized Walsh coefficients \(\widehat\phi(T)\),
\[
\boxed{|E(f)|=2^{m-1}\sum_{|T|\ {\rm odd}}|T|\widehat\phi(T)^2\ge2^{m-1}.}
\tag{SP1}
\]
Equality holds precisely for a signed one-bit reader \(f(x)=a+x_j\).

*Proof.* Sum the switching probabilities across all \(m\) bit directions, each having \(2^{m-1}\) undirected cube edges. Parseval and the absence of even Walsh levels give the lower bound. Equality forces Fourier support solely at singleton sets. If \(\phi=\sum_j a_j\chi_j\) is Boolean, comparing the degree-two coefficients of \(\phi^2=1\) gives \(a_ja_l=0\) for all \(j\ne l\); Parseval leaves just one coefficient of magnitude one. \(\square\)

For odd functions \(f_1,\ldots,f_k\), put \(r_e=|\{i:e\in E(f_i)\}|\), \(R=\sum_e(r_e-1)_+\), and \(U=|\{e:r_e=0\}|\). Let
\(\Delta_i=\sum_{|T|\ge3}(|T|-1)\widehat\phi_i(T)^2\), where \(\phi_i=(-1)^{f_i}\).

**Theorem (switch-incidence budget).**
\[
\boxed{R-U=2^{m-1}\left(k-m+\sum_{i=1}^k\Delta_i\right).}
\tag{SP2}
\]
On every full antipodal geodesic \(P\), if the \(i\)-th odd function switches \(1+2a_i(P)\) times, and \(R(P),U(P)\) denote repeated-switch and no-switch edge counts along \(P\), then
\[
\boxed{R(P)-U(P)=k-m+2\sum_i a_i(P).}
\tag{SP3}
\]
*Proof.* Count all switch incidences first by odd functions, then by cube edges. Each function contributes \(2^{m-1}(1+\Delta_i)\) from (SP1), while the edge sum is \(|E(Q_m)|-U+R=m2^{m-1}-U+R\). The same count on a full path proves (SP3), because every odd function switches an odd positive number of times between antipodal endpoints. \(\square\)

**Theorem (near-capacity rigidity).** Suppose the switch sets \(E(f_i)\) are pairwise disjoint, and \(k\ge m-1\). Then \(k\le m\), and all \(f_i\) are signed one-bit readers with *different* reader bits. If \(k=m-1\), the family extends to size \(m\) by adjoining the unique unused bit reader, with either sign.

*Proof.* On a full antipodal path, the disjoint switch sets each require one edge, forcing \(k\le m\). For \(k\ge m-1\), if any \(f_i\) switched three times on a full path, the other \(k-1\) functions would require at least \(k+2>m\) distinct edges, impossible. Thus each \(f_i\) switches once along **every** full antipodal path. Under the uniform distribution on rooted full geodesics, every cube edge occurs with probability \(2^{-(m-1)}\); hence \(|E(f_i)|=2^{m-1}\). The isoperimetric lemma makes each a signed reader. Their switch sets are disjoint only when their reader bits differ. \(\square\)

**Corollary (gap for maximal disjoint switch families).** A family maximal under adding further odd functions has either at most \(m-2\) members or \(m\) members: there is no maximal family of size \(m-1\). This gap is sharp for \(m\ge3\). Take the odd triple-parity function \(f_1=x_1+x_2+x_3\) and the independent one-bit readers \(f_2=x_4,\ldots,f_{m-2}=x_m\). Their switch supports partition all cube edges, so no further odd function can avoid their union.

**Theorem (common-switch avoidance dichotomy).** For any family of odd functions, let \(\Gamma\) retain every cube edge belonging to at least one \(E(f_i)\), keeping isolated vertices. There exists another odd function \(g\) with no switches in \(\Gamma\) if and only if \(\Gamma\) has no antipodally invariant connected component. If the components of \(\Gamma\) form \(p\) pairs under antipodal inversion, precisely \(2^p\) such functions \(g\) exist.

*Proof.* Avoiding every retained edge means \(g\) is constant on every connected component of \(\Gamma\). Oddness requires its constant values on antipodal components to be opposite. This is possible precisely when no component contains an antipodal vertex pair, leaving one binary choice per pair. \(\square\)

These theorems apply to arbitrary dimensions and arbitrary numbers of odd switch functions, without a finite-case search. The budget makes nonlinear dependence consume additional switch capacity, while the component theorem identifies when any further independent odd switch channel is impossible. A NORI1 closing step would have to turn unavoidable common-switch edges into dimension-simple path exchanges; no such general exchange is yet established.

#### Full antipodal switch-geodesics at deficiency two

Let \(m\ge3\), and take \(k=m-2\) antipodally odd Boolean functions \(f_1,\ldots,f_k:Q_m\to\mathbb F_2\), with pairwise disjoint edge-switch sets. Let \(\Gamma\) be the union of their switch-edge graphs.

**Theorem (dimension-simple saturation dichotomy).** The following are equivalent: (a) at least one \(f_i\) is not a signed one-bit reader; (b) \(\Gamma\) contains a full antipodal geodesic of length \(m\); (c) \(\Gamma\) contains a connected component preserved by antipodal inversion; (d) no further odd Boolean function can be added while preserving pairwise disjointness of switch sets. If all functions are readers, their reader bits are different, and the family instead extends to the full set of \(m\) bit readers.

*Proof.* If all functions are signed readers, the disjointness assumption makes their reader bits distinct. Two bit directions remain absent from the union switch graph. Every component therefore fixes those two bits and is disjoint from its antipodal image; the missing bit readers can be adjoined.

If some \(f_i\) is nonlinear, odd-switch isoperimetry gives \(|E(f_i)|>2^{m-1}\). A uniformly random rooted antipodal full geodesic contains each edge with probability \(2^{-(m-1)}\); hence the expected number of \(f_i\)-switches exceeds one. Every antipodal path has an odd number of \(f_i\)-switches, so some full antipodal geodesic \(P\) has at least three such switches. All other \(k-1=m-3\) odd functions switch on \(P\) at least once. Their switch sets are pairwise disjoint. Therefore at least \(3+(m-3)=m\) different edges of this length-\(m\) geodesic lie in \(\Gamma\). All its edges must lie in \(\Gamma\), with three switches of one function and one of every other function. This proves (b), implying (c). A switch-union component containing antipodes forbids any further odd function with disjoint switch support by the previously proved antipodal component duality, proving (d). All implications and the reader alternative follow. \(\square\)

For normalized Walsh spin coefficients \(\widehat\phi_i(T)\), \(\phi_i=(-1)^{f_i}\), write
\[
\Delta_i=\sum_{\substack{|T|\ge3\\|T|\ {\rm odd}}}(|T|-1)\widehat\phi_i(T)^2.
\]

**Theorem (saturation frequency identity).** For a uniformly chosen rooted full antipodal geodesic \(P\),
\[
\boxed{\Pr[E(P)\subseteq E(\Gamma)]=\frac12\sum_{i=1}^{m-2}\Delta_i.}
\tag{SG1}
\]

*Proof.* Every odd function switches an odd positive number of times on \(P\), and disjointness limits the total to \(m\). With \(m-2\) functions, either all switch once and two path edges have no switch, or one function switches three times, the others once, and every path edge belongs to the union. Thus the switch-incidence excess above \(m-2\) equals two times the indicator of full path saturation. The expected number of switches of function \(i\) is \(|E(f_i)|/2^{m-1}=1+\Delta_i\). Taking expectations proves (SG1). \(\square\)

**Sharp examples.** Odd parity in three bit directions, together with individual readers of every remaining bit, forms a maximal disjoint family of \(m-2\) functions with saturation probability one. Replacing the triple-parity function by odd majority on those three bits gives probability \(1/4\), since its Walsh weight at degree three is \(1/4\).

This is a global passage from switch-graph connectivity to a *dimension-simple full antipodal geodesic*, retaining the requirement that no dimension repeat. It makes no assumption that the auxiliary odd functions are original cube-edge colors: a further structural exchange theorem is needed to turn their switch path into a monochromatic NORI1 path.


#### Global influence-congestion law for unrestricted NORI1 colorings

Let \(c\) be any legal antipodally odd binary coloring of the undirected edges of \(Q_n\), \(n\ge2\). Extend each direction-\(i\) edge-color function to a Boolean vertex function
\[
f_i(x)=c(\{x,x\oplus e_i\}),
\]
which is independent of \(x_i\) and antipodally odd on \(Q_n\). For a vertex-cube edge \(e=\{x,x\oplus e_j\}\), let
\[
\boxed{r(e)=|\{i\ne j:f_i(x)\ne f_i(x\oplus e_j)\}|.}
\tag{IC1}
\]
This counts how many other direction-edge colors change when the vertex bit \(j\) is toggled. Call an edge *silent* if \(r(e)=0\), and count its excess simultaneous switch incidences by \((r(e)-1)_+\). Write
\[
U(c)=|\{e:r(e)=0\}|,\qquad
R(c)=\sum_{e\in E(Q_n)}(r(e)-1)_+.
\]

**Theorem (unrestricted influence-congestion identity).** With normalized Walsh coefficients of \(\phi_i=(-1)^{f_i}\),
\[
\boxed{
R(c)-U(c)=2^{n-1}
\sum_{i=1}^n
\sum_{\substack{T\subseteq[n]\setminus\{i\}\\|T|\ge3,\ |T|\ {\rm odd}}}
(|T|-1)\widehat\phi_i(T)^2
\ge0.
}
\tag{IC2}
\]
Equality holds precisely when **all** direction-edge functions are signed one-bit readers, \(c_i(x)=a_i+x_{p(i)}\). If any direction function is nonlinear, then \(R(c)>U(c)\).

*Proof.* Apply the global switch-incidence budget (SP2) to the family \(f_1,\ldots,f_n\) on \(Q_n\), with the number of odd functions equal to the dimension \(k=m=n\). Their cube-edge switch multiplicity is (IC1), because \(f_j\) does not read bit \(j\). The budget gives (IC2). Every summand is nonnegative. Vanishing forces every \(\phi_i\) to have Walsh support only on singleton sets, and Booleanity forces a single signed singleton character. \(\square\)

**Theorem (pathwise influence curvature).** On every full antipodal geodesic \(P\), let \(U(P)\) count silent edges and \(R(P)\) the excess simultaneous switch incidences. Then
\[
\boxed{
R(P)-U(P)=2\sum_{i=1}^n a_i(P)\ge0,
}
\tag{IC3}
\]
where the number of changes of \(f_i\) along \(P\) is \(1+2a_i(P)\). In particular, the surplus is even on every path, and a direction-edge color function changing three or more times forces at least two more excess switch incidences than silent edges on that path.

*Proof.* Each \(f_i\) is odd at the antipodal endpoints, so it changes an odd positive number of times along \(P\). Specialize the pathwise switch budget (SP3) to \(k=m=n\). \(\square\)

**Corollary (all-dimensional no-congestion closure).** If no cube edge changes the colors of two different direction-edge functions simultaneously, then \(c\) has a monochromatic antipodal full geodesic.

*Proof.* The no-congestion assumption gives \(r(e)\le1\) everywhere, hence \(R(c)=0\). Formula (IC2) forces \(U(c)=0\) and all nonlinear Walsh masses to vanish. Therefore each direction-edge function is a signed one-bit reader. The all-dimensional functional-reader root theorem already proved in Article XIV then produces a monochromatic antipodal geodesic. \(\square\)

**Closure target without hub-count induction.** A bad legal coloring must have strictly more repeated than silent switch incidences, with a nonnegative even surplus on each full antipodal geodesic. Thus the first global missing step can be expressed as a *congestion-to-exchange principle*: exploit an overloaded edge along a minimum-switch Petrie geodesic to perform a dimension-simple square exchange that lowers the number of color changes, or identify an antipodal topological obstruction to doing so. Unlike proving one extra bounded hub case, this target involves every direction simultaneously and makes no fixed-dimensional reduction.

#### Canonical saturation of disjoint odd switch channels

Let \(F=\{f_1,\ldots,f_k\}\) be antipodally odd Boolean functions on \(Q_m\) with pairwise disjoint switching-edge sets.

**Lemma (reader peeling).** If \(f_i=a+x_j\), then every other \(f_l\) is independent of bit \(j\); after removing this function and bit, the remaining odd functions have pairwise disjoint switch sets on \(Q_{m-1}\).

*Proof.* A signed reader changes across every edge in direction \(j\), so no other member can change along such an edge. Thus the other members ignore bit \(j\), and their oddness and switch disjointness descend to the remaining cube. \(\square\)

**Theorem (global switch-channel saturation).** Every pairwise-disjoint family can be extended to a maximal such family \(F^*\), through at most \(m-k\) additions. Every maximal family falls into one of two disjoint classes:

1. A complete collection of \(m\) signed bit readers, with all reader bits different.
2. At most \(m-2\) functions, whose switch-union graph has a connected component containing antipodal vertices and whose residual family after reader peeling is nonempty and nonlinear.

*Proof.* Every odd function switches on each full antipodal geodesic at least once, so disjointness bounds the family size by \(m\). Whenever the union switch graph has no antipodally invariant component, the earlier switch-component duality constructs another odd function avoiding all retained switch edges; adjoin it. The procedure terminates within \(m-k\) steps. At termination the union graph has a component containing antipodal vertices. The near-capacity rigidity theorem forces an \(m\)-member family to be the full signed reader basis and excludes a maximal \((m-1)\)-member family. Every smaller maximal family therefore has at most \(m-2\) members. It cannot consist entirely of readers, since one missing reader could be added. Reader peeling leaves a nonempty nonlinear residual family. \(\square\)

**Corollary (full geodesics at the near-capacity boundary).** When the second alternative has \(m-2\) members, its union switch graph already contains a full dimension-simple antipodal geodesic, by the earlier switch-saturation theorem.

This construction terminates for all dimensions without separate case checks. The two remaining mechanisms are the rigid basis at high switch capacity and antipodal component connectivity at low capacity. Passing from an antipodally connected component at arbitrary switch density to a dimension-simple path, and then to a monochromatic path in the original edge coloring, remains a proof target rather than an established implication.

#### Opposed-root cylinders through terminal acyclic blocks

Let \(f,g\) be arbitrary edge colorings of the same \(Q_m\). Let \(A(f)\) denote the roots admitting full antipodal geodesics with edge-color word \(0^*1^*\). Let \(D\) be a common directed influence supergraph: an arrow \(p\to q\) means bit \(p\) may influence the color of a direction-\(q\) edge in either coloring.

**Theorem (acyclic block cylinder).** Partition the dimensions into \(S\sqcup T\), where \(D[S]\) is acyclic and no arrow leads from \(S\) into \(T\). The \(T\)-edge colors are therefore independent of the \(S\)-bits and induce colorings \(f_T,g_T\). Then
\[
\boxed{
Q_S\times \bigl(A(f_T)\cap\overline{A(g_T)}\bigr)
\subseteq A(f)\cap\overline{A(g)}.
}
\tag{RC1}
\]

*Proof.* Choose \(z\in A(f_T)\cap\overline{A(g_T)}\). Select favorable complete \(T\)-geodesics in \(f_T,g_T\), rooted respectively at \(z,\bar z\). Let \(v,w\) be their possibly different zero-to-one seam vertices. Fix any \(u\in Q_S\). The \(S\)-fiber colorings of \(f\) at \(T\)-state \(v\) and of \(g\) at \(T\)-state \(w\) have acyclic influence graphs, because all their influence arrows belong to \(D[S]\). By the previously established acyclic all-root theorem, each has a favorable full \(S\)-geodesic rooted at \(u\) and \(\bar u\), respectively. Insert these \(S\)-geodesics at the corresponding \(T\)-seams. Every \(T\)-edge color is independent of the \(S\)-bits, so both original \(T\)-words are unchanged. Inserting \(0^*1^*\) at a zero-to-one seam preserves nondecreasing color words. The resulting complete paths use each direction once and are rooted at the antipodal vertices \((u,z),(\bar u,\bar z)\). Since \(u\) was arbitrary and \(z\) was fixed, the claimed whole cylinder belongs to the opposed favorable-root set. \(\square\)

**Corollary (multiplicity).** If the common influence digraph on \(T\) has at most two vertices with internal indegree greater than one in each SCC, then
\[
\bigl|A(f)\cap\overline{A(g)}\bigr|
\ge 2^{|S|}
\prod_{B\in\operatorname{SCC}(D[T])}\lambda(B),
\tag{RC2}
\]
where the component factors \(\lambda(B)>0\) are those of the published quantitative cross-coloring condensation theorem. Each opposed favorable \(T\)-root supplies a full parallel \(S\)-subcube of favorable roots.

This result extends the previously published prescribed constant-leaf lemma: direction colors within \(S\) may depend nonlinearly on \(T\) and may have arbitrary acyclic internal dependencies. It is an unrestricted-dimensional transport theorem, not a fixed-order calculation.

#### Flat subcubes in square derivatives of hypothetical four-hub obstructions

Let \(c\) be a legal antipodally odd coloring of the undirected edges of \(Q_n\). Call a direction *simple* if its color is a signed one-bit reader \(c_i(x)=a_i+x_{r(i)}\), and otherwise *exceptional*. Fix distinct directions \(h,j\), both exceptional, and assume that there are at most four exceptional directions overall.

Set \(D'=D(c)-\{h,j\}\). Choose any partition of the remaining dimensions into \(S\sqcup T\) such that \(D'[S]\) is acyclic and no influence arrow goes from \(S\) into \(T\). Define the square derivative of the direction-\(j\) edge-color function by
\[
\partial_h c_j(u,z)=c_j(h=0,u,z)+c_j(h=1,u,z)\pmod2,
\]
where \(u\in Q_S,z\in Q_T\).

**Theorem (flat square-derivative cylinders).** If \(c\) is a NORI1 counterexample, then there exists a set \(K\subseteq Q_T\) with
\[
\boxed{|K|\ge\prod_{B\in\operatorname{SCC}(D'[T])}\lambda(B)>0}
\tag{FC1}
\]
such that
\[
\boxed{\partial_h c_j(u,z)=0\quad\text{for every }u\in Q_S,\ z\in K.}
\tag{FC2}
\]
Thus the zero set of the derivative contains at least \(|K|\) disjoint parallel full \(S\)-subcubes. Here the factors \(\lambda(B)\) are those in the previously proved quantitative two-hub opposed-root theorem; the corresponding estimate relies on its published computer-assisted component bound.

*Proof.* Restrict the coloring first to \(h=0\), then split its directions by \(j=0,1\), obtaining arbitrary horizontal colorings \(f_{00},f_{01}\) on \(Q_{S\cup T}\). Their common influence supergraph is \(D'\). On the induced \(T\)-direction colorings, at most two original exceptional direction functions remain; all others are constants or signed readers after restriction. Hence each SCC of \(D'[T]\) has at most two vertices with internal indegree greater than one. The quantitative cross-coloring theorem produces
\[
K=A((f_{01})_T)\cap\overline{A((f_{00})_T)}
\]
of cardinality at least the product in (FC1). The acyclic-block cylinder theorem (RC1) gives
\[
Q_S\times K\ \subseteq\
A(f_{01})\cap\overline{A(f_{00})}=L_{h,j}.
\]
The previously proved cross-witness square-flatness theorem states that badness of \(c\) forces \(\partial_hc_j\) to vanish at all \(L_{h,j}\). This proves (FC2). \(\square\)

**Corollary (uniform higher-derivative exclusion).** Under the same hypotheses, if for some nonempty \(R\subseteq S\) the iterated Boolean derivative \(\partial_R\partial_h c_j\) is identically one, then \(c\) has a monochromatic full antipodal geodesic. Indeed, if \(c\) were bad, (FC2) would force every derivative in nonempty directions \(R\subseteq S\) to vanish throughout each full \(S\)-subcube in its zero set, contrary to the stipulated uniform value.

**Corollary (acyclic external control).** Suppose additionally that \(\partial_hc_j\) depends only on the bits of \(S\). If it is nonzero at any input, then \(c\) is good: the cylinder (FC2) ranges over all \(u\in Q_S\), so under badness the derivative would be identically zero.

The theorem generalizes the earlier leaf-supported derivative exclusion to all terminal acyclic blocks, with arbitrary nonlinear dependence on other directions. It imposes all-dimensional flatness conditions on the overlap of cross-facet favorable paths, but it does not close unrestricted NORI1 or all four-hub configurations.



#### Maximal influence congestion and unbounded exchange plateaus

For every even \(n=2m\ge6\), color direction-\(i\) cube edges by
\[
c_i(x)=\sum_{j\ne i}x_j\pmod 2. \tag{EP1}
\]
This coloring is well-defined because \(c_i\) ignores \(x_i\), and it is antipodally odd because \(n-1\) is odd. By an *adjacent-direction exchange* we mean swapping successive dimensions of a rooted full antipodal geodesic while preserving its root. A *Petrie rotation* shifts the starting point along the cycle consisting of a geodesic followed by its antipodal image.

**Theorem (maximal-congestion strict-descent obstruction).** In (EP1), every cube edge has influence multiplicity \(r(e)=n-1\). There is a rooted full antipodal geodesic \(P\) with color word
\[
\boxed{w(P)=0\,1^{n-2}\,0.}\tag{EP2}
\]
No adjacent-direction exchange or Petrie rotation strictly reduces its two color changes. Nevertheless a monochromatic full antipodal geodesic exists from the same root, and the minimum number of adjacent-direction exchanges between \(P\) and such a geodesic is \(m-1\).

*Proof.* Flipping bit \(j\) changes every function \(c_i\) with \(i\ne j\). Hence all cube edges have \(r(e)=n-1\); in the influence-congestion notation, \(U=0\) and \(R=n(n-2)2^{n-1}\).

Fix a dimension order \(\pi_0,\ldots,\pi_{n-1}\), indexed from zero, and root \(x\). Define \(T=\sum_i x_i\) and \(b_k=T+x_{\pi_k}\) in \(\mathbb F_2\). The color of step \(k\) is
\[
w_k=b_k+k\pmod2. \tag{EP3}
\]
Conversely every word \(w\) is obtained by putting \(b_k=w_k+k\), \(T=\sum_kb_k\), and \(x_{\pi_k}=b_k+T\): as \(n\) is even, \(\sum_i x_i=T\). Thus a root giving (EP2) exists.

An adjacent exchange at positions \(k,k+1\) replaces the two color bits by
\[
\boxed{(w_k,w_{k+1})\longmapsto(1-w_{k+1},1-w_k).}\tag{EP4}
\]
Pairs \(01,10\) remain unchanged; \(11\) becomes \(00\) and \(00\) becomes \(11\). In (EP2) the only equal adjacent pair is \(11\), within a central block of at least four ones. Replacing any such pair by \(00\) leaves at least two changes, while each boundary exchange preserves the word. Hence no adjacent exchange improves \(P\).

The antipodal Petrie cycle has color word \(w\bar w\). Its length-\(n\) window starting after \(1\le k<n\) steps reads \(w_k\cdots w_{n-1}\bar w_0\cdots\bar w_{k-1}\). Because \(w_0=w_{n-1}=0\), it has \(3-\mathbf1_{\{w_{k-1}\ne w_k\}}\), hence two or three, switches. The windows beginning at offsets \(0,n\) also have two. Thus no Petrie rotation improves \(P\).

Under adjacent exchanges, the binary entries \(b_k\), each attached to its direction, merely undergo adjacent transpositions. In (EP2) the one-positions of \(b\) are \(2,4,\ldots,2m-2,2m-1\). A constant-zero word requires one-positions \(1,3,\ldots,2m-1\); a constant-one word requires \(0,2,\ldots,2m-2\). For binary strings containing equally many ones, the minimum adjacent-transposition distance equals the sum of absolute differences between corresponding ordered one-positions. These distances are \(m-1\) and \(2m-1\), respectively. Repeatedly exchanging the first pair of ones remaining in the central block of (EP2) attains the former bound: the two-switch word remains two-switch until the final exchange makes it constant zero. \(\square\)

Consequently maximum simultaneous switching of direction-color functions does not imply an immediately improving square exchange, even allowing Petrie rotations. An exchange-based NORI1 proof must accommodate nondecreasing steps or use a global invariant detecting improving sequences whose length grows with dimension.


##### Nested prefix carriers are homotopically constant; top degrees remain movable

Use the notation of the preceding Subsection. For every ordered partition \(\mathcal P\) into at least two nonempty blocks, put
\[
K_{\mathcal P}=\{v\in W:\langle v,T_{A_j}\rangle>0
\text{ for each proper cumulative first-block union }A_j\},
\]
and
\[
\mathcal C_{\mathcal P}
=\{\Pi\in\widetilde{\mathrm{Gr}}_2(W):
\Pi\cap K_{\mathcal P}\ne\varnothing\}.
\]
A refinement \(\mathcal Q\) of \(\mathcal P\) yields inclusions \(K_{\mathcal Q}\subseteq K_{\mathcal P}\) and \(\mathcal C_{\mathcal Q}\subseteq\mathcal C_{\mathcal P}\).

**Theorem 1 (all refinement inclusions are homotopy equivalences).** For every refinement \(\mathcal Q\) of \(\mathcal P\), the inclusion
\[
\boxed{\mathcal C_{\mathcal Q}\hookrightarrow\mathcal C_{\mathcal P}}
\tag{1}
\]
is a homotopy equivalence, inducing multiplication by \(\pm1\) on \(\pi_{n-3}\cong\mathbb Z\).

*Proof.* Let \(B_{\mathcal R}=K_{\mathcal R}\cap S(W)\), for \(\mathcal R=\mathcal P,\mathcal Q\). Both are nonempty contractible spherical convex sets, and \(B_{\mathcal Q}\subseteq B_{\mathcal P}\). Define incidence spaces
\[
E_{\mathcal R}
=\{(\Pi,v):\Pi\in\mathcal C_{\mathcal R},
\ v\in B_{\mathcal R}\cap\Pi\}.
\]
Projection \(E_{\mathcal R}\to B_{\mathcal R}\) is the \(S^{n-3}\)-bundle of oriented orthogonal companions of \(v\). Fix any \(v_0\in B_{\mathcal Q}\), and identify its fiber with \(S(v_0^\perp)\). Since each base is contractible, inclusion of this fiber is a homotopy equivalence for both \(E_{\mathcal Q}\) and \(E_{\mathcal P}\). The inclusion \(E_{\mathcal Q}\hookrightarrow E_{\mathcal P}\) is the identity on that common fiber, so is also a homotopy equivalence.

The projection \(E_{\mathcal R}\to\mathcal C_{\mathcal R}\) is a homotopy equivalence by the feasible-plane selection and contractible-fiber proof in the preceding Subsection; these projections commute with the refinement inclusions. The two-out-of-three property therefore implies (1) is a homotopy equivalence. QED.

**Theorem 2 (degree transport within the positive-carrier system).** Let \(F\) be any reversal-equivariant positive-carrier filling of the \((n-3)\)-skeleton, as constructed previously, with \(n\ge4\). Fix a three-block cell
\[
D_{A|B|C},\qquad A,B,C\ne\varnothing.
\]
It lies in precisely the two top cells
\[
D_{A|(B\cup C)}\quad\text{and}\quad
D_{(A\cup B)|C}.
\]
One can modify \(F\) inside the relative interior of this three-block cell, leaving its entire boundary and all other lower-dimensional cells fixed, and preserving all positive carriers, so that the two adjacent integral top-cell obstruction degrees each change by \(+1\) or \(-1\). No other top-cell degree changes. The modification on the reversal partner cell is uniquely prescribed by odd equivariance.

*Proof.* The three-block cell is an \((n-3)\)-ball, whose carrier has \(\pi_{n-3}(\mathcal C_{A|B|C})\cong\mathbb Z\). Replace its interior filling, relative to its fixed boundary, by the connected sum with any representative of a generator supported on a small interior ball. This changes its relative homotopy class by one and remains inside its carrier. The boundary of each adjacent top cell includes this three-block facet once. Under its inclusion into either two-block carrier, the added homotopy class maps to a generator by Theorem 1, changing that top attaching degree by \(\pm1\). No other top cell is incident with this three-block cell. Transport the modification to its reversed partner to retain global equivariance. QED.

**Corollary 3 (no fixed distribution of top-degree parity).** The graph on reversal-orbits of two-block cells, joining two vertices whenever they share a three-block facet orbit, is connected. Consequently, the changes allowed by Theorem 2 span all even-sum changes of the modulo-two top-degree vector. In particular, carrier preservation alone cannot determine which two-block cells have odd obstruction degree: it can move the odd degrees between different top-cell orbits.

*Proof.* Two-block cells are indexed by bipartitions \(\{A,V\setminus A\}\). Refining one side or the other gives a three-block incidence, and inclusions of proper nonempty subsets connect the bipartitions; more explicitly any proper subset can be reduced to a singleton by successive deletion, and singleton bipartitions connect through two-element unions. Hence the incidence graph is connected. Each three-block modification toggles the parity at its two endpoints. In a connected graph, endpoint-toggle vectors of edges span the even-sum subspace over \(\mathbb F_2\). QED.

**Interpretation and limitation.** The nested cone carriers solve the problem of constructing compatible fillings through the entire lower skeleton, but their facewise inclusions retain the full top-dimensional homotopy group: no natural degree is lost when a cell is refined. Thus the higher obstruction is a universal characteristic-class obstruction rather than an invariant of the particular color words. A proof of either original conjecture requires a further **color-sensitive restriction on allowed fillings or top-cell degrees**; positivity, reversal symmetry, and the nested-carrier condition alone do not provide one.

##### Power-of-two equivariant degree criterion

**Theorem 1.** Let (D=P_a\times P_b), (a=2^r,b=2^s\ge2), with its blockwise regular action of (G=(\mathbb Z/2)^r\times(\mathbb Z/2)^s). Let (H=W_A\oplus W_B) be the corresponding zero-sum permutation representation. Every equivariant map (\partial D\to S(H)) has odd degree, hence cannot extend equivariantly over the ball.

*Proof.* Radial projection from the barycenter identifies (\partial D) equivariantly with (S(H)). For each regular elementary-abelian action, the centered permutation representation is the direct sum of every nontrivial one-dimensional real character, each once. Thus the mod-two equivariant Euler class of (H) is the product of all nonzero linear forms in the first (r) variables times the product of all nonzero linear forms in the last (s) variables, an element of (H^{a+b-2}(BG;\mathbb F_2)). Both products are nonzero polynomials, hence their product is nonzero. In the Serre spectral sequence of the Borel sphere bundle, the top fiber class transgresses to this Euler class. Any equivariant sphere self-map induces identity on base cohomology and multiplication by its degree modulo two on top fiber cohomology. Naturality of transgression forces its degree to be one modulo two. QED.

**Theorem 2 (contrast).** For (a=3,b=2), the full block permutation group (S_3\times S_2) admits an equivariant self-map of (\partial D\cong S^2) of degree minus two.

*Proof.* Identify (W_A) with the complex plane with the dihedral action generated by (z\mapsto\omega z), (\omega^3=1), and (z\mapsto\overline z). The second factor acts on (W_B=\mathbb R) by (t\mapsto-t). On the unit sphere in (\mathbb C\oplus\mathbb R), send ((z,t)) to ((\overline z^2/|z|,t)) for nonzero (z), and to ((0,t)) for zero (z). This continuous map commutes with both groups, preserves the sphere, and is the suspension of the degree minus two circle map (z\mapsto\overline z^2). QED.

**Application and limitation.** For a coloring whose vertex tensor labels and nonvanishing boundary interpolation are equivariant under blockwise regular 2-groups, top-cell parity is rigid under equivariant changes of lower-cell fillings. Neither unrestricted coloring oddness condition forces this block symmetry. The theorem isolates extra rigidity of symmetric top cells without resolving the global conjectures.

##### Twisted involution stabilizers and the dyadic separation

**Theorem 1 (common stabilizer criterion).** Let \(R\) be a free involution on a finite set \(X\), and let \(G\) act on \(X\) commuting with \(R\). Fix a character \(\chi:G\to\mathbb F_2\). There is a coloring \(c:X\to\mathbb F_2\) satisfying \(c(Rx)=c(x)+1\) and \(c(gx)=c(x)+\chi(g)\) if and only if
\[
gx=x\ \Longrightarrow\ \chi(g)=0,
\qquad gx=Rx\ \Longrightarrow\ \chi(g)=1
\tag{1}
\]
for all \(x,g\).

*Proof.* Necessity is immediate. For sufficiency, let \(G\times C_2\) act on \(X\), with the second factor acting by \(R\). The prescribed color-change character is \((g,\epsilon)\mapsto\chi(g)+\epsilon\). Conditions (1) state precisely that this character vanishes on every point stabilizer. Choose a representative of each group orbit and assign it color zero, then transport by the character. The stabilizer condition makes the coloring well-defined. QED.

The theorem applies to antipodal cube edges and to ordered distinct triples with reversal \(R(a,b,c)=(c,b,a)\), yielding the same abstract coloring criterion for both unrestricted systems.

**Theorem 2 (semiregular automorphism 2-groups of triple colorings).** For every reversal-odd coloring of ordered distinct triples on \(n\ge3\) vertices, each 2-subgroup \(P\) of its color-preserving automorphism group acts freely on the vertices. Consequently \(|P|\mid n\), and for odd \(n\) its full color-preserving automorphism group has odd order. Conversely, every free vertex action of a finite 2-group admits an invariant reversal-odd triple coloring.

*Proof.* If a nonidentity element \(g\in P\) fixes \(e\), write its order as \(2^k\), and select a cycle of length \(2^k\). Then \(h=g^{2^{k-1}}\) fixes \(e\) and exchanges two vertices \(a,c\) of that cycle. It sends \((a,e,c)\) to \((c,e,a)\), forbidden by (1) with \(\chi=0\). Thus all nonidentity group elements are fixed-point-free, and all group orbits have size \(|P|\). If the full automorphism group has even order on odd \(n\), Cauchy's theorem supplies a forbidden involution. Conversely, in a free action no nonidentity element fixes a triple or sends one to its reversal, since the latter would fix its middle vertex. Apply Theorem 1 with the zero character. QED.

**Theorem 3 (dyadic block actions separate the two original models).** Partition the symbols into \(A\sqcup B\), with \(|A|=2^r\), \(|B|=2^s\) and \(r,s\ge1\). Let \(G=E_r\times E_s\), each elementary-abelian factor acting regularly on its own block and trivially on the other.

(a) A reversal-odd ordered-triple coloring can transform uniformly by a character \(\chi:G\to\mathbb F_2\) only if \(r=s=1\). In that case such a coloring exists, with \(\chi\) equal to one on each factor generator. In particular a strictly \(G\)-invariant triple coloring never exists.

(b) A strictly \(G\)-invariant antipodally odd cube-edge coloring exists for every \(r,s\ge1\).

*Proof.* Every nonidentity \(t\in E_r\) exchanges \(a\) and \(a+t\) while fixing any \(e\in B\). Hence it sends \((a,e,a+t)\) to its reversal. Theorem 1 requires \(\chi(t)=1\) for every nonidentity \(t\). For \(r\ge2\) this contradicts additivity, since \(\chi(t+u)=\chi(t)+\chi(u)=0\) for distinct nonzero \(t,u\). The same argument applies to \(E_s\). For \(r=s=1\), take the character that is one on both generators; only individual factor generators can reverse a triple, and there are no nontrivial stabilizers of ordered triples. Theorem 1 then provides the coloring.

For (b), choose nonzero translations \(t_A\in E_r\), \(t_B\in E_s\) and define a fixed-point-free permutation \(\sigma\) on \(A\sqcup B\) by these translations. The abelian group \(G\) commutes with \(\sigma\). For a cube edge in direction \(i\), set
\[
\boxed{c(\{x,x\oplus e_i\})=x_{\sigma(i)}.}
\tag{2}
\]
It is well-defined since \(\sigma(i)\ne i\), it complements under \(x\mapsto\bar x\), and it is unchanged by the simultaneous action of \(G\) on directions and vertex entries. QED.

**Interpretation.** The nonzero equivariant Euler-class obstruction for dyadic permutahedral products is compatible with globally invariant cube colorings but incompatible with globally invariant reversal-odd boundary triple colorings. Even twisting every color by a group character fails for block sizes at least four. Thus a unified argument should keep the abstract stabilizer criterion, but cannot assume identical untwisted block symmetries in both models.

##### Stabilizer cycle criterion for cube edges and the balanced-layer geodesic

Let \(n\ge2\), let \(E_n\) be the set of undirected edges of the binary cube \(Q_n\), and let \(R\) complement both endpoints of an edge. The permutation group \(S_n\) acts on \(E_n\) by permuting directions and vertex entries, commuting with \(R\).

**Theorem 1 (antipodal-edge cycle criterion).** For a permutation \(g\in S_n\), there exists an edge \(e\in E_n\) with \(ge=Re\) if and only if \(g\) has precisely one fixed symbol \(i\), and every other cycle of \(g\) has even length. Furthermore \(g\) fixes some edge of \(Q_n\) if and only if it fixes at least one direction.

*Proof.* Represent an undirected edge by its direction \(i\) and a bit assignment to the \(n-1\) other directions. If \(ge=Re\), the direction is unchanged, so \(g(i)=i\). On every other direction \(j\), the bit assignment must satisfy
\[
x_{g^{-1}j}=1-x_j.
\tag{1}
\]
Going once around a cycle of \(g\) shows its length must be even. Conversely, on every even cycle, alternating zeros and ones satisfies (1), yielding such an edge. Every other fixed direction would be an odd length-one cycle, so \(i\) is unique. For the second assertion, an edge fixed by \(g\) must have its direction fixed; conversely the edge from \(0^n\) in any fixed direction is fixed. QED.

**Theorem 2 (complete permutation-equivariance test).** Let \(G\le S_n\) and \(\chi:G\to\mathbb F_2\) be a homomorphism. There is an antipodally odd edge coloring \(c:E_n\to\mathbb F_2\) satisfying \(c(ge)=c(e)+\chi(g)\) for all \(g,e\) if and only if:
(i) \(\chi(g)=0\) for every \(g\in G\) fixing any direction; and
(ii) \(G\) contains no permutation having a unique fixed direction and only even cycles otherwise.

*Proof.* By Theorem 1, condition (i) is precisely the fixed-edge constraint of the universal twisted-color stabilizer criterion in the preceding Subsection. Condition (ii) rules out a permutation carrying some edge to its antipodal edge, because (i) would force its twist to be zero while reversal oddness would force its twist to be one. The universal criterion gives sufficiency as well. QED.

**Corollary 3 (fully symmetric cube colorings).** A color-preserving antipodally odd cube-edge coloring invariant under all direction permutations \(S_n\) exists if and only if \(n\) is even.

*Proof.* When \(n\) is even, the set of \(n-1\) directions outside a fixed direction has odd cardinality; it cannot be partitioned into exclusively even cycles. Theorem 2 applies to \(G=S_n,\chi=0\). Explicitly, for an edge in direction \(i\), let \(k\) be the number of ones on the other \(n-1\) directions and put \(c(e)=h(k)\), where the arbitrary function \(h:\{0,\ldots,n-1\}\to\mathbb F_2\) satisfies \(h(n-1-k)=1-h(k)\). Such an \(h\) exists because \(n-1\) is odd. If \(n\) is odd, a permutation fixing one direction and exchanging all other directions in pairs violates Theorem 2. QED.

**Theorem 4 (dimension-simple monochromatic geodesic in every fully symmetric odd coloring).** Suppose \(n=2m\) and \(c\) is any \(S_n\)-invariant antipodally odd cube-edge coloring. Then it admits an antipodal geodesic using every direction once whose \(n\) edges all have the same color.

*Proof.* By symmetry the color of an edge joining vertices of Hamming weights \(k\) and \(k+1\) depends only on \(k\); call it \(h(k)\). Choose a root vertex with precisely \(m\) ones. Alternate toggling a previously unused one-direction and a previously unused zero-direction, until all \(2m\) directions have been used. Each pair of steps changes the Hamming weight from \(m\) to \(m-1\) and back to \(m\), so *every edge lies between the same two middle weight levels*. Every edge therefore has color \(h(m-1)\). All directions are distinct, and the last vertex is the complement of the root. QED.

**Comparison with reversal-odd boundary triples.** Every transposition of two symbols fixes a third when \(n\ge3\) and consequently sends a suitable triple to its reversal, so no \(S_n\)-invariant reversal-odd triple coloring exists. In even dimension the cube permits the full \(S_n\) symmetry and its full-dimensional monochromatic geodesic follows from the middle-layer alternation. Thus the stabilizer condition supplies a sharp common framework for the two coloring classes while exposing a structural difference between their permissible symmetries.

##### Integrability of switch cochains: local completeness for cubes and a large overlap-graph gap

A legal odd binary coloring on an elementary-state double cover produces a switch one-cochain on the quotient incidence graph in the canonical covering cohomology class. We compare the completeness of the most natural local cycle equations in the two original problems.

**Theorem 1 (a local cycle presentation of legal cube switches).** Let \(n\ge3\), and let \(H_n=L(Q_n)/R\), where vertices of \(L(Q_n)\) are undirected cube edges, its edges are incidences of two cube edges at a common cube vertex, and \(R\) is antipodal complementation. Let \(\eta\in C^1(H_n;\mathbb F_2)\). Then \(\eta\) is the quotient switch assignment of an antipodally odd cube-edge coloring if and only if:
1. Its sum around every projected incidence triangle (three cube edges sharing a cube vertex) is zero.
2. Its sum around every projected four-cycle corresponding to the four successive cube edges of an elementary cubical square is zero.
3. Its sum around one chosen closed walk in \(H_n\) with nontrivial covering monodromy is one.

Every such \(\eta\) determines its coloring uniquely up to global complementation.

*Proof.* Form a two-dimensional cell complex \(K_n\) from \(L(Q_n)\) by filling the incidence triangles and the four-edge loops associated with all elementary squares in \(Q_n\). Filling the entire clique simplex of the \(n\) cube edges incident to each vertex does not affect fundamental groups beyond its two-skeleton. Because \(Q_n\) has no triangles, each clique of \(L(Q_n)\) lies in one such incidence simplex. These simplices form a good cover: an intersection of two distinct ones is one vertex precisely when the underlying cube vertices are adjacent; triple intersections are empty. By the nerve theorem their union is homotopy equivalent to the one-skeleton of \(Q_n\). Under this homotopy equivalence, the four-edge loop from an elementary square maps to the boundary of that cubical square. Attaching its two-cell for every square therefore yields a space with the same fundamental group as the cubical two-skeleton of \(Q_n\). This latter complex is simply connected, as it is the two-skeleton of a contractible \(n\)-cube. Thus \(\pi_1(K_n)=0\).

The antipodal involution acts freely on \(K_n\) for \(n\ge3\): it pairs distinct star simplices and pairs opposite square two-cells, with no pointwise or setwise fixed cell. Hence \(\pi_1(K_n/R)\cong C_2\), and
\[
H^1(K_n/R;\mathbb F_2)\cong\mathbb F_2
\]
is generated by the covering class \(\alpha\). Conditions (1) and (2) assert precisely that \(\eta\) extends to a cellular one-cocycle on \(K_n/R\). Condition (3) forces its cohomology class to be \(\alpha\). Pulling \(\eta\) to \(L(Q_n)\) therefore gives a coboundary; integrating it produces a coloring of elementary cube edges whose antipodal difference is one. Since the line graph is connected, the coloring is unique modulo global complement. Necessity is the telescoping identity for differences of endpoint colors along closed walks. QED.

**Theorem 2 (canonical quadrilateral relations are far from complete for boundary tournaments).** Let \(n\ge5\), and let \(O_n\) be the connected graph of injective ordered triples, with an undirected edge between \(abc\) and \(bcd\) whenever \(a,b,c,d\) are distinct. Reversal \(R(abc)=cba\) is free on vertices and edges. Write \(H_n^{\mathrm{tri}}=O_n/R\), and put \(N=n(n-1)(n-2)\).

(a) The quotient graph has
\[
|V(H_n^{\mathrm{tri}})|=N/2,\qquad
|E(H_n^{\mathrm{tri}})|=N(n-3)/2.
\tag{1}
\]
The directed sliding quadrilaterals
\[
abc\longrightarrow bcd\longrightarrow cda
\longrightarrow dab\longrightarrow abc
\tag{2}
\]
form \(N(n-3)/8\) distinct quotient cycles. Their edge supports are pairwise disjoint, hence their boundary chains are independent over \(\mathbb F_2\).

(b) Attach a two-cell along each of these canonical quadrilaterals, obtaining the quotient complex \(X_n\). Its first mod-two Betti number is
\[
\boxed{b_1(X_n)=1+\frac{N(3n-13)}8.}
\tag{3}
\]
The covering class \(\alpha=w_1(O_n\to H_n^{\mathrm{tri}})\) is a nonzero element of \(H^1(X_n;\mathbb F_2)\). Thus the quadrilateral parity equations, supplemented by the required odd monodromy around one essential quotient walk, leave
\[
\boxed{\frac{n(n-1)(n-2)(3n-13)}8}
\tag{4}
\]
additional independent linear conditions before a quotient switch cochain is known to arise from a reversal-odd coloring of ordered triples.

*Proof.* There are \(N\) injective triples, and each has \(n-3\) allowable forward successors. Every edge has a unique forward orientation: if both \(abc\to bcd\) and \(bcd\to abc\) were possible, injectivity would fail. Consequently the original graph has \(N(n-3)\) edges. Its reversal has no fixed vertex or edge, proving (1).

Any forward arc \(abc\to bcd\) belongs to precisely one directed quadrilateral of form (2): in any directed closed walk of length four, the four-symbol sliding sequence is periodic, forcing its remaining symbols to be \(a,b,c\). Thus the directed quadrilaterals partition the original edge set. Reversal pairs distinct such quadrilaterals, and does not identify vertices within one, because the reverse of any three-symbol segment is not a cyclic shift of that segment in a cyclic word with four distinct symbols. They consequently partition the quotient edges as well. Dividing its edge count by four gives \(N(n-3)/8\) independent two-cell boundaries.

The graph \(O_n\) is connected for \(n\ge5\) (elementary overlapping shifts implement replacements and adjacent exchanges of any injective triple), so the quotient is connected. The cycle rank of its one-skeleton is \(E-V+1\). Independent two-cell boundaries reduce the first Betti number by their count, yielding
\[
E-V+1-\frac{N(n-3)}8
=\frac{N(n-3)}2-\frac N2+1-\frac{N(n-3)}8
=1+\frac{N(3n-13)}8.
\]
Every quadrilateral (2) lifts to a closed cycle upstairs, so \(\alpha\) evaluates zero on its boundary and extends to a one-cocycle on \(X_n\). As the double cover is connected, \(\alpha\ne0\).

An arbitrary quotient one-cochain satisfying all independent quadrilateral parity equations has \(E-N(n-3)/8\) free binary parameters. Requiring its value to be one on one covering-odd walk imposes another independent linear condition. By the shared odd-cover integrability theorem, however, realizable switch cochains are precisely the cochains in cohomology class \(\alpha\), an affine space of dimension \(V-1\). Their codimension inside the quadrilateral-plus-one-period solution space is therefore
\[
\left(E-\frac{N(n-3)}8-1\right)-(V-1)
=\frac{N(3n-13)}8.
\]
This proves (4). QED.

**Numerical instances.** The additional codimensions in (4) are \(15\) at \(n=5\), \(75\) at \(n=6\), and \(210\) at \(n=7\).

**Proof-search consequence.** In the cube model, incidence triangles and geometric squares already kill every closed-cover cycle, leaving only the one antipodal monodromy bit. In the ordinary boundary-tournament model, canonical four-step sliding cycles are edge-disjoint and leave a large homology space of additional coherence relations. Thus a proposed common local deletion, smoothing, or integration rule based only on the shortest obvious four-step turn cycles cannot characterize unrestricted tournament switch sets. The distinction is not an obstruction to a stronger common theorem: both systems remain pullbacks of their respective odd covering classes, but their presentations require different amounts of nonlocal cycle data.

#### A dimension-independent bounded-cycle presentation of tournament switches

The preceding gap theorem counted only the canonical *directed* quadrilaterals. Surprisingly, allowing all overlap cycles up to a fixed length gives a complete integration criterion. We prove the uniform bound nine.

**Lemma 4 (cycle structure of crown graphs).** Let \(C_m=K_{m,m}\setminus\{L_iR_i:1\le i\le m\}\), with \(m\ge3\). Its two vertices \(L_i,R_i\) have distance three, two distinct vertices on the same side have distance two, and distinct opposite-side vertices with different indices are adjacent. For \(m\ge4\), its binary cycle space is generated by four-cycles. For \(m=3\), \(C_3\) itself is a six-cycle.

*Proof.* The distance assertions follow by choosing one or two additional indices, and \(C_3\cong C_6\). At \(m=4\), \(C_4\) is the three-dimensional cube graph, whose cycle space is generated by its square faces. For larger \(m\), adjoining \(L_m,R_m\) to \(C_{m-1}\) adds two vertices and \(2(m-1)\) edges, increasing the cycle rank by \(2m-4\). Fix one old right vertex \(R_j\). For every other old right vertex \(R_k\), the two new edges \(L_mR_j,L_mR_k\) participate in a square through an old left vertex whose index differs from \(j,k\). These \(m-2\) squares give independent new-edge differences at \(L_m\). The analogous construction at \(R_m\) gives another \(m-2\) independent differences. They span the rank increment and complete the induction. QED.

**Lemma 5 (directed triangles generate the bidirected complete graph).** Consider the graph with vertex set \([n]\) and one distinct undirected graph edge for each ordered pair \(a\to b\) with \(a\ne b\), so that \(a\to b\) and \(b\to a\) are parallel edges. For \(n\ge5\), its binary cycle space is generated by directed triangles
\[
a\to b\to c\to a,\qquad a,b,c\ \text{distinct}.
\tag{10}
\]

*Proof.* Let \(\lambda_{ab}\in\mathbb F_2\) annihilate every directed triangle, so that \(\lambda_{ab}+\lambda_{bc}+\lambda_{ca}=0\). Fix a root symbol \(r\). For \(a,b\ne r\), the triangle \(r,a,b\) gives \(\lambda_{ab}=\lambda_{ra}+\lambda_{br}\). Put \(s_a=\lambda_{ra}+\lambda_{ar}\). Every triangle on \(a,b,c\ne r\) yields \(s_a+s_b+s_c=0\). Since there are at least four symbols besides \(r\), comparison of triples implies that all \(s_a\) are equal, and then any one triple forces their common value to be zero. Thus \(\lambda_{ra}=\lambda_{ar}\) and \(\lambda_{ab}=u_a+u_b\), with \(u_r=0,u_a=\lambda_{ra}\). This is a cut cochain. The annihilator of the directed triangles is therefore precisely the cut space, so their span is the full cycle space. QED.

**Theorem 6 (nine-step generation of the triple-overlap cycle space).** For every \(n\ge5\), the binary cycle space of \(O_n\) is generated by closed walks of length at most **nine**. Consequently it is generated by simple cycles of length at most nine.

*Proof.* For each ordered pair \(bc\), let \(B_{bc}\) be the graph whose left vertices are the triples \(abc\), whose right vertices are \(bcd\), and whose edges are precisely the legal overlaps \(abc\sim bcd\). The external labels \(a,d\) range over the \(m=n-2\) symbols other than \(b,c\), with \(a\ne d\). Thus \(B_{bc}\cong C_m\), the crown graph of Lemma 4. These crowns partition \(E(O_n)\), and each state \(abc\) lies in precisely two crowns, \(B_{ab}\) and \(B_{bc}\).

Split every triple state \(abc\) into its two incidences with those crowns and join them by a bridge edge, whose contraction recovers \(O_n\). Contracting a spanning tree in each crown produces a graph with one vertex per ordered pair \(ab\), one connecting edge per ordered triple \(abc\) joining \(ab\) and \(bc\), and additional loops spanning the cycle spaces of the crowns. Hence \(H_1(O_n;\mathbb F_2)\) is generated by (i) cycles within the \(B_{bc}\), and (ii) lifts of cycles in the **ordered-pair overlap graph** \(T_n\), whose vertices are ordered pairs and whose edges are legal shifts \(ab\sim bc\). The cycles of (i) have length at most six by Lemma 4.

We similarly decompose \(T_n\) into crowns \(C_b\) indexed by a single middle symbol \(b\). Their left vertices are \(ab\), their right vertices are \(bc\), with \(a,c\ne b\), \(a\ne c\). Thus \(C_b\cong C_{n-1}\). Each ordered pair \(ab\) lies in the two crowns \(C_a,C_b\). Splitting and contracting spanning trees now leaves the **bidirected complete graph** of Lemma 5, with one connecting edge \(a\to b\) for each ordered pair \(ab\), together with cycles inside the \(C_b\). By Lemmas 4 and 5, \(H_1(T_n;\mathbb F_2)\) is generated by (ii-a) alternating squares in the crowns \(C_b\), and (ii-b) directed triangles
\[
(ab)\sim(bc)\sim(ca)\sim(ab).
\tag{11}
\]

Finally lift these \(T_n\)-cycles back into \(O_n\). At each ordered-pair state \(ab\), two incident \(T_n\)-edges correspond to two triple states in the crown \(B_{ab}\). For an alternating square in \(C_b\), the two triple states belong to the *same* bipartition class of \(B_{ab}\), and are connected by a two-edge path, by Lemma 4. Thus a square lifts to a closed walk of length \(4\cdot2=8\). For a directed triangle (11), the two states at \(ab\) are \(cab\) and \(abc\): they are opposite-side vertices of \(B_{ab}\) with the *same* external label \(c\). Lemma 4 joins them by a three-edge path. Thus a directed triangle lifts to a closed walk of length \(3\cdot3=9\). These lifts together with the internal crown cycles generate \(H_1(O_n;\mathbb F_2)\). Every closed walk of length at most nine decomposes into simple cycles of no greater length. QED.

**Corollary 7 (bounded-local integrability, both unrestricted problems).** Let \(n\ge5\) and \(H_n^{\mathrm{tri}}=O_n/R\). A binary cochain \(\eta\) on its edges comes from a reversal-odd coloring of ordered triples if and only if:
1. \(\eta\) sums to zero on every quotient closed walk of length at most nine whose lift to \(O_n\) is closed.
2. \(\eta\) sums to one on the following explicit six-step quotient loop, using any five distinct symbols \(a,b,c,d,e\):
\[
abc\sim bcd\sim cde\sim deb\sim ade\sim bad\sim cba.
\tag{12}
\]
The last vertex is the reversal of the first, so the projected loop has nontrivial covering monodromy.

For the cube, the corresponding bounded-local test is already complete using projected incidence triangles, elementary square cycles, and one covering-odd loop, by Theorem 1.

*Proof.* By Theorem 6, projections of closed walks of length at most nine generate the image of \(H_1(O_n;\mathbb F_2)\) in \(H_1(H_n^{\mathrm{tri}};\mathbb F_2)\). This image is the kernel of evaluation against the connected double-cover class \(\alpha\): every trivial-monodromy loop lifts closed, and any binary cycle of zero total monodromy is a sum of such loops. The walk (12) is legal at every step because the five symbols are distinct, and it connects a triple to its reversal; its projection evaluates to one under \(\alpha\). Thus the two conditions specify precisely the cohomology class \(\alpha\), which integrates to a reversal-odd triple coloring, unique modulo complementation, by the shared covering-class theorem. QED.

**Interpretation and remaining work.** The large quadrilateral-only gap in Theorem 2 does not entail that the tournament model needs relations of unbounded length. Its full switch-integrability condition admits a dimension-independent nine-step cycle presentation. This brings the two unrestricted models substantially closer: each has a bounded-local presentation of legal switch cochains, although the boundary tournament needs richer local motifs than the cubical triangle-square model. The theorem does not guarantee a complete path with few switches; it supplies the correct class of admissible local switch modifications for a common criticality argument.## Sharp four- and five-cycle generation

Let \(T_n\) be the ordered-pair overlap graph from the previous proof. For distinct \(x_1,\ldots,x_k\), write \(C(x_1,\ldots,x_k)\) for the directed cycle through the ordered pairs \((x_1,x_2),(x_2,x_3),\ldots,(x_k,x_1)\).

**Lemma 8 (four and five steps generate the pair graph).** For \(n\ge5\), the cycle space of \(T_n\) is generated by its directed quadrilaterals and pentagons.

*Proof.* The crown decomposition in Theorem 6 reduces its cycle space to directed triangles and alternating crown squares. Both are generated by directed quadrilaterals and pentagons using five symbols. Writing all chains over \(\mathbb F_2\), direct edge cancellation gives
\[
\begin{aligned}
C(0,1,2)={}&C(0,1,3,4)+C(0,3,4,2)+C(1,2,3,4)\\
&+C(0,1,2,3,4)+C(0,1,3,4,2)+C(0,3,4,1,2).
\end{aligned}
\tag{13}
\]
For the alternating square \(Q\) with ordered-pair vertices \((0,1),(1,2),(3,1),(1,4)\), one likewise has
\[
\begin{aligned}
Q={}&C(0,1,4,3)+C(0,2,1,4)+C(0,2,3,1)\\
&+C(0,2,4,3)+C(1,2,4,3)\\
&+C(0,1,2,4,3)+C(0,2,1,4,3)\\
&+C(0,2,3,1,4)+C(0,2,4,3,1).
\end{aligned}
\tag{14}
\]
In each displayed identity, a directed overlap edge occurs oddly on the right-hand side if and only if it belongs to the left-hand cycle. Every directed triangle is a symbol relabeling of \(C(0,1,2)\), and every alternating square is a relabeling of \(Q\), since its four external symbols and central symbol are distinct. Thus (13)-(14) and Theorem 6 give the required generation. QED.

**Theorem 9 (four- and five-cycle generation upstairs).** For \(n\ge6\), the binary cycle space of the triple-overlap graph \(O_n\) is generated by three families: alternating squares in its local crowns \(B_{bc}\); directed sliding quadrilaterals \(abc\sim bcd\sim cda\sim dab\sim abc\); and directed sliding pentagons \(abc\sim bcd\sim cde\sim dea\sim eab\sim abc\), with distinct symbols in each cyclic word. Hence all cycles are sums of cycles of lengths four and five.

For \(n=5\), these same families plus the single six-cycle of each \(B_{bc}\cong C_6\) generate the cycle space.

*Proof.* By Theorem 6, the original overlap graph is a graph of local crowns \(B_{bc}\cong K_{n-2,n-2}\) minus the matching, with underlying ordered-pair overlap graph \(T_n\). The local crowns have their cycles generated by squares when \(n\ge6\), and by one hexagon apiece when \(n=5\), by Lemma 4.

Lemma 8 says that the remaining cycle space of \(T_n\) is generated by directed four- and five-cycles. Such a directed cycle with distinct symbols \(x_1,\ldots,x_k\), \(k=4\) or \(5\), lifts from ordered pairs \((x_i,x_{i+1})\) to triple states \((x_i,x_{i+1},x_{i+2})\). At each ordered-pair state the incoming and outgoing triple states lie in opposite classes of its local crown, with external labels \(x_{i-1}\) and \(x_{i+2}\). These labels differ because the cyclic word has length at least four and all symbols are distinct. The two states are therefore directly adjacent in the crown. Thus the lifted cycle has the same length \(k\), with no detours. Such lifts are precisely the directed sliding quadrilaterals and pentagons displayed in the theorem. They generate the remaining cycle space, completing the proof. QED.

**Corollary 10 (uniform six-step switch integration).** For every \(n\ge6\), a binary edge cochain \(\eta\) on \(O_n/R\) comes from an unrestricted reversal-odd triple coloring if and only if it has even period on every projected alternating crown square, directed sliding quadrilateral, and directed sliding pentagon, and odd period on the explicit covering-odd six-step quotient walk (12). At \(n=5\), require in addition even period on the projected hexagon in every local crown.

*Proof.* Theorem 9 generates the cover graph cycle space by the listed motifs. Their quotient images span precisely the kernel of the covering monodromy functional on the quotient graph cycle space, and (12) supplies one complementary odd-monodromy loop. These periods characterize the canonical covering cohomology class. The common odd-cover integration theorem reconstructs the coloring uniquely up to global complementation. QED.

**Research consequence.** Although canonical directed quadrilateral equations alone leave the large deficit quantified in Theorem 2, adding alternating crown squares and directed pentagons fills that deficit for every \(n\ge6\). The complete admissibility conditions for tournament switch cochains therefore have a dimension-independent, bounded-width local presentation, much like the cube triangle-square presentation. These explicit cycle motifs are the natural constraints to preserve in any legal switch-deletion or criticality induction; the bounded integration theorem by itself does not imply a Hamilton ordering with at most one switch.

### Hereditary reversal-cover switch sets and deletion-critical paths

Let \(G\to H=G/\tau\) be a two-sheeted graph cover with free involution and class \(\alpha\in H^1(H;\mathbb F_2)\). A binary state coloring \(b\) is reversal-odd if \(b(\tau v)=b(v)+1\). Its switch bit on edge \(vw\) is \(b(v)+b(w)\); the quotient switch cochains are precisely the affine cut coset \(\alpha+B^1(H;\mathbb F_2)\), as proved in the preceding local-cycle-integration subsection.

The two intended covers are (i) the line graph \(L(Q_n)\) of undirected cube edges under antipodality and (ii) the overlap graph of injective ordered triples under reversal. Restrict complete paths respectively to dimension-simple antipodal cube geodesics and Hamilton tight triple paths. Put \(\ell=[\mathbf1_{E(H)}]\), the graph-length parity class, and \(\beta=\alpha+\ell\). Define the realizable support family \(\mathfrak A_\alpha=\{\operatorname{supp}s:[s]=\alpha\}\) and its deletion closure
\[
\boxed{\mathfrak H_\alpha=\{D\subseteq S:S\in\mathfrak A_\alpha\}.}
\tag{1}
\]

**Theorem 1 (intrinsic hereditary characterization).** For every \(D\subseteq E(H)\),
\[
\boxed{D\in\mathfrak H_\alpha\iff \beta|_{H[D]}=0
\iff \forall C\subseteq H[D]\text{ cycles},\
|C|\equiv\langle\alpha,[C]\rangle\pmod2.}
\tag{2}
\]
This also means that on \(H[D]\), the reversal double cover is isomorphic to the canonical length-parity bipartite double cover.

*Proof.* Fix a representative \(s_0\) of \(\alpha\). A legal switch cochain equal to one on D has the form \(s_0+\delta f\), requiring \(\delta f(e)=1+s_0(e)\) for every \(e\in D\). These prescribed edge differences admit a vertex potential f if and only if their sum on each cycle of \(H[D]\) vanishes. That sum is \(|C|+\langle\alpha,[C]\rangle\), proving all equivalences. \(\square\)

**Theorem 2 (deletion closure preserves the path conjecture).** Given a family \(\mathscr P\) of admissible complete paths and an integer \(t\ge0\), the condition
\[
\forall S\in\mathfrak A_\alpha\ \exists P\in\mathscr P:
|S\cap E(P)|\le t
\]
is equivalent to
\[
\boxed{\forall D\in\mathfrak H_\alpha\ \exists P\in\mathscr P:
|D\cap E(P)|\le t.}
\tag{3}
\]
At \(t=1\), this is the boundary 3-tournament one-switch conjecture. For cubes it is equivalent to NORI1 by the established antipodal root-rotation lemma.

*Proof.* By (1), each hereditary set D is contained in a realizable S. Any path with at most t hits of S also has at most t hits of D. Conversely every realizable S is itself hereditary. The cube equivalence uses the odd total switch parity on a covering-odd rainbow projective cycle: a one-switch geodesic's projective closure has only one switch, which can be omitted by choosing another starting point. \(\square\)

**Theorem 3 (two-switch criticality).** If (3) at \(t=1\) fails and D is an inclusion-minimal hereditary counterexample, then
\[
\boxed{\forall e\in D\quad\exists P_e\in\mathscr P:
e\in E(P_e),\quad |D\cap E(P_e)|=2.}
\tag{4}
\]

*Proof.* Deleting e preserves the hereditary constraint and permits a complete path with at most one remaining hit. The original D hits every complete path at least twice. Thus the selected path uses e, with total count two. \(\square\)

**Proposition 4 (sharp size of legal coloring changes).** For \(n\ge3\), two distinct legal antipodally odd cube-edge switch sets differ on at least \(2(n-1)\) antipodal unoriented-turn orbits. For \(n\ge5\), the corresponding bound for reversal-odd ordered triple colorings is \(2(n-3)\) reversal-turn orbits. Both are sharp.

*Proof.* A legal change is a graph cut by the cohomology-class characterization. The relevant quotient incidence graphs are simple and vertex-transitive, with regular degrees \(2(n-1)\) and \(2(n-3)\). By Mader's edge-connectivity theorem a nonempty cut has size at least its degree. Recoloring one deck-paired state vertex produces a star cut, attaining the lower bound. For the alternate oriented-cube-arc state convention, one undirected turn has two directed traversals, and the cube bound doubles to \(4(n-1)\) directed-turn orbits. \(\square\)

**Cycle restrictions.** A triangle formed by three cube edges incident to one vertex has trivial cover monodromy and odd length, so it cannot lie entirely in a hereditary switch set. The same holds for a closed-lift tight pentagon of ordered triples. Averaging the latter condition over cyclic five-tuples shows that at least one fifth of ordered distinct quadruples have equal colors on overlapping ordered triples, and hence at any fixed tight-switch position at least \(n!/5\) Hamilton orders avoid that switch.

These results supply a signed-graph deletion-stable alternative to working directly in the nonhereditary affine coset of odd switch colorings. The hereditary family is not asserted to be a matroid independence system. Excluding its two-switch-critical configurations remains open.

Reference: Mader's edge-connectivity theorem for connected vertex-transitive graphs, as discussed in M. DeVos, *Sumsets and Connectivity of Symmetric Graphs*, Theorem 10.2.

#### Uniform Hamilton incidence and a hereditary tournament density barrier

The same double-counting principle used for rainbow projective cube cycles applies to the second original geometry, now with Hamilton permutations rather than rainbow cycles.

Let \(n\ge5\). Let \(H_n^\triangle=O_n/R\) be the reversal quotient of the tight-overlap graph of distinct ordered triples, with \(R(abc)=cba\). Its quotient edge-orbits are reversal pairs of tight transitions \(abc\to bcd\). Put \(N=n(n-1)(n-2)/2\). Then
\[
\boxed{|V(H_n^\triangle)|=N,\qquad
|E(H_n^\triangle)|=N(n-3).}
\tag{8}
\]

**Theorem 5 (Hamilton turn incidence).** Every quotient turn edge of \(H_n^\triangle\) occurs in
\[
\boxed{2(n-3)!}
\tag{9}
\]
of the \(n!\) Hamilton vertex orderings, counted with their full ordered tight-transition lists. Consequently for every switch subset D,
\[
\boxed{
\mathbb E_{\pi\in S_n}|D\cap\operatorname{turns}(\pi)|
=(n-3)\frac{|D|}{|E(H_n^\triangle)|}.}
\tag{10}
\]

*Proof.* An oriented tight transition is specified by four distinct consecutive symbols \(a,b,c,d\). Treating this block as one item, the number of Hamilton orders containing it consecutively is \((n-3)!\). Its reversal \(d,c,b,a\) represents the same quotient transition and occurs in another \((n-3)!\) Hamilton orders. Summing gives (9). The n! Hamilton orderings each have n−3 tight transitions, so counting incidences yields (10). \(\square\)

**Theorem 6 (necessary density for hereditary one-switch counterexamples).** If \(D\in\mathfrak H_\alpha\) meets every Hamilton tight path in at least two marked turns, then
\[
\boxed{
|D|\ge n(n-1)(n-2),\qquad
\frac{|D|}{|E(H_n^\triangle)|}\ge\frac2{n-3}.}
\tag{11}
\]
Conversely, every hereditary D has
\[
\boxed{\frac{|D|}{|E(H_n^\triangle)|}\le\frac45}
\tag{12}
\]
because no such D may contain all five edges of a closed-lift tight pentagon.

*Proof.* By Theorem 5, the mean marked-turn count over Hamilton orders is \((n-3)|D|/|E|\). If each count is at least two, its mean is also at least two, proving (11). For (12), choose the family of closed-lift pentagons defined by cyclic lists of five distinct symbols. Each pentagon has trivial \(\alpha\)-monodromy but odd length; hence the hereditary cycle criterion forbids D from containing all five of its edges, bounding its D-hit count by four. The full symbol-permutation group is transitive on quotient turn edges and preserves this pentagon family, so every turn edge occurs in the same number of pentagons. Double-counting pentagon-edge incidences yields \(5|D|/|E|\le4\), proving (12). \(\square\)

For \(n=5\) the two inequalities are incompatible, recovering the one-switch Hamilton theorem in that dimension by a counting proof. For higher n the interval between the two bounds is nonempty, so a contradiction requires additional constraints on how selected turns distribute among intersecting Hamilton paths. The local pentagon restriction and global Hamilton incidence are the tournament analogues of the bipartite cube-corner bound and rainbow-cycle census, while the quantitative densities differ between the two geometries.

#### A relative integrability test for tight three-hit witnesses

A three-hit rainbow cycle of a hereditary switch set is not automatically realizable with only those three switches by a legal coloring. The obstruction is a component-overlap holonomy, parallel to the red-blue seam incidence obstruction in Article XIV.

Let \(H\) be either reversal-cover quotient comparison graph, fix a representative one-cochain a of its covering class \(\alpha\), and let \(D\in\mathfrak H_\alpha\). Write \(U=(V(H),D)\) for the spanning marked-edge subgraph. Let C be a covering-odd cycle with \(|D\cap C|\) odd (in particular, a three-hit rainbow projective cycle). Put \(F=U\cup C\). Define a prescribed switch cochain \(\rho\) on F by
\[
\boxed{\rho(e)=1\ (e\in D),\qquad
\rho(e)=0\ (e\in E(C)\setminus D).}
\tag{9}
\]

**Theorem 7 (tight-witness extension criterion).** There exists a legal reversal-odd state coloring whose switch set contains D and whose switches on C are precisely \(D\cap C\) if and only if
\[
\boxed{[\rho]=\alpha|_F\ \text{in }H^1(F;\mathbb F_2).}
\tag{10}
\]
The condition already holds on U and on C separately. Its only possible failure is on cycles of F mixing marked-subgraph paths with unmarked arcs of C.

*Proof.* A legal quotient switch cochain has the form \(a+\delta f\). To equal \(\rho\) on F requires \(\delta f=\rho+a\) there. A vertex potential f exists precisely when this edge cochain has zero sum on every cycle of F, proving (10); extend f arbitrarily to all vertices of H. On U, this condition is \((\alpha+\ell)|_U=0\), which is the defining hereditary property. On C its sum is \(\alpha(C)+|D\cap C|=1+1=0\), by the hypotheses. Only mixed cycles can obstruct. \(\square\)

**Theorem 8 (overlap-multigraph holonomy).** Choose potentials \(f_U\) solving \(\delta f_U=\rho+a\) on U, and \(f_C\) solving the same equation on C. Let \(\Gamma(U,C)\) be the bipartite multigraph whose vertices are the connected components of U and the one connected component C, and whose edges are the connected components of \(U\cap C\). Label such an edge I by the constant bit
\[
\boxed{k_I=f_U(v)+f_C(v)\quad(v\in I).}
\tag{11}
\]
Then the extension criterion (10) holds if and only if the sum of these labels around every cycle of \(\Gamma(U,C)\) is zero. In particular, it always holds if every connected component of U meets C in at most one connected component.

*Proof.* The difference \(f_U+f_C\) is constant on every connected overlap component because both potentials have the same edge differences there. The potentials may be changed by a constant independently on each component of U and on C. They can be made to agree on overlaps precisely when the edge labels \(k_I\) are a coboundary on the overlap multigraph. This is equivalent to vanishing around its graph cycles. If each U component has at most one connected intersection piece with C, the overlap graph is a star forest and has no cycles. \(\square\)

**Research consequence.** A three-hit witness promised by inclusion-criticality carries a *relative integrability obstruction* invisible to its total three-hit parity. A potential proof that modifies an odd coloring around such witnesses must either control the overlap holonomy or work directly with the hereditary switch sets, where deleting a marked turn is always legal. This is a necessary bookkeeping step for converting cycle-criticality into a coloring-sensitive exchange argument.

### Projective rainbow geodesic cycles and three-hit switch criticality

Let \(H_n=L(Q_n)/A\) be the antipodal quotient of the line graph of **undirected** cube edges, \(n\ge3\). Its vertices represent antipodal cube-edge pairs, labeled by their cube directions, and its edges represent antipodal orbits of unoriented two-edge turns. Let \(\alpha\in H^1(H_n;\mathbb F_2)\) classify the double cover. Call a simple cycle \(C\) a *rainbow projective n-cycle* when it has length n, uses every dimension label once, and obeys \(\langle\alpha,[C]\rangle=1\).

**Theorem 1 (rainbow projective lifting).** Every rainbow projective n-cycle lifts to a dimension-simple antipodal geodesic of \(Q_n\). Conversely, every such geodesic projects to a rainbow projective n-cycle.

*Proof.* Lift a quotient cycle to a sequence \(e_1,\ldots,e_n,Ae_1\) of undirected cube edges, with each successive pair incident. The final edge meets the antipodal image \(Ae_1\) because the cover monodromy of the quotient cycle is one. Since consecutive directions differ, their incidence point is unique. Write \(q_i=e_i\cap e_{i+1}\) for \(1\le i<n\), \(q_n=e_n\cap Ae_1\), and \(q_0=Aq_n\in e_1\). For each i, \(q_{i-1}\) and \(q_i\) are points on cube edge \(e_i\); they are either identical or joined by that edge. Thus the sequence \(q_0,\ldots,q_n\) is a possibly stationary walk in which each dimension can be used at most once. However, \(q_n=Aq_0\) differs from \(q_0\) in every dimension. It follows that none of the n steps is stationary and all n dimensions are traversed. The sequence is a full antipodal geodesic.

Conversely a full antipodal geodesic with edge sequence \(e_1,\ldots,e_n\) has \(e_n\) incident with \(Ae_1\) at its endpoint. Therefore its quotient edge sequence closes with monodromy one; the distinct direction labels give a simple rainbow n-cycle. \(\square\)

**Theorem 2 (cyclic root rotation).** Let D be any subset of turn-orbits of \(H_n\), and let \(C(P)\) denote the rainbow projective cycle associated with a full antipodal geodesic P. The minimum switch count over its antipodal root rotations is
\[
\boxed{
\min_{P'\text{ a root rotation of }P}
|D\cap\operatorname{turns}(P')|
=
\max(0,|D\cap E(C(P))|-1).}
\tag{1}
\]

*Proof.* Start P at any intermediate vertex, first following its suffix and then the antipodal image of its prefix. The resulting walk remains a full geodesic, and its quotient turn sequence opens the same rainbow cycle at the selected turn. Every cycle turn can be chosen as the omitted turn, so the least number of marked turns equals the cycle's number of marked edges minus one if this number is positive, and zero otherwise. \(\square\)

For odd cube-edge colorings the realizable switch set S represents \(\alpha\), so \(|S\cap C|\) is odd on any rainbow projective n-cycle. Therefore NORI1 is equivalent to the one-hit cycle assertion
\[
\boxed{
\forall S,\ [\mathbf1_S]=\alpha,\quad
\exists\text{ rainbow projective n-cycle }C:
|S\cap C|=1.}
\tag{2}
\]
Using the hereditary switch-set theorem of the preceding subsection, it is also equivalent to
\[
\boxed{
\forall D\subseteq E(H_n),\
(\alpha+\ell)|_{H_n[D]}=0
\quad\Longrightarrow\quad
\exists\text{ rainbow projective n-cycle }C:
|D\cap C|\le2.}
\tag{3}
\]
Here \(\ell\) is the cycle-length-parity class.

**Theorem 3 (three-hit critical witnesses).** If (3) fails, choose an inclusion-minimal hereditary counterexample D. Then every rainbow projective n-cycle has at least three D-edges, and for every marked edge \(e\in D\) there exists a rainbow projective n-cycle \(C_e\) such that
\[
\boxed{e\in C_e,\qquad |D\cap C_e|=3.}
\tag{4}
\]

*Proof.* The first claim is the counterexample property. Deletion preserves the hereditary class; minimality means that \(D\setminus\{e\}\) permits a rainbow projective cycle with at most two hits. If this cycle avoided e, it would contradict the counterexample property for D. Thus it includes e, and its D-hit count is three. \(\square\)

**Scope and implications.** An arbitrary line-graph walk may execute an illegal transition by touching the middle edge twice at its same endpoint. The lift in Theorem 1 rules this out by using antipodal displacement and the one-use-per-dimension budget. This supplies a closed-cycle characterization that retains cube geodesicity and dimension-simplicity.

The common hereditary switch-class framework is not asserted to be a matroid. In the cube quotient, a triangle of turns among three cube edges meeting at one vertex has odd length and trivial cover monodromy. Hence the signed-graph restriction forbids D from containing all three turns. A minimal counterexample must simultaneously satisfy these local exclusions and cover every marked turn by a three-hit rainbow cycle. Exploiting the exchange and overlap geometry of those cycles is the next proof objective. Neither the lift theorem nor criticality proves NORI1.

#### Uniform rainbow-cycle incidence and switch-density rigidity

The rainbow projective cycles admit a uniform incidence count that imposes numerical constraints on all hereditary switch obstructions.

**Theorem 4 (rainbow cycle census).** For every \(n\ge3\), the antipodal quotient line graph \(H_n=L(Q_n)/A\) has
\[
\boxed{|V(H_n)|=n\,2^{n-2},\qquad
|E(H_n)|=n(n-1)\,2^{n-2},}
\tag{5}
\]
and its number of undirected covering-odd, direction-rainbow n-cycles is
\[
\boxed{|\mathcal C_n|=2^{n-2}(n-1)!.}
\tag{6}
\]
Every turn-orbit of \(H_n\) lies on precisely
\[
\boxed{(n-2)!}
\tag{7}
\]
of these cycles.

*Proof.* The cube has \(n2^{n-1}\) undirected edges, paired by antipodality, giving the quotient vertex count. Each quotient state has \(2(n-1)\) turn neighbors, giving the edge count by the degree-sum rule.

There are \(2^n n!\) rooted directed full cube geodesics, one per root and direction permutation. By the lifting theorem, each undirected rainbow projective cycle yields \(2n\) distinct cyclically placed, oriented quotient edge sequences (n possible starts and two traversal directions). Every such quotient sequence has two antipodal lifts, giving \(4n\) rooted full geodesics per projective cycle. Dividing \(2^n n!\) by \(4n\) yields (6). The cube automorphism group acts transitively on turn-orbits and preserves the rainbow cycle family. Counting cycle-turn incidences gives the common turn multiplicity
\[
\frac{n|\mathcal C_n|}{|E(H_n)|}
=\frac{n2^{n-2}(n-1)!}{n(n-1)2^{n-2}}
=(n-2)!.
\]
\(\square\)

**Theorem 5 (critical switch-density lower bound).** If a hereditary set \(D\in\mathfrak H_\alpha\) meets *every* rainbow projective n-cycle in at least three turns, then
\[
\boxed{|D|\ge 3(n-1)2^{n-2}.}
\tag{8}
\]
This is three times the size of a quotient state's degree-one star multiplied by a factor of \(2^{n-3}\); more intrinsically, D occupies at least \(3/n\) of all quotient turn-orbits. The inequality applies in particular to every hypothetical deletion-minimal NORI1 counterexample D.

*Proof.* Count pairs \((e,C)\) with \(e\in D\cap C\). Each \(e\in D\) lies on \((n-2)!\) rainbow cycles by (7), while each rainbow cycle supplies at least three such pairs. Hence
\[
(n-2)!|D|\ge3|\mathcal C_n|
=3\,2^{n-2}(n-1)!,
\]
giving (8). \(\square\)

**Theorem 6 (local bipartite upper bound).** Every hereditary \(D\in\mathfrak H_\alpha\) satisfies
\[
\boxed{|D|\le 2^{n-1}\left\lfloor\frac{n^2}{4}\right\rfloor.}
\tag{9}
\]
Every legal odd switch set S obeys the same inequality. Equality requires that, at every antipodal pair of cube vertices, the marked turn graph on the n incident dimension edges be a complete bipartite graph with the two parts as balanced as possible.

*Proof.* At a cube vertex v, its n incident undirected edges form a clique \(K_n\) of turn edges in the line graph. The antipodal clique supplies the paired turn orbits. Every cycle in this clique lifts closed, so the covering class \(\alpha\) vanishes on it. The hereditary condition \((\alpha+\ell)|_{H_n[D]}=0\) thus requires the graph of marked turns within the clique to have only even cycles; in other words that local marked graph is bipartite. A bipartite graph on n vertices has at most \(\lfloor n^2/4\rfloor\) edges, with equality only for the balanced complete bipartite graph. Each quotient turn edge belongs to one antipodal pair of cube-vertex cliques, and there are \(2^{n-1}\) such pairs. Summing proves (9). \(\square\)

**Corollary 7 (all-dimensional mean switch bound and extremal rigidity).** For a uniformly random undirected rainbow projective cycle \(C\),
\[
\boxed{
\mathbb E|D\cap C|=\frac{|D|}{(n-1)2^{n-2}}
\le\frac{2\lfloor n^2/4\rfloor}{n-1}.}
\tag{10}
\]
Thus if \(2\lfloor n^2/4\rfloor<3(n-1)\), the hereditary two-hit conjecture follows without further work; this includes \(n=3,4\).

For \(n=5\), the upper bound in (9) and lower bound in (8) coincide. Any hypothetical hereditary counterexample must therefore be a **realizable** switch set S whose incident-edge colors split in sizes two and three at every cube vertex, and every rainbow projective 5-cycle must have three marked turns.

*Proof.* The expectation is the cycle-incidence census divided by the number of cycles. Apply (9). In dimension five, both inequalities read \(|D|=96\). The local inequality is therefore saturated at every cube-vertex orbit. Since D is a subset of some realizable legal switch set S and S satisfies the same local upper bound, S must coincide with D on every turn. Every rainbow 5-cycle has at least three hits, and the mean in (10) is three; therefore all such cycles have three hits. \(\square\)

**Research meaning.** The lower and upper density constraints force a substantial spread of marked turns in a critical hereditary obstruction. Local balance is stronger than merely forbidding fully marked incidence triangles: the entire marked graph at each cube vertex must be bipartite. The low-dimensional consequences are consistency checks, not a proposed approach of exhaustive small-order analysis. In higher dimensions, the still-open issue is to exploit the global compatibility of these local bipartitions with the forced three-hit cycles.

#### Uniform near-monochromatic antipodal geodesics from the rainbow census

The incidence identity above yields an all-dimensional bound for every legal antipodally odd cube-edge coloring without requiring a topological chain transfer.

Let \(c\) be a legal coloring, and let \(S=S(c)\subseteq E(H_n)\) be its quotient switch set. At a cube vertex v, let \(a(v)\) be the number of color-one edges among the n incident cube edges. Then the number of switched unoriented turns based at v is \(a(v)(n-a(v))\). Antipodality sends \(a(v)\) to \(n-a(v)\), so each antipodal vertex pair contributes this same number to \(|S|\).

**Theorem 8 (mean projective switches and a universal even-switch bound).** For every legal odd coloring of \(Q_n\), \(n\ge3\),
\[
\boxed{\mathbb E_{C\in\mathcal C_n}|S\cap C|
=\frac1{(n-1)2^{n-1}}\sum_{v\in Q_n}a(v)(n-a(v))
\le\frac{2\lfloor n^2/4\rfloor}{n-1}.}
\tag{11}
\]
Every projective rainbow cycle has an odd number of S-edges. Consequently some full dimension-simple antipodal geodesic has at most
\[
\boxed{2\left\lfloor\frac{n-1}{4}\right\rfloor}
\tag{12}
\]
ordinary color switches.

*Proof.* Each turn orbit lies on \((n-2)!\) cycles by Theorem 4, so the expected S-hit count is \(|S|/((n-1)2^{n-2})\). Summing the local complete-bipartite turn counts gives \(|S|=\tfrac12\sum_v a(v)(n-a(v))\), and establishes (11). Every rainbow cycle evaluates \(\alpha\) to one, so its S-hit count is odd. Let \(h=2\lfloor(n-1)/4\rfloor+1\). Directly evaluating the displayed upper bound in each residue class of n modulo four shows it is strictly less than \(h+2\). If every rainbow cycle had at least \(h+2\) hits, its mean would violate (11). Thus some cycle has at most h odd hits. Root rotation deletes one marked turn, yielding a complete geodesic with at most \(h-1\) ordinary switches, which is (12). \(\square\)

**Corollary 9 (local imbalance improves the bound in dimensions \(4k+1\)).** Let \(n=4k+1\ge5\). If at least one cube vertex has other than \(2k\) or \(2k+1\) incident edges of color one, then there is a full antipodal geodesic with at most \(2k-2\) color switches. If an odd coloring in dimension \(4k+1\) has no geodesic with at most \(2k-2\) switches, then every vertex must have a locally balanced split \(2k\) versus \(2k+1\), and every rainbow projective cycle has \(2k+1\) switched turns.

*Proof.* In these dimensions, the right side of (11) equals \(2k+1\), an odd integer. Strict local imbalance reduces its mean below \(2k+1\); since every cycle count is odd, some cycle has at most \(2k-1\) hits, and root rotation gives the improved path. Conversely absence of such a path forces every cycle to have at least \(2k+1\) hits, so mean equality holds, implying equality in the local inequality at every vertex and equality of every cycle hit count with \(2k+1\). \(\square\)

The estimate applies only to realized odd switch sets, where the projective hit parity is odd. A hereditary subset D of a realizable switch set need not preserve this oddness; its universal mean and density estimates are instead Theorems 5–7. The strengthened result pinpoints a potential obstruction to improving average switch bounds: in dimensions \(4k+1\), only everywhere-balanced colorings can saturate the mean limit.

#### Adjacent-exchange traps in rainbow projective cycles

**Theorem.** For every \(n\ge9\), an antipodally odd coloring of \(Q_n\) can have a three-switch projective rainbow geodesic cycle C for which every cyclic adjacent-dimension exchange produces a five-switch cycle. The coloring may also have a monochromatic full antipodal geodesic.

*Proof.* On the standard geodesic rooted at the zero vertex, with dimension order \(1,\ldots,n\), assign successive edge colors \(0001110^{n-6}\). The projective closing turn compares the final edge to the antipode of the first. Its only three switched turns lie after positions \(3,6,n\), separated cyclically by distances \(3,n-6,3\). Every three-turn window contains at most one switch.

Swapping two cyclically adjacent dimension edges changes just the three turns entering, between, and leaving the two-edge square route. Its parity is fixed by the colors a,b of the unchanged outer edges. If a=b, prescribe the alternate pair of square-edge colors as \((1-a,1-a)\), changing zero switches to two; if a differs from b, prescribe \((1-a,a)\), changing one switch to three. Every cyclic adjacent exchange thus adds two switches.

The n squares have distinct unordered direction pairs \(\{1,2\},\ldots,\{n-1,n\},\{n,1\}\). Their two alternate edges each are distinct from the standard path and the other alternate edges. No two specified edge orbits coincide under antipodality: opposite squares preserve the direction pair but are disjoint from the corresponding prescribed square for \(n\ge9\). The 3n edge-orbit prescriptions are consistent with antipodal oddness and extend freely to all other orbits.

There are \(n2^{n-2}\) antipodal orbits of cube edges. A uniformly random rooted full geodesic has n edges each marginally uniform on these orbits. Its expected number of encounters with the 3n prescribed orbits is \(3n/2^{n-2}<1\). Therefore some full geodesic misses them all. Color this additional geodesic monochromatically, enforce complementary antipodal colors, and fill remaining orbits arbitrarily. This preserves the frozen three-hit cycle. \(\square\)

**Implication.** The three-hit sublevel graph under cyclic adjacent exchanges may have isolated vertices even when a one-hit rainbow cycle exists elsewhere. Consequently neither one-step descent nor monotone three-hit plateau connectivity is a valid unconditional NORI1 proof mechanism. A critical-set closure argument must exploit relations among multiple tight witness cycles or allow temporary increases to five switches.

The construction extends to odd \(t\ge3\) when \(n\ge3t\), using t cyclic switches spaced at least three apart; every adjacent exchange can be prescribed to raise the switch count from t to t+2.

#### Dimension-parity barrier for linear witness-cycle closure

Let \(H_n=L(Q_n)/A\) be the antipodal quotient line graph of undirected cube edges. Let \(\alpha\) be its covering class, let \(\ell\) be the class evaluating a cycle by its length modulo two, and put \(\beta=\alpha+\ell\). Let \(\mathcal C_n\) denote the covering-odd, dimension-rainbow projective n-cycles.

**Theorem (character separation).** Every \(C\in\mathcal C_n\) satisfies
\[
\boxed{\alpha(C)=1,\quad\ell(C)=n\bmod2,\quad
\beta(C)=n+1\bmod2.}
\tag{16}
\]
Every triangle T formed by three incident cube edges at one cube vertex satisfies \(\alpha(T)=0\), \(\ell(T)=1\), and \(\beta(T)=1\). Therefore:
- for odd n, the binary cycle-space span of the projective rainbow cycles lies in the proper hyperplane \(\ker\beta\), and a star triangle witnesses that the inclusion is strict;
- for even n, their span lies in the proper hyperplane \(\ker\ell\), again excluding each star triangle.

*Proof.* By definition a rainbow projective n-cycle has covering monodromy one and has n edges. A star triangle lifts to two closed triangles based at antipodal cube vertices, so its covering monodromy is zero, while its length is three. Linear extension to cycle-space spans gives the two separation statements. \(\square\)

**Corollary (necessary odd triangle flux for odd-dimensional linear certificates).** If n is odd, any binary sum of rainbow projective n-cycles and their adjacent-exchange symmetric differences evaluates to zero under \(\beta\). Thus no such sum alone can furnish a \(\beta\)-odd cycle supported inside a candidate hereditary switch set D. A contradiction to the hereditary criterion \(\beta|_{H[D]}=0\) must use at least one additional cycle with nonzero \(\beta\), such as a star triangle, or a nonlinear operation not captured by these binary cycle sums.

The local star triangles are therefore not merely a nuisance of the line-graph encoding: they represent homological information invisible to dimension-rainbow projective cycles in the sparse *odd* dimensions targeted by the Grassmannian proof program. A promising closure route must couple tight three-hit cycles to triangle-containing exchange chains and force their unmarked parts to cancel. This is a necessary structural observation, not a construction of the required certificate.

#### Projective turn cycles are generated by rainbow cycles and star triangles

For \(n\ge3\), let \(G_n=Q_n/A\) and \(H_n=L(Q_n)/A\). Since G_n is simple, the quotient turn graph satisfies \(H_n\cong L(G_n)\).

**Theorem.** There is a short sequence of binary cycle spaces
\[
\boxed{0\to \bigoplus_{v\in V(G_n)}Z_1(K_n(v))
\to Z_1(H_n)\to Z_1(G_n)\to0,}
\]
where \(K_n(v)\) is the clique of the n edges incident with projective vertex v. The kernel has dimension \((n-1)(n-2)2^{n-2}\) and is spanned by local star triangles. Since the preceding Article XV Petrie theorem shows that full dimension-simple projective n-cycles span \(Z_1(G_n)\), it follows that **projective rainbow n-cycles and local star triangles together span \(Z_1(H_n)\)**.

*Proof.* Fill each star clique of H_n by a simplex. Distinct star simplices intersect in one vertex precisely when their centers in G_n are adjacent, and triple intersections are empty. Their nerve is G_n, hence their union has its homotopy type. Filling star simplices kills precisely the triangle-generated subspace, giving the short sequence. Different star cliques have disjoint graph-edge sets, so their cycle spaces sum directly. There are \(2^{n-1}\) stars, each of cycle rank \((n-1)(n-2)/2\). Finally rainbow cycles map to the Petrie generators of the quotient graph, proving the spanning claim. \(\square\)

**Triangle-flux invariant.** Write \(\alpha\) for covering monodromy on H_n and \(\ell\) for cycle-length parity. Let \(\chi_n=\ell+(n\bmod2)\alpha\). Every rainbow n-cycle has \(\chi_n=0\), while every star triangle has \(\chi_n=1\). Hence the parity of the number of star triangles in any rainbow-plus-triangle decomposition is independent of the decomposition.

In odd dimensions, \(\chi_n=\alpha+\ell=\beta\), the hereditary switch class. Therefore a parity-based contradiction for an alleged hereditary three-hit obstruction must retain odd star-triangle flux after canceling every unmarked turn. The theorem gives the complete cycle-space generators, but not the constrained cancellation needed to close NORI1.

#### Local flatness and a modulo-four switch improvement

Let c be an antipodally odd edge coloring of Q_n, n>=5, and let h(C) be the number of switched turns on a covering-odd dimension-rainbow projective n-cycle.

**Lemma.** If a cube vertex x has at least two incident edges of each color, there exist two rainbow cycles differing by one adjacent dimension exchange whose switch counts are different.

*Proof.* Select incident dimensions i,j of opposite colors. Among remaining dimensions select p,p' of opposite colors and a third q distinct from both; n>=5 assures this is possible. For r=p or p', start at x toggled in r, traverse r,i,j,q, then all other dimensions; compare with the geodesic exchanging i,j. Denote the two colored routes across the square at x by (u,v) and (u',v'), where u differs from u'. Let a_r be the incoming r-edge color and b the outgoing q-edge color. The total switch-count change is

Delta_r=([a_r !=u]-[a_r !=u'])+([u!=v]-[u'!=v'])+([v!=b]-[v'!=b]).

The last two differences do not depend on r. Since a_p and a_p' are opposite and u,u' are opposite, Delta_p-Delta_p' is either +2 or -2. Both changes cannot vanish. The projective closing turn is unchanged by the adjacent exchange. QED.

**Theorem.** If h(C) is constant over all rainbow projective n-cycles, then that constant equals one.

*Proof.* The lemma implies that every cube vertex has at most one incident edge of its minority color. If its zero/one incident counts are a,n-a, its switched incident turns number a(n-a)<=n-1. There are 2^(n-1) antipodal vertex orbits, so the quotient switch set has size at most (n-1)2^(n-1). The proven uniform cycle-incidence identity gives mean h=|S|/((n-1)2^(n-2))<=2. Each cycle has positive odd h because its monodromy evaluates to one. The common value is consequently one. QED.

**Corollary.** For n=4k+1, k>=1, every antipodally odd coloring has a full antipodal dimension-simple geodesic with at most 2k-2 ordinary color switches.

*Proof.* The mean projective switch bound is at most 2 floor(n*n/4)/(n-1)=2k+1. If no cycle had at most 2k-1 turns switched, every cycle (which has odd switch count) would have at least 2k+1, forcing h(C)=2k+1 for all cycles. The theorem contradicts this constant value. Hence some cycle has at most 2k-1 switched turns. Root rotation omits a switched turn, yielding a full geodesic with at most 2k-2 switches. QED.

This gives monochromatic closure at n=5 and bounds of two, four, and six switches at n=9,13,17. Unlike the earlier critical-cycle approach, the proof uses just one square, two predecessor colors, and uniform counting; it is uniform in dimension.

#### Quantitative exchange activity from a single vertex

For a vertex x let a(x),b(x) count its incident zero- and one-colored edges, with a+b=n. Choose a uniform rooted full cube geodesic, let H be the number of switched turns of its projective completion, and let H' be the count after exchanging its second and third dimensions. Both marginal distributions are uniform on rainbow projective cycles.

**Theorem (local exchange variance).** For n>=5 define
[
p_n(a,b)=\frac{2ab\bigl[(a-1)\min(a-2,b-1)+(b-1)\min(a-1,b-2)\bigr]}
{n(n-1)(n-2)(n-3)}
]
for a,b>=2 and put p_n=0 otherwise. Then
[
\boxed{\operatorname{Var}(H)\ge 2^{-n}\sum_{x\in Q_n}p_n(a(x),b(x)).}
	ag{24}
]

*Proof.* The initial four dimensions of a random rooted full geodesic have ordered roles (r,i,j,q), all distinct. Its square exchange takes place at x after direction r. For i,j of opposite incident colors at x, the swap effect Delta_r differs by two between predecessor colors zero and one, regardless of the square's other edge colors and the outgoing color in direction q. Among the possible r of the two colors, at least the size of the smaller group therefore produces nonzero Delta. There are 2ab choices of ordered opposite-colored i,j. After these are chosen, there are a-1 directions of color zero and b-1 of color one available. For a zero-colored q, the remaining predecessor groups have sizes a-2,b-1, while for a one-colored q they have sizes a-1,b-2. Counting the forced nonzero swaps gives the stated lower fraction p_n(a,b) among all n(n-1)(n-2)(n-3) ordered role choices at x.

Every nonzero swap change has absolute value at least two by three-turn parity. Thus E[(H-H')^2]>=4 E_x p_n(a(x),b(x)). Because H and H' have the same distribution, E[(H-H')^2]<=4 Var(H), proving (24). QED.

**Corollary (polynomial abundance in the balanced worst case).** Let n=4k+1, k>=1. If every cube vertex has incident colors split 2k versus 2k+1, then
[
\boxed{\operatorname{Var}(H)\ge
\frac{4k^2-1}{16k^2-1}.}
	ag{25}
]
Moreover, the proportion of rainbow projective cycles with at most 2k-1 switched turns is at least
[
\boxed{\frac{4k^2-1}{8k^2(16k^2-1)}.}
	ag{26}
]
Every such cycle has a root rotation giving at most 2k-2 ordinary switches.

*Proof.* Substitute a=2k,b=2k+1 in (24). The fraction simplifies to (4k^2-1)/(16k^2-1). The projective switch count H is odd, supported on [1,4k+1], and its mean under the local balance assumption is 2k+1. Let t=Pr(H<2k+1). Write A=2k for the maximum downward deviation and B=2k for the maximum upward deviation. Positive and negative deviations have the same expectation m<=tA. Their squares are bounded by B and A times their absolute magnitudes, so Var(H)<=m(A+B)<=8k^2t. Combine with (25) to obtain (26). QED.

This quantifies, rather than merely asserts, the obstruction to uniform projective switch count in locally balanced colorings. It provides polynomially many near-monochromatic geodesics in the extremal balancing regime, without coordinating a family of critical witness cycles.

##### Systolic and maximum-cut constraints on switch-component graphs

Let \(p:T\to H\) be a connected free double cover of a connected comparison graph, and let a legal odd coloring yield a quotient switch cocycle \(\eta\) with support \(S\). Let \(Z=(V(H),E(H)\setminus S)\). Contract every connected component of \(Z\) to obtain the connected multigraph \(F\), retaining all switches as edges, including possible loops. These objects are the cographic deletion normal form of the preceding gauge-criticality Subsection.

**Theorem 1 (short odd cycle survives all nonswitch contractions).** Suppose \(H\) contains a closed walk \(C\) of length at most \(L\) whose lift under the double cover joins a state to its involutive mate. Then \(F\) contains an odd circuit of length at most \(L\), with loops counted as odd circuits of length one.

*Proof.* Every legal switch cochain represents the covering class, so \(\sum_{e\in C}\eta(e)=1\pmod2\). Contracting nonswitch edges maps \(C\) to a closed walk in \(F\); the walk traverses precisely the switched edges of \(C\), counted with multiplicity, and has odd length at most \(L\). Every odd closed walk in a multigraph decomposes into circuits, at least one of which has odd length no greater than the walk. QED.

**Corollary 2 (uniform odd-girth bounds in the two unrestricted models).** For any antipodally odd edge coloring of \(Q_n\), the component multigraph \(F\) has odd girth at most \(n\), attained as an upper bound by following a full projective dimension-simple Petrie loop of length \(n\). For any reversal-odd ordered-triple coloring on \(n\ge5\) symbols, \(F\) has odd girth at most six, using the six-step reversal-monodromy walk in the preceding local-cycle Subsection.

**Theorem 3 (quantitative persistent frustration).** Let \(m=|S|=|E(F)|\). Then
\[
\boxed{m-\operatorname{MaxCut}(F)\ \ge\
\begin{cases}
(n-1)2^{n-2},& H=L(Q_n)/J,\quad n\ge3,\\[2pt]
\dfrac{n-4}{4(n-3)}\,|E(H)|,&H=O_n/R,\quad n\ge6.
\end{cases}}
\tag{1}
\]
Consequently, if \(m\) exceeds the respective lower bound by fewer than \(\lambda(F)\) edges, then the zero-switch graph \(Z\) must be connected.

*Proof.* By the cographic deletion theorem, deleting a maximum cut of \(F\) is legal and removes \(\operatorname{MaxCut}(F)\) switches without adding others. The resulting odd coloring has \(m-\operatorname{MaxCut}(F)\) switched comparisons. Every legal cube comparison cochain has at least \((n-1)2^{n-2}\) switches, by the sharp Petrie-averaging cosystole calculation. Every legal reversal-odd triple comparison cochain has at least \(((n-4)/(4(n-3)))|E(H)|\) switches, by the complementary signed-spectral bound in the matroid generalizations section. This proves (1). If \(Z\) is disconnected, \(F\) has at least two vertices and therefore admits a nonempty cut of size at least \(\lambda(F)\). The maximum cut is at least that large, so (1) implies \(m\) is at least the lower bound plus \(\lambda(F)\). Contraposition proves the connectivity criterion. QED.

**Corollary 4 (frustration survives every legal monotone reduction).** The maximum-cut residual graph is still forced to contain an odd circuit of length at most the monodromy length bound from Corollary 2, and its remaining number of switched comparisons obeys (1). Thus no sequence of legal switch deletions can collapse the odd class to a bipartite component quotient; its frustrated core carries both a short odd-cycle certificate and a globally extensive support constraint.

**Interpretation.** The inherited short odd cycle is a *local witness of nonzero covering monodromy*, whereas the maximum-cut deficit measures the global complexity of maintaining that monodromy across all comparisons. The boundary model differs sharply from the cube: its residual signed switch support is a positive fraction of all turns asymptotically, while the cube can reach fraction \(1/n\). Neither statement by itself forces a spanning Hamilton path with one switch or a dimension-simple monochromatic cube geodesic. Their combined constraints provide quantitative tests for proposed switch-critical counterexamples and legal deletion strategies.

##### Product factorization of paired roots and the prime closure target

Let \(f\) be an arbitrary binary coloring of the undirected edges of \(Q_d\), without antipodal hypotheses. For a root \(z\in Q_d\), let \(z\in A(f)\) mean that a full dimension-simple geodesic from \(z\) to \(\bar z\) has color word \(0^p1^{d-p}\) for some \(0\le p\le d\). Both monochromatic words are admitted, corresponding to empty initial or final blocks. Define the **paired-root set**
\[
P(f)=A(f)\cap\bar A(f)
=\{z:z\in A(f)\text{ and }\bar z\in A(f)\}.
\tag{1}
\]
By the universal bridge equivalence in the gauge-criticality Subsection, NORI1 in dimension \(d+1\) is equivalent to \(P(f)\ne\varnothing\) for every \(d\)-cube edge coloring \(f\).

**Theorem 1 (Cartesian factorization).** Let \(f\) and \(g\) be arbitrary edge colorings of \(Q_a\) and \(Q_b\). Define \(f\boxtimes g\) on \(Q_{a+b}=Q_a\times Q_b\) by coloring edges moving in the first block according to \(f\) and edges moving in the second block according to \(g\), independently of the opposite block. Then
\[
\boxed{A(f\boxtimes g)=A(f)\times A(g),\qquad
P(f\boxtimes g)=P(f)\times P(g).}
\tag{2}
\]

*Proof.* Restrict any full geodesic \(P\) in \(Q_a\times Q_b\) to the steps moving in the first factor. Its subsequence is a full dimension-simple geodesic from the first root to its antipode, and its colors are precisely the corresponding \(f\)-edge colors. The same applies to the second factor. Every subsequence of a word \(0^*1^*\) is itself of this form, proving \(A(f\boxtimes g)\subseteq A(f)\times A(g)\). Conversely, take paths in the factors whose words are respectively \(0^{p}1^{a-p}\) and \(0^{q}1^{b-q}\). Traverse the zero prefixes in both factors, followed by their one suffixes in both factors. The result is a full dimension-simple product geodesic with color word \(0^{p+q}1^{a+b-p-q}\), proving equality. Antipodal complementation acts componentwise on roots, so intersecting with the antipodal images gives the second identity. QED.

**Theorem 2 (exponentially sparse favorable and paired roots).** Let \(h\) color the two edges incident with \(00\in Q_2\) by 1 and the two edges incident with \(11\in Q_2\) by 0. Then
\[
A(h)=\{01,10,11\},\qquad P(h)=\{01,10\}.
\tag{3}
\]
For the \(k\)-fold Cartesian product \(h^{\boxtimes k}\) on \(Q_{2k}\),
\[
\boxed{
|A(h^{\boxtimes k})|=3^k,\quad
|P(h^{\boxtimes k})|=2^k,\quad
\frac{|A|}{2^{2k}}=(3/4)^k,\quad
\frac{|P|}{2^{2k}}=(1/2)^k.
}\tag{4}
\]
In particular there is no positive dimension-independent lower bound on the *density* of favorable roots or of paired roots, even within colorings satisfying the paired-root conclusion. Moreover the number of antipodal pairs contained in \(P(h^{\boxtimes k})\) equals \(2^{k-1}\), which is even for every \(k\ge2\).

*Proof.* From root \(00\), both possible two-step full geodesics have word \(10\), so \(00\notin A(h)\). From \(11\), both have word \(01\), so \(11\in A(h)\). From \(01\) or \(10\), one order gives word \(00\) and the other gives word \(11\), so both roots belong to \(A(h)\). The paired roots are \(01,10\), giving (3). Apply Theorem 1 repeatedly to obtain (4) and divide by the \(4^k\) total roots. The antipodal involution on \(P\) has no fixed root, giving \(2^{k-1}\) orbits. QED.

**Theorem 3 (canonical interaction-prime decomposition).** For any undirected edge coloring \(f\) of \(Q_d\), write \(f_i(x)\) for the color of the direction-\(i\) edge at \(x\), so \(f_i(x)=f_i(x\oplus e_i)\). For distinct dimensions \(i,j\), put
\[
\partial_j f_i(x)=f_i(x)+f_i(x\oplus e_j)\pmod2.
\]
Form the **interaction graph** \(\Gamma(f)\) on the \(d\) dimensions, joining \(i\) and \(j\) if either \(\partial_jf_i\) or \(\partial_if_j\) is nonzero somewhere. If \(C_1,\ldots,C_t\) are its connected components, there are uniquely determined factor colorings \(f^{(s)}\) such that
\[
\boxed{f=\boxtimes_{s=1}^t f^{(s)},\qquad
A(f)=\prod_{s=1}^t A(f^{(s)}),\qquad
P(f)=\prod_{s=1}^t P(f^{(s)}).}
\tag{5}
\]
Consequently the paired-root conjecture for all cube colorings is equivalent to its restriction to colorings whose interaction graph is connected. Any counterexample of least dimension must have connected interaction graph.

*Proof.* If \(i\in C_s\) and \(j\notin C_s\), then \(\partial_j f_i\equiv0\). Hence \(f_i\) is invariant under changing any bit outside \(C_s\); therefore it depends only on the bits within \(C_s\). This defines the factor coloring \(f^{(s)}\), and proves the product representation. Conversely, any product decomposition yields no interaction edges between different factors. Thus the component partition is the unique finest product decomposition, and (5) follows from Theorem 1. If a product has no paired root, one factor has no paired root; a minimum-dimension counterexample cannot have more than one factor. QED.

**Closure program and its limits.** The bridge theorem reduces NORI1 to paired-root existence, while Theorem 3 further reduces it to **interaction-connected** edge colorings. Theorems 1-2 rigorously rule out two tempting shortcuts: pigeonholing from a fixed positive favorable-root density and an odd-parity count of antipodal paired-root orbits. A prospective closure proof should instead detect an invariant of the *antipodal arrangement* of feasible roots that is preserved under Cartesian products and is forced for interaction-connected colorings. The interaction graph records all cross-dimension dependence (square derivatives), offering a natural induction parameter tied to dimension-simplicity rather than the total number of local switches. The result by itself does not prove the paired-root conjecture for connected interaction graphs.

#### Interaction-connected sparse-root colorings

The previous product construction has disconnected interaction graph. A one-dimensional coupling shows that even restricting to interaction-prime colorings cannot support a uniform positive density lower bound for favorable roots.

**Theorem 4 (connected interactions with exponentially sparse roots).** For every \(k\ge1\), there is an edge coloring \(F_k\) of \(Q_{2k+1}\) for which:
1. its interaction graph \(\Gamma(F_k)\) is connected (indeed, contains a spanning star);
2. \(P(F_k)\ne\varnothing\);
3. its favorable-root and paired-root densities obey
\[
\boxed{
\frac{|A(F_k)|}{2^{2k+1}}\le(3/4)^k,\qquad
\frac{|P(F_k)|}{2^{2k+1}}\le(1/2)^k.
}
\tag{6}
\]
Thus both densities tend to zero even for interaction-connected colorings that satisfy the paired-root conclusion.

*Proof.* Take the \(2k\)-dimensional product coloring \(f_k=h^{\boxtimes k}\) of Theorem 2. Extend it to \(Q_{2k+1}=Q_{2k}\times Q_1\) by retaining all its old-dimension edge colors unchanged in both layers, and assigning to the new-direction edge above \(x\in Q_{2k}\) the color
\[
F_k(x,\mathrm{new})=\sum_{i=1}^{2k}x_i\pmod2.
\tag{7}
\]
This is well-defined on the unoriented new edge, because it is independent of the new bit. Its derivative in each old dimension equals one. Therefore the interaction graph contains every edge joining the new dimension to an old dimension and is connected.

Take any full \(0^*1^*\) geodesic in the enlarged cube and delete its unique step in the new dimension. All remaining old steps form a full geodesic in \(Q_{2k}\), with the same color subsequence, hence remain \(0^*1^*\). Therefore
\[
A(F_k)\subseteq A(f_k)\times\{0,1\}
\]
and, after antipodal intersection,
\[
P(F_k)\subseteq P(f_k)\times\{0,1\}.
\]
Using \(|A(f_k)|=3^k\), \(|P(f_k)|=2^k\) gives the two density bounds.

To show a paired root exists, take any \(x\in P(f_k)=\{01,10\}^k\). Every such \(x\) has Hamming weight \(k\), and its antipode in \(Q_{2k}\) has the same Hamming weight \(k\). Thus the new-direction edge color at \(x\) and \(\bar x\) is the common bit \(k\bmod2\). If this bit is zero, insert the new-direction step **before** a \(0^*1^*\) old path from each of \(x,\bar x\); if it is one, insert the step **after** each old path. The resulting geodesics in \(Q_{2k+1}\) still have word \(0^*1^*\), from both antipodal roots \((x,t)\) and \((\bar x,1-t)\). Hence \(P(F_k)\ne\varnothing\). QED.

**Corollary 5 (absence of a rootwise orientation covering).** Let \(A_1(f)\) denote roots supporting a \(1^*0^*\) geodesic. Reversal of full paths gives \(A_1(f)=\bar A(f)\). For the product coloring \(f_k=h^{\boxtimes k}\),
\[
\boxed{|A(f_k)\cup A_1(f_k)|=2\cdot3^k-2^k.}
\tag{8}
\]
The fraction of roots supporting *either* one-switch orientation tends to zero. The same upper bound (after dividing by the corresponding total vertex count) holds for the connected extension \(F_k\), because restriction to old directions preserves both monotone color-word types.

*Proof.* By Theorem 2, \(|A(f_k)|=3^k\) and \(|A(f_k)\cap\bar A(f_k)|=2^k\). Inclusion–exclusion gives (8). Restriction of any full \(1^*0^*\) path to the old dimensions gives a path of that type in \(f_k\), and similarly for \(0^*1^*\). QED.

**Implication for closure.** Even a prime-interaction hypothesis cannot force a fixed positive density of favorable roots or a rootwise choice of one of the two monotone orientations. Cartesian factorization remains useful as an induction simplification, but the missing theorem has to use the precise antipodal *placement* and mutual compatibility of the favorable roots rather than their abundance or mere interaction-connectedness.

#### Seam insertion and the directed dependency cycle core

**Lemma 6 (unrestricted seam insertion).** Let \(f\) be an arbitrary binary edge coloring of \(Q_d\). Color both horizontal layers of \(Q_{d+1}=Q_d\times Q_1\) identically by \(f\), and color the vertical edge over \(x\) arbitrarily by \(h(x)\). For \(F\) so obtained,
\[
\boxed{A(F)=A(f)\times\{0,1\},\qquad P(F)=P(f)\times\{0,1\}.}
\tag{9}
\]

*Proof.* Restrict a full \(0^*1^*\) geodesic under \(F\) to the old directions. Its subsequence remains a full antipodal geodesic in \(Q_d\), with unchanged colors, hence has the same monotone word pattern. Conversely, let a favorable full path under \(f\) have word \(0^p1^{d-p}\), allowing \(p=0,d\). Starting at \((z,t)\), traverse its first \(p\) edges in layer \(t\), traverse the new vertical edge at the switch vertex \(v\), then traverse its final \(d-p\) old-direction edges in layer \(1-t\). If \(h(v)=0\), the extra edge extends the zero prefix; if \(h(v)=1\), it starts or extends the one suffix. Either way the full path is favorable, regardless of \(h\) and \(t\). Its endpoint is \((\bar z,1-t)\). This proves the first equality, and intersection with the componentwise antipodal images yields the second. QED.

**Theorem 7 (directed dependency sink elimination).** For an arbitrary edge coloring \(f\) of \(Q_d\), define a digraph \(\vec\Gamma(f)\) on dimensions by placing an arc \(i\to j\) if \(i\ne j\) and
\[
\partial_i f_j(x):=f_j(x)+f_j(x\oplus e_i)
\]
is nonzero at some cube vertex. If \(i\) has outdegree zero, the coloring on every other direction is independent of the \(i\)-th bit. Deleting that dimension gives a smaller coloring \(g\), with
\[
\boxed{A(f)=A(g)\times\{0,1\},\qquad P(f)=P(g)\times\{0,1\}.}
\tag{10}
\]
Repeated sink deletion gives an induced core with no outdegree-zero vertices, preserving paired-root existence.

*Proof.* An absent arc \(i\to j\) states precisely that the \(j\)-edge colors are invariant under the \(i\)-bit flip. The \(i\)-edge colors themselves are arbitrary functions of the other bits. Thus Lemma 6 applies. Removing a dimension does not change interactions between remaining dimensions; repeating gives the core. QED.

**Corollary 8 (full-root theorem for acyclic dependencies).** If \(\vec\Gamma(f)\) is acyclic, every vertex of \(Q_d\) supports a complete \(0^*1^*\) geodesic, and
\[
\boxed{A(f)=P(f)=V(Q_d).}
\tag{11}
\]

*Proof.* Remove sink dimensions successively in an acyclic digraph, reaching the zero-dimensional cube, whose empty path is favorable. Each inverse seam insertion duplicates its entire favorable-root set by Lemma 6. Hence every root is favorable and paired. QED.

**Corollary 9 (cycle core is necessary for minimal failure).** If the paired-root conjecture is false, any counterexample of minimum dimension has a directed dependency graph with minimum outdegree at least one, so it contains a directed cycle. By the earlier product theorem, its underlying undirected interaction graph may also be assumed connected.

*Proof.* A sink would reduce the failure to fewer dimensions without changing paired-root existence, contradicting minimal dimension. A finite digraph of minimum outdegree one has a directed cycle. Disconnected undirected interaction graphs split as Cartesian products, and failure in a product implies failure in a factor. QED.

**Corollary 10 (connected sparse-root gadget revisited).** The interaction-connected coloring \(F_k\) in Theorem 4 has identical old edges across its added dimension. Thus the earlier root-count upper estimates are equalities:
\[
\boxed{|A(F_k)|=2\cdot3^k,\qquad |P(F_k)|=2^{k+1}.}
\tag{12}
\]
Its added direction has outdegree zero in \(\vec\Gamma(F_k)\), illustrating that undirected interaction-connectedness is weaker than directed sink irreducibility.

**Closure program.** This is a proof-preserving reduction for *every* arbitrary lower-cube coloring: strip all sink dimensions without changing the paired-root question. It rules out all directed-acyclic colorings and isolates a cyclic dependency core as the first remaining case. The seam insertion operation preserves dimension-simplicity and works regardless of the added edge's color. Root density cannot replace this reduction, since root densities in the preceding product and connected gadget examples tend to zero. The cyclic-core paired-root conjecture remains open.### The full two-layer arm interface and inductive closure target

Let \(F\) be any binary edge coloring of \(Q_{d+1}=Q_d\times\{0,1\}\), described by horizontal-layer colorings \(f_0,f_1\) and vertical-edge colors \(h(y)\). Fix a root \((z,t)\). For a subset \(U\subseteq[d]\), put \(y=z\oplus\mathbf1_U\). A directed *zero arm* uses only color-zero edges; a *one arm* only color-one edges; a *monotone arm* has color word \(0^*1^*\). Each arm follows dimensions from its prescribed subset without repetition; empty arms are allowed.

**Theorem 11 (two-layer interface equivalence).** The root \((z,t)\) admits a full dimension-simple \(0^*1^*\) geodesic if and only if there exists \(U\subseteq[d]\) such that one of the following holds:

(i) \(h(y)=0\), there is a zero arm from \(z\) to \(y\) in layer \(t\) using all and only \(U\), and there is a monotone arm from \(y\) to \(\bar z\) in layer \(1-t\) using all and only \(U^c\).

(ii) \(h(y)=1\), there is a monotone arm from \(z\) to \(y\) in layer \(t\) using all and only \(U\), and there is a one arm from \(y\) to \(\bar z\) in layer \(1-t\) using all and only \(U^c\).

The root is paired if and only if the criterion holds both at \((z,t)\) and its antipode \((\bar z,1-t)\), with independently chosen seam subsets.

*Proof.* Any full geodesic uses the new vertical dimension precisely once. Before it, the old steps use a subset \(U\) and end at \(y=z\oplus\mathbf1_U\); after it, the remaining steps use \(U^c\) and end at \(\bar z\). If the vertical bit is zero, any earlier color one would break the nondecreasing word, so the initial arm must be all zero while the final arm can be monotone. If it is one, any later zero would break the word, so the final arm must be all one while the initial arm can be monotone. Conversely each indicated pair of arms concatenated across the vertical edge forms a full dimension-simple monotone-color geodesic. QED.

**Proposition 12 (order-compatible seam suffices).** Suppose a full dimension order \(\pi\) starting at \(z\) has words \(0^{p_0}1^{d-p_0}\) in layer \(f_0\) and \(0^{p_1}1^{d-p_1}\) in layer \(f_1\), where \(p_0\ge p_1\). Then for **every** vertical coloring \(h\), the extended cube has a full favorable geodesic from \((z,0)\). The new step can be inserted at any rank \(r\) with \(p_1\le r\le p_0\).

*Proof.* Traverse the first \(r\) old directions in layer zero, the vertical edge at the resulting vertex, then the remaining old directions in layer one. The first block is entirely zero since \(r\le p_0\); the last block is entirely one since \(r\ge p_1\). The inserted edge may have either color without creating a decrease. Every dimension occurs once. QED.

**Induction blueprint.** The universal bridge equivalence reduces NORI1 in dimension \(d+1\) to paired-root existence for arbitrary horizontal layer colorings and vertical bits. To induct from dimension \(d\), it would suffice to prove that the two layerwise monotone-arm systems always have complementary seam certificates simultaneously at some antipodal roots, as characterized by Theorem 11. The newly proved seam-insertion lemma settles the whole two-layer problem when \(f_0=f_1\), regardless of vertical colors; the order-interlacing proposition supplies a further sufficient certificate for one orientation. The missing assertion is a coupling of directed arm reachability under distinct layers, while preserving the partition of dimensions before and after the crossing. This assertion is not proved here.

#### Closing paired roots on functional cyclic cores with arbitrary nonlinear tails

The directed sink reduction and the existing affine one-dependency theorem combine to settle a substantial family that retains cyclic dependencies and allows unrestricted nonlinear color functions on all removable dimensions.

**Theorem 13 (paired roots for disjoint directed-cycle cores).** Let \(f\) be any binary coloring of the undirected edges of \(Q_d\). Repeatedly remove dimensions of outdegree zero in its directed dependency graph \(\vec\Gamma(f)\), as in Theorem 7, and let \(C\) be the retained dimension set. Assume the induced directed dependency graph on \(C\) is a disjoint union of directed cycles of lengths at least two. Then
\[
\boxed{P(f)\ne\varnothing.}
\tag{13}
\]
Indeed, on the core, if the cycles have lengths \(\ell_1,\ldots,\ell_r\), then at least
\[
\boxed{\prod_{j=1}^r(2^{\ell_j}-2)}
\tag{14}
\]
different roots admit a **monochromatic zero** full geodesic both from themselves and from their antipodes. On the original \(Q_d\), each of these paired core roots lifts to \(2^{d-|C|}\) paired roots supporting \(0^*1^*\) complete geodesics. The case \(C=\varnothing\) is covered by the full-root acyclic theorem.

*Proof.* Theorem 7 shows that deletion of each sink direction preserves the favorable-root and paired-root sets, after projection to the remaining dimensions. Thus it suffices to analyze the restricted core coloring \(g\) on \(Q_C\).

For every \(i\in C\), the core dependency digraph has precisely one incoming arc, from its predecessor \(p(i)\ne i\) on a directed cycle. Therefore the color of a direction-\(i\) edge is independent of all old dimensions except \(p(i)\), and independent of bit \(i\) by undirected-edge consistency. Since the derivative in predecessor direction is nonzero, the color is necessarily
\[
g_i(x)=a_i+x_{p(i)}\pmod2
\tag{15}
\]
for some constant bit \(a_i\).

Choose a root \(z\in Q_C\), and define \(b_i=a_i+z_{p(i)}\). For an order of the dimension labels, the color seen when dimension \(i\) is traversed is \(b_i+\mathbf1_{\{p(i)\text{ occurs earlier than }i\}}\). Thus an all-zero geodesic from \(z\) exists precisely when the precedence constraints
\[
\mathbf1_{\{p(i)\text{ before }i\}}=b_i
\tag{16}
\]
admit a linear ordering. On a directed dependency cycle, these constraints are inconsistent only when they orient every relation cyclically in one of the two directions, equivalently when all bits \(b_i\) on that cycle are equal. If the bits are not all equal, the resulting orientation of that cycle is acyclic and admits a topological ordering. Different dependency cycles are disjoint, so such orderings can be concatenated. Consequently an all-zero geodesic from \(z\) exists whenever the \(b\)-sequence is nonconstant on each cycle.

At the antipodal root \(\bar z\), the values become \(b_i+1\). Complementing all bits preserves nonconstancy, so the same acyclicity argument supplies an all-zero geodesic from \(\bar z\), possibly under a different dimension order. Thus every such \(z\) is a paired root.

On a cycle of length \(\ell\), the map \(z\mapsto(b_i)_{i\text{ in cycle}}\) is a bijection because \(p\) permutes that cycle. Precisely two of its \(2^\ell\) assignments are constant. The number of roots satisfying all cycle conditions is therefore at least the product (14). Reinsert each deleted dimension using Lemma 6: favorable-root and paired-root sets duplicate across its two possible starting bits without requiring any restriction on that dimension's own edge-color function. This establishes (13) and the asserted lifted count. QED.

**Corollary 14 (in-degree-one cyclic core).** The conclusion holds whenever the sink-deletion core has **indegree at most one at every vertex**. Since every retained vertex has outdegree at least one and the total indegree equals the total outdegree, this forces indegree and outdegree one everywhere, and hence a union of directed cycles.

**Closure implication.** In any least-dimensional counterexample to paired-root existence, the dependency digraph has no sink and cannot be a disjoint union of directed cycles. In particular it must have a vertex of indegree at least two, or an equivalent branching feature. The proof extends the established affine one-predecessor construction to arbitrary nonlinear colorings outside the directed cyclic core, relying on the seam-insertion identity rather than on color density. This is not a proof for general branching cores.

#### Fiberwise seam insertion removes globally cyclic dependency blocks

Let \(Q_{a+b}=Q_A\times Q_B\) be a Cartesian splitting of the dimensions. Let \(F\) be an arbitrary binary edge coloring such that every edge moving in \(A\) has a color depending only on its \(A\)-vertex, not on the \(B\)-bits; these \(A\)-edges induce a coloring \(f\) of \(Q_A\). For each \(x\in Q_A\), let \(g_x\) denote the induced coloring of the \(B\)-dimensional fiber \(\{x\}\times Q_B\). The \(g_x\) may differ arbitrarily with \(x\).

**Theorem 15 (all-root fiber gluing).** If
\[
\boxed{A(g_x)=V(Q_B)\qquad\text{for every }x\in Q_A,}
\tag{17}
\]
then
\[
\boxed{A(F)=A(f)\times V(Q_B),\qquad
P(F)=P(f)\times V(Q_B).}
\tag{18}
\]
Consequently an arbitrary collection of \(B\)-directions can be removed without changing paired-root nonemptiness whenever the outer edge colors are independent of them and each fixed outer-vertex fiber has all roots favorable.

*Proof.* Take any full \(0^*1^*\) geodesic of \(F\) and erase all steps in dimensions \(B\). Since the remaining \(A\)-edge colors are independent of \(B\), their sequence is unchanged and retains the form \(0^*1^*\). This gives \(A(F)\subseteq A(f)\times V(Q_B)\).

Conversely, fix \(z\in A(f)\) and any \(t\in Q_B\). Choose a full \(A\)-geodesic from \(z\) to \(\bar z\) whose word is \(0^p1^{a-p}\), and let \(v\) be its vertex after the first \(p\) edges. By (17) the fiber coloring \(g_v\) admits a full \(B\)-geodesic from \(t\) to \(\bar t\) with word \(0^q1^{b-q}\). Insert this full fiber path at \(v\), between the zero prefix and one suffix of the \(A\)-path. The resulting word is \(0^{p+q}1^{a+b-p-q}\); all dimensions in \(A\cup B\) are used once, and the endpoint is \((\bar z,\bar t)\). Thus the reverse inclusion holds. Intersecting with antipodal images gives the formula for \(P\). QED.

**Corollary 16 (fiberwise acyclic criterion).** The conclusion holds whenever, for every \(x\in Q_A\), the directed dependency graph **within the fiber** \(g_x\) is acyclic. The dependency graph of the full coloring \(F\) may nonetheless contain directed cycles and vertices with several incoming dependencies.

*Proof.* Corollary 8 gives \(A(g_x)=V(Q_B)\) for every fiber. Apply Theorem 15. QED.

**Example 17 (a sink-free branching dependency graph eliminated by fibers).** Split three dimensions as \(A=\{a\}\) and \(B=\{u,v\}\). Color every \(a\)-edge zero, independent of \(u,v\). For the other directions set
\[
\begin{array}{c|cc}
a&F_u(a,u,v)&F_v(a,u,v)\\ \hline
0&0&u\\
1&v&0
\end{array}
\tag{19}
\]
where each expression is independent of the bit in its own direction and hence defines an undirected edge coloring.

When \(a=0\), the fiber dependency graph has one arc \(u\to v\); when \(a=1\), it has one arc \(v\to u\). Both are acyclic, so all four roots of each \(Q_2\) fiber are favorable. However the dependency digraph of the full \(Q_3\) coloring contains \(u\to v\), \(v\to u\), \(a\to u\) and \(a\to v\). It has no sink, possesses a directed two-cycle, and has branching at \(a\). The preceding single-direction sink reduction therefore cannot remove any dimension. Nevertheless Theorem 15 applies to the entire block \(B\), with the base \(a\)-edge constantly zero, and proves
\[
\boxed{A(F)=P(F)=V(Q_3).}
\]
This illustrates that fiberwise gluing handles some cyclic dependency cores with branching, not merely acyclic global dependency digraphs.

**Closing direction.** Theorem 15 reframes the remaining induction obstacle: when an external block affects its internal colorings, gluing succeeds if the fibers are root-universally favorable. To extend it beyond acyclic fibers, one needs a weaker two-fiber antipodal-intersection principle that permits fibers having only some favorable roots. This is precisely where the paired-root theorem is stronger than all-root feasibility; the product examples show that all-root feasibility cannot be demanded in full generality.

#### Sink strongly connected cycle elimination: closure reduces to internal branching

The preceding sink-dimension reduction and disjoint-cycle theorem leave a gap for interactions **between** different directed cycles. The following fiberwise overlap principle removes that gap without assuming any independence of the cycle edge colors from the outside bits.

For an arbitrary binary edge coloring f of \(Q_d\), write \(A(f)\) for the starting roots supporting a full \(0^*1^*\) geodesic and \(P(f)=A(f)\cap\overline{A(f)}\) for its paired roots.

**Lemma 18 (paired-root gluing across a fiber block).** Suppose \(Q_{a+b}=Q_A\times Q_B\) carries a coloring F whose A-direction edge colors depend only on the A-vertex, inducing f on \(Q_A\). For each \(x\in Q_A\), let \(g_x\) be the B-fiber coloring above x. Assume
\[
\boxed{A(g_x)\cap\overline{A(g_y)}\ne\varnothing
\quad\text{for all }x,y\in Q_A.}
\tag{20}
\]
Then
\[
\boxed{P(F)\ne\varnothing\iff P(f)\ne\varnothing.}
\tag{21}
\]
More quantitatively, if the intersections in (20) all have cardinality at least L, then \(|P(F)|\ge L|P(f)|\).

*Proof.* Any full favorable path in F projects, after deleting B-direction steps, to a full favorable path in f. Thus a paired root of F projects to a paired root of f.

Conversely choose \(z\in P(f)\). Take full favorable A-paths from \(z\) and from \(\bar z\), and denote the A-vertices at their respective color switch seams by x and y; seam vertices exist even for monochromatic paths by allowing an empty prefix or suffix. Choose \(t\in A(g_x)\cap\overline{A(g_y)}\). Insert a full favorable B-path from t at the first seam and a full favorable B-path from \(\bar t\) at the second seam. Since each fiber path has a \(0^*1^*\) color word, its insertion between the zero prefix and one suffix of the A-path preserves monotonicity and uses every B-direction once. Hence \((z,t)\) and \((\bar z,\bar t)\) are both favorable in F, proving pairedness. Distinct t give distinct paired roots. Since z ranges over all P(f), this proves the quantitative statement as well. \(\square\)

**Lemma 19 (all-root except one for a directed dependency cycle).** Let g color the undirected edges of \(Q_m\), \(m\ge2\), and suppose its directed dependency graph is a subgraph of a fixed directed cycle of length m. Then
\[
\boxed{|Q_m\setminus A(g)|\le1.}
\tag{22}
\]
For \(m=1\), every root is favorable.

*Proof.* If one dependency arc of the cycle is missing, the directed dependency graph is acyclic, and the established acyclic-dependency theorem gives \(A(g)=Q_m\). Otherwise each direction i has one predecessor \(p(i)\), with \(\partial_{p(i)}g_i\ne0\) and no other dependencies. Thus
\[
g_i(u)=a_i+u_{p(i)}
\]
for constant bits a_i. At root z put \(b_i=a_i+z_{p(i)}\). During a dimension order \(\pi\), the edge in direction i has color \(b_i+[p(i)\text{ occurs before }i]\).

If the bits b_i are not all equal, orient each relation between p(i) and i to make the edge color zero. The resulting orientation of the underlying directed cycle cannot itself be a directed cycle, as that would require all b_i equal. It therefore admits a total order, yielding an all-zero full geodesic.

If all b_i equal zero, order dimensions along the reverse cyclic dependency, so that every predecessor occurs *after* its direction except for the last direction. The resulting geodesic color word is \(0^{m-1}1\), which is favorable.

If all b_i equal one, the first direction of every order has color one (its predecessor has not appeared), while the final direction has color zero (its predecessor has appeared), so no order is favorable. Since the predecessor map p permutes the dimension set, there is only one root with all b_i=1. This proves (22). \(\square\)

**Theorem 20 (SCC cycle elimination and root-count lower bound).** Let f be any binary edge coloring of \(Q_d\), with directed dependency graph \(\vec\Gamma(f)\). Suppose **every strongly connected component** is either a singleton or a directed simple cycle (of length at least two). Let the nontrivial components have sizes \(m_1,\ldots,m_s\), and let there be r singleton components. Then
\[
\boxed{
|P(f)|\ge2^r\prod_{j=1}^s(2^{m_j}-2)>0.}
\tag{23}
\]
In particular every coloring with a directed pseudoforest condensation of cyclic components satisfies the paired-root theorem and hence the corresponding NORI1 bridge conclusion. Edges between distinct components may be arbitrarily numerous and their color dependence nonlinear.

*Proof.* The condensation of any finite directed graph is acyclic and has a sink component B. No directed dependency arrow leads from B to its complement A, so all A-direction edge colors are independent of B-bits. For every fixed outer vertex x, the dependency graph of the B-fiber g_x is a subgraph of the component's induced dependency graph. If B is a singleton then \(A(g_x)=Q_B\). If B is a directed cycle of size m, Lemma 19 shows that each fiber favorable-root set omits at most one root. Thus for every x,y, the intersection \(A(g_x)\cap\overline{A(g_y)}\) has size at least \(2^m-2\), positive for m>=2. Apply Lemma 18 to remove B, preserving paired-root nonemptiness and multiplying the lower bound for the number of paired roots by two for a singleton or \(2^m-2\) for a cyclic component. Repeat along the condensation DAG. At the empty cube there is one paired root (the empty path), proving (23). \(\square\)

**Corollary 21 (structural minimum-counterexample obstruction).** If the paired-root theorem—and hence NORI1—fails, an edge coloring of least dimension with no paired root has a **strongly connected dependency component with branching inside the component**: it is neither a singleton nor a directed simple cycle. This is strictly stronger than ruling out globally acyclic graphs, disconnected interactions, sinks, or an entire digraph that is a disjoint union of cycles. Arbitrarily complicated nonlinear branching *between* cyclic strongly connected components cannot produce a counterexample.

**Research significance.** A proof of paired-root existence for a single strongly connected branching dependency core, stable under arbitrary exterior fiber parameters, is now the well-delimited missing step. The obstruction is not a large family of geodesics but the interaction pattern of the directional Boolean derivatives within one component. The full theorem remains open for such components.

#### A nonlinear single-branch dependency core has strictly more than half its roots favorable

The SCC reduction above settles directed simple cycles, but a first strongly connected branching pattern also admits a structural solution. Fix \(m\ge3\). Let the dimensions of a fiber be \(0,1,\ldots,m-1\), and suppose every non-hub direction i, \(1\le i<m\), has edge color
\[
\boxed{g_i(u)=a_i+u_{i-1},}
\tag{24}
\]
whereas the hub-direction color \(g_0(u)=h(u_1,\ldots,u_{m-1})\) is an **arbitrary Boolean function**. In particular the hub may depend nonlinearly on all other dimensions and receive arbitrarily many incoming dependency arcs. No assumption is made about the functional form of h. The non-hub predecessor derivatives in (24) are active for every input, not merely somewhere.

**Theorem 22 (single-branch favorable-root majority).** Every coloring of the displayed form satisfies
\[
\boxed{|A(g)|>2^{m-1}.}
\tag{25}
\]
More precisely, unless h is constant, one has
\[
\boxed{|A(g)|\ \ge 2^{m-1}+|\{u\in\{0,1\}^{m-1}:h(u)=0\}|.}
\tag{26}
\]
When h is constant, all roots are favorable.

*Proof.* For each starting root \(z\), prescribe that every direction i>=1 traverse a color-zero edge. This imposes the precedence relation
\[
[i-1\prec i]=a_i+z_{i-1}\quad(i=1,\ldots,m-1).
\tag{27}
\]
These comparisons orient the edges of the path \(0-1-\cdots-(m-1)\), so they always admit a total order.

If \(a_1+z_0=0\), the constraint at the first path edge orients \(1\prec0\). The hub vertex 0 is then a sink in this oriented path and can be placed **last** in a topological ordering. The non-hub edges have color zero, and the last hub edge has either color, giving a favorable word \(0^{m-1}0\) or \(0^{m-1}1\).

If \(a_1+z_0=1\), the constraint orients \(0\prec1\). The hub is a source in the oriented path and can be placed **first**. Its edge color is \(h(z_1,\ldots,z_{m-1})\), independent of z0. Whenever this bit is zero, all m edges in this order have color zero.

For each assignment of the other m−1 starting bits, one of the two choices of z0 belongs to the first case; the second choice is also favorable whenever h equals zero. This proves (26). If h is nonconstant it has at least one zero, giving (25). If h is constant, the hub has no incoming dependency arcs, and the dependency graph is the directed path \(0\to1\to\cdots\to m-1\), which is acyclic. The existing acyclic-dependency theorem then gives \(A(g)=Q_m\). \(\square\)

**Corollary 23 (nonlinear one-branch SCC elimination).** In the sink-component paired-root gluing lemma, the sink component B can also be removed if, for each fixed outside assignment x, its fiber coloring can be relabeled into the displayed nonlinear single-branch form (24), with arbitrary offsets \(a_i(x)\) and hub function \(h_x\). Indeed,
\[
\boxed{|A(g_x)\cap\overline{A(g_y)}|\ge2
\quad\text{for every outside pair }x,y.}
\tag{28}
\]
Therefore paired-root existence for the full cube is equivalent to paired-root existence for the outside coloring, and the number of paired roots in the full cube is at least twice that of the outside cube.

*Proof.* Each fiber favorable-root set has cardinality at least \(2^{m-1}+1\) by Theorem 22, so any two sets, one of them antipodally complemented, intersect in at least two roots. Apply Lemma 18. \(\square\)

**Scope.** This settles a strongly connected dependency component with arbitrarily many additional incoming arcs into **one** hub, allowing any nonlinear Boolean hub color and arbitrary dependence of fiber offsets on outside bits. It does not cover components where the non-hub predecessor derivatives can vanish on some outside fibers, nor components with independent branching at two or more targets. Under these assumptions, the first unresolved local core must exhibit one of those latter features, rather than merely a nonlinear hub with many dependencies.


#### Arbitrary small terminal fibers: a sharp majority gluing theorem

This extends the prior paired-root fiber-overlap lemma to all fiber colorings on up to three dimensions, without an acyclicity, affine, or single-branch assumption.

For any binary coloring \(g\) of \(Q_b\), write \(A(g)\) for the roots supporting a full dimension-simple geodesic of color word \(0^*1^*\), with empty blocks permitted, and \(P(g)=A(g)\cap\overline{A(g)}\).

**Lemma 24 (sharp favorable-root majority in ranks two and three).** Every coloring of \(Q_2\) satisfies \(|A(g)|\ge3\). Every coloring of \(Q_3\) satisfies \(|A(g)|\ge6\). Both bounds are attained.

*Proof.* An unfavorable \(Q_2\) root has both incident edge bits one and both opposite edge bits zero, making the other three roots favorable.

For \(Q_3\), cube automorphisms reduce any two distinct roots with the same vertex parity to vertices \(0\) and \(3\) in binary integer notation. Label edge colors
\[
a=g(01),\ b=g(13),\ c=g(37),\ d=g(15),\
e=g(57),\ f=g(04),\ h=g(45).
\]
Here \(uv\) refers to the unoriented edge joining vertices \(u,v\). Three full color words from root \(0\) are \(abc,ade,fhe\), and three from root \(3\) are \(baf,bdh,ceh\). If both roots were unfavorable, each word would contain a descent \(10\).

If \(a=0\), the words \(abc,ade\) force \(b=d=1,c=e=0\), while \(bdh\) forces \(h=0\). Then \(ceh=000\), contradiction. If \(a=1\), the word \(baf\) forces \(f=0\), then \(fhe\) forces \(h=1,e=0\), \(ceh\) forces \(c=1\), and \(abc\) forces \(b=0\); but \(bdh=0d1\) is favorable. Therefore no two roots in the same vertex-parity class can be unfavorable. Each class has four vertices, so at most two roots are unfavorable. Taking the Cartesian product of the sharp \(Q_2\) coloring with a constant-colored one-dimensional factor gives six favorable \(Q_3\) roots, attaining the bound. \(\square\)

**Theorem 25 (majority-overlap gluing for arbitrary fibers).** Split \(Q_{a+b}=Q_A\times Q_B\). Suppose every \(A\)-edge color is independent of the \(B\)-bits, inducing a coloring \(f\) of \(Q_A\). Above each \(x\in Q_A\), permit an arbitrary \(B\)-fiber coloring \(g_x\). If \(|A(g_x)|\ge\mu>2^{b-1}\) for every \(x\), then
\[
\boxed{|P(F)|\ge (2\mu-2^b)|P(f)|.}
\tag{29}
\]
For arbitrary fibers of dimension \(b=1,2,3\), this specializes respectively to
\[
\boxed{|P(F)|\ge 2|P(f)|,\qquad
|P(F)|\ge 2|P(f)|,\qquad
|P(F)|\ge 4|P(f)|.}
\tag{30}
\]

*Proof.* Fix \(z\in P(f)\). Choose a full \(0^*1^*\) geodesic in \(Q_A\) from \(z\) to \(\bar z\), and another from \(\bar z\) to \(z\); let their zero-to-one seam vertices be \(v,v'\). By inclusion--exclusion,
\[
|A(g_v)\cap\overline{A(g_{v'})}|
\ge |A(g_v)|+|A(g_{v'})|-2^b
\ge 2\mu-2^b.
\]
For each root \(t\) in that intersection, insert a favorable full \(B\)-fiber geodesic from \(t\) at the seam \(v\), and another from \(\bar t\) at seam \(v'\). The two resulting full geodesics in \(Q_{a+b}\) start at \((z,t)\) and its antipode \((\bar z,\bar t)\), both have word \(0^*1^*\), and use every dimension once. Different pairs \((z,t)\) give different paired roots, yielding (29). In dimension one both fiber roots are favorable; in dimensions two and three Lemma 24 gives \(\mu=3,6\), proving (30). \(\square\)

**Corollary 26 (no small terminal dependency component in a minimum obstruction).** Form the directed dependency graph whose vertices are cube directions, with an arc \(j\to i\) whenever changing input bit \(j\) can change a direction-\(i\) edge bit. If an arbitrary edge coloring of least possible dimension has no paired root, then every terminal strongly connected component of its dependency graph has at least four directions.

*Proof.* A terminal component \(B\) has no outgoing dependence on directions outside \(B\). Thus the outer edge colors are independent of \(B\)-bits, and Theorem 25 applies. If \(|B|\le3\) and the outer block is nonempty, least-dimensionality supplies a paired root in the smaller outer coloring, so Theorem 25 forces one in the full cube. If the outer block is empty, the strict favorable-root majority in \(Q_{|B|}\) itself forces an antipodal pair of favorable roots. Both contradict minimality. \(\square\)

**Structural significance.** In the full unrestricted paired-root conjecture equivalent to NORI1 one dimension higher, terminal nonlinear dependency blocks of size one, two, or three can always be eliminated by monotone fiber-path insertion and antipodal overlap. This supplements the previous cycle-component and special branching-fiber results: a least-dimensional obstruction must contain a terminal strongly connected component of size at least four. No global closure is asserted for those larger components.


#### A full-component closure theorem for bounded and cyclic dependency blocks

The fiber gluing lemma is inductive over the **condensation DAG** of the directed dependency graph. The new nonlinear-hub theorem combines with the independently proved arbitrary-three-dimensional fiber majority to give the following all-dimensional closure result.

Call a strongly connected component B of the directed dependency graph **reducible** if at least one of the following holds:
(i) \(|B|\le3\), with no restriction on its internal edge-color functions;
(ii) its induced dependency digraph is a directed simple cycle, of any length;
(iii) after a cyclic relabeling \(B=\{0,\ldots,m-1\}\), all non-hub direction colors satisfy \(f_i(x)=x_{i-1}+a_i(x_{B^c})\) for \(1\le i<m\), with arbitrary Boolean outside-offset functions \(a_i\), while the hub edge color \(f_0\) is any Boolean function independent of bit 0 (possibly nonlinear in all other bits).

For each such B set
\[
L(B)=
\begin{cases}
2,&|B|=1\text{ or }2,\\
4,&|B|=3,\\
2^{|B|}-2,&B\text{ is a directed cycle of size }\ge4,\\
2,&B\text{ satisfies (iii) and is not already covered above}.
\end{cases}
\tag{31}
\]

**Theorem 27 (SCC-by-SCC paired-root closure).** If **every** strongly connected component of the directed dependency graph of an arbitrary binary cube-edge coloring f is reducible, then
\[
\boxed{|P(f)|\ge\prod_{B\in\operatorname{SCC}(\vec\Gamma(f))}L(B)>0.}
\tag{32}
\]
This holds regardless of how many nonlinear dependencies run *between* the components, and regardless of their directed-acyclic arrangement.

*Proof.* Choose a sink SCC B in the condensation DAG, and put A equal to the remaining dimensions. Because no arrow leaves B for A, the A-direction edge colors are independent of B-bits, inducing a smaller coloring on Q_A. For each outer assignment x, the induced B-fiber coloring g_x has: (i) at least 2,3,6 favorable roots respectively when \(|B|=1,2,3\), by Lemma 24; (ii) at most one unfavorable root if the global induced component is a simple directed cycle, because each fiber dependency graph is a subgraph of this cycle and Lemma 19 applies; or (iii) strictly more than half its roots favorable, by Theorem 22. Therefore for every x,y the intersection \(A(g_x)\cap\overline{A(g_y)}\) has at least L(B) roots. Lemma 18 gives \(|P(f)|\ge L(B)|P(f_A)|\).

Removing B from the global dependency graph leaves the induced graph on A, whose SCCs are the remaining original SCCs, since a sink has no outgoing arrows and cannot participate in another component. Apply induction until no dimensions remain. The empty cube has one paired root, proving (32). \(\square\)

**Corollary 28 (unrestricted small-SCC theorem).** In particular, **every** binary coloring of \(Q_d\) whose dependency SCCs all have size at most three has a paired root. Thus NORI1 holds for every upper-cube antipodally odd coloring whose bridge restriction is in this class, with no bound on d. The theorem is not a small-dimension test: d can be arbitrarily large and the quotient SCC network can have arbitrarily complicated interactions.

**Corollary 29 (irreducible local obstruction).** A paired-root counterexample, if one exists, must have a sink SCC of size at least four that is neither a directed simple cycle nor a uniformly active single-hub cycle with arbitrary hub nonlinearity. For a counterexample of minimum dimension, every sink component must have this property. The remaining problem is therefore internal branching or input-dependent loss of some non-hub predecessor interactions inside a sufficiently large terminal SCC, not interaction between already reducible components.

The proof is fully constructive given favorable-root witnesses for the smaller quotient problem and for the pertinent B-fiber roots: insert a B-geodesic at each of the two color-switch seams. It neither uses switch-count averaging nor requires tracking a global family of geodesics.

#### Fan-cycle fiber majority without uniform predecessor derivatives

The single-branch theorem above assumed that each non-hub predecessor derivative remains one in every outside fiber. That assumption can be removed: *every* subgraph of a directed cycle with arbitrary additional arcs into one hub has strict favorable-root majority.

Call a directed graph on \(\{0,\ldots,m-1\}\), \(m\ge2\), a **fan-cycle dependency graph** if its arrows belong to
\[
\boxed{\{i-1\to i:1\le i<m\}\ \cup\
\{i\to0:1\le i<m\}.}
\tag{33}
\]
The set of arrows into hub 0 is unrestricted; its edge color may be any Boolean function of bits \(1,\ldots,m-1\). Each non-hub edge color is of the form
\[
g_i(u)=a_i+\lambda_i u_{i-1},\qquad
a_i,\lambda_i\in\mathbb F_2,\quad 1\le i<m,
\]
with \(\lambda_i\) possibly zero. The function \(g_0\) is arbitrary and independent of its own bit.

**Lemma 30 (all fan-cycle colorings have favorable-root majority).** Every binary cube-edge coloring g whose directed dependency graph is a subgraph of (33) satisfies
\[
\boxed{|A(g)|>2^{m-1}.}
\tag{34}
\]
In particular for any two such colorings g,h (which may have different predecessor activations and unrelated hub functions),
\[
\boxed{|A(g)\cap\overline{A(h)}|\ge2.}
\tag{35}
\]

*Proof.* Every directed cycle of the dependency digraph contains hub 0, since after deleting hub 0 all remaining arrows strictly increase their labels. Thus there is at most one nontrivial strongly connected component B. If no such component exists the entire graph is acyclic, and the acyclic-dependency theorem gives \(A(g)=Q_m\).

Otherwise B consists of a prefix \(\{0,\ldots,s\}\), \(1\le s<m\), or of the full vertex set: for 0 to reach a vertex i it must traverse the successive predecessor arrows \(0\to1\to\cdots\to i\), and for i to lie in B there must be a return path to 0. All predecessor arrows inside B are therefore present. The induced coloring on any B-fiber, after fixing the bits outside B, is in the *uniformly active nonlinear single-hub* form of Theorem 22, so its favorable-root set has size strictly greater than \(2^{|B|-1}\).

In the condensation DAG repeatedly remove terminal **singleton** components as long as B is not terminal. A singleton terminal component is a sink direction, whose deletion duplicates neither restrictions nor losses in favorable-root density: the earlier seam-insertion theorem states that its favorable-root set is the smaller set times both bit values. This process terminates with B as a terminal component, possibly together with singleton components pointing into B. The remaining outside graph is acyclic, since B is its only nontrivial SCC. Hence its coloring f has **all roots favorable**.

For each outside starting root z choose a full favorable f-geodesic and its zero-to-one seam vertex x. Every root t favorable in the B-fiber g_x can be inserted at this seam, producing a full favorable geodesic starting at (z,t). Thus the full favorable-root set has cardinality at least
\[
|A(f)|\min_x|A(g_x)|
>2^{|B^c|}2^{|B|-1}
=2^{m-1}.
\]
Reinserting each previously deleted terminal singleton doubles the root count and retains the strict majority. This proves (34). By inclusion-exclusion, both \(A(g)\) and \(\overline{A(h)}\) contain more than half the \(2^m\) roots, so their intersection contains at least two vertices, proving (35). \(\square\)

**Theorem 31 (fan-cycle SCC elimination).** In the SCC-by-SCC closure theorem, replace condition (iii) with the strictly broader condition:

> The induced dependency digraph on the SCC is isomorphic to a subgraph of a fan-cycle graph (33), and its edge color functions may depend arbitrarily and nonlinearly on the outside bits.

If **every** SCC of the full directed dependency graph is either of size at most three, a directed cycle, or a fan-cycle component as above, then the coloring has a paired root. For every fan-cycle component B, the paired-root count gains a factor of at least two upon removal.

*Proof.* Pick a terminal SCC B. Its outside-edge colors are independent of B. At every fixed outside assignment, the internal fiber dependency digraph is a subgraph of the same fan-cycle pattern; some predecessor arrows may disappear, but Lemma 30 still gives favorable-root majority. Consequently any two B-fiber favorable-root sets intersect after complementing one, in at least two roots. Apply the paired-root fiber-gluing lemma and induct on the SCC condensation DAG. Components covered by the other two hypotheses were already handled in Theorem 27. \(\square\)

**Closure significance.** An internal SCC with only a single extra nonlinear dependency target on a directed cyclic spine cannot obstruct NORI1, *even when the other cycle derivatives switch off in some outside fibers*. Any remaining minimal obstruction must have a terminal SCC whose internal influence graph is not of this fan-cycle type (and is not covered by the small-component or ordinary-cycle theorems). This is an all-dimensional structural reduction; it does not rely on switch-count averages or search through low-order cubes.

#### Square-factorable fiber gluing with variable matchings

**Theorem.** Let F be any edge coloring of Q_{a+2r}, with dimension blocks A and B, where |B|=2r>=2. Assume A-edge colors do not depend on B-bits, inducing a coloring f of Q_A. For each outer vertex x, assume only that the B-fiber coloring g_x is a Cartesian product of arbitrary colored Q2 squares across a perfect matching M_x of B. The matchings M_x may vary arbitrarily with x.

For every paired root z of f, choose favorable full 0*1* paths from z and from its antipode, with seam vertices v_z,w_z. Then
|P(F)| >= sum_{z in P(f)} 2^{c(M_{v_z},M_{w_z})} >= 2|P(f)|,
where c(M,N) is the number of alternating-cycle components in the multigraph union of matchings M,N, including parallel pairs. In particular, paired-root existence always lifts through such an even-dimensional fiber block, regardless of the size of B.

*Proof.* The cross-orientation square-matching theorem in the separate Subsection "Cross-orientation root intersections for distinct square factorizations" proves that for any two square-factorable colorings g,g' with matchings M,N,
|A(g) intersect antipodal(A(g'))| >= 2^{c(M,N)}.
Each square factor forbids at most one of four root patterns for each monotone orientation; the combined forbidden-pattern constraints form disjoint alternating cycles, each admitting at least two assignments. Apply this to g_{v_z},g_{w_z}. Every root t in this intersection allows a favorable full B-geodesic from t at the first seam and from its antipode at the second seam. Inserting these B-geodesics into the two outer paths yields full dimension-simple 0*1* geodesics from (z,t) and its antipode. Counting distinct roots proves the inequality.

**Corollary.** A least-dimensional coloring without a paired root cannot contain a terminal dimension block of any even size whose fibers are all products of colored squares, even if their matchings depend on the outer vertex.

This result goes beyond majority-based gluing: for r>=3, a product of r sharp Q2 colorings has favorable-root density (3/4)^r below one half, yet cross-fiber intersection is forced by the cycle structure of two matchings. The outstanding closure problem is to extend the intersection principle to fibers with overlapping dependencies.

#### Nonlinear star feedback: a sharp three-quarter favorable-root theorem

Let Q_{m+1}, m>=2, have hub bit t and leaf bits x in F_2^m. Assume each leaf-direction edge has color g_i(t,x)=a_i+t for a fixed bit a_i, while the hub-edge color is g_0(t,x)=h(x) for an **arbitrary Boolean function** h. Thus every hub-to-leaf influence is present but feedback to the hub is unrestricted.

**Theorem (sharp star majority).** Such a coloring satisfies
\[
\boxed{|A(g)|\ge3\cdot2^{m-1},\qquad |P(g)|\ge2^m.}
\tag{38}
\]
Furthermore **one entire hub-bit slice** consists of favorable roots, and the opposite slice contains at most 2^{m-1} unfavorable roots. The first bound is sharp for every m.

*Proof.* For a root (t,x), put J={i:a_i+t=0}, I={i:a_i+t=1}. Before the hub flip, J-leaf steps are zero and I-leaf steps are one; afterward their colors reverse. For any subset U of J:
- If h(x xor 1_U)=0, use the dimension order U,hub,I,J\U. Its color word is 0^*1^*.
- If h(x xor 1_I xor 1_U)=1, use U,I,hub,J\U, likewise with word 0^*1^*.

Thus a root can fail only if h is constantly one on C_0=x+F_2^J and constantly zero on C_1=x+1_I+F_2^J. If I is empty the two subcubes coincide, so no root in that hub slice fails. If I is nonempty the involution x↦x+1_I exchanges C_0,C_1, and at most half of that hub slice can fail.

Suppose at least one root with hub bit t fails. Its two J-subcubes C_0,C_1 have opposite constant h-values. Reversing the hub starting bit swaps I and J. Failure in that opposite hub slice would require h to be constant on an I-subcube, which varies the I-bits while keeping J-bits fixed. But every such I-subcube meets **both** C_0 and C_1, so h assumes both values on it. Hence every root in the other hub slice is favorable. This proves at most 2^{m-1} unfavorable roots overall and the A bound. Since P=A intersect antipodal(A), inclusion-exclusion gives |P|>=2|A|-2^{m+1}>=2^m.

For sharpness take all a_i=0 and h(x)=x_1. All roots with t=0 are favorable. For t=1, any root with x_1=1 is unfavorable: every leaf step before the hub has color one and after the hub color zero, while the hub color switches from one to zero when leaf 1 is traversed. If leaf 1 is before the hub, a zero-colored hub follows a one-colored leaf; if after the hub, a zero-colored leaf follows a one-colored hub. Thus 2^{m-1} roots fail, meeting the bound. QED.

**Corollary (star SCC cross-fiber gluing).** Suppose a terminal dependency SCC B has active hub-to-leaf derivatives throughout every fixed outside fiber, but arbitrary and possibly nonlinear leaf-to-hub feedback and outside-dependent offsets. Its fiber favorable sets each contain at least three quarters of Q_B. Any two such sets after complementing one intersect in at least 2^{|B|-1} roots. The paired-root fiber gluing theorem therefore gives
\[
\boxed{|P(F)|\ge2^{|B|-1}|P(f_A)|,}
\tag{39}
\]
and this terminal SCC cannot cause a paired-root failure.

The theorem is an all-dimensional closure result for a branching SCC with unrestricted nonlinear feedback at one hub. It does not yet cover multi-level branching or disappearing hub-to-leaf derivatives in some outside fibers.

#### Partial-matchings remove fiber blocks in every dimension

**Lemma (path-cycle feasibility).** Take a union H of two partial matchings on a finite set of binary variables. On each edge forbid at most one of four assignments to its endpoints, allowing independent constraints on parallel edges. Then the system has at least 2^{c(H)} satisfying assignments, where isolated variables count as components.

*Proof.* Every component of H is a path, an even cycle (possibly a parallel-edge two-cycle), or a singleton. On a path, choose the initial bit in either of two ways and greedily choose subsequent bits; at most one next bit is forbidden, hence both initial choices extend. On a cycle, delete one constraint, and similarly build two assignments having different first bits. The removed constraint, incident to that first variable, can invalidate at most one, so a satisfying assignment exists. If a cycle had a unique satisfying assignment, each single-variable flip would have to violate an incident constraint. Each currently satisfied constraint can prohibit flipping at most one endpoint, since only one binary endpoint pair is forbidden. A cycle has as many constraints as variables; hence each constraint would protect one different vertex and its forbidden pair would differ from the solution pair in one bit. Complement every bit: each edge pair now differs from the original solution in two bits and therefore violates none of those constraints, contradicting uniqueness. Each component thus contributes at least two assignments, and components multiply. QED.

**Corollary (changing-partial-matching fiber gluing).** In the preceding variable-matching fiber theorem, one may allow a B-fiber of *any dimension*, decomposed as a Cartesian product of arbitrarily colored Q2 squares and independent Q1 edges. The factorization and partial matching M_x may vary with the outer vertex x. For every paired root z of the outer coloring, let v_z,w_z be seam vertices of two favorable outer paths. If c_z is the number of components of M_{v_z} union M_{w_z}, including isolated directions, then
|P(F)| >= sum_{z in P(f)} 2^{c_z} >= 2|P(f)|.

*Proof.* Every colored Q2 square excludes at most one of four favorable-root patterns; every colored Q1 factor excludes none. The intersection A(g_{v_z}) intersect antipodal(A(g_{w_z})) is the solution set of forbidden-pattern constraints on the union of the two partial matchings. By the lemma it has at least 2^{c_z} members. Insert full favorable fiber paths from a compatible root and its antipode into the respective two outer paths at their zero-to-one seams. Each resulting full path uses every direction once. Summing gives the inequality. QED.

This yields an all-dimensional terminal-block elimination rule for variable square and singleton decompositions. It applies even when fiber favorable-root densities are exponentially smaller than one half. The unresolved case requires overlapping dependencies not representable by such partial matchings.

#### Star-root majority persists when hub-to-leaf dependencies disappear

The three-quarter favorable-root theorem is stable under arbitrary deletion of hub-to-leaf dependency arrows, a feature needed when passing to fibers of a larger coloring.

**Theorem (full star-pattern three-quarter bound).** Let a colored cube have hub bit t and m leaf bits \(x_1,\ldots,x_m\). Assume its direction-i leaf-edge bit is
\[
\boxed{g_i(t,x)=a_i+\lambda_i t,\quad i=1,\ldots,m,}
\]
where \(a_i,\lambda_i\in\mathbb F_2\) are arbitrary, and the hub-edge bit \(g_0(t,x)=h(x)\) is any Boolean function. Then, for every m>=1,
\[
\boxed{|A(g)|\ge\tfrac34 2^{m+1},\qquad
|P(g)|\ge\tfrac12 2^{m+1}.}
\tag{40}
\]
The three-quarter factor is sharp. In particular any two such colorings g,g' of the same dimension satisfy
\[
\boxed{|A(g)\cap\overline{A(g')}|\ge2^m.}
\tag{41}
\]

*Proof.* Partition the leaves into the active set T={i:lambda_i=1} and the inactive set I={i:lambda_i=0}. The inactive-direction edge colors are fixed constants a_i, independent of the hub and the active-leaf bits. Treat Q_I as an outer cube and Q_{\{0\}\cup T} as the inner fiber. The outer coloring has every starting root favorable: traverse its zero-colored dimensions first and its one-colored dimensions afterward.

For each fixed outside leaf assignment y, the inner fiber has all active hub-to-leaf arrows and an arbitrary hub function \(h_y\). If T is nonempty, the three-quarter theorem applies to this fiber (including the elementary one-leaf case, which is a colored Q2 with at least three favorable roots). If T is empty, the inner fiber is a single edge and both its roots are favorable. Hence every inner fiber has at least three quarters of its roots favorable.

For every outer starting root z, choose a favorable outer geodesic with seam vertex y. Insert any favorable full inner-fiber path beginning at a chosen inner root into that seam; this produces a full favorable path in the combined cube. Thus the favorable-root count is at least
\[
2^{|I|}\cdot\tfrac34 2^{|T|+1}
=\tfrac34 2^{m+1}.
\]
Antipodal inclusion-exclusion gives the P bound. Applying the same count to any two colorings and complementing one gives (41). Sharpness follows from the active-star instance with all offsets zero and hub function h(x)=x_1. \(\square\)

**Corollary (terminal star SCC closure without uniform activation).** A terminal dependency SCC can be removed by paired-root gluing whenever its internal dependency graph is a subgraph of a bidirected star (all arrows join the hub to leaves), even if individual hub-to-leaf derivatives vanish on some fixed outside fibers and all leaf-to-hub feedback is nonlinear. Every such fiber has at least three quarters favorable roots, so the paired-root lower bound gains a factor of at least \(2^{|B|-1}\) upon removal.

This eliminates the variable-activation caveat from the star SCC result. A minimal obstruction must contain a terminal SCC whose internal directed graph is neither a fan-cycle nor a bidirected-star subgraph nor one of the other reducible component types.

#### Arbitrary rooted-tree feedback: three-quarter favorable-root theorem

Let T be a rooted tree on dimensions 0,...,m with parent map p(i), and color edges by
\[
f_0(x)=h(x_1,\ldots,x_m),\quad f_i(x)=a_i+\lambda_i x_{p(i)}\quad(i>0),
\]
where h is an arbitrary Boolean function and \(a_i,\lambda_i\in\mathbb F_2\).

**Lemma (monochromatic branch).** If all lambda_i=1, any branch B hanging off hub 0 can be traversed using only color \(a_c+t\), where c is its top direction and t is the current hub bit.

*Proof.* The top edge c has color k=a_c+t. For every other descendant i, obtaining color k requires [p(i) before i]=k+a_i+x_{p(i)}, using the initial B-bits x. These relations orient the edges of the tree B and therefore admit a total order. Such an order traverses every B direction in color k. QED.

**Theorem (active tree).** If every lambda_i=1 then
\[
\boxed{|A(f)|\ge\tfrac34 2^{m+1},\quad |P(f)|\ge\tfrac12 2^{m+1}.}
\]

*Proof.* Partition the nonhub dimensions into the disjoint child branches B_1,...,B_r. The full-branch toggles 1_Bj generate an r-dimensional subspace of F_2^m. Partition leaf-root assignments into cosets of that subspace. In each coset choose representative y and let s_j encode whether branch B_j is toggled. Define a macro-star coloring on Q_{r+1} by
\[
g_j(t,s)=a_{c_j}+t,\quad
g_0(t,s)=h(y+\sum_j s_j1_{B_j}),
\]
where c_j is the first direction of branch B_j. The established nonlinear-star theorem gives a favorable full 0*1* macro-geodesic from at least three quarters of the macro-roots. Expand each macro-leaf step into a monochromatic full traversal of B_j using the lemma. Each expansion has the color of the replaced step and flips every bit of that branch, so the new full word is still 0*1*. At the hub step the leaf bits agree with the macro assignment, hence its edge color is also preserved. Thus every favorable macro-root gives a favorable original root. Sum over the disjoint cosets to obtain the bound on A. Inclusion-exclusion for P=A intersect antipodal(A) gives the other bound. QED.

**Theorem (inactive interactions).** The same bounds hold for arbitrary lambda_i in F_2.

*Proof.* In the dependency digraph, nonhub arcs go outward along the parent tree and all other arcs enter hub 0. Therefore every directed cycle contains hub 0 and there is at most one nontrivial SCC B. If the whole digraph is acyclic, every root is favorable. Otherwise B consists of hub 0 and an outward-rooted subtree in which every internal parent arc is active, since each vertex of B must be reached from hub along its unique ancestral path. Outside B, every SCC is a singleton and the induced graph is acyclic.

Remove terminal singleton SCCs by the proven one-direction seam-insertion identity, which duplicates favorable roots. Once B becomes terminal, the remaining outside coloring has acyclic dependencies, so all outer roots are favorable. For each such root choose a favorable outer path and its zero-to-one seam. At that seam the B-fiber has active rooted-tree form; the preceding theorem guarantees favorable B-paths from at least three quarters of its roots. Insert each such B-path at the outer seam. At least three quarters of combined roots are favorable. Reinsert removed singleton directions, preserving this fraction. The antipodal paired-root bound follows by inclusion-exclusion. QED.

**Corollary (SCC elimination).** Any terminal dependency SCC whose internal arcs lie in an outward-rooted tree plus arbitrary feedback arrows to the root can be removed through paired-root fiber gluing. Fixed outside assignments may deactivate parent arrows, and root-edge color functions can vary arbitrarily. Every fiber is still at least three quarters favorable; hence any two fibers have at least half their roots in the intersection of one favorable set with the antipodal image of the other.

This proves the all-dimensional rooted-tree feedback majority conjecture; its three-quarter factor is sharp over the class, as witnessed by the nonlinear star. The remaining hard cores require more than one nonlinear feedback target or overlapping feedback circuits.

#### Quantitative SCC root count and two-branch necessary condition

The rooted-tree feedback theorem extends across the condensation DAG of any directed dependency graph by the paired-root fiber gluing lemma.

**Theorem (exponentially many paired roots).** Let f be a binary cube-edge coloring of Q_d. Suppose every nontrivial SCC B of its directed dependency graph has an internal graph whose arcs lie in an outward rooted tree together with arbitrary arcs entering the root of that tree. Let k denote the number of SCCs of size at least two. Then
\[
\boxed{|P(f)|\ge 2^{d-k}>0.}
\tag{44}
\]
The bound is sharp, for example when f is a Cartesian product of k copies of the sharp two-dimensional coloring and d−2k independent one-dimensional factors. Arbitrary nonlinear dependencies **between** the SCCs do not affect the bound.

*Proof.* Remove sink SCCs one at a time. If B is a singleton, its fiber has both starting roots favorable, and paired-root seam gluing multiplies the count of paired outside roots by two. If |B|=s>=2, each fixed-outside B-fiber has at least three quarters of its roots favorable, by the rooted-tree theorem. For any two outside seam vertices, the corresponding fiber favorable sets intersect after antipodal complement in at least
\[
2\cdot\tfrac34\,2^s-2^s=2^{s-1}
\]
roots, so seam gluing multiplies the paired-root count by at least \(2^{s-1}\). The condensation is acyclic and the outer edge colors are independent of the terminal component's bits, so the argument iterates. Starting from the empty cube with one paired root, multiplication yields \(2^{\sum_B |B|-\#\{B:|B|\ge2\}}=2^{d-k}\). For sharpness, each independent sharp Q2 factor has two paired roots and each Q1 factor has two; their Cartesian product has \(2^{d-k}\) paired roots. \(\square\)

**Lemma (one internal branching target is reducible).** Let D be a finite strongly connected loopless digraph with at least two vertices. If at most one vertex has indegree greater than one, then D is a directed cycle or an outward rooted spanning tree together with additional arrows entering its root.

*Proof.* Every vertex of a nontrivial strongly connected digraph has indegree at least one. If each has indegree one, strong connectivity forces a single directed cycle. Otherwise let v be the sole vertex of indegree greater than one. Every other vertex u has a unique predecessor p(u). A directed path from v to u exists by strong connectivity; its final step must be p(u)->u. Thus the shortest-path distance from v strictly increases along every arrow p(u)->u, so these n−1 arrows form an outward arborescence rooted at v. All further arrows enter v, since no other vertex has a second incoming arrow. \(\square\)

**Corollary (irreducible minimal obstruction).** In a least-dimensional counterexample to paired-root existence, **every terminal SCC** must have at least four vertices and at least **two distinct vertices of internal indegree at least two**. Otherwise that component is a singleton, a small arbitrary SCC already handled by the three-dimensional majority theorem, or a rooted-tree feedback component removable by the theorem above. Hence any first obstruction must contain multiple independent branching targets inside one feedback-connected component.

These constraints are structural and dimension-uniform; they do not depend on mean switch counts or enumeration of small cubes.

#### Multi-hub forest compression: root-wise lift preserving antipodal pairs

The macro-star proof generalizes to **any number of nonlinear feedback hubs**. Its value is that long tree branches can be collapsed without losing dimension-simple geodesic witnesses or paired-root witnesses.

Choose a subset H of k hub dimensions in a cube Q_{k+m}. Partition the remaining m dimensions into vertex-disjoint rooted branch trees \(B_1,\ldots,B_r\). The top direction \(c_j\) of B_j has a hub parent \(h(j)\in H\). Suppose for every nonhub direction i the edge color is
\[
\boxed{f_i(x)=a_i+x_{p(i)},}
\tag{45}
\]
where \(p(i)\) is either another direction in B_j or, for its top direction, the hub h(j). Each hub-direction edge color may be any Boolean function of all cube bits except its own.

Let \(L\subseteq\mathbb F_2^m\) be the span of the disjoint branch-toggle vectors \(\mathbf1_{B_1},\ldots,\mathbf1_{B_r}\). Partition nonhub starting assignments into cosets \(y+L\). For one coset, encode a root by hub bits \(t\in\mathbb F_2^k\) and branch bits \(s\in\mathbb F_2^r\), representing the original root \((t,y+\sum_j s_j\mathbf1_{B_j})\).

Define its **compressed coloring** \(g_y\) on \(Q_{k+r}\) as follows: a macro-leaf direction j has color
\[
\boxed{g_{y,j}(t,s)=a_{c_j}+t_{h(j)},}
\]
and a hub direction i has the color of the corresponding original hub edge evaluated at the represented original vertex.

**Theorem (multi-hub monotone lifting).** Every full \(0^*1^*\) macro-geodesic of \(g_y\) lifts to a full \(0^*1^*\) geodesic of f at the represented root. Moreover the antipodal map acts **within each coset** by \((t,s)\mapsto(\bar t,\bar s)\), and consequently
\[
\boxed{
|A(f)|\ge\sum_{y+L}|A(g_y)|,\qquad
|P(f)|\ge\sum_{y+L}|P(g_y)|.}
\tag{46}
\]
In particular if all macro-hub colorings in this class satisfy the paired-root assertion, then all their arbitrary rooted-tree expansions satisfy it as well.

*Proof.* Expand each macro-leaf traversal into the monochromatic full geodesic in its branch, using the tree-ordering lemma established above. The top edge has color \(a_{c_j}+t_{h(j)}\) and the target color at every deeper edge is imposed by orienting its parent-child relation, an acyclic tree. Thus all expanded branch edges have the macro-step color. Since the branch is traversed in full, its binary starting assignment changes by \(\mathbf1_{B_j}\), precisely the change of its macro-bit s_j. Hub edges occur at the represented original states and retain their macro colors. All dimensions are used once and replacing a macro color by a nonempty block of the same color preserves the monotone word.

The branches partition all nonhub dimensions, so full complementation of the represented root is
\[
(\bar t,\bar y+\sum_j s_j\mathbf1_{B_j})
=(\bar t,y+\sum_j(1-s_j)\mathbf1_{B_j}).
\]
It therefore corresponds to \((\bar t,\bar s)\) in the **same** coset. Each favorable macro-root and each paired macro-root lifts to an original root of the corresponding kind; roots from distinct cosets remain distinct. Summing gives (46). \(\square\)

**Closure use.** With one hub, the compressed coloring is the nonlinear star, yielding the three-quarter theorem. With two hubs, every arbitrary-depth forest attached to those hubs reduces to the **two-hub star** problem: two arbitrary nonlinear hub functions and macro-leaf colors each depending on one assigned hub. The latter is the first unproved structurally richer target; two-root interaction, rather than tree depth, carries the remaining difficulty. This theorem is a reduction, not a proof of the two-hub assertion.

#### Two branching targets: compression to a two-hub star

**Lemma (unique-predecessor forest).** Let D be a finite strongly connected loopless digraph with at least two vertices. Let H be the vertices of indegree greater than one, and assume H is nonempty. Every cycle meets H, and the arrows entering vertices outside H form outward-rooted trees attached to H.

*Proof.* Every vertex outside H has a unique predecessor. A cycle contained entirely outside H already uses the sole incoming arrow of every vertex on it, so no path from H could enter it, contradicting strong connectivity. Thus the subgraph outside H is acyclic. Following predecessors backward from any other vertex must terminate at H, or else produce a cycle outside H. Those unique predecessors define a forest rooted at H. All additional arrows enter H. QED.

**Theorem (two-hub compression).** Suppose a binary cube-edge coloring f has a strongly connected directed dependency graph with two vertices of indegree greater than one. Every other dimension i has one incoming dependency from a predecessor p(i), so its edge color is
\[
\boxed{f_i(x)=a_i+x_{p(i)}.}
\]
All such dimensions form disjoint rooted tree branches attached to the two hub dimensions. Each hub edge color may be an arbitrary nonlinear Boolean function of every other bit. The previous multi-hub macro-forest theorem therefore constructs, for each coset of branch-toggle vectors, a two-hub star coloring g whose favorable and paired macro-root sets lift to corresponding root sets of f. Hence a universal paired-root theorem for two-hub stars would settle this full class of arbitrary-size, arbitrary-depth strongly connected dependency colorings.

*Proof.* Apply the unique-predecessor lemma to the two hubs. A Boolean edge color depending on only one other bit, with an active dependency, has the indicated affine form. Compress each branch to one macro-leaf, using monochromatic tree traversal, and apply the previously published macro-forest lifting theorem. The paired-root correspondence respects antipodal complementation within each coset. QED.

**Corollary (minimal graph excess).** Any least-dimensional paired-root counterexample has a terminal SCC with at least four vertices and at least two vertices of indegree greater than one. Therefore that SCC has at least s+2 arrows if it has s vertices. If it has s+2 arrows, it has two indegree-two branching targets and all other vertices have indegree one; hence the two-hub reduction above applies. The minimal directed graph excess is thus a two-hub problem, independent of the lengths of its intervening dependency paths.

**Next conjecture (unproved).** For every coloring of Q_{r+2} with two hub bits t_0,t_1, with leaf j edge color \(a_j+t_{\eta(j)}\), \(\eta(j)\in\{0,1\}\), and arbitrary nonlinear edge colors in the two hub directions, does
\[
\boxed{|A(g)|>2^{r+1}}
\]
always hold? This favorable-root strict-majority conjecture would permit paired-root gluing of every terminal SCC with two branching targets. A candidate stronger bound is \( |A(g)|\ge (9/16)2^{r+2}\), attained by a product of two sharp star gadgets, but it is not yet established.

#### Rootwise orientation coverage for rooted-tree feedback

The rooted-tree majority theorem has a stronger pointwise companion. Write \(A_0(f)\) and \(A_1(f)\) for roots admitting full geodesics with words \(0^*1^*\) and \(1^*0^*\), respectively.

**Theorem (hub-first orientation at every prescribed root).** Suppose
\[
f_0(x)=h(x_1,\ldots,x_m),\qquad
f_i(x)=a_i+\lambda_i x_{p(i)}\quad(i>0),
\]
where the parent relations form a tree rooted at \(0\), the hub function \(h\) is arbitrary, and \(a_i,\lambda_i\in\mathbb F_2\). For every root \(z\), put \(q=h(z_1,\ldots,z_m)\). There is a full geodesic starting with direction \(0\) whose word is
\[
\boxed{q^*(1-q)^*.}
\]
In particular,
\[
\boxed{A_0(f)\cup A_1(f)=V(Q_{m+1}).}
\]

*Proof.* Traverse the hub edge first, obtaining color \(q\) and fixing the hub bit at \(1-z_0\). Delete the hub from the parent tree and remove each remaining parent link whose child has \(\lambda_i=0\). The resulting components are rooted trees. The top direction \(c\) of each component has a fixed edge color \(k_c\): it is \(a_c+\lambda_c(1-z_0)\) when its parent is the hub, and \(a_c\) when its parent link was removed.

Every other direction \(i\) in that component has \(\lambda_i=1\). To give its edge color \(k_c\), impose the precedence condition
\[
[p(i)\text{ occurs before }i]=k_c+a_i+z_{p(i)}.
\]
These conditions orient the component's tree edges. Every orientation of a tree is acyclic, so a total order satisfying them exists. Traversing the component in this order colors all its steps \(k_c\). Its edge colors are independent of bits in other components: removed parent links have coefficient zero.

Traverse all components of color \(q\), followed by all components of color \(1-q\). Together with the initial hub edge, this gives the required full dimension-simple word. \(\square\)

**Corollary (one branching target in a strongly connected dependency graph).** If a cube coloring has a strongly connected directed dependency graph with at most one vertex of indegree greater than one, every root admits at least one monotone orientation.

*Proof.* A one-direction coloring is constant and every root is paired. For a strongly connected graph with at least two vertices and no branching target, the graph is a directed cycle; designate any vertex as the hub. With one such vertex, the unique-predecessor lemma gives an outward rooted tree with all remaining arrows entering that hub. Each nonhub edge-color function depends on its sole predecessor and has the form \(a_i+x_{p(i)}\). Apply the theorem. \(\square\)

**Restoration consequence.** The endpoint restoration theorem in the gauge-criticality Subsection produces an affected zero face with two prescribed opposite roots admitting neither orientation. Such a face, and any isolated factor carrying its sole exceptional edge, cannot have rooted-tree feedback form. If the surviving defect factor is strongly connected, it must have at least two distinct internal branching targets. This applies the rooted-tree argument at the prescribed restoration corners, without transporting a paired root from elsewhere in the face.

The hub-first construction was additionally checked on 640 sampled rooted-tree instances in dimensions two through nine, allowing inactive parent links. The proof above establishes the statement in every dimension.


**Audit of the graph reductions.** The unique-predecessor forest lemma assumes a nonempty branching set \(H\). Without this hypothesis a directed cycle has \(H=\varnothing\) and remains cyclic after deleting \(H\), so the formerly unrestricted statement was false. The one-target graph classification assumes at least two vertices; singleton strongly connected graphs are handled separately. The two-hub compression and all nontrivial-component applications satisfy these hypotheses. The hub-first rooted-tree theorem and its critical-face consequence are unchanged.


#### Four-type macro-branch reduction for arbitrary two-hub feedback

Let f be a coloring of the undirected edges of Q_(m+2) with hub bits t_0,t_1 and leaves indexed by j, such that each leaf-edge bit has form f_j(t,x)=a_j+t_(eta(j)), where eta(j) is 0 or 1 and a_j is 0 or 1. The hub edge-bit functions are arbitrary Boolean functions of all bits other than their own hub bit.

Group leaf directions by their pair (eta(j),a_j). There are at most four nonempty classes B_1,...,B_r. The disjoint indicator vectors 1_(B_i) generate a subspace L of F_2^m of rank r. For each coset y+L write a represented root as
\[
(t,s)\longmapsto(t,y+\sum_i s_i1_{B_i}).
\]
Define a compressed coloring g_y on Q_(r+2) by giving each macro leaf the color a_i+t_(eta(i)) and both hub directions the colors of f at the represented vertex. These are well-defined undirected edge colors.

**Theorem (four-type compression).** The two-hub favorable and paired-root counts satisfy
\[
\boxed{|A(f)|\ge\sum_{y+L}|A(g_y)|,\qquad
|P(f)|\ge\sum_{y+L}|P(g_y)|.}
\]
Every favorable or paired macro-root expands to the corresponding kind of original root, and in particular every two-hub star in arbitrary dimension reduces to structured stars on at most six directions.

*Proof.* Expand a macro leaf step into a consecutive traversal of all original dimensions in its type class. Those edges have the macro color because no controlling hub is flipped during expansion. The expanded step flips the entire class, retaining the represented macro state; hub steps inherit their original colors. Hence expanding a full dimension-simple nondecreasing-color word gives a full dimension-simple nondecreasing-color word. The classes partition the nonhub directions, so taking the antipode of a represented root acts inside the same coset by (t,s) -> (1-t,1-s). Thus paired macro-roots also lift. Cosets are disjoint and partition the original vertex set. QED.

If the conjectural sharp nine-sixteenths favorable-root lower bound holds for every reduced star with r<=4 and one leaf of each present type, then it holds for all two-hub stars in all dimensions. This is a *reduction*, not a proof of that numerical bound.

**Multi-hub version (parameterized kernel).** Suppose a strongly connected dependency digraph has k>=1 vertices of indegree at least two. Every other vertex has a unique predecessor and belongs to an outward-rooted tree attached to a branching hub: a cycle avoiding the hubs would have no incoming arrows and contradict strong connectivity. Each nonhub edge color is an affine function of its predecessor bit. First collapse each entire branch using its monochromatic tree-ordering traversal, then merge branches with the same hub parent and the same leading-edge offset. There are at most two macro leaves per hub, so one obtains a coloring with at most 3k directions on every coset of branch-toggle vectors. Favorable and paired macro-roots lift to favorable and paired roots of the original coloring. The hubs retain arbitrary nonlinear color functions. Thus the dependency-core complexity can be reduced to at most 3k directions, although k itself need not be bounded.

**Remaining target.** For k=2 this yields a bounded, structured six-direction theorem. Any proof of strict favorable-root majority in that class would establish the corresponding result for all two-hub stars, with arbitrary numbers of repeated leaf types and arbitrary nonlinear hub feedback. The reduction does not claim this majority theorem or NORI1.


#### Nonlinear antipodal two-direction deletion and fixed-rank kernel improvement

Let c_k(x) be the color of the undirected direction-k cube edge incident at x, independent of bit x_k. Assume c_k(\bar x)=1+c_k(x) for every k.

**Theorem (nonlinear twin-pair restoration).** Suppose distinct i,j satisfy
\[
c_k(x+e_i+e_j)=c_k(x)\ (k\ne i,j),\quad
c_i(x+e_j)=c_i(x),\quad c_j(x+e_i)=c_j(x)
\]
for all vertices x. Restrict to the face x_i=x_j=0 to obtain c' on Q_(n-2). Then c' is antipodally odd, and any monochromatic full antipodal geodesic in c' lifts to one in c of the same color.

*Proof.* Write y for the other bits, u,v for the selected bits. The assumptions yield c_k(y,u,v)=g_k(y,u+v) for k outside {i,j}, c_i=h_i(y), and c_j=h_j(y), for arbitrary Boolean functions. Full antipodal oddness gives g_k(\bar y,p)=1+g_k(y,p) and h_i(\bar y)=1+h_i(y), h_j(\bar y)=1+h_j(y). Thus c'_k(y)=g_k(y,0) is odd.

Take a monochromatic complete c' path of color b from y to \bar y. Reverse its traversal if necessary, choosing its start s with h_i(s)=b (possible because h_i(\bar y)=1+h_i(y)). If h_j(s)=b, start at (s,0,0), traverse i and j consecutively to (s,1,1), then follow the smaller path. The selected edges and the smaller edges all have color b; along the smaller path u+v=0. The destination (\bar s,1,1) is the antipode.

If h_j(s)=1+b, start at (s,1,0), traverse i to (s,0,0), follow the smaller path to (\bar s,0,0), then traverse j to (\bar s,0,1). The first selected edge has color h_i(s)=b; the last has h_j(\bar s)=1+h_j(s)=b. The smaller path again runs with u+v=0. Both resulting full paths use every direction once. QED.

**Lemma (unread-direction deletion).** If c_k(x+e_i)=c_k(x) for all k different from i, then deleting i preserves oddness and every smaller monochromatic full geodesic lifts by inserting i at its beginning. Choose the path's starting endpoint so the color of the i-edge matches the monochromatic color; oddness gives opposite i-edge colors at the two possible endpoints.

**Corollary (affine column-twin elimination).** For an affine odd coloring c_i(x)=(Lx)_i+a_i with L_ii=0 and L1=1, equality of columns Le_i=Le_j alone suffices for pair deletion. The equal columns imply L_ij=L_ji=0 and invariance of all other direction colors under toggling i and j together. No equality of rows or offsets is required.

**Corollary (finite rank kernel).** Any such rank-r matrix, r>=2, can be reduced by zero-column and repeated-column-pair deletions to a row-odd zero-diagonal matrix of rank at most r with at most
\[
\boxed{2^r-2}
\]
remaining directions. Each deleted dimension or pair can be restored along any smaller monochromatic full path.

*Proof.* All deletions preserve odd row sums and zero diagonal. In the final matrix, columns are distinct and nonzero. If its rank is s<=r, choose a basis U of s independent odd rows and let t_i=Ue_i; these are distinct nonzero vectors in F2^s. Their XOR equals U1=1_s, which is nonzero. For s>=2 the XOR of all 2^s-1 nonzero vectors is zero. Therefore some nonzero vector is absent, and at most 2^s-2<=2^r-2 columns remain. The nonempty rank-one odd zero-diagonal case is impossible. QED.

This improves the earlier fixed-rank bound 2^(r-1)(2^(r-1)-1): rank three now needs at most six residual dimensions, and rank four at most fourteen. The first theorem also eliminates nonlinear symmetric dimension pairs from any least-dimensional hypothetical NORI1 obstruction.



#### Bounded global Boolean influence rank forces nonlinear twin reduction

The nonlinear pair deletion theorem admits a dimension-free structural consequence based on the binary rank of the full Boolean-derivative profile matrix.

For an arbitrary antipodally odd cube-edge coloring c, define the global derivative matrix J(c) over F2. Its columns are indexed by cube directions i; its rows are indexed by pairs (k,x) with k a direction and x a cube vertex. Put
\[
J(c)_{(k,x),i}=c_k(x+e_i)+c_k(x)=\partial_i c_k(x).
\]
Its diagonal direction derivatives vanish because undirected edge colors do not depend on their own direction bit. Write \(r(c)=\operatorname{rank}_{F2}J(c)\).

**Lemma (derivative twins imply antipodal twins).** If column i of J(c) is zero, direction i is unread and can be deleted by the preceding one-direction theorem. If columns i,j agree, then i,j satisfy every hypothesis of the nonlinear antipodal pair-deletion theorem and can be deleted together.

*Proof.* A zero column says \(\partial_i c_k(x)=0\) for every k,x, so no other direction color reads bit i. If columns i,j agree, then for every k,x
\[
c_k(x+e_i)=c_k(x+e_j).
\]
Replace x by x+e_i to obtain \(c_k(x)=c_k(x+e_i+e_j)\), giving simultaneous-flip invariance for all other directions. For k=i, the self-derivative \(\partial_i c_i\) vanishes, so column equality forces \(\partial_j c_i=0\). Similarly \(\partial_i c_j=0\). These are the remaining pair-deletion conditions. \(\square\)

**Theorem (nonlinear rank kernel).** If \(r(c)=r\), repeated unread-direction and equal-derivative-column pair deletions produce an antipodally odd coloring of a cube with at most
\[
\boxed{2^r-1}
\]
directions, such that **every** monochromatic full geodesic of the residual coloring lifts to one in c.

*Proof.* Each deletion is justified by the preceding lemma and the nonlinear restoration theorem. Its induced coloring is the restriction of the remaining edge-color functions to a face. The new global derivative matrix is obtained by retaining some original direction columns and projecting their entries onto the smaller set of remaining rows and face vertices. Hence its rank never exceeds r. Continue until every remaining derivative column is nonzero and the columns are pairwise distinct. A binary vector space of dimension at most r has only 2^r-1 distinct nonzero vectors, proving the bound. Reversing the sequence of deletions lifts every residual monochromatic full geodesic to the original coloring. \(\square\)

**Corollary (minimum-obstruction derivative-rank bound).** A least-dimensional odd coloring of \(Q_n\) without any monochromatic full antipodal geodesic would necessarily satisfy
\[
\boxed{r(c)\ge\lceil\log_2(n+1)\rceil.}
\]
Indeed a minimal obstruction has neither an unread dimension nor equal derivative columns, so all n columns of J(c) are distinct nonzero vectors and n<=2^{r(c)}-1.

**Scope and closure route.** This works for arbitrary nonlinear Boolean edge-color functions, not merely affine readers. It proves an all-dimensional induction reduction for every class with a uniform bound on global derivative-column rank. The stronger affine kernel bound 2^r-2 uses the extra constant-matrix odd-row identity and need not hold for nonlinear derivatives. The remaining unrestricted obstruction requires derivative-column diversity large enough to prevent both unary deletion and paired symmetry restoration.



#### Closure transfer from finite dimensions to bounded nonlinear derivative rank

The nonlinear derivative-column deletion theorem yields a useful quantified induction principle.

**Theorem (finite-dimension closure transfer).** Fix \(D\ge2\) and suppose the ordinary **edge-coloring NORI1** assertion is established for every antipodally odd coloring of \(Q_d\), for each \(2\le d\le D\). Then:
1. every antipodally odd coloring of arbitrary dimension whose global Boolean derivative-column rank is \(r\) with \(2^r-1\le D\) has a monochromatic full antipodal geodesic;
2. every affine antipodally odd coloring of arbitrary dimension whose reader matrix has rank \(r\ge2\) with \(2^r-2\le D\) has such a geodesic.

*Proof.* In the first case, apply nonlinear unread-direction and twin-pair deletions until the residual cube has at most \(2^r-1\le D\) directions. The reduced coloring remains antipodally odd, and its derivative rank has not increased. By the assumed finite-dimensional edge-coloring NORI1 theorem, it has a monochromatic full geodesic; restore all deleted directions to lift that path to the original cube. The affine case is identical using its sharper \(2^r-2\) column-kernel bound. Odd edge colorings cannot exist in dimension one, so there is no exceptional rank-one terminal coloring to consider. \(\square\)

**Important distinction.** A dimension-six closure result for **ordered three-face colorings with one permitted color change** is not the edge-coloring NORI1 assertion assumed here. The two statements must not be interchanged. The rank-three affine result already established in this project has its own finite transition-state verification; the improved six-dimension column kernel offers a smaller alternative verification target, but it does not itself constitute an unconditional proof for rank three without a valid edge-coloring result in those residual dimensions.



#### Paired-root twin restoration for arbitrary cube-edge colorings

Let P(f)=A_0(f) intersection A_1(f), with A_0 and A_1 denoting full dimension-simple monotone edge-color geodesics of opposite orientations. Assume distinct directions i,j satisfy
\[
f_k(x+e_i+e_j)=f_k(x)\quad(k\ne i,j),\quad
f_i(x+e_j)=f_i(x),\quad f_j(x+e_i)=f_j(x).
\]
Let g_0,g_1 be the two reduced colorings obtained by setting the chosen two bits to parity zero or parity one respectively.

**Theorem (two-slice restoration without antipodal oddness).**
\[
\boxed{|P(f)|\ge2|P(g_0)|+2|P(g_1)|.}
\]
For every paired root z of g_p, both full roots with outside bits z and selected-bit parity p are paired.

*Proof.* The other direction colors depend on the selected two bits only through their parity, while the two selected edge colors depend on neither selected bit. Choose the two opposite monotone geodesics of g_p from z. Insert both selected directions consecutively at the respective monotone switch seams, sorting their two edge colors 0 before 1 in the nondecreasing path and 1 before 0 in the nonincreasing path. Because the selected colors do not change while either inserted edge is traversed, and the selected parity before and after the pair is p, every other edge retains its lower-cube color. Both enlarged paths start from either specified parity-p two-bit assignment and end at its antipode. Counting the disjoint lifts proves the bound. QED.

**Lemma (unread direction).** If direction i influences no other direction edge color, removing i yields g with |P(f)|>=2|P(g)|. Insert the removed dimension at the monotone switch seam of each reduced favorable path; its own edge bit fits either orientation. The starting bit i is arbitrary.

Define global derivative matrix J(f) by J_(k,x),i=f_k(x+e_i)+f_k(x). Equal columns imply the twin hypotheses, and zero columns identify unread dimensions. The derivative rank cannot increase after restriction to a face.

**Theorem (sharp half-cube root guarantee at derivative rank two).** Every undirected binary cube-edge coloring with rank J(f)<=2 satisfies
\[
\boxed{|P(f)|\ge2^{n-1}.}
\]
Proof by induction on n. Dimensions one, two and three have respectively at least 2,2 and 4 paired roots, the last from the sharp three-cube majority bound |A_0|,|A_1|>=6. For n>=4, there are more than three columns in a binary rank-two space, so some column is zero or some two coincide. Deleting a zero column and using induction doubles the lower bound. Deleting two equal columns and applying induction separately on both parity-slice colorings, followed by the displayed twin inequality, multiplies the two separate (n-2)-cube lower bounds by two and sums them, again giving 2^(n-1). The result is sharp: take reciprocal readers f_1=x_2, f_2=x_1 on Q_2 and constant edge colors in all other independent directions. The square has paired roots 01 and 10 only, so the product has 2^(n-1) paired roots and derivative rank two. QED.

These results apply directly to the arbitrary facet coloring in the universal odd-bridge equivalence. In particular NORI1 holds for any odd upper-cube coloring whose lower facet has derivative rank at most two, yielding at least 2^(n-1) lower-facet paired-root witnesses.



#### Exterior derivative-rank degree theorem

Let f be an arbitrary binary undirected cube-edge coloring. Form its global derivative matrix J with entries J_(k,x),i = f_k(x+e_i)+f_k(x), and put r=rank J and C=ker J. For direction k let epsilon_k be one if column k is zero and zero otherwise.

**Theorem.** The algebraic normal form of f_k has degree at most r-1+epsilon_k. Furthermore, the binary vector space of Boolean functions satisfying the first-order derivative relations of C and the self-edge condition D_k f_k=0 has dimension 2^(r-1+epsilon_k).

*Proof.* The vector space of squarefree Boolean polynomials is the exterior algebra on the degree-one symbols x_1,...,x_n over F2. Differencing in one bit, D_i f(x)=f(x+e_i)+f(x), removes x_i from each monomial containing it, so it is contraction by the corresponding dual basis vector. Every vector a in C gives a linear derivative operator sum_i a_i D_i annihilating each f_k. Self-edge invariance adds D_k f_k=0. Thus all contractions associated to H_k=C+span(e_k) annihilate f_k. This space has dimension n-r+1 when derivative column k is nonzero and dimension n-r when it vanishes.

For any s-dimensional subspace H of the dual of an n-dimensional vector space E, the common kernel of contractions from H on the exterior algebra is the exterior algebra of H-perp. To see this choose bases adapted to H; the contractions remove s independent generators, so the surviving monomials involve only the other n-s generators. The common kernel has dimension 2^(n-s) and degree no greater than n-s. Substitute the two possible dimensions of H_k. QED.

**Corollary (affine and quadratic rigidity).** If no direction is unread, rank at most two forces every edge-color function to be affine; rank at most three forces every such function to be quadratic. At rank three with nonzero derivative column k, the space of allowed direction-k functions has dimension four, of which the affine functions comprise a dimension-three subspace. Thus each direction has at most one independent nonlinear quadratic mode modulo affine terms.

*Proof.* The full allowed function space has dimension 2^(3-1)=4. The affine functions b+sum_i a_i x_i have gradients a in C-perp of dimension three; the condition a_k=0 removes one independent gradient dimension because e_k lies outside C. Including b gives dimension three. QED.

**Corollary (minimal obstruction).** A least-dimensional hypothetical paired-root-free coloring has nonzero pairwise distinct derivative columns, by the unread/twin restoration theorem. If it has n directions and derivative rank r, necessarily
\[
\boxed{n\le2^r-1,\qquad \max_k\deg f_k\le r-1.}
\]
This constraint applies to arbitrary nonlinear edge-colorings.

**Limitation.** Linear relations among first-order Boolean differences do not imply invariance under simultaneous flips of three or more original cube bits. The exterior-contraction proof only uses the valid linear differential relations.



#### Binary matroid exterior normal form for nonlinear edge colorings

Let T be an r-by-n binary matrix of rank r, with columns t_1,...,t_n in F2^r. Interpret squarefree polynomials in the n vertex bits x_i as the exterior vector space Lambda(E), where E is the degree-one span of x_i. Exterior products represent squarefree coefficient tensors, not ordinary multiplication of Boolean functions.

For each direction k set
\[
\boxed{W_k=\{\sum_i(a\cdot t_i)x_i:\ a\cdot t_k=0\}\subseteq E.}
\tag{MN1}
\]
For t_k nonzero this has dimension r-1; for t_k zero it has dimension r.

**Theorem (complete derivative-matroid representation).** If every direction-k edge-color polynomial f_k is chosen from the exterior algebra Lambda(W_k), then it is independent of its own bit x_k and the global Boolean derivative matrix J(f) has rank at most r with all dependencies from ker T. Conversely, every arbitrary undirected binary cube-edge coloring f of global derivative rank r has some rank-r matrix T for which every f_k belongs to Lambda(W_k).

*Proof.* The Boolean derivative D_i f=f(x+e_i)+f(x) removes x_i from every squarefree monomial containing it; as a linear map on the exterior space, this is contraction with the i-th dual basis vector. For u in ker T, the contraction D_u=sum_i u_i D_i annihilates every degree-one form in W_k because D_u(sum_i(a dot t_i)x_i)=a dot Tu=0, and hence annihilates all of Lambda(W_k). Contraction by e_k also annihilates W_k, because a dot t_k=0. Therefore the chosen f_k are legal edge-color functions whose global derivative columns obey all relations of ker T, so rank J<=r.

Conversely choose a basis for the column span of J(f), and let the t_i encode its columns. Then ker J=ker T. Every f_k is annihilated by contractions from ker T and by its self-edge contraction D_k. The common kernel of contractions from a subspace H is the exterior algebra on its annihilator H-perp, proved in the previous degree theorem. Here H=ker T+span(e_k) and its annihilator is W_k. QED.

**Corollary (simple binary matroid obstruction).** A least-dimensional paired-root counterexample has a derivative-column matroid with no zero or repeated columns, by unrestricted paired-root unread/twin restoration. Thus its matroid is simple, has at most 2^r-1 points at rank r, and each point t_k carries a local exterior polynomial from Lambda(W_k). This also explains the degree bound deg f_k<=r-1.

**Theorem (canonical Fano quadratic normal form).** Suppose r=3 and the n=7 derivative labels comprise all seven nonzero vectors of F2^3. Then every permitted direction-k color polynomial has the form
\[
\boxed{f_k(x)=b_k+\sum_i(a_k\cdot t_i)x_i+
\eta_k\sum_{i<j}\det(t_i,t_j,t_k)x_ix_j,\quad a_k\cdot t_k=0,}
\tag{MN2}
\]
with binary constants b_k,eta_k and any a_k in the two-dimensional annihilator of t_k. Conversely these choices define legitimate edge colorings of global derivative rank at most three.

*Proof.* W_k has dimension two, so Lambda(W_k) has graded dimensions 1,2,1. The linear part has the displayed form. Let a,b be a basis for the annihilator of t_k. Its unique nonzero degree-two exterior generator has coefficient
(a dot t_i)(b dot t_j)+(a dot t_j)(b dot t_i)
on x_i x_j. This equals the alternating three-dimensional determinant det(t_i,t_j,t_k); the exterior two-form formed by a,b is normalized uniquely over F2. The quadratic component therefore has the one-bit coefficient eta_k. The converse follows from the general theorem. QED.

**Fano geometry.** For each k, det(t_i,t_j,t_k) is zero precisely when the three corresponding Fano points are collinear. Among the other six points there are fifteen unordered pairs, three of which lie with k on a Fano line. Thus each canonical nonlinear quadratic mode contains twelve quadratic monomials. Every local direction-k function in this maximal rank-three derivative kernel has four binary parameters (one constant, two linear, one quadratic), yielding sixteen permitted local functions.

**Research target.** Every derivative-irreducible paired-root obstruction has a simple binary-matroid exterior model. The first full nonlinear model occurs at rank three with the Fano plane. The missing general theorem is a matroid-compatible selection of two opposite monotone full cube paths, not another small-cube enumeration.



#### Projective binary submatroids force high-order nonlinear translation symmetries

Let f be an arbitrary undirected cube-edge coloring with global derivative-column matrix J(f) of rank r. Represent its columns by t_i in F2^r as in the binary-matroid exterior normal form, so that every linear relation among the t_i is a global relation among the derivative operators on every edge-color function.

**Theorem (projective-subspace translation invariance).** Suppose there is a direction subset S whose derivative-column labels consist of the \(2^s-1\) nonzero vectors of an s-dimensional linear subspace of F2^r, each occurring once, with \(s\ge3\). Then for every direction k and every cube vertex x,
\[
\boxed{f_k(x+\mathbf1_S)=f_k(x),}
\tag{PG1}
\]
where \(\mathbf1_S\) flips all the direction bits of S simultaneously. This holds for arbitrary nonlinear functions f_k and arbitrary coloring outside S; no antipodal or affine assumption is needed.

*Proof.* Let D_i denote the Boolean difference operator \(D_i f(x)=f(x+e_i)+f(x)\). It satisfies \(D_i^2=0\), and all D_i commute. Choose basis labels for the s-dimensional subspace and corresponding s independent derivative operators \(\mathcal D_1,\ldots,\mathcal D_s\) acting on the span of the color functions and their translates. Every derivative operator D_i with i in S acts on that space as
\[
D_i=\sum_{a=1}^s t_{ai}\mathcal D_a.
\]
This identity follows from the global derivative-column relations: they hold on all color functions at every cube vertex and are preserved under further translations or Boolean derivatives. The operators \(\mathcal D_a\) commute and square to zero.

Flipping bit i acts as \(I+D_i\). Thus flipping all bits in S acts on every color function by
\[
\prod_{i\in S}(I+D_i)
=
\prod_{v\in\mathbb F_2^s\setminus\{0\}}
\left(I+\sum_{a=1}^s v_a\mathcal D_a\right).
\tag{PG2}
\]
We prove that this product is the identity in the algebra
\(A_s=\mathbb F_2[X_1,\ldots,X_s]/(X_1^2,\ldots,X_s^2)\) for every s>=3.

In the ordinary polynomial ring define
\[
F_s(Z)=\prod_{v\in\mathbb F_2^s}(Z+\sum_av_aX_a).
\]
Induction on s shows \(F_s(Z)\) is a linearized additive polynomial in Z with monomial powers \(Z^{2^j}\): for s=1, \(F_1(Z)=Z^2+X_1Z\); and
\[
F_s(Z)=F_{s-1}(Z)F_{s-1}(Z+X_s)
=F_{s-1}(Z)^2+F_{s-1}(X_s)F_{s-1}(Z).
\]
Its leading term is \(Z^{2^s}\). By homogeneity, the coefficient of each other possible monomial \(Z^{2^j}\), \(j\le s-1\), has X-degree \(2^s-2^j\), at least \(2^{s-1}\). For s>=3 we have \(2^{s-1}>s\). Every positive-degree coefficient therefore vanishes in \(A_s\), where a nonzero squarefree monomial has degree at most s. Consequently \(F_s(1)=1\) in \(A_s\). The v=0 factor of \(F_s(1)\) is one, so this proves (PG2) is the identity after substituting X_a=\mathcal D_a, and hence (PG1). \(\square\)

**Corollary (maximal simple derivative matroids are antipodally even).** If the derivative columns of an n-direction coloring comprise every nonzero vector of F2^r once, with n=2^r-1 and r>=3, then
\[
\boxed{f_k(\bar x)=f_k(x)\quad\text{for every }k,x.}
\]
Thus every such coloring is antipodally even, despite no symmetry being assumed in its definition.

**Lemma (path reversal for an even coloring).** If all edge-color functions satisfy f_k(\bar x)=f_k(x), then for every root z and every full dimension order \(\pi\),
\[
w_f(z,\pi^R)=\operatorname{rev}(w_f(z,\pi)).
\]
Indeed the reverse traversal of a full geodesic starts at its antipode and reverses the sequence of undirected edge colors. Translating that reverse geodesic antipodally starts it at the original root and preserves edge colors under the evenness assumption. Consequently
\[
\boxed{A_0(f)=A_1(f)=P(f).}
\tag{PG3}
\]
For these colorings the unrestricted paired-root assertion reduces to the one-sided existence of any full nondecreasing color geodesic.

**Caution.** The conclusion (PG1) concerns a simultaneous toggle of the whole \(2^s-1\)-direction projective set. It does not assert that the corresponding first-order derivative columns vanish or repeat. The projective submatroid may be simple, with every involved derivative column nonzero and distinct. This is a new high-order symmetry beyond the previously established single-direction and twin-direction deletion rules.

**Closure target.** The projective translation theorem identifies large nonlinear symmetry subsets in any coloring whose derivative matroid contains a full binary projective geometry of dimension at least two. A restoration theorem accommodating a \(2^s-1\)-direction invariant block, or a one-sided nondecreasing-geodesic theorem for antipodally even edge colorings, would immediately dispose of the maximal simple derivative kernels in all ranks. Neither further assertion is established by the present symmetry theorem.



#### Quadratic-moment compression of Boolean derivative rank

Let \(f=(f_1,\ldots,f_n)\) be an arbitrary binary coloring of the undirected edges of \(Q_n\), with \(f_i(x+e_i)=f_i(x)\). The global Boolean-derivative matrix \(J(f)\) has \(i\)-th column \((D_i f_k(x))_{k,x}\), where \(D_i f_k(x)=f_k(x+e_i)+f_k(x)\). Put \(r=\operatorname{rank}_{\mathbb F_2}J(f)\). After choosing a basis of its column span, denote the label of column \(i\) by \(t_i\in\mathbb F_2^r\). Define
\[
q=r+\binom r2,\quad
\nu(t)=\bigl((t_a)_{a=1}^r,(t_at_b)_{1\le a<b\le r}\bigr)\in\mathbb F_2^q,\quad
M=(\nu(t_1)\ \cdots\ \nu(t_n)).
\]

**Theorem (quadratic-moment period theorem).** Every \(u\in\ker M\) is a simultaneous translation period of all the edge-color functions:
\[
\boxed{f_k(x+u)=f_k(x)\quad(k\in[n],\ x\in Q_n).}\tag{QM1}
\]
Consequently their common period group has codimension at most \(q\), and there exist functions \(F_k:\operatorname{im}M\to\mathbb F_2\) satisfying
\[
\boxed{f_k(x)=F_k(Mx),\qquad F_k(y+\nu(t_k))=F_k(y).}\tag{QM2}
\]

*Proof.* Consider the commutative square-zero algebra \(B_r=\mathbb F_2[X_1,\ldots,X_r]/(X_1^2,\ldots,X_r^2)\). Every linear form in the \(X_a\) has square zero. Define
\[
\Phi_T(u)=\prod_{i:u_i=1}(1+t_i\cdot X)\in B_r.
\]
Since each factor is its own inverse, \(\Phi_T\) is a homomorphism from the additive group \(\mathbb F_2^n\) to the multiplicative group of units of \(B_r\). We first establish
\[
\boxed{\Phi_T(u)=1\iff Mu=0.}\tag{QM3}
\]
Indeed, the coefficient of \(X_a\) in \(\Phi_T(u)\) is \(S_a=\sum_i u_i t_{ai}\). For \(a<b\), the coefficient of \(X_aX_b\) is
\[
S_aS_b+\sum_i u_i t_{ai}t_{bi}.
\]
Thus \(\Phi_T(u)=1\) implies \(Mu=0\).

Conversely, combine all factors with a common label \(t\), cancelling each pair, and observe that label \(0\) contributes the identity. The resulting choice of labels is an indicator vector \(v\) on \(\mathbb F_2^r\setminus\{0\}\), extended by zero at \(0\). For \(r\ge3\), let \(\mathcal C\) be the binary vector space of evaluation vectors of squarefree polynomials in the label variables of degree at most \(r-3\), punctured at label zero. This puncturing is injective, since the indicator of the single point zero has degree \(r\). Hence
\[
\dim\mathcal C=\sum_{j=0}^{r-3}\binom rj=2^r-1-q.
\]
Every vector in \(\mathcal C\) has zero first and second moments: the product of its defining polynomial with any monomial of degree one or two has degree at most \(r-1\), so its sum on \(\mathbb F_2^r\) is zero; the test monomial vanishes at label zero. The \(q\) first- and second-moment test vectors are linearly independent on the nonzero labels, because a polynomial of degree at most two with zero constant term that vanishes there also vanishes at zero and therefore vanishes identically. Dimension comparison identifies \(\mathcal C\) with the full kernel of these moment tests.

We show that \(\Phi(v)=1\) for all \(v\in\mathcal C\). The support of a label monomial \(\prod_{a\in I}t_a\), with \(|I|\le r-3\), is an affine subspace of dimension \(r-|I|\ge3\), partitionable into affine three-flats. The monomial evaluation vectors span \(\mathcal C\); it suffices to establish the identity on an affine three-flat \(w+\langle a,b,c\rangle\). Put \(z=1+w\cdot X\), \(A=a\cdot X\), \(B=b\cdot X\), \(C=c\cdot X\). Their squares vanish, and direct multiplication in \(B_r\) gives
\[
\prod_{\epsilon,\eta\in\mathbb F_2}(z+\epsilon A+\eta B)=z^4+ABz^2.
\]
Replacing \(z\) by \(z+C\) leaves the right-hand side unchanged. Multiplying the two four-point products gives
\[
(z^4+ABz^2)^2=z^8=1,
\]
the product over the eight labels of the flat. Any factor for label zero is \(1\). Taking products over sums of evaluation vectors proves \(\Phi(v)=1\) for all \(v\in\mathcal C\), hence for every vanishing-moment selection. For \(r\le2\), the moment evaluations distinguish all nonzero labels and are linearly independent, so vanishing moments allow only zero labels and cancellations of repeated labels. This establishes (QM3) in all ranks.

Choose \(r\) directions \(b_1,\ldots,b_r\) whose derivative columns form the selected basis. On the vector space spanned by all translates of all \(f_k\), the difference operators satisfy \(D_i=\sum_a t_{ai}D_{b_a}\). The equality follows from \(J(f)\) on each \(f_k\) at each vertex and persists under translation because the difference operators commute with translations. All \(D_{b_a}\) commute and square to zero. Translation by \(u\) is \(\prod_{i:u_i=1}(I+D_i)\). Substituting \(X_a=D_{b_a}\) into (QM3) shows that this is the identity on every \(f_k\) whenever \(Mu=0\), proving (QM1). Thus every \(f_k\) factors through \(M\), and its self-edge invariance gives the second equality in (QM2). \(\square\)

**Corollary (period code of a complete simple derivative matroid).** If the labels are precisely the \(2^r-1\) nonzero vectors of \(\mathbb F_2^r\), each once, then \(\operatorname{rank}M=q\), so \(\ker M\) has dimension
\[
2^r-1-r-\binom r2.
\]
For \(r\ge3\), this kernel is the binary Reed--Muller evaluation code of degree at most \(r-3\), punctured at zero. The code is generated by indicators of affine three-flats (punctured at zero). Thus the projective \(2^s-1\)-direction translation periods, \(s\ge3\), are instances of a larger system of periods determined by the quadratic moments of the derivative-column labels.

**Scope.** The theorem compresses the vertex dependence of every rank-\(r\) coloring to a linear quotient of dimension at most \(r(r+1)/2\), independently of \(n\). In the quotient the original \(n\) directions become labeled moves \(\nu(t_i)\), which a full cube geodesic must still traverse once each. The resulting path-selection problem remains open.



##### Optimality of the quadratic-moment period bound

**Theorem (sharpness for every derivative rank at least three).** For every \(r\ge3\) there exists an edge coloring on the \(2^r-1\) directions labeled by all nonzero \(t\in\mathbb F_2^r\) whose derivative matrix has rank \(r\) and whose common translation-period group is precisely \(\ker M\). Thus the bound \(r+\binom r2\) in the quadratic-moment period theorem cannot be decreased for this class by replacing \(\ker M\) with a larger universally guaranteed translation-period group.

*Proof.* Write the cube bits as \(x_t\), indexed by the nonzero \(t\in\mathbb F_2^r\), and put
\[
L_a(x)=\sum_{t\ne0}t_a x_t,\qquad Q_{ab}(x)=\sum_{t\ne0}t_at_bx_t\quad(a<b).
\]
For each unordered pair \(a<b\), choose the direction \(k_{ab}\) labeled by the binary vector having zeros in positions \(a,b\) and ones at every other position. These \(\binom r2\) labels are nonzero and distinct because \(r\ge3\). Color direction \(k_{ab}\) by
\[
f_{k_{ab}}(x)=L_a(x)L_b(x)+Q_{ab}(x)
=\sum_{s<t}(s_at_b+s_bt_a)x_sx_t,
\]
where the sum is over a fixed ordering of the nonzero binary labels. Color all remaining directions constantly zero. Because the label of \(k_{ab}\) has zero entries at \(a,b\), its color is independent of its own direction bit, so this defines an undirected-edge coloring.

Its first derivatives satisfy
\[
D_t f_{k_{ab}}(x)=t_aL_b(x)+t_bL_a(x).
\]
As \(x\) varies, \((L_1(x),\ldots,L_r(x))\) ranges over all of \(\mathbb F_2^r\). For each \(a<b\), the derivative rows from direction \(k_{ab}\) therefore span the two linear functionals \(t\mapsto t_a\) and \(t\mapsto t_b\). Taking all pairs shows that the derivative-column rank is \(r\), with column labels \(t\) in this basis.

For a translation vector \(u\), write \(U_a=L_a(u)\). Direct expansion yields
\[
f_{k_{ab}}(x+u)+f_{k_{ab}}(x)
=U_aL_b(x)+U_bL_a(x)+U_aU_b+Q_{ab}(u).
\]
If \(u\) preserves all the color functions, this expression vanishes for every \(x\) and every pair \(a<b\). Independence of the forms \(L_a,L_b\) forces \(U_a=U_b=0\) for each pair, hence \(L(u)=0\). The displayed expression then reduces to \(Q_{ab}(u)\), which must also vanish for every pair. Therefore \(Mu=0\). The converse is the quadratic-moment period theorem, proving that the period group is \(\ker M\). \(\square\)

In particular the codimension \(r(r+1)/2\) can be attained by a family of quadratic color functions, even though their global derivative rank is only \(r\). Any stronger all-rank compression must use information beyond universal translation periods.



##### A simple twelve-point derivative matroid with no affine three-flat

**Proposition (flat-free quadratic-moment period).** Let
\[
T=\{t\in\mathbb F_2^5:t_1t_2+t_3t_4=1\}.
\]
Then \(T\) contains twelve distinct nonzero vectors and satisfies \(\sum_{t\in T}\nu(t)=0\) for the quadratic-moment lift \(\nu:\mathbb F_2^5\to\mathbb F_2^{15}\). Nevertheless \(T\) contains no affine three-flat and no complete seven-point projective plane. Consequently **every** cube-edge coloring whose twelve derivative columns have these distinct labels is antipodally even, although its derivative matroid contains neither of these saturated local configurations.

*Proof.* The quadratic Boolean polynomial \(q(t)=t_1t_2+t_3t_4\) is the indicator of \(T\). Its first four bits have six solutions, and the fifth bit is free; thus \(|T|=12\) and \(0\notin T\). For every squarefree monomial \(p(t)\) of degree one or two, the product \(p(t)q(t)\) has degree at most four in five variables, so its sum over \(\mathbb F_2^5\) is zero. These are precisely the first- and second-moment identities \(\sum_{t\in T}\nu(t)=0\).

The six solutions in the first four bits are
\[
\{(11,v):v\in\{00,01,10\}\}\ \cup\
\{(u,11):u\in\{00,01,10\}\}.
\]
No four distinct points of this six-point set sum to zero. Indeed, if three are taken from one group and one from the other, the fixed two-bit block has nonzero sum; if two are taken from each group, the sum of the two distinct variable blocks is nonzero. Thus the six-point set has no affine two-flat. Any affine three-flat in \(\mathbb F_2^5\) projects onto an affine subspace of dimension at least two in the first four bits, and hence cannot lie inside \(T\).

If the seven nonzero members of a three-dimensional linear subspace \(U\) lay in \(T\), the restriction \(q|_U\) would equal the indicator of the nonzero vectors of \(U\). In three independent binary variables that indicator has algebraic degree three, whereas \(q|_U\) has degree at most two. This contradiction excludes complete projective planes. Finally, the quadratic-moment period theorem applied to \(\sum_{t\in T}\nu(t)=0\) shows that flipping all twelve directions preserves every color function. \(\square\)

**Structural implication.** The period code \(\ker M\) can contain nonzero words even when the derivative-label configuration contains no affine three-flat or complete projective plane. Thus a proof based solely on detecting saturated projective subsets would overlook global nonlinear translation periods; structural induction must account for aggregate moment cancellations.



**Nonlinear realization.** Identify the twelve direction labels in \(T\) with integers in low-bit-first binary order, and put \(L_a(x)=\sum_{t\in T}t_ax_t\). For the five distinct labels \(k_1=12,k_2=13,k_3=3,k_4=7,k_5=11\), each having \((k_a)_a=0\), assign \(f_{k_a}=L_a\). The remaining colors are initially zero. The five derivative rows span the five label-component functions, and \(T\) spans \(\mathbb F_2^5\). Hence the resulting derivative matrix has rank five with nonzero pairwise distinct columns labeled by \(T\).

Now set, in the previously unused direction \(28=(0,0,1,1,1)\in T\),
\[
f_{28}(x)=L_1(x)L_2(x)+\sum_{t\in T}t_1t_2x_t.
\]
This rule is independent of bit \(x_{28}\), has a nonzero quadratic part, and satisfies \(D_t f_{28}=t_1L_2+t_2L_1\). All its derivative rows lie in the previous five-dimensional span. The full coloring therefore has derivative rank five, a non-affine color function, twelve distinct nonzero derivative labels, and the flat-free twelve-direction period.


##### One-way periodic block restoration

Let \(S,T\) be a partition of the direction set of an arbitrary binary edge coloring \(f\), with both parts nonempty. Assume
\[
 f_i(s,t)=h_i(s)\quad(i\in S),\qquad
 f_j(s+\mathbf1_S,t)=f_j(s,t)\quad(j\in T).
 \tag{PB1}
\]
For each \(s\in Q_S\), let \(g_s\) be the edge coloring of \(Q_T\) obtained by fixing the \(S\)-bits to \(s\).

**Theorem (periodic-block restoration).** Under (PB1),
\[
\boxed{\bigcup_{s\in P(h)}\bigl(\{s\}\times P(g_s)\bigr)\subseteq P(f),
\qquad
|P(f)|\ge\sum_{s\in P(h)}|P(g_s)|.}
\tag{PB2}
\]
An analogous inclusion holds for each monotone orientation separately.

*Proof.* Fix \(s\in P(h)\) and \(t\in P(g_s)\). Choose nondecreasing full geodesics in \(h\) and \(g_s\) with initial roots \(s,t\), and words \(0^a1^b\), \(0^p1^q\). Follow the first \(p\) steps of the \(T\)-geodesic, then the whole \(S\)-geodesic, then the remaining \(q\) steps of the \(T\)-geodesic. The \(S\)-bits equal \(s\) before their complete traversal and \(\bar s=s+\mathbf1_S\) afterward. By the second part of (PB1), all \(T\)-edges have the colors they had in \(g_s\). By the first part of (PB1), all \(S\)-edges have their colors from \(h\), independently of the \(T\)-bits. Therefore the resulting full geodesic has word \(0^{p+a}1^{b+q}\).

Repeat from the same root \((s,t)\) with the nonincreasing geodesics in \(h\) and \(g_s\), inserting the full \(S\)-path at the \(1\)-to-\(0\) seam of the \(T\)-path. This gives word \(1^*0^*\). Both paths use every dimension once. Hence \((s,t)\in P(f)\), and distinct choices give distinct roots. The same construction restricted to either orientation proves the final assertion. \(\square\)

**Corollary (minimal-counterexample exclusion).** A least-dimensional paired-root-free coloring contains no proper nonempty block \(S\) satisfying (PB1). Otherwise \(h\) and each \(g_s\) have fewer dimensions and possess paired roots by minimality, contradicting (PB2).

**Corollary (projective source-block elimination).** Suppose a proper nonempty set \(S\) of directions has derivative-column labels comprising all nonzero vectors of a binary subspace of dimension \(r\ge3\), each once. If every \(S\)-direction color function is independent of the bits in \(T\), then \(S\) is removable in the paired-root minimal-counterexample induction.

*Proof.* The projective translation-period theorem guarantees that simultaneous flipping of the bits in \(S\) preserves every edge-color function, giving the second hypothesis of (PB1). The assumed external independence gives its first hypothesis. Apply the preceding corollary. \(\square\)

This mechanism permits nonlinear dependence of \(T\)-direction colors on \(S\)-bits. For instance,
\[
f_1=x_2,\quad f_2=x_3,\quad f_3=x_1,\quad
f_4=x_5+x_1+x_2,\quad f_5=x_4\pmod2
\]
has directed cycles on \(S=\{1,2,3\}\) and \(T=\{4,5\}\), together with arrows from \(S\) to \(T\), and no directed sink. Nevertheless (PB1) holds. Periodic-block restoration thus eliminates configurations which survive every individual sink-deletion step. The theorem applies at arbitrary block size and does not resolve unrestricted strongly connected influence cores.


##### Quadratic-moment period supports must receive external influence

Retain the global derivative-column labels \(t_i\in\mathbb F_2^r\) and the quadratic-moment matrix \(M\) with columns
\[
\nu(t_i)=\bigl((t_{ia})_{a\in[r]},(t_{ia}t_{ib})_{a<b}\bigr).
\]
Let \(D(f)\) be the directed influence graph, with an arc \(j\to i\) when \(D_jf_i\) is nonzero somewhere.

**Corollary (period-support indecomposability of a minimal obstruction).** If \(f\) is a least-dimensional paired-root-free coloring, then for every nonzero \(u\in\ker M\) having proper support \(S=\{i:u_i=1\}\subsetneq[n]\), there is an influence arc
\[
\boxed{j\longrightarrow i\quad\text{with }j\notin S,\ i\in S.}
\tag{PM1}
\]
Equivalently, no proper nonempty source-closed direction set can equal the support of a word in the quadratic-moment period code \(\ker M\).

*Proof.* By the quadratic-moment period theorem, \(u\in\ker M\) implies \(f_k(x+u)=f_k(x)\) for every \(k\) and \(x\). If there were no arc from \(T=[n]\setminus S\) into \(S\), the color function of every \(S\)-direction edge would be independent of all \(T\)-bits. Flipping all bits of \(S\) is precisely translation by \(u\), and preserves every \(T\)-direction edge color. Thus (PB1) would hold and the periodic-block restoration theorem would contradict minimality. \(\square\)

This condition applies to nonlinear period words of arbitrary support, including the twelve-point flat-free example above: a complete projective subgeometry is unnecessary. It couples the binary-matroid moment kernel to the condensation structure of the directed influence graph. A future proof through this route would need either to produce a period word whose support is source-closed, or to show that the forced incoming arcs for every proper period support cannot coexist in a minimal obstruction.


##### Extremal geodesic blockers and exponential paired-root stability

Let \(d\ge2\). A complete geodesic traverses each cube dimension once between antipodal vertices. For an arbitrary binary edge coloring \(f\), let \(A(f)\) denote roots admitting a complete path with word \(0^*1^*\), and \(P(f)=A(f)\cap\overline{A(f)}\). By reversing paths, a root is paired precisely when it admits both \(0^*1^*\) and \(1^*0^*\) orientations. Either color of monochromatic complete path certifies a paired root.

**Theorem 1 (minimum blocker rigidity).** An edge set \(S\) intersecting every full antipodal geodesic has \(|S|\ge2^{d-1}\), with equality precisely when it consists of the entire edge class of one direction.

*Proof.* A uniformly sampled rooted full geodesic uses every specified cube edge with probability \(2^{-(d-1)}\). Its expected \(S\)-count is \(|S|/2^{d-1}\), proving the bound. At equality all full geodesics contain one \(S\)-edge. On a square with cyclically ordered membership indicators \(a,b,c,e\), compare full paths beginning with the two dimensions from one corner and then from an adjacent corner. The two swaps give \(a+b=c+e\) and \(b+c=a+e\); hence \(a=c\), \(b=e\). All opposite edges of all squares have equal membership. Thus membership is constant on every direction class. Since every full path uses every direction once and hits \(S\) once, a single direction is selected. QED.

Fix direction \(i\). Let \(c_i\) color all \(i\)-edges one and all other edges zero. Every root has both oriented witnesses: putting \(i\) last produces \(0^{d-1}1\); putting it first produces \(10^{d-1}\).

**Theorem 2 (stability through the endpoint radius).** If any binary edge coloring \(f\) differs from \(c_i\) on at most \(2^{d-2}\) edges, then \(P(f)\ne\varnothing\).

*Proof.* Let \(F\) be the changed-edge set, and split the cube as \(Q_{d-1}\times Q_1\), using \(i\) vertically. For every root \(z=(y,s)\) and permutation \(\pi\) of the horizontal dimensions, take the two complete paths with \(i\) last and first. They are edge-disjoint and support the two desired orientations under \(c_i\). For uniform \(z,\pi\), each cube edge occurs in their union with probability \(2^{-(d-2)}\): for an \(i\)-edge the candidate horizontal positions are \(y\) and \(\bar y\); for a horizontal edge the same horizontal geodesic occurs in both vertical layers. Thus
\[
\mathbb E|F\cap(P_{\rm first}\cup P_{\rm last})|=|F|/2^{d-2}.
\tag{1}
\]
If \(|F|<2^{d-2}\), some path pair is untouched, giving a paired root.

Suppose \(|F|=2^{d-2}\) but there is no paired root. Every candidate path pair then hits \(F\) at least once. Equation (1) forces the hit count to be one **for every root and permutation**.

Let \(F_i(y)\) indicate the changed vertical edge at horizontal location \(y\). For a horizontal edge \(e\), define the nonnegative integer weight \(w(e)=F^0(e)+F^1(e)\in\{0,1,2\}\), the number of its two layer copies changed. For every horizontal root \(y\) and full horizontal geodesic \(G(y,\pi)\), the count-one identity reads
\[
F_i(y)+F_i(\bar y)+\sum_{e\in G(y,\pi)}w(e)=1.
\tag{2}
\]
For fixed \(y\), the weighted horizontal path sum is therefore independent of \(\pi\). Compare the two routes through a horizontal square from two neighboring corners, holding the remaining dimension order fixed. The resulting pair of equations forces opposite edges of the square to have equal \(w\)-weight, just as in Theorem 1. Hence \(w\) is constant on each horizontal direction class; this is also immediate when the horizontal cube has dimension one. Denote the constants \(w_j\), and let \(W_0=\sum_{j\ne i}w_j\). Equation (2) gives
\[
F_i(y)+F_i(\bar y)+W_0=1,
\]
so \(W_0\in\{0,1\}\).

If \(W_0=0\), all horizontal edges retain color zero and each antipodal pair of vertical edges has one changed member. From any root, taking the vertical edge first or last at its zero-colored location yields a full **monochromatic zero** geodesic. Every root is paired.

If \(W_0=1\), all vertical edges retain color one; all horizontal directions except one, say \(j\), retain color zero. The \(j\)-edge colors may vary without affecting the argument. From every root, listing all dimensions other than \(i,j\), then \(j\), then \(i\) gives a \(0^*1^*\) word. Listing \(i\), then \(j\), then the remaining dimensions gives a \(1^*0^*\) word. Every root is again paired. Both cases contradict the premise. QED.

**Corollary 3 (separation of hypothetical counterexamples).** If \(P(f)=\varnothing\), then \(f\) has at least \(2^{d-1}+1\) edges of each color, and its Hamming distance to every one-direction reference coloring \(c_i\), as well as to its global complement, exceeds \(2^{d-2}\).

*Proof.* A coloring without paired roots contains no monochromatic complete path of either color. Each color class therefore blocks all such paths and has size at least \(2^{d-1}\), by Theorem 1. Equality would make one class a full direction class, giving paired roots. The Hamming separation follows from Theorem 2 and global color complementation. QED.

**Closure perspective.** The minimum transversals of the full geodesic system are rigid direction classes. A substantial Hamming neighborhood around every such extremizer is paired-root-safe. To complete NORI1 through this strategy one needs a stability theorem forcing a minimal paired-root-free coloring near an extremizer, or an exchange argument coupling its repaired witnesses; neither follows merely from the bound here. This route respects dimension-simpleness and avoids reliance on favorable-root density, which can decay exponentially under Cartesian products.

#### Quantitative stability of all near-minimum antipodal geodesic blockers

Write \(M=2^{d-1}\), so each direction of \(Q_d\) contains \(M\) undirected edges. For a blocker \(S\subseteq E(Q_d)\) of all full antipodal geodesics, put \(|S|=M+t\), \(t\ge0\).

**Theorem 4 (square-pivot/Poincaré stability).** There exists a union \(U\) of whole direction edge classes such that
\[
\boxed{|S\mathbin{\triangle}U|\le 2d(d-1)t.}
\tag{3}
\]
When \(t\le M/(4d(d-1))\), \(U\) consists of just one direction class and the corresponding characteristic coloring \(f=\mathbf1_S\) has a paired root.

*Proof.* Choose a uniform cube root \(z\), a uniform ordered pair of distinct directions \(i,j\), and a uniform ordering \(\rho\) of the remaining directions. Form four full geodesics: from \(z\), traverse \(i,j,\rho\) or \(j,i,\rho\); from \(z\oplus e_i\), traverse \(j,i,\rho\) or \(i,j,\rho\). Each of these four geodesics, considered marginally, is uniformly distributed over all rooted dimension-ordered complete geodesics, so each has expected \(S\)-count
\[
\mu=|S|/M=1+t/M.
\]
Every count is at least one, whence each path has probability at most \(t/M\) of having two or more \(S\)-edges. With probability at least \(1-4t/M\), all four geodesics have \(S\)-count one.

Denote the cyclically consecutive membership indicators of the initial \(i,j\) square by \(a,b,c,e\), so \(a,c\) are opposite \(i\)-edges and \(b,e\) are opposite \(j\)-edges. When the two full paths rooted at \(z\) both have count one, their shared suffix cancels and yields \(a+b=c+e\). When the two full paths rooted at \(z\oplus e_i\) both have count one, their shared suffix cancels and yields \(b+c=a+e\). Therefore, outside a probability at most \(4t/M\), the square satisfies \(a=c,b=e\).

For each direction \(i\), let \(f_i:\{0,1\}^{d-1}\to\{0,1\}\) indicate membership in \(S\) of its edges. Define the direction influence
\[
I_{ij}=\Pr_{z}\bigl(f_i(z)\ne f_i(z\oplus e_j)\bigr),\qquad i\ne j.
\]
A uniformly sampled ordered pair \(i,j\) and square root \(z\) has
\[
\mathbb E\bigl[
\mathbf1_{f_i(z)\ne f_i(z\oplus e_j)}
+\mathbf1_{f_j(z)\ne f_j(z\oplus e_i)}
\bigr]
=\frac{2}{d(d-1)}\sum_{i\ne j}I_{ij}.
\]
The summand is zero when both square equalities hold, and is at most two otherwise. Hence
\[
\boxed{\sum_{i\ne j}I_{ij}\le 4d(d-1)\frac tM.}
\tag{4}
\]

Write \(p_i=\mathbb E f_i\), and let \(u_i\in\{0,1\}\) be a majority value of \(f_i\). The Boolean-cube Poincaré inequality gives
\[
p_i(1-p_i)\le\frac14\sum_{j\ne i}I_{ij}.
\]
Since \(\min(p_i,1-p_i)\le2p_i(1-p_i)\), the number of direction-\(i\) edge labels differing from \(u_i\) is at most \((M/2)\sum_{j\ne i}I_{ij}\). Let \(U\) be the union of those whole direction classes with \(u_i=1\). Summing and using (4) gives (3).

Now suppose \(t\le M/(4d(d-1))\). Then \(k=|S\triangle U|\le M/2\), whereas \(|S|=M+t\) and \(t\le M/8\). Since the size of \(U\) is a multiple of \(M\), the inequality \(\bigl||U|-|S|\bigr|\le k\) rules out \(|U|=0\) and \(|U|\ge2M\). Thus \(|U|=M\): \(U\) is one full direction class. Theorem 2 then supplies a paired root, since \(k\le M/2=2^{d-2}\). QED.

**Corollary 5 (uniform exponential excess in every paired-root counterexample).** If an arbitrary coloring \(f\) of \(Q_d\) has no paired root, then both its color classes obey
\[
\boxed{|E_c(f)|>2^{d-1}\left(1+\frac{1}{4d(d-1)}\right),
\qquad c\in\{0,1\}.}
\tag{5}
\]

*Proof.* A paired-root-free coloring has no monochromatic full antipodal geodesic. Thus each color class is a blocker as in Theorem 4. If either had cardinality no more than the threshold in (5), Theorem 4 applied to that class (with the two color values exchanged if necessary) would supply a paired root, contradiction. QED.

**Closure implication and caution.** This supplies a rigorous quantitative bridge from the cardinality of a complete-geodesic transversal to the bridge-theorem paired-root goal. It does not show that an arbitrary minimal paired-root-free coloring has color-class size near the minimum, so the unrestricted conjecture remains open. The product-factorization counterexamples to favorable-root density make such an isoperimetric or critical-repair step essential rather than automatic. The proof uses only complete dimension-simple geodesics and commuting square exchanges.

#### Abundance of paired roots under Hamming perturbations

**Theorem 6 (paired-root loss bounded by four per edited edge).** Let \(c_i\) be the reference coloring with all direction-\(i\) edges one and every other edge zero. For any binary edge coloring \(f\) at Hamming distance \(k\) from \(c_i\),
\[
\boxed{|P(f)|\ge\max\{0,\,2^d-4k\}.}
\tag{6}
\]
In particular at most \(2k\) antipodal pairs of roots can fail to be paired when measured against this reference witness construction.

*Proof.* For each root \(z\) and permutation \(\pi\) of the other \(d-1\) dimensions, take the pair of complete geodesics that places \(i\) first or last, as in Theorem 2. If neither path contains a changed edge, both one-switch orientations remain valid from \(z\), so \(z\in P(f)\). Thus for every nonpaired root \(z\), each of the \((d-1)!\) paired witness choices has at least one changed edge in its union. Summing over all roots and permutations, we obtain
\[
(2^d-|P(f)|)(d-1)!
\le \sum_{z,\pi}|F\cap(P_{\rm first}(z,\pi)\cup P_{\rm last}(z,\pi))|.
\]
Every edge belongs to \(4(d-1)!\) of these indexed witness unions by the uniform incidence calculation in Theorem 2. Hence the right side equals \(4k(d-1)!\), proving (6). Since \(P(f)\) is antipodally symmetric by definition, its complement consists of antipodal root pairs. QED.

**Corollary 7 (paired-root abundance close to minimum blockers).** If a full-geodesic blocker \(S\) has cardinality \(2^{d-1}+t\), and the nearest union-of-directions approximation \(U\) from Theorem 4 consists of one direction, then its characteristic coloring obeys
\[
\boxed{|P(\mathbf1_S)|\ge\max\{0,\,2^d-8d(d-1)t\}.}
\]
In particular, the paired-root set occupies almost the entire cube whenever the blocker excess is small compared with \(2^d/d^2\).

*Proof.* Use Theorem 4 to obtain \(|S\triangle U|\le2d(d-1)t\), and apply Theorem 6 with \(k=|S\triangle U|\). QED.

**Interpretation.** The stability theorem is not purely existential. Each unit of Hamming perturbation can spoil the chosen two-orientation witness pairs at at most four root vertices, measured by uniform fractional path incidence. This abundance statement may be useful when attempting to couple the repaired roots of two critical edge recolorings.

#### Every direction-uniform coloring has the same protected paired-root radius

Let \(d\ge2\), \(M=2^{d-1}\), and let \(c\) be any cube edge coloring **constant on each dimension class**, with a partition \([d]=A\sqcup B\): all \(A\)-edges have color zero and all \(B\)-edges have color one. Either part may initially be empty.

**Theorem 8 (universal directional-template stability).** If an arbitrary binary cube-edge coloring \(f\) has Hamming distance
\[
\boxed{\operatorname{dist}(f,c)\le M/2=2^{d-2},}
\tag{7}
\]
then \(f\) has a paired root. The assertion holds for **every** direction-uniform template \(c\), not just those with one exceptional dimension.

*Proof.* If \(A\) or \(B\) is empty, \(c\) is monochromatic. Were \(f\) to lack a paired root, it would in particular lack a monochromatic full geodesic of the template color. Its altered-edge set would then meet every full geodesic, and the minimum-blocker theorem would force at least \(M\) altered edges, contrary to (7).

Suppose \(a=|A|,b=|B|\) are positive. Write vertices as \((u,v)\in Q_A\times Q_B\). For any root \((u,v)\), an arbitrary full \(A\)-geodesic \(P_A\) from \(u\) to \(\bar u\), and an arbitrary full \(B\)-geodesic \(P_B\) from \(v\) to \(\bar v\), form the following two full paths:
\[
P_{01}= (P_A\text{ at }v)\,\cdot\,(P_B\text{ at }\bar u),\qquad
P_{10}= (P_B\text{ at }u)\,\cdot\,(P_A\text{ at }\bar v).
\tag{8}
\]
They are edge-disjoint and have words \(0^a1^b\) and \(1^b0^a\) under \(c\). Let \(F\) be the edges on which \(f\ne c\), with \(k=|F|\). Sampling the root and the two blockwise dimension orders uniformly, each edge of \(Q_d\) belongs to the union in (8) with probability \(2/M\), because each path is marginally a uniformly translated complete direction-simple path. Thus
\[
\mathbb E|F\cap(P_{01}\cup P_{10})|=2k/M.
\tag{9}
\]
If \(k<M/2\), some rectangle is untouched and supplies a paired root.

Now suppose \(k=M/2\) and, toward contradiction, that \(f\) has no paired root. Every rectangle (8) must contain an altered edge, so (9) implies it contains **precisely one altered edge for every root and both blockwise orders**.

For an \(A\)-direction edge \(e\) in the \(A\)-cube, fix \(v\in Q_B\) and define its paired-layer weight
\[
w_A(e;v)=\mathbf1_F(e,v)+\mathbf1_F(e,\bar v)\in\{0,1,2\}.
\]
Similarly, for a \(B\)-direction edge \(e'\) in \(Q_B\) and \(u\in Q_A\), put
\[
w_B(e';u)=\mathbf1_F(u,e')+\mathbf1_F(\bar u,e').
\]
The one-hit identity is
\[
\sum_{e\in P_A}w_A(e;v)+\sum_{e'\in P_B}w_B(e';u)=1
\quad\text{for all }u,v,P_A,P_B.
\tag{10}
\]
Holding \(u,v,P_B\) fixed, every complete \(A\)-geodesic from \(u\) has the same total \(w_A\)-weight. Exchanging the first two directions around an arbitrary \(A\)-square, and repeating the exchange from an adjacent root, shows that opposite \(A\)-square edges have equal weights. Hence for fixed \(v\), \(w_A(e;v)\) depends only on the direction \(i\in A\), say \(\alpha_i(v)\in\{0,1,2\}\). The same square argument in \(Q_B\) yields direction constants \(\beta_j(u)\in\{0,1,2\}\) for \(j\in B\). For one-dimensional factors this direction constancy holds without exchanges.

Consequently (10) becomes
\[
\sum_{i\in A}\alpha_i(v)+\sum_{j\in B}\beta_j(u)=1
\quad\text{for every }u,v.
\tag{11}
\]
Since the two nonnegative integer sums depend on disjoint arguments, they are constants \(r,s\ge0\), with \(r+s=1\). Thus one is zero and the other one.

If \(r=0\), no \(A\)-edge was altered anywhere. For each fixed \(u\), the relation \(\sum_{j\in B}\beta_j(u)=1\) says that all \(B\)-edges are unaltered except possibly those of one direction \(j(u)\), since \(\beta_j(u)=0\) means neither of the two \(u,\bar u\) copies was altered. From root \((u,v)\), traverse every \(A\)-direction first, placing the possibly exceptional \(B\)-direction first among the \(B\)-steps at \(\bar u\); the word is \(0^*1^*\). For the opposite orientation traverse the \(B\)-directions first at \(u\), placing the possibly exceptional one last within \(B\), followed by all \(A\)-directions; the word is \(1^*0^*\). Thus **every root is paired**.

If \(s=0\), no \(B\)-edge was altered, and for each fixed \(v\) at most one \(A\)-direction can contain altered edges there. Take all \(A\)-directions first with that exceptional direction last, then all \(B\)-directions: the word is \(0^*1^*\). For the reverse orientation put all \(B\)-directions first, then the possibly exceptional \(A\)-direction first among the \(A\)-steps, followed by the remaining \(A\)-directions: the word is \(1^*0^*\). Again every root is paired. This contradicts the premise and proves the theorem. QED.

**Corollary 9 (a square-variation necessary condition for counterexamples).** For each \(i\in[d]\), write \(f_i(x)\) for the color of the direction-\(i\) edge at \(x\), independent of the \(i\)-th bit, and for \(j\ne i\) define
\[
I_{ij}(f)=\Pr_{x\in Q_d}[f_i(x)\ne f_i(x\oplus e_j)].
\]
If \(f\) has no paired root, then
\[
\boxed{\sum_{i\ne j}I_{ij}(f)>1.}
\tag{12}
\]
Equivalently, more than \(2^{d-2}\) total incidences of disagreeing opposite-edge comparisons must occur over all cubical squares, counting separately the two directions of each square.

*Proof.* Let \(p_i=\Pr f_i=1\) and let \(c_i\in\{0,1\}\) be the majority color of direction-\(i\) edges. Then the nearest direction-uniform template \(c\) differs from \(f\) on
\[
k=M\sum_i\min(p_i,1-p_i).
\]
By the Boolean-cube Poincaré inequality, \(p_i(1-p_i)\le\frac14\sum_{j\ne i}I_{ij}\), and \(\min(p_i,1-p_i)\le 2p_i(1-p_i)\). Hence
\[
k\le\frac M2\sum_{i\ne j}I_{ij}.
\]
Theorem 8 forces \(k>M/2\) for any paired-root-free \(f\), yielding (12). For each unordered pair of dimensions and each of its \(2^{d-2}\) squares, the two opposite-edge disagreements contribute once each to the sum multiplied by \(2^{d-2}\); this is the equivalent integer statement. QED.

**Consequence for the closure plan.** A minimum paired-root-free coloring must be Hamming-far from *every* direction-uniform template, not only the one-direction blockers. It must also have total transverse square variation exceeding one in normalized units. This is a color-sensitive restriction based solely on commuting-square interactions and uses no small-dimension assumption. It is not sufficient by itself to prove paired-root existence.

#### Two arbitrary exceptional directions still force many paired roots

For a binary edge coloring \(f\) of \(Q_d\), say that a dimension \(i\) is *uniform* if every edge of direction \(i\) has the same color, independent of its location. No restriction is imposed on the coloring of the remaining directions.

**Lemma 10 (square favorability).** For any coloring \(g\) of the four edges of \(Q_2\), the set \(A_0(g)\) of roots admitting a complete two-edge path with nondecreasing color word has size at least three. The same is true of the set \(A_1(g)\) of roots admitting a nonincreasing word.

*Proof.* A root \(x\) fails to lie in \(A_0(g)\) only if both possible two-step paths beginning at \(x\) have color word \(10\). Thus both edges incident with \(x\) must have color one and both incident with its antipode must have color zero. This pins down all four square-edge colors and makes every other root favorable. Hence at most one root is excluded. Swapping zero and one gives the nonincreasing assertion. QED.

**Theorem 11 (two-exception paired-root theorem).** If at most two dimensions of an arbitrary binary edge coloring \(f\) of \(Q_d\) are nonuniform, then
\[
\boxed{|P(f)|\ge 2^{d-1}.}
\tag{13}
\]
If at most one direction is nonuniform, every root is paired. The lower bound with two exceptional directions is attained by Cartesian-product colorings.

*Proof.* Let \(S\) contain all nonuniform directions, extending it to two dimensions if necessary. Partition the remaining directions into \(A\) (uniform color zero) and \(B\) (uniform color one), so \([d]=A\sqcup S\sqcup B\). Write a root as \((u,x,v)\in Q_A\times Q_S\times Q_B\).

To construct a \(0^*1^*\) complete path from this root, first traverse all \(A\)-directions, reaching outside configuration \((\bar u,v)\); next traverse the two \(S\)-directions along a nondecreasing two-edge path in the corresponding \(S\)-fiber; finally traverse all \(B\)-directions. The resulting full word is nondecreasing whenever
\[
x\in A_0\bigl(f^{(\bar u,v)}_S\bigr).
\]
For a \(1^*0^*\) path, traverse all \(B\)-directions first, then a nonincreasing two-edge path in the \(S\)-fiber at outside configuration \((u,\bar v)\), then all \(A\)-directions. This requires
\[
x\in A_1\bigl(f^{(u,\bar v)}_S\bigr).
\]
The two restricted square colorings are entirely arbitrary and need not agree. By Lemma 10, each of these favorable-root sets has at least three members among the four \(S\)-roots. Their intersection therefore contains at least two members. For every choice of the \(d-2\) outside-root bits \((u,v)\), at least two values of \(x\) give both orientations at the **same root**. Hence \(|P(f)|\ge2\cdot2^{d-2}=2^{d-1}\).

If at most one direction is nonuniform, take \(S\) with one element. Every path in its one-dimensional fiber is monochromatic, so both orientation requirements hold from both roots; the same concatenation shows \(P(f)=V(Q_d)\).

To see sharpness for two exceptions, take the square coloring \(h\) with \(A_0(h)=\{01,10,11\}\), \(P(h)=\{01,10\}\) from the Cartesian-factorization Subsection. Form \(f=h\boxtimes g\), where \(g\) is any direction-uniform coloring on the other \(d-2\) dimensions. The factorization of paired-root sets gives
\[
|P(f)|=|P(h)|\,|P(g)|=2\cdot2^{d-2}=2^{d-1}.
\]
QED.

**Corollary 12 (at least three variable direction classes).** Any hypothetical coloring of \(Q_d\) with no paired root must have at least three nonuniform dimension classes. This is stronger than interaction-graph connectedness alone: nonuniformity is allowed to depend on all remaining dimensions, yet two exceptional classes can never obstruct paired roots.

**Closure significance.** The proof needs neither antipodal oddness nor a bound on the number of nonuniform edges within the two exceptional direction classes. It converts paired-root compatibility into an intersection property for favorable-root sets of arbitrary fiber colorings. This suggests a possible general proof scheme through cross-intersection of feasible-root families on higher-dimensional fibers. The square case is strong enough to force intersection because each favorable set has density at least three quarters. Cartesian products show that such favorable-root density need not remain above one half in arbitrarily high fiber dimension, so a higher-dimensional argument must exploit more than a uniform cardinality bound.

#### Three arbitrary nonuniform directions force paired roots

We strengthen the preceding two-exception theorem by proving a sharp three-cube favorability bound without enumeration.

**Lemma 13 (same-parity two-root certificate in a colored three-cube).** For every arbitrary binary coloring of the edges of \(Q_3\), any two distinct root vertices of the same Hamming parity cannot both fail to admit a complete \(0^*1^*\) geodesic. Consequently
\[
\boxed{|A_0(g)|\ge6,\qquad |A_1(g)|\ge6.}
\tag{14}
\]
Both bounds are sharp.

*Proof.* Every pair of distinct three-bit vertices of the same parity has Hamming distance two. By a cube automorphism we may take the roots to be \(000\) and \(110\), using bit positions \((0,1,2)\). Denote the following seven undirected cube edges by letters:
\[
\begin{array}{lll}
a=000\!-\!100,& b=100\!-\!110,&c=100\!-\!101,\\
d=101\!-\!111,&e=001\!-\!101,&f=000\!-\!001,\\
g=110\!-\!111.& &
\end{array}
\]
Here the symbols \(a,\ldots,g\) also denote their edge-color bits. The following six length-three, dimension-simple full paths start at one of our two roots:
\[
(a,b,g),\quad(a,c,d),\quad(f,e,d);
\qquad
(b,a,f),\quad(b,c,e),\quad(g,d,e).
\tag{15}
\]
For bits \(x,y\), the descending-comparison indicator is \(x(1-y)\). A binary length-three word is not of type \(0^*1^*\) precisely when it contains a descent, and such a word contains at most one descent. Summing the numbers of descents in the six paths (15), and maximizing independently over their three internal edge bits \(c,f,g\), bounds the sum from above by
\[
\boxed{
(a\oplus b)+(d\oplus e)+
\max(a,1-e)+\max(b,1-d)+
\max(a+b,2-d-e).
}
\tag{16}
\]
Indeed, the comparisons \(a\leftrightarrow b\) and \(d\leftrightarrow e\) yield the two XOR terms; the two-comparison chains \(a\to f\to e\) and \(b\to g\to d\) produce the next two maxima; the comparisons \(a\to c,b\to c,c\to d,c\to e\) give the final maximum. Expression (16) never exceeds five: if \(d=e=0\), it is \(4+(a\oplus b)\le5\); if \(d=e=1\), it is \((a\oplus b)+2(a+b)\le4\); and if \(d\ne e\), direct consideration of the four choices for \((a,b)\) gives maximum five. Hence at least one of the six paths has no descent. So two same-parity roots cannot both be unfavorable.

There are four roots of each Hamming parity. Each parity class has at most one unfavorable root, proving \(|A_0|\ge6\). Interchanging the two colors proves the identical bound for \(A_1\).

To witness sharpness, take the two-cube coloring \(h\) with \(A_0(h)=\{01,10,11\}\) from the Cartesian-factorization Subsection, and form \(g=h\boxtimes q\), where \(q\) colors the edges of the one-cube uniformly. Product factorization gives \(|A_0(g)|=3\cdot2=6\). QED.

**Theorem 14 (three-exception paired-root theorem).** Let \(f\) be an arbitrary binary coloring of \(Q_d\), \(d\ge3\). If all but at most three dimension classes have colors independent of location, then
\[
\boxed{|P(f)|\ge2^{d-1}.}
\tag{17}
\]
The bound is sharp. Consequently any hypothetical paired-root-free coloring must have at least **four nonuniform direction classes**.

*Proof.* Extend the collection of nonuniform directions to a three-element set \(S\), and partition the others into \(A\) (uniformly zero) and \(B\) (uniformly one). Every root has form \((u,x,v)\in Q_A\times Q_S\times Q_B\), with \(x\in Q_3\). Traverse all \(A\)-dimensions first, then a complete nondecreasing \(0^*1^*\) geodesic in the \(S\)-fiber with outside location \((\bar u,v)\), and finally all \(B\)-dimensions. This yields a \(0^*1^*\) full path provided \(x\in A_0(g_{\bar u,v})\). Traverse all \(B\)-dimensions first, then a nonincreasing \(1^*0^*\) path in the \(S\)-fiber with outside location \((u,\bar v)\), then all \(A\)-dimensions. This yields the opposite path orientation provided \(x\in A_1(g_{u,\bar v})\).

The two fiber colorings need not be related. Nevertheless Lemma 13 guarantees that each of the two feasible-root sets in \(Q_3\) has at least six of the eight vertices. Their intersection has at least four elements. Thus for each fixed outside configuration \((u,v)\), at least four values of \(x\) make the same root paired. There are \(2^{d-3}\) outside configurations, giving (17).

Sharpness follows from \(f=h\boxtimes q\) on three dimensions, where \(h\) is the preceding extremal two-cube coloring and \(q\) is a monochromatic one-cube; by the previously proved factorization \(|P(f)|=2\cdot2=4=2^{3-1}\). Add any number of uniform-factor dimensions to preserve the paired-root fraction one half. QED.

**Proof-search consequence.** The paired-root exclusion threshold for the number of nonuniform edge-direction classes rises from three to **four**, with no assumption on how any exceptional class depends on other vertex bits. The underlying structural ingredient is a two-source descent-count certificate in \(Q_3\), which is small but powers an unrestricted all-dimensional theorem. Extending this fiber method to four or five arbitrary exception dimensions requires a suitable cross-intersection statement for their nondecreasing and nonincreasing feasible-root families, not a general density bound in arbitrarily many dimensions.

#### Four unrestricted exceptional directions by a finite computer-assisted lemma

Define
\[
m_k=\min_{g:E(Q_k)\to\{0,1\}}|A_0(g)|,
\]
where \(A_0(g)\) is the set of roots admitting a full \(0^*1^*\) geodesic.

**Theorem 15 (general fiber-transfer principle).** If a binary edge coloring \(f\) of \(Q_d\) has at most \(k\) nonuniform direction classes, then
\[
\boxed{|P(f)|\ge2^{d-k}\max(0,2m_k-2^k).}
\tag{18}
\]

*Proof.* Enlarge the nonuniform direction set to a \(k\)-element block \(S\), and partition the remaining directions into uniform zero block \(A\) and uniform one block \(B\). For each outside root \((u,v)\in Q_A\times Q_B\), a nondecreasing full path is formed by all \(A\)-steps, then a nondecreasing full path in the \(S\)-fiber at \((\bar u,v)\), then all \(B\)-steps. The opposite orientation is formed by all \(B\)-steps, then a nonincreasing full path in the \(S\)-fiber at \((u,\bar v)\), then all \(A\)-steps. Each of these two arbitrary fiber colorings has a favorable-root set of size at least \(m_k\); interchange zero and one to cover the second orientation. Their intersection has size at least \(\max(0,2m_k-2^k)\), and there are \(2^{d-k}\) outside roots. QED.

The preceding analytical lemmas give \(m_1=2,m_2=3,m_3=6\). We next give a finite computational evaluation at four dimensions.

**Lemma 16 (computer-assisted four-cube root minimum).** Every binary coloring of the 32 undirected edges of \(Q_4\) has at least nine roots admitting a full nondecreasing color word, and this bound is attained:
\[
\boxed{m_4=9.}
\tag{19}
\]

*Reproducible binary-integer certificate.* Introduce binary edge colors \(x_e\) for the 32 cube edges. For each ordered consecutive-edge pair \((e,f)\) appearing on any rooted four-step full geodesic, introduce a binary variable \(y_{ef}\) with the three constraints
\[
y_{ef}\le x_e,\quad y_{ef}+x_f\le1,\quad x_e-x_f-y_{ef}\le0.
\tag{20}
\]
Thus \(y_{ef}\) is one precisely at a descent from color one to color zero. Introduce a binary variable \(b_v\) at each of the sixteen roots. For all \(24\) direction permutations \(\pi\), impose
\[
b_v\le\sum_{j=1}^{3}y_{e_j(v,\pi),e_{j+1}(v,\pi)}.
\tag{21}
\]
Maximize \(\sum_v b_v\). This binary integer program contains 32 edge-color bits, 192 distinct directed comparison bits, 16 unfavorable-root bits, and 960 linear inequalities. The integer solver HiGHS via SciPy reported a certified optimizer objective of seven unfavorable roots, a matching branch-and-bound dual bound of seven, a zero optimality gap, and 328 explored nodes. An independent path-evaluation routine checked a returned feasible assignment and counted nine favorable roots.

All input coefficients in (20)-(21) are integers, and the indexing is explicit: enumerate the 32 cube edges by direction \(i=0,1,2,3\), followed by vertex integers \(v=0,\ldots,15\) with bit \(i\) zero; edge \(e=(v,v\oplus2^i)\). Enumerate roots in integer order and the 24 permutations of the four directions. The displayed constraints can therefore be reproduced using any binary integer-programming implementation. An attaining coloring without a solver is \(h\boxtimes h\), the product of two square colorings \(h\) each with \(|A_0(h)|=3\), giving \(|A_0(h\boxtimes h)|=9\) by Cartesian factorization.

The lemma is labeled **computer-assisted**. A pen-and-paper certificate for the lower bound would be preferable for a final publication; the integer solver's dual bound is the computational evidence for the exhaustive optimum.

**Corollary 17 (four-exception paired-root theorem, computer-assisted).** Any coloring of \(Q_d\), \(d\ge4\), with at most four nonuniform dimension classes satisfies
\[
\boxed{|P(f)|\ge2^{d-3}.}
\tag{22}
\]
Thus a hypothetical paired-root-free coloring requires at least **five** nonuniform direction classes.

*Proof.* Substitute \(m_4=9\) into Theorem 15. QED.

**Limitation of cardinality-only transfer.** The \(r\)-fold Cartesian product of the extremal square coloring has \(m_{2r}\le3^r\). For \(k=6\), this gives \(m_6\le27<32\), so the numerical intersection term in (18) need not be positive once six arbitrary direction classes are permitted. Further progress toward full NORI1 requires structural compatibility, not just favorable-root cardinalities.

##### Cross-orientation intersection for crossed square factorizations

For a cube-edge coloring \(f\), let \(A_0(f)\) and \(A_1(f)\) be the roots admitting full dimension-simple geodesics with color words \(0^*1^*\) and \(1^*0^*\), respectively. Fix two perfect matchings \(M,N\) of the \(2r\) dimensions. Suppose \(f\) is a Cartesian product of arbitrary colored squares on the pairs in \(M\), and \(g\) is a product of arbitrary colored squares on the pairs in \(N\). Let \(c(M,N)\) be the number of connected components of the multigraph \(M\cup N\), which is a union of even cycles, allowing parallel-edge cycles of length two.

**Lemma 1 (binary cycle feasibility).** A cycle of \(m\ge2\) Boolean variables, with one constraint per consecutive pair forbidding at most one two-bit pattern, has at least two satisfying assignments.

*Proof.* Add an arbitrary forbidden pattern to every unconstrained pair. Delete the last constraint. Either initial bit can be extended greedily across the remaining path, because for each fixed earlier bit at least one choice of the next bit is permitted. The deleted constraint can reject at most one of the two constructed assignments, since they have different initial bits. Hence a satisfying assignment exists.

If there were only one solution, changing any single variable would have to violate an adjacent constraint. Each currently satisfied pair constraint can forbid changing at most one of its endpoints, because its forbidden two-bit pattern differs from the current pair in at least one bit. With \(m\) constraints guarding \(m\) variables, each constraint must guard one endpoint. Thus on every edge the forbidden pattern differs from the solution's pattern in one bit. Complementing all variables changes both bits on every edge and avoids all forbidden patterns, giving a second solution. QED.

**Theorem 2 (cross-matching feasible-root intersection).**
\[
\boxed{|A_0(f)\cap A_1(g)|\ge2^{c(M,N)}.}
\tag{1}
\]
The bound is sharp for every pair \(M,N\).

*Proof.* By the two-cube favorability lemma, each of \(A_0\) and \(A_1\) excludes at most one of the four roots of a colored square. The Cartesian product property identifies common feasible roots with Boolean assignments satisfying one such forbidden-pattern constraint on each edge of \(M\cup N\). Apply Lemma 1 independently to its cycle components.

For sharpness, put on every square the two-cube coloring \(h\) with \(A_0(h)=Q_2\setminus\{00\}\), \(A_1(h)=Q_2\setminus\{11\}\). The \(M\)-constraints then say \(x_u+x_v\ge1\), while the \(N\)-constraints say \(x_u+x_v\le1\). On a component containing \(2s\) variables, summing the inequalities in either matching yields \(\sum x_i\ge s\) and \(\sum x_i\le s\). All inequalities are tight, so every pair of neighboring bits is complementary. Each even cycle permits just its two alternating assignments, attaining (1). QED.

**Corollary 3 (two common roots in unbounded dimension).** Take \(M=(1,2),(3,4),\ldots,(2r-1,2r)\) and \(N=(2,3),(4,5),\ldots,(2r,1)\). Their union is a single \(2r\)-cycle. The corresponding \(h\)-product colorings have \(|A_0(f)|=|A_1(g)|=3^r\), but their intersection consists of only the two alternating bit strings. For \(r\ge3\), both feasible sets are smaller than half the cube, yet the intersection remains nonempty through a structural, rather than cardinality, argument.

**Open sufficient strengthening of NORI1.** Ask whether arbitrary binary cube-edge colorings \(f,g\) satisfy \(A_0(f)\cap A_1(g)\ne\varnothing\). Choosing \(g=f\) would yield a paired root and hence NORI1 in one higher dimension. This proposed cross-favorability principle is stronger than NORI1 and may fail in general; Theorem 2 proves it only for independent Cartesian products of colored squares.


#### Cross-orientation overlap for pseudoforest incidence graphs

The preceding crossed-perfect-matching theorem considers Cartesian products of colored squares. The correct ambient structure is the **factor-incidence multigraph** of any two Cartesian decompositions: vertices are factor blocks, one part for each coloring, and every cube direction is an edge joining the two factor blocks that contain it. A substantially wider all-dimensional overlap theorem holds whenever that multigraph is a pseudoforest.

Let \(B\) be a nonempty finite dimension set. Let \(g,h\) be arbitrary binary colorings of \(Q_B\) which each factor as Cartesian products of edge-colorings on disjoint nonempty direction blocks,
\[
g=\prod_{\alpha\in I}g_\alpha,\qquad h=\prod_{\beta\in J}h_\beta.
\]
Write \(\mathcal U=\{U_\alpha:\alpha\in I\}\) and \(\mathcal V=\{V_\beta:\beta\in J\}\) for their partitions of \(B\). Define the bipartite multigraph \(H(\mathcal U,\mathcal V)\) with one vertex for each \(U_\alpha,V_\beta\) and one edge labeled \(i\in B\) connecting its two containing blocks. Parallel edges are allowed. Assume each individual factor's oriented favorable-root set has density at least \(3/4\):
\[
|A_0(g_\alpha)|\ge 3\cdot 2^{|U_\alpha|-2},
\qquad
|A_1(h_\beta)|\ge 3\cdot 2^{|V_\beta|-2},
\tag{4}
\]
interpreted as an ordinary real inequality, so singleton factors (both roots favorable) qualify. The small-cube root-majority theorem supplies these bounds automatically for arbitrary factors of sizes one, two, or three.

**Lemma 4 (binary pseudoforest constraint extension).**
Let \(H\) be a finite multigraph, and give each vertex \(v\) a nonempty set \(L_v\subseteq\{0,1\}^{E(v)}\) of permitted assignments to its incident edges, with
\[
|L_v|\ge \tfrac34\,2^{\deg v}.
\]
If every connected component of \(H\) is a tree or contains precisely one cycle (counting a pair of parallel edges as a two-cycle), then the edge-variable constraint system has at least \(2^{c(H)}\) global satisfying assignments, where \(c(H)\) is the number of connected components.

*Proof.* Work componentwise. For any vertex \(v\) and prescribed bit on one incident edge, at least one choice for its other incident bits is permitted: the forbidden set has size at most \(2^{\deg v-2}\), smaller than the size \(2^{\deg v-1}\) of either one-bit slice. Thus, in a tree component, choose either value on any one edge, then extend its endpoint assignments and proceed away from that edge through the tree. Every prescribed entering-edge bit has a permitted continuation. Both initial values extend, so the component has at least two solutions.

For a unicyclic component, first consider the variables on the unique cycle. At any cycle vertex, fixing the two incident cycle-edge bits leaves \(2^{\deg v-2}\) choices of its other incident edges. Since the total forbidden set has at most this size, **at most one** of the four cycle-bit pairs can have no permitted continuation. Thus each cycle vertex forbids at most one of the four possible assignments to its two neighboring cycle edges. The binary cycle feasibility lemma from Theorem 2 proves that the resulting cycle constraints have at least two solutions, including for parallel-edge two-cycles. At each cycle vertex choose a permitted completion of its off-cycle edge bits; then extend outward along the attached trees, using the one-prescribed-bit extension property from the first paragraph. The choices of cycle solutions produce distinct complete assignments. Finally distinct components have disjoint edge-variable sets, so their solution counts multiply. \(\square\)

**Theorem 5 (cross-factorization intersection beyond matchings).**
Under (4), if the factor-incidence multigraph \(H(\mathcal U,\mathcal V)\) is a pseudoforest, then
\[
\boxed{|A_0(g)\cap A_1(h)|\ge 2^{c(H)}\ge2.}
\tag{5}
\]
In particular, this holds for any two Cartesian decompositions into arbitrarily colored \(Q_1,Q_2,Q_3\) factors whose incidence multigraph is a pseudoforest. The block pairings and block sizes may differ between the two colorings.

*Proof.* A Cartesian-product coloring has a favorable root precisely when each constituent factor has a favorable root for the same orientation: favorable factor paths concatenate in sorted order of their color blocks, and conversely deleting the other factor steps from a favorable full geodesic preserves monotonicity. Thus a common root is an assignment to the \(|B|\) direction bits satisfying, at every factor vertex of \(H\), the corresponding local allowable root pattern. Each vertex's allowed fraction is at least \(3/4\) by (4). The lemma supplies at least \(2^{c(H)}\) compatible assignments. \(\square\)

**Corollary 6 (pseudoforest terminal-fiber gluing).**
Split the directions of an arbitrary coloring \(F\) as \(A\sqcup B\), with all \(A\)-edge colors independent of the \(B\)-bits, inducing outer coloring \(f\). Suppose that for every outer vertex \(x\), the \(B\)-fiber coloring \(g_x\) factors into arbitrary colored blocks of sizes at most three, and for every pair \(x,y\) the incidence multigraph of their two factor partitions is a pseudoforest. Then
\[
\boxed{|P(F)|\ge2|P(f)|.}
\tag{6}
\]
More precisely, for each outer paired root \(z\), with two chosen favorable outer paths and respective switch-seam vertices \(v_z,w_z\),
\[
|P(F)|\ge\sum_{z\in P(f)}2^{c(H_{v_z,w_z})}.
\]
Here \(H_{v_z,w_z}\) is the incidence multigraph of the two fiber partitions. Every constructed witness remains a full dimension-simple geodesic.

*Proof.* By path reversal, \(A_1(g)=\overline{A_0(g)}\). Therefore Theorem 5 ensures at least \(2^{c(H)}\) fiber roots in \(A_0(g_{v_z})\cap\overline{A_0(g_{w_z})}\). Insert the two corresponding favorable fiber paths at the zero-to-one seams of the two outer paths starting at antipodal roots \(z,\bar z\), respectively. Each insertion preserves the monotone word and uses each \(B\)-direction once; the outer paths use each \(A\)-direction once. Distinct fiber roots yield distinct paired roots, giving the bounds. \(\square\)

**Closure perspective.** The earlier two-matching theorem corresponds to factor-incidence graphs of maximum degree two, hence disjoint paths and cycles. Theorem 5 permits arbitrary factor-vertex branching and all three-dimensional factors, as long as the incidence graph has at most one independent cycle per component. Thus the real obstruction to this local intersection *method* is a factor-incidence component of cyclomatic number at least two. That is not asserted to be an obstruction to the paired-root conjecture itself; additional coloring-specific structure may still force intersections in multicyclic components.


#### Multicyclic cross-factor intersections: theta and cactus

Assume every factor vertex permits at least three quarters of the assignments to its incident binary edge variables. A vertex of degree one permits both bits, a vertex of degree two forbids at most one of four pairs, and a vertex of degree three forbids at most two of eight triples.

**Lemma (path reduction).** A chain of degree-two vertices, each forbidding at most one pair, induces a terminal two-bit relation forbidding at most one pair. This follows inductively: composing two binary relations that each omit at most one of four pairs still omits at most one, since blocking both possible values of the intermediate bit consumes the unique forbidden pair in each relation. A direct edge identifies its endpoint bit copies.

**Theorem (theta intersection).** Two trivalent vertices joined by three internally disjoint paths, with any number of degree-two internal vertices, have a compatible global assignment under the stated local constraint bound, including when some paths are direct parallel edges.

*Proof.* Contract the paths to their endpoint relations. Each indirect relation contains at least three pairs, so it has nonempty rows and columns and at most one row of size one. The allowed incident-bit triple sets U,V at the two trivalent vertices each have size at least six.

For zero direct paths, at least four start triples have at least four compatible end triples. U contains one such start, while V excludes at most two endings. For one direct path, write a_t,b_t for the forbidden counts in the two four-pattern slices of the junction sets having shared bit t. Some t has a_t+b_t at most two. If either slice is full, compatibility follows from nonempty rows and columns; otherwise both slices contain at least three patterns, and some permitted start has at least two permitted end options, meeting the other size-three slice. For two direct paths, each of the four shared two-bit values t induces sets X_t,Y_t of possible last bits. If no value t were compatible with the remaining indirect relation, then at each t either X_t or Y_t would be empty, or both would be singletons. This requires at least two excluded junction patterns per t, totaling eight, while only four exclusions are allowed. For three direct paths, U and V intersect in at least four triples. QED.

**Lemma (pendant-cycle extension).** For a cycle with one extra bridge bit at one trivalent attachment vertex, fixing that bridge bit leaves at least two admissible patterns for the two cycle edges at the attachment. The complementary degree-two path admits at least three endpoint pairs by path reduction. Their intersection is nonempty, so the cycle can be solved for either bridge-bit choice.

**Theorem (subcubic cactus intersection).** Every cactus multigraph of maximum degree three has a global solution to three-quarter-dense local binary edge constraints.

*Proof.* Root its bridge/cycle block tree. Terminal branches composed of trees extend from either choice of their entering edge bit because each local constraint admits a continuation after fixing one incoming bit. Terminal cycle blocks extend from either choice of their attachment bit by the pendant-cycle lemma, after treating attached tree branches. Remove terminal blocks inductively, retaining their ability to extend any parent-bridge bit. The remaining root vertex or cycle is solvable by direct local feasibility or the binary-cycle lemma. Restore removed blocks in reverse order. QED.

**Corollary (dimension-simple seam gluing).** If two conditional fiber colorings factor into blocks each with at least three quarters of roots favorable in the required orientation, their favorable-root sets intersect whenever every connected block-incidence component is a pseudoforest, a theta, or a subcubic cactus. Arbitrary colored factors of dimension one, two, or three satisfy the density requirement. Inserting two compatible fiber paths at the opposite outer switch seams preserves full dimension-simplicity and gives a paired root.

Cycles linked through bridge trees and the basic three-path multicyclic core therefore cannot obstruct this cross-factor intersection method. The remaining unresolved structure involves more highly connected multicyclic factor-incidence blocks, or individual factors with smaller favorable-root density.


#### Unrestricted crossing of all one-, two-, and three-dimensional Cartesian factors

The preceding pseudoforest, theta, and cactus theorems controlled the topology of the block-incidence graph. A stronger *linear matroid selection* argument removes **every incidence restriction** for arbitrary factors of sizes one, two, and three. It also identifies a sufficient local condition for larger factors.

Let \(B\) be a finite dimension set, \(m=|B|\), and let \(g,h\) be arbitrary binary cube-edge colorings each expressible as a Cartesian product of factor colorings across a partition of \(B\). The two partitions may overlap in any fashion. For an orientation \(\sigma=0,1\), denote by \(A_\sigma(g)\) the roots of a full dimension-simple geodesic whose color word has form \(0^*1^*\) when \(\sigma=0\), or \(1^*0^*\) when \(\sigma=1\). Empty color blocks are permitted.

A factor with variable set \(U\) and allowed root set \(A\subseteq\mathbb F_2^U\) has the **two-dimensional safe-check property** if it admits a two-dimensional binary linear subspace \(L\subseteq\mathbb F_2^U\) such that for every nonzero \(v\in L\), some affine parity equation
\[
\boxed{v\cdot x=b_v}
\tag{10}
\]
has its full solution hyperplane inside \(A\). The value \(b_v\) may depend on \(v\).

**Lemma 16 (affine-span criterion for safe checks).** Let \(F=\mathbb F_2^U\setminus A\) be the unfavorable root set, with \(s=|U|\ge2\). If the affine span of \(F\) has dimension at most \(s-2\), then \(A\) has the two-dimensional safe-check property. In particular, every subset of \(\mathbb F_2^2\) omitting at most one point and every subset of \(\mathbb F_2^3\) omitting at most two points has this property.

*Proof.* If \(F\) is nonempty, fix \(p\in F\) and let \(D=\operatorname{span}\{x+p:x\in F\}\). Its dimension is the affine dimension of \(F\), at most \(s-2\). Choose a two-dimensional subspace \(L\subseteq D^\perp\). For any nonzero \(v\in L\), the scalar \(v\cdot x\) equals \(v\cdot p\) on every forbidden root. The opposite parity equation \(v\cdot x=1+v\cdot p\) therefore excludes all of \(F\). If \(F\) is empty, choose any two-dimensional \(L\); both right-hand sides yield allowed hyperplanes. The final assertions use the respective bounds on the cardinality of \(F\). \(\square\)

**Lemma 17 (two-fold support and independent parity selectors).** Let \(U_1,\ldots,U_k\) be two-dimensional linear subspaces of \(\mathbb F_2^m\), each supported on a subset \(B_i\subseteq[m]\), such that each ground-set position occurs in at most two of the subsets \(B_i\). Then there exist linearly independent nonzero representatives \(u_i\in U_i\) for all \(i=1,\ldots,k\).

*Proof.* Use Rado's independent-transversal theorem for a family of subsets of a representable matroid: it suffices to prove
\[
\dim\left(\sum_{i\in S}U_i\right)\ge|S|
\quad\text{for every }S\subseteq[k].
\tag{11}
\]
Fix \(S\), put \(W=\sum_{i\in S}U_i\), and write \(r=\dim W\). Choose an information set \(J\subseteq[m]\) of size \(r\) on which the projection \(W\to\mathbb F_2^J\) is injective; such a set exists by selecting pivot columns in a basis matrix of \(W\). Its restriction to each \(U_i\subseteq W\) is also injective. Since \(\dim U_i=2\), at least two positions of \(J\) must belong to \(B_i\). Each position of \(J\) belongs to at most two \(B_i\), so double counting gives
\[
2|S|\le\sum_{i\in S}|J\cap B_i|\le2|J|=2r.
\]
This proves (11) and hence the independent-representative assertion. \(\square\)

**Theorem 18 (universal cross-factor favorable-root intersection).** Suppose each non-singleton factor of \(g\) or \(h\), in its respective required orientation, has the two-dimensional safe-check property, while singleton factors permit both possible roots. Let \(k\) be the total number of non-singleton factors across the two decompositions. Then
\[
\boxed{|A_0(g)\cap A_1(h)|\ge 2^{m-k}\ge1.}
\tag{12}
\]
In particular, this conclusion holds for **every pair of Cartesian products of arbitrary colored \(Q_1,Q_2,Q_3\) factors**, with absolutely no restriction on their two partitions or their factor-incidence multigraph.

*Proof.* For each non-singleton factor choose a two-dimensional safe-check subspace as above, embedded by zeros in the \(m\)-bit ground space. Each ground dimension belongs to precisely one factor of \(g\) and one factor of \(h\), so it belongs to at most two such subspace supports. Apply Lemma 17 to choose a linearly independent safe-check vector \(u_v\) for every non-singleton factor \(v\). Choose the corresponding right-hand side \(b_v\) from its safe-check property. The affine linear system
\[
u_v\cdot x=b_v\qquad\text{for all chosen factors }v
\tag{13}
\]
has \(k\) independent equations in \(m\) binary variables, and therefore admits \(2^{m-k}\) solutions. Each solution satisfies every factor's safe equation and hence every local favorable-root requirement. For singleton factors both bits are always favorable. Finally favorable-root sets of Cartesian-product colorings are Cartesian products of the local favorable-root sets: necessity follows by deleting steps in other blocks from a monotone full path, and sufficiency by taking full monotone factor paths and interleaving all their zero prefixes before all their one suffixes. Thus all solutions of (13) belong to \(A_0(g)\cap A_1(h)\). The small-cube majority results give at most one unfavorable root in \(Q_2\) and at most two in \(Q_3\), so Lemma 16 applies to every possible factor of those sizes. \(\square\)

**Corollary 19 (unrestricted terminal-fiber gluing for variable small-block partitions).** Let the dimensions of an arbitrary coloring \(F\) split into outer directions \(A\) and fiber directions \(B\), with all outer-edge colors independent of fiber bits, inducing coloring \(f\). Suppose that for every outer vertex \(x\), its fiber coloring \(g_x\) is an arbitrary Cartesian product of colored factors of sizes at most three. The factorization and block partition may vary freely with \(x\). For any \(z\in P(f)\), choose full favorable outer paths from \(z\) and \(\bar z\) and let \(k_z\) be the total number of nonsingleton factors across the two fiber colorings encountered at their respective seam vertices. Then
\[
\boxed{
|P(F)|\ge\sum_{z\in P(f)}2^{|B|-k_z}\ge|P(f)|.
}
\tag{14}
\]
Thus no least-dimensional paired-root counterexample can have a terminal fiber block whose conditional colorings all factor into blocks of size at most three, **even when their block decompositions overlap arbitrarily**. The full paths produced by insertion are dimension-simple.

*Proof.* By full-path reversal, \(A_1(g_{w_z})=\overline{A_0(g_{w_z})}\). Apply Theorem 18 to \(g_{v_z},g_{w_z}\) to obtain at least \(2^{|B|-k_z}\) fiber roots in the required opposite-orientation intersection. At the two switch seams insert full favorable fiber geodesics starting respectively from such a root and from its antipode. The resulting full paths have both monotone color orientations and traverse every dimension once. Summing distinct paired starting roots gives (14). \(\square\)

**Path to closure.** The obstruction has moved away from the *geometry of overlapping small factors* altogether. Linear-matroid selection solves all such overlaps, even where their factor-incidence graph has arbitrarily high cycle rank. What remains are conditional fiber colorings with **indecomposable blocks of dimension at least four**, or larger blocks whose unfavorable-root affine span has codimension below two. The natural next task is to seek a safe-check substitute with higher-dimensional coefficient modules or supported path chains on those irreducible blocks, preserving the two-fold overlap rank argument where possible.


#### General rank-overlap principle and failure of safe hyperplanes in higher ranks

**Theorem (linear safe-check selection at matching overlap multiplicity).** Let local permitted-pattern sets A_v depend on bit sets B_v among m global binary variables. Suppose each bit occurs in at most t of the sets B_v. Suppose for every factor v there is a binary linear space L_v of dimension at least t, supported on B_v, whose every nonzero vector u admits a right-hand side b_u such that the full affine solution hyperplane u·x=b_u lies in A_v. Then all local constraints have a common solution; indeed they contain an affine solution space of at least 2^(m-k) points, where k is the number of factors.

*Proof.* For any subset S of factors let W be the sum of their L_v, with rank r. Choose r pivot positions on which projection of W is injective. For every v in S the projection of L_v is injective, so those pivot positions contain at least t elements of B_v. Every pivot position belongs to at most t factor supports. Double counting gives t|S|<=tr, hence rank(W)>=|S|. Rado's linear independent-transversal theorem selects one independent vector u_v from each L_v. Give every selected vector its safe right-hand side; all k affine equations are independent, and their 2^(m-k) common solutions satisfy every factor. QED.

**Corollary (unfavorable affine-span criterion).** The theorem applies whenever each nonempty forbidden pattern set F_v has affine span dimension at most |B_v|-t. Pick one excluded pattern p. The subspace orthogonal to all differences q-p with q in F_v then has dimension at least t; for every nonzero vector in it, the affine equation whose bit value is opposite to its value at p avoids every excluded pattern. Empty forbidden sets impose no restriction.

**Proposition (an all-dimensional barrier to linear safe checks).** For every even d=2r>=4, set the color on an edge in direction i to the parity of all vertex bits other than bit i. The set of roots supporting full 0*1* paths has Hamming weights r or r+(-1)^r, as proved by the rooted parity-reader count in Article XIV. Thus all middle-layer roots of weight r are paired with their antipodes. Yet the favorable-root set contains no affine hyperplane. Its complement contains the zero vector and all d unit vectors because weights zero and one are excluded when r>=2. Those d+1 excluded patterns affinely span the full d-dimensional binary cube; they cannot all lie on one affine hyperplane. Hence no affine hyperplane can avoid them.

**Closure target.** Two-fold factor overlap is solved when every block possesses two independent safe-check directions; arbitrary colored Q2 and Q3 factors satisfy this. For larger indecomposable blocks, favorable paths may exist abundantly despite there being no safe affine parity equation. A full proof of NORI1 therefore needs a richer supported intersection object, or a higher-codimension substitute for safe parity hyperplanes.

#### Three-family overlap obstruction on four bits

**Proposition.** Let g1,g2,g3 be Cartesian products of colored Q2 factors on four dimensions, using the three matchings M1={(0,1),(2,3)}, M2={(0,2),(1,3)}, M3={(0,3),(1,2)}. Choose the colored-square favorable-root exclusions on these six pairs as (0,1):00, (0,2):00, (0,3):10, (1,2):11, (1,3):01, (2,3):01. Every prescribed excluded pattern is realizable by a colored Q2 factor through translation of the sharp three-favorable-root example.

Then A0(g1) intersect A0(g2) intersect A0(g3) is empty, although the intersection of any two of these favorable-root sets is nonempty by the crossed-square matching theorem.

*Proof.* Avoiding patterns 00 on pairs (0,1) and (0,2) says x0 OR x1 and x0 OR x2. Avoiding pattern 11 on pair (1,2) says NOT x1 OR NOT x2. These three constraints imply x0=1, since x0=0 forces x1=x2=1. Avoiding pattern 10 on (0,3) then forces x3=1. Avoiding patterns 01 on (1,3) and (2,3) forces x1=x2=1, contradicting the forbidden 11 pattern. No common root exists. All two-family intersections exist by the preceding general matroid theorem. QED.

The result shows the two-fold-support parameter in the safe-check matroid theorem cannot be replaced by three-family Helly without stronger local safety rank. It does not produce a counterexample to the paired-root theorem, which involves two orientations of one coloring.


#### Sharp three-quarter threshold for local cubic root constraints

**Theorem (density threshold for bipartite cubic factor incidence).** In any bipartite multigraph with binary variables on edges and permitted local patterns on each vertex star, if all degree-three vertices permit at least six of eight bit triples, all degree-two vertices at least three of four pairs, and all degree-one vertices both bits, then there is a satisfying global assignment. However, replacing six of eight by five of eight at degree-three vertices is not sufficient, even for the simple bipartite graph \(K_{3,3}\).

*Sufficiency.* At each degree-two or degree-three vertex the forbidden patterns have affine dimension at most the star degree minus two, yielding a two-dimensional subspace of safe parity-check vectors. Every original edge variable lies in at most two vertex stars. The independent-transversal theorem established earlier therefore chooses one linearly independent safe parity-check equation per nonsingleton vertex. Their full-rank affine system has a solution, which meets all the local restrictions.

*Sharpness.* Put nine binary variables \(x_{ij}\) on \(K_{3,3}\), for \(i,j\in\{0,1,2\}\). At its row vertices prescribe
\[
\begin{array}{ll}
R_0:&\neg x_{01}\ \lor\ (\neg x_{00}\land x_{02}),\\
R_1:&\neg x_{12}\ \lor\ (x_{10}\land\neg x_{11}),\\
R_2:&x_{22}\ \lor\ (x_{20}\land x_{21}),
\end{array}
\]
and at the three column vertices prescribe
\[
\begin{array}{ll}
C_0:&x_{00}\ \lor\ (\neg x_{10}\land x_{20}),\\
C_1:&x_{01}\ \lor\ (x_{11}\land\neg x_{21}),\\
C_2:&x_{12}\ \lor\ (\neg x_{02}\land\neg x_{22}).
\end{array}
\]
Every rule accepts five of the eight assignments to its own three variables: it is one Boolean input condition OR a conjunction of two independently varying input conditions.

Suppose a global assignment satisfied the rules. If \(x_{12}=0\), then \(C_2\) gives \(x_{02}=x_{22}=0\); \(R_2\) gives \(x_{20}=x_{21}=1\); \(C_1\) gives \(x_{01}=1\); and \(R_0\) requires \(x_{02}=1\), contradiction. If \(x_{12}=1\), then \(R_1\) gives \(x_{10}=1,x_{11}=0\); \(C_0\) gives \(x_{00}=1\); \(R_0\) gives \(x_{01}=0\); and \(C_1\) requires \(x_{11}=1\), contradiction. Hence the six five-eighths-dense constraints have no joint solution. \(\square\)

**Research consequence.** Merely knowing that local favorable-root sets have strict majority is not enough to glue two arbitrarily crossing factor partitions. The three-quarter lower bound guaranteed for every colored \(Q_3\) factor is sharp as a general cardinality hypothesis on cubic vertex constraints. These abstract five-eighths permitted sets need not be realizable as favorable-root sets of cube-edge colorings, so this does not challenge NORI1 or the preceding small-factor gluing theorem. It rules out the proposed density-only extension and directs attention to stronger algebraic invariants of large root sets.



#### One exceptional safe-parity factor: an integral-rank strengthening

The two-fold-support matroid argument tolerates one factor whose family of safe parity-check vectors has rank **one** instead of two. No increase in the rank of the remaining factors is required. The reason is the integral rounding in the information-set double count.

**Lemma 25 (nonuniform rank-overlap bound).** Let \(L_1,\ldots,L_k\subseteq\mathbb F_2^m\) be linear spaces supported respectively on \(B_1,\ldots,B_k\subseteq[m]\). Suppose each bit position occurs in at most \(t\) of the supports \(B_i\). Then for every \(S\subseteq[k]\),
\[
\boxed{
\dim\left(\sum_{i\in S}L_i\right)
\ge \left\lceil\frac{\sum_{i\in S}\dim L_i}{t}\right\rceil.
}
\tag{21}
\]

*Proof.* Put \(W=\sum_{i\in S}L_i\), \(r=\dim W\), and select \(r\) pivot positions \(J\subseteq[m]\) such that projection onto \(J\) is injective on \(W\). Its restriction to each \(L_i\) is injective, so \(|J\cap B_i|\ge\dim L_i\). Counting incidences and using the support multiplicity bound gives
\[
\sum_{i\in S}\dim L_i
\le\sum_{i\in S}|J\cap B_i|
\le t|J|=tr.
\]
Take ceilings. \(\square\)

**Theorem 26 (one rank-one exception in two-fold fiber gluing).** Consider two arbitrary Cartesian decompositions of the same binary root variables, with a local allowed set at each factor. At every factor except possibly one, assume the two-dimensional safe-check property of Theorem 18; at the exceptional factor assume only that its permitted set contains some full affine parity hyperplane. Singleton factors permit both roots. Then the two products of allowed local sets have a common root.

More precisely, if \(m\) is the number of shared bit variables and \(k\) is the number of factors imposing a nontrivial permitted-root restriction, there are at least
\[
\boxed{2^{m-k}}
\tag{22}
\]
common roots.

*Proof.* Represent each local safe-check family by a linear subspace \(L_v\) of coefficient vectors, supported on its factor directions. All but one have dimension at least two. The exceptional factor has a nonzero safe coefficient vector, spanning a one-dimensional space. Since each dimension belongs to one factor from each Cartesian decomposition, every bit lies in at most two supports.

Fix any nonempty subfamily \(S\) of size \(s\). If it omits the exceptional factor, the sum of the safe-check ranks is at least \(2s\); if it includes the exception, the sum is at least \(2s-1\). Lemma 25 with \(t=2\) gives
\[
\dim\left(\sum_{v\in S}L_v\right)
\ge\left\lceil\frac{2s-1}{2}\right\rceil=s
\]
in either case. This is the Hall--Rado rank condition. Select linearly independent nonzero safe-check vectors, one per nontrivial factor, and give each its favorable parity right-hand side. The resulting \(k\) affine equations are consistent and admit \(2^{m-k}\) solutions. Every solution belongs to every local permitted-root set by the definition of a safe check. \(\square\)

**Corollary 27 (an exceptional conditional fiber block).** The paired-root seam-lifting theorem remains valid when, at its two conditional fiber states, every local Cartesian factor has a two-dimensional safe-check coefficient space except for one factor across the two decompositions, which may have only a single safe parity hyperplane. In particular, one exceptional factor of any dimension is allowed, provided its feasible-root set contains an affine hyperplane and all other factors meet the two-dimensional condition. The two fiber decompositions may overlap arbitrarily; all constructed full paths remain dimension-simple.

This is a strict enlargement of the previous equal-rank assumption. It does **not** handle a parity-reader factor having no favorable affine hyperplane, nor two unrelated rank-one factors. Those remain potential requirements for a nonlinear or higher-chain proof.



#### Absorbing arbitrary irreducible factors by safe-rank surplus

The independent-transversal method can also accommodate local factors with **no safe affine hyperplane whatsoever**, provided other factors have enough rank surplus to absorb their shared variables. This is relevant to parity-reader-type favorable-root sets and is not a statement about local density alone.

Let the ground binary variable set \(B\) be partitioned in two ways, \(\mathcal U\) and \(\mathcal V\), and impose one permitted-pattern set \(A_D\subseteq\mathbb F_2^D\) for each block \(D\) of either partition. Call a coefficient vector \(u\in\mathbb F_2^D\) *safe* if one of the two affine equations \(u\cdot x=b\) has its entire solution hyperplane inside \(A_D\); a *safe-check space* is a linear subspace all of whose nonzero vectors are safe.

Select any collection \(\mathcal E\subseteq\mathcal U\) of **exceptional blocks on one side**, and put \(W=\bigcup_{D\in\mathcal E}D\). The sets in \(\mathcal E\) are disjoint. Assume their allowed sets are nonempty but make **no** affine-safe-check assumption about them.

**Theorem 28 (arbitrary-factor absorption from neighboring rank surplus).** Suppose every other nontrivial factor block \(D\notin\mathcal E\) admits a safe-check space \(L_D\) satisfying
\[
\boxed{\dim L_D\ge2+|D\cap W|.}
\tag{23}
\]
Singleton factors may instead be completely unrestricted, permitting both root bits. Let \(k\) be the number of nonexceptional factors to which a safe-check equation is applied. Then all local constraints have at least
\[
\boxed{
\left(\prod_{D\in\mathcal E}|A_D|\right)\,
2^{\,|B\setminus W|-k}
}
\tag{24}
\]
joint solutions. In particular, any finite family of large irreducible factors can be absorbed without any safe affine hyperplane of their own, if they lie in one partition and their neighbors carry the stated rank surplus.

*Proof.* Choose permitted assignments independently on every exceptional block \(D\in\mathcal E\). Together they fix the bits in \(W\), and there are \(\prod_{D\in\mathcal E}|A_D|\) choices.

For each remaining factor \(D\), restrict its coefficient space to vectors with zero entries on \(D\cap W\):
\[
L_D'=\{u\in L_D:u|_{D\cap W}=0\}.
\]
Restriction to \(D\cap W\) has rank at most \(|D\cap W|\), so
\[
\dim L_D'\ge\dim L_D-|D\cap W|\ge2.
\]
Every vector in \(L_D'\) involves only unfixed variables and retains its original safe right-hand side, which still guarantees the full local permitted-pattern condition regardless of the fixed bits. Each unfixed bit belongs to at most two remaining factor blocks, one from each partition. Apply the two-fold-support linear independent-transversal theorem to the spaces \(L_D'\) on \(B\setminus W\). Select \(k\) independent safe parity equations; their solution set has \(2^{|B\setminus W|-k}\) points. Each such assignment, combined with the arbitrarily selected permitted exceptional roots, satisfies all local restrictions. The solution sets for distinct exceptional choices are disjoint, establishing (24). \(\square\)

**Corollary 29 (one parity-reader-type conditional factor can be glued).** Suppose two conditional terminal-fiber colorings factor across possibly unrelated direction partitions. One of them may include an arbitrary indecomposable factor \(D_*\), whose favorable-root set is merely assumed nonempty, even if it has no safe affine hyperplane. Assume every other nonsingleton factor \(D\) has a safe-check space of dimension at least \(2+|D\cap D_*|\). Then the two required favorable-root sets intersect, and a paired outer root lifts through the fiber by the usual dimension-simple seam insertion.

For example, if each factor in the opposite partition shares **at most one bit** with \(D_*\) and has at most one forbidden root among its patterns, a factor of size four offers safe-check rank three and can absorb the shared bit. All other colored \(Q_2\) or \(Q_3\) factors offer rank two. This gives a family of intersections in which the exceptional factor may have any dimension and arbitrary nonlinear internal dependencies.

**Scope.** The theorem is conditional on a permitted root in each exceptional factor; it does not establish nonemptiness for an arbitrary cube coloring. It gives an all-dimensional gluing mechanism for locally irreducible factors supported by sufficiently flexible neighbors. When exceptional factors occur on both sides, or neighboring safe-check ranks have insufficient surplus, the method does not guarantee consistency. These cases remain candidates for supported-path or equivariant-index arguments.



#### Hall-deficiency localization of failed root intersections

The rank-overlap inequality also gives an obstruction certificate for any two factorized permitted-root families that do **not** intersect. This is a necessary condition for failure, not a sufficient condition for failure.

**Theorem 30 (a two-unit local deficit is necessary for incompatibility).** Let \(\mathcal U,\mathcal V\) be any two partitions of the same binary dimension set \(B\), and let \(A_D\) be a permitted-root subset on each factor \(D\). For every factor choose any safe-check linear space \(L_D\) (possibly zero-dimensional), embedded in \(\mathbb F_2^B\). If
\[
\boxed{\bigcap_{D\in\mathcal U\cup\mathcal V}\{x:x|_D\in A_D\}
=\varnothing,}
\]
then there exists a nonempty factor subfamily \(S\) for which
\[
\boxed{
\dim\left(\sum_{D\in S}L_D\right)<|S|,
\qquad
\sum_{D\in S}(2-\dim L_D)\ge2.
}
\tag{25}
\]
Equivalently, if every nonempty subfamily has total safe-check rank at least \(2|S|-1\), then all local root constraints have a common assignment.

*Proof.* Suppose all subfamilies met the Hall--Rado rank condition \(\dim\sum_{D\in S}L_D\ge|S|\). Rado's independent-transversal theorem would select one nonzero safe-check vector per factor, the chosen vectors being linearly independent. Giving each vector its permitted parity right-hand side would yield a consistent affine system all of whose solutions lie in the local permitted sets. This contradicts the assumed empty intersection. Thus some subfamily \(S\) has sum rank at most \(|S|-1\).

Every ground-set bit belongs to at most two factor supports, one in each partition. The nonuniform information-set inequality from Lemma 25 gives
\[
\frac12\sum_{D\in S}\dim L_D
\le\dim\left(\sum_{D\in S}L_D\right)
\le |S|-1.
\]
Rearranging proves (25). The contrapositive gives the equivalent compatibility assertion. \(\square\)

**Corollary 31 (where a paired-root gluing obstruction must concentrate).** If a pair of conditional terminal-fiber colorings has disjoint required monotone-root sets, then *any chosen family* of local safe-check spaces must have a subfamily with at least two units of deficiency relative to rank two per factor. Thus a single rank-one factor among rank-two factors cannot prevent root overlap, agreeing with Theorem 26. A no-safe-hyperplane factor can supply two deficiency units by itself; Theorem 28 explains a separate mechanism by which sufficient neighboring rank surplus can nevertheless absorb such a factor.

**Closure use.** This converts failure of affine-safe-check gluing into a rank-deficient *subcollection* of interacting factors. A future supported-chain or Smith-index proof need not repair all factor overlaps uniformly: it may instead localize its obstruction to one Hall-deficient cluster, where two or more effective safe-check degrees are missing. However, the existence of such a cluster does not imply a counterexample to the underlying paired-root conjecture; larger-root-set compatibility may survive despite the failure of all selected parity checks.


##### Arbitrary nonlinear star interactions force paired roots

Let \(f\) color the undirected edges of \(Q_d\), \(d\ge2\). Suppose its interaction graph is a star with center direction \(c\), including the possibility of isolated directions. Split the dimensions into leaves \(L=[d]\setminus\{c\}\) and center \(c\). An edge in leaf direction \(i\) has color \(a_i(s)\), where \(s\in\{0,1\}\) is the current center bit, while center edges have unrestricted color \(b(x)\) depending on the entire leaf configuration \(x\in Q_L\). There is no affine or oddness hypothesis.

Define \(A_0(f)\) and \(A_1(f)\) as roots with full dimension-simple geodesics of respective color words \(0^*1^*\) and \(1^*0^*\), and let \(P(f)=A_0(f)\cap A_1(f)\).

**Theorem (star paired-root closure).** Every star-interaction cube-edge coloring satisfies \(P(f)\ne\varnothing\). If any leaf configuration \(x\) obeys \(b(x)=b(\bar x)\), both roots \((x,0),(x,1)\) are paired. Otherwise a paired root can be constructed from any leaf-cube edge on which \(b\) changes.

*Proof.* From root \((x,s)\), leaf steps taken before the center edge have colors \(a_i(s)\), regardless of their order, and leaf steps afterward have colors \(a_i(1-s)\). Within each group the leaf steps may therefore be sorted by color.

Suppose \(b(x)=b(\bar x)=0\). Placing the center edge first gives a \(0^*1^*\) full geodesic: its center color is zero, then post-center leaf colors are sorted ascending. Placing it last gives a \(1^*0^*\) full geodesic: initial leaf colors are sorted descending, then the center has color zero. For \(b(x)=b(\bar x)=1\), exchange which orientation uses center first and which uses center last. This proves the assertion for both starting center bits.

Otherwise \(b(\bar x)=1-b(x)\) for all \(x\), so \(b\) is nonconstant. Choose a leaf direction \(j\) and adjacent configurations \(x,y=x\oplus e_j\) with \(b(x)=0,b(y)=1\). Choose \(s\in\{0,1\}\) such that \(a_j(s)=1\) or \(a_j(1-s)=0\). An admissible \(s\) exists: if neither condition holds for \(s=0\), then \(a_j(0)=0,a_j(1)=1\), making the first condition true for \(s=1\).

From \((x,s)\), placing the center first (color zero) and sorting all leaf steps ascending yields \(0^*1^*\).

For the reverse orientation there are two cases. If \(a_j(s)=1\), take direction \(j\) first (color one), then center at leaf configuration \(y\) (color one), followed by every other leaf direction sorted descending; this gives \(1^*0^*\). Otherwise \(a_j(1-s)=0\). Take all leaf steps except \(j\) first, sorted descending; then cross the center; then take \(j\) last. At the center crossing the leaf configuration equals \(\bar y\), so the center color is \(b(\bar y)=1-b(y)=0\); the final \(j\)-edge also has color zero. This again gives \(1^*0^*\). Both witnesses start at \((x,s)\) and traverse every dimension once. QED.

**Corollary.** An interaction-connected paired-root counterexample cannot have a star interaction graph, even when every dimension class is nonuniform. More generally, a counterexample under the Cartesian-product factorization must have some interaction component not governed by a single hub.

**Closure direction.** This proof supplies an all-dimensional leaf-exchange argument: an edge where the hub color changes permits relocating one leaf relative to the hub crossing to force the opposite monotone orientation. The next natural goal is to generalize such synchronization from stars to arbitrary interaction trees.

##### Stronger theorem: paired roots in every hub fiber, without symmetry

**Theorem 3 (sharp fiberwise star theorem).** Under the star coloring hypotheses of Theorem 1, for every leaf configuration \(x\in Q_L\),
\[
\boxed{(x,0)\in P(f)\quad\text{or}\quad(x,1)\in P(f).}
\tag{3}
\]
Consequently \(|P(f)|\ge2^{d-1}\). This bound holds for arbitrary hub function \(b\), with no antipodal symmetry assumption, and is sharp even when the interaction star is connected.

*Proof.* Fix \(x\), and put \(q=b(x)\). Choose the leaf subset
\[
S=\{i\in L:a_i(0)=1-q\},\qquad y=x\oplus\bigoplus_{i\in S}e_i.
\tag{4}
\]
Set the starting hub bit to \(s=0\) when \(b(y)=1-q\), and to \(s=1\) when \(b(y)=q\).

We construct the two required monotone color words from root \((x,s)\).

The orientation beginning with color \(q\) is always obtained by traversing the hub direction first (color \(b(x)=q\)), followed by all leaf directions sorted by their post-hub colors \(a_i(1-s)\): increasing if \(q=0\), decreasing if \(q=1\). The full word has form \(q^*(1-q)^*\).

For the opposite orientation \((1-q)^*q^*\), distinguish the two choices of \(s\).

If \(s=0\), take all leaves of \(S\) first. By (4), their colors \(a_i(0)=1-q\); the hub crossing at \(y\) also has color \(b(y)=1-q\). Afterwards traverse the remaining leaves sorted toward final color \(q\). Thus the full word is \((1-q)^*q^*\).

If \(s=1\), first traverse the leaves in \(S\), sorted toward color \(q\), using their pre-hub colors \(a_i(1)\). Cross the hub at \(y\), where its color is \(b(y)=q\). Traverse the remaining leaves, whose post-hub colors are \(a_i(0)=q\), in any order. Again the full word has form \((1-q)^*q^*\).

Hence \((x,s)\) is a paired root. Every step uses a distinct direction. Since \(x\) was arbitrary, each hub fiber contains a paired root, proving (3).

For sharpness, take the product of the two-dimensional square coloring \(h\) from the Cartesian factorization theorem, which has two paired roots among four, with a one-direction monochromatic factor for every further dimension. This is a star-interaction coloring and its paired-root count is \(2^{d-1}\). To make the interaction star connected, one may instead take center color \(b(x)=0\) and leaf colors \(a_i(s)=s\) for every \(i\in L\). Then every leaf interacts with the hub, while direct evaluation of the two orientations shows precisely one of the two hub bits is paired for each leaf configuration, again attaining \(2^{d-1}\). QED.

**Corollary 4 (one-bit constructive selector).** A paired root can be found from any prescribed leaf configuration using one evaluation of \(b(x)\), one evaluation of \(b(y)\), and the list of leaf colors \(a_i(0),a_i(1)\). No search over permutations or over the full coloring space is required.

**Toward closure.** The star theorem now supplies a fiberwise lower bound of one half with arbitrarily many interacting directions. A leaf-elimination induction on more general interaction trees would be especially valuable if it preserved this fiberwise property on an appropriate separator.### Sharp favorable-root fractions for nonlinear star colorings

Let \(f\) be a coloring of \(Q_d\) with star interaction graph and central direction \(c\). Denote by \(A_0(f)\) and \(A_1(f)\) roots with full monotone words \(0^*1^*\) and \(1^*0^*\).

**Theorem 5.**
\[
\boxed{|A_0(f)|,\ |A_1(f)|\ge3\cdot2^{d-2}.}
\tag{5}
\]
The bounds are sharp, without any symmetry assumption on the central edge-color function.

*Proof.* Partition roots into four-element blocks \(\{(x,0),(x,1),(\bar x,0),(\bar x,1)\}\). If the center-edge colors satisfy \(b(x)=b(\bar x)\), Theorem 1 shows all four roots are paired.

Otherwise one of \(x,\bar x\) has center color zero; placing the center direction first gives a nondecreasing path from both roots over that configuration. The other has center color one; placing center first gives a nonincreasing path from both of those roots. The fiberwise Theorem 3 guarantees at least one paired root above *each* configuration. Hence each four-root block contributes at least three roots to each orientation's favorable set. There are \(2^{d-2}\) blocks.

For equality, take the Cartesian product of the extremal colored square \(h\), with three favorable roots in each orientation, and a monochromatic factor for every remaining direction. QED.

**Corollary 6 (two independent star colorings).** Suppose arbitrary colorings \(f,g\) of \(Q_d\) each have star interaction graphs, possibly with different hub directions and unrelated nonlinear edge functions. Then
\[
\boxed{|A_0(f)\cap A_1(g)|\ge2^{d-1}.}
\tag{6}
\]
This follows from the preceding lower bounds by inclusion-exclusion. It verifies the stronger two-coloring favorable-root intersection statement for two unrelated stars in all dimensions.

**Scope.** The interaction-star assumption is essential to the present proof; no claim is made for general interaction graphs.### Erratum: connected-star sharpness

The earlier constant-hub example following Theorem 3 does not attain the stated half-root bound: it has paired roots everywhere.

A valid connected-star extremizer is
\[
b(x)=x_j,\qquad a_i(s)=1-s\quad(i\in L),
\]
where (j\in L) is one selected leaf. Every leaf interacts with the center. Fix any leaf configuration (x), and consider initial center bit (s=1-x_j). Every leaf step before the center has color (x_j), every leaf step after the center has color (1-x_j), and the center edge has color (x_j) when leaf (j) precedes it, and (1-x_j) when leaf (j) follows it. Consequently every full geodesic from that root has both colors and the single monotone orientation (x_j^*(1-x_j)^*). No geodesic realizes the opposite orientation, so this root is unpaired. The fiberwise theorem guarantees the other root ((x,x_j)) is paired. Thus every hub fiber has one paired root, and the lower bound \(|P(f)|=2^{d-1}\) is attained with connected interaction graph. This corrects only the equality example; preceding theorems are unaffected.

##### Star forests and interaction-prime reduction

**Corollary 7 (quantitative star-forest theorem).** Suppose the interaction graph \(\Gamma(f)\) is a disjoint union of components, each either isolated or a star. Let \(c\) denote the number of nontrivial components (those containing at least two dimensions). Then
\[
\boxed{|P(f)|\ge2^{d-c}.}
\tag{8}
\]
The bound is sharp for every such component-size partition.

*Proof.* By the Cartesian factorization theorem, \(f\) is the product of its component colorings, and \(P(f)\) is the Cartesian product of their paired-root sets. An isolated direction, whose edge color is constant, has both roots paired. A nontrivial star component of dimension \(m\) has at least \(2^{m-1}\) paired roots by Theorem 3. Multiplication over components gives \(2^{d-c}\). Equality follows by using the connected-star extremizer \(b(x)=x_j,\ a_i(s)=1-s\) in every nontrivial component and any constant edge color in the isolated components. QED.

**Corollary 8 (star-or-small reduction for potential counterexamples).** Suppose every connected component of \(\Gamma(f)\) is either a star or has at most four dimensions. Then \(P(f)\ne\varnothing\). Consequently any hypothetical paired-root-free coloring has an interaction component of size at least five that is not a star; in particular a minimum-dimension counterexample must have a connected, non-star interaction graph on at least five directions.

*Proof.* Star components have paired roots by Theorem 1. Every coloring on at most four dimensions has a paired root by the previously established finite-dimensional paired-root theorem. Apply Cartesian factorization of \(P(f)\). QED.

**Corollary 9 (independent star factors and two-coloring cross-intersection).** Suppose \(f\) and \(g\) share a decomposition of their dimension set into \(c\) nontrivial component blocks and any number of singleton blocks, such that on each nontrivial block both factor colorings have star interaction graphs, with their hubs and edge rules allowed to differ. Then
\[
\boxed{|A_0(f)\cap A_1(g)|\ge2^{d-c}.}
\tag{9}
\]
This follows from the product factorization and Corollary 6 applied independently on every component, while a singleton factor permits either monotone orientation at both roots.

**Proof-search consequence.** Arbitrarily large interaction systems assembled from nonlinear hubs cannot obstruct NORI1. The first interaction-graph shapes outside this theorem arise by connecting hubs together or introducing cycles. Establishing a similar root-selector property for an interaction tree with two adjacent hubs would extend the theorem from star forests toward arbitrary forests, while retaining the same dimension-simple path geometry.### Free-bridge NORI1 closure and abundance

**Corollary 10 (odd cube colorings with star lower facet).** Let \(n=d+1\ge3\). Suppose the undirected edges of \(Q_n=Q_d\times\{0,1\}\) are colored antipodally oddly, and the induced coloring \(f\) on its lower \(Q_d\) facet has a star interaction graph. The vertical bridge colors are unrestricted except for antipodal oddness. Then there are at least
\[
\boxed{2^{n-2}}
\]
distinct directed monochromatic full antipodal geodesics oriented from the lower facet to the upper facet.

*Proof.* Every such odd coloring is the universal bridge extension \(C(f,h)\) of the earlier paired-root Subsection, where \(h(\bar z)=1-h(z)\). The bridge equivalence assigns to every paired root \(z\in P(f)\) a monochromatic full antipodal geodesic whose unique vertical step uses the bridge at \(z\). Theorem 3 proves \(|P(f)|\ge2^{d-1}=2^{n-2}\). Paths coming from different roots \(z\) traverse different vertical bridges, so they are distinct. QED.

**Corollary 11 (star-forest extension).** If the lower-facet interaction graph is a disjoint union of stars with \(c\) nontrivial components, the same argument gives at least \(2^{d-c}\) distinct directed monochromatic full antipodal geodesics.

This closes an all-dimensional class of NORI1 instances with nonlinear hub functions and unrestricted odd bridge assignments. It makes no claim about unrestricted facets or the boundary tournament conjecture.

##### A linear-query monochromatic-path algorithm for star facets

**Theorem 12 (constructive oracle bound).** Given an antipodally odd coloring of \(Q_{d+1}=Q_d\times\{0,1\}\) whose lower facet has star interaction graph with known hub direction, one can construct a monochromatic full antipodal geodesic with \(O(d)\) color queries and \(O(d)\) elementary operations. The vertical bridge colors remain arbitrary subject to oddness.

*Proof.* Fix any leaf configuration \(x\), for example the all-zero string. Read the leaf edge colors \(a_i(0),a_i(1)\) for every leaf direction \(i\), and read the lower-facet hub color \(q=b(x)\). Form
\[
S=\{i:a_i(0)=1-q\},\qquad y=x\oplus\bigoplus_{i\in S}e_i.
\]
Read the hub-edge color \(b(y)\), and set the starting hub bit \(s=0\) if \(b(y)=1-q\), otherwise \(s=1\). Theorem 3 explicitly constructs from \(z=(x,s)\) a full lower-facet path \(P_q\) of word \(q^*(1-q)^*\) and a full path \(P_{1-q}\) of word \((1-q)^*q^*\). Both are obtained by sorting leaf directions into their two color classes and positioning the hub first or between those classes, without any path search.

Read the vertical bridge color \(h(z)\) in \(Q_{d+1}\), and choose the lower-facet witness \(P_{h(z)}\). Write its vertices as \(z=z_0,z_1,\ldots,z_d=\bar z\), with color change after edge \(k\), and let \(w=z_k\). Construct a full geodesic starting at lower vertex \((w,0)\): first traverse the prefix of \(P\) in reverse from \(w\) to \(z\), then use the vertical bridge at \(z\), then traverse in the upper facet the antipodal image of the suffix of \(P\), reversed, from \(z\) to \(\bar w\). Its lower edges have color \(h(z)\), its vertical edge also has color \(h(z)\), and its upper edges have color \(1-(1-h(z))=h(z)\) by antipodal oddness. Its horizontal directions are the disjoint dimension sets from the original prefix and suffix, and the new vertical dimension is used once. Therefore the resulting path is dimension-simple, monochromatic, and antipodal, as claimed. QED.

The query bound uses at most \(2(d-1)+3\) lower/vertical edge-color evaluations, with constant-work sorting into two binary color classes. The hub-direction identity may be part of the input promise; discovering it from a completely unrestricted black-box coloring is a separate task.

#### Uniform Hamming robustness of nonlinear star selectors

For any binary edge coloring \(f\) of \(Q_d\), write \(P(f)\) for the paired-root set. The star selector of Theorem 3 chooses one paired root \(z(x)=(x,s(x))\) above each leaf configuration \(x\in Q_{d-1}\), and constructs two full geodesics from that same root, of color words \(0^*1^*\) and \(1^*0^*\).

**Lemma 13 (fixed-order edge incidence).** Fix a permutation \(\pi\) of the \(d\) cube directions. Every undirected cube edge \(e\) belongs to precisely two full directed antipodal geodesics \(P(z,\pi)\), as the root \(z\) ranges over \(Q_d\).

*Proof.* Let \(i\) be the direction of \(e\), and let \(S\) be the set of directions preceding \(i\) in \(\pi\). The direction-\(i\) step of the path rooted at \(z\) joins \(z\oplus S\) to \(z\oplus S\oplus e_i\). It equals the prescribed undirected edge \(e\) for precisely the two values of \(z\) obtained by translating the two endpoints of \(e\) by \(S\). QED.

**Lemma 14 (bounded permutation certificate).** For every star-interaction coloring \(f\), the \(2^{{d-1}}\) distinct paired roots \(z(x)\) furnished by the fiberwise selector have orientation witnesses drawn from at most **eight fixed permutations** of the \(d\) directions, independently of the hub function and of \(d\).

*Proof.* Recall the explicit algorithm of Theorem 3. For each leaf configuration \(x\), put \(q=b(x)\), define \(S(q)=\{i:a_i(0)=1-q\}\), and select \(s\in\{0,1\}\) from the hub-color value \(b(x\oplus S(q))\). The witness of word \(q^*(1-q)^*\) places the hub first and sorts the remaining leaf directions by their post-hub colors \(a_i(1-s)\). The witness of word \((1-q)^*q^*\) has a fixed ordering of \(S(q)\) before the hub and its complement afterward, with the two groups sorted by their known leaf colors as required. Once the pair \((q,s)\in\{0,1\}^2\) is specified, **both direction orders are fixed**, independently of \(x\). Thus four values of \((q,s)\) produce at most eight dimension orders. QED.

**Theorem 15 (Hamming stability around arbitrary stars).** Let \(f\) be any binary coloring of \(Q_d\) whose interaction graph is a star, with arbitrary nonlinear hub-edge colors. Let \(g\) differ from \(f\) on \(k\) undirected edges. Then
\[
\boxed{|P(g)|\ge\max\{0,\ 2^{d-1}-16k\}.}
\tag{11}
\]
In particular, when \(k<2^{d-5}\), the coloring \(g\) has a paired root.

*Proof.* Choose the \(2^{d-1}\) pairwise distinct roots \(z(x)\) and their two star-selector witness paths. Theorem 3 certifies both monotone orientations for \(f\) at every selected root. Under recoloring \(k\) edges, a selected root remains paired for \(g\) if neither of its witness paths contains a changed edge. By Lemmas 13-14, a prescribed changed edge belongs to at most \(2\cdot8=16\) of the witness paths indexed by all selected roots. It can therefore invalidate at most 16 root certificates. The union bound over \(k\) changed edges leaves at least \(2^{d-1}-16k\) unaffected roots, proving (11). QED.

**Corollary 16 (stability of NORI1 over star-like facets).** Let an antipodally odd coloring of \(Q_{d+1}=Q_d\times\{0,1\}\) have lower-facet coloring \(g\) at Hamming distance \(k\) from some star-interaction coloring \(f\) of \(Q_d\). The vertical bridge colors are arbitrary subject to oddness. Then at least
\[
\boxed{\max\{0,\,2^{d-1}-16k\}}
\tag{12}
\]
distinct directed monochromatic dimension-simple antipodal geodesics, oriented from the lower to the upper facet, exist.

*Proof.* Apply Theorem 15 to \(g\) and invoke the universal free-bridge correspondence for each surviving paired root, as in Corollary 10. Distinct paired roots correspond to distinct vertical bridges and hence distinct full geodesics. QED.

**Prospective closure use.** Minimal hypothetical paired-root-free colorings must be separated by at least \(2^{d-5}\) edge changes from every star interaction coloring. This extends the earlier Hamming obstruction around direction-uniform templates to arbitrarily nonlinear hub functions. It does not yet prove that a critical bad coloring lies near a star, but yields a uniform stability barrier should a structural reduction or interaction-tree decomposition produce such proximity.### Six-order witnesses and robust cross-favorability near stars

**Lemma 17 (six-order orientation certificates).** For every binary coloring \(f\) of \(Q_d\) whose interaction graph is a star, there are at least \(3\cdot2^{d-2}\) roots with \(0^*1^*\) full geodesics whose dimension orders belong to a fixed family of at most six permutations. The same holds for \(1^*0^*\).

*Proof.* Write a root as \((x,s)\), where \(x\) comprises all leaf bits and \(s\) the hub bit. Partition the roots into four-element groups over antipodal leaf pairs \(\{x,\bar x\}\).

If \(b(x)=b(\bar x)=0\), all four roots have \(0^*1^*\) paths obtained by hub first and leaves sorted by their post-hub colors. If both hub colors are one, all four have \(0^*1^*\) paths obtained by hub last and leaves sorted by their pre-hub colors. If the hub colors differ, the two roots over the zero-colored leaf configuration have hub-first \(0^*1^*\) paths, and the star fiberwise selector supplies at least one root over the one-colored configuration with a \(0^*1^*\) path. In every group at least three roots are thus certified.

The three possible path constructions have respectively two dimension orders, one for each starting hub bit: hub first with leaves ascending; hub last with leaves ascending; and the \(q=1\) selector's opposite-orientation path as in Theorem 3. For each fixed construction and starting hub bit the order of the leaf dimensions depends only on the given star's functions \(a_i(0),a_i(1)\), not on \(x\). Hence at most six permutations suffice. Interchanging the two colors proves the other orientation. QED.

**Theorem 18 (favorable-root stability around any star).** If a coloring \(g\) differs from some star-interaction coloring of \(Q_d\) on \(k\) undirected edges, then
\[
\boxed{|A_0(g)|,\ |A_1(g)|\ge \max\{0,\ 3\cdot2^{d-2}-12k\}.}
\tag{13}
\]

*Proof.* Lemma 17 supplies at least \(3\cdot2^{d-2}\) rooted paths in each monotone orientation, drawn from six fixed dimension orders. For one given order, each undirected cube edge belongs to two rooted full geodesics, by Lemma 13. Each altered edge can therefore spoil at most twelve of the chosen certificates. Union bounding over \(k\) changed edges proves the inequalities. QED.

**Corollary 19 (robust cross-orientation intersection for unrelated stars).** Suppose \(g,h\) have respective Hamming distances \(k,\ell\) from two star-interaction colorings, whose hubs and edge-color rules need not agree. Then
\[
\boxed{|A_0(g)\cap A_1(h)|\ge\max\{0,\ 2^{d-1}-12(k+\ell)\}.}
\tag{14}
\]
In particular, the stronger two-coloring intersection conjecture holds whenever \(k+\ell<2^d/24\).

*Proof.* Apply Theorem 18 to the two colorings and use inclusion-exclusion in the \(2^d\) cube vertices. QED.

**Implication.** Abundant root certificates supported on finitely many dimension orders admit quantitative stability under arbitrary edge recoloring, even if the base coloring has nonlinear dependence on arbitrarily many leaf bits. Controlling the number of such orders under interaction-tree gluing is a possible induction target toward unrestricted paired-root existence.

#### Transverse square-variation obstruction to paired-root failure

For an arbitrary cube-edge coloring \(f\) of \(Q_d\), let \(f_i(x)\) denote the color of the direction-\(i\) edge incident with \(x\). It is independent of \(x_i\). Define the directed square-influence
\[
I_{ij}(f)=\Pr_{x\in Q_d}[f_i(x)\ne f_i(x\oplus e_j)],\qquad i\ne j.
\]
For a designated potential hub \(c\in[d]\), set
\[
D_c(f)=\sum_{\substack{i,j\ne c\\i\ne j}}I_{ij}(f).
\tag{15}
\]
This records only square variation *among the leaves*, discarding every term incident with \(c\).

**Lemma 20 (projection onto a nonlinear star by leaf Poincare).** For every binary edge coloring \(f\) of \(Q_d\) and every proposed center \(c\), there exists a star-interaction coloring \(g\) with center \(c\), agreeing with \(f\) on every center-direction edge, such that
\[
\boxed{\operatorname{dist}(f,g)\le2^{d-2}D_c(f).}
\tag{16}
\]

*Proof.* Keep the center-direction edge colors \(g_c=f_c\), which may depend arbitrarily on every leaf bit. For each leaf direction \(i\ne c\) and each fixed hub bit \(s\in\{0,1\}\), choose \(g_i\) to be the majority color of \(f_i\) over all \(2^{d-2}\) undirected direction-\(i\) edges in the hub-\(s\) facet. This produces a star coloring: each \(g_i\) depends only on the hub bit.

Let \(p_{i,s}\) be the fraction of these leaf-direction edges colored one. The number of altered edges in this slice is \(2^{d-2}\min(p_{i,s},1-p_{i,s})\). The Boolean-cube Poincare inequality for the \(d-2\) leaf bits other than \(i,c\) gives
\[
p_{i,s}(1-p_{i,s})
\le\frac14\sum_{j\notin\{i,c\}}
\Pr[\partial_j f_i=1\mid x_c=s].
\]
Since \(\min(p,1-p)\le2p(1-p)\), summing over \(i\ne c\) and both hub bits yields
\[
\operatorname{dist}(f,g)
\le2^{d-3}\sum_{i\ne c}\sum_{j\notin\{i,c\}}\sum_{s=0}^1
\Pr[\partial_j f_i=1\mid x_c=s]
=2^{d-2}D_c(f).
\]
QED.

**Theorem 21 (transverse curvature sufficient condition).** Every arbitrary cube-edge coloring \(f\) satisfies
\[
\boxed{|P(f)|\ge\max\{0,\ 2^{d-1}(1-8D_c(f))\}}
\quad\text{for every }c\in[d].
\tag{17}
\]
In particular, if some \(c\) has \(D_c(f)<1/8\), then \(f\) has a paired root.

*Proof.* Let \(g\) be the star approximation from Lemma 20. Theorem 15 gives
\[
|P(f)|\ge2^{d-1}-16\operatorname{dist}(f,g)
\ge2^{d-1}-16\cdot2^{d-2}D_c(f)
=2^{d-1}(1-8D_c(f)).
\]
QED.

**Corollary 22 (hereditary spread of transverse interactions in every putative counterexample).** If \(P(f)=\varnothing\), then
\[
\boxed{\sum_{\substack{i,j\ne c\\i\ne j}}\Pr_x[\partial_j f_i(x)=1]\ge\tfrac18
\qquad\text{for every }c\in[d].}
\tag{18}
\]
Thus no dimension can serve as an approximate hub with total leaf-leaf square variation below \(1/8\), even if all \(d\) directions have nonuniform colors. Equivalently, every putative paired-root-free coloring is quantitatively separated in square-influence from the entire nonlinear star class.

**Closure interpretation.** The new obstruction is localized by *deleting one candidate hub* from the directed square-influence sum, rather than by counting global switch support. A proof that switch-criticality forces some dimension with \(D_c<1/8\) would establish NORI1 through the existing free-bridge equivalence. No such implication is presently known; arbitrary random colorings typically have much larger variation, so an induction must exploit the criticality or full-path witness geometry rather than treat (18) as an immediate contradiction.

##### A coupled-hub obstruction to independent leaf elimination

The nonlinear star theorem supplies a paired-root hub selector in every leaf fiber. A natural attempt at an interaction-tree induction is to apply the star selector separately at two adjacent hubs and then solve the two selected hub-bit conditions. The following example shows this procedure can fail even when the complete double-star coloring is exceptionally favorable.

**Proposition 1 (incompatible isolated-star selectors but compatible complete paths).** Consider the four-dimensional cube with two adjacent hubs \(a,b\) and one leaf at each hub, called \(u,v\). Use bits \(a,b,u,v\), and color its undirected edges as follows:
\[
\boxed{
f_a=b\oplus u,\qquad
f_b=a\oplus v\oplus1,\qquad
f_u=1-a,\qquad
f_v=1-b.
}
\tag{1}
\]
Every formula is independent of the bit in its own edge direction. Its interaction graph is the path \(u-a-b-v\), a connected double-star.

Fix the leaf configuration \(u=v=0\). When the hub \(b\) is held fixed, the isolated \(a,u\) star has a unique paired root bit \(a=b\). When hub \(a\) is held fixed, the isolated \(b,v\) star has a unique paired root bit \(b=1-a\). Hence the two independently selected hub bits cannot simultaneously satisfy both conditions.

Nevertheless **every** of the four full roots \((a,b,0,0)\) is paired, and in fact each has a monochromatic complete antipodal geodesic. For roots \((a,b)=(0,0),(1,1)\), direction order \(a,b,u,v\) is monochromatic, with respective constant colors zero and one. For roots \((a,b)=(1,0),(0,1)\), direction order \(b,u,a,v\) is monochromatic, again with respective constant colors zero and one.

*Proof.* The local star selectors follow from the sharp connected-star model \(f_{\rm hub}=x_{\rm leaf}\oplus t,\ f_{\rm leaf}=1-s\), whose unique paired hub choice at a fixed leaf root is \(s=x_{\rm leaf}\oplus t\). The first isolated star has \(t=b\), the second \(t=a\oplus1\). These yield the stated inconsistent equations. For the four complete roots, substitute the displayed direction orders into (1). Each traversal uses all directions once, and its four colors are \(0000\) or \(1111\), as indicated. A monochromatic full geodesic qualifies for both orientations at its root. QED.

**Corollary 2 (obstruction to unmodified local-selector gluing).** Even for an affine coloring with a four-vertex path interaction graph, separately chosen star selectors need not have a simultaneous solution. Any tree-induction theorem must permit *interleaving the hub crossings and leaf steps*, rather than imposing an independent paired-root selector at each hub. The phenomenon persists in every dimension \(d\ge4\) after Cartesian multiplication by constant-color single-direction factors.

##### Finite test of the two-hub fiber conjecture

For an interaction double-star with two central directions, two leaf groups, and arbitrary nonlinear dependence allowed by the interaction graph, the stronger conjecture is that every fixed assignment of the leaf bits has at least one paired choice of the two hub bits. This has not been proved.

We exhaustively tested two small parameter families to identify sharp local cases:
- \(Q_4\), one leaf at each hub: the permitted edge-color dependence has 12 independent binary parameters. All \(2^{12}=4096\) colorings were enumerated, and for each all four possible leaf configurations were checked. The smallest paired-root count in a four-root hub fiber was one.
- \(Q_5\), two leaves attached to the first hub and one to the second: there are 18 independent edge-color parameters. All \(2^{18}=262144\) assignments were enumerated, with the leaf root fixed to zero; flipping prescribed leaf bits permutes the parameter family, so this suffices for all leaf configurations. Again the minimum hub-fiber paired-root count was one.

Both calculations used a binary subset dynamic program for each root and orientation, in which the state is the used-direction set and whether the unique permitted monotone phase change has happened. These are **finite computational checks**, not a general two-hub theorem.

**Closure direction.** A viable two-hub induction should study the four joint hub states as a *single square-valued interface*, with monotone path certificates that permit leaf steps on either side of both hub crossings. The example (1) rules out the simpler fixed-point approach using independent star selectors. Establishing a four-state interface intersection lemma under arbitrary nonlinear hub functions would extend the all-dimensional star theorem to double-stars and could initiate an interaction-tree reduction.

#### A six-dimensional obstruction to fixed-leaf hub selection

The four-type macro compression reduces unrestricted nonlinear two-hub stars to at most six dimensions, but the resulting six-dimensional root interface cannot be solved independently over each fixed leaf assignment.

Let Q_6 have hub bits \(t_0,t_1\) and four leaf bits \(x_2,x_3,x_4,x_5\). Color undirected direction-i edges by the following Boolean functions (all arithmetic in \(\mathbb F_2\)):
\[
\boxed{\begin{aligned}
f_0&=1+x_2+t_1(x_2+x_3),\\
f_1&=1+x_4+t_0(x_4+x_5),\\
f_2&=t_0,\quad f_3=1+t_0,\quad
f_4=t_1,\quad f_5=1+t_1.
\end{aligned}}
\tag{A}
\]
Each f_i is independent of its own bit and hence defines a valid undirected-edge coloring. All four leaf types of the two-hub macro-star are represented.

**Proposition (failure of fixed-leaf selector).** At each root \((t_0,t_1,0,0,0,0)\) with \(t_0,t_1\in\mathbb F_2\), there is NO full dimension-simple antipodal geodesic with word \(0^*1^*\). Nonetheless,
\[
\boxed{|A(f)|=48,\qquad|P(f)|=36}
\tag{B}
\]
among the 64 cube roots. In particular the proposed rule that every fixed leaf assignment allows some favorable, or paired, hub-bit choice is false. This does not refute the conjectured global nine-sixteenths favorable-root bound.

**Reproducible finite certificate.** Fix root z. A state R0(S) means that the dimensions in S can be traversed from z with all edge colors zero. A state R1(S) means they can be traversed with a word \(0^*1^+\). Initialize R0(empty)=true and R1(empty)=false. For unused direction i and current vertex \(v=z+\mathbf1_S\), propagate R0(S) to R0(S union {i}) if \(f_i(v)=0\), and propagate R0(S) or R1(S) to R1(S union {i}) if \(f_i(v)=1\). No other transitions are allowed. Root z is favorable if either terminal state at S=[6] is true.

For the four roots at leaf 0000, the counts of reachable states R0/R1 as subset cardinality grows from 0 to 6 are:
- hubs 00 or 11: R0 counts (1,2,3,4,2,0,0), R1 counts (0,4,14,20,14,4,0);
- hubs 01 or 10: R0 counts (1,2,1,0,0,0,0), R1 counts (0,4,12,14,8,2,0).

Thus the terminal state is unreachable for all four roots. Applying the same recurrence to all 64 roots gives 48 favorable and 36 paired, where pairing means z and its antipode are both favorable. This is a finite exhaustive verification of the six-dimensional example, not an all-dimensional theorem.

**Proof-closure consequence.** Any general two-hub theorem must permit favorable roots to move *between different leaf assignments*. Applying an isolated one-hub selector to each hub, or demanding one favorable hub choice over every fixed leaf assignment, is insufficient. The macro-reduction gives a bounded structured problem, but global compatible root placement remains its unresolved substance.

**Small benchmark.** Exhaustive search over the 256 choices for each hub Boolean color function in the Q4 double-star with one leaf per hub, at normalized leaf offsets, gives a minimum of 9 favorable roots out of 16 and 4 paired roots. The six-dimensional example above shows that its stronger fixed-leaf property does not extrapolate to four leaf types. These computations do not establish the proposed lower bound for arbitrary Q6 two-hub stars.

#### Hub-color CNF and a short three-root contradiction

**Theorem (k-hub SAT reduction).** For a coloring with k hub directions, suppose every nonhub edge color is determined by the starting root and the order of the hub flips. Regard the values of all hub-edge color functions as independent Boolean variables. For a specified root z, the assertion that no full dimension-simple antipodal geodesic has color word \(0^*1^*\) is equivalent to a CNF with clause width at most k. In particular, a two-hub bad-root condition is 2-SAT.

*Proof.* Fix any dimension ordering. Its nonhub edge colors are determined, and its k hub steps read at most k hub variables. For each assignment to those hub values that makes the full color word nondecreasing, forbid that assignment with a clause stating at least one accessed variable differs. Conjoin these clauses across all full dimension orders. The root is unfavorable precisely when all forbidden patterns are avoided. QED.

For the four-leaf-type Q6 model, put \(L(x)=x_2+2x_3+4x_4+8x_5\). Let X0,...,X63 be the hub-edge table bits: hub 0 reads \(X_{16x_1+L(x)}\) and hub 1 reads \(X_{32+16x_0+L(x)}\). The leaf colors are \(x_0,1+x_0,x_1,1+x_1\). Encode an initial root as \(\sum_i2^i z_i\).

**Proposition (three-root incompatibility).** No two-hub coloring of this class makes all three initial roots \(0,3,23\) unfavorable.

*Proof.* The following eight forbidden hub assignments are forced if those three roots are all unfavorable: each row supplies a dimension ordering that would otherwise be a full nondecreasing geodesic.

| Root | Order | Forbidden hub values | Resulting path colors |
|---|---|---|---|
|0|240315|X5=0, X55=0|000000|
|3|324150|X55=1, X15=1|011111|
|23|351024|X63=0, X15=0|000000|
|0|240351|X5=0, X63=1|000011|
|3|142035|X48=0, X5=1|001111|
|23|241035|X48=1, X0=1|111111|
|0|041352|X0=0, X52=0|000001|
|3|412035|X52=1, X5=1|111111|

Negating these permitted patterns gives both implication chains
\[
X_5=0\Rightarrow X_{55}=1\Rightarrow X_{15}=0
\Rightarrow X_{63}=1\Rightarrow X_5=1,
\]
\[
X_5=1\Rightarrow X_{48}=1\Rightarrow X_0=0
\Rightarrow X_{52}=1\Rightarrow X_5=0.
\]
Either bit value for X5 forces its opposite. This contradiction proves the proposition. QED.

**Computational checks, not a general theorem.** Each root in the reduced Q6 class yields 66 distinct 2-SAT clauses. All 64 individual root constraints and all 2016 distinct pairs are jointly satisfiable. Among 41664 root triples, 5952 are inconsistent. The corresponding 3-uniform obstruction hypergraph has independence number 32, as certified by integer optimization using one root variable and one inequality per forbidden triple. Therefore triple incompatibilities alone cannot establish the conjectural nine-sixteenths favorable-root lower bound (at most 28 unfavorable roots). Four-root and higher compatibility must enter such a proof.

This gives an intrinsic implication-graph formulation for nonlinear hub interactions, without assuming independent hub selectors. The general two-hub conjecture remains open.

#### Computer-assisted sharp two-hub majority and two-branch closure

**Theorem (sharp nine-sixteenths favorable-root bound; computer-assisted).** Let f be any binary edge coloring of Q_(m+2) with two hub directions 0,1, arbitrary nonlinear hub edge-color functions, and every other direction j colored by \(a_j+t_{\eta(j)}\), where eta(j) in {0,1}. Then
\[
\boxed{|A(f)|\ge\frac9{16}2^{m+2},\qquad
|P(f)|\ge\frac18 2^{m+2}.}
\tag{A}
\]
The favorable-root constant is sharp. Sharpness of the paired-root lower bound is not established here.

*All-dimensional reduction.* The established four-type compression groups leaves by their controlling hub and offset bit. Its full-branch expansion preserves full dimension-simple nondecreasing paths and antipodal paired roots. The root-density bound thus reduces to structured two-hub colorings with at most four distinct macro leaves, on at most six dimensions. Missing macro types can be added as independent sink directions with their prescribed hub-controlled colors; since no existing edge color depends on an added bit, the seam-insertion identity duplicates the favorable-root set. It therefore suffices to prove the nine-sixteenths bound on the full four-type Q6 model.

*Finite verified step.* On Q6 let the leaf-edge bits be
\[
f_2=x_0,\ f_3=1+x_0,\ f_4=x_1,\ f_5=1+x_1.
\]
Let L(x)=x_2+2x_3+4x_4+8x_5, and encode the 64 free hub-edge color bits as X0,...,X63, with f0 at x reading \(X_{16x_1+L(x)}\) and f1 at x reading \(X_{32+16x_0+L(x)}\).

For each root z create Boolean indicator b_z. Traverse all 720 dimension orders from z. Each path reads one hub-0 and one hub-1 variable; its other four edge colors are determined by the root and the order. For each pair of hub-value assignments that makes the complete color word nondecreasing, require
\[
\boxed{b_z\Rightarrow(X_u\ne a\ \vee\ X_v\ne b).}
\tag{B}
\]
This is a two-SAT clause conditioned on root un-favorability. The construction yields 66 distinct clauses per root, thus 4224 clauses. Add
\[
\boxed{\sum_{z=0}^{63}b_z\ge29.}
\tag{C}
\]
The resulting finite SMT-LIB formula was verified **UNSAT** with Z3 4.13.3. If any two-hub coloring had at least 29 unfavorable roots, choose b_z=true at 29 of them; the formula would be satisfiable. Contradiction. Hence Q6 has at least 36 favorable roots and the asserted nine-sixteenths bound follows in every dimension by compression.

The generated check input comprises 4224 implication clauses and (C). The generator and SMT-LIB files are named nori_two_hub_sat_certificate.py and nori_two_hub_29_bad_unsat.smt2; their SHA256 fingerprints are respectively 440bb657a03e0024e1035e37d58fb260a66cf23ae3ae9b91294e396ba2aeef70 and 78930da53de38a93e48c94d861d8e6d2d8f29d0313e2290ab4b72cf715074d11. The check script also independently counts roots in the following sharp witness.

*Sharpness.* Choose
\[
f_0=1+x_3,\qquad f_1=1+x_5
\]
and retain the four leaf rules above. This is the Cartesian product of two three-dimensional sharp nonlinear-star colorings, each having 6 favorable roots and 4 paired roots. Thus the six-dimensional product has precisely 36 favorable and 16 paired roots. Paired-root inclusion-exclusion in any n-dimensional coloring gives
\[
|P(f)|=|A(f)\cap\bar A(f)|\ge2|A(f)|-2^n,
\]
giving the one-eighth bound in (A). The displayed witness proves sharpness of the favorable-root bound; its paired-root density is one quarter, so it does not prove sharpness of the one-eighth paired-root bound. \(\square\)

**Corollary (closure of all two-branch dependency components).** If every strongly connected component of the directed dependency graph of an arbitrary cube-edge coloring has at most two vertices with internal indegree greater than one, then the coloring has a paired root.

*Proof.* A terminal SCC with no or one branching target is handled by the earlier directed-cycle or rooted-tree feedback theorem. With two branching targets, the unique-predecessor forest lemma compresses its nonhub trees to a two-hub star. At every fixed outside assignment the component fiber is a coloring of this class, so by (A) at least nine-sixteenths of its roots are favorable. Any two such fiber favorable sets intersect after antipodal complementation in at least
\[
\boxed{(2\cdot9/16-1)2^s=2^{s-3}}
\]
roots for a component of size s. Paired-root fiber gluing therefore removes the terminal SCC. Induct over the component condensation DAG. \(\square\)

**Remaining closure target.** If NORI1 fails, a minimal paired-root counterexample must have a terminal strongly connected dependency component with at least **three independent branching targets**. The bounded hub compression reduces k such targets to at most 3k dimensions, but for k>=3 a general density majority cannot hold, as independent star products show. A cross-fiber intersection principle stronger than majority is still needed. The result above is computer-assisted and does not yet provide an elementary six-dimensional proof or unrestricted NORI1.

#### Median structure and robust cross-fiber two-hub gluing

**Theorem (median closure of prescribed unfavorable roots).** Fix a two-hub star leaf template (the controlling hub and offset of each leaf), and let U denote the set of Boolean assignments to all hub-edge table entries. For a root z, let \(\mathcal B_z\subseteq U\) be the assignments for which z has no full geodesic of word \(0^*1^*\). Then \(\mathcal B_z\) is the solution set of a 2-CNF formula. For every set R of prescribed unfavorable roots, the intersection
\[
\boxed{\mathcal B_R=\bigcap_{z\in R}\mathcal B_z}
\]
is closed under the componentwise ternary majority operation.

*Proof.* The previous hub SAT theorem expresses each \(\mathcal B_z\) as a conjunction of clauses with at most two hub-table variables. Intersections retain the 2-CNF form. If three assignments satisfy a two-variable clause, their pointwise majority cannot violate it: if both clause terms were false in the majority, each term would be false in at least two of the three assignments, and the two subsets of size at least two intersect, yielding an input assignment violating the clause. Thus the majority satisfies every clause. \(\square\)

**Corollary (implication-cycle obstruction certificates).** If no hub coloring simultaneously makes all roots in R unfavorable, the joint 2-CNF is unsatisfiable. Consequently its implication digraph contains a hub-bit variable X for which directed paths exist from \(X=0\) to \(X=1\) and back. Each implication has a two-step square-path witness in the underlying root constraints; the eight-path certificate for roots 0,3,23 is an illustrative short instance. This characterization is uniform in the leaf count and nonlinear hub functions.

**Theorem (arbitrary cross-star favorable intersection; computer-assisted via sharp bound).** Let f and g be any two two-hub star edge colorings on the *same* \(Q_d\), with arbitrarily differing nonlinear hub functions, leaf offsets, and leaf-to-hub assignments. Then
\[
\boxed{|A(f)\cap\overline{A(g)}|\ge 2^{d-3}.}
\tag{D}
\]
The two colorings need not share a dependency pattern other than each having at most two hubs and every other direction colored by an affine function of one of its hubs or a constant.

*Proof.* The sharp two-hub computer-assisted theorem gives \(|A(f)|,|A(g)|\ge(9/16)2^d\). Antipodal complement preserves cardinality. Inclusion-exclusion yields the lower bound \((2\cdot9/16-1)2^d=2^{d-3}\). Constant-colored leaves are harmless: their edge colors are independent of every other dimension and a full constant-color leaf traversal can be placed in the appropriate zero or one segment of any favorable full path, so favorable-root density does not diminish under their addition. \(\square\)

**Lemma (fiberwise disappearance of tree predecessor arrows).** Suppose a directed dependency SCC in the full coloring has precisely two branching hubs and every other direction has one predecessor, so its underlying nonhub arrows form outward trees from the two hubs. Fix any outside assignment. The induced fiber coloring can deactivate some parent arrows, leaving \(f_i=a_i+\lambda_i x_{p(i)}\) with \(\lambda_i\in\{0,1\}\). The fiber's favorable-root density remains at least nine-sixteenths, and its paired-root density at least one-eighth.

*Proof.* Remove every inactive parent arrow from the outward trees. The resulting components not attached to either hub are rooted subtrees with a constant-color top edge. Each can be traversed monochromatically in that top color from **every** starting root, by orienting the active descendant parent-child dependencies to attain the same color. The color functions of those components are independent of all directions outside the component: the removed parent arrow has coefficient zero, and the other outgoing dependencies remain inside its descendant tree, while all feedback arrows in the global graph enter the hubs and do not alter edge colors of these tree components. Thus these tree components are Cartesian factors whose favorable-root sets are the entire component cubes. Their insertion at a favorable path's zero-to-one seam (on the zero or one side, as appropriate) preserves all dimensions and color monotonicity. Removing them therefore preserves or increases favorable-root density and paired-root density.

The residual component has two hubs and active outward rooted trees. Apply the monochromatic macro-forest compression to produce a two-hub star with at most two leaf types per hub, and apply the computer-assisted nine-sixteenths theorem. Reinsert the independent monochromatic tree components; every root in them can be used, so the same density lower bound holds for the full fiber. Antipodal inclusion-exclusion yields the paired-root bound. \(\square\)

This supplies the missing fiberwise activation check in the SCC corollary of the nine-sixteenths theorem. Cross-fiber compatibility now holds even if different outside assignments suppress different predecessor arrows and change the active tree shapes. The case of three or more branching hubs remains open; its unfavorable-root constraint is generally 3-CNF or wider, and no analogous majority-closure argument follows automatically.

##### Correction to the vanished parent-arrow argument

The conclusion of the inactive-parent SCC lemma remains valid, but its previous claim that detached trees form Cartesian factors of the **entire** coloring was erroneous: hub edge colors may still depend on detached tree bits.

**Correct proof via one-way fiber insertion.** Fix the external bits of a two-branch SCC. Delete inactive parent arrows in the outward predecessor forest. Let A consist of the resulting subtrees detached from both hubs; let B consist of the remaining hub-rooted active forest. Every A-direction edge color is independent of B-bits, because A-direction color functions depend only on active parent bits within their detached subtree, or are constant at the detached top vertex. Hub-direction colors may nevertheless depend arbitrarily on A-bits; no two-sided independence is assumed.

Every root of the A-block is favorable: each detached tree can be traversed monochromatically, in the constant color of its top edge, by orienting its active parent-child relations. Since different A-trees have no dependencies between their edge colors, concatenate their zero-colored full paths followed by their one-colored full paths.

For each A-starting root z, choose a favorable full A-path and its zero-to-one seam y. At fixed y the induced B-fiber has an active outward forest on two hubs, and the published macro-forest compression reduces it to a two-hub star. The computer-assisted theorem gives at least nine-sixteenths favorable roots in *each* such B-fiber. Insert any favorable B-fiber path at seam y. This yields at least ((9/16)2^{|B|}) favorable combined roots above each z, hence
[
\boxed{|A(F)|\ge(9/16)2^{|A|+|B|}.}
]
The bound also holds for every earlier-parameter fiber of the SCC, so any two favorable sets have an antipodally complemented intersection of size at least (2^{|SCC|-3}) by inclusion-exclusion. The paired-root SCC deletion conclusion is therefore unchanged.

This note **supersedes the Cartesian-factor assertion** in the preceding lemma. The correct structural relation is one-way dependence, with detached trees outside and the two-hub core inside; seam insertion, not Cartesian factorization, proves the bound.

##### Directional influence components and monotone seam insertion

For an arbitrary binary coloring \(f\) of the undirected edges of \(Q_d\), write \(f_i(x)\) for the direction-\(i\) edge color, independent of the bit \(x_i\). Define the **directed influence graph** \(D(f)\) by placing an arc
\[
j\to i\quad\Longleftrightarrow\quad
\partial_jf_i(x)=f_i(x)+f_i(x\oplus e_j)
\]
is nonzero at some cube vertex. This records which direction changes can affect the colors of other directions. The undirected interaction graph forgets these arc directions.

Let \(A_0(f)\) and \(A_1(f)\) denote roots admitting full dimension-simple geodesics with color words \(0^*1^*\) and \(1^*0^*\), and put \(P(f)=A_0(f)\cap A_1(f)\). Define the cross-orientation intersection constant
\[
\kappa_k=\min_{g,h:E(Q_k)\to\{0,1\}}|A_0(g)\cap A_1(h)|.
\tag{1}
\]
The known dimension-one, square, and three-cube favorability results imply
\[
\boxed{\kappa_1=2,\qquad\kappa_2=2,\qquad\kappa_3=4.}
\tag{2}
\]
For \(k=3\), the lower bound follows from \(|A_0(g)|,|A_1(h)|\ge6\) and inclusion-exclusion among eight roots; equality is furnished by the product of an extremal colored square with a constant-colored one-cube. For \(k=4\), the previously recorded computer-assisted result \(m_4=9\) and the crossed-square construction give \(\kappa_4=2\), conditional on that finite computation.

**Theorem 1 (seam-lifting across a one-way dependence block).** Partition the directions as \(R\sqcup S\). Suppose all \(R\)-direction edge colors are independent of the \(S\)-bits, while the \(S\)-direction colors may depend arbitrarily on both their own bits and the \(R\)-bits. Denote the fixed induced \(R\)-coloring by \(f_R\), and the \(S\)-coloring at \(R\)-state \(y\) by \(g_y\). Then
\[
\boxed{|P(f)|\ge\kappa_{|S|}\,|P(f_R)|.}
\tag{3}
\]

*Proof.* Choose \(x\in P(f_R)\). Select an \(R\)-geodesic \(P_0\) from \(x\) with word \(0^a1^{|R|-a}\), and a second geodesic \(P_1\) from the same \(x\) with word \(1^b0^{|R|-b}\). Let \(y_0,y_1\) be the respective \(R\)-vertices immediately after the zero prefix and after the one prefix. Their locations may differ.

By (1), at least \(\kappa_{|S|}\) roots \(z\in Q_S\) belong to \(A_0(g_{y_0})\cap A_1(g_{y_1})\). From each such \(z\), insert a complete \(0^*1^*\) geodesic of the \(S\)-block at the seam of \(P_0\), and a complete \(1^*0^*\) \(S\)-geodesic at the seam of \(P_1\). During an inserted block the \(R\)-bits do not change, so its edge colors come from the stated induced coloring. The remaining \(R\)-steps retain their colors because no \(R\)-edge depends on the \(S\)-bits. Both enlarged paths start at \((x,z)\), use each dimension once, and have the desired opposite monotone words. Therefore every such \((x,z)\) is paired. Counting these distinct roots proves (3). QED.

**Theorem 2 (strongly connected component bound).** Let \(C_1,\ldots,C_t\) be the strongly connected components of \(D(f)\), in topological order of the condensation digraph. Then
\[
\boxed{|P(f)|\ge\prod_{\nu=1}^{t}\kappa_{|C_\nu|}}
\tag{4}
\]
whenever the factors on the right are positive.

*Proof.* For every topological prefix \(R=C_1\cup\cdots\cup C_{\nu-1}\), no edge-color function of a direction in \(R\) depends on a bit belonging to a later component. Such dependence would give a directed arc entering the prefix, contrary to the topological order. Therefore Theorem 1 applies when adjoining \(C_\nu\) to the prefix. Begin with the dimension-zero cube, whose empty root supports both empty monotone words, and multiply the estimates (3) along the component order. QED.

**Corollary 3 (unrestricted nonlinear closure for feedback components of size at most three).** If every strongly connected component of \(D(f)\) has size at most three, then \(P(f)\ne\varnothing\). If \(t_j\) is the number of components having \(j\) dimensions, then
\[
\boxed{|P(f)|\ge2^{t_1+t_2+2t_3}.}
\tag{5}
\]
In particular, when \(D(f)\) is acyclic, every cube vertex is paired, even if its underlying undirected interaction graph is complete.

*Proof.* Insert (2) into Theorem 2. In the acyclic case \(t_1=d\), and the lower bound equals all \(2^d\) roots. QED.

**Corollary 4 (computer-assisted component-size-four extension).** Assuming the previously reported integer-optimization certificate that every coloring of \(Q_4\) has at least nine nondecreasing feasible roots, Theorem 2 extends paired-root existence to all colorings with directed influence components of size at most four, with
\[
\boxed{|P(f)|\ge2^{t_1+t_2+2t_3+t_4}.}
\tag{6}
\]
This extension relies on that finite calculation; Corollary 3 has a noncomputational proof.

**Corollary 5 (feedback-size obstruction for a hypothetical counterexample).** Any paired-root-free coloring must possess a strongly connected directed influence component involving at least four dimensions. Subject to the computer-assisted four-cube bound, the size must be at least five. A directed cycle somewhere is therefore necessary but far from sufficient: feedback must organize into a large mutually dependent block.

**Corollary 6 (NORI1 for facets with small directed feedback components).** Suppose an antipodally odd edge coloring of \(Q_{d+1}=Q_d\times\{0,1\}\) restricts on its lower facet to a coloring whose directed influence components have sizes at most three. Then at least \(2^{t_1+t_2+2t_3}\) distinct directed monochromatic full antipodal geodesics exist, each using a different vertical bridge. The bridge colors are otherwise arbitrary. The same conclusion extends to components of size four subject to the finite four-cube certificate.

*Proof.* Combine Corollary 3 with the universal free-bridge equivalence of the gauge-criticality Subsection. Each paired lower-facet root supplies a monochromatic geodesic across its designated vertical bridge. QED.

**Proof-closure perspective.** The seam-lifting theorem isolates the difficulty inside mutually dependent feedback blocks. Directed acyclic attachments may be absorbed in any dimension without losing dimension-simplicity, and small strongly connected blocks are handled by cross-orientation root intersection. A successful intersection theorem for arbitrary large feedback blocks would propagate automatically through all their directed attachments. The unrestricted NORI1 and ordinary boundary 3-tournament conjectures remain open.### Conditional cross profiles and hybrid feedback-block closure

The universal intersection constants \(\kappa_m\) consider all binary colorings of \(Q_m\). In the directed influence decomposition of one fixed coloring, the next strongly connected block usually encounters only a restricted family of conditional colorings, indexed by earlier-bit assignments. Cross-intersection for that family alone suffices.

For a component \(C_\nu\) following a topological prefix \(R_\nu\), denote the induced \(C_\nu\)-coloring at earlier state \(y\in Q_{R_\nu}\) by \(g_y^{(\nu)}\), and set
\[
\rho_\nu=\min_{y,y'\in Q_{R_\nu}}
|A_0(g_y^{(\nu)})\cap A_1(g_{y'}^{(\nu)})|.
\tag{8}
\]

**Theorem 7 (conditional component product theorem).**
\[
\boxed{|P(f)|\ge\prod_{\nu}\rho_\nu.}
\tag{9}
\]

*Proof.* Fix a paired root and two oppositely monotone full paths in the already constructed prefix. Their zero-to-one and one-to-zero seam vertices are possibly different prefix states \(y_0,y_1\). By the definition of \(\rho_\nu\), at least \(\rho_\nu\) roots of the next block admit both a nondecreasing full geodesic for coloring \(g_{y_0}^{(\nu)}\) and a nonincreasing full geodesic for \(g_{y_1}^{(\nu)}\). Insert these block geodesics into their respective prefix-path seams. All earlier-direction edge colors are independent of the later block bits, so the words remain monotone and the paths remain dimension-simple. Multiply the number of paired roots at each topological stage. QED.

**Corollary 8 (nonlinear star feedback blocks of any dimension).** If the conditional colorings on a component \(C_\nu\) of size \(m\ge2\) all have star interaction graphs, with hub directions and nonlinear functions allowed to vary with the preceding state, then
\[
\boxed{\rho_\nu\ge2^{m-1}.}
\tag{10}
\]
Indeed any two star colorings have at least \(3\cdot2^{m-2}\) roots in their respective required orientations; inclusion-exclusion forces at least \(2^{m-1}\) common roots.

**Corollary 9 (changing square matchings).** Let a component \(C_\nu\) have an even number \(m=2r\) of directions. Suppose each conditional coloring is a Cartesian product of arbitrary colored squares, but the perfect matching \(M_y\) of directions defining its product may depend on the earlier state \(y\). Then
\[
\boxed{\rho_\nu\ge\min_{y,y'}2^{c(M_y,M_{y'})}\ge2,}
\tag{11}
\]
by the all-dimensional crossed-matching intersection theorem. Here \(c(M,N)\) counts the alternating cycles in the multigraph formed by the two matchings.

**Corollary 10 (hybrid component closure).** Every binary edge coloring of \(Q_d\) has a paired root if every strongly connected component of its directed influence graph belongs to at least one of the following classes: a component of size at most three; a component whose conditional colorings are all star colorings; or an even-sized component whose conditional colorings all factor into colored squares, with the pairing permitted to vary between conditional states. The previous computer-assisted four-cube cross bound also permits arbitrary components of size four.

**Unbounded non-star feedback example.** Let \(c\) be one predecessor direction with constant edge color zero, followed by \(2r\) further directions. In the \(c=0\) facet color the further directions by Cartesian copies of a two-direction coloring \(h\) with both cross-dependencies nonzero, using matching \(M=(1,2),(3,4),\ldots,(2r-1,2r)\). In the \(c=1\) facet use the same square coloring along shifted matching \(N=(2,3),(4,5),\ldots,(2r,1)\). The directed influence graph on the later \(2r\) directions contains both orientations of every edge of \(M\cup N\), a connected even cycle. Thus it is one strongly connected feedback block of unbounded size, whose underlying interaction graph is non-star when \(r\ge2\). Still its two conditional colorings are square products, so (11) and (9) give at least four paired roots in the full cube.

**Closure interpretation.** The difficulty is not merely the existence or size of directed feedback, or the lack of a fixed square factorization. The remaining problem is to understand the cross-intersection behavior of conditional favorable-root families inside irreducible feedback components. Theorem 7 localizes the desired structural argument there, without unnecessarily demanding an intersection theorem for every possible coloring of a given order.

##### Constructive algorithm for bounded directed feedback components

**Theorem 11 (linear-query paired-root construction).** Suppose the directed influence graph of an arbitrary binary edge coloring \(f\) of \(Q_d\) is supplied with its strongly connected components in topological order, each of size at most three. Then one paired root and full witnesses of both monotone orientations can be constructed using \(O(d)\) edge-color queries and \(O(d^2)\) elementary bit/list operations. The query estimate is conditional on being given the component decomposition; verifying the influence graph from an unrestricted black-box coloring may itself require exponentially many queries.

*Proof.* Start with the empty dimension prefix, its empty root, and the two empty witness paths. Process the components \(C_\nu\) in topological order. At each step, recover the zero-to-one seam vertex \(y_0\) of the current first witness and the one-to-zero seam vertex \(y_1\) of the second. Read the edge colors in the two induced colorings \(g_{y_0}^{(\nu)}\) and \(g_{y_1}^{(\nu)}\) of \(Q_{|C_\nu|}\).

For a component of size \(s\le3\), each induced \(s\)-cube has \(s2^{s-1}\le12\) edges, so both together require at most 24 color queries. Enumerate the at most \(2^s\le8\) possible new-block roots and the at most \(s!\le6\) direction orders. Test which roots support a \(0^*1^*\) path in the first induced coloring and a \(1^*0^*\) path in the second. The cross-intersection bounds \(\kappa_1=2,\kappa_2=2,\kappa_3=4\) guarantee a common root. Insert its two chosen block paths at the old seam vertices, preserving both monotone words and using each direction once by Theorem 1.

There are at most \(d\) components and each adds at most three dimensions, so at most \(24d\) color queries suffice, aside from the constant-size bookkeeping of the existing paths. Maintaining the two ordered lists of traversed directions and their seam positions costs \(O(d^2)\) elementary operations over all stages, with bit-vector representations of cube states. The final root and two full paths are explicit. QED.

**Corollary 12 (constructive monochromatic NORI1 path).** In an antipodally odd coloring of \(Q_{d+1}\) whose lower-facet directed influence components are all of size at most three, one can construct a monochromatic dimension-simple antipodal geodesic using the preceding paired-root algorithm and one additional vertical bridge-color query, again conditional on the supplied influence-component decomposition. The free-bridge path reconstruction is given in the star algorithm Subsection.

**Further computational extension.** Under the finite four-cube certificate \(\kappa_4=2\), the same procedure handles components of size four, still with a constant number of queries per component (at most 64 queries for two four-cube induced colorings). The analytical size-three algorithm requires no such certificate.

#### Functional-dependency colorings: full root classification and Hall cross-root theorem

Call a cube-edge coloring f **functional** if each direction-i color depends on at most one other direction bit:
\[
f_i(x)=a_i+\lambda_i x_{p(i)},\qquad a_i,\lambda_i\in\mathbb F_2,
\]
where lambda_i=0 is a constant direction color, and p(i) differs from i whenever lambda_i=1. Direct an active dependency arrow p(i)->i. Its connected components are rooted outward trees or outward trees attached to a directed cycle; distinct dependency cycles have disjoint direction sets.

For any root x and any active i, put \(b_i=a_i+x_{p(i)}\). Write A0(f) and A1(f) for the starting roots of full dimension-simple geodesics whose edge-color words are respectively 0*1* and 1*0*.

**Theorem 1 (complete favorable-root classification).** For every functional coloring,
\[
\boxed{x\in A_0(f)\iff
\text{each directed dependency cycle }C\text{ has some }i\in C\text{ with }b_i=0.}
\tag{1}
\]
\[
\boxed{x\in A_1(f)\iff
\text{each directed dependency cycle }C\text{ has some }i\in C\text{ with }b_i=1.}
\tag{2}
\]
In particular, if \(\mathcal C(f)\) is its family of feedback cycles,
\[
\boxed{|A_0(f)|=|A_1(f)|
=2^n\prod_{C\in\mathcal C(f)}(1-2^{-|C|}).}
\tag{3}
\]

*Proof.* The color traversed in direction i is \(b_i+[p(i)\text{ before }i]\) modulo two. If every b_i=1 on a feedback cycle, the first cycle direction traversed has color one, while its last has color zero. This descent rules out a 0*1* full geodesic. Conversely, for a feedback cycle whose b-values contain both bits, orient each dependency comparison so that its traversed direction has color zero. The orientation is acyclic because the b-values are not constant, and gives an all-zero full cycle traversal. If every b_i=0 on a feedback cycle, traverse its directions in reverse dependency order, producing \(0^{|C|-1}1\).

For every direction i in a tree growing outward from such a cycle, or from a constant-colored tree root, orient its parent comparison so that direction i takes the **same color as its parent**:
\[
[p(i)\text{ before }i]=a_i+x_{p(i)}+c_{p(i)}.
\]
The tree edges introduce no directed cycles or color-descending comparisons. All comparison orientations therefore form an acyclic digraph, with no arrow from a color-one direction to a color-zero direction. Topologically sort all color-zero directions before all color-one directions to obtain the desired full geodesic. Color complementation proves (2).

A feedback cycle C forbids just one assignment to the starting bits whose indices lie in C, because the predecessor map permutes that set. These cycle sets are disjoint within one coloring. Multiplying the allowed assignments gives (3). QED.

**Theorem 2 (Hall's marriage theorem for two unrelated functional colorings).** For any two functional colorings f,g on the same Q_n,
\[
\boxed{A_0(f)\cap A_1(g)\ne\varnothing.}
\tag{4}
\]
If the two dependency digraphs contain respectively r and s directed feedback cycles, then
\[
\boxed{|A_0(f)\cap A_1(g)|\ge2^{n-r-s}.}
\tag{5}
\]
Their controlling predecessor maps and underlying interaction graphs can differ arbitrarily; the union interaction graph need not be a path, forest, or cycle.

*Proof.* By (1), each directed feedback cycle C of f forbids a single assignment to all root bits indexed by its directions; by (2), each directed feedback cycle D of g forbids one such assignment on D. All cycles within f are pairwise disjoint, and likewise all cycles within g. Each forbidden-cycle condition involves at least two starting-bit indices, since self-influence is impossible; each starting-bit index participates in at most two conditions, at most one from each coloring.

Construct a bipartite incidence graph from the forbidden-cycle conditions to their participating starting-bit indices. For any subset S of the conditions, the number of incidences is at least 2|S| and at most 2|N(S)|, hence \(|N(S)|\ge|S|\). Hall's marriage theorem gives an injection assigning each forbidden-cycle condition its **own different starting-bit index**. Set that bit to disagree with the corner value forbidden by the assigned condition. All other bits may be chosen freely. Every forbidden corner is thereby avoided, so the root satisfies both (1) and (2). There are \(n-r-s\) unmatched bits, whose assignments are arbitrary; this gives at least \(2^{n-r-s}\) common roots. The constructive orientations of Theorem 1 recover both monotone full dimension orders. QED.

**Theorem 3 (t-coloring extension).** Let \(f^{(1)},\ldots,f^{(t)}\) be functional colorings, and prescribe independently one orientation A0 or A1 for each. If every directed feedback cycle of every coloring has length at least t, then
\[
\boxed{\bigcap_{h=1}^t A_{\epsilon_h}(f^{(h)})\ne\varnothing.}
\tag{6}
\]
Indeed each forbidden-cycle condition involves at least t starting-bit indices, while each such bit appears in at most t conditions. Hall's incidence criterion therefore applies again. If R is the total number of feedback cycles across the t colorings, the construction supplies at least \(2^{n-R}\) common roots.

**Closure implications.** The theorem covers projection/constant cyclic-local pairs even when the union of their interaction graphs forms a full cycle or multiple nontrivial components. It bypasses favorable-root density, parity-cycle repair, and finite-state path enumeration. A counterexample to unrestricted cyclic cross-favorability must contain a local direction rule that depends on **both** neighboring bits in at least one of the two colorings; two independent one-predecessor rules are insufficient. Theorem 3 gives a simultaneous multicoloring extension when feedback cycles are long.

**Audit.** An independent full-order enumeration compared (1),(2) with all starting roots for 250 random functional-dependency colorings per dimension n=2,3,4,5, with no disagreements. The argument itself is all-dimensional.

#### Sharp two-root strengthening of the functional Hall theorem

**Corollary (two distinct common favorable roots).** Under the hypotheses of the preceding Hall theorem, for any two functional cube-edge colorings f,g on Q_n, n>=2,
\[
\boxed{|A_0(f)\cap A_1(g)|\ge2.}
\tag{7}
\]
This is sharp, already for n=2.

*Proof.* By Theorem 2, at least one root x avoids every forbidden feedback-cycle corner. Let m be the total number of forbidden-cycle conditions from the two colorings. Since each condition has at least two participating root bits and every bit occurs in at most two conditions, m<=n.

A root bit j is **pivotal** at x if flipping it destroys one of the satisfied cycle conditions. This happens only when some cycle condition is satisfied by a **single** mismatching root bit, namely j. Each such cycle condition can make at most one bit pivotal. Thus there are at most m pivotal bits.

If m<n, some bit is not pivotal, so flipping it gives a second root satisfying all conditions.

If m=n, the incidence inequalities are tight: every cycle condition has length two, and every root bit belongs to two cycle conditions. Again, if some bit is not pivotal, flip it. Otherwise all n bits are pivotal and all n cycle conditions must each be satisfied by **precisely one** mismatching bit. Complement the whole root x. On each two-bit condition, the originally mismatching bit becomes matching and the originally matching bit becomes mismatching. Each condition still has one mismatch, so the antipodal root is also favorable in f and g. Since n>=2, it differs from x. This proves the bound.

For sharpness take n=2 with both f and g having reciprocal dependencies \(f_0=g_0=x_1,\ f_1=g_1=x_0\). The f-nondecreasing favorable roots exclude only 11; the g-nonincreasing roots exclude only 00; the intersection consists of 01 and 10. QED.

The argument is a combinatorial strengthening of Hall's matching certificate, not a density estimate. In the critical equality case, the antipodal map supplies a second solution automatically.

#### Sharp obstruction to three-way cross-favorability with short feedback cycles

The t-coloring Hall extension above requires each feedback cycle to have length at least t. This cycle-size condition matters: even three **functional** colorings of Q4 need not possess a common favorable root, although every pair does.

**Proposition (a four-direction, three-coloring obstruction).** Let the four directions be 0,1,2,3. Define three functional colorings F,G,H by their controlling-predecessor maps:
\[
\begin{array}{l}
F_0=1+x_1,\ F_1=1+x_0,\ F_2=1+x_3,\ F_3=1+x_2;\\
G_0=1+x_2,\ G_2=1+x_0,\ G_1=1+x_3,\ G_3=1+x_1;\\
H_0=x_3,\ H_3=x_0,\ H_1=x_2,\ H_2=x_1.
\end{array}
\]
Then
\[
\boxed{A_0(F)\cap A_0(G)\cap A_0(H)=\varnothing.}
\tag{8}
\]
Nevertheless every two of these three favorable-root sets intersect, by the preceding universal two-coloring Hall theorem.

*Proof.* Each coloring consists of two reciprocal directed dependency pairs. Theorem 1 shows that F forbids the root-bit corner 00 on pairs {0,1},{2,3}, and G forbids 00 on {0,2},{1,3}. Thus the indices with starting bit zero cannot include both an index of A={0,3} and an index of B={1,2}, because the four cross pairs form precisely the edges of the complete bipartite graph K_(2,2).

But H forbids the corner 11 on the two within-group pairs {0,3} and {1,2}. Hence each of A and B must contain at least one zero starting bit. That contradicts the first two constraints. Therefore no common root exists. QED.

This shows why the unrestricted pairwise cross-root theorem cannot simply be strengthened to arbitrary finite families. The t-coloring extension with feedback-cycle sizes at least t remains valid; the example has three colorings but two-direction feedback cycles and violates that sufficient hypothesis.

#### Antipodal double-failure formula and hybrid cross-root thresholds

Let f be any functional-dependency cube coloring. Let its directed feedback cycles have lengths \(\ell_1,\ldots,\ell_r\ge2\). Write
\[
B_f=V(Q_n)\setminus A_0(f),\quad
S_f=B_f\cap\overline{B_f}
\]
for roots where the f-nondecreasing orientation fails and where it fails at **both antipodal roots**, respectively.

**Theorem 4 (double-failure census).** With \(p_j=2^{-\ell_j}\),
\[
\boxed{
|S_f|=2^n\left[1-2\prod_{j=1}^r(1-p_j)
+\prod_{j=1}^r(1-2p_j)\right].
}
\tag{9}
\]
In particular S_f is empty whenever f has at most one feedback cycle.

*Proof.* On a feedback cycle C_j, the initial-color vector \((a_i+x_{p(i)})_{i\in C_j}\) runs over all binary strings uniformly as the starting root varies, because the predecessor map permutes the cycle directions. Distinct cycles use disjoint starting bits, so these vectors are independent. By Theorem 1, x fails A0(f) iff at least one cycle is all one. Its antipode fails A0(f) iff at least one cycle is all zero, since complementing x complements the initial-color vector on every active cycle. For cycle j, the all-one and all-zero events each have probability p_j and are disjoint. Inclusion-exclusion across the independent cycle events yields the displayed formula. \(\square\)

**Lemma 5 (antipodal transversal criterion).** Let g be any binary cube-edge coloring with paired-root set \(P(g)=A_0(g)\cap A_1(g)\). Then
\[
\boxed{|P(g)|>|S_f|\ \Longrightarrow\
A_0(f)\cap A_1(g)\ne\varnothing.}
\tag{10}
\]
In particular if f has at most one directed feedback cycle and g has even one paired root, the cross-root intersection is nonempty.

*Proof.* Reversing a full dimension-simple geodesic from x starts at its antipode and reverses its color word. Hence \(A_1(g)=\overline{A_0(g)}\) and P(g) is closed under antipodal complementation. If the cross intersection were empty, P(g) would be contained in B_f. Antipodal closure of P(g) would then imply \(P(g)\subseteq B_f\cap\overline{B_f}=S_f\), contradicting the cardinality inequality. \(\square\)

**Corollary 6 (functional with up to four cycles versus an arbitrary star).** If f is functional with at most **four** feedback cycles and g has a star direction-interaction graph, then
\[
\boxed{A_0(f)\cap A_1(g)\ne\varnothing.}
\]
The star center function may be any nonlinear Boolean function, and its leaf functions may be arbitrary one-bit functions.

*Proof.* Each p_j<=1/4. The probability that among r independent variables taking states all-one, all-zero, other with probabilities p_j,p_j,1−2p_j, both extreme states occur is increasing in every p_j and in r. Thus the bracket in (9) is at most its value with four p_j=1/4:
\[
1-2(3/4)^4+(1/2)^4
=\boxed{55/128}<1/2.
\]
The established nonlinear star theorem gives \(|P(g)|\ge2^{n-1}\). Apply Lemma 5. \(\square\)

**Corollary 7 (hybrid with the computer-assisted two-hub class).** Suppose f is functional and has at most two directed feedback cycles, not both of length two. Suppose g is any coloring covered by the sharp two-hub favorable-root theorem, so that \(|P(g)|\ge2^{n-3}\). Then
\[
\boxed{A_0(f)\cap A_1(g)\ne\varnothing.}
\]
With two f-cycles the double-failure fraction in (9) equals \(2p_1p_2\), strictly less than 1/8 unless both lengths are two; with fewer than two cycles it is zero. Apply Lemma 5.

**Scope.** These are all-dimensional hybrid cross-orientation theorems that permit f and g to have unrelated interaction graphs, and allow nonlinear color behavior in g. The census also identifies where this direct antipodal-size method can fail: for five or more short feedback cycles the fraction of doubly excluded antipodal roots can exceed one-half, so merely knowing that g has half its roots paired no longer guarantees an intersection. Additional geometric information is needed there.

#### Protected bit fiber and nonlinear star opponent

**Theorem.** Let f be functional and g an arbitrary nonlinear star coloring with center direction h. Then A0(f) intersects A1(g), independent of the number of feedback cycles in f.

**Proof.** For every feedback cycle C of f choose a starting bit index in C other than h (possible because each cycle has at least two directions). Different cycles use disjoint bits. Assign these chosen bits opposite to their forbidden f-corner values. Then BOTH completions of the remaining h bit are favorable for f, by the functional cycle classification. The earlier fiberwise star theorem says that for each fixed assignment of leaf bits, at least one of the two hub-bit completions is a paired root of g. Choose that completion. It is in A0(f) and A1(g). QED.

**Generalization.** If H is any direction set containing no entire f feedback cycle, one can assign the bits outside H to make the whole H-fiber favorable for f. If a second coloring g admits some paired root on each H-fiber, then the two colorings are cross-favorable. This is the protected bit-block gluing lemma. The earlier four-cycle counting threshold is superseded for nonlinear star opponents.

**Active rooted-tree variant.** The same result holds when g is a rooted active tree with arbitrary nonlinear hub color: compress each full rooted branch into a monochromatic macro-leaf. For each fixed nonhub assignment, the fiberwise star theorem supplies a paired hub-bit completion in the compressed star; expand both favorable macro-geodesics into full monochromatic tree-block traversals. Thus g has a paired root in every hub-bit fiber, and the protected bit lemma applies.

#### Constructive Hall root extractor and independent full-geodesic audit

The Hall-based functional cross-favorability theorem admits an algorithm constructing the common root and both full dimension-simple geodesics. Find each directed feedback cycle of f and g by following the unique predecessor pointer from each dimension. For each f-cycle create its forbidden root-bit assignment with b_i=1 for all i; for each g-cycle use b_i=0 for all i. Build the cycle-to-root-bit incidence graph and use a bipartite matching to choose one distinct starting bit per forbidden cycle. Set the chosen bit opposite to the corner assignment forbidden by its matched cycle, leaving other bits free.

At the resulting root, orient every feedback cycle of f for a 0*1* path, and every feedback cycle of g for a 1*0* path. To orient a feedback cycle for 0*1*, if its initial colors b_i are mixed, make all traversed cycle colors zero by orienting each predecessor relation according to b_i; the mixed bits exclude a consistently cyclic order. If all initial colors are zero, traverse the directed feedback cycle in the reverse cyclic order, producing 0^(length-1)1. Every outward tree edge is then oriented so that the child direction traverses in its parent direction's color. The resulting comparison graph is acyclic and has no color-one to color-zero arrow. Topologically order all color-zero directions before color-one directions. For g reverse the target colors (equivalently complement its entire edge-coloring) and apply the same construction.

**Independent validator.** The source file nori_functional_hall_validator.py implements this procedure separately from the mathematical argument, and recomputes the full cube-edge color at each traversed step of each returned dimension order. It passed 100 independent random functional f/g pairs at each n=2,3,5,10,30,100 (600 tests), with no failures. Each test includes arbitrary active predecessor maps, constants, short or long feedback cycles, and outward branching. A separate root-by-root full-permutation enumeration through n=5 verified the favorable-root classification before the Hall extractor was implemented. The existence proof is combinatorial; finite checks are corroborative.

#### Necessary local obstructions to cyclic cross-root closure

For cyclic-neighbor local colorings f,g, failure of A0(f) intersect A1(g) requires ALL of the following: (i) the union direction-interaction graph contains the entire cycle, because removing any common interaction edge reduces to the proved path theorem; (ii) no direction is constant in both f and g, because the cyclic constant-site corollary permits deletion and extreme reinsertion; (iii) at least one direction j has empty local success set D_j={neighbor inputs with f_j=0 and g_j=1}, because the all-dimensional nonempty-overlap theorem settles every pair without such a site; and (iv) at least one local direction rule in f or g depends on BOTH neighboring bits, because the new functional Hall theorem settles any pair of projection/constant local colorings, with at least two common roots. These necessary conditions are not sufficient for failure. They isolate overlapping two-parent feedback near locally deficient directions as the remaining proof target. The protected bit-selector theorem also works with the two colors swapped, solving any functional-versus-fiberwise-paired nonlinear star or active rooted feedback tree pair in either monotonicity orientation.

#### One nonlinear hub versus arbitrary functional coloring

**Theorem.** Let f,g be edge colorings of Q_n. Every direction of g depends on at most one other direction bit, and every direction of f except h also depends on at most one other bit. The color of direction h in f may be an arbitrary Boolean function of all other bits. Then A0(f) intersects A1(g).

**Protected Hall lemma.** List the directed feedback cycles among the functional directions of f, excluding h, and all feedback cycles of g. Every f-cycle uses at least two direction bits distinct from h. Every g-cycle uses at least two bits; at most one g-cycle contains h, and even that cycle has another bit. For any set of m cycle conditions there are at least 2m-1 incidences with bits different from h, while each available bit participates in at most two conditions. Hence the set has at least m different neighbors. Hall's theorem assigns every cycle a different bit other than h. Fix each assigned bit opposite to the corner forbidden by its cycle, leaving the remaining bits free. All f-cycle conditions and g-cycle conditions are satisfied regardless of the h-bit.

**Proof.** Let B contain h and every direction reachable from h by the active functional dependency arrows of f, and A all other directions. An A-direction color cannot depend on a B-bit, else that direction would be reachable from h. Thus f on A is functional and independent of B; its directed feedback cycles are among those already satisfied by Hall. The root on A therefore supports a full nondecreasing geodesic, by the functional cycle classification. Choose its zero-to-one seam vertex y.

On the B-fiber over y, the directions below h form active outward rooted dependency trees, and the h-edge color is an unrestricted Boolean function of the other B-bits. The established fiberwise rooted-tree paired-selector theorem says that for the already prescribed starting bits B other than h, some h-bit gives a paired root of the fiber. Insert its nondecreasing full geodesic at the seam y of the A-geodesic. This gives an f-nondecreasing full geodesic from the chosen complete root. Hall also satisfied each forbidden all-zero cycle of functional g using a bit other than h. Consequently this same complete root admits a g-nonincreasing full geodesic by the functional cycle classification. QED.

**Corollary (cyclic single two-neighbor exception).** For two cyclic-local colorings f,g, if all g direction rules are constant or one-neighbor projections and at most one f direction depends on both cyclic neighbors, then A0(f) intersects A1(g). The statement with the roles and color orientations exchanged also holds. This is an all-dimensional induction step allowing unlimited nonlinear incoming dependencies into one f-direction; the first unresolved extension permits two independently nonfunctional direction rules.

#### Density and feedback-cycle threshold for a pair of exceptional nonlinear hubs

For a coloring f with every direction except one hub h functional, let C_f consist of the directed feedback cycles on functional directions, none involving h. Define q_f as the product over these cycles C of (1−2^(−|C|)).

**Theorem.** Both favorable-root sets satisfy |A0(f)|>= (3/4) q_f 2^n and |A1(f)|>= (3/4) q_f 2^n.

*Proof.* Let B be the hub h and all functional descendants of h; let A be the remaining directions. A-direction edge colors are independent of B bits, and their induced functional coloring has favorable-root fraction q_f by the Hall cycle classification. For each favorable A-root choose a full nondecreasing A-geodesic and its zero-to-one seam vertex y. In the B-fiber above y every nonhub direction has one active predecessor on an outward tree rooted at h, while the hub color is unrestricted. The active rooted-tree nonlinear-hub theorem guarantees at least three quarters of the B-root choices are favorable. Insert those paths at y and sum over different starting roots. Color complementation proves the A1 estimate. QED.

**Corollary (two nonlinear hubs in two colorings).** If f and g separately satisfy this single-exception hypothesis, with products q_f,q_g, then |A0(f) intersect A1(g)| >= 2^n max(0,(3/4)(q_f+q_g)−1). In particular, if each coloring has at most ONE other functional feedback cycle, both products are at least 3/4, giving at least 2^(n−3) common roots. If f has no other feedback cycle and g has at most THREE, the same argument gives at least (17/256)2^n common roots. All these are dimension-uniform closure classes allowing unrelated exceptional hubs with arbitrary nonlinear color functions.

A counterexample within the two-exception class must therefore contain a more substantial collection of independent functional feedback cycles; one per coloring is insufficient. These are structural induction thresholds, not the unrestricted two-exception result.

#### Two exceptional hubs: Hall deficiency at most one and checkerboard selector obstruction

Consider two colorings f,g each functional except for one unrestricted hub direction. Write h for f's hub and k for g's hub, and suppose h and k are different. Let C_f,C_g be all directed functional feedback cycles not containing their respective hubs. Their cycle sets are disjoint within each coloring and have size at least two.

**Lemma (two-hub protected Hall deficiency).** After deleting h and k from the available starting-bit indices, the cycle-to-bit incidence graph has maximum Hall deficiency at most one. Equivalently, there is a matching assigning distinct available bits to all but at most one of the feedback-cycle conditions.

*Proof.* For any m selected feedback cycles, at most one f-cycle contains k and at most one g-cycle contains h. No f-cycle contains h, and no g-cycle contains k. Consequently there are at least 2m−2 incidences with the bits outside {h,k}. Any available bit belongs to at most one f-cycle and one g-cycle, hence has incidence degree at most two. Therefore the m selected cycles touch at least m−1 available bits. This holds for every selected family; the deficiency form of Hall's theorem gives a matching missing at most one condition. QED.

**Lemma (only the checkerboard can defeat two selectors).** Let F,G be subsets of the four pairs (s,t) in {0,1}². Assume for every t there is an s with (s,t) in F, and for every s there is a t with (s,t) in G. If F and G are disjoint, they must each contain just two points and form complementary diagonals: either F={(0,0),(1,1)}, G={(0,1),(1,0)}, or vice versa.

*Proof.* Both sets have at least two points. If either has three points, its complement has at most one point and cannot support the other set's two independent row or column requirements. Thus both have two points and partition the square. To meet both columns F must choose one in each column. If its points share one row, its complement misses that row and cannot meet both rows for G. The only remaining possibilities are the two diagonals. QED.

**Conditional two-hub closure criterion.** Suppose the cycle-condition incidence graph has a complete matching outside {h,k}. Break every forbidden cycle corner by the selected nonhub bit and assign all other nonhub bits freely. For every fixed assignment obtained this way, the established rooted-tree hub-selector theorem implies: the favorable f-roots in the four-point (h,k) square meet both k-columns, while favorable g-roots of the opposite monotonicity meet both h-rows. Consequently, if the full cross-root intersection is empty, BOTH of these favorable-root restrictions must form complementary checkerboards. In particular, ruling out checkerboard patterns for one-exception favorable-root sets would prove the cross-root theorem in every two-hub instance with a complete protected Hall matching. The Hall-deficiency lemma shows that an arbitrary two-exception instance differs from this favorable matching situation by **at most one unresolved functional feedback-cycle condition**.

**Unproved local structural conjecture.** For a coloring with only one direction permitted a multi-bit Boolean color function and every other direction functional, its favorable-root set A0 contains no 2-dimensional square on the exceptional hub direction and any other direction in which just the two opposite corners are favorable. Color complementation gives the analogous claim for A1. Exhaustive direct geodesic reachability verified the exclusion for all 131072 Q4 colorings with hub fixed at direction zero, and all their 2-dimensional hub faces. Additional independent random checks of 30000 Q5 and 3000 Q6 colorings found no violation. This remains a conjecture in arbitrary dimension. Proving it would remove the checkerboard obstruction above; the single remaining functional-cycle condition would still need a separate repair lemma.

This identifies a two-part closure target: one missing Hall clause, and one sharply prescribed four-root checkerboard. Neither is a global geodesic counting problem.

#### Acyclic-facet monochromatic confluence and strict-majority root theorem

Let f color undirected edges of Q_n. Fix a direction h and assume **both** induced facet colorings f^0 and f^1, obtained by fixing the h-bit to 0 or 1 and retaining all other directions T, have acyclic directed dependency graphs. The two facet graphs may use different topological orders; their union need not be acyclic. The color b(y) of the h-edge is an arbitrary Boolean function of the T-bits y.

**Lemma (acyclic monochromatic confluence).** In any binary edge coloring q with acyclic directed dependencies, for any starting roots u,v there are dimension-simple partial paths from u and v meeting at a common vertex w, one all color zero and the other all color one.

*Proof.* Process the direction bits in a topological order of their dependency digraph. At each direction i the two evolving vertices already agree in every earlier bit. If their ith bits differ, their two ith-direction incident edges have the same color, because the edge rule depends only on already matched predecessor bits. If that color is zero, flip i on the u-side; otherwise flip i on the v-side. The ith bits become equal. Continue. Each direction is used on at most one side, and the endpoints coincide after all directions. QED.

Write R0^q(u) and R1^q(v) for endpoints of such partial monochromatic paths, including empty paths.

**Lemma (constraints from an unfavorable full root).** If a full root (s,y) of f has no 0*1* dimension-simple antipodal geodesic, then
\[
\boxed{b(z)=1\text{ for every }z\in R0^{f^s}(y),\quad
b(z)=0\text{ for every }z\in R1^{f^{1-s}}(\bar y).}
\]
*Proof.* For z reached from y by an all-zero partial f^s path using directions U, if b(z)=0, cross h in color zero and then traverse the remaining directions T\U in the opposite facet along a 0*1* full path. This is possible because the induced dependency graph on any face of an acyclic coloring remains acyclic. The resulting full word is monotone, contradiction. Thus b(z)=1.

For z reached from bar y by an all-one partial f^(1-s) path using directions V, first traverse the complementary directions T\V from y to z in the initial facet along a 0*1* path, possible by acyclic dependencies. If b(z)=1, cross h in color one and reverse the previous all-one path from z to bar y. The complete direction order is again 0*1*, contradiction. Thus b(z)=0. QED.

**Theorem (one fully favorable starting half-cube).** There is a bit s such that **every** root (s,y) is in A0(f).

*Proof.* Otherwise choose unfavorable roots (0,y) and (1,y'). The preceding constraints force b=1 on R0^{f^0}(y) and b=0 on R1^{f^0}(bar y'). But the first lemma supplies a point in their intersection, impossible. Hence all unfavorable roots lie on at most one side of the h-bit partition. QED.

**Theorem (strict majority, sharp paired-root count).**
\[
\boxed{|A0(f)|\ge2^{n-1}+1,\qquad |P(f)|\ge2.}
\]
If b(y)=0 at any T-vertex y, both (0,y) and (1,y) are favorable: traverse h first in color zero, then use an acyclic-facet monotone path on all T-directions. At least one of those two roots lies outside the guaranteed favorable half-cube, giving the strict-majority bound. If b is identically one, every root is favorable by traversing an acyclic-facet monotone T-path first and h last in color one. Reversing antipodal full paths gives A1(f)=antipodal(A0(f)), so P=A0 intersect A1 has size at least twice |A0| minus 2^n, hence at least two. These bounds are sharp for Q2 reciprocal coloring f0=x1,f1=x0. QED.

**Cross-coloring theorem.** Let f,g be any two binary cube-edge colorings, each having some (possibly different) direction whose two opposite facets have acyclic directed dependencies. Then
\[
\boxed{|A0(f)\cap A1(g)|\ge2.}
\]
Indeed the theorem gives both favorable-root sets cardinality at least 2^(n-1)+1, so inclusion-exclusion proves the claim. If their distinguished directions differ, the two fully favorable half-cubes already meet in a codimension-two cube of size 2^(n-2).

**NORI1 closure.** A directed dependency graph with feedback vertex set of size at most one automatically meets the facet hypothesis. The hypothesis is broader, permitting different acyclic dependency orders in the two opposite facets even when the union digraph has cycles. Every such coloring has paired roots; by the established free-bridge correspondence the associated next-dimensional antipodally odd NORI1 instance has a monochromatic full antipodal geodesic without restrictions on the bridge-edge colors.

**Research path.** The greedy confluence lemma is a new dimension-uniform structural invariant and works for arbitrary acyclic Boolean dependency rules, not only functional directions. To extend beyond one hub, a candidate is two-dimensional confluence of four initial roots after deleting a two-bit feedback set. The present proof does not assert such a stronger property. Randomized independent full-path checks with differing facet topological orders passed 500 Q4, 250 Q5, and 80 Q6 instances.

#### Universal gluing of an acyclic-facet coloring to any paired-root coloring

**Theorem (half-cube versus antipodal-pair intersection).** Let f be any binary cube-edge coloring satisfying the two-facet acyclicity hypothesis of the preceding confluence theorem in some direction h. Let g be ANY other binary cube-edge coloring with at least one antipodally paired root P(g)=A0(g) intersect A1(g). Then

A0(f) intersect P(g) is nonempty, and therefore A0(f) intersect A1(g) is nonempty.

More quantitatively |A0(f) intersect A1(g)| is at least |P(g)|/2. The orientation-swapped assertion also holds: A1(f) intersects P(g).

*Proof.* By the full-slice confluence theorem, A0(f) contains every root whose bit h equals some s. By reversing full dimension-simple geodesics, P(g) is invariant under antipodal complementation, so its roots occur in antipodal pairs. Each such pair contains one root with h-bit s, lying in A0(f). These |P(g)|/2 different roots also lie in A1(g). For the swapped orientation, apply the same reasoning to the coloring obtained from f by interchanging colors zero and one. QED.

**Corollary (unicyclic nonlinear pendant-tree closure).** Let F have a unicyclic undirected direction-interaction graph with arbitrary nonlinear rooted pendant trees. Let g0,g1 be its two induced core colorings in the established pendant-tree interface reduction. Each cyclic-local core coloring separately has paired roots by the proved nonlinear cycle paired-root theorem. Suppose EITHER g0 OR g1 has a cycle direction h such that both facets obtained by fixing its h-bit have acyclic directed dependencies on the remaining core directions. Then A0(g0) intersects A1(g1): use the full favorable half-cube of the acyclic-facet core and an antipodal pair of paired roots in the other core. The pendant-tree interface theorem lifts this common root to a paired root of F; the free-bridge correspondence supplies the associated NORI1 monochromatic antipodal geodesic. No joint constant-color site or nonempty local opposite-color overlap is required. Only ONE induced core needs the acyclic-facet property.

**Inductive significance.** A fully favorable starting half-cube is a universal transversal of every nonempty antipodally symmetric paired-root set. This converts any established one-coloring paired-root theorem into a two-coloring cross-root theorem whenever the opposite coloring has an acyclic-facet direction. It generalizes the earlier protected functional-hub gluing principle and does not require independent favorable-root density estimates.

#### Sharp fiberwise paired selector and SCC gluing from acyclic opposite facets

**Theorem (paired-root selector in every hub fiber).** Under the two-facet acyclicity hypothesis of the preceding confluence theorem for distinguished direction h,
\[
\boxed{\forall y\in Q_{n-1}\ \exists s\in\{0,1\}:\ (s,y)\in P(f).}
\tag{CF7}
\]
Consequently \(|P(f)|\ge2^{n-1}\). The bound is sharp for reciprocal Q2 dependency coloring and its Cartesian products with independent monochromatic directions.

*Proof.* Let b(y) be the color of the h-edge between (0,y) and (1,y). The preceding full-slice theorem provides an h-bit value t for which every (t,z) is favorable, for all nonhub z.

For any y, if b(y)=0, both (0,y) and (1,y) are favorable: traverse h first in color zero, then use an acyclic-facet full nondecreasing path. The antipode of one of these two roots lies in the fully favorable t-slice; hence one of them is paired.

If b(y)=1 and b(bar y)=1, both hub completions of y are likewise favorable: traverse all nonhub directions first along an acyclic-facet full nondecreasing geodesic, then traverse h last in color one. Again one has its antipode in the fully favorable t-slice and is paired.

The remaining case is b(y)=1 and b(bar y)=0. Both hub completions of bar y are favorable by traversing h first at bar y. At least one completion (t,y) is favorable by the full-slice theorem, and its antipode is one of those two favorable roots at bar y. Thus (t,y) is paired.

All cases give a paired root over the prescribed y. Distinct y give distinct roots, yielding the count. QED.

**Theorem (one-feedback-vertex SCC closure).** Let f be an arbitrary binary cube-edge coloring, with directed dependency graph D(f). Suppose that in EVERY strongly connected component B of D(f), one can delete at most one direction vertex h_B so that the induced dependency digraph on B\{h_B} is acyclic. (Singleton components qualify.) Then
\[
\boxed{P(f)\ne\varnothing,\quad
|P(f)|\ge2^{\,\#\operatorname{SCC}(D(f))}.}
\tag{CF8}
\]

*Proof.* Select a terminal strongly connected component B in the condensation DAG and write A for the remaining directions. No B-bit influences any A-direction edge color, so A-direction colors are independent of B. For each fixed outside assignment x, the induced B-fiber coloring has the same internal dependency graph or a subgraph thereof; by assumption its two facets after fixing h_B have acyclic dependencies. The strict-majority theorem above gives at least \(2^{|B|-1}+1\) favorable roots in each such fiber, for |B|>=2. Hence for any two outside assignments x,y, inclusion-exclusion gives
\[
|A_0(g_x)\cap\overline{A_0(g_y)}|
\ge 2(2^{|B|-1}+1)-2^{|B|}=2.
\]
For a singleton B both possible roots are favorable and the same overlap bound two holds. The established paired-root seam-gluing theorem therefore removes B while multiplying the lower bound for the number of paired roots by at least two. Apply induction to the remaining SCCs of the condensation DAG, starting from one paired root of the empty cube. This yields at least two roots per SCC and proves (CF8). QED.

**Structural obstruction corollary.** Any paired-root counterexample must contain a terminal strongly connected dependency component whose directed feedback vertex set has size **at least two**: deleting any single direction from that component still leaves a directed feedback cycle. This excludes feedback cores with arbitrarily many branching vertices when all directed cycles pass through one hub. The result is independent of any upper bound on internal indegrees or nonlinear Boolean complexity.

The theorem strengthens the earlier active rooted-tree feedback, fan-cycle, nonlinear star, and one-exception results, while complementing the separate computer-assisted two-hub theorem for SCCs with at most two branching-indegree vertices. It does not settle SCCs that require at least two directions to hit all internal feedback cycles.

##### Correction to the SCC obstruction statement

The preceding SCC theorem proves that any counterexample must contain **some** strongly connected dependency component whose internal feedback vertex set requires at least two directions. It does NOT prove that every counterexample has such a component among the terminal SCCs: a nonterminal hard SCC can feed a removable terminal SCC.

The stronger terminal assertion is valid only for a **least-dimensional** counterexample. Indeed, if a terminal SCC B of a least-dimensional counterexample admitted an internal feedback vertex set of size at most one, the paired-root seam-gluing equivalence would imply that deleting B leaves a smaller paired-root counterexample, contradicting minimality. Thus every terminal SCC in a least-dimensional counterexample requires deletion of at least two internal direction vertices to destroy all directed feedback cycles. This qualification supersedes the unqualified terminal-SCC sentence in the prior theorem while leaving its proof and quantitative paired-root bound unchanged.

#### Mixed-facet confluence: one confluent facet and one hereditarily favorable facet

For a binary cube-edge coloring q of Q_m, define \(R^q_0(u)\) as endpoints of dimension-simple partial paths starting at u using only edges of color zero, and \(R^q_1(v)\) analogously for color one; empty paths are permitted.

Call q **monochromatically confluent** if
\[
\boxed{R^q_0(u)\cap R^q_1(v)\ne\varnothing\quad\text{for all }u,v\in Q_m.}
\tag{MC1}
\]
Call q **hereditarily favorable** if every root of every nonempty subface of q admits a full dimension-simple \(0^*1^*\) geodesic in that subface. An acyclic dependency coloring has both properties by the published greedy confluence lemma and sink-direction seam insertion; hereditary favorability is a weaker hypothesis than acyclic dependencies.

**Theorem (mixed-facet selector).** Let F color the edges of Q_(m+1), with distinguished hub bit h. Write q^0,q^1 for its two opposite m-dimensional facet colorings and b(y) for its arbitrary h-edge color at nonhub vertex y. Suppose q^0 is monochromatically confluent and q^1 is hereditarily favorable. No dependency relationship between q^0 and q^1 is required. Then
\[
\boxed{\exists s\in\{0,1\}:\{(s,y):y\in Q_m\}\subseteq A_0(F),}
\tag{MC2}
\]
\[
\boxed{|A_0(F)|\ge2^m+1,\qquad
\forall y\in Q_m\ \exists s:(s,y)\in P(F).}
\tag{MC3}
\]
Consequently \(|P(F)|\ge2^m\), sharply.

*Proof.* Confluence of q^0 implies every root u of q^0 admits a full \(0^*1^*\) geodesic: apply (MC1) to \(u,\bar u\), join the all-zero path from u to a meeting point with the reverse all-one path from \(\bar u\), which use complementary direction sets. Hereditary favorability of q^1 supplies full monotone paths from every root in all its faces.

Suppose (0,y) is unfavorable in F. For each \(z\in R^{q^0}_0(y)\), if b(z)=0, traverse the zero path from y to z, cross h in color zero, then traverse all remaining dimensions in the q^1 subface starting at z along a full monotone path. This contradicts unfavorability. Thus
\[
b=1\text{ throughout }R^{q^0}_0(y).
\tag{MC4}
\]

Suppose (1,y') is unfavorable. For every \(z\in R^{q^0}_1(\bar y')\), let V be the directions of a monochromatic-one q^0 path from \(\bar y'\) to z. Starting at y', traverse the complementary directions T\V inside the appropriate q^1 subface along a full monotone geodesic, ending at z. If b(z)=1, cross h in color one and then reverse the q^0 one-path from z to \(\bar y'\). This is a complete monotone geodesic from (1,y'), a contradiction. Therefore
\[
b=0\text{ throughout }R^{q^0}_1(\bar y').
\tag{MC5}
\]

Confluence (MC1) supplies a meeting point of the two reachable sets in (MC4),(MC5), forcing b to be both one and zero. Thus unfavorable roots cannot occur in both hub-bit slices. This proves (MC2).

If b(y)=0 for some y, both hub-bit completions of y are favorable by crossing h first in color zero and following a monotone full path in the opposite facet. If b is identically one, all roots are favorable by following a monotone full path in the initial facet and crossing h last in color one. Hence (MC2) always extends to at least \(2^m+1\) favorable roots.

For each nonhub y, if b(y)=0, both completions at y are favorable, so one has its antipode in the fully favorable hub slice (MC2) and is paired. If b(y)=1=b(\bar y), both completions at y are favorable by traversing the initial facet first and crossing h last at \(\bar y\); again one is paired. Otherwise b(y)=1 and b(\bar y)=0. Both completions at \(\bar y\) are favorable by crossing h first, and (MC2) supplies at least one favorable completion at y whose antipode is among them. Therefore one completion at y is paired in every case. Distinct nonhub assignments y give distinct paired roots, establishing (MC3). \(\square\)

**New feedback-two application.** On three directions 0,1,2 define
\[
q_0(x)=x_1x_2,\qquad q_1(x)=x_0(1-x_2),\qquad q_2(x)=0.
\tag{MC6}
\]
Its global dependency digraph contains both 0->1 and 1->0. Nevertheless q is hereditarily favorable: each proper subface has an acyclic dependency digraph (the two reciprocal arrows cannot be simultaneously active after fixing x_2), and every full root even admits an all-zero geodesic. From x_2=1, traverse direction 2 first in color zero; with x_2=0, if x_0=1 traverse 0 then 1, otherwise traverse 1 then 0; all traversed edges have color zero. Finish with direction 2 when starting x_2=0.

Construct a Q4 coloring F with hub h=3: the h=0 facet is identically zero in directions 0,1,2; the h=1 facet is q of (MC6); and the h-direction color is \(b(x)=x_0+x_1\) modulo two. The full dependency digraph has directed cycles after deletion of **any single** direction, but deletion of {0,1} leaves an acyclic digraph; hence its directed feedback vertex set has size two. Nevertheless the mixed-facet theorem gives \(|P(F)|\ge8\). The result thus goes beyond the previously proved one-feedback-vertex theorem, allowing a nonlinear two-feedback core on one side of the hub.

**Structural scope.** The mixed-facet theorem isolates the real ingredients of the acyclic-facet proof: monochromatic confluence is needed on only one facet, while the other facet needs monotone geodesics in every restricted face. Confluence is not generally preserved when adding a hub, so this is a sufficient induction rule rather than a universal closure of NORI1.

#### Hereditary favorability under constant-control grafting, with arbitrarily dense global feedback

Call a cube-edge coloring **hereditarily favorable** if every root in every subface admits a full \(0^*1^*\) geodesic within that face (including zero-dimensional faces).

**Theorem (constant-control grafting).** Let q^0,q^1 be any two hereditarily favorable colorings of Q_m, possibly with entirely unrelated dependency digraphs. Construct a coloring q on Q_(m+1) whose restrictions to the two facets of a new direction z are respectively q^0,q^1, and whose z-direction edges all have the same constant color c in {0,1}. Then q is hereditarily favorable.

*Proof.* Take an arbitrary subface S of Q_(m+1) and a starting root in it. If z is fixed throughout S, the induced coloring belongs to a subface of q^0 or q^1 and is favorable by hypothesis. If z is free, consider its two facet subfaces S^0,S^1; their colorings are hereditarily favorable. When c=0, traverse z first in color zero, entering the opposite z-facet, and then take a full \(0^*1^*\) geodesic there. When c=1, first traverse all other free directions along a \(0^*1^*\) path in the initial z-facet, then traverse z last in color one. Both constructions use every free direction once and yield the desired monotone word. Since S and its starting root were arbitrary, hereditary favorability follows. \(\square\)

**Corollary (hierarchical conditional-facet closure).** Begin with any collection of hereditarily favorable base colorings, including every coloring with an acyclic dependency graph. Repeatedly adjoin a new constant-color control direction, choosing *independently* arbitrary previously constructed colorings on its two opposite facets. Every coloring produced in this recursive class remains hereditarily favorable. Finally adjoin one more hub direction h with **arbitrary** edge-color Boolean function of all other bits, placing an acyclic monochromatically confluent coloring on its h=0 facet and any recursively produced hereditary coloring on its h=1 facet. By the mixed-facet confluence theorem, the resulting cube has
\[
\boxed{|A_0|\ge2^{n-1}+1,\qquad
|P|\ge2^{n-1}}
\]
and has a paired root over every assignment of its nonhub starting bits.

**Example (unbounded feedback vertex number).** Fix m>=2 ordinary directions 1,...,m and a control direction z. Let its z-edge color be constant zero, and define ordinary direction-i colors by
\[
q_i(x,z=0)=\bigoplus_{j<i}x_j,\qquad
q_i(x,z=1)=\bigoplus_{j>i}x_j.
\tag{HG1}
\]
For each fixed z, the direction-dependency graph on the ordinary directions is a DAG: the natural total order when z=0, and its reversal when z=1. Hence both facets and all their subfaces are hereditarily favorable. The constant-control theorem shows that q is hereditarily favorable.

But in the *global* dependency graph, for every distinct ordinary directions i,j, **both** arrows i->j and j->i occur: the first is active in one control facet and the reverse in the other. Thus the m ordinary directions induce a complete bidirected graph. At least m−1 direction vertices must be deleted to make the global dependency digraph acyclic, so the directed feedback vertex number grows without bound with m.

Add one final hub direction h whose h=0 facet is an arbitrary acyclic edge coloring of Q_(m+1), whose h=1 facet is q, and whose h-edge color is an **arbitrary nonlinear Boolean function** of the m+1 nonhub bits. The mixed-facet theorem gives a paired-root selector along h and at least \(2^{m+1}\) paired roots. The resulting global dependency digraph still contains the complete bidirected graph on the ordinary directions and can include additional hub feedback cycles.

**Proof-closure lesson.** The global directed dependency graph can be highly cyclic even when the coloring is built from a sequence of completely tractable conditional facets. Feedback vertex number is therefore not a sufficient measure of local proof complexity. A structurally natural induction should track monochromatic confluence and hereditary monotone-path solvability **after fixing control bits**, allowing different dependency orders in different facets. The mixed-facet theorem supplies a nonconstant final-hub operation above this hereditary class; extending this operation to multiple mutually interacting arbitrary hub layers remains open.

#### Canonical seam permutations for acyclic dependency colorings

Let q color cube edges in dimension m, with an acyclic directed dependency graph. Let \(c_q(w)=(q_i(w))_{i=1}^m\) denote the vector of the m incident direction-edge colors at a cube vertex w.

**Theorem (triangular seam bijection).** The map
\[
\boxed{T_q(w)=w\oplus\mathbf1\oplus c_q(w)}
\tag{S1}
\]
is a bijection of the m-cube. For every root y, the unique solution \(w=T_q^{-1}(y)\) is the transition seam of a full dimension-simple antipodal geodesic from y with color word \(0^*1^*\). Its zero phase traverses all directions with q_i(w)=0 in a dependency-topological order; its one phase traverses all directions with q_i(w)=1 in reverse dependency-topological order. The seam w is independent of the chosen topological order.

*Proof.* Fix a topological order i_1,...,i_m of the dependency DAG. Each q_(i_j)(w) depends only on earlier listed bits and not on w_(i_j). Thus (S1) is triangular with a bijective one-bit diagonal map at each stage. Solve \(w_{i_j}=y_{i_j}\oplus1\oplus q_{i_j}(w)\) successively; every starting root y determines precisely one w.

Put Z={i:q_i(w)=0} and O={i:q_i(w)=1}. Equation (S1) says y differs from w on Z, and w differs from the antipode of y on O. Starting at y, traverse Z in topological order. Each predecessor bit of a traversed direction i already equals its value at w, whether previously changed in Z or unchanged in O. Hence every edge has color q_i(w)=0. From w traverse O in reverse topological order. Each predecessor bit of direction i remains at w when i is traversed, so every remaining edge has color q_i(w)=1. All directions are used once. \(\square\)

**Corollary (seam distribution).** The canonical monotone paths from all \(2^m\) roots have all \(2^m\) different transition seams. For any prescribed set U of seam vertices, precisely |U| starting roots have a canonical seam in U.

**Corollary (two acyclic colorings).** Let q,r be any two acyclic-dependency colorings on Q_m, allowing unrelated topological orders. Their canonical monotone paths from the *same root* can share a seam vertex w if and only if
\[
\boxed{c_q(w)=c_r(w)\quad\text{in every direction}.}
\tag{S2}
\]
Indeed the common-root condition T_q(w)=T_r(w) reduces immediately to (S2). Such alignment is not automatic, even when both colorings have every root favorable, because their incident direction-color vectors may disagree at every vertex.

**Theorem (canonical two-source gate).** For any two starts u,v, their greedy acyclic monochromatic confluence construction has one canonical meeting point w in their smallest common face. With directions processed in a dependency-topological order, the meeting bits satisfy
\[
\boxed{
w_i=u_i=v_i\quad\text{if }u_i=v_i;\qquad
w_i=u_i\oplus1\oplus q_i(w)\quad\text{if }u_i\ne v_i.
}
\tag{S3}
\]
These equations are triangular and define one w independent of the topological order. The path from u to w is all zero, the path from v to w is all one, and their disjoint direction sets partition the bit positions where u and v differ.

**Relevance to two-feedback restoration.** A cube coloring that becomes acyclic after fixing two exceptional direction bits has four canonical seam permutations T_00,T_01,T_10,T_11. The alignment criterion (S2) converts common canonical-seam questions into local equalities of direction-color vectors. Requiring all four seam maps to agree is not a valid general induction invariant, since even two acyclic facet colorings may lack any shared canonical seam. The new maps give an algebraic language for controlled exchanges of the two exceptional directions; unrestricted two-feedback closure remains open.

#### Bipolar square restoration for two-feedback-direction cube colorings

Let F be a binary edge coloring of Q_(m+2), with two distinguished hub directions h,k and m other directions T. For each fixed assignment (s,t) of the hub bits, suppose the induced T-direction facet coloring has an **acyclic directed dependency graph**. The facet dependency orders may depend arbitrarily on (s,t). Hub-edge colors can depend on every ordinary bit and on the other hub bit.

Fix an ordinary starting assignment y in Q_T. The four hub edges with ordinary bits y form a colored square. Write their colors as
\[
F_h(s,t,y)=a+t,\qquad F_k(s,t,y)=b+s
\tag{BS1}
\]
for a,b in F2, if both hub directions depend nontrivially on the *other* hub bit at this y.

**Lemma (two bipolar roots of a reciprocal hub square).** Under (BS1), the two opposite hub corners
\[
\boxed{(s,t)=(1+b,a)\quad\text{and}\quad(s,t)=(b,1+a)}
\tag{BS2}
\]
each admit both a full all-zero hub-square geodesic and a full all-one hub-square geodesic, using the two different hub orders.

*Proof.* From corner (1+b,a), traverse h then k. The h-edge has color a+a=0; after flipping h, the k-edge has color b+b=0. For the opposite hub order k then h, the k-edge has color b+(1+b)=1 and the subsequent h-edge has color a+(1+a)=1. Interchanging starting corner and hub orders gives the same property for the other opposite corner. \(\square\)

**Theorem (local reciprocal-square paired-root restoration).** If (BS1) holds for even **one** ordinary assignment y, then F has a paired root. In fact both complete starting roots whose ordinary bits equal y and whose hub bits are the corners (BS2) belong to P(F). If m>=1, antipodal symmetry gives at least four distinct paired roots.

*Proof.* Choose either hub corner sigma of (BS2). For the full F-geodesic of word 0*1*, first traverse both hub directions along the all-zero hub-square path at ordinary vertex y. This reaches the opposite hub corner bar sigma, without changing any ordinary bit. Inside the fixed-bar-sigma T-facet, start at ordinary y and traverse a complete 0*1* antipodal geodesic. Such a path exists from EVERY T-root since its dependency graph is acyclic. Concatenating the two paths gives a full dimension-simple nondecreasing geodesic starting at (sigma,y).

For the opposite word 1*0* from the SAME root (sigma,y), traverse the two hub directions first along the all-one square path (in the other order), then traverse a complete 1*0* geodesic in that same opposite T-facet from ordinary y. Color complementation of the acyclic-facet theorem gives this path. The resulting full path uses every original direction once, proving (sigma,y) paired. Do the same for the other hub corner. Antipodal closure of P(F) supplies the additional roots stated. \(\square\)

**Corollary (necessary obstruction for a two-vertex feedback set).** Suppose deleting two designated directions h,k from the global directed dependency graph of F leaves an acyclic digraph. Then every fixed-hub T-facet is acyclic, so the theorem applies. If F is a paired-root counterexample, for **every** ordinary vertex y the restricted colored hub square must fail reciprocal dependence. Equivalently at each y at least one of the two restricted hub-direction color functions is constant with respect to the other hub bit. In particular the two directed hub-to-hub dependencies can never both be simultaneously active on the same ordinary square.

This excludes a broad nonlinear feedback configuration by a two-edge-order exchange, without any enumeration of high-dimensional paths. It is a sufficient paired-root restoration lemma, not a proof for all colorings with a two-vertex directed feedback set.

#### Two-hub sandwich restoration and bounded square interface

Let F be an edge coloring of Q_(m+2), with two special hub directions 0,1 and m ordinary directions T. Assume each of the four T-facet colorings, obtained after fixing both hub bits, has acyclic directed dependencies. Hub edge colors can depend arbitrarily on all ordinary bits and the other hub bit.

For a fixed ordinary starting root y, denote by a the hub-square coloring at y and by b the hub-square coloring at its antipode bar y. For hub starting state sigma and a hub order (i,j), write tau=sigma+e_i. For epsilon=0 or 1, define three possible local certificates:

(Early) a_i(sigma)=epsilon and a_j(tau)=epsilon.
(Late) b_i(sigma)=1-epsilon and b_j(tau)=1-epsilon.
(Split) a_i(sigma)=epsilon and b_j(tau)=1-epsilon.

**Theorem (sandwich lifting).** If at least one of these conditions holds for some hub order (i,j), then (sigma,y) supports a full dimension-simple antipodal geodesic with word epsilon*(1-epsilon)*. If conditions hold for epsilon=0 and epsilon=1 from the same root (possibly using different orders), the root is paired.

*Proof.* In the early case traverse the two hub edges first, in color epsilon, then traverse all m ordinary directions in the opposite hub facet along a monotone full geodesic. In the late case first traverse all ordinary directions in the initial hub facet, arriving at bar y, and then both hub edges in color 1-epsilon. In the split case traverse one hub edge at y in color epsilon, then all ordinary directions in the intermediate hub facet along a monotone full geodesic from y to bar y, and then the final hub edge at bar y in color 1-epsilon. Each fixed-hub T facet admits the required complete monotone path from every starting root by the acyclic dependency theorem. Each construction traverses every original direction once and has the required monotone word. QED.

**Uniform finite classification.** A hub square coloring is encoded by a 4-bit integer a, in which bits 0 and 1 give the direction-0 color when hub bit 1 is zero and one, while bits 2 and 3 give the direction-1 color when hub bit 0 is zero and one. There are 16 choices for a and 16 for b. Direct evaluation of the three certificates across both hub orders, both target orientations, and all four starting hub corners gives:
- 196 of the 256 ordered pairs (a,b) admit a common hub corner with both polarity certificates and hence a paired root for **every** acyclic four-fiber extension.
- 60 ordered pairs do not admit a paired root through these restricted sandwich constructions. This does NOT assert that the full coloring lacks paired roots.
- If a is any of {5,6,9,10}, the two hub directions are mutually active on the square at y, and both polarity certificates hold for two opposite starting hub corners regardless of b. This is the previously proved bipolar-square restoration theorem.
- Only the ordered pairs (3,12) and (12,3) fail to provide an orientation-zero sandwich certificate at every hub root above both y and bar y.

The finite check uses the following formulas, evaluated for each a,b in {0,...,15}, sigma in {0,...,3}, epsilon in {0,1}, and order (i,j) in {(0,1),(1,0)}. Define edge(c,0,sigma)=bit_(sigma_1)(c), edge(c,1,sigma)=bit_(2+sigma_0)(c), tau=sigma XOR (1<<i), and evaluate Early, Late, Split with the above formulas. A pair passes the paired test if some sigma passes one test for epsilon zero and one for epsilon one. Reversing full geodesics gives paired(b,a) = antipodal(paired(a,b)), so the paired test is symmetric upon exchanging a and b. No SAT or unbounded search is involved: the classification has 256 inputs **after** the dimension-uniform sandwich lifting theorem.

**Proof-closure target.** The hard cases are not failures of the original cube theorem; they require paths that interleave ordinary dimensions with the hub crossings more flexibly. The two pairs (3,12),(12,3) isolate a particularly rigid special form: at ordinary y one hub direction is uniformly zero and the other uniformly one, whereas at bar y these two values reverse. A full two-feedback-direction restoration theorem must be able to move an ordinary direction through the hub crossings when this polarity changes.

#### Hereditary favorability implies monochromatic confluence

**Lemma (interval confluence).** Let q be a hereditarily favorable coloring of Q_m, meaning that every starting vertex of every subface has a full \(0^*1^*\) geodesic inside that subface. Then q is monochromatically confluent: for any two vertices u,v, a partial dimension-simple all-zero path from u and a partial dimension-simple all-one path from v meet at a common vertex inside their smallest containing subface.

*Proof.* Let I be the set of directions in which u and v differ, and let C be the |I|-dimensional face obtained by fixing all other bits. Inside C, the two vertices u and v are antipodal. By hereditary favorability there is a complete nondecreasing q-geodesic in C from u to v. Split it at its zero-to-one color transition seam w. Its first part is an all-zero path u to w, and reversing its second part gives an all-one path v to w. The two paths are dimension-simple, use disjoint direction sets partitioning I, and lie entirely in C. QED.

**Corollary (two arbitrary hereditary facets).** Let F color cube edges in Q_(m+1). Suppose the two opposite m-dimensional facet colorings at a chosen direction h are BOTH hereditarily favorable, with no requirement that their dependency digraphs share any structure. The h-edge colors may be arbitrary. Then F has one entire favorable hub-bit half-cube and a paired-root selector over every assignment of the other m bits:
\[
\boxed{|A_0(F)|\ge2^m+1,\qquad |P(F)|\ge2^m.}
\]
Indeed the lemma supplies monochromatic confluence for either facet, while both supply hereditary favorability. Apply the mixed-facet restoration theorem. The class is stable under repeated constant-colored control grafts, but an arbitrary-color final hub generally yields only the paired-selector conclusion, not hereditary favorability; a repeated arbitrary-hub step needs an additional restoration principle.

**Closure relevance.** The abstract property driving one-hub restoration is interval monochromatic confluence, rather than directed graph acyclicity. The hereditary class is much larger than the DAG class: opposite conditional acyclic orders can generate complete bidirected dependency graphs of arbitrary order while remaining hereditarily favorable. The next two-feedback-direction problem concerns the weaker *paired-selector* outputs of one hub restoration, which need not themselves be hereditarily favorable.

#### Seven symmetry orbits of the residual two-hub sandwich interface

In the preceding dimension-uniform two-hub sandwich restoration theorem, encode a hub-square coloring by four bits: the two direction-0 edge colors indexed by the other hub bit (positions 0,1), followed by the two direction-1 colors indexed by the first hub bit (positions 2,3). Let \(R(a,b)\) be the subset of the four starting hub corners at ordinary root y for which the three sandwich alternatives certify BOTH monotone polarities, using a at y and b at its antipode.

The preceding bounded 16-by-16 interface census found \(R(a,b)\ne\varnothing\) for 196 square pairs and \(R(a,b)=\varnothing\) for the remaining 60. The latter are **failures only of the restricted sandwich witness**, not refutations of paired-root existence.

**Theorem (seven residual orbit types).** Under the operations
(a) independently translate either hub bit in the labels of both square colorings;
(b) interchange the two hub directions in both colorings;
(c) complement all eight hub-edge color bits in both squares;
(d) interchange the two squares a and b, corresponding to reversing antipodal full witnesses;
the sixty noncertified pairs split into precisely **seven symmetry orbits**:
\[
\boxed{
\begin{array}{c|rrrrrrr}
\text{representative }(a,b)&(0,3)&(0,7)&(0,15)&(1,12)&(1,13)&(1,14)&(3,12)\\
\text{orbit size}&8&16&2&16&8&8&2
\end{array}}
\tag{SO1}
\]
The sizes sum to 60.

*Proof.* Each listed operation preserves paired-root existence under the sandwich alternatives. Bit translations merely relabel the starting hub corner and its two possible orders. Hub interchange relabels the two orders. Complementing both edge colors exchanges the two monotonicity polarities. Exchanging a and b reverses the complete full geodesics, replacing a root with its antipode and swapping the two polarities, so \(R(b,a)=\overline{R(a,b)}\). Thus the collection of failing pairs is stable under all four operations.

The orbit classification is a bounded sixteen-square computation. To reproduce it, evaluate for every pair a,b in 0,...,15 and every starting hub corner sigma and the two hub orders the three Early/Late/Split tests of the previous theorem for epsilon=0 and epsilon=1. Retain the sixty pairs for which no corner passes both tests. Generate each symmetry orbit by repeatedly applying: the four hub translations, the swap of the two two-bit square-code halves, simultaneous code complements (a,b)->(15-a,15-b), and (a,b)->(b,a). The seven representatives above generate disjoint sets of the displayed sizes, whose union has sixty members. These finite assertions follow by direct examination of at most 256 ordered square pairs, **after** the dimension-uniform mathematical lifting reduction. No unbounded cube enumeration or optimization is involved. \(\square\)

**Interpretation.** One of the seven types, represented by (3,12), is the antipodally odd opposite-hub-polarity obstruction: at y one hub direction is uniformly one and the other uniformly zero, while at bar y their colors reverse. The other six types include fully monochromatic hub squares opposite asymmetric hub squares. The classification replaces 60 local configurations by seven structural boundary patterns, but does not establish that every such pattern can be restored in the full cube.

**Next closure direction.** A full two-feedback-direction theorem could arise from a single dimension-simple exchange rule permitting an ordinary direction to be traversed before one hub crossing and another ordinary direction after it. Such a rule needs to repair the seven residual types, while the sandwich theorem already handles the other 196 interface configurations. The one-feedback confluence permutations offer a controlled way to choose those ordinary directions without laddering through successive cube dimensions.

#### Antipodally matching hub squares force paired roots

Let F be a binary cube-edge coloring with two hubs h,k such that all four induced T-direction facet colorings obtained after fixing both hub bits have acyclic directed dependency graphs. For each ordinary starting vertex y let H_y denote the coloring of the four hub-square edges over y.

**Theorem (opposite-square equality).** If for some ordinary root y the four hub-edge colors at y equal their corresponding colors at bar y, then F has at least two paired roots.

*Proof.* Every binary edge coloring of Q2 has at least two paired hub starting corners. Choose any such corner sigma in H_y. It supports both a full 0*1* hub geodesic and a full 1*0* hub geodesic. Lift either path as follows. If its two hub edges are monochromatic in the initial phase (zero for the nondecreasing order, one for the nonincreasing order), traverse the two hubs first at ordinary y, then traverse all T directions in the final hub facet. If both hub edges have the terminal phase color, traverse all T directions first in the initial hub facet, arriving at bar y, then traverse the two hub edges there. If its hub colors are initial-phase then terminal-phase, traverse the first hub at y, all T directions in the intermediate hub facet, then the second hub at bar y. The required hub-edge colors agree at y and bar y by hypothesis, and the needed full T geodesic of either orientation exists from every root in every fixed-hub facet because its dependency digraph is acyclic. Both hub geodesics therefore lift to complete dimension-simple monotone geodesics from the SAME full starting root (sigma,y). The other paired hub corner lifts in the same way. QED.

**Corollary (necessary two-feedback obstruction).** If deleting two designated hubs h,k from the global directed dependency graph makes its remaining digraph acyclic, but F has no paired root, then at every ordinary vertex y both restrictions hold:
(i) the two hub directions are not mutually dependent in the four-edge hub square over y, by the previous bipolar square theorem;
(ii) the square-coloring vector H_y is different from H_(bar y), by the theorem above.
These local constraints are necessary but are not asserted sufficient for failure. They sharpen the next two-feedback closure target without restricting the nonlinear Boolean rules on ordinary directions or requiring their four facet dependency orders to agree.


##### Cross-favorability under the combined directed influence decomposition

Let \(f,g\) be arbitrary binary colorings of the undirected edges of \(Q_d\), and let \(D=D(f)\cup D(g)\) record each dependence arc \(j\to i\) of either coloring. List the strongly connected components in topological order \(C_1,\ldots,C_t\), and put \(R_\nu=\bigcup_{\mu<\nu}C_\mu\). For \(y\in\{0,1\}^{R_\nu}\), let \(f^{(\nu)}_y,g^{(\nu)}_y\) be the induced colorings on \(C_\nu\), with the bits in \(R_\nu\) fixed to \(y\). Later bits do not influence these colorings. Set
\[
\rho_\nu=
\min_{y,z\in\{0,1\}^{R_\nu}}
\bigl|A_0(f^{(\nu)}_y)\cap A_1(g^{(\nu)}_z)\bigr|.
\]

**Theorem (two-coloring directed-component product).** For every pair \(f,g\),
\[
\boxed{\bigl|A_0(f)\cap A_1(g)\bigr|
\ge \prod_{\nu=1}^{t}\rho_\nu
\ge \prod_{\nu=1}^{t}\kappa_{|C_\nu|},}
\]
where \(\kappa_m=\min_{u,v:E(Q_m)\to\{0,1\}}
|A_0(u)\cap A_1(v)|\). Empty products are one.

*Proof.* Induct over the ordered components. Suppose \(x\) supports an \(f\)-geodesic with word \(0^*1^*\) and a \(g\)-geodesic with word \(1^*0^*\) in the earlier directions. Let \(y\) be the first path's vertex after its zero prefix, and \(z\) the second path's vertex after its one prefix; these states may differ. Choose
\[
w\in A_0(f^{(\nu)}_y)\cap A_1(g^{(\nu)}_z).
\]
Insert a full \(f^{(\nu)}_y\)-geodesic from \(w\) at the first seam and a full \(g^{(\nu)}_z\)-geodesic from \(w\) at the second seam. Both resulting words retain their monotonicity. Every earlier direction's edge colors are independent of the bits in \(C_\nu\); otherwise \(D\) would contain an arc from \(C_\nu\) into an earlier component, contradicting the topological order. Thus the old steps retain their colors, and both enlarged paths start at the same root \((x,w)\) and traverse every processed direction once. For each earlier common root there are at least \(\rho_\nu\) distinct choices of \(w\). Multiplication gives the first inequality, and the definition of \(\kappa_m\) gives the second. \(\square\)

**Corollary (jointly acyclic influences).** If \(D(f)\cup D(g)\) is acyclic, then
\[
\boxed{A_0(f)=A_1(g)=V(Q_d).}
\]
Indeed every component is a singleton, whose two induced colorings are constant; thus \(\rho_\nu=\kappa_1=2\), and the lower bound is \(2^d\).

**Corollary (joint feedback blocks).** If every strongly connected component of \(D(f)\cup D(g)\) has size at most three, then
\[
\boxed{|A_0(f)\cap A_1(g)|\ge2^{t_1+t_2+2t_3},}
\]
where \(t_j\) is the number of components of size \(j\). This follows analytically from \(\kappa_1=\kappa_2=2\) and \(\kappa_3=4\). The separately certified four-cube result \(\kappa_4=2\) also gives a factor \(2^{t_4}\) when four-direction components occur.

More generally, the theorem applies if every conditional pair \((f^{(\nu)}_y,g^{(\nu)}_z)\) has intersecting opposite-orientation favorable-root sets. The interaction-path, nonlinear-star, and crossed-square-factorization theorems supply arbitrarily large eligible components. Any counterexample to unrestricted two-coloring cross-favorability therefore has a strongly connected component of at least four directions in its **combined** influence digraph, or at least five subject to the four-cube certificate.

This extension of the one-coloring component theorem allows the two colorings and their seam states to differ. It leaves open the case of an unrestricted large feedback component, including the unresolved cyclic-neighbor cross-favorability conjecture.


##### Abundant paired roots need not share a phase seam

For a full \(0^*1^*\) direction-simple geodesic define its *rising seam* to be the vertex reached after its zero-colored prefix. For a full \(1^*0^*\) geodesic define its *falling seam* to be the vertex reached after its one-colored prefix. The seams are well defined also for monochromatic words: an all-zero rising path has seam at its endpoint, while an all-zero falling path has seam at its starting root.

**Theorem (complete influence with no common-seam root).** For every \(n\ge3\), there is an arbitrary undirected binary edge coloring \(h\) of \(Q_n\) such that
\[
\boxed{D(h)\text{ is the complete bidirected influence graph},\qquad
P(h)=Q_n\setminus\{0^n,1^n\},}
\tag{CS1}
\]
yet for **no** starting root do a rising full geodesic and a falling full geodesic have the same seam vertex.

*Proof.* Give color one to precisely the \(n\) cube edges incident with \(0^n\), and color zero to every other edge. Equivalently, the direction-\(i\) edge-color function is
\[
h_i(x)=\prod_{j\ne i}(1+x_j)\pmod2.
\tag{CS2}
\]
For each distinct \(i,j\), flipping bit \(j\) changes \(h_i\) when all other arguments vanish, so every influence arc \(j\to i\) occurs.

From \(0^n\), the first edge of every complete geodesic is colored one and all subsequent edges zero. Thus the rising orientation is impossible there. The reversed statement holds from \(1^n\), where every complete geodesic ends with a color-one edge, preventing the falling orientation.

Take now a root \(x\) with Hamming weight \(1\le k\le n-1\). Traverse first every bit that is initially zero, then every bit initially one. The resulting full geodesic never visits \(0^n\), so every edge has color zero. It supports both monotone orientations, proving the paired-root assertion of (CS1).

Every full geodesic from such a root either avoids \(0^n\), and has word \(0^n\), or visits \(0^n\) after the \(k\) initially-one bits have been flipped and before any initially-zero bit is flipped. In the second case its edge word is
\[
\boxed{0^{k-1}11\,0^{n-k-1}.}
\tag{CS3}
\]
(The two color-one edges enter and leave the origin.) If \(1<k<n-1\), word (CS3) has two switches, so every favorable full geodesic is all zero. Its rising seam is \(\bar x\), while its falling seam is \(x\), distinct vertices.

If \(k=1\), the rising full geodesics must again have all-zero words, so their seam is \(\bar x\), of Hamming weight \(n-1\). Every falling geodesic has seam of Hamming weight one: either its root \(x\) in the all-zero case, or the vertex reached immediately after the two one-colored steps in (CS3). These seam sets are disjoint for \(n\ge3\).

If \(k=n-1\), the argument reverses. Every falling geodesic is all zero and has seam \(x\), of weight \(n-1\), while every rising seam has Hamming weight one, whether the word is all zero or of the form (CS3). The seam sets again are disjoint. The endpoint roots \(0^n,1^n\) have only one monotone orientation. Hence no root admits a shared rising/falling seam. \(\square\)

**Implication for source-block gluing.** A proposed induction deleting arbitrary source strongly connected components cannot rely on choosing opposite monotone paths with a common seam. This construction has maximum possible off-diagonal influence and paired-root density \(1-2^{1-n}\to1\), but its two phase-seam sets remain disjoint at every root. Therefore a source-block induction must exploit two distinct seam slices through cross-favorability, or use an insertion mechanism such as periodic-block restoration that does not require seam coincidence.



##### Strong connectivity is necessary for a cyclic-local cross-root obstruction

**Theorem (cyclic feedback irreducibility).** Let \(n\ge3\), and let \(f,g\) be arbitrary binary colorings of the undirected edges of \(Q_n\) whose local edge-color functions depend only on the two cyclically neighboring direction bits. If the **union directed influence graph**
\[
D=D(f)\cup D(g)
\]
is not strongly connected, then
\[
\boxed{A_0(f)\cap A_1(g)\ne\varnothing.}\tag{CF1}
\]
Consequently, a counterexample to the shared-site cyclic cross-favorability conjecture can occur only when the combined directed influence graph is strongly connected on the entire cycle. The assertion places no restriction on the local truth tables, and applies to two unrelated cyclic-local colorings even without a common site.

*Proof.* Let \(C_1,\ldots,C_t\) be the strongly connected components of \(D\). Since \(D\) is not strongly connected, \(t\ge2\), and every \(C_\nu\) is a proper subset of the \(n\) direction indices. The union **undirected** interaction graph of \(f,g\) is contained in the simple cycle on those indices. Therefore the interaction graph induced on \(C_\nu\) is a disjoint union of paths and isolated vertices. Fix arbitrary assignments of the bits in all earlier components. Because the SCCs are topologically ordered, neither induced coloring on \(C_\nu\) depends on bits in later components. The two resulting conditional colorings have a combined interaction graph contained in a path forest. The established all-dimensional path cross-favorability theorem gives
\[
A_0(f^{(\nu)}_y)\cap A_1(g^{(\nu)}_z)\ne\varnothing
\quad\text{for every earlier-state pair }(y,z).
\]
Thus \(\rho_\nu\ge1\) for every component in the combined directed-component product theorem. Their product is positive, proving (CF1). \(\square\)

**Degree-two extension.** Suppose the union undirected interaction graph of \(f,g\) has maximum degree at most two. Each connected component is a path, a cycle, or a singleton. A path component is settled by universal path cross-favorability. A cyclic component is settled by the theorem above unless its entire vertex set is one strongly connected component of the union directed influence graph. Cartesian factorization across independent interaction components then shows that any cross-root failure requires at least one cyclic interaction component that is strongly connected under the union directed influence graph. This statement makes no claim about branched trees or general pseudoforests.

The theorem isolates **irreducible global feedback**, rather than deficient overlap sites, as a necessary obstruction for arbitrary cyclic pairs. It combines two distinct all-dimensional tools: componentwise phase-seam insertion and path-local cross-favorability.



**Corollary (directed Hamilton feedback forced by a shared projection site).** In the preceding cyclic-local setting, suppose that at some site \(j\) the two local functions agree and are the projection \(f_j=g_j=x_{j-1}\), with cyclic indices. If
\[
A_0(f)\cap A_1(g)=\varnothing,
\]
then the combined directed influence graph contains the consistently oriented directed Hamilton cycle
\[
\boxed{j\longrightarrow j+1\longrightarrow j+2
\longrightarrow\cdots\longrightarrow j-1\longrightarrow j.}
\tag{CF2}
\]

*Proof.* The shared projection gives the arc \(j-1\to j\), and ensures the reverse-neighbor arc \(j+1\to j\) is absent. By the previous theorem, a hypothetical cross-root failure forces the union influence graph to be strongly connected. Moreover the union undirected interaction graph must use the edge \(j,j+1\): if that edge were absent, the entire interaction graph would lie in a path, where cross-favorability has already been proved. As \(j+1\to j\) is absent, the arc \(j\to j+1\) must therefore occur.

Strong connectivity supplies a directed simple path from \(j+1\) to \(j\). Since its first vertex is \(j+1\), it cannot use the nonexistent direct arc \(j+1\to j\). Every arc follows an edge of the undirected cycle \(C_n\), and the only simple path in \(C_n\) from \(j+1\) to \(j\) avoiding their direct edge is
\[
j+1,j+2,\ldots,j-1,j.
\]
Hence every successive forward arc occurs. Joining the already established \(j\to j+1\) gives (CF2). \(\square\)

In particular, if the union pair has no directed Hamilton cycle of this orientation, the shared-projection cross-root assertion holds in every dimension. The other unresolved shared-site prototype, \(H(a,b)=a\land b\), has two incoming neighbor influences and requires a different structural argument.


##### Independent incidence realization on interaction trees

Let \(f\) be an arbitrary binary coloring of the undirected edges of \(Q_d\). For each dimension \(i\), write \(f_i(x)\) for the color of the direction-\(i\) edge incident with \(x\); this is independent of \(x_i\). Its **interaction graph** \(G(f)\) joins \(i,j\) when either \(\partial_j f_i\) or \(\partial_i f_j\) is nonzero. Consequently \(f_i\) depends only on the bits of the neighboring directions \(N_G(i)\).

For every incident pair of graph vertices \(i,j\), regard \(a_{ij}\in\mathbb F_2\) as a prescribed value of bit \(j\) at the instant a full direction-simple path traverses dimension \(i\). Let \(\pi\) be the order of the traversed dimensions. The incidence equation is
\[
\boxed{a_{ij}=x_j+[\pi(j)<\pi(i)]\pmod2.}
\tag{1}
\]

**Lemma 1 (universal realization of prescribed incidences on trees).** Let \(T\) be any tree on a set of \(m\ge2\) directions. Prescribe the two incidence bits \(a_{ij},a_{ji}\) independently for every edge \(ij\) of \(T\). There exist an initial cube vertex \(x\) and a permutation \(\pi\) of the directions satisfying every equation (1). In fact, there are two antipodal choices of \(x\), with corresponding reverse orientations of \(T\). A suitable pair can be constructed in linear time from the incidence data.

*Proof.* Choose a tree root \(r\) and set \(x_r\) arbitrarily. Process the tree outward. When the parent \(p\) has known bit \(x_p\) and \(c\) is a new child, orient the edge \(p\to c\) if
\[
\varepsilon_{pc}=a_{cp}+x_p=1,
\]
and orient it \(c\to p\) otherwise. In either case define
\[
x_c=a_{pc}+1+\varepsilon_{pc}\pmod2.
\]
If \(p\) is earlier, its bit at the traversal of \(c\) is \(x_p+1=a_{cp}\); if it is later, the bit is \(x_p=a_{cp}\). The definition of \(x_c\) similarly makes the bit of \(c\) at traversal of \(p\) equal \(a_{pc}\). Thus the incidence equations hold on the new edge. Repeat for all edges. Every orientation of a tree is acyclic, so it extends to a total permutation \(\pi\). Changing \(x_r\) flips all inferred root bits and reverses every tree-edge orientation, giving the second solution. QED.

**Theorem 2 (admissible monochromatic targets on arbitrary nonlinear trees).** Suppose the interaction graph \(G(f)\) is a tree and choose a prescribed color \(t\in\{0,1\}\) **attained by every direction's local neighbor-bit function**:
\[
\boxed{t\in\bigcap_{i\in V(G)}\operatorname{im}(f_i).}
\]
Then there exists a full dimension-simple antipodal geodesic of constant color \(t\). The statement holds for arbitrary nonlinear local functions and is constructive.

*Proof.* For each \(i\), the displayed hypothesis permits an independent assignment \((a_{ij})_{j\in N(i)}\) satisfying \(f_i((a_{ij})_j)=t\). Lemma 1 realizes all chosen incidence bits simultaneously through a root and an acyclic orientation of the tree; topologically order its vertices to obtain a full antipodal geodesic. Every traversed edge has color \(t\). QED.

**Necessary qualification.** Connectedness of the *undirected* interaction graph alone does not imply that each \(f_i\) is nonconstant. An edge \(ij\) can arise solely from dependence of \(f_j\) on bit \(i\), while \(f_i\) is constant. For example on \(Q_3\) let \(f_1\equiv0\), \(f_3\equiv1\), and \(f_2(x)=x_1+x_3\). The interaction graph is the connected path \(1-2-3\), but no monochromatic full geodesic can exist, because every full geodesic uses direction 1 of color zero and direction 3 of color one. Thus the previously published unrestricted monochromatic-tree claim was false; the theorem above replaces it.

**Corollary 3 (paired roots in target-admissible interaction forests).** Suppose \(G(f)\) is a forest with \(c\) nontrivial connected tree components and \(r\) isolated vertices. Assume that in each nontrivial component \(C\), there is a bit \(t_C\) attained by **every** local color function in \(C\). Then
\[
\boxed{|P(f)|\ge 2^{c+r}.}
\]
In particular the condition holds when all local functions in each nontrivial component are nonconstant.

*Proof.* Theorem 2 produces a monochromatic color-\(t_C\) antipodal geodesic in each component; reversing it gives a second root at its antipode. An isolated direction has a constant color and allows either root bit. Select the roots independently in all components. To form a \(0^*1^*\) full geodesic, concatenate all component paths and singleton directions colored zero, followed by those colored one. For the reverse \(1^*0^*\) orientation, concatenate the same selected component paths in the opposite color-block order. Independence between interaction components preserves all edge colors and all dimensions are used once. The choices give at least \(2^{c+r}\) paired roots. QED.

**Corollary 4 (NORI1 over target-admissible forest facets).** An antipodally odd coloring of \(Q_{d+1}=Q_d\times\{0,1\}\) whose lower-facet interaction forest satisfies the common-target condition of Corollary 3 admits at least \(2^{c+r}\) distinct directed monochromatic full antipodal geodesics, for arbitrary odd vertical bridge colors.

*Proof.* Apply Corollary 3 and the universal paired-root bridge equivalence. QED.

##### Cycle-syndrome criterion for arbitrary interaction graphs

The tree realization proof extends to a graph with cycles, but now two precisely described obstructions arise.

For an arbitrary undirected graph \(G\) on the direction set and a full specification of the incident bits \(a_{ij}\) on its edges, set
\[
\lambda_{ij}=1+a_{ij}+a_{ji}\pmod2
\tag{3}
\]
for each edge \(ij\).

**Theorem 5 (cycle parity and acyclic orientation characterization).** The incidence prescription (1) is realizable by a root \(x\) and a total direction order \(\pi\) if and only if the following two conditions hold:

(i) for every cycle \(C\) of \(G\),
\[
\boxed{\sum_{ij\in E(C)}\lambda_{ij}=0\pmod2;}
\tag{4}
\]

(ii) choose either vertex potential \(x\) solving \(x_i+x_j=\lambda_{ij}\) on each connected component, and orient every graph edge \(j\to i\) when \(a_{ij}+x_j=1\); the resulting graph orientation is acyclic.

When (i) holds, the solutions for \(x\) are the two global-complement choices on each connected component. Replacing a potential by its complement reverses every edge orientation in that component, so condition (ii) is independent of which potential is chosen.

*Proof.* If (1) holds for some \(x,\pi\), summing the two incidence equations at the endpoints of an edge gives
\[
a_{ij}+a_{ji}=x_i+x_j+1.
\]
Thus the \(\lambda\)-values form a vertex coboundary, which is equivalent to (4). The induced edge orientations follow the total order \(\pi\) and hence are acyclic.

Conversely (4) makes the edge equations \(x_i+x_j=\lambda_{ij}\) solvable, uniquely up to one bit per connected component. Orient edge \(j\to i\) whenever \(a_{ij}+x_j=1\). Since
\[
(a_{ij}+x_j)+(a_{ji}+x_i)
=a_{ij}+a_{ji}+\lambda_{ij}=1,
\]
this assigns one direction to each undirected graph edge. If the orientation is acyclic, choose any of its topological total orders \(\pi\). The incidence equations (1) hold by construction. Replacing all \(x_i\) in one component by \(x_i+1\) reverses each orientation there; directed cycles exist in an orientation if and only if they exist in its reversal. QED.

**Corollary 6 (cyclomatic localization of a monochromatic obstruction).** If local neighbor-bit inputs making every direction color \(t\) can be chosen independently, then failure to realize those inputs as a monochromatic full geodesic can arise only from the cycle-parity constraints (4) and the acyclicity requirement in Theorem 5. A graph with cycle-space dimension
\[
\beta_1(G)=|E(G)|-|V(G)|+\#\text{components}
\]
has \(\beta_1(G)\) independent parity equations. On a forest there are none and the orientation condition is automatic. This gives a cycle-rank parameterization of the remaining difficulty, preserving all direction uses.

**Example 7 (a single even cycle already obstructs monochromaticity).** On \(Q_{2r}\), \(r\ge2\), index dimensions cyclically and define
\[
f_i(x)=x_{i-1}+x_{i+1}+a_i\pmod2,
\qquad \sum_i a_i=1\pmod2.
\tag{5}
\]
Its interaction graph is the even cycle \(C_{2r}\). Along any full antipodal dimension order, each graph edge contributes once to the sum of the traversed colors, while every starting bit appears twice. Therefore
\[
\sum_{\text{all }2r\text{ steps}}\text{color}
=\sum_i a_i+|E(C_{2r})|
=1\pmod2.
\]
A monochromatic word of even length has parity zero, so this coloring has **no monochromatic full antipodal geodesic from any root**. This shows that the tree monochromatic theorem does not extend unchanged to unicyclic interaction graphs. The paired-root conjecture remains a different and weaker assertion: existence of both monotone orientations from one root is not ruled out by this parity obstruction.

**Closure program.** Theorem 5 isolates the first obstruction after constructing admissible local tree prescriptions: nonzero syndrome around independent cycles and directed circuits of an induced orientation. To extend a closure proof toward general interactions, one should seek simultaneous prescribed input patterns supporting the two monotone orientations and show that a minimal incompatible cycle can be repaired by changing the seam placement or by an exchange of path orders. Unlike a bound based on small cube dimensions, the present realization and obstruction calculus applies to graphs of arbitrary order and arbitrary nonlinear local coloring functions.### Quantitative tree incidence paths

For a connected nontrivial interaction tree \(T\), let
\[
r_i(t)=|\{a\in\mathbb F_2^{N(i)}:f_i(a)=t\}|\ge1.
\]
Let \(G_t(f)\) be the number of directed rooted full antipodal geodesics of constant color \(t\).

**Theorem 8 (tree path census).** For each \(t\in\{0,1\}\),
\[
\boxed{G_t(f)\ge2\prod_i r_i(t).}
\tag{6}
\]
Indeed, if \(\mathcal A_t=\prod_i f_i^{-1}(t)\), and \(O(a)\) is the oriented tree resulting from the incidence-realization lemma with root bit fixed, while \(L(O)\) counts its topological total orders, then
\[
\boxed{G_t(f)=2\sum_{a\in\mathcal A_t}L(O(a)).}
\tag{7}
\]

*Proof.* For each local-successful incidence specification \(a\), the tree realization lemma supplies two antipodal initial vertices. Their tree orientations are reversals and have equal numbers of topological orders. Each topological order traverses every dimension once, realizing the specified neighbor-bit inputs and therefore constant edge color \(t\). Conversely each such rooted monochromatic path determines its local incidence specification, so paths from different specifications cannot coincide. Summation gives (7), and \(L(O)\ge1\) gives (6). QED.

**Corollary 9 (balanced nonlinear trees).** If each local color function gives color \(t\) on half of its neighbor assignments, then
\[
G_t(f)\ge2^{d-1},
\]
since \(\sum_i(\deg_T(i)-1)=d-2\). There is no linearity assumption.

##### Affine parity colorings on one interaction cycle

Index the \(n\ge3\) directions cyclically. Define
\[
\boxed{f_i(x)=a_i+x_{i-1}+x_{i+1}\pmod2,}
\tag{8}
\]
and write \(A=\sum_i a_i\pmod2\). Fix a root \(x\) and let \(b_i=a_i+x_{i-1}+x_{i+1}\), so \(\sum_i b_i=A\). If a direction permutation orients each cycle edge from earlier to later, with \(p_i\) the parity of the number of earlier neighbors of \(i\), then its step color in direction \(i\) is \(b_i+p_i\).

**Lemma 10 (acyclic cycle indegree parity).** A vector \(p\in\mathbb F_2^n\) arises as the indegree-parity vector of an acyclic orientation of \(C_n\) if and only if
\[
\boxed{\sum_i p_i=n\pmod2,\qquad p\ne\mathbf1.}
\tag{9}
\]
When the parity equation holds there are two orientations having those parities, related by reversal of every cycle edge; they are both cyclic precisely for \(p=\mathbf1\).

*Proof.* Let \(u_i=1\) if \(i\) precedes \(i+1\) on their graph edge. Then
\(p_i=1+u_{i-1}+u_i\pmod2\).
Summing gives the parity condition. If it holds, choosing one \(u_i\) freely determines all the others around the cycle, with two complementary solutions. An orientation of a simple cycle is cyclic precisely when all its graph edges point around the cycle consistently; this makes \(p_i=1\) at every vertex. Every other orientation admits a total topological ordering. QED.

**Theorem 11 (full paired-root classification for cycle-neighbor parity colorings).**
\[
\boxed{|P(f)|=\begin{cases}2^n,&n\text{ even},\\2^n-2,&n\text{ odd}.\end{cases}}
\tag{10}
\]
More precisely:
(a) If \(n\) is even and \(A=0\), every root supports a monochromatic full geodesic.
(b) If \(n\) is even and \(A=1\), no root supports a monochromatic full geodesic, yet every root supports both color words \(0^{n-1}1\) and \(10^{n-1}\).
(c) If \(n\) is odd, every root except two antipodal roots supports a monochromatic full geodesic of color \(1+A\); those two exceptional roots admit no monotone full color word.

*Proof.* Suppose \(n\) is even. If \(A=0\), the parity vector \(p=b\) meets Lemma 10's sum condition. If \(b\ne\mathbf1\), its acyclic orientation gives all-zero traversed edge colors. If \(b=\mathbf1\), take \(p=\mathbf0\) instead, giving all-one traversed colors. Hence every root is paired.

If \(n\) is even and \(A=1\), then \(b\) has odd Hamming parity. Choose \(v\) with \(b_v=1\) and prescribe the traversed color of direction \(v\) to be one and all others zero. The required indegree parity is \(p=b+e_v\), whose total parity is zero and whose value at \(v\) is zero. The two opposite acyclic orientations from Lemma 10 make \(v\) respectively a source (indegree zero) and a sink (indegree two). Extend the first to a topological order with \(v\) first, and the second to one with \(v\) last. These give the two required words from the **same root**. No constant-color word is possible: every full path has total color parity
\(\sum_i b_i+\sum_i p_i=A+n=1\), while any constant word of even length has parity zero.

Now suppose \(n\) is odd. Let \(t=1+A\). To obtain a constant color-\(t\) path, the desired indegree parity is \(p=b+t\), with sum \(A+nt=A+t=1=n\pmod2\). Lemma 10 therefore gives a suitable acyclic orientation unless \(p=\mathbf1\), equivalently \(b_i=A\) at every direction. The exceptional roots solve
\[
x_{i-1}+x_{i+1}=A+a_i\pmod2
\quad\text{for all }i.
\]
The right side sums to zero; the linear map \(x\mapsto(x_{i-1}+x_{i+1})_i\) on an odd cycle has kernel consisting of the two constant binary strings, because kernel elements have period two and \(n\) is odd. Thus precisely two antipodal roots are exceptional.

At either exceptional root \(b_i=A\) for every \(i\). Along any full direction order the first step has no earlier graph neighbors and the last has two, so their colors both equal \(A\). A monotone binary word with equal first and last entries must be constant \(A\). But total step-color parity is \(\sum_i b_i+\sum_i p_i=A+1\), whereas the constant word \(A^n\) has parity \(A\). Thus no monotone full path exists from either exceptional root. This proves the theorem. QED.

**Closure implication.** The first cycle-parity obstruction to a monochromatic full geodesic is sometimes unavoidable: case (b) rules out such a path in every even dimension. Nevertheless the obstruction can be moved between the first and last directions by reversing a cycle orientation, yielding the paired paths NORI1 requires at every root. This identifies an induction motif beyond the tree-realization theorem but does not settle nonlinear cyclic interactions.

#### Pendant direction elimination by a two-word insertion lemma

The tree realization theorem resolves interaction forests, but a stronger property is available: a responsive pendant direction can be removed from **any** interaction graph, regardless of the complexity of the remaining graph.

Let \(f\) color the edges of \(Q_{m+1}\), with a distinguished direction \(i\) and another direction \(j\ne i\). Assume
\[
f_i(x)=x_j+a\quad(a\in\mathbb F_2)
\tag{11}
\]
for every direction-\(i\) edge, and assume that for all directions \(k\notin\{i,j\}\), the color \(f_k\) is independent of bit \(x_i\). The color \(f_j\) may depend **arbitrarily** on \(x_i\) and all other permitted bits. These assumptions hold whenever \(i\) is a leaf of the undirected interaction graph and its own color function depends nontrivially on the bit of its neighbor \(j\). Let \(f^{(0)},f^{(1)}\) denote the facet colorings obtained by fixing \(x_i=0,1\).

**Theorem 12 (responsive-leaf paired-root lifting).** Under (11), every root \(x\in P(f^{(0)})\) has at least one lift among \((x,0),(x,1)\) belonging to \(P(f)\). The same conclusion holds with the facet \(x_i=1\) in place of \(x_i=0\). Consequently
\[
\boxed{|P(f)|\ge |P(f^{(0)})\cup P(f^{(1)})|
\ge\max(|P(f^{(0)})|,|P(f^{(1)})|).}
\tag{12}
\]
In particular, paired-root existence is preserved by adjoining a responsive pendant direction, even when the interaction between that leaf and its neighbor is bidirectional.

*Proof.* Fix \(x\in P(f^{(0)})\), and select complete facet geodesics \(P_\uparrow,P_\downarrow\) from \(x\) with color words \(0^*1^*\) and \(1^*0^*\). Let \(u\) be the color of direction \(j\) on \(P_\uparrow\), and \(v\) its color on \(P_\downarrow\). Put
\[
\alpha=x_j+a,\qquad\beta=1+\alpha.
\tag{13}
\]
If the new \(i\)-step is inserted **after** the \(j\)-step into either facet path, start the enlarged path with \(x_i=0\). All old step colors remain unchanged: direction \(j\) is traversed while \(x_i=0\), and the colors of all other old directions are independent of \(x_i\). The inserted \(i\)-edge then has color \(\beta\), because the \(j\)-bit has been toggled. Inserting a bit \(\beta\) after direction \(j\) preserves the nondecreasing word if \(\beta=1\) or \(u=0\); it preserves the nonincreasing word if \(\beta=0\) or \(v=1\). When \(\beta=1\), place the inserted step at the end of the nondecreasing path and immediately after \(j\) in the nonincreasing path (provided \(v=1\)). When \(\beta=0\), put it immediately after \(j\) in the nondecreasing path (provided \(u=0\)) and at the end of the nonincreasing path.

Alternatively, insert the new \(i\)-step **before** direction \(j\) and start at \(x_i=1\). Again all old colors are read from facet zero. The inserted step has color \(\alpha\), since \(j\) is still unused. Such insertion preserves the nondecreasing word when \(\alpha=0\) or \(u=1\), and preserves the nonincreasing word when \(\alpha=1\) or \(v=0\), placing the new step at the beginning or immediately before \(j\) as appropriate.

Now \(\alpha+\beta=1\). If \(\alpha=0,\beta=1\), the after-\(j\) construction works when \(v=1\), and the before-\(j\) construction works when \(v=0\). If \(\alpha=1,\beta=0\), the after-\(j\) construction works when \(u=0\), and the before-\(j\) construction works when \(u=1\). Thus one starting \(i\)-bit always supports both monotone words from the same enlarged root. All steps remain dimension-simple. This proves the first assertion; interchanging the two facets gives the same argument for \(f^{(1)}\).

For every \(x\) in the union of the two facet paired-root sets, choose one successful enlarged root in its two-element \(i\)-fiber. Different \(x\) give different roots, proving (12). QED.

**Corollary 13 (responsive-leaf pruning of irreducible obstructions).** Starting with any cube-edge coloring, repeatedly remove a leaf direction \(i\) of its undirected interaction graph whenever \(f_i\) depends nontrivially on its unique neighbor. At each removal restrict to either chosen facet of \(i\). If the final lower-dimensional coloring has a paired root, then the initial coloring also has a paired root. In particular the terminal coloring may be resolved by any previously proved criterion, including the corrected target-admissible forest theorem, the star theorem, or directed influence component seam lifting. Every hypothetical paired-root counterexample remains a counterexample under either facet restriction at every responsive pendant direction.

*Proof.* Theorem 12 lifts paired roots from either facet; contraposition and iteration prove the last assertion. QED.

**Proposition 14 (residual constant-source leaf obstruction).** Suppose instead the pendant direction \(i\) has constant edge color \(t\in\{0,1\}\), while its sole neighbor \(j\) may depend on bit \(i\), and all other old direction colors are independent of \(i\). Fix a paired root \(x\) of facet zero. If either of its two monotone witness paths traverses direction \(j\) with color \(t\), then at least one of \((x,0),(x,1)\) is paired in the full cube.

*Proof.* In the preceding insertion argument, now \(\alpha=\beta=t\). If \(t=0\) and the nondecreasing witness has its \(j\)-step colored zero, insert \(i\) after \(j\) when starting at \(i=0\); append \(i\) to the nonincreasing witness. If the nonincreasing witness has its \(j\)-step colored zero, insert \(i\) before \(j\) when starting at \(i=1\), and prepend it to the nondecreasing witness. The two cases for \(t=1\) follow by interchanging the colors and orientations. Old colors again remain unchanged because direction \(j\) is traversed in facet zero. QED.

Thus, for a constant-color pendant direction to obstruct this elementary lifting construction, **every** monotone facet witness at **every** paired root must traverse its neighboring direction with the opposite color. This gives a precise rigidity condition for the remaining source-leaf case, which is not settled by the responsive-leaf theorem.

**Connection to closure.** The directed SCC theorem removes one-way dependence blocks, while Theorem 12 eliminates bidirectionally interacting pendant directions with a nonconstant leaf function. Together they show that a minimal counterexample cannot be explained solely by a large strongly connected component with responsive trees attached to it. The unresolved leaf obstruction is asymmetric: a constant-colored leaf influencing its neighbor, rather than a leaf whose own color responds to that neighbor.

#### Source-pendant directions and the one-class cross-favorability bottleneck

Let \(f\) be any binary coloring of \(Q_{m+1}=Q_m\times\{0,1\}\) whose edges in the added direction \(i\) all have the same color \(t\). No other hypothesis is imposed initially. Let \(h_0,h_1\) be the induced colorings of the two \(m\)-dimensional facets.

**Lemma 15 (constant-direction cross-seam gluing).** If either of the two intersections
\[
\boxed{A_0(h_0)\cap A_1(h_1),\qquad
A_0(h_1)\cap A_1(h_0)}
\tag{14}
\]
is nonempty, then the full coloring \(f\) has a paired root.

*Proof.* Suppose \(z\in A_0(h_0)\cap A_1(h_1)\). If \(t=0\), start at \((z,1)\). A nondecreasing full path traverses the new direction first (color zero) and then follows the chosen \(0^*1^*\) path in facet zero. A nonincreasing full path follows the chosen \(1^*0^*\) path in facet one and then traverses the new direction last (color zero). Both begin at the same root, are dimension-simple and monotone. If \(t=1\), start instead at \((z,0)\): the nondecreasing path follows its facet-zero path first and then uses the new direction last (color one), whereas the nonincreasing path uses the new direction first and then follows its facet-one path. The other intersection in (14) is handled by interchanging the two facets. QED.

**Corollary 16 (two-sided cross separation forced by a bad source leaf).** If \(f\) has no paired root and its direction-\(i\) edges have constant color, both intersections in (14) must be empty.

If, in addition, \(i\) is a leaf of the undirected interaction graph with sole neighbor \(j\), then \(h_0,h_1\) differ only in the colors of the edges of direction \(j\); every other direction has the same colors in both facets. Thus a bad constant-source pendant direction forces a pair of colorings with **one direction-class difference** whose opposite-orientation feasible-root sets are mutually disjoint.

**Theorem 17 (necessary structure of a minimum-dimension counterexample).** Suppose the paired-root conjecture fails and choose a counterexample \(f\) of least cube dimension \(d\). Then:

1. Every proper facet coloring has a paired root, by minimum-dimensional choice.
2. The undirected interaction graph is connected, by Cartesian product factorization.
3. The interaction graph cannot satisfy the common-local-target hypothesis of corrected Theorem 2, since such a coloring would have a monochromatic geodesic and hence a paired root. It is **not proved** that a connected interaction forest always has paired roots without that hypothesis.
4. Every pendant direction \(i\), if present, has a **constant** edge color. Otherwise responsive-leaf lifting would produce a paired root from a lower-dimensional facet.
5. For each constant-colored pendant direction with neighbor \(j\), the two lower-dimensional facet colorings differ only on direction \(j\); they each have paired roots but their two cross-orientation feasible-root intersections vanish.
6. Its directed influence graph has a strongly connected component of size at least four by seam lifting, or at least five using the separate computer-assisted four-cube certificate.

*Proof.* The cited factorization, conditional tree, pendant lifting, and seam theorems prove the assertions. The earlier statement that connectedness and badness force an undirected graph cycle depended on the incorrect unrestricted forest claim and has been withdrawn. QED.

**Proposed sufficient closure lemma (open).** Let \(g,h\) be two arbitrary binary colorings of \(Q_m\) that **agree on every edge outside one direction class**. Prove
\[
\boxed{A_0(g)\cap A_1(h)\ne\varnothing.}
\tag{15}
\]
This is considerably narrower than demanding cross-favorability for two completely unrelated colorings. If established for every \(m\), Lemma 15 and Theorem 12 would rule out all pendant directions in a least-dimension paired-root counterexample, leaving an undirected interaction graph of minimum degree at least two. Moreover the theorem would make *all* constant-source pendant directions safely removable, complementing the responsive-leaf elimination theorem.

**Additional implication.** If either facet coloring \(h_s\) of a constant-source leaf has a paired root with a monochromatic full path of the same color \(t\) as the leaf, that path lifts to a monochromatic full path of the full cube: start in facet \(s\), retain every old direction's edge colors by taking the constant new direction at the suitable end while the sole neighbor is read in facet \(s\), and append the same-color step. In particular the failure certificates above require careful attention to the one-switch witnesses, not merely the existence of independently monochromatic facet paths of the favorable color.

The unresolved source-leaf obstruction has thus been isolated as a one-direction cross-intersection problem, while responsive leaves have been removed unconditionally. This provides a focused next target for root-synchronization or path-exchange arguments.

#### Local-incidence enumeration of arbitrary full geodesic color words

The cycle-syndrome theorem can be sharpened to describe *all* rooted full geodesics and both monotone orientations as local incidence constraints, with no restriction to trees, affine color functions, or special orders.

Let \(G=G(f)\) be a connected interaction graph on the \(d\) cube directions, and let
\[
f_i:\mathbb F_2^{N_G(i)}\to\mathbb F_2
\]
be its arbitrary local direction-color functions. Fix any prescribed direction-indexed step-color vector \(t=(t_i)_{i\in V(G)}\in\mathbb F_2^d\). Define the independently selectable local input patterns
\[
\mathcal A(t)=\prod_{i\in V(G)} f_i^{-1}(t_i).
\tag{16}
\]
For \(a\in\mathcal A(t)\), put \(\lambda_{ij}=1+a_{ij}+a_{ji}\) on each graph edge. If \(\lambda\) has zero sum around every cycle, choose either solution \(x\) of \(x_i+x_j=\lambda_{ij}\), orient graph edge \(j\to i\) when \(a_{ij}+x_j=1\), and denote the resulting orientation by \(O(a,x)\). The other root potential is \(\bar x\), which reverses the entire orientation.

Let \(L(O)\) be the number of topological total orders of an acyclic graph orientation \(O\), and zero when \(O\) has a directed cycle. Let \(L_\uparrow(O,t)\) count those topological total orders \(\pi\) that also satisfy
\[
t_{\pi_1}\le t_{\pi_2}\le\cdots\le t_{\pi_d},
\]
and define \(L_\downarrow(O,t)\) similarly with reversed inequality.

**Theorem 18 (local incidence path census).** The number of rooted directed full cube geodesics whose edge color in direction \(i\) is \(t_i\) equals
\[
\boxed{
N_t(f)=\sum_{\substack{a\in\mathcal A(t)\\
\lambda(a)\text{ has zero cycle periods}}}
\Bigl(L(O(a,x))+L(O(a,x)^{\rm rev})\Bigr).
}
\tag{17}
\]
The corresponding number whose *ordered* step colors are nondecreasing, respectively nonincreasing, is obtained by replacing \(L\) with \(L_\uparrow(O,t)\), respectively \(L_\downarrow(O,t)\), in both summands.

*Proof.* A rooted geodesic with root \(x\) and direction order \(\pi\) yields the incidence inputs
\(a_{ij}=x_j+[\pi(j)<\pi(i)]\).
Its color in direction \(i\) is \(f_i((a_{ij})_j)=t_i\), so its incidence specification lies in \(\mathcal A(t)\). As in Theorem 5, the resulting edge cochain \(\lambda\) is a vertex coboundary and the induced graph orientation is acyclic, with \(\pi\) among its topological extensions.

Conversely, for any \(a\) with zero cycle periods, the two root potentials \(x,\bar x\) give opposite graph orientations. Each topological extension of either orientation realizes the same prescribed incident bit values at all direction steps. Its color vector is therefore \(t\). Distinct incidence specifications cannot represent the same rooted order, because the latter determines every \(a_{ij}\). Summing counts every rooted geodesic once and gives (17). Restricting the counted topological extensions to color-sorted orders proves the monotone versions. QED.

**Corollary 19 (monotone path criterion by an oriented graph cut).** Given an incidence choice \(a\in\mathcal A(t)\) with vanishing cycle periods, a rooted full \(0^*1^*\) geodesic with step-color vector \(t\) is represented by one of its two potentials if and only if its induced orientation is acyclic **and every edge between a vertex with \(t_i=0\) and one with \(t_j=1\) points from the zero vertex toward the one vertex**. For a \(1^*0^*\) path, reverse the direction of all cross-color edges.

*Proof.* A topological order that first lists all vertices of color zero and then all of color one exists if and only if the orientation has no directed cycle and no edge pointing from a one-labeled vertex toward a zero-labeled vertex. Under these conditions, take a topological order of the zero-induced subgraph followed by one of the one-induced subgraph. The reverse-color assertion is analogous. QED.

**Corollary 20 (topological reduction of the paired-root requirement).** A root \(x\) is paired precisely when there are two locally successful incidence patterns \(a^\uparrow,a^\downarrow\) (possibly having different step-color vectors \(t^\uparrow,t^\downarrow\)), both inducing *the same root potential \(x\)*, whose graph orientations are acyclic and whose respective color cuts point in opposite monotone directions. This is a finite local-incidence formulation of the paired-root problem that retains the full one-use-per-dimension condition.

**Structural significance.** Tree interaction graphs have no cycle-period restrictions and every induced orientation is acyclic, explaining Theorem 2. A graph with cycles introduces a graphic-cohomology obstruction \(\lambda\notin B^1(G;\mathbb F_2)\), followed by acyclic-orientation restrictions. The cross-color cut criterion adds a further orientation constraint only when both colors occur. This exposes an intrinsic incidence/chamber object on which a deletion-contraction or cycle-exchange proof may operate, rather than testing small cube orders.

**Relation to existing graph-orientation literature.** The parity part is closely related to the acyclic orientation with prescribed indegree parities problem: see Sylvain Gravier, Matthieu Petiteau, and Isabelle Sivignon, *Some polynomial classes for the acyclic orientation with parity constraint problem*, arXiv:2603.09475 (March 2026), and the EGRES open problem on acyclic orientations with parity constraints. Acyclicity is essential and nontrivial on graphs with many cycles, as illustrated already by complete graphs. The added feature here is that the target parities and color cut can be chosen through the local color-function fibers and that two compatible root certificates are sought, rather than one prescribed parity vector.

#### Unconditional paired-root theorem for arbitrary nonlinear interaction trees

The preceding target-admissible monochromatic-tree theorem is intentionally conditional: opposite constant-colored direction classes prevent monochromatic full paths. Nevertheless **every** tree-local coloring admits both monotone path orientations at one common root. This resolves the source-pendant obstruction for entire interaction trees without requiring monochromatic paths.

Let \(T\) be a tree on the direction set \(V(T)\), and let
\[
f_v:\{0,1\}^{N_T(v)}\to\{0,1\}
\]
be completely arbitrary local functions for the colors of the undirected direction-\(v\) cube edges. Fix a tree root \(r\) and orient the tree away from it. We construct one common initial cube vertex and two directed orientations of the tree edges, to be extended to full dimension orders.

For a nonroot vertex \(v\), denote its parent by \(p\) and its children by \(w_1,\ldots,w_k\). An *opposite-bit interface request* specifies:
- the starting bit \(s_p\in\{0,1\}\) of parent direction \(p\);
- the color \(U\) traversed at \(p\) in the required nondecreasing path and \(V\) traversed there in the nonincreasing path;
- two different bits \(a_\uparrow,a_\downarrow=1-a_\uparrow\), required as the observed value of bit \(v\) at the traversal of direction \(p\) in the respective paths.

The task is to choose the same starting bits for all vertices of the subtree rooted at \(v\), and to orient all its tree edges separately in the two paths, so that every oriented tree edge has nondecreasing colors in the first path and nonincreasing colors in the second. In particular the parent edge \(pv\) must satisfy its color comparison and interface request.

**Lemma 21 (universal opposite-bit subtree interface).** Every such request is feasible for every finite rooted tree and every collection of nonlinear local color functions. It can be realized recursively with two evaluations of \(f_v\) per processed direction.

*Proof.* Induct on the subtree size. At vertex \(v\), evaluate
\[
p_0=f_v(s_p+1,0,\ldots,0),\qquad
p_1=f_v(s_p,1,\ldots,1),
\tag{21}
\]
where the first argument is the parent bit and the remaining arguments are the children's bits seen when direction \(v\) is traversed.

**Case A:** If \(p_0\ge U\) and \(p_1\ge V\), choose the starting bit
\(s_v=a_\uparrow\).
Put \(p\) before \(v\) in the nondecreasing orientation and \(v\) before \(p\) in the nonincreasing orientation. Thus at the parent traversal the observed bit of \(v\) is respectively \(s_v=a_\uparrow\) and \(1-s_v=a_\downarrow\). Demand that every child bit seen at \(v\) be zero in the first orientation and one in the second. Under these requests the edge of direction \(v\) has colors \(p_0,p_1\), respectively. The required parent-edge comparisons are \(U\le p_0\) and \(p_1\ge V\), which hold.

**Case B:** Otherwise choose \(s_v=1-a_\uparrow\), put \(v\) before \(p\) in the nondecreasing orientation and \(p\) before \(v\) in the nonincreasing orientation. Demand that every child bit seen at \(v\) be one in the first orientation and zero in the second. The resulting colors of direction \(v\) are \(p_1,p_0\), respectively; the parent comparisons require \(p_1\le U\) and \(p_0\le V\).

Case B is always valid when A fails, because all four quantities are Boolean:
\[
\boxed{\neg(p_0\ge U\land p_1\ge V)
\quad\Longrightarrow\quad
(p_1\le U\land p_0\le V).}
\tag{22}
\]
To check (22), if \(U=V=0\), A always succeeds; if \(U=V=1\), the right side is automatic. When \((U,V)=(0,1)\), failure of A forces \(p_1=0\); when \((U,V)=(1,0)\), failure forces \(p_0=0\). Both give the desired inequalities.

In both cases the chosen parent-edge orientations and root bit \(s_v\) satisfy the interface request. Each child's required observed-bit pair is either \((0,1)\) or \((1,0)\). Apply the induction hypothesis independently to the child subtrees, taking their parent bit to be \(s_v\) and their parent color pair to be the constructed \((p_0,p_1)\) or \((p_1,p_0)\). The child realizations use mutually disjoint direction sets, so they combine into a single root assignment and two oriented trees. Every edge comparison holds. The base case of no children uses the same two schemes. QED.

**Theorem 22 (unrestricted nonlinear tree paired-root closure).** If the interaction graph of an arbitrary binary coloring of \(Q_d\) is a tree, then
\[
\boxed{P(f)\ne\varnothing.}
\tag{23}
\]
More strongly, for any specified direction \(r\) and either prescribed starting bit \(s_r\in\{0,1\}\), there is a paired root having that bit. Hence \(|P(f)|\ge2\) when \(d\ge1\).

*Proof.* Root the interaction tree at \(r\), and fix the starting bit \(s_r\) as prescribed. In the first desired orientation prescribe observed bit zero for every child of \(r\) at its traversal; in the second prescribe observed bit one. This makes the colors of direction \(r\)
\[
U=f_r(0,\ldots,0),\qquad V=f_r(1,\ldots,1).
\]
For each child of \(r\), use Lemma 21 with parent bit \(s_r\), parent color pair \((U,V)\), and interface request \((0,1)\). Combining these recursive subtree constructions gives one common starting cube vertex and two edge orientations of \(T\) such that every earlier-to-later oriented edge respects the nondecreasing, respectively nonincreasing, color order.

Because \(T\) is a tree, each orientation is acyclic. Since every cross-color edge is oriented from color zero to color one in the first orientation, a topological order of all zero-colored directions followed by one of all one-colored directions extends the entire first orientation. Similarly a topological order of one-colored directions followed by zero-colored directions extends the second. Each resulting full cube geodesic uses every direction once; the initial cube vertex is shared, because Lemma 21 uses common subtree starting bits for both orientations. Their color words are \(0^*1^*\) and \(1^*0^*\). Since either starting bit \(s_r\) may be prescribed independently, the theorem follows. QED.

**Corollary 23 (unrestricted nonlinear forest theorem).** If the interaction graph is a forest with \(c\) connected components, including isolated directions, then
\[
\boxed{|P(f)|\ge2^c.}
\tag{24}
\]
No target-admissibility, linearity, or symmetry condition is needed. The theorem follows by taking two paired roots in each component and using Cartesian factorization of the paired-root sets.

**Corollary 24 (NORI1 over arbitrary forest facets).** Let the edges of \(Q_{d+1}\) be antipodally oddly colored, with completely unrestricted odd vertical bridge colors. If the restriction to one \(Q_d\)-facet has an interaction forest with \(c\) connected components, then at least \(2^c\) directed monochromatic full antipodal geodesics cross that facet. This follows from the universal bridge equivalence and Corollary 23.

**Algorithmic form.** When the interaction forest and the local edge-color evaluation oracle are provided, the proof constructs a paired root and two full direction orders using at most two local color evaluations per direction, followed by two color-respecting topological sorts. Thus the paired-root and bridge-geodesic constructions take \(O(d)\) color queries and linear work on the forest representation.

**Audit.** An independent implementation assembled both orientations and their shared starting vertex, evaluated the traversed cube-edge colors rather than relying on the stored tree labels, and verified the monotone full color words on 4,200 randomized nonlinear tree cases in dimensions \(2\) through \(15\). Independent exhaustive checks on all \(4,096\) path-local colorings of \(Q_4\) and all \(65,536\) path-local colorings of \(Q_5\) found no paired-root-free instances. These finite audits supplement the unrestricted induction proof.

**Correction and closure interpretation.** The previously withdrawn claim that all tree-interaction colorings have *monochromatic* full paths remains false when constant directions of opposite colors occur. The new unconditional result instead guarantees the two monotone orientations from one root, which is the target needed for the bridge reduction. It eliminates all undirected interaction forests from a minimum counterexample without assuming local color targets. Thus a paired-root-free coloring must possess at least one cycle in its undirected interaction graph; its directed influence feedback components must also satisfy the independent restrictions of the SCC seam theorem. The next obstruction is cycle consistency, not pendant-tree structure.

#### Full geodesic monotonicity on a cyclic interaction graph is a bounded-width constraint problem

The incidence-cycle syndrome theorem addressed monochromatic paths. For **monotone two-color paths**, the missing condition is that an acyclic orientation permit an ordering with every color-zero direction before every color-one direction. On a cycle this requirement is also local, and it yields an all-order transfer description of the paired-root conjecture.

Let the direction interaction graph be a subgraph of the cyclic graph on \(0,\ldots,n-1\), \(n\ge3\). The direction-i edge color therefore has the form \(f_i(x_{i-1},x_{i+1})\), with subscripts modulo n; all these functions may be nonlinear. Fix a root \(x\in\mathbb F_2^n\). For a cyclic edge \(i,i+1\), write \(u_i=1\) if i precedes i+1 in a dimension ordering, and \(u_i=0\) otherwise. Define
\[
\boxed{c_i(x,u)=f_i(x_{i-1}+u_{i-1},\,x_{i+1}+1-u_i).}
\tag{48}
\]
All additions to Boolean arguments are modulo two.

**Theorem (cyclic orientation criterion for monotone geodesics).** A full dimension-simple geodesic from x with word \(0^*1^*\) exists **if and only if** there is a nonconstant vector \(u\in\{0,1\}^n\) such that for each i modulo n,
\[
\boxed{
u_i=1\Longrightarrow c_i(x,u)\le c_{i+1}(x,u),\qquad
u_i=0\Longrightarrow c_{i+1}(x,u)\le c_i(x,u).
}
\tag{49}
\]
For word \(1^*0^*\), reverse both displayed inequalities. The criterion remains valid for any subgraph of the cyclic interaction graph, by allowing a local function to ignore a neighbor.

*Proof.* A direction ordering induces an orientation of each cycle edge by its earlier-to-later relation. In a consistently cyclic orientation all orientation bits u_i coincide. Conversely a nonconstant u gives an acyclic orientation of the undirected cycle and hence admits a topological ordering. Under the orientation u, the bit of predecessor i−1 seen when direction i is traversed is \(x_{i-1}+u_{i-1}\); the bit of successor i+1 is \(x_{i+1}+1-u_i\). Its traversed color is therefore c_i(x,u), independently of which topological order is chosen.

An acyclic orientation admits a topological ordering in which every color-zero vertex precedes every color-one vertex **if and only if** it has no directed edge from a color-one vertex to a color-zero vertex. Necessity is immediate. For sufficiency, take topological orderings of the induced zero-color and one-color subgraphs separately, concatenating zero before one; the absence of one-to-zero arrows ensures the result respects every oriented edge. The absence condition is precisely (49). Such a topological ordering gives a full geodesic with color word \(0^*1^*\). Reversing color order proves the second assertion. \(\square\)

**Theorem (paired roots as a constant-width cyclic CSP).** Let f and g be two arbitrary binary edge colorings with interaction graphs contained in the same direction cycle. Then
\[
\boxed{A_0(f)\cap A_1(g)\ne\varnothing}
\tag{50}
\]
holds if and only if one can choose a common root x and two nonconstant orientation words u,v satisfying (49) for f and the reversed version of (49) for g. Write the column symbol \(s_i=(x_i,u_i,v_i)\in\{0,1\}^3\). Every local constraint involves at most the four consecutive symbols
\[
\boxed{(s_{i-1},s_i,s_{i+1},s_{i+2}).}
\tag{51}
\]
Therefore (50) is decidable by a cyclic transfer algorithm of width three over an eight-symbol alphabet. Its underlying de Bruijn transfer graph has at most \(8^3=512\) boundary states; two additional two-bit masks can record whether both values occur in each of u and v, excluding cyclic orientations. The computation is **linear in n with a dimension-independent constant** (allowing enumeration of a fixed set of initial boundary states). When f=g, this tests the paired-root property.

*Proof.* Apply the first theorem to f using u and to g using v at the same root x. Each color \(c_i^u\) depends on \(x_{i-1},x_{i+1},u_{i-1},u_i\), and each neighboring color \(c_{i+1}^u\) depends on \(x_i,x_{i+2},u_i,u_{i+1}\); their comparison uses at most the four consecutive column symbols in (51). The same holds for v and g. A transfer state retains three consecutive symbols and appends one new symbol, rejecting any transition that violates the middle local condition. Recording occurrence of zero and one in each orientation word ensures neither is constant. Cyclic consistency is enforced by matching the final and initial column triples. Each valid closed walk of this transfer system gives a common root and two valid orientations, and every such triple yields a valid closed walk. The state space depends only on the eight-symbol alphabet and not on n. \(\square\)

**Corollary (finite-language closure reduction for unicyclic interactions).** Each local pair of edge-color functions \((f_i,g_i)\) belongs to an alphabet of \(16^2=256\) possibilities. The set of cyclic input words for which (50) holds is a regular language, recognized by the finite transfer system with cyclic boundary matching and nonconstant-orientation masks. Consequently the universal claim
\[
\forall n\ge3,\ \forall(f_i,g_i)_{i\in\mathbb Z_n},\
A_0(f)\cap A_1(g)\ne\varnothing
\tag{52}
\]
reduces to a finite automaton universality question. This is an **all-dimensional, finite-state proof target**, not an enumeration of a bounded set of cube dimensions. It is not asserted here that (52) is true or that its automaton universality has been decided. If proved, (52) combined with the previously established nonlinear pendant-tree elimination theorem would settle paired-root existence for every coloring whose undirected interaction graph is unicyclic, with arbitrary nonlinear pendant trees.

**Independent verification.** The orientation-CSP test was checked against an unrelated subset-reachability dynamic program for full nondecreasing and nonincreasing geodesics. All roots and both orientations were tested for 1000 random local colorings each at dimensions 3 and 4, 300 at dimension 5, and 60 at dimension 6; all results agreed. Exhaustive analysis of the 65536 possible four-direction local cycle colorings additionally gives, among those with all four cycle adjacencies present in the interaction graph, at least 12 favorable and at least 8 paired roots out of 16. This finite check is evidence only, and no all-dimensional favorable-density bound is inferred from it.

**Proof-closure significance.** The current arbitrary-cycle obstruction is not inherently factorial in the number of directions. It is represented by bounded-width local constraints, so a successful invariant of the transfer-state semigroup would establish the relevant universal intersection theorem in one argument for all cycle lengths. The next task is to find such an invariant or a counterexample to (52), not to extrapolate from small instances.

#### Rigidity of nonlinear colorings on a cyclic direction-interaction graph

Let n>=3 and suppose the color of an undirected cube edge in direction i is \(f_i(x)=F_i(x_{i-1},x_{i+1})\), cyclic subscripts, where every two-input Boolean function \(F_i\) is nonconstant. An affine parity site is one of the form \(F_i(a,b)=\epsilon_i+a+b\).

**Lemma (cycle input repair).** Fix target bit t attained by every local function. Write \(S_i=F_i^{-1}(t)\subseteq\mathbb F_2^2\), with an input pair's parity being the sum of its two bits.

(a) If one site i admits two target-t inputs with equal parity and a different site j admits target-t inputs of both parities, then a full monochromatic color-t antipodal geodesic exists.

(b) If three distinct sites admit target-t inputs of both parities, the same conclusion holds.

*Proof.* Choose a permitted local input pair \(a_i=(a_i^-,a_i^+)\) for every site. The previously established cycle-incidence theorem shows these inputs can be realized by a cube root and a cycle-edge orientation whenever
\[
\boxed{\sum_i(a_i^-+a_i^++1)=0\pmod2.}
\tag{A}
\]
Such an orientation produces a full monochromatic geodesic unless all cycle edges point consistently around the cycle, because every other orientation is acyclic and has a topological direction ordering.

For (a), take one of the two equal-parity permitted inputs at i and choose the parity at j so that (A) holds, keeping all other permitted inputs arbitrary. If its orientation is cyclic, replace the input at i by the other permitted pair, which differs in both bits. Equation (A) persists; the new root is obtained by toggling bit x_i alone, while the new orientation reverses precisely the two cycle edges incident with i. Therefore it cannot also be cyclic, and gives the required full monochromatic geodesic.

For (b), use one flexible site to satisfy (A). If the resulting orientation is cyclic, choose three flexible sites. At each, an allowed single-bit input change is available, because inputs of opposite parity on two bits differ in one bit. Each selected input bit reads the starting vertex bit at one of the site's two neighboring directions. Since a starting vertex bit has only two neighboring sites, two of our three sites admit allowed changes reading *different* starting bits. Make both selected input changes, preserving (A).

These two changed entries cannot result in another cyclic orientation. Indeed every cyclic incidence prescription can be written, possibly after complementing its root, as
\[
\boxed{a_i^-=x_{i-1}+1,\qquad a_i^+=x_{i+1}.}
\tag{B}
\]
Under (B), toggling one root bit changes precisely the two incident inputs that read **that same root bit**. Toggling two or more root bits changes at least four input entries, with no cancellations, because each entry reads just one root bit. Our altered prescription changes only two entries, and they read different root bits. Thus it cannot be cyclic. Its acyclic orientation gives a full monochromatic geodesic. QED.

**Theorem (nonaffine cycle rigidity).** If every \(F_i\) is nonconstant, and at least one of the \(F_i\) is **not** an affine parity site \(F_i(a,b)=\epsilon_i+a+b\), then the coloring has a full monochromatic dimension-simple antipodal geodesic.

*Proof.* Every nonconstant Boolean function on two bits is either (i) parity or its complement, (ii) one-bit projection or its complement, or (iii) nonlinear with a quadratic term. A parity site's target-t preimage has two inputs of one parity, for either t. A projection site's target-t preimage has one input of each parity, for either t. A nonlinear site's three-input majority-color preimage has both types of flexibility.

If a parity site and a non-parity site occur, choose a target for which the non-parity site is parity-flexible. Apply Lemma (a), with the parity site furnishing the equal-parity pair.

If no parity site occurs but both a projection and a nonlinear site occur, take the nonlinear site's majority color. It furnishes the equal-parity pair and the projection site is parity-flexible. If all sites are nonlinear, among n>=3 sites two have the same majority color; again apply Lemma (a). Finally, if all sites are projections, at least three sites are flexible for either target; apply Lemma (b). These cases exhaust all nonconstant local functions. QED.

**Corollary (paired-root theorem for nonconstant cyclic locality).** Every such coloring has a paired root. The only potential exceptions to monochromaticity are the pure affine neighbor-parity colorings \(f_i(x)=\epsilon_i+x_{i-1}+x_{i+1}\) for all i; those are already handled by the all-dimensional affine-cycle theorem in this subsection, which gives all roots paired for even n and all but two antipodal roots paired for odd n. Therefore
\[
\boxed{P(f)\ne\varnothing\quad\text{for every cyclic-local coloring with no constant direction function.}}
\]
A monochromatic full path qualifies for both \(0^*1^*\) and \(1^*0^*\), proving paired-root membership whenever the first theorem applies.

**Boundaries and next target.** This theorem does not assert the result for sites with constant local color functions, where one target color may be unattainable. It also does not provide a **cross-fiber** root intersection for two unrelated cyclic colorings, which is required to apply the existing pendant-tree elimination theorem to all unicyclic interaction graphs with attached trees. That cross-intersection remains the closure target. The published bounded-width orientation-transfer system gives an all-dimensional finite-state formulation of it.

**Independent test.** Exhaustive enumeration of all \(14^4=38416\) cyclic-local Q4 colorings with nonconstant local functions found only eight without a monochromatic full geodesic. All eight belong to the pure affine parity family and match its predicted obstruction. The proof above holds in every dimension and does not rely on this finite test.

##### Linear-time constructive paired roots on a nonconstant cyclic interaction graph

**Corollary (optimal constructive algorithm).** Under the hypotheses of the preceding nonlinear-cycle rigidity theorem, given the n local two-bit truth tables \(F_i\) of an arbitrary edge coloring with no constant direction function, a paired root and full monotone geodesic witnesses can be found in \(O(n)\) arithmetic operations.

*Proof.* Read each truth table and classify it as neighbor parity, one-input projection, or nonlinear. If all are neighbor parity, apply the constructive affine cycle orientation and root-classification algorithm already proved in this subsection; it performs a constant number of traversals around the cycle and constructs a root and two opposite monotone full paths.

Otherwise select target bit t and the permitted local incidence patterns using the case analysis in the preceding theorem. For the doubled-site case, choose local patterns with the required total parity; if the induced orientation is cyclic, change the two incidences at the doubled site and toggle the corresponding root bit. For the three-flexible-site case, if necessary change two permitted incidences reading different starting bits as in the parity-repair proof. Compute the root potential by propagating along the n equations \(x_i+x_{i+1}=1+a_{i,i+1}+a_{i+1,i}\); parity consistency ensures the closure equation. Orient the cycle edges according to the prescribed incidence patterns, and topologically order the resulting acyclic orientation using a queue of sources. Every stage requires only O(n) operations and yields a full monochromatic geodesic. A monochromatic path itself satisfies both monotone orientations and is therefore a paired-root witness.

Reading the n truth tables requires Omega(n), so the algorithm has optimal linear asymptotic complexity. This is a constructive **all-dimensional** theorem, not a fixed-dimension search or an average switch estimate.

The hypothesis that every local function is nonconstant is material. Extending the explicit construction to constant-color sites and, especially, to *two unrelated cyclic fiber colorings* is the remaining cross-intersection problem needed for the nonlinear pendant-tree 2-core reduction.


#### Unary-reader dependency cycles admit paired monochromatic roots

Let \(d\ge2\) and let every direction-\(i\) edge have color
\[
f_i(x)=x_{r(i)}+a_i\pmod2,
\qquad r(i)\ne i.
\]
The functional digraph \(i\mapsto r(i)\) has disjoint directed reader cycles of lengths \(\ell_1,\ldots,\ell_c\ge2\), with attached trees.

**Theorem (monochromatic reversal-paired roots).** The number of starting cube vertices \(z\) for which some full dimension ordering \(\pi\) yields a zero-colored full geodesic, and the reverse ordering \(\pi^R\) from the same \(z\) yields a one-colored full geodesic, is
\[
\boxed{2^d\prod_{\nu=1}^c\left(1-2^{1-\ell_\nu}\right)
\ge2^{d-c}>0.}
\]
In particular every such coloring has paired roots, with no bound on the number of directed cycles or the sizes of their attached trees.

*Proof.* On the direction-\(i\) step of an ordering \(\pi\), the color equals
\[
a_i+z_{r(i)}+
[\pi^{-1}(r(i))<\pi^{-1}(i)].
\]
For every step to have color zero, the ordering must realize one precedence relation for every reader arrow. These relations define an orientation of the undirected reader graph. Tree edges never create an orientation cycle. On a reader cycle of length \(\ell\ge3\), the precedence relations are inconsistent only when all arrows orient consistently clockwise or consistently counterclockwise. The root bits of the readers on that cycle independently control the individual precedences, so two of its \(2^\ell\) patterns are bad. For a reciprocal-reader two-cycle, the two precedence relations must agree on the order of those two dimensions; two of four root patterns work. Different reader cycles use disjoint controlling bits, and bits of their attached trees are unrestricted, giving the stated multiplicative count.

For a permitted starting root, take a topological sort of the precedence graph. This orders every direction once and makes each direction color zero. Reversing that order reverses the relative order of each dimension and its distinct reader, so every direction color becomes one along the reverse path from the *same* root. Thus the root supports both monotone orientations. The count bound uses \(\ell_\nu\ge2\). \(\square\)

**Corollary (all unary edge-local colorings).** If every direction-edge bit depends on at most one other input bit, the coloring has a paired root. Its undirected dependency components are either cyclic unary-reader components covered above or dependency trees terminating at constant-colored directions. The latter are covered by the unconditional nonlinear-tree paired-root theorem in this Subsection. The Cartesian factorization theorem combines the paired roots across components.

Thus any least-dimensional paired-root counterexample must have a direction whose edge-color function depends essentially on at least two other input bits. Cyclic dependence alone, even across many functional cycles, cannot obstruct closure.


##### Cyclic cross-fiber overlap theorem. Let f and g be binary edge colorings whose direction-i bits depend on the adjacent dimension bits. Suppose at each i at least two of the four possible neighboring-bit inputs make f_i=0 and g_i=1. Then some full antipodal geodesic has f-word 0*1* and g-word 1*0*. Proof: apply the established doubled/flexible incidence-repair lemma. Its exceptional case has allowed inputs forming fixed-parity antipodal pairs, with odd cyclic syndrome. The auxiliary affine cycle coloring h_i=p_i+x_(i-1)+x_(i+1) admits a full geodesic with h-word 0^(n-1)1 by the affine word-realization lemma. The first n-1 inputs meet both local requirements, making both original color words monotone. For three or more allowed pairs at every site, every prescribed dimension order has a starting root giving monochromatic f-zero and g-one paths, using composition of binary relations with at most one excluded pair.

**Affine word-realization lemma.** Write h_i(x)=p_i+x_(i-1)+x_(i+1), cyclic indices. If a prescribed bit b_i is desired as the traversed color in direction i and sum_i b_i=sum_i p_i+n modulo two, there exists a root and dimension order attaining all b_i with any chosen direction j last. To prove it, orient the cycle of dimension comparisons with u_i=1 if i is earlier than i+1. Require j to be a sink; this guarantees an acyclic orientation and a topological order ending in j. The parity of previously traversed neighbors at i is k_i=1+u_(i-1)+u_i. Let (Lx)_i=x_(i-1)+x_(i+1). The desired colors require Lx=p+b+k. For odd n, im(L) is the even-total-sum subspace, and the assumed parity equation ensures the right side lies there. For even n, im(L) requires zero sums on each cyclic parity class. In either class sum k_i=n/2+sum u_i modulo two. The assumed parity relation makes the two target sums equal, so one free u_i away from the edges fixed at the sink sets both to zero. Solve for x, then topologically sort the oriented cycle. In the exceptional overlap case set b_j=1 and all other b_i=0; the result gives a path with auxiliary word 0^(n-1)1.

**Proof of the doubled/flexible overlap dichotomy.** An allowed set D_i of two-bit neighbor inputs is doubled when it includes a complementary pair of the same input parity and flexible when it has allowed inputs of both parities. For a simultaneous monochromatic path, select one input per direction satisfying the cyclic incidence parity sum_i(1+a_i^-+a_i^+)=0 and a noncyclic orientation of the direction cycle. Distinct doubled and flexible sites permit parity correction at the flexible site. If the resulting orientation is cyclic, complement both bits at the doubled site. This keeps the incidence parity unchanged but reverses its two neighboring comparison edges, making the orientation acyclic. Any set of three permitted pairs is both doubled and flexible, so it can be combined with another site. If no doubled set occurs, each site is flexible; the earlier three-flexible-site repair lemma gives an acyclic input pattern. The sole remaining case is all allowed sets being size-two complementary pairs, with fixed input parities p_i. The incidence condition is then possible precisely if sum_i(1+p_i)=0. When the syndrome vanishes, complementing both inputs at one site removes a cyclic orientation. When it is nonzero, a simultaneous monochromatic path is impossible, but the affine one-defect lemma gives a simultaneous monotone path.

**Fixed-order three-input theorem proof.** For a fixed dimension order, the two neighbor bits seen at direction i differ from starting bits x_(i-1),x_(i+1) by flags determined by the order. Requiring membership in D_i therefore defines a binary relation on those two starting bits, containing at least three of four pairs. The constraint graph joins vertices i-1 and i+1, giving one cycle when n odd, two when n even, with parallel edges in the n=4 case. Such relations are closed under composition: a pair (a,c) can fail the composition only if the successor set of a and predecessor set of c are disjoint. In a relation omitting at most one pair, all but possibly one row or column have two possible entries, so the composition can omit at most one pair as well. Composing constraints around each cycle yields a relation containing at least three pairs, including some (t,t). Backtrack to assign each starting bit consistently along that cycle, and combine the assignments. All desired local simultaneous-success inputs are attained in the prescribed full order. The procedure is linear in n using constant-size relation tables. This theorem is stronger than merely finding a common root, but requires at least three permitted local inputs at every direction.

#### Punctured-cycle incidence and one-flexible-site cross-fiber closure

Let n>=3 and prescribe, for each direction i other than j, a two-bit input pair a_i=(a_i^-,a_i^+) recording the neighbor bits that the direction-i edge must see. There exists a root and a full dimension order with j last realizing every prescribed pair **if and only if** a_(j-1)^+=a_(j+1)^-. Necessity: since direction j is last, both of its neighbors see the original starting bit x_j, so their prescribed entries must agree. Sufficiency: orient the comparison cycle so that j is a sink, writing u_i=1 when direction i precedes i+1. Set x_j equal to the common prescribed bit. Along the path j+1,...,j-1, recursively solve x_i+x_(i+1)=1+a_i^++a_(i+1)^-. These equations always admit a solution because that path has no cycle. On each internal comparison edge define u_i=a_(i+1)^-+x_i. The orientation has j as a sink and is acyclic; a topological direction order ending at j realizes every prescribed neighbor input. This is an all-dimensional necessary-and-sufficient lemma.

**Corollary (one flexible site suffices).** For cyclic-local colorings f,g, let D_i be the neighboring-bit inputs producing f_i=0 and g_i=1. Assume every D_i is nonempty and at least one D_k contains two or more input pairs. Then some single full antipodal geodesic has f-word 0*1* and g-word 1*0*. Proof: Since D_k has at least two inputs, either its left-bit projection or its right-bit projection contains both zero and one. In the first case choose final direction j=k-1; in the second choose j=k+1. The other direction neighboring j has a nonempty local set, so choose a permitted pair there; the two-bit projection at site k can match its required starting bit x_j. Choose arbitrary permitted pairs at the other n-3 directions. The punctured-cycle incidence lemma realizes all the chosen inputs with j last. The first n-1 edges have f=0,g=1; the final edge may have either bit, yielding the required monotone words. If all D_i are singleton, the same result holds whenever there is at least one j for which the right bit of the input at j-1 equals the left bit at j+1. Hence the **only** remaining pattern not covered by this method has D_i={a_i} at every site and a_(j-1)^+ differing from a_(j+1)^- for every j. Exhaustive checks of dimensions 3 through 5 confirm the punctured-incidence criterion; the theorem itself is constructive and dimension-independent.

#### Odd-dimensional cyclic cross-fiber theorem under nonempty local overlap

Let f,g be cyclic-local colorings and D_i their local f-zero/g-one input sets. If every D_i is nonempty and n is odd, a common starting root exists for a nondecreasing f-geodesic and nonincreasing g-geodesic. Indeed one full geodesic can satisfy both.

*Proof.* The punctured-cycle theorem handles every case with a flexible D_i, and also singleton cases admitting a final direction j with a_(j-1)^+=a_(j+1)^-. The only remaining case has singleton inputs a_i=(l_i,r_i) with r_i=1+l_(i+2) everywhere. Put the reference root x_i=1+l_(i+1). For each cyclic rotation pi_j=(j,j+1,...,j-1) choose starting root y=x+e_(j-1). Direct substitution shows every direction except the final two j-2,j-1 sees its permitted input a_i; the final two see the permitted inputs with the right neighboring bit toggled. Consequently the first n-2 steps have paired colors (f,g)=(0,1), while the last two have values in the three-element set {(0,0),(1,1),(1,0)}. Order these values by increasing f and decreasing g. The only incomparable pair is (0,0) against (1,1). If no cyclic rotation gave a favorable path, every adjacent ordered pair of the last-two labels would have to be incomparable; thus the right-flip labels would alternate between (0,0) and (1,1) around the n-cycle. This cannot happen for odd n. Hence some rotation supplies a single geodesic monotone in both colorings. QED.

For even n, the same proof reduces the hard singleton case to an alternating right-flip label sequence. The reversed orientation yields a second alternating left-flip sequence. These alternating patterns are necessary for a counterexample, not sufficient. A full all-dimensional even-case proof is still open.

#### Full cyclic cross-fiber theorem under nonempty local overlap

Let f,g be two cyclic-local cube-edge colorings, and D_i the two-bit inputs where f_i=0 and g_i=1. **Theorem.** If every D_i is nonempty, then A_0(f) intersects A_1(g) for every n>=3. The paths may use different dimension orders. The theorem has no favorable-root density hypothesis.

Proof part I: If some D_i has two inputs, the punctured-cycle theorem supplies one common monotone full geodesic. If all D_i are singleton inputs a_i=(l_i,r_i) and some final direction j has r_(j-1)=l_(j+1), the same punctured-cycle theorem applies. Otherwise the mismatch equation r_i=1+l_(i+2) holds for all i. Set reference root x_i=1+l_(i+1). Every desired pair then has form a_i=(x_(i-1)+1,x_(i+1)), corresponding to the cyclic clockwise orientation of direction comparisons, which is the sole obstruction to using all desired inputs at once. For a cyclic order j,j+1,...,j-1, start instead at x+e_(j-1). Every edge except the final two sees its desired local input a_i; the last two directions j-2,j-1 see the pair obtained from a_i by flipping its right bit. Their f/g output pairs belong to {(0,0),(1,1),(1,0)}, with (0,1) occurring only at the desired input. A two-bit output pair is ordered by increasing f and decreasing g, with (0,1) least and (1,0) greatest. Thus unless every consecutive pair of right-flipped output labels is incomparable, one of these paths is favorable for both. Incomparability occurs only between (0,0) and (1,1), forcing those right-flipped labels to alternate around the entire cycle. This is impossible for odd n, proving the theorem in odd dimensions.

Proof part II (even n): Reverse the cyclic order of direction traversals, beginning at the complementary reference root (bar x)+e_(j+1). The same local incidence calculation gives all desired pairs except at the final two directions j+2,j+1, where the *left* input bit is flipped. If the left-flipped labels ever give a comparable consecutive pair in the output order, this again supplies one full path favorable in both colorings. Otherwise the left-flipped labels also alternate between (0,0) and (1,1). Since n is even, both right-flipped and left-flipped labels now have a constant value on each direction-parity class, with opposite values on opposite parity classes.

At the original reference root x, place all even-indexed directions before all odd-indexed directions. Each even direction is a source in the undirected interaction cycle, so its neighbor input is the left-flipped pair, and each odd direction is a sink, so its input is the right-flipped pair. The resulting f/g output word has two constant blocks, each either (0,0) or (1,1). Reverse the parity-block order: all odd directions before all even. Its first output block is the complement of the preceding first block, and its second is the complement of the preceding second block, because both left- and right-flipped labels alternate. Since (0,0) and (1,1) have equal first and second bits, one of these two orders has its f-bit nondecreasing, and one (possibly different) has its g-bit nonincreasing. Both full geodesics start at the SAME root x. Therefore x lies in A_0(f) intersect A_1(g), closing the even-dimensional case. The proof uses only local input patterns and the bipartition of an even cycle, not root-density estimates or case enumeration.

#### Even-cycle overlap can require two different full direction orders

The odd-dimensional nonempty-overlap theorem produces one order monotone in both colorings. In even dimensions that stronger objective has an all-dimensional obstruction, while the desired cross-root conclusion can hold at every root.

Let \(n\ge4\) be even. For neighboring bits \(a=x_{i-1},b=x_{i+1}\), put \(I(a,b)=a(1-b)\), and define
\[
\boxed{
\begin{array}{c|cc}
 &f_i&g_i\\ \hline
i\text{ even}&0&I(a,b)\\
i\text{ odd}&1-I(a,b)&1.
\end{array}}
\tag{EO1}
\]
These are ordinary undirected cube-edge colorings with cyclic-neighbor dependence. At every direction the simultaneous \(f=0,g=1\) input set is the singleton
\[
\boxed{D_i=\{(1,0)\}.}
\]
Both left-flip and right-flip labels alternate between \((0,0)\) at even directions and \((1,1)\) at odd directions, realizing the remaining pattern of the preceding even-case discussion.

**Theorem (all roots cross-favorable, no common monotone order).** For (EO1),
\[
\boxed{A_0(f)=A_1(g)=V(Q_n),}
\tag{EO2}
\]
while no starting root and no single full direction order give both an \(f\)-word \(0^*1^*\) and a \(g\)-word \(1^*0^*\).

*Proof of cross-favorability.* From any root, traverse all even directions first. Their \(f\)-colors are zero. Every odd direction then sees its final even-neighbor bits, independently of the order among odd directions. Traverse the odd directions of \(f\)-color zero and then those of color one. This gives a full nondecreasing \(f\)-path.

For \(g\), traverse all odd directions first, each of color one. The even direction colors are then independent of their relative order. Traverse the even directions of color one and then those of color zero. This gives a full nonincreasing \(g\)-path from the same prescribed root. Thus (EO2) holds.

*Proof of the common-order obstruction.* The only traversed color pairs are \((0,1)\), \((0,0)\), and \((1,1)\). Under the joint monotonicity requirement, \((0,1)\) precedes both other pairs, and \((0,0),(1,1)\) are incomparable. A successful pair word therefore cannot contain both incomparable values.

Suppose it contains no \((1,1)\). Every odd direction must then see input \((1,0)\). Each even direction is read with opposite requested bits by its two odd neighbors: its left odd neighbor requests zero and its right odd neighbor requests one. Since a bit is flipped once, the even direction must be traversed strictly between those two neighbors. If that even direction has pair \((0,0)\), its later odd neighbor has \((0,1)\), violating the nonincreasing \(g\)-word. Thus every even direction must also see input \((1,0)\).

If the pair word contains no \((0,0)\), reverse the parity classes. Every even direction sees \((1,0)\), every odd direction lies between its neighboring even directions, and any odd pair \((1,1)\) precedes a later \((0,1)\), violating the nondecreasing \(f\)-word. Again all directions must see \((1,0)\).

Finally, realizing \((1,0)\) at every direction would require every direction to be traversed between its two neighbors. The first direction in a total order cannot satisfy that condition. This rules out the common order. \(\square\)

**Closure consequence.** Nonempty local overlap supports the desired two-order cross-favorability problem beyond the single-order method. The theorem above supplies a sharp obstruction to extending the preceding odd-dimensional common-order theorem unchanged to all even dimensions. It simultaneously demonstrates that alternating left/right-flip labels can coexist with maximal cross-favorability. The preceding full cyclic nonempty-overlap theorem closes this case using two orders at one root, as the pendant-tree interface and the paired-root implication formula also permit. Earlier statements leaving the even nonempty-overlap case open are superseded by that theorem. General cyclic cross-favorability with empty local overlap sets remains unresolved.

Independent exhaustive checks in dimensions four and six confirmed the common-order obstruction for the displayed family. The proof above covers every even dimension at least four.


**Deficient-direction corollary (one missing local overlap).** Suppose a pair of cyclic-local colorings has a direction j with D_j empty, and every other D_i nonempty. Put R=the set of right-neighbor bits appearing in D_(j-1) and L=the set of left-neighbor bits appearing in D_(j+1). If R intersects L, then the cross-favorable root intersection is nonempty. More strongly, there is one full geodesic with j last for which all previous edges satisfy f=0 and g=1. Proof: choose compatible bits and permitted pairs at the two neighbors of j, choose arbitrary permitted pairs at every other direction, and apply the punctured-cycle incidence criterion. This also covers any local D_j of size zero or one when at least one of the two bordering permitted sets has the relevant bit projection equal to {0,1}. Any obstruction in the single-empty-site regime must therefore impose opposite fixed values of the starting bit x_j at the two adjacent sites. Those contradictory local prescriptions, rather than the absence of overlap at j by itself, are the structural defect to analyze next. The result is a direct corollary of the preceding all-dimensional incidence lemma.### One exceptional reversed-color site in cyclic cross-favorability

Let F_i,G_i be two binary cyclic-neighbor edge-color functions on Q_n, n>=4. Define D_i={(a,b):F_i(a,b)=0,G_i(a,b)=1} and E_i={(a,b):F_i(a,b)=1,G_i(a,b)=0}.

**Theorem.** If |D_i|>=3 for every i distinct from j, and D_j union E_j is nonempty, then there is ONE full dimension-simple path whose F-colors are nondecreasing and G-colors nonincreasing. If D_j is nonempty the path has respective constant words 0^n and 1^n. Otherwise it has 0^(n-1)1 and 1^(n-1)0.

*Proof.* Put direction j last, and at that step prescribe an input from D_j if available, otherwise E_j. This fixes the starting bits x_(j-1),x_(j+1), since both neighbor directions precede j. Every other site's requirement D_i becomes a binary relation R_i on starting bits x_(i-1),x_(i+1), with at most one forbidden pair. The incidence graph of these relations is one cycle for odd n, two parity cycles for even n. Removing R_j opens a path whose endpoints are the just-prescribed bits.

Two binary relations omitting at most one pair compose to the FULL relation when their omitted values on their shared bit agree. Indeed the only obstruction to an intermediate value is a pair of disjoint singleton permitted sets, which requires different omitted middle values. FULL composed with a relation omitting at most one pair is again FULL.

If n is odd and at least five, choose site relations j+1 and j+3, sharing starting bit x_(j+2). If n is even and at least six, choose j+2 and j+4, sharing x_(j+3). None of these three directions equals j. By placing the shared direction before or after each of its two neighboring site directions, independently, ensure that their forbidden shared-bit values agree (or use that a relation is already full). This is compatible with j last. The two relations compose to FULL; further composition with the other at-least-three-pair relations leaves the whole opened path FULL. Any specified endpoint pair is therefore realizable. In the even case the remaining parity cycle has only at-least-three-pair relations; its composition contains a diagonal pair, so it too is satisfiable.

At n=4 the opened component has only site j+2. Its two neighbor directions can be placed independently before or after that site while j remains last, moving a possible forbidden pair to any of four starting-bit values. Avoid the prescribed endpoint pair. The other parity component consists of two at-least-three-pair relations on the same two bits, so their intersection is nonempty.

These choices give a root and total direction order realizing pair (F_i,G_i)=(0,1) at all i other than j, and at j either (0,1) or (1,0). Thus both ordered color words have the claimed monotonicities. QED.

The result extends the previously established nonempty-overlap theorem to one site with *empty* D_j, provided its reverse-color set E_j is nonempty and all other sites have three permitted joint inputs. Binary relation propagation constructs the witness in O(n) time.

#### Terminal-block incidence realization on a cyclic direction graph

Let f,g be cyclic-neighbor cube edge colorings on Q_n, n>=3. Let B be a consecutive interval of m directions in the cyclic direction graph, with 2<=m<n; let A be its nonempty complementary path. For each i in A prescribe an arbitrary two-bit neighbor input a_i=(a_i^-,a_i^+). Then there exists a cube starting root and a total order of all n directions such that every A direction is traversed before every B direction and sees its prescribed input a_i. The order within B is arbitrary. This is a structural incidence theorem and imposes NO restrictions on the prescribed inputs.

Proof. For each internal edge (i,i+1) of the A path, impose the binary equation x_i+x_(i+1)=1+a_i^++a_(i+1)^-. Because A is a path these equations have two solutions differing by complementing all A bits. Fix either one, and orient each internal A edge so that u_i=a_(i+1)^-+x_i is the bit indicating i is traversed before i+1. With that orientation, the local neighbor bit read at each end of the internal edge agrees with the prescribed values. Choose any topological order of this oriented path. Its two endpoints abut distinct B directions because B has at least two consecutive members. Since every B direction is traversed after A, its bit is not yet toggled when read by the adjacent endpoint of A. Choose the two boundary B starting bits equal to the respective prescribed endpoint input bits. The remaining m-2 B starting bits may be chosen freely. Append all B directions after the A topological order. Every A direction reads its desired two neighbor inputs. QED.

Corollary (many compatible-prefix roots). If each i in A has at least one neighbor input where f_i=0 and g_i=1, then there are at least 2^(m-1) distinct starting roots supporting full geodesics whose first n-m edge pairs all equal (f_i,g_i)=(0,1), with the m consecutive B directions last. This follows by fixing allowed a_i and an internal A orientation, choosing either of the two A-root solutions and freely choosing the m-2 interior B bits.

For a terminal block B of size two, the remaining question is a finite two-step interface: among the two possible orders of the last two directions and the two compatible-prefix starting roots, does one order yield a sequence of f/g output pairs that is nondecreasing under the partial order (a,b)<=(c,d) iff a<=c and b>=d? If so the same full path is favorable in f and g. Failure of this two-edge test is not asserted to imply cross-root failure, since different orders in f and g can still succeed. The lemma avoids path-family complexity by localizing all failure to the terminal interval. It does not prove unrestricted cyclic cross-favorability.


##### Simultaneous incidence parity and the three signed leaf ports

Let \(f,g\) be arbitrary binary edge colorings of \(Q_d\), and let \(G\) be the union of their undirected direction-interaction graphs. At every directed incidence \((i,j)\) of \(G\), prescribe two bits \(a_{ij},b_{ij}\), interpreted as the bit of \(j\) observed when the first and second full paths traverse \(i\). Put
\[
u_i=f_i((a_{ij})_{j\in N_G(i)}),\qquad
v_i=g_i((b_{ij})_{j\in N_G(i)}).
\]
All additions of incidence bits are modulo two.

**Theorem (simultaneous incidence realization).** These prescribed inputs are realized by two dimension-simple full geodesics from one common root, with the first \(f\)-color word nondecreasing and the second \(g\)-color word nonincreasing, if and only if the following conditions hold:

(i) Every edge \(ij\) satisfies
\[
\boxed{a_{ij}+b_{ij}=a_{ji}+b_{ji}.}\tag{SI1}
\]
(ii) With \(\lambda_{ij}=1+a_{ij}+a_{ji}=1+b_{ij}+b_{ji}\), every cycle \(C\) of \(G\) has \(\sum_{ij\in E(C)}\lambda_{ij}=0\). Equivalently, a potential \(x\) exists with \(x_i+x_j=\lambda_{ij}\) for every edge.
(iii) For at least one such potential, orient \(j\to i\) in \(O_f\) when \(a_{ij}+x_j=1\), and in \(O_g\) when \(b_{ij}+x_j=1\). Both orientations are acyclic. Every \(j\to i\) in \(O_f\) has \(u_j\le u_i\); every \(j\to i\) in \(O_g\) has \(v_j\ge v_i\).

*Proof.* Along two paths from a common root \(x\), the incidence equations are
\[
a_{ij}=x_j+[\text{\(j\) precedes \(i\) in the first order}],\qquad
b_{ij}=x_j+[\text{\(j\) precedes \(i\) in the second order}].
\]
On every edge, one end precedes the other in each order. Comparing the two equations at both ends proves (SI1), and adding either path's equations on an edge gives \(x_i+x_j=\lambda_{ij}\). The orders supply the acyclic orientations and monotone color inequalities.

Conversely the cycle conditions supply \(x\). For an edge \(ij\),
\[
(a_{ij}+x_j)+(a_{ji}+x_i)=1,
\]
and likewise for \(b\); therefore the orientation prescriptions choose one direction per edge. Since \(O_f\) is acyclic and contains no arrow from a color-one direction to a color-zero direction, topologically order its color-zero vertices and then its color-one vertices. For \(O_g\) topologically order the color-one vertices and then the color-zero vertices. Both total orders recover the incidence assignments from \(x\), so they yield the required full paths. \(\square\)

For an interaction forest, the cycle condition and the acyclicity tests are automatic. Condition (SI1) provides the shared parity constraint on each edge. The possible potentials form two complementary choices per connected nontrivial tree, and free starting bits at isolated directions. The color-order tests thus depend on one global binary sign per tree component, after the local incidence data are selected.

**Lemma (signed leaf-port classification).** Let \(w\) be a leaf of \(G\) with neighbor \(v\). Fix the common starting bit \(x_v=s\) and two *candidate* traversal colors \(U,V\) at \(v\). Consider the leaf-edge comparison constraints before imposing the equations defining the traversal colors at \(v\). Write \(p=0\) for traversing \(w\) before \(v\) and \(p=1\) for traversing \(v\) before \(w\). The allowable choices are
\[
B_f=\{0:f_w(s)\le U\}\cup\{1:U\le f_w(1-s)\},
\]
\[
B_g=\{0:g_w(s)\ge V\}\cup\{1:V\ge g_w(1-s)\}.\tag{SI2}
\]
Both sets are nonempty. If \(r_f,r_g\) denote the bits of \(w\) observed at the two traversals of \(v\), then, as its **common** initial bit \(x_w\) varies, the relation allowed by these leaf-edge comparisons, **before testing the parent-color equations**, is one of
\[
\boxed{\{00,11\},\qquad \{01,10\},\qquad \{00,01,10,11\}.}\tag{SI3}
\]
The diagonal relation occurs if all pairs in \(B_f\times B_g\) have equal precedences, the antidiagonal if all have unequal precedences, and the full relation if both types occur.

*Proof.* The first set is nonempty because \(U=1\) always permits \(p=0\), while \(U=0\) always permits \(p=1\). Likewise \(V=0\) always permits \(p=0\), while \(V=1\) always permits \(p=1\) in the second set. For \(p_f\in B_f,p_g\in B_g\),
\[
r_f=x_w+1-p_f,\qquad r_g=x_w+1-p_g.
\]
Hence \(r_f+r_g=p_f+p_g\), and the two choices of \(x_w\) realize both pairs of the permitted parity. Taking the union over allowed precedences gives precisely (SI3). \(\square\)

All three cases occur on a two-direction tree with constant colors at \(v\). For the diagonal, choose \((U,V)=(1,0)\) and \(f_w=0,g_w=1\). For the antidiagonal, choose \((U,V)=(1,1)\) and \(f_w=g_w=0\). For the full relation, take \(s=0,(U,V)=(1,0)\) and \(f_w(x_v)=x_v,\ g_w(x_v)=1-x_v\).

**Consequence for induction.** When the two paths belong to unrelated colorings, deleting a leaf must retain whether its two observations at the parent agree, disagree, or are unrestricted, together with the parent root bit and traversal colors. Replacing all leaf interfaces by opposite-bit observations loses admissible pairs already in dimension two. The unconditional opposite-bit interface for two paths in a *single* coloring uses the common-coloring hypothesis essentially. The parity relation (SI1) and the three-way relation (SI3), subsequently intersected with the parent-local color equations, describe the boundary information needed by a simultaneous-root induction on trees.


##### One-direction completion gives a 2-SAT paired-root obstruction

Fix an edge coloring \(B\) of every direction of \(Q_d\) except one direction \(i\). Let \(X_e\) be the freely assigned color of each direction-\(i\) edge. Every full dimension-simple path \(P\) uses just one such edge \(e(P)\). Thus the requirement that its color word be nondecreasing or nonincreasing, denoted \(L_\uparrow(P)\) or \(L_\downarrow(P)\), is either false, true, \(X_{e(P)}=0\), or \(X_{e(P)}=1\).

**Theorem 1 (Boolean face of one-sided avoidance).** For any root set \(R\) and a chosen monotone orientation \(\sigma\), the completions \(X\) for which no root of \(R\) supports an orientation-\(\sigma\) full geodesic form either an empty family or one Boolean face: some variables are forced and all others are free. The face is empty precisely when a single full path works for both values of its variable or two full paths from roots of \(R\) cross the same direction-\(i\) edge and require opposite color values.

*Proof.* Avoidance is the conjunction of negations of the unary predicates \(L_\sigma(P)\) over all rooted full paths \(P\) from \(R\). These impose only one-variable conditions, so only the stated two inconsistencies can arise. QED.

**Theorem 2 (paired-root failure is 2-SAT).** The direction-\(i\) completions having no paired root in \(R\) are the solutions of
\[
\boxed{\Phi_{B,R}(X)=
\bigwedge_{r\in R}\ 
\bigwedge_{P,Q\text{ full from }r}
\left(\neg L_\uparrow(P)\lor\neg L_\downarrow(Q)\right).}
\tag{1}
\]
After simplification every clause contains at most two Boolean tests on individual variables. Hence the counterexample-completion family is a 2-CNF solution set, and is closed under ternary bitwise majority.

*Proof.* A root \(r\) is paired if and only if some nondecreasing path \(P\) and nonincreasing path \(Q\) from \(r\) both succeed. The clause forbids their simultaneous success. Each success test has at most one adjustable variable. Majority closure follows because if a ternary majority falsified a two-test clause, at least one of the three inputs would falsify both tests. QED.

**Corollary 3 (two-path universal restoration).** Fix a completed coloring \(g\) extending \(B\), and set \(R=A_\uparrow(g)\). Every second completion \(h\) satisfies \(A_\uparrow(g)\cap A_\downarrow(h)\ne\varnothing\) if and only if there is a nonincreasing full path from a root of \(R\) working for either value of its adjustable edge, or two paths from roots of \(R\) cross the same adjustable edge and require its two opposing values.

*Proof.* By Theorem 1, the family of completions avoiding all nonincreasing paths from \(R\) is empty precisely under the stated one- or two-path condition. QED.

**Example 4 (the root must adapt).** On \(Q_3\), take \(f_0(x)=x_2\) and \(f_1(x)=1-x_2\), with direction-2 edge colors free. No single root has a nonincreasing full path under every completion; nevertheless the nondecreasing favorable-root set is all eight vertices when direction-2 colors are zero. Two full paths rooted at \(000\) and \(001\) impose opposing conditions on the direction-2 edge based at \(000\), yielding the universal two-path restoration certificate.

**Independent check.** All 256 choices of outside coloring in three dimensions were enumerated. For every such choice the 2-CNF formula with all eight roots was unsatisfiable, confirming the published small-dimensional paired-root result through an independent implication-graph calculation.

**Closure perspective.** Through the universal bridge equivalence, the unresolved NORI1 conjecture reduces to proving that every full-root formula \(\Phi_{B,V(Q_d)}\) is unsatisfiable. This asks for a contradictory implication cycle derived from square exchanges and root reversal. The reduction is valid in all dimensions, but its universal unsatisfiability is not established.### Shared-site four-bit 2-SAT kernel

Fix edge colors of two cube colorings f,g outside one direction j. Require the j-edge colors in both to be the same four-entry local Boolean function H(x_(j-1),x_(j+1)). Then the sixteen candidate functions H giving disjoint root sets A0(f) and A1(g) are the satisfying assignments of a Boolean formula with clauses of width at most two, on the four entries of H.

*Proof.* Every full dimension-simple path uses one j-edge. With other colors fixed, success in a chosen monotone orientation is either always true, always false, or requires one chosen truth-table bit of H to have value zero or one. To forbid a pair of successful paths from the same root, conjoin the disjunction of their two negated success conditions. These are two-clause conditions on four variables. There are at most eight unit clauses and twenty-four clauses on distinct variable pairs, so 32 nontrivial clause types suffice. QED.

**Fourteen-pair certificate.** If no H gives disjoint cross-root sets, the failure formula is unsatisfiable. Its implication digraph has eight signed variable states. A variable and its negation lie in one strongly connected component, so two simple directed paths connecting them, with at most seven edges each, give a contradiction. Each implication edge originates in one rooted pair of full geodesics. Thus at most fourteen rooted path pairs suffice to certify all sixteen cases of H simultaneously.

**Four pairs can be necessary.** In Q5 with j=0, fix outside cyclic-local truth tables f_1..f_4=(5,0,5,12) and g_1..g_4=(10,15,10,3). Full-path enumeration produces twenty different nonempty pair-success patterns, each covering four of the sixteen H. Four path pairs cover all choices and no three do.

The shared-even-site theorem rules out H=0,6,9,15 as possible failures for cycle-local outside colorings. The remaining projection and unbalanced nonlinear cases are therefore a fixed four-variable implication-graph closure problem, independent of cycle dimension.

##### Eliminating all pendant trees while preserving paired-root certificates

Let \(f\) be an arbitrary binary coloring of the undirected edges of \(Q_d\), and let \(G(f)\) be its undirected direction-interaction graph. Let \(H\) be the **2-core** of \(G(f)\), obtained by iteratively deleting vertices of degree at most one. Every component of the deleted subgraph belonging to a connected component with nonempty 2-core is a tree joined to the core by a single edge. Thus the noncore directions form independent rooted pendant trees attached at core directions.

For each core direction \(v\in V(H)\), its edge-color function \(f_v\) depends on its neighboring core bits and on the bits of the immediately attached noncore children. Define two induced core colorings \(g^0,g^1\) by
\[
\boxed{
g^s_v(z)=f_v\bigl((z_w)_{w\in N_H(v)},\,
                  (s)_{w\in N_G(v)\setminus V(H)}\bigr),
\quad s\in\{0,1\}.
}
\tag{1}
\]
The bit of the traversed direction \(v\) is omitted, as it must be for an undirected cube-edge coloring. The two induced colorings are unrelated in general.

**Theorem 1 (nonlinear pendant-tree elimination).** Suppose \(G(f)\) is connected and its 2-core \(H\) is nonempty. Then
\[
\boxed{|P(f)|\ge |A_0(g^0)\cap A_1(g^1)|.}
\tag{2}
\]
Every root of the intersection on the right can be lifted constructively to a paired root of the full coloring, using the universal opposite-bit subtree-interface lemma of the preceding nonlinear-tree Subsection. If \(H\) is empty, \(G(f)\) is a tree and the unconditional tree theorem already gives at least two paired roots.

*Proof.* Choose a core root \(z\in A_0(g^0)\cap A_1(g^1)\). Let \(P_0,P_1\) be full dimension-simple core geodesics starting at \(z\), with color words \(0^*1^*\) in \(g^0\) and \(1^*0^*\) in \(g^1\). Their core direction orders may differ. For every core vertex \(v\), denote its prescribed traversal colors in the two paths by \(U_v,V_v\), and its common starting bit by \(z_v\).

Apply the universal opposite-bit subtree-interface lemma independently to each pendant branch rooted at a noncore neighbor \(w\) of \(v\). Give the branch parent starting bit \(z_v\), parent colors \((U_v,V_v)\), and prescribe that the parent sees bit \(w\) equal to zero in the first path and one in the second. The lemma supplies common initial bits for the entire branch and two sets of edge orientations, compatible with the required nondecreasing and nonincreasing color comparisons across every branch edge. Different branches have disjoint direction sets and may be constructed independently.

To form each full direction order, retain the selected order of all core directions as a directed chain, and adjoin the oriented edges of all pendant trees. This union is acyclic: each attached tree meets the core chain at one vertex. Moreover all its earlier-to-later edge comparisons respect the required monotone colors, because the core chain was already color sorted and every attached edge is by the interface lemma. Hence one can choose a topological order listing all color-zero directions before color-one directions in the first mode, and the reverse in the second. These topological orders retain the original relative core orders, so each core direction reads its core-neighbor bits as in \(P_0,P_1\). Each attached neighbor bit observed at a core traversal has the prescribed value zero or one, so its core edge color is \(g^0_v\) or \(g^1_v\), as required. The pendant direction colors agree with their inductively constructed interfaces. The two resulting full paths begin at the same root assignment, use each dimension once, and have opposite monotone words. Distinct core roots give distinct full roots. QED.

**Corollary 2 (nonlinear unicyclic triangles in all dimensions).** If a connected interaction graph has a triangle as its 2-core, with arbitrary attached trees, then
\[
\boxed{|P(f)|\ge4.}
\tag{3}
\]
Indeed every arbitrary three-dimensional edge coloring has at least six nondecreasing and six nonincreasing favorable roots, so any two such colorings have at least four roots in their cross-orientation intersection. No restriction is imposed on the nonlinear local functions along the triangle or trees. In particular a minimum counterexample cannot have a triangular unicyclic interaction graph.

**Corollary 3 (2-core order at most four).** If a connected interaction graph has nonempty 2-core on at most three dimensions, it has paired roots by Corollary 2 and the \(\kappa_m\) bounds. With the separately recorded computer-assisted four-cube minimum favorable-root count \(m_4=9\), the same conclusion holds for any 2-core on four dimensions, with at least two paired roots. The order-four part depends on the finite optimization certificate; the order-three result is analytic.

**Corollary 4 (large cores with cross-favorable induced colorings).** Let the 2-core have \(m\) dimensions. If both \(g^0,g^1\) have star interaction graphs (their hubs may differ), then
\[
\boxed{|P(f)|\ge 2^{m-1}.}
\tag{4}
\]
If \(m=2r\) and both induced core colorings factor into arbitrarily colored squares along possibly different perfect matchings \(M,N\), then
\[
\boxed{|P(f)|\ge2^{c(M,N)}\ge2.}
\tag{5}
\]
These follow by applying the existing all-dimensional cross-star and crossed-matching intersection theorems to (2). Thus arbitrarily large feedback cores can be favorable despite nonlinear attached trees and changing square decompositions.

**Corollary 5 (forest and multiple-component extension).** If the whole interaction graph has connected components \(G_1,\ldots,G_s\), apply the unconditional tree theorem to each acyclic component and Theorem 1 to each cyclic component, then multiply paired-root counts using Cartesian factorization. In particular, for an interaction forest with \(s\) components the lower bound is \(2^s\), with no target-admissibility assumption.

**Corollary 6 (NORI1 with eliminable interaction cores).** Every antipodally odd coloring of \(Q_{d+1}\) whose lower facet satisfies a positive cross-intersection hypothesis from Theorem 1 or its corollaries admits monochromatic full antipodal geodesics, for arbitrary odd vertical bridge colors. The number of directed geodesics distinguished by their vertical crossing edge is at least the paired-root lower bound in the corresponding corollary, by the universal free-bridge equivalence.

**Independent reconstruction check.** A separate implementation generated arbitrary nonlinear color functions on interaction graphs whose 2-core was a triangle with randomly attached trees, in dimensions \(4,6,9,12,15\). For 80 independent cases per dimension it selected cross-favorable core paths, reconstructed both full paths using the subtree-interface recursion, and evaluated every original cube-edge color along the two geodesics. All 400 tests produced a common root and monotone full words.

**Closure perspective.** The earlier monochromatic-tree argument failed because of opposing constant-colored directions. The opposite-bit interface succeeds despite them. Therefore every pendant tree may be pruned without losing the paired-root objective, at the cost of replacing its core by two induced colorings \(g^0,g^1\). The remaining unrestricted obstruction lives in the 2-core cross-favorability problem. On a unicyclic graph this becomes a problem about two independent colorings of the cycle, a significantly smaller and geometrically constrained target than arbitrary colorings of the full high-dimensional cube.### Exhaustive cross-favorability for four- and five-cycle cores

Consider arbitrary binary edge colorings on \(Q_m\) with cyclic-neighbor dependence,
\[
f_i(x)=F_i(x_{i-1},x_{i+1}),\qquad F_i:\{0,1\}^2\to\{0,1\},
\]
with cyclic indices. Each of the \(m\) local truth tables has four free bits, so there are \(2^{4m}\) such colorings, including cases with inactive interaction edges. Write \(A_0(f)\) for roots admitting a full nondecreasing geodesic and \(A_1(f)=\overline{A_0(f)}\).

**Theorem 1 (finite computer-assisted census).** Exhaustive enumeration yields
\[
\begin{array}{c|r|r|r|r}
m&\text{colorings}&\text{distinct }A_0\text{ masks}&
\min_f|A_0(f)|&\min_{f,g}|A_0(f)\cap A_1(g)|\\
4&65,536&193&9&2\\
5&1,048,576&2,723&18&6.
\end{array}
\tag{1}
\]
In particular two arbitrary cyclic-neighbor colorings of either \(Q_4\) or \(Q_5\) have common roots for opposite monotone path orientations.

*Reproducible enumeration.* Encode the four truth-table bits \(F_i(0,0),F_i(0,1),F_i(1,0),F_i(1,1)\) in positions \(4i,\ldots,4i+3\), with direction zero least significant. For every integer code \(c\) from zero to \(2^{4m}-1\), run through all roots \(r\in\{0,1\}^m\) and all \(m!\) permutations of the directions. At each step \(i\), read \(F_i\) on the two neighbor bits at the current cube vertex, then toggle bit \(i\). Mark root \(r\) favorable if at least one such word is nondecreasing, thereby producing a \(2^m\)-bit root mask \(M_c\). Deduplicate all masks. The nonincreasing root mask of any coloring is its antipodal translate, obtained by replacing root index \(r\) with \(r\oplus(2^m-1)\). Minimize the population count of the bitwise intersection of \(M_c\) with that antipodal translate over all pairs of *distinct masks*, also including equality pairs. This deterministic finite algorithm gives the entries in (1); a separate direct evaluator independently checked the equality witnesses.

For \(m=5\), equality for the last column is attained at the two truth-table codes
\[
c=0{\rm x}53ad3,\qquad c'=0{\rm x}c5a35,
\]
whose nondecreasing root masks are respectively \(0{\rm x}f0ffa0aa\) and \(0{\rm x}eeee00ee\), each with 18 favorable roots. The cross-orientation intersection is the six roots \(1,5,13,28,29,30\). For \(m=4\), the two root masks \(0{\rm x}eee0\), \(0{\rm x}fca8\) give cross-orientation intersection \(\{5,10\}\).

**Corollary 2 (unicyclic closure up to pentagonal cores).** Let the undirected interaction graph of an arbitrary binary edge coloring be connected and unicyclic, with its unique cycle of length \(m\in\{3,4,5\}\). Arbitrary nonlinear trees may be attached to the cycle. Then the coloring has paired roots. Lower bounds on their number are 4, 2, and 6 for \(m=3,4,5\), respectively.

*Proof.* The preceding pendant-tree elimination theorem lifts each root in \(A_0(g^0)\cap A_1(g^1)\) to a paired root of the full coloring. The induced core colorings \(g^0,g^1\) have cyclic-neighbor dependence, so apply Theorem 1 when \(m=4,5\); for \(m=3\), use the analytic three-dimensional cross-root bound of four. QED.

The universal free-bridge theorem consequently establishes NORI1 for any antipodally odd coloring whose chosen lower facet has one of these interaction graphs; the number of distinct directed monochromatic geodesics is at least the same paired-root bound.

**Closure boundary.** At order six, the product of three colored squares has just \(27\) favorable roots among \(64\), so a purely cardinality-based cross-intersection proof no longer applies. The crossed-square theorem still gives two common roots for two shifted matching products. Arbitrary cycle-local colorings in dimension six and higher remain unresolved; an additional compatibility mechanism is required.### Square templates, alternating constraint paths, and a potential cycle closure

For a matching \(M\) of the cube direction set, covering all but at most one direction, choose a forbidden bit pair \(q_{ij}\in\{0,1\}^2\) for every edge \(ij\in M\). The corresponding **square template** is
\[
T(M,q)=\{x:(x_i,x_j)\ne q_{ij}\text{ for every }ij\in M\}.
\tag{5}
\]
It contains \(3^{\lfloor d/2\rfloor}2^{d\bmod2}\) roots. Taking antipodes of every root produces another template with the same matching.

**Lemma 3 (sharp path constraint bound).** If a path on \(p\ge1\) Boolean variables has one constraint on each neighboring pair, forbidding at most one of the four possible pairs, then it has at least \(p+1\) satisfying assignments.

*Proof.* For one vertex there are two choices. When a new endpoint is appended, each old satisfying assignment extends at least once. At least one old assignment ends with the bit that permits *both* values of the new endpoint: construct it backward greedily from that desired terminal bit, avoiding the sole forbidden pair at each earlier edge. Thus every extension adds at least one to the solution count. Induction gives \(p+1\). Equality is attained by forbidding \(10\) at every step, leaving just the \(p+1\) nondecreasing words. QED.

**Theorem 4 (matching-template intersection).** Given two matchings \(M,N\), each leaving at most one unmatched direction, the union multigraph consists of alternating paths and even cycles, with parallel-edge cycles allowed. If its path components have \(p_1,\ldots,p_s\) vertices and there are \(c\) cycle components, then for arbitrary forbidden bit pairs,
\[
\boxed{|T(M,q)\cap T(N,q')|
\ge2^c\prod_{\nu=1}^s(p_\nu+1)>0.}
\tag{6}
\]
The path estimate is Lemma 3; every binary constraint cycle has at least two solutions by the crossed-square Subsection. Independence of the components gives their product. QED.

**Corollary 5 (sharp odd-cycle bound).** On the odd cycle \(C_d\), \(d=2r+1\), restrict \(M,N\) to adjacent almost-perfect matchings, each missing one vertex. Then
\[
\boxed{|T(M,q)\cap T(N,q')|\ge d+1.}
\tag{7}
\]
The bound is sharp. For an even cycle, adjacent perfect matching templates always intersect in at least two roots, and this is sharp.

*Proof.* The union of the odd-cycle matchings contains one alternating path with odd vertex count \(p\) and \(k=(d-p)/2\) parallel-edge cycles. Formula (6) gives \((p+1)2^k\ge d+1\), since \(2^k\ge k+1\) and \(p\ge1\). Choose matchings with a spanning alternating path and forbid \(10\) along that path to attain \(d+1\) solutions. For an even cycle choose the two distinct adjacent perfect matchings; their union is one even cycle. Forbid \(00\) on one matching and \(11\) on the other to leave precisely the two alternating bit strings. QED.

**Corollary 6 (root-template sufficient criterion).** If the nondecreasing favorable-root sets \(A_0(f),A_0(g)\) of two arbitrary cube colorings each contain a square template, then
\[
\boxed{A_0(f)\cap A_1(g)\ne\varnothing.}
\tag{8}
\]
Indeed \(A_1(g)=\overline{A_0(g)}\) contains the antipodal translate of its template, and Theorem 4 supplies a common root.

The open statement that would complete the **unicyclic interaction-graph case** is:

**Square-template containment conjecture (open).** For every chordless cycle \(C_d\), \(d\ge4\), and arbitrary binary local edge-color functions \(f_i(x)=F_i(x_{i-1},x_{i+1})\), the set \(A_0(f)\) contains a template from *some* matching of the \(d\) directions. The matching may include nonadjacent pairs.

If proved, Corollary 6 would show cross-favorability for every pair of cyclic-neighbor colorings, and pendant-tree elimination would resolve every unicyclic interaction graph with arbitrary nonlinear attachments. For odd cycle order an even stronger version may hold with an adjacent almost-perfect matching. The complete \(C_4,C_5\) enumerations verify containment in these dimensions, and the odd-cycle matching bound explains their cross-intersection minima 2 and 6. Additional sampling found suitable matchings in 100,000 \(C_6\) cases, 25,000 \(C_7\) cases, 10,000 perturbed \(C_8\) cases and 1,000 perturbed \(C_9\) cases. This is evidence, not a general proof.

**Nonadjacent pairs cannot be excluded.** A coloring with all six cyclic-neighbor interactions active, encoded by its six four-bit local truth tables as hexadecimal \(0{\rm x}ca83ad\), has favorable-root mask \(0{\rm x}cfcfcfcfcfcf\). It contains no template built from either neighboring-direction perfect matching of the six-cycle. It does contain a template for the nonlocal matching \(\{(0,3),(1,2),(4,5)\}\), with forbidden two-bit values \((0,1,3)\). Independent direct path enumeration verified this mask.

**The conjecture must remain restricted to chordless cycles of order at least four.** In the odd three-cycle parity coloring \(f_i(x)=x_{i-1}+x_{i+1}\) the unfavorable roots are \(000,111\). Multiply by a one-dimensional factor of constant edge color. Its unfavorable set in four dimensions becomes \(\{000,111\}\times\{0,1\}\). No two forbidden square faces on disjoint matched direction pairs can cover these four roots: a face fixing the fourth bit covers at most one, and a face fixing two of the first three bits covers at most two. Thus the favorable set has 12 roots but contains no square template. This interaction graph is a triangle plus an isolated direction and has maximum degree two, showing that the proposed containment is not an unrestricted low-degree theorem.

The remaining problem is the template-containment conjecture, not compatibility of templates. Its proof would turn the cycle's nonlinear path constraints into a system of forbidden binary pairs whose union graph has maximum degree two.

#### Unicyclic NORI1 closure from local opposite-fiber overlap

Let F be a binary cube-edge coloring whose undirected direction-interaction graph is connected and unicyclic. The cycle H consists of m directions, and the other directions form rooted pendant trees. Define induced core colorings g0,g1 by assigning every pendant-child bit zero or one respectively when evaluating a core-direction color. Assume that for every cycle direction i some pair of its two cyclic neighbor bits yields g0_i=0 and g1_i=1. Thus each local simultaneous-success set D_i is nonempty.

**Theorem.** Under this condition, F has an antipodally paired root. By the established free-bridge correspondence, the one-higher-dimensional antipodally odd NORI1 instance has a monochromatic full antipodal geodesic.

*Proof.* The all-dimensional cyclic cross-fiber theorem in the nonlinear tree-incidence subsection supplies z in A0(g0) intersect A1(g1), possibly using two different cycle direction orders. The previously proved pendant-tree interface theorem lifts those two monotone core paths to two full monotone geodesics from one cube root, establishing P(F) nonempty. Apply the free-bridge equivalence. The attached trees and their nonlinear color functions have unrestricted depth and size, subject only to the interaction graph and local crossing condition. This is a new all-dimensional sufficient closure class, not the unrestricted unicyclic assertion.### Adaptive polarization closes responsive unicyclic interactions

Let a connected direction-interaction graph have unique cycle C_n, n>=3, with arbitrary pendant trees. At a cycle direction i, denote by L_i its immediate attached children and write its arbitrary local edge-color function as F_i(a,b;y), where a,b are the neighboring cycle bits and y is the L_i-bit vector.

Call i **antipodally responsive** if there exists y_i such that F_i(.;y_i) and F_i(.;complement(y_i)) differ at some cycle-neighbor input (a,b).

**Theorem.** If every cycle direction is antipodally responsive through its pendant children, then the full cube-edge coloring has a paired root, without any restrictions on the nonlinear color functions elsewhere in the pendant trees.

*Proof.* Choose for every cycle site i one y_i for which the two opposite attachment slices differ. If at some input their values are (0,1), retain y_i for the nondecreasing witness and its complement for the nonincreasing witness. If their values are (1,0), swap those choices. Distinct cycle sites have disjoint pendant branches, so all polarities can be chosen independently. This gives two induced cyclic-neighbor colorings g0,g1 on the same C_n satisfying, at every site i, at least one input with g0_i=0 and g1_i=1.

Apply the previously established all-dimensional cyclic nonempty-overlap theorem in the nonlinear-tree incidence Subsection: any pair of cyclic-neighbor colorings satisfying this local overlap has a common root supporting a nondecreasing full g0-geodesic and a nonincreasing full g1-geodesic, possibly with distinct dimension orders. Record the resulting core traversal colors U_i,V_i.

At each pendant child w of site i prescribe its observed bit at traversal of i to equal y_i(w) in the first path and its complement in the second. The unconditional opposite-bit subtree interface theorem supplies common starting bits and two oriented traversal trees compatible with parent colors U_i,V_i. Attach these separately to the two core orders. Since every pendant tree meets the core at one site, the joined precedence graphs remain acyclic, and sorting their two color phases gives two full dimension-simple geodesics from the same root with words 0*1* and 1*0*. The resulting root is paired. QED.

**Corollary (responsive sun graphs).** If every cycle direction i has a single pendant leaf w_i and its edge-color function depends nontrivially on bit w_i at some cycle-neighbor input, then the theorem applies. Arbitrary further trees may be attached below these leaves. The free-bridge equivalence therefore proves NORI1 for antipodally odd extensions of all these facets, with unrestricted odd bridge colors.

**Induction lesson.** The appropriate interface carried by the pendant-tree proof is an adaptively selected opposite-bit polarization, rather than a fixed square template. The remaining cycle sites for this method are those whose attachment-complement slices coincide for every attached-bit assignment; they require the terminal-defect or checkerboard analysis.

#### Full unicyclic closure with a jointly constant core direction

Consider an arbitrary binary cube-edge coloring F whose undirected direction-interaction graph has a unique cycle H and arbitrary rooted pendant trees. Define the two induced cycle colorings g0,g1 by assigning all attached child bits zero or one in the manner of the established pendant-tree interface theorem. Suppose some cycle direction j has a constant color in g0 AND a constant color in g1, with the two constants allowed to differ. Then the original coloring F has an antipodally paired root. Indeed, fixing bit j leaves a pair of path-local colorings; by the new 66-core finite induction theorem in the subsection universal_path_local_cross_favorability_66_core_finite_induction, any such pair has a common root for an f-nondecreasing and a g-nonincreasing full path. Insert direction j first or last in either path according to the two constant colors, using the appropriate fixed-bit fibers. This gives A0(g0) intersection A1(g1) nonempty. The published nonlinear pendant-tree interface theorem lifts the two monotone core paths to full monotone paths with one common original root. Under the free-bridge equivalence, the associated antipodally odd one-higher-dimensional NORI1 instance has a monochromatic full geodesic.

All four pairs of constant core colors are covered: (0,1) prepend j to both paths; (1,0) append j to both; (0,0) prepend to the nondecreasing path and append to the nonincreasing path; (1,1) do the reverse. No opposite-color local-overlap assumption is required, and all attached tree color functions may be nonlinear. The path theorem is computer-assisted through an independently checked 66-mask inductive invariant. This result is an all-dimensional sufficient closure class, not the unrestricted unicyclic theorem.

##### Shared-site cyclic cross-favorability is sufficient for all unicyclic interaction graphs

For a unicyclic direction-interaction graph with arbitrary pendant trees, write the edge color of a core direction \(i\) as \(F_i(a,b;y)\), with \(a,b\) its two cycle-neighbor bits and \(y\) the immediate attached-child bits.

Call a site *responsive* when some complementary choices \(y,\bar y\) produce distinct two-input functions \(F_i(\cdot;y)\ne F_i(\cdot;\bar y)\). Call it *nonresponsive* otherwise.

**Reduction theorem.** The following proposed statement is sufficient to establish paired-root existence for every binary coloring with a unicyclic interaction graph:

> Any pair of arbitrary cyclic-neighbor colorings \(g,h\) whose local functions agree at at least one cycle direction satisfies \(A_0(g)\cap A_1(h)\ne\varnothing\).

*Proof of sufficiency.* If every core site is responsive, the adaptive pendant-polarization theorem in this Subsection already constructs two conditional cycle colorings with a common local \((0,1)\) input at every site. The established cyclic nonempty-overlap theorem then supplies compatible core geodesics and the opposite-bit interfaces restore all pendant trees.

Otherwise choose a nonresponsive site \(j\). By definition, for every attached-bit assignment \(y_j\), the two conditional functions \(F_j(\cdot;y_j)\) and \(F_j(\cdot;\bar y_j)\) agree on all four cycle-neighbor inputs. Choose arbitrary complementary polarizations at the other core sites. The two conditional cycle colorings therefore share their entire direction-\(j\) truth table. The proposed shared-site statement supplies a common opposite-orientation core root; the pendant-tree interface restores its two full geodesics. Hence the full coloring has a paired root. QED.

**Proved constant-site case.** If at the shared site \(j\) both conditional local functions are constants (possibly different), the new 66-state path cross-favorability theorem already supplies the needed core intersection. Therefore any unresolved unicyclic example under this reduction must have at least one nonresponsive core site whose common local two-input function is **nonconstant**.

**Focused remaining cases.** Nonconstant binary functions on two inputs fall into the one-input projection/complement class, the neighbor-parity/complement class, and the eight unbalanced nonlinear truth-table types. Proving the shared-site cross statement for these classes would close every unicyclic interaction coloring in all dimensions, with arbitrary nonlinear attached trees, without requiring unrestricted cross-favorability for every pair of unrelated cyclic colorings.

This is a sufficient proof target, not a claim that the shared-site statement is established.

#### Unicyclic paired-root closure with independently functional induced core colorings

Let F color cube edges with a unicyclic undirected direction-interaction graph and arbitrary nonlinear rooted pendant trees. Denote its two induced cycle colorings by g0,g1, obtained by fixing every immediately attached noncore child bit to zero or one respectively. Suppose that at every cycle direction each of the two induced local edge-color functions depends on at most one of its two cyclic-neighbor bits; the controlling neighbor may be different for g0 and g1, and constant functions are permitted.

**Theorem.** Under these hypotheses F has at least two paired roots. Indeed g0 and g1 are unrelated functional-dependency colorings. By the Hall cross-root theorem and its sharp two-root strengthening, |A0(g0) intersect A1(g1)|>=2. The already proved pendant-tree interface lifts each different core root to a different paired root of F. By the free-bridge equivalence, the corresponding next-dimensional antipodally odd NORI1 coloring has monochromatic antipodal geodesics. This allows arbitrary nonlinear functions on all pendant trees; only the two induced core-local functions are restricted. The result does not require nonempty local opposite-color overlap or a jointly constant core direction.

#### Unicyclic paired-root closure with one acyclic-facet conditional core

Let F be any binary cube-edge coloring whose undirected direction-interaction graph has one cycle H with arbitrary nonlinear rooted pendant trees. Let g0,g1 be the two induced cycle-core colorings obtained by assigning the immediate pendant-child bits zero or one in the established nonlinear pendant-tree interface theorem. The previously established cyclic-local single-coloring theorem guarantees P(g0) and P(g1) nonempty.

**Theorem.** If either induced core coloring, say g0, has a cycle direction h such that its two fixed-h facet colorings have acyclic directed dependencies, then F has a paired root; likewise if g1 has such a direction. Indeed the new monochromatic confluence theorem says A0(g0) contains a full starting half-cube on one h-bit value. Since P(g1) is antipodally closed and nonempty, one root of an antipodal pair in P(g1) lies in that half-cube. Hence A0(g0) intersect A1(g1) is nonempty. If g1 is the acyclic-facet core instead, use the full half-cube in A1(g1) and a paired antipodal pair in P(g0). In either case the nonlinear pendant-tree interface lifts the common core root to a paired root of F, and the free-bridge equivalence supplies the associated NORI1 monochromatic full antipodal geodesic.

This sufficient all-dimensional closure hypothesis is distinct from a jointly constant core direction, functional core rules, or nonempty local opposite-color input sets. Only ONE of the two conditional core colorings needs an acyclic-facet direction; the other may have arbitrary cyclic-local nonlinear rules. Tree depth, branching, and internal Boolean edge-color functions are unrestricted.

##### Bipartite block-order synchronization of two arbitrary cube colorings

Let \(f,g\) be arbitrary binary edge colorings of \(Q_d\). Suppose the union of their undirected direction-interaction graphs is bipartite with a common partition \([d]=U\sqcup V\). Therefore each \(U\)-direction edge color depends only on the starting \(V\)-bits, and each \(V\)-direction color depends only on the starting \(U\)-bits. Neither coloring is assumed affine or antipodally odd.

Write a starting vertex as \((a,b)\in Q_U\times Q_V\), and let \(\bar a,\bar b\) denote bitwise complements within those blocks. Define four Boolean feasibility predicates:
\[
\begin{aligned}
A(b)&:\ f_u(b)=0\quad\text{for all }u\in U,\\
B(a)&:\ f_v(\bar a)=1\quad\text{for all }v\in V,\\
C(a)&:\ g_v(a)=1\quad\text{for all }v\in V,\\
D(b)&:\ g_u(\bar b)=0\quad\text{for all }u\in U.
\end{aligned}
\tag{1}
\]
Here \(f_u(b)\) means the color of a direction-\(u\) edge at any vertex whose \(V\)-bits equal \(b\). Define the solution sets of these four predicates by the same capital letters.

**Theorem 1 (two opposite block orders).** A root \((a,b)\) admits a nondecreasing full \(f\)-geodesic with all \(U\)-steps before all \(V\)-steps, and a nonincreasing full \(g\)-geodesic with all \(V\)-steps before all \(U\)-steps, if and only if
\[
\boxed{(A(b)\lor B(a))\ \land\ (C(a)\lor D(b)).}
\tag{2}
\]
Consequently, such a common root exists if and only if at least one of the following four conditions holds:
\[
\boxed{
(A\ne\varnothing\land C\ne\varnothing)
\ \lor\ (A\cap D\ne\varnothing)
\ \lor\ (B\cap C\ne\varnothing)
\ \lor\ (B\ne\varnothing\land D\ne\varnothing).
}
\tag{3}
\]
If \(N\) denotes the number of roots supplied by this pair of block-order strategies, then
\[
\boxed{N\ge\max\{
|A||C|,\quad 2^{|U|}|A\cap D|,
\quad2^{|V|}|B\cap C|,\quad |B||D|
\}.}
\tag{4}
\]

*Proof.* In an \(f\)-path taking all \(U\) directions first, every \(U\)-edge color is determined by the unchanged \(V\)-bits \(b\), regardless of the order of the \(U\)-steps. We can sort these first-block colors increasingly. Afterwards the \(U\)-bits have all toggled to \(\bar a\). Every \(V\)-edge color is then determined by \(\bar a\), and can again be sorted increasingly. The concatenated word is nondecreasing precisely when no color-one first-block edge precedes a color-zero second-block edge, equivalently all first-block colors are zero or all second-block colors are one. This is \(A(b)\lor B(a)\).

The \(g\)-path taking \(V\) first and \(U\) second behaves dually. Sort each block decreasingly. The complete word is nonincreasing precisely when the first block is entirely one or the second block entirely zero, giving \(C(a)\lor D(b)\). Both paths start at \((a,b)\) and use every direction once. Expanding the conjunction of the two disjunctions yields four sufficient alternatives. Their free variables separate into the \(a\) and \(b\) blocks, proving both the nonemptiness criterion (3) and the four cardinality lower bounds (4). QED.

**Theorem 2 (linear-time checkerboard transfer for two even-cycle colorings).** Suppose \(d=2r\ge4\) and the union interaction graph is contained in the direction cycle \(C_{2r}\). Choose \(U\) to be the even directions and \(V\) the odd directions. Nonemptiness of each of the six sets
\[
A,\quad B,\quad C,\quad D,\quad A\cap D,\quad B\cap C
\tag{5}
\]
can be decided using a product of \(2\times2\) Boolean relations around one \(r\)-variable cycle. Hence the criterion (3) and a witnessing common root, whenever it holds, are computable in \(O(d)\) operations from the local four-bit truth tables.

*Proof.* For example \(A\) requires \(f_i(b_{i-1},b_{i+1})=0\) at each even \(i\). The participating variables are precisely the odd starting bits, and successive constraints join consecutive odd variables around their parity cycle. Each local truth table therefore gives a binary relation \(R_i\subseteq\{0,1\}^2\). There exists a cyclic assignment satisfying all these relations if and only if their Boolean relation product has a diagonal entry, equivalently nonzero Boolean trace. The same construction applies to \(B,C,D\), with appropriate complements of their variables. For \(A\cap D\), the local relation at even site \(i\) is the conjunction \(f_i(b_{i-1},b_{i+1})=0\) and \(g_i(1-b_{i-1},1-b_{i+1})=0\); for \(B\cap C\), make the analogous conjunction at odd sites. Each is still an arbitrary four-pair binary relation. Products of \(2\times2\) Boolean matrices and backtracking a successful two-state cycle take linear time. The case \(r=2\) simply has a two-edge parallel constraint cycle and is covered by the same product. QED.

**Corollary 3 (a no-overlap sufficient condition).** In the even-cycle setting, suppose every even-direction local function of \(f\) has at least three of four neighbor inputs giving color zero, and every odd-direction local function of \(g\) has at least three inputs giving color one. Then \(A,C\) are both nonempty and the two colorings have a common opposite-orientation root. The same conclusion holds with even and odd interchanged.

*Proof.* The binary relations for each of \(A,C\) omit at most one of their four possible pairs. Their cyclic Boolean composition also omits at most one pair, hence contains a diagonal pair. Apply Theorem 1. QED.

**Example 4 (all local simultaneous-opposite sets may be empty).** Let \(d\ge4\) be even, and set \(f=g\), with \(f_i(x)=x_{i+1}\) for every cyclic direction \(i\). Then the local sets \(\{(a,b):f_i(a,b)=0,\ g_i(a,b)=1\}\) are all empty. Nevertheless take a root whose even bits are one and odd bits zero. In the \(f\)-path with even directions first, all traversed edges have color zero. In the \(g\)-path with odd directions first, all edges have color one. Both are full dimension-simple antipodal geodesics from the same root. Thus Theorem 1 supplies compatibility unavailable to a method that requires shared opposite-color local inputs at every site.

**Proof-closure use.** The current unrestricted even-cycle cross-favorability question would be solved if one could prove that either these checkerboard conditions, or a bounded set of exchange repairs starting from them, succeeds for every pair of cyclic-local colorings. Theorem 2 isolates the failure of the two block-order strategies in a constant-size Boolean relation algebra, allowing explicit obstruction certificates for those strategies. It does not assert that the block orders suffice for every cyclic coloring: independent six-direction tests find pairs with compatible full paths but neither checkerboard strategy succeeds. The theorem instead supplies a second all-dimensional forcing mechanism orthogonal to the existing local-overlap and pendant-tree interface arguments.

##### A universal terminal-defect repair with one reversed local color pair

Let \(n\ge3\). Let \(f,g\) be arbitrary cyclic-neighbor edge colorings of \(Q_n\), with
\[
f_i(x)=F_i(x_{i-1},x_{i+1}),\quad
g_i(x)=G_i(x_{i-1},x_{i+1})
\tag{1}
\]
and cyclic indices. Write
\[
D_i=\{(a,b): F_i(a,b)=0,\ G_i(a,b)=1\},\quad
E_i=\{(a,b): F_i(a,b)=1,\ G_i(a,b)=0\}.
\tag{2}
\]
Call a binary relation \(R\subseteq\{0,1\}^2\) **bi-surjective** if both of its projections onto \(\{0,1\}\) are surjective. Equivalently it is a complementary-pair relation \(\{00,11\}\) or \(\{01,10\}\), or contains at least three pairs.

**Lemma 1 (complementary input flip).** If \(R\) is bi-surjective, complementing one argument gives another relation \(R'\) with
\[
\boxed{R\cup R'=\{0,1\}^2.}
\tag{3}
\]
A composition of bi-surjective relations is again bi-surjective. In particular, whenever \(P,S\) are bi-surjective,
\[
\boxed{(P\circ R\circ S)\ \cup\
(P\circ R'\circ S)
=P\circ\{0,1\}^2\circ S
=\{0,1\}^2.}
\tag{4}
\]
*Proof.* Fix the argument that is not complemented. Surjectivity onto this argument guarantees at least one value of the other argument is permitted. Flipping that other argument permits the remaining value as well, proving (3). For a composition, each input has some intermediate continuation and every output has some incoming intermediate predecessor; this proves both projections are surjective. A full relation composed on either side with a bi-surjective relation stays full, giving (4). QED.

**Theorem 2 (bi-surjective terminal-defect cross-favorability).** Suppose some direction \(j\) has \(E_j\ne\varnothing\), and for every other direction \(i\ne j\) the relation \(D_i\) is bi-surjective. Then the two colorings share a starting root and a **single** full dimension-simple antipodal geodesic with respective color words
\[
\boxed{
f(P)=0^{n-2}\,\alpha\,1,\qquad
g(P)=1^{n-2}\,\beta\,0
\quad\text{for some }\alpha,\beta\in\{0,1\}.}
\tag{5}
\]
In particular \(A_0(f)\cap A_1(g)\ne\varnothing\). This holds for every \(n\ge3\), without any affine or oddness assumptions and without requiring three permitted local pairs.

*Proof.* Choose a neighbor input in \(E_j\), which requires color pair \((1,0)\) at direction \(j\). Place \(j\) last in the full direction order and some other direction \(k\) penultimate. At every earlier direction require color pair \((0,1)\), by choosing its local neighbor input in \(D_i\). Direction \(k\) is left unrestricted. Any pair of bit colors \((\alpha,\beta)\) at \(k\) is between \((0,1)\) and \((1,0)\) under the order making the first component increase and the second decrease, so these requirements produce (5).

It remains to realize all local neighbor inputs along one direction order and one starting root. Fix a tentative direction order \(\pi\). Every \(D_i\) requirement for \(i\ne j,k\) becomes a bi-surjective relation \(R_i^\pi\) on the two starting bits \(x_{i-1},x_{i+1}\); complementing one or both arguments according to the earlier steps preserves bi-surjectivity. Since \(j\) is last, its prescribed neighbor input fixes the starting pair \((x_{j-1},x_{j+1})\). The graph of the relations \(R_i^\pi\) on the starting bits has one cycle when \(n\) is odd, or two parity cycles when \(n\) is even, prior to deleting the unconstrained relations at \(j,k\).

If \(n\) is odd, choose any \(k\ne j\) penultimate. Removing relations at \(j,k\) splits the single root-bit cycle into two paths, one containing each of the two fixed bits at the endpoints of the removed \(j\)-edge. Along either path, bi-surjectivity allows an assignment to be propagated from that fixed endpoint through every relation, regardless of whether its arguments are read forward or backward. The two assignments combine, giving the desired root.

If \(n\) is even, take \(k=j+1\pmod n\) penultimate, put \(a=j+2\) and \(b=j+3\), and put \(a,b\) consecutively somewhere before \(k,j\). Consider two orders \(\pi,\pi'\), identical except that \(a,b\) are swapped. The sites \(a,b\) are adjacent on the interaction cycle and have opposite parities. Consequently the swap changes the observed bit \(x_b\) in the local relation \(R_a\), while leaving every other relation in the parity component containing site \(j\) unchanged. Let \(R_a'\) denote the changed relation; it is obtained from \(R_a\) by complementing the argument associated with \(x_b\).

Removing site \(j\) from its parity component opens a path between the fixed starting bits \(x_{j-1},x_{j+1}\). For orders \(\pi,\pi'\), its endpoint feasibility relations can be written
\[
P\circ R_a\circ S,\qquad P\circ R_a'\circ S,
\tag{6}
\]
where \(P,S\) are compositions of other bi-surjective relations and are themselves bi-surjective (empty products are identities, also bi-surjective). By Lemma 1, the **union** of the two endpoint relations is full. Therefore the prescribed pair at \(j\) is feasible under at least one of the two orders. In the *other* parity component, removal of the penultimate site \(k\) also opens a path. Its relations are all bi-surjective and its starting bits are unprescribed, so it can always be solved. The two parity components involve disjoint starting bits and their assignments combine.

Thus in either parity of \(n\) there is a full direction order and a common root satisfying all the chosen local pair requirements. The first \(n-2\) direction steps have pair \((0,1)\), the penultimate step has arbitrary pair \((\alpha,\beta)\), and the last step has pair \((1,0)\). The color words (5) follow, and both are monotone. QED.

**Corollary 3 (locally sparse overlap is sufficient).** In every dimension, the theorem permits each nonexceptional \(D_i\) to have just two of the four local neighbor inputs, provided these are the complementary assignments \(00,11\) or \(01,10\). This improves the preceding three-of-four single-exception repair. If instead \(D_j\ne\varnothing\), the earlier all-sites-nonempty cyclic overlap theorem supplies cross-favorability. Thus when all other \(D_i\) are bi-surjective, either a nonempty \(D_j\) or a nonempty \(E_j\) guarantees the desired common root.

**Constructive certificate and audit.** For odd \(n\), one prescribed order and two binary path propagations suffice. For even \(n\), try the two orders related by the adjacent transposition \(a,b\) and propagate binary path constraints for each. This produces the root and both monotone color words in \(O(n)\) operations given local four-entry truth tables. The proposed two-order construction was independently evaluated on 1,500 random cyclic-local pairs in dimensions three through eight; each computed root and full order yielded the color words (5).

**Closure role.** When one conditional core-coloring site lacks a simultaneous opposite-color input but admits the reversed input, an arbitrary large cyclic consistency obstruction can be eliminated using **one unrestricted penultimate direction**. The even-dimensional step is a local adjacent exchange whose two possibilities cover every endpoint assignment. Remaining potential obstructions must involve multiple deficient sites, locally one-sided \(D_i\) relations (both permitted pairs in one row or column), or sites where the conditional local functions agree everywhere. These are narrower targets than unrestricted cyclic locality and retain dimension-simpleness throughout.

#### One arbitrary deficient direction: sharpened terminal exchange theorem

For cyclic-neighbor cube colorings f,g, let \(D_i=\{(a,b):f_i(a,b)=0,\ g_i(a,b)=1\}\). Call a binary relation *bi-surjective* when each of its two projections onto \(\{0,1\}\) is surjective.

**Theorem (one arbitrary defect).** If every \(D_i\), except possibly \(D_j\), is bi-surjective, there is a full dimension-simple antipodal geodesic traversing direction j last whose first n−1 edges all have the joint color pair (f,g)=(0,1). Hence \(f(P)=0^{n-1}*\) and \(g(P)=1^{n-1}*\), so both have the requested monotonicity. Direction j has **no local restriction**: \(D_j,E_j\) may both be empty.

*Proof.* Fix a dimension order ending in j. Every requirement \(D_i\) for i≠j becomes a bi-surjective binary relation \(R_i\) between starting bits \(x_{i-1},x_{i+1}\); the chosen order complements zero, one, or both input bits but preserves bi-surjectivity. The starting-bit constraint graph connects indices at distance two on the cyclic direction graph.

For odd n this is one cycle, with the relation at j removed. The remaining path of bi-surjective relations is always satisfiable by propagating from one endpoint. Thus every order with j last works in odd dimension.

For even n there are two independent parity cycles. Removing R_j opens one into a path; the other remains a cycle and may have inconsistent parity in a fixed order. Choose cyclically adjacent directions \(a=j+2\) and \(b=j+3\), all subscripts modulo n. Put a,b consecutively before j, and compare the two total orders obtained by swapping a and b. On the intact parity cycle, the only altered relation is \(R_b\): its new version \(R_b'\) is obtained by flipping the input associated with starting bit \(x_a\). The other altered relation is R_a, which lies on the opened path and causes no obstruction.

For any bi-surjective relation R on two bits, R together with its one-input-flipped relation R' covers all four input pairs. Composition of bi-surjective relations preserves bi-surjectivity. If P and S compose the remaining relations in the intact parity cycle, then
\[
(P\circ R_b\circ S)\cup(P\circ R_b'\circ S)
=P\circ\mathbb F_2^2\circ S=\mathbb F_2^2.
\]
At least one ordering therefore yields a cyclic composition admitting an equal initial and terminal bit. That cycle has a satisfying assignment. The opened path has one independently, and the two parity classes are disjoint, so their assignments combine. Every earlier edge then has pair (0,1).

Because (0,1) is the minimum of the four joint color pairs under the order in which f increases and g decreases, the final edge can have any pair and the resulting whole path is monotone in both senses. QED.

**Audit of scope.** The preceding terminal-defect result required \(E_j\ne\varnothing\) and used a free penultimate step. Neither is necessary. The tempting stronger statement that every prescribed order ending at j works is **false for even n**: a cycle of disequality relations has no fixed point when their number is odd. The proof above uses one adjacent transposition to repair that obstruction. This theorem is dimension-independent. Remaining induction targets: two exceptional sites and local relations that are nonempty but one-sided rather than bi-surjective.

#### Two exceptional sites: one arbitrary and one merely nonempty

Retain the cyclic-local colorings f,g, opposite-color success relations \(D_i=\{(a,b):f_i(a,b)=0,\ g_i(a,b)=1\}\), and the definition of bi-surjective binary relations.

**Theorem (two-defect terminal repair).** Fix distinct cyclic directions j and k. Suppose \(D_j\) is completely arbitrary, \(D_k\ne\varnothing\), and \(D_i\) is bi-surjective for every \(i\notin\{j,k\}\). Then there is a full antipodal dimension-simple geodesic with j last and the joint pair (f,g)=(0,1) on every earlier edge. Thus \(A_0(f)\cap A_1(g)\ne\varnothing\). This holds for every n≥3, allowing \(D_k\) to be a singleton and allowing \(D_j\) to be empty.

**Relation lemma.** Let R be any nonempty binary relation on \(\mathbb F_2\), and let R' be obtained by flipping one of its two input bits. The union \(R\cup R'\) contains a complete row or a complete column. Let P,S be bi-surjective relations, or empty compositions interpreted as identity relations. Then
\[
\boxed{(P\circ R\circ S)\cup(P\circ R'\circ S)}
\]
contains at least one diagonal pair.

*Proof.* Choose any (a,b) in R. Flipping the second argument puts both (a,0),(a,1) in the union; flipping the first argument puts both (0,b),(1,b) there. If a row is full, the surjectivity of the right projection of P provides an initial bit x linked by P to its row index; surjectivity of the right projection of S supplies a continuation to output x. If a column is full, choose any final bit y reachable from the column index through S; surjectivity of the left projection of P supplies a preceding path from y. Either case yields a diagonal pair. \(\square\)

*Proof of the theorem.* Fix a direction ordering with j last. Each local \(D_i\) for i≠j becomes a binary relation \(R_i\) on start bits \(x_{i-1},x_{i+1}\), transformed by possible input flips prescribed by the ordering. Bi-surjectivity and nonemptiness are invariant under these flips.

For odd n, removing R_j from the sole cyclic relation graph leaves a path with one nonempty relation R_k and every other relation bi-surjective. Such a path is satisfiable: choose any pair in R_k, then propagate backward and forward through the bi-surjective relations. Hence any order with j last works.

For even n, the relation graph has two disjoint parity cycles; removing R_j opens one into a path, while the other remains a cycle.

If k lies in the opened path, that path is satisfiable by the preceding propagation argument. The intact cycle has all relations bi-surjective. Choose adjacent cyclic directions a=j+2 and b=j+3 and place them consecutively before j. Exchanging a,b flips one argument of the intact relation R_b (b has parity opposite j), while changing only R_a in the opened path. By the full-union property of a bi-surjective relation, one of the two orders admits a satisfying cyclic assignment. The opened path is satisfiable for either order independently.

If k lies in the intact cycle, the opened path consists solely of bi-surjective relations and is satisfiable. Choose one of the two neighbors a of k on the direction cycle with a≠j (possible for n≥4). Put k,a consecutively before j and compare their two orders. The exchange flips one argument of R_k, changing only R_a in the opened path. Write the intact cycle's composite in the two orders as P∘R_k∘S and P∘R_k'∘S, where P,S compose the remaining bi-surjective relations. By the relation lemma, at least one composite has a diagonal pair; thus the intact cycle is satisfiable in at least one order. The opened path remains satisfiable.

In all cases, the two disjoint relation components supply a common starting root realizing (0,1) at every nonfinal direction. The final direction j can have any joint color pair and preserves the nondecreasing f-word and nonincreasing g-word. \(\square\)

**Inductive significance.** This settles one fully arbitrary deficient direction **and** one additional direction whose overlap may be singleton, with all remaining directions bi-surjective. The next induction frontier is to handle two or more additional one-sided relations on the same remaining relation path or cycle. The argument uses a single local adjacent transposition and a complete-row/column completion property; it is independent of dimension and avoids averaging or path-family enumeration.

For every n>=3, let j be a cyclic direction, a=j+1, b=j-1. Define two cyclic-local edge colorings by f_j=g_j=0, f_a=x_j, g_a=1+x_j, f_b=1+x_j, g_b=x_j, and for all other directions f_i=0, g_i=1. Then D_j is empty, D_a and D_b prescribe opposite initial j bits, and all other D_i are full. Every starting root is simultaneously favorable for the two separate orientations: if x_j=0, f admits order (j,b,others,a) with word 0^(n-1)1, while g admits order (others,a,b,j) with word 1^(n-2)00; if x_j=1, interchange a and b. But there is NO single order that works for both. Its joint pair in direction j is always (0,0), between (0,1) and (1,0) in the order where f increases and g decreases. The a,b pairs before j are (0,1) and (1,0); crossing j interchanges them. Therefore any order has either a maximal (1,0) before j or a minimal (0,1) after j, which violates joint monotonicity. This proves that induction on deficient directions must preserve two potentially different orders from a common root, not require a common order. Valid in all dimensions and not a counterexample to cross-root existence.

##### The two-defect theorem is a corollary of the earlier punctured-cycle endpoint criterion

The terminal-direction lemma in the nonlinear tree-incidence subsection says that arbitrary nonempty success relations D_i at every i other than j can be realized by some dimension order ending in j if and only if the right-bit projection of D_(j-1) intersects the left-bit projection of D_(j+1). Both neighbors read the unchanged starting bit x_j, proving necessity. The path of remaining incidence equations admits a topological order and root whenever that one endpoint condition holds, proving sufficiency.

This criterion already implies the one-arbitrary-defect and two-defect theorems of this subsection: if the other success relations are all bi-surjective then both boundary projections are full; if only one additional D_k is nonempty and all the rest bi-surjective, at most one boundary projection can be proper, so the projections intersect. The longer adjacent-exchange arguments give alternate constructions, but no new hypothesis is needed for these corollaries.

The unresolved induction case starts where both neighbors of j require opposite values of starting bit x_j. The separate-orders gadget of this subsection shows that such a mismatch can obstruct a common monotone dimension order while still permitting two favorable orders from every root. Thus a further induction must retain two witness orders from one root, rather than a single shared order.

#### Constant deficient direction: conditional induction from cyclic to path interaction

Let f,g be arbitrary binary edge colorings on Q_n whose direction-i edge colors depend only on the two cyclically adjacent direction bits. Fix direction j and assume its color is the SAME CONSTANT c∈{0,1} in both colorings:
\[
\boxed{f_j=g_j=c.}
\]
Delete j to form the path of the other n−1 directions. For b∈{0,1}, denote the induced path-local fiber colorings by \(f^{(b)},g^{(b)}\), obtained by fixing initial bit x_j=b.

**Proposition (opposite-fiber extreme insertion).** If c=0 and for some b
\[
\boxed{A_0(f^{(1-b)})\cap A_1(g^{(b)})\ne\varnothing,}
\]
then \(A_0(f)\cap A_1(g)\ne\varnothing\). If c=1, the analogous sufficient condition is
\[
\boxed{A_0(f^{(b)})\cap A_1(g^{(1-b)})\ne\varnothing.}
\]

*Proof.* In the first case choose a common lower-dimensional root z. Start both full paths at (z,b). For f, traverse direction j FIRST (color zero), then follow a favorable full f^(1-b) geodesic from z. Its whole word is \(0\,0^*1^*\). For g, first follow a favorable full g^b path from z, and traverse j LAST (color zero); its word is \(1^*0^*0\). In the second case c=1, traverse j LAST in the f path, and FIRST in the g path, using the respective indicated fiber colorings. The resulting words \(0^*1^*1\) and \(1\,1^*0^*\) are favorable. Every direction appears once. \(\square\)

**Conditional path-to-cycle closure.** If arbitrary pairs of binary colorings whose direction-interaction graphs are contained in a path always have \(A_0(u)\cap A_1(v)\ne\varnothing\), then *every* cyclic-local pair with a common constant direction satisfies the same cross-favorability. This implication has no local overlap or favorable-root density assumptions.

**Limit and inductive target.** The universal cross-intersection assertion for two unrelated path-local colorings is an additional theorem to establish; the known unconditional paired-root theorem for ONE tree-local coloring does not by itself imply it for a pair. The existing single-deficient-direction example with common constant j supports the proposed induction: each root has two favorable orders, one starting with j and the other ending with j. The general induction should preserve such two-path boundary information rather than demand one common full order.

##### Acyclic opposite-fiber corollary. Suppose f_j=g_j=c is constant in two cyclic-local cube colorings, and denote their induced colorings on the remaining direction path by f^b,g^b for initial j bit b. If c=0 and for some b either f^(1-b) or g^b has acyclic directed dependencies, then A0(f) intersects A1(g). For c=1 use f^b and g^(1-b). Proof: an acyclic-dependency coloring has every root favorable, while every path-local coloring has at least one root favorable in each orientation by the established tree paired-root theorem. The two relevant favorable sets therefore intersect. Insert j at the start of the zero-color path and at the end of the opposite path when c=0, reversing the insertion roles when c=1. Corollary: a failed common-root instance with constant j requires each of its four relevant path fibers to contain a directed cycle; because the undirected interaction graph is a path, every such cycle is a mutual influence pair between neighboring directions. This reduces the remaining constant-site obstruction to configurations with bidirected path feedback in both opposite fibers.### One arbitrary exceptional site on a cyclic pair

Let \(F_i,G_i\) be arbitrary binary two-neighbor edge-color functions indexed cyclically on \(n\ge3\) cube directions. Define
\[
D_i=\{(a,b):F_i(a,b)=0,\ G_i(a,b)=1\}.
\]
Call \(D_i\) bi-surjective when each input projection takes both binary values; its smallest possible form is the pair \(00,11\) or \(01,10\).

**Theorem.** If all \(D_i\), apart from one \(D_j\), are bi-surjective, then at least two roots support a *common* full dimension-simple geodesic, with direction \(j\) last, whose two color words are
\[
\boxed{0^{n-1}\alpha,\qquad 1^{n-1}\beta},
\quad\alpha,\beta\in\{0,1\}.
\]
The two functions at the exceptional direction \(j\) are unrestricted. In particular cross-favorability holds even if neither opposite-color pair occurs there.

*Proof.* Fix a direction permutation ending with \(j\). For each \(i\ne j\), the condition that the two colors at the direction-\(i\) step equal \((0,1)\) becomes a relation \(R_i\) between the root bits \(x_{i-1},x_{i+1}\). Since the traversal order merely complements some arguments, every \(R_i\) is bi-surjective. The relation graph on root bits uses the pairs \(\{i-1,i+1\}\), with the \(j\)-relation absent.

For odd \(n\), this is a path on all starting-bit variables. Bi-surjectivity permits a chosen bit to be extended across each relation, in either direction. Both choices of an initial endpoint bit therefore produce solutions.

For even \(n\), the relation graph comprises an open path and a separate cycle on the other parity class. The open path always admits at least two solutions. On the closed component, bi-surjective relations are either equality/inequality bijections or contain at least three pairs. Composing such relations preserves bi-surjectivity, and a composition containing any three-pair relation retains at least three pairs, so it has a diagonal pair and satisfies the cycle. If instead every relation on the closed component is a bijection, consistency is the parity of its equality/inequality signs.

Take two consecutive direction steps \(i=j+1,t=j+2\) at the beginning of the traversal, with \(j\) still last. Swap these two steps to obtain a second order. Only the two corresponding local relations change, by complementing one argument in each. The relation at \(i\) lies on the closed parity cycle; that at \(t\) lies on the open path. The swap therefore toggles the consistency parity of the closed cycle while the open path remains satisfiable. One of the two orders yields a root meeting every nonexceptional relation. The open path contributes at least two different roots.

Every nonexceptional edge then has first color zero and second color one. The terminal direction \(j\) has arbitrary colors \((\alpha,\beta)\); both complete words remain monotone. This proves the result. QED.

**Construction and audit.** Given the local truth tables, try at most two dimension orders and solve the binary path/cycle relations by two-state propagation. This uses \(O(n)\) operations. Independent exhaustive checks of all bi-surjective relation systems at the nonexceptional sites for \(n=3,4,5,6,7\) covered respectively \(49,343,2401,16807,117649\) systems with no failures. The theorem itself is not limited to these dimensions.

**Closure implication.** A cyclic pair without a common opposite-orientation root must have at least **two** sites whose simultaneous \((0,1)\) input relations are not bi-surjective. This strengthens the earlier terminal-defect theorem by placing **no condition** on the exceptional pair of edge-color functions.## Absorbing independent sets of exceptional cycle directions

Let \(f,g\) be arbitrary binary cycle-local colorings of \(Q_n\), \(n\ge3\), and write
\[
D_i=\{(a,b):F_i(a,b)=0,\ G_i(a,b)=1\}.
\]
Let \(S\subseteq\mathbb Z_n\) be a nonempty **independent set of the cycle**, meaning no two members of \(S\) are adjacent. Assume \(D_i\) is bi-surjective for every \(i\notin S\), with no restrictions on any \(F_i,G_i\) at sites in \(S\).

**Theorem (separated-defect absorption).** Suppose either (a) \(n\) is odd, (b) \(n\) is even and \(S\) meets both parity classes, or (c) \(n\) is even and \(S\) is a proper subset of one parity class. Then
\[
\boxed{|A_0(f)\cap A_1(g)|\ge2^{|S|}.}
\tag{3}
\]
For each of these roots, the two paths can share a prefix consisting of **all** directions outside \(S\), with its colors identically zero under \(f\) and identically one under \(g\). They may then traverse the exceptional directions in **different orders**, ascending by \(f\)-color and descending by \(g\)-color.

*Proof.* Choose a permutation \(\pi\) of all nonexceptional directions and postpone every direction of \(S\). For \(i\notin S\), the requirement \((F_i,G_i)=(0,1)\) gives a bi-surjective binary relation \(R_i^\pi\) between the starting bits \(x_{i-1},x_{i+1}\), with its input bits complemented according to the preceding directions of \(\pi\). Its bi-surjectivity is preserved. Consider the root-bit relation graph with edge \(\{i-1,i+1\}\) for each \(i\notin S\).

When \(n\) is odd, these potential relation edges form one cycle before deletion. Removing the \(|S|\) exceptional relations splits it into \(|S|\) disjoint paths, isolated single-vertex paths allowed. Every bi-surjective relation allows either bit at a starting endpoint to be propagated to its neighbor. Each path therefore has at least two satisfying assignments, independently. Their Cartesian product contains at least \(2^{|S|}\) common starting roots, for any chosen prefix order.

When \(n\) is even, the relation graph starts as two separate parity cycles. In case (b), the exceptional sites remove at least one relation from each parity cycle. Both become unions of paths, whose total number of connected components is \(|S|\). The same argument supplies at least \(2^{|S|}\) roots.

In case (c), the exceptional sites remove relations from one parity cycle, leaving \(|S|\) independent paths; the other parity cycle remains closed. If its bi-surjective relations contain a three-pair or full relation, their cyclic composition also contains at least three pairs and hence has a diagonal entry, giving a cyclic solution. Otherwise every relation on the closed cycle is a two-pair equality/inequality bijection, and solvability is the parity of its signs.

Since \(S\) does not exhaust its parity class, choose a nonexceptional direction \(t\) with the same parity as \(S\), and an adjacent direction \(i\) of opposite parity (also nonexceptional). Make \(i,t\) consecutive at the beginning of the common prefix; compare their two possible orders, keeping all other precedences unchanged. Swapping \(i,t\) complements one argument in each of the two corresponding root-bit relations. The relation at \(i\) belongs to the intact closed parity cycle, so its bijection sign toggles. The relation at \(t\) lies in an already open path component and remains bi-surjective. Therefore one of the two prefix orders makes the closed cycle satisfiable. All \(|S|\) path components still contribute two choices each, proving the root lower bound in (3).

For any such root, traverse the common prefix \(\pi\). Every step outside \(S\) has color zero for \(f\) and one for \(g\). Since \(S\) is independent in the **direction interaction cycle**, the colors of the remaining exceptional directions depend only on their neighbors **outside** \(S\), whose bits have all been toggled during the prefix. Therefore those colors are unaffected by the relative order in which the directions of \(S\) are subsequently traversed. Sort the exceptional suffix ascending by its \(f\)-colors to obtain a full \(0^*1^*\) word; independently sort it descending by its \(g\)-colors to obtain a full \(1^*0^*\) word. Both full paths start at the same root and traverse every direction once. Distinct root-bit solutions remain distinct paired roots. QED.

**Algorithm and audits.** The proof gives an \(O(n)\) method: select one or two prefix orders, propagate the root-bit relations on their path components and test the one possible closed component, then sort the exceptional suffix in each of the two binary color orders. An independent C++ verification exhausted all \(7^{n-|S|}\) choices of bi-surjective nonexceptional local relations for the representative configurations
\[
(n,S)=(7,\{0,2,4\}),\ (8,\{0,2\}),\
(8,\{0,3\}),\ (8,\{0,2,4\}),
\]
with respectively \(2401,117649,117649,16807\) systems and **no failures**. Random full edge-color checks in dimensions five through nine also passed. The all-dimensional theorem follows from the preceding proof, not from the finite tests.

**Sharp boundary for this prefix strategy.** If \(n\) is even and \(S\) is an entire parity class, every nonexceptional direction belongs to the other parity class. The remaining root-bit relation graph is one unbroken cycle, and there is no adjacent pair of nonexceptional directions to perform the parity-flipping swap. This can cause the common-prefix requirements to fail: for \(n=4\), take \(S=\{0,2\}\), and set the two nonexceptional relations to \(D_1=\{00,11\}\), \(D_3=\{01,10\}\). Their demands on the same pair of root bits are contradictory. This does **not** show a failure of cross-favorability; it only excludes the shared-prefix construction.

**Closure significance.** The number of deficient sites is not by itself the obstruction. Any number of pairwise nonadjacent sites can be postponed and individually sorted, except for the saturated checkerboard case on an even cycle. Remaining cyclic cross-favorability failures, if any exist, must involve **adjacent** deficient sites or that saturated checkerboard configuration. This is an all-dimensional combinatorial reduction in the number and placement of local obstructions, preserving dimension-simple geodesics throughout.### Separated defects in unicyclic NORI1 facets

**Corollary.** Let a binary edge coloring of a cube have a unicyclic direction-interaction graph, with arbitrary nonlinear pendant trees. Choose complementary attached-bit assignments for the two cyclic core orientations by the universal subtree-interface theorem, and let \(g^0,g^1\) be the resulting pair of cycle-local colorings. Write
\[
D_i=\{(a,b):g_i^0(a,b)=0,\ g_i^1(a,b)=1\}.
\]
If the sites at which \(D_i\) is not bi-surjective form an independent set of the core cycle, other than a whole parity class of an even cycle, then the full coloring has a paired root. The conclusion also holds when every site is bi-surjective.

*Proof.* For an empty exceptional set, use the one-arbitrary-defect theorem by choosing any direction last. Otherwise apply the separated-defect theorem to \(g^0,g^1\), obtaining at least \(2^{|S|}\) shared cycle roots with opposite monotone geodesics. The earlier opposite-bit subtree-interface lemma reconstructs their full cube paths from common roots, keeping every direction simple. QED.

The universal free-bridge correspondence lifts this to NORI1 for any antipodally odd coloring of the next-dimensional cube whose chosen facet has this interaction structure, with arbitrary odd bridge bits.

**Remaining cyclic obstruction.** Any failure of cross-favorability between two cyclic-local colorings must have adjacent non-bi-surjective sites or, in even dimension, an entire parity class of such sites. The former requires a coupled multi-direction seam; the latter retains one closed parity relation cycle without an available adjacent-swap repair. The present results do not establish that either obstruction can cause a counterexample.### Checkerboard saturation: only a pure parity-frustrated cycle resists the prefix method

Let \(n=2m\ge4\), and suppose the exceptional set \(S\) is one entire parity class of the direction cycle. Thus \(S\) contains \(m\) mutually nonadjacent directions, and each direction \(i\notin S\) has a bi-surjective relation
\[
D_i=\{(a,b):F_i(a,b)=0,\ G_i(a,b)=1\}.
\]

**Theorem (checkerboard relation-cycle criterion).** If the cyclic composition of the \(m\) relations \(D_i\), \(i\notin S\), contains a diagonal binary pair, then
\[
\boxed{|A_0(f)\cap A_1(g)|\ge2^m.}
\tag{4}
\]
If every such \(D_i\) is a two-pair equality/inequality relation and their cycle parity is consistent, then the stronger bound \(2^{m+1}\) holds. In particular (4) holds whenever **at least one** nonexceptional \(D_i\) contains three or four input pairs.

*Proof.* Traverse all nonexceptional directions first, in any order. They are mutually nonadjacent, so each sees the starting bits of its two neighboring exceptional directions, unaffected by the prefix traversal. Their requirement \((F_i,G_i)=(0,1)\) gives the unmodified relations \(D_i\) on the \(m\) starting bits indexed by \(S\); these relations form one cycle. The starting bits on the \(m\) nonexceptional directions are entirely free.

If the relation-cycle composition has a diagonal pair, it admits at least one satisfying assignment of the exceptional root bits. Combined with the \(2^m\) free nonexceptional bits, this gives at least \(2^m\) valid starting roots for a common prefix of colors \(0\) under \(f\) and \(1\) under \(g\).

After the prefix, all nonexceptional bits have toggled. Every exceptional direction depends only on neighboring nonexceptional bits, so its edge colors are independent of the traversal order inside the exceptional suffix. Sort that suffix increasingly under \(f\) and decreasingly under \(g\) to obtain complete opposite monotone words from each of the counted starting roots.

Finally, a composition of bi-surjective Boolean relations is bi-surjective; once a three-pair relation occurs, every later composition contains at least three pairs, so its cyclic trace is nonempty. If all relations are two-pair bijections, the product is either identity or swap. The identity case supplies two satisfying assignments of the exceptional root bits, giving \(2^{m+1}\) full roots; the swap case has no solution for this prefix strategy. QED.

**Residual obstruction.** Hence a cyclic cross-root counterexample, if it exists, has either adjacent non-bi-surjective sites, or the following checkerboard-parity form: one entire parity class is deficient, every site of the other parity has an equality/inequality \(D_i\), and the XOR of these relation signs around that parity cycle is one. The latter condition is an obstruction to the *common-prefix construction*, not an established obstruction to cross-favorability itself. Restoring it requires letting at least one exceptional direction cross before some of the nonexceptional directions, potentially at different positions in the two monotone paths.

##### A probabilistic obstruction to square-template induction

For d=2r, define an edge coloring of Q_d with one hub bit s and d-1 leaf bits x by f_hub(x,s)=b(x), f_leaf(x,s)=s. The interaction graph is a connected star. The nondecreasing favorable-root set is

A0 = {(0,x): all x} union {(1,x): b(x)=0 or b(complement x)=1}.

**Theorem.** In every even dimension d>=10 some such connected-star coloring has a favorable-root set containing no product of forbidden two-bit corners along any perfect matching of the directions.

*Proof.* Sample the values of b independently as fair bits. A template on 2r directions has r forbidden corners along a perfect matching. Choose one permitted value of the leaf bit paired with the hub, holding the hub bit at one. The other r-1 pairs each have three choices, producing 3^(r-1) leaf assignments. They all share one leaf bit, so no two are complements. For each assignment x the event that its hub-one root is unfavorable equals b(x)=1 and b(complement x)=0, of probability 1/4. These events are independent. Hence a fixed template is fully favorable with probability at most (3/4)^(3^(r-1)). There are (2r-1)!! times 4^r templates. The union bound is therefore (2r-1)!!*4^r*(3/4)^(3^(r-1)), which is below 0.000074 for r=5 and decreases thereafter. QED.

**Explicit small witness.** Already for d=6, setting b's 32-bit truth table to 0x23975ee9 gives the favorable-root mask 0xf7ff7fddfdd7f77d with 54 of 64 roots. Direct path enumeration confirms this mask. The ten unfavorable root indices are 1,7,11,19,21,25,33,37,47,59, with the hub as least significant bit. All 15 perfect matchings and 64 corner assignments for each were independently checked; none yields a template contained in the favorable set.

This theorem does not refute the chordless-cycle-specific template conjecture. It proves that template containment is not a valid general invariant for an induction that adds arbitrary tree branches, even when paired-root existence and cross-favorability are already guaranteed by the star theorem. An induction must carry a less rigid two-orientation relation.

##### All-dimensional cross-favorability on a common interaction path

Let \(f,g\) be arbitrary binary colorings of the undirected edges of \(Q_n\), \(n\ge2\), whose combined direction-interaction graph lies inside the path \(0-1-\cdots-(n-1)\). Edge colors in direction \(i\) depend only on the bits of the adjacent path directions. The colorings may have unrelated nonlinear local truth tables.

**Theorem 1 (computer-certified path cross-favorability).** For every \(n\ge2\),
\[
\boxed{A_0(f)\cap A_1(g)\ne\varnothing.}
\tag{1}
\]
A common root and two full dimension-simple antipodal geodesics with respective words \(0^*1^*\) and \(1^*0^*\) can be reconstructed in \(O(n)\) time from the local truth tables. The universal existence assertion follows from a finite 66-mask induction certificate described below, verified independently in Python and C++.

**Orientation criterion.** Choose a common starting cube vertex \(x\), and independent orientations \(u_i,v_i\in\{0,1\}\) of the interaction edge \(i,i+1\) for the \(f\)- and \(g\)-orders: bit one means dimension \(i\) precedes \(i+1\). The traversed colors at an interior direction \(i\) are
\[
a_i=F_i(x_{i-1}\oplus u_{i-1},x_{i+1}\oplus(1-u_i)),\quad
b_i=G_i(x_{i-1}\oplus v_{i-1},x_{i+1}\oplus(1-v_i)),
\tag{2}
\]
with the absent argument omitted at endpoints. The required monotone paths exist for this root and these orientations if and only if, for each adjacency \(i,i+1\),
\[
u_i=1\Rightarrow a_i\le a_{i+1},\qquad
u_i=0\Rightarrow a_{i+1}\le a_i,
\]
\[
v_i=1\Rightarrow b_i\ge b_{i+1},\qquad
v_i=0\Rightarrow b_{i+1}\ge b_i.
\tag{3}
\]
Necessity follows from dimension precedence. Conversely every orientation of an undirected path is acyclic. Conditions (3) prohibit a precedence edge pointing from color one to zero in the \(f\)-order, or zero to one in the \(g\)-order. Topologically order the first color class and then the second in the appropriate orientation. The resulting total direction orders give full geodesics from \(x\) with precisely the locally computed edge colors (2), hence the desired monotone words.

**The 64-state transfer.** After processing directions \(i,i+1\), retain
\[
s_i=(x_i,x_{i+1},u_i,v_i,a_i,b_i)\in\{0,1\}^6.
\tag{4}
\]
There are 256 possible pairs of four-entry interior truth tables. For each such label \(\ell\), and each state \(s_i\), choose the three new bits \(x_{i+2},u_{i+1},v_{i+1}\), evaluate \(a_{i+1},b_{i+1}\) by (2), and retain the successor state precisely if (3) holds. This defines a 64-state nondeterministic transfer table. At the left endpoint, the 16 pairs of unary tables each yield a 16-element starting state set \(I_h\); at the right endpoint, each unary pair defines an acceptance mask \(E_t\) whose states pass the final comparison.

Encode a state by the integer
\[
x_i+2x_{i+1}+4u_i+8v_i+16a_i+32b_i.
\tag{5}
\]
Encode a two-input table with input index \(L+2R\), assigning the low four bits of an eight-bit transfer label to \(F_i\) and the high four to \(G_i\). For a subset mask \(M\), let \(T_\ell(M)\) be the union of its successors under label \(\ell\).

**Finite-state induction certificate.** There exists a family \(\mathcal B\) of 66 nonempty state-subset masks satisfying:
- Each of the 16 initial masks \(I_h\) contains a member of \(\mathcal B\).
- For each of 66 masks \(B\in\mathcal B\) and each of 256 interior labels \(\ell\), the mask \(T_\ell(B)\) contains some mask \(B'\in\mathcal B\).
- Each mask \(B\in\mathcal B\) intersects all 16 terminal acceptance masks \(E_t\).

Induction over the sequence of local truth tables therefore leaves a member of \(\mathcal B\) inside every reachable state set. Its intersection with the relevant right endpoint mask is nonempty, giving a common root and two valid orientation assignments. The orientation criterion proves (1).

**Reproducible finite verification.** Starting from the 16 endpoint masks, breadth-first closure under all 256 subset transitions has **3,191** distinct nonempty masks. All **816,896** state-set transitions were evaluated, and none of the 3,191 sets is disjoint from any of the 16 endpoint acceptance sets. Its inclusion-minimal antichain consists of **66** masks: 16 of size 16, 32 of size 28, and 18 of size 32. Checking the smaller inductive certificate requires **16,896** mask containment tests for transitions and **1,056** terminal nonempty-intersection tests; every test succeeds. Sorting the 66 masks numerically and writing each as sixteen lowercase hexadecimal characters followed by a newline gives SHA-256
\[
\texttt{3c0450114b54eb377ade6e7412b9b5bcd3bb8b8f999bb73b1eeaab59eefb7d4b}.
\tag{6}
\]
The finite certificate uses integer bit operations and no external solver. Independent Python and C++ subset implementations both found the same closure size. A separate root-and-path reconstruction checked 960 randomly generated instances in dimensions two through nine by reevaluating every edge color on both resulting full paths. Those additional tests are an audit, not the logical basis for the all-dimensional theorem.

**Corollary 2 (path forests).** If the union of the interaction graphs of \(f,g\) is a disjoint union of paths, then \(A_0(f)\cap A_1(g)\ne\varnothing\). Both favorable-root families factor as Cartesian products over independent components; apply Theorem 1 to each component.

**Corollary 3 (a jointly constant site closes arbitrary cyclic-local pairs).** Suppose \(f,g\) have cyclic-neighbor locality and some direction \(j\) has constant color in both colorings, \(f_j\equiv c\), \(g_j\equiv d\), with arbitrary \(c,d\in\{0,1\}\). Then \(A_0(f)\cap A_1(g)\ne\varnothing\). Fix the common initial \(j\)-bit \(t\), and remove direction \(j\), leaving a path-local pair on the remaining directions. In the \(f\)-order, traverse \(j\) first when \(c=0\), or last when \(c=1\). In the \(g\)-order, traverse \(j\) first when \(d=1\), or last when \(d=0\). The induced path colorings see a fixed \(j\)-bit equal to \(1-t\) or \(t\), independently for each ordering. Apply Theorem 1 to these two path colorings at a common lower-dimensional root, and reinsert \(j\) at the chosen extremes. Both full paths are monotone and start at the same root.

**Corollary 4 (unicyclic facets with a core-constant site).** Let a cube-edge coloring have a unicyclic undirected interaction graph, with arbitrary nonlinear pendant trees. If at one core direction \(j\) its edge-color function is independent of its two neighboring cycle bits (but may depend on its pendant-child bits), then the coloring has a paired root. The pendant-tree opposite-bit interface theorem yields two induced cycle-local colorings whose \(j\)-direction colors are constants, possibly different. Apply Corollary 3, then lift the two witnesses through the pendant trees. By the free-bridge correspondence, NORI1 holds for every antipodally odd next-dimensional extension of this facet class with unrestricted bridge colors.

**Algorithmic form.** Given the truth tables, propagate sets of at most 64 transfer states along the direction path, recording predecessors. Choose an accepted final state and backtrack the common starting bits and the two orientation strings. For each orientation, topologically sort its zero-color and one-color induced subgraphs in the required phase order. This constructs both full direction-simple paths in \(O(n)\) time and space.

**Proof-closure status.** This theorem resolves an all-dimensional **two-coloring** cross-root problem on interaction paths, eliminating the constant-site cyclic obstruction and supplying a gluing tool for subsequent separator inductions. Universal cross-favorability for arbitrary cycle-local pairs, and therefore unrestricted NORI1, remains open. A larger finite-state invariant or a handwritten classification of the remaining cyclic constraints is the next target.

##### Unrestricted paired roots for all interaction graphs of degree at most two

**Corollary (unrestricted cyclic-local single-coloring closure).** Let an arbitrary binary edge coloring \(f\) of \(Q_n\) satisfy \(f_i(x)=F_i(x_{i-1},x_{i+1})\) at all directions, cyclic subscripts, without any further assumptions. Then
\[
\boxed{A_0(f)\cap A_1(f)\ne\varnothing.}
\tag{9}
\]

*Proof.* If each \(F_i\) is nonconstant, apply the nonlinear cyclic-local paired-root theorem established in the nonlinear-tree incidence and cycle-syndrome Subsection: either a monochromatic full geodesic exists or \(f\) belongs to the affine neighbor-parity exception family, also proved to have paired roots. If some \(F_j\) is constant, apply the path cross-favorability theorem above to the pair \((f,f)\) via Corollary 3, since both induced direction-\(j\) colors are constant. These cases exhaust all cyclic-local colorings. QED.

**Corollary (all degree-two interaction graphs).** Suppose the undirected direction-interaction graph of an arbitrary binary edge coloring of \(Q_d\) has maximum degree at most two. Then \(P(f)\ne\varnothing\). Every connected component is a path, a cycle, or a singleton. Paths have paired roots by the previously established nonlinear tree theorem, cycles by the preceding corollary, and singletons trivially. Cartesian factorization multiplies the paired-root sets of these independent factors. No affine or antipodal hypothesis is used.

**NORI1 consequence.** Every antipodally odd edge coloring of \(Q_{d+1}\) whose chosen lower \(Q_d\) facet has direction-interaction graph of maximum degree two admits a monochromatic full dimension-simple antipodal geodesic, with no further restriction on the odd vertical bridge colors.

**Remaining distinction.** Pure cycle-local paired-root existence is now established. Pendant-tree elimination on a unicyclic interaction graph generally creates two *different* conditional cycle colorings. Each is individually paired-root favorable, but their opposite-orientation feasible-root sets need not intersect merely from that fact. Universal cross-favorability for two arbitrary cycle-local colorings remains open, and is the remaining obstacle to unicyclic closure with unrestricted nonlinear pendant branches.

##### Explicit 66-mask certificate

The finite induction basis from Theorem 1 consists of the following 66 unsigned 64-bit masks, in ascending numeric order, encoded as hexadecimal. Bit `s` indicates presence of the six-bit state of integer index `s` as defined in (5). Grouping into four entries per line is for legibility; the checksum in (6) uses one entry per line.

~~~text
000000000000ffff 000000003c3cc3c3 00000000c3c33c3c 00000000ffff0000
000033cc0000cc33 0000cc33000033cc 0000ffff00000000 0140314cc143fd7f
0280328cc283febf 03c0300cc0030c30 0410c413341cf7df 0820c823382cfbef
0c30c003300c03c0 100413c41c34dff7 11441144dd77dd77 13c41004dff71c34
1414d7d71414d7d7 1c34dff7100413c4 200823c82c38effb 22882288eebbeebb
23c82008effb2c38 2828ebeb2828ebeb 2c38effb200823c8 300c03c00c30c003
314c0140fd7fc143 328c0280febfc283 33cc0000cc330000 341cf7df0410c413
382cfbef0820c823 3c3cc3c300000000 40014c3143c17ffd 41417d7d41417d7d
43c17ffd40014c31 4411441177dd77dd 4c3140017ffd43c1 5555555555555555
77dd77dd44114411 7d7d41417d7d4141 7ffd43c14c314001 80028c3283c2bffe
8282bebe8282bebe 83c2bffe80028c32 88228822bbeebbee 8c328002bffe83c2
aaaaaaaaaaaaaaaa bbeebbee88228822 bebe8282bebe8282 bffe83c28c328002
c0030c3003c0300c c143fd7f0140314c c283febf0280328c c3c33c3c00000000
c4130410f7df341c c8230820fbef382c cc33000033cc0000 d7d71414d7d71414
dd77dd7711441144 dff71c3413c41004 ebeb2828ebeb2828 eebbeebb22882288
effb2c3823c82008 f7df341cc4130410 fbef382cc8230820 fd7fc143314c0140
febfc283328c0280 ffff000000000000
~~~

A standalone verifier need only (i) generate the sixteen left and right boundary masks and the 256-by-64 transition table according to equations (2)-(5); (ii) assert that every left boundary contains some listed mask; (iii) assert that every image of each listed mask under all 256 transition labels contains at least one listed mask; (iv) assert that every listed mask meets all sixteen right acceptance masks. These are finite bitset assertions and prove the unbounded-length theorem by induction. No enumeration of all colorings of an n-dimensional cube is required.


##### Shared antipodally-even local functions close the cyclic two-coloring problem

Let \(f,g\) be arbitrary cyclic-neighbor colorings of the cube \(Q_n\), \(n\ge3\). Suppose a distinguished direction \(j\) has the same local function in the two colorings, \(f_j=g_j=H\), and
\[
\boxed{H(a,b)=H(1-a,1-b)\quad\text{for all }a,b\in\{0,1\}.}
\tag{10}
\]
The only such two-input Boolean functions are the two constants and the two neighbor-parity functions \(a\oplus b\) and \(1\oplus a\oplus b\).

**Theorem (shared-parity cyclic cross-favorability).** Under this assumption,
\[
\boxed{A_0(f)\cap A_1(g)\ne\varnothing.}
\tag{11}
\]
The two witness paths can be constructed in linear time using the finite-state path solver, and the reinsertion of \(j\) requires no search.

*Proof.* Delete direction \(j\), leaving a path on the other \(n-1\) directions. Fix the \(j\)-bit to one in \(f\), obtaining a path-local coloring \(f^{(1)}\), and fix it to zero in \(g\), obtaining a path-local coloring \(g^{(0)}\). By the universal path cross-favorability theorem, there exist a common starting bit assignment \(x\) on those \(n-1\) directions, a full nondecreasing path \(P_f\) from \(x\) in \(f^{(1)}\), and a full nonincreasing path \(P_g\) from \(x\) in \(g^{(0)}\).

Put \(p=H(x_{j-1},x_{j+1})\). By (10), this is also \(H(1-x_{j-1},1-x_{j+1})\), which is the color of direction \(j\) after all other directions have been traversed.

Choose the common full starting root to have \(j\)-bit \(p\). If \(p=0\), put \(j\) **first** in the \(f\)-path, giving the leading zero color, and **last** in the \(g\)-path, giving a trailing zero. The remaining \(f\)-steps then see bit \(j=1\), while the remaining \(g\)-steps see \(j=0\), matching the chosen path-fiber pair \(f^{(1)},g^{(0)}\). Thus the full words are \(0\,0^*1^*\) and \(1^*0^*\,0\).

If \(p=1\), instead put \(j\) **last** in the \(f\)-path and **first** in the \(g\)-path. The other \(f\)-steps again see \(j=1\), and the other \(g\)-steps again see \(j=0\). The color of \(j\) at either extreme is one, so the full words are \(0^*1^*\,1\) and \(1\,1^*0^*\). All directions occur once, and the full paths share their starting root. QED.

**Corollary (responsive or even-shared unicyclic closure).** Consider a coloring whose connected undirected interaction graph is unicyclic with arbitrary nonlinear pendant trees. If either (i) every cycle site has an antipodally responsive pendant interface as in the adaptive-polarization theorem, or (ii) some nonresponsive cycle site has a common induced two-input color function \(H\) invariant under complementing both cycle-neighbor bits, then the coloring has a paired root. The free-bridge equivalence proves NORI1 for antipodally odd extensions of these facets with unrestricted odd bridge colors.

*Proof.* Case (i) is the established adaptive-polarization theorem. In case (ii), choose complementary pendant polarizations at every cycle site. The induced cycle colorings share the function \(H\) at the nonresponsive site. The theorem supplies compatible core paths, and the opposite-bit subtree interface lifts them to full paths from one starting root. QED.

**Unresolved shared-site classes.** The remaining nonconstant shared local functions are the four projections/complements, and the eight unbalanced nonlinear two-input truth tables. The endpoint-extension proof above fails for these functions because their values can change when both neighbor bits are complemented; this is a limitation of the extreme-insertion construction, not a counterexample to cross-favorability.

**Audit.** A separate implementation used the path root solver on arbitrary random cyclic pairs with shared even functions \(H\in\{0,6,9,15\}\) in dimensions three through seven. It inserted direction \(j\) according to the observed value \(p\), then independently evaluated every edge color along both complete paths. All 360 tested instances satisfied the claimed opposite monotonicities.
##### Two disjoint opposite-fiber lifts through a shared even site

Under the shared parity theorem hypotheses, remove the distinguished direction j and define
\[
R_{10}=A_0(f^{(1)})\cap A_1(g^{(0)}),\qquad
R_{01}=A_0(f^{(0)})\cap A_1(g^{(1)}).
\]
These are cross-favorable root sets of two pairs of path-local colorings.

**Theorem (additive multiplicity).** If \(f_j=g_j=H\) with \(H(a,b)=H(1-a,1-b)\), then
\[
\boxed{|A_0(f)\cap A_1(g)|\ge |R_{10}|+|R_{01}|
\ge2\kappa_{\mathrm{path}}(n-1).}
\tag{12}
\]
Here \(\kappa_{\mathrm{path}}(m)\) is the minimum cross-orientation root intersection for arbitrary pairs of path-local colorings of \(Q_m\), positive in every dimension by the 66-state theorem.

*Proof.* The previous theorem injectively lifts each root \(x\in R_{10}\) to the full root whose deleted j-bit is \(H(x_{j-1},x_{j+1})\). Construct a second lift from \(R_{01}\) with deleted j-bit \(1-H(x_{j-1},x_{j+1})\). When \(H(x)=0\), place j first in the f-geodesic and last in the g-geodesic. Their remaining steps see the j-bit as 0 and 1, respectively, so they follow the selected \(f^{(0)},g^{(1)}\) paths; the inserted j-edge has color zero at both extremes. When \(H(x)=1\), place j last in f and first in g. Again the remaining steps see j-bits 0 and 1, while the inserted edge has color one at either extreme. Both full paths retain their required monotone words. The images of the two lifts are disjoint because for the same lower root x their initial j-bits are complementary. The stated count follows. QED.

**Finite values.** Independent complete enumeration gives \(\kappa_{\mathrm{path}}(2)=2,\ \kappa_{\mathrm{path}}(3)=4,\ \kappa_{\mathrm{path}}(4)=4,\ \kappa_{\mathrm{path}}(5)=6\), from 5, 17, 117 and 729 distinct favorable-root masks respectively. Therefore cyclic pairs with a shared even local function have at least 4, 8, 8, 12 common roots in dimensions 3, 4, 5, 6. The general theorem needs no finite census.

**Inductive implication.** The parity gluing lemma preserves two disjoint full-root families. For shared projections or unbalanced nonlinear functions, the extreme-insertion method is insufficient; an induction must allow the deleted direction to cross at an interior seam.

##### Antipodal-input seam gluing beyond even local functions

Let \(f,g\) be arbitrary cyclic-neighbor colorings of \(Q_n\), \(n\ge3\), sharing one local edge-color function \(H\) at direction \(j\):
\[
f_j(a,b)=g_j(a,b)=H(a,b).
\]
Delete \(j\) to obtain four path-local fiber colorings \(f^{(0)},f^{(1)},g^{(0)},g^{(1)}\), and define
\[
R_{10}=A_0(f^{(1)})\cap A_1(g^{(0)}),\qquad
R_{01}=A_0(f^{(0)})\cap A_1(g^{(1)}).
\]
Both are nonempty by the universal path cross-favorability theorem. Define the **antipodal-input agreement set**
\[
E_H=\{x\in Q_{n-1}:H(x_{j-1},x_{j+1})=
H(1-x_{j-1},1-x_{j+1})\}.
\]

**Theorem (localized double-fiber lifting).**
\[
\boxed{
|A_0(f)\cap A_1(g)|
\ge |R_{10}\cap E_H|+|R_{01}\cap E_H|.
}
\tag{15}
\]

*Proof.* Fix \(x\in R_{10}\cap E_H\), and put \(b=H(x_{j-1},x_{j+1})\). The shared local function also has color \(b\) after both neighboring directions have toggled. Assign starting bit \(x_j=b\). If \(b=0\), insert \(j\) at the beginning of the nondecreasing \(f^{(1)}\)-path and the end of the nonincreasing \(g^{(0)}\)-path. If \(b=1\), insert \(j\) at the end of the \(f^{(1)}\)-path and the beginning of the \(g^{(0)}\)-path. These two full paths start at the same vertex and have the desired monotone color words.

For \(x\in R_{01}\cap E_H\), instead assign starting bit \(x_j=1-b\). When \(b=0\), insert \(j\) first in the \(f^{(0)}\)-path and last in the \(g^{(1)}\)-path. When \(b=1\), insert \(j\) last in \(f^{(0)}\) and first in \(g^{(1)}\). Again both words remain monotone and the starting root is common. Each lift is injective; at a given lower root the two lifts choose opposite starting bits for direction \(j\), so their images are disjoint. Counting gives (15). QED.

**Corollary (classification of the remaining shared-site obstruction).** The sixteen two-input functions \(H\) divide into three classes:

1. For the four complement-even functions \(H=0,6,9,15\), the set \(E_H\) is the entire lower cube; (15) recovers the full double-fiber theorem.
2. For the eight unbalanced nonlinear functions, \(E_H\) is one of the two parity classes \(x_{j-1}\oplus x_{j+1}=0\) or \(1\). Consequently cross-favorability follows if either \(R_{10}\) or \(R_{01}\) meets that parity class. **A hypothetical failure requires both cross-root sets to be confined to the opposite parity class.**
3. For the four projections/complements, \(H(a,b)\ne H(1-a,1-b)\) for every input, so \(E_H=\varnothing\). The extreme-insertion theorem supplies no witness and an interior crossing is indispensable for this method.

This separates the unresolved shared-site cycle problem into *parity-rigid path interfaces* for unbalanced nonlinear functions and *intrinsically interior crossing* for projections. It does not claim these obstructions can occur in a full counterexample.

**A finite rigidity example.** Take \(n=5,j=0\) and the outside local truth tables
\[
(F_1,F_2,F_3,F_4)=(12,10,12,10),\qquad
(G_1,G_2,G_3,G_4)=(12,5,3,10),
\]
using neighbor-input index left plus twice right. The two opposite-fiber path cross-root sets both consist of the four lower roots whose adjacent endpoint bits satisfy \(x_1=x_4=0\). Let \(H(a,b)=a\wedge b\), with truth table 8. Its agreement set is the opposite endpoint-parity class \(x_1\ne x_4\). Hence (15) gives the zero lower bound, and no witness is produced by that extreme-insertion construction. Nevertheless direct full-path enumeration finds eight common roots in the original five-cube. The example demonstrates that one must allow nonextreme insertion when the path interfaces are parity-rigid.

**Closure direction.** The next useful induction lemma is not universal endpoint-parity flexibility, which is false for arbitrary path-local pairs. It should say that **when both opposite-fiber cross-root sets are parity-rigid on the wrong side, the deleted shared direction can be inserted at an interior seam**. Proving this for unbalanced \(H\), together with a distinct projection-site exchange, would finish the shared-site cross-favorability theorem and thus every unicyclic interaction graph by adaptive pendant polarization.
##### Majority partition theorem for shared cyclic sites

Let \(f^H,g^H\) be two arbitrary cyclic-neighbor colorings agreeing on one local two-input function \(H\), while all remaining local tables are fixed independently. The failed choices
\[
\mathcal F=\{H:A_0(f^H)\cap A_1(g^H)=\varnothing\}
\]
form a majority-closed subset of the sixteen four-bit Boolean tables by the previously established shared-site 2-CNF theorem. They exclude the four antipodally even tables \(0,6,9,15\) by the shared-parity gluing theorem.

**Theorem.** \(|\mathcal F|\le8\). More precisely, at least one member of each triple
\[
(1,2,12),\quad(3,4,14),\quad(5,8,11),\quad(7,10,13)
\]
is cross-favorable.

*Proof.* The twelve other tables form the four disjoint triples displayed above. Their coordinatewise three-element majorities are respectively \(0,6,9,15\). If all members of one triple failed, majority closure would make its even majority fail, contradicting shared-parity gluing. Thus each triple contributes at most two failures. QED.

The bound eight is optimal for an abstract majority-closed subset disjoint from the even tables: the solutions of \(h_{00}\ne h_{11}\) constitute eight assignments and obey both properties. This does not establish attainability by cyclic cube colorings.

**Polarization corollary.** If at one cycle direction the attached-tree choices realize all three shared tables from one of these triples, while leaving the other induced cycle rules fixed, choosing the appropriate attached-bit polarization guarantees a cross-favorable core pair. The existing opposite-bit tree interface then lifts the pair to a paired root of the original cube coloring. The shared-site conjecture for a *fixed arbitrary* \(H\) remains open.### Two symmetry prototypes for the shared-site closure problem

Suppose two arbitrary cyclic-neighbor cube-edge colorings \(f,g\) share one local two-input edge-color rule \(H\) at direction \(j\). The cross-root existence statement is unchanged if we simultaneously apply to both colorings any of the following: complement either neighboring input bit by a cube translation; exchange the two neighboring directions by reflecting the cycle; or complement both edge-color bits. For the last operation, \(A_0(1-f)\cap A_1(1-g)=A_1(f)\cap A_0(g)\), which is the antipodal translate of \(A_0(f)\cap A_1(g)\).

These symmetries partition the 16 Boolean functions of two inputs into four orbits, with truth-table code indexed by left-bit plus twice right-bit:
\[
\begin{array}{c|c|c}
\text{type}&\text{codes}&\text{representative}\\
\hline
\text{constant}&0,15&0\\
\text{parity}&6,9&a\oplus b\\
\text{projection}&3,5,10,12&a\\
\text{unbalanced}&1,2,4,7,8,11,13,14&a\land b.
\end{array}
\tag{17}
\]

**Theorem (two-prototype sufficiency).** To prove cross-favorability for *every* pair of cycle-local colorings sharing one local function, it is sufficient to prove just the two cases
\[
\boxed{H(a,b)=a,\qquad H(a,b)=a\land b.}
\tag{18}
\]
The constant and parity cases were established by the shared-even-site theorem, and the listed symmetries carry all other local functions to the two representatives. Conversely the unrestricted shared-site claim includes both representatives. QED.

**Finite audit.** For \(Q_6\), exhaustive enumeration of the \(16^5=1,048,576\) choices of other local truth tables per fixed shared function, followed by deduplication of nondecreasing favorable-root masks and full pairwise comparison, gave:
\[
\begin{array}{c|r|r|r}
H&\text{distinct masks}&\min |A_0|&\min|A_0(f)\cap A_1(g)|\\
a&6539&27&7\\
a\land b&15859&36&12.
\end{array}
\tag{19}
\]
The census uses rooted subset dynamic programming with bit-parallel root masks, not SAT or integer optimization. These results verify the claim for this finite dimension only. The unbounded shared-site assertion remains open.### Cyclic transfer using 64 boundary states and two monodromy bits

Let \(f_i(x)=F_i(x_{i-1},x_{i+1})\) and \(g_i(x)=G_i(x_{i-1},x_{i+1})\) be two arbitrary cyclic-neighbor cube-edge colorings, with \(n\ge3\). For a common starting root \(x\), let \(u_i\) and \(v_i\) be the orientations of cycle edge \(i,i+1\) induced by the first and second dimension orders; bit one means direction \(i\) precedes direction \(i+1\). Their traversed colors are
\[
c_i=F_i(x_{i-1}\oplus u_{i-1},x_{i+1}\oplus(1-u_i)),\quad
d_i=G_i(x_{i-1}\oplus v_{i-1},x_{i+1}\oplus(1-v_i)).
\tag{20}
\]
The monotone-word conditions on cycle adjacency \(i,i+1\) are
\[
u_i=1\Rightarrow c_i\le c_{i+1},\quad
u_i=0\Rightarrow c_{i+1}\le c_i,\quad
v_i=1\Rightarrow d_i\ge d_{i+1},\quad
v_i=0\Rightarrow d_{i+1}\ge d_i.
\tag{21}
\]

**Theorem (64-state cyclic monodromy criterion).** The common opposite-orientation root set \(A_0(f)\cap A_1(g)\) is nonempty if and only if there is a cyclic closed walk in the following 64-state transfer, with **both** orientation bits attaining zero and one during the walk.

At site \(i\) retain \(s_i=(x_i,x_{i+1},u_i,v_i,c_i,d_i)\in\{0,1\}^6\). Its transition from \(s_{i-1}\) to \(s_i\), labeled by \((F_i,G_i)\), chooses \(x_{i+1},u_i,v_i\), calculates the two colors in (20), and checks (21) for the preceding adjacency. The cyclic condition matches the state after \(n\) transitions to the starting state. Two additional flags record whether any \(u_i\) differs from its initial value and whether any \(v_i\) differs from its initial value; acceptance requires both flags set.

*Proof.* Two full direction orders from the same root give a closed walk satisfying these conditions. Conversely, the closed walk provides consistent starting bits and two orientations of the direction cycle. An oriented cycle is acyclic precisely when its edge-orientation bits are not all identical. Both flags set therefore guarantee acyclicity of the two precedence relations. The local inequalities (21) prevent precedence arrows pointing from the later monotone color phase into the earlier phase. Topologically sort the first color class and then the second for each path, respecting the corresponding precedence edges. This gives two full dimension-simple geodesics from the same root, with nondecreasing f-word and nonincreasing g-word. QED.

**Algorithmic corollary.** The criterion gives an \(O(n)\)-time decision and witness-construction algorithm with fixed constants. Enumerate 64 initial states, propagate four 64-bit state masks tracking the change flags, then test cyclic return with both flags set. Store predecessors to recover the common root and two orientation vectors; topologically sort to obtain the complete paths. This reduces the earlier team's 512-state cyclic transfer to 64 boundary states plus two flags, and shares its state representation with the successful 66-mask path induction.

**Independent audit.** A C++ cyclic transfer implementation was compared with an unrelated bit-parallel rooted monotone-path dynamic program for 20,000 random cyclic-local pairs in each of dimensions 3,4,5 and 10,000 pairs in each of dimensions 6,7. All **80,000** decisions agreed. These tests check the implementation; the theorem follows from the transfer equivalence proof.

**Closure target.** Universal cyclic cross-favorability is equivalent to the assertion that every sequence of the 256 transfer labels has a closed walk satisfying both change flags. The statement remains open. An all-word fixed-point invariant extending the eight-prototype path induction would prove the cyclic cross-root theorem and, by pendant-tree elimination, close every unicyclic interaction coloring. A closed walk without the two flags is insufficient: it can represent a directed cycle in an attempted dimension order.### Rigidity at the eight-failure threshold

Fix two cycle-local colorings outside a shared direction, and let \(\mathcal F\subseteq\{0,\ldots,15\}\) be the truth-table codes of the shared local functions for which opposite-orientation cross-favorability fails. The preceding 2-CNF theorem makes \(\mathcal F\) closed under bitwise ternary majority, and the shared-even theorem excludes \(0,6,9,15\). The majority partition theorem shows \(|\mathcal F|\le8\).

**Theorem (classification of equality).** If \(|\mathcal F|=8\), then \(\mathcal F\) must be one of two eight-element sets:
\[
\boxed{
\mathcal F=\{H:h_{00}\ne h_{11}\}
\quad\text{or}\quad
\mathcal F=\{H:h_{01}\ne h_{10}\}.
}
\tag{22}
\]
Thus an eight-function failure set is determined by disagreement of one *antipodal pair* of input entries.

*Proof, with a 81-choice finite certificate.* Partition the twelve codes outside \(\{0,6,9,15\}\) into the four triples
\[
T_0=(1,2,12),\quad T_6=(3,4,14),\quad
T_9=(5,8,11),\quad T_{15}=(7,10,13).
\]
Their ternary bitwise majorities belong respectively to the four excluded codes. Since \(|\mathcal F|=8\), it contains two elements of each triple. There are only \(3^4=81\) possibilities, obtained by specifying one omitted entry in each triple. Check closure under majority for all unordered triples of distinct included codes; repeated-entry majority gives an already included code automatically. The following direct finite check describes the entire verification:
\[
\begin{array}{l}
\text{for }(q_0,q_6,q_9,q_{15})\in\{0,1,2\}^4:\\
\quad S=\bigcup_{t\in\{0,6,9,15\}}\bigl(T_t\setminus\{T_t[q_t]\}\bigr);\\
\quad\text{retain }S\text{ if }\ (a\&b)\,|\,(a\&c)\,|\,(b\&c)\in S\\
\qquad\text{for all distinct }a,b,c\in S .
\end{array}
\]
Only two subsets survive:
\[
\{1,3,5,7,8,10,12,14\},
\qquad
\{2,3,4,5,10,11,12,13\}.
\]
The first is \(h_{00}\ne h_{11}\), the second \(h_{01}\ne h_{10}\), proving (22). The verification has 81 candidate sets of size eight and at most 56 three-element checks per set; it requires no SAT or optimization algorithm. QED.

**Caution.** Both equality patterns are possible *abstractly* as 2-CNF solution families, since each is defined by the conjunction of the two clauses expressing unequal bits. This classification does not exhibit cycle-local colorings with eight failures. The finite six-dimensional census with a shared projection or conjunction found no failures for any of the sixteen common functions.

**Closure implication.** If a hypothetical shared-site obstruction fails for half the possible local functions, it must localize to a single antipodal input-pair disagreement. Excluding these two extreme patterns via a square-exchange or path-monodromy argument would improve the universal guaranteed-success count from eight to nine. To prove the full shared-site theorem, the remaining smaller majority-closed failure sets must ultimately also be ruled out.

### Universal cross-favorability on a path: 66-core finite induction

**Theorem (all-dimensional, computer-assisted).** For arbitrary binary edge colorings f,g of Q_n whose union direction-interaction graph is contained in a path, there is a root with a full dimension-simple 0*1* geodesic for f and a full dimension-simple 1*0* geodesic for g. No assumptions of affine dependence, antipodal oddness, or root-density bounds are required. The two full direction orders may differ.

**Geometry.** Write u_i=1 if dimension i precedes i+1 in the f-order, and v_i=1 for the g-order. With root bits x and traversed color bits c_i,d_i, for each internal direction
\[
c_i=F_i(x_{i-1}+u_{i-1},x_{i+1}+1-u_i),\qquad
d_i=G_i(x_{i-1}+v_{i-1},x_{i+1}+1-v_i)
\]
over F2. A compatible pair of monotone full paths exists if and only if, on every edge i,i+1,
\[
u_i=1\Rightarrow c_i\le c_{i+1},\quad u_i=0\Rightarrow c_{i+1}\le c_i;
\]
\[
v_i=1\Rightarrow d_i\ge d_{i+1},\quad v_i=0\Rightarrow d_{i+1}\ge d_i.
\]
Sufficiency follows by ordering the two color phases topologically inside their oriented interaction paths, which have no directed cycles.

**Inductive state.** Retain six bits
\[
(a,b,u,v,c,d)=(x_i,x_{i+1},u_i,v_i,c_i,d_i).
\]
For arbitrary next two-input Boolean rules F,G, choose a new starting bit z and next orientation bits u',v', and compute
\[
c'=F(a+u,z+1-u'),\qquad d'=G(a+v,z+1-v').
\]
The successor state is (b,z,u',v',c',d') if both oriented color inequalities hold. There are 64 boundary states and 256 possible interior rule pairs.

**Finite inductive certificate.** The independently preserved file nori_path_induction_66_masks.txt lists 66 explicit masks of these 64 states. A dependency-free Python checker verifies: (i) every one of the 16 paired initial endpoint tables produces a reachable state set containing a listed mask; (ii) the image of every listed mask under each of the 256 interior rules contains another listed mask; (iii) every listed mask meets the successful final state set for every one of the 16 paired terminal endpoint tables. This is 16896 interior-extension checks. By induction, every path length has a compatible final state, proving the theorem.

The SHA256 digest of the 66-mask file is 3c0450114b54eb377ade6e7412b9b5bcd3bb8b8f999bb73b1eeaab59eefb7d4b. An independent full saturation produces 3191 reachable boundary-state sets, of which these 66 are inclusion-minimal. Direct geodesic dynamic programming agreed with the orientation method in 128792 separate comparisons, including all path-local coloring pairs in dimensions two and three. The finite induction is machine checked; no short conceptual classification of the 66 masks is presently claimed.

**Cyclic constant-site corollary.** If two cyclic-local colorings have a direction j whose color is constant in each coloring, fixing bit j leaves two path-local colorings. Apply the theorem to the necessary fibers, then insert j at the beginning or end of the two monotone geodesics according to its color pair: (0,1) first in both; (1,0) last in both; (0,0) first in f and last in g; (1,1) last in f and first in g. Choosing the fiber before or after the bit toggle ensures a common root. Hence any such cyclic-local pair is cross-favorable. The previously proved pendant-tree lifting and free-bridge equivalence then give the corresponding all-dimensional NORI1 closure class.

The unrestricted cyclic pair problem and NORI1 remain open.

#### Eight-prototype refinement of the 66-mask induction

The preceding 66-mask certificate admits a much smaller representation. Identify its 64 boundary states with six-bit integers s (in bit order a,b,u,v,c,d). For a state-set mask M and a six-bit translation k, let
\[
\boxed{\tau_k(M)=\sum_{s:\,M_s=1}2^{s\mathbin{\mathrm{xor}}k}.}
\]
Thus tau_k permutes the 64 states by independently flipping any selection of their six bits.

The entire inductive certificate is the union of translation orbits of just **eight prototype masks**:
\[
\begin{array}{ll}
P_1=\mathtt{000000000000ffff},&
P_2=\mathtt{000000003c3cc3c3},\\
P_3=\mathtt{000033cc0000cc33},&
P_4=\mathtt{0140314cc143fd7f},\\
P_5=\mathtt{03c0300cc0030c30},&
P_6=\mathtt{11441144dd77dd77},\\
P_7=\mathtt{1414d7d71414d7d7},&
P_8=\mathtt{5555555555555555}.
\end{array}
\]
Their respective orbit sizes under k in F2^6 are 4,4,4,32,4,8,8,2, totaling **66 distinct masks**. Four orbit types are affine codimension-two state constraints, one is a half-cube, and the remaining three are more flexible nonlinear state conditions.

**Eight-prototype certificate theorem.** Generate the 66 masks by all tau_k(P_i). With the six-bit transition map defined above, the generated family satisfies:
(1) every first-direction reachable mask contains a generated mask;
(2) for each generated mask and each of 256 interior paired color tables, its successor mask contains a generated mask;
(3) every generated mask intersects every terminal-success mask.

An independent standalone Python verifier, **nori_path_8_prototype_induction.py**, contains all eight hexadecimal constants, generates the 66 masks by XOR translation, and directly checks the three properties with no external data files or dependencies. Output: PASS, 66 inductive cores, 16896 extension checks, all initial and terminal tables. SHA256 of the verified Python file:
\[
\mathtt{7ed6dbc8034dae69f4c644b44b8f0df72c904e43f340fcd87d5ce7dfb9a2edc8}.
\]

This eight-prototype presentation supersedes the need for a 66-line externally stored list as a proof certificate. The translation closure is a convenient description of the masks; **it is not assumed that each individual transition commutes with every translation**. Instead the verifier checks the full generated family for closure. A conceptual derivation of the eight shapes, in particular their nonlinear orbit types, remains an attractive further step.

#### Constructive linear-time witness extraction and linear forests

**Theorem (constructive version).** The path-local pair theorem is algorithmic: from the local Boolean edge-color tables F_i,G_i on a path of n dimensions, one can construct a common starting root x and two full dimension-simple monotone geodesic orders in **O(n)** time and space.

*Proof.* Maintain for each of the 64 six-bit boundary states either no predecessor or one predecessor state witnessing reachability. The initialization, eight possible successors per state per interior direction, and terminal test are given by the transfer equations above. The verified eight-prototype invariant guarantees that some terminal state succeeds for every input sequence. Store predecessor pointers at each position, requiring O(64n) memory. Backtrack from a successful terminal state to recover all root bits x_i, f-orientation bits u_i, g-orientation bits v_i, and traversed edge colors c_i,d_i.

Build the directed path with edge i−(i+1) oriented according to u_i. Its inequalities exclude directed arrows from the f-one phase into the f-zero phase, so topologically sort the induced f-zero subgraph and then the induced f-one subgraph. This gives the required f-geodesic. Similarly topologically order the g-one subgraph first and the g-zero subgraph last using the v-orientations. Each topological sorting step is linear in n and traverses each dimension once. The result is a constructive pair of monotone full geodesics starting at the same recovered root. QED.

**Independent implementation.** The self-contained Python program nori_path_constructive_solver.py implements this procedure and independently evaluates each reconstructed path against the original edge-color truth tables. It passed 720 independent witness checks, including random dimension-100 path-local pairs. Its SHA256 is 13afaeaddb9b57a6795631fe7651338c755be00681423127572eb60fd45b75a3. These tests audit the constructor; the all-input guarantee is supplied by the eight-prototype induction.

**Corollary (linear forests).** The same cross-favorability assertion and constructive linear-time algorithm hold when the union direction-interaction graph is a *disjoint union of paths*, rather than a single path. Apply the path theorem independently to each connected component and concatenate the component paths, taking all f-zero phases before all f-one phases, and all g-one phases before all g-zero phases. Edge colors in separate components are independent of the other component bits, so each component can be traversed without disturbing the other. The starting roots concatenate to give one common root. Each direction is traversed once.

The theorem therefore settles all binary coloring pairs with union interaction graph a linear forest, in arbitrary dimension and with unrelated nonlinear local functions. A minimal cross-root obstruction must contain either an interaction cycle or a vertex of degree at least three in the union graph.

#### Boundary-fiber obstruction to a stronger path induction

The universal path-pair theorem cannot be strengthened by prescribing either endpoint starting bit. In Q4 with path directions 0,1,2,3, encode endpoint one-input color truth tables by two-bit integers and internal two-input tables by four-bit integers, indexing the latter by left+2*right. Take f local truth tables (2,10,12,2), and g tables (2,5,3,2). Direct geodesic reachability from every root gives

A0(f) intersect A1(g) = {0000, 0010, 0100, 0110}

with written bit order x3 x2 x1 x0. Thus every common root has x0=x3=0. There is no common root on either face x0=1 or x3=1, nor with x0+x3=1. Yet the unconditioned cross-root theorem succeeds at four roots.

This finite example refutes the stronger endpoint-prescribed claim without challenging the path theorem. It shows why a cyclic proof cannot simply impose a prescribed endpoint parity on the 66-core induction: adding the closing interaction edge requires a richer boundary relation or a change in the witness orders. The root set was independently checked over every permutation of the four directions and every starting root.
