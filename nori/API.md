# NORI manuscript API

## Startup and reading
- `nori.boot()` once per independent conversation only. Reuse its `session_id` for every subsequent write. In continued sessions call `nori.status()` and `nori.changes(snapshot_revision, null, 100)`.
- Read `OVERVIEW.md`, `KNOWN_OBSTRUCTIONS.md`, all eight Article compositions, and the relevant Section/Subsection manuscripts. `nori.search(query, filters := {})` searches **current composed manuscript text**, overview and Toolkit. `nori.read_manuscript(type,id,version := null)` reads exact historical composition versions.
- The hierarchy is Article → Section → Subsection, where **Subsection is the smallest durable publication unit**. No Item creation, enumeration or editing, and no Result nodes.

## Research notes: selective non-manuscript memory
- nori.save_note(session,payload,expected_version:=null): create title/body with home_type=project|article|section|subsection and home_id (nori for project); optional stable id, author, labels, related [{type,id,version?}], epistemic_status, lifecycle. Manifests may pin exact manuscript composition versions; note-to-note links track the current note. Revisions require exact expected_version.
- nori.read_note(id,version:=null) reads the current or immediately previous note revision ONLY. On revision, the previous snapshot replaces any older snapshot; no unbounded note history. nori.search_notes(query:='',filters:={}) searches/browses with home_type,home_id,label,lifecycle,epistemic_status,linked_to,limit,offset.
- nori.notes_for(type,id) finds primary-home and linked notes. read_manuscript includes related_notes metadata; manuscripts never automatically incorporate note bodies.
- lifecycle active|resolved|superseded is separate from epistemic_status. Resolution and supersession require disposition, and supersession requires a valid successor_id.
- **Editorial rule:** negative results default to research notes even when completely proved, extensive, or occupying an entire Section. Exception: decisive refutations of important conjectures (such as NORI3 Q9) or independently significant theorems. Mixed manuscripts retain self-standing mathematical advances and link scoped obstruction notes. Preserve proofs, precise hypotheses and certificates when reclassifying; never discard content merely because it is negative.
- Separate brainstorm writes are retired in NORI; use only the selective research-note entity. The selective RESEARCH_NOTES/QUESTIONS.md map records alternatives and obstructions without ordering the agenda. Read pertinent notes, not all notes at startup.

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
