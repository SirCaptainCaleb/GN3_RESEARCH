# 03 — GN3 research protocol

This file governs live mathematical search, Director/Vice Director structural synthesis and conceptual ascent, guidance, and maintenance of `RESEARCH_TREE.md`.

## What counts as progress

Research progress is not artifact production. A step counts as progress when it improves a plausible proof, proves or sharpens a load-bearing gap, replaces local machinery by a simpler structural principle, supplies a genuinely reusable theorem that changes the search, or identifies a concrete obstruction, necessary missing hypothesis, or counterexample that changes the mathematical picture.

A correct side lemma that does none of these may still be useful scratchwork, but it is not automatically theorem progress. No role has a quota for named results, lemmas, Engines, or nonempty returns.

## Null results and failure classification

A researcher may return `no proof found`, `no theorem progress found`, or `the attempted construction did not resolve the stated gap`. Do not manufacture narrow lemmas or finish irrelevant easy branches merely to avoid a null result.

When a route stalls, distinguish:

1. **counterexample or impossibility** — the proposed statement or mechanism is false;
2. **necessary missing hypothesis** — a concrete additional condition appears necessary;
3. **specific structural obstruction** — a precise configuration or invariant blocks the proposed realization;
4. **no proof found** — the search failed but the abstraction has not been defeated.

Only the first three justify abandoning or materially revising the abstraction. Failure to find a proof does not refute it.

## Guidance and Slack research roots

The ordinary strategic question is: **what is the earliest statement in the shortest currently favored proof that we cannot justify?** That statement is the Director default target. Alternative abstractions remain useful when they could bypass the gap, yield a stronger parent theorem, or simplify the global picture.

Each Director research wave receives a monotonically increasing tag `[G##]`. The guidance root lives in `#gn3-guidance` and states the mathematical target and enough context to explain why it matters.

Researchers responding to that guidance post each discovery as a top-level `#gn3-research` message prefixed by the same `[G##]`.

### Hard root-message invariant

A top-level message in `#gn3-research` is a **mathematical headline only**. It states exactly what was proved, disproved, obstructed, or otherwise established. The root contains only the mathematical assertion itself: the minimum hypotheses and notation required to state it, any mathematically necessary cases or formulas, and the conclusion.

If every reply to the root were deleted, the root should read like a theorem, lemma, proposition, counterexample statement, obstruction statement, or precise null statement — **not** like a research note.

The following material is forbidden in a research root and belongs in replies:

- proofs, derivations, proof sketches, forcing chains, case analysis, computations, certificates, or explanation of why the assertion is true;
- motivation, strategic interpretation, “why this matters,” route discussion, comparison with earlier work, dependency commentary, or suggested next steps;
- audit status, provenance, archaeology, citations used as justification, implementation notes, worker coordination, or commentary about how the result was found;
- summaries of several related discoveries when they can instead be posted as separate exact mathematical statements;
- explanatory paragraphs before or after the mathematical assertion.

A root may be long only when the **statement itself** genuinely requires that much mathematical data. Length never licenses proof, commentary, logic, or research narration in the root. Conversely, do not weaken or make a statement ambiguous merely to keep it short.

All supporting material goes in the thread. The normal shape is therefore:

`[G##] <exact mathematical statement>`

followed by one or more replies containing proof, derivation, qualifications, motivation, strategic consequences, and discussion.

This is a **hard communication invariant, not a style preference**. Before posting, the researcher must remove every sentence that is not part of the exact mathematical assertion and place it in a reply instead. If a researcher posts a violating root, that researcher must immediately edit the root down to the headline statement and move the removed material into the thread. Do not leave an oversized root in place as a historical record; Slack edit history is sufficient. The Vice Director may perform this shape-only cleanup when encountered, provided the mathematical claim itself is not changed.

A precise obstruction or null result may itself be the root statement, but the supporting analysis still belongs in replies.

The `[G##]` tag is administrative retrieval metadata, not mathematical notation, theorem identity, or provenance inside canonical mathematics.

## Researcher method

Before detailed construction, identify the ordinary mathematical structure being studied, the coarse mechanism being tested, and what concrete construction would accomplish if successful. Work at increasing resolution: begin with the structural requirement and refine only the parts whose realization matters.

Stop elaborating an abstraction when it is genuinely defeated and no credible repair preserves its purpose. If the only outcome is no proof found, record that accurately.

Scratch research may use temporary names, case trees, calculations, exploratory constructions, heuristic pictures, and unaudited results. Search may consume unaudited work optimistically unless it has been explicitly failed, invalidated, quarantined, or superseded. Repeated use does not certify it; certification is governed by `04_AUDIT_PROTOCOL.md`.

