# Incidence-tree labels on central Freudenthal

- Stable ID: note_nori_xvii_incidence_tree_labeling_freudenthal_r12147_3
- Author: unspecified; session provenance retained
- Primary home: subsection:central_freudenthal_subdivision_and_the_all_root_geodesic_chamber_sphere
- Labels: NORI1, topology, structural-representation
- Lifecycle: active
- Epistemic status: proved
- Current version: 5
- Retention: current and at most one previous snapshot
- Created session: session_nori_r12147_3
- Updated session: session_nori_r12147_3
- Disposition: none
- Successor: none

## Related references

- None

## Research note

Session session_nori_r12147_3. On a type-D chamber tree T, let R(v),B(v) be the red and blue connected components. Make a bipartite graph I(T) whose component vertices are R and B and whose edge labeled v joins R(v),B(v). THEOREM: I(T) is a tree with 2^n labeled edges. Indeed if T has N=2^n vertices and red/blue edge counts r,b, then its two component counts sum to (N-r)+(N-b)=N+1. The graph is connected because adjacent original tree vertices give incident edges. Thus it is a tree. Its labeling is injective. If P_T(v,w) has s color switches then the corresponding labeled edges in I(T) have line-graph distance s+1: each maximal monochromatic run passes through one component node, and component recurrence is impossible in a tree. Hence a chamber tree has a monochromatic antipodal geodesic iff some edge pair labeled v,bar(v) in I(T) is incident. For each face sigma of the type-D coarsening of the central Freudenthal complex, let F_sigma be the common-edge intersection of all incident chamber trees. F_sigma is a forest. Its incidence graph I(F_sigma) is a bipartite forest; component inclusion gives canonical graph maps under face inclusion, strictly coherent for all higher-dimensional faces. Antipodality swaps component bipartitions and sends label v to bar(v). Under a hypothetical globally bad coloring all antipodal labeled-edge pairs are disjoint in every such forest. WARNING: each forest incidence vector e_R-e_B is independent of the others, so a direct rook-root map has ambient dimension N rather than n-1. No low-dimensional equivariant forcing target has been constructed. A single fixed-root top relative class cannot have a winning-geodesic-supported representative, since some legal colorings have a root without any monochromatic complete path. This is a proposed new label and a proved graph representation, NOT a NORI1 closure.

## Geodesic-packet resolution and the core component (session session_nori_r12147_3)

For every type-D chamber tree T, write e_* for the unique edge shared by every antipodal tree geodesic. Let K(T,c) be the tree component of the color of e_* containing that edge. Then T contains a monochromatic antipodal geodesic if and only if K(T,c) contains antipodal vertices. This follows because all antipodal tree paths use e_*, hence any such monochromatic path must lie entirely in K. Thus the full red/blue incidence tree is unnecessarily large for a SINGLE chamber: the central component is the complete chamber-level existence certificate.

Rank directions i_1,...,i_n and root the canonical tree at its reference vertex g. Identify vertices with subsets S of directions flipped from g. Each nonroot parent deletes the maximum-ranked member of S. Hence K is an ancestral subtree containing both g and g xor e_(i_1). Define b_i(K)=sum_(v in K) (-1)^(v_i). 

LEMMA (transverse centroid). If b_(i_2)(K)=...=b_(i_n)(K)=0, then K contains EVERY cube vertex.

PROOF. Every vertex of K having its largest-ranked bit i_n flipped has its counterpart with i_n unflipped in K. The corresponding injection implies b_(i_n) has a fixed nonnegative sign relative to g, and equality means K is invariant under toggling i_n. Remove that direction and iterate down ranks i_(n-1),...,i_2. Equality in all these marginal counts makes K invariant under each of those directions. Since K contains both endpoints of the central i_1 edge, K is the whole cube. QED.

CAUTION. For n>=2 the highest-ranked tree edges include antipodal edge pairs; a legal odd coloring colors each pair oppositely. Thus K is NEVER the entire tree, even when NORI1 succeeds. The transverse centroid is nonzero in every legal coloring, not merely in a conjectural bad one. Any topological zero would have to arise through higher-face gluing, and such a zero is not automatically a good-path witness. The singleton central-edge subtree already has the same pointwise nonvanishing property independent of the coloring.

## Homotopy type of the UNCOLORED packet resolution

