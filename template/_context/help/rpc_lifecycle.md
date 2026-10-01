RPC MANUAL — LIFECYCLE

### authoring_schema
Signature: __template__.authoring_schema() -> jsonb
Purpose: Authoring Schema operation on the managed project API.
Parameters: (none)
Returns: JSON worker/API result with run, assignment, delta, revision, or introspection metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### changes_since
Signature: __template__.changes_since(p_since_revision bigint, p_after_revision bigint DEFAULT NULL::bigint, p_limit integer DEFAULT 100) -> jsonb
Purpose: Changes Since operation on the managed project API.
Parameters: p_since_revision bigint, p_after_revision bigint DEFAULT NULL::bigint, p_limit integer DEFAULT 100
Returns: JSON worker/API result with run, assignment, delta, revision, or introspection metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### context
Signature: __template__.context(p_focus_id text) -> jsonb
Purpose: Context operation on the managed project API.
Parameters: p_focus_id text
Returns: JSON worker/API result with run, assignment, delta, revision, or introspection metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### continue
Signature: __template__.continue(p_worker_id bigint, p_outcome text DEFAULT NULL::text, p_details jsonb DEFAULT '{}'::jsonb) -> jsonb
Purpose: Refresh an existing worker run; outcome overloads may transition the assignment.
Parameters: p_worker_id bigint, p_outcome text DEFAULT NULL::text, p_details jsonb DEFAULT '{}'::jsonb
Returns: JSON worker/API result with run, assignment, delta, revision, or introspection metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('lifecycle').

### continue
Signature: __template__.continue(p_worker_id bigint, p_outcome text, p_details text) -> jsonb
Purpose: Refresh an existing worker run; outcome overloads may transition the assignment.
Parameters: p_worker_id bigint, p_outcome text, p_details text
Returns: JSON worker/API result with run, assignment, delta, revision, or introspection metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('lifecycle').

### get_policy
Signature: __template__.get_policy(p_policy_key text) -> jsonb
Purpose: Get Policy operation on the managed project API.
Parameters: p_policy_key text
Returns: JSON worker/API result with run, assignment, delta, revision, or introspection metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### head
Signature: __template__.head() -> jsonb
Purpose: Head operation on the managed project API.
Parameters: (none)
Returns: JSON worker/API result with run, assignment, delta, revision, or introspection metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### help
Signature: __template__.help(p_topic text) -> jsonb
Purpose: Read shared help documentation; help() is the normal entry point.
Parameters: p_topic text
Returns: JSON worker/API result with run, assignment, delta, revision, or introspection metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### help_core
Signature: __template__.help_core(p_topic text) -> jsonb
Purpose: Read shared help documentation; help() is the normal entry point.
Parameters: p_topic text
Returns: JSON worker/API result with run, assignment, delta, revision, or introspection metadata as applicable.
Semantics/constraints: Low-level/compatibility export; prefer the ordinary/newest documented wrapper.

### next
Signature: __template__.next(p_worker_id bigint, p_outcome text DEFAULT NULL::text, p_details jsonb DEFAULT '{}'::jsonb) -> jsonb
Purpose: Close the current assignment and schedule the next one.
Parameters: p_worker_id bigint, p_outcome text DEFAULT NULL::text, p_details jsonb DEFAULT '{}'::jsonb
Returns: JSON worker/API result with run, assignment, delta, revision, or introspection metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('lifecycle').

### next
Signature: __template__.next(p_worker_id bigint, p_outcome text, p_details text) -> jsonb
Purpose: Close the current assignment and schedule the next one.
Parameters: p_worker_id bigint, p_outcome text, p_details text
Returns: JSON worker/API result with run, assignment, delta, revision, or introspection metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('lifecycle').

### next_core
Signature: __template__.next_core(p_worker_id bigint, p_outcome text DEFAULT 'completed'::text, p_details jsonb DEFAULT '{}'::jsonb) -> jsonb
Purpose: Close the current assignment and schedule the next one.
Parameters: p_worker_id bigint, p_outcome text DEFAULT 'completed'::text, p_details jsonb DEFAULT '{}'::jsonb
Returns: JSON worker/API result with run, assignment, delta, revision, or introspection metadata as applicable.
Semantics/constraints: Low-level/compatibility export; prefer the ordinary/newest documented wrapper.

### next_retry
Signature: __template__.next_retry(p_worker_id bigint, p_source_claim_id bigint) -> jsonb
Purpose: Next Retry operation on the managed project API.
Parameters: p_worker_id bigint, p_source_claim_id bigint
Returns: JSON worker/API result with run, assignment, delta, revision, or introspection metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### release
Signature: __template__.release(p_worker_id bigint) -> jsonb
Purpose: Release the worker claim; overload may request follow-up dispatch.
Parameters: p_worker_id bigint
Returns: JSON worker/API result with run, assignment, delta, revision, or introspection metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('lifecycle').

### release
Signature: __template__.release(p_worker_id bigint, p_receive_followup boolean) -> jsonb
Purpose: Release the worker claim; overload may request follow-up dispatch.
Parameters: p_worker_id bigint, p_receive_followup boolean
Returns: JSON worker/API result with run, assignment, delta, revision, or introspection metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('lifecycle').

### rpc_list
Signature: __template__.rpc_list() -> text[]
Purpose: List public RPC names.
Parameters: (none)
Returns: text array.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### rpc_signatures
Signature: __template__.rpc_signatures(p_name text DEFAULT NULL::text) -> jsonb
Purpose: Return exact live signatures for one RPC.
Parameters: p_name text DEFAULT NULL::text
Returns: JSON worker/API result with run, assignment, delta, revision, or introspection metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### startup
Signature: __template__.startup(p_worker_id bigint DEFAULT NULL::bigint) -> jsonb
Purpose: Establish worker identity/session and shared startup context without embedding the Atlas. The required next step is atlas(); after reading it, call continue(worker_id) for the first assignment.
Parameters: p_worker_id bigint DEFAULT NULL::bigint
Returns: JSON worker/API result with run, assignment, delta, revision, or introspection metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('lifecycle').

### sync
Signature: __template__.sync(p_worker_id bigint, p_since_revision bigint DEFAULT NULL::bigint, p_keep_mode boolean DEFAULT false) -> jsonb
Purpose: Refresh project delta/state while preserving the run.
Parameters: p_worker_id bigint, p_since_revision bigint DEFAULT NULL::bigint, p_keep_mode boolean DEFAULT false
Returns: JSON worker/API result with run, assignment, delta, revision, or introspection metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('lifecycle').

### update_policy
Signature: __template__.update_policy(p_worker_id bigint, p_policy_key text, p_body text) -> jsonb
Purpose: Update Policy operation on the managed project API.
Parameters: p_worker_id bigint, p_policy_key text, p_body text
Returns: JSON worker/API result with run, assignment, delta, revision, or introspection metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### work_digest
Signature: __template__.work_digest(p_since_revision bigint DEFAULT NULL::bigint, p_focus_ids text[] DEFAULT NULL::text[]) -> jsonb
Purpose: Work Digest operation on the managed project API.
Parameters: p_since_revision bigint DEFAULT NULL::bigint, p_focus_ids text[] DEFAULT NULL::text[]
Returns: JSON worker/API result with run, assignment, delta, revision, or introspection metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