Concurrent mathematics is part of the live search. During a long research task, resynchronize relevant Slack activity at natural mathematical boundaries when newly posted work could materially change the mechanism, target, or shortest route. This is not a requirement for constant polling; finish a coherent local step, then incorporate important concurrent results before building substantially on a stale picture.

## Conservative computation discipline

Prefer a human-scale mathematical argument to a broad symbolic or exhaustive computation whenever the former is reasonably available. Computation is most useful when it answers a sharply stated finite question; it is not the default way to compare two formulations or re-derive a known structural fact.

Before launching a calculation, state the exact quantity, identity, case set, or counterexample being sought and estimate the expected output. Prefer targeted scalar evaluations, short exact checks, bounded case tables, or a small script that returns a concise invariant over expanding large symbolic expressions, matrices, spectra, polynomial recurrences, or exhaustive traces.

**Do not flood the working context with large computational output.** If a symbolic comparison or finite enumeration begins producing long expansions, large tables, or repeated near-duplicate output, stop rather than retrying increasingly broad variants. Replace it with a conceptual derivation, a smaller check, or a clearly isolated computational subclaim. In particular, do not expand Johnson-scheme polynomials, characteristic polynomials, large matrices, or comparable algebra from scratch merely to verify a few values when those values can be obtained or checked directly.

When computation is genuinely load-bearing, retain only what makes the argument checkable: the precise input, method, concise output or certificate, and the mathematical inference drawn from it. A huge transcript is not a proof. If a computation cannot be reduced to a checkable certificate or independently reproducible bounded calculation, treat the conclusion as provisional rather than silently relying on the output.

## Structural synthesis and conceptual ascent

The Director/Vice Director must perform two complementary comprehension operations over the live mathematics: **structural synthesis** and **conceptual ascent**. They are coupled but not synonymous.

Structural synthesis reconstructs the best combined mathematical picture from old and new work. Conceptual ascent deliberately climbs above that picture in search of stronger, more intrinsic, and more explanatory mathematics. Neither is merely housekeeping, result placement, or application of a recent lemma to an earlier proof point. Together they are the project’s main mechanism for attaining maximal comprehension before choosing strategy.

### Structural synthesis

Read old and new mathematics together and ask what the arguments are **actually saying**, independently of the names, chronology, proof machinery, or local task that produced them.

For each substantive result or mechanism:

- identify its intrinsic hypotheses, conclusion, and mathematical mechanism rather than inheriting its discovery-time packaging;
- compare it with nearby stronger, weaker, equivalent, special-case, converse, and competing formulations;
- determine which hypotheses are structural and which are artifacts of the construction that first exposed the result;
- test how it composes with earlier and later facts, including combinations that were not considered when either fact was discovered;
- locate redundancy, subsumption, hidden equivalence, incompatibility, and opportunities to replace several local statements by one parent statement;
- reconsider where the result belongs in the abstraction hierarchy: theorem-level principle, intermediate bridge, local mechanism, obstruction, reusable toolkit fact, or temporary search aid;
- ask whether the current decomposition of the proof into branches and subproblems is itself the most explanatory and strategically useful decomposition, rather than merely the one inherited from research history;
- reconstruct dependencies according to mathematical necessity rather than discovery order, and distinguish facts that merely helped find a route from facts that actually explain or sustain it.

Structural synthesis is not restricted to audited mathematics. Unaudited results may participate provisionally so long as their certification state is not confused with correctness. Audit establishes confidence in exact mathematics; structural synthesis determines mathematical meaning, interaction, and role; canonical placement is a later editorial decision.

### Conceptual ascent

Starting from the synthesized picture, deliberately search for mathematics one or more abstraction levels above the current statements. The goal is not simply a stronger lemma. It is to identify the concept that makes the lower-level phenomena natural consequences rather than a collection of coincidences.

In particular:

- seek strengthenings, generalizations, parameterized forms, and parent theorems that make several current facts manifestations of one mechanism;
- strip accidental coordinates, chosen labels, extremal witnesses, or proof-specific language when an intrinsic formulation carries the same content;
- formulate useful weakenings when the proof needs less than the current statement and the weaker form exposes the real mechanism more clearly;
- examine contrapositives, obstruction forms, dual formulations, complementary viewpoints, and the **negative space**: what must fail, be absent, or become rigid if the desired construction does not exist;
- ask what invariant, exchange principle, closure phenomenon, extremality principle, compactness principle, or local-to-global mechanism conceptually enables a recent result;
- search for an object or relation in which several apparently different operations become the same operation viewed in different coordinates;
- test whether the phenomenon persists when the current numerical threshold, complement size, chosen path, or extremal witness is varied, and identify the sharp parameter on which it really depends;
- ask whether the theorem should be phrased about existence of a desired object or rigidity of all counterexamples to that object, whichever gives the more explanatory statement;
- test whether a newly recognized mechanism reaches beyond the current proof coordinate, collapses a branch, changes the natural induction/minimality parameter, or suggests a different global proof architecture;
- distinguish a genuinely stronger explanation from a reformulation that merely hides the same case complexity behind new terminology.

