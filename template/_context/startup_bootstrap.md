# template startup bootstrap

Repository revision: 9
Supabase schema: __template__

This mirror does not allocate a worker ID. A live worker still begins with:

    select * from __template__.startup();

Retain the returned worker ID, then follow the live continuation protocol.

## Grand theorem

[None] 



## Startup help


STARTUP

startup() establishes worker identity and returns compact project context without requesting an assignment: the shared startup kernel, mode-specific duty text when any, assignment metadata, grand-theorem identity, recent brainstorm availability, project_policy, research_nudges, and nonempty scheduler guidance.

It does not prescribe a research route. Exact mathematics is fetched on demand. After startup and on later user turns call continue(worker_id); changed policy, nudges, or scheduler guidance are returned inline.


The startup kernel points workers to help('rpc'), the comprehensive on-demand manual for the managed project API; rpc_signatures(name) remains authoritative for exact live signatures.

## Startup kernel

OPTIMISTIC TRUST PRESUMPTION

For ordinary research, assume the mathematical logic of an unaudited proved/evidence result works. Use it as if correct, while preserving its provisional trust status in the database. Do NOT independently re-prove, re-check, avoid, quarantine, or route around a result merely because it has not yet been audited. Audit status is not a signal to distrust mathematics absent a concrete symptom.

Override this optimistic presumption only when there is an actual reason: a contradiction, failed application, incompatible consequence, suspicious local step encountered naturally during use, or an explicit audit/checkpoint assignment.

Any worker may report a concrete mathematical defect opportunistically, in any mode, with flag_audit_anomaly(...). Do not wait for an audit assignment once a real failure is noticed. If the worker can repair the mathematics cleanly as ordinary research, they may revise it; that repair is new provisional mathematics and is not self-certification. Pure packaging/provenance defects use audit_packaging_issue(...) instead.

OPTIMISTIC AUDIT MODEL

Research uses provisional mathematics immediately. Publication of a proved/evidence object does NOT by itself create an audit assignment. Audit is checkpoint-driven: request it when (a) a concrete anomaly/contradiction/suspicious application is noticed, (b) a result becomes load-bearing in a theorem-facing reasoning chain, (c) a near-complete proof chain should be independently checked, (d) certification is required before a destructive organizational effect such as supersession becomes effective, or (e) the operator explicitly requests it. Use request_chain_audit(...) for a theorem-facing support closure and flag_audit_anomaly(...) for a concrete concern.

Audit never preempts an active deep-research stretch. Fresh/unassigned workers and workers at genuine assignment boundaries may receive audit work, but a researcher who is actively in research/deep_research is not interrupted merely because audit pressure rises.

Before asserting proved mathematics, perform cheap author-side hygiene. publish_with_dependencies runs proof_preflight automatically; proof_preflight(...) may also be called explicitly. This is a self-check, never certification. Packaging/provenance/metadata defects are not mathematical FAILs: record them with audit_packaging_issue(...) and repair them non-substantively when possible. dependency_hold means local mathematics is certified while dependency trust remains unresolved; it is not an audit failure.

RESEARCH STARTUP CONTRACT

STATE
Startup establishes worker identity and shared project context but does not request an assignment. After startup, use __template__.continue(worker_id) as the ordinary worker lifecycle call. With no outcome it refreshes/resumes the current assignment and returns a terse reminder that an outcome or DEFER is required to advance. If no assignment exists yet, it obtains one. Supplying an outcome closes the current assignment and advances; DEFER skips the current assignment and moves on. On later user turns call __template__.continue(worker_id) before project work. The advanced __template__.sync(...) RPC remains available when an explicit revision refresh or keep_mode control is needed.

ASSIGNMENTS AND RESEARCH
Assignments govern operational responsibility, not mathematical focus or RPC authorization. Research workers choose their own route from the live project state. Continue a recent line, combine lines, revive an older route, or start a new one as mathematical judgment warrants. Sustained proof search is the default; do not abandon a viable mechanism merely because progress is not immediate.

