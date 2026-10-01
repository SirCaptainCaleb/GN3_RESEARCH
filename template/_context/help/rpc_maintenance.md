RPC MANUAL — MAINTENANCE

### create_project_from_template
Signature: __template__.create_project_from_template(p_project_schema text) -> jsonb
Purpose: Create a new managed project by cloning the configured seed schema (__template__ by default), synchronizing public wrappers, and cloning centrally stored per-project configuration whose key is namespaced by the seed project.
Parameters: p_project_schema text
Returns: JSON creation report including cloned table/row/foreign-key/trigger counts, project_configuration_entries_copied, token replacement, and wrapper synchronization.
Semantics/constraints: Administrative/coordination operation. Centrally stored configuration keys namespaced by the configured seed project are copied with that project namespace replaced by the new project schema, so shared control-center features such as startup-Atlas selection inherit project defaults automatically.
Deeper help: help('api_modification').

### initialize_project
Signature: __template__.initialize_project(p_worker_id bigint, p_initialization jsonb) -> jsonb
Purpose: Initialize managed project state/schema.
Parameters: p_worker_id bigint, p_initialization jsonb
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### migration_preflight
Signature: __template__.migration_preflight() -> jsonb
Purpose: Run migration preflight checks.
Parameters: (none)
Returns: JSON report with status/details/findings.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('api_modification').

### prune_preview
Signature: __template__.prune_preview(p_ids text[]) -> jsonb
Purpose: Preview subtree-removal impact.
Parameters: p_ids text[]
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('maintenance').

### purge_trashed_subtrees
Signature: __template__.purge_trashed_subtrees(p_worker_id bigint, p_ids text[]) -> jsonb
Purpose: Trash, restore, or permanently purge subtrees.
Parameters: p_worker_id bigint, p_ids text[]
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Destructive and irreversible after purge; preview first.
Deeper help: help('maintenance').

### record_acceptance
Signature: __template__.record_acceptance(p_architecture_version integer, p_suite_name text, p_passed boolean, p_details jsonb) -> jsonb
Purpose: Record architecture acceptance-suite outcome.
Parameters: p_architecture_version integer, p_suite_name text, p_passed boolean, p_details jsonb
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Administrative/coordination operation; use only for documented maintenance.
Deeper help: help('api_modification').

### remove_standardization_term
Signature: __template__.remove_standardization_term(p_worker_id bigint, p_term text) -> jsonb
Purpose: Mutate project-local vocabulary rules.
Parameters: p_worker_id bigint, p_term text
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('vocabulary').

### restore_subtrees
Signature: __template__.restore_subtrees(p_worker_id bigint, p_ids text[]) -> jsonb
Purpose: Trash, restore, or permanently purge subtrees.
Parameters: p_worker_id bigint, p_ids text[]
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('maintenance').

### storage_report
Signature: __template__.storage_report() -> jsonb
Purpose: Report managed-project storage footprint.
Parameters: (none)
Returns: JSON report with status/details/findings.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.

### sync_all_project_wrappers
Signature: __template__.sync_all_project_wrappers() -> jsonb
Purpose: Synchronize thin public project wrappers.
Parameters: (none)
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Administrative/coordination operation; use only for documented maintenance.
Deeper help: help('api_modification').

### sync_project_wrappers
Signature: __template__.sync_project_wrappers(p_project_schema text) -> jsonb
Purpose: Synchronize thin public project wrappers.
Parameters: p_project_schema text
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Administrative/coordination operation; use only for documented maintenance.
Deeper help: help('api_modification').

### trash_subtrees
Signature: __template__.trash_subtrees(p_worker_id bigint, p_ids text[]) -> jsonb
Purpose: Trash, restore, or permanently purge subtrees.
Parameters: p_worker_id bigint, p_ids text[]
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('maintenance').

### upsert_standardization_term
Signature: __template__.upsert_standardization_term(p_worker_id bigint, p_term text, p_status text, p_preferred_term text DEFAULT NULL::text, p_definition text DEFAULT NULL::text, p_notes text DEFAULT NULL::text) -> jsonb
Purpose: Mutate project-local vocabulary rules.
Parameters: p_worker_id bigint, p_term text, p_status text, p_preferred_term text DEFAULT NULL::text, p_definition text DEFAULT NULL::text, p_notes text DEFAULT NULL::text
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('vocabulary').

### wave_reset
Signature: __template__.wave_reset(p_reason text DEFAULT NULL::text) -> jsonb
Purpose: Administratively reset wave/batch state.
Parameters: p_reason text DEFAULT NULL::text
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Administrative/coordination operation; use only for documented maintenance.
