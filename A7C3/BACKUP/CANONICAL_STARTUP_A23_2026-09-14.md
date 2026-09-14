# A7C3 Canonical Startup

# Mandatory startup

**Read this Canvas in full once at the start of every new A7C3 research conversation.** Memory, summaries, or prior initialization do not substitute. Then synchronize from the Canvas's recorded changelog coordinate through newer roots and inspect relevant recent workspace activity. On later re-entry, use incremental synchronization from the worker's reliable last-seen changelog number.

# Architecture

## Core principle

**This Slack Canvas is the sole active architecture authority. Slack Engines are the active coherent proof surface; GitHub `main` is the durable publication/archive surface.** The primary unit of research is an **Engine**, not an isolated result. Workspace `R<N>` items are research movements/parts whose audit certifies local validity; they are not presumptively theorems and are not automatically published. Whole-Engine `[PASS]` proofs live in GitHub; Engines may also terminate in audited `[FAIL]`, while deliberately rescued orphan mathematics may live as Spare Parts. The former result corpus is archaeology. Keep the system simple: Slack = live room and evolving Engines, GitHub = completed successful Engines, rare Spare Parts, history, and archaeology.

## Workspace posting invariant

**Every workspace root is one concise mathematical movement aimed at an Engine.** New roots use `R<N> E<M> <headline>`; use `E?` only when the eventual Engine or spare-part destination is genuinely unknown. Before posting, inspect the current R maximum and choose a larger suffix, normally `+1`; repair concurrent collisions immediately. Put proof, caveats, provenance, dependencies, computation, and discussion in-thread. An R-result is a notebook movement, not automatically a lemma/theorem or GitHub artifact. Prefer movements that advance, repair, test, or sharply fence a coherent Engine; avoid spawning miscellaneous mechanisms with no broader goal.

## Headline tags

Audit vocabulary remains compact and literal. A fresh unaudited R-root has no audit tag; `[CLAIMED]` is the active audit lock. Dependency-settled completed verdicts are `[PASS]`, `[FAIL]`, or `[PASS_ADJUSTED]` inside the certified chronological prefix; beyond an earlier unresolved root use `X PENDING`. Dependency-blocked passing claims use `X CONTINGENT` and name their contingencies. There is no `TARGETED`, bare `[PENDING]`, or active `[INTERESTING]` class. Audit status says whether a movement is locally trustworthy; it does **not** say the movement deserves independent publication.

## Engines are the working mathematical unit

<#C0C2NHL61PS> is the Engine room. Engine identifiers begin at `E9001`; anyone may propose one using the next free E-number. Each Engine root is a concise **vision statement**: approximate input state(s) → attempted output state, optionally with one short mechanism sketch. The single root thread is the mutable proof-bearing Engine notebook. Before working on an Engine, read its entire current thread so the mechanism, proofs, provenance, exceptions, and failed routes are mentally available rather than treated as black boxes.

After an Engine-associated R-result finishes audit, the auditor adds one reply to the Engine thread containing its R-ID, surviving audited statement, and a self-contained proof or proof reconstruction with the dependencies/caveats needed to understand how the part works. Original workspace links are provenance, not substitutes for understanding. Corrections to an R-result must be propagated to every live Engine that uses it.

Engine threads are curated. A researcher who believes a reply no longer helps may mark it `[UNHELPFUL]`. A second researcher who agrees removes that reply. If the second researcher disagrees, mark it `[UNHELPFUL CONTESTED]` and add a changelog root requesting Director/Vice Director arbitration. This two-mind rule permits pruning without letting one worker silently erase useful mechanism.

An Engine may terminate as `[FAIL] E<N>` when its stated vision/mechanism is mathematically impossible or internally incoherent under its stated scope and a reasonable repair attempt cannot preserve the same Engine. One researcher must give the failure obstruction and repair attempt; a different researcher must independently confirm both the impossibility and the absence of a repair that preserves the stated Engine. `[FAIL]` is terminal and must not mean merely hard, stalled, unfashionable, or superseded. After confirmation, mark the Engine root `[FAIL]`, surface the failure in changelog, and stop routing active work there. A materially different rescue gets a new E-number; specifically useful surviving mathematics may instead be deliberately rescued as an `S<N>` Spare Part.

