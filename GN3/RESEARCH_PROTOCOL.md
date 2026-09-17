# GN3 research protocol

This file governs live mathematical search during and after migration. Canonical proof-writing rules remain in `ARCHITECTURE.md`; the current mathematical target is summarized in `RESEARCH_STATE.md`; the mutable hierarchy of active approaches is `RESEARCH_TREE.md`.

## What counts as progress

Research progress is not the production of an artifact. A step counts as progress when it does at least one of the following:

- improves a plausible proof of the theorem;
- proves, sharpens, or removes a load-bearing gap in that proof;
- replaces local machinery by a simpler structural principle;
- discovers a reusable theorem that materially changes the search;
- identifies a genuine obstruction, necessary missing hypothesis, or counterexample that changes the structural picture.

A correct side lemma that does none of these may still be useful scratchwork, but it is not automatically theorem progress.

## Null results are legitimate

A researcher may return, without manufacturing filler:

- **no proof found**;
- **no theorem progress found**;
- **the attempted construction did not resolve the stated gap**.

Do not finish irrelevant easy branches, introduce unnecessary terminology, or create narrow lemmas merely to avoid a null result.

## Classify failure accurately

When a route stalls, distinguish:

1. **counterexample or impossibility** — the proposed statement/mechanism is false;
2. **necessary missing hypothesis** — the statement can only plausibly survive after adding a concrete condition;
3. **specific structural obstruction** — a precise configuration or invariant blocks the proposed realization;
4. **no proof found** — the search failed, but the abstraction has not been defeated.

Only the first three justify abandoning or materially revising the abstraction. “No proof found” does not.

## Director default

The ordinary strategic question is:

> What is the earliest statement in the shortest currently favored proof that we cannot justify?

That statement is the default target. The Director should keep the proof-level reason for the target visible and continually reassess whether new work changes the favored route.

This is a default, not a monopoly. Bounded exploration of genuinely different abstractions is encouraged when it could bypass the gap, yield a stronger parent theorem, or reveal a simpler global picture.

Guidance is normally **team-wide** and should state the mathematical target and why it matters.

## Guidance waves and Slack reporting

Each Director research wave receives a tag `[G##]`, with the number increasing monotonically. The guidance root lives in `#gn3-guidance` and states the common target with enough mathematical motivation for researchers to understand why it matters.

Researchers working under that guidance post each discovery as a top-level message in `#gn3-research` prefixed by the same `[G##]`. **The root is statement-only:** it contains the exact mathematical assertion being reported, with only the hypotheses, notation, cases, formulas, and conclusion needed to state that assertion precisely. It is not a mini-proof or a mini-report.

All supporting material belongs in replies to the root: proofs, derivations, reasons, proof sketches, case analysis, computations, counterexamples, citations used as justification, qualifications, motivation, usefulness commentary, strategic interpretation, and discussion. In particular, a root should not contain sentences such as “this follows from/by/because ...”. The channel timeline should read as a compact index of mathematical statements; the thread is where the argument lives.

If several distinct assertions are discovered, use separate roots unless they naturally form one theorem statement. A precise obstruction or null result may itself be the root statement, but the evidence distinguishing an obstruction from “no proof found” belongs in the thread. Directors and Vice Directors should repair malformed roots by trimming them to the statement while preserving the supporting material in replies.

The tag is deliberately administrative. `[G##]` must not become mathematical notation, theorem identity, provenance inside canonical proofs, or a replacement for stating hypotheses and conclusions. Its purpose is retrieval: after the wave, the Director or Vice Director can collect the responses to exactly that guidance without reconstructing the burst from chronology.

A null return need not manufacture a headline theorem. If useful, a researcher may post a `[G##]` root stating the precise obstruction or that no proof was found, with enough detail in the thread to distinguish those outcomes.

## Researcher default

Before committing to detailed construction, a researcher should be able to state internally:

- the ordinary mathematical structure being studied;
- the coarse mechanism or global picture being tested;
- what concrete construction would accomplish if successful.

Then work at increasing resolution: begin with the coarse structural requirement and refine only the parts whose realization matters. Continue until the abstraction becomes a literal proof/construction or until a specific obstruction is identified.

Do not elaborate an abstraction merely because some easy branches remain. Stop developing it when it is genuinely defeated and no credible repair preserves its purpose. If the only outcome is “no proof found,” record that honestly instead.