Conceptual ascent should aggressively challenge the current abstraction ceiling. It may conclude that the present formulation is already optimal, but only after actively testing plausible parents, duals, obstruction forms, and generalizations. It should not be reduced to “try the new lemma earlier in the proof.”

### Outputs of a synthesis-and-ascent pass

A pass should leave the project with the clearest available answer to six questions:

1. **What do the currently relevant results jointly imply?**
2. **What underlying mechanism best explains those implications?**
3. **What stronger, more intrinsic, dual, obstruction, or negative-space formulation best captures that mechanism?**
4. **What is the most natural abstraction hierarchy and shortest plausible proof route now?**
5. **What exact unresolved mathematical statement should research attack next?**
6. **Does the new picture require escalation to Astra, and why or why not?**

Possible outputs are a revised research tree, a new or revised guidance target, a parent theorem or obstruction proposed for research, a changed dependency chain, a decision to retire or demote machinery, an audit batch for newly load-bearing mathematics, or—when certification and stability justify it—a canonical proof/toolkit edit. A pass is successful when the mathematical picture becomes more coherent and explanatory, even if none of these artifacts needs to change.

## Director cycle

The Vice Director runs a continuous Director cycle around and between research waves. A wave is one instrument inside the cycle, not a batch that must finish before direction changes.

1. **Synchronize the live picture.** Read the current proof spine, toolkit, research tree, current guidance, relevant new research, and the certification state of mathematics the favored route actually depends on. During a long cycle, resynchronize at natural mathematical boundaries when concurrent work may have changed that picture.
2. **Perform structural synthesis and conceptual ascent.** Run the full synthesis-and-ascent pass above over the mathematics relevant to the live frontier. Re-test substantive new results at their earliest natural proof coordinates, but do not stop there: compare old and new formulations globally, determine what they are really expressing together, seek the mechanism behind them, test stronger/weaker/generalized/dual/obstruction/negative-space forms, and reconsider the abstraction tree itself. This stage determines the best current mathematical picture before operational choices are made.
3. **Select, track, and batch load-bearing mathematics for audit.** Determine which exact extra-spine statements and proofs have become necessary to the shortest favored route, an important live alternative, a proposed core-shelf composition, or a genuinely reusable utility argument. The Vice Director owns this audit triage and keeps track of which active load-bearing dependencies still require independent certification. At natural synthesis points, group the currently relevant exact targets into a coherent **audit batch** and hand that batch to one independent Auditor under `04_AUDIT_PROTOCOL.md`. A batch may contain several related statements, proofs, or shelf candidates, and should include enough context to explain their mathematical relationship and priority without asking the Auditor to reconstruct the research strategy. Do not turn the general research backlog into an audit batch: there is no chronological audit frontier and no requirement to certify intermediate results that the live strategy does not depend on.
4. **Propagate certified mathematics and maintain the shelves.** When targets in a batch pass, update the live dependency picture to use the certified facts where they remain relevant. If certified mathematics now plausibly belongs to the surviving proof route, merge it with nearby certified material into a coherent core-shelf candidate; if it is plausibly reusable independently, prepare a utility-shelf candidate. The exact composed candidate must itself be independently audited before shelf admission, even when every ingredient was previously certified. Keep admitted shelf files organized by mathematical topic/proof coordinate rather than guidance era. If an audit fails, weakens, or materially repairs a live dependency, rerun the affected structural synthesis and conceptual ascent rather than merely patching the old route.
5. **Re-evaluate the shortest favored route from the top down.** Starting from the theorem and earliest unresolved bridge, express the route in the abstraction discovered by structural synthesis and conceptual ascent. Remove or compress branches that are closed, subsumed, contradicted, bypassed, unnecessarily strong, or artifacts of an older explanation.
6. **Rewrite the research tree as a pure outline.** Preserve the hierarchy theorem-level objective → unresolved bridge → candidate mechanism → concrete subproblem only when that hierarchy still reflects the mathematics. If synthesis and ascent found a better decomposition, rewrite the hierarchy accordingly. Express every node as one brief headline line and let nesting carry the refinement.
7. **Place guidance in the tree.** Ensure the mathematical target of current guidance appears at the correct node or leaf of the outline. The tree records the target itself, not prose explaining why the guidance was chosen; that rationale belongs in `#gn3-guidance`.
8. **Issue or revise guidance.** State the common mathematical target and enough context to make its role in the current structural picture clear. Do not preserve an old target merely because it was previously issued.
9. **Promote from shelves only after structural stability.** The core and utility shelves preserve audited mathematics before its final home is settled. Promote a core-shelf argument into the proof spine when its sequential role and exposition are stable; promote a utility-shelf argument into the toolkit when its independent reuse value and final formulation are stable. Do not use final canonization as the first moment at which an already-audited surviving proof is gathered out of Slack.
10. **Make an explicit Astra-escalation decision.** Every Director cycle must decide whether the synthesized picture requires escalation to Astra. Escalate when the abstraction itself needs to change: for example, a strategic reframe, stronger parent theorem that changes the theorem-level route, global bypass, major invariant or induction/minimality change, substantial proof-architecture decision, or a conflict between comparably plausible global architectures that warrants Director-level adjudication. Do not escalate merely because a local lemma is difficult, a current branch needs ordinary tactical direction, or a cleaner coordinate system refines the same already-approved parent strategy.
11. **Report the Astra decision.** The cycle report to the project owner must state either that the matter was escalated to Astra and what abstraction-level question was sent, or that it was not escalated and the concrete reason the current change remains within the existing strategic mandate. A silent non-escalation is not sufficient. When the case is genuinely borderline, prefer a short Astra escalation over implicitly making a major abstraction decision at Vice-Director level.

