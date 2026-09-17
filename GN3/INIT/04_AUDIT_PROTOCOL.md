# 04 — GN3 audit protocol

This file governs independent certification of GN3 mathematics. Research may use provisional mathematics optimistically; certification attaches only to the exact statement and proof independently checked.

## What gets audited

GN3 does **not** audit every intermediate research result. Slack discoveries, temporary lemmas, research-tree observations, and other extra-spine mathematics remain ordinary search material until they become load-bearing.

The Vice Director owns audit triage during the Director cycle. Send an exact mathematical object to `#gn3-audit` when independent certification would materially change how the active proof is allowed or expected to rely on it—for example when it has become necessary to the shortest favored proof, an important live alternative, a proposed canonical rewrite, or a genuinely reusable toolkit theorem.

The handoff identifies the exact statement and proof to be checked and why it is load-bearing. It does not ask the Auditor to reconstruct the research strategy.

## What an audit certifies

An audit certifies an **exact mathematical target**: a stated theorem, lemma, proof section, proposed canonical rewrite, or other explicitly delimited text. GitHub placement, downstream use, recency, and agreement among researchers do not certify mathematics.

The Auditor must be independent of the authorship of the exact text being certified. An author may explain or repair the work but may not self-certify it.

A substantive repair, strengthening, or rewrite is new mathematical text and requires fresh independent audit. Purely editorial changes may retain certification only after an independent auditor confirms that the mathematics is unchanged.

Research does not pause while audit is underway. If an audit fails, weakens, or materially repairs a load-bearing statement, the Vice Director propagates that correction through the favored route, research tree, guidance, and any affected canonical candidate.

## Visible status travels with a research result

A top-level `#gn3-research` mathematical discovery headline that may be relied on downstream carries its audit status on the headline itself, so workers do not need to search the audit channel merely to learn whether the result is certified.

Ordinary status tags are:

- `[PENDING]` — not independently certified at the displayed exact statement/proof, or substantively changed since certification;
- `[PASS]` — independently certified exactly as displayed;
- `[PASS_ADJUSTED]` — independently certified after audit-driven corrections or qualifications incorporated into the displayed result;
- `[FAIL]` — independently determined false or invalid as displayed.

The guidance tag precedes audit status, for example `[G17][PENDING] ...`. These tags are workflow metadata only and never enter mathematical statements.

## Contingent certification

Use `[CONTINGENT]` when the displayed result has passed its local audit but still depends on one or more unresolved upstream results. Typical forms are `[PASS][CONTINGENT]` and `[PASS_ADJUSTED][CONTINGENT]`.

The audit thread states the exact unresolved dependencies. A contingent result may be used optimistically if those dependencies are carried explicitly, but it is treated as pending for unconditional certification and for the audit frontier.

When every named contingency becomes certified at exactly the required statement and no unresolved dependency remains, remove `[CONTINGENT]` without repeating the completed local audit. If a dependency changes materially rather than merely becoming certified, reconsider the dependent result and audit again when necessary.

## Audit frontier

`[FRONTIER]` is an independent modifier attached to the latest audit-resolved mathematical research headline such that every earlier auditable research-result headline in `#gn3-research` is also audit-resolved and none is contingent.

An auditor scanning backward may stop at `[FRONTIER]`: there is no unresolved audit debt earlier than that point. Audit-resolved means `[PASS]`, `[PASS_ADJUSTED]`, or `[FAIL]` without `[CONTINGENT]`. `[PENDING]` and every `[CONTINGENT]` result block the frontier.

Keep one current frontier marker. After status changes, advance it through the longest contiguous chronological run of audit-resolved research-result headlines and stop at the first pending or contingent result. Guidance posts, administrative messages, ordinary discussion, and explicit non-result/null reports do not block it. If an earlier result is substantively changed and loses certification, retreat the frontier to the latest earlier point where the invariant remains true.

## `#gn3-audit` structure

Each audit target gets one concise top-level root identifying the exact target. Prefer a GitHub path plus commit or blob coordinate for repository text; for Slack mathematics, link the exact research root/thread and state the scope being audited. Retain the `[G##]` tag when useful for retrieval.

Detailed verification, derivations, counterexamples, objections, proposed repairs, author responses, and discussion belong in replies to the audit root. The final disposition belongs in the same thread and names the exact revision it applies to. Then update the corresponding research headline's visible status and maintain `[FRONTIER]` when appropriate.

Use these dispositions:

- **PASS** — the exact target is certified at the stated scope;
- **PASS_ADJUSTED** — corrections or qualifications were required and the final repaired version was checked;
- **REVISION REQUIRED** — not certified as written, but the defect appears repairable or falsity has not been established; keep the research result pending and state what requires recheck;
- **FAIL** — false or invalid as stated; give a concrete counterexample, invalid inference, or other decisive reason when possible.

A PASS may include non-load-bearing editorial notes. If only a cleanly separable substatement survives a failed larger target, certify that substatement explicitly rather than inferring partial certification.

## Auditing computations

Audit the mathematical claim, not a wall of machine output. For a computationally supported step, identify the exact finite question and the smallest independently checkable calculation or certificate that verifies it. Prefer direct evaluation of the few needed values, a bounded table, or a concise reproducible script over regenerating large symbolic expansions or exhaustive traces.

If independent verification begins producing large output with little additional mathematical information, stop and reduce the check rather than repeatedly widening the computation. A load-bearing computation must have a reproducible method and a concise mathematical interface; raw output volume is not evidence of correctness.

## Propagation after audit

A PASS does not itself rewrite canonical project state. When certification changes durable mathematics, update the appropriate proof-spine or toolkit text and record the high-signal delta in `#gn3-changelog`. Preserve provenance only when it materially improves recoverability or future audit.

There is no separate `STATUS.md`. Current proof openness is visible in the proof spine; live strategic dependence is visible in the research tree; exact research certification is visible on the result and in its audit thread.

A REVISION REQUIRED or FAIL that changes the live search is fed back to the Vice Director so the research tree and guidance can be recompressed. Audit transcripts do not belong in the research tree.
