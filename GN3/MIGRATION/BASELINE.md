# GN3 migration baseline

Status: **active migration control record**.

## Migration owner

The migration is owned by the **GN3 Research Overhaul Migration Director**. The owner is responsible for checklist maintenance, interruption recovery, baseline/delta reconciliation, and cutover accounting. A replacement owner must begin from this record, `GN3/ARCHITECTURE.md`, and the migration checklist rather than from conversational memory.

## Repository baseline

The pre-migration repository baseline is the exact `main` commit:

`7b68b016d3fd309f8a81070bd140e4718d309f53`

Commit timestamp: 2026-09-16 15:24:44 UTC.

Commit message: `Remove redundant architecture backup`.

All GN3 migration commits are descendants of this coordinate. This SHA is evidence/provenance only; it is not a second architecture authority.

## Slack baseline

The A7C3 Canonical Startup Canvas was read in full at migration start. Its recorded live coordinate was changelog `64`, guidance `G53`, architecture `A47`. The changelog was independently synchronized through numbered root 64 before migration writes began.

The live shortest A7C3 route at the baseline is:

`E8997 -> E9007 -> E9008`.

The baseline mathematical state is preserved under `GN3/MIGRATION/EVIDENCE/` rather than by Slack links alone. The evidence includes the Canonical Startup snapshot and the live proof/audit frontier needed to reconstruct the active state.

## Research during migration

Ordinary A7C3 research is **not paused**. Until GN3 cutover, intervening discoveries continue to land only on the existing A7C3 research surfaces and/or legacy `A7C3/` GitHub area under the existing rules. They do not become GN3 canon merely by occurring during migration.

Everything materially created, repaired, audited, invalidated, or superseded after the baseline coordinate is a **post-baseline delta**. The migration owner must reconcile every material delta before cutover by one of three explicit dispositions: incorporated into GN3, superseded by GN3, or deliberately deferred as a post-migration research target. Cutover is forbidden while material deltas are unaccounted for.

## Legacy boundary

`A7C3/`, the A7C3 Canonical Startup Canvas, and A7C3-era Slack channels are legacy state. They remain readable for provenance and archaeology. They are not to be renamed, mechanically rewritten, or incrementally mutated into GN3 canon. Only narrowly necessary archival corrections are allowed.

The already-renamed Slack channel `#gn3-lab` is treated as a transitional legacy surface, not a canonical GN3 channel created by this migration. The canonical GN3 Slack surfaces are newly created channels recorded in `GN3/ARCHITECTURE.md`.

## Migration-order override

The user has explicitly required the **blank-page simplified proof-spine reconstruction to occur before vocabulary/neologism normalization**, regardless of the original checklist ordering. The migration therefore pauses after the pre-reconstruction setup items so the user can oversee the reconstruction manually. Vocabulary normalization is not to begin before that supervised reconstruction.

## Recovery rule

If migration is interrupted, recover in this order:

1. Read one complete revision of `GN3/ARCHITECTURE.md`.
2. Read this baseline record and the evidence index under `GN3/MIGRATION/EVIDENCE/`.
3. Read the current migration checklist and identify the first unchecked item, respecting the user-ordered manual reconstruction gate.
4. Synchronize post-baseline A7C3 deltas before making any cutover decision.
