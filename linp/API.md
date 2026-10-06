# Research API

The artifact is a snapshot; these RPCs are the live worker interface.

## Startup and reading

### boot()
Starts a session and returns the artifact snapshot revision, startup broadcasts, notices, and session ID.

### search(query, filters := {})
Discovers Articles, Sections, Subsections, Toolkit, documents, and Brainstorms.

### read(ids, math_versions := {}, cursor := null, page_chars := 9000)
Reads durable Article, Section, Subsection, Toolkit, and Brainstorm content.

### context(research_id)
Shows mathematical dependencies, consumers, supersessions, Article references, and origin.

### composition_status(node_type, node_id)
Shows the current composition version, explicit dependency staleness, and frontier metadata describing what material existed when the composition was written.

### dependencies(node_type, node_id)
Shows the dependency manifest for a manuscript node.

### changes(since_revision := 0, until_revision := null, limit := 100)
Returns live events and current composition state since a revision.

## Development

### new_subsection(session_id, section_id, payload, expected_section_version)
Creates a local Subsection development branch.

### save_subsection(session_id, section_id, payload, expected_section_version, expected_subsection_version)
Edits an existing Subsection by stable ID.

### compose(session_id, node_type, node_id, payload, expected_composition_version)
Writes a deliberately lossy composition. payload contains body and, for Sections and Articles, depends_on as an explicit array of direct lower-level composition IDs. Use [] when independent. Pass NULL only for the first composition; otherwise pass the current composition version. Only the current and immediately previous composition are retained.

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
