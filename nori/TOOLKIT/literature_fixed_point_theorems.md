# Literature Fixed Point Theorems

**Summary:** One toolkit entry for fixed-point and cubical-labeling theorem statements; proofs, research cautions, and application discussions are gathered at the end.

## Statement

Consolidated fixed-point and combinatorial-topology reference: Brouwer, Borsuk–Ulam, Poincaré–Miranda, Sperner/KKM, Tucker, cubical Sperner, generalized Hex, and related variants. Precise hypotheses and conclusions appear together before all discussions.

## Body

# Literature Fixed Point Theorems

A single theorem-first reference for fixed-point, antipodal-labeling, cubical/polyhedral Sperner, KKM, Hex, and closely related separation theorems. **All theorem statements and their hypotheses appear first.** Sources and verification limits are identified alongside statements. Proof explanations, methodological cautions, NORI-specific interpretations, and the discussions formerly scattered through the separate toolkit entries are consolidated at the END.

Notation: I^d=[0,1]^d; Q_d={0,1}^d; a label in {0,1}^d is identified with a coordinate subset of [d]; "neutral" means BOTH 0 and 1 appear in each coordinate across the labels of a simplex. No neutrality theorem below alone asserts an exactly complementary pair of whole bit strings.

# I. Theorem statements

## A. Classical fixed-point and antipodal theorems

**A1. Brouwer fixed-point theorem.** Every continuous map f:K→K on a nonempty compact convex subset K⊂R^d has a fixed point x=f(x). In particular every continuous self-map of the d-cube or d-ball does.

**A2. Borsuk–Ulam theorem.** Every continuous map f:S^d→R^d identifies some antipodal pair: f(x)=f(−x). Equivalently, every continuous antipodally odd map f:S^d→R^d has a zero. Consequently there is no equivariant map S^d→S^(d−1) for their antipodal involutions.

**A3. Poincaré–Miranda theorem.** If f:I^d→R^d is continuous, f_i(x)≤0 on the facet x_i=0 and f_i(x)≥0 on the opposite facet x_i=1, for each i (or all inequalities simultaneously reversed), then some x∈I^d has f(x)=0.

**A4. Ham-sandwich theorem, discrete version.** For finite P_1,…,P_d⊂R^d there is an affine hyperplane H such that each open halfspace bounded by H contains at most ⌊|P_i|/2⌋ points of P_i for every i. It follows from the continuous ham-sandwich/Borsuk–Ulam theorem by perturbation or thickening. (Preserved from literature_discrete_ham_sandwich_theorem.)

**A5. Brouwer projected normal-cone alternative.** Let Q be a nonempty compact convex polytope in its affine span E, and V:Q→E continuous. For ε>0 define T_ε(x)=Proj_Q(x−εV(x)). A Brouwer fixed point x of T_ε satisfies −V(x)∈N_Q(x), or equivalently ⟨V(x),z−x⟩≥0 for all z∈Q, with N_Q the outward normal cone of Q. If x lies in the relative interior of Q, then V(x)=0. (Former projected_brouwer_normal_cone_alternative.)

## B. Simplicial and polytopal Sperner/KKM

**B1. Sperner's lemma.** Triangulate a d-simplex Δ with vertices v_0,…,v_d. Label each triangulation vertex lying in a face spanned by {v_i:i∈J} by an index from J. Then some d-simplex in the triangulation has all d+1 distinct labels (indeed an odd number of top simplices are fully labeled in the standard parity form).

**B2. KKM covering lemma.** Let closed sets F_0,…,F_d⊂Δ have the property that for each nonempty J⊆{0,…,d}, the face conv{v_j:j∈J} lies inside ⋃_(j∈J)F_j. Then ⋂_(i=0)^d F_i is nonempty.

**B3. Colorful KKM (Gale).** Given d+1 families (F_i^j)_(i=0,…,d), j=0,…,d, each family consisting of closed sets satisfying KKM's face-covering condition, there exists a permutation π of {0,…,d} with ⋂_(i=0)^d F_i^(π(i))≠∅. The conclusion is a rainbow *intersection* under KKM hypotheses, not necessarily a common discrete Boolean label.

