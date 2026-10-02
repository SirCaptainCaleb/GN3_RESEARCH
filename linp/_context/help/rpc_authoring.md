RPC MANUAL — AUTHORING

### add_dependency_current
Signature: linp.add_dependency_current(p_worker_id bigint, p_consumer_id text, p_premise_id text, p_metadata jsonb DEFAULT '{}'::jsonb) -> jsonb
Purpose: Add a dependency pinned to current premise math_version.
Parameters: p_worker_id bigint, p_consumer_id text, p_premise_id text, p_metadata jsonb DEFAULT '{}'::jsonb
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('writing').

### add_edge
Signature: linp.add_edge(p_worker_id bigint, p_from_id text, p_to_id text, p_kind text, p_metadata jsonb DEFAULT '{}'::jsonb) -> jsonb
Purpose: Add a typed relation.
Parameters: p_worker_id bigint, p_from_id text, p_to_id text, p_kind text, p_metadata jsonb DEFAULT '{}'::jsonb
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('writing').

### bind_composition
Signature: linp.bind_composition(p_worker_id bigint, p_composition_id text, p_source_ids text[], p_note text DEFAULT NULL::text) -> jsonb
Purpose: Attach recomposition/source-manifest metadata.
Parameters: p_worker_id bigint, p_composition_id text, p_source_ids text[], p_note text DEFAULT NULL::text
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('reasoning').

### bind_composition_v2
Signature: linp.bind_composition_v2(p_worker_id bigint, p_composition_id text, p_source_ids text[], p_presence_id bigint, p_presence_generation bigint, p_note text DEFAULT NULL::text) -> jsonb
Purpose: Attach recomposition/source-manifest metadata.
Parameters: p_worker_id bigint, p_composition_id text, p_source_ids text[], p_presence_id bigint, p_presence_generation bigint, p_note text DEFAULT NULL::text
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Stronger/current guarded variant where specialized help recommends it.
Deeper help: help('reasoning').

### bind_replacement_composition_v2
Signature: linp.bind_replacement_composition_v2(p_worker_id bigint, p_composition_id text, p_source_ids text[], p_presence_id bigint, p_presence_generation bigint, p_note text DEFAULT NULL::text) -> jsonb
Purpose: Attach recomposition/source-manifest metadata.
Parameters: p_worker_id bigint, p_composition_id text, p_source_ids text[], p_presence_id bigint, p_presence_generation bigint, p_note text DEFAULT NULL::text
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Stronger/current guarded variant where specialized help recommends it.
Deeper help: help('reasoning').

### create_object
Signature: linp.create_object(p_worker_id bigint, p_object_type text, p_title text, p_statement text DEFAULT NULL::text, p_body text DEFAULT ''::text, p_parent_id text DEFAULT NULL::text, p_position bigint DEFAULT 0, p_metadata jsonb DEFAULT '{}'::jsonb, p_research_interface jsonb DEFAULT '{}'::jsonb, p_mathematical_status text DEFAULT NULL::text, p_research_level text DEFAULT 'working_unit'::text, p_lifecycle_status text DEFAULT 'active'::text, p_attention text DEFAULT 'available'::text, p_id text DEFAULT NULL::text, p_legacy_id text DEFAULT NULL::text, p_simplified_statement text DEFAULT NULL::text, p_atlas_height text DEFAULT NULL::text, p_atlas_hidden boolean DEFAULT false) -> jsonb
Purpose: Create a repository object.
Parameters: p_worker_id bigint, p_object_type text, p_title text, p_statement text DEFAULT NULL::text, p_body text DEFAULT ''::text, p_parent_id text DEFAULT NULL::text, p_position bigint DEFAULT 0, p_metadata jsonb DEFAULT '{}'::jsonb, p_research_interface jsonb DEFAULT '{}'::jsonb, p_mathematical_status text DEFAULT NULL::text, p_research_level text DEFAULT 'working_unit'::text, p_lifecycle_status text DEFAULT 'active'::text, p_attention text DEFAULT 'available'::text, p_id text DEFAULT NULL::text, p_legacy_id text DEFAULT NULL::text, p_simplified_statement text DEFAULT NULL::text, p_atlas_height text DEFAULT NULL::text, p_atlas_hidden boolean DEFAULT false
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('writing').

