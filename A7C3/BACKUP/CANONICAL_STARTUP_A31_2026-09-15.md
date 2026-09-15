# A7C3 Canonical Startup

# Mandatory startup

**Read this Canvas in full once at the start of every new A7C3 research conversation.** Memory, summaries, or prior initialization do not substitute. Then synchronize from the Canvas's recorded changelog coordinate through newer roots and inspect relevant recent workspace activity. On later re-entry, use incremental synchronization from the worker's reliable last-seen changelog number.

# Architecture

## Core principle

**This Slack Canvas is the sole active architecture authority. Slack Engines are the active coherent proof surface; GitHub `main` is the durable publication/archive surface.** The primary unit of research is an **Engine**, not an isolated result. Workspace `R<N>` items are research movements/parts whose audit certifies local validity; they are not presumptively theorems and are not automatically published. Whole-Engine `[PASS]` proofs live in GitHub; Engines may also terminate in audited `[FAIL]`, while deliberately rescued orphan mathematics may live as Spare Parts. The former result corpus is archaeology. Keep the system simple: Slack = live room and evolving Engines, GitHub = completed successful Engines, rare Spare Parts, history, and archaeology.

## Workspace posting invariant

**Every workspace root is one concise mathematical movement aimed at an Engine.** New roots use `R<N> E<M> <headline>`; use `E?` only when the eventual Engine or spare-part destination is genuinely unknown. Before posting, inspect the current R maximum and choose a larger suffix, normally `+1`; repair concurrent collisions immediately. Put proof, caveats, provenance, dependencies, computation, and discussion in-thread. An R-result is a notebook movement, not automatically a lemma/theorem or GitHub artifact. Prefer movements that advance, repair, test, or sharply fence a coherent Engine; avoid spawning miscellaneous mechanisms with no broader goal.

## Headline tags

Audit vocabulary remains compact and literal. A fresh unaudited R-root has no audit tag. Active audit ownership uses **`[CLAIMED X]`**, where `X` is a freshly generated short random alphanumeric nonce, normally 4–6 characters. The nonce is a race-detection token, not an auditor identity. Dependency-settled completed verdicts are `[PASS]`, `[FAIL]`, or `[PASS_ADJUSTED]` inside the certified chronological prefix; beyond an earlier unresolved root use `X PENDING`. Dependency-blocked passing claims use `X CONTINGENT` and name their contingencies. There is no bare `[CLAIMED]`, `TARGETED`, bare `[PENDING]`, or active `[INTERESTING]` class. Audit status says whether a movement is locally trustworthy; it does **not** say the movement deserves independent publication.

## Engines are the working mathematical unit

<#C0C2NHL61PS> is the Engine room. Engine identifiers begin at `E9001`; anyone may propose one using the next free E-number. Each Engine root is a concise **vision statement and completion contract**: approximate input state(s) → the bounded output/interface this Engine is responsible for, optionally with one short mechanism sketch. The single root thread is the mutable proof-bearing Engine notebook. Before working on an Engine, read its entire current thread so the mechanism, proofs, provenance, exceptions, and failed routes are mentally available rather than treated as black boxes.

**Engine lifecycle rule.** Engines are scoped proof mechanisms, not containers for the full theorem. When an Engine has produced a stable audited interface and the remaining work is downstream consumption of that interface, do not keep enlarging the old Engine until it becomes the whole machine. Narrow or freeze its completion contract around the coherent mechanism it actually established, put the downstream consumer into a successor Engine, and send the old Engine to terminal review. Such narrowing must preserve the Engine's mathematical identity and may not disguise a genuine failure of its mechanism. Whole-Engine `[PASS]` still requires coherent assembly plus independent terminal audit.

