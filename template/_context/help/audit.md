
AUDIT

Auditing is a Worker mode, not a permanent identity, but self-audit is prohibited for substantive authors.

Assigned target_ids are one shared audit batch whenever more than one target remains.

Normal batch workflow:
1. Call __template__.open_audit_batch_v2(worker_id,'{}','math',12000) once.
2. Consume its issued read_page cursor chain completely. This is one exact-version stream containing all pending target bodies and the union of their directly relevant premise/fence/interface/reference mathematics.
3. Audit the targets together. Compare statements, shared premises, duplicated arguments, inconsistencies, possible synthesis, and common failure modes before committing individual verdicts.
4. Call __template__.submit_audit_batch_v2(worker_id, decisions, consumer_impacts) once. decisions is a JSON array with exactly one object per still-pending target:
   {"id":"...","outcome":"pass","note":"...","verification_method":"independent_check"}
   {"id":"...","outcome":"fail","reason":"..."}
   {"id":"...","outcome":"defer","note":"..."}
5. Submission is atomic. Individual targets retain independent certificates/failures and exact target-specific audit snapshots inside the shared read basis.
6. If mathematical repair changes watched mathematics, reopen and reread the shared batch before simultaneous verdict submission.
7. After the batch is terminal, call __template__.next(...) and continue in the same response while substantial runway remains.

__template__.open_audit_bundle_v2(...) and __template__.begin_audit(...) remain for singleton/ad-hoc exceptional auditing. Do not turn a normal assigned batch into a sequence of separately opened singleton bundles.

Audit failure and localized repair generate bounded audit notices automatically. Failed objects require real mathematical repair before another audit.


STALE CERTIFICATE RECONFIRMATION

A certified object whose support_status is stale only because a logical premise math_version changed remains usable certified mathematics. Stale is a yellow trust flag, not quarantine. Such objects are automatically audit-requested and may be scheduled as lightweight premise-impact checks without changing audit_status to pending. PASS refreshes only the certificate premise manifest/signature; it does not claim a fresh proof reconstruction. DEFER leaves the stale object usable and queued.

AUDIT CONSUMER IMPACT

The v2 audit opener includes directly affected stale consumers when their only certificate mismatch is among the current audit targets and the auditor is independent of that consumer. The package reads those consumer bodies on the same exact-version basis. The auditor must submit one PASS or DEFER line for each offered consumer. PASS means the unchanged consumer proof still works with the updated premise version(s); it cheaply refreshes that premise snapshot. This is bounded to direct consumers and does not recursively expand the package.

COMPACT AUDIT SUBMISSION RECEIPTS

Batch audit submission responses are intentionally compact. __template__.submit_audit_batch_v2(...) must not echo certified theorem statements, proof bodies, full certificates, audit snapshots, or other large nested objects back through the connector. For each target it returns only a small receipt containing the target id, outcome, audited math version, dominance, and any small state/revision/support fields needed to confirm the mutation. Consumer-impact PASS receipts are compact for the same reason. The full mathematical object and certificate remain stored in the repository and may be read separately only when actually needed. This keeps large shared audit batches safe under connector payload limits without weakening atomicity or audit semantics.
