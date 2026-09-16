# GN3 Architecture

**Status: PROVISIONAL — governs migration work until this same file is finalized at cutover.**

## Mandatory startup

After only the access, authentication, repository-location, and tool-discovery actions necessary to retrieve this file, every GN3 worker must fetch and read **one complete, internally consistent revision of this entire file** before synchronizing Slack, making mathematical inferences, editing migration state, or doing research. Search excerpts, selected ranges, summaries, memory, and prior initialization do not count. If retrieval truncates or paginates, continue until the complete revision has been obtained.

GitHub is the sole durable GN3 architecture authority. Slack is a live communication and search surface. No Canvas is required for ordinary GN3 startup.

## Governing principle

**Discovery may be expansive; canonical mathematics must be compressive. Search expansively. Think abstractly. Construct at increasing resolution. Admit failure early. Canonize conservatively. Rewrite compressively.**

Scratchwork may use temporary names, case trees, constructions, computations, and exploratory organization. Canonical GN3 state should inherit only mathematics and operating structure that survives deliberate compression.

## Namespace and legacy boundary

New canonical mathematics belongs under `GN3/`. The existing `A7C3/` tree, A7C3 Slack channels, and A7C3 Canonical Startup Canvas are legacy history, provenance, and archaeology. Do not migrate by renaming or gradually rewriting them into GN3. Make only narrowly necessary archival corrections.

The migration baseline and recovery record is `GN3/MIGRATION/BASELINE.md`. Migration evidence lives under `GN3/MIGRATION/EVIDENCE/`. Provenance is kept thin and outside mathematical exposition.

## Migration concurrency

A7C3 research may continue during migration on the legacy A7C3 surfaces. Anything material after the recorded baseline is a post-baseline delta and must be explicitly incorporated, superseded, or deferred before cutover. Migration work itself belongs under `GN3/` and the new `gn3-*` Slack surfaces.

The user has imposed one migration-order override: **the blank-page simplified proof-spine reconstruction occurs before vocabulary/neologism normalization.** Migration pauses at that boundary for user-supervised work. Do not begin vocabulary normalization first merely because it appears earlier in the original checklist.

## Live Slack surfaces

The intentionally small active GN3 channel set is:

- `#gn3-changelog` (`C0C1VMME8MV`): high-signal project deltas, architecture changes, certification-impact changes, and migration/cutover notices.
- `#gn3-research` (`C0C2ENRLHE0`): expansive mathematical research, proof construction, discussion, and temporary structures.
- `#gn3-audit` (`C0C2D179WSV`): independent skeptical verification and certification work on exact proposed GN3 mathematics.

The pre-existing renamed `#gn3-lab` is transitional legacy and is not a canonical GN3 surface established by this migration.

Do not mechanically recreate the A7C3 channel taxonomy. Add another GN3 channel only when a recurring operational need cannot be served cleanly by these three.

## Authority and mathematical status

GitHub placement does not by itself certify a theorem. Exact status must remain visible. During research, unaudited mathematics may be consumed optimistically unless explicitly failed, invalidated, quarantined, or superseded; canonical certification remains conservative and attaches only to the exact statement/proof independently checked.

A substantive rewrite is new mathematical text for certification purposes. Old A7C3 PASS status is provenance, not automatic certification of a GN3 rewrite. Editorial inheritance is allowed only after an auditor confirms that the mathematics is unchanged.

## Canonical mathematical representation

The canonical proof spine will be a sequential, readable mathematical argument rather than an Engine dependency graph. Its exact representation is intentionally **not yet fixed**: the migration will first reconstruct the active proof from a blank page under user supervision. Unresolved steps may be explicit. Engine-like units, if retained later, are secondary organizational devices corresponding to coherent proof sections or genuinely reusable bounded mechanisms.

Do not use this provisional architecture to pre-decide theorem boundaries, legacy vocabulary, or proof topology before reconstruction.

## Compactness invariant

This file must remain small enough that full-file reading is routine. Keep proofs, catalogs, transcripts, detailed archaeology, volatile research state, and migration evidence elsewhere. When architecture grows, compress it rather than teaching workers to read excerpts.

## Migration recovery

After reading this file in full, a migration worker reads `GN3/MIGRATION/BASELINE.md`, the evidence index, and the temporary Slack migration checklist. Completed checklist items must have durable evidence; conversational memory is never sufficient. At cutover this Canvas dependency disappears and this same architecture file is finalized rather than replaced.

## End of complete architecture

A startup read is complete only after reaching this line in the same fetched revision that supplied the beginning of the file.
