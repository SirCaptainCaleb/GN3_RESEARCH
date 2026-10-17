# Article XVI — NORI1: Obstruction Compatibility and Routes to Closure

## Global compatibility and routes to closure

### Obstruction compatibility and a programme for NORI1 closure

#### Scope and status

This is a strategic synthesis dated 17 October 2026, prepared in session `session_nori_r11487_1`. It surveys the ten active Articles I and VII–XV, their subsection catalogue, the retired Article II–VI shells, and the research-note catalogue. All fifteen article compositions and the initial 471 note bodies were retrieved; central arguments and obstruction records were examined selectively in depth. Two subsequently published notes were also checked. This is a broad research assessment, not an independent verification of every proof or every finite certificate.

NORI1 remains open in the reviewed record. The recommendations below are research problems, not new closure theorems. Two elementary propositions are proved here to clarify how obstructions may be combined. “Unresolved in the reviewed record” means that no resolution was found in this survey; it does not assert priority or certify that no worker has attempted the question.

The main recommendation is to study compatibility on one legal coloring, retaining the root, direction order, and shared edge variables throughout. The direct Eulerian/rainbow formulation is a leading route within this programme. Extending Hollom-type hypotheses is not a priority.

#### 1. The mathematical target and the available reductions

A legal coloring assigns a bit to each undirected edge of \(Q_n\), with \(c(\bar e)=1-c(e)\). NORI1 asks for a monochromatic path between antipodes using every direction once. A full geodesic is determined by a root and a permutation of the directions.

For an ordinary coloring \(f\), let \(A_0(f)\) and \(A_1(f)\) be the roots permitting temporal color words \(0^*1^*\) and \(1^*0^*\), respectively. Reversal gives \(A_1(f)=\overline{A_0(f)}\). The universal paired-root assertion \(A_0(f)\cap A_1(f)\ne\varnothing\), with its quantification over ordinary colorings and dimensions, is equivalent to NORI1 through the odd bridge construction. It does not justify prescribing the root or choosing the two paths independently of their common root.

Three equivalent or sufficient closure targets deserve special attention.

* **Orbit-flip preservation.** If existence of a monochromatic full geodesic survives every flip of an antipodal edge pair, connectivity of the space of legal colorings proves NORI1. A first good-to-bad flip isolates a sharply constrained boundary instance.
* **Sublinear defect or detour.** Let \(\delta(c)\) be the minimum minority-color count on a full geodesic. Cartesian products add \(\delta\). A uniform \(o(n)\) bound therefore proves NORI1. The recent shortest-monochromatic-path result supplies a parallel amplification: if \(L(c)\) is the shortest monochromatic antipodal path length, then \(L-n\) is additive under products. A uniform \(L\le n+o(n)\) also proves NORI1.
* **Entropy loss for bad colorings.** Counterexample-preserving lifts imply that, if any counterexample exists, the family of bad colorings has asymptotically full normalized entropy, including in the balanced regime. A sufficiently strong counting upper bound would contradict this amplification.

These targets offer different ways to avoid proving an unnecessarily rigid local statement.

#### 2. What the articles collectively establish

The following table records the compositions used for the main survey. Later additions are identified separately below.

| Article | Composition reviewed | Main contribution to the closure question |
|---|---:|---|
| I | 42 | Foundations, closure results, and the distinction between unrestricted and rooted assertions. |
| VII | 22 | Low-dimensional endpoint constraints and tournament structure; useful local information without a general extension theorem. |
| VIII | 128 | Edge carriers, profiles, incidence, and shared-edge consistency. Full profile data and rooted support have very different information content. |
| IX | 15 | Faithful cube/boundary reformulations and the extra compatibility required for a common theorem. |
| X | 26 | Low-switch face induction, seam placement, and the obstruction to matching independently obtained endpoints. |
| XI | 414 | Matroidal, Eulerian, rainbow, and holonomy formulations; substantial restricted-family theorems and limitations of generic exchange. |
| XII | 2 | A Hamming-gallery framework with faithful endpoint specializations; the proposed general forcing principle remains a separate problem. |
| XIII | 22 | General involutive rainbow formulations and counterexamples showing that several attractive graph axioms are insufficient. |
| XIV | 260 | Coxeter and rook-gallery geometry, reconstruction laws, relative topology, and localization of the remaining obstruction. |
| XV | 550 | Projective flags, influence and feedback, critical switches, balancing, entropy, turn incidence, and many of the strongest recent obstructions. |

