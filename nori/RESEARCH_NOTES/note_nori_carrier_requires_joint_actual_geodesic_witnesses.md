# Carrier compatibility must mean common realizability, not just pairwise window agreement

- Stable ID: note_nori_carrier_requires_joint_actual_geodesic_witnesses
- Author: NORI manuscript editorial migration; mathematical origins recorded in original compositions
- Primary home: article:nori_article_ii_topological_carriers
- Labels: obstruction, partial_argument
- Lifecycle: active
- Epistemic status: method_limitation
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r4593_2
- Updated session: session_nori_r4593_2
- Disposition: none
- Successor: none

## Related references

- note:note_joint_realizability_selection_for_nori1_and_boundary_tournaments
- article:nori_article_iii_reachability, exact version 2
- subsection:appendix_known_obstructions_to_proposed_nori_mechanisms
- subsection:cubical_tucker_labels_and_fixed_point_extraction_barriers, exact version 1
- subsection:ordered_segment_posets_memory_braids_and_equivariant_collapse, exact version 1
- subsection:physical_root_order_prisms_and_balanced_two_cap_packets, exact version 1
- subsection:static_path_nerve_index_limits_and_five_block_root_repairs, exact version 1

## Research note

## Scoped obstruction

A topological or hypergraph selection argument can output a complete clique (pairwise compatible labels) without outputting a single physical path. This is the **extraction gap**, not a universal no-go theorem against topology.

Article II establishes that some proposed carriers disregard actual path transitions: the ambient root/order index and formal equal-support diagonals alone cannot certify a joint physical ordered-window witness. Article III gives a legal Q7 example where good proper-support paths all exist from a prescribed root but no good full path exists there. The later Q9 construction refutes unrestricted NORI3 outright. None of these refutes the NORI1 problem or an adequately witnessed carrier for ordinary boundary tournaments.

## Reusable obligation

Define labels with exact root, ordered direction support, and exterior bits in a way that their *simplex* condition is equivalent to simultaneous occurrence in **one** genuine antipodal cube geodesic (or, for a separate transfer, one vertex-simple tight path). For every proposed Sperner/Tucker/q-star argument, prove:

(1) label extension is carried out within this genuine witness complex;
(2) the final rainbow/antipodal output corresponds to one common witness;
(3) the witness satisfies the specific monochromatic/one-switch conclusion in the applicable surviving NORI class.

## What remains

Whether a sufficiently connected jointly witnessed complex exists for NORI1 or all boundary 3-tournaments is open. A counterexample must name a concrete proposed complex and show failure of its extension/connectivity or extraction lemma. Routine unsuccessful attempts without a precise failure are not evidence of impossibility.

**Provenance:** Articles II and III and their path-flag / rooted-support manuscripts; companion project question note and economically hierarchic / q-star Toolkit entries.

# Migrated complete source proofs

Certified topological carrier limitations; each archived Subsection's full proof is reproduced below so no physical witness, computation or hypothesis is lost.

---

## Retired Subsection: Cubical Tucker labels and fixed-point extraction barriers

Source ID: `cubical_tucker_labels_and_fixed_point_extraction_barriers`
Source Section: `nori_topological_carriers`
Exact original Subsection composition: v1.

# Cubical Tucker labels and actual geodesic extraction

Root and support labels for a cube path can be represented by binary strings, but the usual scalar Tucker labels only force a complementary pair or a neutral simplex in a triangulation. The distinction is crucial: coordinatewise complementary bit strings, equality of root-support labels, and a pair of *physically compatible monochromatic geodesic witnesses* are different targets.

One can formulate a valid positive extraction theorem by requiring the labels to form a chain of nested supports, each certified by actual path reachability, and by retaining the antipodal reversal action on the terminal memory. Under those additional geometric hypotheses a neutral or complementary configuration provides the necessary genuine path pair. Without the nested-support and physical-face hypotheses, cubical fixed-point conclusions alone do not imply the NORI grand conjecture.

## Cubical Tucker lemma, exact limitation on complementary bit-string pairs, and implications for NORI

**Literature identification.** Elyot Grant and Will Ma, "A Geometric Approach to Combinatorial Fixed-Point Theorems" (2013), arXiv:1305.6158, Theorem 1.9, explicitly proves "Tucker's Lemma with Cubical Labels." Primary paper: https://arxiv.org/abs/1305.6158 ; accessible author PDF: https://www.columbia.edu/~wm2428/papers/combinatorial_fixed_point.pdf (p. 4, theorem 1.9). An application explicitly distinguishing neutral simplices from complementary bit-string pairs appears in "Lower Bounds on Tree Covers," ITCS 2026, Theorems 5/6, https://drops.dagstuhl.de/storage/00lipics/lipics-vol362-itcs2026/html/LIPIcs.ITCS.2026.38/LIPIcs.ITCS.2026.38.html .

**Theorem (Grant–Ma cubical Tucker).** Let T triangulate a d-ball, with centrally symmetric boundary triangulation, and let lambda:V(T)->{+1,-1}^d satisfy lambda(-v)=-lambda(v) on the boundary. Then T has a NEUTRAL simplex: for every coordinate i, both signs occur among the labels of vertices of that simplex. The conclusion means coordinatewise sign variation, NOT a pair of vertex labels lambda(u)=-lambda(v).

**Stronger direct Borsuk–Ulam corollary.** Extend lambda affinely over each d-simplex to F:|T|->R^d. Its restriction to the boundary is odd. Therefore F has a zero somewhere in the ball (otherwise normalization gives a map of the d-ball into S^(d-1) whose boundary restriction is odd of odd degree, contradicting nullhomotopy). Hence for some simplex sigma, 0 belongs to conv{lambda(v):v in sigma}. This is stronger than neutrality but STILL does not entail a complementary pair: e.g. in 3 bits, the four labels 000,011,101,110 (with bits mapped to signs) have center 0 in their convex hull, yet no two are complementary. Even three labels 000,011,101 give a neutral simplex without any complementary pair.

**Sharp general obstruction for arbitrary bit-string labels.** For k-bit labels there are N=2^(k-1) complementary pairs. An ordinary Tucker guarantee of an EDGE whose two labels are bitwise complementary holds for ALL antipodally-boundary-labeled triangulations of a d-ball if and ONLY if d>=N:
- Sufficiency: choose any bijection between the N complementary label pairs and signed scalar labels +/-1,...,+/-N, preserving complementation. When N<=d, classical d-dimensional Tucker, which permits labels +/-1,...,+/-d, forces a complementary edge.
- Necessity: if d<N, take the boundary of the d-dimensional crosspolytope (an antipodally symmetric (d-1)-sphere), triangulate its d-ball by coning the boundary triangulation to a central interior apex, give the d antipodal pairs of boundary vertices d distinct complementary bit-string pairs, and label the central apex with a bit string belonging to an UNUSED complementary pair. Boundary antipodality holds. Every boundary edge joins vertices from distinct crosspolytope antipodal pairs, and every apex-edge joins labels from distinct label pairs. Therefore NO edge joins complementary bit-string labels. This is an explicit sharp counterexample to the desired unconstrained extension for d<N.
- For k=d=n>=3, N=2^(n-1)>n, so n-dimensional Tucker on arbitrary n-bit labels does NOT force a complementary pair. The n=3 construction is a cone over an octahedron: boundary vertices use three of the four complementary 3-bit pairs and the cone apex uses the unused fourth pair. For k=1 or k=2, ordinary d=k Tucker DOES give a complementary edge.

**Direct mathematical relevance.** The user's root/support NORI research seeks complementary EXACT reachable dimension-support strings in an n-dimensional topological carrier. Cubical Tucker is precisely an applicable generalization to arbitrary n-bit labels, but its guaranteed neutral simplex permits different label pairs to certify different coordinates, so it does not extract a single complementary pair. A direct forced pair from no further hypotheses would require an ambient ball of dimension at least 2^(n-1), a prohibitive exponential increase. The promising target is a new reachability-specific *neutral-simplex-to-complementary-pair* principle, exploiting nested geodesic support chains, facet carrier transport, color-consistent paths and/or restricted label types. Such a principle is not established by Grant–Ma or classical Tucker. In ordered-three-face NORI, retaining the correct reversed-antipodal involution and two-window seam information remains additionally necessary.

