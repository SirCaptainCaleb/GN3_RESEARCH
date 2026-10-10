# Holmsen–Martínez-Sandoval–Montejano: q-star completions and higher-order Hall selection (2016)

**Summary:** An extension property against any 2k+2 vertices forces k-connectivity of a higher-order compatibility complex, yielding rainbow selection by topological Hall. Unlike edge-clique methods, completion can track forbidden triples and larger configurations—potentially significant for NORI's joint path realization.

## Statement

For a d-dimensional simplicial complex K, if K is (2k+2)-star, then its d-completion is k-connected (Lemma 4.4). Via Kalai–Meshulam, every finite family of planar/spatial point sets whose subfamily unions have sufficiently large general-position subsets admits rainbow general-position representatives; the Hall function is O(j^d). The proof extends to matroid uniformity complexes.

## Body

# Higher-order compatibility, q-star connectivity, and topological rainbow selection

**Source and provenance:** A. F. Holmsen, L. Martínez-Sandoval and L. Montejano, *A geometric Hall-type theorem*, Proceedings of the American Mathematical Society **144** (2016), 503–511, DOI https://doi.org/10.1090/proc12733 . Open full paper (arXiv v3, January 2015): https://arxiv.org/pdf/1412.6639 ; abstract https://arxiv.org/abs/1412.6639 . Precise references below: Theorems 1.1, 3.1, 5.1; Proposition 3.3; Lemma 4.4.

## The higher-order compatibility complex

For a finite multiset X⊂R^d, write φ(X) for the maximal cardinality of a subset in general position, meaning every subset of at most d+1 points is affinely independent. Let
  G(X) = {S⊆X : S is in general position in R^d}.
This is a simplicial complex, **not** generally a flag (clique) complex: in R^2 all pairs may be legal while some triples are collinear.

For any simplicial complex K of dimension d, define its d-completion:
  Δ_d(K) = K ∪ {S : |S|≥d+2 and every (d+1)-subset of S is in K}.
Because K is downward-closed, it is enough to check the (d+1)-subsets. If K is the rank-(d+1) matroid independence complex of a spanning configuration X in R^d, then G(X)=Δ_d(K). It is important that **the completion retains all the higher-order constraints on small supports**; it is not an invitation to declare arbitrary pairwise-compatible families simultaneously realizable.

## q-star extension lemma (Lemma 4.4)

Let K have dimension d, let q≥1, and write K[Y] for the induced subcomplex on Y. Say K is **q-star** if |V(K)|>q and, for every Y⊂V(K) of size q, there is v∈V(K)\Y with
  S∪{v}∈K
for every S∈K[Y] of size at most d.

**Lemma 4.4 (Holmsen–Martínez-Sandoval–Montejano).** If K is (2k+2)-star for k≥0, then Δ_d(K) is k-connected.

The lemma is an honest extension-to-connectivity principle: every (2k+2)-vertex set admits one vertex simultaneously extending *all its legal subsets of size ≤d*. It is considerably stronger than an ability to extend just one chosen compatible pair or simplex.

**Proof architecture (§4).** Cover the completed complex by vertex stars. Their intersections can be expressed via d-completions of certain neighborhood complexes Γ_K(v); the q-star hypothesis descends to these intersections with fewer required vertices. Apply induction on k and the homotopy nerve theorem. The q-star assumption forces the nerve to have a complete (2k+1)-skeleton, giving enough connectivity. This is not an independent new proof, but a map of the published argument.

## Topological colorful-simplex / Hall principle (Proposition 3.3)

Let L be a simplicial complex with vertices partitioned into nonempty color classes V_1,…,V_m. Put L_I = L[⋃_{i∈I}V_i]. If for every nonempty I⊆[m], **L_I is (|I|−2)-connected**, then L contains a simplex with exactly one vertex from every color class. This Kalai–Meshulam sufficient condition is the bridge from topology to rainbow selection.

In particular, to use the q-star lemma, one may prove for every I that L_I is a suitable completion Δ_d(K_I) with enough q-star extension to guarantee connectivity |I|−2. Merely proving an abundant number of vertices, or pairwise compatibility in the underlying one-skeleton, does not establish connectivity.

## Quantitative geometric consequence (Theorems 1.1 and 3.1)

For each fixed d≥1 there is a function f_d:N→N such that finite X_1,…,X_m⊂R^d admit representatives x_i∈X_i in general position whenever
  φ(⋃_{i∈I} X_i) ≥ f_d(|I|)
for every nonempty I⊆[m]. Repeated points from distinct colors can be treated as formally distinct occurrences.

The authors prove f_d(j)=O(j^d) for fixed d. A concrete sufficient choice obtained from their bounds is
  f_d(j)=j for 1≤j≤d+1,
  f_d(j)= d*C(2j−2,d)+1 for j≥d+2,
where C(a,b) is the binomial coefficient. The low-index case uses matroid intersection; for j≥d+2, set k=j−2≥d and combine Theorem 3.1's g_d(k)≤d*C(2k+2,d)+1 with Kalai–Meshulam (Prop. 3.3). The introductory text also gives an elementary O(j^(d+1)) proof based on large in-general-position subsets.

Geometric proof of the q-star bound: given q=2k+2 existing points, the d-tuples span at most C(q,d) hyperplanes. Any in-general-position set puts at most d of its points in each such hyperplane. If φ(X)>d*C(q,d), one can choose a point avoiding **all** those hyperplanes, simultaneously extending every affinely independent subset of size ≤d. Apply Lemma 4.4.

## Arbitrary matroid extension (Theorem 5.1)

For a **loopless matroid** M of rank r≥2, call S uniform if either S is independent or every r-subset of S is independent. All uniform sets form the (r−1)-completion of the matroid independence complex. Write μ(M) for the maximum size of a uniform set. Theorem 5.1 shows that μ(M) sufficiently large makes this uniformity complex k-connected. The paper proves the explicit sufficient inequality
  μ(M) > (r−1)*C(2k+2,r−1)
in the range where this rank-bound argument applies, by verifying the q-star condition; lower k can be handled by matroid independence complex connectivity. Applying the same colorful-simplex criterion yields uniform systems of representatives. This is a genuinely combinatorial, non-Euclidean extension.

## Why this is potentially closer to NORI than pairwise matching

The source explicitly emphasizes that general position is NOT a pairwise property for d≥2. Completion and q-star connectivity capture higher-order constraints, unlike ordinary clique complexes or edge-disjointness graphs. This resonates with NORI's established distinction between a clique of locally consistent window data and a simultaneously realizable full ordered-face path.

**Critical research test:** build a simplicial complex L whose simplices are *exactly jointly realizable finite families of NORI physical path certificates* (with root, direction-order, exterior-bit, and seam provenance). Then establish induced-subcomplex connectivity or a q-star-type augmentation property for all relevant index subfamilies. Only if a colorful simplex of L can be proven to decode to a single physical antipodal geodesic of at most one change would topological Hall yield the grand conjecture. The "exactly jointly realizable" condition is the hard mathematics, NOT an automatic consequence of local extendibility. No NORI closure claim is made.

## Relation to other Toolkit records

literature_aharoni_haxell_economically_hierarchic_sperner_construction (economically hierarchic simplex triangulation, pairwise compatibility);
literature_aharoni_chudnovsky_kotlov_triangulated_spheres_colored_cliques (graph compatibility and controlled sphere-to-ball filling);
literature_martinez_montejano_geometric_hall_tight_triangulations_2013 (geometric Hall instances).

## Metadata

- ID: literature_holmsen_martinez_montejano_general_position_complex_q_star_2016
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