Fix any root r. Over a central Freudenthal face sigma, let Q_(sigma,r) be the convex hull in the standard order permutohedron of all rooted orders realized by chambers refining sigma. The relevant orders are the refinements of one weak order. Consequently Q_(sigma,r) is a nonempty face of a permutohedron and is a product of smaller permutohedra, hence contractible. Face incidence gives canonical inclusions of these packet polytopes in the reverse face direction. Their homotopy colimit has a natural projection to the classifying realization of the central face poset. Since the objectwise natural transformation Q_(sigma,r)->point is a weak equivalence, this projection is a homotopy equivalence.

For all roots simultaneously, the uncolored packet resolution is equivariantly homotopy equivalent to L_n times the discrete root set Q_n, with antipodality acting on both factors. This follows because the contractions to the one-point fibers are natural and antipodally compatible.

IMPLICATION. Filling every packet polytope and all of its face attachments without reference to color creates NO new homotopy obstruction beyond the original central Freudenthal sphere. The color-sensitive geometry MUST modify a fiber or an attaching map in a way not killed by these natural contractions. Merely counting or preserving the full set of rooted orders over faces is geometrically faithful but topologically inert. This is a method limitation, not a proof of NORI1. Further work should identify a color-defined obstruction with an integral full-geodesic witness at its critical cell, while respecting all square and braid attachments.


## Local realizability of antipodal-free central components (session session_nori_r12147_3)

Fix a type-D chamber tree T with ranks i_1,...,i_n, a reference corner g, and the central first-rank edge e_*. Let K be a connected vertex subtree of T containing e_* and no pair of antipodal vertices. It is an ancestor ideal when T is rooted at g. Split K by its highest-ranked direction i_n into lower and upper sets K_0,K_1, translated into the same (n-1)-cube. Ancestral closure gives K_1 subset K_0. Define the top frontier D=K_0 minus K_1.

THEOREM. A legal antipodally odd edge coloring of the ENTIRE original Q_n can have K as the monochromatic component of e_* in T if and only if D contains no antipodal pair in Q_(n-1).

PROOF OF NECESSITY. Every T edge crossing from K to its complement must have color opposite that of e_*. Therefore two antipodal T-edges cannot both cross this boundary. For a rank i_r lower than n, every T edge has a fixed higher-ranked exterior bit equal to g, while its antipodal mate has that bit different. Hence both cannot belong to T. For rank i_n, T contains all edges in that direction, and their antipodal pairs are indexed by antipodal lower-dimensional positions. Such a highest-rank edge meets K in one endpoint if and only if its lower position lies in D=K_0 minus K_1. Therefore D cannot contain antipodal positions.

PROOF OF SUFFICIENCY. Color every T edge with both endpoints in K by a chosen bit a, and every T edge with just one endpoint in K by 1-a. Antipodal-freeness of K ensures no pair of interior edges are antipodal. The frontier condition precludes boundary-versus-boundary antipodal conflicts. An interior edge and the antipode of a boundary edge, when both belong to T, receive opposite prescribed colors, as required. All remaining edge orbits can be assigned either bit independently, with their antipodal mates complemented. The component of e_* of color a is then precisely K. QED.

This characterization was cross-checked by complete enumeration of legal Q_3 and Q_4 colorings for a fixed chamber tree: the counts of distinct antipodal-free central components were respectively 4 and 100, matching the ancestral-ideal/frontier criterion.

SIGNIFICANCE. A single chamber's central label is not an arbitrary antipodal-free connected subtree: legal global edge coloring imposes an additional antipodal restriction on its highest-rank boundary. Conversely these two restrictions characterize EVERY locally possible bad central component. The unresolved issue is how the frontiers of such components must agree across ALL adjacent chamber trees through the original shared edge colors. Any NORI1 forcing must exploit this global multi-chamber compatibility rather than one subtree or the contractible uncolored path packet.