**Scope caveat.** The no-go concerns ARBITRARY equivariant bit-string labelings; it does not disprove any reachability-constrained Tucker/KKM strengthening or the NORI grand conjecture.

## Key extraction insight: cubical Tucker neutrality plus CHAIN labels forces a full geodesic

Let n>=2. For a finite set of n-bit labels lambda(V(sigma)) subset {0,1}^n identify each label with a coordinate support S subseteq[n].

**Theorem 1 (exact chain-neutrality lemma).** Suppose the supports appearing as labels on ONE simplex sigma are totally ordered by inclusion (a Boolean-lattice chain). If sigma is NEUTRAL in the cubical Tucker sense -- for each coordinate i both 0 and 1 occur among its labels -- then the MINIMUM support in sigma is empty and the MAXIMUM support is [n]. Thus lambda(sigma) contains the EXACT complementary pair (0^n,1^n).

Proof. Let A and B be minimum and maximum. Because every label T obeys A subseteq T subseteq B, coordinate i can vary among labels only if i notin A and i in B. Neutrality for all i yields A=empty and B=[n]. QED.

**Theorem 2 (conditional, immediately closing the edge proving ground).** Suppose a triangulation T of an n-dimensional ball has antipodally symmetric boundary and a labeling lambda:V(T)->{0,1}^n such that:
(i) lambda(-v)=complement(lambda(v)) on the boundary;
(ii) for each simplex sigma, its support labels form a chain under inclusion;
(iii) whenever a simplex has labels empty and full, those labels are certified by a single ACTUAL one-color cube-geodesic prefix chain sharing a physical root (rather than two unrelated paths).
Then there is a monochromatic antipodal geodesic: cubical Tucker (Grant-Ma Theorem 1.9) supplies a neutral simplex, Theorem 1 supplies both extreme labels, and (iii) extracts the witnessed full geodesic. If (iii) instead certifies an at-most-one-switch edge-geodesic chain, antipodally odd edge coloring rotates that into a monochromatic antipodal geodesic.

For full NORI, replacing the word-color condition in (iii) by at most one change in the ORDERED-THREE-FACE window word likewise gives the grand conclusion as soon as this hypothetical carrier is established. Thus one can obtain exact complementary support labels from the EXISTING cubical Tucker conclusion, without needing a new "fully complementary edge" theorem.

**Theorem 3 (the actual barrier is antipodal equivariance).** On the natural barycentric subdivision sd(Q_n), a vertex corresponding to a face H has support label S(H)=free-coordinate set. Every simplex is a nested face chain, so its S(H) labels form an inclusion chain. But physical antipodality maps H to bar H with the SAME free-coordinate support: S(bar H)=S(H), not complement S(H). Therefore lambda(-v)=lambda(v), not complement lambda(v), so this *correctly chain-compatible* labeling does NOT meet cubical Tucker's antipodal boundary requirement. The user's root-progress state space E_q(x,S) has the analogous issue: physical oddness maps E_q(x,S) to E_(1-q)(bar x,S), again preserving S. The formal involution beta(x,S)=(bar x,[n]\S) would supply complemented labels, but its preservation of ACTUAL reachability states is precisely an additional nontrivial connector assertion, not a consequence of color oddness.

**Topological interpretation.** Earlier arbitrary-bit-string Tucker obstruction showed that neutral simplices need not contain complementary pairs: e.g. 000,011,101 in Q_3. This obstruction disappears entirely for geodesic PREFIX CHAINS, since they have nesting. The missing NORI theorem can now be stated sharply: construct an n-ball (or an appropriately indexed equivariant carrier) of actual path-certified root-progress states whose boundary involution sends SUPPORTS to COMPLEMENTS while each simplicial flag keeps labels nested and path-compatible. If it exists, known Grant–Ma cubical Tucker yields full closure. No such carrier construction has yet been proved, so this is a CONDITIONAL extraction theorem, not an unconditional solution.

## Comparison of candidate combinatorial fixed-point principles for NORI reachability bit-string labels

**Test 1: Kuhn/Fan cubical Sperner (HIGHEST direct complementary-pair conclusion).** On a cubical grid in [0,M]^n, face-fixed bit labels lambda_i=0 on v_i=0 and =1 on v_i=M, plus one-bit Hamming Lipschitz across EVERY grid edge, force a cell with every one of 2^n labels. This is stronger than merely a neutral simplex. It would suffice for the user's common-target program only if the complementary labels in the guaranteed cell are rooted at compatible antipodes or the same root and carry actual monochromatic geodesic witnesses. Existing NORI reachability does not establish either boundary-face rules or local 1-bit stability. See Musin 2014 arXiv:1406.5082; Wolsey JCTA 1977.

**Test 2: Grant–Ma cubical Tucker (BEST chain-compatible).** Under antipodally complemented boundary labels lambda(-v)=bar lambda(v), an n-ball triangulation contains a simplex with both bits in every coordinate. For arbitrary bit-string labels this is only coordinatewise neutral (e.g. 000,011,101); for a simplex whose used-coordinate support labels form a NESTED CHAIN, neutrality forces min label empty and max label full, an exact complementary pair. If the nested simplex carries a shared actual monochromatic geodesic-prefix witness, this yields a full geodesic. The remaining gap is to build an antipodally ODD chain-labeled carrier; physical antipodality preserves used support instead of complementing it. See Grant–Ma 2013 arXiv:1305.6158 theorem 1.9.

**Test 3: Poincare–Miranda / Brouwer / cubical KKM (BALANCE not exact target).** The continuous coordinate sign-crossing theorem yields F(x)=0 for suitable opposite-face inequalities. Applied to the PL extension of cube-valued vertex labels, it yields 0 in convex hull of labels in one simplex, but may fail to yield any exactly complementary pair. Counterexample: sign vectors for 000,011,101,110 are four vertices of a tetrahedron whose average is 0, but NONE are complementary. Even antiperiodic matching of boundary labels without path compatibility cannot resolve this. Need an integer/cubical degree+1-bit-Lipschitz upgrade for discrete geodesic extraction.

**Test 4: Sperner–Shapley, KKMS, Komiya, colorful KKM (BETTER for set-valued carriers).** These let simplex/polytope vertices carry SETS/FACES or use many covering families and ensure intersecting/balanced collections, sometimes colorful permutation matchings. They are candidates for the NORI reachability sets A_q(z) and target-fiber facet transports, because those are honestly multivalued. However balanced *convex combinations* of different target vertices may intersect without sharing a physical Boolean target. A literal shared target is exact if embedded in a simplex with independent basis e_z for all 2^n physical targets, but the ambient dimension becomes 2^n-1. A dimension-efficient proof requires carrier convexity/Helly/Tucker exchange reflecting prefix-chain witnesses. Literature: Shapley KKMS (1973); Komiya polytopal KKM; Frick–Zerbib colorful polytopal KKM; Gale colorful KKM (1982).

**Test 5: multilabeled high-dimensional Hex / Lebesgue covering lemma (BEST for connected reachability sets).** The Hex theorem forces a colored connection between opposite faces in an n-dimensional lattice/triangulation. Recent multilabeled versions handle several concurrent labels and n-essential complexes; Lebesgue covering lemmas force overlap multiplicity n+1 if no closed cover set meets opposite faces. These could act on connected regions of compatible ROOT/TARGET or REPAIR states without selecting one arbitrary bit string. But connectedness in the carrier does NOT force a directed monotone monochromatic geodesic, and overlapping witness sets may not share a single root/color/seam certificate. The missing condition is a directed geodesic carrier version of Hex preserving nested used directions. Sources: P. Tkacz and M. Piekarska, "Multilabeled and topological versions of the Hex theorem", Topology Appl. 332 (2023), 108525, DOI 10.1016/j.topol.2023.108525; D. Baralic and R. Zivaljevic, "Colorful versions of the Lebesgue, KKM, and Hex theorem", JCTA 146 (2017), 295-311, arXiv:1412.8621; Ivanov "Cubes and cubical chains and cochains in combinatorial topology", arXiv:2012.13104.

