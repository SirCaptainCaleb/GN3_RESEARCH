# 01 — GN3 architecture

**Status: CANONICAL.**

This file defines only the durable project topology and authority model. Mathematical-language rules are in `02_MATHEMATICAL_LANGUAGE.md`; research operation and Director behavior are in `03_RESEARCH_PROTOCOL.md`; certification and audit are in `04_AUDIT_PROTOCOL.md`. All four are mandatory startup context through `00_START.md`.

## Authority and namespace

GitHub is the durable GN3 authority. Slack is the live communication and search surface. Canonical current mathematics belongs under `GN3/`; the `A7C3/` tree and A7C3-era Slack/Canvas material are legacy provenance and archaeology, not current operating authority.

Migration evidence under `GN3/MIGRATION/` is archival. It may describe older startup paths or file layouts and must not override the numbered init documents.

## Canonical mathematical surfaces

- `GN3/PROOF_SPINE/TWO_TIGHT_PATHS.md` is the single sequential canonical proof attempt. Open implications remain visibly open in that document.
- `GN3/RESEARCH_TREE.md` is the mutable top-down model of the live search. It is working state, not canonical mathematics, an audit ledger, or a historical archive.
- `GN3/TOOLKIT/README.md` indexes selected reusable mathematics. Standalone toolkit rewrites have their own exact audit status.
- `GN3/PROVENANCE.md` is a thin recovery aid for source and audit history when such history materially helps verification. It is not startup mathematical exposition.

There is **no separate `STATUS.md` or `RESEARCH_STATE.md` layer**. The proof spine states the proved/open mathematical boundary; the research tree states the current live abstraction and target; exact certification is governed by `04_AUDIT_PROTOCOL.md` and the relevant audit records. Avoid duplicating those facts into another summary document that can drift.

## Live Slack surfaces

The active GN3 channel set is:

- `#gn3-changelog` (`C0C1VMME8MV`): high-signal project deltas, architecture changes, certification-impact changes, and major research-state changes.
- `#gn3-guidance` (`C0C2ET66370`): Director/Vice Director research guidance waves and material revisions.
- `#gn3-research` (`C0C2ENRLHE0`): mathematical research, proof construction, discussion, and temporary structures.
- `#gn3-audit` (`C0C2D179WSV`): independent verification of exact load-bearing mathematics selected for audit.

The renamed `#gn3-lab` is transitional legacy, not a canonical GN3 surface. Add another active channel only for a recurring need that these four cannot serve cleanly.

## Governing shape

Discovery may be expansive; durable mathematics must be compressive. Scratch work can be broad, but permanent GN3 state should retain only the mathematics and operating structure that survive deliberate simplification.

Computation is auxiliary rather than the default way to compare or verify mathematical statements. In particular, output-heavy symbolic expansion, large tables, and broad recomputation should be avoided unless they are genuinely needed; the operational rule is in `03_RESEARCH_PROTOCOL.md`.

The project deliberately separates live search from canonical mathematics. Slack may contain provisional ideas, the research tree compresses the current search, and audited mathematics enters the proof spine or toolkit only when it has earned a durable role.

## Maintenance

Keep the numbered init set small, explicit, and nonredundant. When a policy belongs to mathematical writing, research operation, or audit, put it in the corresponding numbered file rather than duplicating it here. When a newer explicit rule conflicts with older wording elsewhere, the newer rule should be consolidated into the appropriate numbered init document and the duplicate removed.