Article XV advanced to composition 551 during the survey. The added shortest-path tensor amplification and the new six-cube critical-profile computation were read separately. Retired Articles II–VI should be treated as historical containers. Inherited arguments about the refuted NORI3 formulation must not be cited as counterexamples to NORI1.

The positive toolkit is substantial. It includes acyclic root saturation; cross-favorability for independent functional reader maps; the common-SCC branching criterion; the finite path-local induction; prescribed roots on source-closed acyclic blocks under the stated fiber hypothesis; square flatness at cross-witness sites in a hypothetical bad coloring; and closure when directed feedback vertex number is at most two. These are useful mechanisms, not merely solved examples.

Articles XIV and XV sharpen the remaining issue in complementary ways. Article XIV shows how much of the coloring can be reconstructed from low-rank gallery data and where a topological obstruction must live. Reconstruction does not itself force a favorable chamber, and an antipodal path supplied by topology need not be direction-simple. Article XV supplies stronger local forcing, normalization, and quantitative machinery, while showing that symmetry, favorable-root density, and low-order statistics can conceal the remaining selection problem.

The turn-incidence programme has also produced positive results: Fourier rigidity, constant-energy forcing, five-cube theorems, and certificates using information beyond a scalar mean. Its failures should be scoped to the particular relaxations tested.

#### 3. Why progress has repeatedly stalled

##### 3.1 Projection removes the dependence needed for selection

A favorable root, an admissible order, and a local exchange often exist separately. The desired path requires their simultaneous realization using the same edge colors. Projecting to a set of roots, a graph of overlaps, a spectrum, or a turn histogram can erase this dependence.

The radial examples are especially informative. Distinct legal colorings can have the same full root/profile incidence and spectrum while having different prefix transport and square curvature. Thus even complete incidence data need not recover the mechanism needed to move a witness. The next invariant must retain some order information.

##### 3.2 Stronger quantifiers create false intermediate goals

NORI1 is existential in both root and order. Prescribing a root, demanding adjacent paired roots, fixing an order in advance, requiring bounded-radius repair, or insisting on a large witness density introduces additional requirements. Several such strengthened statements fail for colorings that already satisfy NORI1.

A useful intermediate lemma should therefore be justified by its implication for the existential target, rather than by its resemblance to a familiar induction hypothesis.

##### 3.3 General graph and matroid models omit cubical consistency

Eulerian balance, involution symmetry, connectivity, square generation, and abstract exchange can coexist without the desired rainbow path in broader models. Their failure identifies missing cube structure. It does not establish that an argument using commuting cube translations and one shared edge assignment must fail.

Conversely, merely adding another generic connectivity axiom is unlikely to recover that structure. Rooted profile sets need not be delta-matroids, and reachability families need not be greedoids.

##### 3.4 Normalization preserves the full difficulty

Counterexample-preserving balancing and distribution lifts make the balanced regime a universal testing ground. They do not make it an easier probabilistic class by themselves. Feed-forward extensions can produce connected interaction graphs while retaining the original difficulty. Cartesian products can dilute witness density and buffer failures in different components.

A proposed simplification must identify a quantity that decreases under the reduction, or a new property that forces a witness despite the embedded core.

##### 3.5 Local exchange can spend the direction budget

A walk can be shortened as a graph walk while remaining unsuitable as a geodesic. Holonomy may connect the desired fiber states through a word that repeats directions too often. Eulerian decomposition controls degrees and edge usage, but a segment need not be rainbow.

The missing lemma concerns bounded direction usage together with color compatibility. Ordinary reachability is too weak a conclusion.

##### 3.6 Scalar averaging misses an extremal event

A monochromatic geodesic is an extremal event. Formal turn distributions can share many moments with legal examples while assigning no mass to the desired minimum. Small principal Walsh tests can all remain positive. Balanced padding can make low-order path statistics resemble independent bits while retaining a hypothetical bad factor.

These results limit particular summaries. They leave room for conditioned statistics coupled across orders and constrained by shared edges.

##### 3.7 Several encodings relocate the same unresolved choice

A faithful equivalence is valuable, but it is not yet a forcing theorem. Moving among galleries, ports, matchings, turns, or return words can repeatedly re-express the same root/order compatibility problem. A new formulation should be evaluated by the new inequality, exchange, or dual certificate it enables.

This diagnosis does not imply that the project has made no progress. The codex now identifies the missing information with much greater precision. The next phase should exploit that precision rather than accumulate additional nearby counterexamples without a named target.

