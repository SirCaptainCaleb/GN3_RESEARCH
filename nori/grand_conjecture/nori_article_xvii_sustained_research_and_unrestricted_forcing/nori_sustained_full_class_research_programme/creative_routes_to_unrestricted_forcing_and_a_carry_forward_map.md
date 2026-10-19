# Creative routes to unrestricted forcing and a carry-forward map

# Creative routes to unrestricted forcing and a carry-forward map

This programme follows the assessment in the preceding Subsection. Its questions are open; the proposed mechanisms are hypotheses for investigation. None is asserted to follow from the known necessary conditions. The ranking reflects present evidence and can change when a stronger argument appears.

## 1. Whole-gate clause transport at a strict critical square

**Statement to attack.** For arbitrary legal fixed gates f_j, j≠i, prove that the geometric 2-CNF forbidding every red full antipodal geodesic has no satisfying legal assignment of the complete gate f_i. A potentially more focused first target is that a satisfying assignment cannot have a one-bit neighbor supporting a red full geodesic. If proved for every pair i and every setting of the other gates, this boundary-preservation statement closes NORI1.

The whole-gate variables are indexed by outside parity u and complementary outside fiber orbit [v]. Each fixed geometric full path uses two original directions of pair i, so, after its other edges are required to be red, its success is a conjunction of at most two gate literals. The bad assignments are precisely those satisfying all clauses forbidding these conjunctions. Clause origin matters: keep the path, root, direction order, and the two evaluation sites with each clause.

**Obstruction.** An arbitrary 2-CNF can have a satisfying vertex adjacent to a nonsatisfying vertex. Nonnegative quadratic witness counts can also vanish. Neither the low polynomial degree nor standard implication-graph theory forces the desired contradiction. The interior and exterior seam zones each have canonical models. Small universal seam-root bounds have already failed.

**Retained ingredient.** All clauses come from one shared coloring, and the two visits of a pair have a direction budget and antipodal relation. Adjacent direction exchanges, root rotations, and the common-prefix switch cocycle relate their supporting paths. This is information absent from arbitrary 2-SAT.

**First creative task.** At a hypothetical critical bit h_s, examine implication paths beginning at its two literals. Ask whether the strict internal-hit condition forces propagation into a second gate-table site and whether path exchange closes that propagation under a proved rule. Permit the implication paths and the collection of supporting geodesics to grow with dimension. The hoped-for output is either a contradictory implication cycle or a repair path assembled with all original directions distinct.

**Continue if** a transport rule derives a new clause from witnessed clauses while preserving their original-coloring interpretation, or if a dual obstruction can be shown incompatible with antipodal path transport. **Change direction if** the rule works only on hand-picked packets, an affine truth table, a fixed number of sites, or an unsupported global compatibility assumption.

This combines Article XVI's Programmes A and the coherent seam line with the new whole-gate law. Whole-gate clauses and the earlier two-direction clauses are related tools; their variables and hypotheses must be kept distinct.

## 2. Coupled reachability cuts, with roots allowed to move

**Statement to attack.** For every legal cube coloring c, prove that at least one root has a full red direction-simple path. For a fixed root x, let R_x consist of subsets A⊆[n] for which there is a red path from x to x⊕1_A using each direction of A once. Then
\[
R_x(\varnothing)=1,\qquad
R_x(A)=\bigvee_{i\in A}
\left(R_x(A\setminus\{i\})\land
[c_i(x\oplus\mathbf1_{A\setminus\{i\}})=0]\right).
\]
The target is R_x([n])=1 for some x. If every root fails, each family has a blue exit boundary in its Boolean path lattice.

**Obstruction.** Individual rooted failures occur in successful legal colorings. Cut size or one root's accessible family therefore cannot force the conclusion. Complementary endpoints and independently selected partial paths need not glue.

**Retained ingredient.** The boundaries for different roots reuse the same undirected edges. Their exit labels are constrained by edge equality, antipodal complementation, and direction-support overlap. Preserve the witnessing subsets rather than only cardinalities or endpoints.

**First creative task.** Translate one root and compare its minimal failed prefixes with those at the translated root. Seek a cancellation or augmentation rule for the entire family of boundaries. A promising dual statement would rule out a coherent choice of separating cuts at every root, rather than show that a prescribed cut must be small. Work first with the recursion above; introducing a new state space is unnecessary unless it simplifies that relation.

