# Obstruction compatibility and a programme for NORI1 closure

# Obstruction compatibility and a programme for NORI1 closure

## Current assessment and revised closure programme — 19 October 2026

This assessment updates the 17 October survey after surveying the catalogue of 36 research notes created or revised since that publication and examining the principal proofs and limitations, Article XVI composition 47, the current strategic Subsection composition 20, the implication-transport Subsection composition 27, and relevant arguments in the gauge Subsection composition 177. The review audits the principal implications and limitations; finite solver certificates retain their recorded verification status. NORI1 remains open.

The earlier thirty-direction catalogue served as an exploration map. The present assessment selects a narrower programme. Its principal target is the unrestricted nonlinear paired-flat square boundary. The seam-interval formulation supplies a second representation of the same full-class problem. Shortest-path methods remain a secondary route with a specific anchor-production obligation.

### A. What the recent work has accomplished

**Balanced boundary normalization is available.** Article XV supplies a good/bad neighboring pair of perfectly balanced paired-flat colorings whenever NORI1 fails. They differ by one antipodal alternating-square switch. The new two-hit involution preserves the temporal word of every full geodesic meeting the switch set twice. Consequently every red witness on the good side meets the switched set once, strictly internally. This resolves the normalization issue raised in the original item 14 and places balance and criticality in one instance.

**The full-class seam representation has improved.** The unrestricted two-direction formula uses one shared partial coloring and is a bipartite 2-CNF whose satisfying assignments are precisely bad completions. Its later seam-interval theorem permits arbitrary dependence on the connector bit. The layer-defect field may be any antipodally even edge assignment, so an argument may use the proved interval constraints but cannot impose an additional defect identity without proof. Interior and exterior seam formulas each have a canonical satisfying completion. A contradiction must use both families. The finite two-seam-root certificates demonstrate one mechanism in small dimensions; the universal transport theorem remains open.

**Nested-core forcing is a substantial theorem.** A nonsingular principal slope core and a legal parity-peeling order give red geodesics for arbitrary nonlinear phase functions, with a prescribed root count in every parity fiber. The directed feedback criterion and rank-at-most-four theorem extend this mechanism to unbounded matrix sizes. These are mathematically useful results. Their hypotheses retain affine dependence on the within-pair bits.

**Shortest-path geometry has gained useful inequalities.** Endpoint absorption, derivative flux, parallel-face cuts, quadratic cut rigidity, and spectral red-anchor bounds give constraints in a single coloring. The anchored three-face example proves that individually compatible demands can incur a collective surplus. The unresolved step is to derive the required face family and anchors from a hypothetical counterexample.

**The team has also corrected its own relaxations.** Walk pumping shows that several unrestricted-walk energy minimizations recover an existing rooted geodesic-defect quantity. The unanchored weighted-capacity calculation proves that its capacity inequality cannot be violated. The growing-degree blocker barrier closes the bounded-degree version of that relaxation. These results should terminate the corresponding proof attempts.

### B. Where the work has drifted

Four patterns recur in the recent record.

1. **Successive finite classifications.** The paired-gate investigation progressed through three, four, five, and six pairs, then through ranks four and five. The nested-core theorem justified part of that progression by exposing a reusable mechanism. The current rank-five projective compression still leaves both arbitrary rank and nonlinear within-pair dependence open. The next rank computation should be justified by a dimension-uniform reduction or a transfer theorem before it receives further priority.
2. **Equivalent energy refinement.** Causal means, Fourier survival, Gibbs energies, odd-occurrence sampling, and correlated transport yield valid pathwise certificates. Introducing another intrinsic energy with “a uniform sublinear bound would close NORI1” leaves the central upper-bound problem in place. Walk pumping gives a rigorous reason for this concern in several of those formulations.
3. **Conditional certificates without a source theorem.** Red endpoint stars, multiple deep red anchors, a near-transitive spine, a favorable near-full face, and a contradictory implication component each support useful forcing lemmas. The existence of those configurations in the required full class is the next mathematical obligation. Refining their consequences alone does not supply it.
4. **A moving small-certificate target.** Four-path packets, six-path packets, parity diamonds, selector portfolios, and two-root certificates have developed a rich local calculus. A universal theorem may require a certificate whose size grows with dimension. Small examples establish feasibility of a mechanism; they do not justify a universal bound on its size.

The publications generally state these scope limits carefully. The corrective issue is allocation of further investigation and visibility of the unresolved implication. The original broad agenda contributed to this dispersion and is narrowed here.

### C. A scope lemma for the affine paired-gate programme

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

### D. The primary closure obligation

For a paired-flat coloring \(G\), let \(S\) be the eight edges of an antipodal pair of alternating squares, and let \(T_SG\) be the legal square switch.

**Boundary-preservation target.** If \(G\) has a red full antipodal geodesic, prove that \(T_SG\) has one.

The paired-flat parameter space is connected under these switches and contains successful colorings. Therefore this target, in all even dimensions, proves NORI1 through the standard lift.

The existing two-hit transport permits the following fully specified equivalent repair obligation. In the only unresolved case every red full geodesic of \(G\) meets \(S\) in one internal edge. Produce a full geodesic \(Q\) such that every edge of \(Q\) outside \(S\) is red in \(G\), and every edge of \(Q\) in \(S\) is blue in \(G\). The path then becomes red after switching. A full geodesic meets \(S\) at most twice. The strict boundary hypothesis excludes a zero-hit repair directly and a two-hit repair through the inverse temporal-word involution. Hence a surviving repair uses one switched edge.

This is a closure-equivalent target, rather than a newly proved repair theorem. It is narrower than an unspecified request for collective behavior: the admissible configurations, legal move, known transport, and required witness are fixed. The next investigation should seek a root-and-order exchange or a dual obstruction with a well-founded decrease. It may use a number of paths or exchanges growing with dimension.

A prospective proof should state which quantity decreases, why the move preserves the legal common coloring data, and how a terminal obstruction contradicts the strict internal-hit boundary. Connectivity of an exchange graph by itself supplies none of these three conclusions.

The nonlinear gate problem belongs at the center of this route. An affine principal-core argument remains useful when a boundary analysis proves that its hypotheses occur. Imposing those hypotheses at the outset changes the class being attacked.

### E. Secondary routes and the next admissible advance

| Route | Next result that would justify sustained priority | Current stopping condition |
|---|---|---|
| Unrestricted seam intervals | Derive transport between interior and exterior clause families from the interval law in arbitrary partial colorings; or prove a reusable clause-generation induction with a stated invariant. | Further fixed-size packet censuses without a general transport rule. |
| Shortest monochromatic paths | Derive overlapping blocked faces with red anchors strong enough to exceed a proved capacity bound, or prove a uniform sublinear detour estimate. | Further optimization of arbitrarily prescribed anchored face configurations without a theorem producing them. |
| Affine principal-core peeling | Prove the unrestricted-rank matrix theorem, or establish a forcing step for nonlinear \(q\)-gates arising at the boundary. | Increasing the finite rank ceiling alone. |
| Entropy compression | Give an encoding or conditional information inequality with savings on the required full-orbit scale, accounting for overlaps and witness selection. | Independent pivot-square packing, whose established capacity is only \(O(n)\) bits. |
| Causal rounding | Prove a uniform estimate for a nondegenerate path family, such as globally shortest red antipodal paths, using constraints absent from arbitrary walks. | Adding a new equivalent intrinsic energy without an upper-bound mechanism. |
| Turn/Fourier inequalities | Use shared-star or cross-order identities to rule out a realizable badness configuration. | Increasing a bounded scalar moment or localization degree already covered by the relaxation barriers. |

These are research decision criteria. A subsidiary theorem may still merit publication for its independent mathematical value. Its contribution to closure should be stated through the implication it supplies.

### F. Two corrections to the quantitative agenda

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

