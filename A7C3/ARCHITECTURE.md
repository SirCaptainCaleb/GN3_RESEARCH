# A7C3 Research Architecture

## Core principle

**GitHub is the research record. Slack is the research room.**

GitHub contains the durable mathematical world: audited reusable results, the small subset of especially interesting mathematics, coherent developments, the current proof spine, durable obligations, strategy, architecture, and references. Slack carries live coordination, discoveries in motion, provisional results awaiting audit, tactical discussion, warnings, speculative observations, and changes whose value depends on recency.

Git history is the revision and archive mechanism. Do not recreate database-style revision objects, worker state, queues, semantic tag systems, dependency databases, or other lifecycle machinery unless actual use later proves they are necessary.

The migration is complete. GitHub `main` is the durable authority for A7C3. Legacy Supabase material is archival source material only and is not the live research record.

Ordinary nonmigration durable work goes directly to `main`. A new standalone theorem-level claim discovered in Slack should normally remain there while unaudited and be promoted to GitHub immediately when audited. GitHub should receive the final audited mathematical version rather than a sequence of provisional theorem variants. Evolving workspace mathematics may be durable before theorem-level audit when clearly presented as development rather than as a trusted reusable result.

Temporary branches are exceptional tools for work that genuinely benefits from isolation or review. They are not the default research workflow.

## Canonical entrance and initialization

**This file is the single canonical entry point for A7C3. There is no separate bootstrap layer.** A fresh worker initializes from current GitHub `main` by reading, in order:

1. `ARCHITECTURE.md` — this file; how the project works.
2. `PROOF_SPINE.md` — where the proof currently stands.
3. `OBLIGATIONS.md` — durable unresolved closure contracts.
4. `STRATEGY/CURRENT.md` — the current strategic interpretation and ambitious targets.

Then inspect pinned/current `#a7c3-control` for live changes newer than GitHub and catch up on the relevant recent `#a7c3-workspace` roots and threads, including audit tags, corrections, provisional dependencies, and concurrent mathematics that could affect the chosen line.

After orientation, expand only the mathematics needed for the chosen attack. Do not preload the whole corpus merely because it exists.

## Durable front door

A fresh Researcher should be able to orient from four small durable surfaces:

- `ARCHITECTURE.md` — **How do we work?**
- `PROOF_SPINE.md` — **Where does the proof currently stand?**
- `OBLIGATIONS.md` — **What durable mathematical requirements remain open?**
- `STRATEGY/CURRENT.md` — **What are we trying to do about them now?**

These files have different jobs. Do not collapse them into one giant status document.

### Proof spine

`PROOF_SPINE.md` is the front-door closure map. It should expose the current reduction chain, surviving major branches, genuine bottlenecks, load-bearing results or workspace sections, and important fences. It is orientation, not mathematical authority. The linked result or workspace proof is authoritative.

### Obligations

`OBLIGATIONS.md` contains durable mathematical closure contracts, not tasks. An obligation has a target, scope, and meaningful closure condition. It has no owner or required traversal order. Researchers may attack it directly, strengthen it, bypass it through a parent theorem, or make it irrelevant by changing the proof architecture.

### Strategy

`STRATEGY/CURRENT.md` is the Director's durable current interpretation of the campaign: important goals, promising representations, ambitious near-term targets, low-value routes to prune, and the rationale connecting them to the proof spine and obligations. It is not a chronological guidance ledger. Replace it when strategy changes; Git remembers the old version.

Slack `#a7c3-control` carries the immediate strategic delta. GitHub carries the durable state that results from it.

## Synchronize before resuming

A worker's local conversation state is never sufficient authority for resuming research. **Every re-entry into an existing research conversation is a synchronization boundary.** When the user says `Continue`, `resume`, `keep going`, or anything equivalent, interpret that as **synchronize with the live project, then continue from the resulting frontier**.

Before doing new mathematics after such a re-entry, refresh the live information that could invalidate, redirect, supersede, or strengthen the current line. At minimum:

- refresh relevant current GitHub `main`, including the proof spine, current strategy and obligations when they bear on the work, and any durable mathematics about to be used;
- inspect `#a7c3-control` for newer guidance, quarantines, trust changes, architecture changes, or strategic redirections;
- inspect relevant `#a7c3-workspace` roots and threads for newer mathematical findings, leading audit tags, corrections, provisional dependencies, or concurrent developments affecting the line;
- when audit state matters, identify the oldest unaudited mathematical workspace root, which is the current chronological audit frontier.

