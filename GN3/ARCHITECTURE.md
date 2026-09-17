# GN3 Architecture

**Status: CANONICAL.**

## Mandatory startup

After only the access, authentication, repository-location, and tool-discovery actions necessary to retrieve this file, every GN3 worker must fetch and read **one complete, internally consistent revision of this entire file** before synchronizing Slack, making mathematical inferences, editing project state, or doing research. Search excerpts, selected ranges, summaries, memory, and prior initialization do not count. If retrieval truncates or paginates, continue until the complete revision has been obtained.

GitHub is the sole durable GN3 architecture authority. Slack is a live communication and search surface. No Canvas is required for GN3 startup.

After the complete architecture read, an ordinary research worker reads `GN3/STATUS.md`, `GN3/RESEARCH_STATE.md`, the current `GN3/RESEARCH_TREE.md`, and the complete reusable toolkit: `GN3/TOOLKIT/README.md` together with every standalone toolkit module it currently indexes. The toolkit is startup mathematical context, not optional archaeology. A worker proving or auditing a statement then reads the relevant exact mathematics in `GN3/PROOF_SPINE/TWO_TIGHT_PATHS.md` and any explicitly cited canonical input. Legacy A7C3 material is pulled only when provenance or archaeology is actually needed.

## Governing principle

**Discovery may be expansive; canonical mathematics must be compressive. Search expansively. Think abstractly. Construct at increasing resolution. Admit failure early. Canonize conservatively. Rewrite compressively.**

Scratchwork may use temporary names, case trees, constructions, computations, and exploratory organization. Canonical GN3 state should inherit only mathematics and operating structure that survives deliberate compression.

## Mathematical language in all communication

The prohibition on proof-meta language is not merely a publication-style rule. It applies to **all mathematical communication in GN3**: Slack research posts and replies, Director guidance, audit discussion, research-tree text, synthesis notes, and canonical proofs.

Whenever the mathematical object or assertion can be named directly, name it directly. Speak about paths, covers, endpoints, triples, orders, intersections, deletions, inequalities, obstructions, and implications rather than replacing them with proof-role descriptions such as “the downstream object”, “the closure witness”, “the output of the previous result”, “the active mechanism”, “the state carried by the branch”, or similar language whose meaning depends on knowing the history of the proof.

Workflow metadata is allowed where it is actually workflow metadata—for example `[G##]`, `[PASS]`, audit status, a request to inspect the earliest open statement, or a note that a branch is obsolete. But workflow language must not substitute for the mathematics itself. A researcher should be able to read a mathematical claim in Slack or in the research tree and understand what it says without reconstructing which proof step produced each object.

This matters especially during research. Meta-language that feels harmless in scratch communication tends to become hidden ontology: later workers reuse a phrase whose mathematical content was never fixed, different branches silently attach different meanings to it, and the ambiguity eventually leaks into the proof. Prefer slightly longer explicit mathematics over a compact proof-history phrase. Temporary terminology is acceptable only when it names a mathematically defined object or condition rather than its role in the argument.

Directors, Vice Directors, auditors, and researchers should actively rewrite meta descriptions into ordinary mathematical language when synthesizing results. The research tree should preserve the best current **mathematical abstraction**, not the vocabulary of the route by which it was discovered.

## Namespace and legacy boundary

Canonical mathematics belongs under `GN3/`. The existing `A7C3/` tree, A7C3 Slack channels, and A7C3-era Canvases are legacy history, provenance, and archaeology. Do not mutate them into GN3 canon. Make only narrowly necessary archival corrections.

Provenance is kept thin and outside mathematical exposition. Migration evidence under `GN3/MIGRATION/` is archaeology, not startup context or architecture authority.

## Live Slack surfaces

The intentionally small active GN3 channel set is:

