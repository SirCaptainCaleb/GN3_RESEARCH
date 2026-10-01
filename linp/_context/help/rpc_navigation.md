
RPC MANUAL — NAVIGATION

Use this page when you are trying to understand where a result sits, how a route reaches it, what nearby objects exist, or when you need the exact mathematics behind an ID.

A good default progression is:
1. atlas() for the project-wide route map;
2. simplified_subtree() or simplified_ancestry() to place a target in the reasoning tree;
3. search_compact() / search_ex_v2() when you know the concept but not the ID;
4. read() for a few exact objects, or open_read()/read_more() for large bodies.

## Project orientation

### atlas
Signature: linp.atlas(p_category text DEFAULT NULL::text, p_limit integer DEFAULT 24) -> jsonb
Purpose: Read the derived semantic-container map of the project. Use this to see the main mathematical routes, interfaces, and unresolved regions before drilling into individual objects.
Parameters: p_category optionally restricts the returned Atlas category/index view; p_limit bounds returned entries.
Returns: Atlas entries in their derived conceptual order, including container summaries and status counts.
Semantics/constraints: This is the high-level map, not the provenance tree. Follow up with simplified_subtree(), simplified_ancestry(), or read() when an Atlas entry looks relevant.
Deeper help: help('atlas').

### simplified_subtree
Signature: linp.simplified_subtree(p_root_id text, p_max_depth integer DEFAULT NULL::integer) -> jsonb
Purpose: Show the reasoning descendants of one object as an indented tree of concise simplified statements. Best for asking “what did this result lead to?”
Parameters: p_root_id is the subtree root; p_max_depth limits child edges followed. NULL uses the configured default.
Returns: A compact rendered tree, node count, depth used, and an ellipsis marker when deeper descendants were omitted.
Semantics/constraints: Follows canonical parent/child reasoning structure only. It does not include cross-links or dependency edges.
Deeper help: help('simplified_subtree').

### simplified_ancestry
Signature: linp.simplified_ancestry(p_object_id text, p_max_depth integer DEFAULT NULL::integer) -> jsonb
Purpose: Show the compact route from a target back toward the reasoning root. Use this before working on a frontier result when you need to recover how the project arrived there.
Parameters: p_object_id is the target; p_max_depth bounds parent edges followed. 0 returns only the target.
Returns: Target-first ancestry with IDs, titles, simplified statements, statuses, parent IDs, depth, and truncation state.
Semantics/constraints: Canonical parent_id ancestry only; logical dependencies and other cross-links are separate.
Deeper help: help('navigation').

### ancestry
Signature: linp.ancestry(p_object_id text, p_max_depth integer DEFAULT NULL::integer, p_include_proofs boolean DEFAULT false) -> jsonb
Purpose: Detailed target-to-root ancestry when simplified statements are not enough. Use p_include_proofs only when exact route content is genuinely needed.
Parameters: p_object_id is the target; p_max_depth bounds parent edges; p_include_proofs controls inclusion of full bodies/proofs.
Returns: Exact statements, IDs/titles, parent IDs, depth, trust/version metadata, truncation state, and optionally bodies.
Semantics/constraints: Canonical parent_id ancestry only. Prefer simplified_ancestry() for orientation because it is much cheaper in context.

## Locate objects

### search_compact
Signature: linp.search_compact(p_query text, p_limit integer DEFAULT 20, p_under_id text DEFAULT NULL::text, p_include_superseded boolean DEFAULT false) -> jsonb
Purpose: Fast, compact concept search over titles, statements, and research interfaces. This is the preferred first search when you want candidate IDs without pulling body text.
Parameters: p_query is free text; p_under_id restricts results to one reasoning subtree; p_include_superseded includes replaced objects when true.
Returns: Ranked IDs/titles with short statement/interface previews and status information.
Semantics/constraints: Archive is excluded. Body text is not searched. Superseded objects are excluded by default.

### search
Signature: linp.search(p_query text, p_limit integer DEFAULT 20, p_attention text DEFAULT NULL::text, p_statement_only boolean DEFAULT false) -> jsonb
Purpose: General search when matching body text may matter. Set p_statement_only=true when you want matching to use the whole searchable object but want only title/statement pairs returned.
Parameters: p_query is free text; p_attention optionally filters attention state; p_statement_only suppresses richer result payloads.
Returns: Ranked live-object matches with snippets and status metadata, or title/statement pairs in statement-only mode.
Semantics/constraints: Uses the richer body-aware search path. Archive and superseded objects are excluded by default.

