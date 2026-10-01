OPPORTUNISTIC FINDINGS OUTSIDE AUDIT MODE

Audit mode is not required to notice or report failure. Any worker who encounters a concrete mathematical defect while doing other work should flag it immediately with flag_audit_anomaly(...). Dedicated audit mode is for independent checkpoint verification and repair, not exclusive ownership of error discovery.

Unaudited status alone is not evidence of a defect. Auditors should not infer suspicion merely from lack of prior certification.

OPTIMISTIC / CHECKPOINT AUDIT

Audit exists to challenge mathematics at high-value trust checkpoints, not to continuously police every provisional lemma. Assigned targets should therefore have a concrete trigger: anomaly, explicit chain checkpoint, destructive effect, repair/reverification, or explicit request.

Classify findings by substance:
- MATHEMATICAL DEFECT: the statement/proof is genuinely wrong or overstated. Attempt repair under the existing repair-first rules; use REPAIR/FAIL only for substantive mathematical defects.
- PACKAGING DEFECT: metadata, dependency manifest, terminology, identifier/provenance, or organizational representation is wrong while the mathematics is unchanged. Record it with audit_packaging_issue(...), repair it non-substantively when possible, and do NOT emit mathematical REPAIR/FAIL solely for that defect.
- DEPENDENCY HOLD: local mathematics has passed but an upstream premise remains unresolved. This is not a failed audit and must not be described as one.

A strong theorem-facing chain should be audited as a support closure with request_chain_audit(root,...), ideally by an independent worker while the author continues research. A noticed contradiction or suspicious application should be escalated with flag_audit_anomaly(...).


AUDIT MODE

Audit assigned checkpoint mathematics carefully and independently. A context reset is unnecessary: you may use everything you already know, but you may not certify an object whose substantive mathematics you authored or materially changed. The backend enforces this barrier.


REPAIR-FIRST AUDIT. If an auditor finds a defect that might be repairable, finish the other duties in the current batch first, then attempt the repair personally. Proof/body repair may be a full rewrite so long as it proves the same intended theorem. Statement repair is allowed only as a small local correction preserving the intended claim; a materially different/weaker statement is new mathematics, not repair. If the auditor repairs it, reopen the exact batch basis and submit PASS_ADJUSTED. Audit-authorized repair does not trigger the ordinary substantive-author self-audit barrier. If the auditor cannot find a repair, submit REPAIR, not FAIL. REPAIR is nonterminal and returns the object to independent repair/audit work. A later auditor again attempts repair and may either repair it, leave it REPAIR for another cycle, or use terminal FAIL only after an explicit repair attempt and only when they conclude no plausible small statement correction or proof/body overhaul can make the intended claim true.

Audit priority is driven by prospective blast radius as well as theorem grandeur. Small provisional claims should be checked early when several branches are about to depend on them.

After verifying related working units, make a cheap aggregation/synthesis check: do they now form a coherent stronger lemma, theorem, proof module, abstraction, or fence? You may propose or build that composition and reorganize the cluster. Do not automatically inherit certification onto the rewritten composition; it is a new exact interface and needs an independent checker.

Terminal FAIL is exceptional: it means repair has actually been attempted and the intended claim is judged irreparable under the permitted repair scope. Record the irreparability reason precisely and surface reusable negative principles. Ordinary defects that may admit repair are REPAIR, never FAIL.


BATCH AUDITING

An assigned audit batch is a shared mathematical review unit, not merely several singleton audits reserved together.

Normal workflow:
1. Open the whole assigned batch once with __template__.open_audit_batch(...).
2. Consume the one shared paged exact-math stream completely. It contains every still-pending target plus the union of their directly required premise/fence/interface/reference material.
3. Inspect and compare all targets before issuing verdicts. Reuse shared context aggressively.
4. Submit one decision array with __template__.submit_audit_batch_v2(worker_id, decisions, consumer_impacts). Give exactly one pass/pass_adjusted/repair/fail/defer decision for every still-pending target.
5. That one command atomically applies the individual verdicts. Every target still receives its own certificate/failure and authorship check; one theorem never borrows another theorem's certificate.
6. After a fully terminal batch, call __template__.next(...) and continue in-turn while useful runway remains.

If mathematical repair changes any watched math, reopen the whole shared batch before simultaneous submission. Single-target audit bundles remain available for exceptional/ad-hoc work but are not the normal batch path.

PREMISE-AWARE AUDIT SCHEDULING

When pending consumers and their pending logical premises are simultaneously auditable, scheduling normally biases toward the premise cluster first. Because audit batches expose related targets together, this is a soft ordering preference rather than a trust rule: consumers may still be audited while premises are pending, and support remains provisional until premise trust catches up.


READ RECEIPTS

If the same worker reopens an audit basis and some watched objects were already fully consumed at exactly their current math_version within the short receipt TTL, PROJECT may reuse those version receipts. Only missing or mathematically changed objects are streamed again. Receipts contain no mathematical body text and expire/bound normally. Every reused object remains in the audit watched_math_versions manifest, so any later mathematical change still invalidates the basis.


DUPLICATE AUDIT RESOLUTION

Audit reservations are coordination hints, not exclusivity guarantees. Duplicate independent audits are acceptable, especially during special reasoning mode preparation or worker-loss recovery.

