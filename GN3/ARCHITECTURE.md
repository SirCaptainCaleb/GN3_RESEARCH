# GN3 Architecture

**Status: CANONICAL.**

## Mandatory startup

After only the access, authentication, repository-location, and tool-discovery actions necessary to retrieve this file, every GN3 worker must fetch and read **one complete, internally consistent revision of this entire file** before synchronizing Slack, making mathematical inferences, editing project state, or doing research. Search excerpts, selected ranges, summaries, memory, and prior initialization do not count. If retrieval truncates or paginates, continue until the complete revision has been obtained.

GitHub is the sole durable GN3 architecture authority. Slack is a live communication and search surface. No Canvas is required for GN3 startup.

After the complete architecture read, an ordinary research worker reads `GN3/STATUS.md` and `GN3/RESEARCH_STATE.md` before choosing a target. A worker proving or auditing a statement then reads the relevant exact mathematics in `GN3/PROOF_SPINE/TWO_TIGHT_PATHS.md` and any explicitly cited canonical input. Legacy A7C3 material is pulled only when provenance or archaeology is actually needed.

## Governing principle

**Discovery may be expansive; canonical mathematics must be compressive. Search expansively. Think abstractly. Construct at increasing resolution. Admit failure early. Canonize conservatively. Rewrite compressively.**

Scratchwork may use temporary names, case trees, constructions, computations, and exploratory organization. Canonical GN3 state should inherit only mathematics and operating structure that survives deliberate compression.

## Namespace and legacy boundary

Canonical mathematics belongs under `GN3/`. The existing `A7C3/` tree, A7C3 Slack channels, and A7C3-era Canvases are legacy history, provenance, and archaeology. Do not mutate them into GN3 canon. Make only narrowly necessary archival corrections.

Provenance is kept thin and outside mathematical exposition. Migration evidence under `GN3/MIGRATION/` is archaeology, not startup context or architecture authority.

## Live Slack surfaces

The intentionally small active GN3 channel set is:

- `#gn3-changelog` (`C0C1VMME8MV`): high-signal project deltas, architecture changes, certification-impact changes, and major research-state changes.
- `#gn3-research` (`C0C2ENRLHE0`): expansive mathematical research, proof construction, discussion, and temporary structures.
- `#gn3-audit` (`C0C2D179WSV`): independent skeptical verification and certification work on exact proposed GN3 mathematics.

The pre-existing renamed `#gn3-lab` is transitional legacy and is not a canonical GN3 surface.

Do not mechanically recreate the A7C3 channel taxonomy. Add another GN3 channel only when a recurring operational need cannot be served cleanly by these three.

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
- Researchers reason abstraction-first and construct at increasing resolution: state the coarse mathematical mechanism, then refine only what is needed to realize it literally.
- Stop elaborating an abstraction when it is genuinely defeated, not merely when one search attempt fails.
- Scratch research may consume unaudited work optimistically; canonization remains conservative and exact-text based.
- Distinguish search progress from proof progress. Scratch structure is periodically compressed back into the proof spine, live research state, selected toolkit, or valuable negative-knowledge/provenance evidence.

No role has a quota for named results, lemmas, Engines, or nonempty returns.

## Canonical mathematical representation

The canonical proof spine is the single sequential document `GN3/PROOF_SPINE/TWO_TIGHT_PATHS.md`. Fresh researchers understand the theorem through that mathematics, not through an Engine dependency graph. The current exact proof/audit status is in `GN3/STATUS.md`; the compact big-picture route and earliest open bridge are in `GN3/RESEARCH_STATE.md`.

The proof spine may contain explicit open statements, but unresolved implications must remain visibly unproved. At the current coordinate the audited argument ends at Proposition 6.2 and the augmentation statement that follows is open.

Engine-like organization is secondary and optional. If a future Engine label is useful for a bounded Slack investigation, it does not create a mathematical ontology or canonical dependency node. A coherent reusable mechanism may become a theorem or section; a one-use argument stays where it is clearest.

Reusable mathematics is selected by factorization rather than historical logging. `GN3/TOOLKIT/README.md` indexes the deliberately small reusable shelf; proof-local lemmas remain in the spine rather than being duplicated into another graph.

## Working-state compression

Slack research may contain temporary terminology, case trees, gadgets, computations, exploratory constructions, and provisional results. Ordinary inheritance is compressed: useful work should return to the sequential proof, the compact research state, the small reusable toolkit, or provenance/negative-knowledge evidence. Temporary search structure does not become mandatory startup context merely because it once helped discovery.

## Compactness and maintenance

This file must remain small enough that full-file reading is routine. Keep proofs, catalogs, transcripts, detailed archaeology, volatile research state, and migration evidence elsewhere. When architecture grows, compress it rather than teaching workers to read excerpts.

Reconstruct or recompress the proof architecture when conceptual sprawl or a major discovery makes doing so mathematically useful. Do not optimize lemma count, Engine count, file length, or compression ratio as ends in themselves; the criterion is improved comprehension and research effectiveness.

## End of complete architecture

A startup read is complete only after reaching this line in the same fetched revision that supplied the beginning of the file.