#### 4. When mutual obstruction is stronger

Four logically different objects must be kept separate.

1. A **successful legal coloring defeating a proposed lemma** disproves that lemma's necessity as a proof route.
2. A **countermodel to a relaxation** shows that the relaxation omits a needed condition; it need not be realizable by a coloring.
3. A **necessary condition for badness** holds for every hypothetical NORI1 counterexample.
4. A **counterexample-preserving reduction** transfers hypothetical failure to another class, while preserving only the properties proved for that reduction.

Only the third category can automatically be conjoined on an arbitrary hypothetical bad coloring. A reduction can support such a conjunction after its preservation properties are checked.

**Proposition 4.1 (common-instance conjunction).** Let \(\mathcal B\) be the class of legal bad colorings. Suppose every \(c\in\mathcal B\) satisfies each condition \(C_i(c)\). If no legal coloring satisfies all the \(C_i\), then NORI1 holds.

**Proof.** A member of \(\mathcal B\) would satisfy their conjunction, contradicting its impossibility. \(\square\)

The elementary proposition exposes the practical issue: conditions derived on different transformed colorings cannot be substituted into one conjunction without a preservation argument. In particular, balance and single-orbit boundary criticality must not be assumed simultaneously merely because each is available through a separate normalization.

**Proposition 4.2 (product-persistent failures).** Suppose a class is closed under Cartesian products. For each \(i\), let \(F_i\) be a property such that \(F_i(c)\) implies \(F_i(c\oplus d)\) and \(F_i(d\oplus c)\) for every legal factor \(d\). If each \(F_i\) has a legal example \(c_i\), then \(\bigoplus_i c_i\) satisfies all the \(F_i\).

**Proof.** Apply the two persistence assumptions successively to the factor carrying each property. \(\square\)

Thus combining failed tests need not strengthen them: products may combine their failures too. Persistence must be proved separately for each proposed test; this proposition makes no claim that every obstruction in the codex has that property.

A useful compatibility ledger should record, for each reduction, whether it preserves badness, balance, a chosen root, an order witness, criticality, direction usage, and the statistic being optimized. Unknown entries should remain unknown.

The most promising conjunctions are instead internal to one coloring:

* square-flatness constraints for all direction pairs, together with mixed-derivative identities;
* critical-orbit constraints for all affected paths, together with shared edge variables;
* full profile rotation, reversal, and square locality;
* turn-incidence relations together with nonlinear star consistency;
* Eulerian flow together with the usage budget of a cubical return word.

None of these conjunctions is proved inconsistent here.

#### 5. Six leading programmes

##### Programme A: critical repair with shared-edge clauses

At a first good-to-bad antipodal-orbit flip, every old red full geodesic must meet the removed red edge internally, and no old path can have the opposite edge as its sole blue edge. Endpoint witnesses admit a rotation repair. The boundary condition therefore gives information about many paths simultaneously.

The proposed first goal is a dimension-uniform implication: these shared-edge constraints force either an avoiding red path, an endpoint witness, or an opposite-edge one-defect path. Such an implication would prove flip preservation and close NORI1.

The Q4 surgery certificate is encouraging evidence for structured path families. Q8 examples defeat a repair argument restricted to two previously free edges. The recent Q6 UNSAT computations extend finite critical-profile exclusions, but no independently checked UNSAT proof log is supplied in that note; they should remain labeled computer-assisted evidence.

The next advance should be a recursive implication scheme with an unbounded number of involved edges and a controlled structural invariant. A larger fixed-dimensional SAT instance alone will not provide it.

##### Programme B: direct Eulerian/rainbow exchange with a usage budget

Balanced orientations and paired lifts provide Eulerian and covering-space structure. In the paired lift, red fiber moves are involutions \(U_i\); return words encode the desired antipodal transport. The simple-bigon formulation uses each base direction twice. This is an appropriate direct target.

Seek an exchange theorem that changes the root and the return word together, retaining the two-use budget, until the fiber endpoint is antipodal. The number of square commutators may grow with dimension. A fixed bound on that number is incompatible with product examples.

The first useful intermediate result would be a dual alternative: either an allowed budget-preserving exchange improves a well-founded potential, or a cut certificate contradicts antipodal color reversal and cubical edge consistency. Generic Eulerian circuit switching is insufficient; the exchange must use the cube's labeled square relations.

