RPC MANUAL — NAVIGATION

### atlas
Signature: __template__.atlas(p_category text DEFAULT NULL::text, p_limit integer DEFAULT 24) -> jsonb
Purpose: Navigate the derived semantic-container Atlas or raw eligible-object index.
Parameters: p_category text DEFAULT NULL::text, p_limit integer DEFAULT 24
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('atlas').

### brainstorm_recent
Signature: __template__.brainstorm_recent(p_limit integer DEFAULT 2, p_revision_window bigint DEFAULT 200) -> jsonb
Purpose: Brainstorm Recent operation on the managed project API.
Parameters: p_limit integer DEFAULT 2, p_revision_window bigint DEFAULT 200
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### canonical_object_id
Signature: __template__.canonical_object_id(p_id text) -> text
Purpose: Canonical Object Id operation on the managed project API.
Parameters: p_id text
Returns: text scalar.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### close_read
Signature: __template__.close_read(p_worker_id bigint, p_session_id bigint) -> boolean
Purpose: Consume or close an exact-read session.
Parameters: p_worker_id bigint, p_session_id bigint
Returns: boolean scalar.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('read').

### dependency_repair_candidates
Signature: __template__.dependency_repair_candidates(p_limit integer DEFAULT 12) -> jsonb
Purpose: Return structural/repair candidates for human review.
Parameters: p_limit integer DEFAULT 12
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### edges
Signature: __template__.edges(p_id text, p_direction text DEFAULT 'both'::text, p_kinds text[] DEFAULT NULL::text[], p_limit integer DEFAULT 100) -> jsonb
Purpose: Read typed relations around an object.
Parameters: p_id text, p_direction text DEFAULT 'both'::text, p_kinds text[] DEFAULT NULL::text[], p_limit integer DEFAULT 100
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### edges_page
Signature: __template__.edges_page(p_id text, p_direction text DEFAULT 'out'::text, p_kinds text[] DEFAULT NULL::text[], p_after_kind text DEFAULT NULL::text, p_after_id text DEFAULT NULL::text, p_limit integer DEFAULT 100) -> jsonb
Purpose: Read typed relations around an object.
Parameters: p_id text, p_direction text DEFAULT 'out'::text, p_kinds text[] DEFAULT NULL::text[], p_after_kind text DEFAULT NULL::text, p_after_id text DEFAULT NULL::text, p_limit integer DEFAULT 100
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### open_read
Signature: __template__.open_read(p_worker_id bigint, p_ids text[], p_content text DEFAULT 'body'::text, p_page_chars integer DEFAULT 12000) -> jsonb
Purpose: Open a version-checked paged exact-read session.
Parameters: p_worker_id bigint, p_ids text[], p_content text DEFAULT 'body'::text, p_page_chars integer DEFAULT 12000
Returns: JSON session/page payload with cursor/content plus consistency/version metadata.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('read').

### open_read_ex
Signature: __template__.open_read_ex(p_worker_id bigint, p_ids text[], p_content text DEFAULT 'body'::text, p_page_chars integer DEFAULT 12000, p_consistency text DEFAULT 'math'::text) -> jsonb
Purpose: Open a version-checked paged exact-read session.
Parameters: p_worker_id bigint, p_ids text[], p_content text DEFAULT 'body'::text, p_page_chars integer DEFAULT 12000, p_consistency text DEFAULT 'math'::text
Returns: JSON session/page payload with cursor/content plus consistency/version metadata.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('read').

### open_read_ex_base
Signature: __template__.open_read_ex_base(p_worker_id bigint, p_ids text[], p_content text DEFAULT 'body'::text, p_page_chars integer DEFAULT 12000, p_consistency text DEFAULT 'math'::text) -> jsonb
Purpose: Open a version-checked paged exact-read session.
Parameters: p_worker_id bigint, p_ids text[], p_content text DEFAULT 'body'::text, p_page_chars integer DEFAULT 12000, p_consistency text DEFAULT 'math'::text
Returns: JSON session/page payload with cursor/content plus consistency/version metadata.
Semantics/constraints: Low-level/compatibility export; prefer the ordinary/newest documented wrapper.
Deeper help: help('read').

### open_search
Signature: __template__.open_search(p_worker_id bigint, p_query text, p_content text DEFAULT 'body'::text, p_page_chars integer DEFAULT 12000, p_attention text DEFAULT NULL::text, p_under_id text DEFAULT NULL::text, p_research_level text DEFAULT NULL::text, p_mathematical_status text DEFAULT NULL::text, p_audit_status text DEFAULT NULL::text, p_object_type text DEFAULT NULL::text) -> jsonb
Purpose: Open a paged read session over search results.
Parameters: p_worker_id bigint, p_query text, p_content text DEFAULT 'body'::text, p_page_chars integer DEFAULT 12000, p_attention text DEFAULT NULL::text, p_under_id text DEFAULT NULL::text, p_research_level text DEFAULT NULL::text, p_mathematical_status text DEFAULT NULL::text, p_audit_status text DEFAULT NULL::text, p_object_type text DEFAULT NULL::text
Returns: JSON session/page payload with cursor/content plus consistency/version metadata.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('read').

