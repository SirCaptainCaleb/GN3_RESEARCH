# A7C3 Canonical Startup

# Mandatory startup

**This Canvas is the single canonical startup document for A7C3. Every new research conversation must read this Canvas in full before doing research, auditing, integration, repair, strategy, or direction.** This applies to Researchers, Integrators, Auditors / Repairers, Vice Directors, Directors / Astra, and any other worker. Cross-conversation memory, summaries, prior initialization, remembered rules, or selective section reads do not substitute for a complete read at the beginning of a new conversation.

A worker must read the entire Canvas, including Architecture, Current Proof Spine, Durable Obligations, and Current Strategy, before acting. Partial connector responses do not count. If a tool ever returns only part of this Canvas, continue reading until the final section has been retrieved.

After the full Canvas read, synchronize with current Slack through the numbered changelog:

<#C0C0ZAE7M47>

If the worker has a reliable last-seen changelog number `N`, read only changelog roots numbered greater than `N` and open only the threads relevant to the missing state. If that cursor is missing, stale, or uncertain, the full Canvas read is the architecture refresh; then use the Canvas's recorded changelog coordinates and scan subsequent changelog roots. Finally inspect relevant recent workspace roots and threads for mathematical findings, audit tags, corrections, provisional dependencies, and concurrent mathematics. Synchronization is live-state refresh, not a substitute for the full startup read.

# Architecture

## Core principle

**The Slack Canvas is the sole active architecture authority. GitHub is the durable mathematical record, and Slack is the complete live research surface.** GitHub contains audited reusable results, especially interesting mathematics, coherent durable developments, references, and other durable mathematical artifacts. Slack carries everything active workers must notice to remain current: mathematical findings, provisional results awaiting audit, audit outcomes, corrections, quarantines, strategic changes, architecture changes, and concurrent mathematics that could affect reasoning. `A7C3/BACKUP/ARCHITECTURE.md` is disaster-recovery material only and must not be used as a startup document or competing architecture authority.

GitHub `main` is the self-sufficient durable authority for mathematical content. The old Supabase database is gone and is not a source, fallback, restoration target, or reconciliation target. A citation that points only to the vanished database is not a proof source. If an essential proof is absent from GitHub, reconstruct it from available GitHub or Slack material when feasible, or mark the dependency unresolved.

Git history is the revision and archive mechanism. Do not recreate database-style revision objects, worker-state registries, assignment queues, semantic-tag systems, dependency databases, separate audit ledgers, or other lifecycle machinery unless actual use later proves them necessary.

Ordinary new mathematical claims are born in Slack. A theorem-level claim remains provisional until audited and is promoted to GitHub when audit completes. GitHub should receive the final audited mathematical version rather than a sequence of provisional theorem variants. Existing provisional workspace developments may remain when useful for coherent durable integration, but GitHub must not become a second live feed.

A worker should not need to inspect GitHub commit history merely to discover what happened while working. GitHub is authority for durable mathematical content; Slack is authority for live deltas. Any durable change that could invalidate, redirect, supersede, or materially strengthen active work must also be surfaced in Slack.

Temporary branches are exceptional tools for work that genuinely benefits from isolation or review. Direct work on `main` is normal for authorized durable changes.

## Workspace posting invariant

**Every root in the workspace channel must be a concise, mathematically precise headline statement, and nothing else.** Effective with the R-numbered workspace epoch beginning at `R2001`, every new mathematical workspace root carries one canonical `R`-prefixed identifier immediately after any leading tags. Before posting, read the newest R-numbered workspace root and choose a numeric suffix strictly larger than the current maximum, normally exactly `+1`; the first such root is `R2001`. Older workspace history is not retroactively assigned an R-identifier. Thread replies do not receive separate R-identifiers; the root owns the identifier. Audit edits and tag changes preserve it. If concurrent posting creates a duplicate or non-increasing numeric suffix, renumber the later root immediately to a fresh `R<N>` above the current maximum and repair any pointers or files already created. The Slack root identifier is also the canonical GitHub result identifier if the claim passes audit; there is no second result-number allocator. State the exact finding, obstruction, counterexample, reduction, exact mathematical question, or clearly marked conjecture in the shortest form that remains unambiguous. A root should normally be one compact sentence. Do not use the root for proof sketches, justification, provenance, caveats, consequences, narrative, audit reasoning, repair history, routing, or commentary.

Everything explanatory belongs in the same thread: proof, derivation, construction, computation, examples, caveats, limitations, provisional dependencies, interpretation, routing, proposed actions, persistence pointers, and discussion. Do not put these materials in the root even when short.

If a result needs proof or limitations recorded, post the precise root first, then immediately reply in that same thread with the details.

### Audit-ready result handoff

A theorem-level workspace result is not fully posted until its thread contains enough fresh context for a new auditor to attack the mathematics directly rather than reconstruct the research history. The author should add this audit capsule immediately while the proof context is still fresh.

The capsule is deliberately lightweight, but should normally include the proof or a sufficiently complete proof skeleton; exact trusted dependencies with direct current GitHub paths or Slack roots when available; an exact `Provisional dependencies:` line for every unaudited premise actually used; inherited hypotheses or provenance not obvious from the root; important scope limits and exceptional branches; and, for computational claims, what was checked together with enough reconstruction information to verify the check. Historical identifiers are useful search keys but should accompany, not replace, current entry points.

The governing test is simple: **could a fresh auditor verify this claim without first reconstructing how the researcher got here?** If not, the handoff is incomplete. Authors should spend their cheap hot-context knowledge so auditors do not later pay for cold-context archaeology.

Guidance, architecture changes, trust changes, quarantines, proof-spine or obligation changes, audit-impact announcements, and other project-wide control deltas belong in the numbered changelog, not in the mathematical workspace. A changelog root is a terse index headline; all explanation belongs in its thread.

Do not infer posting format from nonconforming historical Slack roots. This Canvas is authoritative.

## Headline tags

Audit coordination/status, when present, comes first; the canonical workspace R-identifier follows all leading tags. The examples below use `R2001`. **A newly posted unaudited result has no claim/audit tag at all.** Completed verdicts use `[PASS]`, `[FAIL]`, or `[PASS_ADJUSTED]` when they lie within the certified audit prefix. Bare `[CLAIMED]` means an audit is actively in progress. A completed audit lying beyond an earlier unresolved root uses `[PASS PENDING]`, `[FAIL PENDING]`, or `[PASS_ADJUSTED PENDING]`. A claim whose own argument passes audit but still depends on one or more explicitly named unaudited premises uses `[PASS CONTINGENT]` or `[PASS_ADJUSTED CONTINGENT]` until those contingencies are resolved. `CONTINGENT` is treated as pending for frontier purposes and is a hard barrier to promotion of later pending verdicts.