**Continue if** a cross-root inequality or exchange uses a shared edge in incompatible ways under universal failure, while retaining used-direction sets. **Change direction if** the argument reduces to an arbitrary family of downsets, loses path witnesses, or assumes a root can be prescribed.

This carries forward items 10, 17 and 18 of the previous catalogue. There is relevant earlier reachability and cut work; the underdeveloped obligation is simultaneous cross-root incompatibility, not the invention of another cut representation.

## 3. Simultaneous derivatives and cross-witness transport

**Statement to attack.** Derive, in an arbitrary hypothetical bad coloring or strict critical boundary, a reducible witnessed configuration or a red full path from the full collection of cross-favorability flatness conditions and shared Boolean derivative identities.

For an edge rule c_i, the derivatives D_jc_i(x)=c_i(x)+c_i(x+e_j) satisfy D_kD_jc_i=D_jD_kc_i. For pair gates, temporal differences along a red trajectory telescope between its two visits. A successful full pair word requires an odd total change for each pair gate between those visits. The new critical curvature condition adds noncommutation immediately next to the unique switched hit.

**Obstruction.** Active derivatives can avoid one selected witness set. Dense dependency graphs and large feedback number can coexist with failed conditional certificates. Formal derivative assignments need not come from one legal coloring. Moreover the opposite-layer seam defect field can be arbitrary subject to its proved evenness law; an extra identity for that field cannot be borrowed from derivatives of a single fixed gate.

**Retained ingredient.** Use finite differences of the same functions, at specified vertices, together with witnessed paths. A graph recording only whether some derivative is nonzero discards too much.

**First creative task.** Starting with the two noncommuting neighbors of a strict one-hit witness, transport the resulting nonzero differences around an overlapping cube of exchanges. Determine whether integrability forces activity at a different witnessed site, or whether it yields a finite state that can be extended until a repair appears. No bound on the number of sites is required.

**Continue if** one can prove a witness-preserving activity transfer, or a reduction whose complexity decreases while retaining criticality. **Change direction if** only another forbidden fixed-size dependency graph is obtained, or if the transported derivative is evaluated where no relevant witness has been established.

This retains Programme C, conditional influence decomposition, and cross-face transport. It should be explored jointly with the first two routes when they impose conditions on the same instance.

## 4. Order-sensitive profile transport and integrable turns

Two established representations retain much more information than a scalar energy. They deserve separate exploration because neither requires affine gates or a bounded interaction graph.

**Profile target.** Prove full direction-profile support, or the weaker uniform estimate
\[
|\mathcal W(c)|\ge 2^{n-o(n)}
\]
over the balanced legal class. The established profile product law makes the latter sufficient for NORI1. Root and order witnesses must accompany supported profiles.

**Turn target.** For the incidence disagreements d_ij(v), retain the triangle, square, antipodal, and odd cyclic-parity conditions of the reconstruction theorem. These determine a legal coloring up to global color complementation. Prove that some full rooted direction order has cyclic turn sum Θ=1. The reconstruction identity μ(c)=min Θ−1 then yields a monochromatic full geodesic.

**Obstruction.** Affine span, low-order marginals, first-direction pairing, profile counts, and rotation cycles can all be compatible with missing constant profiles in formal models. Successful legal colorings have strict nonoptimal local turn minima. Shannon profile entropy can have a linear deficit even in successful product examples. Increasing the number of scalar moments does not address these barriers.

**Retained ingredient.** For profiles, use square-local exchanges with their common prefixes and suffixes. For turns, use the nonlinear star identity h_ijh_jk=h_ik together with shared-edge square consistency; the variables are attached to vertices and directions, not just to a histogram.

**First creative tasks.** Seek a profile augmentation rule that moves both the order witness and root, or a conditioned turn inequality whose overlapping conditions cannot be simultaneously realized when every cyclic turn sum is at least three. A nonlocal exchange or a proved barrier-crossing operation is admissible; strict adjacent descent is already ruled out.

**Continue if** a new relation separates realizable systems from the known formal countermodels and supplies an augmentation or estimate. **Change direction if** it only reconstructs the input again, proves another bounded projection surjective, or replaces the unresolved minimum by a new energy without control.

These are Programmes E and F, together with items 24 and 28. Their principal missing implications have received less sustained attention than the succession of core classifications. That is an assessment of the reviewed record, not a claim that no researcher has examined them.

## 5. Shortest-path estimates and overlapping entropy compression

