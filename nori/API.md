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

## NORI coordination
- `coordination_strategy()`: live scope, obligations, active claims, parked approaches, decisive updates, stale/freshness signals, and exact evidence.
- `coordination_metrics()`: prospective coordination indicators.
- `coordination_claim(session,objective_id,target_key,question,method,decision_enabled,role,selection,lease_minutes := 90)`: transactional target claim. Role: primary_proof, independent_verification, alternative_method, counterexample_search, synthesis, or exploration. Selection JSON requires target, consequence, remaining_gap, decisive_step, alternative.
- `coordination_checkpoint(session,task_id,checkpoint,lease_minutes := 90)`: checkpoint and renewal; JSON requires mathematical_change, obligation_effect, next_step, alternative_comparison. Optional bridge_unchanged tracks repeated unchanged central obligations.
- `coordination_finish(session,task_id,outcome,decision)`: outcome JSON requires mathematical_change, evidence, remaining_bridge, next_step, alternative_comparison; decision: continue, park, resolve, switch.
- `coordination_publish_update(session,kind,objectives,item_versions,discovery,implication,priority_change,evidence := [],reopening_condition := null)`: records mathematical and strategic impact with exact currently valid Item versions, notifying active dependent claims.
- `coordination_commit_batch_update(session,batch_id,overlap_checked,kind,objective_ids,item_versions,discovery,implication,priority_change,evidence := [],reopening_condition := null)`: commits a staged mathematical publication and its strategic consequences in one transaction; Item versions are checked after manuscript commit and rollback together on failure.
- `coordination_decide_versioned(session,objective_id,expected_revision,state,truth_status,reason,reopening_condition := null)`: optimistic objective lifecycle changes; state proposed/active/parked/resolved. Track truth independently.
- `coordination_prioritize(session,objective_id,expected_revision,priority_rank,selection_assessment,selection_rationale)`: optimistic ranking and documented comparison; assessment JSON requires mathematical_relevance, tractability, information_gain, reuse, expected_effort, active_overlap, strongest_alternative.
- `coordination_record_baseline(session,snapshot_revision)`: dated inventory and obligations.
- `coordination_relationships`: evidence-backed strengthening, duplication, refutation, and transfer relationships (maintained by research stewards).

At task selection state the exact assertion, consequence, remaining closure gap, decisive test, and strongest alternative. Compare relevance, tractability, information, reuse, effort, and active overlap. Reassess after a decisive result, failed attempt, significant update, or session end. Two bridge-unchanged extensions trigger review, with room for justified persistence.

Research Items and Article compositions remain the mathematical record. Preserve source versions and provenance, and synthesize selectively.