**B4. Polytopal face-respecting Sperner packet theorem.** Let Q be a convex polytope and T a triangulation. For every triangulation vertex x choose a vertex λ(x) of the minimal face of Q containing x. Then some simplex σ of T has a point y∈σ∩conv{λ(x):x a vertex of σ}. Equivalently, the continuous piecewise-affine label map f:Q→Q has a fixed point. This is a direct application of Brouwer. (Former polytopal_sperner_packet_theorem_for_face_respecting_labels.)

**B5. Barycentric subset-choice corollary.** If ℓ(S)∈S for every nonempty S⊆[d], then there exists a permutation π=(π_1,…,π_d) such that for every k=1,…,d,
ℓ({π_1,…,π_k})=π_k.
Proof is Sperner on sd(Δ^(d−1)): maximal simplices are nested subsets, and their distinct labels must be the successive newly added coordinates. (Former sperner_choice_rule_on_the_completed_cube_boundary.)

## C. Tucker, Ky Fan, cubical and octahedral labeling

**C1. Classical Tucker's lemma.** For an antipodally symmetric triangulation of the d-ball boundary extended to a triangulated d-ball, a labeling of vertices by {±1,…,±d} satisfying ℓ(−v)=−ℓ(v) on boundary vertices has an edge whose two labels are i and −i. (The labeled domain may be a crosspolytope with the usual antipodal triangulation.)

**C2. Cubical Tucker, Grant–Ma Theorem 1.9.** Triangulate a d-ball with antipodally symmetric boundary, assign each vertex λ(v)∈{−1,+1}^d, and require λ(−v)=−λ(v) on boundary vertices. Then some simplex σ is *neutral*: for every coordinate i its vertex labels exhibit both signs. This is NOT an unconditional guarantee that two of its labels are complete bitwise complements.

**C3. Cubical Sperner with cubical labels, Grant–Ma Theorem 1.5.** Triangulate [−1,1]^d and assign every vertex an n-component sign vector λ∈{−1,+1}^d, respecting the signs on prescribed cube boundary facets: if vertex x has x_i=±1 then λ_i(x)=x_i. Then some simplex is neutral.

**C4. Cubical Sperner with octahedral labels, Grant–Ma Theorem 1.6.** Triangulate [−1,1]^d and label vertices by ±e_i (the 2d vertices of the d-crosspolytope). Impose its stated cubical boundary rule: if x_i is fixed at ±1, forbid the opposite signed label −x_i e_i. Then a simplex contains an edge bearing opposite labels ±e_j.

**C5. Octahedral Sperner with cubical labels, Grant–Ma Theorem 1.7.** Triangulate the d-crosspolytope. Label vertices with vectors from {−1,+1}^d under the theorem's supporting-facet restriction: when x belongs to the facet supported by sign vector v, the label may not be −v. A neutral simplex exists. Consult the paper for all equivalent ways of stating the supporting-face restriction.

**C6. Kuhn's cubical Sperner theorem (scalar).** Appropriate simplex-style labels 1,…,d+1 on a unit-grid subdivision of a d-cube, with the cubical boundary admissibility conditions of Kuhn's theorem, force a small unit cube that carries all d+1 scalar labels. Wolsey provides complementary-pivoting proofs and variants. The exact boundary convention varies across formulations; do not interchange it with (C7).

**C7. Binary cubical Sperner with neighborhood condition.** On the unit-grid subdivision of [0,M]^d, assign λ(v)∈{0,1}^d. Assume λ_i(v)=0 at v_i=0, λ_i(v)=1 at v_i=M, and neighboring grid vertices have labels at Hamming distance ≤1. Then some unit d-cube has all 2^d binary labels on its corners, including complete complementary pairs. The one-bit-neighborhood assumption is material.

