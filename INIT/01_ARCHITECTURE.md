# 01 — GN3 architecture

**Status: CANONICAL.**

This file defines only the durable project topology and authority model. Mathematical-language rules are in `02_MATHEMATICAL_LANGUAGE.md`; research operation, structural synthesis, conceptual ascent, and Director behavior are in `03_RESEARCH_PROTOCOL.md`; certification and audit are in `04_AUDIT_PROTOCOL.md`. All four are mandatory startup context through `START.md`.

## Authority and namespace

GitHub is the durable GN3 authority. Slack is the live communication and search surface. The repository root is the active GN3 namespace: current operating material lives directly in `START.md`, `INIT/`, `PROOF_SPINE/`, `TOOLKIT/`, and `RESEARCH_TREE.md`.

`ARCHAEOLOGY/` is legacy provenance, recovery material, and source archaeology, not current operating authority. The completed A7C3→GN3 migration archive is `ARCHAEOLOGY/a7c3_gn3_migration/`. Historical files may describe older paths or layouts; those descriptions remain provenance and must not override the current root-level startup files.

## Canonical mathematical surfaces

- `PROOF_SPINE/TWO_TIGHT_PATHS.md` is the single sequential canonical proof attempt. Open mathematical implications remain visibly open in that document.
- `RESEARCH_TREE.md` is the mutable top-down outline of the live proof search. It is the deliberate exception to the math-only document rule below: it may contain concise proof-strategy guidance, route selection, search directives, and progressively finer mathematical targets. It should remain an outline rather than a store of full proofs or extended discussion; maintenance rules are in `03_RESEARCH_PROTOCOL.md`.
- `TOOLKIT/README.md` indexes selected reusable mathematics. `TOOLKIT/` contains standalone mathematics worth retaining independently of the route that first produced it. Broadly reusable statements belong there; proof-local mathematics normally remains in the proof spine.

Audit certification, structural synthesis, conceptual ascent, and canonical placement are distinct. Audit includes both verification and repair: when an exact target has a localized defect, the Auditor is expected to repair the text rather than merely diagnose it. Localized repairs may be checked and certified by that Auditor under `04_AUDIT_PROTOCOL.md`; a substantial auditor-authored mathematical change requires a second independent Auditor before certification. A PASS certifies the exact mathematics checked; it does **not** by itself imply that the result belongs in the proof spine or toolkit. Structural synthesis, defined in `03_RESEARCH_PROTOCOL.md`, determines how old and new mathematics fit together, what the arguments are really expressing, which formulations subsume or combine with others, and what abstraction hierarchy best explains the live corpus. Conceptual ascent then deliberately searches above that combined picture for stronger or more intrinsic mathematics: parent theorems, generalizations, useful weakenings, invariant reformulations, dual or obstruction forms, contrapositives, and negative-space descriptions that reveal why the observed phenomena occur. Only after mathematical role and explanatory level are understood does the Vice Director choose durable placement. A certified result belongs in the proof spine when it has acquired a stable load-bearing role in the favored sequential proof and its inclusion clarifies the proved/open boundary. A certified result belongs in the toolkit when it is worth retaining as reusable mathematics independently of the current route, including when its eventual role in the proof spine is uncertain. A certified result may also remain only in Slack and the research tree while its long-term utility or best abstraction is still unresolved. Conversely, once a result is both certified and clearly part of the stable proof route, it should be integrated at its natural proof coordinate rather than withheld merely because it was discovered or audited separately.

The persistent mathematical documents themselves are **math only**. Files under `PROOF_SPINE/` and `TOOLKIT/`, including `TOOLKIT/README.md`, may contain definitions, mathematical statements, proofs, examples, counterexamples, corollaries, and explicit mathematical remarks. They do not contain document-purpose explanations, curation rationale, “why retained” discussion, workflow instructions, audit status, certification prose, migration commentary, or legacy provenance. Those belong in `INIT/`, Slack, Git history, or `ARCHAEOLOGY/` according to their role.

In particular, audit certification is not embedded as status wrappers in mathematical files. Exact certification is recorded by the audit protocol and its audit threads, keyed to exact revisions; Git history supplies revision identity. Removing or adding nonmathematical metadata must not become a reason to clutter mathematical documents again.

There is **no separate `STATUS.md`, `RESEARCH_STATE.md`, active provenance layer, or project-wide audit ledger**. The proof spine states the proved/open mathematical boundary; the research tree states the current live abstraction and target; the Vice Director tracks which live dependencies require certification; exact certification is governed by `04_AUDIT_PROTOCOL.md` and the relevant audit records. Avoid duplicating those facts into another summary document that can drift.

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

The project deliberately separates live search, structural synthesis, conceptual ascent, certification, and canonical placement. Slack may contain provisional or certified mathematics. Structural synthesis reconstructs the best combined mathematical picture and abstraction hierarchy from old and new work. Conceptual ascent searches above that picture for the strongest explanatory formulation and for alternate dual, obstruction, or negative-space views. The research tree records the compressed live search that results; audit verifies and repairs exact load-bearing targets, with second-auditor verification required after substantial auditor-authored mathematical changes; and the Vice Director separately decides which certified mathematics has earned a durable role in the proof spine or toolkit.

## Maintenance

Keep the numbered init set small, explicit, and nonredundant. When a policy belongs to mathematical writing, research operation, structural synthesis, conceptual ascent, or audit, put it in the corresponding numbered file rather than duplicating it here. When a newer explicit rule conflicts with older wording elsewhere, the newer rule should be consolidated into the appropriate numbered init document and the duplicate removed.

Because initialization is one-time, changelog completeness is a durability requirement. A material change to `START.md`, the numbered init policies, the canonical proved/open boundary, or another durable fact that an already-initialized worker must know to work safely must be surfaced in `#gn3-changelog`. The changelog entry either states the usable delta or tells workers exactly what must be reread; if full reinitialization is genuinely required, it says so explicitly.