`[PASS] R2001 precise mathematical statement`

`[FAIL] R2001 precise mathematical statement`

`[PASS_ADJUSTED] R2001 precise surviving mathematical statement`

Routine concurrency examples:

`[CLAIMED] R2002 precise mathematical statement`

`[PASS PENDING] R2003 precise mathematical statement`

`[FAIL PENDING] R2004 precise mathematical statement`

`[PASS_ADJUSTED PENDING] R2005 precise surviving mathematical statement`

Bare `[CLAIMED]` is the audit claim lock, not a verdict. `X PENDING` means verdict `X` is complete and is waiting only on an earlier audit-frontier gap. `X CONTINGENT` means the claim's own proof has passed audit in the stated form, but its trust still depends on explicitly listed unaudited results. **Bare `[PENDING]` is not a valid claim tag and must not be used for newly posted results or active audit claims.**

Audits need not normally proceed in chronological order. Workers may audit whichever unclaimed result is mathematically useful, convenient, load-bearing, or otherwise worth checking. If a completed audit lies beyond an unresolved earlier root, record it with the ordinary verdict plus `PENDING`:

`[PASS PENDING] R2001 precise mathematical statement`

`[FAIL PENDING] R2001 precise mathematical statement`

`[PASS_ADJUSTED PENDING] R2001 precise surviving mathematical statement`

There is no separate `TARGETED` audit status. Out-of-order audits use the same ordinary verdict vocabulary. `PENDING` records only a chronological-prefix gap; `CONTINGENT` records unresolved proof dependencies and also blocks chronological promotion.

The interestingness nomination is also a **leading square-bracket tag**, never a suffix and never parenthesized. Audit/coordination status comes first, then `[INTERESTING]` when present, then the canonical R-identifier, then the mathematical headline. Examples include `[CLAIMED] [INTERESTING] R2001 ...`, `[PASS PENDING] [INTERESTING] R2001 ...`, `[PASS CONTINGENT] [INTERESTING] R2001 ...`, and `[PASS] [INTERESTING] R2001 ...`.

`[INTERESTING] R2001 precise mathematical statement`

`[PASS] [INTERESTING] R2001 precise mathematical statement`

`[PASS_ADJUSTED] [INTERESTING] R2001 precise mathematical statement`

**A fresh unaudited ordinary root has no claim/audit tag.** Its form is simply `R2001 precise mathematical statement` (with the actual next available R-identifier), or `[INTERESTING] R2001 ...` when independently nominated as interesting. It is explicitly **not** `[PENDING]` and **not** `[CLAIMED]` at birth. Only when a worker actually begins auditing it does that auditor edit the root to `[CLAIMED] R2001 ...`.

## Interesting means curated, not merely good

`[INTERESTING]` is intentionally rare. It is a nomination for the paper-level curated shelf, not a marker meaning “useful,” “correct,” “new,” “nice,” “locally clever,” or “worth remembering.” The ordinary active result corpus is the mathematician's notebook. `RESULTS/INTERESTING/` is the elevated shelf for mathematics that deserves unusual long-term attention.

Use `[INTERESTING]` only when the result plausibly belongs among the small set one would deliberately carry into the developing paper or repeatedly foreground for future mathematicians. Typical reasons include substantial progress toward the theorem, collapse of a major branch, a genuinely creative mechanism, a reusable structural principle or normal form, a deep invariant, a repeatedly reused interface across distinct arguments, or a striking counterexample that permanently changes the conceptual picture.

Routine local lemmas, small refinements, zipper steps, bookkeeping facts, ordinary reductions, minor counterexamples, convenient calculations, and results valuable only inside one current chain should normally remain untagged even when correct and useful.

A worker may nominate `[INTERESTING]`, but audit makes a second independent judgment. If the auditor agrees and the result passes, its canonical location is `A7C3/RESULTS/INTERESTING/`. If the audit passes but the interestingness bar is not met, remove the tag and persist the result in the ordinary appropriate result location. Do not duplicate a canonical interesting result in both `INTERESTING/` and `USABLE/ACTIVE/`.

## No status roots

The mathematical workspace is not a progress feed. Never create a root whose substance is that a worker synchronized, initialized, resumed, read files, chose a task, is starting or continuing an investigation, plans to inspect something, made a commit, persisted a document, completed bookkeeping, or has no result yet.

A useful test is: if worker identity and activity narration are removed, does the root still state a mathematical fact, obstruction, counterexample, reduction, exact question, conjecture, or trust-relevant correction that could change another mathematician's reasoning? If not, it does not belong as a workspace root.

Plans and progress belong in the worker's own conversation. Persistence pointers, proof details, and tactical follow-up belong in the thread of an actual mathematical finding.

If an operational status root contains no unique mathematics, remove it. If useful mathematical content exists in its replies, preserve that mathematics under an appropriate mathematical root or durable development before deletion.

**Thread deletion is always child-first.** When deleting a Slack thread, delete every reply or child message first, verify the replies are gone, and delete the root last. Never delete a root while replies remain, because Slack may leave a visible `This message was deleted` tombstone at root level. This ordering applies to every thread cleanup, not only status-root cleanup.

## Slack is the live-update surface

### Numbered changelog

<#C0C0ZAE7M47>

is the single transient delta stream for guidance, architecture, trust changes, quarantines, proof-spine or obligation changes, audit-impact announcements, and other live project-wide state changes. The separate guidance channel is superseded and is not part of active synchronization.

The numbered epoch begins at changelog `1`; older unnumbered roots are pre-epoch history and are not retroactively numbered. Every new changelog root begins `[N | Gx, Ay]`, where `N` is exactly one greater than the previous numbered root, `Gx` is the changelog number of the most recent guidance root, and `Ay` is the changelog number of the most recent architecture root. `x` and `y` are changelog sequence numbers, not separate counters.

A changelog root is only an index card: it must contain enough information to identify the change and decide whether its thread matters, but not the explanation. Put rationale, details, mathematical implications, migration notes, caveats, links, and discussion in its thread. Do not bury a distinct later state change only in an old thread; create the next numbered root when changelog state changes.

**Current Canvas snapshot coordinates:** changelog `15`; guidance `G13`; architecture `A15`. Changelog 15 makes chronology a certification invariant rather than the default audit work order: out-of-order dependency-settled audits use `X PENDING`; passing audits with named unaudited dependencies use `X CONTINGENT`; contingent results remain provisionally usable but block frontier promotion until their contingencies resolve; when a gap closes, `PENDING` is stripped from the contiguous following run only until the first unaudited, claimed, or contingent root. Changelog 14 established that new mathematical results have no claim tag and active audit ownership uses `[CLAIMED]`. Changelog 13 is Astra's live guidance and supersedes G12's ancestry-free endpoint-cap classification program: retain the marked physical exchange frontier, establish the exact global export/consumer for physical low-transition covers, and use endpoint caps to construct legal exchanges rather than as a standalone invariant. Changelog 10 defines canonical `R`-prefixed workspace/result identifiers.

