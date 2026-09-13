# A7C3 Research Architecture

## Core principle

**GitHub is the research record. Slack is the research room.**

GitHub contains the durable mathematical world: results, proofs, coherent developments, the current proof spine, durable obligations, strategic interpretation, architecture, and references. Slack carries live coordination, discoveries in motion, tactical discussion, warnings, and changes whose value depends on recency.

Git history is the revision and archive mechanism. Do not recreate database-style revision objects, worker state, queues, semantic tag systems, or lifecycle machinery unless actual use later proves they are necessary.

The migration is complete. GitHub `main` is the durable authority for A7C3. Legacy Supabase material is archival source material only and is not the live research record.

Ordinary nonmigration research work should be written directly to `main`. This includes new results and proofs, workspace development, integration, audit repairs, proof-spine updates, obligations, strategy, architecture changes, and references. Temporary branches are exceptional tools for work that genuinely benefits from isolation or review; they are not the default research workflow and should be merged or deleted promptly when no longer needed.

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

Folder location encodes trust and current relevance:

- `RESULTS/USABLE/ACTIVE/` — valid, safe, and part of the current preferred toolbox.
- `RESULTS/USABLE/LEGACY/` — valid and safe, but superseded, off the current route, or otherwise lower priority.
- `RESULTS/UNUSABLE/QUARANTINED/` — live repair targets that must not be used as premises.
- `RESULTS/UNUSABLE/INVALID/` — known-invalid mathematics.

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

## Slack

Permanent channels:

- `#a7c3-control` — low-volume changes that can redirect or invalidate current work: Director guidance, quarantines, architecture changes, major strategic pivots, and other control-plane deltas.
- `#a7c3-workspace` — mathematics happening now: discoveries, partial arguments, useful failures, questions, cross-worker observations, and notices that durable mathematics was written to GitHub.
- `#a7c3-audit` — adversarial verification, suspected gaps, dependency failures, repair work, invalidations, and clearances.

Temporary campaign channels are allowed when one campaign would genuinely overwhelm the main workspace channel.

Slack is provisional by default. If durable mathematics will rely on a Slack finding, promote that finding to GitHub first or together with the dependent mathematics.

Post during active work when another active Researcher could plausibly change what they are doing if they knew the finding. Use threads for discussion. If a thread produces a materially new finding, surface it as a new root message rather than burying it.

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

- A standalone reusable theorem goes in `RESULTS/`.
- Connected evolving proof architecture goes in the appropriate `WORKSPACE/` development.
- A change in the closure map updates `PROOF_SPINE.md`.
- A stable unresolved requirement updates `OBLIGATIONS.md`.
- A strategic reinterpretation updates `STRATEGY/CURRENT.md`.
- A trust failure moves or edits the result itself and should be announced in `#a7c3-control` when current work could be affected.

Integration is mathematical research, not clerical filing. A result is not fully integrated merely because it was cited or placed in the right folder. Integration asks how its proof mechanism changes what can now be proved.

Audit does not create a parallel permanent review universe. Trust changes should be reflected in the mathematical object and its folder. Reusable audit mathematics becomes ordinary durable mathematics.

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
- no durable Slack mirror;
- no explicit revision database.

The filesystem is the model. Git is the history. Search is the retrieval layer. Slack is the room full of mathematicians.

When actual use reveals a better structure, change the architecture in Git. The architecture is allowed to evolve.
