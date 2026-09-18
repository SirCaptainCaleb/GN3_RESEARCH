# 07 — GN3 communication and posting standard

**Status: CANONICAL.**

This file is the sole authority for the **shape, self-containment, placement, and repair of live GN3 communication**. Mathematical-language rules remain in `02_MATHEMATICAL_LANGUAGE.md`; the shared certification interface is in `04_AUDIT_PROTOCOL.md`; detailed Auditor operation is in `AUDITOR.md`; controlled terminology remains in `06_TERMINOLOGY.md`.

The purpose of this standard is to keep live communication mathematically compilable. A reader should not have to reconstruct neighboring Slack threads, discovery chronology, worker state, or project-specific metaphors in order to know what a mathematical post says.

## 1. Surface contracts

The four active Slack surfaces have different root-message contracts.

### `#gn3-research`

A top-level research message is one **standalone mathematical statement** prefixed by the current `[G##]` tag.

The root contains only:
- the minimum hypotheses and notation needed to state the result;
- the exact conclusion;
- mathematically necessary cases, formulas, or quantified alternatives.

The root does **not** contain:
- proof, derivation, motivation, strategic interpretation, usefulness claims, audit status, or discovery history;
- references such as “under the hypotheses of root …”, “in the preceding setup”, “keep the same frame”, or “as above”;
- an informal theorem nickname that substitutes for the statement;
- workflow language standing in for mathematical hypotheses.

If every reply and every neighboring Slack message vanished, the root must still be understandable as a theorem, lemma, proposition, counterexample, obstruction, or exact null statement.

Supporting material belongs in replies. The first substantive reply should normally contain the proof or derivation. Later replies may contain consequences, generalizations, failed extensions, computation, strategic interpretation, or discussion.

### `#gn3-guidance`

A guidance root states:
- the current mathematical target;
- the mathematical reason it is the right target;
- enough current structural context for a researcher to begin without reconstructing Director history.

Guidance may discuss strategy, unlike a research root. It must still name mathematical objects and assertions directly. Do not express strategy only through result IDs, branch nicknames, or proof-state metaphors.

### `#gn3-audit`

A top-level audit root is workflow metadata, not a theorem statement. It identifies a coherent audit batch and gives exact targets: Slack messages or repository revisions, mathematical scope, and the particular checks that matter.

Detailed verification, repairs, derivations, objections, author discussion, and final itemwise dispositions belong in the audit thread.

Audit roots must not ask the Auditor to reconstruct which text is meant from vague phrases such as “the latest version” when exact coordinates are available.

### `#gn3-changelog`

A changelog root states one durable project delta precisely enough for an already-initialized worker to act safely.

It should identify:
- what changed;
- the exact durable surface affected;
- the commit or exact revision when useful;
- whether existing workers can incorporate the stated delta directly or must reread a named document or section.

The changelog is not a research diary. Do not post ordinary discoveries, local proof attempts, or transient worker status there.

## 2. Standalone mathematical compilability

Every current mathematical statement, especially every `#gn3-research` root, must satisfy all of the following.

### Bind the ambient object

Declare the mathematical universe before using it.

Good:
`Let K be a boundary tournament with pc(K)>2 and V(K)=S⊔Y, where |S|=4.`

Bad:
`Let K=S⊔Y be in the outer-endpoint frame.`

When a letter denotes a vertex set, do not write as though it denotes the induced tournament. Use `H[X]`, `K[S]`, or explicitly say that a set induces a Hamiltonian boundary tournament.

### Bind every symbol before use

Every variable, set, path, cover, endpoint, index range, and auxiliary quantity must have a determined meaning and domain in the root itself.

In particular:
- define `n` before writing `n-4`;
- define the cover `T` before writing `T[S]`, `e_T`, or deleting vertices from `T`;
- define endpoint labels such as `L,u,v,R` rather than relying on a neighboring Hamilton order;
- state nonemptiness and cardinality hypotheses needed to make path slices or internal deletions meaningful.

A statement may use standard notation defined project-wide in the proof spine or toolkit, but local symbols must still be bound locally.

### Repeat mathematical hypotheses; do not inherit setups by provenance

A theorem may depend in its proof on an earlier result, but its **statement** must contain the hypotheses under which its conclusion is asserted.

Do not write:
- “under the hypotheses of root 1789…”
- “in the same-profile case”
- “keep the transition-minimal setup”
- “in the preceding frame”
- “for the actual endpoints”
- “the exchanged side again has the G07 conclusions”

Instead state the relevant mathematical conditions literally.

Proof replies may cite earlier certified or provisional theorems as dependencies. Citation is not a substitute for stating the theorem’s own hypotheses.

### Use intrinsic mathematical language

Apply `02_MATHEMATICAL_LANGUAGE.md` and `06_TERMINOLOGY.md` strictly.

Do not encode mathematics by:
- discovery chronology;
- proof role;
- worker state;
- branch names;
- result numbers;
- unregistered metaphors.

Write the set, path, partition, orientation, inequality, or deletion condition itself.

### Type set/tournament operations correctly

Be explicit about the object on which an operation acts.

Prefer:
- `V(K)=S⊔Y`;
- `K[S]` is non-Hamiltonian;
- `Y-d` for deleting a vertex from a set or path support;
- `K-d` for the induced boundary tournament after vertex deletion.

Avoid overloading one letter as both a tournament and its vertex set.

### State the exact strength proved

Do not smuggle stronger interpretation into descriptive prose.

If the proof establishes a dichotomy, state the dichotomy. If it establishes a result only under an order-preserving hypothesis, retain that hypothesis. If an index range requires `m≥5`, say so.