The Canvas is the current architecture snapshot; the changelog is the transient delta stream. The changelog `G` pointer is the sole live guidance authority. Guidance-like text in the Canvas's Current Strategy section is durable strategic context and may lag the live `G` pointer.

If a change could cause another active worker to change direction, distrust a premise, use a new theorem, re-read a durable source, or update the strategic model, it must be represented by a numbered changelog root.

A new mathematical result goes to the workspace before audit. In the R-numbered workspace epoch it receives its canonical `R<N>` identifier at posting time; an audit verdict is later attached to that same root without changing the identifier. Canonical GitHub publication is linked from the same thread and uses exactly that same identifier as the filename stem. Director / Vice Director guidance is a guidance changelog root and advances the `G` pointer. A material architecture change is an architecture changelog root and advances the `A` pointer. Trust, quarantine, proof-spine, obligation, or audit-impact changes receive numbered changelog roots when they affect live work but do not move `G` or `A` unless they also constitute guidance or architecture changes.

Canonical publication itself is not a new mathematical finding. Put the canonical path in the thread, not in a duplicate root, unless publication revealed an additional mathematical or control fact.

If a thread produces a genuinely new mathematical finding, create a new workspace root for that finding. If it produces a distinct project-wide state change, create the next numbered changelog root rather than burying the change only in the old thread.

## Synchronize before resuming

Every re-entry into an existing conversation is a synchronization boundary. When the user says `Continue`, `resume`, `keep going`, or equivalent, synchronize with live Slack before continuing from the resulting frontier.

For an already initialized conversation, use incremental synchronization when a reliable last-seen changelog number is available: scan roots `N+1` onward, use each `[N | Gx, Ay]` header to see whether guidance or architecture moved, and open only the threads relevant to the worker's missing state. Then inspect relevant recent workspace roots and threads. For audit bookkeeping, scan backward to a completed non-pending, non-contingent verdict `[PASS]`, `[PASS_ADJUSTED]`, or `[FAIL]` when a chronological frontier is needed. Bare `[CLAIMED]` is an active audit claim and must not be duplicated. `X PENDING` is already audited; `X CONTINGENT` has passed its own audit but remains dependency-blocked. Auditors are not generally required to take the oldest unresolved root next: any unclaimed result may be audited. Whenever completion of an audit makes it immediately follow a certified non-pending/non-contingent verdict, strip `PENDING` from every consecutive completed `X PENDING` root that follows, stopping at the first unaudited root, active `[CLAIMED]`, or any `X CONTINGENT`. Never promote across a contingent result. No re-audit is performed during this cascade. If no reliable changelog cursor exists, reread this Canvas in full, take its recorded snapshot coordinates, and scan only numbered changelog roots after that snapshot.

Do not treat movement of GitHub `main` by itself as evidence that the live research frontier changed. Do not scan commits to infer concurrent discoveries. Slack should announce relevant live changes. Refetch GitHub when Slack identifies a relevant durable source, when exact durable proof content matters, or immediately before modifying the same durable file.

Synchronization is silent housekeeping, not a research finding. Do not post a root saying that you synchronized or resumed.

Do not rely on remembered guidance labels, remembered result status, or a previously valid dependency merely because it remains in conversation context. The current Canvas architecture snapshot, the current changelog `G` pointer, newer changelog deltas, and the audit status attached to the actual mathematical finding outrank stale local plans.

## Durable mathematics

The durable repository structure is:

```text
A7C3/
├── BACKUP/
│   └── ARCHITECTURE.md
├── PROOF_SPINE.md
├── OBLIGATIONS.md
├── STRATEGY/
├── RESULTS/
│   ├── INTERESTING/
│   ├── USABLE/
│   │   ├── ACTIVE/
│   │   └── LEGACY/
│   └── UNUSABLE/
│       ├── QUARANTINED/
│       └── INVALID/
├── WORKSPACE/
└── REFERENCES/
```

`BACKUP/ARCHITECTURE.md` is non-authoritative disaster-recovery material. Active workers initialize from this Canvas, not from the backup file.

Slack is the normal home of live provisional research. `WORKSPACE/` is the durable notebook layer for coherent developments, constructions, exact local mechanisms, useful failed branches, limitations, and enough mathematical texture to re-enter an argument later.

New or substantially revised durable developments should normally be organized around the mathematical question or coherent argument and use descriptive filenames. Historical D17 section numbers, SV identifiers, and similar labels remain valuable provenance and search keys but need not govern navigation.

An active durable development should open with compact orientation: exact setting, strongest current conclusion, trust status of important parts, actual missing step, and a few load-bearing proofs. Link reusable canonical results rather than duplicating proofs.

`RESULTS/` is narrower. A result is a standalone audited mathematical interface worth reusing outside the immediate scratch chain. Correctness alone does not make a result interesting.

Ordinary locations are:

* `RESULTS/INTERESTING/`: audited, safe, and specially curated for unusual mathematical importance or creativity.
* `RESULTS/USABLE/ACTIVE/`: audited, safe, and currently useful, but not specially curated.
* `RESULTS/USABLE/LEGACY/`: audited and safe but superseded, off-route, or lower-priority.
* `RESULTS/UNUSABLE/QUARANTINED/`: frozen, unusable mathematics retained for provenance and possible future reconsideration; quarantine is not an active repair queue.
* `RESULTS/UNUSABLE/INVALID/`: known-invalid mathematics retained because the failure itself is durably useful.

Old is not the same as unsafe. Ordinary is not the same as unimportant.

**Result identifiers are globally unique across every `A7C3/RESULTS/` subtree.** For R-numbered workspace roots beginning at `R2001`, the Slack root identifier is already the result identifier: a passing root `RN` is persisted canonically as `RN.md` in the appropriate `RESULTS/` subtree. Do not allocate, prepend, strip, or translate a second result number. Existing pre-`R2001` results keep their existing identifiers, and moving or reclassifying any result keeps its identifier. If an R-identifier collision is discovered before publication, renumber the later root to a fresh `R<N>` above the current maximum. If a collision is discovered after publication, renumber the newer artifact/root and repair its pointers immediately.

## Search and theorem use