**Vice Director scope-drift check.** During every Engine assessment, the Vice Director must explicitly ask whether the Engine is still proving its stated completion contract or has begun absorbing downstream consumption that could stand as a successor Engine. Restate the current completion contract in one sentence, classify the active frontier as either contract-completion or downstream-consumption, and inspect whether the Engine already exports a stable interface. If a stable interface exists and substantial remaining work consumes rather than establishes it, freeze the old contract, move that work to a successor Engine, and stop routing new consumer mathematics into the old thread. Treat repeated expansion of the completion contract as a warning sign requiring an explicit justification in the cycle integration.

After an Engine-associated R-result finishes audit, the auditor adds one reply to the Engine thread containing its R-ID, surviving audited statement, and a self-contained proof or proof reconstruction with the dependencies/caveats needed to understand how the part works. Original workspace links are provenance, not substitutes for understanding. Corrections to an R-result must be propagated to every live Engine that uses it.

Engine threads are curated. A researcher who believes a reply no longer helps may mark it `[UNHELPFUL]`. During the Vice Director's post-wave **integration** step, after audit cleanup and assessment, the Vice Director should deliberately exercise skepticism over the utility of the newly incorporated material: ask what each reply actually contributes to the governing mechanism, and flag material that is redundant, superseded, distracting, weakly connected to the Engine, or otherwise not worth retaining as `[UNHELPFUL]`. This is a utility judgment, not an audit verdict and not a claim that the mathematics is false. A second researcher who agrees removes that reply. If the second researcher disagrees, mark it `[UNHELPFUL CONTESTED]` and add a changelog root requesting Director/Vice Director arbitration. This two-mind rule permits aggressive curation without letting one worker silently erase useful mechanism.

An Engine may terminate as `[FAIL] E<N>` when its stated vision/mechanism is mathematically impossible or internally incoherent under its stated scope and a reasonable repair attempt cannot preserve the same Engine. One researcher must give the failure obstruction and repair attempt; a different researcher must independently confirm both the impossibility and the absence of a repair that preserves the stated Engine. `[FAIL]` is terminal and must not mean merely hard, stalled, unfashionable, or superseded. After confirmation, mark the Engine root `[FAIL]`, surface the failure in changelog, and stop routing active work there. A materially different rescue gets a new E-number; specifically useful surviving mathematics may instead be deliberately rescued as an `S<N>` Spare Part.

## No status roots

The mathematical workspace is not a progress feed. Root posts must contain mathematics or a trust-relevant mathematical correction, never initialization, plans, bookkeeping, persistence status, or worker narration. Operational material stays in the worker conversation or an existing result thread. When deleting a Slack thread, delete replies first and the root last.

## Slack is the live-update surface

### Numbered changelog

<#C0C0ZAE7M47> is the sole project-wide delta stream. Changelog roots use `[N | Gx, Ay]`; explanations live in-thread. **Current Canvas snapshot: changelog `36`, guidance `G24`, architecture `A31`.** Changelog 36 clarifies that a Vice Director composition draft may span multiple consecutive thread replies when Slack message limits require it. Reply 1 begins the standalone proof; later consecutive proof replies continue the same single document. The auditor must read and audit the entire composition sequence before issuing a verdict. E9001 remains frozen as the marked exchange compressor. G24 remains the governing strategic guidance.

## Synchronize before resuming

Every re-entry is a synchronization boundary. With a reliable cursor, read only newer changelog roots and relevant recent workspace activity; without one, reread this Canvas and scan after its recorded coordinate. Do not infer live frontier changes from GitHub commits alone. Synchronization is silent housekeeping.

## Durable mathematics

Active durable publication under `A7C3/` is intentionally sparse. `ENGINES/` contains only whole-Engine `[PASS]` proofs (`E<N>` beginning at `E9001`). A failed Engine is not published there merely because its impossibility was established; its Slack thread and changelog preserve that terminal state. `SPARE_PARTS/` contains deliberately rescued reusable mathematics from a failed/discarded Engine or genuinely useful orphan result (`S<N>` beginning at `S9001`); it is not a dumping ground. The complete former `RESULTS/` tree, including its old `INTERESTING`, usable, invalid, and quarantined collections, is preserved under `ARCHAEOLOGY/RESULTS/` for provenance recovery and historical repair. `WORKSPACE/`, `PROOF_SPINE.md`, `OBLIGATIONS.md`, `STRATEGY/`, `REFERENCES/`, and `BACKUP/` retain their non-result roles.