These remain independent alternatives to critical-square repair. They offer weaker quantitative targets whose universal versions already imply closure.

For minority defect δ(c), a uniform bound δ(c)=o(n) suffices by the established identity δ(c^{\square k})=kδ(c). More generally, any F(c)≥δ(c) with a uniform o(n) upper bound suffices; F itself need not be additive. For the shortest monochromatic antipodal path length L(c), the established excess amplification makes L(c)−n=o(n) sufficient as well.

**Obstruction.** Unrestricted walks admit pumping that collapses several proposed intrinsic energies to an existing defect quantity. Prescribed roots can require linearly many switches. Anchored face inequalities do not help until the anchors and overlap are derived from a hypothetical counterexample. Unanchored weighted capacity cannot provide the hoped-for violation.

**Retained ingredient.** Global shortestness, its forbidden shortcuts, endpoint absorption, and shared-face curvature. Work with a justified minimizing path family and allow the root to vary globally.

**First task.** Produce the anchors needed by an existing cut theorem from shortestness, or prove a charging inequality in which repeated-direction excess forces a sublinear total cost. An unbounded family of coupled faces may be necessary. Continue on a useful uniform estimate; stop refining arbitrary prescribed anchor patterns without a production argument.

The separate counting route uses the number B_N^bal of bad balanced colorings. A bad seed yields normalized log-count approaching the ambient orbit-bit count L_N=N2^{N-2}. Consequently an upper bound
\[
\log_2 B_N^{\mathrm{bal}}\le(1-\eta)L_N
\]
for some fixed η>0 along arbitrarily large even N would force closure.

**Obstruction.** Independent pivot-square packing yields only a linear-bit saving, far below this scale. Local pseudorandomness can coexist with an embedded hypothetical obstruction.

**Retained ingredient.** Overlapping failed path networks sharing orbit variables. The decoder or conditional-information argument must exploit their dependence and include the cost of selecting the network.

**First task.** Recover a positive fraction of orbit bits conditionally from the others, with a complete decoding argument, or prove an entropy inequality of the displayed strength. Continue only when there is a quantified saving on the ambient scale. A new encoding whose saving is unspecified has not earned a new programme.

These carry forward Programmes D and items 7, 8, 11 and 25. They should remain available even if square repair receives most attention.

## 6. A common subset-state forcing principle for the grand conjecture

The boundary target is: for every reversal-odd binary coloring b of ordered distinct triples on an n-element set V, find a permutation of all original vertices whose consecutive triple-color word has at most one change. A monochromatic path of order sqrt(n) is insufficient.

The existing ordered-terminal states (A,u,v), with {u,v}⊆A⊆V, record the used original vertices and the ordered terminal pair. Appending a fresh vertex gives an acyclic colored extension system. Its complement-reversal map is
\[
J(A,u,v)=((V\setminus A)\cup\{u,v\},v,u).
\]
For color ε, let R_ε be reachability from all two-vertex sources. The proved equivalence is
\[
R_\epsilon\cap J(R_\epsilon)\ne\varnothing
\quad\text{for some }\epsilon
\]
if and only if the boundary one-change Hamiltonian conclusion holds. The two arms use complementary sets outside their shared terminal pair, so decoding preserves original-vertex simplicity.

**Statement to attack.** Identify a common intrinsic extension-system law, verified for both this boundary system and cubical support-aware path systems, that forces the required complementary reachability intersection. Prove its forcing content before expanding the abstract framework.

**Obstruction.** Antipodal symmetry, generic graph connectivity, Eulerian balance, or abstract matroid language alone are insufficient. Fixed-terminal reachable sets need not satisfy greedoid augmentation. Cube edges and boundary triples give different observable color layers. A simple path in a quotient or line graph can repeat original vertices or fail coherent orientation.

**Retained ingredient.** Used sets, ordered terminals, the extension recursion, and complement-reversal polarity. In the cube, keep original direction support; in the boundary system, keep distinct original vertices and ordered-triple seams.

**First creative task.** Compare the recursions and their separating cuts, looking for a shared exchange that moves the terminal data as well as the used set. Any proposed common axiom must be derived for unrestricted boundary colorings and arbitrary legal cube colorings. It may not impose additional label identities on boundary triples.

**Continue if** one common exchange or separation lemma has both verified specializations and a nontrivial forcing consequence. **Change direction if** the framework becomes a tagged union, requires unrelated axioms for the two examples, or proves only reachability without the spanning and simplicity conclusions.