Do not rely on remembered guidance labels, remembered result status, or a previously valid dependency merely because it remains in conversation context. Fresh control information, current GitHub state, and audit status attached to the relevant mathematical finding outrank stale local plans.

This applies to Researchers, Directors, Integrators, Auditors / Repairers, and any other continuing worker. Specialized information boundaries may restrict what a worker can inspect, but do not waive synchronization against permitted sources.

## Durable mathematics

```text
A7C3/
├── ARCHITECTURE.md
├── PROOF_SPINE.md
├── OBLIGATIONS.md
├── STRATEGY/
│   ├── README.md
│   └── CURRENT.md
├── RESULTS/
│   ├── INTERESTING/
│   ├── USABLE/
│   │   ├── ACTIVE/
│   │   └── LEGACY/
│   └── UNUSABLE/
│       ├── QUARANTINED/
│       └── INVALID/
├── WORKSPACE/
└── REFERENCES/
```

### Scratch, development, and results

Most mathematical work is scratch work. That is normal. A long campaign produces many local observations, short chains of reasoning, abandoned routes, calculations, partial constructions, and lemmas that were useful once but do not deserve permanent foreground attention.

`WORKSPACE/` is the durable notebook layer. It contains coherent evolving developments, constructions, exact local mechanisms, useful failed branches, limitations, and enough old mathematical texture to rifle through when necessary. Persistence here is valuable even when future workers will rarely read most of it.

`RESULTS/` is narrower. A result is a standalone audited mathematical interface worth reusing outside the immediate scratch chain that produced it. Correctness alone does not make a result important.

A reusable result under `RESULTS/` is understood to have passed audit in its durable form.

### Interesting results

`RESULTS/INTERESTING/` is the curated shelf: the small subset of audited mathematics that deserves unusually high future attention.

Interesting mathematics includes, for example:

- results that make substantial progress toward the theorem or collapse a major branch;
- ideas or mechanisms that are genuinely creative or conceptually clarifying;
- results that become repeatedly reused across otherwise different arguments;
- especially strong reductions, normal forms, invariants, or reusable structural principles;
- very non-obvious constructions or counterexamples that kill a tempting route and teach something durable about the problem.

The standard is mathematical interest, not merely validity. The folder should remain selective. It is expected to be much smaller than the surrounding notebook and ordinary-result corpus.

A worker who discovers a result they judge strong, creative, unusually reusable, or otherwise mathematically interesting should append `(INTERESTING)` to the Slack root. This is a nomination, not yet a curation decision. When the result is audited, the auditor also judges the nomination. If the auditor agrees and the result receives `[PASS]` or `[PASS_ADJUSTED]`, persist the final audited result canonically in `RESULTS/INTERESTING/`. If the audit passes but the auditor does not agree that the result clears the interestingness threshold, persist it in the ordinary appropriate result location instead.

`(INTERESTING)` is independent of audit status. A root may therefore begin `[PASS]` or `[PASS_ADJUSTED]` and also end with `(INTERESTING)`. If audit rejects the interestingness nomination, remove `(INTERESTING)` when recording the audit status.

Do **not** keep duplicate canonical copies of an interesting result in both `INTERESTING/` and `USABLE/ACTIVE/`. The interesting file is the canonical result. Duplication creates drift. If later audit invalidates it, move it out of `INTERESTING/` into the appropriate unusable location. If it merely becomes old or strategically inactive while remaining mathematically interesting, it may stay on the interesting shelf.

### Ordinary result locations

- `RESULTS/INTERESTING/` — valid, audited, safe, and specially curated for mathematical importance or creativity.
- `RESULTS/USABLE/ACTIVE/` — valid, audited, safe, and currently useful, but not specially curated as interesting.
- `RESULTS/USABLE/LEGACY/` — valid, audited, and safe, but superseded, off the current route, or otherwise lower priority.
- `RESULTS/UNUSABLE/QUARANTINED/` — live repair targets that must not be used as trusted premises.
- `RESULTS/UNUSABLE/INVALID/` — known-invalid mathematics retained because the failure itself is durably useful.

Old is not the same as unsafe, and ordinary is not the same as unimportant. The interesting tier exists to expose diamonds, not to demean the notebook around them.

## Search and theorem use

