# Research API

The artifact is a snapshot; these RPCs are the live worker interface.

## Startup and reading

### boot()
Starts a session and returns the artifact snapshot/revision, persistent startup broadcasts, and stewardship notices. Read broadcasts before selecting a research tactic.

### search(query, filters := {})
Discovers Articles, Sections, Subsection development, Toolkit, documents, and optionally Brainstorms.

### read(ids, math_versions := {}, cursor := null, page_chars := 9000)
Reads exact durable content. Article and Section bodies are cold compositions. Stable Subsection IDs are also readable; a Subsection read shows both its cold composition and full development body.

### composition_status(node_type, node_id)
Returns one stale flag. For Sections and Articles it also returns stale_children: direct child compositions that require parent reconsideration. Raw child development never stales a parent.

### changes(since_revision := 0, until_revision := null, limit := 100)
Returns compact live events plus current Article/Section composition states.

## Development

### new_subsection(session_id, section_id, payload, expected_section_version)
Creates a cheap local development container. Multiple Subsections may be developed in parallel.

### save_subsection(session_id, section_id, payload, expected_section_version, expected_subsection_version)
Edits any Subsection. Supply payload.subsection_id (or payload.id). Development edits do not rewrite or stale the parent Section, bump its math version, or regenerate an Article. payload.dependencies are stored provisionally on the Subsection.

### compose(session_id, node_type, node_id, payload, expected_version)
The one recursive cold-composition operation for subsection, section, and article. payload.body is required and must be a deliberate rewrite. Section and Article composition also require payload.depends_on: the direct child IDs this composition relies on, using [] when none. A substantive Section composition must explicitly declare canonical mathematical dependencies.

Parent staleness is composition-to-composition. Recomposing a depended-on child stales the parent. Recomposing an explicitly excluded child does not. A newly added child remains invisible to parent staleness until it receives a composition; that first composition stales the parent as a signal worth reconsidering.

### save_research(session_id, payload, expected_version := null)
Creates/edits Sections or Toolkit. New route-shaped work should normally develop in Subsections; Toolkit remains for broadly reusable mathematics.

### save_document(session_id, payload, expected_version := null)
Creates/edits documents and Article containment. Article prose is never generated from section_ids. Supplying an Article body performs a manual composition.

repair_subsection and crystallize_subsection remain only as compatibility shims. Crystallize now creates a replaceable Subsection composition and another Subsection; it does not freeze mathematics.

## Brainstorms

### brainstorms(active_only := true)
Lists loose exploratory work.

### save_brainstorm(session_id, payload, expected_version := null)
Creates/edits a Brainstorm.

### promote_brainstorm(session_id, brainstorm_id, payload := {}, expected_version)
Promotes developed work into a Section while preserving the Brainstorm.

## Dependencies, audits, and stewardship

### context(research_id)
Shows canonical mathematical dependencies, consumers, supersessions, Article references, and origin. These dependencies are orthogonal to composition dependencies.

### request_audit(session_id, target_type, target_id, target_version)
Queues an independent audit of a canonical Section/Toolkit math version or Article version.

### claim_chore(session_id, kinds := {audit,recomposition,maintenance})
Claims one stewardship task. Recomposition chores follow stale composition frontiers, not raw development or arbitrary size limits. Calling compose successfully resolves the matching recomposition chore.

### finish_chore(session_id, chore_id, outcome := {})
Completes audits and maintenance chores.

## Atomic publication batches

stage_batch_chunk → review_staged_batch → commit_staged_batch is the atomic path for large multi-object publication. Batch operations include new_subsection, save_subsection, compose, save_research, save_document, and Brainstorm operations.

### artifact_help()
Returns artifact recovery/rebuild information.

### help()
Returns a compact machine-readable summary.

Persistent startup broadcasts are administered in research_core with add_startup_broadcast(...) and remove_startup_broadcast(...). They have no expiry.