### G. Grand-conjecture scope and publication discipline

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

### H. Sources for this revision

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


## Historical survey — 17 October 2026

This is a strategic synthesis dated 17 October 2026, prepared in session `session_nori_r11487_1`. It surveys the ten active Articles I and VII–XV, their subsection catalogue, the retired Article II–VI shells, and the research-note catalogue. All fifteen article compositions and the initial 471 note bodies were retrieved; central arguments and obstruction records were examined selectively in depth. Two subsequently published notes were also checked. This is a broad research assessment, not an independent verification of every proof or every finite certificate.

NORI1 remains open in the reviewed record. The recommendations below are research problems, not new closure theorems. Two elementary propositions are proved here to clarify how obstructions may be combined. “Unresolved in the reviewed record” means that no resolution was found in this survey; it does not assert priority or certify that no worker has attempted the question.

The main recommendation is to study compatibility on one legal coloring, retaining the root, direction order, and shared edge variables throughout. The direct Eulerian/rainbow formulation is a leading route within this programme. Extending Hollom-type hypotheses is not a priority.

## 1. The mathematical target and the available reductions

A legal coloring assigns a bit to each undirected edge of \(Q_n\), with \(c(\bar e)=1-c(e)\). NORI1 asks for a monochromatic path between antipodes using every direction once. A full geodesic is determined by a root and a permutation of the directions.

For an ordinary coloring \(f\), let \(A_0(f)\) and \(A_1(f)\) be the roots permitting temporal color words \(0^*1^*\) and \(1^*0^*\), respectively. Reversal gives \(A_1(f)=\overline{A_0(f)}\). The universal paired-root assertion \(A_0(f)\cap A_1(f)\ne\varnothing\), with its quantification over ordinary colorings and dimensions, is equivalent to NORI1 through the odd bridge construction. It does not justify prescribing the root or choosing the two paths independently of their common root.

Three equivalent or sufficient closure targets deserve special attention.

* **Orbit-flip preservation.** If existence of a monochromatic full geodesic survives every flip of an antipodal edge pair, connectivity of the space of legal colorings proves NORI1. A first good-to-bad flip isolates a sharply constrained boundary instance.
* **Sublinear defect or detour.** Let \(\delta(c)\) be the minimum minority-color count on a full geodesic. Cartesian products add \(\delta\). A uniform \(o(n)\) bound therefore proves NORI1. The recent shortest-monochromatic-path result supplies a parallel amplification: if \(L(c)\) is the shortest monochromatic antipodal path length, then \(L-n\) is additive under products. A uniform \(L\le n+o(n)\) also proves NORI1.
* **Entropy loss for bad colorings.** Counterexample-preserving lifts imply that, if any counterexample exists, the family of bad colorings has asymptotically full normalized entropy, including in the balanced regime. A sufficiently strong counting upper bound would contradict this amplification.

These targets offer different ways to avoid proving an unnecessarily rigid local statement.

## 2. What the articles collectively establish

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

## 3. Why progress has repeatedly stalled

### 3.1 Projection removes the dependence needed for selection

A favorable root, an admissible order, and a local exchange often exist separately. The desired path requires their simultaneous realization using the same edge colors. Projecting to a set of roots, a graph of overlaps, a spectrum, or a turn histogram can erase this dependence.

The radial examples are especially informative. Distinct legal colorings can have the same full root/profile incidence and spectrum while having different prefix transport and square curvature. Thus even complete incidence data need not recover the mechanism needed to move a witness. The next invariant must retain some order information.

### 3.2 Stronger quantifiers create false intermediate goals

NORI1 is existential in both root and order. Prescribing a root, demanding adjacent paired roots, fixing an order in advance, requiring bounded-radius repair, or insisting on a large witness density introduces additional requirements. Several such strengthened statements fail for colorings that already satisfy NORI1.

A useful intermediate lemma should therefore be justified by its implication for the existential target, rather than by its resemblance to a familiar induction hypothesis.

### 3.3 General graph and matroid models omit cubical consistency

Eulerian balance, involution symmetry, connectivity, square generation, and abstract exchange can coexist without the desired rainbow path in broader models. Their failure identifies missing cube structure. It does not establish that an argument using commuting cube translations and one shared edge assignment must fail.

Conversely, merely adding another generic connectivity axiom is unlikely to recover that structure. Rooted profile sets need not be delta-matroids, and reachability families need not be greedoids.

### 3.4 Normalization preserves the full difficulty

Counterexample-preserving balancing and distribution lifts make the balanced regime a universal testing ground. They do not make it an easier probabilistic class by themselves. Feed-forward extensions can produce connected interaction graphs while retaining the original difficulty. Cartesian products can dilute witness density and buffer failures in different components.

A proposed simplification must identify a quantity that decreases under the reduction, or a new property that forces a witness despite the embedded core.

### 3.5 Local exchange can spend the direction budget

A walk can be shortened as a graph walk while remaining unsuitable as a geodesic. Holonomy may connect the desired fiber states through a word that repeats directions too often. Eulerian decomposition controls degrees and edge usage, but a segment need not be rainbow.

The missing lemma concerns bounded direction usage together with color compatibility. Ordinary reachability is too weak a conclusion.

### 3.6 Scalar averaging misses an extremal event

A monochromatic geodesic is an extremal event. Formal turn distributions can share many moments with legal examples while assigning no mass to the desired minimum. Small principal Walsh tests can all remain positive. Balanced padding can make low-order path statistics resemble independent bits while retaining a hypothetical bad factor.

These results limit particular summaries. They leave room for conditioned statistics coupled across orders and constrained by shared edges.

### 3.7 Several encodings relocate the same unresolved choice

A faithful equivalence is valuable, but it is not yet a forcing theorem. Moving among galleries, ports, matchings, turns, or return words can repeatedly re-express the same root/order compatibility problem. A new formulation should be evaluated by the new inequality, exchange, or dual certificate it enables.

This diagnosis does not imply that the project has made no progress. The codex now identifies the missing information with much greater precision. The next phase should exploit that precision rather than accumulate additional nearby counterexamples without a named target.

## 4. When mutual obstruction is stronger

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

## 5. Six leading programmes

### Programme A: critical repair with shared-edge clauses

At a first good-to-bad antipodal-orbit flip, every old red full geodesic must meet the removed red edge internally, and no old path can have the opposite edge as its sole blue edge. Endpoint witnesses admit a rotation repair. The boundary condition therefore gives information about many paths simultaneously.

The proposed first goal is a dimension-uniform implication: these shared-edge constraints force either an avoiding red path, an endpoint witness, or an opposite-edge one-defect path. Such an implication would prove flip preservation and close NORI1.

The Q4 surgery certificate is encouraging evidence for structured path families. Q8 examples defeat a repair argument restricted to two previously free edges. The recent Q6 UNSAT computations extend finite critical-profile exclusions, but no independently checked UNSAT proof log is supplied in that note; they should remain labeled computer-assisted evidence.

The next advance should be a recursive implication scheme with an unbounded number of involved edges and a controlled structural invariant. A larger fixed-dimensional SAT instance alone will not provide it.

### Programme B: direct Eulerian/rainbow exchange with a usage budget

Balanced orientations and paired lifts provide Eulerian and covering-space structure. In the paired lift, red fiber moves are involutions \(U_i\); return words encode the desired antipodal transport. The simple-bigon formulation uses each base direction twice. This is an appropriate direct target.

Seek an exchange theorem that changes the root and the return word together, retaining the two-use budget, until the fiber endpoint is antipodal. The number of square commutators may grow with dimension. A fixed bound on that number is incompatible with product examples.

The first useful intermediate result would be a dual alternative: either an allowed budget-preserving exchange improves a well-founded potential, or a cut certificate contradicts antipodal color reversal and cubical edge consistency. Generic Eulerian circuit switching is insufficient; the exchange must use the cube's labeled square relations.

