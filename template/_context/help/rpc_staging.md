RPC MANUAL — STAGING

### active_stages
Signature: __template__.active_stages(p_worker_id bigint, p_global boolean DEFAULT false, p_limit integer DEFAULT 64) -> jsonb
Purpose: List live staged work.
Parameters: p_worker_id bigint, p_global boolean DEFAULT false, p_limit integer DEFAULT 64
Returns: JSON stage/status payload with identity/revision and guards/conflicts/verification as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('staging').

### append_stage
Signature: __template__.append_stage(p_worker_id bigint, p_stage_id bigint, p_operations jsonb) -> jsonb
Purpose: Append to a stage.
Parameters: p_worker_id bigint, p_stage_id bigint, p_operations jsonb
Returns: JSON stage/status payload with identity/revision and guards/conflicts/verification as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('staging').

### append_stage_v2
Signature: __template__.append_stage_v2(p_worker_id bigint, p_stage_id bigint, p_expected_stage_revision bigint, p_operations jsonb) -> jsonb
Purpose: Append to a stage.
Parameters: p_worker_id bigint, p_stage_id bigint, p_expected_stage_revision bigint, p_operations jsonb
Returns: JSON stage/status payload with identity/revision and guards/conflicts/verification as applicable.
Semantics/constraints: Stronger/current guarded variant where specialized help recommends it.
Deeper help: help('staging').

### claim_verified_stage
Signature: __template__.claim_verified_stage(p_worker_id bigint, p_stage_id bigint) -> jsonb
Purpose: Claim Verified Stage for staged-work recovery/lifecycle.
Parameters: p_worker_id bigint, p_stage_id bigint
Returns: JSON stage/status payload with identity/revision and guards/conflicts/verification as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('staging').

### commit_stage
Signature: __template__.commit_stage(p_worker_id bigint, p_stage_id bigint) -> jsonb
Purpose: Commit a verified stage atomically.
Parameters: p_worker_id bigint, p_stage_id bigint
Returns: JSON stage/status payload with identity/revision and guards/conflicts/verification as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('staging').

### commit_stage_base
Signature: __template__.commit_stage_base(p_worker_id bigint, p_stage_id bigint) -> jsonb
Purpose: Commit a verified stage atomically.
Parameters: p_worker_id bigint, p_stage_id bigint
Returns: JSON stage/status payload with identity/revision and guards/conflicts/verification as applicable.
Semantics/constraints: Low-level/compatibility export; prefer the ordinary/newest documented wrapper.
Deeper help: help('staging').

### commit_stage_core
Signature: __template__.commit_stage_core(p_worker_id bigint, p_stage_id bigint) -> jsonb
Purpose: Commit a verified stage atomically.
Parameters: p_worker_id bigint, p_stage_id bigint
Returns: JSON stage/status payload with identity/revision and guards/conflicts/verification as applicable.
Semantics/constraints: Low-level/compatibility export; prefer the ordinary/newest documented wrapper.
Deeper help: help('staging').

### commit_stage_locked_base
Signature: __template__.commit_stage_locked_base(p_worker_id bigint, p_stage_id bigint) -> jsonb
Purpose: Commit a verified stage atomically.
Parameters: p_worker_id bigint, p_stage_id bigint
Returns: JSON stage/status payload with identity/revision and guards/conflicts/verification as applicable.
Semantics/constraints: Low-level/compatibility export; prefer the ordinary/newest documented wrapper.
Deeper help: help('staging').

### discard_stage
Signature: __template__.discard_stage(p_worker_id bigint, p_stage_id bigint) -> boolean
Purpose: Discard Stage for staged-work recovery/lifecycle.
Parameters: p_worker_id bigint, p_stage_id bigint
Returns: boolean scalar.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('staging').

### get_stage
Signature: __template__.get_stage(p_worker_id bigint, p_stage_id bigint) -> jsonb
Purpose: Read one stage and its guards/status.
Parameters: p_worker_id bigint, p_stage_id bigint
Returns: JSON stage/status payload with identity/revision and guards/conflicts/verification as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('staging').