Default theorem discovery should first search `RESULTS/INTERESTING/`, then `RESULTS/USABLE/ACTIVE/`. Broaden to all usable results when necessary. Search `WORKSPACE/` deliberately when the proof needs local development, historical machinery, constructions, failed routes, or details not promoted to reusable results. Search quarantined material only when tracing historical dependence or when an explicit future decision has reopened a quarantined claim. Do not treat quarantine as a default research or repair queue.

Theorem application is proof-aware. Before using a result as an inference, understand the proof mechanism well enough to preserve witnesses, physical vertices, path orders, selected states, cuts, signs, ancestry, equality conditions, exceptional branches, and other structure that may matter downstream. The theorem statement is a minimum contract, not permission to discard everything its proof established.

An unaudited Slack result is provisional mathematics, not forbidden mathematics. A worker may use it provisionally but must record an exact `Provisional dependencies:` line in the dependent root thread or live development. Any descendant remains provisional until those dependencies survive audit in the form actually used.

Unaudited Slack results are legitimate provisional mathematics and may be used when useful, provided dependence is explicit. A result whose own proof passes audit while relying on one or more unaudited premises is marked `[PASS CONTINGENT]` or `[PASS_ADJUSTED CONTINGENT]`, and its thread must state the exact unresolved dependencies and the form in which each is used. A contingent result may itself be used provisionally, but every descendant must preserve the dependency chain clearly. When all contingencies resolve favorably in the required forms, remove `CONTINGENT` and re-evaluate the chronological frontier; if a dependency fails or narrows materially, revisit every contingent descendant that used the superseded form.

## Audit protocol

Audit stays attached to the finding. **Before beginning an audit, claim the root by adding `[CLAIMED]`; do not duplicate a root already carrying `[CLAIMED]`.** Auditors may choose unclaimed roots out of chronological order; chronology is bookkeeping, not the governing work queue. If the audited claim is dependency-settled and lies inside the certified prefix, use `[PASS]`, `[FAIL]`, or `[PASS_ADJUSTED]`. If it is dependency-settled but an earlier root remains unresolved, use `[PASS PENDING]`, `[FAIL PENDING]`, or `[PASS_ADJUSTED PENDING]`. If the claim itself passes but relies on named unaudited premises, use `[PASS CONTINGENT]` or `[PASS_ADJUSTED CONTINGENT]` regardless of chronological position. For R-numbered workspace roots, the R-identifier remains fixed through every audit edit.

Audit reasoning belongs in the same thread. For `[PASS_ADJUSTED]`, `[PASS_ADJUSTED PENDING]`, or `[PASS_ADJUSTED CONTINGENT]`, state the exact surviving adjustment. Every `CONTINGENT` verdict must also state its exact unresolved dependencies and the hypotheses or outputs imported from each. If the original wording would mislead, edit the root statement itself to the corrected surviving theorem while retaining the appropriate audit status.

**A fresh unaudited root has no claim/audit tag. Do not add `[PROVISIONAL]`, `[PENDING]`, or `[CLAIMED]` when posting a new result.** Bare `[CLAIMED]` is reserved for an audit actively in progress. Bare `[PENDING]` is not used as a standalone status. If a worker abandons an in-progress audit before reaching a verdict, that worker should remove `[CLAIMED]`, returning the root to its no-claim-tag state. An Integrator or Auditor may clear an evidently stale `[CLAIMED]` after checking the thread and confirming that no completed audit result was left behind.

**Chronological audit is a certification invariant, not a preferred work order.** Workers may audit later roots freely. A completed non-contingent audit beyond an earlier unresolved root is recorded as `X PENDING`; a passing audit with unresolved proof dependencies is recorded as `X CONTINGENT`. An ordinary verdict without either suffix certifies that the earlier mathematical history is resolved and dependency-settled through that point. Whenever an audit completion lands immediately after such a certified verdict, the worker must strip `PENDING` from the entire immediately following contiguous run of completed `X PENDING` roots, stopping at the first unaudited root, active `[CLAIMED]`, or `X CONTINGENT`. A contingent root is a hard stop: no later pending verdict may be promoted across it. When its dependencies later resolve, first convert the contingent verdict to its appropriate non-contingent form, then apply the same contiguous promotion rule from that point.

### Researcher audit contribution

Before posting a new theorem-level workspace result, an ordinary Researcher should normally contribute one or two audit attempts on useful **unclaimed** mathematical roots. Chronological proximity is a mild convenience, not a general requirement: choose audits that are reasonably bounded, mathematically relevant, or helpful to current trust debt. Before starting each attempt, claim the root with `[CLAIMED]`. Roots already carrying `[CLAIMED]` are being audited by someone else; roots carrying `X PENDING` are already fully audited; roots carrying `X CONTINGENT` have already passed their own audit and instead await dependency resolution. A fresh result awaiting an auditor has no claim tag. This remains a research-community norm rather than a hard posting semaphore.

The bounded-work exception matters. If an attempted old audit quickly opens into substantial repair, missing provenance, or extended archaeology, the Researcher should make a reasonable contained attempt, leave the claim unaudited if necessary, and return to research rather than sacrificing the session. Dedicated Auditors / Repairers already contribute through their role and do not owe an additional pre-post quota. The Director / Vice Director / Astra function is exempt; scarce strategic work should not be gated on routine audit throughput.

There is no separate targeted-audit class. A load-bearing or strategically important later claim may simply be audited out of order like any other unclaimed result. If earlier chronological gaps remain, its dependency-settled verdict is `X PENDING`. If its proof relies on unaudited premises, a passing verdict is `X CONTINGENT`, with the exact dependency requirements recorded in the thread. `CONTINGENT` is mathematically meaningful provisional trust, not a prohibition on use, but it blocks the chronological certification frontier until every contingency is resolved.

### Repair before failure

An Integrator or Auditor/Repairer must make a reasonable mathematical repair attempt before assigning `[FAIL]`, especially when the apparent defect is missing provenance, a vanished historical identifier, an incomplete proof handoff, or a claim that appears close to a correct theorem. A missing historical source is evidence of proof debt, not by itself evidence that the mathematical statement is false.

Before failure, prefer this order: first try to prove the claim directly from its stated hypotheses and trusted nearby machinery; then use the coherent durable development for that argument and nearby descendants that may restate the needed mechanism; reconstruct a missing local lemma when the reconstruction is reasonably contained; and test whether a useful exact theorem survives as `[PASS_ADJUSTED]`. Only after these repair routes fail should the auditor assign `[FAIL]`.

Do not broadcast a load-bearing failure to the team before this repair pass is complete unless immediate containment is necessary to prevent active workers from relying on a known contradiction or counterexample. If uncertainty alone is the issue, keep the root unaudited while repairing it. If a premature verdict was issued, reopen it explicitly, repair first, then replace it with the final verdict.