- `#gn3-changelog` (`C0C1VMME8MV`): high-signal project deltas, architecture changes, certification-impact changes, and major research-state changes.
- `#gn3-guidance` (`C0C2ET66370`): Director/Vice Director team-wide research guidance waves and material guidance revisions. Each `[G##]` guidance root lives here.
- `#gn3-research` (`C0C2ENRLHE0`): expansive mathematical research, proof construction, discussion, and temporary structures responding to current or recent guidance.
- `#gn3-audit` (`C0C2D179WSV`): independent skeptical verification and certification work on exact proposed GN3 mathematics.

The pre-existing renamed `#gn3-lab` is transitional legacy and is not a canonical GN3 surface.

Do not mechanically recreate the A7C3 channel taxonomy. Add another GN3 channel only when a recurring operational need cannot be served cleanly by these four.

### Research-root discipline

A top-level message in `#gn3-research` is an **index entry for one mathematical result**, not a container for its argument. Every `[G##]` research root must contain only the guidance tag and the exact mathematical statement being reported. The statement may include whatever hypotheses, notation, cases, displayed formulas, or conclusion are necessary to make the claim precise and self-contained.

**No proof or explanatory prose belongs in a research root.** In particular, do not put derivations, reasons, proof sketches, case analysis, computations, citations used as reasons, motivation, usefulness commentary, strategic interpretation, qualifications about how the claim was obtained, or sentences such as “this follows because/from/by ...” in the top-level message. Put all of that in one or more replies to the root. A precise obstruction or null result may itself be the root statement, but the evidence and analysis supporting it still belong in the thread.

If several distinct mathematical assertions are discovered, use separate roots unless they naturally form one theorem statement. Directors and Vice Directors should repair malformed research roots when they notice them: preserve the exact statement at top level and move or retain all argument, explanation, and discussion in the thread. The root timeline should therefore read like a compact list of mathematical statements; opening a thread reveals the work behind each statement.

## Authority and mathematical status

GitHub placement does not by itself certify a theorem. Exact status must remain visible. During research, unaudited mathematics may be consumed optimistically unless explicitly failed, invalidated, quarantined, or superseded; canonical certification remains conservative and attaches only to the exact statement/proof independently checked.

A substantive rewrite is new mathematical text for certification purposes. Old A7C3 PASS status is provenance, not automatic certification of a GN3 rewrite. Editorial inheritance is allowed only after an auditor confirms that the mathematics is unchanged.

`GN3/STATUS.md` records the exact audited proof coordinate and the open mathematical frontier. Status metadata belongs outside proof exposition.

## Global proof-coding policy

The proof-writing standards enforced in `GN3/PROOF_SPINE/` are **project-wide mandatory coding rules for all canonical GN3 mathematics**, not local style preferences.

