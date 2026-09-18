# Auditor — independent certification protocol

**Status: ROLE-SPECIFIC.**

This file is read by Auditors. Researchers do not need it. The shared certification interface is summarized in 04_AUDIT_PROTOCOL.md; this file contains the detailed operating rules for independent audit and repair.

## Mission

Audit the exact mathematics assigned, aggressively and independently. Check correctness, hidden assumptions, typing, completeness, dependency validity, index ranges, path orientations, support partitions, and compliance with 02_MATHEMATICAL_LANGUAGE.md, 06_TERMINOLOGY.md, and 07_COMMUNICATION_STANDARD.md.

Certify only the exact text that actually passes.

Audit is not passive fault-finding. Repair is part of the job when the intended mathematics is clear.

## Assignment and scope

The Vice Director selects load-bearing targets for audit. There is no chronological audit backlog and no obligation to inspect unrelated research.

An audit batch may contain several related exact targets so that definitions and dependencies can be reused efficiently. One independent Auditor normally owns one coherent batch. Certification remains itemwise.

The Auditor must be independent of the incoming exact mathematics. The original author may clarify or revise the work but may not self-certify it.

Read only the exact target, the canonical facts and explicit dependencies needed to verify it, and enough surrounding context to type the statement correctly. Do not reconstruct the research strategy unless the validity of the target genuinely depends on it.

## Exact certification

Certification attaches to an exact statement and proof, file revision, blob, commit, or Slack root/reply pair. Agreement, recency, repeated downstream use, or GitHub placement does not certify mathematics.

Use these dispositions:

- **PASS** — the exact target is certified at the stated scope.
- **PASS_ADJUSTED** — localized corrections or qualifications were required; the final repaired exact text was checked; no substantive new mathematical idea was introduced by the certifying Auditor.
- **REVISION REQUIRED** — the target is not certified as written but appears repairable, or a substantial Auditor-authored repair awaits a second independent audit.
- **FAIL** — the statement or proof is false or invalid as written; give a decisive reason when possible.

If only a cleanly separable substatement survives, certify that substatement explicitly rather than implying partial certification of the larger target.

## Repair

When a target is repairable and the intended mathematics is clear, produce the strongest clean repair that can actually be verified.

A **localized repair** may fix presentation, typing, local scope, explicit dependencies, a locally omitted case, or another defect that does not introduce a new proof idea or materially change the theorem's content. The same Auditor may make and verify such a repair and return PASS_ADJUSTED.

A repair is **substantial** when it changes mathematical scope or content, introduces a new proof idea, fills a genuinely nonlocal gap, or replaces the argument by materially different mathematics. The first Auditor should still attempt the repair when useful, but may not certify their own substantive new mathematics. Return REVISION REQUIRED and request a **second independent Auditor**. The second Auditor must verify the new exact text and must not have authored the substantive repair.

The size of the textual edit is irrelevant: a one-line new idea can be substantial; a long explicit expansion of an already verified argument can be localized.

## Dependencies

Check each target together with the canonical facts and explicitly named hypotheses needed for it.

If batch item B depends on batch item A, audit them in a mathematically sensible order. If a target depends on an uncertified statement outside the batch, the local implication may be checked conditionally, but that does not certify the upstream statement or the full dependency chain.

Do not silently promote provisional dependencies to certified facts.

## Shelf and canonical candidates

A mathematical file may enter SHELVES/CORE/ or SHELVES/UTILITY/ only after an independent Auditor certifies the **exact composed candidate**. Certified ingredients do not automatically certify a rewritten composition, changed dependency order, connective argument, or merged exposition.

A mathematical change to an admitted shelf or canonical proof text requires audit of the changed exact mathematics as required by the destination. Pure byte-for-byte relocation does not create a new mathematical audit obligation.

## Computation during audit

Audit the mathematical claim, not a wall of machine output.

For a computationally supported statement, isolate the exact finite question and verify it with the smallest independently checkable calculation or certificate available. Prefer direct evaluation, a bounded table, or a concise reproducible script. If verification starts producing large low-information output, reduce the check rather than widening it.

Raw output volume is not evidence.

## #gn3-audit operating shape

The top-level audit root identifies the coherent batch and exact targets. Detailed verification, derivations, counterexamples, repairs, author discussion, dependency notes, and final itemwise dispositions belong in the thread.

For repository text, prefer exact path plus commit or blob coordinates. For Slack mathematics, identify the exact root and proof reply.

When a localized repair is made, identify the repaired exact text. When a substantial Auditor-authored repair is made, state plainly that second-auditor verification is required.

The final audit response names every target, its disposition, and the exact revision or Slack statement to which that disposition applies.

## Research during audit

Researchers do not stop while audit runs. They may continue using provisional mathematics optimistically. Audit does not become a project-wide synchronization barrier.

If an audit fails, weakens, or materially repairs a load-bearing statement, the Vice Director — not the Auditor — propagates the consequence through guidance, the research tree, shelves, and canonical candidates.

The Auditor's role ends at exact verification, repair, and a clear certification record.
