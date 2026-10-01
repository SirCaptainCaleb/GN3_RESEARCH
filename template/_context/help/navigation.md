
RICH ON-DEMAND NAVIGATION

atlas()
  Complete conceptual Atlas derived from live semantic-container boundaries. It returns every eligible semantic container, hierarchically ordered. atlas_height affects prominence/order only and never controls membership.

atlas(object_or_container_id)
  Conceptual Atlas subtree beneath that object. Targeted subtree entries additionally include their direct member object IDs.

atlas('pending') / atlas('obstructed')
  Conceptual containers with direct pending-audit or obstructed/blocked members.

atlas(classification)
  Conceptual containers represented by the requested object_type, research_level, mathematical_status, audit_status, or support_status.

atlas('all',limit)
  Paginated raw eligible-object index for exhaustive object-level navigation. aliases: objects, raw.

simplified_subtree(root_id,max_depth=null)
  Compact indented tree of object IDs plus simplified_statement. max_depth defaults from subtree.simplified_default_depth. A … child marker means that branch has deeper descendants omitted by the depth limit.

edges(id,direction='both',kinds=null,limit=100)
  Direct logical and research-influence dependencies/dependents.

subtree(root_id,after_path=null,limit=100)
  Canonical nonrecursive tree_path pagination over the current hierarchy.

subtree(root_id,max_depth,limit)
  Depth-bounded compatibility/navigation form. Returns the root and descendants whose relative depth is at most max_depth, up to limit.

open_subtree(worker_id,root_id,content='body',page_chars=12000)
  Open a transient exact-read cursor over a subtree.

search_ex(query,limit,attention,under_id,research_level,mathematical_status,audit_status,object_type)
  Filtered current-state search returning compact capsules.

open_search(...)
  Same selection idea, but opens a transient exact-content cursor.

changes_since(since_revision,after_revision=null,limit=100)
  Bounded logical journal paging.

work_digest(since_revision=null,focus_ids=null)
  Compact global/current-focus digest for coordination or deliberate broad review.

storage_report()
  Current replacement-system footprint and row counts; Atlas is derived from semantic containers rather than materialized.


simplified_ancestry(object_id,max_depth=null)
  Walk upward from a target object through canonical reasoning-tree parents, returning target-first IDs/titles plus simplified_statement. depth 0 is the target; max_depth bounds parent edges followed. Reports truncated=true when more live ancestors exist.

ancestry(object_id,max_depth=null,include_proofs=false)
  Exact target-to-root reasoning chain. Returns full statement text and trust/version metadata for each node; set include_proofs=true to include each node body/proof. Uses the same depth semantics and truncation marker as simplified_ancestry.