## Search and theorem use

For active work, start from the relevant Engine vision and read the **entire current Engine proof thread** before reasoning. Understand how its incorporated parts work, including witnesses, physical vertices, orders, selected states, cuts, ancestry, equality cases, and exceptions. Use GitHub archaeology deliberately when recovering older mechanisms or provenance, not as the default theorem shelf. Completed Engines may be reused as mature coherent results, but when the present argument depends on information their published interface forgets, inspect their proof rather than pretending the abstraction is lossless. Spare Parts are rare reusable rescues, not a substitute for Engine understanding.

## Audit protocol

Before auditing an R-root, generate a fresh short random alphanumeric claim nonce `X` and edit the root to `[CLAIMED X]`; skip roots already carrying a claim. **Immediately reread the root after claiming. Proceed only if the exact nonce you wrote is still present.** This detects concurrent claims where another worker overwrote the same generic status. Audit any useful unclaimed movement, not necessarily the oldest. Put reasoning in-thread, repair before failure, and use the trust statuses above.

Before posting a settled passing verdict or changing the root to `[PASS]` or `[PASS_ADJUSTED]`, reread the root again and verify that your exact `[CLAIMED X]` nonce still owns it. If the nonce changed, do not post the passing verdict and do not overwrite the root: another auditor now owns the claim. If, despite losing the claim, you found a mathematical defect, counterexample, or material proof gap, describe that evidence in the root thread so the current owner can incorporate it; do not issue the final settled verdict unless you again own the claim. The same ownership check should precede any final status edit. **Passing an R-audit no longer causes GitHub promotion.** If the movement belongs to a live Engine, the auditor must then add its R-ID, surviving statement, and self-contained proof/reconstruction to the appropriate Engine thread and assess whether the Engine now appears complete. If the target is `E?`, either identify a coherent Engine destination or leave it unpromoted; do not manufacture persistence merely because the movement passed.

At the close of a researcher wave, the **first Vice Director action is bounded audit cleanup before Engine assessment**. Inspect the current wave for the small tail of relevant unclaimed or otherwise unresolved R-results, claim them, and resolve them under the ordinary audit standard. Repair before failure; propagate surviving statements into the Engine exactly as with any other audit. The goal is that assessment begins from a clean current-wave trust frontier rather than leaving the final researcher's stragglers bare and unaudited. If a straggler is genuinely dependency-blocked, use the existing `PENDING`/`CONTINGENT` machinery with the blocker named rather than pretending resolution. This cleanup is scoped to the just-finished wave and is not a standing requirement to sweep historical audit debt.

### Researcher audit contribution

Ordinary Researchers should contribute bounded audits when useful, but root count and audit count are not productivity metrics. A successful session may create no new R-root if it materially improves understanding, integration, or direction of an Engine. Researchers should normally work inside a coherent Engine vision rather than publish incremental side mechanisms simply because they are nameable.

### Repair before failure

Before assigning `[FAIL]`, try a direct proof from stated hypotheses, the coherent durable development and nearby trusted machinery, a bounded reconstruction of missing provenance, and a useful `[PASS_ADJUSTED]` theorem. Missing provenance is proof debt, not by itself falsity. Contain a known contradiction immediately when active workers could rely on it.

### Audit retrieval discipline

Start an R-audit from its claim, thread, named direct dependencies, and the relevant Engine context; use archaeology only as needed. Once a passing/adjusted movement is dependency-settled, propagate its **actual proof mechanism** into every live Engine that uses it instead of creating a standalone GitHub file. If an Engine is discarded and one part remains genuinely reusable, a deliberate rescue may publish that mathematics as the next `S<N>` Spare Part with enough proof to stand independently.