A Minty-inspired potential over walks remains plausible only if it tracks direction multiplicities and proves that its minimum has the required budget. Minimizing ordinary length or repeated vertices does not establish this.

##### Programme C: simultaneous flatness and derivative integrability

Badness forces flatness on cross-favorable sites for every relevant pair of directions. The individual active-derivative avoidance example is a successful coloring; it does not establish compatibility of all badness constraints.

Work on one shared Boolean edge assignment. Combine all pairwise flatness implications, source-block root prescription, and the identities among iterated Boolean derivatives. The first goal is to prove that persistent activity avoiding one cross-witness set must create activity on another such set.

A proof would need to move witness information between fibers, not merely show that a surviving cycle exists. The arc-complement theorem supplies a surviving directed cycle after deleting the endpoints of an influence arc. It does not supply two vertex-disjoint cycles.

A useful intermediate theorem would force a reducible feedback block under the full conjunction. Enlarging the solved bound from two exceptional directions to another fixed number is lower priority unless it reveals such a mechanism.

##### Programme D: entropy compression across overlapping path networks

Let \(L_N=N2^{N-2}\) be the number of independent antipodal edge-orbit bits. The amplification theorem gives, from a bad seed of dimension \(d\), a balanced bad family with
\[
\log_2 B_N^{\rm bal}\ge
[N-d-2\log_2(N-d+1)]2^{N-2}.
\]
Consequently an upper bound
\[
B_N^{\rm bal}\le 2^{(1-\eta)L_N}
\]
for a fixed \(\eta>0\) along arbitrarily large even dimensions would prove NORI1.

This is a precise quantitative target. Existing random-coloring bounds save too few bits on this scale. Independent or parity-peelable Petrie packings encounter a counting barrier; overlapping constraints must do more than reproduce an independence estimate.

Try an injective encoding of bad colorings that conditionally recovers a positive fraction of edge-orbit bits from the others. The decoder must exploit the failure of whole overlapping path networks. A small expected number of violations or a high-probability theorem with insufficient exponent does not meet the target.

##### Programme E: integrable profile transport with order witnesses

Full path profiles satisfy rotation, reversal, and square locality. Together these laws reconstruct a legal coloring. Rotation and reversal alone admit formal countermodels. Root/profile incidence alone admits twins with different transport behavior.

The first goal is a transport invariant retaining a controlled set of witnessing orders for each profile. It should respond to adjacent swaps using the shared-edge square law and allow the root to move.

One possible target is an augmentation theorem for partial profile coverage under these laws, with a dual certificate that cannot occur in an integrable system. Full direction-profile surjectivity would close NORI1 through direction gauges. A perfect matching between roots and profiles is stronger and should not be imposed without need.

##### Programme F: nonlinear star consistency in turn incidence

Write \(s_i(x)\in\{-1,1\}\) for the color sign of the incident direction-\(i\) edge. Besides edge consistency and antipodal oddness, the pair variables \(h_{ij}(x)=s_i(x)s_j(x)\) obey
\[
h_{ij}(x)h_{jk}(x)=h_{ik}(x).
\]
These nonlinear identities couple the turn data. They are absent from many formal moment countermodels.

The first goal is a conditioned, cross-order inequality forcing positive mass at turn grade one. The full two-sector Fourier calculations and existing certificates supply useful starting identities. Fixed low-order scalar moments and small principal Walsh minors are already poor candidates for a universal criterion.

A successful approach must explain why the formal zero-minimum distributions cannot be realized simultaneously across stars and path orders.

#### 6. Twenty-four further directions with explicit tests

The following are additional problems or refinements of the leading programmes. They are ordered by their connection to a closure mechanism, rather than presented as twenty-four equally likely solutions.

**7. Near-geodesic detour bounds.** Use the known existence of a monochromatic antipodal path and seek \(L-n=o(n)\). The tensor theorem makes this sufficient for closure. Test any shortening potential against holonomy examples with large excess.

**8. Sublinear minority bounds.** Seek \(\delta(c)=o(n)\) by an adaptive root/order algorithm. Product additivity makes this sufficient. A sublinear switch count is a different statement and does not have this implication.

**9. A coherent seam invariant.** Retain two interior seams together with their witnessing partial paths in a paired-root induction. First prove a composition rule under gluing. Endpoint-prescription failures prohibit replacing this data by endpoints alone.

