
QUIET TTL PRESENCE

Presence prevents wasteful concurrent coordination without becoming an activity feed.

linp.begin_reasoning_activity(worker_id,activity,scope_id,message,exclusive=true,ttl_minutes=null)
  activity = compose | restructure | rehearse

Composition/restructure publication may be exclusive on overlapping tree scopes. Independent proof rehearsal is intentionally nonexclusive: several workers may attempt genuinely independent full proofs of the same root.

linp.announce(...)
  Lower-level general presence API.

linp.presence(scope_id,global=false,limit=32)
  Inspect current relevant activity when needed.

linp.end_presence(worker_id,presence_id)
  End an announcement immediately.

Worker release and genuine mode transitions clear that worker's presence automatically.

Do not announce ordinary local research. Presence is ephemeral, capped at 64, and exists only to avoid concrete collision/wasted duplication.