A Minty-inspired potential over walks remains plausible only if it tracks direction multiplicities and proves that its minimum has the required budget. Minimizing ordinary length or repeated vertices does not establish this.

### Programme C: simultaneous flatness and derivative integrability

Badness forces flatness on cross-favorable sites for every relevant pair of directions. The individual active-derivative avoidance example is a successful coloring; it does not establish compatibility of all badness constraints.

Work on one shared Boolean edge assignment. Combine all pairwise flatness implications, source-block root prescription, and the identities among iterated Boolean derivatives. The first goal is to prove that persistent activity avoiding one cross-witness set must create activity on another such set.

A proof would need to move witness information between fibers, not merely show that a surviving cycle exists. The arc-complement theorem supplies a surviving directed cycle after deleting the endpoints of an influence arc. It does not supply two vertex-disjoint cycles.

A useful intermediate theorem would force a reducible feedback block under the full conjunction. Enlarging the solved bound from two exceptional directions to another fixed number is lower priority unless it reveals such a mechanism.

### Programme D: entropy compression across overlapping path networks

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

### Programme E: integrable profile transport with order witnesses

Full path profiles satisfy rotation, reversal, and square locality. Together these laws reconstruct a legal coloring. Rotation and reversal alone admit formal countermodels. Root/profile incidence alone admits twins with different transport behavior.

The first goal is a transport invariant retaining a controlled set of witnessing orders for each profile. It should respond to adjacent swaps using the shared-edge square law and allow the root to move.

One possible target is an augmentation theorem for partial profile coverage under these laws, with a dual certificate that cannot occur in an integrable system. Full direction-profile surjectivity would close NORI1 through direction gauges. A perfect matching between roots and profiles is stronger and should not be imposed without need.

### Programme F: nonlinear star consistency in turn incidence

Write \(s_i(x)\in\{-1,1\}\) for the color sign of the incident direction-\(i\) edge. Besides edge consistency and antipodal oddness, the pair variables \(h_{ij}(x)=s_i(x)s_j(x)\) obey
\[
h_{ij}(x)h_{jk}(x)=h_{ik}(x).
\]
These nonlinear identities couple the turn data. They are absent from many formal moment countermodels.

The first goal is a conditioned, cross-order inequality forcing positive mass at turn grade one. The full two-sector Fourier calculations and existing certificates supply useful starting identities. Fixed low-order scalar moments and small principal Walsh minors are already poor candidates for a universal criterion.

A successful approach must explain why the formal zero-minimum distributions cannot be realized simultaneously across stars and path orders.

## 6. Twenty-four further directions with explicit tests

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

## 7. Tests every proposed route should pass

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

## 8. Source register and limits of the assessment

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


#### Article XVI update: resolved normalization interface and two-hit square transport (17 October 2026)

The normalization compatibility issue listed as item 14 above has now been audited against Article XV. The existing Subsection *Gauge-critical switch cochains and clustered near-good paths* already proves a stronger statement than the originally requested combination: if NORI1 fails, a perfectly vertex-balanced paired-flat bad coloring is adjacent, by a single antipodally paired alternating-square flip, to a good balanced paired-flat coloring. This is the established one-paired-square boundary reduction, originally accompanying the one-Lipschitz defect estimate (EC8). Accordingly, **item 14's joint-balance/square-boundary existence problem is settled by the preceding Article XV work**. The unsolved problem is to eliminate the resulting boundary.