### open_subtree
Signature: __template__.open_subtree(p_worker_id bigint, p_root_id text, p_content text DEFAULT 'body'::text, p_page_chars integer DEFAULT 12000) -> jsonb
Purpose: Open a paged read session over a subtree.
Parameters: p_worker_id bigint, p_root_id text, p_content text DEFAULT 'body'::text, p_page_chars integer DEFAULT 12000
Returns: JSON session/page payload with cursor/content plus consistency/version metadata.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('read').

### proof_overview
Signature: __template__.proof_overview(p_root_id text) -> jsonb
Purpose: Return a compact structural overview rooted at an object.
Parameters: p_root_id text
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### read
Signature: __template__.read(p_ids text[], p_content text DEFAULT 'statement'::text) -> jsonb
Purpose: Read exact requested content for a small ID set.
Parameters: p_ids text[], p_content text DEFAULT 'statement'::text
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('read').

### read_more
Signature: __template__.read_more(p_worker_id bigint, p_session_id bigint, p_max_pages integer DEFAULT 4, p_max_output_chars integer DEFAULT 50000) -> jsonb
Purpose: Consume or close an exact-read session.
Parameters: p_worker_id bigint, p_session_id bigint, p_max_pages integer DEFAULT 4, p_max_output_chars integer DEFAULT 50000
Returns: JSON session/page payload with cursor/content plus consistency/version metadata.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('read').

### read_page
Signature: __template__.read_page(p_worker_id bigint, p_session_id bigint, p_cursor jsonb DEFAULT NULL::jsonb) -> jsonb
Purpose: Consume or close an exact-read session.
Parameters: p_worker_id bigint, p_session_id bigint, p_cursor jsonb DEFAULT NULL::jsonb
Returns: JSON session/page payload with cursor/content plus consistency/version metadata.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('read').

### read_page_base
Signature: __template__.read_page_base(p_worker_id bigint, p_session_id bigint, p_cursor jsonb DEFAULT NULL::jsonb) -> jsonb
Purpose: Consume or close an exact-read session.
Parameters: p_worker_id bigint, p_session_id bigint, p_cursor jsonb DEFAULT NULL::jsonb
Returns: JSON session/page payload with cursor/content plus consistency/version metadata.
Semantics/constraints: Low-level/compatibility export; prefer the ordinary/newest documented wrapper.
Deeper help: help('read').

### read_preview
Signature: __template__.read_preview(p_ids text[]) -> jsonb
Purpose: Preview size/version/headings before a large read.
Parameters: p_ids text[]
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('read').

### read_section
Signature: __template__.read_section(p_id text, p_heading text, p_occurrence integer DEFAULT 1) -> jsonb
Purpose: Read one exact Markdown section with watch metadata.
Parameters: p_id text, p_heading text, p_occurrence integer DEFAULT 1
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('read').

### reasoning_diagnostics
Signature: __template__.reasoning_diagnostics(p_limit integer DEFAULT 100) -> jsonb
Purpose: Return structural/repair candidates for human review.
Parameters: p_limit integer DEFAULT 100
Returns: JSON report with status/details/findings.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### reasoning_overview
Signature: __template__.reasoning_overview(p_root_id text) -> jsonb
Purpose: Return a compact structural overview rooted at an object.
Parameters: p_root_id text
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### search
Signature: __template__.search(p_query text, p_limit integer DEFAULT 20, p_attention text DEFAULT NULL::text, p_statement_only boolean DEFAULT false) -> jsonb
Purpose: Search live objects; extended variants add filters/supersession controls.
Parameters: p_query text, p_limit integer DEFAULT 20, p_attention text DEFAULT NULL::text, p_statement_only boolean DEFAULT false
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### search_compact
Signature: __template__.search_compact(p_query text, p_limit integer DEFAULT 20, p_under_id text DEFAULT NULL::text, p_include_superseded boolean DEFAULT false) -> jsonb
Purpose: Search live objects; extended variants add filters/supersession controls.
Parameters: p_query text, p_limit integer DEFAULT 20, p_under_id text DEFAULT NULL::text, p_include_superseded boolean DEFAULT false
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### search_ex
Signature: __template__.search_ex(p_query text, p_limit integer DEFAULT 20, p_attention text DEFAULT NULL::text, p_under_id text DEFAULT NULL::text, p_research_level text DEFAULT NULL::text, p_mathematical_status text DEFAULT NULL::text, p_audit_status text DEFAULT NULL::text, p_object_type text DEFAULT NULL::text) -> jsonb
Purpose: Search live objects; extended variants add filters/supersession controls.
Parameters: p_query text, p_limit integer DEFAULT 20, p_attention text DEFAULT NULL::text, p_under_id text DEFAULT NULL::text, p_research_level text DEFAULT NULL::text, p_mathematical_status text DEFAULT NULL::text, p_audit_status text DEFAULT NULL::text, p_object_type text DEFAULT NULL::text
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### search_ex_v2
Signature: __template__.search_ex_v2(p_query text, p_limit integer DEFAULT 20, p_attention text DEFAULT NULL::text, p_under_id text DEFAULT NULL::text, p_research_level text DEFAULT NULL::text, p_mathematical_status text DEFAULT NULL::text, p_audit_status text DEFAULT NULL::text, p_object_type text DEFAULT NULL::text, p_include_superseded boolean DEFAULT false) -> jsonb
Purpose: Search live objects; extended variants add filters/supersession controls.
Parameters: p_query text, p_limit integer DEFAULT 20, p_attention text DEFAULT NULL::text, p_under_id text DEFAULT NULL::text, p_research_level text DEFAULT NULL::text, p_mathematical_status text DEFAULT NULL::text, p_audit_status text DEFAULT NULL::text, p_object_type text DEFAULT NULL::text, p_include_superseded boolean DEFAULT false
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Stronger/current guarded variant where specialized help recommends it.

