
WORKER LIFECYCLE

Fresh ordinary worker:
  __template__.startup()
Keep the returned worker_id for the conversation.

Normal user "continue":
  __template__.sync(worker_id,last_seen_revision)
This preserves the conversation's mathematical run across short ownership leases when possible and returns a compact delta.

At a genuine mathematical/mode boundary:
  __template__.next(worker_id,outcome,details)
The current assignment closes and asynchronous scheduling chooses the next useful mode.

Known outcomes include completed, deferred, blocked, superseded and the documented research/methodology transition signals.

special reasoning mode is separate:



TURN CONTINUITY

__template__.next(...) is an in-turn transition as well as a conversation lifecycle transition. When a routine assignment finishes and useful turn budget remains, call it immediately and keep working on the returned assignment rather than returning merely because the first assignment ended. Audit batches should normally be exhausted before __template__.next(completed).


NEW RESEARCHER BATCH / WAVE

Normal operation: tell workers to Continue. Claims/runs retain ordinary continuity and lease semantics.

At the deliberate beginning of a new researcher batch, tell the first new worker explicitly that it is the beginning of a new batch. That worker calls __template__.begin_research_batch(worker_id, note) once.


The announcing worker itself is not retired. After the cutover it receives a fresh scheduler assignment. Other displaced worker IDs are remembered only for the current batch so zombie/late-returning workers cannot silently re-enlist themselves.

Repeated batch announcements within ten minutes are idempotent no-ops, protecting against several newly launched workers receiving the same operator message.