**Test 6: Ky Fan alternating-simplex and complementary labels (MULTIPLE witnesses, not shared target).** With signed scalar labels +/-i, excluding complementary edges forces alternating simplices involving n+1 distinct magnitudes; regarding all 2^(n-1) complementary n-bit pairs as scalar indices requires exponential many magnitudes, and Fan's lemma no longer forces a pair. Alternating simplices may be useful if labels are compressed into a controlled number of path-witness TYPES; absent a proven exchange relation, alternating signed pair-types do not imply actual shared-reachable-target coordinates.

**Prioritization.** The strongest concrete NORI synthesis is NOT a new theorem but the Grant–Ma cubical Tucker theorem plus the PROVED nested-chain neutrality lemma, with exact full-geodesic extraction. In parallel, cubical Sperner may apply if an actual reachable-target selector can be chosen with one-bit-Lipschitz repair changes and appropriate face boundary conditions; multivalued Hex/KKM may avoid needing such a selector. All remain CONDITIONAL, and none constitutes grand closure.

## Root-profile nerve for exact reversed-tail NORI: a Tucker-compatible label reduction

## Scope and inputs
This is a proved reformulation and label-space reduction for the ACTIVE ordered-three-face problem, not a proof of the grand conjecture. It uses the exact splice theorem nori_exact_color_free_reversed_two_tail_complement_reachability_grand_equivalence_20261008 and the classical Tucker/Borsuk–Ulam statements in literature_fixed_point_theorems. No new web or literature search was used.

Let n>=4. For J=(a,b), put D_J=[n]\{a,b}. Let R_J(x) be the either-color monochromatic terminal-memory support family of the exact splice theorem. Only nonempty PROPER U subset D_J are retained, since both branches must have a nonempty support.

Define the formal label alphabet
Omega={(J,U): J an ordered pair, empty != U proper subset D_J}
with FREE involution
tau(J,U)=(rev J,D_J\U).
Define the root profile
L_x={(J,U) in Omega: U in R_J(x)}.
Then grand closure holds iff L_x contains a tau-pair for some x. This statement retains the terminal order and has no additional seam-color condition.

Every L_x is nonempty: every singleton U yields a path of exactly three edges, hence one three-face window, for every admissible J. There are |Omega|=n(n-1)(2^(n-2)-2) labels and M=binom(n,2)(2^(n-2)-2) formal antipodal pairs.

## Theorem 1: an exact equivariant carrier without assuming physical support-complement symmetry
Let
K= union_x [Delta(L_x) union Delta(tau L_x)],
a simplicial complex on Omega. Then tau acts simplicially on K, and the following are equivalent:
(a) grand closure;
(b) K contains an edge {u,tau u};
(c) |K| has a tau-fixed point.

Proof. The splice equivalence gives (a) iff a profile L_x contains a tau-pair. Every face of K lies in L_x or tau L_x. Thus a tau-pair in K yields one in L_x after applying tau if needed, proving (a)<=> (b). An opposite edge has fixed midpoint. Conversely the unique minimal simplex supporting a fixed point is invariant under tau; since tau has no fixed vertex, it contains a tau-pair. QED.

The added reflected simplices are FORMAL carriers. We do not claim tau L_x is an actual profile at a physical antipodal root. Extraction is sound because an opposite pair inside a reflected profile reflects back to an opposite pair inside the original SAME-root profile. This avoids requiring the unsupported identity between physical antipodality and support complementation.

## Theorem 2: root-profile nerve and exponential factor reduction
Index the generating simplices by (x,+) and (x,-), and put S_(x,+)=L_x, S_(x,-)=tau L_x. Define the nerve N on these signed roots by
I in N iff intersection_(i in I) S_i != empty.
Its involution sends (x,+) to (x,-).

Then K and N are equivariantly homotopy equivalent. More directly, grand closure holds iff N has an opposite edge {(x,+),(x,-)}, equivalently iff |N| has a fixed point.

The direct extraction proof is
L_x intersect tau L_x != empty
iff there exists u with both u and tau u in L_x.
Thus an opposite root pair in this nerve is exactly the desired same-root complementary-tail witness, not merely a convex intersection.

For completeness, the equivariant nerve equivalence needs no unverified external theorem. On nonempty face posets define
F(sigma)={i: sigma subset S_i},
G(I)=intersection_(i in I) S_i.
Both maps reverse inclusion, commute with the involutions, and induce simplicial maps of the order complexes (barycentric subdivisions). Their composites satisfy sigma subset G(F(sigma)) and I subset F(G(I)). The standard prism homotopy for pointwise comparable order-preserving maps gives homotopies of both composites to the identity; these homotopies commute with the involutions because the inclusions do. Thus the equivalence is equivariant.

N uses at most 2^n SIGNED MAGNITUDES (2^(n+1) signed vertices), compared with M=binom(n,2)(2^(n-2)-2) magnitudes for the direct tail/support alphabet. For n>=5 this is already smaller; asymptotically the reduction factor is n(n-1)/8. This removes the ordered-tail factor, not the remaining exponential dependence on n. No polynomial-size bound follows.

## Theorem 3: retain only maximal root profiles
Choose one actual root representative for every distinct inclusion-maximal L_x. Let p be the number retained, so p<=2^n. Every profile is contained in a retained profile. Consequently deleting the nonmaximal generating simplices leaves K EXACTLY unchanged. The nerve of the retained signed cover is still equivariantly homotopy equivalent to K and has p signed magnitudes.

In the full nerve this deletion can also be performed by paired strong folds. If L_x subset L_y and x!=y, every nerve face containing (x,+) can be enlarged by (y,+): any label witnessing the original intersection lies in L_x and hence L_y. The same holds for the two negative vertices. Mapping x+ to y+ and x- to y- is an equivariant retraction; every face together with its image remains a face, so affine contiguity gives an equivariant strong deformation retraction. Repeat toward selected maximal representatives.

Unlike the earlier edge-reachability graph reduction, this proof needs no symmetry of a directed reachability relation. It applies directly to the full ordered-three-face terminal-memory profiles.

## Exact applicability of the fixed-point toolkit
1. CLASSICAL TUCKER (C1): with p retained profiles, it suffices to build a triangulated p-ball and label vertices by signed retained roots, odd on the boundary, such that every domain edge maps to a nerve edge or a single vertex. Explicitly, for each edge vw, S_label(v) intersect S_label(w) must be nonempty. Tucker supplies labels +x and -x on an edge; their intersection gives the exact reversed-tail splice. No whole-simplex carrier condition is needed for this Tucker criterion.

2. BORSUK–ULAM (A2): if an equivariant continuous map S^p -> |N| can be established, closure follows. Indeed failure of closure makes N an invariant subcomplex of the boundary of the p-crosspolytope, yielding a forbidden equivariant map S^p -> S^(p-1). Equivalently work on K through the proved equivariant homotopy equivalence. The needed high-index map has NOT been constructed.

3. EULER / ACYCLIC SUFFICIENT CONDITIONS: odd Euler characteristic of N forces a fixed simplex, hence closure, because a fixed-point-free involution pairs all nonempty simplices dimension by dimension. In particular F_2-acyclicity suffices. Neither odd Euler characteristic nor acyclicity is claimed universally.

4. KKM: any use on this carrier must prove literal set intersections or a valid simplicial carrier. Replacing actual labels by their bit-vector convex hulls is insufficient; the earlier genuine doubled-Fano edge-reachability example already disproves that general relaxation. It is not a counterexample to the active three-face conjecture.

5. CUBICAL TUCKER / BINARY SPERNER / HEX: neutrality, one-bit legality on existing extensions, and connectedness remain weaker than the required witness without their extra carrier/extraction hypotheses. The signed-root nerve gives an exact opposite-pair target, making classical Tucker the cleanest currently rigorous fit. The partially verified multilabeled Hex entry D5 was not used.

