# Cubical Tucker labels and fixed-point extraction barriers

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