### create_object_core
Signature: linp.create_object_core(p_worker_id bigint, p_object_type text, p_title text, p_statement text DEFAULT NULL::text, p_body text DEFAULT ''::text, p_parent_id text DEFAULT NULL::text, p_position bigint DEFAULT 0, p_metadata jsonb DEFAULT '{}'::jsonb, p_research_interface jsonb DEFAULT '{}'::jsonb, p_mathematical_status text DEFAULT NULL::text, p_research_level text DEFAULT NULL::text, p_lifecycle_status text DEFAULT 'active'::text, p_attention text DEFAULT 'available'::text, p_audit_requested boolean DEFAULT NULL::boolean, p_audit_priority integer DEFAULT 0, p_id text DEFAULT NULL::text, p_legacy_id text DEFAULT NULL::text) -> jsonb
Purpose: Create a repository object.
Parameters: p_worker_id bigint, p_object_type text, p_title text, p_statement text DEFAULT NULL::text, p_body text DEFAULT ''::text, p_parent_id text DEFAULT NULL::text, p_position bigint DEFAULT 0, p_metadata jsonb DEFAULT '{}'::jsonb, p_research_interface jsonb DEFAULT '{}'::jsonb, p_mathematical_status text DEFAULT NULL::text, p_research_level text DEFAULT NULL::text, p_lifecycle_status text DEFAULT 'active'::text, p_attention text DEFAULT 'available'::text, p_audit_requested boolean DEFAULT NULL::boolean, p_audit_priority integer DEFAULT 0, p_id text DEFAULT NULL::text, p_legacy_id text DEFAULT NULL::text
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Low-level/compatibility export; prefer the ordinary/newest documented wrapper.
Deeper help: help('writing').

### create_reasoning_child
Signature: linp.create_reasoning_child(p_worker_id bigint, p_parent_id text, p_title text, p_statement text DEFAULT NULL::text, p_body text DEFAULT ''::text, p_node_kind text DEFAULT 'step'::text, p_route_key text DEFAULT NULL::text, p_metadata jsonb DEFAULT '{}'::jsonb, p_research_interface jsonb DEFAULT '{}'::jsonb, p_mathematical_status text DEFAULT NULL::text, p_research_level text DEFAULT 'working_unit'::text, p_attention text DEFAULT 'available'::text, p_audit_requested boolean DEFAULT NULL::boolean, p_audit_priority integer DEFAULT 0, p_id text DEFAULT NULL::text, p_simplified_statement text DEFAULT NULL::text, p_atlas_height text DEFAULT NULL::text, p_atlas_hidden boolean DEFAULT false) -> jsonb
Purpose: Create a reasoning-tree child.
Parameters: p_worker_id bigint, p_parent_id text, p_title text, p_statement text DEFAULT NULL::text, p_body text DEFAULT ''::text, p_node_kind text DEFAULT 'step'::text, p_route_key text DEFAULT NULL::text, p_metadata jsonb DEFAULT '{}'::jsonb, p_research_interface jsonb DEFAULT '{}'::jsonb, p_mathematical_status text DEFAULT NULL::text, p_research_level text DEFAULT 'working_unit'::text, p_attention text DEFAULT 'available'::text, p_audit_requested boolean DEFAULT NULL::boolean, p_audit_priority integer DEFAULT 0, p_id text DEFAULT NULL::text, p_simplified_statement text DEFAULT NULL::text, p_atlas_height text DEFAULT NULL::text, p_atlas_hidden boolean DEFAULT false
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('reasoning').

### create_reasoning_child_core
Signature: linp.create_reasoning_child_core(p_worker_id bigint, p_parent_id text, p_title text, p_statement text DEFAULT NULL::text, p_body text DEFAULT ''::text, p_node_kind text DEFAULT 'step'::text, p_route_key text DEFAULT NULL::text, p_metadata jsonb DEFAULT '{}'::jsonb, p_research_interface jsonb DEFAULT '{}'::jsonb, p_mathematical_status text DEFAULT NULL::text, p_research_level text DEFAULT 'working_unit'::text, p_attention text DEFAULT 'available'::text, p_id text DEFAULT NULL::text) -> jsonb
Purpose: Create a reasoning-tree child.
Parameters: p_worker_id bigint, p_parent_id text, p_title text, p_statement text DEFAULT NULL::text, p_body text DEFAULT ''::text, p_node_kind text DEFAULT 'step'::text, p_route_key text DEFAULT NULL::text, p_metadata jsonb DEFAULT '{}'::jsonb, p_research_interface jsonb DEFAULT '{}'::jsonb, p_mathematical_status text DEFAULT NULL::text, p_research_level text DEFAULT 'working_unit'::text, p_attention text DEFAULT 'available'::text, p_id text DEFAULT NULL::text
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Low-level/compatibility export; prefer the ordinary/newest documented wrapper.
Deeper help: help('reasoning').

### mark_proof_node
Signature: linp.mark_proof_node(p_worker_id bigint, p_object_id text, p_node_kind text, p_route_key text DEFAULT NULL::text, p_note text DEFAULT ''::text) -> jsonb
Purpose: Annotate an existing reasoning node.
Parameters: p_worker_id bigint, p_object_id text, p_node_kind text, p_route_key text DEFAULT NULL::text, p_note text DEFAULT ''::text
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('reasoning').