### search_ex_v2
Signature: linp.search_ex_v2(p_query text, p_limit integer DEFAULT 20, p_attention text DEFAULT NULL::text, p_under_id text DEFAULT NULL::text, p_research_level text DEFAULT NULL::text, p_mathematical_status text DEFAULT NULL::text, p_audit_status text DEFAULT NULL::text, p_object_type text DEFAULT NULL::text, p_include_superseded boolean DEFAULT false) -> jsonb
Purpose: Fully filtered search for cases where you already know the structural/status slice you want.
Parameters: In addition to free-text query and limit, filters by subtree, attention, research level, mathematical status, audit status, object type, and supersession.
Returns: Ranked matches with statement preview, snippet, research interface, statuses, score, and a read hint.
Semantics/constraints: Prefer search_compact() for ordinary discovery. Use this when filters materially reduce a large result set.

### search_ex
Signature: linp.search_ex(p_query text, p_limit integer DEFAULT 20, p_attention text DEFAULT NULL::text, p_under_id text DEFAULT NULL::text, p_research_level text DEFAULT NULL::text, p_mathematical_status text DEFAULT NULL::text, p_audit_status text DEFAULT NULL::text, p_object_type text DEFAULT NULL::text) -> jsonb
Purpose: Compatibility wrapper for filtered search without explicit supersession control.
Semantics/constraints: Prefer search_ex_v2().

### canonical_object_id
Signature: linp.canonical_object_id(p_id text) -> text
Purpose: Resolve an old/migrated/superseded object ID to the unique current live object. Useful when following older notes, archived references, or IDs copied from before migrations/recompositions.
Parameters: p_id is any known object ID or supported legacy migration ID.
Returns: The current canonical live object ID.
Semantics/constraints: Follows migration aliases and single-successor supersession chains. Raises if the object is missing or supersession branches into multiple live replacements.

## Inspect structure

### reasoning_overview
Signature: linp.reasoning_overview(p_root_id text) -> jsonb
Purpose: Inspect the immediate reasoning structure below one reasoning node without reading an entire subtree.
Parameters: p_root_id is a reasoning-node object.
Returns: Root capsule plus direct children, their reasoning node kinds, route keys/notes, and descendant counts.
Semantics/constraints: Good for choosing which branch to inspect next.

### proof_overview
Signature: linp.proof_overview(p_root_id text) -> jsonb
Purpose: Alias of reasoning_overview() retained for proof-oriented callers.
Semantics/constraints: Prefer reasoning_overview() unless the proof-oriented name is clearer in context.

### subtree
Signature: linp.subtree(p_root_id text, p_max_depth integer, p_limit integer) -> jsonb
Purpose: Structured depth-bounded tree retrieval when you need object capsules rather than the compact rendered simplified tree.
Parameters: p_root_id selects the subtree; p_max_depth bounds descendant depth; p_limit bounds returned objects.
Returns: Tree-ordered object capsules with paths/depth plus truncation metadata.
Semantics/constraints: Prefer simplified_subtree() for human/LLM orientation; use subtree() when metadata-rich object capsules are needed.

### subtree
Signature: linp.subtree(p_root_id text, p_after_path text DEFAULT NULL::text, p_limit integer DEFAULT 100) -> jsonb
Purpose: Page through an arbitrarily large subtree in canonical tree-path order.
Parameters: p_after_path is the pagination cursor returned by the previous page.
Returns: Object capsules with path/depth, page counts, and next_after_path when more remain.

### edges
Signature: linp.edges(p_id text, p_direction text DEFAULT 'both'::text, p_kinds text[] DEFAULT NULL::text[], p_limit integer DEFAULT 100) -> jsonb
Purpose: Inspect typed non-tree relations around one object—for example dependencies, supersession, route relations, or other graph edges.
Parameters: p_direction is in/out/both; p_kinds optionally restricts edge kinds; p_limit bounds results.
Returns: Matching typed relations and neighboring IDs.
Semantics/constraints: Use this when parent/child provenance is not the relation you need.

### edges_page
Signature: linp.edges_page(p_id text, p_direction text DEFAULT 'out'::text, p_kinds text[] DEFAULT NULL::text[], p_after_kind text DEFAULT NULL::text, p_after_id text DEFAULT NULL::text, p_limit integer DEFAULT 100) -> jsonb
Purpose: Paginated form of edges() for objects with many relations.
Parameters: p_after_kind and p_after_id continue from the previous page.
Returns: A stable page of typed relations plus continuation state.

## Read exact mathematics

