# Research API

## Startup and live reads
- `boot()`: once per independent conversation; preserve returned session_id for every write.
- `status()`: live project revision, Articles, Sections, and composition dependency states.
- `changes(since_revision, until_revision := null, limit := 100)`: local project revision events; use artifact snapshot revision at startup.
- `search(query, filters := {})`, `read(ids, math_versions := {}, cursor := null, page_chars := 9000)`, `context(research_id)`, `items(subsection_id)`, `read_item(item_id)`: research content.
- `composition_status(node_type,node_id)` and `dependencies(node_type,node_id)`: direct composition dependencies and source coverage.
- `artifact_help()` and `help()`: artifact and interface metadata.

## Atomic Items, consumption, and composition
Items are atomic nodes under Subsections with one body and optional mathematical status; the Result node type is retired. `new_item(session_id,subsection_id,payload)` takes id, kind, title, status, body; `save_item(session_id,item_id,payload,expected_version)` updates by optimistic version. `new_item_result` and `save_item_result` reject writes. `item_results` and `article_results` are legacy read names.

`set_consumes(session_id,parent_id,child_ids)` and `set_consumed_by(session_id,child_id,consumer_ids)` replace mathematical-consumption lists transactionally; preserve existing relationships when extending them.

`compose(session_id,node_type,node_id,payload,expected_composition_version)` applies only to Subsections, Sections, and Articles. The payload contains body and explicit depends_on direct-child IDs. Pass NULL only when absent; then use current composition version. Compose selectively when rigorous mathematical exposition is ready.

`new_subsection`, `save_subsection`, `save_research`, `save_document`, `save_brainstorm`, `promote_brainstorm` perform structured development. `stage_batch_chunk`, `review_staged_batch`, `commit_staged_batch`, `discard_staged_batch` support atomic publication. `claim_chore`, `finish_chore`, and `request_audit` support stewardship.