### rebase_stage
Signature: __template__.rebase_stage(p_worker_id bigint, p_stage_id bigint) -> jsonb
Purpose: Rebase Stage for staged-work recovery/lifecycle.
Parameters: p_worker_id bigint, p_stage_id bigint
Returns: JSON stage/status payload with identity/revision and guards/conflicts/verification as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('staging').

### replace_stage
Signature: __template__.replace_stage(p_worker_id bigint, p_stage_id bigint, p_operations jsonb) -> jsonb
Purpose: Replace a stage operation set.
Parameters: p_worker_id bigint, p_stage_id bigint, p_operations jsonb
Returns: JSON stage/status payload with identity/revision and guards/conflicts/verification as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('staging').

### replace_stage_v2
Signature: __template__.replace_stage_v2(p_worker_id bigint, p_stage_id bigint, p_expected_stage_revision bigint, p_operations jsonb) -> jsonb
Purpose: Replace a stage operation set.
Parameters: p_worker_id bigint, p_stage_id bigint, p_expected_stage_revision bigint, p_operations jsonb
Returns: JSON stage/status payload with identity/revision and guards/conflicts/verification as applicable.
Semantics/constraints: Stronger/current guarded variant where specialized help recommends it.
Deeper help: help('staging').

### stage_batch
Signature: __template__.stage_batch(p_worker_id bigint, p_label text, p_operations jsonb) -> jsonb
Purpose: Create staged operations for race-safe publication.
Parameters: p_worker_id bigint, p_label text, p_operations jsonb
Returns: JSON stage/status payload with identity/revision and guards/conflicts/verification as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('staging').

### stage_batch_base
Signature: __template__.stage_batch_base(p_worker_id bigint, p_label text, p_operations jsonb) -> jsonb
Purpose: Create staged operations for race-safe publication.
Parameters: p_worker_id bigint, p_label text, p_operations jsonb
Returns: JSON stage/status payload with identity/revision and guards/conflicts/verification as applicable.
Semantics/constraints: Low-level/compatibility export; prefer the ordinary/newest documented wrapper.
Deeper help: help('staging').

### stage_reasoning_bundle
Signature: __template__.stage_reasoning_bundle(p_worker_id bigint, p_label text, p_nodes jsonb) -> jsonb
Purpose: Create staged operations for race-safe publication.
Parameters: p_worker_id bigint, p_label text, p_nodes jsonb
Returns: JSON stage/status payload with identity/revision and guards/conflicts/verification as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('staging').

### verify_stage
Signature: __template__.verify_stage(p_worker_id bigint, p_stage_id bigint) -> jsonb
Purpose: Verify a stage against current state.
Parameters: p_worker_id bigint, p_stage_id bigint
Returns: JSON stage/status payload with identity/revision and guards/conflicts/verification as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('staging').

### watch_stage_reads
Signature: __template__.watch_stage_reads(p_worker_id bigint, p_stage_id bigint, p_object_ids text[]) -> jsonb
Purpose: Attach exact-read/math-version watches to a stage.
Parameters: p_worker_id bigint, p_stage_id bigint, p_object_ids text[]
Returns: JSON stage/status payload with identity/revision and guards/conflicts/verification as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('staging').

### watch_stage_reads_v2
Signature: __template__.watch_stage_reads_v2(p_worker_id bigint, p_stage_id bigint, p_expected_math_versions jsonb) -> jsonb
Purpose: Attach exact-read/math-version watches to a stage.
Parameters: p_worker_id bigint, p_stage_id bigint, p_expected_math_versions jsonb
Returns: JSON stage/status payload with identity/revision and guards/conflicts/verification as applicable.
Semantics/constraints: Stronger/current guarded variant where specialized help recommends it.
Deeper help: help('staging').
