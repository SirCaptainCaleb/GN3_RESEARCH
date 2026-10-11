# NORI manuscript research guide

**Publish mathematics that resolves consequential questions after the unrestricted NORI3 conjecture's refutation. Establish correctness, precise scope, and its effect on an open problem.**

## One structure, one conjecture, two exact consequences

**The grand research task is to DEFINE ONE concrete mathematical structure and FORMULATE ONE mathematically precise conjecture about that structure, whose resolution would resolve both unrestricted NORI1 and the target long monochromatic vertex-simple tight-path problem for ordinary boundary 3-tournaments.** Discovering the right object and conjecture is itself the central creative problem. A general vocabulary, analogy, common slogan, or theorem only about one of the two families is not enough.

An acceptable proposed unification must specify:

1. **One class of objects** \(\mathcal C\), described by explicit intrinsic data, operations and structural axioms. It should not be a tagged disjoint union of a NORI1 class and a boundary-tournament class.
2. **One conjecture** \(\mathbf U\) stated entirely in the language of those objects, quantifying over the intended class and making a definite path/selection/witness assertion (including a meaningful quantitative bound where appropriate).
3. **Two exact encoding and extraction theorems.** Show that *every* legal antipodally odd coloring of undirected physical cube edges yields an object of \(\mathcal C\), and *every* ordinary reversal-odd boundary 3-tournament, including non-edge-orderable instances, yields an object of the SAME class. Explain how a witness of \(\mathbf U\) produces a full monochromatic antipodal cube geodesic in the first case and the desired original-vertex-simple monochromatic tight path in the second.
4. **Resolution logic.** Write the actual implications, not merely an aspiration: prove that a proof of \(\mathbf U\) gives both desired results. Ideally build reductions strong enough that a refutation of \(\mathbf U\) also provides a meaningful resolution of both, or clearly identify why a negative answer would instead require refinement. Calling the conjecture a resolution of both requires the appropriate logical deductions.

The NORI1 family permits arbitrary nonlinear physical-edge colorings; the boundary family permits every ordered triple coloring \(b(a,b,c)\) satisfying \(b(c,b,a)=1-b(a,b,c)\), without a global edge order. Physical edge/face identities, antipodal symmetry, genuine root compatibility and original-vertex simplicity must survive the relevant reductions. At three-face level, two additional seam windows are a central obstacle: proving an edge-color statement without those windows does not establish the ordered-triple consequence.

**Use NORI1 as a toy laboratory.** Its physical squares, rooted antipodal pairings, witness intersections and geodesic operations may reveal what the unified objects and axiom should be. Such exploratory work is welcome, including on restricted model cases, when it illuminates a plausible one-structure conjecture.

**Use ordinary boundary tournaments to test the same proposed structure.** Test every suggested operation and witness theorem on arbitrary reversal-odd tournaments, including non-edge-orderable cases, to determine whether the one conjecture genuinely has the needed vertex-simple tight-path consequence.

Researchers are free to invent different candidate structures and challenge prior formulations. Judge mathematical progress by movement toward ONE well-posed conjecture and its TWO rigorous specialization deductions, not by separately accumulating progress on the two original problems.

Before investing deeply in a subsidiary question, identify the mathematical implication that would make its solution useful. Make that implication explicit enough to examine. If the strongest plausible answer would leave the main argument in essentially the same position, reconsider the question.

Treat a succession of tractable extensions as a reason to step back. Look for the conceptual change that would make those extensions matter. Choose finite-dimensional computations to discriminate between general claims or reveal mechanisms.

When an approach already has substantial development, assess what additional insight your investigation could supply. Consider a substantially different route when the existing work repeatedly reaches the same obstacle.

Spend your effort on the strongest mathematical opportunity you can identify. Report an inconclusive outcome plainly when that is where the investigation ends.

## Mathematical acceptance test for the grand conjecture

For a proposed object class \(\mathcal C\) and candidate conjecture \(\mathbf U\), provide an explicit mathematical certificate of the following form:

- **Intrinsic definition:** specify \(\mathcal C\), its admissible finite objects, its allowed local-to-global operations and a *single* witness predicate \(W(X)\). State \(\mathbf U:\ orall X\in\mathcal C,\ W(X)\) (or a precise quantitative variant).
- **NORI1 reduction:** for each arbitrary antipodally odd physical-edge coloring \(c\), construct \(X(c)\in\mathcal C\) and prove \(W(X(c))\) yields a genuine full monochromatic antipodal cube geodesic.
- **Boundary reduction:** for each ordinary reversal-odd ordered-triple tournament \(b\), construct \(X(b)\in\mathcal C\) and prove \(W(X(b))\) yields a monochromatic tight path of the required quantified length with distinct original vertices. Edge-orderable tournaments alone are a helpful example, not the whole class.
- **One common reason:** justify why the same axioms and witness predicate handle both encodings. Mere disjoint tagging, two independent clauses or parallel proofs under one heading is not a unification.
- **Logical closure:** state explicitly which conjectures would follow from a proof of \(\mathbf U\). Explain the status of counterexamples to \(\mathbf U\); if falsity would not settle both originals, that asymmetry is a research gap, not an already completed full reduction.

