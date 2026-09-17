# GN3 audit protocol

This file specifies the operational structure of independent mathematical audit. The certification principles in `ARCHITECTURE.md` remain authoritative.

## What an audit certifies

An audit certifies an **exact mathematical target**: a stated theorem, lemma, proof section, proposed canonical rewrite, or other explicitly delimited mathematical text. GitHub placement, downstream use, or agreement among researchers does not certify mathematics.

The auditor must be independent of the authorship of the exact text being certified. An author may explain, repair, or defend their work, but may not self-certify it.

## Slack structure

`#gn3-audit` uses the same high-signal root/thread discipline that has worked well for research, but for a different purpose.

Each audit target gets one concise top-level message. The root should state what is being audited and identify the exact target sufficiently to retrieve it. Prefer a GitHub path plus commit or blob coordinate for repository text. For pre-canonical Slack mathematics, link the exact research headline/thread and state the scope being audited.

When an audit target arose from a Director research wave, retain its `[G##]` tag in the audit root when useful for retrieval. The guidance tag is administrative metadata only.

Detailed verification, derivations, counterexamples, objections, proposed repairs, author responses, and discussion belong in replies to the audit root. Do not paste a long proof or audit transcript into the channel root merely to make it visible.

The final audit disposition should be posted in the same thread and should name the exact revision it applies to.

## Audit dispositions

Use three ordinary dispositions:

- **PASS** — the exact target is mathematically certified at the stated scope.
- **REVISION REQUIRED** — the target is not certified as written, but the defect appears repairable or the auditor has not established falsity. State the precise defect and what must be rechecked.
- **FAIL** — the target is false or invalid as stated. Give a concrete counterexample, invalid inference, or other decisive reason whenever possible.

A PASS may include non-load-bearing editorial notes. Those notes do not alter the certified target.

If the text changes after PASS, the old PASS continues to apply only to the old exact target. A revised target requires fresh audit unless an independent auditor explicitly compares the revisions and confirms that the change is purely editorial and leaves the mathematics unchanged. Any substantive change, strengthening, changed hypothesis, changed construction, repaired inference, or materially different proof requires fresh audit.

If only a cleanly separable substatement survives a failed larger target, the auditor may explicitly certify that substatement; certification must never be inferred from partial success.

## Queueing and concurrency

GN3 has no mandatory chronological audit queue, nonce-claim system, or contingent-status chain. Audit the work whose certification most matters to the live proof and research picture.

Multiple auditors may independently inspect the same target. If duplicate effort becomes wasteful, coordinate informally in the audit thread; do not create permanent claim bureaucracy merely to avoid overlap.

## Propagation after audit

A PASS does not by itself rewrite canonical project state. When certification changes the canonical proof coordinate, reusable toolkit, or other durable mathematics, update the appropriate GitHub text and `STATUS.md` and record the high-signal delta in `#gn3-changelog`.

A REVISION REQUIRED or FAIL that changes the live search should be communicated to the Director or Vice Director so the active research tree can be recompressed. Audit transcripts themselves do not belong in `RESEARCH_TREE.md`.

## Headline discipline across Slack

The root/thread rule is intentionally scoped, not universal:

- In `#gn3-research`, `[G##]` discovery roots are concise mathematical headline statements; proofs, derivations, qualifications, computations, and discussion go in replies.
- In `#gn3-audit`, each root is a concise audit-target headline; the audit work and disposition go in replies.
- In `#gn3-changelog`, roots are concise high-signal project deltas.
- Ordinary replies and conversational discussion do not need to be headline statements.

The purpose is scannability and retrieval, not forcing every Slack utterance into theorem form.