### mark_reasoning_node
Signature: linp.mark_reasoning_node(p_worker_id bigint, p_object_id text, p_node_kind text, p_route_key text DEFAULT NULL::text, p_note text DEFAULT ''::text) -> jsonb
Purpose: Annotate an existing reasoning node.
Parameters: p_worker_id bigint, p_object_id text, p_node_kind text, p_route_key text DEFAULT NULL::text, p_note text DEFAULT ''::text
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('reasoning').

### mark_route_relation
Signature: linp.mark_route_relation(p_worker_id bigint, p_older_id text, p_newer_id text, p_relation text DEFAULT 'bypassed_by'::text, p_note text DEFAULT NULL::text) -> jsonb
Purpose: Record an older/newer route relation.
Parameters: p_worker_id bigint, p_older_id text, p_newer_id text, p_relation text DEFAULT 'bypassed_by'::text, p_note text DEFAULT NULL::text
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('writing').

### move_object
Signature: linp.move_object(p_worker_id bigint, p_id text, p_expected_version bigint, p_new_parent_id text DEFAULT NULL::text, p_new_position bigint DEFAULT 0) -> jsonb
Purpose: Reparent/reposition an object organizationally.
Parameters: p_worker_id bigint, p_id text, p_expected_version bigint, p_new_parent_id text DEFAULT NULL::text, p_new_position bigint DEFAULT 0
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Version-guarded; use exact current versions and reread on conflict.
Deeper help: help('writing').

### proof_preflight
Signature: linp.proof_preflight(p_object jsonb, p_dependency_ids text[] DEFAULT '{}'::text[]) -> jsonb
Purpose: Validate a prospective proof object/dependency set.
Parameters: p_object jsonb, p_dependency_ids text[] DEFAULT '{}'::text[]
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('reasoning').

### publish_with_dependencies
Signature: linp.publish_with_dependencies(p_worker_id bigint, p_object jsonb, p_dependency_ids text[] DEFAULT '{}'::text[]) -> jsonb
Purpose: Create/publish an object with dependencies.
Parameters: p_worker_id bigint, p_object jsonb, p_dependency_ids text[] DEFAULT '{}'::text[]
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('writing').

### remove_edge
Signature: linp.remove_edge(p_worker_id bigint, p_from_id text, p_to_id text, p_kind text) -> jsonb
Purpose: Remove a typed relation.
Parameters: p_worker_id bigint, p_from_id text, p_to_id text, p_kind text
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('writing').

### replace_dependency
Signature: linp.replace_dependency(p_worker_id bigint, p_consumer_id text, p_old_premise_id text, p_new_premise_id text, p_expected_new_premise_math_version bigint, p_note text DEFAULT NULL::text) -> jsonb
Purpose: Replace a dependency under a version guard.
Parameters: p_worker_id bigint, p_consumer_id text, p_old_premise_id text, p_new_premise_id text, p_expected_new_premise_math_version bigint, p_note text DEFAULT NULL::text
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('writing').

### revise_current
Signature: linp.revise_current(p_worker_id bigint, p_id text, p_patch jsonb, p_substantive boolean DEFAULT true, p_expected_math_version bigint DEFAULT NULL::bigint) -> jsonb
Purpose: Patch an object guarded by current math_version.
Parameters: p_worker_id bigint, p_id text, p_patch jsonb, p_substantive boolean DEFAULT true, p_expected_math_version bigint DEFAULT NULL::bigint
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Version-guarded; use exact current versions and reread on conflict.
Deeper help: help('writing').

### unsupersede
Signature: linp.unsupersede(p_worker_id bigint, p_superseder_id text, p_target_id text, p_reason text DEFAULT NULL::text) -> jsonb
Purpose: Reverse a supersession relation.
Parameters: p_worker_id bigint, p_superseder_id text, p_target_id text, p_reason text DEFAULT NULL::text
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('writing').

### update_object
Signature: linp.update_object(p_worker_id bigint, p_id text, p_expected_version bigint, p_patch jsonb, p_substantive boolean DEFAULT true, p_nonsubstantive_override boolean DEFAULT false) -> jsonb
Purpose: Apply a version-checked object patch.
Parameters: p_worker_id bigint, p_id text, p_expected_version bigint, p_patch jsonb, p_substantive boolean DEFAULT true, p_nonsubstantive_override boolean DEFAULT false
Returns: JSON operation/read result; lists and mutations include relevant IDs/state and revision/version metadata as applicable.
Semantics/constraints: Version-guarded. statement/body/mathematical_status normally require p_substantive=true. Set p_substantive=false and p_nonsubstantive_override=true only when the caller explicitly guarantees that an apparently mathematical text/status edit does not change the mathematics; this preserves math_version and trust state while still advancing ordinary version. The override is recorded in the change metadata.
Deeper help: help('writing').
