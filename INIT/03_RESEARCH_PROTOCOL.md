# 03 — GN3 research protocol

This file governs live mathematical search, Director/Vice Director structural synthesis, guidance, and maintenance of `RESEARCH_TREE.md`.

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

Researchers responding to that guidance post each discovery as a top-level `#gn3-research` message prefixed by the same `[G##]`. The root is **statement-only**: it contains the exact mathematical assertion, with only the hypotheses, notation, cases, formulas, and conclusion needed to state it precisely.

Proofs, derivations, reasons, proof sketches, case analysis, computations, counterexamples, citations used as justification, qualifications, motivation, strategic interpretation, and discussion belong in replies to that root. A precise obstruction or null result may itself be the root statement, with the supporting analysis in the thread.

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

## Structural synthesis

**Structural synthesis** is the Director/Vice Director comprehension pass over the live mathematics. It replaces the narrower ideas of “integration” and “elevation” as separate housekeeping steps. Its purpose is not merely to place new results, apply them at an earlier proof coordinate, or search for a stronger lemma. Its purpose is to reconstruct the best current mathematical understanding of the problem from the interaction of old and new results, then reshape the proof search so that its abstractions reflect that understanding.

Structural synthesis has two inseparable directions.

### Reconciliation and composition

Read old and new mathematics together and ask what the arguments are **actually saying**, independently of the names, chronology, proof machinery, or local task that produced them.

For each substantive result or mechanism:

- identify its intrinsic hypotheses, conclusion, and mathematical mechanism rather than inheriting its discovery-time packaging;
- compare it with nearby stronger, weaker, equivalent, special-case, converse, and competing formulations;
- determine which hypotheses are structural and which are artifacts of the construction that first exposed the result;
- test how it composes with earlier and later facts, including combinations that were not considered when either fact was discovered;
- locate redundancy, subsumption, hidden equivalence, incompatibility, and opportunities to replace several local statements by one parent statement;
- reconsider where the result belongs in the abstraction hierarchy: theorem-level principle, intermediate bridge, local mechanism, obstruction, reusable toolkit fact, or temporary search aid;
- ask whether the current decomposition of the proof into branches and subproblems is itself the most explanatory and strategically useful decomposition, rather than merely the one inherited from research history.

This reconciliation is not restricted to audited mathematics. Unaudited results may participate provisionally in structural synthesis so long as their certification state is not confused with correctness. Audit establishes confidence in exact mathematics; structural synthesis determines mathematical meaning and role; canonical placement is a later editorial decision.

### Abstraction and conceptual lift

For the resulting combined picture, search deliberately for the most informative abstraction that explains **why** the current phenomena occur.

In particular:

- seek strengthenings, generalizations, parameterized forms, and parent theorems that make several current facts manifestations of one mechanism;
- strip accidental coordinates, chosen labels, extremal witnesses, or proof-specific language when an intrinsic formulation carries the same content;
- formulate useful weakenings when the full statement is stronger than the proof actually needs;
- examine contrapositives, obstruction forms, dual formulations, complementary viewpoints, and the **negative space**: what must fail, be absent, or become rigid if the desired construction does not exist;
- identify the invariant, exchange principle, compactness/closure phenomenon, extremality principle, or local-to-global mechanism that conceptually enables a recent result;
- test whether a newly recognized mechanism reaches beyond the current proof coordinate, collapses a branch, changes the natural induction/minimality parameter, or suggests a different global proof architecture;
- distinguish a genuinely stronger explanation from a reformulation that merely hides the same case complexity behind new terminology.

Structural synthesis should maximize comprehension, not novelty. It may conclude that the current abstraction is already the right one. It may also conclude that a correct new result is strategically peripheral, that an old lemma has become more important in a new formulation, or that the current research tree should be reorganized even when no theorem has just been proved.

### Outputs of a structural-synthesis pass

A pass should leave the project with the clearest available answer to four questions:

1. **What do the currently relevant results jointly imply?**
2. **What underlying mechanism best explains those implications?**
3. **What is the most natural abstraction hierarchy and shortest plausible proof route now?**
4. **What exact unresolved mathematical statement should research attack next?**

Possible outputs are a revised research tree, a new or revised guidance target, a parent theorem or obstruction proposed for research, a changed dependency chain, a decision to retire or demote machinery, an audit batch for newly load-bearing mathematics, or—when certification and stability justify it—a canonical proof/toolkit edit. Structural synthesis is successful when the mathematical picture becomes more coherent, even if none of these artifacts needs to change.

## Director cycle

The Vice Director runs a continuous Director cycle around and between research waves. A wave is one instrument inside the cycle, not a batch that must finish before direction changes.