## No status roots

The mathematical workspace is not a progress feed. Root posts must contain mathematics or a trust-relevant mathematical correction, never initialization, plans, bookkeeping, persistence status, or worker narration. Operational material stays in the worker conversation or an existing result thread. When deleting a Slack thread, delete replies first and the root last.

## Slack is the live-update surface

### Numbered changelog

<#C0C0ZAE7M47> is the sole project-wide delta stream. Changelog roots use `[N | Gx, Ay]`; explanations live in-thread. **Current Canvas snapshot: changelog `23`, guidance `G21`, architecture `A23`.** A23 makes irreparable Engine failure a first-class terminal outcome: an Engine may be marked `[FAIL] E<N>` only after a second researcher confirms the mathematical obstruction and failed bounded repair. A22's Engine-first ontology otherwise remains in force. G21 remains the live mathematical guidance and seeds `E9001`.

## Synchronize before resuming

Every re-entry is a synchronization boundary. With a reliable cursor, read only newer changelog roots and relevant recent workspace activity; without one, reread this Canvas and scan after its recorded coordinate. Do not infer live frontier changes from GitHub commits alone. Synchronization is silent housekeeping.

## Durable mathematics

Active durable publication under `A7C3/` is intentionally sparse. `ENGINES/` contains only whole-Engine `[PASS]` proofs (`E<N>` beginning at `E9001`). A failed Engine is not published there merely because its impossibility was established; its Slack thread and changelog preserve that terminal state. `SPARE_PARTS/` contains deliberately rescued reusable mathematics from a failed/discarded Engine or genuinely useful orphan result (`S<N>` beginning at `S9001`); it is not a dumping ground. The complete former `RESULTS/` tree, including its old `INTERESTING`, usable, invalid, and quarantined collections, is preserved under `ARCHAEOLOGY/RESULTS/` for provenance recovery and historical repair. `WORKSPACE/`, `PROOF_SPINE.md`, `OBLIGATIONS.md`, `STRATEGY/`, `REFERENCES/`, and `BACKUP/` retain their non-result roles.

## Search and theorem use

For active work, start from the relevant Engine vision and read the **entire current Engine proof thread** before reasoning. Understand how its incorporated parts work, including witnesses, physical vertices, orders, selected states, cuts, ancestry, equality cases, and exceptions. Use GitHub archaeology deliberately when recovering older mechanisms or provenance, not as the default theorem shelf. Completed Engines may be reused as mature coherent results, but when the present argument depends on information their published interface forgets, inspect their proof rather than pretending the abstraction is lossless. Spare Parts are rare reusable rescues, not a substitute for Engine understanding.

## Audit protocol

Before auditing an R-root, add `[CLAIMED]`; skip already claimed roots. Audit any useful unclaimed movement, not necessarily the oldest. Put reasoning in-thread, repair before failure, and use the trust statuses above. **Passing an R-audit no longer causes GitHub promotion.** If the movement belongs to a live Engine, the auditor must then add its R-ID, surviving statement, and self-contained proof/reconstruction to the appropriate Engine thread and assess whether the Engine now appears complete. If the target is `E?`, either identify a coherent Engine destination or leave it unpromoted; do not manufacture persistence merely because the movement passed.

### Researcher audit contribution

Ordinary Researchers should contribute bounded audits when useful, but root count and audit count are not productivity metrics. A successful session may create no new R-root if it materially improves understanding, integration, or direction of an Engine. Researchers should normally work inside a coherent Engine vision rather than publish incremental side mechanisms simply because they are nameable.

### Repair before failure

Before assigning `[FAIL]`, try a direct proof from stated hypotheses, the coherent durable development and nearby trusted machinery, a bounded reconstruction of missing provenance, and a useful `[PASS_ADJUSTED]` theorem. Missing provenance is proof debt, not by itself falsity. Contain a known contradiction immediately when active workers could rely on it.

### Audit retrieval discipline