### ancestry
Signature: __template__.ancestry(p_object_id text, p_max_depth integer DEFAULT NULL::integer, p_include_proofs boolean DEFAULT false) -> jsonb
Purpose: Walk the canonical reasoning-tree parent chain from a target toward the root, target first.
Parameters: p_object_id text; p_max_depth bounds parent edges followed (0 = target only; NULL uses the configured simplified navigation default); p_include_proofs controls whether exact object bodies/proofs are included.
Returns: Exact statement text, IDs/titles, parent IDs, depth, trust/version metadata, truncation state, and optionally bodies/proofs.
Semantics/constraints: Follows only canonical parent_id ancestry; cross-links/dependencies are not included.
Deeper help: help('navigation').

### simplified_ancestry
Signature: __template__.simplified_ancestry(p_object_id text, p_max_depth integer DEFAULT NULL::integer) -> jsonb
Purpose: Compact target-to-root canonical ancestry for elevation and proof-route orientation.
Parameters: p_object_id text; p_max_depth bounds parent edges followed (0 = target only; NULL uses the configured simplified navigation default).
Returns: IDs/titles, simplified_statement, statuses, depth, parent IDs, and truncation state.
Semantics/constraints: Follows only canonical parent_id ancestry; cross-links/dependencies are not included.
Deeper help: help('navigation').

### simplified_subtree
Signature: __template__.simplified_subtree(p_root_id text, p_max_depth integer DEFAULT NULL::integer) -> jsonb
Purpose: Render a compact depth-bounded reasoning subtree.
Parameters: p_root_id text, p_max_depth integer DEFAULT NULL::integer
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('simplified_subtree').

### standardization_dictionary
Signature: __template__.standardization_dictionary() -> jsonb
Purpose: Return project-local vocabulary rules.
Parameters: (none)
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### subtree
Signature: __template__.subtree(p_root_id text, p_after_path text DEFAULT NULL::text, p_limit integer DEFAULT 100) -> jsonb
Purpose: Navigate a hierarchy subtree by path pagination or depth bound.
Parameters: p_root_id text, p_after_path text DEFAULT NULL::text, p_limit integer DEFAULT 100
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### subtree
Signature: __template__.subtree(p_root_id text, p_max_depth integer, p_limit integer) -> jsonb
Purpose: Navigate a hierarchy subtree by path pagination or depth bound.
Parameters: p_root_id text, p_max_depth integer, p_limit integer
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### trust_report
Signature: __template__.trust_report(p_id text) -> jsonb
Purpose: Report trust/certification/dependency state.
Parameters: p_id text
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### unary_chain_candidates
Signature: __template__.unary_chain_candidates(p_min_length integer DEFAULT 3, p_limit integer DEFAULT 64) -> jsonb
Purpose: Return structural/repair candidates for human review.
Parameters: p_min_length integer DEFAULT 3, p_limit integer DEFAULT 64
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Heuristic review output, never an automatic merge/delete instruction.

### unary_cleanup_candidates
Signature: __template__.unary_cleanup_candidates(p_min_chain_length integer DEFAULT 3, p_limit integer DEFAULT 64) -> jsonb
Purpose: Return structural/repair candidates for human review.
Parameters: p_min_chain_length integer DEFAULT 3, p_limit integer DEFAULT 64
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Heuristic review output, never an automatic merge/delete instruction.
