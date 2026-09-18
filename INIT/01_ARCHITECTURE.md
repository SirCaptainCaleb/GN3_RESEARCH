# 01 — GN3 architecture

**Status: CANONICAL.**

This file defines only the durable project topology and authority model. Mathematical-language rules are in 02_MATHEMATICAL_LANGUAGE.md; research operation, structural synthesis, conceptual ascent, and Vice-Director behavior are in 03_RESEARCH_PROTOCOL.md; the shared certification interface is in 04_AUDIT_PROTOCOL.md; computation discipline is in 05_COMPUTATION_DISCIPLINE.md; the controlled project terminology registry is in 06_TERMINOLOGY.md; and live communication shape, self-containment, placement, and repair are in 07_COMMUNICATION_STANDARD.md. Detailed role operation is separated into ASTRA.md and AUDITOR.md. START.md is authoritative for which roles read which files; the init directory is not a universal read-all bundle.

## Role-specific architecture

GN3 deliberately separates strategic direction, research, operational integration, and certification.

- **Astra** is a scarce strategic Director. Astra works at theorem-level abstraction, supplies forward-facing guidance, probes high-level alternatives, and generates or evaluates moonshots. Astra is not responsible for clerical project management. INIT/ASTRA.md is the role-specific startup and resource-discipline authority.
- **Vice Director** performs structural synthesis and conceptual ascent continuously, issues ordinary guidance, integrates Astra guidance, maintains RESEARCH_TREE.md, selects and tracks audit targets, composes shelf candidates, propagates audit corrections, and handles routine durable project-state maintenance.
- **Researchers** do mathematics under the live guidance and research protocol. They do not need detailed audit-operation rules merely to conduct research.
- **Auditors** independently verify and repair exact assigned mathematics. INIT/AUDITOR.md contains the detailed role protocol. Auditors do not need to reconstruct the research strategy unless an exact target depends on it.

Role-specific startup is a context-efficiency feature, not a weakening of mathematical standards. Every role still retrieves any exact mathematics or policy needed for the task at hand. START.md defines the startup route.

## Authority and namespace

GitHub is the durable GN3 authority. Slack is the live communication and search surface. The repository root is the active GN3 namespace: current operating material lives directly in `START.md`, `INIT/`, `PROOF_SPINE/`, `SHELVES/`, `TOOLKIT/`, and `RESEARCH_TREE.md`.

`ARCHAEOLOGY/` is legacy provenance, recovery material, and source archaeology, not current operating authority. The completed A7C3→GN3 migration archive is `ARCHAEOLOGY/a7c3_gn3_migration/`. Historical files may describe older paths or layouts; those descriptions remain provenance and must not override the current root-level startup files.

For legacy mathematical discovery, search `SEARCH_CORPUS.md` first, before resorting to repository-wide GitHub search or manual archaeology browsing, which is usually harder and noisier. `SEARCH_CORPUS.md` can be found in the ChatGPT Project sources or the user's Library and consolidates most old research results into one searchable file, so it is the preferred archaeology index. Resort to GitHub search or open individual files under `ARCHAEOLOGY/` when the corpus points to a specific source, when exact provenance or surrounding context is needed, or when the sought material is absent from the corpus. `SEARCH_CORPUS.md` remains a discovery aid rather than current mathematical authority: any legacy statement recovered from it must still be rechecked and translated into current GN3 language before use.

## Mathematical surfaces