1. **Synchronize the live picture.** Read the current proof spine, toolkit, research tree, current guidance, relevant new research, and the certification state of mathematics the favored route actually depends on. During a long cycle, resynchronize at natural mathematical boundaries when concurrent work may have changed that picture.
2. **Perform structural synthesis.** Run the full reconciliation/composition and abstraction/conceptual-lift pass above over the mathematics relevant to the live frontier. Re-test substantive new results at their earliest natural proof coordinates, but do not stop there: compare old and new formulations globally, seek the mechanism behind them, test stronger/weaker/dual/obstruction forms, and reconsider the abstraction tree itself. This stage determines the best current mathematical picture before operational choices are made.
3. **Select, track, and batch load-bearing mathematics for audit.** Determine which exact extra-spine statements and proofs have become necessary to the shortest favored route, an important live alternative, a proposed canonical rewrite, or a genuinely reusable toolkit theorem. The Vice Director owns this audit triage and keeps track of which active load-bearing dependencies still require independent certification. At natural synthesis points, group the currently relevant exact targets into a coherent **audit batch** and hand that batch to one independent Auditor under `04_AUDIT_PROTOCOL.md`. A batch may contain several related statements, proofs, or rewrites, and should include enough context to explain their mathematical relationship and priority without asking the Auditor to reconstruct the research strategy. Do not turn the general research backlog into an audit batch: there is no chronological audit frontier and no requirement to certify intermediate results that the live strategy does not depend on.
4. **Propagate certified mathematics and decide durable placement.** When targets in a batch pass, update the live dependency picture to use the certified facts where they remain relevant. Separately decide whether each fact has earned a stable place in the proof spine, toolkit, or neither, under `01_ARCHITECTURE.md`. If an audit fails, weakens, or materially repairs a live dependency, rerun the affected part of structural synthesis rather than merely patching the old route.
5. **Re-evaluate the shortest favored route from the top down.** Starting from the theorem and earliest unresolved bridge, express the route in the abstraction discovered by structural synthesis. Remove or compress branches that are closed, subsumed, contradicted, bypassed, unnecessarily strong, or artifacts of an older explanation.
6. **Rewrite the research tree as a pure outline.** Preserve the hierarchy theorem-level objective → unresolved bridge → candidate mechanism → concrete subproblem only when that hierarchy still reflects the mathematics. If structural synthesis found a better decomposition, rewrite the hierarchy accordingly. Express every node as one brief headline line and let nesting carry the refinement.
7. **Place guidance in the tree.** Ensure the mathematical target of current guidance appears at the correct node or leaf of the outline. The tree records the target itself, not prose explaining why the guidance was chosen; that rationale belongs in `#gn3-guidance`.
8. **Issue or revise guidance.** State the common mathematical target and enough context to make its role in the current structural picture clear. Do not preserve an old target merely because it was previously issued.
9. **Canonize only after exact certification and structural stability.** Durable proof dependencies belong eventually in audited canonical mathematics rather than remaining only in Slack or the tree. A passed local fact need not be canonized if structural synthesis has not yet established its durable role.
10. **Escalate to Astra when the abstraction itself needs to change.** Escalate for a strategic reframe, stronger parent theorem, global bypass, major invariant change, or substantial architecture decision rather than ordinary local direction.

Then repeat. The cycle exists to keep rebuilding the best mathematical understanding as the corpus changes, not merely to accumulate results, move them between surfaces, or push the current proof one lemma at a time. Audit tracking, tree maintenance, and canonical placement serve structural synthesis; they are not substitutes for it.

## Research-tree management

`RESEARCH_TREE.md` is a **pure nested outline** of the live mathematical search. The file contains nothing except the outline itself: no title, preamble, legend, framing paragraphs, instructions, rationale, commentary, bibliography, audit notes, or closing remarks. All rules for maintaining the tree belong here in `INIT/` rather than in the tree.

Each outline item is one brief Markdown line expressing a mathematical headline statement or guiding abstraction. Multiple short sentences, formulas, or clauses may appear on that same line when needed for precision, but a node has no attached body paragraph. Do not turn a node into a mini-memo, proof sketch, implementation checklist, literature note, or explanation of why it matters.

Nesting carries resolution. A parent states the coarser abstraction; each child refines that parent into a finer abstraction, branch, mechanism, obstruction, or concrete target. Continue downward only as far as the live search usefully distinguishes the mathematics. Leaves should be concrete headline statements or concrete open subproblems when the search has reached that resolution.

The outline may use bullets or numbering. It should normally use one consistent style within a given revision. Semantic mathematical statements, not result IDs or workflow history, define the nodes. A guidance tag such as `[G##]` may be included inline on the relevant item when useful for retrieval, but it does not justify any additional prose.

Full proofs are excluded from the research tree. Proofs, derivations, casework, computations, examples, supporting evidence, and detailed obstructions belong in Slack threads or canonical mathematical documents. Only when the exact mathematical nature of a node makes a small amount of proof-like content genuinely inseparable from stating it may the minimum unavoidable content appear inline in that same outline item; never add a separate proof body beneath the node.

Individual discoveries enter the tree only when they change the live abstraction, create or eliminate a branch, sharpen an obstruction, or become a concrete leaf target needed by a live route. A discovery does not earn a node merely because it is correct, useful, audited, recent, or repeatedly cited.

Researchers normally communicate tree corrections and structural suggestions through `#gn3-research`; the Director or delegated Vice Director performs the low-concurrency rewrite. For a given structural-synthesis pass, one compressor owns the tree edit so that the hierarchy remains coherent.

The tree has a low admission bar for a genuinely live branch and a high retention bar thereafter. Merge overlapping nodes, promote stronger parent abstractions, split only where the mathematics truly branches, and delete dead or redundant branches aggressively. Git history is sufficient recovery; chronology, credit, audit transcripts, and obsolete proof ontology do not belong in the outline.

## Search state and durable mathematics

Slack is the discovery stream. The research tree is the terse hierarchical outline of the current search. The proof spine is the sequential canonical proof. The toolkit is the selected reusable shelf.

Compression from Slack into the tree is structural synthesis, not copying. Compression from the tree into proof or toolkit is stricter still: only mathematics that has earned a durable role survives.

There is no separate `RESEARCH_STATE.md`. The research tree carries the current live abstraction and guidance location; the proof spine carries the mathematical route and explicit open boundary. Avoid creating another summary layer that can drift between them.
