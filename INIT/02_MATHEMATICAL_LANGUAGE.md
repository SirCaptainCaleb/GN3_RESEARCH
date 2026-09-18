# 02 — Mathematical language and proof coding

These rules apply to **all mathematical communication in GN3**: Slack research posts and replies, Director guidance, audit discussion, research-tree text, synthesis notes, toolkit statements, and canonical proofs. They are not merely publication-style preferences. The structural rules for how live Slack messages are divided into roots and replies, made self-contained, and repaired are governed by `07_COMMUNICATION_STANDARD.md`.

## Say the mathematics, not the proof history

Whenever the mathematical object or assertion can be named directly, name it directly. Speak about paths, covers, endpoints, triples, orders, intersections, deletions, inequalities, obstructions, and implications rather than replacing them with proof-role descriptions such as “the downstream object”, “the closure witness”, “the output of the previous result”, “the active mechanism”, or “the state carried by the branch”.

Workflow metadata is allowed where it is actually workflow metadata—for example `[G##]`, `[PASS]`, audit status, a note that a branch is obsolete, or a request to inspect the earliest open statement. It must not substitute for the mathematics itself. A mathematical claim in Slack or the research tree should be intelligible without reconstructing which proof step produced each object.

This is especially important during research: convenient meta-language tends to harden into hidden ontology. Different branches then silently attach different meanings to the same phrase and the ambiguity leaks into the proof. Prefer slightly longer explicit mathematics over a compact proof-history phrase. Temporary terminology is acceptable only when it names a mathematically defined object or condition rather than its role in the argument.

Directors, Vice Directors, auditors, and researchers should actively rewrite meta descriptions into ordinary mathematical language during synthesis.

## Mathematical compilability

Canonical GN3 mathematics must be natural mathematical prose that is also unambiguous and mathematically compilable:

- every nonstandard object is defined before use;
- every symbol and variable has a determined meaning and domain;
- every operation has mathematically specified inputs and outputs;
- notation has stable scope;
- every proof step can be interpreted without guessing an omitted type, invariant, transition, or change of meaning.

Definitions are **ontological first**: say what kind of mathematical object is being defined, then state its distinguishing conditions. Prefer “An `X` is a `Y` such that ...” or “Define `X` to be ...” over descriptions of what `X` “records”, “permits”, or “begins with”.

Definitions must be **intrinsic**. Never define an object, operation, relation, hypothesis, or conclusion as “the output of Lemma X”, “the object produced above”, or another proof-history description. Theorem numbers may be cited as reasons an intrinsically stated fact holds; they must not supply the meaning of the fact.

Operations and relations must be defined by their mathematical domains, hypotheses, and outputs. Pseudo-formal notation is not a substitute for a definition.

## Terminology

Prefer standard graph-theoretic and combinatorial language. Project-coined reusable mathematical vocabulary is controlled by `06_TERMINOLOGY.md`, which is the authoritative terminology registry.

Standard mathematical terms and literal descriptive phrases do not require registration. A reusable GN3-specific English label does. **If a project-coined term is not approved in `06_TERMINOLOGY.md`, do not use it as established shorthand; spell out the mathematics instead.**

Do not introduce vocabulary merely to encode proof position, discovery history, audit state, or workflow. Avoid vague meta-nouns such as “data”, “state”, “current”, “active”, “physical”, “certificate”, or “credit” when the intended referent is actually a path, cover, ordering, orientation, witness, inequality, or other explicit mathematical object or property.

A technical word such as “continuation” is permissible only when it denotes a precisely defined and registry-approved mathematical object, operation, or relation. Its ordinary-language connotations may not smuggle in extra reachability or persistence assumptions.

Workers may propose new terminology in discussion, but it is not GN3 mathematical vocabulary until the registry is updated. Archaeology and legacy Slack do not grandfather terminology into the current project.

## No hidden provenance or unlawful reachability

State exact hypotheses and conclusions. Do not rely on remembered context, implicit phase, theorem-output provenance, or an unnamed earlier construction to supply missing assumptions.

An object is not mathematically distinguished merely because it appeared earlier. If a later argument reuses a particular path, cover, pair, witness, or ordering, quantify or fix it together with every property needed later.

Every transition, replacement, deletion, shortening, continuation, inheritance step, or reuse of an earlier object must be mathematically lawful. A subpath obtained by deleting vertices is not thereby a later member of a structured construction unless a defined operation places it there. Retaining a true fact about an earlier object is different from producing a new object.

Preserve every feature actually needed downstream—orientation, endpoint choice, witness, disjointness, maximality, exact order, recurrence condition, and scope. Simplification may remove historical scaffolding, but it may not hide mathematically load-bearing complexity.

## Strengthening, factorization, and finite checks

Actively test straightforward natural strengthenings. Do not fossilize a weaker historical statement merely because that was the accepted legacy form. If a stronger theorem follows by a short or moderate argument and is useful, prefer it. A strengthening proved by a new argument is new mathematics and requires fresh audit before certification.

Do not “simplify” by inventing a stronger abstraction that merely masks unresolved work. If proving the stronger formulation opens a substantial new research program, keep the strongest proved statement and record the stronger claim only as a research target.

When two arguments share a weaker natural parent lemma, factor that parent rather than duplicating stronger hypotheses. Inline one-use machinery; extract only statements that improve reuse, clarity, or proof topology.

Finite case checks and exceptional configurations must be checkable from the text by a conceptual argument, an explicit bounded table, or a precisely stated earlier lemma. “One checks” is not acceptable at a load-bearing step.

## Canonical proof form

Canonical proofs must be sequentially readable and self-contained up to explicitly named canonical inputs. Provenance, audit history, A7C3 Engine/R identifiers, discovery transcript, migration vocabulary, and obsolete machinery belong outside the mathematical exposition.

Unresolved implications must be stated as gaps or research targets, never disguised as continuations, heuristics, bookkeeping ranks, inherited status, or theorem-output objects.

Auditors and integrators enforce these rules globally. A mathematically plausible argument that violates them is not ready for canonical GN3 status until it has been rewritten into explicit mathematics.
