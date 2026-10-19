## Global compatibility and routes to closure

### Obstruction compatibility and a programme for NORI1 closure

#### Current assessment and revised closure programme — 19 October 2026

This assessment updates the 17 October survey after surveying the catalogue of 36 research notes created or revised since that publication and examining the principal proofs and limitations, Article XVI composition 47, the current strategic Subsection composition 20, the implication-transport Subsection composition 27, and relevant arguments in the gauge Subsection composition 177. The review audits the principal implications and limitations; finite solver certificates retain their recorded verification status. NORI1 remains open.

The earlier thirty-direction catalogue served as an exploration map. The present assessment selects a narrower programme. Its principal target is the unrestricted nonlinear paired-flat square boundary. The seam-interval formulation supplies a second representation of the same full-class problem. Shortest-path methods remain a secondary route with a specific anchor-production obligation.

##### A. What the recent work has accomplished

**Balanced boundary normalization is available.** Article XV supplies a good/bad neighboring pair of perfectly balanced paired-flat colorings whenever NORI1 fails. They differ by one antipodal alternating-square switch. The new two-hit involution preserves the temporal word of every full geodesic meeting the switch set twice. Consequently every red witness on the good side meets the switched set once, strictly internally. This resolves the normalization issue raised in the original item 14 and places balance and criticality in one instance.

**The full-class seam representation has improved.** The unrestricted two-direction formula uses one shared partial coloring and is a bipartite 2-CNF whose satisfying assignments are precisely bad completions. Its later seam-interval theorem permits arbitrary dependence on the connector bit. The layer-defect field may be any antipodally even edge assignment, so an argument may use the proved interval constraints but cannot impose an additional defect identity without proof. Interior and exterior seam formulas each have a canonical satisfying completion. A contradiction must use both families. The finite two-seam-root certificates demonstrate one mechanism in small dimensions; the universal transport theorem remains open.

**Nested-core forcing is a substantial theorem.** A nonsingular principal slope core and a legal parity-peeling order give red geodesics for arbitrary nonlinear phase functions, with a prescribed root count in every parity fiber. The directed feedback criterion and rank-at-most-four theorem extend this mechanism to unbounded matrix sizes. These are mathematically useful results. Their hypotheses retain affine dependence on the within-pair bits.

**Shortest-path geometry has gained useful inequalities.** Endpoint absorption, derivative flux, parallel-face cuts, quadratic cut rigidity, and spectral red-anchor bounds give constraints in a single coloring. The anchored three-face example proves that individually compatible demands can incur a collective surplus. The unresolved step is to derive the required face family and anchors from a hypothetical counterexample.

**The team has also corrected its own relaxations.** Walk pumping shows that several unrestricted-walk energy minimizations recover an existing rooted geodesic-defect quantity. The unanchored weighted-capacity calculation proves that its capacity inequality cannot be violated. The growing-degree blocker barrier closes the bounded-degree version of that relaxation. These results should terminate the corresponding proof attempts.

##### B. Where the work has drifted

Four patterns recur in the recent record.

1. **Successive finite classifications.** The paired-gate investigation progressed through three, four, five, and six pairs, then through ranks four and five. The nested-core theorem justified part of that progression by exposing a reusable mechanism. The current rank-five projective compression still leaves both arbitrary rank and nonlinear within-pair dependence open. The next rank computation should be justified by a dimension-uniform reduction or a transfer theorem before it receives further priority.
2. **Equivalent energy refinement.** Causal means, Fourier survival, Gibbs energies, odd-occurrence sampling, and correlated transport yield valid pathwise certificates. Introducing another intrinsic energy with “a uniform sublinear bound would close NORI1” leaves the central upper-bound problem in place. Walk pumping gives a rigorous reason for this concern in several of those formulations.
3. **Conditional certificates without a source theorem.** Red endpoint stars, multiple deep red anchors, a near-transitive spine, a favorable near-full face, and a contradictory implication component each support useful forcing lemmas. The existence of those configurations in the required full class is the next mathematical obligation. Refining their consequences alone does not supply it.
4. **A moving small-certificate target.** Four-path packets, six-path packets, parity diamonds, selector portfolios, and two-root certificates have developed a rich local calculus. A universal theorem may require a certificate whose size grows with dimension. Small examples establish feasibility of a mechanism; they do not justify a universal bound on its size.

The publications generally state these scope limits carefully. The corrective issue is allocation of further investigation and visibility of the unresolved implication. The original broad agenda contributed to this dispersion and is narrowed here.

##### C. A scope lemma for the affine paired-gate programme

The following observation makes the transfer obligation explicit.

Write the members of pair \(i\) as \(a_i,b_i\), put \(q_i=x_{a_i}\) and \(p_i=x_{a_i}+x_{b_i}\), and use addition in \(\mathbb F_2\). A paired-flat coloring has complementary rules \(f_i(p,q)\) and \(1+f_i(p,q)\), independent of both bits in its own pair. Its gate satisfies \(f_i(p,q+\mathbf1)=1+f_i(p,q)\).

**Proposition C.1 (the universal lift retains nonlinear gate dependence).** Let \(b\) be any legal coloring of \(Q_m\). Its standard paired-flat lift is
\[
c_{a_i}(x,y)=b_i(x),\qquad c_{b_i}(x,y)=1+b_i(x).
\]
In the variables \(q=x,\ p=x+y\), its gates are \(f_i(p,q)=b_i(q)\). Such a gate has the form
\[
f_i(p,q)=a_i(p)\cdot q+\theta_i(p)
\]
for every \(p,q\) if and only if \(b_i\) is affine.

**Proof.** Fix any \(p\). The displayed representation then expresses \(b_i(q)\) as an affine function of \(q\). Conversely an affine \(b_i\) supplies the representation with coefficients independent of \(p\). Uniqueness of the Boolean affine representation also forces any representing coefficients to be independent of \(p\). \(\square\)

Thus even a proof of odd-matrix peeling for all ranks would settle the stated affine-gate class. Applying that theorem to the standard lift covers affine original edge rules. A further reduction or nonlinear forcing argument is needed for arbitrary original rules.

**Proposition C.2 (one permitted square switch can leave the affine-gate class).** Suppose there are \(m\ge4\) pairs and gate \(i\) is affine in \(q\) on every parity fiber. Switching one antipodal pair of alternating \(i\)-squares makes that gate nonlinear in \(q\) on the affected outside-parity fiber.

**Proof.** Put \(k=m-1\), and restrict to the outside pair parities fixed by the switched square. Its two antipodal outside assignments correspond to \(q=z\) and \(q=z+\mathbf1\) in \(\mathbb F_2^k\). The gate changes by
\[
d(q)=\mathbf1_{\{q=z\}}+\mathbf1_{\{q=z+\mathbf1\}}
=\prod_{j=1}^{k}(1+z_j+q_j)+\prod_{j=1}^{k}(z_j+q_j).
\]
The degree-\(k\) terms cancel. For each \(j\), the coefficient of \(\prod_{\ell\ne j}q_\ell\) is \((1+z_j)+z_j=1\). Hence \(d\) has Boolean algebraic degree \(k-1=m-2\ge2\). Adding an affine gate preserves that highest degree. \(\square\)

This proposition explains why closure of the affine-gate subclass does not establish preservation under the elementary switches used by the full paired-flat boundary reduction. It also supplies a focused bridge problem: handle the nonlinear truth-table perturbations generated by legal square switches, allowing arbitrary previously generated nonlinear dependence.

##### D. The primary closure obligation

For a paired-flat coloring \(G\), let \(S\) be the eight edges of an antipodal pair of alternating squares, and let \(T_SG\) be the legal square switch.

**Boundary-preservation target.** If \(G\) has a red full antipodal geodesic, prove that \(T_SG\) has one.

The paired-flat parameter space is connected under these switches and contains successful colorings. Therefore this target, in all even dimensions, proves NORI1 through the standard lift.

The existing two-hit transport permits the following fully specified equivalent repair obligation. In the only unresolved case every red full geodesic of \(G\) meets \(S\) in one internal edge. Produce a full geodesic \(Q\) such that every edge of \(Q\) outside \(S\) is red in \(G\), and every edge of \(Q\) in \(S\) is blue in \(G\). The path then becomes red after switching. A full geodesic meets \(S\) at most twice. The strict boundary hypothesis excludes a zero-hit repair directly and a two-hit repair through the inverse temporal-word involution. Hence a surviving repair uses one switched edge.

This is a closure-equivalent target, rather than a newly proved repair theorem. It is narrower than an unspecified request for collective behavior: the admissible configurations, legal move, known transport, and required witness are fixed. The next investigation should seek a root-and-order exchange or a dual obstruction with a well-founded decrease. It may use a number of paths or exchanges growing with dimension.

A prospective proof should state which quantity decreases, why the move preserves the legal common coloring data, and how a terminal obstruction contradicts the strict internal-hit boundary. Connectivity of an exchange graph by itself supplies none of these three conclusions.

The nonlinear gate problem belongs at the center of this route. An affine principal-core argument remains useful when a boundary analysis proves that its hypotheses occur. Imposing those hypotheses at the outset changes the class being attacked.

##### E. Secondary routes and the next admissible advance

| Route | Next result that would justify sustained priority | Current stopping condition |
|---|---|---|
| Unrestricted seam intervals | Derive transport between interior and exterior clause families from the interval law in arbitrary partial colorings; or prove a reusable clause-generation induction with a stated invariant. | Further fixed-size packet censuses without a general transport rule. |
| Shortest monochromatic paths | Derive overlapping blocked faces with red anchors strong enough to exceed a proved capacity bound, or prove a uniform sublinear detour estimate. | Further optimization of arbitrarily prescribed anchored face configurations without a theorem producing them. |
| Affine principal-core peeling | Prove the unrestricted-rank matrix theorem, or establish a forcing step for nonlinear \(q\)-gates arising at the boundary. | Increasing the finite rank ceiling alone. |
| Entropy compression | Give an encoding or conditional information inequality with savings on the required full-orbit scale, accounting for overlaps and witness selection. | Independent pivot-square packing, whose established capacity is only \(O(n)\) bits. |
| Causal rounding | Prove a uniform estimate for a nondegenerate path family, such as globally shortest red antipodal paths, using constraints absent from arbitrary walks. | Adding a new equivalent intrinsic energy without an upper-bound mechanism. |
| Turn/Fourier inequalities | Use shared-star or cross-order identities to rule out a realizable badness configuration. | Increasing a bounded scalar moment or localization degree already covered by the relaxation barriers. |

These are research decision criteria. A subsidiary theorem may still merit publication for its independent mathematical value. Its contribution to closure should be stated through the implication it supplies.

##### F. Two corrections to the quantitative agenda

**Walk restriction.** The walk-pumping result applies to the intrinsic uniform odd-occurrence Gibbs energy and the hybrid/coupled policies containing it. Those quantities equal the minimum blue count of a full geodesic rooted in a red-antipodally connected component, for every fixed positive inverse temperature. Their pathwise inequalities remain valid. The globally shortest-path restriction blocks that pumping operation and defines a meaningful new estimate to seek. The collapse should accompany every citation of the affected intrinsic energies.

**Amplification needs an upper bound, with no extra tensor requirement on the certificate.** Let \(\delta(c)\) be the global minority defect, with the established product law \(\delta(c^{\square k})=k\delta(c)\). If any nonnegative statistic \(F\) satisfies \(\delta(c)\le F(c)\) for every legal coloring and
\[
\sup_{c\text{ on }Q_n}F(c)=o(n),
\]
then NORI1 follows. Indeed, for a seed of dimension \(d\),
\[
k\delta(c)=\delta(c^{\square k})\le F(c^{\square k})=o(kd).
\]
Divide by \(k\) and let \(k\) grow. Thus \(\delta(c)=0\). This argument requires no product identity for \(F\). It is already implicit in the recent entropy-localization note and should govern subsequent searches: permit couplings that improve a universal bound even when they sacrifice additivity of the auxiliary statistic.

##### G. Grand-conjecture scope and publication discipline

The project API states a grand objective covering both unrestricted NORI1 and the intended vertex-simple boundary-tournament conclusion through one common structure. The recent work reviewed here is overwhelmingly cubical. A cube closure theorem would be a major advance; a claimed grand closure must also supply the boundary reduction and preserve distinct original vertices.

For any proposed common exchange principle, record its admissible objects and terminal simplicity condition in both settings. A cube-only determinant, paired lift, or seam formula currently contributes to the NORI1 side. A broader theorem requires its own verified transfer. The boundary comparison should test a mechanism after its cubical forcing content is identified.

Future updates to this Subsection should distinguish:
* a newly proved forcing mechanism;
* a theorem establishing that its hypotheses occur in the required class;
* a closure-equivalent reformulation;
* a restricted-family theorem;
* a computational certificate;
* a method obstruction.

The most consequential next paper would supply the second item for an existing strong mechanism. The historical catalogue below is retained for context. Its priorities are superseded by this assessment; its mathematical statements and subsequent developments retain their stated scope.

##### H. Sources for this revision

The principal new sources are the current gauge and implication-transport manuscripts cited above, together with:

* `note_nori_double_square_temporal_word_transport_r11510`, v1: balanced strict internal-hit boundary.
* `note_nori_nested_core_phase_peeling_r11660`, v2, and `note_nori_m6_full_peeling_feedback_core_r11685`, v1: nested-core forcing and feedback.
* `note_nori_rank4_fano_column_quartet_forcing_r11704`, v1: all-size rank-four theorem with finite bases.
* `note_28429d9005d311b5a8dfea67`, v1: rank-five compression, conditional on solver certificate validation.
* `note_nori_xvi_walk_pumping_shortest_repair_20261018`, v3: degeneration of unrestricted-walk energies and shortest-path repair.
* `note_nori_xvi_budgeted_bigon_partition_exchange_20261017_r11435`, v18: budgeted exchange, causal rounding, coupling, and transverse-flux identities.
* `note_nori_xvi_odd_rank_quadratic_face_pairwise_gluing_20261018_r11531`, v2: unanchored capacity limitation.
* `note_nori_xvi_anchored_three_face_surplus_duality_20261018_r11531`, v2, and `note_nori_xvi_spectral_cross_layer_blue_surplus_20261018_r11531`, v2: anchored surplus and deep-orbit capacity.
* `note_44a31df94fce8e46e5802ac0`, v1: growing-degree blocker-relaxation barrier.
* `note_nori_projective_support_code_fractional_critical_boundary_20261017_r11510`, v4: pivot packing and its linear capacity ceiling.

Propositions C.1 and C.2 are proved above as scope checks. The priority judgments are research recommendations. The boundary-preservation, unrestricted transport, and universal quantitative bounds remain open.

---


#### Historical survey — 17 October 2026

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

The elementary proposition exposes the practical issue: conditions derived on different transformed colorings cannot be substituted into one conjunction without a preservation argument. For single-edge-orbit criticality, balance requires its own preservation argument. For antipodally paired alternating-square criticality, Article XV supplies simultaneous balance and a good/bad boundary; the revised programme uses that established normalization.

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

**14. Balanced square-boundary normalization: resolved.** Article XV supplies a balanced paired-flat good/bad pair differing by one antipodal alternating-square switch. The two-hit transport theorem strengthens this to the strict internal-hit boundary. The current objective is elimination of that boundary, as stated in the revised programme above.

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


###### Article XVI update: resolved normalization interface and two-hit square transport (17 October 2026)

The normalization compatibility issue listed as item 14 above has now been audited against Article XV. The existing Subsection *Gauge-critical switch cochains and clustered near-good paths* already proves a stronger statement than the originally requested combination: if NORI1 fails, a perfectly vertex-balanced paired-flat bad coloring is adjacent, by a single antipodally paired alternating-square flip, to a good balanced paired-flat coloring. This is the established one-paired-square boundary reduction, originally accompanying the one-Lipschitz defect estimate (EC8). Accordingly, **item 14's joint-balance/square-boundary existence problem is settled by the preceding Article XV work**. The unsolved problem is to eliminate the resulting boundary.

