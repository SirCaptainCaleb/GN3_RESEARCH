# 03 — GN3 research protocol

This file governs live mathematical search, Director/Vice Director synthesis, guidance, and maintenance of `GN3/RESEARCH_TREE.md`.

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

## Director cycle

The Vice Director runs a continuous Director cycle around and between research waves. A wave is one instrument inside the cycle, not a batch that must finish before direction changes.

1. **Synchronize the live picture.** Read the current proof spine, toolkit, research tree, current guidance, relevant new research, and the certification state of mathematics the favored route actually depends on. During a long cycle, resynchronize at natural mathematical boundaries when concurrent work may have changed that picture.
2. **Re-test every substantive new result at the earliest possible proof coordinate.** Test the statement as written and natural strengthened or useful weakened forms. Ask at the earliest point where its hypotheses can hold whether it proves, simplifies, strengthens, bypasses, or invalidates an existing step. A result discovered later in the proof may close an earlier branch or make later machinery unnecessary.
3. **Select, track, and batch load-bearing mathematics for audit.** Determine which exact extra-spine statements and proofs have become necessary to the shortest favored route, an important live alternative, a proposed canonical rewrite, or a genuinely reusable toolkit theorem. The Vice Director owns this audit triage and keeps track of which active load-bearing dependencies still require independent certification. At natural synthesis points, group the currently relevant exact targets into a coherent **audit batch** and hand that batch to one independent Auditor under `04_AUDIT_PROTOCOL.md`. A batch may contain several related statements, proofs, or rewrites, and should include enough context to explain their mathematical relationship and priority without asking the Auditor to reconstruct the research strategy. Do not turn the general research backlog into an audit batch: there is no chronological audit frontier and no requirement to certify intermediate results that the live strategy does not depend on.
4. **Integrate audited mathematics.** When targets in a batch pass, place the surviving mathematical facts at their natural locations in the live abstraction if they are still needed, and decide whether they should be compressed into the proof spine or toolkit. If an audit fails, weakens, or materially repairs a live dependency, propagate that change through the favored route, research tree, and guidance. Batch assignment does not make certification collective: each exact mathematical target retains its own disposition and scope.
5. **Re-evaluate the shortest favored route from the top down.** Start from the theorem and earliest unresolved step. Identify branches that are closed, subsumed, contradicted, bypassed, or unnecessarily strong, and remove or compress obsolete structure.
6. **Rewrite the research tree as a pure outline.** Preserve the hierarchy theorem-level objective → unresolved bridge → candidate mechanism → concrete subproblem, but express every node as one brief headline line and let nesting carry the refinement. Remove explanations, proof sketches, checklists, framing prose, and other material that belongs in Slack, guidance, the proof spine, toolkit, or these init files.
7. **Place guidance in the tree.** Ensure the mathematical target of current guidance appears at the correct node or leaf of the outline. The tree records the target itself, not prose explaining why the guidance was chosen; that rationale belongs in `#gn3-guidance`.
8. **Issue or revise guidance.** State the common mathematical target and enough context to make its role in the proof clear. Do not preserve an old target merely because it was previously issued.
9. **Canonize only after exact certification.** Durable proof dependencies belong eventually in audited canonical mathematics rather than remaining only in Slack or the tree. A passed local fact need not be canonized if it is still temporary working structure.
10. **Escalate to Astra when the abstraction itself needs to change.** Escalate for a strategic reframe, stronger parent theorem, global bypass, major invariant change, or substantial architecture decision rather than ordinary local direction.

Then repeat. The cycle exists to keep asking whether new mathematics shortens the proof and improves the abstraction, not merely to generate more local results. Audit tracking is part of this synthesis responsibility: the Vice Director needs to know which facts the favored route presently relies on and which of those still need certification, and normally sends those needs to the Auditor in coherent batches rather than as a stream of one-off requests. GN3 does not maintain a project-wide audit backlog for every research result.

## Research-tree management

`GN3/RESEARCH_TREE.md` is a **pure nested outline** of the live mathematical search. The file contains nothing except the outline itself: no title, preamble, legend, framing paragraphs, instructions, rationale, commentary, bibliography, audit notes, or closing remarks. All rules for maintaining the tree belong here in `GN3/INIT/` rather than in the tree.

Each outline item is one brief Markdown line expressing a mathematical headline statement or guiding abstraction. Multiple short sentences, formulas, or clauses may appear on that same line when needed for precision, but a node has no attached body paragraph. Do not turn a node into a mini-memo, proof sketch, implementation checklist, literature note, or explanation of why it matters.

Nesting carries resolution. A parent states the coarser abstraction; each child refines that parent into a finer abstraction, branch, mechanism, obstruction, or concrete target. Continue downward only as far as the live search usefully distinguishes the mathematics. Leaves should be concrete headline statements or concrete open subproblems when the search has reached that resolution.

The outline may use bullets or numbering. It should normally use one consistent style within a given revision. Semantic mathematical statements, not result IDs or workflow history, define the nodes. A guidance tag such as `[G##]` may be included inline on the relevant item when useful for retrieval, but it does not justify any additional prose.

Full proofs are excluded from the research tree. Proofs, derivations, casework, computations, examples, supporting evidence, and detailed obstructions belong in Slack threads or canonical mathematical documents. Only when the exact mathematical nature of a node makes a small amount of proof-like content genuinely inseparable from stating it may the minimum unavoidable content appear inline in that same outline item; never add a separate proof body beneath the node.

Individual discoveries enter the tree only when they change the live abstraction, create or eliminate a branch, sharpen an obstruction, or become a concrete leaf target needed by a live route. A discovery does not earn a node merely because it is correct, useful, audited, recent, or repeatedly cited.

Researchers normally communicate tree corrections and structural suggestions through `#gn3-research`; the Director or delegated Vice Director performs the low-concurrency rewrite. For a given synthesis pass, one compressor owns the tree edit so that the hierarchy remains coherent.

The tree has a low admission bar for a genuinely live branch and a high retention bar thereafter. Merge overlapping nodes, promote stronger parent abstractions, split only where the mathematics truly branches, and delete dead or redundant branches aggressively. Git history is sufficient recovery; chronology, credit, audit transcripts, and obsolete proof ontology do not belong in the outline.

## Search state and durable mathematics

Slack is the discovery stream. The research tree is the terse hierarchical outline of the current search. The proof spine is the sequential canonical proof. The toolkit is the selected reusable shelf.

Compression from Slack into the tree is synthesis, not copying. Compression from the tree into proof or toolkit is stricter still: only mathematics that has earned a durable role survives.

There is no separate `RESEARCH_STATE.md`. The research tree carries the current live abstraction and guidance location; the proof spine carries the mathematical route and explicit open boundary. Avoid creating another summary layer that can drift between them.
