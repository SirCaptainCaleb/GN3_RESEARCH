# 04 — GN3 audit protocol

This file governs independent certification of GN3 mathematics. Research may use provisional mathematics optimistically; certification attaches only to the exact statement and proof independently checked.

## What gets audited

GN3 does **not** audit every intermediate research result. Slack discoveries, temporary lemmas, research-tree observations, and other extra-spine mathematics remain ordinary search material unless and until the Vice Director determines that they have become load-bearing.

The Vice Director owns audit triage and audit tracking during the Director cycle. At natural synthesis points, the Vice Director sends a **batch audit request** containing the exact load-bearing mathematical targets that currently need independent certification—for example statements necessary to the shortest favored proof, an important live alternative, proposed canonical rewrites, or genuinely reusable toolkit theorems.

A batch should identify each exact statement and proof to be checked, together with enough context to explain why the items are load-bearing and how they relate. The Auditor is not asked to reconstruct the research strategy, maintain a chronological audit backlog, or inspect unrelated pending research. Batching is for coherent verification and efficient context reuse, not for sweeping up every recent result.

There is no project-wide audit frontier, no requirement that research results carry audit-status tags, and no requirement to certify results merely because they were posted earlier. The Vice Director tracks the certification needs of the mathematics the live strategy actually depends on and decides what belongs in the next batch.

## What an audit certifies

An audit batch may contain several **exact mathematical targets**: stated theorems, lemmas, proof sections, proposed canonical rewrites, or other explicitly delimited texts. GitHub placement, downstream use, recency, and agreement among researchers do not certify mathematics.

Each audit batch is owned by **one independent Auditor**. The Auditor must be independent of the authorship of the exact text being certified. The Auditor may exploit shared definitions, dependencies, or context across the batch, and may choose a sensible internal order of verification. Routine batches should not be duplicated in parallel or split among several auditors merely for throughput. If a batch is genuinely too large for one coherent audit, the Vice Director decides explicitly how to divide it without losing necessary whole-object or cross-dependency verification.

Certification remains **itemwise even when assignment is batched**. Each exact target receives its own scope and disposition; one failed or revised item does not automatically determine the status of the others. The Auditor should also report material dependency interactions across batch items when one target's validity changes what can be concluded about another.

An author may explain or repair the work but may not self-certify it.

A substantive repair, strengthening, or rewrite is new mathematical text and requires fresh independent audit. Purely editorial changes may retain certification only after an independent auditor confirms that the mathematics is unchanged.

Research does not pause while audit is underway. Researchers may continue to use provisional mathematics optimistically. If an audit fails, weakens, or materially repairs a load-bearing statement, the Vice Director propagates that correction through the favored route, research tree, guidance, and any affected canonical candidate.

## Dependencies

The Auditor checks each exact target together with the canonical facts and explicitly named hypotheses needed to verify it. If one batch item depends on another batch item, audit that dependency in a mathematically sensible order. If a target depends on an uncertified statement outside the batch, the Auditor may verify the local implication conditional on that exact hypothesis, but doing so does not certify the upstream statement or make the whole dependency chain unconditional.

The audit response should name unresolved dependencies clearly. The Vice Director then decides whether they belong in a later audit batch. GN3 does not maintain separate `CONTINGENT` status tags or a chronological mechanism for clearing them.

## `#gn3-audit` structure

Each Vice-Director batch gets one concise top-level audit root identifying the batch and enumerating or linking its exact targets. Prefer GitHub paths plus commit or blob coordinates for repository text; for Slack mathematics, link the exact research roots/threads and state the scope being audited. Retain the `[G##]` tag when useful for retrieval.

Detailed verification, derivations, counterexamples, objections, proposed repairs, author responses, dependency notes, and discussion belong in replies to the batch root. The Auditor may organize replies itemwise when useful. The final batch response gives a separate disposition for every exact target and names the exact revision or Slack statement to which each disposition applies. That thread is the record of the certification event; the Vice Director consumes the results during synthesis and updates the live strategy or canonical candidates as needed.

Use these dispositions for each target:

- **PASS** — the exact target is certified at the stated scope;
- **PASS_ADJUSTED** — corrections or qualifications were required and the final repaired version was checked;
- **REVISION REQUIRED** — not certified as written, but the defect appears repairable or falsity has not been established; state exactly what requires recheck;
- **FAIL** — false or invalid as stated; give a concrete counterexample, invalid inference, or other decisive reason when possible.

A PASS may include non-load-bearing editorial notes. If only a cleanly separable substatement survives a failed larger target, certify that substatement explicitly rather than inferring partial certification.

## Auditing computations

Audit the mathematical claim, not a wall of machine output. For a computationally supported step, identify the exact finite question and the smallest independently checkable calculation or certificate that verifies it. Prefer direct evaluation of the few needed values, a bounded table, or a concise reproducible script over regenerating large symbolic expansions or exhaustive traces.

If independent verification begins producing large output with little additional mathematical information, stop and reduce the check rather than repeatedly widening the computation. A load-bearing computation must have a reproducible method and a concise mathematical interface; raw output volume is not evidence of correctness.

## Propagation after audit

A PASS does not itself rewrite canonical project state. The Vice Director decides how the certified mathematics affects the favored route and whether it should enter the proof spine or toolkit. When certification changes durable mathematics, update the appropriate canonical text and record the high-signal delta in `#gn3-changelog`. Preserve provenance only when it materially improves recoverability or future audit.

There is no separate `STATUS.md`, project-wide audit ledger, chronological audit frontier, or research-headline status system. Current proof openness is visible in the proof spine. The live abstraction and the set of audit-relevant dependencies are managed by the Vice Director through the Director cycle. Exact certification of audited targets is recorded in the corresponding batch audit thread and, when mathematics becomes durable, in the canonical revision that incorporates it.

A REVISION REQUIRED or FAIL that changes the live search is fed back to the Vice Director so the research tree and guidance can be recompressed. Audit transcripts do not belong in the research tree.