## Search state versus canonical mathematics

Scratch research may use temporary names, gadgets, computations, case trees, heuristic pictures, and unaudited results. Useful concurrent work may be consumed optimistically during search unless it has been explicitly failed, invalidated, quarantined, or superseded.

Canonical GN3 mathematics is different. It inherits only exact statements and proofs that survive compression and the certification policy in `ARCHITECTURE.md`. Repeated downstream use does not certify a result.

`RESEARCH_TREE.md` sits between these layers. It is synthesized working state: more organized than Slack scratch, but neither certified mathematics nor a durable theorem inventory. It may record compact audit status for exact live facts when that helps distinguish trusted support from optimistic support.

## Search progress versus proof progress

Exploration can be valuable without advancing the proof. Before reporting **proof progress**, ask whether the work:

- strengthens or simplifies the currently justified argument;
- resolves or sharpens its earliest governing gap;
- supplies a reusable structural result that changes the route; or
- materially changes the global proof abstraction.

If not, report it as search information, not proof closure.

## Continuous Director/Vice Director synthesis

Synthesis is continuous, not merely an end-of-wave cleanup. The Vice Director should repeatedly restore a top-down view from theorem to unresolved bridge to candidate mechanism to concrete subproblem, because incoming research will naturally skew local and constructive.

For every substantive recent finding, deliberately test the statement as written, natural strengthened forms, and useful weakened forms at the **earliest place in the proof spine where they can apply**. A discovery should not be evaluated only inside the branch that produced it. If a weaker form already closes an earlier obligation, prefer the simpler requirement; if a useful stronger form collapses several obligations and has a real proof, pursue it as new mathematics.

At the same time, inspect mathematics being relied on by the active strategy that is not already in the audited proof spine or an audited toolkit module. Decide whether it has become load-bearing. Load-bearing extra-spine mathematics must be routed to independent audit promptly; optimistic use may continue during research, but the favored route should not silently accumulate unaudited dependencies. A passed exact result may be recorded at its natural node in `RESEARCH_TREE.md`, and the Vice Director then decides whether it should be canonized into the proof spine or toolkit.

The Vice Director updates `RESEARCH_TREE.md` during the cycle whenever the abstraction changes, not only after a wave. Guidance must have an identifiable place in the tree. Before issuing or materially revising guidance, determine which node or closely related cluster of nodes it attacks and why that is the right next descent from the theorem-level objective. If guidance no longer matches the best abstraction, revise the tree and guidance together.

## Research-tree synthesis

The Director or a delegated Vice Director acts as the **compressor**. Only one compressor should own a given synthesis pass.

The compressor reads the relevant `[G##]` roots and proof threads, then updates `RESEARCH_TREE.md` according to what the mathematics changed in the live picture. This is synthesis, not transcription:

- merge equivalent or overlapping discoveries;
- replace several local facts by a supported stronger abstraction when appropriate;
- preserve precise blockers and necessary hypotheses;
- split a node only when the mathematics genuinely branches;
- delete dead routes and redundant local steps;
- place current guidance in the hierarchy rather than treating it as a free-floating task;
- do not create a node merely because a result was proved or audited.

Researchers normally do not edit the tree directly. They communicate discoveries, corrections, and structural suggestions in `#gn3-research`; the Director or delegated Vice Director performs the low-concurrency rewrite.

The tree should remain aggressively mutable. Its purpose is to show **what the current search looks like from the top down**, not to preserve credit, chronology, or every true intermediate statement.

## Compression cycle

The ordinary cycle is:

**top-down tree review → team-wide guidance → tagged research burst → continuous Director/Vice Director synthesis and audit triage → research-tree rewrite → next guidance.**

From there, stronger compression happens when mathematics earns a durable role:

1. proof-carrying mathematics enters the canonical sequential proof spine after exact audit;
2. independently reusable mathematics enters the small toolkit after exact audit;
3. the compact research-state file records the big picture and governing frontier;
4. unusually valuable negative knowledge or provenance is retained only when it prevents future reconstruction of a known bad route.

Temporary search structure does not become permanent startup context merely because it was useful during discovery. The active research tree is startup context only because it represents the current live search; obsolete branches should be removed rather than accumulated.