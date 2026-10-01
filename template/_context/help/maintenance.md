
MAINTENANCE / DISCOVERY

prune_preview(ids)
  Preview subtree size, external incoming edges, and project-state impact before removal.

trash_subtrees(worker_id,ids)
restore_subtrees(worker_id,ids)
purge_trashed_subtrees(worker_id,ids)
  Trash is reversible current-state hiding; purge is physical deletion. Project-state/focus subtrees cannot be trashed until coordination moves the live state away.

active_stages(worker_id,global=false,limit=64)
  Inspect owned/claimed transient work. global=true requires coordination mode.

rpc_signatures(name=null)
  Discover exact current public * function signatures on demand.
