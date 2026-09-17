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

## Conservative computation discipline

Prefer a human-scale mathematical argument to a broad symbolic or exhaustive computation whenever the former is reasonably available. Computation is most useful when it answers a sharply stated finite question; it is not the default way to compare two formulations or re-derive a known structural fact.

Before launching a calculation, state the exact quantity, identity, case set, or counterexample being sought and estimate the expected output. Prefer targeted scalar evaluations, short exact checks, bounded case tables, or a small script that returns a concise invariant over expanding large symbolic expressions, matrices, spectra, polynomial recurrences, or exhaustive traces.

**Do not flood the working context with large computational output.** If a symbolic comparison or finite enumeration begins producing long expansions, large tables, or repeated near-duplicate output, stop rather than retrying increasingly broad variants. Replace it with a conceptual derivation, a smaller check, or a clearly isolated computational subclaim. In particular, do not expand Johnson-scheme polynomials, characteristic polynomials, large matrices, or comparable algebra from scratch merely to verify a few values when those values can be obtained or checked directly.

When computation is genuinely load-bearing, retain only what makes the argument checkable: the precise input, method, concise output or certificate, and the mathematical inference drawn from it. A huge transcript is not a proof. If a computation cannot be reduced to a checkable certificate or independently reproducible bounded calculation, treat the conclusion as provisional rather than silently relying on the output.

## Director cycle

The Vice Director runs a continuous Director cycle around and between research waves. A wave is one instrument inside the cycle, not a batch that must finish before direction changes.

1. **Synchronize the live picture.** Read the current proof spine, toolkit, research tree, current guidance, relevant new research, and the audit state of mathematics the favored route depends on.
2. **Re-test every substantive new result at the earliest possible proof coordinate.** Test the statement as written and natural strengthened or useful weakened forms. Ask at the earliest point where its hypotheses can hold whether it proves, simplifies, strengthens, bypasses, or invalidates an existing step. A result discovered later in the proof may close an earlier branch or make later machinery unnecessary.
3. **Select load-bearing mathematics for audit.** Determine which exact extra-spine statements and proofs have become necessary to the shortest favored route, an important live alternative, a proposed canonical rewrite, or a genuinely reusable toolkit theorem. Route those exact objects—not the general research backlog—to independent audit under `04_AUDIT_PROTOCOL.md`.
4. **Integrate audited mathematics.** When an exact result passes, place the mathematical fact at its natural location in the live abstraction if it is still needed, and decide whether it should be compressed into the proof spine or toolkit.
5. **Re-evaluate the shortest favored route from the top down.** Start from the theorem and earliest unresolved step. Identify branches that are closed, subsumed, contradicted, bypassed, or unnecessarily strong, and remove or compress obsolete structure.
6. **Maintain the research tree.** Keep `GN3/RESEARCH_TREE.md` as the best current hierarchy of theorem-level objective → unresolved bridge → candidate mechanism → concrete subproblem. Merge overlapping discoveries, promote a supported parent abstraction when it explains several local facts, preserve concrete blockers, and split only where the mathematics truly branches.
7. **Place guidance in the tree.** Before or while issuing guidance, identify the live node or closely related node cluster being attacked and why it is the right next descent from the theorem-level objective. If guidance no longer matches the best abstraction, revise the tree and guidance together.
8. **Issue or revise guidance.** State the common mathematical target and enough context to make its role in the proof clear. Do not preserve an old target merely because it was previously issued.
9. **Canonize only after exact certification.** Durable proof dependencies belong eventually in audited canonical mathematics rather than remaining only in Slack or the tree. A passed local fact need not be canonized if it is still temporary working structure.
10. **Escalate to Astra when the abstraction itself needs to change.** Escalate for a strategic reframe, stronger parent theorem, global bypass, major invariant change, or substantial architecture decision rather than ordinary local direction.

Then repeat. The cycle exists to keep asking whether new mathematics shortens the proof and improves the abstraction, not merely to generate more local results.

## Research-tree management

`GN3/RESEARCH_TREE.md` is the mutable hierarchical model of the live search. It is not canonical mathematics, an audit ledger, or an archive of discoveries. It should keep visible the chain

`theorem -> earliest unresolved bridge -> candidate mechanism -> concrete subproblem`.

Nodes have semantic mathematical names rather than result IDs. A node may contain a compact argument sketch, a synthesized observation, a blocker, or children representing genuine decomposition or competing mathematical routes. Current guidance should have an identifiable place in the hierarchy.

Individual discoveries do not become nodes merely because they were proved or audited. The Director or delegated Vice Director acts as the compressor: read the relevant `[G##]` roots and threads, merge equivalent facts, promote a supported abstraction, preserve precise blockers and necessary hypotheses, and delete dead routes or redundant local steps.

Researchers normally communicate tree corrections and structural suggestions through `#gn3-research`; the Director or delegated Vice Director performs the low-concurrency rewrite. For a given synthesis pass, one compressor owns the tree edit so that the hierarchy remains coherent.

The tree has a low admission bar during synthesis and a high retention bar. Keep a branch only while it represents a live unresolved subproblem, a genuinely competitive route, or a local fact still needed by a live route. Once an argument solidifies, move the surviving mathematics to the proof spine or toolkit if it earns a durable role. Once a route dies, remove it unless a concise negative lesson is worth preserving elsewhere.

Git history provides recovery for deleted tree structure. Do not preserve chronology, credit, audit transcripts, or obsolete proof ontology merely because they once helped discovery.

## Search state and durable mathematics

Slack is the discovery stream. The research tree is the compressed current search model. The proof spine is the sequential canonical proof. The toolkit is the selected reusable shelf.

Compression from Slack into the tree is synthesis, not copying. Compression from the tree into proof or toolkit is stricter still: only mathematics that has earned a durable role survives.

There is no separate `RESEARCH_STATE.md`. The research tree carries the current live abstraction and guidance location; the proof spine carries the mathematical route and explicit open boundary. Avoid creating another summary layer that can drift between them.