This carries forward Programme B and item 30 in a form that can also interact with the coupled-cut route. It is an independent creative line; cubical closure need not wait for its resolution. Grand closure, however, requires both full-strength implications.

## 7. Disposition of every direction in the earlier catalogue

The following map preserves deserving lines without presenting thirty simultaneous assignments. “Reserve” means a mathematically legitimate alternative to reopen with a specific mechanism. “Pause” means that the reviewed evidence gives no reason for routine continuation.

| Article XVI direction | Disposition and reason |
|---|---|
| A. Critical shared-edge repair | Leading route 1; strict boundary normalization is already available. |
| B. Eulerian/rainbow budgeted exchange | Retain in routes 1 and 6; exchange must preserve direction counts or original vertices. |
| C. Derivative integrability | Leading route 3; combine all constraints on one instance. |
| D. Overlapping entropy compression | Independent route 5; require ambient-scale savings. |
| E. Integrable profile transport | Route 4; retain order witnesses. |
| F. Nonlinear star/turn consistency | Route 4; use reconstruction laws beyond scalar moments. |
| 7. Near-geodesic detour | Route 5; seek a uniform shortest-path estimate. |
| 8. Sublinear minority defect | Route 5; root selection remains existential. |
| 9. Coherent seam invariant | Route 1; retain mixed zones and permit growing clause networks. |
| 10. Cross-face witness transport | Routes 2 and 3; witness gluing is the target. |
| 11. Conditional influence decomposition | Retain as a possible dichotomy supplying hypotheses, without asserting it. |
| 12. Padding-stable complexity | Supporting work only if it enables a proved decreasing reduction. |
| 13. Balanced reconfiguration | Normalization now available; explore a different move only if it improves repair. |
| 14. Balanced square boundary | Resolved normalization; eliminate the boundary. |
| 15. Symbolic clause elimination | Route 1; seek a proof schema with path provenance. |
| 16. Recursive finite certificate | Use computation to discover or refute one recursion; pause repeated censuses. |
| 17. Adaptive root selection | Route 2 and profile transport; avoid fixed-root assumptions. |
| 18. Support-aware Boolean cuts | Leading route 2, with boundary comparison in route 6. |
| 19. Noncommutative positive expansion | Reserve: seek positivity and support-preserving operations, then a nonvanishing mechanism. |
| 20. Variable interlacement | Reserve within budgeted exchange; unbounded complexity is allowed. |
| 21. Relative top-cell cancellation | Reserve: supply a color-sensitive cancellation identity in the localized obstruction. |
| 22. Direction-graded chains | Reserve: prove that the surviving class decodes to a direction-simple spanning path. |
| 23. Coupled Smith obstruction | Reserve: establish a new cross-fiber relation; a tower alone supplies no bound. |
| 24. Conditioned turns | Route 4; couple overlapping witnessed prefixes. |
| 25. Tensor-stable spectra | Retain only with a usable universal estimate; rank/mixing padding is blocked. |
| 26. Common-class extremizers | Supporting method across routes; preserve the conditions being conjoined. |
| 27. Witness-preserving smoothing | Reserve: require an explicit path transfer back to the source coloring. |
| 28. Diagonal-fiber identities | Route 4 or full-halfword exchange; retain diagonal and order data. |
| 29. Joint obstruction catalogue | Use selectively to test a named lemma; pause indiscriminate catalogue growth. |
| 30. Boundary transfer | Active route 6, with spanning original-vertex simplicity mandatory. |

Arbitrary-rank affine peeling remains a legitimate algebraic problem, but a proof still leaves the nonlinear transfer. It is not the default continuation for this closure project. The same applies to new nonlinear families engineered to satisfy an existing core theorem.

## 8. How to use this programme

At the beginning of a substantial investigation, choose one precise statement and name its strongest known obstruction. Explain what structure the argument keeps, what intermediate evidence would justify continued effort, and what would make the mechanism untenable. These statements guide reasoning; they are not required manuscript output.

A continuation may spend its entire effort trying to prove or disprove one such statement and end inconclusively. Report that honestly and persist no mathematical result. If a useful line remains open after the attempt, retain the question without claiming that persistence itself is progress.

Refresh concurrent work when it can change the proof route or before publication. Carry forward valid earlier proofs and histories. Add to the shared record when there is something consequential for the next researcher to learn, rather than something merely new to append.
