
PROOF REHEARSAL MODE

A proof rehearsal is a fresh global proof-design and proof-synthesis exercise over the current mathematical state. Its durable output is not a research log. It is a cold-readable mathematical manuscript that a new researcher can read without reconstructing the repository history.

SCHEDULER NEUTRALITY

A scheduler-forced proof rehearsal is route-neutral. The scheduler requests a rehearsal of the grand theorem; it must not choose, endorse, or implicitly assign a proof route. Recent results, stale compositions, or changed objects carried with the scheduler pressure explain why a new rehearsal is due. They are orientation metadata, not a route assignment.

GLOBAL SURVEY AND JUDGMENT

Begin from the whole current mathematical landscape. Inspect the major live proof directions, reusable lemmas and constructions, known obstructions, alternate formulations, and current end-to-end compositions. Exercise mathematical judgment about relevance. The rehearsal need not mechanically repeat every repository object, but it must account for all major non-superseded findings that materially affect the approach being synthesized or the choice among serious approaches.

The worker may omit:
- superseded results;
- genuinely redundant reformulations;
- low-level details that are fully subsumed by a stronger statement proved in the rehearsal;
- failed directions whose only remaining value is the obstruction that rules them out.

A failed direction does not need a full reconstruction. State the obstruction precisely enough that a new worker will not repeat the same investigation. If the construction or counterexample is useful but would interrupt the main proof, place it in an appendix.

PUBLICATION-STYLE DELIVERABLE

The final rehearsal must read like a mathematical paper or a polished proof section, not like project notes.

The manuscript should:
- state the theorem and hypotheses clearly;
- introduce notation and definitions only when needed;
- use theorem/lemma/proposition statements where they improve readability;
- prove intermediate claims locally in the manuscript rather than referring the reader to repository object identifiers;
- give a coherent mathematical narrative from hypotheses toward the conclusion;
- separate genuinely independent alternatives cleanly;
- isolate any remaining unsupported step as a precise mathematical statement;
- use appendices for secondary failed routes, counterexamples, finite checks, or technical constructions that are useful for completeness but would distract from the main argument.

The document should stand on its own if copied out of the database. A reader should not need Atlas entries, object IDs, audit state, scheduler state, provenance metadata, or hidden project context to understand the mathematics.

SELF-CONTAINED AND MOSTLY COMPLETE

The rehearsal is expected to be self-contained and mostly complete.

"Mostly complete" means that the mathematical content required for the chosen proof architecture is actually developed in the manuscript. It does not mean that every failed research branch receives a full proof-history narrative. A branch known not to succeed may be compressed to the precise obstruction, with supporting detail moved to an appendix when useful.

Do not replace proofs with phrases such as "by the repository result", "as already certified", or "the previous worker showed". If an earlier project result is needed, restate it as a mathematical lemma in the manuscript and give enough proof or derivation that the rehearsal can be read independently. Classical background facts may be invoked in the ordinary style of a mathematical paper when genuinely standard; project-local results must be incorporated mathematically rather than referenced administratively.

PRECISION AND VOCABULARY

Precision is mandatory. Every nonstandard term must have a clear definition before substantive use.

Prefer standard graph-theoretic and hypergraph-theoretic vocabulary. Use project-specific terminology only when it appears in the standardization dictionary as an approved precise term and genuinely improves the mathematics. The standardization dictionary is authoritative for forbidden, ambiguous, and preferred language.

The mathematical manuscript must avoid proof-management and repository language. In particular, do not write object IDs, database paths, worker history, audit/certification labels, support-status labels, scheduler language, "research handoff" language, or other provenance/status scaffolding into the proof. Do not use a forbidden or ambiguous dictionary term merely because it appeared in older notes. Replace it with standard mathematical language or an approved precise definition.

Avoid rhetorical filler and proof-stage interjections. Statements such as "once and for all", "the key breakthrough", "the route now closes", or similar project-style commentary do not belong in the mathematical body unless they express an actual mathematical claim in standard prose.

COMPREHENSIVE SYNTHESIS

The rehearsal should preserve enough breadth that a new worker can cold-read it and avoid repeating investigations that have already reached a mathematical conclusion.

For the selected approach or combination of approaches:
- incorporate all major non-superseded ingredients that materially strengthen, constrain, or obstruct it;
- explain how the ingredients fit together mathematically;
- include stronger formulations that subsume older lemmas rather than duplicating weaker chains;
- record important negative information as mathematical obstructions, not as research-history narration;
- retain alternate live mechanisms when they remain genuinely distinct and potentially useful.

Use judgment. Comprehensive synthesis does not mean indiscriminate inclusion. The aim is maximal mathematical coverage with a coherent paper-like structure.

ACTIVE GAP ATTACK

Draft the strongest end-to-end composition presently available. Reaching an unsupported inference is not itself completion. When the composition first reaches a gap:
- search the current mathematical state for another result that closes or weakens it;
- try a different organization of the same ingredients;
- attempt a stronger or better-shaped local lemma;
- compare against other serious live approaches and switch if another organization has greater theorem leverage;
- publish genuinely new reusable mathematics separately when appropriate, then incorporate its mathematical content into the rehearsal.

Only after a serious bridge attempt may the remaining gap be recorded.

If the theorem is not closed, the manuscript should finish with a precise Remaining Lemma, Remaining Case, or equivalent mathematical statement. That statement should be the narrowest unsupported inference left by the synthesized proof, not a vague research objective.

PROOF COMPRESSION AND STRUCTURE

Actively compress the proof when stronger statements subsume several earlier steps. Distinguish a reusable standalone lemma from a step that belongs only inside one proof. Do not flatten genuinely independent ideas merely to make the presentation linear.

The final structure should optimize mathematical readability, not mirror the reasoning-tree shape or the chronology in which results were discovered.

DURABLE MAIN-LINE SYNTHESIS

The canonical Comprehensive Proof Rehearsals collection is the durable home for major proof-direction syntheses. If the rehearsal produces or materially improves a durable synthesis of a major proof direction, create or revise the appropriate direct child of that collection rather than leaving the substance only in an operational completion record. Do not create a duplicate child when an existing rehearsal already represents the same major direction; improve the existing rehearsal when appropriate.

A scheduler completion record may preserve historical information, but it is not a substitute for the publication-style synthesis when the mathematics has durable value.

COMPLETION RECORD

A non-closing rehearsal should report:
- manuscript: the publication-style rehearsal body;
- attempted_organization: a concise description of the mathematical organization used;
- route_selection: why that organization was chosen after surveying the serious live alternatives;
- bridge_attempts: the concrete mathematical attempts made to remove or bypass the first apparent gap;
- first_unsupported_inference and/or gap_id: the residual mathematical statement that remains;
- shortcuts_or_strengthenings: stronger statements or proof compression discovered during the rehearsal;
- changed_bottleneck: whether the theorem-level remaining lemma changed;
- highest_leverage_next_result: the missing mathematical statement that now appears most consequential.

For a closure candidate, publish or identify the complete reusable composition and provide composition_id.

SCHEDULER-FORCED PROOF REHEARSAL

The scheduler may request a new rehearsal after substantial theorem-scale change or sufficient repository progress. The assignment is always global and route-neutral. Completion requires both:
1. a serious fresh attempt to synthesize and improve the end-to-end mathematics; and
2. a manuscript-quality, self-contained, mostly complete rehearsal satisfying the standards above.