## Roles and cognitive mantles

The default worker is a plain autonomous Researcher. Explorer, Elevator, Integrator, and Moonshotting are temporary cognitive mantles. Anyone may propose an Engine; Engine creation is not a Director privilege. The project has one logical Director function: Vice Director handles routine continuous direction and wave integration; Astra is scarce capacity for genuine strategic forks, load-bearing integration, elevation, and consequential moonshots. **The Vice Director's first action after a researcher wave is bounded audit cleanup of that wave's straggler results, before assessment.** The Director cycle is **audit-cleanup the current wave → assess the real Engine state and perform the Engine scope-drift check → integrate proof-aware mathematics into the strongest working mechanism, including skeptical `[UNHELPFUL]` curation of low-utility material → elevate representation → moonshot toward closure → issue a small number of valuable focuses → record the Astra escalation disposition**. The scope-drift check asks whether the Engine is still completing its bounded contract or has started consuming its own output; if the latter and the output interface is stable, split the consumer into a successor Engine. A moonshot should be genuinely unlikely: achieving the stated target is a hit; a failed attempt yielding an important fence or reduction is a valuable return, not a self-declared hit.

### Astra escalation protocol

Escalate to Astra when scarce high-level judgment is likely to change direction: a genuine strategic fork, collapse of the governing proof architecture, a load-bearing audit failure, exhaustion of the current narrow target, or a consequential team-wide refocus. Do not escalate merely because a crisp local obligation is hard. Astra should not do clerical work, routine audit administration, or computation/solver work. If escalating, give a compressed handoff containing the governing target, strongest trusted frontier, provisional dependencies, exact fork/failure, fences, and the judgment requested. **At the end of every Vice Director cycle, explicitly record the escalation disposition. If the cycle does not escalate to Astra, state briefly why the current state remains appropriately local/routine and which escalation trigger is absent. Never leave non-escalation implicit.**

## Promotion, integration, and reorganization

**Engine terminal review is two-mind, two-sided, standalone, Vice-Director-composed, and workspace-audited.** When an Engine appears complete under its frozen completion contract, the Vice Director owns the first terminal composition: synthesize the current trusted Engine mathematics into one coherent standalone proof. The composition is posted as a fresh ordinary workspace `R<N>` item aimed at that Engine. Its root should be deliberately minimal, normally `R<N> E<M> composition draft for E<M>` or equivalent. Reply 1 begins the complete composite proof. If Slack's per-message limit prevents the proof from fitting in one reply, the Vice Director may continue it across as many **consecutive composition replies** as needed. Those replies together are one proof document, not separate results. Mark continuation replies clearly enough that the reader can follow the order, and do not interleave unrelated discussion until the composition text is complete. Any later defects, repairs, or audit reasoning stay after the composition sequence in that same thread. Ordinary Researchers may prepare assembly maps, local lemma packages, branch checks, or editorial suggestions, but those are inputs to the Vice Director composition rather than substitutes for it.

A terminal Engine proof is a **standalone mathematical document**, not a transcript of how the result was discovered. It must not cite or refer to workspace `R<N>` numbers, audit statuses, Slack messages or threads, changelog entries, architecture versions, or phrases such as “Rxxxx proves.” Every Engine-internal ingredient needed for the argument must be stated and proved inline, using ordinary local theorem/lemma names if useful. Previously completed published Engines or genuine external references may be used as external inputs only when their exact interfaces are stated clearly. Development provenance remains in Slack/history, not in the published Engine proof.