- `PROOF_SPINE/TWO_TIGHT_PATHS.md` is the single sequential canonical proof attempt. Open mathematical implications remain visibly open in that document.
- `SHELVES/CORE/` is the **core-argument shelf**. It contains independently audited, theorem-quality mathematical expositions that plausibly belong in the proof spine but have not yet reached a sufficiently stable final position there. Its purpose is to preserve the exact proofs and their conceptual assembly so that research-tree compression does not strand load-bearing mathematics in scattered Slack threads.
- `SHELVES/UTILITY/` is the **utility-argument shelf**. It contains independently audited standalone mathematics that plausibly belongs in the reusable toolkit but has not yet been selected or edited into its final toolkit form.
- `SHELVES/HOT/` is the **provisional strategic hot shelf**. It is not an audited mathematical shelf and does not confer certification. It exists to compress recent state-shaping mathematics for Astra when that material is too new, provisional, unsettled, or strategically framed to belong yet in `CORE/` or `UTILITY/`. Its operating rules are in `SHELVES/HOT/README.md`; the rolling Astra-facing file is `SHELVES/HOT/ASTRA.md`.
- `RESEARCH_TREE.md` is the mutable top-down outline of the live proof search. It is deliberately lossy: it may be rewritten aggressively as the strategy changes because audited mathematics worth retaining has a shelf or canonical destination.
- `TOOLKIT/README.md` is the startup-facing statement index for the toolkit and should contain every retained toolkit statement at statement-level detail. Individual files under `TOOLKIT/` contain the corresponding proofs and fuller exposition and are retrieved when needed. `TOOLKIT/` contains the final selected standalone mathematics worth retaining independently of the route that first produced it.

### Shelf admission and organization

**Nothing mathematical enters either shelf before independent audit of the exact shelf candidate.** Certification of ingredients does not automatically certify a rewritten or merged exposition. A shelf candidate is drafted outside the shelf—normally in Slack or on a temporary Git branch—and the exact candidate is audited under `04_AUDIT_PROTOCOL.md`. Only a `PASS` or `PASS_ADJUSTED` exact revision may be admitted to `SHELVES/CORE/` or `SHELVES/UTILITY/`. A mathematical change to an admitted shelf file is likewise drafted and audited before replacing the admitted revision.

The shelves are organized by **mathematical topic and proof coordinate, not by guidance era, worker, result number, or discovery chronology**.

A core-shelf file should normally be a coherent proto-proof section: merge nearby certified lemmas into an intelligible conceptual movement, remove discovery-time repetition, order dependencies naturally, and write the mathematics at roughly proof-spine quality. Do not preserve a pile of tiny Slack results merely because they were discovered separately. Split core files only when the proof naturally has distinct mathematical coordinates large enough to be read independently.

A utility-shelf file should be organized around a reusable mathematical topic. It may contain one theorem or a family of related lemmas of any size. Utility arguments should be understandable independently of the current proof route and should not carry proof-search chronology or route-specific scaffolding unless that structure is mathematically intrinsic.

`SHELVES/CORE/` and `SHELVES/UTILITY/` are **certified staging surfaces, not final canonical destinations and not status ledgers**. Their files are math only. `SHELVES/HOT/` is a deliberate exception: it is a provisional strategic delta surface, may mark certification state and strategic relevance, and must never be cited as certified merely because it is under `SHELVES/`. Audit records, provenance, guidance tags, and admission rationale remain in Slack and Git history. Promotion from `SHELVES/CORE/` to the proof spine is an editorial/structural decision after the argument has stabilized in the sequential proof. Promotion from `SHELVES/UTILITY/` to `TOOLKIT/` is the corresponding selection decision for reusable mathematics. A shelf item may instead be removed when later synthesis subsumes it, shows it irrelevant, or identifies a better formulation; Git history preserves recovery.

Audit certification, structural synthesis, conceptual ascent, shelf admission, and final canonical placement are distinct. Audit verifies exact mathematics. Structural synthesis determines how results fit together and which arguments should be merged. Conceptual ascent searches for stronger or more intrinsic explanations. Shelf admission preserves audited mathematics that has become plausibly durable before its final exposition is settled. Final proof-spine/toolkit placement occurs only after the mathematical role has stabilized.

A certified result that is plausibly part of the surviving proof route should not remain indefinitely only in Slack: once its conceptual neighborhood is understood, it should be incorporated into an audited core-shelf exposition. Likewise, a certified reusable result that is plausibly worth retaining independently should be incorporated into an audited utility-shelf exposition. This requirement is the durable **assembly map** missing from a Slack-only research stream.