NORI1 toy lemmas can suggest the candidate \(W\); boundary examples expose missing face-memory and vertex-simplicity constraints. Same-face reversal oddness, antipodal invariance, witness nerves and paired-root selection are possible inspirations, not assumed solutions. A candidate structure need not be perfect on its first attempt: record its exact domain, the missing specialization theorem and a concrete path to strengthening it. Pursue the conjecture whose verified implications reach both original problems.

## Selective research notes — separate from manuscript publication
Save a note only when another researcher could make a materially better decision. Use the narrowest primary home (Project, Article, Section or Subsection), and link additional relevant manuscripts or notes. Record the precise claim, scope, evidence, why it matters, and a discriminating next step where applicable. Before starting or revisiting an approach, inspect the Known obstructions appendix and only the relevant notes. Extend existing notes on the same question rather than fragmenting them.

**Default destination for negative results is a research note, EVEN IF rigorous, lengthy, technically sophisticated, or currently developed as a complete Section or Subsection.** This includes counterexamples to a proposed implication, methods that provably cannot close a gap, bounded exhaustive exclusions, and failed generalizations whose principal value is redirecting future research. Proof size and amount of effort do not by themselves confer publication status. Make a genuine exception for a negative theorem or counterexample that decisively resolves a central conjecture, establishes an independently important mathematical result, or makes another substantial standalone contribution (for example, the legal Q9 refutation and its all-dimensional consequences). Evaluate mathematical significance, NOT the positive/negative label alone.

For mixed material, preserve the independently significant positive theorem or reduction in a coherent Subsection and put the method-specific obstruction, exact failure certificate or unsuccessful extension in a linked research note. An entire Section dominated by negative method audits may properly be consolidated into notes; preserve every reusable rigorous proof and provenance while revising the containing Article/Section compositions rather than silently discarding mathematics. The Known Obstructions appendix remains a curated high-level synthesis, with detailed evidence linked from notes, not a dumping ground for all negative experiments. Distinguish proved false implications, exhaustive exclusions within explicit bounds, limitations of a specific method and attempts that merely failed. Keep epistemic status separate from lifecycle; resolve or supersede notes with an explanation and successor link. Notes are never automatically composed into manuscripts; neither publication nor a note is mandatory. Notes, recency and convenient next steps do not rank the research agenda.

## Manuscript structure and publication
Read the original (now refuted) grand conjecture, the latest counterexamples, OVERVIEW.md, KNOWN_OBSTRUCTIONS.md, and all eight Article compositions before choosing your approach; follow relevant Sections and Subsections for proofs. Historical effort is evidence about cost, not a ranking. Independently challenge inherited formulations and pursue original routes.

Articles, Sections, and Subsections form one assembled manuscript. **A Subsection is the smallest durable mathematical publication.** Revise a Subsection when a proof or correction belongs there. Create a new one only for coherent substantial development. Section and Article prose should connect arguments rather than repeat every proof. Check adjacent manuscripts before publishing; combine overlapping statements, preserve distinct meaningful proofs, and state exact dependencies and uncertainty.

Publish coherent, correct, independently consequential theorems, reductions, decisive counterexamples to central conjectures, and necessary corrections. A short decisive lemma may qualify; length, proof sophistication, effort spent, and the existence of a complete counterexample to a subsidiary METHOD are insufficient for manuscript admission. Negative results ordinarily go to selective notes even when extensive. A negative result may remain a manuscript only if its actual mathematical consequence is independently publication-worthy. An inconclusive session may leave neither manuscript nor note; routine failed attempts have no preservation requirement.

The Known obstructions appendix preserves counterexamples and reusable false implications with their exact scopes. The unrestricted original NORI3 one-switch conjecture and all fixed k>=3 switch hierarchies are disproved. Do not treat these as open questions or revive the obsolete universal square-root monochromatic-path target. Distinguish them from the open unrestricted NORI1 full-monochromatic-geodesic problem and NORI1-preserving strengthened variants of the higher-face problems. Do not initiate old unrestricted NORI2 investigations. Preserve established logarithmic NORI3 counterexamples as obstructions against overly weak proposed generalizations.

Use the boot session_id for writes. Publish Subsections with `publish_subsection` and optimistic composition versions; use `compose` for Sections and Articles. Stage related writes and commit atomically when needed. Historical identifiers are recoverable from a fixed GitHub snapshot through explicit lookup only. No Items, tasks, leases, checkpoints, or compulsory progress reporting.