### read
Signature: linp.read(p_ids text[], p_content text DEFAULT 'statement'::text) -> jsonb
Purpose: Fetch exact content for a small known ID set. This is the normal way to move from orientation/search into the actual mathematics.
Parameters: p_ids is a small array of object IDs; p_content selects the documented content view such as statement/summary/math/body.
Returns: Exact requested content with current object/version metadata.
Semantics/constraints: Use paged reads for large bodies or many objects.
Deeper help: help('read').

### read_preview
Signature: linp.read_preview(p_ids text[]) -> jsonb
Purpose: Check size, headings, and versions before opening a potentially large exact read.
Returns: A lightweight preview useful for deciding whether to use read(), read_section(), or a paged read.
Deeper help: help('read').

### read_section
Signature: linp.read_section(p_id text, p_heading text, p_occurrence integer DEFAULT 1) -> jsonb
Purpose: Read one exact Markdown section from a large object without loading the whole body.
Parameters: p_heading identifies the section heading; p_occurrence disambiguates repeated headings.
Returns: Exact section text plus watch/version metadata.
Deeper help: help('read').

### open_read
Signature: linp.open_read(p_worker_id bigint, p_ids text[], p_content text DEFAULT 'body'::text, p_page_chars integer DEFAULT 12000) -> jsonb
Purpose: Start a version-checked paged exact-read session for large content.
Parameters: p_worker_id owns the session; p_ids selects objects; p_content selects content; p_page_chars controls page size.
Returns: Session ID, first page/cursor, and consistency/version metadata.
Deeper help: help('read').

### open_read_ex
Signature: linp.open_read_ex(p_worker_id bigint, p_ids text[], p_content text DEFAULT 'body'::text, p_page_chars integer DEFAULT 12000, p_consistency text DEFAULT 'math'::text) -> jsonb
Purpose: Start a paged read with explicit consistency semantics.
Semantics/constraints: Prefer this when you specifically need to control consistency; otherwise open_read() is simpler.
Deeper help: help('read').

### open_read_ex_base
Signature: linp.open_read_ex_base(p_worker_id bigint, p_ids text[], p_content text DEFAULT 'body'::text, p_page_chars integer DEFAULT 12000, p_consistency text DEFAULT 'math'::text) -> jsonb
Purpose: Low-level compatibility export behind open_read_ex().
Semantics/constraints: Prefer open_read_ex().
Deeper help: help('read').

### read_page
Signature: linp.read_page(p_worker_id bigint, p_session_id bigint, p_cursor jsonb DEFAULT NULL::jsonb) -> jsonb
Purpose: Fetch the next page from an open exact-read session.
Returns: Page content, cursor, and consistency/version metadata.
Deeper help: help('read').

### read_more
Signature: linp.read_more(p_worker_id bigint, p_session_id bigint, p_max_pages integer DEFAULT 4, p_max_output_chars integer DEFAULT 50000) -> jsonb
Purpose: Consume several pages from an open read in one call when you know the remaining material is manageable.
Parameters: p_max_pages and p_max_output_chars cap context growth.
Returns: Concatenated paged content plus continuation state.
Deeper help: help('read').

### read_page_base
Signature: linp.read_page_base(p_worker_id bigint, p_session_id bigint, p_cursor jsonb DEFAULT NULL::jsonb) -> jsonb
Purpose: Low-level compatibility export behind read_page().
Semantics/constraints: Prefer read_page().
Deeper help: help('read').

### close_read
Signature: linp.close_read(p_worker_id bigint, p_session_id bigint) -> boolean
Purpose: Close an exact-read session when you are done with it.
Returns: true on successful close.
Deeper help: help('read').

### open_search
Signature: linp.open_search(p_worker_id bigint, p_query text, p_content text DEFAULT 'body'::text, p_page_chars integer DEFAULT 12000, p_attention text DEFAULT NULL::text, p_under_id text DEFAULT NULL::text, p_research_level text DEFAULT NULL::text, p_mathematical_status text DEFAULT NULL::text, p_audit_status text DEFAULT NULL::text, p_object_type text DEFAULT NULL::text) -> jsonb
Purpose: Search and immediately open the matching content as a paged read session. Useful when the result set itself, rather than a few selected hits, must be read sequentially.
Returns: A read session over matching objects.
Deeper help: help('read').

### open_subtree
Signature: linp.open_subtree(p_worker_id bigint, p_root_id text, p_content text DEFAULT 'body'::text, p_page_chars integer DEFAULT 12000) -> jsonb
Purpose: Open an entire reasoning subtree as a paged exact-read session.
Semantics/constraints: Use only when compact subtree views are insufficient; this can be large.
Deeper help: help('read').