The persistent certified mathematical documents themselves are **math only**. Files under `PROOF_SPINE/`, `SHELVES/CORE/`, `SHELVES/UTILITY/`, and `TOOLKIT/`, including `TOOLKIT/README.md`, may contain definitions, mathematical statements, proofs, examples, counterexamples, corollaries, and explicit mathematical remarks. `SHELVES/HOT/` is not part of this certified-math-only class; it is a compact handoff surface governed by its own README. They do not contain document-purpose explanations, curation rationale, “why retained” discussion, workflow instructions, audit status, certification prose, migration commentary, or legacy provenance. Those belong in `INIT/`, Slack, Git history, or `ARCHAEOLOGY/` according to their role.

In particular, audit certification is not embedded as status wrappers in mathematical files. Exact certification is recorded by the audit protocol and its audit threads, keyed to exact revisions; Git history supplies revision identity. Removing or adding nonmathematical metadata must not become a reason to clutter mathematical documents again.

There is **no separate `STATUS.md`, `RESEARCH_STATE.md`, active provenance layer, or project-wide audit ledger**. `SHELVES/CORE/` and `SHELVES/UTILITY/` do not recreate any of those layers: they store audited mathematics itself, not summaries of project state. `SHELVES/HOT/` is narrower than a status layer: it contains only the recent mathematics and negative evidence needed for Astra's strategic delta, and is aggressively pruned after that mathematics settles elsewhere or ceases to shape the frontier. The proof spine states the proved/open mathematical boundary; the research tree states the current live abstraction and target; the Vice Director tracks which live dependencies require certification; exact certification is governed by `04_AUDIT_PROTOCOL.md` and the relevant audit records. Avoid duplicating those facts into another summary document that can drift.

## Live Slack surfaces

The active GN3 channel set is:

- `#gn3-changelog` (`C0C1VMME8MV`): the continuity stream for high-signal project deltas, including startup-policy changes, certification-impact changes, canonical proof-boundary changes, and major research-state changes that already-initialized workers need to know.
- `#gn3-guidance` (`C0C2ET66370`): Director/Vice Director research guidance waves and material revisions.
- `#gn3-research` (`C0C2ENRLHE0`): mathematical research, proof construction, discussion, and temporary structures.
- `#gn3-audit` (`C0C2D179WSV`): independent verification and repair of exact load-bearing mathematics selected by the Vice Director for audit.

The renamed `#gn3-lab` is transitional legacy, not a canonical GN3 surface. Add another active channel only for a recurring need that these four cannot serve cleanly.

## Governing shape

Discovery may be expansive; durable mathematics must be compressive. Scratch work can be broad, but permanent GN3 state should retain only the mathematics and operating structure that survive deliberate simplification.

Computation is auxiliary rather than the default way to compare or verify mathematical statements. In particular, output-heavy symbolic expansion, large tables, and broad recomputation should be avoided unless they are genuinely needed; the operational rule is in `03_RESEARCH_PROTOCOL.md`.

The project deliberately separates live search, structural synthesis, conceptual ascent, certification, shelf preservation, and final canonical placement. Slack may contain provisional or certified mathematics. Structural synthesis reconstructs the best combined mathematical picture and abstraction hierarchy from old and new work. Conceptual ascent searches above that picture for the strongest explanatory formulation and for alternate dual, obstruction, or negative-space views. The research tree records the compressed live search that results; audit verifies and repairs exact load-bearing targets, with second-auditor verification required after substantial auditor-authored mathematical changes; and the Vice Director separately decides which certified mathematics has earned a durable role in the proof spine or toolkit.

## Maintenance

Keep the shared numbered init set small, explicit, and nonredundant, and keep specialized role machinery in the corresponding role-specific file. When a policy belongs to mathematical writing, research operation, structural synthesis, conceptual ascent, shared certification, terminology, or live communication, put it in the corresponding numbered file rather than duplicating it here. Detailed Astra and Auditor operation belongs in ASTRA.md and AUDITOR.md. When a newer explicit rule conflicts with older wording elsewhere, the newer rule should be consolidated into the appropriate numbered init document and the duplicate removed.

Because initialization is one-time, changelog completeness is a durability requirement. A material change to `START.md`, the numbered init policies, the canonical proved/open boundary, or another durable fact that an already-initialized worker must know to work safely must be surfaced in `#gn3-changelog`. The changelog entry either states the usable delta or tells workers exactly what must be reread; if full reinitialization is genuinely required, it says so explicitly.