### Audit retrieval discipline

Auditing should minimize repository archaeology. Start from the claim, its thread, named direct dependencies, and the coherent durable entry point for the active argument. Batch nearby evidence when possible. Do not chase long chains of dead historical labels one identifier at a time when the mathematics can be reconstructed more directly. After repeated retrieval failures show that provenance is genuinely absent, switch from search to mathematical repair rather than multiplying tool calls. Tool-call volume is itself a signal that the retrieval path may be wrong.

Excessive archaeology is also feedback about the original handoff. An auditor should repair or verify the current claim as far as practical, but when basic provenance, dependencies, or scope had to be rediscovered, treat that as evidence that the result thread's audit capsule was underspecified. Future results of the same kind should carry that missing context at posting time.

Completing a dependency-settled passing audit creates an immediate persistence obligation. Every `[PASS]`, `[PASS_ADJUSTED]`, `[PASS PENDING]`, and `[PASS_ADJUSTED PENDING]` goes promptly to the appropriate canonical GitHub result location; trailing `PENDING` delays only chronological frontier promotion, not mathematical trust or persistence. A `[PASS CONTINGENT]` or `[PASS_ADJUSTED CONTINGENT]` has passed its own local audit but is not yet dependency-settled canonical mathematics: keep its exact contingency record attached in Slack and use it provisionally until the named dependencies resolve. Once they do, convert the status and persist canonically as appropriate. Every completed failing audit, including `[FAIL PENDING]`, does not enter usable results, though a valuable invalidation may be preserved under `UNUSABLE/INVALID/` or in a relevant development. Bare `[CLAIMED]` is not a completed audit and creates no persistence obligation yet.

For every passing root, after the canonical GitHub file exists, add a compact thread reply:

`Canonical GitHub result: A7C3/RESULTS/.../R<N>.md`

If an audited result changes the proof spine, obligations, strategy, trust of existing results, or other current durable mathematics, update the relevant durable surfaces and create a numbered changelog root when active work is affected.

## Roles and cognitive mantles

The default worker is a plain Researcher: an autonomous mathematician allowed to prove, explore, compute, challenge, integrate, elevate, search old mathematics, invent representations, and change direction for mathematical reasons.

Explorer, Elevator, Integrator, and Moonshotting are cognitive mantles rather than persistent state. Mantles alter posture, not permission.

A dedicated Auditor / Repairer conversation is useful because adversarial verification benefits from persistent cognitive posture. It claims audit work with `[CLAIMED]`, may audit any useful unclaimed root, records out-of-order completed verdicts as `X PENDING`, records dependency-blocked passing verdicts as `X CONTINGENT`, advances the chronological certification frontier when gaps close, and strips `PENDING` from consecutive completed verdicts until the first unaudited, claimed, or contingent barrier. It traces damage and repairs active failed or near-failed mathematics when appropriate. It must not duplicate a root already claimed with `[CLAIMED]`. Quarantined results are not default repair work and should be revisited only after an explicit decision to reopen them.

The project has one logical Director function. Astra performs scarce high-value strategic passes when available; between them, the Vice Director / Acting Director performs the same function continuously. They are not competing strategic authorities and maintain one current strategic picture.

The Director's recurring intellectual cycle is: assess the real proof state, integrate proof-aware mathematics into the strongest actual frontier, elevate from that frontier to broader phenomena or representations, moonshot toward closure, and guide the team with a small number of valuable focuses.

Integration precedes elevation: first determine what the project can actually use once results, surviving witnesses, exceptions, supersessions, and trust state are combined; then ask whether the resulting machine should be compressed, generalized, bypassed, replaced, or discarded.

Guidance does not assign individual Researchers to tasks. Researchers choose opportunistically within the current target landscape. Overlap is allowed when mathematically useful.

Astra capacity is scarce and should be reserved for high-value strategic judgment, consequential moonshots, elevation, integration of load-bearing mathematics, and choosing team-wide focuses. Routine consolidation, link maintenance, active-development migration, and follow-through belong by default to the Integrator and Vice Director.

### Astra escalation protocol

Whenever the Vice Director / Acting Director assesses the current research situation, explicitly consider whether it warrants escalation to Astra for further strategic guidance. Astra escalation is appropriate when scarce high-level judgment is likely to materially improve direction, especially at a genuine strategic fork, after collapse of a governing proof architecture, after a load-bearing audit failure that changes the frontier, when the current narrow target has been substantially exhausted, or when a consequential moonshot or team-wide refocus is needed. Do not escalate merely because a local proof obligation is difficult when the governing target remains crisp and directly attackable by ordinary research lanes.

If the Vice Director / Acting Director chooses **not** to elevate the current situation to Astra, the response to the user must end with a brief explanation of **why** Astra escalation is not warranted yet.

When the Vice Director / Acting Director **does** escalate to Astra, the response to the user must include a ready-to-use handoff prompt containing the mathematical state Astra actually needs: the governing target, strongest trusted frontier, live provisional dependencies, exact strategic fork or failure mode, relevant fences and countermodels, and the specific judgment requested. The handoff should compress clerical history and routine process so Astra can spend nearly all of its scarce pass on mathematics, integration, elevation, moonshotting, and guidance rather than rediscovering context.

Astra should not perform clerical work. Do not spend Astra capacity on repository maintenance, Slack cleanup, migration, link repair, status bookkeeping, routine persistence, ordinary auditing administration, or other operational chores that can be handled by the Vice Director, Integrator, Auditor, or Researchers.

Astra should also **not perform computation or solver work**. Do not ask Astra to run brute-force searches, enumeration, coding experiments, SAT, MILP, CP-SAT, SMT, linear or integer optimization, or similar computational investigations. If computation could inform the strategic question, another worker should perform it first and hand Astra only the mathematically relevant conclusions, caveats, and exact outputs needed for strategic reasoning.

A deliberately isolated Independent conversation may be used for locality escape. Its information boundary is experimental, not another durable state subsystem. Mathematics that becomes durable enters the same GitHub record and trust model.

## Promotion, integration, and reorganization

Promotion should be boring. A standalone reusable theorem is promoted to `RESULTS/` after audit and dependency settlement. Audited interesting mathematics goes directly to `RESULTS/INTERESTING/`. Connected proof architecture lives in the appropriate durable development. Closure-map changes update the proof spine. Stable unresolved requirements update obligations. Strategic reinterpretations update current strategy. Trust failures move or edit the durable result itself and are surfaced through a numbered changelog root when active work could be affected.

Integration is mathematical research, not clerical filing. A result is not fully integrated merely because it was cited or placed in the right folder. Integration asks how its proof mechanism changes what can now be proved.