A new unrestricted strengthening is now proved and integrated into that same Article XV Subsection at composition 170, with provenance research note \`note_nori_double_square_temporal_word_transport_r11510\` (session \`session_nori_r11510_3\`).

**Two-hit temporal-word involution.** Let \(T_F\) flip an antipodal pair of alternating squares \(F,\tau F\) on two cube directions. The family of full rooted geodesics traversing two switched edges admits a bijection across \(T_F\) that preserves every temporal color position. In one case both edges lie on the same square and are consecutive; swapping their two directions chooses the alternate two-step route, and the color switch restores their old ordered colors. In the other case the two hits lie in opposite squares and must be the first and last edges; simultaneously exchange the endpoint directions \(i,j\) and translate the root by \(e_i\oplus e_j\). The intermediate edges agree, and alternating color rules restore the endpoint colors after switching. Both transformations are involutions.

**Strict critical boundary.** If a good legal coloring \(G\) and a bad legal coloring \(B=T_FG\) differ by one alternating antipodal square pair, every red full geodesic of \(G\) has precisely one switched edge, strictly internally. A path with no hits remains red in \(B\); a path with two hits is carried by the involution to a red witness in \(B\); a path with one endpoint hit becomes a one-blue endpoint path in \(B\), made red by cyclic root rotation. Combining with Article XV's earlier balanced boundary theorem therefore places the *strict one-internal-hit condition* and *perfect vertex balance* in a single hypothetical bad/good neighboring pair.

This substantially refines Programme A by removing the zero- and two-hit alternatives from its critical-boundary interface. It remains to prohibit one strictly internal switched edge across **all** red witnesses of a balanced good coloring while the switched coloring admits no monochromatic path. No closure theorem for that configuration is claimed.


#### A two-pair compatibility forcing lemma

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


#### Joint obstruction rigidity: three pairs and local active cycles

**Three-pair theorem.** Let c be an arbitrary legal antipodally odd paired-flat edge coloring of Q6 with three direction pairs P_0,P_1,P_2. If no four-dimensional face retaining two whole pairs and freezing the third admits a monochromatic full geodesic, then its three pair gates are signed unary readers arranged around a directed three-cycle. Explicitly, after cyclic relabeling or reversing the cycle, f_i(x)=x_(d_(i-1))+epsilon_i where d_(i-1) is one of the two bits in the previous pair. There are 128 labeled systems of this form (2 cyclic orientations * 2^3 reader choices * 2^3 phases), and every one admits an all-red full antipodal geodesic. Therefore every legal paired-flat Q6 coloring has a constructive red full witness: either extend a red two-pair face by the omitted pair using antipodal oddness, or normalize a reader cycle and use its explicit full red path.

**Proof of rigidity.** For each pair-parity vector p in F2^3, parameterize states by (q_i,q_i+p_i) in each pair. The restricted gate h_i^p(q)=f_i(q,q+p) is independent of q_i and satisfies h_i^p(bar q)=1+h_i^p(q). An odd function of two Boolean inputs is a signed unary reader. Thus each h_i^p reads some q_(sigma_p(i)), with sigma_p(i)!=i. If sigma_p(i)=j and sigma_p(j)=i, then in the four-face on pairs i,j with third pair fixed from that state both gates are nonconstant, so the established R=2E(a)E(b) identity supplies a red full face path. Under the hypothesis this is prohibited. Hence sigma_p is a loopless functional digraph on three labels with no two-cycle, so it is one of the two directed three-cycles.

Because f_i ignores the bits of its own pair, sigma_p(i) is independent of p_i. A change of directed three-cycle orientation changes sigma_p(i) for every i. Thus the orientation is independent of each p_i and is constant over all p. Write sigma(i)=j and sigma(k)=i for the remaining label k. With any fixed assignment of pair j, gate f_k varies under flipping both bits of pair i, because its diagonal restriction reads q_i. The absence of a red two-pair face on i,k then forces f_i to be independent of pair k for every fixed assignment of pair j. It already ignores pair i, so f_i depends only on pair j, and antipodal oddness makes it a signed unary reader of one of the two bits of j. Repeat for all i. Conversely a signed three-cycle has an omitted reader pair in every proper two-pair face, so no such face succeeds.

Swapping labels within direction pairs and translating vertices converts every signed reader three-cycle to f_i=x_(a_(i-1)). From the root with x_(a0)=1 and other bits zero, direction order (b1,a0,a2,a1,b0,b2) is a full all-red antipodal geodesic. This proves the classification and witness statement without solver assumptions.

**All-dimensional active-cycle dichotomy.** For every legal paired-flat Q_(2m), m>=2, and every vector p of pair parities, the induced Boolean network h^p(q)=f_i(q,q+p) is antipodally self-dual and ignores its own component. By the Shih-Dong local-Jacobian fixed-point theorem, some state q has a directed cycle in the local derivative graph: otherwise h^p would have a unique fixed point, impossible because self-duality pairs fixed points antipodally. If no two-pair face succeeds, the local derivative graph has no two-cycle (each such cycle would give mutually nonconstant gates on a common four-face); it has no loops since gates ignore their own pair. Thus every parity fiber contains an active directed cycle of length at least 3. As the derivative graph at q equals that at bar q, there are at least 2^(m+1) distinct (p,q) states with such a cycle. This is an all-dimensional necessary structure for avoiding local two-pair witnesses, not a full geodesic theorem.

**Validation.** A standalone Z3 Boolean encoding of the 24 independent legal pair-gate bits, constrained by failure of every two-pair face, returns UNSAT when any gate is required to be non-unary. A separate independent enumeration validates all 128 three-cycle reader systems, the face obstruction, and existence of a full red geodesic in each. Full detailed proof: /mnt/data/nori_three_pair_global_compatibility.md; verifier: /mnt/data/nori_three_pair_compatibility_verifier.py.

**Scope.** This converts a family of simultaneously failed local forcing conditions into an explicit *globally successful* cycle structure in dimension six. It is an analytic closure proof for the paired-flat Q6 case, independent of earlier exhaustive profile SAT. In higher dimensions, the induced self-dual gates have more inputs and can be nonlinear; local cycles of length at least three do not yet provide a dimension-simple antipodal geodesic. Unrestricted NORI1 remains open.

#### Four-pair pointwise Jacobian cycle rigidity

Let h:F2^4->F2^4 satisfy h_i(q+e_i)=h_i(q) and h_i(q+1111)=1+h_i(q). Suppose for all i!=j and q that D_jh_i(q)D_ih_j(q)=0, where D_jh_i(q)=h_i(q)+h_i(q+e_j).

**THEOREM.** At EVERY q the local digraph j->i iff D_jh_i(q)=1 contains a directed three- or four-cycle. The only possibilities are (a) four signed unary readers, containing a permanent directed 3- or 4-cycle; (b) three unary readers forming a permanent directed 3-cycle and one gate depending on all three other inputs; or (c) four three-input signed-majority gates, in which case the local digraph at every q is a tournament with indegrees (0,2,2,2), and the three nonsource vertices form a directed 3-cycle.

**PROOF.** An antipodally odd Boolean function of three inputs is one of six signed unary projections, two signed parities of three bits, or eight signed-input majority functions. Its essential input count is one or three. If a unary h_j reads i, then D_ih_j is identically one, so h_i cannot depend on q_j under the no-reciprocal hypothesis. Hence unary gates must read other unary gates. A nonempty closed functional reader network without loops or two-cycles on four labels has at least three unary vertices and a 3- or 4-cycle. In the remaining case, all gates use all three inputs. A full parity gate is impossible because all its derivatives are one while every other gate depends on its bit, creating a reciprocal pair. Hence all gates are signed majority functions. For each pair {i,j}, the two reciprocal sensitivities are balanced affine parity functions of the same remaining two bits, and disjoint activation requires them to be complementary. Thus precisely one direction per pair is active at every q. Each majority gate has local indegree zero or two. Since a tournament on four nodes has six arcs, its indegree multiset is (0,2,2,2). The unique source points to the other three; within their induced tournament each has indegree one, so they form a directed triangle. QED.

**PAIRED-FLAT APPLICATION IN DIMENSION EIGHT.** For any legal antipodally odd paired-flat Q8 coloring, let p_i=x_(a_i)+x_(b_i) and q_i=x_(a_i). The induced h_i^p(q)=f_i(x(q,p)) is self-dual and ignores q_i. If every four-face retaining two entire paired direction groups lacks monochromatic full geodesics, no local reciprocal derivative pair can appear: such a pair would make both gates nonconstant on the same four-face, so the established two-pair identity R=2E(a)E(b)>0 would give a red full geodesic there. Therefore all 16 q-states in each of the 16 parity fibers have an active directed cycle of length at least three.

**UNCONDITIONAL DICHOTOMY.** Every legal paired-flat Q8 coloring either has a monochromatic full geodesic in some two-pair four-face, or has an active local directed three- or four-cycle at all 256 vertices. In any four-majority parity fiber the local Jacobian is a tournament with one source and a directed triangle at every q.

**VERIFICATION.** A standalone exhaustive script nori_rank_four_local_cycles.py checks all 65536 self-dual four-gate networks. Of them 1248 avoid reciprocal derivatives at all 16 states: 480 all-unary, 640 with one three-input gate, and 128 with four three-input gates. Every one has the stated pointwise cycle property. Complete proof: nori_rank_four_pointwise_cycle.md.

**SCOPE.** This theorem improves the prior at-least-two-cycle-states-per-parity-fiber bound in the face-free four-pair branch. It does not itself construct a full red geodesic: activation can change when a red step changes the pair-parity fiber. The rank-four Boolean classification does not extend automatically to arbitrarily many paired directions, and unrestricted NORI1 remains open.

#### Four-cycle parity synchronization and mixed-reader forcing

**Theorem.** Let c be any legal antipodally odd paired-flat coloring of Q8. Suppose (i) no four-face retaining two entire direction pairs has a monochromatic full geodesic, and (ii) in every pair-parity fiber, the induced four self-dual Boolean gates are signed unary readers whose reader graph is one directed four-cycle. Then c has an all-red full antipodal geodesic. Indeed, either a full red three-pair face exists, or c is equivalent by cube automorphisms to a signed four-cycle reader.

**Synchronization proof.** Write p_i=x_(a_i)+x_(b_i), q_i=x_(a_i). For each p write h_i^p(q)=q_(sigma_p(i))+alpha_i(p). Gate f_i ignores its own direction pair, so sigma_(p+e_i)(i)=sigma_p(i)=j. Gate i is sensitive to pair j on every face with the other two pair values prescribed at parity p. By (i) and the rank-two identity R=2E(a)E(b), gate j must be constant on pair i throughout those faces. Hence h_j^(p+e_i)=h_j^p, and sigma_(p+e_i)(j)=sigma_p(j). The two four-cycles sigma_p and sigma_(p+e_i) have the same consecutive arrows i->j->sigma_p(j), which determine the entire cycle on four vertices. Thus sigma_p is constant over p. Relabel to sigma(i)=i+1 mod4. Since gate i ignores pair i, and gate i-1 reads pair i on every face, the four-face failure also forces gate i to ignore pair i-1. Hence there exist arbitrary Boolean two-bit functions phi_i such that
 f_i(q,p)=q_(i+1)+phi_i(p_(i+1),p_(i+2)).                  (FC1)

**Parity guard gives a red three-pair path.** If phi_i varies with p_(i+2) for some fixed p_(i+1)=t, freeze pair i+1 at parity t and retain A=i,B=i+2,C=i+3. On this ordinary six-face f_A=epsilon+p_B, while f_B=q_C+phi_B(p_C,p_A), f_C=q_A+phi_C(p_A,p_B). Since f_A is nonconstant in B, failure of the two-pair A,B face forces f_B independent of A. Thus f_B is a signed reader of one bit in pair C. Since f_B is nonconstant in C, failure of the B,C face forces f_C independent of B, making it a signed reader of one bit in A. Swap labels inside A,C as needed and absorb phases, obtaining
 f_A=epsilon+p_B, f_B=x_(a_C)+eta, f_C=x_(a_A)+theta.
Choose the starting root so f_A=1 and f_C=0. The pair-word (A,B,C,A,B,C) then traverses all six directions once, all red. Indeed first A takes b_A, first B toggles parity p_B enabling the complementary A direction; first C takes a_C and changes the reader input of B; second A takes a_A and changes the reader input of C; the subsequent B,C visits take their other directions. The existing paired-endpoint insertion lemma places both members of omitted pair i+1 around the red six-step geodesic, yielding a full red Q8 geodesic.

**No guards gives a signed cyclic reader.** If each phi_i ignores its second argument, phi_i=beta_i+lambda_i p_(i+1). Therefore f_i=q_(i+1)+lambda_i p_(i+1)+beta_i is a signed reader of one bit of pair i+1. Pair-member swaps and vertex translations normalize to f_i=q_(i+1). From the root q_0=1 with every other bit zero, the direction order (b_3,a_0,a_1,a_2,a_3,b_0,b_2,b_1) is red and visits every direction once. Undoing the automorphisms supplies a full red geodesic in c. QED.

**Audit.** In normal form (FC1), each phi_i has sixteen truth tables. Absence of successful two-pair faces forbids dependence on opposite pair parity in both directions of either opposite gate pair (0,2) and (1,3). Each opposite gate pair allows 4*16+16*4-4*4=112 table combinations. Thus 112^2=12544 systems meet (i) in this normal form. Of them 256 have no opposite-parity dependency; the other 12288 have the constructed six-step red face. The separate verifier nori_fourcycle_sync_verifier.py checked all 12544 and explicitly reconstructed the required red routes. Detailed written proof: nori_fourcycle_sync.md.

**Scope.** This positive forcing theorem concerns all legal paired-flat Q8 colorings with the indicated unary four-cycle fiber structure. It leaves majority-type and three-reader-plus-one-extra-gate fiber types unresolved, and does not establish unrestricted NORI1.

#### Dimension-uniform cyclic sensitivity-product forcing and the three-pair closure lemma

**THEOREM.** For any m>=2 let an ordinary edge coloring of Q_(2m) have paired directions P_i={a_i,b_i}, with color rules g_i(x|P_(i-1)) and 1+g_i(x|P_(i-1)). The gates g_i:F2^2->F2 are arbitrary. For the fixed pair-label order W=(0,1,...,m-1,0,1,...,m-1), the number of starting roots giving a red full antipodal geodesic is
 R_W=product_i E(g_i),
where E(g_i) counts sensitive undirected edges of its four-vertex input square. If every gate is nonconstant, at least 2^m roots work for W. No legal oddness is required for this ordinary coloring.

**PROOF.** Choose independently one sensitive input edge e_i of each g_i, of direction d_i in predecessor pair P_(i-1). Prescribe the member used at the first visit to each pair as ell_(i-1)=1+d_i for i>=1 and ell_(m-1)=d_0. For i>=1 let t_i be the endpoint of e_i where g_i(t_i)=ell_i; start predecessor pair i-1 at v_(i-1)=t_i+e_(ell_(i-1)). Thus the first visit to gate i sees t_i, while its second visit sees t_i+e_(d_i) because the predecessor's second step occurs between those visits. Its output flips, so both members of pair i are used. For i=0 choose endpoint t_0 of e_0 with g_0(t_0)=ell_0 and initialize the last pair to t_0. Its first traversal, between the two visits of gate zero, flips direction d_0 and changes gate zero's value. This defines a red full path and uniquely determines all initial pair states. Conversely the sensitive edge crossed by each predecessor between the visits of gate i is recoverable from every successful W-path. These constructions are inverse, proving the formula. QED.

**ORDINARY THREE-PAIR COMPATIBILITY LEMMA.** In an ordinary paired-flat Q6 coloring suppose one parity fiber has three signed unary reader gates in a directed 3-cycle, and every two-pair four-face lacks a monochromatic spanning geodesic. Normalize the parity to zero and the gates to h_i^0(q)=q_(i+1) modulo three. On two P0,P1 faces with P2 equal 00 or11, gate f0 varies in P1, forcing f1 independent of P0 there. Its corresponding values are 0 and1. Hence f1 varies in P2 for every P0 assignment, forcing f2 independent of P1 everywhere. By the initial reader-cycle values, f2 then varies between P0=00 and11 for every P1 setting, forcing f0 independent of P2 globally. Cyclic repetition forces f1 independent of P0 globally. Each gate now reads only the preceding pair, and is nonconstant. The product theorem gives a red full Q6 geodesic.

**NORI1 Q8 APPLICATION.** In any legal paired-flat Q8 coloring without successful two-pair faces, a parity fiber having three unary-reader gates and one three-input gate has a reader 3-cycle among its unary gates, by the previously proved pointwise rank-four rigidity. Freeze the fourth pair. The ordinary three-pair lemma supplies a full red geodesic in the remaining six-dimensional face, and paired-endpoint insertion produces a red full Q8 antipodal geodesic. Thus the three-reader-plus-one-extra-gate type is excluded by mathematical forcing. The four-majority type remains an open branch.

**VERIFICATION.** The script paired_cycle_product_verifier.py exhaustively checks 256 two-gate and 4096 three-gate systems and tests additional four- and five-gate systems. Detailed complete manuscript nori_cyclic_pair_sensitivity_product.md. The formula holds in every dimension; it is an unrestricted-dimensional forcing tool for the specified pair-reader structure, and the general NORI1 conjecture remains open.

#### Majority-fiber transport: a static fixed word and a seven-word common-coloring portfolio

**SCOPE.** Work continuing Article XVI's unrestricted compatibility programme. One proved constructive theorem concerns static four-majority gates, while the general parity-dependent seven-word forcing assertion is a finite UNSAT finding awaiting a hand derivation or independently checked UNSAT proof log. NORI1 remains open.

**THEOREM A: a common static majority word.** Let h_i:F2^4->F2 ignore q_i and obey h_i(q+1111)=1+h_i(q). Suppose all h_i have three essential inputs, and no state has reciprocal nonzero derivatives D_jh_i D_ih_j. For the red paired-matching system with gates h_i independent of paired parity bits, the fixed pair-label word W=(3,2,1,2,0,3,0,1) is a red full antipodal geodesic from ONE and only one starting q in F2^4. Consequently it succeeds from sixteen full Q8 roots, one per initial pair-parity vector.

**Proof.** Each h_i is a signed majority, h_i(q)=Maj(q_j+a_ij:j!=i). For unordered i,j and complementary k,l the absence of reciprocal derivatives is equivalent to a_ik+a_il+a_jk+a_jl=1. These six F2-linear equations on twelve signs have rank five. Fix a reference solution h*_0=Maj(q1,q2,q3), h*_1=Maj(q0,1+q2,q3), h*_2=Maj(1+q0,1+q1,q3), h*_3=Maj(q0,1+q1,q2). All solutions are h_i(q)=h*_i(q+t)+s_i for some t,s in F2^4, with only the common global redundancy (t,s)~(t+1111,s+1111). For each of sixteen s, direct substitution in W gives the sole successful q=(s1,s3,1+s3,s1)+t. An independent 128-network by 16-root exhaustive checker verifies this short substitution and uniqueness. QED. A general paired-flat coloring depends on pair parity, so the static theorem does not apply without a transport argument.

**GENERAL Q8 SAT PORTFOLIO.** Let c be an arbitrary legal paired-flat Q8 coloring. Suppose that at one parity fiber, after translation and pair-member relabeling, f_0 restricted to diagonal pair inputs is Maj(q1,q2,q3), and that no four-face retaining P0 and one other complete pair contains a red full geodesic. Then at least one of the opposite six-faces P0=00 and P0=11 contains a red full three-pair geodesic with pair-label word among
  121323, 213123, 213132, 213231, 231231, 312123, 312321.
Such a red face geodesic extends to a red full Q8 antipodal geodesic by the established paired-endpoint insertion theorem.

**Computational verification of portfolio.** Use 256 Boolean gate variables v_(i,s) (64 per pair), 128 antipodal-oddness equations, and eight fixed f0 majority values. For every P0,Pj four-face, forbid a red full face geodesic by demanding that at least one of its two gates is constant on that face (rank-two identity R=2E(a)E(b)). For each chosen pair word, each rooted geodesic on faces P0=00 and11 and each first-member choice in the three retained pairs, forbid the all-red path by a six-edge Boolean blocking clause. After removing repeated clauses there are 7168 path constraints. Z3 returns UNSAT. Removing any one of the seven entire pair-word families yields SAT; this was separately checked seven times. This is a finite reproducible SAT implication, with a much smaller order family than all possible three-pair words. No proof-log checker or short paper proof has yet been obtained, and minimality among all possible portfolios is not claimed.

**LESSON FOR UNRESTRICTED NORI1.** The static majority theorem has a one-word constructive witness. Pair-parity dependence invalidates the single-word guarantee; a direct SAT attempt with the one static word is satisfiable. Restoring the simultaneous no-two-pair-face compatibility restrictions makes seven words sufficient in the full parity-dependent system. Pairwise cross-face equalities alone, even combined with oddness, are insufficient; a separate SAT model satisfies those weaker constraints while avoiding red full paths on both candidate six-faces. These results localize the required transport to specific joint cross-parity constraints rather than separate scalar influence counts.

**FILES.** Full mathematical and computational audit: /mnt/data/nori_majority_joint_transport.md. Reproducer: /mnt/data/nori_majority_transport_certificate.py. Generated standalone SMT-LIB2 instance: /mnt/data/nori_majority_seven_word.smt2. The checker verifies the 128-network theorem without external packages and obtains the seven-word UNSAT result with installed libz3.so.4.

#### Fiberwise parity-root forcing in Q6 and the full paired-flat Q8 computational audit

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


#### Affine red-return holonomy and joint phase forcing (18 October 2026)

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

#### Five-pair phase-immune forcing and transported-incidence cancellation

Let N=2m and let a legal paired-flat coloring have pair-parity bits p_i=x_(a_i)+x_(b_i) and first-member bits q_i=x_(a_i). Suppose its gate has form f_i(p,q)=a_i dot q + theta_i(p_except_i), with odd off-diagonal slope row a_i fixed independently of p, and arbitrary Boolean phase function theta_i. This permits nonlinear dependence on pair-parity bits.

**DIMENSION-UNIFORM TRANSPORTED-INCIDENCE LEMMA.** Let S_i=I+e_i a_i^T. For any double-occurrence pair-label word w=(i_1,...,i_(2m)) and starting parity p, set p_t=p+sum_(s<t)e_(i_s), L=S_(i_(2m))...S_(i_1), and v_t=S_(i_(2m))...S_(i_(t+1)) e_(i_t). The red return equation is
  (L+I)q=1+sum_t v_t+sum_t theta_(i_t)((p_t)_except_i_t) v_t.
The word admits a full red antipodal path from some q for EVERY assignment of the independent phase truth values iff, for all z in ker((L+I)^T), (1) z dot (1+sum_t v_t)=0 and (2) for each phase key (i,u), sum_(t: i_t=i and (p_t)_except_i=u) z dot v_t=0. Proof: the right side must be orthogonal to every left-null vector for all independent phase variables, forcing each affine coefficient to vanish. When these conditions hold and k=corank(L+I), every phase assignment has 2^k red starting q-roots in the prescribed parity fiber. This is a shared-coloring compatibility condition expressed through transported occurrence vectors.

**COMPUTER-ASSISTED FINITE THEOREM IN Q10.** For m=5, every one of the 32768=8^5 odd off-diagonal slope matrices admits a double-occurrence word whose transported-incidence conditions hold; hence EVERY one of the 2^95 corresponding legal paired-flat Q10 colorings has a red full antipodal geodesic starting in EVERY prescribed pair-parity fiber. The witness word depends only on the slope matrix, not on the 80 arbitrary nonlinear phase bits. The 32768 matrices form 324 relabeling classes under S5. Independent Python and C++ implementations test all 39480 admissible double-occurrence pair words, checking all 324 class representatives. Every class succeeds. With the first word chosen by the deterministic search, the corank distributions are: k=0: 83 classes/8848 labeled matrices; k=1:129/12800; k=2:43/4760; k=3:69/6360. Thus the selected order guarantees respectively 1,2,4,8 red starting roots q for every phase assignment. Direct red-step trajectory checks in 1296 independently sampled class/phase instances reproduced those root counts.

**FILES.** Full proof nori_affine_m5_static_transport.md; standard-library independent verifier nori_affine_m5_static_cover.py; C++ verifier nori_m5_phase_exhaust.cpp. The parent prior note note_nori_affine_holonomy_joint_phase_forcing_r11510 already proves the general affine return mechanism and the m=3,4 cases. This is a dimension-ten extension and a more geometric phase-cancellation criterion, not a complete proof of NORI1.

**RESEARCH BOUNDARY.** The existence of such a phase-immune word for every static odd slope matrix in arbitrary dimension remains unproved. For general legal colorings the slope rows may themselves depend on p and may be nonlinear in q, so the present sufficient criterion does not apply.

**Extended transported-incidence scope.** For any fiberwise-affine paired-flat gate f_i(p,q)=a_i(p) dot q+theta_i(p_except_i), the transported-occurrence proof remains valid with step-dependent shears S_t=I+e_(i_t) a_(i_t)(p_t)^T along the fixed pair-parity trajectory of the selected word. The same left-null constant and phase-key coefficient cancellation conditions are necessary and sufficient for that word to succeed from some q for every phase assignment. Only the positive Q10 classification assumes a_i is independent of p; the algebraic cancellation criterion applies to arbitrary parity-varying affine slope rows.

#### Isolated-chord corank rigidity for phase-immune geodesic returns

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

#### All-dimensional double-sweep determinant forcing



Let A be a zero-diagonal odd-row slope matrix independent of pair parity, while phase functions theta_i(p_except_i) are arbitrary Boolean functions. For any permutation pi of the pair labels let T_pi=S_(pi_m)...S_(pi_1), with S_i=I+e_i a_i^T; the double sweep w=pi pi has linear return matrix L_w=T_pi^2.

**THEOREM.** det(L_w+I)=det A over F2, and the word pi pi is phase-immune if and only if A is nonsingular. If A is nonsingular, that SAME prescribed word yields a red full antipodal geodesic from a unique starting q in EVERY prescribed parity fiber, for EVERY choice of nonlinear phase functions.

**PROOF.** Relabel so pi=(1,...,m), write A=B+C with B strictly lower triangular, and let delta=T_pi q+q. During one sweep each bit changes once; at step i,
 delta_i=(Aq)_i+sum_(j<i) a_ij delta_j.
Hence (I+B)delta=Aq and T_pi+I=(I+B)^(-1)A. As I+B has determinant one, det(T_pi+I)=det A. In characteristic two T_pi^2+I=(T_pi+I)^2, proving det(L_w+I)=det A. If A is nonsingular, every affine return equation has one q solution. If A is singular, the chord diagram of pi pi is fully interlaced (with no isolated chords). The isolated-chord theorem already proved in this note then precludes phase immunity. QED.

**GRAPH COROLLARY.** Interpret a_ij=1 as an arc j->i. Since det A counts directed spanning cycle covers modulo two, an odd number of cycle covers (including a unique cycle cover) guarantees a red full antipodal geodesic in every parity fiber for every phase assignment, using any double sweep. This is a graph-theoretic, unbounded-dimensional positive forcing condition, not a necessary condition.

**INDEPENDENT AUDIT.** The checker nori_double_sweep_gauss_seidel_check.py tested all 256 odd slope matrices at m=4 (88 nonsingular) and all 32768 at m=5 (10048 nonsingular), comparing the sweep rank and the phase-immune return condition against det A. All passed. Complete proof nori_double_sweep_gauss_seidel.md. For singular A other, partially noninterlaced words may still be phase-immune.


#### Nested principal-core double sweeps and odd-indegree parity peeling

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

#### Nested phase forcing with parity-varying affine slopes

 The nested forcing proof does not require slopes independent of pair parity. Let f_i(p,q)=a_i(p) dot q+theta_i(p_except_i), with a_i(p) odd-weight, zero on self, and independent of p_i. Fix a prescribed starting parity, outer labels i_1,...,i_k, and an inner double-occurrence pair word v on complementary labels R. Let p^(t) be the parity state before the first outer occurrence of i_t; require sum_(s<t) a_(i_t)(p^(t))_(i_s)=0 for every t. Along the inner parity trajectory after the outer prefix, let L_(R,v) be the homogeneous affine-return matrix acting on inner q_R, using time-dependent slope shears evaluated at each visited parity. If det(L_(R,v)+I)=1, then the nested word i_1...i_k v i_k...i_1 gives precisely 2^k red full antipodal starting q-roots in the prescribed parity fiber, for ANY choices of phase truth tables. Proof: the inner return equation has a unique q_R solution for each arbitrary fixed postprefix outer q-state; during nested return, each outer gate has the same coefficients and phase at its two occurrences because all other parities are restored and it ignores its own parity. Its output changes by the odd sum of slope entries on inner labels, hence the two red steps traverse opposite directions. The first outer prefix is bijective. This is an all-dimensional positive criterion, not a universal existence theorem for parity-varying slopes. A separate simulator tested 2000 random five-pair systems with varying slope tables and nonlinear phases; for each, it directly simulated all 32 starting q-states and found precisely eight red antipodal roots for the selected nesting.



#### Nonlinear nested-pair gluing and a three-pair transfer theorem

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


#### Complete six-pair peeling and directed feedback-core forcing (18 October 2026)

**Finite theorem (computer-assisted).** Every zero-diagonal 6x6 binary matrix A satisfying A1=1 has an ordered deletion i_1,...,i_k (0<=k<=4) with sum_(s<t) a_(i_t,i_s)=0 at each step and nonsingular remaining principal matrix A[R,R]. A portable C++17 verifier explicitly enumerates all 16^6=16,777,216 such matrices and performs subset-reachability plus binary Gaussian elimination. There are no failures.

**MINIMUM DELETION COUNTS.** k=0:5,000,192; k=1:7,958,848; k=2:2,933,900; k=3:658,510; k=4:225,766. Total 16,777,216. This table counts the smallest feasible k for each matrix, not merely the first successful subset in numerical order. An independently written Python audit verified positive results on 15,000 sampled six-pair matrices, and a separate red-path simulator validated predicted 2^k roots for 2,000 random six-pair nonlinear-phase instances.

**NORI1 CONSEQUENCE.** By the established nested-core forcing theorem, every legal paired-flat Q12 coloring with fixed odd affine q-slope matrix A and arbitrary nonlinear parity-phase gates has a red full antipodal geodesic rooted in EVERY prescribed pair-parity fiber. There are 2^24 eligible coefficient matrices and 2^192 possible phase tables, covering 2^216 such colorings. The pair order is selected from A alone and guarantees 2^k starting q-states in each fiber.

**ALL-DIMENSIONAL FEEDBACK-CORE THEOREM.** Put a directed influence arc j->i when a_ij=1. Suppose some label set R satisfies det A[R,R]=1 and the induced subgraph on D=[m]\R is acyclic. Deleting D in reverse topological order is a valid parity peel, because no newly deleted vertex receives an arc from a previously deleted vertex. The nested-core word produces 2^|D| full red geodesic roots in each prescribed parity fiber for arbitrary nonlinear phase assignments. This gives a simple constructive graph certificate for any dimension.

**SCC CYCLE-INTERSECTION COROLLARY.** In particular, suppose NO strongly connected component contains two vertex-disjoint directed cycles. For each cyclic SCC H choose a shortest directed cycle C_H. It is an induced cycle (a chord would create a shorter directed cycle), so the corresponding adjacency submatrix is a cyclic permutation matrix with determinant one. Their union R has block-triangular principal adjacency, hence det A[R,R]=1. Every cycle lies within an SCC and meets C_H by hypothesis; thus the complement D is acyclic. The feedback-core theorem applies. This is an unbounded-dimensional forcing theorem for potentially singular influence matrices and arbitrary nonlinear phase gates. A separate full graph enumeration verified the criterion for 8/8 matrices on three labels, 231/256 on four labels, and 17,664/32,768 on five labels.

**PRINCIPAL-MINOR PARITY LEMMA.** Every zero-diagonal A with A1=1 has an odd number of nonsingular principal minors of order at least two. Over F2, det(I+A)=sum_(R subset [m]) det A[R,R], with det(empty)=1. But (I+A)1=0 so det(I+A)=0, and singleton principal minors vanish. Therefore sum_(|R|>=2) det A[R,R]=1. This proves that an invertible principal core ALWAYS EXISTS; the general conjecture asks additionally for one accessible through legal parity peeling.

**STATUS AND LIMITS.** The six-pair conclusion is a complete finite computation with reproducible source, not a dimension-uniform proof of the odd-matrix peeling conjecture. The SCC-feedback criterion is proved in all dimensions, but does not cover every odd matrix (on five labels it covers 17,664 of 32,768). Full NORI1 allows parity-varying affine slopes or non-affine dependence on q; neither is resolved by the finite static-slope result.

**AUDIT FILES.** /mnt/data/nori_six_pair_peeling_feedback_report.md, /mnt/data/nori_matrix_m6_minpeel.cpp, /mnt/data/nori_matrix_m6_exhaust.cpp, /mnt/data/nori_m6_independent_audit.py, /mnt/data/nori_feedback_cycle_test.py, /mnt/data/nori_nested_direct_paths.py. Research archive /mnt/data/nori_six_pair_peeling_feedback_bundle.zip.

#### Rank-four column reduction and four-column zero-sum compatibility forcing

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

### Independent rank-five affine-coset certificates and the twelve-label barrier

This update replaces the preliminary solver-only eight-point and twelve-label checks with three standalone exhaustive C++17 certificates. The matrix is a zero-diagonal odd-row binary matrix \(A\); a legal peel deletes labels whose rows have even parity toward earlier deletions. Prior results prove peeling for rank at most four and compress a minimal rank-five obstruction to nonzero quotient columns of \(\mathbb F_2^4\) with at most one duplicated quotient class.

**Lemma 1 (unconditional affine eight-plane).** For all eight quotient columns \(t=(1,u)\), \(u\in\mathbb F_2^3\), and arbitrary permitted lifts, some four-point affine plane has zero full-column sum and permits a legal deletion of its four labels. The verifier normalizes one of the eight four-bit row factors to zero by the common gauge translation and enumerates the remaining seven. The search visits \(1,1,16,256,2176,34816,49152,0,0\) partial nodes at successive depths, with no survivors. If the eight total lifted columns have odd sum, deleting this plane leaves a four-label odd-row matrix, handled by the earlier theorem.

**Lemma 2 (even-sum affine eight-point closure).** If the eight columns have total sum zero, all eight labels have a legal full peel. An independent integer-only verifier checks all \(134217728\) gauge-normalized even-sum assignments. Complementary peelable four-planes certify \(134167552\), while direct Boolean reachability on all \(256\) deletion subsets certifies the remaining \(50176\). There are no failures. This replaces the former eight-point SMT UNSAT assertion with a checked finite enumeration.

**Lemma 3 (twelve-label projective quartet).** For quotient labels \(3,5,6,7,9,10,11,12,13,14,15,15\), the duplicated quotient columns having opposite lift bits, one of eleven fixed candidate quotient-zero-sum quartets is a full-column-zero-sum quartet that permits complete legal peeling. The proof enumerator needs only the eight indexed labels \(0,2,3,5,6,9,10,11\), fixing one four-bit gauge vector to zero, and visits \(1,1,16,256,2176,2048,32768,15360,0\) nodes. In the local four-label test, the 16 exceptional even-row matrices are precisely a bidirected triangle with no outgoing triangle arcs to the fourth label; the fourth row may have any even pattern. This characterization has an independent 256-case audit.

**Theorem (rank-five threshold).** With the preceding rank-four theorem and minimal-counterexample compression, no size-minimal rank-five counterexample has \(m\ge12\) pair labels. The earlier projective reductions for \(m=13,14,15\) now use Lemmas 1 and 2 instead of solver assumptions. The twelve-label configuration with one duplicated class is eliminated by Lemma 3 and minimality: after its zero-sum quartet deletion, the odd-row residual is strictly smaller and has rank at most five. For twelve distinct classes the three missing points form a quotient projective line. Its three complementary four-point cosets have odd total lift parity; choose an odd one as the inside of a containing hyperplane, making the outside eight-point affine coset even-sum. Lemma 2 removes that outside set, leaving a four-label odd-row residual.

This is a finite-audit strengthening, **not** a proof of rank-five closure in the remaining \(7\le m\le11\), of the arbitrary-rank peeling conjecture, or of unrestricted NORI1. Full report and integer-only source files: `nori_rank5_independent_finite_closure.md`, `nori_affine8_plane_exhaust.cpp`, `nori_affine8_even_full_exhaust.cpp`, `nori_rank5_local_quartet_exhaust.cpp`; research note `note_43efdcdab134f6eee75a199b`.


#### Analytic Fano quartet forcing and projective row-distance rigidity

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

### Rank-five parity-peeling closure in all dimensions

**Theorem (computer-assisted, all sizes).** Every \(m\times m\) binary matrix \(A\) with zero diagonal, \(A\mathbf1=\mathbf1\), and \(\operatorname{rank}A\le5\) admits a legal parity peel \(i_1,\ldots,i_k\) whose remaining principal matrix \(A[R,R]\) is nonsingular. Consequently, by the nested-core forcing theorem, every legal paired-flat coloring with a fixed affine fiber-reader matrix of rank at most five and arbitrary nonlinear parity-phase functions has a red full antipodal geodesic in every prescribed parity fiber.

**Proof framework.** Choose a smallest counterexample of rank at most five. The preceding rank-four theorem and complete at-most-six-label finite base force rank five and at least seven labels. The established column compression factors \(A_{ij}=(z_i+z_j)\cdot t_j\), where \(t_i\in\mathbb F_2^4\setminus\{0\}\), \(\sum_i t_i=0\), at most one quotient class is duplicated, and any duplicate has opposite full lifts. A common shift of all \(z_i\) preserves the matrix, permitting gauge \(z_0=0\).

All seven- and eight-label quotient multisets are classified under \(GL(4,2)\) by elementary transvections. There are two orbits at seven labels and three at eight. Independent finite audits check \(4194304+8388608\) eligible seven-label matrices, \(67108864\) matrices in the duplicated eight-label orbit, plus small finite certificates for the distinct and affine-coset eight-label orbits. All succeed.

At nine labels there are four quotient orbits. For every orbit, an independent bounded search shows that some proper subset of three, four, or six labels has zero full-column sum and admits complete legal peeling. Deleting it preserves odd row sums and yields a smaller matrix of rank at most five, contrary to minimality.

At ten or eleven labels the quotient classification has respectively four or two orbits, each containing one of the two six-column patterns \((1,1,2,3,4,5)\) or \((1,2,3,4,5,6)\). An independent six-column verifier checks all \(524288\) and \(1048576\) normalized permitted assignments, respectively. Every assignment has a peelable zero-sum block of size three, four, **or six**; the whole six-column option is essential. Again minimality rules out a counterexample.

For twelve or more labels, the preceding projective hyperplane reductions and the separately checked eight-point affine-coset and twelve-point quartet certificates force a peelable zero-sum block, or rule out the column multiplicity pattern by parity. These exhaust all possible minimal sizes, proving the theorem.

**Reproducibility.** Standalone integer-only enumeration, subset reachability and binary Gaussian elimination are supplied in \`nori_rank5_complete_proof_bundle.zip\` with proof \`nori_rank5_matrix_closure_complete.md\`. The principal research note is \`note_92ce6bdf09135a7de5fb4d8a\`. This is **not** unrestricted NORI1: higher-rank matrices, parity-varying affine slopes, and nonlinear fiber dependence remain open.


## Scope audit: why bounded terminal components do not control unrestricted NORI1

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

### General terminal seams and the ordinary one-change geodesic problem

There is an exact unlimited-rank version of the finite seam mechanism. Fix \(k\ge1\) and let \(A\) be any ordinary paired-flat binary coloring of undirected edges of \(Q_{2k}\); it need not be antipodally odd. Define its dual \(A^\vee(e)=1+A(\bar e)\). A *red seam completion* is a full antipodal geodesic using each of the \(2k\) original directions once, with an initial consecutive block of edges red in \(A\), followed by a final consecutive block red in \(A^\vee\). The transition occurs at a common vertex and both blocks may have length zero.

**Proposition (exact one-change transfer).** Such a red seam completion exists if and only if \(A\) has a full antipodal geodesic with at most one color change. More precisely, red seam completions with specified starting vertex \(x\) correspond bijectively to red-then-blue antipodal full geodesics of \(A\) with the color-change vertex at \(x\).

*Proof.* Let a red seam start at \(x\), traverse the \(A\)-red prefix to \(u\), then traverse the \(A^\vee\)-red suffix to \(\bar x\). Reverse the first segment, obtaining an \(A\)-red path from \(u\) to \(x\). Complement the vertices and reverse the second segment; because \(A^\vee(e)=1+A(\bar e)\), this is an \(A\)-blue path from \(x\) to \(\bar u\). Their concatenation is a full antipodal geodesic with word red followed by blue; the sets of original directions are disjoint and exhaust all \(2k\) labels. Conversely, start with an \(A\)-geodesic \(u\to x\to\bar u\) consisting of a red prefix and blue suffix. Reverse its red prefix and complement/reverse its blue suffix to construct the red seam \(x\to u\to\bar x\). These operations are mutually inverse. A blue-then-red one-change geodesic can be reversed, so existence with at most one change is equivalent. \(\square\)

If \(A\) is itself antipodally odd, any one-change full geodesic becomes monochromatic after cyclic root rotation at its color-change vertex: the antipodally translated initial color block joins the final block with its color complemented. Thus the universal arbitrary-\(k\) paired-flat seam-completion assertion would imply unrestricted NORI1 through the established paired-flat lift. It is a full-strength general forcing problem, not a routine extrapolation of the finite one-, two-, and three-pair checks. The original cube directions remain distinct throughout the correspondence.

The fiberwise finite seam property asks for more than one unrooted one-change path: the pivot \(x\) must occur in every prescribed pair-parity fiber. The distinction matters. No all-\(k\) proof, uniform root-selector theorem, or reduction of arbitrary critical colorings to bounded-size terminal blocks is currently available.

**Research decision.** Close the bounded-pair classification programme until an independent structural theorem derives its hypotheses for arbitrary critical colorings. Transfer research effort to the unrestricted paired-flat square-switch boundary and, separately, to dimension-uniform red/blue one-change exchanges in ordinary paired-flat systems. Both target arbitrary nonlinear truth tables; finite examples should be used to refute a sharply formulated general exchange lemma rather than to raise the bounded rank ceiling.