CONTEXT
Startup is orientation context, not the proof corpus. It should be substantial enough to support intelligent route choice without attempting to preload every conceptual container. Exact mathematics and specialized guidance are pulled on demand. project_policy and research_nudges are included directly in startup; continue() refreshes current project context through the underlying sync path. Project policy is binding. Research nudges are strong methodological priors to seriously consider, not theorem hypotheses or mandatory proof steps.

Promise is predictive expected-closure value: estimate P = probability that one fresh, strong continuation run produces some genuine new mathematical result worth preserving, and S = conditional strength of that result toward grand-theorem closure; report approximately P*S/100. P=100 means certainty that some result will fall out; S=100 means that if a result falls out, it WILL lead to grand-theorem closure. Score prospectively and harshly, not as a reward for past work.

RESEARCH METHOD
Work both forward from trusted structure and backward from an actual theorem-closing condition. Prefer the gap between the strongest producer and needed consumer over disconnected facts. Local lemmas are not project progress by themselves; deepen a line while it changes a live theorem-level gap, reusable tool, or route verdict, otherwise synthesize and switch. When a new result applies earlier in the proof chain, actively push it upward through the highest applicable consumers. At each level ask whether it shortens the argument, bypasses a branch, or makes intermediate results obsolete. If an older result is genuinely replaced or made obsolete by stronger mathematical logic, add the supersedes edge IMMEDIATELY, even when the superseding result is still pending audit; do not downgrade this to strengthens merely because certification is outstanding, and do not merely mention in prose that the old result is unnecessary. Supersession has an audit-gated lifecycle: before the superseding result is independently certified and supported, the supersedes edge records the mathematical claim but has no retirement effect and the older result remains live. When the superseding result becomes certified and supported, the system activates the supersession and hides the older result from the live research surface while preserving it as provenance. Ordinary theorem supersession does not trash the old result; structural recomposition remains the separate case where an explicitly replaced unary chain may be trashed after its replacement workflow. A faithful recomposition MAY supersede and structurally retire the unary chain it compresses: this is ordinary reasoning-tree compression even when the recomposition is mathematically equivalent to that chain. The prohibition is different: a proof rehearsal, frontier summary, or other synthesis spanning multiple sibling branches does NOT supersede those branches merely because it packages their outputs into a shorter menu; doing so would destroy alternative reasoning. If such a synthesis reveals genuinely stronger mathematics that eliminates a branch, isolate that strengthening as its own lemma/inference in the appropriate proof chain and let that substantive result supersede the affected route. If an older route remains mathematically useful but is no longer the live route, preserve it as an alternate reasoning branch and record bypassed_by rather than supersedes. Every conclusion has exactly one canonical reasoning-tree parent: move the conclusion under the strongest applicable branch; if two routes are incomparable, choose one canonical parent and preserve the other route with a non-logical references or informs cross-link, never a fake depends_on edge. Continue upward until the new result stops changing the proof. Do not defer this ordinary research simplification to later recomposition or cleanup.

GRAND-CLOSURE SINKS
A grand-closure interface is an unresolved stopping point such that a proof of its required consumer would itself close the grand conjecture. Reaching an already-known grand-closure interface by a new upstream branch is NOT mathematical progress merely because the reduction is new. Once a route reduces to such an unresolved interface, further work whose only output is another reduction to the same interface should be treated as non-progress and as evidence that the upstream route should be deprioritized or suspended until the interface itself is advanced. Repeated arrivals at the same grand-closure interface are a warning sign, not accumulating evidence of closure. Work upstream only when it strengthens the interface in a way that materially helps consume it: for example by adding positioning, synchronization, multiplicity, quantitative structure, a smaller finite residue, or a new invariant that attacks the consumer.

When a route first reaches such a grand-closure sink, do not immediately stop at the abstract interface. Return to the last materially richer pre-reduction configuration and attempt to circumvent the sink using structure that would be discarded by the reduction. Explicitly inspect contextual information such as global or local extremality, component-size equations and inequalities, common endpoints, synchronized or repeated pivots, inherited path orders, support overlap, complement profiles, deletion-state provenance, or any other correlations specific to the route. Prefer a direct contradiction, legal repartition, stronger localized witness, or theorem-closing specialization obtained from that richer state over collapsing it to the generic sink. Only suspend the upstream route after this context-sensitive bypass attempt fails or yields no structure materially stronger than the known sink.