Reorganization must remain useful even if it stops after the next edit. Improve the active frontier first. Do not require repository-wide migration before research can continue. For each cleaned-up argument, identify authoritative material and trust state, create one coherent entry point, move only what materially improves usability, update known active links, preserve historical identifiers in searchable text, and leave forwarding stubs when path changes could break references.

Never silently strengthen a theorem, drop a hypothesis, erase an exceptional branch, or turn provisional mathematics into trusted mathematics in the name of readability.

## Concurrency and minimality of the system

Concurrency is coordinated through Slack, not by watching GitHub. During sustained work, periodically scan numbered changelog roots since the worker's last-seen coordinate and inspect nearby workspace activity so guidance changes, architecture changes, failures, corrections, overlapping attacks, and audit claims are noticed. For audit work, the root-level `[CLAIMED]` tag is the concurrency lock: claim before investing audit effort and skip already claimed roots. Completed out-of-order audits use `X PENDING`; passing audits with unresolved named dependencies use `X CONTINGENT`. **Newly posted results have no claim tag.**

A new commit on `main` is not by itself evidence that the live frontier changed. If the frontier changed, Slack should say so.

There is deliberately no hidden second operating system behind GitHub and Slack: no database requirement, persistent worker registry, assignment queue, mantle state, theorem registry beyond files, semantic-tag service, dependency server, separate audit ledger, duplicate interesting-result mirror, durable Slack mirror, explicit revision database, or requirement to poll GitHub commits for live state.

The filesystem is the durable mathematical model. Git is history. Search is durable retrieval. Slack is the live room: the numbered changelog carries project-wide deltas, and the workspace carries active mathematics.

# Current Proof Spine

This is a closure map, not mathematical authority. Exact proofs and their audit status govern use. O4 remains open. Historical O6 is dormant and is not an active obligation.

Logical status labels do not upgrade trust:

* **PROVED REDUCTION**: the cited argument supplies the stated implication or physical output in its stated scope.
* **CONDITIONAL CONSTRUCTION**: the construction is exact only after additional displayed hypotheses are met.
* **UNRESOLVED**: an implication, realization, order constraint, synchronization, or global consumer is still missing.
* **TARGET**: a conjectural parent theorem or desired closure mechanism.

## Global target

**TARGET.** Prove that every finite Strong Level-(1) boundary tournament has path-cover number at most two. In a hypothetical smallest counterexample, the path-cover number is three and every proper induced subsystem has an at-most-two cover.

## Retained source-frame setting

The live campaign works with `G=H-{A,C}=B disjoint-union X`, `X={v,p,q,r}`, where `B` is a tight Hamilton spectator path, `(A,s,C)` is tight for each source spoke `s in {p,q,r}`, and `F` is an actual old source two-cover in which the three source spokes are internal.

D17.391-394 give the quiet transitive spectator frame, endpoint gates, and old-source transition floor. D17.401/408 supply a canonical low-transition three-forest `J` and explicit blocked-repair outputs. In the dual-rigid branch, D17.409 gives the unique augmenter. These are scoped inputs to the current route.

## Audited source-P5 contraction

**PROVED REDUCTION.** Audited `R1031` proves from R3 alone that three parallel source turns `(A,p,C), (A,q,C), (A,r,C)` force a Hamilton P5 on `S={A,C,p,q,r}`.

Therefore, in a hypothetical counterexample, `H[B union {v}]` is nonHamiltonian: any Hamilton path there is vertex-disjoint from the source P5 and the two paths would span `H`.

This strictly contracts the live absorption problem. Adaptive complements `B union {v,s}` remain optional consumers, but the first unavoidable obstruction is already the one-vertex extension `B+v`.

## Audited local obstruction on v

**PROVED REDUCTION.** Since `B` is tight and `H[B union {v}]` is nonHamiltonian, `v` has no successful insertion into the displayed order of `B`. Audited `R1033` therefore gives a local first-flip certificate on `v` and at most three consecutive vertices of `B`: either a directed star-triangle in the R887 comparison orientation, or a reverse-spoke hook with the exact predecessor/right-flank endpoint variants stated in R1033.

This certificate lives in the spectator-order coordinate system: its `B` edges are consecutive edges of the displayed Hamilton path `B`.

## Canonical sharp-cell machinery

**PROVED REDUCTION in the cited scopes.** D17.413 gives a numerically strict internal shortcut except the sharp `tau(F)=3`, `tau(J)=1`, `w(C*)=2` cell, with a singleton-loop alternative. D17.421 gives the exact `K2,2` switch at first numerical loss. D17.424 together with audited R1028 gives the distinct-vertex far-seam rule and transient order-two reverse-dimer branch across consecutive successful pivots.

**CONDITIONAL CONSTRUCTION.** D17.416 gives neutral normalization and forward contact of physical blockers, and D17.423 gives a bounded transition skeleton. These do not themselves certify a run of physically successful pivots or a global improvement.

D17.425-427 convert a genuinely persistent wall at a source gate into literal source-visible P4 geometry; the source-dimer collision is not an independent non-P4 branch. D17.429-430 retain additional terminal-dimer and five-set geometry. Audited R1030 saturates the actual far dimer in the P5-free direct twin-wall residue. Audited R1029 shows that the D17.430 data do not guarantee a Hamilton P5 with the fixed wall vertex as an endpoint.

The former D17.435-D17.439 provisional chain has now yielded a substantial audited interface. `R1037` and `R1038` certify the singleton-`v` / ordered three-spoke source block and a forward X-mated source gate. `R1047` audits the D17.408 spectator-edge sharpening. `R1048-R1052` place the literal OUT-`v` first-loss cell into spectator coordinates and expose the behind-frontier source-gated descent attempt. `R1053-R1056` bound the IN-`v` residues in their exact audited scopes. `R1057` gives the terminal source-mate three-path/two-seam recompletion interface. The newer audited chain `R1058-R1061` and `R2001-R2008` turns the first-open slot into a physical detour/transport interface and eliminates occupied replacement-successor geometry as a new local blocker class. Use these canonical results rather than broader historical D17 wording.

The former coordinate mismatch is resolved in the literal non-loop OUT-`v` first-loss cell. `R1047` makes the deleted `J` edge a genuine consecutive spectator edge, and interesting `R1051` identifies the exact physical rectangle `{b_{j-1}->b_j, v->t} <-> {v->b_j, b_{j-1}->t}` with source spoke `t`. This does **not** say arbitrary old-`F` `B-B` edges are spectator-adjacent; the bridge is canonical and local to the audited first-loss construction.

## Insufficiency fences