## A precise limitation: singleton availability alone has zero topological force
For an abstract profile system, take every L_x to consist exactly of all labels (J,{i}), for all admissible J and i. For n>=5, |D_J|>=3, so singleton supports and their (|D_J|-1)-element complements are disjoint. K is then the disjoint union of two simplices exchanged by tau, and N likewise consists of the all-positive root simplex and the all-negative root simplex. It equivariantly retracts to S^0, has Euler characteristic 2, and has no opposite edge.

This is NOT asserted realizable by a NORI coloring. It proves only that the automatic one-window reachability data cannot itself provide the missing Tucker carrier or index bound. Any successful argument must exploit additional relations among longer reachable supports imposed by one common coloring.

## Research consequence
The fixed-point toolkit is applicable through an exact, color-free, equivariant root-profile nerve. Formal symmetrization repairs the support-involution mismatch at the carrier level; the nerve removes the tail/support multiplicity; maximal profiles give a further safe reduction. The remaining mathematical task is to prove a topological forcing property of this actual nerve (or construct a smaller admissible Tucker carrier) using the constraints tying the root profiles together. None of the constructions above alone proves grand closure.


The preceding results should therefore be applied as an *implication with explicit hypotheses*: (1) a continuous or simplicial antipodal domain with the claimed topological index; (2) an admissible local labeling whose adjacent labels reflect a genuine root/support incidence relation; (3) an extraction lemma that converts the guaranteed complementary or neutral configuration to two admissible monochromatic branches with reversed common two-direction tails. The missing bridge in the unrestricted conjecture is not a formal generalization from scalar colors to arbitrary bit strings, but the physical path-compatibility property of the label carrier.



---

## Retired Subsection: Ordered-segment posets, memory braids, and equivariant collapse

Source ID: `ordered_segment_posets_memory_braids_and_equivariant_collapse`
Source Section: `nori_topological_carriers`
Exact original Subsection composition: v1.

# Ordered-segment posets, memory braids, and equivariant collapse

Order-sensitive reachability requires states representing directed path segments rather than just their endpoints. A signed ordered-segment poset records the current root, the traveled support and the last few directions; its face maps delete admissible stages while retaining the physical path structure. Such a carrier can be equivariant yet topologically thin after memory is forgotten.

## Sharpness of the one-switch skeleton and the exact 3-face defect chambers

For an edge coloring c of Q_n, retain A_1 as the subcomplex of sd(Q_n) generated by all rooted geodesic-prefix face flags with at most one edge-color change.

**Theorem 1 (exact missing 3-chambers).** Let H be any physical three-dimensional face. Its barycentric subdivision has top-dimensional simplices indexed by starting corners z of H and permutations (i,j,k) of its three free coordinates. The corresponding 3-simplex belongs to A_1 if and only if the color sequence along its three-edge monotone geodesic is not 010 or 101. These two alternating words are the COMPLETE list of forbidden local 3-chambers. Every proper face of H is entirely contained in A_1, because it is a physical face of dimension at most two.

**Theorem 2 (every 3-face barycenter is represented).** For EVERY two-coloring of the edges of H (no antipodal hypothesis needed), there exists at least one one-switch three-edge geodesic spanning H. Thus the physical barycenter b_H is a vertex of A_1. Proof: at any corner of H, among its three incident edges two have the same color q. They form a q-monochromatic two-edge path passing through that corner between two of its neighbors. This path uses two distinct cube directions; extend it at either endpoint along the unique missing third direction. The new edge may be either color, so the extended full three-edge geodesic has at most one change. Its rooted barycentric flag contains b_H.

**Theorem 3 (the universal cubical skeleton bound is sharp).** For every even n>=4, use the antipodally odd exterior-parity edge coloring
c_i(x)=sum_(j neq i)x_j mod2.
Starting at the all-zero root and traversing any three distinct directions, the three consecutive edge colors are exactly 010. Thus for any physical 3-face H incident with the all-zero root, each barycentric 3-chamber of H rooted at that corner is missing from A_1. In particular, A_1 does not generally contain the full geometric three-skeleton of Q_n, even when the coloring has monochromatic antipodal geodesics from other roots. The inclusion of the complete two-skeleton is the sharp universal automatic skeleton-filling statement.

**Topological interpretation.** On each physical 3-face the one-switch carrier has the whole boundary 2-sphere and at least one interior tetrahedron reaching the barycenter, but may omit other interior tetrahedra. A facewise radial filling of the whole boundary sphere inside THAT 3-face would require the entire 3-cell: the mod-two relative fundamental chain of (H,boundary H) contains every top tetrahedron. Therefore local monochromatic/one-switch witness existence at a face barycenter is insufficient to extend its boundary antipodally by a disk. A genuine high-index proof must exploit global cross-face incidence or a topological move changing the target/root.

All results are in the ordinary antipodally odd EDGE setting, the proving ground for the user's face-label program; they do not assert grand ordered-three-face NORI closure.

## Explicit zero-free odd map on the FULL ordered-segment poset: exact index ceiling

Let n>=2. Define P_n to be the finite poset of all directed cube geodesic segments P=(v_0,...,v_k), 0<=k<=n, ordered by oriented contiguous-subsegment inclusion. Its involution is Theta(P)=(bar v_k,...,bar v_0). In NORI, every color-admissible one-switch segment subposet G_n(c) is Theta-invariant and included in P_n.

**Theorem (unconditional equivariant map to S^(n-1)).** There exists an EXPLICIT simplicial-PL Theta-odd map U:|P_n|->R^n that never vanishes, hence a Theta-equivariant map |P_n|->S^(n-1), and the same map restricts to every |G_n(c)|. In particular, the free Z2 cohomological index of ANY admissible ordered-segment complex is at most n-1. Therefore a proposed proof of NORI via forcing index >= n on THIS carrier is IMPOSSIBLE, regardless of the coloring.

**Construction.** At any nonfull segment P=(x,...,y) of rank k<n, put
U(P)=x+y-1, interpreted coordinatewise in R^n. Its i-th component is +1 if both endpoints have bit 1 at i, -1 if both have bit 0, and 0 if the segment traverses i. At any FULL antipodal segment P=(x,...,bar x) with distinct direction order p=(p_1,...,p_n), set
U(P)=(1-2x_(p1)) e_(p1) + (2x_(pn)-1)e_(pn).
Since n>=2, p1 and pn differ, so this vector is nonzero. Extend U affinely on every simplex of the order complex.

**Oddness.** If k<n, Theta(P) starts at bar y and ends at bar x, so U(Theta P)=(1-y)+(1-x)-1=-(x+y-1). If k=n, Theta(P) starts at x (since y=bar x) and its direction order is rev(p). Hence its first direction is pn and its last is p1. The prescribed vector becomes
(1-2x_(pn))e_(pn)+(2x_(p1)-1)e_(p1)=-U(P).
Thus the affine map is Theta-odd.

**No zero on any simplex.** A simplex is a chain P_0<...<P_m. If its maximal segment P_m has rank<n, choose any coordinate i not used by P_m. Every nested subsegment also avoids i and has both endpoint bits equal to the same b; hence every vertex of the simplex has U_i=2b-1, so each convex combination has that nonzero component.

If P_m is full, consider its largest proper subsegment P_(m-1), which is a contiguous portion of the full segment and therefore omits the FIRST direction p1 or the LAST direction pn (or both). If it omits p1, its entire vertex interval lies strictly after the first edge, so every nonfull subsegment P_j in the chain has both endpoint bits equal to 1-x_(p1) in coordinate p1. Thus U_(p1)(P_j)=1-2x_(p1). At the full vertex P_m our assigned U_(p1) is precisely the same sign. Therefore U_(p1) is constant nonzero throughout the simplex. If P_(m-1) instead omits pn, every lower segment lies before the last edge, with common pn-bit x_(pn), and U_(pn)(P_j)=2x_(pn)-1, agreeing with the prescribed component of the full vertex. Again U cannot vanish. In a singleton full-vertex simplex U(P_m) is nonzero directly. This handles all chains.

