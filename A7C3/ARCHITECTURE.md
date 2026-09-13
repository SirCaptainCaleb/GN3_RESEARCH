# A7C3 Research Architecture

## Core principle

**GitHub is the research record. Slack is the research room.**

GitHub contains the durable mathematical world: audited reusable results, proofs, coherent developments, the current proof spine, durable obligations, strategic interpretation, architecture, and references. Slack carries live coordination, discoveries in motion, provisional results awaiting audit, tactical discussion, warnings, speculative observations, and changes whose value depends on recency.

Git history is the revision and archive mechanism. Do not recreate database-style revision objects, worker state, queues, semantic tag systems, or lifecycle machinery unless actual use later proves they are necessary.

The migration is complete. GitHub `main` is the durable authority for A7C3. Legacy Supabase material is archival source material only and is not the live research record.

Ordinary nonmigration durable work should be written directly to `main`. This includes audited results and proofs, coherent workspace development, integration, audit repairs, proof-spine updates, obligations, strategy, architecture changes, and references. A new standalone theorem-level claim discovered in Slack should normally remain there while unaudited and be promoted to GitHub immediately when audited. GitHub should receive the final audited mathematical version rather than a sequence of provisional theorem variants. Evolving workspace mathematics may be durable before theorem-level audit when it is clearly presented as development rather than as a trusted reusable result.

Temporary branches are exceptional tools for work that genuinely benefits from isolation or review; they are not the default research workflow and should be merged or deleted promptly when no longer needed.

## Durable front door

A fresh Researcher should be able to orient from four small durable surfaces:

- `ARCHITECTURE.md` — **How do we work?**
- `PROOF_SPINE.md` — **Where does the proof currently stand?**
- `OBLIGATIONS.md` — **What durable mathematical requirements remain open?**
- `STRATEGY/CURRENT.md` — **What are we trying to do about them now?**

These files have different jobs. Do not collapse them into one giant status document.

### Proof spine

`PROOF_SPINE.md` is the front-door closure map. It should expose the current reduction chain, surviving major branches, genuine bottlenecks, load-bearing results or workspace sections, and important fences. It is intentionally small enough to read on ordinary startup.

The spine is orientation, not mathematical authority. The linked result or workspace proof is authoritative. When integration changes how the proof fits together, update the spine.

### Obligations

`OBLIGATIONS.md` contains durable mathematical closure contracts, not tasks. An obligation has a target, scope, and meaningful closure condition. It has no owner, assignee, worker lane, or required traversal order. Researchers may attack it directly, strengthen it, bypass it through a parent theorem, or make it irrelevant by changing the proof architecture.

Only stable unresolved requirements belong here. Git history preserves closed or superseded formulations.

### Strategy

`STRATEGY/CURRENT.md` is the Director's durable current interpretation of the campaign: the important goals, promising representations, ambitious near-term targets, low-value routes to prune, and the rationale connecting them to the proof spine and obligations.

It is not a chronological Guidance ledger. Replace it when the strategy changes; Git remembers the old version.

Slack `#a7c3-control` carries the immediate strategic delta. GitHub carries the durable state that results from it.

### Synchronize before resuming

A worker's local conversation state is never sufficient authority for resuming research. **Every re-entry into an existing research conversation is a synchronization boundary.** When the user says `Continue`, `resume`, `keep going`, or anything equivalent, interpret that as **synchronize with the live project, then continue from the resulting frontier**, not as permission to continue immediately from cached conversational state.

Before doing new mathematics after such a re-entry, refresh the live information that could invalidate, redirect, supersede, or strengthen the worker's current line. At minimum:

- refresh the relevant current GitHub `main` state, including the proof spine, current strategy and obligations when they bear on the work, plus any result or workspace material the worker is about to use;
- inspect `#a7c3-control` for newer guidance, quarantines, trust changes, architecture changes, or strategic redirections;
- inspect the relevant `#a7c3-workspace` roots and threads for newer mathematical findings and for audit suffixes or audit followups affecting any Slack mathematics the worker may rely on;
- inspect other recent workspace developments that may supersede or interact with the worker's local frontier.

Do not rely on remembered guidance labels, remembered result status, or a previously valid dependency simply because it remains in the conversation context. Fresh control information, current GitHub state, and audit status attached to the relevant mathematical finding outrank stale local plans. If synchronization changes the frontier, adapt before continuing; if it does not, resume the prior attack without ceremony.

This rule applies to Researchers, Directors, Integrators, Auditors / Repairers, Independents when their information boundary permits it, and any other continuing worker. Specialized information boundaries may restrict what a worker is allowed to inspect, but they do not waive synchronization against the sources that worker is permitted to see.

## Durable mathematics