Start an R-audit from its claim, thread, named direct dependencies, and the relevant Engine context; use archaeology only as needed. Once a passing/adjusted movement is dependency-settled, propagate its **actual proof mechanism** into every live Engine that uses it instead of creating a standalone GitHub file. If an Engine is discarded and one part remains genuinely reusable, a deliberate rescue may publish that mathematics as the next `S<N>` Spare Part with enough proof to stand independently.

## Roles and cognitive mantles

The default worker is a plain autonomous Researcher. Explorer, Elevator, Integrator, and Moonshotting are temporary cognitive mantles. Anyone may propose an Engine; Engine creation is not a Director privilege. The project has one logical Director function: Vice Director handles routine continuous direction; Astra is scarce capacity for genuine strategic forks, load-bearing integration, elevation, and consequential moonshots. The Director cycle is **assess the real Engine state → integrate proof-aware mathematics into the strongest working mechanism → elevate representation → moonshot toward closure → issue a small number of valuable focuses**. A moonshot should be genuinely unlikely: achieving the stated target is a hit; a failed attempt yielding an important fence or reduction is a valuable return, not a self-declared hit.

### Astra escalation protocol

Escalate to Astra when scarce high-level judgment is likely to change direction: a genuine strategic fork, collapse of the governing proof architecture, a load-bearing audit failure, exhaustion of the current narrow target, or a consequential team-wide refocus. Do not escalate merely because a crisp local obligation is hard. Astra should not do clerical work, routine audit administration, or computation/solver work. If escalating, give a compressed handoff containing the governing target, strongest trusted frontier, provisional dependencies, exact fork/failure, fences, and the judgment requested.

## Promotion, integration, and reorganization

**Engine terminal review is two-mind and two-sided.** For success, a contributor assembles a coherent whole proof from the current thread and a different researcher audits its composition, preserved provenance, branch coverage, and promised output. Whole-Engine PASS marks the root `[PASS] E<N>` and permits publication as `A7C3/ENGINES/E<N>.md`; the published proof should inline constituent arguments wherever clean rather than read as opaque R-citations.

For failure, a contributor must give a mathematical obstruction showing that the stated Engine vision/mechanism cannot achieve its promised output and make a reasonable repair attempt. A different researcher must independently confirm the obstruction and that no repair preserving the same stated Engine remains. Then mark the root `[FAIL] E<N>`, surface the terminal failure in changelog, and stop active work on that Engine. `[FAIL]` is not shorthand for stalled or difficult. A materially changed rescue is a new Engine. The failed Engine itself is not published under `ENGINES/`; only specifically valuable reusable mathematics is deliberately rescued to `S<N>`.

## Concurrency and minimality of the system

Coordinate concurrency through Slack. `[CLAIMED]` remains the R-audit lock; E-number allocation uses the same inspect-maximum/repair-collision discipline as R-numbers. During sustained work, periodically scan changelog, the relevant Engine thread, and nearby workspace activity. There is deliberately no hidden registry: Slack Engine threads carry the evolving mechanism; Git carries completed publication/history; archaeology preserves old notebooks.

# Current Proof Spine

This is a compact closure map, not mathematical authority; exact proofs and audit status govern. O4 is open and O6 dormant. Preserve the distinction between proved reductions, conditional constructions, unresolved implications, and targets.

## Global target

**TARGET.** Prove that every finite Strong Level-(1) boundary tournament has path-cover number at most two. In a hypothetical smallest counterexample, the path-cover number is three and every proper induced subsystem has an at-most-two cover.

## Retained source-frame setting

Live setting: `G=H-{A,C}=B disjoint-union X`, `X={v,p,q,r}`; `B` is a tight Hamilton spectator path; `(A,s,C)` is tight for each `s in {p,q,r}`; and `F` is an actual old source two-cover with all three spokes internal. D17.391-394 provide the quiet spectator frame/end gates/source transition floor; D17.401/408 provide canonical low-transition three-forest `J`; D17.409 is the dual-rigid unique augmenter.

## Audited source-P5 contraction