**10. Cross-face witness transport.** Form a compatibility structure whose vertices are witnessed cross-favorable roots in different deleted-direction faces. Seek a transport rule derived from common edge variables. Pairwise nonempty sets alone are insufficient.

**11. Conditional influence decomposition.** Prove a dichotomy between a reducible feedback region and a family of sufficiently strong overlapping path constraints for entropy compression. This is a proposed dichotomy, not an established consequence of high influence or connectivity.

**12. A complexity measure stable under padding.** Define a measure that ignores feed-forward reader attachments and records the obstruction-bearing core. Test additivity or monotonicity under Cartesian products. Connected interaction graphs and raw direction counts do not serve this purpose.

**13. Balanced reconfiguration boundaries.** Use connectivity under directed-cycle flips to locate a first failing balanced move. Derive the constraints on every geodesic meeting that cycle. This may retain balance more naturally than a single-orbit flip, at the cost of a larger repair interface.

**14. A normalization compatibility theorem.** Determine which critical boundary conditions survive balanced lifts, or derive a replacement boundary condition that does. A positive theorem would permit several currently separate constraints to be used together.

**15. Symbolic critical-clause elimination.** Encode path failure using one variable per antipodal edge orbit. Seek a dimension-uniform resolution or algebraic elimination rule guided by cube squares. The deliverable should be a proof schema, rather than a sequence of solver verdicts.

**16. Learn a recursive certificate from finite surgery.** Compare minimal useful path families in dimensions four through six and identify a structural recursion. Require a proof that the recursion covers all assignments. Failure of such a recursion would also sharply delimit this route.

**17. Adaptive root selection.** Allow an algorithm to choose roots after observing edge information. Establish an invariant that explains why an unresolved region contains a new useful root. Fixed-root lower bounds do not automatically defeat adaptive selection.

**18. Support-aware cuts in Boolean path DAGs.** For each root, the subset lattice records geodesic prefixes. Study cut certificates for failed monochromatic reachability and relate cuts at different roots through shared edges. The target is an incompatibility theorem for the family of cuts.

**19. A noncommutative positive expansion.** Seek an algebraic expression whose positive terms correspond to legal budgeted return words. Ordinary linear span and cancellation-prone determinants lose support information; positivity must be proved before nonvanishing becomes useful.

**20. Interlacement with variable complexity.** In the commutator factorization of return words, allow a dimension-dependent interlacement graph while controlling each direction's occurrences. Identify a structural exchange on that graph that preserves the cubical interpretation.

**21. Relative top-cell cancellation.** Article XIV localizes the primary obstruction to bad Coxeter cells. Seek color-sensitive identities forcing their total obstruction to vanish under global badness. Ambient equivariant index alone does not provide the required cancellation.

**22. Direction-support graded chains.** Refine a chain complex so that a boundary operation records repeated directions instead of forgetting them. First establish that a nonzero class forces a full-support simple path; otherwise the construction merely recovers antipodal connectivity.

**23. A coupled Smith obstruction.** Investigate whether shared-color constraints between root fibers force additional relations among the obstruction classes. Constructing a Smith tower is not automatically easier than proving the corresponding index bound.

**24. Conditioned turn inequalities.** Condition on a witnessed prefix or a star pattern before averaging turns. Compare the resulting conditional relations across overlapping prefixes. The target is an inequality unavailable to an arbitrary scalar turn distribution.

**25. Tensor-stable spectral information.** Search for a statistic whose vanishing characterizes failure and whose product law retains rare witnesses. A statistic that decays harmlessly under tensor powers is unlikely to force closure through a uniform positive lower bound.

**26. Extremizers within a common legal class.** Optimize a potential only after fixing which conditions must be preserved: legality, balance, boundary criticality, or badness. Derive first- and second-variation inequalities for permitted moves. Combining extrema from different classes is unjustified.

**27. Witness-preserving smoothing.** Study whether a distributional smoothing move can be accompanied by a controlled transfer of a newly found geodesic back to the original coloring. Without transfer, pseudorandomization may simply conceal the original core.

**28. Global diagonal-fiber constraints.** The joint orientation fibers have strong overlap identities but may have sparse supported labels. Seek an identity involving the diagonal condition itself, retaining order witnesses. Connectivity of the incidence graph or strong connectivity of one orientation has already proved insufficient.

**29. A minimal joint obstruction catalogue.** For each candidate model, impose all known laws that arise from a single coloring and identify a smallest incompatible subsystem under badness. This should target a named forcing lemma; indiscriminate searches for another obstruction have diminishing value.