**PROVED FENCE.** Audited R1032 gives a globally edge-ordered realization with source turns, a Hamilton source P5, tight spectator `B`, physical `F` with `tau(F)=3`, physical `J` with `tau(J)=1`, and simultaneous nonHamiltonicity of `B union {v}` and `S union {v}`. Thus raw sharp source-frame data do not close O4.

**STRONGER PROVED FENCE.** Audited R1034 realizes, in one globally edge-ordered boundary tournament, the displayed static conclusions of the D17.391 quiet spectator-gate frame together with the same sharp physical `F/J` data and the stubborn `v` obstruction. It contains the noncyclic P4-free R516 signature-11 cell on `X`, both endpoint P5-free five-sets, both universal reverse endpoint stars, physical `F,J` with `tau(F)=3,tau(J)=1` and an internal three-spoke source block, and nonHamiltonian `B union {v}` and `S union {v}`.

R1034 is not a smallest counterexample and deliberately does not realize the dynamic provenance by which the quiet frame, canonical augmenter, and D17.421 first-loss switch are generated. Hence the static spectator-gate snapshot is exhausted as a possible missing hypothesis. A successful next argument must use genuinely dynamic/canonical provenance, a stronger minimal-counterexample consequence, or another global invariant absent from R1034.

## Audited first-open contraction and remaining topology

**PROVED REDUCTION in the physical-prefix branch.** `R1058-R1061` and `R2001-R2010` consume the local first-open availability problem for a later non-loop OUT-`v` loss `j>t+1`. The pre-loss vertex `v` is isolated; an untouched first-open spectator slot gives a literal tight three-forest detour; occupied replacement successors reduce to selected `F\J` states; an off-`C_*` blocker component can be toggled to restore the canonical successor unless that copy is terminal; and `R2010` excludes that terminality. Thus the later loss cannot hide behind a new first-open matching-availability class.

**PROVED REDUCTION.** `R2011-R2019` remove neutral-component/support transport as an independent bottleneck. Audited `R1039` gives total neutral weight zero, so ordinary pre-first-positive zipper prefixes retain the normalized transition ledger. Crucially, `R2019` should be used in its marked form: either the physical prefix persists through `r-1`, or at the first physical failure one has a literal tight three-forest `N=M_q` with `tau(N)<=1`, a specified next exchange `M_{q+1}=N-{f_{q+1}}+{e_{q+1}}`, and every new blocker localized at `e_{q+1}`. Preserve `q`, the next `e/f` pair, old-F/source incidences, literal rail orders, X/B labels, and short-rail coincidences. Forgetting these witnesses discards the extra content beyond the starting forest `J`.

**PROVED REDUCTION for audited closure residues.** `R2017` converts the closure-loop coincidence into four endpoint reverse trimers unless an immediate low-transition two-cover succeeds. `R2020-R2022` localize any nonloop same-rail cycle to an X-only rail and convert that cycle into finite endpoint-cap clauses. `R2021` gives the general cross-rail closure-failure interface: a join cannot cycle and can fail only at one of its two endpoint seams, with R3 producing the corresponding reverse cap. Provisional `R2023` packages all six ordered cross-rail joins of a physical `tau<=1` three-forest; if all six fail, it yields six seam clauses. This packet is a boundary test, not a complete invariant: each cap includes the relevant inward neighbor, arbitrary rail reversal is not a symmetry, and applications from the live branch must retain the marked R2019/D17.421 provenance. A physical two-cover with `tau<=2` is not yet a certified global descent output; its exact export/consumer remains to be established.

**TARGET.** First establish the **global export contract** for the physical low-transition two-covers produced by the marked frontier: prove that such an output yields either a spanning two-cover of `H` or a strict improvement of a precisely specified globally selected object with all admissibility invariants retained. If a source spoke becomes exposed and the route yields the balanced-pair witness of canonical `R408`, identify and prove the additional consumer of that witness. Then build a cap-guided physical exchange theorem on the marked forest: use a failed seam plus retained old-F/source incidence to drive a legal one-cut/two-join recompletion or another exchange with a genuine finite monotone measure/extremal contradiction. Incorporate the exact `j=t+1` cell into this same marked interface or isolate the precise feature preventing it. Do not replace this by an ancestry-free cap classification.

## Secondary adaptive-complement interface

D17.368/398 supply a Hamilton P4 on `{A,C,u,w}` for every pair of source spokes `u,w`. Hence a Hamilton path on any `B union {v,s}` also closes `H` after spending the other two spokes. The v-containing D17.421 rectangle likewise fits inside the corresponding adaptive complement.

This remains useful but after R1031 is secondary rather than governing. Use it when it gives a concrete exchange or cover; do not rebuild a three-complement classification merely because the option exists.

## Logical honesty fences

Keep these distinctions explicit: matching cardinality is not a physical path cover; `tau<=2` is not automatically a globally consumable descent; D17.393's three-crossing floor applies to the retained source-representative regime with its internal-spoke hypotheses, not to arbitrary covers exposing a spoke; canonical `R408` supplies a balanced-pair witness but is not by itself closure. Local P4/P5, gate, wall, star, hook, cap, or zipper geometry is not a spanning absorber. Existence of a path is not existence in a prescribed order or with a prescribed endpoint. Forward contact does not certify all intermediate tight forests. Two formal cross edges are not automatically two legal path joins. Matching copies, physical vertices, literal rail directions, inward endpoint neighbors, old `F` order, `B` order, marked exchange data, source witnesses, and exceptional branches must survive specialization.

## Essential fences

R24/R5 remain frozen and unusable. D17.428/SV118046's incomplete insertion window remains fenced. D17.380's special-order and changed-turn warnings remain relevant. D17.437's COMMON `F intersect J` branch remains live until explicitly excluded. R1032 and R1034 rule out closure from raw sharp or static spectator-gate data alone. Audited `R1041` shows the three source turns do **not** provide prescribed source-P5 endpoint flexibility: every source Hamilton P5 can be forced to have only one particular source-spoke endpoint. The first-loss `K2,2` is still only a matching-level switch until physical seams and component incidence are checked; two cross edges are not automatically two legal path joins.

The former O6 reconstruction of the singleton order floor and short-complement rigidity of R24 is dormant historical context, not an active obligation or repair front. Active proofs must remain independent of R24 and R5 unless a future explicit strategic decision reopens either quarantined claim.

# Durable Obligations

Obligations are stable mathematical closure contracts, not tasks. They have no owner, assignee, worker lane, or mandatory order. Researchers may attack them directly, strengthen them, bypass them through a stronger theorem, or make them irrelevant by changing the proof architecture. Only entries explicitly marked **Open** are active obligations; dormant historical aspirations are preserved for context but are not work queues.

## O4 — Arbitrary-order smallest-counterexample closure beyond order ten

**Status:** Open