Then repeat. The cycle exists to keep rebuilding the best mathematical understanding as the corpus changes, not merely to accumulate results, move them between surfaces, or push the current proof one lemma at a time. Audit tracking, tree maintenance, and canonical placement serve structural synthesis and conceptual ascent; they are not substitutes for them.

## Research-tree management

`RESEARCH_TREE.md` is a **pure nested outline** of the live mathematical search. The file contains nothing except the outline itself: no title, preamble, legend, framing paragraphs, instructions, rationale, commentary, bibliography, audit notes, or closing remarks. All rules for maintaining the tree belong here in `INIT/` rather than in the tree.

Each outline item is one brief Markdown line expressing a mathematical headline statement or guiding abstraction. Multiple short sentences, formulas, or clauses may appear on that same line when needed for precision, but a node has no attached body paragraph. Do not turn a node into a mini-memo, proof sketch, implementation checklist, literature note, or explanation of why it matters.

Nesting carries resolution. A parent states the coarser abstraction; each child refines that parent into a finer abstraction, branch, mechanism, obstruction, or concrete target. Continue downward only as far as the live search usefully distinguishes the mathematics. Leaves should be concrete headline statements or concrete open subproblems when the search has reached that resolution.

The outline may use bullets or numbering. It should normally use one consistent style within a given revision. Semantic mathematical statements, not result IDs or workflow history, define the nodes. A guidance tag such as `[G##]` may be included inline on the relevant item when useful for retrieval, but it does not justify any additional prose.

Full proofs are excluded from the research tree. Proofs, derivations, casework, computations, examples, supporting evidence, and detailed obstructions belong in Slack threads or canonical mathematical documents. Only when the exact mathematical nature of a node makes a small amount of proof-like content genuinely inseparable from stating it may the minimum unavoidable content appear inline in that same outline item; never add a separate proof body beneath the node.

Individual discoveries enter the tree only when they change the live abstraction, create or eliminate a branch, sharpen an obstruction, or become a concrete leaf target needed by a live route. A discovery does not earn a node merely because it is correct, useful, audited, recent, or repeatedly cited.

Researchers normally communicate tree corrections and structural suggestions through `#gn3-research`; the Director or delegated Vice Director performs the low-concurrency rewrite. For a given synthesis-and-ascent pass, one compressor owns the tree edit so that the hierarchy remains coherent.

The tree has a low admission bar for a genuinely live branch and a high retention bar thereafter. Merge overlapping nodes, promote stronger parent abstractions, split only where the mathematics truly branches, and delete dead or redundant branches aggressively. Git history is sufficient recovery; chronology, credit, audit transcripts, and obsolete proof ontology do not belong in the outline.

## Search state and durable mathematics

Slack is the discovery stream. The research tree is the terse hierarchical outline of the current search. `SHELVES/CORE/` preserves audited proto-proof sections whose final proof-spine placement is not yet settled. `SHELVES/UTILITY/` preserves audited reusable mathematics whose final toolkit placement is not yet settled. The proof spine is the sequential canonical proof, and the toolkit is the final selected reusable mathematics.

Compression from Slack into the tree is structural synthesis and conceptual ascent, not copying. Movement from Slack into a shelf is stricter: the exact shelf candidate must be audited, and core-shelf material should be consolidated into natural conceptual movement rather than archived as a result list. Promotion from a shelf into the proof spine or toolkit requires further structural stability, though not a new mathematical idea merely for changing destination.

There is no separate `RESEARCH_STATE.md`. The shelves are not summaries of state; they contain the exact audited mathematics needed to prevent proof reconstruction from becoming Slack archaeology. The research tree carries the current live abstraction and guidance location; the proof spine carries the final sequential route and explicit open boundary.