**C8. Elementary chain-neutrality strengthening (proved combinatorial consequence).** Suppose labels on one simplex are a nested chain S_0⊆S_1⊆…⊆S_k⊆[d]. If they are cubically neutral, then S_0=∅ and S_k=[d]. Thus for *chain-compatible* labels, C2 yields an exact complementary pair, subject to its antipodal boundary hypothesis.

**C9. Ky Fan alternating-simplex lemma (qualitative form).** Under antipodally odd signed scalar vertex labels on an appropriate antipodally symmetric sphere triangulation, and with no complementary labeled edge, an alternating signed-label top simplex exists (and the classical parity refinement counts them oddly up to antipodal pairing). The exact sign/order/parity formulation depends on the triangulation and labeling convention. This is not a theorem about a pair of complementary d-bit strings.

## D. Higher-dimensional, colorful and multilabeled Hex

**D1. Gale's n-dimensional Hex theorem (1979).** Let the vertices of the finite board be [k]^d, with Hex adjacency between distinct coordinatewise comparable vectors whose coordinate differences are at most one in every coordinate. For every coloring of vertices with colors 1,…,d, there exists some color i with a connected i-monochromatic component meeting both opposite coordinate faces x_i=1 and x_i=k.

**D2. Tkacz–Turzański n-dimensional Steinhaus chessboard theorem (2008), Theorem 1.** Regularly subdivide a d-cube into k^d smaller d-cubes and color these cells by 1,…,d. There exists i and a chain of i-colored cells connecting the opposite i-faces, using the article's specified i-connected adjacency between cells. This is a cell-colored analogue of higher-dimensional Hex, with a connection to Poincaré–Miranda.

**D3. Baralić–Živaljević colorful Hex on a simple polytope (2017), Theorem 6.1.** Let P be a simple d-polytope with a proper d-coloring of its facets, and fix a vertex V. Write F_i(V) for the uniquely incident facet of color i. If P is covered by d closed sets X_1,…,X_d, then for some i a connected component of X_i meets F_i(V) and another, distinct facet of the same facet color i. The cube with opposite facet pairs carrying the same color specializes to the standard Hex conclusion.

**D4. Colorful Lebesgue covering theorem on a simple polytope, Baralić–Živaljević Theorem 3.1.** For a simple d-dimensional polytope admitting a proper d-coloring of facets, a finite closed cover of order/multiplicity at most d has some connected component of a cover member meeting two distinct facets of the same facet color. The cover-multiplicity hypothesis here is distinct from the d *named* covering sets in D3.

**D5. Tkacz–Piekarska multilabeled Hex (2023), Theorems 1 and 4 [partial source verification].** The paper establishes a combinatorial/algorithmic theorem for d+1 concurrent Hex games on cubical boards, involving a winning connected set with a multilabeled neighborhood certificate, and extends the construction to *d-essential abstract complexes*. It develops a topological Hex property related to Poincaré–Miranda and covering dimension, including equivalence statements for compact locally connected locally compact spaces. The FULL technical definitions of adjacency, “d-essential,” and all quantifiers of Theorems 1 and 4 were not verified from accessible full text; consequently this is a documented theorem *scope*, not a safe replacement for the paper's formal statement.

# II. Sources

- Brouwer/Borsuk–Ulam/Sperner/KKM/Poincaré–Miranda: standard foundational statements; derivations A5, B4, B5 are preserved from NORI toolkit research.
- Elyot Grant and Will Ma, *A Geometric Approach to Combinatorial Fixed-Point Theorems* (2013), arXiv:1305.6158, especially Theorems 1.5–1.9. https://arxiv.org/abs/1305.6158 ; https://www.columbia.edu/~wm2428/papers/combinatorial_fixed_point.pdf
- H. W. Kuhn, *Some Combinatorial Lemmas in Topology*, IBM J. Research and Development 4 (1960).
- Laurence A. Wolsey, *Cubical Sperner lemmas as applications of generalized complementary pivoting*, JCTA 23 (1977), 78–87, DOI 10.1016/0097-3165(77)90081-4.
- Oleg Musin, *Sperner type lemma for quadrangulations*, arXiv:1406.5082.
- David Gale, *The Game of Hex and the Brouwer Fixed-Point Theorem*, American Mathematical Monthly 86 (1979), 818–827, DOI 10.1080/00029890.1979.11994922.
- Przemysław Tkacz and Marian Turzański, *An n-dimensional version of Steinhaus' chessboard theorem*, Topology and its Applications 155 (2008), 354–361, DOI 10.1016/j.topol.2007.07.005.
- Đorđe Baralić and Rade Živaljević, *Colorful versions of the Lebesgue, KKM, and Hex theorem*, JCTA 146 (2017), 295–311, DOI 10.1016/j.jcta.2016.10.002; https://arxiv.org/abs/1412.8621 .
- Przemysław Tkacz and Maria Piekarska, *Multilabeled and topological versions of the Hex theorem*, Topology and its Applications 332 (2023), 108525, DOI 10.1016/j.topol.2023.108525; https://www.sciencedirect.com/science/article/pii/S0166864123001190 .