Do not use “equivalently”, “consequently”, or “in particular” unless the displayed consequence really follows at the stated level of generality.

## 3. Root/reply separation

A research root is an indexable exact assertion, not a mini-paper.

The following belong in replies:
- proofs and proof sketches;
- casework;
- explanations of why a definition was chosen;
- citations justifying an inference;
- computation and certificates;
- historical notes;
- strategic consequences;
- proposed strengthenings or weakenings not already included as part of the exact theorem;
- discussion of which earlier result the theorem subsumes.

When several independently useful mathematical conclusions emerge, prefer separate roots to a root that narrates a sequence of discoveries.

A root may be long when its **statement** is genuinely long. Length is not itself a defect. Hidden context is.

## 4. Proof replies

A proof reply may rely on named dependencies, but it must make the logical use of them explicit.

Preferred form:
- name the exact theorem or canonical file/section;
- state the conclusion taken from it in the symbols of the current root;
- continue the argument.

Avoid proof replies whose essential logic is only:
“root A gives root B, so root C applies.”

For provisional Slack dependencies, exact root timestamps may be included for retrieval, but the mathematical fact consumed should also be written.

If a proof uses a local claim that later becomes reusable, extract it as its own research root or utility candidate rather than leaving it permanently hidden in the reply.

## 5. Corrections, repairs, and retractions

### Shape-only or editorial repair

If a root violates the communication standard but its mathematics is unchanged, edit the root in place:
- bind omitted variables;
- replace provenance shorthand by literal hypotheses;
- remove proof/commentary from the root;
- replace forbidden terminology;
- correct set/tournament typing;
- expand a non-substantive “dual statement” when the exact dual is clear.

Move removed proof material into the thread when needed. Slack edit history is sufficient; do not preserve a malformed root merely as historical evidence.

### Local mathematical repair

If a localized mathematical correction is permitted by the audit protocol, the repaired exact statement must itself satisfy this communication standard. Record the repair in the relevant audit thread when certification is involved.

### Substantive change

Do not silently rewrite an audited theorem into materially different mathematics. Follow `04_AUDIT_PROTOCOL.md`: substantive Auditor-authored repairs require independent second audit, and any mathematically changed shelf/canonical revision must be audited as required by its destination.

### Retraction

A retraction root must be self-contained about the defect.

Good:
`RETRACTED. The proof reversed a tight path, but tight paths are not generally reversible.`

Bad:
`RETRACTED. Root 123 is invalid because root 456 was retracted.`

A historical message ID may be placed in a reply for retrieval, but the root must state the mathematical failure itself.

A later correction should normally be posted as the corrected mathematical theorem, not as a root-level memo saying “CORRECTION — the old theorem was actually valid.”

## 6. Concurrent editing and hygiene authority

Researchers are responsible for the shape of their own posts.

The Vice Director may make **shape-only, terminology-only, typing-only, or explicit-dependency-expansion edits** to live research roots when the mathematical assertion is unchanged and the repair is unambiguous.

An Auditor may make repairs according to `04_AUDIT_PROTOCOL.md`.

No one should use communication cleanup as a pretext for silently strengthening, weakening, or changing mathematics outside the repair rules above.

During long research waves, the Vice Director should periodically perform a communication-hygiene pass on newly load-bearing roots before they are used in guidance, shelf composition, or audit.

## 7. Pre-post compile check

Before posting a mathematical root, answer all of these affirmatively:

1. **Standalone:** Would the statement still make sense if every neighboring Slack message and every reply were deleted?
2. **Ambient object:** Have I declared the boundary tournament or other ambient structure?
3. **Bindings:** Is every local symbol defined before use?
4. **Typing:** Are sets, induced tournaments, paths, and covers being used as the right kinds of objects?
5. **Scope:** Are all needed nonemptiness, order, endpoint, and index-range hypotheses explicit?
6. **No provenance inheritance:** Does the root avoid “root X”, “preceding”, “same setup”, “keep the frame”, and similar context inheritance?
7. **Intrinsic language:** Does it say the mathematics rather than the proof role or discovery history?
8. **Terminology:** Does it avoid every unapproved GN3 shorthand in `06_TERMINOLOGY.md`?
9. **Statement only:** Have proof, motivation, and strategy been moved to replies?
10. **Exact strength:** Does every conclusion follow under exactly the stated hypotheses?

If any answer is no, repair the post before treating it as part of the live mathematical corpus.

## 8. Lightweight linting

Mechanical scanning is encouraged as a **warning system**, not as a substitute for mathematical review.

Useful warning patterns include:
- `root <id>`, “preceding theorem”, “same setup”, “keep … frame”;
- forbidden vocabulary from `06_TERMINOLOGY.md`;
- `n-4` without a local definition of `n`;
- use of `T[S]`, `e_T`, or `T-D` before `T` is introduced;
- constructions such as `K=S⊔Y` when `K` is meant to be a tournament;
- an ambient letter `H` or `K` used without a local declaration;
- proof words such as “Proof”, “because”, “we show”, or strategic commentary in a research root.

A lint hit is only a request for inspection. Standard mathematical uses and locally defined notation can produce false positives. The repair decision remains mathematical.

## 9. Promotion boundary

Communication cleanliness is necessary but not sufficient for certification or canonization.

A well-formed research root may still be false or provisional. Audit determines correctness. Structural synthesis determines conceptual placement. Shelf admission and proof-spine/toolkit promotion follow their own rules.

Conversely, correct mathematics should not remain in malformed communication indefinitely. Before a live result becomes load-bearing, audit-targeted, shelf-composed, or guidance-defining, repair its statement so the exact mathematical content can be read without archaeology.