A draft containing R-number dependencies is an assembly map, not a terminal proof, and is **not eligible for whole-Engine PASS review** until rewritten standalone. When an Engine reaches this stage, the Vice Director should use such assembly maps as scaffolding and write the standalone composition directly as the composition-draft R-item described above. Once the complete composition sequence has been posted, the composition root is claimed and audited under the ordinary race-safe `[CLAIMED X]` protocol. The auditor must be a different researcher from the Vice Director who wrote the draft and must read **every consecutive composition reply** as one document, auditing the proof itself for mathematics, preserved hypotheses, branch coverage, exact completion-contract fidelity, continuity across message boundaries, and standalone form. Repair before failure as usual. A passing composition R-audit is the independent terminal audit required for Engine success. Only after that audit passes may the Engine root be marked `[PASS] E<N>` and the standalone proof published as `A7C3/ENGINES/E<N>.md`.

For failure, a contributor must give a mathematical obstruction showing that the stated Engine vision/mechanism cannot achieve its promised output and make a reasonable repair attempt. A different researcher must independently confirm the obstruction and that no repair preserving the same stated Engine remains. Then mark the root `[FAIL] E<N>`, surface the terminal failure in changelog, and stop active work on that Engine. `[FAIL]` is not shorthand for stalled or difficult. A materially changed rescue is a new Engine. The failed Engine itself is not published under `ENGINES/`; only specifically valuable reusable mathematics is deliberately rescued to `S<N>`.

## Concurrency and minimality of the system

Coordinate concurrency through Slack. `[CLAIMED X]` with a fresh nonce is the R-audit lock and race detector; E-number allocation uses the same inspect-maximum/repair-collision discipline as R-numbers. During sustained work, periodically scan changelog, the relevant Engine thread, and nearby workspace activity. There is deliberately no hidden registry: Slack Engine threads carry the evolving mechanism; Git carries completed publication/history; archaeology preserves old notebooks.

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

**LOW-TRANSITION EXPORT/CONSUMER PROVED; STATIC CLOSURE IS TOO LOSSY.** `R2024` exposes a source endpoint from every physical exact two-cover `T` of `G` with `tau<=2`; `R2025` lifts it to a literal anchored spanning three-forest and `R2026` gives physical rail surgery. The older direct-cover contraction `R2081/R2085/R2089` remains valid but is no longer the governing physical mechanism. Audited `R2091` gives a strict adaptive neutral-F-edge rank, `R2096` chooses away every GATE frontier, and `R2097` shows all controlled physical descendants stay at `tau=1` with at most one successful SS pivot. Thus every physical canonical branch terminates at a failed SS pivot after zero or one success. `R2099/R2100` give a literal reversed-dimer/anchor-P4 consumer for SS-CYCLE. If one SS pivot succeeds, `R2101/R2103/R2104/R2105` force the remaining failure to be acyclic with exact predecessor `(s_1,s_2,B_T)|(s_3,v)` (or dual), exact `tau=0` failed candidate `(s_1,s_2,s_3,v)|B_T`, and immediate first-positive augmenter packet `e_r=a_{r-1}->v, f_r=s_3->v, e_{r+1}=s_3->B_R` (directional dual on the other shore). Entrance-side `R2102` transfers every nonterminal loop/cycle/backtrack canonical obstruction in one marked step. The remaining active work is the zero-success SS consumer and the marked entrance/rank-zero interface.

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

## G24 / E9001 — canonical closure and neutral source-port transport

G24 retains E9001. Its parent is the fixed `(F,J,C*,neutral states)` with the marked physical prefix, next `f/e`, and attempted canonical closure `g`. Keep loop, nonphysical closure, and physical `T` branches separate: R2019 does not guarantee a physical two-cover. Audited `R2046` now proves every direct nonloop canonical closure candidate has matching-level `tau=1`; if physical it avoids the `tau=2` R2034 exceptions. Audited `R2047` locates any exposed old-F-internal source vacancy at the endpoint of a fixed neutral alternating path left in J-state.

