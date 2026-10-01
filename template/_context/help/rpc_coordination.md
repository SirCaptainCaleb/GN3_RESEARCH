RPC MANUAL — COORDINATION

### adjust_need
Signature: __template__.adjust_need(p_worker_id bigint, p_need_key text, p_action text, p_priority integer DEFAULT NULL::integer, p_reason text DEFAULT NULL::text, p_target_ids text[] DEFAULT NULL::text[]) -> jsonb
Purpose: Create/adjust/review scheduler need pressure.
Parameters: p_worker_id bigint, p_need_key text, p_action text, p_priority integer DEFAULT NULL::integer, p_reason text DEFAULT NULL::text, p_target_ids text[] DEFAULT NULL::text[]
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### announce
Signature: __template__.announce(p_worker_id bigint, p_activity text, p_scope_id text DEFAULT NULL::text, p_message text DEFAULT ''::text, p_ttl_minutes integer DEFAULT NULL::integer, p_exclusive_key text DEFAULT NULL::text) -> jsonb
Purpose: Create/read/end TTL presence for collision avoidance.
Parameters: p_worker_id bigint, p_activity text, p_scope_id text DEFAULT NULL::text, p_message text DEFAULT ''::text, p_ttl_minutes integer DEFAULT NULL::integer, p_exclusive_key text DEFAULT NULL::text
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('presence').

### assignment_request_status
Signature: __template__.assignment_request_status(p_worker_id bigint DEFAULT NULL::bigint) -> jsonb
Purpose: Inspect or cancel scheduler intent.
Parameters: p_worker_id bigint DEFAULT NULL::bigint
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('requests').

### begin_proof_activity
Signature: __template__.begin_proof_activity(p_worker_id bigint, p_activity text, p_scope_id text, p_message text DEFAULT ''::text, p_exclusive boolean DEFAULT true, p_ttl_minutes integer DEFAULT NULL::integer) -> jsonb
Purpose: Create/read/end TTL presence for collision avoidance.
Parameters: p_worker_id bigint, p_activity text, p_scope_id text, p_message text DEFAULT ''::text, p_exclusive boolean DEFAULT true, p_ttl_minutes integer DEFAULT NULL::integer
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('presence').

### begin_reasoning_activity
Signature: __template__.begin_reasoning_activity(p_worker_id bigint, p_activity text, p_scope_id text, p_message text DEFAULT ''::text, p_exclusive boolean DEFAULT true, p_ttl_minutes integer DEFAULT NULL::integer) -> jsonb
Purpose: Create/read/end TTL presence for collision avoidance.
Parameters: p_worker_id bigint, p_activity text, p_scope_id text, p_message text DEFAULT ''::text, p_exclusive boolean DEFAULT true, p_ttl_minutes integer DEFAULT NULL::integer
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('presence').

### begin_research_batch
Signature: __template__.begin_research_batch(p_worker_id bigint, p_note text DEFAULT NULL::text) -> jsonb
Purpose: Declare a new researcher batch.
Parameters: p_worker_id bigint, p_note text DEFAULT NULL::text
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### broadcast
Signature: __template__.broadcast(p_worker_id bigint, p_message text, p_mode text DEFAULT NULL::text) -> jsonb
Purpose: Create/update/delete project broadcasts.
Parameters: p_worker_id bigint, p_message text, p_mode text DEFAULT NULL::text
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### broadcast_sticky
Signature: __template__.broadcast_sticky(p_worker_id bigint, p_message text, p_ttl bigint DEFAULT 0, p_mode text DEFAULT NULL::text) -> jsonb
Purpose: Create/update/delete project broadcasts.
Parameters: p_worker_id bigint, p_message text, p_ttl bigint DEFAULT 0, p_mode text DEFAULT NULL::text
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### cancel_assignment_request
Signature: __template__.cancel_assignment_request(p_worker_id bigint, p_request_id bigint) -> jsonb
Purpose: Inspect or cancel scheduler intent.
Parameters: p_worker_id bigint, p_request_id bigint
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('requests').

### defer_to_research
Signature: __template__.defer_to_research(p_worker_id bigint, p_reason text, p_focus_id text DEFAULT NULL::text) -> jsonb
Purpose: Return/defer current work toward research scheduling.
Parameters: p_worker_id bigint, p_reason text, p_focus_id text DEFAULT NULL::text
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('requests').