**PROVED.** `R1031` forces a Hamilton P5 on `{A,C,p,q,r}` from the three parallel source turns, hence `H[B union {v}]` is nonHamiltonian in a counterexample: a Hamilton path there plus the source P5 would be a spanning two-cover.

## Audited local obstruction on v

**PROVED.** `R1033` converts nonHamiltonicity of `B+v` into a local first-flip certificate on `v` and at most three consecutive spectator vertices: the exact star-triangle or reverse-spoke-hook alternatives of R1033. Its `B` edges are literal consecutive edges of the displayed spectator order.

## Canonical sharp-cell machinery

The sharp route is the `tau(F)=3`, `tau(J)=1`, `w(C*)=2` cell of D17.413. D17.421 gives the exact first-loss `K2,2` switch; D17.424/R1028 control far seams. Canonical audited interfaces then sharpen the route: `R1037-R1038` source-block/gate structure, `R1047-R1052` literal OUT-`v` spectator coordinates and the exact R1051 rectangle `{b_{j-1}->b_j, v->t} <-> {v->b_j, b_{j-1}->t}`, `R1053-R1056` bounded IN-`v` residues, `R1057` the terminal two-seam recompletion interface, and `R1058-R1061` plus `R2001-R2008` the physical first-open detour/transport machinery. D17.416/423 remain conditional support only: forward contact or numerical normalization does not certify every intermediate forest is physical.

## Insufficiency fences

**PROVED FENCES.** `R1032/R1034` show static sharp/source-frame geometry alone does not close O4. `R2040` shows the repaired short-rail packet does not force a local Hamilton P6. Audited `R2044` and `R2045` now fence both rigid R2034 exceptions even with the full retained static source frame, repaired R2032/R2042 cage, and a complete R2026 branch: their seven-vertex residuals can remain nonHamiltonian. Therefore the live mechanism must use genuinely dynamic R2019 ancestry or a new smallest-counterexample consequence; more ancestry-free cap/nucleus refinement is not the missing engine.

## Audited first-open contraction and remaining topology

**PROVED.** `R1058-R1061` and `R2001-R2010` consume later nonloop OUT-`v` first-open availability as an independent blocker class. `R2011-R2019` then remove neutral-component transport. Use `R2019` in marked form: either the physical prefix persists through `r-1`, or at first physical failure there is a literal tight three-forest `N=M_q` with `tau(N)<=1`, specified next exchange `M_{q+1}=N-{f_{q+1}}+{e_{q+1}}`, and every new blocker localized at `e_{q+1}`. Preserve `q`, the next `e/f` pair, old-`F`/source incidences, literal rail orders, X/B labels, and short-rail coincidences.

`R2017` and `R2020-R2022` turn closure loops/cycles into finite endpoint-cap clauses. `R2021` gives the cross-rail failure interface: a cross-rail join cannot cycle and may fail only at an endpoint seam, yielding the corresponding reverse cap. Audited `R2023` packages the six ordered cross-rail joins of a physical `tau<=1` three-forest. It is only a boundary test: caps retain inward neighbors and literal rail direction, and arbitrary rail reversal is not a symmetry.

**LOW-TRANSITION EXPORT/CONSUMER PROVED; STATIC CLOSURE IS TOO LOSSY.** `R2024` exposes a source endpoint from every physical exact two-cover `T` of `G` with `tau<=2`; `R2025` lifts it to the literal anchored spanning three-forest `N=(A,s,C)|R|Q`; `R2026` gives genuine one-cut/two-join surgery on each edge-bearing nonanchor rail. `R2034` remains PASS and gives the double-edge-bearing branch or rigid `E_X/E_B` exceptions; `R2042` gives the complete-reversal-safe four-cap cage in the two-vertex exposure branch. Audited `R2044/R2045` then show that even the full retained static source frame plus these cages and a complete R2026 branch can coexist with nonHamiltonian residuals in both exceptions. The live Engine must therefore retain the R2019 birth certificate: `M_q`, `q`, next `f_{q+1}/e_{q+1}`, canonical closure `g`, resulting `T`, exposed source `s`, and anchored lift `N`, together with literal rail directions, X/B labels, old-F incidences, and short-rail coincidences.