# III. Discussions, proofs and research applications (migrated to end)

## 1. Why exact opposite labels differ from continuous balance

Cubical Tucker, Poincaré–Miranda, Brouwer, and KKM typically supply a neutral simplex, a zero of a convexly interpolated vector field, or a balanced intersection. They do NOT automatically give one pair of complementary *whole* d-bit labels. For example the four sign/bit labels 000,011,101,110 average to the center (1/2,1/2,1/2), but no two are complements; three labels 000,011,101 are neutral without containing a complementary pair.

For arbitrary d-bit Tucker labels there are 2^(d−1) independent complementary pairs. An ordinary Tucker pairing of every label type with a signed scalar requires at least 2^(d−1) scalar magnitudes; in dimension d≥3, a direct complementary edge from unrestricted bit-vector labels is false. This obstruction is for arbitrary labels only; additional nestedness or reachability geometry can yield stronger conclusions.

The key *positive* observation is C8: if one neutral simplex consists of mutually nested *actual geodesic support labels*, min/max must be ∅/[d]. But the physical antipodal involution on the barycentric cube preserves the *set of used directions*, S(bar H)=S(H), whereas cubical Tucker's boundary hypothesis requires λ(−v)=complement(λ(v)). A two-family connector also requires both extremes to come from the correctly compatible families rather than arbitrary paths. Establishing these conditions is the missing mathematical work.

## 2. Cubical Sperner neighborhood condition and why it matters

The full-label binary theorem (C7) is stronger than mere neutrality but demands a full cubical grid, boundary signs on all opposite faces, and local label differences of at most one bit. Face boundary rules without neighbor locality do NOT force a fully labeled cell. Explicit n≥2 example: on {0,1,2}^n use λ_i(t)=1 iff t_i=2 for every point except m=(1,...,1), where set λ(m)=1^n. The boundary rules hold and no unit n-cell is fully labeled; neighbors of m may differ in n bits.

NORI *legal one-coordinate geodesic extensions* P→P' do satisfy d_H(S(P),S(P'))=1. But this holds only on existing legal transitions, not across edges of a whole filled grid. The NORI antipodal-reversal involution preserves used-direction supports rather than complementing them. Treating an abstract full grid as path-certified without proving every transition legal would assume what must be shown.

## 3. How Gale and Hex connect to Brouwer and to root/target carrier geometry

Gale's Hex theorem (D1) is a connected-component/facet-spanning statement and is famously equivalent to Brouwer's fixed-point theorem through discretization and interpolation. The Hex adjacency permits comparable diagonal moves, so a winning path can revisit coordinate directions or fail to be monotone. Tkacz–Turzański's cell-adjacency formulation similarly connects to Poincaré–Miranda but its i-connected path is not automatically a cube-graph shortest path.

On a polytope, Baralić–Živaljević establish D3 using a quasitoric manifold and a nonzero top cup product: if no color-i cover set component connects the required facets, corresponding cohomology classes become inessential on each cover member, contradicting the product. Theorem 3.1 instead constrains arbitrary cover multiplicity. The special-polytope and facet-coloring conditions are important and should not be silently dropped.