Workers should not routinely excavate the entire scratch corpus. Default theorem discovery should first search `RESULTS/INTERESTING/`, then `RESULTS/USABLE/ACTIVE/`. Broaden to all usable results when necessary. Search `WORKSPACE/` deliberately when the proof needs local development, historical machinery, constructions, failed routes, or details not promoted to reusable results. Search quarantined material only for repair work.

When searching for older machinery, use several literal mathematical concepts rather than betting everything on one guessed phrase. Prefer recall over an artificially narrow query, then inspect the strongest matches proof-aware.

High recall still matters when the obvious surfaces fail, but the architecture should make the best mathematics easy to encounter before notebook archaeology begins.

**Theorem application is proof-aware.** Before using a result as an inference, understand the proof mechanism well enough to preserve structure that survives specialization: witnesses, physical vertices, path orders, selected states, cuts, signs, ancestry, equality conditions, exceptional branches, or other information that may matter downstream. The statement is a minimum contract, not an instruction to discard what the proof already paid for.

An unaudited Slack result is **provisional mathematics, not forbidden mathematics**. A worker may use it without first advancing the audit frontier to it, but must make that dependence explicit. In the dependent root's thread or the corresponding live development, record a compact `Provisional dependencies:` line identifying the exact unaudited Slack root or roots being used. Any conclusion depending on them remains provisional until those dependencies are audited successfully.

The worker may instead choose to advance the chronological audit frontier through the needed result before relying on it. This is a judgment call: audit now for confidence, or proceed provisionally for speed while accepting repair risk if an upstream dependency later fails.

A theorem-level claim cannot acquire trusted audited status while an unaudited dependency remains beneath it. If a provisional dependency later receives `[FAIL]` or a materially narrowing `[PASS_ADJUSTED]`, downstream claims that relied on the superseded form must be revisited before promotion or reuse as trusted mathematics.

## Slack

Slack is an attention surface, not a second durable record. Its purpose is to expose the most valuable current facts with very low reading cost while allowing supporting detail to remain attached and searchable in threads.

Permanent channels:

- `#a7c3-control` — low-volume changes that can redirect or invalidate current work: Director guidance, quarantines, architecture changes, major strategic pivots, and other control-plane deltas.
- `#a7c3-workspace` — mathematics happening now that another active Researcher could plausibly use or act on: discoveries, partial arguments, useful failures, questions, cross-worker observations, audit status, interestingness nominations, provisional dependencies, and notices that durable mathematics was written to GitHub.
- `#a7c3-lab` — lower-pressure ephemeral research chatter worth retaining: motivated conjectures, speculative connections, constructions or examples that may generalize, counterexample intuitions, half-formed abstractions, and other unexpected mathematical talk that does not yet belong in control, workspace, or GitHub.

If a finding should change what another active Researcher does now, put it in `#a7c3-workspace`. If a trust failure redirects the team or invalidates active dependencies, also surface that consequence in `#a7c3-control`. Otherwise `#a7c3-lab` is the default home for interesting but non-operational chatter.

Temporary campaign channels are allowed when one campaign would genuinely overwhelm the main workspace channel.

### Root messages are headline space

A Slack root message should maximize valuable attention. Treat root space as a stream of precise headlines, not as a place for proofs, derivations, constructions, interpretation manuals, action lists, or discussion.

For a mathematical finding, the root should contain **the finding itself expressed as a precise mathematical statement**. It should not merely name the topic, summarize the proof, or describe what the worker did. **Precision outranks brevity. A long mathematical sentence is preferable to a shorter but ambiguous headline.**

Put the proof, construction, derivation, interpretation guidelines, caveats, examples, supporting computations, proposed actions, routing detail, provisional-dependency declaration, canonical GitHub pointer, and local discussion in the thread under that root. Threading is assumed: do not waste headline space on phrases such as “proof in thread” or “details in thread.”

In `#a7c3-workspace`, the root is the precise mathematical finding, obstruction, counterexample, reduction, or clearly marked conjecture, optionally preceded by one leading audit tag and optionally followed by `(INTERESTING)`. In `#a7c3-control`, the root is the exact guidance, quarantine, trust change, architecture change, or strategic redirection. In `#a7c3-lab`, the root is the precise provisional observation, conjecture, construction, example, analogy, or counterexample intuition.

If a thread produces a genuinely new mathematical finding or control fact, create a new root headline for that new fact rather than burying it in the old thread.

Recent mathematical roots stay in `#a7c3-workspace` after audit. Do not move or delete a root merely because it passed or failed; its leading audit tag makes its state visible while preserving the chronological live stream.

