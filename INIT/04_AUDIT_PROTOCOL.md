# 04 — GN3 shared certification interface

This file contains the audit rules that non-Auditor roles need in order to use certification correctly. Detailed Auditor operation, repair practice, dependency checking, computation verification, and audit-thread procedure live in INIT/AUDITOR.md.

## Certification scope

Research may use provisional mathematics optimistically. Certification attaches only to the **exact mathematical text** independently checked.

GN3 does not audit every research result. The Vice Director selects load-bearing targets: mathematics needed by the favored proof route, an important live alternative, a shelf candidate, a canonical rewrite, or a genuinely reusable theorem.

There is no chronological audit frontier and no project-wide audit backlog that must be cleared.

## Independence

The incoming exact mathematics must be checked by an independent Auditor.

The original author may explain or revise their work but may not self-certify it.

One independent Auditor normally owns one coherent audit batch. Certification is itemwise even when several related targets are checked together.

## Dispositions

Use exactly these dispositions:

- **PASS** — the exact target is certified at the stated scope.
- **PASS_ADJUSTED** — localized corrections or qualifications were required, the repaired exact text was checked, and the certifying Auditor did not introduce substantive new mathematics.
- **REVISION REQUIRED** — the target is not certified as written but appears repairable, or a substantial Auditor-authored repair awaits independent second audit.
- **FAIL** — the target is false or invalid as stated.

A downstream argument may use PASS or PASS_ADJUSTED mathematics as certified at the exact audited scope. Do not silently strengthen the certified statement.

## Repair and second audit

Repair is part of audit.

A localized repair may be certified by the same Auditor when it does not introduce a new proof idea or materially change the theorem's mathematical content.

A **substantial Auditor-authored repair** requires a **second independent Auditor**. The repairing Auditor must not certify their own substantive new mathematics. Until the second audit passes, the repaired target remains REVISION REQUIRED.

The distinction is mathematical rather than textual: a short new inference can be substantial, while a long explicit expansion of an already verified argument can be localized.

## Shelf and canonical admission

Nothing mathematical enters SHELVES/CORE/ or SHELVES/UTILITY/ until the **exact composed candidate** has independent PASS or PASS_ADJUSTED certification.

Previously certified ingredients do not automatically certify a rewritten or merged exposition.

A mathematical edit to an admitted shelf or canonical text must be audited as required by its destination. A byte-for-byte move does not create a new mathematical audit obligation.

## Vice-Director responsibilities

The Vice Director:

- decides what is load-bearing enough to audit;
- provides exact targets and enough mathematical context for efficient verification;
- tracks which live dependencies are certified;
- propagates FAIL, REVISION REQUIRED, or materially weakened mathematics through guidance and the research tree;
- decides whether certified mathematics should be composed into a shelf candidate or later promoted.

Audit certification does not itself rewrite project state.

## Researcher responsibilities

Researchers do not need the detailed audit protocol.

They may continue working while audits run and may use provisional mathematics optimistically, provided they do not present provisional work as certified. If an audit changes a load-bearing fact, follow the updated guidance or changelog.

## Auditor responsibilities

Auditors must read INIT/AUDITOR.md. That file is authoritative for detailed checking, repair, dependency handling, computation verification, and #gn3-audit operating procedure.

## Communication

The shared surface contract for #gn3-audit is in INIT/07_COMMUNICATION_STANDARD.md. Exact audit records live in the relevant audit threads; GN3 does not maintain a separate project-wide audit ledger.
