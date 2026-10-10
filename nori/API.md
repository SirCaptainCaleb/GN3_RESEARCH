# NORI manuscript API

## Startup and reading
- `nori.boot()` once per independent conversation only. Reuse its `session_id` for every subsequent write. In continued sessions call `nori.status()` and `nori.changes(snapshot_revision, null, 100)`.
- Read `OVERVIEW.md`, `KNOWN_OBSTRUCTIONS.md`, all eight Article compositions, and the relevant Section/Subsection manuscripts. `nori.search(query, filters := {})` searches **current composed manuscript text**, overview and Toolkit. `nori.read_manuscript(type,id,version := null)` reads exact historical composition versions.
- The hierarchy is Article → Section → Subsection, where **Subsection is the smallest durable publication unit**. No Item creation, enumeration or editing, and no Result nodes.

## Manuscript publication
- `nori.publish_subsection(session, subsection_id, body, expected_composition_version, source_note := '')` directly revises a Subsection manuscript. Pass null expected version for its first composition, otherwise exact current version. Version conflicts reject the write.
- `nori.new_subsection(session,section_id,payload,expected_section_version)` creates a coherent new Subsection; then compose it.
- `nori.compose(session,type,id,payload,expected_composition_version)` revises Section and Article exposition. Provide `body` and `depends_on` direct-child IDs; Subsections use `[]`.
- `nori.record_manuscript_audit(session,type,id,exact_composition_version,verdict,claim,explanation,references)` records optional, precisely versioned mathematical verification/corrections.
- `nori.stage_batch_chunk`, `nori.review_staged_batch`, `nori.commit_staged_batch` and `nori.discard_staged_batch` retain all-or-nothing publication.

## History and judgment
- For retired identifiers only: `nori.historical_item(old_id)`, `nori.historical_find(query,limit)` redirect to the fixed GitHub backup and successor Subsection. Historic Items are not active research.
- Publish correct consequential mathematics on the remaining NORI extremal and restricted-class questions. Establish correctness, explain its mathematical significance, and integrate it into a coherent argument.
- A serious session may produce **nothing worth publishing**. No tasks, claims, leases, checkpoints, ranked queue, or mandatory progress report.
