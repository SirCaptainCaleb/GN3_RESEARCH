
WORKER LIFECYCLE

Fresh ordinary worker:
  linp.startup()
Keep the returned worker_id for the conversation.

Every subsequent user turn in the same worker run — including ordinary "Continue" and substantive follow-ups — begins with:
  linp.continue(worker_id)
Do this before further project work. The call refreshes the scheduler assignment and project delta while preserving the same run. If last_seen_revision is unavailable, pass NULL rather than skipping the refresh. If delta.has_more=true, consume the remaining change pages before treating state as current.

"Continue" means keep the same mathematical line unless refreshed state says otherwise; it does not mean reuse stale project state.

To advance at an assignment boundary:
  linp.continue(worker_id,outcome,details)
Use outcome DEFER to skip the current assignment.

special reasoning mode is a separate session:


special reasoning mode activity refreshes the session's publication lease marker. If special reasoning mode disappears after fully verifying a stage, that verified stage may be handed to an ordinary worker for commit-only recovery after one normal claim TTL. Unverified special reasoning mode scratch is not recovered.

linp.continue(..., outcome, details) is an in-turn transition as well as a conversation lifecycle transition. When a routine assignment finishes and useful turn budget remains, advance immediately rather than returning just because the first assignment ended.

Use linp.next_retry(worker_id,old_claim_id) to recover a lost transition response; never replay a completed continue(..., outcome, details) transition.



- verified special reasoning mode stages are recovered commit-only by ordinary workers;
- unverified special reasoning mode scratch is discarded;
- after verified work is committed or no verified work exists, the stale handoff is released and a fresh special reasoning mode request is required.
This recovery path is allowed under an special reasoning mode usage veto because it consumes no special reasoning mode usage.


RUN RETENTION, RECYCLING, AND COMPACTION

Runs are a bounded resumable working set, not an append-only set of live scheduler slots.

- max_runs means maximum retained ACTIVE runs. The shared default is 128.
- A live claim, live presence, active special reasoning mode ownership, or unhandoffable unverified stage protects a run from recycling.
- Lease-expired unprotected runs are marked recycled rather than deleted.
- Under capacity pressure, the scheduler preferentially recycles the oldest idle run; after the grace preference is exhausted it may recycle the oldest otherwise eligible inactive-work run rather than failing startup.
- Only when all retained slots are genuinely protected/live does capacity reject a new run.
- Recycled, superseded, released, or completed runs older than the configured compaction age are compacted to small historical tombstones. Run history is not lifecycle-deleted.
- Returning to a recycled or compacted worker_id through continue(...) transparently obtains a fresh scheduler assignment and reports reinitialized/run_rehydrated state, while preserving small revision/history metadata.
- Explicit begin_research_batch(...) remains a semantic wave transition, not routine run garbage collection.


RUN TERMINAL-STATE VOCABULARY

Run status records why a run stopped being active:
- superseded: a newer scheduler/batch/operator transition replaced the run's previous assignment;
- released: the worker explicitly relinquished the run via release();
- recycled: capacity/lease lifecycle retired an unprotected run automatically;
- completed: the run reached a genuine completed lifecycle state;
- compacted: an older inactive run was reduced to its historical tombstone.

The old reassigned run status is obsolete and is not an allowed database value. Transition responses use assignment_changed as the canonical field. The legacy reassigned boolean remains temporarily as a deprecated compatibility alias with the same value; it is not a persisted run lifecycle status.


TRANSITION RESPONSE COMPATIBILITY

Canonical transition fields are assignment_changed and previous_assignment. Legacy reassigned and reassigned_from fields remain temporarily as deprecated compatibility aliases with identical semantics. New code should use the canonical names.