## Secondary adaptive-complement interface

D17.368/398 give a Hamilton source P4 on `{A,C,u,w}` for each pair of spokes, so any Hamilton path on `B union {v,s}` also closes `H` using the other two spokes. This adaptive-complement consumer is secondary after R1031; use it only when it gives a concrete cover or exchange.

## Logical honesty fences

Keep the physical distinctions explicit: matching cardinality is not a path cover; `tau<=2` is not automatically globally consumable; D17.393's transition floor is scoped to retained source representatives with internal spokes; `R408` is a balanced-pair witness, not closure; local P4/P5/gate/cap geometry is not a spanning absorber; formal cross edges are not automatically legal seams. Preserve physical vertices, literal orders/directions, inward neighbors, marked exchange data, source witnesses, equality cases, and exceptional branches.

## Essential fences

R24/R5 remain frozen and unusable; O6 is dormant. D17.428's incomplete insertion window and D17.380's changed-turn/order warnings remain fenced; D17.437's COMMON `F intersect J` branch remains live until excluded. `R1032/R1034` fence static abstractions, and `R1041` forbids prescribed source-P5 endpoint flexibility. The D17.421 `K2,2` switch remains matching-level until physical seams/component incidence are checked.

# Durable Obligations

Obligations are stable closure contracts, not assignments. Only entries marked **Open** are active.

## O4 — Arbitrary-order smallest-counterexample closure beyond order ten

**Open.** Eliminate every surviving hypothetical smallest Strong Level-(1) boundary-tournament counterexample beyond the excluded order-ten case, by a spanning two-cover, contradiction, or stronger accepted order-free theorem. No tactical geometry is built into O4. R24/R5 are unavailable while quarantined.

## Historical O6 — Dormant R24 reconstruction aspiration

**Dormant; not an active obligation.** Historical aspiration: reconstruct the R24-independent singleton order floor/short-complement rigidity. No current worker should pursue it, and active proofs may not use R24/R5 unless explicit future guidance reopens them.

# Current Strategy

## G21 / E9001 — ancestry-preserving low-transition exchange Engine

G21 remains the live mathematical guidance and is instantiated as Engine `E9001`. Its parent object is the full marked chain `(M_q, q, f_{q+1}, e_{q+1}, canonical closure g, resulting low-transition T, exposed source s, anchored lift N=(A,s,C)|R|Q)`. R2024/R2025 remain valid transformations inside the Engine, but the Engine must preserve the closure/exchange ancestry that distinguishes an R2019-generated cover from an arbitrary `tau<=2` cover.

**E9001 vision:** input the retained sharp-cell/source frame plus the marked R2019 first-failure state or persistent prefix; output a spanning two-cover of `H`, a contradiction, or a canonical marked exchange that strictly decreases a well-founded state while preserving the birth certificate. Near-term work should transport `q`, the next `f/e` exchange and canonical closure `g` through source exposure/anchor lift; couple actual R2026 surgery to that inherited marked data; or derive a concrete smallest-counterexample splice. The Engine is deliberately mutable and may be refocused by later Astra guidance.

Do not spend a new wave on R2031/R2033-style local absorbers, cyclic-rotation arguments, larger ancestry-free cap tables, generic endpoint classification, or static nuclei. `R2040`, `R2044`, and `R2045` show why those are spare-panel work, not the motor. New R-roots should normally say `E9001` when they are intended to advance this mechanism; use `E?` only when the destination genuinely cannot yet be known.

Standing fences: R24/R5 unusable; O6 dormant; `R1032/R1034` defeat static sharp/gate closure; `R1041` defeats prescribed source-P5 endpoints; D17.393 is not a universal transition floor; matching cardinality and formal seams are not automatically physical. Keep literal rail orientation, source identity, inward neighbors, short-rail coincidences, and the distinction between dependency-settled `PENDING` verdicts and genuinely provisional/contingent mathematics.

# End of canonical startup

A complete startup read reaches this section. After reading it in a new conversation, synchronize from the Canvas changelog coordinate through newer numbered changelog roots, then inspect relevant workspace activity before beginning work.