**Consequences.** Earlier NORI research correctly built a free ordered-segment involution and an equivariant map onto physical barycentric face data, but suggested trying to prove index(|G_n|)>=n. The universal zero-free map here refutes that SPECIFIC INDEX OBJECTIVE, without affecting the correctness of the geometrical carrier or the NORI grand conjecture. The stronger topological program must use relative endpoint conditions, a carrier WITHOUT an equivariant inclusion into P_n, or a coloring-dependent obstruction not reducible to absolute Z2-index. The preserved actual-geodesic face labels remain useful.

This theorem is independent of all coloring axioms. It is a sharp methodological no-go for the full ordered-segment carrier, not a counterexample to NORI.

## Contiguous extension flags have only window-graph topology

Let window size r>=1 and n>=r+1. A path predicate is hereditary under taking contiguous subpaths and invariant under physical antipodal reversal Theta. For NORI take the predicate "at most one ordered-window color change"; every path of length r and r+1 is then admitted.

Consider either:
(a) actual rooted admitted geodesic paths, or
(b) their complete ordered PHYSICAL window sequences, identifying exactly the root translations preserving all physical windows.
Order the objects by contiguous subpath/subsequence inclusion. Let P_good be the resulting finite poset, and take its order complex. Theta acts on it simplicially and preserves ranks (path lengths).

THEOREM. Removing all objects of length k>=r+2, in decreasing length, gives an equivariant homotopy equivalence to the rank-r/r+1 order complex. In version (b), this is the barycentric subdivision of the full actual physical window-shift graph H. Hence for the <=1-switch predicate its equivariant homotopy type is independent of the coloring. Its cohomological antipodal index is at most one.

PROOF. At the removal of a maximal admitted path P of length k>=r+2, all of its proper subpaths of length >=r remain, by heredity. Its lower link is the order complex of proper contiguous edge intervals of P of length >=r. This link is the union of:
 L_left = all subpaths of the prefix of length k-1,
 L_right = all subpaths of the suffix of length k-1.
Each is a cone, with its full prefix or suffix as maximum. Their intersection is the cone of all subpaths of the common middle interval of length k-2>=r. Thus the lower link is contractible. Attaching the cone at P along this contractible link changes no homotopy type; equivalently one may remove P.

Remove vertices in Theta pairs. They have the same rank, are distinct, and are incomparable, so their stars meet only in the retained complex. Choose the two relative homotopies as Theta-images. This gives equivariant homotopy equivalences throughout. Exact physical-window identification in version (b) preserves the interval-poset description: distinct positions of one geodesic have distinct direction sets, and its contiguous window strings specify the same fixed physical subpath fiber. At the end, length-r objects are windows and length-(r+1) objects subdivide edges joining two consecutive windows. All such objects are admitted for the <=1-switch predicate. QED.

The involution on the flag complex is free even when full good paths exist: an invariant chain would have an invariant vertex at each of its distinct ranks, whereas reversal of a direction-distinct path of length >=2 has no fixed ordered path. This observation is consistent with the low-index conclusion.

RELATION TO THE STATIC-BOX THEOREM. The exact physical-box nerve isolates all paths of length >=2r in root/used-support components. Adding only contiguous extension flags supplies connections, but their long-path cones are homotopically redundant by the theorem above. To retain higher-dimensional path information, a carrier must also identify common physical windows or other certified data ACROSS DIFFERENT path orders. Such identifications have potentially noncontractible fibers and cannot be replaced by the interval poset.

This is a structural restriction on carrier design. It does not assert that a larger order-exchange carrier cannot force NORI closure.

The resulting collapses and indexing limits explain why a theorem about arbitrary bit-string labels cannot be applied directly to path supports. Genuine extraction needs an incidence complex that preserves the two-window state.



---

## Retired Subsection: Physical root-order prisms and balanced two-cap packets

Source ID: `physical_root_order_prisms_and_balanced_two_cap_packets`
Source Section: `nori_topological_carriers`
Exact original Subsection composition: v1.

# Physical root-order prisms and balanced two-cap packets

Adjacent transpositions of full coordinate orders and single-coordinate root slides form small permutohedral–cubical prisms. Their vertices are actual paths, and some crossing ordered faces remain literally identical across the prism. Combined with balanced two-cap selection, this yields opposite central colors on verifiable physical witnesses.

## A simultaneous permutohedral Borsuk–Ulam zero with NO jointly balanced actual vertex in its own face

This is a sharp **physical ordered-face no-go** for a tempting but invalid extension of the scalar endpoint-zero face lemma to a pair of physical roots. It does NOT contradict the proved global same-order synchronization theorem for n≥10, which ensures a joint actual order somewhere else in the permutohedron.

Take any \(n\ge8\), choose an arbitrary physical cube root \(x\), and partition the direction set into disjoint sets \(S,T\) with \(|S|=4\), \(|T|=n-4\ge4\). Fix a total order of direction names. Define the following colors on actual ordered 3-faces THROUGH \(x\):
- For all triples \((a,b,c)\) with \(\{a,b,c\}\subseteq S\), prescribe
\[
h_x(a,b,c)=\mathbf1_{\{b\in S_1\}},
\tag{1}
\]
where \(S_1\subset S\) is any two-element subset. This is **reversal-even** within the first block: \(h_x(a,b,c)=h_x(c,b,a)\). Among all 24 ordered triples of distinct S-elements, exactly 12 have h-value0 and 12 have h-value1.
- For all triples with \(\{a,b,c\}\subseteq T\), prescribe
\[
h_x(a,b,c)=\mathbf1_{\{a<c\}},
\tag{2}
\]
which is **reversal-odd**: \(h_x(c,b,a)=1\oplus h_x(a,b,c)\), and precisely half of all ordered triples of T have value1.
- Assign arbitrary binary colors to every other ordered physical 3-face through \(x\), including all mixed-S/T free triples.
- For every ordered physical 3-face through the ANTIPODAL root \(\bar x\), assign the NORI-required bit \(c(\bar F,\operatorname{rev}\pi)=1\oplus c(F,\pi)\). For all remaining ordered-face involution orbits, choose arbitrary bits in antipodally complementary pairs.

This defines a COMPLETE valid active NORI coloring, because \(n\ge8\) ensures a three-face cannot contain both \(x\) and \(\bar x\); the sets of faces through them are distinct, and the paired-orbit prescription never conflicts.

Let \(H_S\) be the PROPER FACET of the standard permutohedron \(P_n\) whose permutation vertices \(\pi\) have precisely S as their first four direction supports (in any order), followed by the T directions (in any order). For any \(\pi\in H_S\) let
\[
u(\pi)=h_x(p_1,p_2,p_3)\in\{0,1\},\qquad
v(\pi)=h_x(p_{n-2},p_{n-1},p_n)\in\{0,1\}.
\]
By construction \(h_x(\operatorname{rev}(p_1,p_2,p_3))=u\), while \(h_x(\operatorname{rev}(p_{n-2},p_{n-1},p_n))=1-v\).

**Theorem (literal phantom simultaneous zero).** On EVERY actual full direction permutation \(\pi\in H_S\), the two physical-root integer endpoint-imbalance functions satisfy
\[
\boxed{
(q_x(\pi),q_{\bar x}(\pi))=(u+v-1,\ v-u)
\in\{(-1,0),(0,1),(0,-1),(1,0)\}.
}
\tag{3}
\]
In particular NO original permutation vertex of the ENTIRE face \(H_S\) has \(q_x=q_{\bar x}=0\).

Nevertheless, for the canonical ODD PL extensions \(F_x,F_{\bar x}\) formed by averaging endpoint imbalance over original vertices of each face and extending on the barycentric subdivision, one has
\[
\boxed{(F_x,F_{\bar x})(b_{H_S})=(0,0)}
\tag{4}
\]
at the actual barycenter \(b_{H_S}\) of this proper permutohedral facet.