**30. Boundary transfer after a cubical mechanism is found.** Test a successful cube argument against boundary tournaments using their ordering and projection constraints. Preserve the projected-edge forest condition where required for simplicity. A unified theorem is valuable, but closure of NORI1 need not await a general matroid theorem.

#### 7. Tests every proposed route should pass

Before substantial computation, state the target implication and the information retained. Run it conceptually against the following families and distinctions:

* fixed-root failures, parity-isolated paired roots, and product buffering;
* connected feed-forward embeddings and strongly coupled examples;
* legal radial incidence twins with different order transport;
* formal profile systems missing square locality;
* formal moment distributions with no minimum-turn mass;
* cyclic-reader obstructions to small principal Walsh tests;
* Eulerian double-label cycles and holonomy words with excess direction use;
* critical-repair examples requiring more than two previously free edges.

Passing these tests is not evidence of a theorem, but failing one should prevent a large search around the same premise.

Finite computation is best used to decide a sharply formulated lemma, identify a recursive certificate, or test whether a proposed conjunction is already inconsistent in small dimensions. A claim of finite exhaustion should include the encoding, symmetry reductions, reconstruction check, and certificate status. Solver output without a checked proof log should be labeled accordingly.

The strongest near-term allocation is to pursue Programmes A and B as direct constructive routes, C and E as compatibility routes, and D as an independent quantitative route. Programme F merits sustained attention because it has already yielded forcing certificates beyond the simplest averages. The remaining problems provide targeted branches and intermediate milestones.

#### 8. Source register and limits of the assessment

The principal subsection sources are:

* `gauge_critical_switches_and_clustered_witnesses_on_full_paths`, composition 168: feedback closure, source-block prescription, balancing, entropy, and criticality.
* `directed_influence_components_and_monotone_seam_lifting`, composition 53.
* `cartesian_factorization_of_paired_roots_and_interaction_prime_reduction`, composition 49.
* `full_geodesic_color_profiles_span_the_entire_binary_space`, catalogue composition 86.
* `paired_direction_involutions_and_geodesic_endpoint_matchings`, catalogue composition 135.
* `integral_saturation_and_fourier_rigidity_of_geodesic_incidence`, composition 7.
* `projective_two_turn_incidence_fourier_kernel_rigidity_and_the_five_cube_theorem`, composition 6.
* `reconstruction_of_antipodally_odd_edge_colorings_from_local_turn_data`, composition 1.
* The path-local finite-induction and pendant-tree subsections cited in the influence and paired-root manuscripts.

Selected research-note sources, identified by stable ID, are:

| Topic | Source |
|---|---|
| Profile integrability | `note_nori_profile_integrability_three_local_laws_20261016_r11254` |
| Incidence twins and prefix failure | `note_nori_radial_majority_middle_sphere_prefix_failure_20261017_r11336`, v2 |
| Orbit boundary, defect, and products | `note_143f396e6155ca89c587d00f`, v5 |
| Four-cube surgery | `note_nori_q4_ten_path_critical_surgery_r11435` |
| Bounded repair obstruction | `note_nori_q8_two_free_edge_critical_repair_obstruction_20261016`, v6 |
| Six-cube computation | `note_nori_q6_profile_critical_sat_extension_r11435`, v1 |
| Shortest-path tensor amplification | `note_98b1e0fc35badd4e7eb3124d`, v1 |
| Joint diagonal fibers | `note_nori_joint_cyclic_orientations_sparse_fibers_20261017_r11435`, v5 |
| Connected reader embedding | `note_nori_universal_nonlinear_interaction_star_embedding_20261017` |
| Formal moment obstruction | `note_9a71476ba3e5aa36d3420ffd` |
| Principal Walsh obstruction | `note_7d57a9fb16864260c6242635` |
| Simple-bigon return words | `note_c944daa4c653527d2f6bf61e` |
| Interlacement and commutators | `note_f45cc9ea86406fa362616dde` |
| Balanced reconfiguration | `note_28253102a7f86f01503ff6a5`, v1 |
| Localized topological obstruction | `note_014bac044b204c87d0b0441d` |
| Relative topology limitation | `note_cb90862e1fbd127a586d2116` |
| General graph square axioms | `note_nori_xiii_joint_square_conditions_fail` |

All recommendations remain conditional research proposals. The central unresolved question is whether the coupled constraints of one legal coloring force a witness, even though their separate projections permit many obstructive configurations.