- Canonical mathematics must be written in natural mathematical prose, but natural language may not carry hidden semantics. The target style is simultaneously human-readable, unambiguous, precise, and **mathematically compilable**.
- Mathematical compilability means that every nonstandard object is defined before use; every symbol and variable has a determined meaning and domain; every operation has mathematically specified inputs and outputs; notation has stable scope; and every proof step can be interpreted without guessing an omitted type, invariant, transition, or change of meaning.
- **Definitions are ontological first.** A definition must first say what kind of mathematical object is being defined and then state its distinguishing conditions. Prefer forms such as “An `X` is a `Y` such that ...” or “Define `X` to be ...”. Do not substitute sentences such as “`X` begins with ...”, “`X` records ...”, “`X` has ...”, or “`X` permits ...” for the underlying definition.
- **Definitions must be intrinsic.** The identity of an object, operation, relation, or admissible move must be determined from the mathematical objects named in the definition itself. Never define something as “the output of Lemma X”, “the object produced above”, “the restriction from Theorem Y”, or by any other proof-history description. Such descriptions create hidden frames.
- Theorem and lemma numbers may be cited inside proofs as reasons that an intrinsically stated fact holds. They must not supply the meaning of a definition, operation, relation, hypothesis, or conclusion. If a later statement needs a property established earlier, state the mathematical property itself and use the earlier result only in the proof.
- Operations and functions must be defined by their domain, required hypotheses, and mathematical output. Relations must be defined by intrinsic conditions on their arguments. It is acceptable to define a relation by saying `Pi -> Pi'` exactly when `Pi'=f(Pi)`, `g(Pi)`, or `h(Pi)`, provided `f,g,h` have already been intrinsically defined. It is not acceptable to define relation membership by saying that one of several lemmas or theorem constructions was applied.
- A technical term such as “continuation” is permitted only when it denotes a precisely defined mathematical object, operation, or relation. The prose meaning of the word may not carry additional reachability, provenance, or persistence assumptions beyond that definition.
- Prefer standard mathematical objects and notation. Introduce a new term only when it names a recurring mathematical object more clearly than standard language. Any such term must have one complete structural definition. Do not introduce vocabulary merely to encode where an object sits in a proof or how it was discovered.
- Prefer the exact mathematical noun over meta-nouns. In canonical proof prose, avoid vague substitutes such as “data”, “state”, “current”, “active”, “physical”, “graph-theoretic”, “certificate”, “credit”, or similar workflow-flavored labels when the intended referent is actually a path, cover, ordering, orientation, witness, intersection condition, inequality, or other explicit mathematical object or property. If such a word is genuinely needed as a technical term, define it precisely first.
- Pseudo-formal notation is not a substitute for a definition. If notation denotes concatenation, deletion, restriction, inheritance, comparison, continuation, or another operation, define that operation and its domain before relying on the notation.
- State exact mathematical hypotheses and exact conclusions. Do not rely on remembered context, implicit phase, result numbers, theorem-output provenance, or an unnamed earlier construction to supply missing assumptions.
- **No hidden provenance.** An object is not mathematically distinguished merely because it arose earlier in the proof. If a later argument reuses a particular path, cover, pair, witness, or ordering, explicitly quantify it or fix and name it together with every property needed later.
- Every transition, replacement, deletion, shortening, continuation, inheritance step, or reuse of an earlier object must be mathematically defined and lawful. An arbitrary sequence of configurations is not a proof of reachability. In particular, a subpath obtained by deleting vertices is not thereby a later member of a structured construction unless an intrinsically stated operation places it there.
- Retaining a true fact about an earlier object is different from producing a new object in a later construction. Never use retained intersection, restriction, cut, or endpoint information to manufacture reachability. If re-formation is required, state and prove the operation that performs it.
- Preserve every mathematical feature actually needed downstream—orientation, endpoint choice, witness, disjointness, maximality, exact order, recurrence condition, and scope. Simplification may remove proof-history scaffolding, but it may not erase mathematically load-bearing structure or hide complexity behind a weaker informal description.
- **Actively test for straightforward strengthening.** Canonicalization should not fossilize a weaker legacy statement merely because that was the certified historical form. When a natural stronger statement appears plausible, try the obvious argument. If it follows by a short or moderate proof and is useful, prefer the stronger theorem. New arguments are allowed and encouraged when they simplify or strengthen the spine without opening a disproportionate research detour.
- A strengthening obtained by a new argument is new mathematics for certification purposes. It does not inherit an older audit merely because the weaker theorem was certified. Mark or treat the stronger statement as requiring fresh independent audit before claiming certification.
- Do not “simplify” by inventing a stronger abstraction that merely hides unresolved work. A stronger formulation must have an actual proof at the stated strength. If proving it begins to require a substantial new research program, record the stronger claim as a research target and keep the strongest proved statement in the canonical spine.
- Finite case checks and exceptional configurations must be fully checkable from the canonical text: give the conceptual argument, explicit cases/table, or a precisely stated earlier lemma. “One checks” is not acceptable at a load-bearing step.
- When two arguments share a weaker natural parent lemma, factor that parent rather than duplicating stronger hypotheses. Inline one-use machinery; extract only statements that improve reuse, clarity, or proof topology.
- Prefer ordinary graph-theoretic and combinatorial objects, but avoid meta phrases such as “graph-theoretic data” or “graph-theoretic state” inside proofs. Nonstandard terminology is permitted only when it compresses a recurring mathematical object and has one precise definition. Do not encode proof position, audit history, or historical workflow as mathematical ontology.
- Canonical proofs must be sequentially readable and self-contained up to explicitly named canonical inputs. Provenance, audit history, Engine/R numbers, discovery transcript, migration vocabulary, and obsolete machinery belong outside the mathematical exposition.
- Unresolved implications must be stated as gaps or research targets, never disguised as continuations, heuristics, bookkeeping ranks, inherited status, or theorem-output objects.

