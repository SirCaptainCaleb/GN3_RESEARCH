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
Shows the current development and composition versions together with dependency staleness.

### dependencies(node_type, node_id)
Shows the dependency manifest for a manuscript node.

### changes(since_revision := 0, until_revision := null, limit := 100)
Returns live events and current composition state since a revision.

## Development

### new_subsection(session_id, section_id, payload, dependencies, expected_section_version)
Creates a local Subsection development branch. Pass dependencies explicitly; use [] for an independent Subsection.

### save_subsection(session_id, section_id, payload, dependencies, expected_section_version, expected_subsection_version)
Edits an existing Subsection by stable ID and records its direct dependencies.

### compose(session_id, node_type, node_id, body, expected_development_version, source_note)
Compresses the current development of an Article, Section, or Subsection into a canonical composition. Composition automatically depends on the current development version of the same node.

### save_research(session_id, payload, dependencies, expected_version := null)
Creates or edits a Section or Toolkit object and records its direct dependencies.

### save_document(session_id, payload, dependencies, expected_version := null)
Creates or edits a project document or Article and records its direct dependencies.

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

Development-save operations place dependencies at the operation top level. Compose operations place body, expected_development_version, and source_note at the operation top level.

### artifact_help()
Returns artifact recovery and rebuild information.

### help()
Returns the compact machine-readable interface summary.