If a Slack root ever genuinely needs deletion, **delete every reply in its thread first, then delete the root**. Deleting only the root can leave replies visible or discoverable in the channel and creates misleading debris. If the replies cannot be cleanly removed, do not treat the thread as cleanly deleted.

Each permanent channel may keep one compact pinned opener that states the channel's routing purpose. Durable policy lives here in GitHub; pinned openers are convenience signage.

## Audit stays attached to the finding

Audit is metadata and discussion attached to a mathematical finding, not a separate page that workers must later correlate back to the mathematics.

When a Slack mathematical root is audited, edit that same root to **prefix** exactly one audit status:

- `[PASS]` — the precise root statement survives audit as written.
- `[FAIL]` — the root statement is not safe to use as a mathematical premise.
- `[PASS_ADJUSTED]` — a valid nearby statement survives after correction, narrowing, or another substantive adjustment.

Audit reasoning belongs in the existing thread. For `[PASS_ADJUSTED]`, the thread must state the exact surviving adjustment. If the old root wording would be materially misleading, edit the mathematical statement itself to the precise surviving version and retain `[PASS_ADJUSTED]` at the beginning.

An unaudited root has **no audit tag**. Do not add a `[PROVISIONAL]` tag; the absence of an audit tag is the provisional state.

### Chronological audit frontier

Routine auditing is strictly chronological within the mathematical roots of `#a7c3-workspace`. **The oldest unaudited mathematical root is the audit frontier and is the only unaudited workspace result eligible for the next routine audit.** To audit a later root, first settle every earlier unaudited mathematical root with `[PASS]`, `[PASS_ADJUSTED]`, or `[FAIL]`.

This rule makes the workspace itself the audit queue without creating a separate queue object. New research may continue and new roots may be posted beyond the frontier; they simply remain unaudited until the frontier reaches them. No result can be silently skipped forever because a more attractive later claim was chosen for audit first.

Research use is deliberately more permissive than audit order. A worker may use a later unaudited result provisionally, provided the exact dependence is recorded clearly as described above. The worker may also choose to clear the audit frontier through that result first. Either choice is allowed; what is forbidden is silently treating unaudited mathematics as trusted.

If the frontier result passes, prefix `[PASS]`. If it survives only after correction, prefix `[PASS_ADJUSTED]`. If it fails, prefix `[FAIL]`. A failed result cannot be used as a trusted premise unless a repaired statement is formulated and eventually audited in its own right. Any provisional descendants that used it must be rechecked.

### Audited means persisted and linked

**Completing an audit creates an immediate persistence obligation.** Do not leave an audited result living only in Slack.

- `[PASS]` goes promptly to its appropriate canonical durable GitHub result location with the audited statement and proof.
- `[PASS_ADJUSTED]` goes promptly to GitHub using only the final corrected statement and proof.
- A passing result whose `(INTERESTING)` nomination is endorsed goes canonically to `RESULTS/INTERESTING/`.
- `[FAIL]` does not enter usable results. Preserve an important invalidation or fence in `RESULTS/UNUSABLE/INVALID/` or the relevant `WORKSPACE/` development when its failure itself has durable value.

For every `[PASS]` or `[PASS_ADJUSTED]` root, after the canonical GitHub file exists, add a compact thread reply of the form:

`Canonical GitHub result: A7C3/RESULTS/.../R....md`

The pointer belongs in the thread, not the root, so the live stream remains mathematically tidy. The GitHub file is the durable mathematical authority; the Slack thread is the bridge from the live finding to that authority. If the canonical result later moves, for example into `RESULTS/INTERESTING/`, update the thread pointer rather than leaving a stale path.

If the audited result changes the proof spine, obligations, strategy, trust of existing durable results, or other current durable mathematics, update those surfaces in the same integration pass.

The Slack thread may retain exploratory proof, audit discussion, counterexamples, correction history, and its place in the recent research stream. GitHub contains the final durable mathematical object.

## Slack is provisional

Slack is provisional by default. `#a7c3-lab` is especially provisional. Unaudited workspace mathematics may feed later provisional research when its dependence is explicit, but it does not thereby become trusted. Before a standalone theorem-level result enters the trusted GitHub result corpus, the chronological audit frontier must reach it and every unaudited dependency it relies on must have survived audit in the form actually used.

Architecture, routing rules, and channel-use conventions belong in GitHub `ARCHITECTURE.md`, not in Slack.