Auditors and integrators must enforce these rules globally. A mathematically plausible argument that violates them is not ready for canonical GN3 status even if its intended legacy source was previously accepted.

## Research method

GN3 optimizes proof progress, not artifact production. `GN3/RESEARCH_PROTOCOL.md` gives the expanded working rules; the durable principles are:

- A useful research step improves a plausible proof, sharpens or removes a load-bearing gap, simplifies the structural picture, supplies a genuinely reusable principle, or identifies a concrete obstruction. Merely producing a valid lemma is not enough.
- Truthful null returns are first-class: “no proof found” and “no theorem progress found” are legitimate outcomes.
- A stalled route must be classified as counterexample/impossibility, necessary missing hypothesis, specific structural obstruction, or no proof found. Failure to find a proof does not refute an abstraction.
- The Director default is the earliest unjustified statement in the shortest presently favored proof, while bounded alternative abstractions remain welcome when they could bypass the gap or simplify the global picture.
- Director guidance states the current mathematical target and why it matters.
- Each Director research wave receives a guidance tag `[G##]`. The guidance post is a top-level message in `#gn3-guidance` and states the common target. A researcher responding to that wave posts each exact discovery statement as a top-level `#gn3-research` message prefixed by the same `[G##]`; **the root contains the statement only**, while every proof, derivation, qualification, computation, explanation, and discussion belongs in replies to that root. This tag is a retrieval device, not mathematical notation or permanent theorem identity.
- Researchers reason abstraction-first and construct at increasing resolution: state the coarse mathematical mechanism, then refine only what is needed to realize it literally.
- Stop elaborating an abstraction when it is genuinely defeated, not merely when one search attempt fails.
- Scratch research may consume unaudited work optimistically; canonization remains conservative and exact-text based.
- Distinguish search progress from proof progress. A burst of local results is raw research material, not a theorem inventory. After a guidance wave, the Director or a delegated Vice Director synthesizes the tagged responses, identifies what changed in the mathematical picture, and compresses that information into the active research structure.

No role has a quota for named results, lemmas, Engines, or nonempty returns.

## Director cycle and abstraction management

The Vice Director runs a continuous Director cycle around and between research waves. A wave is one instrument inside this cycle, not a batch that must finish before direction can change. The purpose of the cycle is deliberately top-down: local constructive work is abundant, so the Vice Director must repeatedly rebuild the global abstraction, determine what the proof actually depends on, and choose guidance by descending from the theorem-level objective to the most useful unresolved node rather than merely continuing the newest local construction.

