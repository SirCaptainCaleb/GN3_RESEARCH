# Research API

These RPCs are the worker-facing interface to live research state. The artifact is a snapshot; use the API whenever current state, exact versions, or publication matters.

## Startup and navigation

### `boot()`
Starts a research session against the current database revision. It returns the session ID required by mutation RPCs, startup notices, artifact metadata, and the snapshot revision. Call it once at startup; call it again after deliberately refreshing a stale artifact.

### `search(query, filters := {})`
Finds relevant Sections, Toolkit entries, Articles and other documents, and optionally Brainstorms by title and mathematical content. Use it for discovery, not as a substitute for reading a manuscript. Useful filters include `kind`, `toolkit_type`, `toolkit_limbo`, `article_id`, and `result_level`.

### `read(ids, math_versions := {}, cursor := null, page_chars := 9000)`
Returns exact durable content for named objects, one bounded page at a time. Reading an Article ID returns its prose document compiled from its ordered Sections with explicit Section boundaries; reading a Section ID returns that Section directly. Pass `next_cursor` back until `complete=true`; `math_versions` can request a retained prior mathematical version when available.

### `context(research_id)`
Shows how one research object sits in the mathematical structure: direct premises and consumers, supersession links, referring Articles, and originating Brainstorm. Use it when following dependencies or deciding where new work belongs.

### `changes(since_revision := 0, until_revision := null, limit := 100)`
Checks what changed after a known artifact/database revision without shipping the changed documents themselves. It returns policy/document events plus current Article and Section versions. Use it for startup freshness checks. Continue from the artifact for matching manuscript versions; call `read()` for each manuscript whose live version is newer.

### `brainstorms(active_only := true)`
Returns the compact Brainstorm collection, including seeds, status, and promotion targets. Use it to scan orthogonal ideas cheaply without searching full manuscript text.

### `dictionary()`
Returns the current canonical terminology and Review Queue in readable form. Use it before introducing or relying on project-specific terminology.

## Publishing research

### `save_research(session_id, payload, expected_version := null)`
Creates or edits a Section or Toolkit object with optimistic version checking. Use `kind: "section"` for Sections. Substantive publications must explicitly declare their dependencies; nonsubstantive edits do not change the mathematical version. New Toolkit entries begin in Toolkit Limbo.

### `save_subsection(session_id, section_id, payload, expected_section_version, expected_subsection_version)`
Edits the current hot Subsection of a Section. This is the normal path for route development. Substantive changes update the assembled Section, bump its mathematical version, and replace its declared dependencies.

### `repair_subsection(session_id, section_id, subsection_no, payload, expected_section_version, expected_subsection_version)`
Edits an older crystallized Subsection in place while preserving the Section manuscript structure. Use it when earlier text itself needs correction; ordinary continuing research belongs in the hot Subsection.

### `crystallize_subsection(session_id, section_id, expected_section_version, expected_subsection_version, next_title := '')`
Freezes the current hot Subsection and opens a new empty hot Subsection. Use it when a coherent stage of a Section is complete and the next stage should begin separately.

### `save_document(session_id, payload, expected_version := null)`
Creates or edits project documents such as Articles and the overview, with version checking and audit bookkeeping. An Article is a prose document automatically composed from an ordered Section sequence. Set `section_ids` to integrate, remove, or reorder mature Sections; the generated Article body is refreshed from that sequence.

## Brainstorms

### `save_brainstorm(session_id, payload, expected_version := null)`
Creates, edits, closes, or annotates a Brainstorm entry. Brainstorms are deliberately low-cost exploratory space and need not satisfy Toolkit or Section publication standards.

### `promote_brainstorm(session_id, brainstorm_id, payload := {}, expected_version)`
Atomically turns a developed Brainstorm into a Section and closes the Brainstorm with a link to the new Section. The promotion payload must declare the new Section's dependencies.

## Audits and chores

### `request_audit(session_id, target_type, target_id, target_version)`
Queues an independent audit of the current mathematical version of a research object or the current version of an Article. Use `article` as the target type for an Article.

### `claim_chore(session_id, kinds := {audit,maintenance})`
Claims one available audit or bounded maintenance task using a lease. Audit claims enforce independence from the authors of the mathematical version being checked.

### `finish_chore(session_id, chore_id, outcome := {})`
Completes a claimed chore. For audits it records pass/fail status and, when needed, whether optimistically retargeted consumer dependencies remain compatible.

## Atomic publication batches

Use these when one logical publication changes several shared objects together. The sequence is stage → review → commit.

### `stage_batch_chunk(session_id, batch_id, part_no, chunk)`
Stores part of a potentially large JSON publication batch. These are transport chunks for the batch payload, unrelated to mathematical Subsections. Re-staging a part invalidates any previous review.

### `review_staged_batch(session_id, batch_id)`
Parses the staged operations and reports concurrent shared-state changes since the session baseline.

### `commit_staged_batch(session_id, batch_id, overlap_checked)`
Atomically executes a reviewed staged batch.

### `discard_staged_batch(session_id, batch_id)`
Abandons an uncommitted staged batch and its stored transport chunks.

## Recovery and introspection

### `artifact_help()`
Returns the current artifact identifier and recovery instructions for rebuilding or locating the research-context artifact.

### `help()`
Returns a compact machine-readable overview of the API and conventions.