```text
A7C3/
├── BOOTSTRAP.md
├── ARCHITECTURE.md
├── PROOF_SPINE.md
├── OBLIGATIONS.md
├── STRATEGY/
│   ├── README.md
│   └── CURRENT.md
├── RESULTS/
│   ├── USABLE/
│   │   ├── ACTIVE/
│   │   └── LEGACY/
│   └── UNUSABLE/
│       ├── QUARANTINED/
│       └── INVALID/
├── WORKSPACE/
└── REFERENCES/
```

### Results

A result is a standalone reusable mathematical interface. Each result file should contain its current durable statement and its preferred proof when available, plus hypotheses, scope, exclusions, validity notes, or other metadata only when they materially affect correct use.

A reusable result placed under `RESULTS/USABLE/` is understood to have passed audit in its durable form. Slack may contain newer provisional claims that have not yet crossed that threshold.

Folder location encodes trust and current relevance:

- `RESULTS/USABLE/ACTIVE/` — valid, audited, safe, and part of the current preferred toolbox.
- `RESULTS/USABLE/LEGACY/` — valid, audited, and safe, but superseded, off the current route, or otherwise lower priority.
- `RESULTS/UNUSABLE/QUARANTINED/` — live repair targets that must not be used as trusted premises.
- `RESULTS/UNUSABLE/INVALID/` — known-invalid mathematics retained because the failure itself is durably useful.

Old is not the same as unsafe. A superseded theorem may remain perfectly valid and belongs under `USABLE/LEGACY`, not `UNUSABLE`.

### Workspaces

`WORKSPACE/` contains coherent evolving mathematical developments descended from the old D* documents. They are not a live message bus and are not merely summaries. They preserve connected proof architecture, constructions, exact local mechanisms, useful failed branches, limitations, and developing synthesis at argument scale.

Slack is the live workspace. GitHub `WORKSPACE/` is the coherent durable workspace.

Use one coherent current file when a development is reasonably sized. Large developments such as D17 may be split into natural searchable argument-sized sections.

## Search and theorem use

Search is the primary discovery layer. Default theorem discovery should search `RESULTS/USABLE/ACTIVE/`; broaden to `RESULTS/USABLE/` for older valid machinery and deliberately search `RESULTS/UNUSABLE/QUARANTINED/` for repair work. Search relevant `WORKSPACE/` subtrees when the needed mathematics lives inside a development.

High recall is preferred. Missing an old useful theorem is more expensive than reading a few false positives.

Exact result references inside proofs remain valuable, but the architecture does not require a separate dependency database.

**Theorem application is proof-aware.** Before using a result as an inference, understand the proof mechanism well enough to preserve structure that survives the specialization: witnesses, physical vertices, path orders, selected states, cuts, signs, ancestry, equality conditions, exceptional branches, or other information that may matter downstream. The statement is a minimum contract, not an instruction to discard what the proof already paid for.

An unaudited Slack result is not forbidden mathematics. Any worker may use it, but **the worker must audit the exact result they intend to rely on before using it as a premise**. This contemporaneous self-audit is part of the theorem application, not optional cleanup for later. If the audit passes or yields an adjusted valid result, mark the Slack root accordingly and persist the audited result to GitHub immediately. This distributes verification across the consumers who actually need a claim and prevents a separate audit backlog from becoming a bottleneck.

## Slack

Slack is an attention surface, not a second durable record. Its purpose is to expose the most valuable current facts with very low reading cost while allowing arbitrary supporting detail to remain attached and searchable in threads.

Permanent channels:

- `#a7c3-control` — low-volume changes that can redirect or invalidate current work: Director guidance, quarantines, architecture changes, major strategic pivots, and other control-plane deltas.
- `#a7c3-workspace` — mathematics happening now that another active Researcher could plausibly use or act on: discoveries, partial arguments, useful failures, questions, cross-worker observations, audit status attached to those findings, and notices that durable mathematics was written to GitHub.
- `#a7c3-lab` — lower-pressure ephemeral research chatter worth retaining: interesting observations, motivated conjectures, speculative connections, constructions or examples that may generalize, counterexample intuitions, half-formed abstractions, and other unexpected mathematical talk that does not yet belong in control, workspace, or GitHub.

The routing threshold matters. If a finding should change what another active Researcher does now, put it in `#a7c3-workspace`. Audit its root in place rather than creating a parallel audit message elsewhere. If a trust change or failure redirects the team or invalidates active dependencies, also surface that consequence in `#a7c3-control`. Otherwise, if something is interesting enough that future workers may want to rediscover it but it is not yet operationally important, `#a7c3-lab` is the default home.

Temporary campaign channels are allowed when one campaign would genuinely overwhelm the main workspace channel.

### Root messages are headline space

A Slack root message should maximize valuable attention. Treat root space as a stream of precise headlines, not as a place for proofs, derivations, constructions, interpretation manuals, action lists, or discussion.