1. **Synchronize the whole live picture.** Read the current proof spine, toolkit, audit status, research tree, current guidance, and relevant new research. Treat the research tree as an object that must be actively maintained during the cycle, not merely rewritten after a wave ends.
2. **Re-test every substantive recent finding at the earliest possible proof coordinate.** For each finding, test the statement as written and also deliberately test natural strengthened and useful weakened forms. Ask at the earliest place in the proof spine where the relevant hypotheses can hold whether any such form proves, strengthens, simplifies, bypasses, or invalidates an existing step. A downstream discovery may close an upstream branch; a stronger form may collapse several obligations; a weaker form may already be sufficient and substantially easier to certify or reuse. Do not evaluate a result only inside the local branch that produced it.
3. **Audit-triage all extra-spine mathematics by load-bearingness.** Inspect mathematics currently being relied on in research, guidance, or the research tree that is not already contained in the audited proof spine or an audited toolkit module. Decide whether each such fact has become load-bearing for the favored route or an important live alternative. If it has, route its exact statement and proof to independent audit promptly. Optimistic use during research is allowed, but the active strategy must not silently accumulate unaudited load-bearing dependencies.
4. **Integrate audited load-bearing results into the abstraction.** When an independently audited result passes, record the mathematical fact at the natural node of `GN3/RESEARCH_TREE.md` when it remains part of the live abstraction, with a compact indication that the exact result has passed audit. Then decide whether it should also be compressed into the proof spine at the earliest natural location or into the toolkit if it is genuinely reusable. The research tree may record that a live supporting fact is audited, but it does not itself confer certification.
5. **Re-evaluate the shortest favored route from the top down.** Starting from the theorem and the earliest unresolved proof step, ask which branches are now closed, subsumed, contradicted, bypassed, or unnecessarily strong. Stop spending research effort on obsolete branches and remove or compress them in the research tree.
6. **Rewrite the research tree during the cycle.** Maintain `GN3/RESEARCH_TREE.md` as the best current hierarchy of theorem-level objective → unresolved bridge → candidate mechanism → concrete subproblem. Merge overlapping discoveries, promote a supported parent abstraction when it explains several local facts, split only where the mathematics genuinely branches, preserve concrete blockers, and delete dead structure aggressively. The tree should make the global proof strategy legible even when most incoming research is local and constructive.
7. **Place guidance explicitly in the tree before or while issuing it.** Determine which live tree node the next guidance wave is meant to attack and why that node is the right next descent from the theorem-level objective. If current guidance no longer matches the best tree, revise the tree and guidance rather than preserving momentum for its own sake. Guidance should normally be understandable as a focused attack on one node or one clearly related cluster of nodes in the current abstraction.
8. **Issue or revise team-wide guidance in `#gn3-guidance`.** State the common target and enough mathematical context to show its place in the current proof strategy. Do not preserve an old target merely because a wave was already launched.
9. **Canonize only after exact certification.** When load-bearing mathematics has passed independent audit, compress it into the proof spine or toolkit when that improves the durable mathematical representation. A passed local fact need not be canonized if the research tree is the right temporary home, but every durable proof dependency eventually belongs in audited canonical mathematics rather than remaining only in Slack or the tree.
10. **Escalate to Astra when the abstraction itself needs to change.** Escalate when progress appears to require a strategic reframe, stronger parent theorem, global bypass, major invariant change, or substantial architecture decision rather than ordinary local direction.

Then repeat. The cycle is not merely a scheduler for local work. Its central job is to keep the proof organized from the top down, continuously test whether recent mathematics changes the earliest part of the proof, and prevent the favored route from depending invisibly on unaudited intermediate results.

## Active research tree

`GN3/RESEARCH_TREE.md` is the current hierarchical model of the **live search**, not canonical mathematics and not an archive of discoveries. It exists to retain enough intermediate structure for difficult arguments to cohere before the final proof topology is known, and to counterbalance the natural tendency of research to become local and constructive by continually restoring a theorem-to-subproblem view.

The tree is organized from the top down by mathematical objectives, unresolved obligations, candidate mechanisms, and concrete subproblems. Nodes should have semantic names. They are not result IDs, theorem IDs, or permanent objects. A node may contain a compact argument sketch, a synthesized observation, a blocker, or children representing genuine mathematical decomposition or competing routes. Current Director guidance should have an identifiable place in this hierarchy; if it does not, the Vice Director should either revise the tree or reconsider the guidance.

Individual research discoveries normally do **not** become nodes merely because they were proved or audited. During a `[G##]` wave, researchers post discoveries in Slack. The Vice Director continuously integrates the mathematics that changes the live abstraction, and after a wave performs any additional compression needed. Several discoveries may collapse into one sentence or one node; a failed branch may be deleted entirely; a stronger abstraction may replace a whole subtree. A passed audit result may be recorded at the node it supports when that result is still load-bearing for the live search.

