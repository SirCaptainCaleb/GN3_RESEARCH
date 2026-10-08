# Research API

The artifact is a snapshot; these RPCs are the live worker interface.

## Startup and reading

### boot()
Starts a session and returns the artifact snapshot revision, startup broadcasts, notices, and session ID.

### search(query, filters := {})
Discovers Articles, Sections, Subsections, Toolkit, documents, and Brainstorms. Explore an individual Subsection using items(subsection_id).

### read(ids, math_versions := {}, cursor := null, page_chars := 9000)
Reads durable Article, Section, Subsection, Toolkit, and Brainstorm content.

### context(research_id)
Shows mathematical dependencies, consumers, supersessions, Article references, and origin.

### composition_status(node_type, node_id)
Returns composition_state=absent or present. Articles, Sections, and Subsections may legitimately have no composition. For existing compositions it shows version, dependencies, and frontier.

### dependencies(node_type, node_id)
Shows the dependency manifest for a manuscript node.

### changes(since_revision := 0, until_revision := null, limit := 100)
Returns live events and current composition state since a revision.

## Mathematical consumption (independent of containment and composition)

All Article, Section, Subsection, Item, and Result IDs are globally unique per schema. Their unified typed records are in `nodes(id, type, data, consumed_by, consumes)`; the former level-specific physical tables have been retired. Consumption RPCs infer node type from ID; callers must not supply a type.

The child is authoritative: Sections, Subsections, Items and Results each store `consumed_by: [parent_ids]`. One child may have multiple consumers. Parent Articles, Sections, Subsections, and Items cache the corresponding `consumes: [child_ids]`; changes update that cache transactionally. None of these links requires an existing composition.

### set_consumed_by(session_id, child_id, consumer_ids)
Replaces all consumers of one child, automatically refreshing the affected parents' `consumes` caches.

### set_consumes(session_id, parent_id, child_ids)
Atomically replaces one parent's consumed children by updating the children's authoritative `consumed_by` lists. Omitted children lose *only that parent*, keeping their other consumers. Omit the `consumes` key on a parent creation/edit to leave relationships unchanged; explicitly pass an empty array to clear them. Creation RPCs for Articles, Sections, Subsections, and Items accept `payload.consumes`.

## Development

### new_subsection(session_id, section_id, payload, expected_section_version)
Creates a new Subsection container.

### items(subsection_id) / read_item(item_id) / item_results(item_id)
Lists Items under a Subsection; reads an Item and its Results; lists Results under an Item.

### new_item(session_id, subsection_id, payload)
Creates an Item. The payload provides id, kind, title, and body; the position is local to its Subsection.

### save_item(session_id, item_id, payload, expected_version)
Revises an Item with optimistic concurrency.

### new_item_result(session_id, item_id, payload)
Creates a named Result/claim within an Item. The payload provides id, kind, title, statement, proof, and status.

### save_item_result(session_id, result_id, payload, expected_version)
Revises an individual Result with optimistic concurrency.

### tree()
Returns the manuscript hierarchy from the grand conjecture through Article, Section, Subsection, Item, and Result.

### save_subsection(session_id, section_id, payload, expected_section_version, expected_subsection_version)
Edits a Subsection title and/or its explicit consumes list. Subsection development bodies are retired; mathematical development belongs in Items and Results.

### compose(session_id, node_type, node_id, payload, expected_composition_version)
Writes optional, publication-quality mathematical exposition for an Item, Subsection, Section, or Article. An absent composition is valid. An existing composition must have precise mathematical statements, full definitions locally or in the Dictionary, justified proofs, and explicit uncertainties; a child inventory or progress log is not a composition. payload contains body and depends_on as an explicit array of selected direct lower-level composition IDs. Items use [] and compress their Results. Use [] when independent. Pass NULL only for the first composition; otherwise pass the current composition version. Only the current and immediately previous composition are retained.

### save_research(session_id, payload, expected_version := null)
Creates or edits Section structure/metadata or a Toolkit object.

### save_document(session_id, payload, expected_version := null)
Creates or edits a project document or Article structure/metadata.

## Brainstorms

### brainstorms(active_only := true)
Lists exploratory work.

### save_brainstorm(session_id, payload, expected_version := null)
Creates or edits a Brainstorm.

### promote_brainstorm(session_id, brainstorm_id, payload := {}, expected_version)
Promotes a Brainstorm into manuscript development while preserving its source history.

## Audits and stewardship

### request_audit(session_id, target_type, target_id, target_version)
Queues an independent audit of a canonical version.

### claim_chore(session_id, kinds := {audit,recomposition,maintenance})
Claims one stewardship task.

### finish_chore(session_id, chore_id, outcome := {})
Completes a claimed audit or maintenance task.

## Atomic publication batches

Use stage_batch_chunk, review_staged_batch, and commit_staged_batch for multi-operation publication. stage_batch_chunk accepts JSON text or base64:<blob>; base64 is decoded as UTF-8 before review and commit.

Compose operations carry payload.body, payload.depends_on, expected_composition_version, and optional source_note. Development operations use their ordinary payload contracts.

### artifact_help()
Returns artifact recovery and rebuild information.

### help()
Returns the compact machine-readable interface summary.