The multilabeled 2023 variant allows several games and works on the authors' n-essential complexes, which may be nonconvex, non-pure, or without a fixed-point property. It is attractive for *set-valued* reachability regions, because it avoids arbitrarily selecting one label per vertex, but its exact formal “winning neighborhood” theorem needs full-text verification before using it in a proof. A connected Hex region does not by itself provide a directed monochromatic GEODESIC with unused directions.

## 4. Sperner choice rules, polytopal packets, and projected Brouwer—preserved proof notes

B5 proof: triangulate Δ^(d−1) barycentrically by nonempty nested subsets S_1⊊...⊊S_d=[d]. The labels ℓ(S)∈S respect the supporting face. Sperner supplies a top simplex whose labels are all distinct. At rank k the previous k−1 labels have already selected the earlier elements; the only remaining possible distinct label is the new coordinate π_k. The completed Freudenthal cube's macroface opposite its distinguished vertex is precisely sd(Δ^(d−1)); this is the geometric interface previously used in NORI's Sperner choice-rule entry.

B4 proof: the affine interpolant f of face-respecting vertex labels sends every face into itself and is a continuous Q→Q map; Brouwer supplies y=f(y), and the triangulation simplex containing y realizes a convexly compatible label packet. This is useful for cut-, matching-, and support-valued labels, but a convex packet need not identify a single common discrete witness. Preserved older NOR discussion: centered hypersimplex p-cut vertices could serve as labels if a protected cut in each minimal face can be produced with root and side provenance. This carrier assumption was NOT proved.

A5 proof: metric projection onto Q is continuous. If x=Proj_Q(x−εV(x)), the projection characterization gives ⟨−εV(x),z−x⟩≤0 for every z∈Q, hence −V(x)∈N_Q(x). An interior fixed point forces the tangential field to vanish, whereas a boundary fixed point is only a normal-face certificate. Unlike hairy ball, the projected-Brouwer alternative is parity-free but requires a continuous field on the entire convex carrier. Preserved older NOR discussion: on a hypersimplex of protected p-cuts, a normal-face result might support induction on minimal carrier dimension, but constructing a provenance-preserving field is open.

## 5. Concrete NORI extraction: use the *current* reversed-terminal-pair theorem

For the active ordered-three-face coloring, the exact proved extraction target is NOT merely two abstract geometric labels meeting in a convex hull. Fix root x, ordered pair J=(a,b), and D=[n]\{a,b}. Let R_J(x) contain nonempty supports U⊆D witnessing some (EITHER-COLOR) monochromatic directed geodesic with direction order (permutation of U,a,b). Let R_revJ(x) use reversed terminal pair (b,a). The proved full grand-closure equivalence is:

  ∃ x,a,b,U:  U∈R_(a,b)(x), D\U∈R_(b,a)(x), with U and D\U both nonempty.

The reversed two-direction common tail absorbs the two ordered-three-face junction windows: no separately checked seam colors are required for this EXACT connector class. This is recorded in NORI item nori_exact_color_free_reversed_two_tail_complement_reachability_grand_equivalence_20261008.

For Tucker, seek an antipodally compliant chain-labeled complex that certifies this CROSS-FAMILY complement. For cubical Sperner, exploit one-bit support transitions but prove boundary and full carrier conditions. For multilabeled Hex/KKM, let the covering sets encode R_J and R_revJ and seek a connected witness that upgrades to an ACTUAL same-root complementary-support overlap. None of these existence steps has yet been proved.

## 6. Documentation scope and source preservation

This consolidated entry supersedes the separate literature/toolkit records listed in its supersession metadata. Their complete earlier bodies remain accessible as archived versioned sources, preserving detailed bibliographies and commentary not repeated word for word here. The separate Wu–Yang chain-level proof of Norine's non-geodesic theorem, the Freudenthal geometric construction, and other problem-specific research lemmas remain separate: they are not themselves statements of general fixed-point theorems. All future fixed-point and Hex theorem *statements* should be added here, keeping discussion in this final part.

## Metadata

- ID: literature_fixed_point_theorems
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