### delete_broadcast
Signature: __template__.delete_broadcast(p_worker_id bigint, p_broadcast_id bigint) -> jsonb
Purpose: Create/update/delete project broadcasts.
Parameters: p_worker_id bigint, p_broadcast_id bigint
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### end_presence
Signature: __template__.end_presence(p_worker_id bigint, p_presence_id bigint) -> boolean
Purpose: Create/read/end TTL presence for collision avoidance.
Parameters: p_worker_id bigint, p_presence_id bigint
Returns: boolean scalar.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('presence').

### force_role
Signature: __template__.force_role(p_worker_id bigint DEFAULT NULL::bigint, p_role text DEFAULT NULL::text, p_task text DEFAULT NULL::text, p_focus_id text DEFAULT NULL::text, p_target_ids text[] DEFAULT '{}'::text[]) -> jsonb
Purpose: Exceptional administrative scheduler bypass.
Parameters: p_worker_id bigint DEFAULT NULL::bigint, p_role text DEFAULT NULL::text, p_task text DEFAULT NULL::text, p_focus_id text DEFAULT NULL::text, p_target_ids text[] DEFAULT '{}'::text[]
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Administrative/coordination operation; use only for documented maintenance.
Deeper help: help('requests').

### list_polls
Signature: __template__.list_polls(p_status text DEFAULT NULL::text, p_limit integer DEFAULT 20) -> jsonb
Purpose: Create/read/respond to bounded coordination polls.
Parameters: p_status text DEFAULT NULL::text, p_limit integer DEFAULT 20
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### poll_queue
Signature: __template__.poll_queue(p_worker_id bigint, p_limit integer DEFAULT 6) -> jsonb
Purpose: Create/read/respond to bounded coordination polls.
Parameters: p_worker_id bigint, p_limit integer DEFAULT 6
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### poll_queue_for_worker
Signature: __template__.poll_queue_for_worker(p_worker_id bigint, p_limit integer DEFAULT NULL::integer, p_claim_actions boolean DEFAULT true) -> jsonb
Purpose: Create/read/respond to bounded coordination polls.
Parameters: p_worker_id bigint, p_limit integer DEFAULT NULL::integer, p_claim_actions boolean DEFAULT true
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### poll_status
Signature: __template__.poll_status(p_poll_id bigint) -> jsonb
Purpose: Create/read/respond to bounded coordination polls.
Parameters: p_poll_id bigint
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### presence
Signature: __template__.presence(p_scope_id text DEFAULT NULL::text, p_global boolean DEFAULT false, p_limit integer DEFAULT 32) -> jsonb
Purpose: Create/read/end TTL presence for collision avoidance.
Parameters: p_scope_id text DEFAULT NULL::text, p_global boolean DEFAULT false, p_limit integer DEFAULT 32
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('presence').

### raise_need
Signature: __template__.raise_need(p_worker_id bigint, p_need_key text, p_priority integer, p_reason text, p_target_ids text[] DEFAULT '{}'::text[]) -> jsonb
Purpose: Create/adjust/review scheduler need pressure.
Parameters: p_worker_id bigint, p_need_key text, p_priority integer, p_reason text, p_target_ids text[] DEFAULT '{}'::text[]
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### raise_signal
Signature: __template__.raise_signal(p_worker_id bigint, p_kind text, p_title text, p_body text DEFAULT ''::text, p_severity integer DEFAULT 1, p_evidence jsonb DEFAULT '{}'::jsonb, p_related_object_ids text[] DEFAULT '{}'::text[], p_signal_key text DEFAULT NULL::text) -> bigint
Purpose: Create/read/resolve bounded health/methodology signals.
Parameters: p_worker_id bigint, p_kind text, p_title text, p_body text DEFAULT ''::text, p_severity integer DEFAULT 1, p_evidence jsonb DEFAULT '{}'::jsonb, p_related_object_ids text[] DEFAULT '{}'::text[], p_signal_key text DEFAULT NULL::text
Returns: bigint identifier.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('observability').

### reject_assignment_for_research
Signature: __template__.reject_assignment_for_research(p_worker_id bigint, p_reason text DEFAULT NULL::text) -> jsonb
Purpose: Return/defer current work toward research scheduling.
Parameters: p_worker_id bigint, p_reason text DEFAULT NULL::text
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('requests').