DEMICUBE LOW-INDEX TARGET (session session_nori_r12147_3). For n=2m>=4 let E,O be even/odd cube vertices. Every odd w has n even neighbors spanning a simplex facet of the even demicube D_E. Take its red-neighbor face R_w and blue-neighbor face B_w, and put U_E=union_w(R_w union B_w). An edge of red union R_w is a valid two-edge red original cube path through w. Thus NORI1 is equivalent to a length-m antipodal 1-skeleton path in the red complexes of E or O. Legal antipodal oddness interchanges red and blue subcomplexes of the same parity. Two different generating colored star simplices overlap in at most one demicube edge, since distinct odd vertices have at most two common even neighbors. Coning each simplex over its shared 1-skeleton gives an antipodally equivariant 2-dimensional CW model of U_E. Hence its projective covering class has vanishing third cup power. In contrast L_n/tau is RP^(n-1), with nonzero third power, so no equivariant map L_n->U_E exists. This is unconditional and not NORI1 closure: the even-central-edge-endpoint map naturally extends equivariantly to the whole demicube sphere, but not necessarily into U_E. Missing demicube edges arise where both original two-edge square routes switch color. The needed no-bad-geodesic-specific selector into U_E is open.


## Audit: the degree-three relative obstruction is universal, not color-induced (session session_nori_r12147_3)

Keep n even >=4, the even demicube D_E, and U_E(c)=R_E(c) union B_E(c). Define the UNCOLORED subcomplex Sigma_E=union_(w odd) F_w, where F_w is the full simplex facet on all n even neighbors of w. Then U_E(c) subset Sigma_E for every coloring, since each monochromatic star simplex is a face of F_w.

Distinct F_w meet in at most one edge: two distinct odd vertices share at most two even neighbors. Replacing each F_w by the cone on its 1-skeleton, with antipodally paired replacements, gives a free equivariant 2-dimensional homotopy model for Sigma_E. In particular the antipodal quotient class a satisfies a^3=0 on Sigma_E/tau, without reference to c.

The subcomplex Sigma_E contains the FULL 2-skeleton of D_E. Every triangular 2-face comes from three of the four even vertices in an original 3-cube; those three are neighbors of one odd vertex and therefore span a triangle in its simplex facet. The 3-dimensional demicube cells corresponding to the four even vertices of an original 3-cube have entire boundaries in Sigma_E but their interiors outside Sigma_E. Those universal missing 3-cells, not coloring-dependent missing 1-edges, already support the degree-three relative obstruction.

Let Y=boundary(D_E)/tau, S=Sigma_E/tau, A=U_E(c)/tau. For all c, the restriction of u^3 in H^3(Y) to S vanishes. Thus it has a relative lift omega_geom in H^3(Y,S). Under the map induced by (Y,A)->(Y,S), the class omega_geom gives a relative lift in H^3(Y,A), for every c. The degree-three obstruction from the previous note therefore has a UNIVERSAL COLOR-FREE source; it is not a discriminant for successful versus unsuccessful NORI1 colorings.

The inclusion U_E(c) subset Sigma_E can be equality even for a colorable cube with a monochromatic antipodal geodesic. Define c(vw)=w_0, where w denotes the odd-weight endpoint of the original edge and n is even. Since the antipode of an odd vertex is odd and flips bit zero, c is legal. Every odd-centered star is monochromatic, so U_E(c)=Sigma_E. Traversing dimensions 1,2,...,n-1,0 from root 0 produces a red full geodesic. In dimension four Sigma_E has eight even vertices, 24 graph edges, all 32 triangular faces of D_E, and eight of its 16 tetrahedral facets; the other eight tetrahedra come from original cube 3-faces.

Even the COLOR-DEPENDENT choices of triangular boundary faces of one original 3-cube admit arbitrary local patterns. Its four odd corners are pairwise nonadjacent, and the three original edges incident to each such corner are disjoint from the triples at the other corners. For each corner independently, prescribe all three colors equal to INCLUDE its triangle in U_E, or a mixed triple to EXCLUDE it. For n even >=4 that 3-cube and its antipodal mate are disjoint, so all 16 patterns extend to one legal global odd coloring by prescribing antipodal complements and filling remaining edge orbits. Hence no parity restriction on the four triangle-presence indicators follows from one tetrahedral 3-cell and legal edge consistency alone. Restrictions would have to couple MULTIPLE adjacent 3-cubes, their common original edges, and complete path packets.

Research decision: do not use the bare relative degree-three class as the proposed NORI1 forcing mechanism; its source is uncolored. Distinguish a future color-sensitive secondary obstruction from this universal class before considering any higher chain-map construction. This does not disprove that a more elaborate diagram incorporating colored 2-faces and full geodesic completions can work.
