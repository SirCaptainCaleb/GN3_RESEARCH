# GN3 research protocol

This file governs live mathematical search during and after migration. Canonical proof-writing rules remain in `ARCHITECTURE.md`; the current mathematical target is summarized in `RESEARCH_STATE.md`.

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

## Search progress versus proof progress

Exploration can be valuable without advancing the proof. Before reporting **proof progress**, ask whether the work:

- strengthens or simplifies the currently justified argument;
- resolves or sharpens its earliest governing gap;
- supplies a reusable structural result that changes the route; or
- materially changes the global proof abstraction.

If not, report it as search information, not proof closure.

## Compression cycle

Slack and scratchwork may be expansive. Periodically compress what survived into one of four places only:

1. the canonical sequential proof spine;
2. the compact research-state description of the live gap;
3. the small reusable toolkit;
4. provenance or negative-knowledge evidence when it prevents future reconstruction of a known bad route.

Temporary search structure does not become required startup context merely because it was useful during discovery.