### request_assignment
Signature: __template__.request_assignment(p_worker_id bigint DEFAULT NULL::bigint, p_intent jsonb DEFAULT '{}'::jsonb, p_priority integer DEFAULT 80, p_timing text DEFAULT 'next_boundary'::text, p_scope text DEFAULT 'next_assignment'::text) -> jsonb
Purpose: Submit soft scheduler intent.
Parameters: p_worker_id bigint DEFAULT NULL::bigint, p_intent jsonb DEFAULT '{}'::jsonb, p_priority integer DEFAULT 80, p_timing text DEFAULT 'next_boundary'::text, p_scope text DEFAULT 'next_assignment'::text
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Soft intent only; hard scheduler constraints still govern.
Deeper help: help('requests').

### resolve_poll_action
Signature: __template__.resolve_poll_action(p_worker_id bigint, p_poll_id bigint, p_outcome text, p_details jsonb DEFAULT '{}'::jsonb) -> jsonb
Purpose: Create/read/respond to bounded coordination polls.
Parameters: p_worker_id bigint, p_poll_id bigint, p_outcome text, p_details jsonb DEFAULT '{}'::jsonb
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### resolve_signal
Signature: __template__.resolve_signal(p_worker_id bigint, p_signal_id bigint, p_status text DEFAULT 'resolved'::text) -> jsonb
Purpose: Create/read/resolve bounded health/methodology signals.
Parameters: p_worker_id bigint, p_signal_id bigint, p_status text DEFAULT 'resolved'::text
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('observability').

### resume_scheduler_dispatch
Signature: __template__.resume_scheduler_dispatch(p_worker_id bigint, p_dispatch_now boolean DEFAULT false) -> jsonb
Purpose: Resume scheduler dispatch.
Parameters: p_worker_id bigint, p_dispatch_now boolean DEFAULT false
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### review_brainstorm_need
Signature: __template__.review_brainstorm_need(p_worker_id bigint, p_decision text, p_reason text DEFAULT NULL::text) -> jsonb
Purpose: Create/adjust/review scheduler need pressure.
Parameters: p_worker_id bigint, p_decision text, p_reason text DEFAULT NULL::text
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### set_guidance
Signature: __template__.set_guidance(p_worker_id bigint, p_message text) -> jsonb
Purpose: Set temporary scheduler guidance.
Parameters: p_worker_id bigint, p_message text
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### set_project_state
Signature: __template__.set_project_state(p_worker_id bigint, p_patch jsonb) -> jsonb
Purpose: Patch managed project control state.
Parameters: p_worker_id bigint, p_patch jsonb
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Administrative/coordination operation; use only for documented maintenance.

### signals
Signature: __template__.signals(p_status text DEFAULT 'active'::text, p_kind text DEFAULT NULL::text, p_limit integer DEFAULT 64) -> jsonb
Purpose: Create/read/resolve bounded health/methodology signals.
Parameters: p_status text DEFAULT 'active'::text, p_kind text DEFAULT NULL::text, p_limit integer DEFAULT 64
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('observability').

### submit_brainstorm
Signature: __template__.submit_brainstorm(p_worker_id bigint, p_ideas jsonb) -> jsonb
Purpose: Submit brainstorm ideas.
Parameters: p_worker_id bigint, p_ideas jsonb
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### submit_poll
Signature: __template__.submit_poll(p_worker_id bigint, p_issue text, p_action text, p_vote_limit integer DEFAULT 3, p_priority integer DEFAULT 80, p_initial_response text DEFAULT 'yes'::text, p_target_ids text[] DEFAULT '{}'::text[]) -> jsonb
Purpose: Create/read/respond to bounded coordination polls.
Parameters: p_worker_id bigint, p_issue text, p_action text, p_vote_limit integer DEFAULT 3, p_priority integer DEFAULT 80, p_initial_response text DEFAULT 'yes'::text, p_target_ids text[] DEFAULT '{}'::text[]
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### update_broadcast
Signature: __template__.update_broadcast(p_worker_id bigint, p_broadcast_id bigint, p_message text DEFAULT NULL::text, p_ttl bigint DEFAULT NULL::bigint) -> jsonb
Purpose: Create/update/delete project broadcasts.
Parameters: p_worker_id bigint, p_broadcast_id bigint, p_message text DEFAULT NULL::text, p_ttl bigint DEFAULT NULL::bigint
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### vote_poll
Signature: __template__.vote_poll(p_worker_id bigint, p_poll_id bigint, p_vote text) -> jsonb
Purpose: Create/read/respond to bounded coordination polls.
Parameters: p_worker_id bigint, p_poll_id bigint, p_vote text
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