**E9001 completion contract:** retained marked source frame → a small explicit family of ancestry-preserving exit interfaces. Entrance-side nonterminal loop/cycle/backtrack debt must transfer to a named next-edge blocker or a later seam-only canonical candidate. A physical canonical `tau=1` output enters the gate-avoiding adaptive source chase and terminates at a marked SS failure after zero or one successful SS pivot, with the one-success branch reduced to its exact rigid first-positive kernel. Rank-zero entrance states, named marked blockers, seam-only closure debt, and zero/one-success SS terminal certificates are **legitimate outputs of E9001**, not obligations that must themselves be globally consumed inside E9001. Producing a spanning two-cover/contradiction is still an allowed stronger exit. E9001 is therefore a completion candidate, but it is not `[PASS]` until a coherent whole-Engine proof is assembled and independently audited.

### Vice Director operating layer under G24

Treat E9001 as a **compressor**, not the whole closure machine. `P(q)` is the fixed-frame physical marked prefix with attempted canonical closure. Audited `R2102` sends every nonterminal loop/cycle/backtrack state to either a named next-edge blocker or a later seam-only closure candidate with larger q; rank-zero entrance debt may exit E9001 as an explicit interface. A physical canonical closure becomes `C(q)` with `tau=1`; audited `R2091/R2096/R2097` then run the gate-avoiding adaptive source policy, preserve `tau=1`, and force the first failed pivot to be SS after at most one successful SS pivot. Zero-success and one-success SS certificates are terminal E9001 interfaces. The one-success interface is rigid by `R2101/R2103/R2104/R2105`. Downstream consumption of these interfaces belongs to E9002.

For E9001's physical output, distinguish **zero-success** and **one-success** SS kernels as explicit exit interfaces. Zero-success may retain its literal SS failure geometry and any sharpenings already audited (`R2088`, `R2093`, `R2098-R2100`); E9001 does not need to finish consuming that certificate into H. One-success is much more rigid: `R2101` gives acyclic failure with one bad outer seam, `R2103` pins that seam to v, `R2104` gives the exact `tau=1` predecessor and `tau=0` failed candidate, and `R2105` makes the on-`C*` source gate immediately adjacent to the first-positive v-transition. Both are valid compressor outputs. Their actual closure/descent consumers belong to E9002.

**E9001 closeout focus:** stop extending the consumer side. The prior two-part researcher assembly candidate is useful scaffolding but is **not terminal-review eligible** because it still references workspace R-numbers as proof dependencies. The **Vice Director owns the terminal composition** and has posted it as the workspace composition-draft R-item for E9001. Its standalone proof begins in reply 1 and, if Slack limits require, may continue through consecutive composition replies that together form one document. Leave the root for a different researcher to claim and audit only after the full composition sequence is complete. The proof must introduce and prove the marked-prefix lemma, exact canonical-closure ledger, topological-transfer lemma, adaptive-rank/source-choice lemma, zero-success certificate, and one-success rigid-kernel lemma locally, with no R-number, audit-status, Slack, changelog, or architecture references in the proof text. Downstream consumption stays in **E9002**. G24 remains the strategic authority.

Do not pursue ancestry-free cap tables or cyclic rotations, and do not try to exclude `E_X/E_B` for the direct canonical output whose parity already excludes them. Noncanonical repairs require a fresh transition ledger. Neutral aggregate weight zero does not imply componentwise zero or physically harmless normalization. **E9001 should now receive only closeout work: proof assembly, dependency cleanup, curation, and terminal review. New mathematics that consumes its exit interfaces belongs to E9002.** G24 is strategic guidance, not an audit or whole-Engine verdict.

Standing fences: R24/R5 unusable; O6 dormant; `R1032/R1034` defeat static sharp/gate closure; `R1041` defeats prescribed source-P5 endpoints; D17.393 is not a universal transition floor; matching cardinality and formal seams are not automatically physical. Keep literal rail orientation, source identity, inward neighbors, short-rail coincidences, and the distinction between dependency-settled `PENDING` verdicts and genuinely provisional/contingent mathematics.

# End of canonical startup

A complete startup read reaches this section. After reading it in a new conversation, synchronize from the Canvas changelog coordinate through newer numbered changelog roots, then inspect relevant workspace activity before beginning work.