**Proof.** The active NORI endpoint formula at the two antipodal roots is
\[
q_x=h_x(\text{first triple})-h_x(\operatorname{rev}(\text{last triple})),
\quad
q_{\bar x}=h_x(\text{last triple})-h_x(\operatorname{rev}(\text{first triple})).
\]
Insert (1)-(2) to obtain (3). No binary u,v solve both \(u+v-1=0\) and \(v-u=0\) (the second forces u=v, the first would then force 2u=1). Thus no actual joint balanced path lies in H_S.

The facet's original vertices are all independent orders of S followed by independent orders of T. The first triple of a uniformly random S-order has its MIDDLE direction uniformly distributed over the four S-directions, so \(E[u]=|S_1|/|S|=1/2\). The last triple of a uniformly random T-order is symmetric under reversing its first/third directions, and the rule (2) changes bit under that reversal, so \(E[v]=1/2\). Consequently \(E[q_x]=E[u]+E[v]-1=0\) and \(E[q_{\bar x}]=E[v]-E[u]=0\). The defined barycentric extension assigns the original-vertex mean at b_H, proving (4). \(\square\)

**Interpretation for the topology-first research program.** The scalar face lemma works because a 1-Lipschitz \(\{-1,0,1\}\)-valued function on a connected polytope graph cannot average to zero in a face unless that face contains a true zero vertex. For TWO such independent physical-root functions, the vector values can wind around the origin with no common zero vertex of the face—even when the roots are ANTIPODAL and the coloring obeys the FULL active ordered-face oddness law. The example realizes the four axial signs \(\pm e_1,\pm e_2\) on genuine complete geodesics, not fictitious combinatorial colors.

The previously proved multi-root Borsuk–Ulam theorem correctly extracts a possibly DIFFERENT endpoint-opposed path at each root from the same face; it cannot be upgraded to a SAME-PERMUTATION statement by applying the single-root scalar face lemma componentwise. The separate disjoint-triple reversal-signature theorem supplies real simultaneous permutations in n≥10, but uses additional combinatorial incidence across different faces. Any further high-index **joint real-path** carrier needs a new labeled-face degree or Sperner-type extraction lemma, not just vector averaging and the existing 1-Lipschitz scalar property.

NORI ROOT/ORDER SWAP PRISM (proved, all dimensions n>=5). Let p be a full distinct direction order, x a root, and k satisfy 2<=k<=n-2. Write t=p_(k-1), a=p_k, b=p_(k+1), d=p_(k+2). Let p' swap a,b. Before the swapped pair both words reach y=x XOR {p_1,...,p_(k-1)}. Their central ordered-three-face windows indexed k-1,k use the SAME TWO PHYSICAL 3-faces: F_minus=the {t,a,b}-face through y and F_plus=the {a,b,d}-face through y, intersecting in the PHYSICAL {a,b}-square through y. For p the two colors are [c(F_minus,(t,a,b)), c(F_plus,(a,b,d))]; for p' they are [c(F_minus,(t,b,a)), c(F_plus,(b,a,d))]. For each T subset {a,b}, translating the starting root x to x XOR T changes only FREE COORDINATE bits in both central faces, hence preserves both actual physical faces and the respective ordered central color pair. Therefore the eight real full geodesic states (root x XOR T, choice p or p') form a certified combinatorial 3-prism (two independent root axes plus one order-swap axis). Under active NORI reversal oddness, full-path antipodal reversal fixes each starting root, reverses p, and maps the central ordered color pair (u,v) to (1-v,1-u), at mirrored swap position n-k. All eight vertices are actual full paths, but only the TWO CENTRAL WINDOWS are certified constant on the root-square fibers. Other windows can change, and the prism need NOT be a cell in a monochromatic or one-switch path subcomplex. Proof: the two central face triples share middle free directions a,b; toggling their starting root bits changes no fixed exterior coordinate. Reversal and the color law give the displayed mirrored complement. This is a literal geometry-preserving building block for an equivariant root/order carrier; global compatible witness filling and grand extraction remain open.

THEOREM (TWO-COLOR CORRELATED POSITION FORCING, ODD n). Fix any odd n>=7, any active NORI coloring, any full path root x, a distinguished coordinate i and two others a,b. Let T=[n] minus {i,a,b}, k=|T|=n−3. The already-proved full permutohedral Borsuk–Ulam packet theorem nori_odd_full_permutohedron_two_cap_actual_opposite_central_face_colors_20261008 yields ACTUAL full x-rooted direction orders pi_r in ONE COMMON PROPER permutohedron face, with weights alpha_r>0 summing1. Let q_r be the GENUINE central ordered-3-face color of pi_r, and b_r in {0,1}^T its actual before-i order bits b_rj=1 iff j precedes i along pi_r. The packet satisfies P_alpha(q=0)=P_alpha(q=1)=1/2 and E_alpha[b_j]=1/2 for every j∈T.
Define the TWO COLOR-CONDITIONAL mean positions u=E[b|q=0] and v=E[b|q=1] in [0,1]^k. The exact balance identities imply
  u+v=mathbf1,
coordinatewise. Equivalently the convex hulls of the two genuinely witnessed coordinate-position sets have COMPLEMENTARY points u and 1−u, represented with the packet's actual conditional weights. This is a COLOR-RESOLVED strengthening of mere mixed-color/position neutrality, though it need not furnish one pair of exactly complementary {0,1}^k positions.
Let Pi_0 and Pi_1 be independent random ACTUAL packet paths sampled conditionally on central face colors q=0 and q=1, respectively. For coordinate j, the two before-i bits differ with probability
  u_j(1−v_j)+(1−u_j)v_j = u_j^2+(1−u_j)^2 = 1/2+2(u_j−1/2)^2.
Therefore
 E[d_H(b(Pi_0),b(Pi_1))] = k/2+2sum_(j∈T)(u_j−1/2)^2 >=k/2.
Hence there exist TWO ACTUAL full x-rooted endpoint-cap-coherent paths P0,P1 among the packet, with central physical ordered-three-face colors 0 and1 and their physical projected i-edge locations separated by at least CEIL((n−3)/2) Hamming coordinates in T. Their direction orders are in the SAME PROPER PERMUTOHEDRAL FACE, and the packet's common fixed prefix support is contained in {a,b} or has complement contained in {a,b}. The bound refines automatically when the color-conditional means are polarized, using the displayed correction term.
This gives a genuine opposite-color, macroscopic, same-root two-cap witness pair. It does NOT claim that their central physical faces overlap, that their two-direction tails are reversed, or that either full path has <=1 switch. In particular, the convex complementarity u+(1−u)=1 is NOT the exact bitwise complementarity required by the grand reversed-tail extraction theorem; achieving compatible paths rather than just complementary convex mixtures is the next missing step.

These configurations provide a concrete local substrate for a topological repair scheme. The unresolved step is to choose a sequence of prisms on which boundary-window defects decrease rather than move between incompatible facets.



---

## Retired Subsection: Static path-nerve index limits and five-block root repairs

Source ID: `static_path_nerve_index_limits_and_five_block_root_repairs`
Source Section: `nori_topological_carriers`
Exact original Subsection composition: v1.

# Static path-nerve index limits and five-block root repairs

Take the static two-sided witness nerve defined by simultaneous compatibility of literal root/support boxes. Short paths may form connected antipodal pieces, while long paths can become isolated once their supported root fibers separate. This yields a sharp index limitation for the static carrier and focuses attention on root slides and adjacent direction exchanges that change the physical boxes.

## PHYSICAL ROOT MOBILITY IS MATHEMATICALLY NECESSARY: NO SAME-ROOT OPPOSITE-SHORE BOX CONTACT ABOVE DIMENSION SIX

Retain the genuine two-sided physical root-box carrier of
nori_two_sided_root_sheet_helly_equivariant_exact_grand_fixedpoint_index_four_ceiling_20261008,
and the exact pairwise box edge test of
nori_two_sided_box_exact_root_support_edge_test_high_index_packet_graph_selection_20261008.

Let r>=2, n>2r, and let P,Q be ACTUAL admitted <=1-switch directed geodesic PATH STATES for a binary physical ordered-r-face coloring, with SAME starting root x∈Q_n. Their lengths k_P,k_Q are at least r and at most n; their used sets W_P,W_Q, unused D_P,D_Q, and common r-window free-coordinate sets M_P,M_Q are as usual, with
  |D_P|=n−k_P, |M_P|=max(2r−k_P,0)
and likewise Q. Physical antipodal complement+path reversal maps P to ΘP whose new root is x XOR D_P, and whose exact root sheet has the same middle free-coordinate set M_P.

**THEOREM 1 (EXACT cross-shore same-root criterion).** The two boxes B(P) and B(ΘQ) have a common actual source-target root pair if and ONLY if
  D_Q ⊆ M_P
AND
  D_P ⊆ M_Q.
This is an exact physical-face criterion, independent of ordered face colors once P,Q have been admitted.

PROOF. The source factor of B(P) is S(P)=x+span M_P, and that of B(ΘQ) is S(ΘQ)=(x XOR D_Q)+span M_Q. Their intersection is nonempty precisely when D_Q⊆M_P∪M_Q; since unused D_Q is disjoint from its own used M_Q, this means D_Q⊆M_P. The target factor of B(P) is S(ΘP)=(x XOR D_P)+span M_P and that of B(ΘQ) is S(Q)=x+span M_Q. Their intersection is nonempty precisely when D_P⊆M_P∪M_Q; since D_P∩M_P=empty, this is equivalent to D_P⊆M_Q. Both factors must intersect, proving the equivalence. QED.

**THEOREM 2 (NO SAME-ROOT MIXED CONTACT IN n>2r EXCEPT FULL GRAND WITNESSES).** If n>2r and B(P)∩B(ΘQ) is nonempty, then BOTH P and Q must be FULL n-edge geodesics. Consequently, under hypothetical GRAND FAILURE, there is NO opposite-shore mixed box edge of this form at any common physical root.

PROOF. If P is full then D_P=empty, and because n>2r its middle common set M_P=empty. Theorem1 forces D_Q=empty, so Q is full also. Similarly with P,Q exchanged.

Now suppose both P,Q are incomplete. By Theorem1,
  n−k_P=|D_P| <= |M_Q|<=max(2r−k_Q,0),
  n−k_Q=|D_Q| <= |M_P|<=max(2r−k_P,0).
Since both left sides are POSITIVE, both right sides are positive, so k_P,k_Q<2r and the maxima can be dropped. Adding gives
  (n−k_P)+(n−k_Q) <= (2r−k_Q)+(2r−k_P),
i.e. n<=2r, contradicting n>2r. QED.

**NORI SPECIALIZATION (r=3).** In EVERY dimension n>=7, suppose P,Q are genuine <=1-switch partial geodesics from the SAME physical cube root x. Then their two-sided product boxes B(P),B(ΘQ) CAN meet only if P,Q are ALREADY full good antipodal geodesics. In particular, among the universal single-window monochromatic THREE-EDGE paths at one root, the full 'positive' clique and its reflected negative clique have NO cross edge in the two-sided Helly nerve. Merely taking all local path branches from ONE physical root and their Θ-images can never provide the mixed-face topology required for grand closure in n>=7.

**CROSS-ROOT TRANSPORT IS REQUIRED.** If P is rooted at x and Q at y (possibly distinct), the exact general cross-shore box compatibility test is
   supp(x XOR y XOR D_Q) ⊆ M_P∪M_Q,
   supp(x XOR y XOR D_P) ⊆ M_P∪M_Q.
Equivalently the ROOT DISPLACEMENT mask x XOR y must agree with BOTH unused support masks D_P and D_Q OUTSIDE the tiny union M_P∪M_Q. In particular, if k_P,k_Q>=6 for ordered three-face NORI, then both middle common sets are empty, so compatibility requires
  x XOR y = D_P = D_Q.
This is a genuinely large, support-dependent PHYSICAL root shift, not a local root slide.

**TOPOLOGICAL INTERPRETATION.** The high-index global program cannot be carried by sign-complementing LOCAL witnesses at one fixed root. Equivariant mixed-carrier faces beyond the universal low-rank skeleton necessarily use different physical roots with exterior differences synchronized to the UNUSED direction masks. This is an exact local-to-global obstruction in the honest double Helly nerve, and explains why a high-dimensional Tucker proof must incorporate root transport/path order exchanges INSIDE its topological framework. It does NOT prove that such transport always exists and does not close the unrestricted NORI grand conjecture.

## Moving-seam cubical transport through central permutohedral adjacent swaps: both genuine face objects preserved by the crossing swap

Let n>=6 and let c be ANY binary coloring of physical ordered three-faces on Q_n. Take a full rooted cube-geodesic direction order p=(p1,...,pn), choose any cut rank ell with 2<=ell<=n−2, and denote four consecutive direction names
  c0=p_(ell−1), a=p_ell, b=p_(ell+1), d=p_(ell+2),
which are pairwise distinct. Let S be the first ell used directions and y=x XOR S the true physical cut vertex of the path from root x. Its TWO actual crossing three-face window objects are
  L=(F(y;{c0,a,b}),(c0,a,b)),
  R=(F(y;{a,b,d}),(a,b,d)).
The two underlying physical faces are flat across the root square spanned by a,b.

**THEOREM 1 (cross-cut central transposition preserves BOTH physical seam face objects).** Let p' be obtained from p by interchanging only the adjacent positions ell,ell+1, replacing (c0,a | b,d) by (c0,b | a,d). The NEW used prefix set is S'=S symmetric-difference {a,b}, so the new cut vertex is y'=y XOR a XOR b, the OPPOSITE corner of the physical seam square. Its two crossing ordered face windows are
  L'=(F(y';{c0,b,a}),(c0,b,a)),
  R'=(F(y';{b,a,d}),(b,a,d)).