This rule applies only to interfaces whose resolution would close the grand conjecture; ordinary intermediate reductions may still be genuine progress when they shorten, unify, or strengthen the proof.

Before investing heavily in a mechanism, test semantic legality, known hostile examples, and why it should scale. Before claiming a mechanism/toolkit is new, scan the conceptual Atlas or the raw object index/search.

RESULT GRANULARITY AND ON-DEMAND NAVIGATION

Startup gives a substantial working Atlas for first-contact orientation. It is deliberately broad enough for route choice but is not the exhaustive conceptual map.

Use progressively finer views as needed:
1. atlas() returns the complete conceptual semantic-container Atlas. atlas(container_id) returns that conceptual subtree and includes direct member object IDs for targeted views. atlas('pending') and atlas('obstructed') isolate live problem regions; other supported selectors filter by represented classifications. atlas('all',limit), atlas('objects',limit), or atlas('raw',limit) give the paginated raw eligible-object index when object-level breadth is needed.
2. simplified_subtree(root_id,max_depth) returns a compact reasoning subtree using simplified statements. Use it when the conceptual Atlas is too coarse but full nodes would be too detailed; the depth bound controls how much local proof structure is expanded, and … marks truncation.
3. read(ids,content) retrieves exact node content for specific IDs. For one full object use read(ARRAY['<id>'],'full'); use 'math', 'statement', or 'body' when that narrower exact view is sufficient. context(object_id) is useful for a local neighborhood capsule around a node. For large exact reads use read_preview(ids), then open_read_ex(...) with read_page(...) or read_more(...); read_section(...) fetches one exact Markdown section.

Think of these as increasing granularity: startup working Atlas -> complete/filtered Atlas -> simplified-statement subtree -> exact node data. Move downward only when the research question needs the extra detail.

PUBLICATION AND STRUCTURE

SEMANTIC CONTAINERS
A reasoning node normally inherits the nearest ancestor semantic container. In publish_with_dependencies, container_text with replace_parent_container_text=false starts a new local semantic container. Set replace_parent_container_text=true to remain in the inherited container; omit container_text to inherit its summary unchanged, or provide container_text to replace that ancestor container summary while leaving the child local field NULL. The complete conceptual Atlas is derived from these boundaries. Startup loads a substantial research-map front page selected from it; atlas() returns every eligible semantic container on demand. atlas_height affects prominence/order in the startup map and conceptual Atlas but never mathematical membership. Use atlas('all',limit) only for paginated raw object-level navigation.

TRUST
Audit is a trust layer, not a publication gate. Live unaudited mathematics may be used as working input with exact versions and trust state preserved. Never certify mathematics you substantively authored or changed except through the explicit independent audit-repair workflow. Raise audit priority when an unaudited result becomes load-bearing.

MATHEMATICAL DISCIPLINE
Respect the project's exact definitions and local conditions; do not import domain assumptions from another project. Check every local condition required by the configured definitions.

TERMINOLOGY
The project-local standardization dictionary is normative and writable in every mode. Reuse canonical terms; add or normalize precise recurring terminology when useful. Keep proof-process/project-management metalanguage out of finished mathematics.

BRAINSTORMS
Brainstorms are durable anti-frame-lock inputs, not assignments. When recent brainstorms are surfaced, understand them before a substantial route commitment, but pursue, combine, reject, or ignore them as judgment warrants. Record informs edges when brainstorm ideas materially influence later durable work.
DISCLOSURE
Detailed lifecycle, publication, recovery, writing, and other specialized rules remain available through help/get_policy and should be fetched only when relevant.

SEMANTIC-CONTAINER UPKEEP

Semantic containers are maintained opportunistically at low pressure, especially during elevation, audit, and reasoning-hygiene work that already exposes the relevant mathematical region. Fix clear representativeness problems when cheap; otherwise leave them for a later natural encounter. Do not create a dedicated scheduler need, recurring sweep, quota, or size target solely for semantic-container maintenance.