Only the Director or a delegated Vice Director normally edits `GN3/RESEARCH_TREE.md`. For any synthesis pass, one such worker should act as the compressor so that researchers never need to coordinate concurrent edits to the tree. Researchers communicate corrections or proposed structural changes through `#gn3-research` rather than racing direct tree edits.

The tree has a low admission bar during synthesis but a high retention bar. Keep a branch only while it represents a live unresolved subproblem, a genuinely competitive route, or a local fact still needed by a live route. Once an argument solidifies, compress its surviving mathematics into the proof spine or selected toolkit; once a route dies, remove it from the active tree unless a concise negative lesson is worth preserving elsewhere.

The tree may be aggressively renamed, merged, moved, shortened, or deleted. Git history provides recovery if an apparently dead branch later matters. The tree must not accumulate serial result logs, audit transcripts, proof-history ontology, or mandatory context that no longer helps the active search. Compact audit labels for exact live facts are allowed when they help distinguish trusted support from optimistic support; detailed audit history stays outside the tree.

## Canonical mathematical representation

The canonical proof spine is the single sequential document `GN3/PROOF_SPINE/TWO_TIGHT_PATHS.md`. Fresh researchers understand the theorem through that mathematics, not through an Engine dependency graph. The current exact proof/audit status is in `GN3/STATUS.md`; the compact big-picture route and earliest open bridge are in `GN3/RESEARCH_STATE.md`.

The proof spine may contain explicit open statements, but unresolved implications must remain visibly unproved. At the current coordinate the audited argument ends at Proposition 6.2 and the augmentation statement that follows is open.

Engine-like organization is not canonical. The active research tree supplies the useful temporary function once served by Engines—organizing uncertain intermediate work before the final argument is known—without turning those structures into permanent proof ontology. A coherent reusable mechanism may become a theorem or section; a one-use argument stays where it is clearest.

Reusable mathematics is selected by factorization rather than historical logging. `GN3/TOOLKIT/README.md` indexes the deliberately small reusable shelf; proof-local lemmas remain in the spine rather than being duplicated into another graph.

## Working-state compression

The ordinary research cycle is:

**team-wide guidance in `#gn3-guidance` → tagged research burst in `#gn3-research` → Director/Vice Director synthesis → research-tree rewrite → next guidance.**

Slack guidance is the low-noise direction stream; Slack research is the high-concurrency discovery stream. `GN3/RESEARCH_TREE.md` is the low-concurrency synthesized model of the current search. `GN3/PROOF_SPINE/TWO_TIGHT_PATHS.md` is the canonical active proof. `GN3/TOOLKIT/README.md` indexes independently reusable mathematics.

Compression from Slack into the tree is **not copying**. The compressor should remove duplication, merge equivalent discoveries, state the strongest useful abstraction actually supported, retain concrete obstructions, and discard local noise. Compression from the tree into the proof spine or toolkit is stricter still: only mathematics that has earned a durable role survives.

Slack research may contain temporary terminology, case trees, gadgets, computations, exploratory constructions, and provisional results. Temporary search structure does not become mandatory permanent context merely because it once helped discovery.

## Compactness and maintenance

This file must remain small enough that full-file reading is routine. Keep proofs, catalogs, transcripts, detailed archaeology, volatile research detail, and migration evidence elsewhere. When architecture grows, compress it rather than teaching workers to read excerpts.

Reconstruct or recompress the proof architecture when conceptual sprawl or a major discovery makes doing so mathematically useful. Reorganize the active research tree whenever its hierarchy stops reflecting the best current abstraction. Do not optimize lemma count, Engine count, node count, file length, or compression ratio as ends in themselves; the criterion is improved comprehension and research effectiveness.

## End of complete architecture

A startup read is complete only after reaching this line in the same fetched revision that supplied the beginning of the file.