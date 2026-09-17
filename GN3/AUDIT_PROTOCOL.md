# GN3 audit protocol

This file specifies the operational structure of independent mathematical audit. The certification principles in `ARCHITECTURE.md` remain authoritative.

## What an audit certifies

An audit certifies an **exact mathematical target**: a stated theorem, lemma, proof section, proposed canonical rewrite, or other explicitly delimited mathematical text. GitHub placement, downstream use, or agreement among researchers does not certify mathematics.

The auditor must be independent of the authorship of the exact text being certified. An author may explain, repair, or defend their work, but may not self-certify it.

## Visible status travels with the research result

Every top-level `#gn3-research` mathematical discovery headline that may be relied on downstream must carry its audit status on the headline itself. A worker should not have to search `#gn3-audit` merely to learn whether a result is certified.

Ordinary status tags are:

- `[PENDING]` — not yet independently certified at the displayed exact statement/proof, or substantively changed since its last certification.
- `[PASS]` — independently certified exactly as displayed.
- `[PASS_ADJUSTED]` — independently certified after audit-driven corrections or qualifications incorporated into the displayed exact result.
- `[FAIL]` — independently determined false or invalid as displayed.

The guidance tag precedes the audit status, for example `[G17][PENDING] ...` or `[G17][PASS] ...`. These tags are workflow metadata only and never enter canonical mathematical statements.

A substantive rewrite of a passed result returns it to `[PENDING]`. Purely editorial changes may retain PASS only after an independent auditor confirms that the mathematics is unchanged.

## Contingent certification

Retain `[CONTINGENT]` as a modifier when the displayed result has passed its local audit but still depends on one or more unresolved upstream results. Typical forms are `[PASS][CONTINGENT]` and `[PASS_ADJUSTED][CONTINGENT]`.

The audit thread must state the exact unresolved dependency or dependencies. A contingent result may be used optimistically in research if those dependencies are carried explicitly, but it is treated as pending for unconditional certification and for the audit frontier.

When every named contingency becomes certified at exactly the required statement and no other unresolved dependency remains, `[CONTINGENT]` may be removed without redoing the already completed local audit. If a dependency changes materially rather than merely becoming certified, the dependent result must be reconsidered and may require fresh audit.

## The audit frontier

`[FRONTIER]` is an independent modifier attached to the latest audit-resolved mathematical research headline such that **every earlier auditable research-result headline in `#gn3-research` is also audit-resolved and none is contingent**.

Thus an auditor scanning backward through research results may stop on seeing `[FRONTIER]`: there is no unresolved audit debt earlier than that point. The frontier is a property of audit coverage, not mathematical strength.

Audit-resolved means `[PASS]`, `[PASS_ADJUSTED]`, or `[FAIL]` without `[CONTINGENT]`. `[PENDING]` and every `[CONTINGENT]` result block the frontier. Because failure is still a completed audit, `[FRONTIER]` may in principle modify `[FAIL]` as well as a passing status.

Only one current `[FRONTIER]` marker should exist. After an audit changes statuses, advance it through the longest contiguous chronological run of audit-resolved research-result headlines and remove the marker from its previous location. Stop immediately at the first `[PENDING]` or `[CONTINGENT]` result. Guidance posts, administrative messages, ordinary discussion, and explicit non-result/null reports do not themselves block the frontier.

If an earlier result is later substantively changed, invalidating its old certification, the frontier must retreat to the latest earlier point for which the invariant remains true.

## Slack structure

`#gn3-audit` uses a high-signal root/thread discipline.

Each audit target gets one concise top-level message. The root states what is being audited and identifies the exact target sufficiently to retrieve it. Prefer a GitHub path plus commit or blob coordinate for repository text. For Slack mathematics, link the exact research headline/thread and state the scope being audited.

When an audit target arose from a Director research wave, retain its `[G##]` tag in the audit root when useful for retrieval. The guidance tag is administrative metadata only.

Detailed verification, derivations, counterexamples, objections, proposed repairs, author responses, and discussion belong in replies to the audit root. Do not paste a long proof or audit transcript into the channel root merely to make it visible.

The final audit disposition belongs in the same thread and names the exact revision it applies to. After disposition, update the corresponding research headline's visible status and then maintain `[FRONTIER]` if the contiguous coverage invariant permits it.

## Audit dispositions

Use the following ordinary dispositions:

- **PASS** — the exact target is mathematically certified at the stated scope.
- **PASS_ADJUSTED** — corrections or qualifications were required and the auditor has checked the final displayed repaired version.
- **REVISION REQUIRED** — the target is not certified as written, but the defect appears repairable or the auditor has not established falsity. The research headline remains `[PENDING]`; state the precise defect and what must be rechecked.
- **FAIL** — the target is false or invalid as stated. Give a concrete counterexample, invalid inference, or other decisive reason whenever possible.

A PASS may include non-load-bearing editorial notes. Those notes do not alter the certified target.

If only a cleanly separable substatement survives a failed larger target, the auditor may explicitly certify that substatement; certification must never be inferred from partial success.

## Queueing and concurrency

GN3 has no mandatory rule that audits themselves must be performed chronologically. Audit the work whose certification most matters to the live proof and research picture. The visible statuses and `[FRONTIER]` marker make outstanding earlier audit debt discoverable without forcing chronological work.

Multiple auditors may independently inspect the same target. If duplicate effort becomes wasteful, coordinate informally in the audit thread; do not create permanent claim bureaucracy merely to avoid overlap.

## Propagation after audit

A PASS does not by itself rewrite canonical project state. When certification changes the canonical proof coordinate, reusable toolkit, or other durable mathematics, update the appropriate GitHub text and `STATUS.md` and record the high-signal delta in `#gn3-changelog`.

A REVISION REQUIRED or FAIL that changes the live search should be communicated to the Director or Vice Director so the active research tree can be recompressed. Audit transcripts themselves do not belong in `RESEARCH_TREE.md`.

## Headline discipline across Slack

The root/thread rule is intentionally scoped, not universal:

- In `#gn3-research`, `[G##]` mathematical discovery roots are concise headline statements carrying visible audit status; proofs, derivations, qualifications, computations, and discussion go in replies.
- In `#gn3-audit`, each root is a concise audit-target headline; the audit work and disposition go in replies.
- In `#gn3-changelog`, roots are concise high-signal project deltas.
- Ordinary replies and conversational discussion do not need to be headline statements.

The purpose is scannability and retrieval, not forcing every Slack utterance into theorem form.