There is no formal Researcher-return object. Leave a concise live handoff only when another conversation actually needs one.

## Researchers, dedicated conversations, and cognitive mantles

The default agent is a plain **Researcher**: an autonomous mathematician allowed to prove, explore, compute, challenge, integrate, elevate, search old mathematics, invent representations, and change direction for mathematical reasons.

Most former roles are better understood as activities or cognitive mantles, not persistent worker identities:

- **Explorer** — sustain a concrete attack.
- **Elevator** — seek parent theorems, invariants, quotients, normal forms, representation changes, or better targets.
- **Integrator** — understand how new and old proof mechanisms fit together; recover stronger consumers, latent witnesses, hierarchy, supersession, fences, shortcuts, compression, or simplification.
- **Moonshotting** — deliberately attack a target whose full success would close the theorem or a major branch.

Mantles change posture, not permission. They are not stored as project state.

### Auditor / Repairer

A dedicated **Auditor / Repairer** conversation is useful because adversarial verification benefits from persistent cognitive posture. Its job is to advance the chronological audit frontier, attack load-bearing durable results when separately requested, trace mathematical damage, and repair failed or quarantined mathematics when possible. It is not the owner of a separate audit ledger.

For routine Slack audit, the Auditor follows the same frontier rule as everyone else and does not skip an older unaudited workspace root to audit a newer one. Status is written onto the originating Slack root, reasoning stays in that thread, completed audit mathematics is persisted immediately and linked back from that thread, and interestingness nominations receive a second mathematical judgment during audit. Separate repair work on already-failed or quarantined durable results is not constrained by the Slack frontier.

### Director

The project has one logical **Director function**. Astra performs scarce high-value strategic passes when available. Between those passes, an Acting Director / Vice Director performs the same kind of work continuously. They are not competing strategic authorities and should update one current durable strategy.

The Director's recurring intellectual cycle is: assess the real proof state, elevate to broader phenomena or representations, integrate proof-aware mathematics, moonshot toward closure, and guide the team with a small number of valuable focuses.

Guidance does **not** assign individual Researchers to tasks. Researchers choose opportunistically within the current target landscape. Overlap is allowed when useful.

### Independent locality escape

A deliberately isolated Independent conversation may still be used when locality escape is valuable. Its information boundary is an experimental choice, not another durable state subsystem. Mathematics that becomes durable enters the same GitHub record and ordinary trust model.

## Promotion and integration

Promotion should be boring.

- A standalone reusable theorem is promoted to `RESULTS/` immediately after its chronological audit completes and its unaudited dependencies, if any, have been settled successfully in the form used.
- An audited result endorsed as interesting is promoted directly to `RESULTS/INTERESTING/`.
- Connected evolving proof architecture goes in the appropriate `WORKSPACE/` development.
- A change in the closure map updates `PROOF_SPINE.md`.
- A stable unresolved requirement updates `OBLIGATIONS.md`.
- A strategic reinterpretation updates `STRATEGY/CURRENT.md`.
- A trust failure moves or edits the durable result itself and is surfaced in `#a7c3-control` when active work could be affected.

Integration is mathematical research, not clerical filing. A result is not fully integrated merely because it was cited or placed in the right folder. Integration asks how its proof mechanism changes what can now be proved.

At natural checkpoints, ask whether the latest work changes the proof spine, obligations, strategy, or trust landscape rather than merely extending the same local machinery. Persist coherent durable advances where they belong and continue doing mathematics from the resulting frontier.

## Concurrency

Concurrency is handled structurally rather than through a custom locking system. Researchers normally work in separate result files or mathematical regions; shared synthesis documents should be edited carefully when active concurrent work overlaps. Ordinary Git conflict handling is preferable to research-specific locks or sessions.

Direct work on `main` is normal. Use temporary branches only when isolation has concrete value.

## Minimality of the system

There is deliberately no hidden second research operating system behind GitHub:

- no database required for correctness after cutover;
- no persistent worker registry;
- no assignment queue;
- no mantle state;
- no separate theorem registry beyond the files themselves;
- no mandatory semantic-tag service;
- no dependency server;
- no separate audit ledger;
- no duplicate interesting-result mirror;
- no durable Slack mirror;
- no explicit revision database.

The filesystem is the model. Git is the history. Search is the retrieval layer. Slack is the room full of mathematicians.

When actual use reveals a better structure, change the architecture in Git. The architecture is allowed to evolve.