For a mathematical finding, the root should contain **the finding itself expressed as a precise mathematical statement**. It should not merely name the topic, summarize the proof, or describe what the worker did. A long mathematical sentence is preferable to a shorter but ambiguous headline.

Put the proof, construction, derivation, interpretation guidelines, caveats, examples, supporting computations, proposed actions, routing detail, and local discussion in the thread under that root. Threading is assumed: do not waste headline space on phrases such as “proof in thread” or “details in thread.”

The same discipline applies by channel:

- In `#a7c3-workspace`, the root is the precise mathematical finding, obstruction, counterexample, reduction, or clearly marked conjecture, together with its compact audit suffix once audited.
- In `#a7c3-control`, the root is the exact guidance, quarantine, trust change, architecture change, or strategic redirection. Rationale and implementation detail belong in the thread.
- In `#a7c3-lab`, the root is the precise provisional observation, conjecture, construction, example, analogy, or counterexample intuition, with conjectural status made explicit when needed.

If a thread produces a genuinely new mathematical finding or a new control fact, create a new root headline for that new fact rather than burying it in the old thread.

Each permanent channel may keep one compact pinned opener that states the channel's routing purpose. The durable policy governing those channels lives here in GitHub, not in the pinned Slack text. Pinned openers are convenience signage and may be reconstructed from this document.

### Audit stays attached to the finding

Audit is metadata and discussion attached to a mathematical finding, not a separate page that workers must later correlate back to the mathematics.

When a Slack mathematical root is audited, edit that same root to append exactly one compact status:

- `(PASS)` — the precise root statement survives audit as written.
- `(FAIL)` — the root statement is not safe to use as a mathematical premise.
- `(PASS_ADJUSTED)` — the audit found a valid nearby statement only after correction, narrowing, or another substantive adjustment.

The audit reasoning belongs in the existing thread under that root. For `(PASS_ADJUSTED)`, the thread must state the exact surviving adjustment. If leaving the original root wording would itself be materially misleading after adjustment, edit the mathematical statement in the root to the precise surviving version and retain `(PASS_ADJUSTED)` so the history of adjustment remains immediately visible.

There is no separate routine audit channel. A worker encountering a root can see its trust status in the same place as the mathematical statement. An unaudited root simply has no audit suffix.

### Audit on use

Unaudited results are available for research, but not for blind composition. A worker may rely on an unaudited Slack result only after auditing the exact claim they need. The worker may perform that audit themselves; they do not need to wait for a dedicated Auditor.

If the result passes, append `(PASS)`. If it survives only after correction, append `(PASS_ADJUSTED)` and record the exact adjustment in the thread. If it fails, append `(FAIL)` and record the failure in the thread. A failed result cannot be used as a premise unless a new repaired statement is formulated and audited in its own right.

This rule deliberately pushes verification toward the point of mathematical consumption. A result that nobody needs need not consume audit attention merely because it was posted, while a result that becomes load-bearing is checked by the worker about to load it.

### Audited means persisted

**Completing an audit creates an immediate persistence obligation.** Do not leave an audited result living only in Slack.

- A `(PASS)` result should be written promptly to its appropriate durable GitHub location with the audited statement and proof.
- A `(PASS_ADJUSTED)` result should be written promptly to GitHub using only the final corrected mathematical statement and proof. Do not preserve the superseded pre-audit statement as a competing durable theorem version merely to mirror the Slack history; Git already records future durable edits.
- A `(FAIL)` result should not enter `RESULTS/USABLE/`. If the invalid result or its failure is important enough to preserve, put the final invalidation or fence in `RESULTS/UNUSABLE/INVALID/` or the relevant `WORKSPACE/` development, whichever best matches the mathematical object.

If the audited result changes the proof spine, obligations, strategy, trust of existing durable results, or other current durable mathematics, update those surfaces in the same integration pass rather than leaving GitHub semantically behind Slack.

The Slack thread may retain the exploratory proof, audit discussion, counterexamples, and correction history. GitHub should contain the final durable mathematical object.

### Slack is provisional

Slack is provisional by default. `#a7c3-lab` is especially provisional: it is a searchable memory of interesting chatter, not a theorem registry or source of authority. If durable mathematics will rely on a Slack finding, audit it and promote the resulting final mathematics to GitHub first or together with the dependent mathematics. If a lab observation becomes strategically or operationally important, surface it again in the appropriate higher-signal Slack channel rather than assuming workers monitor the lab continuously.

Architecture, routing rules, and channel-use conventions belong in GitHub `ARCHITECTURE.md`, not in Slack.

There is no formal Researcher-return object. Leave a concise live handoff only when another conversation actually needs one.

## Researchers, dedicated conversations, and cognitive mantles

