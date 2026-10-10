# NORI manuscript transition — recovery and migration

Project: Supabase RESEARCH `fewmvjslkhoygixiimgn`, schema `nori`. Migration session: `session_nori_r4593_2`.

This transition is recorded as ordered **Supabase SQL migrations** (see migration list) and the tracked artifact source `scripts/sync_research_mirror.py`. It changes only NORI, not other research schemas.

## Immutable original source

The pre-transition repository commit **`8e738d2766976fbfe0df2997a09ce2b1098bdb00`** contains all 493 source Item files under `nori/grand_conjecture/<article>/<section>/<subsection>/<old-id>.md`. The corresponding completed artifact is GitHub Actions artifact `11661377615` (snapshot revision `1073`), independently inspected to contain 493 Item files. Git history preserves prior committed revisions when present; do not infer complete database edit-by-edit bodies from Git.

Old IDs resolve through `nori.historical_item(old_id)`, `nori.historical_find(query)`, and (for direct legacy reads) `nori.read(array[old_id])`. The small `nori.legacy_item_redirects` table stores no full proof body. There is no second active-database Item archive.

## Applied database migrations (chronological)

1. `nori_item_historical_archive_before_manuscript_transition` — temporary lossless safety snapshot during transition (later deliberately dropped).
2. `nori_retire_active_items_enable_direct_subsection_publication` — legacy nodes marked inactive; direct versioned Subsection publication API.
3. `nori_discard_duplicate_item_archive_use_versioned_github_backup_and_redirects` — confirm fixed Git backup, record 493 old-ID redirects, delete 493 Item nodes, drop temporary duplicate archive.
4. `nori_manuscript_first_search_current_compositions` — default search over live Article/Section/Subsection composition text, overview and Toolkit.
5. `nori_expose_manuscript_read_search_status_and_exact_composition_audits` and `nori_fix_exact_manuscript_audit_provenance_insert` — manuscript reads, versioned audit records, startup status.
6. `nori_read_legacy_id_redirects_to_committed_github_sources` — historical IDs resolve from ordinary read without returning to active search.

The earlier coordination system was retired separately; no task claims, leases, checkpoints or rankings remain.

## Editorial migration

- Preserve existing 50 composed Subsections and their SQL composition versions.
- Curate into full compositions the previously unfinished `maximal_geodesic_blockers_and_snake_exchanges` and `exterior_face_charts_and_fourier_transport`, integrating important proofs and certificates selectively.
- Add `appendix_known_obstructions_to_proposed_nori_mechanisms` under Article I's foundational Section. This is a concise cross-approach appendix, not a statement that NORI is refuted.
- Article, Section, and Subsection compositions remain separately versioned in `nori.compositions`. Current source dependencies on archived Items were removed; old composition snapshots retain provenance metadata.
- `scripts/sync_research_mirror.py` now emits eight assembled `MANUSCRIPT.md` files, `KNOWN_OBSTRUCTIONS.md`, `WORKER_PROMPT.md`, and NORI-specific `GUIDE.md`, `REFLEXES.md`, `API.md`.

## Verification and operations

```sql
select nori.status();
select nori.changes(1073,null,100);
select nori.search('forcing', '{}'::jsonb);
select nori.read_manuscript('subsection','appendix_known_obstructions_to_proposed_nori_mechanisms',1);
select nori.historical_item('nori_q6_922_good_geodesics_pentagon_certificate_20261009');
select count(*) from nori.legacy_item_redirects; -- 493
select count(*) from nori.nodes where type='item'; -- 0
```

New mathematical writing uses `nori.publish_subsection(session,subsection_id,body,expected_composition_version,source_note)`. No publication is required after an inconclusive research session. Do not run `boot()` again while continuing an existing NORI conversation.
