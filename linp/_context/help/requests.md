
SOFT ASSIGNMENT REQUESTS

Assignment requests express intent to the scheduler; they do not create or override an assignment.

General form:
  linp.request_assignment(
    worker_id,
    intent_jsonb,
    priority,
    timing,
    scope
  )

intent may contain:
- role: researcher | auditor | coordinator;
- mode: research | audit | coordination | proof_rehearsal | methodology_review | literature_bridge;
- task: a concise requested objective;
- focus_id: preferred live object;
- target_ids: preferred live objects.

priority is a preference strength from 0 to 100, not authority. Internally its scheduler contribution is deliberately capped below hard recovery work. A high-priority project need, audit pressure, verified-stage recovery, special reasoning mode state, audit independence, collisions, and other hard constraints can still win.

timing:
- next_boundary: apply at the next genuine assignment boundary;
- now_if_safe: record stronger intent to pivot promptly, but never destroy a live claim automatically. Finish or safely hand off the current mathematical unit, then transition normally.

scope:
- next_assignment: one scheduler attempt for this worker;
- this_worker: retain across this worker's future assignment boundaries until satisfied or expired;
- until_satisfied: persistent soft intent, including project-scoped use when no target worker is supplied;
- next_worker: project-scoped intent for the next eligible dispatch.

The scheduler records a disposition:
- satisfied;
- partially_satisfied;
- deferred;
- superseded;
- cancelled;
- expired.

Inspect recent intent with:
  linp.assignment_request_status(worker_id)

Cancel pending intent with:
  linp.cancel_assignment_request(worker_id,request_id)

Requests and project needs are different:
- a need says the project needs work done;
- a request says a worker/operator prefers a particular assignment if sensible.

force_role(...) remains an exceptional administrative bypass. Do not use it for ordinary steering.
