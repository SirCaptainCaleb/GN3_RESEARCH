# Research API

These RPCs are the worker-facing interface to live research state. The artifact is a snapshot; use the API whenever current state, exact versions, or publication matters.

## Startup and navigation

### `boot()`
Starts a research session against the current database revision. It returns the session ID required by mutation RPCs, startup notices, artifact metadata, and the snapshot revision. Call it once at startup; call it again after deliberately refreshing a stale artifact.

### `search(query, filters := {})`
Finds relevant Research Lines, Toolkit entries, documents, and optionally Brainstorms by title and mathematical content. Use it for discovery, not as a substitute for reading a manuscript. Useful filters include `kind`, `toolkit_type`, `toolkit_limbo`, `main_line_id`, and `result_level`.

### `read(ids, math_versions := {}, cursor := null, page_chars := 9000)`
Returns exact durable content for named objects, one bounded page at a time. Reading a Main Line ID compiles its ordered Research Line sequence with explicit Research Line boundaries; reading a Research Line ID returns that segment directly. Pass `next_cursor` back until `complete=true`; `math_versions` can request a retained prior mathematical version when available.

### `context(research_id)`
Shows how one research object sits in the mathematical structure: direct premises and consumers, parent/child Research Lines, supersession links, referring Main Lines, and originating Brainstorm. Use it when following dependencies or deciding where new work belongs.

### `changes(since_revision := 0, until_revision := null, limit := 100)`
Checks what changed after a known artifact/database revision without shipping the changed documents themselves. It returns policy/document events plus current Main Line and Research Line versions. Use it for startup freshness checks. Continue from the artifact for matching manuscript versions; call `read()` for each manuscript whose live version is newer.

### `brainstorms(active_only := true)`
Returns the compact Brainstorm collection, including seeds, status, and promotion targets. Use it to scan orthogonal ideas cheaply without searching full manuscript text.

### `dictionary()`
Returns the current canonical terminology and Review Queue in readable form. Use it before introducing or relying on project-specific terminology.

## Publishing research

### `save_research(session_id, payload, expected_version := null)`
Creates or edits a Research Line or Toolkit object with optimistic version checking. Substantive publications must explicitly declare their dependencies; nonsubstantive edits do not change the mathematical version. New Toolkit entries begin in Toolkit Limbo. An independent reviewer promotes an entry by a nonsubstantive edit setting `toolkit_limbo=false`.

### `save_line_chunk(session_id, line_id, payload, expected_line_version, expected_chunk_version)`
Edits the current hot chunk of a Research Line. This is the normal path for route development. Substantive changes update the assembled line, bump its mathematical version, and replace its declared dependencies.

### `repair_line_chunk(session_id, line_id, chunk_no, payload, expected_line_version, expected_chunk_version)`
Edits an older crystallized chunk in place while preserving the chunked manuscript structure. Use it only when earlier text itself needs correction; ordinary continuing research belongs in the hot chunk.

### `crystallize_line_chunk(session_id, line_id, expected_line_version, expected_chunk_version, next_title := '')`
Freezes the current hot chunk as a completed manuscript section and opens a new empty hot chunk. Use it when a coherent stage of a Research Line is complete and the next stage should begin separately.

### `save_document(session_id, payload, expected_version := null)`
Creates or edits project documents such as Main Lines and the overview, with version checking and audit bookkeeping. Main Line content is an ordered Research Line sequence: set `research_line_ids` to integrate, remove, or reorder mature Research Lines. Main Line prose is compiled from those Research Lines rather than stored independently.

## Brainstorms

### `save_brainstorm(session_id, payload, expected_version := null)`
Creates, edits, closes, or annotates a Brainstorm entry. Brainstorms are deliberately low-cost exploratory space and need not satisfy Toolkit or Research Line publication standards.

### `promote_brainstorm(session_id, brainstorm_id, payload := {}, expected_version)`
Atomically turns a developed Brainstorm into a Research Line and closes the Brainstorm with a link to the new line. The promotion payload must declare the new line's dependencies.

## Audits and chores

### `request_audit(session_id, target_type, target_id, target_version)`
Queues an independent audit of the current mathematical version of a research object or the current version of a Main Line. The target version is explicit so an audit cannot silently drift onto newer work.

### `claim_chore(session_id, kinds := {audit,maintenance})`
Claims one available audit or bounded maintenance task using a lease. Audit claims enforce independence from the authors of the mathematical version being checked.

### `finish_chore(session_id, chore_id, outcome := {})`
Completes a claimed chore. For audits it records pass/fail status and, when needed, whether optimistically retargeted consumer dependencies remain compatible.

## Atomic publication batches

Use these when one logical publication changes several shared objects together. The sequence is stage → review → commit; do not bypass it for substantial multi-object publication.

### `stage_batch_chunk(session_id, batch_id, part_no, chunk)`
Stores part of a potentially large JSON publication batch. Re-staging a part invalidates any previous review of that batch.

### `review_staged_batch(session_id, batch_id)`
Parses the staged operations and reports concurrent shared-state changes since the session baseline. Use the result to check mathematical overlap before committing.

### `commit_staged_batch(session_id, batch_id, overlap_checked)`
Atomically executes a reviewed staged batch. It refuses to commit if the batch changed after review or if another session changed shared research after the overlap review.

### `discard_staged_batch(session_id, batch_id)`
Abandons an uncommitted staged batch and its stored chunks. Use it when a proposed publication is obsolete or must be rebuilt from scratch.

## Recovery and introspection

### `artifact_help()`
Returns the current artifact identifier and recovery instructions for rebuilding or locating the research-context artifact. This is an exceptional recovery path, not part of ordinary research.

### `help()`
Returns a compact machine-readable overview of the API and conventions. Prefer this Markdown reference for normal reading; use `help()` when the artifact is unavailable or you suspect the live API has changed since the snapshot.