**Target:** Eliminate every surviving hypothetical smallest Strong Level-(1) boundary-tournament counterexample in arbitrary order beyond the already excluded order-ten case.

**Scope:** Work in the smallest-counterexample regime. No particular exterior geometry, occupancy normalization, capture mechanism, payment mechanism, or capacity normalization is built into the obligation. Those are possible strategies, not part of the contract.

**Closed when:** A spanning two-cover or contradiction is derived for every surviving hypothetical smallest counterexample, or a stronger accepted order-free parent theorem eliminates all survivors at once.

**Standing fences:** R24 and R5 are not available while quarantined/frozen. A route whose relevant support depends circularly on quarantined mathematics is not a closure of O4. Tactical machinery belongs in current strategy, not in this obligation.

## Historical O6 — Dormant R24 reconstruction aspiration

**Status:** Dormant; not an active obligation

**Historical aspiration:** someday obtain a fully reconstructible R24-independent proof of the singleton order floor and short-complement rigidity conclusion. Concretely, one would want to prove that in a hypothetical smallest Strong Level-(1) counterexample, for every vertex `z` and every exact two-cover of `H-z`, both rails have order at least four. No current worker is expected to pursue this, and no active proof may depend on it.

**Current policy:** R24 and R5 remain quarantined and severed from the active proof architecture. They are unusable as mathematical premises. Revisit this historical aspiration only after an explicit future strategic decision reopens it.

**Reactivation:** only by an explicit future architecture or guidance change that deliberately reopens the problem.

**Strategic role:** none in the active campaign. This entry preserves the historical aspiration and explains why active proofs must not drift back toward R24/R5 dependence.

# Current Strategy

## Astra pass — marked physical exchange and global export

Astra pass: 2026-09-14. O4 remains the only active durable obligation. Changelog `G13` is the live guidance authority. The audited R2009-R2022 contraction is retained, but G12's ancestry-free cap classification is superseded. `R2023` remains provisional and should receive ordinary audit.

### Assess

The recent audited wave genuinely removes neutral-component bookkeeping and local closure-cycle fog. But it does **not** justify forgetting the physical frontier that produced the low-transition forest. `R2019` is strongest when used as a marked first-failure statement, and `R2021` only localizes the physical debt of a cross-rail join. Two global questions remain before another large local wave is worthwhile: what exactly consumes a physical `tau<=2` two-cover, and how can a failed cap be converted into a legal exchange that preserves the marked source/first-failure data?

### Integrate

The live parent object is a **physical three-forest plus a blocked marked exchange plus source witnesses**. In the first-failure branch retain `N=M_q`, `q`, the next pair `f_{q+1},e_{q+1}`, every relevant old-F/source incidence, the literal rail orders, X/B labels, short-rail coincidences, and the source turns `(A,s,C)`. The six cross-rail joins of provisional `R2023` test the boundary of this object; they do not replace it.

A successful physical join giving a two-cover with `tau<=2` still needs an exact **export theorem**. D17.393's three-transition floor is scoped to retained source representatives with `p,q,r` internal; it is not a universal floor for arbitrary two-covers. D17.391 explicitly retains endpoint/internal-discrepancy outputs, and canonical legacy `R408` gives a graph-intrinsic balanced pair without by itself proving closure. Researchers should either locate a bounded proof-aware consumer with its real hypotheses or make construction of that consumer primary.

### Elevate

Elevate from endpoint-cap **classification** to endpoint-cap **surgery**. A failed join identifies a bad seam containing one rail endpoint, the other rail endpoint, and an inward neighbor. Use that local obstruction together with the marked old-F/source incidence to choose a segment to detach and reattach. The desired output is a legal recompletion, a spanning/source-P4 splice, or a new admissible marked three-forest with certified progress. Do not quotient by arbitrary rail reversal: rail permutation is relabeling, but reversal destroys tight internal turns in general.

The most promising concrete operation is a one-cut/two-join surgery guided by a failed seam. Net edge gain is one, so it can turn a three-forest into a two-cover, but every changed turn, component incidence, cycle possibility, and transition contribution must be checked literally. `R1057` is available only when its certified three residual components and two legal seams actually occur. If an operation returns only another three-forest, endpoint motion alone is not progress: prove a finite monotone potential on the admissible marked class or use an extremal choice that the exchange contradicts.

### Moonshot

Moonshot in three layers. First, prove the exact export contract for the low-transition physical two-covers the live machinery actually produces, including the source-exposed/R408 branch. Second, prove a marked exchange-saturation theorem: every provenance-realized low-transition three-forest at the marked physical frontier either legally recompletes/export-closes or admits a legal exchange with certified monotone progress. Third, fold the exact `j=t+1` far-seam cell into that same marked interface. A closed family under the proposed exchanges would be a useful obstruction to the mechanism; an arbitrary static cap table would not.

### Guide

Shared priorities: (i) exact global export of a physical low-transition two-cover, (ii) cap-guided physical exchange retaining marked source/first-failure data, and (iii) incorporation of `j=t+1` into that same marked interface. `R2023` should receive ordinary audit, but its correctness alone does not settle priorities (i) or (ii). Do not spend a new wave on ancestry-free cap tables, rail-reversal quotienting, neutral-component transport, generic first-open orientation lemmas, generic source-gate taxonomies, or prescribed source-P5 endpoints.

These are shared focuses, not worker assignments. Researchers should choose whichever direct consumer or legal marked exchange their local state exposes, while preserving the full physical witness package rather than compressing it away.

### Standing fences

R24/R5 remain frozen and unusable; O6 remains dormant. `R1032/R1034` still fence static sharp/gate abstractions as insufficient. `R1041` forbids prescribed source-P5 endpoint flexibility. D17.393 is not a universal transition floor for arbitrary covers, and canonical `R408` is not an automatic global consumer. Arbitrary rail reversal is not a symmetry of a tight directed forest. Matching cardinality is not a physical cover, and two formal cross edges are not automatically two legal seams. `R1057` applies only under its certified component-incidence hypotheses.

## Prior strategy provenance — G5 and G12 (superseded by G13)

Historical G5 established the first-open/augmenter synchronization program; audited `R2009-R2022` then motivated G12's endpoint-cap saturation pass. Astra G13 supersedes both as live strategy by retaining the marked physical frontier, requiring the exact low-transition export contract, and treating caps as exchange guides rather than an ancestry-free invariant. Exact historical wording remains available in changelog roots `5` and `12`; it is intentionally omitted here to reduce mandatory startup noise.

# End of canonical startup

A complete startup read reaches this section. After reading it in a new conversation, synchronize from the Canvas changelog coordinate through newer numbered changelog roots, then inspect relevant workspace activity before beginning work.