Since a,b are free directions of BOTH old physical faces,
  F(y';{c0,a,b})=F(y;{c0,a,b}),
  F(y';{a,b,d})=F(y;{a,b,d}).
Thus the old/new pairs L,L' are DIFFERENT ORIENTATIONS of exactly the SAME actual physical three-face, and likewise R,R' are different orientations of exactly the SAME actual second physical three-face. The four actual seam-window colors are
  c(F_L,(c0,a,b)), c(F_L,(c0,b,a)),
  c(F_R,(a,b,d)),  c(F_R,(b,a,d)),
with two fixed physical faces F_L,F_R. Every one of these four values remains unchanged when the STARTING ROOT is independently flipped in a, b, or both. This gives a literal 2-by-4 physically grounded seam-color table, unlike an interpolated Tucker label.

**THEOREM 2 (adjacent moves on either side transport one physical seam face).**
(a) Swap the two last directions of the prefix, positions ell−1,ell: (c0,a | b,d) becomes (a,c0 | b,d). The cut USED support S and physical cut vertex y do not change. The new LEFT crossing window has triple (a,c0,b) and uses the SAME underlying physical face F_L=F(y;{c0,a,b}), while the new RIGHT window has triple (c0,b,d) on a generally different physical face. The seam-square axes change from {a,b} to {c0,b}, two squares sharing direction b.
(b) Swap the first two suffix directions, positions ell+1,ell+2: (c0,a | b,d) becomes (c0,a | d,b). The cut support and y again do not change. The new RIGHT crossing window has triple (a,d,b) on the SAME underlying physical face F_R=F(y;{a,b,d}), while the new LEFT window has triple (c0,a,d) on a generally different face. The seam-square axes change from {a,b} to {a,d}, two squares sharing direction a.

**PROOF.** For Theorem1 the transposition crosses the cut, so S' replaces a by b, changing the cut vertex by a XOR b. Each crossing face's free triple includes both a and b, so changing the reference vertex y on those two coordinates leaves the physical face literally unchanged. The ordered triples transform exactly as stated. Flipping starting root in any subset of {a,b} changes the cut vertex only on the same free directions, establishing the four-root square invariance. For Theorem2 the transpositions lie wholly inside S or its complement, so the cut endpoint y is unchanged. The left seam free 3-set {c0,a,b} is unchanged by the left transposition, and the right free set {a,b,d} is unchanged by the right transposition, whereas the other seam free set generally changes. The resulting direction words determine the displayed orientations. QED.

**PHYSICAL ORDER-EXCHANGE FRAMEWORK.** These three elementary adjacent permutation moves give genuine transport rules for a root-coupled moving seam-square label:
- crossing swap: the physical root cut moves by a XOR b, the pair {a,b} stays fixed, and BOTH physical seam faces are preserved;
- left-neighbor swap: cut root fixed, seam pair changes {a,b}->{c0,b}, LEFT physical face preserved;
- right-neighbor swap: cut root fixed, seam pair changes {a,b}->{a,d}, RIGHT physical face preserved.

The central root-square label pair {a,b} cannot be fixed globally without killing antipodal index, by Item nori_fixed_pair_separating_permutohedron_facets_antipodal_index_zero_square_alignment_nogo_20261008. The present theorem identifies the precise COLOR-INDEPENDENT GEOMETRIC transport operations for a MOVING pair, requiring only genuine physical faces and adjacent-coordinate exchanges. Color memory remains attached to these actual ordered faces. These operations are promising 1-cells for an enriched equivariant root-square / permutohedral repair complex.

**LIMITATION.** The active NORI antipodal-reversal law relates colors on antipodal faces with reversed entire direction triples; it does NOT relate two different orders of the SAME physical face. Thus the four crossing-swap seam bits above can be arbitrarily assigned locally, and none of the three elementary moves is automatically defect-decreasing. The missing forcing step is a parity/holonomy or fixed-point principle applied to the WHOLE system of these actual ordered-face transport moves, using all-root antipodal compatibility and genuine path-window color incidence. This theorem is a rigorous geometric toolkit item, NOT an unrestricted grand proof.

## COMPLETE 30-bit classification of a five-direction chart in which ALL 120 anchored permutations have two changes, with arbitrary opposite central colors

Fix a physical cube Q_n, n>=5, an ordered FIVE-element coordinate subset B, and a specific starting physical cube vertex r of a five-coordinate B-face (all coordinates outside B fixed). Consider the 120 genuine five-edge cube geodesics rooted at r that traverse EACH direction in B exactly once, with direction order (a,b,c,d,e) a permutation of B. These paths have three ordered-three-face windows, hence color words of length three. For a binary ordered-PHYSICAL-three-face coloring, 'bad relative to the one-switch target' for an anchored length-five path means its three window colors have EXACTLY TWO switches, i.e. (q,1-q,q).

Define the ACTUAL local ordered-face colors by their physical exterior-B bit layers relative to the anchored root r:
- F_0(a,b,c): actual face with free ordered triple (a,b,c), both remaining B exterior coordinates d,e still at root r values (zero of them flipped);
- F_1(b,c,d;a): actual face with free ordered triple (b,c,d), outside it a already flipped relative to r and e unflipped;
- F_2(c,d,e): actual face with free ordered triple (c,d,e), outside it both remaining B directions a,b flipped relative to r.
All exterior coordinates outside B are fixed by the ambient anchored five-face. These are genuine, distinct physical face objects at the indicated layers, and their colors need not be affine or coordinate-only. For each five-order (a,b,c,d,e), its actual color word is
  (F_0(a,b,c), F_1(b,c,d;a), F_2(c,d,e)).

**THEOREM 1 (complete classification, NECESSARY AND SUFFICIENT).**
Every one of the 120 anchored five-orders has exactly two changes IF AND ONLY IF there is a uniquely determined family of 30 arbitrary binary parameters
  t(c,A) ∈ F2,
indexed by the choice of a MIDDLE DIRECTION c∈B and an UNORDERED two-element set A⊂B\{c}, such that, for EVERY ordered list of distinct directions a,b,c,d,e exhausting B,
  F_0(a,b,c)    = t(c,{a,b}),
  F_1(b,c,d;a) = 1−t(c,{a,b}),
  F_2(c,d,e)   = t(c,{a,b})
                    = t(c, B\{c,d,e}).
The 30 parameters are independent. The number of possible assignments to all local ordered-physical-three-face objects of the anchored five-face satisfying this property is EXACTLY 2^30.

**Proof.** If all 120 length-five paths are two-switch, every ordered permutation satisfies
  F_0(a,b,c)=F_2(c,d,e)=1−F_1(b,c,d;a).
Fix c and a,b,d,e distinct in B\{c}. Swapping d,e while keeping (a,b,c) fixed shows F_2(c,d,e)=F_2(c,e,d). Swapping a,b while keeping (c,d,e) fixed shows F_0(a,b,c)=F_0(b,a,c). Therefore F_0(a,b,c) depends only on c and the UNORDERED set A={a,b}; call its bit t(c,A). Then every F_2(c,d,e) is forced to the value t(c,B\{c,d,e}) and every mixed-layer central F_1(b,c,d;a) is forced to 1−t(c,{a,b}). Conversely these formulas make every full 5-path word exactly (t,1−t,t), hence two-switch. The 30 parameters are uniquely read from the 5*choose(4,2)=30 independent first-layer ordered-face color classes. Every ordered physical three-face supported on B has exactly TWO exterior B directions, in one of the four exterior states 00,10,01,11; it appears in precisely one of the layer categories F_0,F_1,F_2 above as its ordered triple and exterior state vary, so there are NO hidden consistency conditions. QED.

**THEOREM 2 (opposite central colors coexist with universal local failure).** Let L:B→F2 be ANY nonconstant binary function and specialize t(c,A)=L(c) for all unordered A. Then ALL 120 anchored full five-geodesics have the word
  (L(c),1−L(c),L(c)),
where c is their THIRD (middle) coordinate direction. Therefore every anchored full five-path has TWO changes, even though the actual CENTRAL ORDERED-THREE-FACE windows take BOTH binary colors among the 120 permutations. A bichromatic central three-face pair in a single five-direction order-exchange block is not sufficient to force even a one-switch full FIVE-edge path rooted at the common chart corner.

**THEOREM 3 (compatibility with the genuine ACTIVE NORI axiom).** For any n>=6, the arbitrary anchored-five-face assignment of Theorem1 extends to a genuine binary ordered physical three-face coloring of the ENTIRE Q_n satisfying
   c(bar F,rev π)=1−c(F,π).
Reason: physical antipodality of any ordered face inside the anchored five-coordinate subcube complements at least one FIXED EXTERIOR coordinate OUTSIDE B, sending that physical face to a different parallel B-face. Hence NO two prescribed ordered face objects in the anchored five-face belong to one physical antipodal-reversal orbit. Assign the complement-reversal mate bit consistently, and choose the remaining orbits arbitrarily.

When n=5 (the anchored five-face is the WHOLE cube), the genuine active axiom imposes the exact additional condition
  t(c,A)+t(c,(B\{c})\A)=1
for each c and unordered A. These conditions pair the six A's per c into three complementary pairs and leave exactly 15 independent bits; hence even in Q5 there are exactly 2^15 valid active NORI colorings with ALL 120 full geodesics BAD from the prescribed corner r. (This does NOT mean grand NORI fails globally; other starting roots may have good full paths.)

**TOPOLOGY-FIRST INTERPRETATION.** This is a sharp LOCAL COUNTEREXAMPLE to the hoped-for five-block repair lemma 'two opposite central-window face colors force a compatible <=1-switch five-geodesic in that block.' The central color interface can vary arbitrarily with the middle coordinate c while EVERY rooted five-order has alternating window colors. The first obstruction identified by the canonical central-window chart is thus a REAL topological transition/holonomy problem across MULTIPLE charts and physical roots, not a single five-block obstruction one can eliminate using its own local opposite colors alone.

The surviving global target is a color-dependent obstruction to extending the 30-bit local atlases consistently across overlapping B-faces and genuine root transport. This theorem classifies the exact local failure configurations and does NOT assert unrestricted grand closure.

Five-direction repair diagrams are locally rich, but their solutions need not glue globally across different permutohedron faces. A dynamic, physically certified carrier is necessary to exceed the static-index ceiling.