The default agent is a plain **Researcher**: an autonomous mathematician allowed to prove, explore, compute, challenge, integrate, elevate, search old mathematics, invent representations, and change direction for mathematical reasons.

Most former roles are better understood as **activities or cognitive mantles**, not persistent worker identities:

- **Explorer** — sustain a concrete attack.
- **Elevator** — seek parent theorems, invariants, quotients, normal forms, representation changes, or better targets.
- **Integrator** — understand how new and old proof mechanisms fit together; recover stronger consumers, latent witnesses, hierarchy, supersession, fences, shortcuts, compression, or simplification; preserve proof-generated structure and ask what stronger deduction becomes reachable because of the synthesis.
- **Moonshotting** — deliberately attack a target whose full success would close the theorem or a major branch, even when the target is probably beyond immediate reach.

Mantles change posture, not permission. They are not stored as project state. One Researcher may move among them naturally in a single conversation.

### Auditor / Repairer

A dedicated **Auditor / Repairer** conversation is useful because adversarial verification benefits from persistent cognitive posture. Its job is to attack load-bearing results, trace mathematical damage, and repair the result or its descendants when possible. It is not restricted to issuing verdicts.

The Auditor works on the same mathematical objects as everyone else: audit status is written onto the originating Slack root, audit reasoning stays in that root's thread, and completed audit mathematics is persisted immediately to GitHub. The dedicated Auditor is therefore a cognitive specialization, not the owner of a separate audit ledger.

A repair produced by the Auditor may still deserve independent checking when it becomes load-bearing.

### Director

The project has one logical **Director function**. Astra performs scarce high-value strategic passes when available. Between those passes, an Acting Director / Vice Director performs the same kind of work continuously. They are not competing strategic authorities and should update one current durable strategy.

The Director's recurring intellectual cycle is:

1. **Assess** — reconstruct what is actually happening in the proof now. Identify what genuinely died, what survived, and where the real bottleneck moved.
2. **Elevate** — seek the broader phenomenon, parent theorem, invariant, quotient, normal form, or representation behind the latest local results.
3. **Integrate** — perform proof-aware synthesis across new and old mathematics. Recover forgotten consumers and fences, preserve latent structure, simplify the theorem lattice, and update the proof spine when the architecture has changed.
4. **Moonshot** — formulate ambitious immediate targets aimed at closure of the theorem or a major branch. Partial progress is valuable, but the gravitational target is closure.
5. **Guide** — issue a small number of team-wide focuses explaining what is now valuable and why.

Guidance does **not** assign individual Researchers to tasks. Researchers choose opportunistically within the current target landscape. Overlap is allowed and often desirable when a hard gap needs many independent attacks.

Scarce Director attention should be spent on synthesis, route redesign, major allocation changes, or moments when the closure map itself has changed, not as an approval gate for ordinary research.

### Independent locality escape

A deliberately isolated Independent conversation may still be used when locality escape is valuable. Its information boundary is an experimental choice, not another durable state subsystem. Any mathematics that becomes durable must enter the same GitHub record and ordinary trust model.

## Promotion, integration, and audit

Promotion should be boring.

- A standalone reusable theorem is promoted to `RESULTS/` immediately after audit.
- Connected evolving proof architecture goes in the appropriate `WORKSPACE/` development, with reusable theorem-level claims promoted after audit.
- A change in the closure map updates `PROOF_SPINE.md`.
- A stable unresolved requirement updates `OBLIGATIONS.md`.
- A strategic reinterpretation updates `STRATEGY/CURRENT.md`.
- A trust failure moves or edits the durable result itself and should be announced in `#a7c3-control` when current work could be affected.

Integration is mathematical research, not clerical filing. A result is not fully integrated merely because it was cited or placed in the right folder. Integration asks how its proof mechanism changes what can now be proved.

Audit does not create a parallel permanent review universe. Its visible status stays attached to the originating Slack finding, and its final mathematical outcome enters the ordinary durable record immediately. Reusable audit mathematics becomes ordinary durable mathematics.

## Concurrency

Concurrency is handled structurally rather than through a custom locking system. Researchers normally work in separate result files or mathematical regions; shared synthesis documents should be edited carefully when active concurrent work overlaps. Ordinary Git conflict handling is preferable to inventing research-specific locks or session machinery.

Direct work on `main` is the normal case. When multiple Researchers are active concurrently, coordinate ownership of the specific files or regions being edited and keep commits reasonably scoped so conflicts remain ordinary Git conflicts. Create a temporary branch only when isolation has concrete value, such as a risky large-scale rewrite, an experiment that should not yet enter the durable record, or work that explicitly needs separate review.

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
- no durable Slack mirror;
- no explicit revision database.

The filesystem is the model. Git is the history. Search is the retrieval layer. Slack is the room full of mathematicians.

When actual use reveals a better structure, change the architecture in Git. The architecture is allowed to evolve.