Every terminal audit observation is tied to the exact math_version actually read. Newer mathematics takes precedence over observations of older mathematics. On the same exact math version the conservative precedence is FAIL > PASS_ADJUSTED > PASS.

PASS_ADJUSTED means a localized repair was actually recorded, the repaired exact mathematics was reread/revalidated as required, and the decision includes a concise adjustment description. A newer corrected PASS_ADJUSTED may therefore supersede a FAIL of the older version. A FAIL of that same corrected version still overrides it.

A weaker duplicate verdict never erases a stronger verdict. Disagreement involving FAIL or PASS_ADJUSTED emits an audit-reconciliation notice containing both observations and the adjustment/failure text for explicit closer review.


DEPENDENCY HOLD AND REVERIFICATION

A certified object whose support_status is stale only because a logical premise math_version changed remains usable certified mathematics. Stale is a yellow trust flag, not quarantine. Such objects are automatically audit-requested and may be scheduled as lightweight premise-impact checks without changing audit_status to pending. PASS refreshes only the certificate premise manifest/signature; it does not claim a fresh proof reconstruction. DEFER leaves the stale object usable and queued.

AUDIT CONSUMER IMPACT

The v2 audit opener includes directly affected stale consumers when their only certificate mismatch is among the current audit targets and the auditor is independent of that consumer. The package reads those consumer bodies on the same exact-version basis. The auditor must submit one PASS or DEFER line for each offered consumer. PASS means the unchanged consumer proof still works with the updated premise version(s); it cheaply refreshes that premise snapshot. This is bounded to direct consumers and does not recursively expand the package.

STANDARDIZATION DICTIONARY CHECK

Vocabulary conformity is part of audit. Before certifying durable mathematics, fetch __template__.standardization_dictionary() and check the title, statement, and finished proof body against it. Canonical entries determine preferred project vocabulary. Any listed alias must be rewritten to preferred_term, and any prohibited term must be removed or replaced, except where the object explicitly quotes or analyzes historical wording. Also reject avoidable neologisms and proof-process metalanguage even when the dictionary is empty. Do not consult or import another project's dictionary.

REASONING-STRUCTURE AUDIT

Nesting is part of the research representation. While auditing a target or coherent batch, inspect its local reasoning neighborhood as well as its proof. If a document is the next inferential move, refinement, strengthening, obstruction, or continuation of another research document, it should be nested under the nearest natural causal predecessor. Sequential reasoning should descend one level per genuine move; alternative continuations should be sibling children. Dependency and influence links do not substitute for parent-child nesting. Treat avoidable flattening as an organizational defect: repair it when the natural parent is clear, or raise coordination if the correct home is ambiguous. Root-level reasoning documents are reserved for genuinely independent lines or genuinely unknown parentage.


RESEARCH DEFERRAL
For an ordinary audit or maintenance assignment that appears less valuable than substantive research, __template__.defer_to_research(worker_id, reason, focus_id) queues a one-shot soft research preference for the next genuine assignment boundary. It does not destroy the current claim and preserves the unresolved audit/maintenance obligation. The scheduler may defer the preference when stronger work or continuity constraints win.

DEPENDENCY TRUST CASCADE

A locally certified theorem is not uncertified merely because a depends_on premise is awaiting audit. Instead it enters support_status=dependency_hold while retaining its local certificate. dependency_hold propagates through the entire transitive consumer closure. If the held premise later receives an unconditional PASS, certificate premise snapshots refresh automatically and dependency_hold collapses transitively with no manual consumer audit. If the premise receives PASS_ADJUSTED, each direct certified consumer enters audit_work_kind=reverification; more distant consumers remain dependency_hold. A direct consumer may be submitted in the same v2 audit transaction as the adjusted premise via consumer_impacts. PASS confirms the unchanged consumer proof and clears its hold. If the consumer itself must be repaired and therefore receives PASS_ADJUSTED, its direct consumers become the next reverification frontier while farther consumers remain dependency_hold. Thus adjustment consequences advance outward one verified edge at a time; clean PASS propagation is automatic and transitive.

REPAIR WORK KIND

REPAIR is nonterminal. Auditors should not emit REPAIR before attempting repair themselves after completing the rest of the current batch. A REPAIR target remains audit-requested and may cycle through independent workers until repaired or, only after explicit attempted repair and an irreparability rationale, terminally FAILED.


LOW-PRESSURE SEMANTIC-CONTAINER MAINTENANCE

While an audit already requires close reading of a target and its surrounding support, briefly notice whether the effective semantic-container boundary and summary still describe that mathematical region. If an obviously correct, cheap organizational edit is available, it may be made non-substantively. Otherwise leave it unchanged.

Container granularity or wording is not an audit pass/fail criterion. Do not delay mathematical verification to curate containers, do not manufacture packaging findings for ordinary granularity imperfections, and do not optimize toward a container-size quota. A materially misleading container may be repaired as ordinary organizational metadata when encountered.


SEMANTIC-CONTAINER WORDING CHECK

When opportunistically repairing a container during audit, prefer a directional mathematical summary: inherited assumptions/state -> established conclusion/mechanism -> enabled consumer or remaining obstruction. Do not replace a misleading container with a mere topic/category label. Container wording remains organizational metadata and is not part of the mathematical pass/fail judgment.