A new unrestricted strengthening is now proved and integrated into that same Article XV Subsection at composition 170, with provenance research note \`note_nori_double_square_temporal_word_transport_r11510\` (session \`session_nori_r11510_3\`).

**Two-hit temporal-word involution.** Let \(T_F\) flip an antipodal pair of alternating squares \(F,\tau F\) on two cube directions. The family of full rooted geodesics traversing two switched edges admits a bijection across \(T_F\) that preserves every temporal color position. In one case both edges lie on the same square and are consecutive; swapping their two directions chooses the alternate two-step route, and the color switch restores their old ordered colors. In the other case the two hits lie in opposite squares and must be the first and last edges; simultaneously exchange the endpoint directions \(i,j\) and translate the root by \(e_i\oplus e_j\). The intermediate edges agree, and alternating color rules restore the endpoint colors after switching. Both transformations are involutions.

**Strict critical boundary.** If a good legal coloring \(G\) and a bad legal coloring \(B=T_FG\) differ by one alternating antipodal square pair, every red full geodesic of \(G\) has precisely one switched edge, strictly internally. A path with no hits remains red in \(B\); a path with two hits is carried by the involution to a red witness in \(B\); a path with one endpoint hit becomes a one-blue endpoint path in \(B\), made red by cyclic root rotation. Combining with Article XV's earlier balanced boundary theorem therefore places the *strict one-internal-hit condition* and *perfect vertex balance* in a single hypothetical bad/good neighboring pair.

This substantially refines Programme A by removing the zero- and two-hit alternatives from its critical-boundary interface. It remains to prohibit one strictly internal switched edge across **all** red witnesses of a balanced good coloring while the switched coloring admits no monochromatic path. No closure theorem for that configuration is claimed.


###### A two-pair compatibility forcing lemma

The paired-flat lift of Article XV permits studying a hypothetical counterexample in a balanced legal coloring of Q_(2m) with m>=3, without bounding the Boolean dependence among direction pairs. A new seam-completion theorem has been proved in the established *Gauge-critical switch* Subsection (composition 171, provenance note \`note_nori_two_pair_seam_forcing_r11510\`).

Fix two paired direction groups P,Q and the remaining direction set J, with |J|=2m-4. Suppose a zero-colored full J-geodesic joins (u,y) to (u,bar y), using one frozen assignment u of the four omitted bits. The restriction of the two pair gates at J-root y is an ordinary Q4 paired-flat coloring A with rules a,1+a,b,1+b. Their values at the opposite J-endpoint are the antipodally reflected complementary coloring A^+. The full J-path extends to a red full antipodal Q_(2m)-geodesic unless both a,b are mutually coupled unary readers,
\[
a=x_r+\alpha,\quad b=x_s+\beta,\qquad
r\in\{2,3\},\ s\in\{0,1\},
\]
and
\[
a(u)={\bf1}_{s=0},\qquad b(u)={\bf1}_{r=2}.
\tag{XVI-S1}
\]
The proof requires only a four-bit lemma, independently verified on all 4096 interfaces. After translating u to zero, 24 explicit root/order/cut routes cover 252 of the 256 gate-table pairs, leaving four mutual-reader cases. In those cases the red graph at the seam is a four-cycle using only the unread directions, so an antipodal completion through the seam cannot occur. This local lemma lifts to every dimension by placing the four omitted steps before and after the witnessed inner J-geodesic.

**Simultaneous counterexample constraint.** For every hypothetical bad paired-flat coloring, every P,Q, and every J-root y, let U_y be the set of frozen four-bit assignments supporting any all-zero full J-geodesic from (u,y). If U_y is nonempty, the two pair gates at y must be mutual unary readers, and U_y is contained in a four-element affine subcube (XVI-S1). Therefore \(|U_y|\le4\). Five distinct compatible inner red witnesses at one J-root force a full monochromatic geodesic. A non-unary outer interface and even one inner red witness also force one.

This creates a specific **obstruction-compatibility problem** beyond scalar histograms: can a single globally legal coloring avoid near-full J-witnesses at all choices of P,Q, or else arrange the required mutual-reader four-cycles simultaneously for every such witness? The theorem does not prove existence of a J-witness, so it does not close NORI1. The four-bit exceptions are compatible with ordinary local paired-flat colorings; eliminating them requires constraints across different deleted-pair choices. A separate endpoint-pair identity in the same Article XV Subsection gives the factor \((1+z^2)\) and invariance of the complete endpoint-pair temporal-word family under arbitrary changes to its paired gate.

The theorem and proof are recorded in \`nori_two_pair_seam_forcing.md\`, with checker \`nori_two_pair_seam_certificate.py\`. The latter also constructs twenty independently generated nonlinear Q8 extensions.


###### Joint obstruction rigidity: three pairs and local active cycles

**Three-pair theorem.** Let c be an arbitrary legal antipodally odd paired-flat edge coloring of Q6 with three direction pairs P_0,P_1,P_2. If no four-dimensional face retaining two whole pairs and freezing the third admits a monochromatic full geodesic, then its three pair gates are signed unary readers arranged around a directed three-cycle. Explicitly, after cyclic relabeling or reversing the cycle, f_i(x)=x_(d_(i-1))+epsilon_i where d_(i-1) is one of the two bits in the previous pair. There are 128 labeled systems of this form (2 cyclic orientations * 2^3 reader choices * 2^3 phases), and every one admits an all-red full antipodal geodesic. Therefore every legal paired-flat Q6 coloring has a constructive red full witness: either extend a red two-pair face by the omitted pair using antipodal oddness, or normalize a reader cycle and use its explicit full red path.

**Proof of rigidity.** For each pair-parity vector p in F2^3, parameterize states by (q_i,q_i+p_i) in each pair. The restricted gate h_i^p(q)=f_i(q,q+p) is independent of q_i and satisfies h_i^p(bar q)=1+h_i^p(q). An odd function of two Boolean inputs is a signed unary reader. Thus each h_i^p reads some q_(sigma_p(i)), with sigma_p(i)!=i. If sigma_p(i)=j and sigma_p(j)=i, then in the four-face on pairs i,j with third pair fixed from that state both gates are nonconstant, so the established R=2E(a)E(b) identity supplies a red full face path. Under the hypothesis this is prohibited. Hence sigma_p is a loopless functional digraph on three labels with no two-cycle, so it is one of the two directed three-cycles.

Because f_i ignores the bits of its own pair, sigma_p(i) is independent of p_i. A change of directed three-cycle orientation changes sigma_p(i) for every i. Thus the orientation is independent of each p_i and is constant over all p. Write sigma(i)=j and sigma(k)=i for the remaining label k. With any fixed assignment of pair j, gate f_k varies under flipping both bits of pair i, because its diagonal restriction reads q_i. The absence of a red two-pair face on i,k then forces f_i to be independent of pair k for every fixed assignment of pair j. It already ignores pair i, so f_i depends only on pair j, and antipodal oddness makes it a signed unary reader of one of the two bits of j. Repeat for all i. Conversely a signed three-cycle has an omitted reader pair in every proper two-pair face, so no such face succeeds.

Swapping labels within direction pairs and translating vertices converts every signed reader three-cycle to f_i=x_(a_(i-1)). From the root with x_(a0)=1 and other bits zero, direction order (b1,a0,a2,a1,b0,b2) is a full all-red antipodal geodesic. This proves the classification and witness statement without solver assumptions.

**All-dimensional active-cycle dichotomy.** For every legal paired-flat Q_(2m), m>=2, and every vector p of pair parities, the induced Boolean network h^p(q)=f_i(q,q+p) is antipodally self-dual and ignores its own component. By the Shih-Dong local-Jacobian fixed-point theorem, some state q has a directed cycle in the local derivative graph: otherwise h^p would have a unique fixed point, impossible because self-duality pairs fixed points antipodally. If no two-pair face succeeds, the local derivative graph has no two-cycle (each such cycle would give mutually nonconstant gates on a common four-face); it has no loops since gates ignore their own pair. Thus every parity fiber contains an active directed cycle of length at least 3. As the derivative graph at q equals that at bar q, there are at least 2^(m+1) distinct (p,q) states with such a cycle. This is an all-dimensional necessary structure for avoiding local two-pair witnesses, not a full geodesic theorem.

**Validation.** A standalone Z3 Boolean encoding of the 24 independent legal pair-gate bits, constrained by failure of every two-pair face, returns UNSAT when any gate is required to be non-unary. A separate independent enumeration validates all 128 three-cycle reader systems, the face obstruction, and existence of a full red geodesic in each. Full detailed proof: /mnt/data/nori_three_pair_global_compatibility.md; verifier: /mnt/data/nori_three_pair_compatibility_verifier.py.

**Scope.** This converts a family of simultaneously failed local forcing conditions into an explicit *globally successful* cycle structure in dimension six. It is an analytic closure proof for the paired-flat Q6 case, independent of earlier exhaustive profile SAT. In higher dimensions, the induced self-dual gates have more inputs and can be nonlinear; local cycles of length at least three do not yet provide a dimension-simple antipodal geodesic. Unrestricted NORI1 remains open.

###### Four-pair pointwise Jacobian cycle rigidity

Let h:F2^4->F2^4 satisfy h_i(q+e_i)=h_i(q) and h_i(q+1111)=1+h_i(q). Suppose for all i!=j and q that D_jh_i(q)D_ih_j(q)=0, where D_jh_i(q)=h_i(q)+h_i(q+e_j).

**THEOREM.** At EVERY q the local digraph j->i iff D_jh_i(q)=1 contains a directed three- or four-cycle. The only possibilities are (a) four signed unary readers, containing a permanent directed 3- or 4-cycle; (b) three unary readers forming a permanent directed 3-cycle and one gate depending on all three other inputs; or (c) four three-input signed-majority gates, in which case the local digraph at every q is a tournament with indegrees (0,2,2,2), and the three nonsource vertices form a directed 3-cycle.

**PROOF.** An antipodally odd Boolean function of three inputs is one of six signed unary projections, two signed parities of three bits, or eight signed-input majority functions. Its essential input count is one or three. If a unary h_j reads i, then D_ih_j is identically one, so h_i cannot depend on q_j under the no-reciprocal hypothesis. Hence unary gates must read other unary gates. A nonempty closed functional reader network without loops or two-cycles on four labels has at least three unary vertices and a 3- or 4-cycle. In the remaining case, all gates use all three inputs. A full parity gate is impossible because all its derivatives are one while every other gate depends on its bit, creating a reciprocal pair. Hence all gates are signed majority functions. For each pair {i,j}, the two reciprocal sensitivities are balanced affine parity functions of the same remaining two bits, and disjoint activation requires them to be complementary. Thus precisely one direction per pair is active at every q. Each majority gate has local indegree zero or two. Since a tournament on four nodes has six arcs, its indegree multiset is (0,2,2,2). The unique source points to the other three; within their induced tournament each has indegree one, so they form a directed triangle. QED.

**PAIRED-FLAT APPLICATION IN DIMENSION EIGHT.** For any legal antipodally odd paired-flat Q8 coloring, let p_i=x_(a_i)+x_(b_i) and q_i=x_(a_i). The induced h_i^p(q)=f_i(x(q,p)) is self-dual and ignores q_i. If every four-face retaining two entire paired direction groups lacks monochromatic full geodesics, no local reciprocal derivative pair can appear: such a pair would make both gates nonconstant on the same four-face, so the established two-pair identity R=2E(a)E(b)>0 would give a red full geodesic there. Therefore all 16 q-states in each of the 16 parity fibers have an active directed cycle of length at least three.

**UNCONDITIONAL DICHOTOMY.** Every legal paired-flat Q8 coloring either has a monochromatic full geodesic in some two-pair four-face, or has an active local directed three- or four-cycle at all 256 vertices. In any four-majority parity fiber the local Jacobian is a tournament with one source and a directed triangle at every q.

**VERIFICATION.** A standalone exhaustive script nori_rank_four_local_cycles.py checks all 65536 self-dual four-gate networks. Of them 1248 avoid reciprocal derivatives at all 16 states: 480 all-unary, 640 with one three-input gate, and 128 with four three-input gates. Every one has the stated pointwise cycle property. Complete proof: nori_rank_four_pointwise_cycle.md.

**SCOPE.** This theorem improves the prior at-least-two-cycle-states-per-parity-fiber bound in the face-free four-pair branch. It does not itself construct a full red geodesic: activation can change when a red step changes the pair-parity fiber. The rank-four Boolean classification does not extend automatically to arbitrarily many paired directions, and unrestricted NORI1 remains open.

###### Four-cycle parity synchronization and mixed-reader forcing

**Theorem.** Let c be any legal antipodally odd paired-flat coloring of Q8. Suppose (i) no four-face retaining two entire direction pairs has a monochromatic full geodesic, and (ii) in every pair-parity fiber, the induced four self-dual Boolean gates are signed unary readers whose reader graph is one directed four-cycle. Then c has an all-red full antipodal geodesic. Indeed, either a full red three-pair face exists, or c is equivalent by cube automorphisms to a signed four-cycle reader.

**Synchronization proof.** Write p_i=x_(a_i)+x_(b_i), q_i=x_(a_i). For each p write h_i^p(q)=q_(sigma_p(i))+alpha_i(p). Gate f_i ignores its own direction pair, so sigma_(p+e_i)(i)=sigma_p(i)=j. Gate i is sensitive to pair j on every face with the other two pair values prescribed at parity p. By (i) and the rank-two identity R=2E(a)E(b), gate j must be constant on pair i throughout those faces. Hence h_j^(p+e_i)=h_j^p, and sigma_(p+e_i)(j)=sigma_p(j). The two four-cycles sigma_p and sigma_(p+e_i) have the same consecutive arrows i->j->sigma_p(j), which determine the entire cycle on four vertices. Thus sigma_p is constant over p. Relabel to sigma(i)=i+1 mod4. Since gate i ignores pair i, and gate i-1 reads pair i on every face, the four-face failure also forces gate i to ignore pair i-1. Hence there exist arbitrary Boolean two-bit functions phi_i such that
 f_i(q,p)=q_(i+1)+phi_i(p_(i+1),p_(i+2)).                  (FC1)

**Parity guard gives a red three-pair path.** If phi_i varies with p_(i+2) for some fixed p_(i+1)=t, freeze pair i+1 at parity t and retain A=i,B=i+2,C=i+3. On this ordinary six-face f_A=epsilon+p_B, while f_B=q_C+phi_B(p_C,p_A), f_C=q_A+phi_C(p_A,p_B). Since f_A is nonconstant in B, failure of the two-pair A,B face forces f_B independent of A. Thus f_B is a signed reader of one bit in pair C. Since f_B is nonconstant in C, failure of the B,C face forces f_C independent of B, making it a signed reader of one bit in A. Swap labels inside A,C as needed and absorb phases, obtaining
 f_A=epsilon+p_B, f_B=x_(a_C)+eta, f_C=x_(a_A)+theta.
Choose the starting root so f_A=1 and f_C=0. The pair-word (A,B,C,A,B,C) then traverses all six directions once, all red. Indeed first A takes b_A, first B toggles parity p_B enabling the complementary A direction; first C takes a_C and changes the reader input of B; second A takes a_A and changes the reader input of C; the subsequent B,C visits take their other directions. The existing paired-endpoint insertion lemma places both members of omitted pair i+1 around the red six-step geodesic, yielding a full red Q8 geodesic.

**No guards gives a signed cyclic reader.** If each phi_i ignores its second argument, phi_i=beta_i+lambda_i p_(i+1). Therefore f_i=q_(i+1)+lambda_i p_(i+1)+beta_i is a signed reader of one bit of pair i+1. Pair-member swaps and vertex translations normalize to f_i=q_(i+1). From the root q_0=1 with every other bit zero, the direction order (b_3,a_0,a_1,a_2,a_3,b_0,b_2,b_1) is red and visits every direction once. Undoing the automorphisms supplies a full red geodesic in c. QED.

**Audit.** In normal form (FC1), each phi_i has sixteen truth tables. Absence of successful two-pair faces forbids dependence on opposite pair parity in both directions of either opposite gate pair (0,2) and (1,3). Each opposite gate pair allows 4*16+16*4-4*4=112 table combinations. Thus 112^2=12544 systems meet (i) in this normal form. Of them 256 have no opposite-parity dependency; the other 12288 have the constructed six-step red face. The separate verifier nori_fourcycle_sync_verifier.py checked all 12544 and explicitly reconstructed the required red routes. Detailed written proof: nori_fourcycle_sync.md.

**Scope.** This positive forcing theorem concerns all legal paired-flat Q8 colorings with the indicated unary four-cycle fiber structure. It leaves majority-type and three-reader-plus-one-extra-gate fiber types unresolved, and does not establish unrestricted NORI1.

###### Dimension-uniform cyclic sensitivity-product forcing and the three-pair closure lemma

**THEOREM.** For any m>=2 let an ordinary edge coloring of Q_(2m) have paired directions P_i={a_i,b_i}, with color rules g_i(x|P_(i-1)) and 1+g_i(x|P_(i-1)). The gates g_i:F2^2->F2 are arbitrary. For the fixed pair-label order W=(0,1,...,m-1,0,1,...,m-1), the number of starting roots giving a red full antipodal geodesic is
 R_W=product_i E(g_i),
where E(g_i) counts sensitive undirected edges of its four-vertex input square. If every gate is nonconstant, at least 2^m roots work for W. No legal oddness is required for this ordinary coloring.

**PROOF.** Choose independently one sensitive input edge e_i of each g_i, of direction d_i in predecessor pair P_(i-1). Prescribe the member used at the first visit to each pair as ell_(i-1)=1+d_i for i>=1 and ell_(m-1)=d_0. For i>=1 let t_i be the endpoint of e_i where g_i(t_i)=ell_i; start predecessor pair i-1 at v_(i-1)=t_i+e_(ell_(i-1)). Thus the first visit to gate i sees t_i, while its second visit sees t_i+e_(d_i) because the predecessor's second step occurs between those visits. Its output flips, so both members of pair i are used. For i=0 choose endpoint t_0 of e_0 with g_0(t_0)=ell_0 and initialize the last pair to t_0. Its first traversal, between the two visits of gate zero, flips direction d_0 and changes gate zero's value. This defines a red full path and uniquely determines all initial pair states. Conversely the sensitive edge crossed by each predecessor between the visits of gate i is recoverable from every successful W-path. These constructions are inverse, proving the formula. QED.

**ORDINARY THREE-PAIR COMPATIBILITY LEMMA.** In an ordinary paired-flat Q6 coloring suppose one parity fiber has three signed unary reader gates in a directed 3-cycle, and every two-pair four-face lacks a monochromatic spanning geodesic. Normalize the parity to zero and the gates to h_i^0(q)=q_(i+1) modulo three. On two P0,P1 faces with P2 equal 00 or11, gate f0 varies in P1, forcing f1 independent of P0 there. Its corresponding values are 0 and1. Hence f1 varies in P2 for every P0 assignment, forcing f2 independent of P1 everywhere. By the initial reader-cycle values, f2 then varies between P0=00 and11 for every P1 setting, forcing f0 independent of P2 globally. Cyclic repetition forces f1 independent of P0 globally. Each gate now reads only the preceding pair, and is nonconstant. The product theorem gives a red full Q6 geodesic.

**NORI1 Q8 APPLICATION.** In any legal paired-flat Q8 coloring without successful two-pair faces, a parity fiber having three unary-reader gates and one three-input gate has a reader 3-cycle among its unary gates, by the previously proved pointwise rank-four rigidity. Freeze the fourth pair. The ordinary three-pair lemma supplies a full red geodesic in the remaining six-dimensional face, and paired-endpoint insertion produces a red full Q8 antipodal geodesic. Thus the three-reader-plus-one-extra-gate type is excluded by mathematical forcing. The four-majority type remains an open branch.

**VERIFICATION.** The script paired_cycle_product_verifier.py exhaustively checks 256 two-gate and 4096 three-gate systems and tests additional four- and five-gate systems. Detailed complete manuscript nori_cyclic_pair_sensitivity_product.md. The formula holds in every dimension; it is an unrestricted-dimensional forcing tool for the specified pair-reader structure, and the general NORI1 conjecture remains open.

###### Majority-fiber transport: a static fixed word and a seven-word common-coloring portfolio

**SCOPE.** Work continuing Article XVI's unrestricted compatibility programme. One proved constructive theorem concerns static four-majority gates, while the general parity-dependent seven-word forcing assertion is a finite UNSAT finding awaiting a hand derivation or independently checked UNSAT proof log. NORI1 remains open.

**THEOREM A: a common static majority word.** Let h_i:F2^4->F2 ignore q_i and obey h_i(q+1111)=1+h_i(q). Suppose all h_i have three essential inputs, and no state has reciprocal nonzero derivatives D_jh_i D_ih_j. For the red paired-matching system with gates h_i independent of paired parity bits, the fixed pair-label word W=(3,2,1,2,0,3,0,1) is a red full antipodal geodesic from ONE and only one starting q in F2^4. Consequently it succeeds from sixteen full Q8 roots, one per initial pair-parity vector.

**Proof.** Each h_i is a signed majority, h_i(q)=Maj(q_j+a_ij:j!=i). For unordered i,j and complementary k,l the absence of reciprocal derivatives is equivalent to a_ik+a_il+a_jk+a_jl=1. These six F2-linear equations on twelve signs have rank five. Fix a reference solution h*_0=Maj(q1,q2,q3), h*_1=Maj(q0,1+q2,q3), h*_2=Maj(1+q0,1+q1,q3), h*_3=Maj(q0,1+q1,q2). All solutions are h_i(q)=h*_i(q+t)+s_i for some t,s in F2^4, with only the common global redundancy (t,s)~(t+1111,s+1111). For each of sixteen s, direct substitution in W gives the sole successful q=(s1,s3,1+s3,s1)+t. An independent 128-network by 16-root exhaustive checker verifies this short substitution and uniqueness. QED. A general paired-flat coloring depends on pair parity, so the static theorem does not apply without a transport argument.

**GENERAL Q8 SAT PORTFOLIO.** Let c be an arbitrary legal paired-flat Q8 coloring. Suppose that at one parity fiber, after translation and pair-member relabeling, f_0 restricted to diagonal pair inputs is Maj(q1,q2,q3), and that no four-face retaining P0 and one other complete pair contains a red full geodesic. Then at least one of the opposite six-faces P0=00 and P0=11 contains a red full three-pair geodesic with pair-label word among
  121323, 213123, 213132, 213231, 231231, 312123, 312321.
Such a red face geodesic extends to a red full Q8 antipodal geodesic by the established paired-endpoint insertion theorem.

**Computational verification of portfolio.** Use 256 Boolean gate variables v_(i,s) (64 per pair), 128 antipodal-oddness equations, and eight fixed f0 majority values. For every P0,Pj four-face, forbid a red full face geodesic by demanding that at least one of its two gates is constant on that face (rank-two identity R=2E(a)E(b)). For each chosen pair word, each rooted geodesic on faces P0=00 and11 and each first-member choice in the three retained pairs, forbid the all-red path by a six-edge Boolean blocking clause. After removing repeated clauses there are 7168 path constraints. Z3 returns UNSAT. Removing any one of the seven entire pair-word families yields SAT; this was separately checked seven times. This is a finite reproducible SAT implication, with a much smaller order family than all possible three-pair words. No proof-log checker or short paper proof has yet been obtained, and minimality among all possible portfolios is not claimed.

**LESSON FOR UNRESTRICTED NORI1.** The static majority theorem has a one-word constructive witness. Pair-parity dependence invalidates the single-word guarantee; a direct SAT attempt with the one static word is satisfiable. Restoring the simultaneous no-two-pair-face compatibility restrictions makes seven words sufficient in the full parity-dependent system. Pairwise cross-face equalities alone, even combined with oddness, are insufficient; a separate SAT model satisfies those weaker constraints while avoiding red full paths on both candidate six-faces. These results localize the required transport to specific joint cross-parity constraints rather than separate scalar influence counts.

**FILES.** Full mathematical and computational audit: /mnt/data/nori_majority_joint_transport.md. Reproducer: /mnt/data/nori_majority_transport_certificate.py. Generated standalone SMT-LIB2 instance: /mnt/data/nori_majority_seven_word.smt2. The checker verifies the 128-network theorem without external packages and obtains the seven-word UNSAT result with installed libz3.so.4.

###### Fiberwise parity-root forcing in Q6 and the full paired-flat Q8 computational audit

**Theorem (finite exhaustive, Q6).** Let c be any legal antipodally odd paired-flat coloring of Q6 with paired directions P_i={2i,2i+1}, i=0,1,2. For EVERY prescribed pair-parity vector p_i=x_(2i)+x_(2i+1), some vertex of that parity fiber starts an all-zero full antipodal geodesic. This assertion is stronger than mere existence somewhere in Q6.

**Finite proof and independent checker.** Translating roots reduces to parity p=000. Reverse any red full geodesic to halve the root search, leaving representatives r=0,12,48,60 for its four antipodal root pairs. The three pair gates each have eight independent odd truth bits, total 24 independent coloring bits and 2^24 legal assignments. Admissible red pair-label words have length six, each of labels 0,1,2 appearing twice, with no equal consecutive labels. A twelve-word portfolio suffices:
 201012, 210102, 021201, 012120,
 210210, 010212, 021021, 202101,
 120201, 120120, 102102, 102021.
For every word enumerate its eight pair-member assignments and four representative roots: 12*8*4=384 red path patterns. Each pattern prescribes up to six of the 24 Boolean gate values. The standalone standard-C++ verifier q6_fiber_portfolio_independent.cpp generates those prescriptions independently of the preceding Z3 reachability solver and represents the union of their satisfaction subcubes as a bitset of size 2^24. It verifies that ZERO legal assignments are uncovered. Therefore every coloring has a red full geodesic rooted within the prescribed fiber. Translating proves all p.

**Portfolio irredundancy.** Removing the word families in the displayed order leaves, respectively, 3488,2976,384,7936,896,768,2112,1184,4128,1248,1248,3776 uncovered legal colorings. Irredundancy is relative to this twelve-word portfolio, not a claim of global minimum portfolio size.

**Sharpness of root-pair coverage.** The four antipodal root pairs in fiber p=000 are {0,63},{12,51},{48,15},{60,3}. For each pair a legal coloring exists having a red full path from that pair and none of the other three pairs. Truth-table masks (f0,f1,f2) indexed by outside-bit assignments 0..15 are:
 {0,63}: (0x5555,0xb2b2,0xff00);
 {12,51}: (0xeaa8,0xbf02,0xff00);
 {48,15}: (0xdf04,0xbf02,0xff00);
 {60,3}: (0xaaaa,0xb2b2,0xff00).
The independent subset-reachability verifier q6_fiber_witness_check.py checks all four certificates. A second complete bitset enumeration q6_fiber_root_sharpness.cpp finds 3584 legal coloring assignments with no red full path from any prescribed THREE of the four root pairs, and none excluding all four. The theorem is sharp with respect to universal selection of antipodal root pairs.

**Prior unpersisted finite Q8 result.** Every legal paired-flat antipodally odd Q8 coloring admits a red full antipodal geodesic, by two independently generated Boolean reachability encodings that return UNSAT. There are 128 independent coloring bits, 32768 root/subset states, and 131072 red transition implications in the first encoding. A nonodd constant-gate negative control returns SAT. Full mathematical audit nori_q8_pairedflat_global_closure.md and reproducible sources nori_q8_all_global_sat.py and nori_q8_global_alternate_sat.py. This Q8 statement is still solver-assisted, with no independently checked UNSAT log; it does NOT imply NORI1 for arbitrary Q8 colorings because arbitrary Q8 lift to paired-flat Q16.

**Scope and next mathematical challenge.** A prescribed-parity-fiber version of the paired-flat Q8 theorem was not determined; a specialized SAT attempt timed out and must not be read as evidence either way. The known Q8 nonlinear face-irreducible example has six successful starting roots in each parity fiber; a legal antipodal square-pair mutation changes some fiber counts to eight while others remain six, refuting uniformity of the counts. The Q6 argument shows how all four root-pair failures can be jointly inconsistent despite each three-root failure being realizable. A dimension-uniform version of this shared-assignment incompatibility is needed. Neither finite theorem settles unrestricted NORI1.

**Reproduction files.** /mnt/data/nori_q6_fiberwise_global_compatibility.md; /mnt/data/q6_fiber_portfolio_independent.cpp; /mnt/data/q6_fiber_root_sharpness.cpp; /mnt/data/q6_fiber_witness_check.py; /mnt/data/nori_q8_pairedflat_global_closure.md; /mnt/data/nori_q8_all_global_sat.py; /mnt/data/nori_q8_global_alternate_sat.py.

**Complete finite Q6 parity-fiber root-support enumeration.** The full 2^24-coloring exhaustive computation now determines the number of successful antipodal root pairs in one prescribed Q6 pair-parity fiber: among all 16,777,216 legal paired-flat Q6 colorings, there are 0 with no successful pairs, 14,336 with one, 610,944 with two, 2,295,552 with three, and 13,856,384 with all four. Each named pair is uniquely successful in 3,584 colorings. A standalone standard-C++ bitset verifier, \`q6_fiber_root_distribution.cpp\`, recomputes these counts independently of the earlier SMT search and the twelve-word forcing-portfolio verifier. This establishes both unconditional fiberwise nonemptiness and sharp root-pair non-prescribability in dimension six. The open extension to arbitrary numbers of pairs is untouched. Provenance: research note \`note_nori_q6_parity_fiber_sharp_q8_global_sat_r11510\`, version 2.


###### Affine red-return holonomy and joint phase forcing (18 October 2026)

**Dimension-uniform theorem.** Write the pair directions of an antipodally odd paired-flat Q_(2m) as P_i={a_i,b_i}, with q_i=x_(a_i) and pair parity p_i=x_(a_i)+x_(b_i) over F2. Assume each pair gate has an affine restriction to every parity fiber:
 f_i(p,q)=a_i(p) dot q + theta_i(p),
 where (a_i(p))_i=0, a_i(p) dot 1=1, and both a_i,theta_i ignore p_i. The phase functions may be nonlinear in the other p-bits. A red step with pair label i changes p_i to p_i+1 and q_i to q_i+1+f_i(p,q). Therefore for any pair-label word w with two appearances of each i, its red return map on a fixed starting parity fiber is affine:
 q_final=A_w(p) q + b_w(p,theta),
 where A_w is a product of elementary shears and b_w is affine in all phase truth values. A red full antipodal geodesic exists with that word precisely when
 (A_w(p)+I)q=1+b_w(p,theta).                    (AH1)
If r=rank(A_w+I), the word has either zero or 2^(m-r) successful starting q-states. If r=m it always has a unique witness independent of the phase values. If r=m-1, its success condition is one affine equation lambda_w(theta)=0, obtained by pairing 1+b_w with the unique nonzero left-null vector. A finite family of such words forces success for every phase assignment whenever the complementary failure equations lambda_w(theta)=1 are linearly inconsistent. This gives a root-and-order compatible parity certificate from the same coloring. Proof: compose the red shears and apply linear algebra over F2.

**The Q6 adaptive six-word theorem.** For m=3, antipodal oddness forces each fixed-p gate to be a signed unary reader of one of the other two q-bits. Each pair gate has four independently chosen reader selections and four independently chosen phase values, giving 12 selector bits and 12 phase bits in all. Translate the prescribed starting pair parity to zero. Any red geodesic must have a pair-label word using 0,1,2 twice without adjacent equal labels; there are 30 such words. A complete 4096-pattern selector audit using (AH1) gives:
 - In 3826 reader systems, some word has invertible A_w+I and succeeds for all phase values.
 - In the remaining 270 systems, a portfolio of at most SIX corank-one words has linearly inconsistent failure equations lambda_w=1. The deterministic certificate lengths are 1:126, 2:30, 3:46, 4:38, 5:18, 6:12.
Therefore every starting pair-parity fiber of EVERY legal paired-flat Q6 coloring contains a red full antipodal geodesic. This is a sharper algebraic proof of the prior complete 2^24-coloring enumeration, with an adaptive word portfolio independent of phase values. For one six-word pattern (selector mask 1370), the simultaneous failure equations on phase bits theta_0,...,theta_11 are:
 theta0+theta1+theta6+theta10=1;
 theta0+theta3+theta5+theta6+theta8+theta11=1;
 theta0+theta3+theta4+theta10=1;
 theta0+theta2=0;
 theta9+theta11=0;
 theta1+theta2+theta4+theta5+theta8+theta9=0.
Adding all equations gives 0=1. The corresponding word family is (010212,012012,012021,020121,021201,101202).
The standalone Python matrix/phase checker verifies all 4096 selector systems and runs 8000 independent red-step samples. A second C++ checker directly simulates EVERY phase assignment for the 270 exceptional systems: 270*4096=1,105,920 colorings, all successful. The Python checker additionally compared 64000 affine predictions against direct path simulation.

**Q8 parity-static odd-slope forcing theorem.** Let m=4 and strengthen the affine-fiber hypothesis by requiring a_i(p)=a_i independent of p, while allowing each phase gate theta_i(p_except_i) to be an arbitrary Boolean function of three other pair-parity bits. Each a_i is an odd three-input linear form, giving FOUR alternatives per i and 4^4=256 coefficient matrices. Every prescribed pair-parity fiber contains a red full antipodal geodesic for all 256 matrices and ALL 2^32 phase assignments. The proof uses a fixed portfolio of 17 pair-label words:
 01230123 01231230 10230231 20130132 30120123 01232310 23010132 02131320 03121230 12030321 13020231 10232301 20131302 21030312 30121203 31020213 32010123.
For every one of the 256 coefficient matrices, one of these words satisfies z dot (1+b_w(theta))=0 AS AN AFFINE POLYNOMIAL IN ALL 32 PHASE VARIABLES for every left-null vector z of A_w+I. Hence its return equation (AH1) is solvable for all phases. The first certified word for each matrix has corank 0 in 88 cases, corank 1 in 92 cases, and corank 2 in 76 cases, guaranteeing respectively 1,2,4 successful q-roots for that word in every fixed pair-parity fiber. A self-contained Python symbolic checker verifies the 256-by-17 cover. Independently developed C++ code computes all 33-bit affine polynomials and their left kernels and independently constructs red full paths in 32768 seeded phase assignments. This is a positive fiberwise result for nonlinear legal Q8 colorings: the phase gates may be completely unrestricted Boolean functions, but their q-slope matrices must remain unchanged across parity fibers.

**Research significance and limit.** The mechanism exploits simultaneous incompatibility of Boolean path failures, not a histogram, fixed root, prescribed near-full face, or a restricted influence graph. It supplies a dimension-uniform linear-algebraic toolkit and stronger finite Q6/Q8 forcing results. For arbitrary paired-flat Q_(2m) with m>=4, parity-fiber gates may be nonlinear in q and their derivative coefficients may change with p; the affine return-map theorem does not cover those colorings. The all-dimensional assertion that parity-static odd slopes always admit some phase-immune double-occurrence word remains unproved. NORI1 is still open.

**Complete files.** nori_affine_holonomy_forcing.md; nori_affine_holonomy_certificate.py; nori_affine_holonomy_independent.cpp; nori_affine_m4_static_transport.md; nori_affine_m4_static_cover.py; nori_affine_m4_static_independent.cpp; archive nori_affine_holonomy_research_bundle.zip.

###### Five-pair phase-immune forcing and transported-incidence cancellation

Let N=2m and let a legal paired-flat coloring have pair-parity bits p_i=x_(a_i)+x_(b_i) and first-member bits q_i=x_(a_i). Suppose its gate has form f_i(p,q)=a_i dot q + theta_i(p_except_i), with odd off-diagonal slope row a_i fixed independently of p, and arbitrary Boolean phase function theta_i. This permits nonlinear dependence on pair-parity bits.

**DIMENSION-UNIFORM TRANSPORTED-INCIDENCE LEMMA.** Let S_i=I+e_i a_i^T. For any double-occurrence pair-label word w=(i_1,...,i_(2m)) and starting parity p, set p_t=p+sum_(s<t)e_(i_s), L=S_(i_(2m))...S_(i_1), and v_t=S_(i_(2m))...S_(i_(t+1)) e_(i_t). The red return equation is
  (L+I)q=1+sum_t v_t+sum_t theta_(i_t)((p_t)_except_i_t) v_t.
The word admits a full red antipodal path from some q for EVERY assignment of the independent phase truth values iff, for all z in ker((L+I)^T), (1) z dot (1+sum_t v_t)=0 and (2) for each phase key (i,u), sum_(t: i_t=i and (p_t)_except_i=u) z dot v_t=0. Proof: the right side must be orthogonal to every left-null vector for all independent phase variables, forcing each affine coefficient to vanish. When these conditions hold and k=corank(L+I), every phase assignment has 2^k red starting q-roots in the prescribed parity fiber. This is a shared-coloring compatibility condition expressed through transported occurrence vectors.

**COMPUTER-ASSISTED FINITE THEOREM IN Q10.** For m=5, every one of the 32768=8^5 odd off-diagonal slope matrices admits a double-occurrence word whose transported-incidence conditions hold; hence EVERY one of the 2^95 corresponding legal paired-flat Q10 colorings has a red full antipodal geodesic starting in EVERY prescribed pair-parity fiber. The witness word depends only on the slope matrix, not on the 80 arbitrary nonlinear phase bits. The 32768 matrices form 324 relabeling classes under S5. Independent Python and C++ implementations test all 39480 admissible double-occurrence pair words, checking all 324 class representatives. Every class succeeds. With the first word chosen by the deterministic search, the corank distributions are: k=0: 83 classes/8848 labeled matrices; k=1:129/12800; k=2:43/4760; k=3:69/6360. Thus the selected order guarantees respectively 1,2,4,8 red starting roots q for every phase assignment. Direct red-step trajectory checks in 1296 independently sampled class/phase instances reproduced those root counts.

**FILES.** Full proof nori_affine_m5_static_transport.md; standard-library independent verifier nori_affine_m5_static_cover.py; C++ verifier nori_m5_phase_exhaust.cpp. The parent prior note note_nori_affine_holonomy_joint_phase_forcing_r11510 already proves the general affine return mechanism and the m=3,4 cases. This is a dimension-ten extension and a more geometric phase-cancellation criterion, not a complete proof of NORI1.

**RESEARCH BOUNDARY.** The existence of such a phase-immune word for every static odd slope matrix in arbitrary dimension remains unproved. For general legal colorings the slope rows may themselves depend on p and may be nonlinear in q, so the present sufficient criterion does not apply.

**Extended transported-incidence scope.** For any fiberwise-affine paired-flat gate f_i(p,q)=a_i(p) dot q+theta_i(p_except_i), the transported-occurrence proof remains valid with step-dependent shears S_t=I+e_(i_t) a_(i_t)(p_t)^T along the fixed pair-parity trajectory of the selected word. The same left-null constant and phase-key coefficient cancellation conditions are necessary and sufficient for that word to succeed from some q for every phase assignment. Only the positive Q10 classification assumes a_i is independent of p; the algebraic cancellation criterion applies to arbitrary parity-varying affine slope rows.

###### Isolated-chord corank rigidity for phase-immune geodesic returns

Let m>=2. In a legal paired-flat Q_(2m) coloring write pair-parity p_i=x_(a_i)+x_(b_i) and first-member q_i=x_(a_i). Suppose the pair gates are affine in q, with possibly parity-dependent slopes:
 f_i(p,q)=a_i(p) dot q + theta_i(p_except_i),
where a_i(p)_i=0 and all phase truth-table entries theta_i(u) can be prescribed independently. Along a fixed pair-label word w=(i_1,...,i_(2m)) containing each label twice, put S_t=I+e_(i_t) a_(i_t)(p_t)^T, L=S_(2m)...S_1, M=L+I, and transported step vectors v_t=S_(2m)...S_(t+1)e_(i_t). The red antipodal return equation is
 Mq=1+sum_t v_t + sum_t v_t theta_(i_t)((p_t)_except_i_t).
Call w phase-immune if this equation is solvable for every phase assignment, allowing starting q to depend on the assignment.

Let H(w) be the chord-interlacement graph: two labels are adjacent if their occurrences alternate. Let I(w) be its isolated-label set.

**THEOREM (dimension-uniform isolated-chord corank bound).** Every phase-immune word obeys
 corank(L+I) <= |I(w)|.
In particular, if H(w) has no isolated labels, then phase immunity is equivalent to invertibility of L+I and the red antipodal starting root q is unique in the prescribed parity fiber for every phase assignment. Generally a phase-immune word gives no more than 2^|I(w)| red starting roots q for each phase assignment.

**PROOF.** First the vectors v_t span F2^m. If z annihilates all v_t, propagate the final covector backwards by z_(2m+1)=z, z_t=S_t^T z_(t+1). Since z dot v_t=(z_(t+1))_(i_t)=0, the transvection S_t^T leaves z_(t+1) unchanged; thus z_t=z at all steps and z_(i_t)=0 for every label. Hence z=0.

For label i with occurrences r<s, the two phase keys agree iff for each j !=i the number of occurrences of j strictly between r,s is even, i.e. iff no label interlaces i. For any z in ker(M^T), phase immunity implies z dot v_r=z dot v_s=0 for each nonisolated label, because those two occurrences read independent phase entries. For isolated i it implies z dot (v_r+v_s)=0, because both occurrences read the same phase entry. Consequently the linear map
 ker(M^T) -> F2^(I(w)), z |-> (z dot v_(first_i))_(i in I(w))
is injective: a vector in its kernel annihilates every v_t, hence vanishes. Thus the left nullity, namely corank M, is at most |I(w)|. If |I(w)|=0, M is invertible, which conversely makes the return equation solvable for every phase assignment. The root count is 2^corank M. QED.

**COROLLARY (single-phase fragility).** If H(w) has no isolated labels and M is singular, then from any phase assignment admitting a red w-geodesic, changing one independent phase truth-table entry destroys ALL red w-geodesics rooted in that parity fiber. For a nonzero z in ker M^T, the full span ensures some z dot v_t=1; that occurrence has a unique phase key, so toggling it violates z-orthogonality of the return right-hand side.

**SHARPNESS.** For m=5 take static odd slope masks (2,1,1,1,1), and word 2340101432. Its isolated labels are {2,3,4}. The symbolic transported return is phase-immune with corank(L+I)=3; the upper bound is attained and it gives eight red q-roots for every phase assignment.

**FINITE AUXILIARY CERTIFICATE.** A standard-library checker tested all 4096 parity-varying odd-slope systems for m=3 and all 30 admissible pair words, verifying the theorem in each of 122880 systems/words. There are 39936 phase-immune pairs: 26112 with corank zero and 13824 with corank one. A fixed ten-word portfolio, namely (021210,102120,120120,120201,120210,201201,201210,210102,210120,210210), has some phase-immune word for every slope system, thus strengthens the prior Q6 twelve-word fixed portfolio. It also verifies the m=5 sharpness example. Full self-contained proof nori_phase_interlacement_corank.md and independent checker nori_phase_interlacement_verifier.py.

**SCOPE.** The corank theorem works with parity-varying affine slopes, and its proof uses neither oddness nor a prescribed Boolean degree beyond affine q-dependence. It is an unconditional structural restriction on any candidate phase-immune word, but does not guarantee a phase-immune word in general dimensions or apply directly to gates nonlinear in q. NORI1 is unresolved.

###### All-dimensional double-sweep determinant forcing



Let A be a zero-diagonal odd-row slope matrix independent of pair parity, while phase functions theta_i(p_except_i) are arbitrary Boolean functions. For any permutation pi of the pair labels let T_pi=S_(pi_m)...S_(pi_1), with S_i=I+e_i a_i^T; the double sweep w=pi pi has linear return matrix L_w=T_pi^2.

**THEOREM.** det(L_w+I)=det A over F2, and the word pi pi is phase-immune if and only if A is nonsingular. If A is nonsingular, that SAME prescribed word yields a red full antipodal geodesic from a unique starting q in EVERY prescribed parity fiber, for EVERY choice of nonlinear phase functions.

**PROOF.** Relabel so pi=(1,...,m), write A=B+C with B strictly lower triangular, and let delta=T_pi q+q. During one sweep each bit changes once; at step i,
 delta_i=(Aq)_i+sum_(j<i) a_ij delta_j.
Hence (I+B)delta=Aq and T_pi+I=(I+B)^(-1)A. As I+B has determinant one, det(T_pi+I)=det A. In characteristic two T_pi^2+I=(T_pi+I)^2, proving det(L_w+I)=det A. If A is nonsingular, every affine return equation has one q solution. If A is singular, the chord diagram of pi pi is fully interlaced (with no isolated chords). The isolated-chord theorem already proved in this note then precludes phase immunity. QED.

**GRAPH COROLLARY.** Interpret a_ij=1 as an arc j->i. Since det A counts directed spanning cycle covers modulo two, an odd number of cycle covers (including a unique cycle cover) guarantees a red full antipodal geodesic in every parity fiber for every phase assignment, using any double sweep. This is a graph-theoretic, unbounded-dimensional positive forcing condition, not a necessary condition.

**INDEPENDENT AUDIT.** The checker nori_double_sweep_gauss_seidel_check.py tested all 256 odd slope matrices at m=4 (88 nonsingular) and all 32768 at m=5 (10048 nonsingular), comparing the sweep rank and the phase-immune return condition against det A. All passed. Complete proof nori_double_sweep_gauss_seidel.md. For singular A other, partially noninterlaced words may still be phase-immune.


###### Nested principal-core double sweeps and odd-indegree parity peeling

Let a legal paired-flat Q_(2m) coloring have gate rules f_i(p,q)=sum_(j!=i) a_ij q_j + theta_i(p_except_i) over F2. The arbitrary Boolean phase functions may be nonlinear. The parity-independent slope matrix A has zero diagonal and A1=1.

**ALL-DIMENSIONAL THEOREM.** Select an ordered sequence of outer pair labels i_1,...,i_k and denote by R the remaining labels (|R|>=2). Suppose det A[R,R]=1 and sum_(s<t) a_(i_t,i_s)=0 for every t. Then, for ANY permutation pi of R, the pair word
  w=i_1 ... i_k pi pi i_k ... i_1
gives precisely 2^k all-red full antipodal geodesics rooted in EVERY prescribed initial pair-parity fiber, for EVERY Boolean phase assignment. The order depends only on A, never on the phase truth tables.

**PROOF.** Each red pair step is an invertible operation. Select arbitrarily the k outer q-bits just after their first steps. During the core double sweep pi pi, these bits and their parities remain fixed. The core linear return on q_R obeys det(L_R+I)=det A[R,R]=1 by the Gauss-Seidel determinant theorem, so its red antipodal return equation has one solution for every affine phase offset. Thus all core q-bits end complemented. Reinsert outer steps in reverse. At the second visit to label i_t, all deeper pair bits have completed their antipodal changes, earlier outer bits are fixed, and every other pair parity equals its value at the first visit; theta_(i_t) ignores its own parity, so its phase is unchanged. The gate color changes by
  sum_(j in R union {i_(t+1),...,i_k}) a_(i_t,j)
  =1+sum_(s<t) a_(i_t,i_s)=1.
The second red step therefore traverses the other member of pair i_t, finishing that pair antipodally. Reverse induction closes every outer pair. The initial k-step red prefix is invertible, giving one initial root per chosen k-bit outer state, hence 2^k witnesses. QED.

**GRAPH AND CHORD INTERPRETATION.** Orient an influence arc j->i when a_ij=1. The core has odd directed cycle-cover parity. The outer vertices can be deleted so that each removed vertex receives even incoming influence from earlier deletions, equivalently odd indegree in the current remaining graph because A1=1. The resulting word has k isolated chords in its interlacement graph and return corank k; it saturates the earlier isolated-chord bound.

**FULL FINITE AUDIT.** A subset-DP peeling algorithm and an independent symbolic affine-return verifier checked ALL odd zero-diagonal matrices through m=5. Every matrix admits a valid peel, and the nested word is phase-immune with corank k. Counts by k are: m=3 (2,6); m=4 (88,76,92); m=5 (10048,8378,6035,8307). The standalone symbolic checker evaluated all 32768 m=5 matrices and confirmed the root-count statement. It also checked every eligible single-outer-label principal minor: 6, 224, and 39360 matrix/label pairs in dimensions m=3,4,5 respectively. As illustration, slope row masks (2,1,1,1,1) admit peel (2,3,4), core {0,1} and word 2340101432, producing eight phase-independent red starting roots in every parity fiber. Exploratory random tests found valid peels in 200000 six-pair systems and additional samples through nine pairs; these are not proofs in those dimensions.

**OPEN ODD-MATRIX CONJECTURE.** Every zero-diagonal binary A satisfying A1=1 admits ordered deletions with even incoming parity from previously deleted vertices, leaving a nonsingular principal submatrix. Proving this would establish fiberwise red-geodesic existence for ALL parity-static affine paired-flat legal colorings of every even dimension, despite arbitrary nonlinear parity phases. This remains UNPROVED. Fully general NORI1 (parity-varying slopes or q-nonlinear gates) also remains open.

**REPRODUCIBILITY.** Full proof nori_nested_sweep_elimination.md; standalone exhaustive certificate nori_nested_sweep_certificate.py. Session session_nori_r11510_3.

###### Nested phase forcing with parity-varying affine slopes

 The nested forcing proof does not require slopes independent of pair parity. Let f_i(p,q)=a_i(p) dot q+theta_i(p_except_i), with a_i(p) odd-weight, zero on self, and independent of p_i. Fix a prescribed starting parity, outer labels i_1,...,i_k, and an inner double-occurrence pair word v on complementary labels R. Let p^(t) be the parity state before the first outer occurrence of i_t; require sum_(s<t) a_(i_t)(p^(t))_(i_s)=0 for every t. Along the inner parity trajectory after the outer prefix, let L_(R,v) be the homogeneous affine-return matrix acting on inner q_R, using time-dependent slope shears evaluated at each visited parity. If det(L_(R,v)+I)=1, then the nested word i_1...i_k v i_k...i_1 gives precisely 2^k red full antipodal starting q-roots in the prescribed parity fiber, for ANY choices of phase truth tables. Proof: the inner return equation has a unique q_R solution for each arbitrary fixed postprefix outer q-state; during nested return, each outer gate has the same coefficients and phase at its two occurrences because all other parities are restored and it ignores its own parity. Its output changes by the odd sum of slope entries on inner labels, hence the two red steps traverse opposite directions. The first outer prefix is bijective. This is an all-dimensional positive criterion, not a universal existence theorem for parity-varying slopes. A separate simulator tested 2000 random five-pair systems with varying slope tables and nonlinear phases; for each, it directly simulated all 32 starting q-states and found precisely eight red antipodal roots for the selected nesting.



###### Nonlinear nested-pair gluing and a three-pair transfer theorem

Work over \(\mathbb F_2\). In a legal paired-flat coloring on \(Q_{2m}\), write \(p_i=x_{a_i}+x_{b_i}\), \(q_i=x_{a_i}\). Its pair gate \(f_i(p,q)\) ignores \(p_i,q_i\); the edge colors in directions \(a_i,b_i\) are \(f_i\) and \(1+f_i\). Antipodal oddness gives \(f_i(p,q+\mathbf1)=1+f_i(p,q)\). At any vertex, there is a unique red edge in pair \(i\), and traversing it defines an involution
\[
T_i:(p,q)\longmapsto(p+e_i,\ q+(1+f_i(p,q))e_i).
\tag{NG1}
\]
This operation changes the pair parity and possibly its \(q\)-bit. A word containing every pair label twice describes a red full antipodal geodesic precisely when its action complements every \(q_i\): then the two occurrences of each label traverse its two distinct directions.

Choose distinct outer labels \(i_1,\ldots,i_k\) and residual core \(R=[m]\setminus\{i_1,\ldots,i_k\}\). For \(t\le k\) put \(D_t=R\cup\{i_{t+1},\ldots,i_k\}\). Assume the nonlinear complement-derivative condition
\[
f_{i_t}(p,q+\mathbf1_{D_t})=1+f_{i_t}(p,q)\quad\text{for all }p,q,\ 1\le t\le k.
\tag{NG2}
\]
For \(t=1\), (NG2) follows directly from antipodal oddness and the gate's independence of its own bits.

**Theorem (nonlinear core-gluing).** Assume (NG2). Suppose that, for every fixed assignment to the outer \(p,q\) bits and every prescribed core parity \(p_R\), the induced red pair-step system on \(R\) contains a red antipodal path using each of its \(2|R|\) original directions once. Then every full starting parity fiber contains at least \(2^k\) roots of red full antipodal geodesics. The resulting pair words are \(i_1\cdots i_k\,v\,i_k\cdots i_1\), where the core word \(v\) may depend on the frozen outer state.

*Proof.* Fix an initial full parity \(p\). The red-step prefix \(T_{i_k}\cdots T_{i_1}\) is a bijection on the starting \(q\)-states. Select arbitrarily the \(k\) outer \(q\)-bits after this prefix. The assumed core theorem selects core initial \(q_R\) and a red full core path; its traversal complements all core \(q\)-bits, restores their parity bits, and leaves all outer bits fixed. Now apply outer steps in reverse order. At the two visits to \(i_t\), every parity bit except \(p_{i_t}\) has the same value; the other \(q\)-bits differ precisely by complementation on \(D_t\). Gate \(f_{i_t}\) ignores \(p_{i_t},q_{i_t}\), and (NG2) says its second value is the complement of its first. The two red steps consequently select different members \(a_{i_t},b_{i_t}\) of the pair, and together complement \(q_{i_t}\). Descending induction over \(t\) completes all directions once, with antipodal endpoint. Each selected postprefix outer \(q\)-state supplies a distinct original root by bijectivity. \(\square\)

**Corollary (nonsingular phase-affine core, nonlinear exterior).** Assume (NG2), \(|R|\ge2\), and for \(j\in R\)
\[
f_j(p,q)=\sum_{\ell\in R}A_{j\ell}q_\ell+\theta_j(p,q_{[m]\setminus R}),
\tag{NG3}
\]
where \(A\) is a fixed nonsingular zero-diagonal binary matrix and \(\theta_j\) ignores \(p_j\). The phases may be arbitrary nonlinear functions of the exterior \(q\)-bits and other parity bits, subject to the coloring being legal. For any ordering \(\pi\) of \(R\), the single nested word \(i_1\cdots i_k\,\pi\pi\,i_k\cdots i_1\) has precisely \(2^k\) red antipodal starting roots in every prescribed parity fiber.

*Proof.* Split \(A=L+U\) in \(\pi\)-order into strict lower and upper triangular matrices. A core sweep has homogeneous \(q_R\)-action \(M=(I+L)^{-1}(I+U)\); changes of phase along the parity trajectory affect only the affine translation. After two sweeps the homogeneous return is \(M^2\). In characteristic two,
\[
\det(I+M^2)=\det(I+M)^2=\det A=1
\]
because \(I+M=(I+L)^{-1}A\). For every frozen exterior state there is one core root with complemented return. Apply the theorem. \(\square\)

**Corollary (variable-slope three-pair core).** Assume (NG2), \(|R|=3\), and
\[
f_j(p,q+\mathbf1_R)=1+f_j(p,q)\quad\text{for each }j\in R\text{ and every }p,q.
\tag{NG4}
\]
Then every prescribed full parity fiber contains at least \(2^k\) successful red antipodal roots. Indeed, freezing the exterior state yields a legal paired-flat \(Q_6\) coloring on the three core pairs. The established fiberwise \(Q_6\) forcing theorem (the independent complete \(2^{24}\)-coloring verification above) supplies the core path for every \(p_R\). The core word may depend on the frozen state, and its slopes may vary with parity.

**Corollary (one-pair square-switch stability).** In either of the preceding classes, switching a legal antipodal pair of alternating squares in pair \(i_1\) changes only its gate. All other hypotheses persist, and (NG2) for \(i_1\) is automatic for every legal gate. Consequently both sides of every such switch have red full antipodal geodesics in each parity fiber. This supplies a nonlinear restricted-family instance of the square-boundary preservation target.

For example, in four pairs take \(R=\{1,2,3\}\), the first outer label \(0\), and
\[
f_0=q_1+(q_1+q_2)(q_2+q_3),\quad
f_1=q_2,\quad f_2=q_3,\quad f_3=q_1.
\tag{NG5}
\]
These are legal odd gates. The first is quadratic in \(q\). The core is the nonsingular three-cycle. The word \(0,1,2,3,1,2,3,0\) has two successful \(q\)-roots \(4,5\) in every pair-parity fiber, with direction order \((1,3,4,6,2,5,7,0)\). Finite-state tests for multiple nonlinear gates through seven pairs agree with the stated \(2^k\) count; the proof uses the involution and core arguments above.

**Remaining transfer.** Arbitrary nonlinear paired-flat gates need not admit a decomposition satisfying (NG2) or (NG4). Producing such a decomposition inside the balanced critical-square boundary would imply unrestricted NORI1 via the existing boundary reduction. That hypothesis-production step is open. The theorem has no established transfer to original-vertex-simple boundary tournaments.


###### Complete six-pair peeling and directed feedback-core forcing (18 October 2026)

**Finite theorem (computer-assisted).** Every zero-diagonal 6x6 binary matrix A satisfying A1=1 has an ordered deletion i_1,...,i_k (0<=k<=4) with sum_(s<t) a_(i_t,i_s)=0 at each step and nonsingular remaining principal matrix A[R,R]. A portable C++17 verifier explicitly enumerates all 16^6=16,777,216 such matrices and performs subset-reachability plus binary Gaussian elimination. There are no failures.

**MINIMUM DELETION COUNTS.** k=0:5,000,192; k=1:7,958,848; k=2:2,933,900; k=3:658,510; k=4:225,766. Total 16,777,216. This table counts the smallest feasible k for each matrix, not merely the first successful subset in numerical order. An independently written Python audit verified positive results on 15,000 sampled six-pair matrices, and a separate red-path simulator validated predicted 2^k roots for 2,000 random six-pair nonlinear-phase instances.

**NORI1 CONSEQUENCE.** By the established nested-core forcing theorem, every legal paired-flat Q12 coloring with fixed odd affine q-slope matrix A and arbitrary nonlinear parity-phase gates has a red full antipodal geodesic rooted in EVERY prescribed pair-parity fiber. There are 2^24 eligible coefficient matrices and 2^192 possible phase tables, covering 2^216 such colorings. The pair order is selected from A alone and guarantees 2^k starting q-states in each fiber.

**ALL-DIMENSIONAL FEEDBACK-CORE THEOREM.** Put a directed influence arc j->i when a_ij=1. Suppose some label set R satisfies det A[R,R]=1 and the induced subgraph on D=[m]\R is acyclic. Deleting D in reverse topological order is a valid parity peel, because no newly deleted vertex receives an arc from a previously deleted vertex. The nested-core word produces 2^|D| full red geodesic roots in each prescribed parity fiber for arbitrary nonlinear phase assignments. This gives a simple constructive graph certificate for any dimension.

**SCC CYCLE-INTERSECTION COROLLARY.** In particular, suppose NO strongly connected component contains two vertex-disjoint directed cycles. For each cyclic SCC H choose a shortest directed cycle C_H. It is an induced cycle (a chord would create a shorter directed cycle), so the corresponding adjacency submatrix is a cyclic permutation matrix with determinant one. Their union R has block-triangular principal adjacency, hence det A[R,R]=1. Every cycle lies within an SCC and meets C_H by hypothesis; thus the complement D is acyclic. The feedback-core theorem applies. This is an unbounded-dimensional forcing theorem for potentially singular influence matrices and arbitrary nonlinear phase gates. A separate full graph enumeration verified the criterion for 8/8 matrices on three labels, 231/256 on four labels, and 17,664/32,768 on five labels.

**PRINCIPAL-MINOR PARITY LEMMA.** Every zero-diagonal A with A1=1 has an odd number of nonsingular principal minors of order at least two. Over F2, det(I+A)=sum_(R subset [m]) det A[R,R], with det(empty)=1. But (I+A)1=0 so det(I+A)=0, and singleton principal minors vanish. Therefore sum_(|R|>=2) det A[R,R]=1. This proves that an invertible principal core ALWAYS EXISTS; the general conjecture asks additionally for one accessible through legal parity peeling.

**STATUS AND LIMITS.** The six-pair conclusion is a complete finite computation with reproducible source, not a dimension-uniform proof of the odd-matrix peeling conjecture. The SCC-feedback criterion is proved in all dimensions, but does not cover every odd matrix (on five labels it covers 17,664 of 32,768). Full NORI1 allows parity-varying affine slopes or non-affine dependence on q; neither is resolved by the finite static-slope result.

**AUDIT FILES.** /mnt/data/nori_six_pair_peeling_feedback_report.md, /mnt/data/nori_matrix_m6_minpeel.cpp, /mnt/data/nori_matrix_m6_exhaust.cpp, /mnt/data/nori_m6_independent_audit.py, /mnt/data/nori_feedback_cycle_test.py, /mnt/data/nori_nested_direct_paths.py. Research archive /mnt/data/nori_six_pair_peeling_feedback_bundle.zip.

###### Rank-four column reduction and four-column zero-sum compatibility forcing

Let A be a zero-diagonal binary m-by-m matrix with A1=1. A deletion sequence i_1,...,i_k is legal when sum_(s<t) a_(i_t,i_s)=0 for every t. It succeeds if A[R,R] on the remaining labels is nonsingular.

**THEOREM A (column cancellation).** (1) Two equal columns can be legally deleted one after the other, with odd row sums retained in the residual matrix; the diagonal zero gives the required two-way entries zero. (2) A zero column can be deleted, again leaving odd row sums. (3) Two disjoint pairs of columns each summing to the all-one vector can always be deleted in some four-step legal order; the total of their four columns is zero, so all surviving row sums remain odd.

**Proof of (3).** Label the pairs (a0,a1), (b0,b1). Write c_t=A_(b_t,a0) and d_s=A_(a_s,b0), over F2. Complementarity makes A_(b_t,a_s)=c_t+s, A_(a_s,b_t)=d_s+t and the two within-pair cross-entries equal one. If c_0!=c_1 use the order (a_(c_0),b0,b1,a_(1-c_0)). If c_0=c_1=c put t=1+d_(1-c), and use (a_c,b_t,a_(1-c),b_(1-t)). The second and third choices have incoming parity zero, while the fourth is legal since the induced four rows have even total parity. QED.

**THEOREM B (bounded-rank compression).** Suppose rank(A)=r. Factor A=UV^T over F2 with U of full column rank, and normalize s=V^T1=e0, so U s=1. Each factor column v_i satisfies u_i dot v_i=0 whereas u_i dot s=1, hence v_i!=s. In a smallest unpeelable matrix the column-cancellation lemma excludes zero factors, repeated factors, and two complete pairs {v,v+s}. Modulo span(s), the nonzero factors occupy at most one representative of each of 2^(r-1)-1 nonzero quotient classes, plus at most one extra representative of one class. Consequently a smallest unpeelable matrix has at most 2^(r-1) labels.

For r<=3, at most four labels remain; this contradicts the previously fully checked odd six-label theorem. For r=4, at most eight remain. Eight is impossible: it would contain one doubled quotient class p and a singleton in each of the other six nonzero F2^3 classes; their quotient XOR is p!=0, whereas sum v_i=s projects to zero. At seven labels, one doubled class and five singleton classes similarly have nonzero quotient XOR p+q (q is the omitted class). Hence the only seven-label pattern chooses one representative of EVERY nonzero quotient class t in F2^3, the Fano-plane configuration.

**THEOREM C (rank at most four, every matrix size; computer-assisted finite base).** Every zero-diagonal A with A1=1 and rank(A)<=4 has a successful legal parity peel. For the rank-four seven-label normal form, normalize s=e0 and write each column factor as v_t=(epsilon_t,t), t=1,...,7, where sum_t epsilon_t=1. There are 64 lift patterns. Each row factor u_t=(1,z_t) satisfies u_t dot v_t=0, giving four choices for z_t. Thus there are 64*4^7=1,048,576 labeled Fano normal forms. A complete portable C++17 subset-DP verification checks every one. Zero failures occur, with minimum peeling counts k=3:920000, k=4:121184, k=5:7392. The earlier analytic reductions prepend legal deletions to these finite certificates, proving the theorem for ALL matrix sizes. Separately coded Python rank/reachability checked 20000 seeded configurations. Another independent canonical check exhausted 540 rank-at-most-three configurations.

**NORI1 CONSEQUENCE.** By the previously proved nested double-sweep theorem, every legal paired-flat Q_(2m) coloring with a parity-independent affine q-slope matrix of rank at most four and arbitrary nonlinear parity-phase functions has an all-red full antipodal geodesic rooted in EVERY prescribed pair-parity fiber, for all m. The pair word depends only on its slope matrix and gives 2^k red starting roots when k labels are peeled. This is a dimension-uniform theorem within this class, not unrestricted NORI1.

**THEOREM D (zero-sum four-column forcing).** Let four distinct columns of A sum to zero. The induced four-row restriction has zero diagonal and even row sums. Of the 256 such four-row patterns, 240 admit a legal deletion of all four labels. The remaining 16 patterns have a bidirected triangle among three labels, with these triangle rows not reading the fourth label. Four choices of the outside label times four even possibilities for its row give the 16. This is an exhaustive four-vertex Boolean lemma verified independently over all 256 cases and all 24 orders. Whenever a zero-sum quartet is not exceptional, its deletion preserves the odd-row property.

**FANO FOUR-COLUMN COVER.** In the rank-four Fano seven-label pattern, the complements of its seven projective lines are four-label sets. Because the lift parity sum is odd and each point belongs to three lines, at least one such quartet has zero column sum. An exhaustive local-only checker on ALL 1,048,576 normal forms shows at least one of these zero-sum quartets is nonexceptional. Thus it can be deleted, reducing to an odd-row three-label matrix. This provides a second finite proof certificate of rank-four success without seven-label reachability calculations.

**OUTLOOK AND STATUS.** The general parity-peeling conjecture remains open for unrestricted ranks. A minimal counterexample must now resist repeated columns, zero columns, complementary-column pairs and every nonexceptional zero-sum column quartet; each additive column parallelogram would have to support the exceptional bidirected-triangle obstruction. This is a common-matrix compatibility condition suitable for direct attack in higher ranks. Fully unrestricted NORI1 remains open.

**REPRODUCIBLE FILES.** nori_low_rank_peeling_and_zero_sum_quartets.md; nori_rank4_fano_enumeration.cpp; nori_rank4_quartet.cpp; nori_rank4_fano_independent_check.py; nori_rank3_column_compression_verifier.py; nori_zero_sum_quartet_verifier.py; nori_rank_four_column_peeling_bundle.zip.

##### Independent rank-five affine-coset certificates and the twelve-label barrier

This update replaces the preliminary solver-only eight-point and twelve-label checks with three standalone exhaustive C++17 certificates. The matrix is a zero-diagonal odd-row binary matrix \(A\); a legal peel deletes labels whose rows have even parity toward earlier deletions. Prior results prove peeling for rank at most four and compress a minimal rank-five obstruction to nonzero quotient columns of \(\mathbb F_2^4\) with at most one duplicated quotient class.

**Lemma 1 (unconditional affine eight-plane).** For all eight quotient columns \(t=(1,u)\), \(u\in\mathbb F_2^3\), and arbitrary permitted lifts, some four-point affine plane has zero full-column sum and permits a legal deletion of its four labels. The verifier normalizes one of the eight four-bit row factors to zero by the common gauge translation and enumerates the remaining seven. The search visits \(1,1,16,256,2176,34816,49152,0,0\) partial nodes at successive depths, with no survivors. If the eight total lifted columns have odd sum, deleting this plane leaves a four-label odd-row matrix, handled by the earlier theorem.

**Lemma 2 (even-sum affine eight-point closure).** If the eight columns have total sum zero, all eight labels have a legal full peel. An independent integer-only verifier checks all \(134217728\) gauge-normalized even-sum assignments. Complementary peelable four-planes certify \(134167552\), while direct Boolean reachability on all \(256\) deletion subsets certifies the remaining \(50176\). There are no failures. This replaces the former eight-point SMT UNSAT assertion with a checked finite enumeration.

**Lemma 3 (twelve-label projective quartet).** For quotient labels \(3,5,6,7,9,10,11,12,13,14,15,15\), the duplicated quotient columns having opposite lift bits, one of eleven fixed candidate quotient-zero-sum quartets is a full-column-zero-sum quartet that permits complete legal peeling. The proof enumerator needs only the eight indexed labels \(0,2,3,5,6,9,10,11\), fixing one four-bit gauge vector to zero, and visits \(1,1,16,256,2176,2048,32768,15360,0\) nodes. In the local four-label test, the 16 exceptional even-row matrices are precisely a bidirected triangle with no outgoing triangle arcs to the fourth label; the fourth row may have any even pattern. This characterization has an independent 256-case audit.

**Theorem (rank-five threshold).** With the preceding rank-four theorem and minimal-counterexample compression, no size-minimal rank-five counterexample has \(m\ge12\) pair labels. The earlier projective reductions for \(m=13,14,15\) now use Lemmas 1 and 2 instead of solver assumptions. The twelve-label configuration with one duplicated class is eliminated by Lemma 3 and minimality: after its zero-sum quartet deletion, the odd-row residual is strictly smaller and has rank at most five. For twelve distinct classes the three missing points form a quotient projective line. Its three complementary four-point cosets have odd total lift parity; choose an odd one as the inside of a containing hyperplane, making the outside eight-point affine coset even-sum. Lemma 2 removes that outside set, leaving a four-label odd-row residual.

This is a finite-audit strengthening, **not** a proof of rank-five closure in the remaining \(7\le m\le11\), of the arbitrary-rank peeling conjecture, or of unrestricted NORI1. Full report and integer-only source files: `nori_rank5_independent_finite_closure.md`, `nori_affine8_plane_exhaust.cpp`, `nori_affine8_even_full_exhaust.cpp`, `nori_rank5_local_quartet_exhaust.cpp`; research note `note_43efdcdab134f6eee75a199b`.


###### Analytic Fano quartet forcing and projective row-distance rigidity

**RESULT.** The seven-label rank-four Fano part of the earlier parity-peeling theorem is proved without enumeration. For its seven columns there are at least three full-column-zero-sum quartets, and no more than two can be exceptional under the four-vertex parity deletion lemma. Thus some quartet can be removed legally, reducing to a three-label odd matrix, which always has a nonsingular accessible core. The former 1048576-instance Fano check is now an independent audit only; the earlier at-most-six-label base remains computer-assisted. Full hand proof: nori_analytic_fano_quartet_forcing.md.

**NORMAL FORM AND CODE DISTANCE.** In the rank-four Fano normal form use labels t in F2^3\{0}, row factors u_t=(1,z_t), column factors v_t=(eps_t,t), with sum eps_t=1 and A_ij=u_i dot v_j. Two row words differ as
  A_(a,*)+A_(b,*) = ((z_a+z_b) dot t)_(t!=0).
If unequal their Hamming distance is FOUR, never two. More generally in a full projective quotient of dimension d=r-1, differences of distinct rows have Hamming weight 2^(d-1)=2^(r-2). This is a dimension-uniform simplex-code restriction on counterexample normal forms.

**AT LEAST THREE ZERO-SUM QUARTETS.** The seven quotient-zero quartets are complements of Fano lines L. Such a quartet has full column sum zero iff line epsilon parity lambda(L)=1, since sum_t eps_t=1. The number of odd lines is odd, because every point lies on three lines. It cannot be one: if a lone line L were odd, pick a point p not on L. Summing lambda over the three lines through p counts each epsilon point once modulo two and must give one, while every contributing line would be even. Hence at least three zero-sum quartets exist.

**PAIR COMPATIBILITY LEMMA.** Two distinct zero-sum Fano quartets C,D intersect in two labels x,y. If both are exceptional, their selected omitted vertices must both lie in C intersection D. To prove this, write C\D={a,b} and D\C={c,d}. If one omitted vertex is unique to its quartet and the other is shared, the two triangle constraints prescribe opposite values on a shared edge. If both omissions are unique, at a and c, each exceptional triangle includes x,y, so A_(x,a)=A_(x,c)=A_(y,a)=A_(y,c)=0 while A_(x,y)=A_(y,x)=1. The four quotient points a,b,c,d form one affine plane with difference space span(x,y), so t_a+t_c is t_z for z equal x or y. Thus v_a+v_c+v_z=delta s with s=(1,0,0,0). Evaluating at row z gives delta=0; evaluating at the other shared row gives delta=1. Contradiction. Therefore both omissions are shared.

**NO THREE EXCEPTIONS.** If three distinct quartets C,D,E were exceptional, the pair lemma forces each omitted vertex into their triple intersection. Three Fano-complement quartets have at most one common point: only two Fano lines avoid a prescribed pair of points. Thus either contradiction immediately or all omissions equal a common z. In the latter case, let p be the second common point of C,D and q the second common point of C,E; p and q are distinct. Row p is one on four points in (C union D)\{p,z}, zero at p,z; since C union D has six points and all row sums are odd, its seventh entry is also one. Hence row p = 1+e_p+e_z. Likewise row q =1+e_q+e_z. Their difference e_p+e_q has Hamming weight two, impossible by the simplex row-distance theorem. So there are at most two exceptional quartets. With at least three zero-sum quartets, a nonexceptional one must exist.

**COROLLARY.** Legally delete its four labels. The full column sum of that quartet is zero, hence every surviving row remains odd. Every odd zero-diagonal three-label matrix has a directed three-cycle (nonsingular) or a reciprocal two-cycle reachable by first deleting the remaining label. Thus every rank-four Fano normal form admits a successful peel without exhaustive computation. Combined with column compression and the earlier finite base for <=6 vertices, this preserves the dimension-uniform rank-at-most-four geodesic result.

**HIGHER-RANK SCOPE.** In rank-five full-projective 15-label normal forms, the analogous row difference has Hamming weight eight. Among the 105 quotient-zero quartets, each odd lift has 45 or more full-column-zero-sum quartets (checked for all 16384 odd lift patterns). This is a promising incidence-vs-exception problem, but the seven-point compatibility proof does not immediately extend.

**CAVEAT ABOUT EIGHT-POINT SPLITS.** A legal eight-point affine block of zero total column sum can fail to split into two independently peelable zero-sum quartets: t=8,...,15, epsilon mask 215 and row slopes z=(11,1,12,10,5,5,4,1) provide such a witness. Its whole eight-point induced graph nevertheless peels in order (0,2,1,4,5,3,6,7). The parallel research note note_43efdcdab134f6eee75a199b has since proved full eight-point peeling by a separate exhaustive certificate, so this example limits only the two-quartet shortcut and is NOT an obstruction to that theorem or to parity peeling.

**REPRODUCTION.** nori_analytic_fano_quartet_forcing.md; nori_fano_parity_audit.cpp; nori_fano_triple_linear.py; nori_rank5_zero_quads.cpp; nori_affine8_partition_counterexample.py; archive nori_analytic_fano_research_bundle.zip. Finite Fano audit reproduces zero-sum-quartet counts three/seven and exceptional count at most two; the proof above needs none of those enumerations. NORI1 and the all-rank matrix-peeling conjecture remain open.

##### Rank-five parity-peeling closure in all dimensions

**Theorem (computer-assisted, all sizes).** Every \(m\times m\) binary matrix \(A\) with zero diagonal, \(A\mathbf1=\mathbf1\), and \(\operatorname{rank}A\le5\) admits a legal parity peel \(i_1,\ldots,i_k\) whose remaining principal matrix \(A[R,R]\) is nonsingular. Consequently, by the nested-core forcing theorem, every legal paired-flat coloring with a fixed affine fiber-reader matrix of rank at most five and arbitrary nonlinear parity-phase functions has a red full antipodal geodesic in every prescribed parity fiber.

**Proof framework.** Choose a smallest counterexample of rank at most five. The preceding rank-four theorem and complete at-most-six-label finite base force rank five and at least seven labels. The established column compression factors \(A_{ij}=(z_i+z_j)\cdot t_j\), where \(t_i\in\mathbb F_2^4\setminus\{0\}\), \(\sum_i t_i=0\), at most one quotient class is duplicated, and any duplicate has opposite full lifts. A common shift of all \(z_i\) preserves the matrix, permitting gauge \(z_0=0\).

All seven- and eight-label quotient multisets are classified under \(GL(4,2)\) by elementary transvections. There are two orbits at seven labels and three at eight. Independent finite audits check \(4194304+8388608\) eligible seven-label matrices, \(67108864\) matrices in the duplicated eight-label orbit, plus small finite certificates for the distinct and affine-coset eight-label orbits. All succeed.

At nine labels there are four quotient orbits. For every orbit, an independent bounded search shows that some proper subset of three, four, or six labels has zero full-column sum and admits complete legal peeling. Deleting it preserves odd row sums and yields a smaller matrix of rank at most five, contrary to minimality.

At ten or eleven labels the quotient classification has respectively four or two orbits, each containing one of the two six-column patterns \((1,1,2,3,4,5)\) or \((1,2,3,4,5,6)\). An independent six-column verifier checks all \(524288\) and \(1048576\) normalized permitted assignments, respectively. Every assignment has a peelable zero-sum block of size three, four, **or six**; the whole six-column option is essential. Again minimality rules out a counterexample.

For twelve or more labels, the preceding projective hyperplane reductions and the separately checked eight-point affine-coset and twelve-point quartet certificates force a peelable zero-sum block, or rule out the column multiplicity pattern by parity. These exhaust all possible minimal sizes, proving the theorem.

**Reproducibility.** Standalone integer-only enumeration, subset reachability and binary Gaussian elimination are supplied in \`nori_rank5_complete_proof_bundle.zip\` with proof \`nori_rank5_matrix_closure_complete.md\`. The principal research note is \`note_92ce6bdf09135a7de5fb4d8a\`. This is **not** unrestricted NORI1: higher-rank matrices, parity-varying affine slopes, and nonlinear fiber dependence remain open.


#### Scope audit: why bounded terminal components do not control unrestricted NORI1

The terminal-seam results for one, two, and three pair labels give correct positive theorems and a progressively stronger necessary restriction on a hypothetical critical good coloring. Their size bounds provide no reduction of arbitrary nonlinear paired-flat colorings to bounded terminal components. The following dimension-uniform calculation quantifies this limitation.

**Proposition (generic dependency saturation).** For \(m\ge3\), choose independently and uniformly for each pair \(i\) a legal paired-flat Boolean gate
\[
f_i:\mathbb F_2^{m-1}\times\mathbb F_2^{m-1}\to\mathbb F_2,
\qquad f_i(p_{-i},q_{-i}+\mathbf1)=1+f_i(p_{-i},q_{-i}).
\]
Draw an arc \(j\to i\) when \(f_i\) depends on at least one of \(p_j,q_j\). For each ordered pair \(i\ne j\),
\[
\Pr(j\not\to i)=2^{-3\cdot2^{2m-5}}.
\tag{G1}
\]
Consequently
\[
\Pr(\text{dependency digraph is not complete})
\le m(m-1)\,2^{-3\cdot2^{2m-5}}.
\tag{G2}
\]
These random instances are all legal, antipodally odd and perfectly vertex-balanced.

*Proof.* For each \(i\), the gate is independently determined by choosing one Boolean value from each complementary pair of \(q_{-i}\)-arguments for each \(p_{-i}\). It therefore has \(N=2^{m-1}2^{m-2}=2^{2m-3}\) independent truth-table bits. The gates ignoring both \(p_j\) and \(q_j\) are precisely the legal gates on the remaining \(m-2\) outside labels, with \(N'=2^{m-2}2^{m-3}=2^{2m-5}\) independent bits. Their proportion is \(2^{N'-N}=2^{-3\cdot2^{2m-5}}\). The union bound over the \(m(m-1)\) ordered arcs gives (G2). Each pair contributes exactly one red and one blue incident edge at every vertex, proving perfect balance. \(\square\)

The first excluded arcs become astronomically rare as \(m\) grows. In particular, the previously proved condition that terminal strongly connected components of a critical good coloring have at least four labels does not provide an avenue to unrestricted closure unless *criticality itself* forces further nontrivial restrictions on the dependency graph. Ordinary legality and balance tend in the opposite direction. Extending the three-pair terminal-seam classification to the next fixed component size would leave this transfer obligation intact.

##### General terminal seams and the ordinary one-change geodesic problem

There is an exact unlimited-rank version of the finite seam mechanism. Fix \(k\ge1\) and let \(A\) be any ordinary paired-flat binary coloring of undirected edges of \(Q_{2k}\); it need not be antipodally odd. Define its dual \(A^\vee(e)=1+A(\bar e)\). A *red seam completion* is a full antipodal geodesic using each of the \(2k\) original directions once, with an initial consecutive block of edges red in \(A\), followed by a final consecutive block red in \(A^\vee\). The transition occurs at a common vertex and both blocks may have length zero.

**Proposition (exact one-change transfer).** Such a red seam completion exists if and only if \(A\) has a full antipodal geodesic with at most one color change. More precisely, red seam completions with specified starting vertex \(x\) correspond bijectively to red-then-blue antipodal full geodesics of \(A\) with the color-change vertex at \(x\).

*Proof.* Let a red seam start at \(x\), traverse the \(A\)-red prefix to \(u\), then traverse the \(A^\vee\)-red suffix to \(\bar x\). Reverse the first segment, obtaining an \(A\)-red path from \(u\) to \(x\). Complement the vertices and reverse the second segment; because \(A^\vee(e)=1+A(\bar e)\), this is an \(A\)-blue path from \(x\) to \(\bar u\). Their concatenation is a full antipodal geodesic with word red followed by blue; the sets of original directions are disjoint and exhaust all \(2k\) labels. Conversely, start with an \(A\)-geodesic \(u\to x\to\bar u\) consisting of a red prefix and blue suffix. Reverse its red prefix and complement/reverse its blue suffix to construct the red seam \(x\to u\to\bar x\). These operations are mutually inverse. A blue-then-red one-change geodesic can be reversed, so existence with at most one change is equivalent. \(\square\)

If \(A\) is itself antipodally odd, any one-change full geodesic becomes monochromatic after cyclic root rotation at its color-change vertex: the antipodally translated initial color block joins the final block with its color complemented. Thus the universal arbitrary-\(k\) paired-flat seam-completion assertion would imply unrestricted NORI1 through the established paired-flat lift. It is a full-strength general forcing problem, not a routine extrapolation of the finite one-, two-, and three-pair checks. The original cube directions remain distinct throughout the correspondence.

The fiberwise finite seam property asks for more than one unrooted one-change path: the pivot \(x\) must occur in every prescribed pair-parity fiber. The distinction matters. No all-\(k\) proof, uniform root-selector theorem, or reduction of arbitrary critical colorings to bounded-size terminal blocks is currently available.

**Research decision.** Close the bounded-pair classification programme until an independent structural theorem derives its hypotheses for arbitrary critical colorings. Transfer research effort to the unrestricted paired-flat square-switch boundary and, separately, to dimension-uniform red/blue one-change exchanges in ordinary paired-flat systems. Both target arbitrary nonlinear truth tables; finite examples should be used to refute a sharply formulated general exchange lemma rather than to raise the bounded rank ceiling.


### Edge-conditioned turn census and critical-flip forcing

Let \(n\ge3\) and let \(c\) color the undirected edges of \(Q_n\) by \(0,1\), with \(c_i(x+e_i)=c_i(x)\) and \(c_i(\bar x)=1-c_i(x)\). Let \(\mathcal O_n\) denote the family of coherent projective supports of full antipodal geodesics, so
\[
M=|\mathcal O_n|=2^{n-2}(n-1)!.
\]
For a projective vertex \([v]=\{v,\bar v\}\) and two distinct dimensions \(j,k\), let
\[
t=([v],\{j,k\}),\qquad I_t(c)=[c_j(v)\ne c_k(v)].
\]
This indicator is well defined because both incident colors complement together at \(\bar v\). Write \(T_c(O)=2\sum_{t\in O}I_t(c)\); the possible cyclic energies are \(2,6,10,\ldots\).

For an antipodal edge orbit \(e\) in direction \(i\), choose its unique representative \(\{x,x+e_i\}\) whose endpoint \(x\) has \(i\)-th bit zero. Let
\[
m=(n-1)!,\qquad D=[n]\setminus\{i\}.
\]
The set of supports containing \(e\) has cardinality \(m\).

#### The edge-turn factorial incidence theorem

**Theorem 1.** For every projective turn \(t=([y],\{j,k\})\), the number \(N(e,t)\) of coherent supports containing both \(e\) and \(t\) is determined by the following mutually exclusive cases.

1. If \([y]=[x]\) or \([y]=[x+e_i]\), then
\[
N(e,t)=\begin{cases}(n-2)!,&i\in\{j,k\},\\0,&i\notin\{j,k\}.\end{cases}
\tag{1}
\]
2. At any other projective vertex, choose the representative \(y^\sharp\in[y]\) with \(i\)-th bit one, and set
\[
S=\operatorname{supp}(y^\sharp+x+e_i)\subseteq D.
\]
Then \(1\le |S|\le n-2\), and
\[
\boxed{
N(e,t)=
\begin{cases}
(|S|-1)!(n-|S|-2)!,&
j,k\in D,\ |\{j,k\}\cap S|=1,\\
0,&\text{otherwise}.
\end{cases}}
\tag{2}
\]

**Proof.** Each support containing \(e\) has a unique orientation beginning at the projective vertex \([x]\), traversing direction \(i\) first, and then traversing the remaining \(n-1\) dimensions in some permutation. Conversely every permutation of \(D\) yields one support containing \(e\). This proves the count \(m\).

At \([x]\) and \([x+e_i]\), the support turns use direction \(i\) and respectively the last and first dimensions from the permutation of \(D\). Specifying either of these other dimensions leaves \((n-2)!\) possibilities, proving (1).

All other vertices visited by the oriented support are uniquely represented by \(x+e_i+\mathbf1_S\), where \(S\) is a nonempty proper prefix set in the permutation of \(D\). This is the representative with \(i\)-th bit one. The turn at this vertex has as its incident labels the last member \(j\) of the prefix \(S\) and the first member \(k\) of \(D\setminus S\), in either order. Thus a specified turn is possible precisely when one of \(j,k\) belongs to \(S\) and the other to \(D\setminus S\). Ordering the remaining members within these two blocks independently gives \((|S|-1)!(n-|S|-2)!\) supports. \(\square\)

Define the **edge-conditioned turn sum**
\[
\mathcal A_e(c):=\sum_t N(e,t)I_t(c).
\tag{3}
\]
Theorem 1 makes (3) an explicit weighted sum of color comparisons at projective vertices. In expanded form,
\[
\begin{aligned}
\mathcal A_e(c)=&
(n-2)!\sum_{j\in D}
\left(I_{ij}([x])+I_{ij}([x+e_i])\right)\\
&+\sum_{\substack{S\subsetneq D\\ S\ne\varnothing}}
(|S|-1)!(n-|S|-2)!
\sum_{\substack{j\in S\\k\in D\setminus S}}
I_{jk}([x+e_i+\mathbf1_S]).
\end{aligned}
\tag{4}
\]
There is no averaging over alternative colorings in this formula.

**Corollary 2 (anchored first moment).**
\[
\boxed{\sum_{O:e\in O}T_c(O)=2\mathcal A_e(c),\qquad
\mathbb E(T_c\mid e\in O)=\frac{2\mathcal A_e(c)}{(n-1)!}.}
\tag{5}
\]
This follows by interchanging the support sum with its constituent projective turns.

#### A sufficient certificate for one-orbit flip stability

Write \(r(v)=|\{i:c_i(v)=1\}|\), and set
\[
\mathcal S(c)=\sum_{[v]}r(v)(n-r(v)).
\]
The unrestricted global turn-star census gives
\[
\sum_{O\in\mathcal O_n}T_c(O)
=2(n-2)!\mathcal S(c).
\tag{6}
\]
Let \(g_{\neg e}(c)\) count the coherent supports containing a monochromatic full geodesic and avoiding the orbit \(e\).

**Theorem 3 (critical-flip exclusion).** Every legal coloring satisfies
\[
\boxed{
g_{\neg e}(c)\ge
\max\left\{0,\
\frac{3\bigl(M-(n-1)!\bigr)-(n-2)!\mathcal S(c)+\mathcal A_e(c)}2
\right\}.}
\tag{7}
\]
In particular, the inequality
\[
\boxed{
(n-2)!\mathcal S(c)-\mathcal A_e(c)
<3\bigl(M-(n-1)!\bigr)
}
\tag{8}
\]
guarantees a monochromatic full antipodal geodesic that avoids \(e\). Such a geodesic survives reversing the colors of the two edges in \(e\). Conversely, at a first good-to-bad antipodal-orbit flip, the good-side coloring necessarily satisfies
\[
\boxed{
(n-2)!\mathcal S(c)-\mathcal A_e(c)
\ge3\bigl(M-(n-1)!\bigr).
}
\tag{9}
\]

**Proof.** There are \(N=M-m\) coherent supports avoiding \(e\). From (5)–(6) their total cyclic turn energy equals
\[
2\bigl((n-2)!\mathcal S(c)-\mathcal A_e(c)\bigr).
\]
A support carrying a monochromatic full geodesic has energy \(2\); every other support has energy at least \(6\). Consequently the energy sum over these \(N\) supports is at least
\[
2g_{\neg e}+6(N-g_{\neg e})=6N-4g_{\neg e}.
\]
Rearranging proves (7). If the right-hand side of (7) is positive, a monochromatic support avoiding \(e\) exists, and changing the two edge colors in \(e\) does not affect it. Hence any good coloring that becomes bad after such a flip must satisfy the reverse inequality (9). \(\square\)

Equivalently put \(\mu=\mathbb E_O T_c(O)\), \(\mu_e=\mathbb E(T_c\mid e\in O)\), and \(\alpha=2^{2-n}\). Then
\[
\boxed{
\mathbb E(T_c\mid e\notin O)
=\frac{\mu-\alpha\mu_e}{1-\alpha},\qquad
g_{\neg e}\ge\frac{M(6-\mu)+m(\mu_e-6)}4,
}
\tag{10}
\]
where the latter lower bound is clipped at zero. Formula (10) shows that edge conditioning can force survival even when \(\mu\ge6\).

#### A balanced five-dimensional witness beyond the global first moment

In \(Q_5\), index dimensions by \(0,1,2,3,4\) and let
\[
c_0(x)=x_1,\quad c_1(x)=1+x_0,\quad
c_2(x)=x_0,\quad c_3(x)=1+x_0,\quad c_4(x)=x_0
\qquad(\bmod 2).
\tag{11}
\]
Every edge rule ignores its own dimension, changes under the full antipodal map, and gives vertex color-one degree \(r(x)=2+x_1\). The coloring is maximally balanced, so its global mean is \(\mu=6\), and the unconditioned first-moment bound gives no positive lower bound on the number of two-turn supports.

Take the direction-four antipodal edge orbit represented by the edge with lower endpoint \(x=6\) (binary \(00110\)). Enumerating the \(192\) coherent supports gives the cyclic-energy histograms
\[
\begin{array}{c|rrr}
& T=2&T=6&T=10\\\hline
\text{all supports}&32&128&32\\
\text{supports containing }e&0&18&6\\
\text{supports avoiding }e&32&110&26 .
\end{array}
\tag{12}
\]
Thus \(\mu_e=7\) and
\[
\boxed{\mathbb E(T_c\mid e\notin O)=\frac{41}{7}<6.}
\tag{13}
\]
Theorem 3 alone guarantees at least six two-turn supports avoiding \(e\), while the complete enumeration gives thirty-two. This is a strict gain over the unconditioned mean criterion within one legal coloring. It certifies that this orbit may be flipped without eliminating every monochromatic full geodesic.

#### Verification and scope

The incidence formula (1)–(2) was checked by enumerating every coherent support and every edge-orbit/turn pair in dimensions \(3,4,5,6\); the support counts were \(4,24,192,1920\), and the projective-turn counts were \(12,48,160,480\). The anchored moment (5) was also checked on five independent sampled legal colorings per dimension. The five-dimensional histograms (12) were reconstructed independently. Verifier:
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/daf5b3ea030d0c2e55d83ce49bc2e59c68c4d8cf/scripts/nori_anchored_turn_census_verify.py.

Theorem 3 imposes a necessary condition on every hypothetical first good-to-bad orbit flip, using the same edge colors for the star census and the anchored turn terms. It is a sufficient one-flip stability criterion, rather than an unrestricted proof that every flip is stable. To close NORI1 through the critical-flip programme, one must exclude (9) jointly with the internal-pivot constraints on monochromatic geodesics in the good-side coloring.

#### Relative kernel theorem after deleting one antipodal edge orbit

Let \(A\) be the real support-by-turn incidence matrix: its rows are the coherent supports \(O\in\mathcal O_n\), and its columns the projective turns \(t\), with \(A_{O,t}=\mathbf1_{\{t\in O\}}\). Let \(A_{\neg e}\) retain the rows for supports avoiding a fixed antipodal edge orbit \(e\), in direction \(i\), whose projective endpoints are \(u=[x]\) and \(v=[x+e_i]\). Define \(E_e\) to be the real subspace of turn weightings supported on the \(2(n-1)\) turns at \(u,v\) that involve direction \(i\).

Recall the independently established unrestricted full-incidence kernel theorem from Article VIII: for \(n\ge5\), every \(f\in\ker_{\mathbb R}A\) has
\[
f_{jk}([y])=a_j+a_k+g_j([y])+g_k([y]),
\quad\sum_j a_j=0,\quad g_j([y+e_j])=-g_j([y]).
\tag{14}
\]
In particular, every full-kernel weighting is *pair-additive* at each projective vertex: \(f_{jk}=h_j+h_k\), with \(h_j\) allowed to depend on the vertex.

**Theorem 4 (punctured turn-incidence rigidity).** For every \(n\ge5\) and every projective edge orbit \(e\),
\[
\boxed{\ker_{\mathbb R}A_{\neg e}=\ker_{\mathbb R}A+E_e,}
\qquad
\boxed{\dim_{\mathbb R}(\ker A_{\neg e}/\ker A)=2n-3.}
\tag{15}
\]
Consequently
\[
\boxed{
\operatorname{rank}_{\mathbb R}A_{\neg e}
=2^{n-1}\binom n2-n2^{n-2}-(n-1)-(2n-3).
}
\tag{16}
\]
Every additional kernel freedom caused by deleting the supports through \(e\) can be represented by turn weights at the two endpoints of \(e\), incident with direction \(i\).

**Proof for \(n\ge6\).** Relabel so \(i=0\), write \(D=[n]\setminus\{0\}\), \(m=|D|=n-1\ge5\), and fix the lower-endpoint representative \(x\) of \(e\). Each support containing \(e\) has a unique oriented representative starting at \([x]\), traversing direction \(0\), then traversing the members of \(D\) in a permutation \(\pi=(\pi_1,\ldots,\pi_m)\). For \(f\in\ker A_{\neg e}\), define
\[
H_f(\pi)=\sum_{t\in O(e,\pi)} f_t.
\tag{17}
\]
The assignment \(f\mapsto H_f\) is linear, with kernel \(\ker A\).

**Interior swaps.** Exchanging adjacent entries \(a,b\) in interior positions \(2,\ldots,m-1\) of \(\pi\) leaves \(H_f\) unchanged. To show this, denote their preceding and succeeding labels by \(c,d\), all distinct and in \(D\), and denote the projective vertex just before \(a,b\) by \([z]\). The difference of the two support sums depends only on this local square:
\[
\begin{aligned}
\mathcal D_f(z;c,a,b,d)={}&f_{ca}([z])-f_{cb}([z])\\
&+f_{ab}([z+e_a])-f_{ab}([z+e_b])\\
&+f_{bd}([z+e_a+e_b])-f_{ad}([z+e_a+e_b]).
\end{aligned}
\tag{18}
\]
Choose a spare direction \(q\in D\setminus\{c,a,b,d\}\); one exists because \(m\ge5\). Starting from the common cube root \(y=z+e_0+e_q+e_c\), compare supports whose initial direction blocks are
\[
(0,q,c,a,b,d)\quad\text{and}\quad(q,0,c,a,b,d),
\]
with the same remaining dimensions after \(d\). In either case interchange the adjacent \(a,b\). The vertex just before \(a,b\) is \([z]\), so both exchanges have the same difference (18). The direction-\(0\) edge occurs at \(y\) in the first pair and at \(y+e_q\) in the second; these belong to distinct projective direction-\(0\) edge orbits. Therefore at least one pair avoids the specified \(e\). Its two support sums vanish because \(f\in\ker A_{\neg e}\), so (18) is zero. This proves the interior-swap invariance for every choice of order and root.

The interior permutations are connected by adjacent swaps, hence \(H_f(\pi)\) depends only on the first and last labels of \(\pi\). Write its value as \(H(j,k)\) for \(j\ne k\in D\).

**Boundary swaps.** Fix four distinct \(j,\ell,k,k'\in D\). Choose \(r\in D\setminus\{j,\ell,k,k'\}\), possible since \(m\ge5\). The difference between orders starting \((j,\ell,r)\) and \((\ell,j,r)\) arises from the adjacent exchange \(j,\ell\), preceded by direction \(0\) and followed by \(r\), at the fixed projective location after \(0\). It therefore has the same value regardless of whether the final label is \(k\) or \(k'\). Hence
\[
H(j,k)-H(\ell,k)=H(j,k')-H(\ell,k').
\tag{19}
\]
For each \(j,\ell\) the left-hand difference is thus independent of the third label \(k\notin\{j,\ell\}\). Write the common difference as \(\delta_{j\ell}\). Choosing a label outside any three prescribed distinct labels shows
\(\delta_{j\ell}+\delta_{\ell h}=\delta_{jh}\), so \(\delta_{j\ell}=a_j-a_\ell\) for some numbers \(a_j\). It follows that
\[
\boxed{H(j,k)=a_j+b_k\quad(j\ne k)}
\tag{20}
\]
for certain vectors \(a,b\in\mathbb R^D\).

The space of functions (20) on ordered distinct pairs has dimension \(2m-1\): the only redundancy for \(m\ge3\) is simultaneous replacement \(a_j\mapsto a_j+t\), \(b_k\mapsto b_k-t\). Thus the image of \(f\mapsto H_f\), and hence \(\ker A_{\neg e}/\ker A\), has dimension at most \(2m-1=2n-3\).

Conversely assign arbitrary weights \(a_j\) to turns \(([x+e_0],\{0,j\})\), and weights \(b_k\) to turns \(([x],\{0,k\})\), and zero elsewhere. This weighting belongs to \(E_e\subseteq\ker A_{\neg e}\), and its support sum on \(O(e,\pi)\) is \(a_{\pi_1}+b_{\pi_m}\). These span all functions (20), of dimension \(2m-1\). The upper bound is attained, and subtracting such an endpoint weighting from any \(f\in\ker A_{\neg e}\) leaves a weighting in \(\ker A\). This proves (15), and (16) follows from the full rank theorem. \(\square\)

**Finite boundary \(n=5\).** Here the spare-label argument requires an additional check. The same endpoint subspace furnishes a seven-dimensional quotient of the punctured kernel, so the real rank of \(A_{\neg e}\) is at most \(116-7=109\). An independent characteristic-two Gaussian elimination on the complete \(168\times160\) punctured support-turn incidence matrix yields rank \(109\) over \(\mathbb F_2\). The real rank is at least the binary rank for an integer matrix, so the real rank is \(109\), completing (15) also for \(n=5\). Cube automorphisms carry every orbit into any other, so it suffices to check one. The same reproducible elimination gives ranks
\[
\begin{array}{c|rrrr}
n&4&5&6&7\\\hline
\operatorname{rank}_{\mathbb F_2}A&23&116&379&1114\\
\operatorname{rank}_{\mathbb F_2}A_{\neg e}&18&109&370&1103
\end{array}
\tag{21}
\]
(the uniform theorem is asserted for \(n\ge5\)). Verifier:
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/b0e25c09bf20e2b738b9b89251f0fd6498c22587/scripts/nori_punctured_turn_rank_verify.py.

#### Relative constant-energy rigidity and the improved flip criterion

**Theorem 5 (relative turn-energy rigidity).** For every \(n\ge5\), every legal coloring \(c\), and every projective edge orbit \(e\),
\[
\boxed{T_c(O)\text{ constant over all supports }O\text{ avoiding }e
\quad\Longrightarrow\quad T_c(O)=2\text{ for all those supports}.}
\tag{22}
\]

**Proof.** Suppose the common energy is \(\tau\). Put
\[
f_t=I_t(c)-\frac{\tau}{2n}.
\]
Each support has \(n\) projective turns, so \(f\in\ker A_{\neg e}\). By Theorem 4, write \(f=f^{(0)}+h\), with \(f^{(0)}\in\ker A\) and \(h\in E_e\). At every projective vertex other than the two endpoints of \(e\), the turn indicators \(I_{jk}([y])\) therefore satisfy the pair-additive four-direction relation
\[
I_{ab}+I_{cd}-I_{ac}-I_{bd}=0
\quad(a,b,c,d\text{ distinct}).
\tag{23}
\]
If at such a vertex at least two incident edges have each color, choose \(a,b\) of the first color and \(c,d\) of the second. Equation (23) becomes \(0+0-1-1=0\), a contradiction. Thus at every projective vertex except possibly the two endpoints of \(e\),
\[
r(y)\in\{0,1,n-1,n\},\qquad r(y)(n-r(y))\le n-1.
\]
At the two exceptional vertices the universal bound is \(r(y)(n-r(y))\le\lfloor n^2/4\rfloor\). Consequently the global turn-star census gives
\[
\begin{aligned}
\mu_{\rm all}
&=\frac4{2^{n-1}(n-1)}\sum_{[y]}r(y)(n-r(y))\\
&\le4+\frac{8\bigl(\lfloor n^2/4\rfloor-(n-1)\bigr)}
{2^{n-1}(n-1)}
<5 \qquad(n\ge5).
\end{aligned}
\tag{24}
\]
Yet the supports avoiding \(e\) form a proportion \(1-\alpha\), with \(\alpha=2^{2-n}\). If \(\tau\ge6\), every avoided support has energy at least \(6\), while every support through \(e\) has energy at least \(2\). It follows that
\[
\mu_{\rm all}\ge6(1-\alpha)+2\alpha
=6-4\alpha\ge\tfrac{11}{2}
\quad(n\ge5),
\]
contradicting (24). Since all cyclic energies belong to \(2+4\mathbb Z_{\ge0}\), necessarily \(\tau=2\). \(\square\)

**Corollary 6 (non-strict anchored forcing, \(n\ge5\)).**
\[
\boxed{\mathbb E(T_c\mid e\notin O)\le6
\quad\Longrightarrow\quad
\exists O\not\ni e:\ T_c(O)=2.}
\tag{25}
\]
Equivalently,
\[
\boxed{
(n-2)!\mathcal S(c)-\mathcal A_e(c)
\le3\bigl(M-(n-1)!\bigr)
\quad\Longrightarrow\quad
\text{a monochromatic full geodesic survives flipping }e.}
\tag{26}
\]
**Proof.** If all avoided supports had energy at least \(6\), their mean at most \(6\) would force all their energies to equal \(6\). Theorem 5 excludes this. Therefore one has energy \(2\) and remains unchanged when the orbit \(e\) is flipped. \(\square\)

This improves the strict first-moment edge-flip certificate (8) to a closed inequality, using the original coloring throughout. For a hypothetical first good-to-bad orbit flip, the necessary inequality from (9) sharpens to the strict form
\[
\boxed{(n-2)!\mathcal S(c)-\mathcal A_e(c)>3\bigl(M-(n-1)!\bigr)\qquad(n\ge5).}
\tag{27}
\]
The implication gives an edge-conditioned forcing theorem in arbitrary dimension. The full unrestricted NORI1 conjecture remains open.


#### Quantitative facet bridge: paired-root multiplicity determines bridge diversity

This result joins the critical edge-orbit programme with Article XV's arbitrary-facet paired-root framework. It counts good supports through each direction orbit, not just the existence of some witness.

Put \(d=n-1\), designate dimension \(i\), and identify its upper facet with \(Q_d\). Every legal antipodally odd coloring of \(Q_n\) consists of an arbitrary edge coloring \(f\) of that facet, together with the colors \(g(z)\) of the direction-\(i\) edges, indexed by \(z\in Q_d\), satisfying \(g(\bar z)=1-g(z)\). The colors on the lower facet are then forced by global antipodal oddness. Conversely any such \(f,g\) determine a legal coloring.

For a root \(z\in Q_d\), let \(N_f^+(z)\) count the \(d!\) full direction orders that yield a rooted geodesic with color word \(0^p1^{d-p}\), \(0\le p\le d\). Define \(N_f^-(z)\) analogously for \(1^p0^{d-p}\). Reversing a path proves
\[
\boxed{N_f^-(z)=N_f^+(\bar z).}
\tag{28}
\]
Let \(e_{[z]}\) be the antipodal pair of dimension-\(i\) edges over \(z,\bar z\). Let \(G_{[z]}(c)\) count monochromatic coherent supports through that edge orbit.

**Theorem 7 (quantitative facet bridge).** For every such \(f,g\) and a chosen representative \(z\) of the projective pair \([z]\),
\[
\boxed{
G_{[z]}(c)=
\begin{cases}
N_f^+(z),&g(z)=0,\\
N_f^+(\bar z),&g(z)=1.
\end{cases}}
\tag{29}
\]
Consequently, with \(\mathcal G(c)=\{O\in\mathcal O_n:T_c(O)=2\}\),
\[
\boxed{
\min_{\substack{g:Q_d\to\mathbb F_2\\g(\bar z)=1-g(z)}}
|\mathcal G(c(f,g))|
=
\sum_{\{z,\bar z\}}\min\{N_f^+(z),N_f^+(\bar z)\}.
}
\tag{30}
\]
Furthermore, defining \(P(f)=\{z:N_f^+(z)>0,\ N_f^+(\bar z)>0\}\),
\[
\boxed{
\min_g\#\{e\text{ of dimension }i:\exists O\in\mathcal G(c(f,g)),\ e\in O\}
=\frac{|P(f)|}{2}.
}
\tag{31}
\]
Every orbit corresponding to a pair in \(P(f)\) appears in some good support for **every** allowed \(g\); all other dimension-\(i\) orbits can be suppressed simultaneously by a suitable \(g\).

**Proof.** Each support through \(e_{[z]}\) has one oriented representative that begins in the lower facet over \(z\), traverses \(i\) into the upper facet, and then traverses the remaining \(d\) dimensions in an arbitrary permutation \(\pi\). This gives a bijection between such supports and \(S_d\). If \(w_f(z,\pi)\) is the color word along the resulting upper-facet geodesic, the cyclic projective change count is the number of changes in the extended word
\[
(g(z),\,w_f(z,\pi),\,1-g(z)).
\]
The endpoints differ, so this number equals one precisely when \(w_f(z,\pi)\) is nondecreasing if \(g(z)=0\), or nonincreasing if \(g(z)=1\). This proves (29). Every coherent support has one direction-\(i\) orbit. Sum (29) over representatives of \(\{z,\bar z\}\), noting that the bits \(g(z)\) can be selected independently on these antipodal pairs. Minimizing each term gives (30). Such a term is positive for both choices of \(g(z)\) precisely when \(z,\bar z\in P(f)\). Otherwise its contribution can be set to zero. Hence (31). \(\square\)

**Corollary 8 (root multiplicity criterion for prescribed-orbit avoidance).** The following are equivalent for each \(n\ge3\):

(a) Every legal \(Q_n\) coloring admits, for every prescribed antipodal edge orbit \(e\), a monochromatic coherent support avoiding \(e\).

(b) Every arbitrary coloring \(f\) of \(Q_{n-1}\) has
\[
\boxed{|P(f)|\ge4.}
\tag{32}
\]

**Proof.** Under (b), (31) gives at least two distinct direction-\(i\) orbits used by good supports for every \(i\), so there is always one different from any prescribed \(e\). Conversely, if some \(f\) has no paired roots or only one antipodal root pair, translate its facet roots if necessary so that its sole pair labels the prescribed edge orbit. Choose \(g\) to suppress every other direction-\(i\) orbit, using (31). Every full geodesic uses direction \(i\) once; thus all good supports, if any, use the prescribed orbit, contradicting (a). \(\square\)

This is a rigorous characterization of the strengthened orbit-avoidance target and explains the finite observations. An arbitrary colored square can have \(|P(f)|=2\), so the strengthening fails in \(Q_3\). All arbitrary three-cube colorings have at least four paired roots, as established by the known cross-orientation intersection theorem, giving the \(Q_4\) case. The reported infeasibility calculation for orbit avoidance in \(Q_5\) is equivalently a computation-backed lower bound \(|P(f)|\ge4\) for arbitrary four-cube colorings. The Cartesian product of two extremal colored squares has four paired roots, showing the bound is sharp in dimension four. The universal bound \(|P(f)|\ge4\) in higher dimensions is not established.

**Corollary 9 (persistent support criterion).** A good coherent support through \(e_{[z]}\) remains good after flipping \(e_{[z]}\) if and only if its associated upper-facet full geodesic rooted at \(z\) is monochromatic. In particular, if \(f\) has a rooted monochromatic full geodesic at \(z\), the corresponding support persists regardless of \(g(z)\).

**Proof.** Flipping the orbit changes \(g(z)\) to \(1-g(z)\), keeping \(w_f(z,\pi)\) unchanged. To yield just one change with both endpoint color choices, this facet word must be simultaneously nondecreasing and nonincreasing, hence constant. \(\square\)

The quantitative bridge and per-orbit support counts were checked against full coherent-support enumeration for multiple independent legal colorings in dimensions \(3,4,5\). Certificate:
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/88fc6f19b9974bb4409c0b348bf289b1dd686af3/scripts/nori_quantitative_facet_bridge_verify.py.

**Closure obligation.** Instead of another turn-energy estimate, the direct forcing target is now a sharp **paired-root multiplicity theorem for an arbitrary facet coloring**. The already-known root-existence theorem must be strengthened from one antipodal pair to two, without assuming independent factorization. This produces distinct edge-orbit witnesses in every direction and would make critical flips incapable of destroying all monochromatic geodesics.


#### Affine bad-extension fibres and critical-flip boundary

Fix an arbitrary coloring \(f\) on \(Q_d\), put \(n=d+1\), and let \(\mathcal R\) contain one representative from each complementary pair of facet vertices. There are \(h=2^{d-1}\) such pairs. Set \(u_z=N_f^+(z)\), \(v_z=N_f^+(\bar z)\), and write \(b_z\) for the freely chosen new-direction edge color over \(z\). Theorem 7 gives
\[
\boxed{G_f(b)=\sum_{z\in\mathcal R}[u_z+(v_z-u_z)b_z].}\tag{34}
\]
Here \(G_f(b)\) is the number of good coherent supports, and the bridge bits \(b_z\) are independent.

Partition the root pairs into \(\mathcal D=\{z:u_zv_z>0\}\), \(\mathcal S=\{z:(u_z>0)\oplus(v_z>0)\}\), and \(\mathcal Z=\{z:u_z=v_z=0\}\).

**Theorem 10 (Boolean-face classification).** The set \(\mathcal B_f=\{b:G_f(b)=0\}\) is either empty or an axis-aligned subcube. It is empty if \(P(f)\ne\varnothing\). When \(P(f)=\varnothing\), its bits at \(\mathcal S\) are forced to select the unfavorable orientation, while its bits at \(\mathcal Z\) are free. Consequently
\[
\boxed{|\mathcal B_f|=\begin{cases}0,&P(f)\ne\varnothing,\\2^{2^{d-1}-|A(f)|},&P(f)=\varnothing.\end{cases}}\tag{35}
\]
If nonempty, the bad face has codimension \(|A(f)|\).

**Proof.** Every summand in (34) is nonnegative. Their sum vanishes precisely when all vanish. A pair with \(u_z,v_z>0\) cannot vanish. A singly favorable pair forces one bridge bit, whereas an entirely unfavorable pair imposes no restriction. In the absence of doubly favorable pairs, \(|\mathcal S|=|A(f)|\), which proves (35). \(\square\)

**Theorem 11 (first-flip boundary).** At any bad extension \(b\), flipping a bridge orbit indexed by \(z\) creates good supports if and only if \(z\in\mathcal S\). All resulting good supports use the flipped orbit, and their number is \(\max(u_z,v_z)\). Thus each bad extension has precisely \(|A(f)|\) good neighbors by flips of the newly designated direction. Conversely a good extension becomes bad upon flipping orbit \(z\) precisely when \(P(f)=\varnothing\), \(z\in\mathcal S\), that orbit selects its favorable orientation, and every other singly favorable orbit selects its unfavorable orientation.

**Proof.** Each bridge orbit contributes just one summand to (34). Flipping it changes no other summand. At a bad extension all summands vanish, so the only possible newly positive term is the flipped one. Its alternative value is \(\max(u_z,v_z)\) for \(z\in\mathcal S\), and zero for \(z\in\mathcal Z\). This proves both directions. \(\square\)

**Theorem 12 (fibre distribution).** For uniformly random legal bridge assignments,
\[
\boxed{\mathbb E_b s^{G_f(b)}=\prod_{z\in\mathcal R}\frac{s^{u_z}+s^{v_z}}2,}\tag{36}
\]
and therefore
\[
\boxed{\mathbb E_bG_f=\tfrac12\sum_{z\in Q_d}N_f^+(z),\quad
\operatorname{Var}_b(G_f)=\tfrac14\sum_{z\in\mathcal R}(u_z-v_z)^2.}\tag{37}
\]
**Proof.** The terms in (34) are independent two-valued random variables; multiply their generating functions and take derivatives. \(\square\)

These formulas hold for an arbitrary fixed facet coloring, not a special class. The required cross-direction closure is not supplied: the possibility of one nonempty bad face remains equivalent to the paired-root existence obstruction in the lower dimension.

**Certificate.** Full enumeration of all 4096 arbitrary facet colorings of \(Q_3\) and all sixteen bridge assignments (65,536 legal \(Q_4\) colorings) verifies (34)–(35) and the support counts independently:
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/1145feadeec3041dc85290b869684e5b6edb2c60/scripts/nori_bad_extension_subcube_verify.py.


#### Two-direction implication transport and alternating forcing packets

Fix distinct directions \(i,j\) in \(Q_n\), \(n\ge3\), and fix all antipodally odd edge-orbit colors outside those two direction classes. The remaining \(v=2^{n-1}\) antipodal edge-orbit colors are free Boolean variables \(X_e\), each belonging to direction \(i\) or \(j\). On a specified edge in orbit \(e\), the edge color is \(X_e\oplus s_e\), where the sign \(s_e\) is zero on the selected orbit representative and one on its antipodal mate.

For any rooted full direction-distinct geodesic \(P\), consider its \(n-2\) edges in the already colored directions. If two of these have different colors, no extension makes \(P\) monochromatic. Otherwise let \(t\) be their common color, and denote the remaining two edge orbits by \(e_i,e_j\), with signs \(s_i,s_j\).

**Theorem 13 (unrestricted two-direction 2-SAT theorem).** Form the clause
\[
\boxed{(X_{e_i}\ne t\oplus s_i)\ \lor\ (X_{e_j}\ne t\oplus s_j)}
\tag{38}
\]
for every rooted full geodesic \(P\) whose other \(n-2\) edge colors agree. Let \(\Phi_{ij}\) be the conjunction of these clauses. Then
\[
\boxed{X\models\Phi_{ij}\quad\Longleftrightarrow\quad
\text{the completed legal coloring has no monochromatic full geodesic}.}
\tag{39}
\]
Each clause uses one variable from each of the two direction classes. Thus the bad-extension region for any shared fixed partial coloring is the solution set of a bipartite 2-CNF formula.

**Proof.** The path \(P\) is monochromatic in the completed coloring precisely when the two free edge colors both equal \(t\), meaning \(X_{e_i}=t\oplus s_i\) and \(X_{e_j}=t\oplus s_j\). Clause (38) forbids precisely this simultaneous assignment. A completion is bad precisely when every rooted full geodesic is nonmonochromatic, which is the conjunction (39). The two free edges belong to different direction classes, so their variables are distinct and the formula is bipartite. Every omitted antipodal image path yields the same clause because all its edge colors complement simultaneously. \(\square\)

**Theorem 14 (two-direction Boolean-majority closure).** For a fixed coloring outside directions \(i,j\), let \(\mathcal B_{ij}\) be its family of bad completions. For any \(X,Y,Z\in\mathcal B_{ij}\), their componentwise majority also belongs to \(\mathcal B_{ij}\):
\[
\boxed{\operatorname{maj}(X,Y,Z)\in\mathcal B_{ij}.}
\tag{40}
\]
This is a compatibility law involving both free direction classes in one original partial coloring. It extends the single-direction affine-face property from Theorem 10.

**Proof.** Consider any binary clause \(L\lor M\) satisfied by three assignments. If their componentwise majority made both clauses' terms false, each of the two terms would be false in at least two of the three assignments. These two groups of cardinality at least two must intersect, producing one assignment that makes both terms false. This contradicts its assumed satisfaction. Every clause, and hence their conjunction, is therefore preserved by majority. \(\square\)

##### Contradictory alternating geodesic packets

A clause forbidding \(X_a=p,X_b=q\) yields the two contrapositive implications
\[
(X_a=p)\Rightarrow(X_b=1-q),
\qquad
(X_b=q)\Rightarrow(X_a=1-p).
\tag{41}
\]
The implication graph has \(2v\) signed states \((e,0),(e,1)\). Every arc moves between the two direction classes, and an arc \(u\to w\) is accompanied by the reversed complemented arc \(\bar w\to\bar u\). Each arc is certified by a rooted full geodesic whose already colored \(n-2\) edges all have one color.

**Theorem 15 (alternating implication-cycle forcing).** For any fixed partial coloring outside directions \(i,j\), the following are equivalent:

(a) Every legal completion in the two free direction classes has a monochromatic full geodesic.

(b) A strongly connected component of the bipartite implication graph contains both signed states \((e,0),(e,1)\) of one edge orbit.

(c) There are two directed alternating implication paths, one from \((e,0)\) to \((e,1)\) and another in the reverse direction.

When these hold, a packet of at most
\[
\boxed{4v-4=2^{n+1}-4}
\tag{42}
\]
rooted full geodesics suffices to force a monochromatic full geodesic **for every assignment of the two free direction classes**. Given any completed coloring, a violated clause identifies one such monochromatic geodesic.

**Proof.** Theorem 13 identifies bad completions with satisfying assignments of a binary CNF. The standard implication-graph criterion says this CNF is inconsistent precisely when one strongly connected component contains both signed states of a variable. This is equivalent to having paths in both directions, proving (a)--(c). Choose simple paths in each direction. Each begins and ends on the same side of the bipartite implication graph, so its arc count is even and no more than \(2v-2\). Their union contains no more than \(4v-4\) arcs, each contributed by a clause and therefore by a rooted full geodesic. This smaller clause set already contradicts both possible values of \(X_e\), so in every assignment some included clause fails. Its associated full geodesic has all the prescribed edges in one color and both free edges matching it, hence is monochromatic. \(\square\)

This is a dimension-uniform constructive forcing mechanism **conditional on an alternating implication-cycle certificate** in the shared partial coloring. The unresolved unrestricted challenge is to establish such certificates for every assignment of the other \(n-2\) direction classes. A satisfiable instance would produce a legal NORI1 counterexample by assigning its remaining two classes accordingly.

**Finite verification.** For \(n=4\), exhaustive computation over the \(256\) possible partial colorings outside two chosen free directions confirms that every resulting 2-CNF is inconsistent. The equivalence between its clauses and full monochromatic geodesics was checked independently for all \(65,536\) legal \(Q_4\) colorings. Greedily reduced inconsistent clause packets have sizes from four to eleven in an independently verified elimination run. Samples in \(Q_5\) and \(Q_6\) also yielded contradictory packets, but cannot establish an all-dimensional existence theorem. Reproducible verifier:
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/ce8c86fcfe8ea07cec1d591457bd170c00fae7f5/scripts/nori_two_direction_implication_verify.py.

**Next closure target.** Prove that the near-monochromatic complete paths associated with an arbitrary shared partial coloring necessarily create two opposing alternating implication paths between the states of at least one free edge orbit. That would force a full monochromatic geodesic in every completion, with a certificate using exponentially rather than factorially many complete paths.


#### An all-dimensional four-path forcing packet with two free directions

The alternating implication theorem has a particularly short constructive instance that persists under arbitrarily many extra directions. It proves an explicit robust completion theorem, rather than claiming that every partial coloring has such a small packet.

Index the dimensions by \(0,1,\ldots,n-1\), \(n\ge4\). Put \(K=(4,5,\ldots,n-1)\), in this order, and \(M_K=\sum_{k\in K}2^k\). For a cube vertex \(x\), let \(\xi=x\bmod16\) encode its first four bits. Define the colors of all edges in directions other than \(0,1\) by
\[
\boxed{
c_2(x)=x_3,\qquad
c_3(x)=x_2,\qquad
c_k(x)=x_0\oplus\mathbf1_{\{\xi\in\{3,12\}\}}
\quad(k\ge4).
}
\tag{43}
\]
Here \(x_t\) denotes the bit of \(x\) in dimension \(t\). Each rule is independent of its own direction bit. The set \(\{3,12\}\) is invariant under complementing the first four bits, so all these rules reverse color under full antipodality. Assign the colors of every direction-\(0\) and direction-\(1\) edge orbit arbitrarily, subject only to legal antipodal oddness.

For a starting vertex \(r\) and an order \(\pi\), denote the rooted full geodesic by \(P(r;\pi)\). Consider the four paths in the following table, where writing \(K\) means inserting every member of \(K\) in its displayed order.

| Label | Root | Direction order | Color of all edges in directions \(2,\ldots,n-1\) |
|---|---|---|---|
| \(P_{00}\) | \(4+M_K\) | \(K,1,0,2,3\) | \(0\) |
| \(P_{11}\) | \(4\) | \(1,0,K,3,2\) | \(1\) |
| \(P_{01}\) | \(6\) | \(0,2,K,3,1\) | \(0\) |
| \(P_{10}\) | \(6\) | \(0,3,K,2,1\) | \(1\) |

**Theorem 16 (uniform four-geodesic forcing packet).** The four paths above always include a monochromatic full antipodal geodesic, regardless of how the remaining two entire direction classes are legally colored. More precisely, let \(a\) be the color of the direction-\(0\) edge orbit through lower endpoint \(6\), with every added bit zero, and let \(b\) be the color of the direction-\(1\) edge orbit through lower endpoint \(4\), with every added bit zero. Then
\[
\boxed{\text{the path }P_{ab}\text{ is monochromatic}.}
\tag{44}
\]
In particular this packet uses just four predetermined full geodesics for every \(n\ge4\).

**Proof.** The table's fixed-direction entries follow directly from (43). At directions \(2,3\), the respective edge colors of the four paths are \(00,11,00,11\). For each added direction \(k\in K\), the path traverses \(k\) while the first four vertex bits equal respectively \(4,7,3,15\). Formula (43) takes respectively the values \(0,1,0,1\) at these four states, giving the displayed uniform fixed-edge colors.

At every direction-\(0\) step, the current vertex lies in the orbit whose lower endpoint has first-four-bit mask \(6\) and all added bits zero, so its edge color is \(a\). At the direction-\(1\) step, \(P_{00}\) and \(P_{11}\) use the edge with lower endpoint mask \(4\) and all added bits zero, of color \(b\); \(P_{01}\) and \(P_{10}\) use its full antipodal mate, of color \(1-b\). Thus the four paths' two free-edge colors are respectively
\[
(a,b),\qquad(a,b),\qquad(a,1-b),\qquad(a,1-b).
\]
Together with the fixed colors in the table, this shows:
\[
P_{00}\text{ is monochromatic if }(a,b)=(0,0),\quad
P_{11}\text{ if }(a,b)=(1,1),
\]
\[
P_{01}\text{ if }(a,b)=(0,1),\quad
P_{10}\text{ if }(a,b)=(1,0).
\]
These are the four possible assignments, proving (44). \(\square\)

**Robustness.** The proof only uses the colors of the fixed-direction edges lying on these four full paths. There are at most \(4(n-2)\) such antipodal orbit constraints, out of \((n-2)2^{n-2}\) orbit variables in the fixed directions. Therefore at least
\[
\boxed{(n-2)(2^{n-2}-4)}
\tag{45}
\]
other fixed-direction orbit colors may be changed independently without losing the forcing packet, in addition to the entirely free direction-\(0\) and direction-\(1\) orbit colors. This creates a large cylinder of original legal colorings carrying the same short forcing certificate.

The packet is an illustration of a dimension-uniform **positive witness mechanism** arising from two-direction square and antipodal transport. It does not assert that four-clause packets exist in every partial coloring; indeed some four-cube partial colorings need longer implication certificates. In general, Theorem 15's alternating forcing packet, rather than this special four-path packet, remains the closure target.

**Independent certificate:** The stated four paths, their fixed colors, shared free orbit identities, antipodal signs and selection rule (44) were checked by direct integer-bit path traversal for \(4\le n\le10\):
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/4209fc1a341bd6a203fa67634aed713145bfb4c1/scripts/nori_four_path_packet_verify.py.


#### Complete geometry of two prescribed edge orbits

The two-direction implication formulation has no geometric absences between edge-orbit variables. Indeed their incidence can be counted by a factorial formula.

Let \(e_i\) and \(e_j\) be antipodal edge orbits in different dimensions \(i\ne j\). Choose the representative \(\{x,x+e_i\}\) of \(e_i\) with \(x_i=0\). Choose the representative \(\{y,y+e_j\}\) of \(e_j\) whose two endpoints have \(i\)-th bit equal to one. Let
\[
S=\{k\notin\{i,j\}:x_k\ne y_k\},\qquad s=|S|.
\]

**Theorem 17 (two-edge factorial incidence).** The number of coherent projective full-geodesic supports containing both prescribed antipodal edge orbits is
\[
\boxed{N(e_i,e_j)=s!(n-2-s)!.}
\tag{46}
\]
Consequently every prescribed pair of different-direction edge orbits belongs to at least one common coherent full geodesic. Moreover, for a support chosen uniformly subject to containing \(e_i\),
\[
\boxed{
\Pr(e_j\in O\mid e_i\in O)=
\frac{1}{(n-1)\binom{n-2}s}.
}
\tag{47}
\]

**Proof.** Every support through \(e_i\) has a unique oriented representation beginning with \(x\to x+e_i\), followed by a permutation of the other \(n-1\) dimensions. In such a representation, the \(i\)-bit is one at the step in dimension \(j\). That step lies in \(e_j\) precisely when the set of dimensions used after \(i\) but before \(j\) is \(S\). Its elements may be ordered in \(s!\) ways; the dimensions remaining after \(j\) may be ordered in \((n-2-s)!\) ways. Every such ordering yields one support, proving (46). Since there are \((n-1)!\) supports through \(e_i\), division gives (47). \(\square\)

Thus any absent implication between two free edge-orbit variables is forced by the **mixed colors of already fixed edges** along all their connecting full geodesics, not by lack of a dimension-distinct path. This distinguishes combinatorial geometry from the still-open color-compatibility step. Exhaustive anchored-support checks of (46) were carried out through \(Q_8\).

#### Paired-bridge forks: a four-geodesic forcing lemma

Recall the two-direction setup: edge-orbit bits in directions \(i,j\) are free while all other edge colors are fixed. Let \(X_e\) encode one chosen direction-\(i\) edge orbit \(e\).

Call a pair of rooted full geodesics a *color-\(t\) fork at \(e\)* if: (a) every edge outside \(i,j\) on each path has fixed color \(t\); (b) both paths traverse the same selected member of orbit \(e\) in direction \(i\), whose color is \(X_e\); and (c) their direction-\(j\) edges are antipodal mates of one common direction-\(j\) edge orbit. Condition (c) means that the two \(j\)-edge colors are complementary under every legal assignment.

**Theorem 18 (opposite-color fork forcing).** If the same direction-\(i\) orbit \(e\) admits both a color-zero fork and a color-one fork, then every legal completion of the two free direction classes has a monochromatic full antipodal geodesic among the four fork paths.

**Proof.** If \(X_e=0\), inspect the color-zero fork. Its fixed-direction edges and both chosen direction-\(i\) edges have color zero. Its two direction-\(j\) edges are antipodal mates, and therefore one has color zero. The corresponding rooted full path is monochromatic. If \(X_e=1\), the identical argument applies to the color-one fork. \(\square\)

This is a certificate criterion inside an arbitrary fixed partial coloring. It does not assert that every partial coloring admits a pair of forks.

#### A uniform cross-square packet with just three free orbit variables

The fork criterion has a particularly simple realization in every \(n\ge4\). Index directions \(0,1,\dots,n-1\), put \(K=(3,4,\ldots,n-1)\), and fix
\[
\boxed{c_2(x)=1+x_0,\qquad c_k(x)=x_0\ \ (k\ge3)}
\quad\text{over }\mathbb F_2.
\tag{48}
\]
These fixed-direction edge colors satisfy undirectedness and antipodal oddness. Every edge orbit in directions \(0,1\) may be colored freely subject to antipodal oddness.

Let \(A\) denote the color of the direction-zero orbit with lower endpoint \(0\). Let \(B,C\) denote the colors of the two direction-one orbits with lower endpoints \(4\) and \(5\), respectively. These three orbit bits are independent.

| Root | Full direction order | Fixed-edge color | Free-edge colors |
|---|---|---|---|
| \(7\) | \((1,2,0,K)\) | \(0\) | \(A,C\) |
| \(5\) | \((2,0,K,1)\) | \(0\) | \(A,1-C\) |
| \(4\) | \((2,0,K,1)\) | \(1\) | \(A,1-B\) |
| \(6\) | \((1,2,0,K)\) | \(1\) | \(A,B\) |

**Theorem 19 (dimension-uniform cross-square four-path packet).** For every \(n\ge4\) and every legal assignment of the entire two free direction classes, at least one of these four rooted full geodesics is monochromatic.

**Proof.** The entries in the table follow from (48) by tracing the vertices along each direction order. The direction-zero edges all represent the same edge orbit \(A\). The first two paths' direction-one edges represent antipodal mates of orbit \(C\), and the last two paths' direction-one edges represent antipodal mates of orbit \(B\). If \(A=0\), either \(C=0\) or \(1-C=0\), so one of the first two paths is monochromatic zero. If \(A=1\), either \(B=1\) or \(1-B=1\), so one of the last two paths is monochromatic one. \(\square\)

The three distinguished free orbits lie in two different projective squares of the \((0,1)\)-direction square system: the direction-zero orbit lies above the class of the all-zero remaining-direction state, whereas \(B,C\) lie above the class with direction \(2\) toggled. This is a **cross-square** forcing certificate; it cannot be confined to a single projective square.

The union of these four paths uses only \(2(n-2)\) antipodal edge orbits among the \((n-2)2^{n-2}\) already colored orbits. The other
\[
\boxed{(n-2)(2^{n-2}-2)}
\tag{49}
\]
fixed-direction orbit colors may be changed arbitrarily, and the same forcing conclusion holds. This proves a robust all-dimensional forcing cylinder with no conditions on the rest of the coloring.

A separate direct traversal audit checked (48), all four path orders, all eight assignments of \(A,B,C\), and the orbit count through dimension twelve. Reproducible certificate:
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/ae7850fe1c8a28edf4d960c0ee31bcc5de49ef46/scripts/nori_two_square_fork_packet_verify.py.

#### Universal two-square forcing in five dimensions: finite certificate

Fix free directions \(0,1\) in \(Q_5\); their \(16\) edge-orbit variables split into four disjoint projective-square blocks of four variables each. For an arbitrary legal coloring of the other three direction classes, restrict the bipartite 2-CNF \(\Phi_{0,1}\) of Theorem 13 to clauses whose two free variables lie in the union of a prescribed pair of square blocks.

**Computational Proposition 20.** Every coloring of the other three direction classes in \(Q_5\) has at least one pair of projective-square blocks whose restricted 2-CNF is inconsistent.

**Verification method.** To seek a counterexample, choose the \(24\) remaining fixed edge-orbit bits and, independently for each of the six pairs of projective squares, choose the eight free orbit bits in that pair's union. This gives \(24+6\cdot8=72\) binary variables. Require every rooted full geodesic whose two free orbits belong to one chosen block pair to be nonmonochromatic under that pair's independent assignment. For each such geodesic with colored edge bits \(d_1,\ldots,d_5\), impose the linear inequality \(1\le d_1+\cdots+d_5\le4\), with all edge colors affine in the relevant independent orbit bits. There are 3840 linear path constraints before row duplication reductions.

The resulting feasibility model is logically equivalent to the existence of a fixed three-direction coloring for which **all six** two-square induced 2-CNF instances are satisfiable. SciPy/HiGHS 1.8.0 reported **infeasible** after 1859 branch-and-bound nodes and 37880 LP iterations. Therefore the proposition is established by this computational audit, not by an independent handwritten infeasibility certificate. Verifier:
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/4f8faeae42a6e8fd709c874eba3d30eeb5922732/scripts/nori_two_square_q5_milp.py.

The proposition is stronger than the known five-dimensional NORI1 existence statement: after the fixed colors are chosen, **at most eight free orbit variables**, lying on two projective squares, suffice to force a full monochromatic geodesic. Theorem 15 then gives a certificate of at most \(28\) rooted full geodesics for that fixed partial coloring.

The proof obligations in higher dimensions remain open. The positive all-dimensional fork mechanism above demonstrates how cross-square transport can force a geodesic even when all single-square implication formulas admit satisfying assignments; no unrestricted theorem currently forces such a packet for an arbitrary fixed coloring.


#### The square-locality dichotomy and the necessity of cross-square transport

The preceding cross-square forcing example has a stronger structural explanation that holds in every dimension and for an arbitrary fixed partial coloring.

Fix free directions \(i,j\), let \(R=[n]\setminus\{i,j\}\), and consider an antipodal pair \(\Sigma=\{F_r,F_{\bar r}\}\) of two-dimensional \((i,j)\)-faces, indexed by a complementary pair of \(R\)-bit states \(r,\bar r\). Its four projective edge orbits—two of direction \(i\), two of direction \(j\)—form one *square block* of the two-direction Boolean variables. Let \(\Phi_{\Sigma}\) be the subformula of the full bipartite 2-CNF whose two variables both belong to this block.

**Lemma 21 (same-square path dichotomy).** Let \(P\) be any full dimension-distinct geodesic whose unique \(i\)-step and \(j\)-step belong to the same square block \(\Sigma\). Then precisely one of the following holds:

(a) the \(i\)-step and \(j\)-step are consecutive in the direction order;

(b) the \(i\)-step and \(j\)-step are the first and last steps, in either order, and the \(n-2\) intervening steps traverse every member of \(R\).

**Proof.** Project the path onto its \(R\)-bit state. At an \(i\)-edge or \(j\)-edge the \(R\)-state does not change. The two free edges belong to the same projective square block precisely when these two \(R\)-states are equal or complementary. Between the two free edges the path flips a subset \(S\subseteq R\), each direction at most once. If the states are equal, \(S=\varnothing\), so the free steps are consecutive. If complementary, \(S=R\), so all fixed-direction steps lie between them. Since there are no other free steps, they occupy the ends of the order. \(\square\)

**Theorem 22 (square-local forcing requires a monochromatic fixed facet).** If the square-block subformula \(\Phi_{\Sigma}\) is inconsistent, then among the four \((n-2)\)-dimensional faces obtained by fixing the \(i,j\) bits, at least one has a monochromatic full \(R\)-geodesic joining the two \(R\)-vertices \(r,\bar r\).

**Proof.** Suppose no such fixed-face full geodesic exists. For any rooted full path whose free edge orbits both belong to \(\Sigma\), Lemma 21 gives two possibilities. In case (b), its intervening fixed-direction edges cannot all have the same color, by assumption, so the path contributes no clause to \(\Phi_\Sigma\). Every clause therefore comes from case (a). Choose the four free orbit bits in block \(\Sigma\) so that, in the face \(F_r\), both direction-\(i\) edges have color zero and both direction-\(j\) edges have color one. Antipodal oddness forces their mates in \(F_{\bar r}\) to have the opposite colors, still different between directions. Consequently every case-(a) path has its two consecutive free edges in different colors and cannot be monochromatic. This assignment satisfies every clause of \(\Phi_\Sigma\), contradicting inconsistency. \(\square\)

**Corollary 23 (a rigorous cross-square necessity criterion).** If the prescribed fixed-direction colors admit no monochromatic full \(R\)-geodesic in any of the four \((i,j)\)-bit faces, then **every** individual projective-square block subformula is satisfiable. Any contradiction in the full two-direction 2-CNF must involve variables from at least two different projective square blocks.

**Proof.** Apply Theorem 22 to every \(\Sigma\). Each single-block formula is satisfiable. An inconsistent full formula therefore cannot be certified by clauses entirely supported on one block. \(\square\)

For the affine fixed-direction coloring of Theorem 19,
\[
c_2(x)=1+x_0,\qquad c_k(x)=x_0\quad(k\ge3),
\]
each \((i,j)=(0,1)\)-bit face fixes \(x_0\). Its direction-two edges therefore have the opposite color from every direction \(k\ge3\). Because \(n\ge4\), both types occur. Consequently no full \(R\)-geodesic in any such face is monochromatic. Corollary 23 proves, without computation and in **all dimensions**, that every individual square-block subformula is satisfiable. Yet the four paths of Theorem 19 force a contradiction using just three free orbit variables drawn from two square blocks.

This proves a dimension-uniform positive distinction: there are robust legal partial colorings for which **cross-square implication transport is mathematically necessary** for the forcing certificate, and an explicit four-path packet completes that transport. It also identifies precisely where a purely face-local strategy must fail. The remaining task is to force some form of cross-square transport for an arbitrary partial coloring, rather than imposing a universal local-square contradiction.


#### Two-stage geodesic resolution and signed holonomy on one free direction

This continues the two-direction implication programme with a forcing certificate that transports constraints across several edge orbits rather than relying on a four-clause packet for one edge-orbit pair.

Fix directions \(i\ne j\) and all edge-orbit colors in the other \(n-2\) directions. Let \(X_e\) denote a free direction-\(i\) orbit bit and \(Y_f\) a free direction-\(j\) orbit bit. Theorem 13 associates to each near-monochromatic rooted full geodesic a forbidden assignment
\[
(X_e=p,\ Y_f=q)
\quad\Longleftrightarrow\quad
(X_e\ne p)\lor(Y_f\ne q).
\tag{50}
\]
The fixed partial coloring decides which such clauses are present.

**Theorem 24 (elimination by paired geodesics).** For each direction-\(i\) orbit \(e\), and for every two clauses
\[
(X_e\ne0)\lor(Y_f\ne q),\qquad
(X_e\ne1)\lor(Y_g\ne r),
\]
form the clause
\[
\boxed{(Y_f\ne q)\lor(Y_g\ne r).}
\tag{51}
\]
Let \(\Psi_j\) be the conjunction of all clauses (51), for every eliminated orbit \(e\). Clauses with \(f=g,q\ne r\) impose no restriction and may be discarded; if \(f=g,q=r\), (51) becomes the unit requirement \(Y_f\ne q\). Then
\[
\boxed{\Phi_{ij}\text{ satisfiable}\quad\Longleftrightarrow\quad
\Psi_j\text{ satisfiable}.}
\tag{52}
\]
Every clause of \(\Psi_j\) is certified by two full geodesics whose direction-\(i\) edges lie in the same antipodal orbit but whose prescribed colors there are opposite. The remaining direction-\(j\) orbits \(f,g\) may belong to different projective-square blocks.

**Proof.** If both \(Y_f=q\) and \(Y_g=r\) hold, the first original clause requires \(X_e=1\) and the second requires \(X_e=0\), an impossibility. Therefore every satisfying assignment of the original clauses obeys (51). Conversely, suppose an assignment of all \(Y\)-bits satisfies all the clauses (51), but for some \(e\) neither value of \(X_e\) satisfies the original clauses involving \(e\). There is then a violated clause under \(X_e=0\), having the form of the first displayed clause with \(Y_f=q\), and another violated clause under \(X_e=1\), with \(Y_g=r\). Their resolvent (51) is false, a contradiction. Thus every eliminated bit \(X_e\) admits at least one legal choice. These choices are independent once the \(Y\)-bits are fixed, so they produce a satisfying assignment of \(\Phi_{ij}\). \(\square\)

Theorem 24 is a projection of the full two-direction bad-extension region onto **one** free direction class. It preserves satisfiability without independent changes to the already colored dimensions. Its clauses have the geometric meaning of two near-monochromatic full geodesics passing through a common orbit, requiring opposite colors at that orbit.

**Theorem 25 (parity-holonomy forcing packets).** Suppose the resolved clauses (51) contain both
\[
(Y_f\ne0)\lor(Y_g\ne1),
\qquad
(Y_f\ne1)\lor(Y_g\ne0).
\]
Then every hypothetical bad completion satisfies \(Y_f=Y_g\). If instead the clauses include
\[
(Y_f\ne0)\lor(Y_g\ne0),
\qquad
(Y_f\ne1)\lor(Y_g\ne1),
\]
then every hypothetical bad completion satisfies \(Y_f\ne Y_g\).

Construct a signed multigraph on the direction-\(j\) edge orbits, placing an edge labeled \(\sigma\in\mathbb F_2\) whenever the resolved clauses enforce
\[
Y_f\oplus Y_g=\sigma.
\tag{53}
\]
If this multigraph contains a closed walk whose edge labels sum to one, then every completion contains a monochromatic full antipodal geodesic. A parity-inconsistent cycle of length \(\ell\) gives a certificate involving at most \(4\ell\) full geodesics. In particular, two parallel edges demanding opposite parities give a forcing certificate with at most eight geodesics.

**Proof.** The first two clauses rule out the assignments \((0,1),(1,0)\); the second pair rules out \((0,0),(1,1)\), giving the respective XOR constraints. Along a closed walk, XOR the enforced differences of successive \(Y\)-bits. The vertex terms cancel, leaving zero on the left. If the edge labels sum to one, this is impossible. Each XOR constraint uses two resolved clauses, and each resolved clause arises from two full geodesics by Theorem 24. Therefore \(\ell\) edges require at most \(4\ell\) geodesics; the unsatisfiability argument guarantees at least one is monochromatic in every completion. \(\square\)

This provides a constructive **transport-and-holonomy mechanism** in the original coloring: two full geodesics transport a constraint between free orbits in direction \(j\), and a parity-inconsistent network of such transports forces a monochromatic full geodesic. The unconditional existence of a parity-inconsistent cycle remains unproved in arbitrary dimensions; the general 2-SAT contradiction may instead arise from implication chains not reducible to pairwise XOR constraints.

#### A six-geodesic forcing packet with no four-clause orbit pair

In \(Q_5\), fix free directions \(0,1\) and order the 24 already-colored antipodal edge orbits by direction \(2,3,4\), then by their canonical smaller lower endpoint. Give them the color bits of the 24-bit hexadecimal mask
\[
\boxed{\texttt{0xce337b}.}
\]
In the ordered list of 16 free edge orbits, denote bits \(X_0,X_1\) from direction zero and \(Y_0,Y_1\) from direction one. The six full geodesics below have all three fixed-direction edges of the indicated common color. Their free-edge colors must therefore avoid the forbidden assignments in the last column of any hypothetical bad completion.

| Root | Direction order | Fixed color | Forbidden assignment |
|---|---|---|---|
| \(1\) | \(0,1,2,3,4\) | \(0\) | \(X_0=0,\ Y_0=0\) |
| \(15\) | \(2,3,1,0,4\) | \(0\) | \(X_0=0,\ Y_1=0\) |
| \(0\) | \(0,4,3,2,1\) | \(1\) | \(X_0=1,\ Y_0=0\) |
| \(2\) | \(1,0,4,3,2\) | \(1\) | \(X_0=1,\ Y_0=1\) |
| \(3\) | \(0,2,3,4,1\) | \(0\) | \(X_1=0,\ Y_1=1\) |
| \(8\) | \(3,1,0,2,4\) | \(1\) | \(X_1=1,\ Y_0=1\) |

**Proposition 26 (six-path transport certificate).** For this fixed partial coloring, every legal assignment of the two free direction classes makes one of the six displayed full geodesics monochromatic. Yet no *single pair* consisting of a direction-zero orbit and a direction-one orbit admits clauses forbidding all four assignments. Thus a single-pair four-clause contradiction is unavailable, while paired-geodesic resolution forces a contradiction across multiple free orbits.

**Proof.** If \(X_0=1\), the third and fourth paths force \(Y_0=1\) and \(Y_0=0\), respectively, unless one is monochromatic. Thus any hypothetical bad completion has \(X_0=0\). The first and second paths then force \(Y_0=Y_1=1\). The fifth path requires \(X_1=1\), while the sixth requires \(X_1=0\), a contradiction. The claimed absence of a full four-clause orbit pair was independently checked by constructing every eligible rooted full path in this partial coloring and finding at most three forbidden assignments for any individual orbit pair. The six-path certificate is irredundant: deleting any one of its six clauses leaves a satisfying assignment of the four displayed free bits. \(\square\)

The six displayed paths were checked directly against all sixteen assignments of \(X_0,X_1,Y_0,Y_1\), and the fixed-edge color requirements were checked from the stated mask. This shows that the path-pair transport framework can force a monochromatic full geodesic in a case where no individual two-orbit four-clause certificate exists.

**Finite all-context audit.** For every one of the 256 assignments of the fixed-direction orbit colors in \(Q_4\), elimination of direction-zero variables produces direction-one XOR constraints demanding opposite parities on at least one pair of direction-one edge orbits. Thus Theorem 25 alone supplies a forcing certificate for all those partial colorings. Sampled partial colorings in dimensions five and six likewise exhibited an opposite-parity pair, but the existence of this stronger packet in all dimensions is unresolved.

**Verifier:** https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/028d1f475fcef9cb27d9700809ef531fe86cf51d/scripts/nori_two_direction_resolution_holonomy_verify.py.

##### Proof-closure direction

The all-dimensional problem can now be sharpened beyond searching for arbitrary contradictory 2-SAT formulas: investigate whether the projective geometry and antipodal color-reversal law always produce a nontrivial parity-holonomy cycle in the resolved direction-one orbit graph. This is stronger than NORI1, and it may fail; in that case a satisfiable parity system together with an inconsistent general 2-SAT instance would identify the extra non-parity forcing that a final proof must accommodate. The theorem and its seven-path certificate establish a rigorous mechanism, not its universal occurrence.


#### Parity-holonomy stress tests and limits

Theorem 25 gives a strictly stronger sufficient certificate than general two-direction 2-SAT inconsistency, so its universal validity cannot be assumed.

**Exhaustive affine Q5 audit.** Keep dimensions \(0,1\) free. In each of the three fixed directions \(k=2,3,4\), prescribe an arbitrary affine legal color rule
\[
c_k(x)=b_k+\sum_{\substack{j\ne k\\j\in[n]}}a_{kj}x_j,\qquad
\sum_{j\ne k}a_{kj}=1\pmod2 .
\]
There are sixteen independent choices for each fixed row, hence \(16^3=4096\) legal affine partial colorings. For every one of these 4096 choices, the two-stage resolution of Theorem 24 contains a pair of direction-one edge orbits forced to satisfy **both** equal and unequal parity. Therefore the eight-path forcing criterion of Theorem 25 succeeds throughout this entire affine five-dimensional family.

The number of direction-one orbit pairs carrying both parity requirements ranges from four to twenty-eight; all cases were enumerated. The independently checked histogram by number of contradictory pairs is
\[
\begin{array}{c|rrrrrrrr}
\#\text{pairs}&4&6&8&9&10&12&14&15\\
\#\text{partial colorings}&32&180&204&8&24&348&216&24
\end{array}
\]
\[
\begin{array}{c|rrrrrrrr}
\#\text{pairs}&16&20&21&22&24&26&27&28\\
\#\text{partial colorings}&888&24&48&84&456&360&48&1152 .
\end{array}
\]
The entries total 4096. This is a finite computational theorem about the stated affine family, not an all-dimensional statement about arbitrary partial colorings. The exhaustive routine is included in the updated verifier:
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/baffc758042950c000cdf8a9c167efd9c3250dac/scripts/nori_two_direction_resolution_holonomy_verify.py.

**Counterexample to universal forcing on each prescribed pair of square blocks.** In \(Q_6\), there are eight projective \((0,1)\)-square blocks. Number them by increasing tuples of their four associated free orbit-variable indices. For the pair of square blocks indexed \(0,1\), the partial coloring of fixed-direction orbits with 64-bit bitmask
\[
\texttt{0x99109910ef268000}
\]
has a satisfiable two-square-restricted 2-CNF. The orbit-bit order is by direction \(2,3,4,5\), then by increasing canonical lower endpoint. A direct binary integer feasibility model found an assignment of the eight free orbit bits satisfying every clause internal to that pair; an independent implication-graph check confirmed satisfiability. Thus it is false that **every** pair of projective-square blocks must independently force a monochromatic geodesic. The still-open two-square question asks instead whether **some** pair forces one for every partial coloring.

These two stress tests sharpen the next decision: pursue a proof of unavoidable parity holonomy only after controlling nonlinear partial colorings, and avoid the disproved universal assertion about arbitrary square pairs. Theorem 25 is a sufficient color-consistency mechanism, not a theorem claiming that its certificate must always exist.


#### Exhaustive five-cube parity-holonomy multiplicity and extremal classification

This section strengthens the finite evidence for the two-stage geodesic-resolution programme. The result is a **complete finite computation**, not a dimension-uniform proof of NORI1. It concerns every antipodally odd partial edge coloring of \(Q_5\) after leaving two fixed direction classes uncolored, including nonlinear rules.

Fix free directions \(0,1\). The three prescribed direction classes \(2,3,4\) contain \(3\cdot2^{5-2}=24\) independent antipodal edge-orbit color bits. Hence there are \(2^{24}=16,777,216\) possible partial colorings. Each free direction has eight edge-orbit variables. Apply the projective geodesic clause construction of Theorem 13 and eliminate all eight direction-zero variables by Theorem 24. For every unordered pair \(f,g\) of distinct direction-one orbits, let \(R_{fg}\subseteq\mathbb F_2^2\) be the set of ordered assignments \((p,q)\) forbidden by the resulting binary clauses \((Y_f\ne p)\lor(Y_g\ne q)\). Define the parity-diamond count
\[
D(c)=\#\{\{f,g\}:f\ne g,\ R_{fg}=\mathbb F_2^2\}.
\tag{54}
\]
Such a pair demands simultaneously \(Y_f=Y_g\) and \(Y_f\ne Y_g\), so by Theorems 24–25 it is a valid forcing certificate using at most eight rooted full geodesics.

**Computational Theorem 27 (universal four-diamond multiplicity in \(Q_5\)).** Every legal partial coloring of \(Q_5\), with arbitrary fixed colors in directions \(2,3,4\), satisfies
\[
\boxed{4\le D(c)\le28.}
\tag{55}
\]
Both inequalities are attained. Among all \(16,777,216\) partial colorings, precisely \(104\) have \(D(c)=4\). Consequently **each** five-dimensional two-direction partial coloring has at least four distinct contradictory parity-orbit pairs, each yielding a forcing packet of at most eight full geodesics. All remaining two-direction orbit colors may be assigned arbitrarily; one of the packet paths is monochromatic.

**Finite verification.** The self-contained C++17 verifier builds all \(16\cdot5!=1920\) rooted projective full geodesics, identifies their orbit-color indices and antipodal signs, and generates the \(1920\) distinct three-fixed-edge patterns for the two-direction clause system. For each of the \(2^{24}\) fixed-color masks, it checks the applicable patterns, forms all binary clauses, resolves the eight direction-zero variables, and counts the direction-one pairs for which all four forbidden assignments occur. The complete census has minimum four, maximum twenty-eight, with 104 minimizers. The histogram totals \(2^{24}\) assignments; its first nonempty entries are
\[
\begin{array}{c|rrrrrrrr}
D&4&6&8&9&10&11&12&13\\\hline
\#c&104&3156&4500&744&7704&8928&35884&33232
\end{array}
\]
and the highest entry is \(D=28\) with \(3,106,200\) colorings. No values \(D=0,1,2,3,5,7\) occur. The C++ verifier enforces the total count and minimum count as runtime assertions. A second Python implementation independently regenerates full geodesic path clauses and the two-step resolutions for all 104 minimizers.

Source:
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/5ef8fa6bd14726dc6ae0dc9647c5cf175875ae64/scripts/nori_q5_parity_census.cpp

Compile with \`g++ -O3 -std=c++17 -fopenmp nori_q5_parity_census.cpp -o census\` and run \`OMP_NUM_THREADS=5 ./census\`. The OpenMP implementation is parallel only for speed; the combinatorial procedure and outputs are deterministic.

**Computational Theorem 28 (five extremal symmetry classes).** Consider the group generated by translating cube vertices, permuting directions \(2,3,4\) while leaving directions \(0,1\) fixed, and complementing all edge colors. These operations preserve \(D(c)\). The 104 minimizers split into five orbits under this group:

| Number of minimizers | Representative fixed-orbit mask |
|---:|---|
| 48 | \(\texttt{0x000057}\) |
| 24 | \(\texttt{0x00005f}\) |
| 24 | \(\texttt{0x000055}\) |
| 6 | \(\texttt{0x5555aa}\) |
| 2 | \(\texttt{0x555555}\) |

The orbit-color indexing is by direction \(2,3,4\), then increasing canonical lower endpoint of each antipodal edge orbit, with bit zero in direction \(i\). An independent Python symmetry-classifier verifies that each orbit lies entirely among the 104 minimizers and that their five sizes total 104. It also reconstructs the parity-diamond graph for every minimizer, whose vertices are the eight direction-one orbits and whose edges are the four contradictory pairs. Precisely **96 minimizers** have a four-cycle on four vertices; the remaining **8 minimizers** have a perfect matching on all eight vertices. Thus every extremal partial coloring possesses at least two vertex-disjoint contradictory parity pairs.

Symmetry and independent parity-resolution verifier:
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/bc8056c0c830cb90d96959e03a5ac04c6adef2dd/scripts/nori_q5_parity_symmetry.py

This gives a more informative finite forcing result than a bare five-cube NORI1 computation: the *same arbitrary fixed edge assignment* already forces multiple separate short implication certificates, and the sparsest certificates exhibit only two structural graph types. The unresolved step is to find a dimension-uniform geometric reason for their multiplicity, without assuming that a proper five-dimensional face inherits the original coloring's antipodal oddness. Under global complementation in \(Q_n\), a proper five-face is normally sent to a different face, so the five-dimensional census cannot simply be applied to a smaller face of an arbitrary larger cube. That is the principal barrier to transferring (55) into unrestricted NORI1.


#### Two disjoint parity diamonds and an orbit-avoiding eight-path certificate in Q5

The preceding complete five-cube census admits a stronger check that directly connects parity holonomy to the critical-orbit avoidance programme. For each partial coloring \(c\), let \(H(c)\) be the simple graph on its eight retained direction-one orbit variables. Put an edge \(\{f,g\}\) in \(H(c)\) precisely when the resolved formula forbids all four assignments of \((Y_f,Y_g)\); these are the parity diamonds counted by \(D(c)\).

**Computational Theorem 29 (disjoint parity diamonds).** For every one of the \(2^{24}\) legal partial colorings of \(Q_5\),
\[
\boxed{\nu(H(c))\ge2,}
\tag{56}
\]
where \(\nu\) denotes maximum matching size.

**Finite verification.** In the same independent 24-bit enumeration as Theorem 27, the C++ certificate computes the intersection of the endpoint sets of all parity-diamond edges. In every one of the \(16,777,216\) cases, this common intersection is empty; the recorded count of star-supported contradiction graphs is zero. By Theorem 27, every \(H(c)\) has at least four edges. A finite simple graph with at least four edges and matching number at most one must have a common vertex incident with every edge: otherwise select two meeting edges \(ab,ac\); a third not using \(a\) must be \(bc\), and no fourth distinct edge can meet all three. Thus the absence of a common vertex together with \(D(c)\ge4\) establishes (56). The verified all-mask census now asserts
\[
\boxed{\texttt{COMMON\_VERTEX\_STAR\_COUNT}=0}.
\]
The updated standalone verifier is:
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/07354bcfb9ea43c680e78bab62703f6a5d5ec2c6/scripts/nori_q5_parity_census.cpp.

**Corollary 30 (robust dimension-five orbit avoidance with at most eight paths).** For every legal antipodally odd edge coloring of \(Q_5\) and every prescribed antipodal edge orbit \(e\), there is a monochromatic full antipodal geodesic avoiding \(e\). Moreover, there is a family of at most eight full rooted geodesics, all avoiding \(e\), such that **every legal assignment of the color bits in two chosen direction classes** makes at least one of these paths monochromatic, provided the edge colors of the other three direction classes remain fixed.

**Proof.** Choose one of the two free direction classes to be the direction of \(e\); call it the retained direction \(j\), and choose any different direction \(i\) as the eliminated free direction. All other three direction classes are held fixed, with arbitrary legal colors. By Theorem 29 their two-direction resolved parity graph \(H(c)\) has two vertex-disjoint parity-diamond edges. At least one of these edges \(\{f,g\}\) avoids the selected orbit \(e\). The two opposite parity requirements on \(Y_f,Y_g\) each arise from two resolved clauses, and each resolved clause is certified by two full geodesics through a common eliminated-direction orbit. Hence at most eight full rooted geodesics certify an inconsistent partial-color formula, and none of these geodesics uses \(e\): their retained-direction steps are exclusively in orbits \(f\) and \(g\). Therefore any completion of the two free direction classes must make one of these paths monochromatic, and that path avoids \(e\). By permuting cube dimensions, every direction can be chosen as retained direction \(j\). \(\square\)

This establishes the earlier five-dimensional prescribed-orbit avoidance phenomenon by a separate, stronger finite verification. It is **robust under changing all the color bits in two entire direction classes**, not just flipping the prescribed orbit. The mechanism is constructive given the three fixed direction classes and the implication-packet extraction. The evidence remains finite-dimensional; a dimension-uniform lower bound on the matching number of parity-diamond graphs would provide a direct route to unrestricted NORI1 and orbit-flip stability, but is not proved here.

The two observed four-diamond extremal graph shapes from Theorem 28, a four-cycle and a four-edge perfect matching, both have matching number at least two. The zero-star computation checks this separation across the full five-cube partial-coloring space, not merely among the 104 extremizers.


#### Cartesian tensorization of the two-direction implication system

Let \(a\ge3,b\ge2\). Fix distinct free directions \(i,j\) in \(Q_a\), and let \(f\) be a legal antipodally odd *partial coloring*: every edge outside directions \(i,j\) is colored, independently across antipodal edge orbits, and the colors of all direction-\(i,j\) orbits are left unspecified. Let \(g\) be a legal antipodally odd full coloring of \(Q_b\). Define \(f\boxtimes g\) on \(Q_{a+b}\) by taking its fixed first-block edge colors from \(f\), with no dependence on second-block bits, and all second-block edge colors from \(g\), with no dependence on first-block bits. The two first-block free directions remain free.

Write \(\Phi_{ij}(f)\) for the near-monochromatic full-geodesic clause formula from Theorem 13; let \(H_{ij}(f)\) be its resolved parity-diamond graph from Theorem 25, \(D_{ij}(f)=|E(H_{ij}(f))|\), and \(\nu_{ij}(f)\) its matching number. Define
\[
M(g)=\{w\in Q_b:\text{a monochromatic full geodesic from }w
\text{ to }\bar w\text{ exists in }g\}.
\]
The set \(M(g)\) is antipodally invariant. At any \(w\in M(g)\), there are both red and blue monochromatic full geodesics from \(w\) to \(\bar w\): reverse the antipodal translate of a geodesic of the other color.

**Theorem 31 (disjoint Cartesian clause lifting).** If \(M(g)\ne\varnothing\), then \(\Phi_{ij}(f\boxtimes g)\) contains, for each \(w\in M(g)\), a copy of the entire formula \(\Phi_{ij}(f)\), up to a relabeling and complementation of individual free Boolean variables. These copies use pairwise disjoint sets of free edge-orbit variables. Hence
\[
\boxed{D_{ij}(f\boxtimes g)\ge |M(g)|D_{ij}(f),}
\tag{57}
\]
and
\[
\boxed{\nu_{ij}(f\boxtimes g)\ge |M(g)|\nu_{ij}(f).}
\tag{58}
\]
Each contradictory implication-path packet in \(f\) also lifts to \(|M(g)|\) disjoint forcing packets in the product.

**Proof.** Choose one representative cube edge \(e\) from each free antipodal edge orbit of \(Q_a\). For \(w\in M(g)\), associate to this orbit the full-product orbit
\[
\phi_w([e])=\{(e,w),(\bar e,\bar w)\}.
\tag{59}
\]
For a fixed \(w\), the map \(\phi_w\) is injective; the images for distinct \(w\) are disjoint, because the chosen first-block representatives never include both \(e\) and \(\bar e\).

Consider any clause of \(\Phi_{ij}(f)\), witnessed by a full geodesic \(P\) whose colored edges outside \(i,j\) all have color \(t\). Antipodally translate \(P\), if needed, so that \(t=0\). This leaves its forbidden free-variable assignment unchanged: the translate complements both the prescribed color and the two free-edge colors.

Each of the two free edges of \(P\) is either its selected orbit representative or that representative's antipodal mate. Assign it a required second-block state, \(w\) in the first case and \(\bar w\) in the second. If the two required states differ, insert a monochromatic red full \(Q_b\)-geodesic between the two free steps of \(P\). If they agree, insert such a geodesic before both or after both, choosing its starting state accordingly. The connector can traverse from \(w\) to \(\bar w\) in either direction and has color zero. All first-block colored edges still have color zero, because their colors are independent of the second-block state. The lifted path traverses every one of the \(a+b\) dimensions once, and its two free steps lie in the respective full orbits \(\phi_w([e_i]),\phi_w([e_j])\). Their color requirements correspond to the original clause, with possible complementation depending on which edge is chosen as the variable representative in the larger cube.

Thus every clause in \(\Phi_{ij}(f)\) appears in the \(w\)-copy. Resolving the common first-direction variables in the larger formula reproduces all resolved clauses in each copy. Any contradictory parity pair in the base therefore supplies a contradictory pair in every copy. Disjointness yields (57) and allows matchings in the copies to be united, proving (58). The same argument transports a selected implication packet. \(\square\)

**Consequence for minimal obstructions.** A putative partial coloring with no parity diamond cannot split in this way into a first block already containing a diamond and a second block with a monochromatic antipodal geodesic. Theorem 31 therefore gives a certificate-preserving interaction-prime reduction for product decompositions, stronger than a qualitative product-existence argument. It does not show that every interaction-prime partial coloring contains a diamond.

#### An all-dimensional sparse parity-diamond graph

The random partial-coloring census cannot reveal how sparse the parity constraints may become. The following nonlinear-in-dimension, but affine-in-bits, family gives a sharp combinatorial benchmark.

Take \(n=m+2\ge3\), leave directions \(0,1\) free, and prescribe
\[
\boxed{c_k(x)=x_0\qquad(2\le k<n).}
\tag{60}
\]
These fixed-direction rules are legal under global antipodal color reversal, and the free directions may be colored in any legal fashion.

Write \(R=\{2,\ldots,n-1\}\), and identify its vertex set with \(\mathbb F_2^m\). For \(s\in\mathbb F_2^m\), define \(X_s\) to be the color of the direction-zero edge whose other bits are \(x_1=0,x_R=s\); define \(Y_s\) as the color of the direction-one edge whose other bits are \(x_0=0,x_R=s\). The antipodal mates have the complementary colors. These are convenient choices of representatives of all free edge orbits; they need not be the smallest-integer representatives used by computer enumerations.

**Theorem 32 (complete star clause formula and matching graph).** In these variables the full near-monochromatic-geodesic 2-CNF forbids precisely the assignments
\[
\boxed{
\begin{aligned}
&(X_s=p,\ Y_r=0)&&\text{for all }s,r\in\mathbb F_2^m,\ p\in\mathbb F_2,\\
&(X_s=1,\ Y_s=1)&&\text{for all }s\in\mathbb F_2^m,\\
&(X_s=0,\ Y_{\bar s}=1)&&\text{for all }s\in\mathbb F_2^m.
\end{aligned}}
\tag{61}
\]
The formula has \(2^{2m+1}+2^{m+1}\) distinct forbidden pairs. After eliminating all \(X\)-variables, for every pair \(r\ne s\) the resolved clauses forbid \((Y_r,Y_s)=(0,0),(0,1),(1,0)\); the fourth assignment \((1,1)\) is also forbidden if and only if \(s=\bar r\). Consequently
\[
\boxed{
H_{01}(c)=\{\{r,\bar r\}:r\in\mathbb F_2^m\},
\quad
D_{01}(c)=\nu_{01}(c)=2^{m-1}=2^{n-3}.
}
\tag{62}
\]
In particular, the parity-diamond graph can be a disjoint matching in arbitrarily high dimension. Its graph connectivity is not a necessary feature of successful parity forcing.

**Proof.** Every fixed-direction edge has color equal to the current bit \(x_0\). Since a full geodesic crosses direction zero once, its \(m\) fixed-direction edges are monochromatic if and only if all their steps lie on the same side of that crossing.

First suppose the direction-one step lies on the side containing all \(R\)-steps. At its crossing, the bit \(x_0\) equals their common color \(t\), and the canonical \(Y_r\)-edge must therefore have color zero to make the full path monochromatic. Conversely, given arbitrary \(s,r,p\), set \(t=0\) and place the direction-zero step last. If \(p=0\), traverse a full \(R\)-geodesic from \(\bar s\) to \(s\), inserting the direction-one step when its \(R\)-state is \(r\), with the direction-one bit changed from one to zero. The last step uses \(X_s\), and the path becomes monochromatic when \(X_s=Y_r=0\). If \(p=1\), traverse a full \(R\)-geodesic from \(s\) to \(\bar s\), inserting the direction-one step at \(R\)-state \(r\), now changing its bit from zero to one. The last direction-zero edge is the antipodal mate of \(X_s\); the path becomes monochromatic when \(X_s=1,Y_r=0\). Every prescribed \(r\) lies on a full monotone cube geodesic from \(s\) to \(\bar s\), by taking the differing directions first. This proves every assignment in the first line of (61) is forbidden.

If instead the direction-one step lies on the other side of the direction-zero crossing from all \(R\)-steps, the two free steps are consecutive. Their \(R\)-states coincide. A short case distinction according to the common fixed-edge color and the intervening direction-one bit shows that the only possible forbidden assignments with \(Y_r=1\) are \((X_s=1,Y_s=1)\) and \((X_s=0,Y_{\bar s}=1)\). Both occur: the full direction order \((1,0,R)\), starting respectively from bit configurations \((x_0,x_1,x_R)=(0,1,s)\) and \((0,0,\bar s)\), has all fixed edges color one and realizes the two indicated assignments. This proves (61).

Resolve a clause \((X_u=0,Y_r=q)\) with a clause \((X_u=1,Y_s=q')\), meaning that both are forbidden, to obtain the forbidden assignment \((Y_r=q,Y_s=q')\). The first line of (61) supplies \((0,0)\) for every pair of retained variables. Combining a first-line clause with either of the last two families gives \((0,1)\) and \((1,0)\). For two clauses both requiring retained color one to have opposite \(X_u\) values, the second line must be paired with the third at the same \(u\), and their retained indices are \(u,\bar u\). Hence \((1,1)\) is forbidden precisely for complementary retained indices. This gives (62). \(\square\)

Theorem 32 is an all-dimensional structural description, but it does not establish a universal lower bound \(D_{ij}(c)\ge2^{n-3}\) for arbitrary legal partial colorings. It identifies a sparse family that such a lower bound, if true, would have to attain.

**Verification.** Full projective geodesic enumeration confirms the clause equality (61), the parity-diamond graph (62), and its disjoint matching in dimensions \(3,4,5,6\). Independent product tests for five sampled \(Q_4\) partial colorings and legal \(Q_2\) factors confirm that every base clause lifts into two disjoint variable sets in \(Q_6\), including the requisite antipodal sign changes. A self-contained verifier is available:
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/1c2600f0124849b9e61386b2ac048d86afabf96c/scripts/nori_parity_tensor_star_verify.py.

**Remaining obstacle.** Theorem 31 propagates existing forcing certificates through independent factors, and Theorem 32 supplies a minimal-looking family of disjoint certificates in every dimension. Neither manufactures a parity contradiction inside an arbitrary interaction-prime coloring. That case remains the unrestricted closure target.


**Corollary 33 (four-path star packet).** In the partial coloring (60), fix any \(s\in\mathbb F_2^m\). Four rooted full geodesics already force a monochromatic one, regardless of all free orbit colors. Their forbidden assignments are
\[
\boxed{
(X_s=1,Y_s=0),\quad(X_s=1,Y_s=1),\quad
(X_s=0,Y_{\bar s}=0),\quad(X_s=0,Y_{\bar s}=1).
}
\tag{63}
\]
These arise from the four constructions in the proof of Theorem 32. If \(X_s=1\), one of the first two geodesics is monochromatic, whichever value \(Y_s\) takes; if \(X_s=0\), one of the last two is monochromatic, whichever value \(Y_{\bar s}\) takes. Thus the sparse all-dimensional parity matching in Theorem 32 also contains many four-path local forcing certificates. The distinction matters: a large parity-diamond matching does not imply that the shortest forcing packet must use eight paths.


#### Two-sided pivot transport and cross-curvature forcing

Let \(Q_n=Q_A\times Q_B\), where \(|A|=a\ge3\), \(|B|=b\ge1\), and two free directions \(i,j\) belong to \(A\). Fix a third direction \(k\in A\setminus\{i,j\}\). For a root \(w\in Q_B\), suppose:

(C1) For every prescribed direction \(\ell\in A\setminus\{i,j\}\), every \(x\in Q_A\) satisfies \(c_\ell(x,w)=c_\ell(x,\bar w)\).

(C2) For every direction-\(k\) edge \(\{z,z+e_k\}\subset Q_A\) and each color \(t\in\mathbb F_2\), **at least one endpoint** has a monochromatic full \(B\)-geodesic of color \(t\) between \(w\) and \(\bar w\), in its induced \(B\)-slice.

Write \(f^{(w)}\) for the prescribed \(A\)-coloring induced by layer \(w\); by (C1) and the full cube's antipodal oddness, \(f^{(w)}\) is antipodally odd.

**Theorem 34 (two-sided pivot transport).** Under (C1)–(C2), the two-direction implication formula \(\Phi_{ij}(c)\) contains a full copy of \(\Phi_{ij}(f^{(w)})\), up to relabeling and complementation of free orbit bits. Different \(w\)'s yield variable-disjoint copies. Consequently, if \(W_k\) is the family of eligible roots,
\[
\boxed{
D_{ij}(c)\ge\sum_{w\in W_k}D_{ij}(f^{(w)}),\qquad
\nu_{ij}(c)\ge\sum_{w\in W_k}\nu_{ij}(f^{(w)}).
}
\tag{64}
\]

**Proof.** For every free antipodal \(A\)-edge orbit select its member in the \(k\)-bit-zero facet, and for each \(w\) map it to the full-cube edge orbit represented by that edge in layer \(w\). These mappings have disjoint images for distinct \(w\).

Take any near-monochromatic full \(A\)-geodesic \(P=(z_0,\dots,z_a)\) producing a clause of \(\Phi_{ij}(f^{(w)})\), with its prescribed edges all color \(t\). Its unique \(k\)-step is \(z_r\to z_{r+1}=z_r+e_k\). Start the lifted path in \(B\)-layer \(w\) if the initial \(k\)-bit is zero, and in layer \(\bar w\) otherwise. Insert one full \(B\)-geodesic **immediately before or immediately after the \(k\)-step**. In both cases, because no free step lies between those two insertion positions, each free \(A\)-edge occurs in the required \(B\)-layer: \(w\) when its \(k\)-bit is zero, \(\bar w\) otherwise. All prescribed \(A\)-edges retain color \(t\), by (C1). By (C2), either \(z_r\) or \(z_{r+1}\) supplies a monochromatic \(B\)-connector of color \(t\); choose that insertion position. The resulting full \((a+b)\)-geodesic witnesses the mapped clause. Do this for every clause, and sum the disjoint parity-diamond graphs and matchings. \(\square\)

There is **no requirement for both connector colors at the same \(A\)-vertex**. One endpoint of a \(k\)-edge may support only color zero and the other only color one. This mechanism therefore applies to coupled colorings with no two-color connector at any individual vertex.

##### A square-curvature criterion when \(B=Q_2\)

Suppose \(B=\{u,v\}\), every \(B\)-slice at fixed \(x\in Q_A\) is itself antipodally odd, and (C1) holds for all \(w\). The slice edge rules have the form
\[
c_u(x,y)=\alpha(x)+y_v,\qquad c_v(x,y)=\beta(x)+y_u,
\]
with \(\alpha,\beta\) antipodally even on \(Q_A\). Put \(s(x)=\alpha(x)+\beta(x)\pmod2\). The roots \(00,11\) possess monochromatic \(B\)-geodesics of both colors if \(s=1\); the roots \(01,10\) possess both if \(s=0\).

**Corollary 35 (cross-curvature imbalance).** If
\[
\boxed{\partial_k s(x)=1\qquad\forall x\in Q_A,}
\tag{65}
\]
then the condition (C2) holds for **all four** \(B\)-roots, and hence
\[
\boxed{D_{ij}(c)\ge\sum_{w\in Q_2}D_{ij}(f^{(w)}),\quad
\nu_{ij}(c)\ge\sum_{w\in Q_2}\nu_{ij}(f^{(w)}).}
\tag{66}
\]
In terms of cross-block square curvatures,
\[
\boxed{\kappa_{k,u}(x,y)+\kappa_{k,v}(x,y)
=\partial_k(\alpha+\beta)(x)=1.}
\tag{67}
\]
Indeed (C1) implies \(\partial_u c_k=\partial_v c_k\) on the two-cube; the other terms in the two curvatures give \(\partial_k\alpha+\partial_k\beta\). Each \(k\)-edge changes the favorable diagonal of its \(B\)-slice, so one of its endpoints supplies both connector colors for each \(w\). Apply Theorem 34.

##### Arbitrarily many copies without any two-color connector

**Corollary 36 (monochrome-fibre amplification).** Let \(f\) be any legal antipodally odd partial coloring on \(Q_A\), directions \(i,j\) free, and \(k\) a third direction. Let \(b\ge1\), and choose an arbitrary antipodally even \(\psi:Q_B\to\mathbb F_2\). Define the prescribed colors on \(Q_A\times Q_B\) by
\[
\boxed{
c_\ell(x,y)=f_\ell(x)+\psi(y)\quad(\ell\in A\setminus\{i,j\}),
\qquad c_t(x,y)=x_k\quad(t\in B).
}
\tag{68}
\]
Then
\[
\boxed{
D_{ij}(c)\ge 2^bD_{ij}(f),\qquad
\nu_{ij}(c)\ge2^b\nu_{ij}(f).
}
\tag{69}
\]

**Proof.** The rules (68) are undirected and globally antipodally odd. Condition (C1) follows from the evenness of \(\psi\). All \(B\)-edges in the slice at \(x\) have the single color \(x_k\). At the other endpoint of every \(k\)-edge, all \(B\)-edges have the opposite color. Thus each endpoint supports full \(B\)-geodesics of one color and together they cover both colors: (C2) holds for every \(w\). Apply Theorem 34. The induced coloring is \(f+\psi(w)\). Globally complementing its prescribed edge colors corresponds to complementing every forbidden free-orbit assignment, preserving both \(D\) and \(\nu\). Hence each of the \(2^b\) copies contributes \(D_{ij}(f)\) and \(\nu_{ij}(f)\). \(\square\)

This is not a Cartesian product or the previous two-color gauge lifting: no induced \(B\)-slice has a monochromatic connector of the opposite color. The full coloring may also have a strongly connected directed influence graph.

**Strongly connected legal \(Q_5\) witness.** With \(A\)-bits \(x_0,x_1,x_2\) and \(B\)-bits \(y_0,y_1\), use
\[
\boxed{
c_0=x_1+x_2+y_0,\quad c_1=x_2,\quad
c_2=x_0+y_0+y_1,\quad c_3=x_2,\quad c_4=x_2
}\pmod2.
\tag{70}
\]
The directed influence graph is strongly connected on all five directions. No \(B\)-slice has both connector colors at any root. Nevertheless the two-direction clause formula contains four disjoint copies of the \(Q_3\) formula (12 clauses and one parity diamond in each copy). Direct enumeration finds 144 full-cube clauses and 22 contradictory parity pairs.

**Verification:** Standalone geodesic-order enumeration checked the pivot position and mapped clauses in the strong \(Q_5\) witness, the curvature corollary for four \(B\)-roots, and arbitrary sampled \(Q_4\) fixed-edge colorings with \(Q_2,Q_3\) monochrome-fibre extensions. The tests certify 4 and 8 distinct implication copies in dimensions five, six, and seven. Local scripts: \`nori_two_sided_pivot_verify.py\` and \`nori_pivot_monochrome_verify.py\`.

**Remaining question.** Theorem 34 supplies an all-dimensional conditional forcing mechanism within an unchanged legal coloring, and (69) amplifies certificates through nonseparable block interactions. It does not establish that edgewise connector coverage must exist in every legal coloring. The unrestricted NORI1 conjecture remains open.


#### Adaptive odd-seam transport without a fixed pivot

Write \(Q_n=Q_A\times Q_B\), with \(|A|=a\ge3\) and free directions \(i,j\in A\). Fix a family \(W\subseteq Q_B\). Assume:

(A1) For every \(w\in W\), prescribed \(A\)-edge colors agree between the layers \(w,\bar w\).

(A2) There is one Boolean function \(h:Q_A\to\mathbb F_2\), independent of \(w\), satisfying
\[
\boxed{h(\bar x)=1-h(x),\qquad \partial_i h=\partial_j h=0.}
\tag{71}
\]

(A3) At every \(A\)-vertex \(x\) and every \(w\in W\), some full \(B\)-geodesic from \(w\) to \(\bar w\) has constant edge color \(h(x)\) in the induced \(B\)-slice at \(x\). No geodesic of the opposite color is required.

Denote by \(f^{(w)}\) the legal antipodally odd prescribed \(A\)-coloring induced in layer \(w\).

**Theorem 37 (adaptive odd-seam lifting).** For each \(w\in W\), the two-direction clause formula \(\Phi_{ij}(f^{(w)})\) embeds into \(\Phi_{ij}(c)\) after consistent relabeling and complementation of its free orbit bits. These clause copies use disjoint variable sets for distinct \(w\). Consequently
\[
\boxed{D_{ij}(c)\ge\sum_{w\in W}D_{ij}(f^{(w)}),\qquad
\nu_{ij}(c)\ge\sum_{w\in W}\nu_{ij}(f^{(w)}).}
\tag{72}
\]

**Proof.** The value of \(h\) is constant along any edge in either free direction. Antipodal oddness of \(h\) therefore selects one member of every free antipodal \(A\)-edge orbit, namely the one on which \(h=0\). Map that representative into \(B\)-layer \(w\) as a representative of the corresponding full-cube free orbit. Use these same \(A\)-representatives for all \(w\); their full-cube images have disjoint variable sets.

Consider a rooted full \(A\)-geodesic \(P\) witnessing a clause, with all prescribed \(A\)-edge colors equal to \(t\). Let \(\alpha,\beta\) be the values of \(h\) at its first and second free steps, in traversal order. The two free steps must lie in layer \(w\) when their \(h\)-value is zero, and in layer \(\bar w\) when that value is one.

If \(\alpha\ne\beta\), insert the full \(B\)-connector *between* the two free steps. The vertex immediately after the earlier free step has \(h=\alpha\), whereas the vertex immediately before the later free step has \(h=\beta\). Since these values differ, one of these insertion vertices has \(h=t\). By (A3), it supports the required monochromatic connector. Choose the initial \(B\)-layer to place the two free steps in their desired layers.

If \(\alpha=\beta\), insert the connector at the start or the end of the full \(A\)-path. Its root and terminal vertex are antipodal, so their \(h\)-values are complementary. One is \(t\), giving a color-\(t\) connector by (A3). Again choose the initial layer to put both free steps in their common desired layer.

In both cases, all prescribed \(A\)-edge colors remain \(t\) by (A1), and the inserted \(B\)-geodesic also has color \(t\). The new full geodesic therefore witnesses the mapped clause, including its projective orbit-color signs. Repeat over all clauses and all \(w\). The disjoint variable copies imply (72). \(\square\)

**Corollary 38 (arbitrary odd-selector amplification).** Let \(f\) be any legal partial antipodally odd \(A\)-coloring with directions \(i,j\) free, and \(h\) any antipodally odd Boolean function independent of those two direction bits. For any \(b\ge1\) and antipodally even \(\psi:Q_B\to\mathbb F_2\), prescribe
\[
\boxed{
c_\ell(x,y)=f_\ell(x)+\psi(y)\quad(\ell\in A\setminus\{i,j\}),\qquad
c_t(x,y)=h(x)\quad(t\in B).
}
\tag{73}
\]
Then
\[
\boxed{D_{ij}(c)\ge2^bD_{ij}(f),\qquad
\nu_{ij}(c)\ge2^b\nu_{ij}(f).}
\tag{74}
\]
Every full \(B\)-geodesic at \(x\) has color \(h(x)\), meeting (A3) for all \(2^b\) roots. The induced \(A\)-coloring is \(f\) or its complement, which have identical parity-diamond counts and matching numbers.

**Strict improvement over the fixed-pivot theorem.** In \(Q_A=Q_5\), leave directions \(0,1\) free and let \(h(x)\) be the majority of the three bits \(x_2,x_3,x_4\). Then \(h\) is antipodally odd and independent of the free directions. For each \(k\in\{2,3,4\}\) there is a \(k\)-edge on which \(h\) is unchanged, so no \(k\) meets the everywhere-toggling hypothesis of the earlier monochrome-fibre pivot theorem. Yet Corollary 38 applies for every legal lower partial coloring \(f\); one explicit choice is \(f_\ell(x)=x_{(\ell+1)\bmod5}\) in each prescribed direction \(\ell=2,3,4\).

**Boundary example (free-direction dependence cannot simply be ignored).** Let \(A=Q_3\), free directions \(0,1\), and sole prescribed edge rule \(f_2(x)=x_1\). Attach \(Q_B=Q_1\), with its edge color \(h(x)=1\) at the four vertices with binary indices \(0,4,5,6\), and color zero at indices \(1,2,3,7\). This \(h\) is antipodally odd but depends on both free bits. The base two-direction formula has twelve clauses. For each of the sixteen ways to choose a representative from each of the four free antipodal \(A\)-edge orbits, map the chosen representatives into one \(B\)-layer and transport the signed clauses. Independent full-geodesic enumeration finds the overlap with the full \(Q_4\) clause set to be eight for four choices, nine for eight choices, and ten for four choices. **No representative-based mapping preserves all twelve original clauses.** This disproves the unconditional extension of the present clause-copy rule without (A2); it does not supply a counterexample to NORI1.

**Executable audit.** A self-contained full-geodesic enumerator tests the signed clause copies in 44 randomly generated legal partial colorings of dimensions \(Q_3\times Q_1\), \(Q_4\times Q_1\), \(Q_3\times Q_2\), \(Q_4\times Q_2\), \(Q_3\times Q_3\), and \(Q_5\times Q_1\), as well as the majority witness and all sixteen boundary representative choices. Verifier:
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/3ea7c0767f4a606c72f1756f9d23c2ebdf62ed9d/scripts/nori_adaptive_odd_seam_verify.py.

**Closure obligation.** Adaptive seam transport removes the need for one fixed pivot direction, but requires the connector-selector function \(h\) to be well-defined on free edges. A universal proof must either produce such compatibility within every hypothetical bad coloring, or replace this free-edge obstruction with a different way of transporting clause contradictions.


#### Four-vertex connector-selector test and local failure certificates

The selector \(h\) in Theorem 37 can be tested within any original legal partial coloring without guessing a Boolean function. Fix the partition \(A\sqcup B\), free directions \(i,j\in A\), and a nonempty collection of \(B\)-roots \(W\). For \(w\in W\) and \(x\in Q_A\), define the available monochromatic connector-color set
\[
S_w(x)=\{t\in\mathbb F_2:\text{the induced }B\text{-slice at }x
\text{ has a monochromatic full }w\text{-to-}\bar w\text{ geodesic of color }t\}.
\]
Put \(S_W(x)=\bigcap_{w\in W}S_w(x)\). These sets may be empty. Global antipodal oddness and reversal of undirected geodesics imply
\[
\boxed{S_w(\bar x)=1-S_w(x),\qquad S_W(\bar x)=1-S_W(x).}
\tag{75}
\]
Here \(1-S=\{1-t:t\in S\}\).

Write \(R=A\setminus\{i,j\}\). For each \(R\)-bit assignment \(z\), let \(F_z\) be the four-vertex \(i,j\)-face having those fixed \(R\)-bits, and define
\[
\boxed{I_W(z)=\bigcap_{x\in F_z}S_W(x).}
\tag{76}
\]
Then \(I_W(\bar z)=1-I_W(z)\).

**Theorem 39 (free-face selector criterion).** There exists a Boolean function \(h:Q_A\to\mathbb F_2\) that is antipodally odd, independent of the two free bits, and satisfies \(h(x)\in S_w(x)\) for every \(x\) and \(w\in W\), **if and only if**
\[
\boxed{I_W(z)\ne\varnothing\qquad\forall z\in Q_R.}
\tag{77}
\]

**Proof.** Independence of the free bits means that \(h\) is constant on each \(F_z\), so its value must belong to \(I_W(z)\); necessity follows. Conversely choose a representative \(z\) from each complementary pair \(\{z,\bar z\}\) of \(Q_R\), and any \(t_z\in I_W(z)\). Set \(h=t_z\) throughout \(F_z\) and \(h=1-t_z\) throughout \(F_{\bar z}\). Identity (75) ensures that the second value belongs to \(I_W(\bar z)\). The resulting \(h\) is independent of \(i,j\), antipodally odd, and supported at every selected connector root. \(\square\)

**Corollary 40 (two-vertex failure certificate).** If the selector does not exist, then some free \(i,j\)-face \(F_z\) contains either (a) a vertex \(x\) with \(S_W(x)=\varnothing\), or (b) two vertices \(x,x'\) with \(S_W(x)=\{0\}\), \(S_W(x')=\{1\}\). Conversely either conflict prevents a selector. This follows because each \(S_W(x)\) is a subset of the two-element set \(\mathbb F_2\): an empty intersection is witnessed by one empty set or two incompatible singleton sets.

Together with opposite-layer consistency (A1), criterion (77) therefore gives a finite, directly checkable sufficient condition for the all-dimensional forcing and certificate amplification of Theorem 37. The criterion does not hold for every legal coloring. A hypothetical coloring in which all such adaptive transports fail must exhibit a local connector-color conflict (or connector absence) on a free two-face for every attempted layer family; establishing an incompatible global arrangement of these local failures remains the missing step to unrestricted NORI1.


#### Sparse selector conflicts: packet robustness measured by Boolean influence

The adaptive seam proof can still transport clauses when the odd connector selector changes along *some*, but not all, free-direction edges. This yields a robustness theorem for arbitrary antipodally odd selector functions, including those depending on both free directions.

Retain the partition \(Q_n=Q_A\times Q_B\), \(|A|=a\ge3\), free directions \(i,j\in A\), and selected \(B\)-roots \(W\). Assume opposite-layer consistency of all prescribed \(A\)-edge colors for each \(w\in W\). Suppose a single antipodally odd Boolean function \(h:Q_A\to\mathbb F_2\), now allowed to depend on **every** \(A\)-bit, satisfies: at each \(x\in Q_A\) and \(w\in W\), a monochromatic full \(B\)-geodesic of color \(h(x)\) joins \(w\) to \(\bar w\) inside the \(B\)-slice at \(x\).

Call a free direction-\(r\) antipodal edge orbit \(e\), \(r\in\{i,j\}\), *safe* when \(h\) is constant across its edge. This is a well-defined orbit property because \(h(\bar x)=1-h(x)\) gives the same derivative on antipodal edges. Let \(U_r(h)\) count unsafe orbits in free direction \(r\), and \(U=U_i+U_j\). Define the ordinary Boolean influence
\[
\operatorname{Inf}_r(h)=2^{-a}\sum_{x\in Q_A}[h(x)\ne h(x+e_r)].
\]
Then
\[
\boxed{U_r(h)=2^{a-2}\operatorname{Inf}_r(h),\qquad
U(h)=2^{a-2}(\operatorname{Inf}_i(h)+\operatorname{Inf}_j(h)).}
\tag{78}
\]

**Theorem 41 (safe-orbit clause transport).** For each \(w\in W\), let \(\Phi^{\rm safe}_{ij}(f^{(w)})\) consist of those near-monochromatic full-geodesic clauses from the induced \(A\)-coloring whose two free edge orbits are both safe. Then this entire restricted clause family embeds in \(\Phi_{ij}(c)\), up to consistent orbit-variable relabeling and complementation. Copies belonging to different \(w\)'s use disjoint full-cube free-orbit variables.

**Proof.** For each safe free antipodal orbit, the member on which \(h=0\) is well-defined because \(h\) is constant along each safe edge and reverses under antipodality. Choose that member as representative for every layer root \(w\). Consider a full \(A\)-geodesic producing a clause with both free orbits safe, and let \(t\) be its prescribed-edge color. The values \(\alpha,\beta\) of \(h\) at the two free steps are constant across those particular steps; no other free-edge invariance of \(h\) is needed. If \(\alpha\ne\beta\), the vertices immediately after the first free step and before the second have \(h\)-values \(\alpha,\beta\), so one permits a color-\(t\) \(B\)-connector between them. If \(\alpha=\beta\), the two antipodal endpoints of the full \(A\)-path have complementary \(h\)-values, so one supplies a color-\(t\) connector before or after the full \(A\)-path. This is the insertion argument from Theorem 37, now applied to the selected safe clauses only. Opposite-layer consistency preserves all prescribed \(A\)-edge colors. The chosen orbit representatives do not depend on \(w\), giving pairwise disjoint copies. \(\square\)

Call a family of full-geodesic clauses a *forcing packet* if its associated two-direction Boolean formula is inconsistent. Define \(\mathscr P(\Phi)\) to be the maximum number of forcing packets with **pairwise disjoint sets of free edge-orbit variables**. This is a stronger disjointness requirement than a matching in the parity-diamond graph: distinct parity diamonds may use the same eliminated-direction orbit in their supporting clauses.

**Theorem 42 (influence-versus-packing survival).** Write \(L_w=\mathscr P(\Phi_{ij}(f^{(w)}))\). Under the hypotheses of Theorem 41,
\[
\boxed{
\mathscr P(\Phi_{ij}(c))\ \ge\
\sum_{w\in W}\max\{0,L_w-U(h)\}.
}
\tag{79}
\]
In particular, if some \(L_w>U(h)\), every legal completion of the two free direction classes contains a monochromatic full antipodal geodesic.

**Proof.** For each \(w\), choose \(L_w\) forcing packets with disjoint free-variable supports. Each unsafe orbit belongs to the support of at most one of these packets, so deleting all packets touching an unsafe orbit removes at most \(U(h)\) packets. Every remaining packet uses only safe orbits. By Theorem 41, it embeds as an inconsistent clause packet in the full formula. Distinct safe packets are variable-disjoint, and their copies for distinct \(w\)'s are disjoint. This gives (79) and the forcing conclusion. \(\square\)

**Corollary 43 (a dimension-uniform low-influence forcing family).** Let the prescribed \(A\)-direction colors be
\[
f_k(x)=x_i,\qquad k\in A\setminus\{i,j\},
\]
where \(a\ge3\). The complete star-clause formula from Theorem 32 contains \(2^{a-3}\) orbit-disjoint four-geodesic forcing packets: one for each unordered complementary pair \(\{s,\bar s\}\) of assignments to the other \(a-2\) directions. Each packet uses one free direction-\(i\) orbit and two free direction-\(j\) orbits, and packets for different complementary pairs have disjoint supports.

Extend this partial coloring by prescribing \(c_t(x,y)=h(x)\) for every new \(B\)-direction \(t\), with any antipodally odd \(h\), and take the prescribed \(A\)-edge colors independent of \(B\). Then
\[
\boxed{
\mathscr P(\Phi_{ij}(c))\ge
2^b\max\{0,\,2^{a-3}-2^{a-2}
(\operatorname{Inf}_i(h)+\operatorname{Inf}_j(h))\}.
}
\tag{80}
\]
Thus \(\operatorname{Inf}_i(h)+\operatorname{Inf}_j(h)<1/2\) is sufficient for a monochromatic full antipodal geodesic, **even when \(h\) depends nontrivially on the two free bits**. This is a direct forcing criterion inside the given legal coloring, not merely an instruction to change its edge colors.

**Perturbation witness beyond every global odd-seam selector.** Set \(a=6\), \(i=0,j=1\), let \(f_k(x)=x_0\) for \(k=2,3,4,5\), and define
\[
\boxed{h(x)=x_2+\mathbf1_{\{x\in\{0,\mathbf1\}\}}\pmod2,}
\tag{81}
\]
where \(\mathbf1\) denotes the all-one vertex of \(Q_6\). The exceptional two-vertex set is antipodally invariant, so \(h\) is odd. The only unsafe free orbits are one in direction zero and one in direction one, giving \(U(h)=2\). The base star formula has eight mutually orbit-disjoint four-path forcing packets. Formula (80) guarantees six intact packets per \(B\)-root. Direct orbit-and-clause enumeration in \(Q_6\times Q_1\) finds that seven of the eight packets survive in each of the two opposite \(B\)-layers. The selector varies along both free directions, so Theorem 37 does not apply, but Theorem 42 still forces monochromatic full geodesics after **any** legal assignment of the two free direction classes.

**Verification.** A fresh signed-geodesic enumerator tests safe-orbit clause embedding for arbitrary sampled antipodally odd \(h\) with nonzero free-direction influences in dimensions \(Q_3\times Q_1\), \(Q_4\times Q_1\), \(Q_3\times Q_2\), \(Q_4\times Q_2\), and \(Q_5\times Q_1\), including a separate numerical check of (78). Independent complete enumeration of the star formula through \(Q_6\) checks the disjoint four-clause packets and the sparse perturbation example (81), with seven of eight packets intact in each \(B\)-layer. Reproducible certificates: https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/81521d2838a2a3d47574d2445deeaed8ab7a0665/scripts/nori_sparse_selector_verify.py and https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/6842601e3a75ccea32143de7eece3d3f26332722/scripts/nori_star_sparse_perturbation_verify.py.

**Closure implication.** The fixed-pivot and adaptive-seam approaches are no longer all-or-nothing conditions. Unsafe cross-direction variation is measured by Boolean influence, and independent geodesic forcing packets provide redundancy that can absorb it. For a universal proof, the next missing theorem would have to guarantee sufficiently many orbit-disjoint forcing packets in a given arbitrary partial coloring, or show that strong connector influence itself creates alternate forcing. Neither is established here.


#### Fractional packet packing and high-influence forcing

Theorem 42 requires inconsistent packets with disjoint free orbit supports. An overlapping family offers more redundancy. For an arbitrary induced legal two-direction partial coloring \(f\), let \(\mathcal P\) be a family of inconsistent subformulas of \(\Phi_{ij}(f)\), and \(V(P)\) the free-orbit variables of packet \(P\). Choose weights \(\lambda_P\ge0\) such that
\[
\boxed{\sum_{P:e\in V(P)}\lambda_P\le1\quad\forall e.}\tag{82}
\]
Let \(L^*=\sum_P\lambda_P\).

**Theorem 44 (fractional unsafe-orbit survival).** Under Theorem 41's opposite-layer and monochromatic-connector hypotheses, let \(S\) be the free orbit set on which the odd connector selector changes. The total weight of forcing packets surviving the clause lift is at least
\[
\boxed{L^*-|S|.}\tag{83}
\]
Thus \(L^*>|S|\) guarantees a monochromatic full antipodal geodesic under every legal completion. For several eligible connector roots \(w\), apply this bound independently to their induced formulas; the resulting full-cube packet copies use disjoint variable sets.

**Proof.** Each packet that cannot be transported meets \(S\). By the union bound and the packing constraints,
\[
\sum_{P:V(P)\cap S\ne\varnothing}\lambda_P
\le\sum_{e\in S}\sum_{P:e\in V(P)}\lambda_P\le|S|.
\]
All remaining packets consist solely of safe clauses, and Theorem 41 transports them as inconsistent packets. Their survival proves the assertion. \(\square\)

More generally, if direction-\(i\) orbits have packet load at most \(\alpha_i\) and direction-\(j\) orbits have load at most \(\alpha_j\), then the surviving weight is at least
\[
\boxed{L^*-\alpha_iU_i(h)-\alpha_jU_j(h).}\tag{84}
\]

**Corollary 45 (two alternative star packets).** For the star partial coloring \(f_k(x)=x_0\), with directions \(0,1\) free, let \(L=2^{a-3}\). At every complementary pair \(\{s,\bar s\}\) of the other \(a-2\) bits, the formula of Theorem 32 contains two alternative contradictory four-clause packets. Their orbit supports are respectively
\(\{X_s,Y_s,Y_{\bar s}\}\) and \(\{X_{\bar s},Y_s,Y_{\bar s}\}\).
Assign each packet weight \(1/2\). Every \(X\)-orbit has load \(1/2\), every \(Y\)-orbit has load one, and total weight is \(L\). Hence a forcing packet survives whenever
\[
\boxed{\tfrac12U_0(h)+U_1(h)<L,}
\tag{85}
\]
equivalently
\[
\boxed{\operatorname{Inf}_0(h)+2\operatorname{Inf}_1(h)<1.}
\tag{86}
\]
This improves the previous criterion
\(\operatorname{Inf}_0(h)+\operatorname{Inf}_1(h)<1/2\).
In fact at least
\[
\boxed{\max\{0,L-U_1(h)-\lfloor U_0(h)/2\rfloor\}}
\tag{87}
\]
complementary pairs retain a packet: a pair fails only if one of its \(Y\)-orbits is unsafe, or both of its \(X\)-orbits are unsafe.

**Verified high-influence witness.** In \(Q_A=Q_6\), choose \(q(x)=[x_3=x_4=x_5]\) and
\[
\boxed{h(x)=\begin{cases}x_2,&q(x)=1,\\x_0,&q(x)=0.\end{cases}}\tag{88}
\]
This \(h\) is antipodally odd, with
\(\operatorname{Inf}_0(h)=3/4,\ \operatorname{Inf}_1(h)=0\), so \((U_0,U_1)=(12,0)\). The old influence criterion proves nothing, but (87) guarantees two surviving four-path packets in each opposite connector layer after adjoining \(Q_B=Q_1\) with its edge color \(h(x)\). Independent enumeration of every rooted full \(Q_7\)-geodesic verifies that both packets' four clauses occur in the full formula for each layer; the entire two-direction formula has 2112 clauses. The signed antipodal orbit conventions are checked separately:
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/a2239cd78476f82a5dc003e50078d03ac6a157ae/scripts/nori_fractional_packet_verify.py.

This theorem applies to arbitrary induced formulas, while the worked star family exposes the power of overlapping alternative certificates. The main open difficulty persists: a selector for which every free orbit is unsafe may generate new implication paths rather than preserve existing packets. Fractional packing cannot itself infer those new constraints, so the unrestricted NORI1 conjecture remains open.


#### Unsafe seam exchange as a signed two-sheet implication cover

The safe-orbit packing theorem discards every clause touching a free orbit across which the connector selector changes. A different construction retains **every** clause and traces how unsafe exchanges move it between two copies of the free orbit variables.

Let \(a\ge3\), and let \(f\) be an arbitrary legal antipodally odd partial coloring of \(Q_a\), with directions \(i,j\) free. Add one direction \(b\), prescribe the other \(A\)-edge colors by \(c_k(x,y)=f_k(x)\), and prescribe the new-direction color by
\[
\boxed{c_b(x,y)=h(x),\qquad h(\bar x)=1-h(x).}
\tag{90}
\]
The two original free direction classes remain entirely unrestricted. There is no hypothesis on \(\partial_i h\) or \(\partial_j h\).

For each free antipodal edge orbit \(e\) of \(Q_a\), select one member as representative. In the expanded cube the two orbit variables represented by this edge in new-direction layers zero and one are \(X_e^0,X_e^1\). The base variable is \(X_e\).

Consider a rooted full \(Q_a\)-geodesic \(P=(z_0,\ldots,z_a)\), with all its prescribed edges colored \(t\). Let its two free edges, in whatever traversal order, belong to orbits \(e,g\), with base forbidden colors \(p,q\). At a cut \(r\in\{0,\ldots,a\}\), the new-direction step may be inserted into \(P\). Define
\[
\delta(P,r)=[\text{the cut }r\text{ lies strictly between the two free steps}].
\]

**Theorem 46 (complete cut-voltage formula).** The complete two-direction formula of the expanded partial coloring (90) consists of all clauses forbidding
\[
\boxed{
X_e^s=p,\quad
X_g^{\,s\oplus p\oplus q\oplus\delta(P,r)}=q,
\qquad s\in\mathbb F_2,
}
\tag{91}
\]
as \(P\) ranges over the rooted full base geodesics whose prescribed edges all have a common color \(t\), and \(r\) ranges over cuts satisfying
\[
\boxed{h(z_r)=t.}
\tag{92}
\]
Every such \(P\) has at least one permissible cut, because \(h(z_a)=1-h(z_0)\).

**Proof.** Every full geodesic in \(Q_{a+1}\) projects, after deleting its unique new-direction step, to one full \(Q_a\)-geodesic \(P\), with a unique cut \(r\) and initial new-direction bit. Its prescribed \(A\)-edge colors are those of \(P\), irrespective of the new-direction bit, and its new-direction edge has color \(h(z_r)\). Hence its prescribed edges are monochromatic precisely when \(P\)'s prescribed edges all have one color \(t\) and (92) holds.

Let \(\sigma_e,\sigma_g\) indicate whether each free base edge is the selected orbit representative or its antipodal mate. The base forbidden values are \(p=t\oplus\sigma_e\) and \(q=t\oplus\sigma_g\). If the starting new-direction layer is \(u\), the sheet index of the full orbit used at a free step is
\[
u\oplus[\text{step occurs after the cut}]\oplus\sigma.
\]
Taking the difference of the two sheet indices cancels \(u\) and gives
\(\sigma_e\oplus\sigma_g\oplus\delta=p\oplus q\oplus\delta\).
Both starting-layer choices occur, giving both values of \(s\). This establishes (91), and every full geodesic arises in this construction. \(\square\)

Thus the enlarged signed implication graph is a **regular two-sheet cover** of the base implication multigraph. A rooted path together with a permissible cut gives voltage
\[
\boxed{v(P,r)=p\oplus q\oplus\delta(P,r).}
\tag{93}
\]
Each base implication arc \((e,p)\to(g,1-q)\), and its complementary reverse arc, lifts with the same sheet change \(v\). A base arc may have both voltages if different supporting paths or cuts produce them. No base arc disappears, even when every free orbit is unsafe.

#### A holonomy criterion for forcing in the expanded cube

Let \(G\) be the base implication multigraph with these voltage-decorated arcs. A strongly connected component \(S\) of \(G\) is *contradictory* if it contains both signed states \((e,0)\) and \((e,1)\) for some free orbit \(e\). Such a component is invariant under the involution \((e,p)\mapsto(e,1-p)\), by contrapositive symmetry.

Call \(S\) *balanced* if every directed closed walk inside \(S\) has total voltage zero. This is equivalent to the existence of a Boolean potential \(\phi\) on its vertices satisfying
\[
\boxed{\phi(v)\oplus\phi(u)=\text{voltage}(u\to v)}
\tag{94}
\]
on every internal arc. In a balanced contradictory component, contrapositive symmetry implies that
\[
\epsilon(S)=\phi(e,0)\oplus\phi(e,1)
\tag{95}
\]
is independent of the choice of orbit \(e\) whose two states lie in \(S\).

**Theorem 47 (holonomy characterization of bad expansions).** The two-direction formula of the expanded partial coloring (90) is satisfiable if and only if **every** contradictory base component \(S\) is balanced and has
\[
\boxed{\epsilon(S)=1.}
\tag{96}
\]
In particular, a single contradictory base component with an odd-voltage closed walk forces a monochromatic full antipodal geodesic for every legal assignment of the two free direction classes. The same forcing conclusion holds for a balanced contradictory component with \(\epsilon(S)=0\).

**Proof.** The full implication graph is the two-sheet voltage cover from Theorem 46. Over a strongly connected base component, an odd-voltage closed walk joins its two sheet copies; the entire inverse image is then strongly connected, including complementary signed states of the same full-orbit variable. That violates 2-SAT satisfiability.

If instead all internal closed walks have voltage zero, choose a potential \(\phi\) satisfying (94). The inverse image separates into two strongly connected components, distinguished by the invariant \(\text{sheet}\oplus\phi(\text{base state})\). Two complementary signed states of the same full-orbit variable lie together precisely when their potential values agree, or \(\epsilon(S)=0\). They lie in different components precisely when \(\epsilon(S)=1\). Finally, any pair of complementary full-orbit signed states lying in the same enlarged strongly connected component projects to a contradictory base component. This proves both directions by the standard 2-SAT implication criterion. \(\square\)

**Corollary 48 (orbit-level parity obstruction).** If the expanded formula is satisfiable, then within every contradictory base component \(S\) there is a Boolean assignment \(\alpha_e\) to its free orbit vertices such that for every internal implication supported by a rooted path \(P\) and permissible cut \(r\),
\[
\boxed{\alpha_e\oplus\alpha_g=1\oplus\delta(P,r).}
\tag{97}
\]
Conversely the existence of such an assignment for every contradictory component implies the expanded formula is satisfiable. Thus a parity-inconsistent closed walk in the corresponding *unsigned-orbit graph with labels \(1\oplus\delta\)* forces a monochromatic full antipodal geodesic.

**Proof.** Under (96), write \(\phi(e,p)=\alpha_e\oplus p\) inside \(S\). Substituting into the implication arc \((e,p)\to(g,1-q)\) of voltage \(p\oplus q\oplus\delta\) gives (97). Conversely, from (97) set \(\phi(e,p)=\alpha_e\oplus p\). It satisfies (94) and has \(\epsilon=1\), so Theorem 47 applies. \(\square\)

**Corollary 49 (straddling-cut forcing).** Suppose a rooted near-monochromatic base path \(P\) yields an implication arc inside a contradictory base component. If it has two permissible insertion cuts \(r,r'\), with one between its free steps and the other outside, then the expanded two-direction formula is inconsistent.

**Proof.** The same base implication arc has the two different sheet voltages from (93), since \(\delta(P,r)\ne\delta(P,r')\). A directed return path exists inside the strongly connected component. Pairing it with the two arcs creates closed walks whose voltage sums differ by one. One is odd, so Theorem 47 forces inconsistency. \(\square\)

This shows why high influence can generate forcing rather than destroy it: different seam positions may give incompatible sheet transports. The relevant obstruction is not the count of unsafe orbits but whether an antipodally antisymmetric orbit potential \(\alpha\) can satisfy all their path-cut requirements simultaneously.

**Computational audit.** Independent full-geodesic enumeration in \(Q_{a+1}\) was compared clause by clause to (91) for fifteen arbitrary legal pairs \((f,h)\) when \(a=3\), twelve when \(a=4\), and four when \(a=5\). Every clause agreed. A separate independent implication-graph checker verified the equivalence (96) for 64 generated pairs when \(a=3\), 50 when \(a=4\), and ten when \(a=5\); all these examples had an odd-voltage closed walk in a contradictory base component. In addition, complete enumeration of the four possible prescribed base colorings and sixteen possible odd connector functions in \(Q_3\) confirms odd holonomy in **all 64** base-and-connector pairs. No all-dimensional theorem of unavoidable odd holonomy is asserted.

**Next closure obligation.** Prove that a hypothetical balanced contradictory base component cannot admit the orbit assignment (97) when its voltages arise from a cube coloring and an odd connector function. The finite experiments support that possibility, but abstract two-sheet covers of contradictory 2-SAT formulas can be satisfiable; the geometry of complete cube geodesics is therefore essential. Theorem 47 isolates the needed global compatibility statement rather than repeating an existence formulation of NORI1.
#### Interior seam forcing criterion

**Theorem 50.** In Theorem 46, every rooted base path with prescribed edge color t has an allowed endpoint seam, since its endpoints have opposite h values. Thus every base clause has a baseline lift with voltage p xor q, and all baseline clauses are simultaneously satisfiable by assigning direction-i sheet bits X_e^s=s and direction-j sheet bits Y_f^s=1-s. A seam between the two free steps has opposite voltage p xor q xor 1.

The expanded 2-SAT formula is inconsistent if and only if a near-monochromatic rooted base path has an allowed interior seam h(z_r)=t and its associated implication arc belongs to a contradictory strongly connected component of the base implication graph.

**Proof.** Baseline implication arcs have a potential phi(e,p)=p on free direction i and phi(f,q)=1-q on free direction j; complementary signed states have opposite potentials. If an interior seam contributes an opposite-voltage arc within a contradictory base component, a baseline return path gives odd holonomy, so the lifted component contains opposite signed states. Conversely, a lifted contradictory component projects into a contradictory base component; if that component has no interior seams, every internal arc retains the baseline potential, separating opposite signed states. Thus no lifted contradiction occurs. QED.

A full base implication graph with one strongly connected component therefore needs just one allowed interior seam to force a monochromatic full antipodal geodesic. Complete Q3 base-and-seam enumeration covers 64 cases, and independent tests cover 100 Q4 and 20 Q5 random cases. The all-dimensional occurrence of such seams remains unproved.

#### Connector-independent opposite-phase interior forcing

Theorem 50 identifies a permitted interior seam as the obstruction to a satisfactory two-sheet expansion. This leads to a stronger certificate that is determined entirely by the base prescribed-edge coloring and works for **every** odd connector selector.

Call a vertex \(z\in Q_a\) an *opposite-phase interior witness* if there exist rooted full base geodesics \(P_0,P_1\) whose prescribed-edge colors are respectively all zero and all one, such that \(z\) lies between their two free steps, and each path's implication arc belongs to a contradictory strongly connected component of the base implication graph.

**Theorem 52 (connector-independent two-phase forcing).** If a legal partial base coloring has an opposite-phase interior witness, then **for every** antipodally odd Boolean function \(h\) used as the added-direction edge color in (90), the expanded two-direction formula is inconsistent. Consequently every legal assignment of the two free direction classes admits a monochromatic full antipodal geodesic.

**Proof.** At the common witness vertex \(z\), the connector color \(h(z)\) is either zero or one. Choose the path \(P_{h(z)}\), whose prescribed edges all have that color. Its connector step can be inserted at \(z\), between its two free steps. The associated implication belongs to a contradictory base component, so Theorem 50 forces inconsistency. \(\square\)

##### An analytic three-dimensional base instance

**Proposition 53.** Let \(a=3\), take free directions \(0,1\), and color the edges in the single prescribed direction \(2\) by an arbitrary legal odd rule \(f_2(x)=F(x_0,x_1)\). Then **every vertex** \(z\in Q_3\) is an opposite-phase interior witness.

**Proof.** For any chosen \(z\), consider the rooted full direction order \((2,0,1)\), starting at \(z+e_2+e_0\). It passes through \(z\) between the free steps, and its prescribed edge has color \(F(1-z_0,z_1)\). Next consider direction order \((2,1,0)\), starting at \(z+e_2+e_1\). It also passes through \(z\) between the free steps, and its prescribed edge has color \(F(z_0,1-z_1)\). These two inputs of \(F\) are complementary, so global antipodal oddness gives opposite prescribed colors. Finally, the base two-direction implication graph is strongly connected on all eight signed states for each of the four possible odd rules \(F\); this follows by direct enumeration of the four binary assignments to \(F(0,0),F(0,1)\). Thus both implication arcs belong to its contradictory component. \(\square\)

The result gives an elementary reason that the one-direction connector extension of any such \(Q_3\) prescribed coloring forces a full monochromatic \(Q_4\)-geodesic regardless of connector variation. This applies even when every free orbit is unsafe.

##### Full four-dimensional prescribed-color census

**Computational Proposition 54.** Take an arbitrary legal antipodally odd partial coloring of \(Q_4\) with two specified free direction classes. There are eight prescribed antipodal edge-orbit bits and thus \(2^8=256\) such colorings. For each, form the complete base implication graph and count the vertices admitting both zero-phase and one-phase internal witnesses whose arcs lie inside contradictory components. The complete distribution is
\[
\boxed{
\begin{array}{c|rrr}
\#\text{witness vertices}&8&14&16\\\hline
\#\text{partial colorings}&4&48&204.
\end{array}}
\tag{101}
\]
In particular every such partial coloring has at least eight opposite-phase interior witnesses. Therefore **every legal one-direction connector extension of such a partial coloring**, for any odd connector selector \(h\), forces a monochromatic full antipodal geodesic under every assignment of the two free direction classes.

The calculation enumerates all \(16\cdot4!=384\) rooted base direction orders per prescribed coloring, constructs its signed base implication graph, identifies its contradictory components, and records the colors of the prescribed steps available at each interior vertex. This is a finite computational result, not a dimension-uniform lower bound on the witness count. In 100 sampled five-dimensional and twelve sampled six-dimensional base colorings, the respective witness counts ranged from 26 to 32, and 62 to 64. No conclusion about all higher-dimensional colorings follows from those samples.

**Closure direction.** The positive results suggest replacing the arbitrary connector-selector problem by a question entirely internal to a partial base coloring: must there be a vertex with two opposite-color interior geodesic certificates inside contradictory implication components? Establishing this for an arbitrary dimension would force every one-direction extension of the layer-independent type (90) and would give a geometric reason for the odd sheet holonomy found in the finite computations. It would still not directly cover full colorings whose prescribed old-direction edge rules depend on the added bit; that compatibility remains an independent obligation for unrestricted NORI1.


#### Unrestricted opposite-layer seam intervals and two-zone clause compatibility

The preceding voltage-cover theorems assume that prescribed old-direction edge colors are independent of an added direction. An arbitrary legal antipodally odd coloring need not satisfy that assumption. The following interval theorem removes it entirely, while also identifying where a forcing contradiction must occur.

Fix a dimension \(b\) and write \(Q_n=Q_a\times Q_1\), \(a=n-1\ge2\). Keep two old directions \(i,j\) free. Prescribe every other edge orbit legally. Define the lower-facet edge colors \(f_k(x)=c_k(x,0)\), the connector colors \(h(x)=c_b(x)\), and the layer-defect function on each prescribed old-direction edge:
\[
\boxed{D_k(x)=c_k(x,0)\oplus c_k(x,1)
=1\oplus f_k(x)\oplus f_k(\bar x).}
\tag{102}
\]
Here \(\bar x\) is the antipode in \(Q_a\). Antipodal oddness makes \(h\) odd, and makes \(D_k\) antipodally even. Each \(D_k\) is constant across the edge in its own direction. Conversely, **every** antipodally even binary assignment to the old edge orbits can arise as a defect field from an arbitrary lower-facet coloring: choose \(f_k\) on one member of each lower-facet antipodal edge pair, then enforce the displayed identity on the other member. Thus no extra integrability identity on \(D\) follows merely from global antipodal oddness.

Let \(P=(z_0,\ldots,z_a)\) be any rooted full \(Q_a\)-geodesic, using old directions \(\pi_0,\ldots,\pi_{a-1}\). For each prescribed step \(q\) put
\[
\alpha_q=f_{\pi_q}(z_q),\qquad
\varepsilon_q=D_{\pi_q}(z_q).
\]
Choose initial connector-layer bit \(u\), desired prescribed-edge color \(t\), and insertion cut \(r\in\{0,\ldots,a\}\). The color of a prescribed old edge at step \(q\) in the lifted geodesic is
\[
\boxed{
\alpha_q\oplus\varepsilon_q\bigl(u\oplus[q\ge r]\bigr).
}
\tag{103}
\]

**Theorem 55 (unrestricted seam-interval theorem).** Let \(L=L(P,u,t)\) and \(R=R(P,u,t)\) be defined by
\[
\boxed{
\begin{aligned}
L&=\max\bigl(\{0\}\cup\{q+1:\varepsilon_q=1,\
\alpha_q\oplus u\oplus t=0\}\bigr),\\
R&=\min\bigl(\{a\}\cup\{q:\varepsilon_q=1,\
\alpha_q\oplus u\oplus t=1\}\bigr).
\end{aligned}}
\tag{104}
\]
If any prescribed step with \(\varepsilon_q=0\) has \(\alpha_q\ne t\), declare the interval empty. Otherwise all prescribed old edges have color \(t\) after inserting the connector if and only if
\[
\boxed{L\le r\le R.}
\tag{105}
\]
The resulting full lifted path has all its prescribed edges colored \(t\) if and only if, additionally,
\[
\boxed{h(z_r)=t.}
\tag{106}
\]
For each such cut and both choices of the initial connector layer \(u\), the two free edges induce their standard forbidden pair of projective edge-orbit variables. Taking the union over all \(P,u,t,r\) reconstructs the **entire** two-direction 2-CNF \(\Phi_{ij}\) of the original arbitrary legal partial coloring, without requiring the two facets to agree.

**Proof.** Before the seam the old steps lie in layer \(u\); after it they lie in layer \(1-u\). Substituting the defect definition gives (103). A zero-defect edge has color \(\alpha_q\) on both layers, requiring \(\alpha_q=t\). For a defective edge, requiring its color to equal \(t\) is equivalent to
\([q\ge r]=\alpha_q\oplus u\oplus t\). When the right side is zero, the seam must be after that step, \(r\ge q+1\). When it is one, \(r\le q\). Intersecting these half-intervals proves (104)--(105). The connector has color \(h(z_r)\), proving (106). Conversely every full \(Q_n\)-geodesic contains the connector direction once; deleting that step yields one such \(P\), cut and initial layer. Consequently the clause union is complete. \(\square\)

For fixed \(P,u,t\), the defect-one steps, read in traversal order and labeled by \(\alpha_q\oplus u\oplus t\), must form a nondecreasing binary word; the eligible seam positions then form one interval. When all prescribed edges are defect-free, this recovers the earlier layer-independent seam rule. When every prescribed edge has defect one, the lower-facet prescribed-color word must be monotone in one orientation. This links the unrestricted layer-coupling formula to Article XV's arbitrary-facet monotone-root programme.

##### Two individually satisfiable seam-zone formulas

Let the two free steps occur at positions \(p<q\) among the old steps. Divide all near-monochromatic full-geodesic clauses into **interior** clauses (connector cut \(p<r\le q\)) and **exterior** clauses (all other cuts). Let their conjunctions be \(\Phi_{\mathrm{in}}\) and \(\Phi_{\mathrm{out}}\). A clause may belong to both families through different supporting paths; their conjunction is the full \(\Phi_{ij}\).

**Theorem 56 (unrestricted two-zone satisfiability).** For every legal prescribed coloring in any dimension,
\[
\boxed{\Phi_{\mathrm{in}}\text{ is satisfiable},
\qquad\Phi_{\mathrm{out}}\text{ is satisfiable}.}
\tag{107}
\]
Two explicit legal completions suffice:
\[
\boxed{
\begin{array}{c|cc}
&c_i(x,y)&c_j(x,y)\\
\Phi_{\mathrm{out}}\text{ model}&y&1\oplus y\\
\Phi_{\mathrm{in}}\text{ model}&y&y
\end{array}}
\tag{108}
\]
where \(y\) is the connector-layer bit.

**Proof.** Each rule (108) is independent of its own edge direction and flips under the full antipode, so defines a legal completion. An exterior path has both free steps in the same connector layer. Under the first completion their colors are \(y\) and \(1-y\), hence differ. An interior path has its two free steps in opposite connector layers. Under the second completion their colors are again different. Thus neither family alone can contain a monochromatic full geodesic under its displayed completion, giving satisfiability. \(\square\)

**Corollary 57 (mixed-zone necessity).** Every contradictory forcing packet in the two-direction formula of an arbitrary fixed coloring contains at least one interior clause and at least one exterior clause. Equivalently, any 2-SAT implication contradiction must rely on interactions between both seam zones. Under the first completion in (108), any monochromatic full antipodal geodesic must cross the connector direction *between* the free directions; under the second completion, any such geodesic must cross the connector *outside* that interval.

Unlike the previous regular two-sheet voltage argument, the interval theorem and zone decomposition make **no layer-independence assumption**. The remaining unrestricted closure question is therefore a compatibility question between two always-satisfiable clause families, with eligible seam cuts governed by the interval inequalities (104)--(106). Neither theorem claims that their union is necessarily inconsistent; that statement remains NORI1 itself.

**Reproducibility.** A standalone Python verifier constructs the full clause formula in two independent ways: enumeration of rooted full \(Q_n\)-geodesics, and the seam-interval inequalities. It separately checks the interior/exterior partition and both legal satisfying assignments. The tests cover all four legal partial colorings for \(Q_3\), all \(256\) for \(Q_4\), forty sampled \(Q_5\) partial colorings, and five sampled \(Q_6\) partial colorings. All checks pass.
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/7068128447b2fefa00deb1d86016a6f39f3535a7/scripts/nori_unrestricted_seam_intervals_verify.py.


#### Projective seam-root transport and the finite two-root forcing theorem

The unrestricted seam-interval formula admits a second decomposition that is useful for locating global contradictions. Fix the connector direction \(b\), and for each \(z\in Q_{n-1}\) let \(\Phi_z\) be the subformula of \(\Phi_{ij}\) containing the clauses supported by full geodesics whose unique connector step lies over old vertex \(z\). Let \(\bar z\) denote its antipode in the old \((n-1)\)-cube.

**Theorem 58 (projective seam-root invariance).** In every dimension, for every legal partial coloring,
\[
\boxed{\Phi_z=\Phi_{\bar z}.}
\tag{109}
\]
Thus the two-direction clause formula decomposes into subformulas indexed by the \(2^{n-2}\) antipodal edge orbits of the connector direction, not by the \(2^{n-1}\) individual connector edges.

**Proof.** Apply full-cube antipodal translation to a full geodesic whose connector step lies over \(z\). Its connector step now lies over \(\bar z\), every edge color complements, and every edge stays in its original antipodal edge orbit. Therefore the two free-orbit variable assignments that make the original path monochromatic also make its antipodal translate monochromatic. If one enumerates rooted paths from only one half of the vertex set, reverse the translated path to restore the allowed rooting; edge colors and forbidden orbit assignments do not change. The construction is involutive, so both subformulas contain each other. \(\square\)

**Computational Proposition 59 (two connector orbits suffice in Q4).** Let \(Q_4\) have any prescribed legal antipodally odd colors in two direction classes, with two other direction classes left free. Choose one of the prescribed classes as the connector direction. Then:

1. The clauses from any **one** projective seam-root orbit are satisfiable.
2. There exist **two distinct** projective seam-root orbits whose combined clauses are inconsistent.

Consequently, after the two prescribed direction classes are colored, there is a selection of two antipodal connector edge orbits such that **every** legal completion of both free direction classes produces a monochromatic full antipodal geodesic crossing one of those two connector orbits. A single orbit never suffices for a forcing certificate of this type, so the minimum forcing size is two.

**Verification.** There are eight prescribed edge-orbit bits in \(Q_4\), hence \(2^8=256\) prescribed colorings. The four projective connector-root subformulas were reconstructed directly from full rooted \(Q_4\)-geodesics, and each formula and pairwise union was checked by an independent binary implication-graph satisfiability test. Each single-root formula was satisfiable in all 256 cases. The number of **incompatible unordered pairs** among the four projective roots had the complete distribution
\[
\boxed{
\begin{array}{c|rrrr}
\#\text{incompatible pairs}&2&4&5&6\\\hline
\#\text{prescribed colorings}&4&76&120&56 .
\end{array}}
\tag{110}
\]
In \(Q_3\), the analogous two-projective-root statement holds for all four prescribed colorings: each individual formula is satisfiable and their union is inconsistent.

This calculation identifies transport between two distinct connector-edge orbits as a sufficient finite forcing mechanism even when the prescribed colors on opposite layers differ arbitrarily. It does **not** establish a two-root forcing theorem in higher dimensions. In samples of forty legal \(Q_5\) partial colorings, no single projective seam-root formula was inconsistent, while many pairs were; these samples are not an all-coloring certificate.

Independent standard-library verifier:
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/8176a237e2bbba3f8a82ceccc521fb85e436a2b6/scripts/nori_projective_seam_pair_census.py.

**Next global compatibility question.** Theorems 55, 56 and 58 replace an assumed layer-independent voltage cover by a collection of seam-root interval constraints in one arbitrary coloring. The two exterior/interior clause families each admit a canonical satisfying assignment, and the finite census shows that individually satisfiable projective seam-root families may jointly force a contradiction. The dimension-uniform challenge is to prove a transport contradiction between a small number of these families, rather than impose a nonexistent restriction on the defect field \(D\). NORI1 remains open.


#### Affine five-cube obstruction to universal two-root forcing; a triadic closure packet

The Q4 result that two projective connector-edge orbits can always force a monochromatic full geodesic does **not** extend to Q5, even for affine legal partial colorings.

Fix free directions 0 and 1, connector direction 4, and prescribe
\[
\boxed{c_2(x)=x_1,\quad c_3(x)=1\oplus x_0,\quad c_4(x)=1\oplus x_1.}
\tag{111}
\]
These rules are undirected and antipodally odd. In canonical fixed-orbit order (directions 2,3,4; smaller lower endpoint ascending) the 24-bit mask is \`0x3355cc\`. Label the eight projective connector-step positions by \(0,1,\ldots,7\) and their clause systems by \(\Phi_z\).

**Proposition 60 (seam-root Helly number three).** Every individual \(\Phi_z\) and every pairwise conjunction \(\Phi_z\land\Phi_{z'}\) is satisfiable, but the conjunction on roots \(0,1,4\) is inconsistent. Only six rooted full geodesics suffice.

For pairwise satisfiability there are explicit 16-bit free-orbit assignments for each of the 28 pairs. Number the sixteen free orbits lexicographically by direction then canonical smaller lower endpoint. The upper triangular table provides satisfying assignment words in hexadecimal:

| \(z\backslash z'\) | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| 0 | cc44 | e80f | aaaa | aaaa | cc70 | cc44 | cc44 |
| 1 | — | e916 | 33d0 | 3bf0 | 00f0 | cc44 | cc44 |
| 2 | — | — | 3311 | 3311 | 3311 | 000f | cc07 |
| 3 | — | — | — | 3311 | 3311 | b30f | aaaa |
| 4 | — | — | — | — | 3311 | b30d | aaaa |
| 5 | — | — | — | — | — | a659 | ccf0 |
| 6 | — | — | — | — | — | — | cc44 |

Each word was checked directly against all corresponding full-geodesic clauses.

**Six-path proof.** Denote free orbit-color variables by
\(A=X_{(0,10)}, B=X_{(0,4)}, C=X_{(0,8)}, D=X_{(1,12)}, E=X_{(1,9)}\).
For each rooted path below, its three prescribed-direction edges have one common color under (111). The listed pair is the free-orbit assignment that would make that full path monochromatic and must therefore be forbidden by any bad completion.

| Path root | Direction order | Seam root | Forbidden pair |
|---:|---|---:|---|
| 11 | 0,2,1,3,4 | 4 | \(A=1,D=1\) |
| 4 | 0,2,3,1,4 | 4 | \(B=0,E=0\) |
| 10 | 0,4,3,1,2 | 4 | \(A=0,D=1\) |
| 5 | 0,4,1,2,3 | 4 | \(B=1,E=0\) |
| 1 | 3,0,2,1,4 | 1 | \(C=0,D=0\) |
| 15 | 2,1,0,3,4 | 0 | \(C=1,E=1\) |

Avoiding both first and third forbidden pairs forces \(D=0\). Avoiding both second and fourth forces \(E=1\). The fifth then forces \(C=1\), but the sixth forces \(C=0\). Contradiction. Every one of the six clauses is essential to this displayed packet. All 28 pairwise root unions remain satisfiable by the witnesses above, so all three root systems are needed.

**Theorem 61 (triadic bridge-fork rule).** The preceding six-clause pattern is an unrestricted dimension-uniform sufficient forcing criterion: whenever three seam-root families support four clauses forcing \(D=0,E=1\) and two further clauses respectively forbidding \(C=0,D=0\) and \(C=1,E=1\), every completion contains a monochromatic full geodesic. This is a local-to-global **three-root** forcing operation, not a theorem asserting that every coloring possesses the pattern.

**Computational Proposition 62 (complete affine Q5 classification).** Among the \(16^3=4096\) legal affine assignments to the three prescribed direction classes in Q5, precisely 4080 have some inconsistent pair of seam-root systems; the remaining 16 have every pair satisfiable but at least one inconsistent triple. Those 16 are precisely
\[
\boxed{
c_2=x_u\oplus a,\quad
c_3=x_{1-u}\oplus b,\quad
c_4\in\{1\oplus c_2,\ 1\oplus c_3\},
\qquad u,a,b\in\mathbb F_2.
}
\tag{112}
\]
The affine census builds 1920 rooted projective full geodesics, runs the two-direction implication-graph test for all root pairs, and tests triples for all 16 exceptions. Its source is
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/ca778e150b205fc21dbfe4d987ca50461157a643/scripts/nori_q5_affine_seam_helly_census.cpp.
An independent Python audit checks the 28 satisfying assignments and each of the six forcing paths:
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/d8fc9f576913de1e188e18f27c9167cd3cd2ce31/scripts/nori_q5_three_root_seam_certificate.py.

**Research consequence.** The proposed universal two-root principle is refuted already by an affine coloring. Any higher-dimensional seam-root compatibility proof must admit cooperation among at least three separately satisfiable root systems. The six-path triadic rule exhibits one positive mechanism, but neither a universal three-root bound nor unrestricted NORI1 follows from the finite computations.


#### Two seam-disjoint triadic forcing packets and robust connector-orbit avoidance

The affine \(Q_5\) partial coloring (111) has more robust three-root forcing than Proposition 60 alone states. Its eight projective connector-step roots admit twenty inconsistent triples out of the \(\binom83=56\) possible triples; every one-root and two-root union is satisfiable. In particular, the two triples
\[
\boxed{T_1=\{0,1,4\},\qquad T_2=\{3,6,7\}}
\tag{113}
\]
are disjoint and each admits a six-geodesic contradictory packet.

Proposition 60 exhibits the six-geodesic packet on \(T_1\). For \(T_2\), set
\[
A'=X_{(0,2)},\quad B'=X_{(0,4)},\quad C'=X_{(0,0)},
\quad D'=X_{(1,4)},\quad E'=X_{(1,5)}.
\]
The second packet is:

| Root | Full direction order | Seam root | Forbidden free-orbit assignment |
|---:|---|---:|---|
| 3 | \(0,2,1,3,4\) | 3 | \(A'=1,D'=1\) |
| 9 | \(2,3,0,1,4\) | 6 | \(B'=0,D'=0\) |
| 0 | \(0,2,1,4,3\) | 7 | \(C'=0,E'=0\) |
| 3 | \(2,1,0,3,4\) | 3 | \(B'=1,E'=1\) |
| 2 | \(0,4,3,1,2\) | 3 | \(A'=0,D'=1\) |
| 1 | \(0,3,4,1,2\) | 7 | \(C'=1,E'=0\) |

The first and fifth clauses force \(D'=0\); the third and sixth force \(E'=1\). The second clause then forces \(B'=1\), whereas the fourth forces \(B'=0\). Thus this second six-path packet is inconsistent for every assignment of the two free direction classes, independently of the first packet.

**Corollary 63 (robust connector-orbit avoidance in the affine obstruction).** For the fixed prescribed colors (111), for **every** legal completion of free directions \(0,1\), and for **every** prescribed antipodal edge orbit \(e\) in connector direction \(4\), there is a monochromatic full antipodal geodesic avoiding \(e\). More strongly, a predetermined packet of at most six full rooted geodesics, all avoiding \(e\), guarantees a monochromatic witness under **every** legal completion of the free direction classes.

**Proof.** The connector orbit \(e\) belongs to at most one of the disjoint projective seam-root sets \(T_1,T_2\). Choose the forcing packet belonging to the other set. Each of its six full paths crosses direction \(4\) at a seam root different from \(e\), hence avoids that antipodal orbit. One of the six is monochromatic under every legal free-direction assignment, by the two triadic contradictions above. \(\square\)

This is a positive robustness statement for the same affine partial coloring that refutes universal two-root forcing. It demonstrates that a failed low-Helly-number assertion does **not** imply fragility under connector-orbit flips. Any full NORI1 proof based on critical flips must account for such redundant multi-root forcing networks, rather than expecting one or two seam-root groups to be universally sufficient.

Direct complete-path verification of both packets, their disjoint seam-root sets, the 28 satisfying pair assignments, and all Boolean cases for their six clauses:
https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/a246800447a8c7548c9fb31f4bcaa8781d511d0a/scripts/nori_q5_three_root_seam_certificate.py.
