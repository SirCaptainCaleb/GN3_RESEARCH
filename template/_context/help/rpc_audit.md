RPC MANUAL — AUDIT

### audit_packaging_issue
Signature: __template__.audit_packaging_issue(p_worker_id bigint, p_id text, p_note text) -> jsonb
Purpose: Record an audit anomaly or packaging/context issue.
Parameters: p_worker_id bigint, p_id text, p_note text
Returns: JSON audit/trust result with target/batch/version/certificate or failure metadata.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('audit').

### begin_audit
Signature: __template__.begin_audit(p_worker_id bigint, p_id text) -> jsonb
Purpose: Begin/claim audit work.
Parameters: p_worker_id bigint, p_id text
Returns: JSON audit/trust result with target/batch/version/certificate or failure metadata.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('audit').

### bind_replacement_composition_v2_base_recomposition_audit
Signature: __template__.bind_replacement_composition_v2_base_recomposition_audit(p_worker_id bigint, p_composition_id text, p_source_ids text[], p_presence_id bigint, p_presence_generation bigint, p_note text DEFAULT NULL::text) -> jsonb
Purpose: Attach recomposition/source-manifest metadata.
Parameters: p_worker_id bigint, p_composition_id text, p_source_ids text[], p_presence_id bigint, p_presence_generation bigint, p_note text DEFAULT NULL::text
Returns: JSON audit/trust result with target/batch/version/certificate or failure metadata.
Semantics/constraints: Low-level/compatibility export; prefer the ordinary/newest documented wrapper.
Deeper help: help('audit').

### certify_object
Signature: __template__.certify_object(p_worker_id bigint, p_id text, p_expected_version bigint, p_note text DEFAULT NULL::text) -> jsonb
Purpose: Record successful verification/certification.
Parameters: p_worker_id bigint, p_id text, p_expected_version bigint, p_note text DEFAULT NULL::text
Returns: JSON audit/trust result with target/batch/version/certificate or failure metadata.
Semantics/constraints: Version-guarded; use exact current versions and reread on conflict.
Deeper help: help('audit').

### certify_object_ex
Signature: __template__.certify_object_ex(p_worker_id bigint, p_id text, p_expected_version bigint, p_note text DEFAULT NULL::text, p_verification_method text DEFAULT 'independent_check'::text) -> jsonb
Purpose: Record successful verification/certification.
Parameters: p_worker_id bigint, p_id text, p_expected_version bigint, p_note text DEFAULT NULL::text, p_verification_method text DEFAULT 'independent_check'::text
Returns: JSON audit/trust result with target/batch/version/certificate or failure metadata.
Semantics/constraints: Version-guarded; use exact current versions and reread on conflict.
Deeper help: help('audit').

### certify_object_ex_base_v4
Signature: __template__.certify_object_ex_base_v4(p_worker_id bigint, p_id text, p_expected_version bigint, p_note text DEFAULT NULL::text, p_verification_method text DEFAULT 'independent_check'::text) -> jsonb
Purpose: Record successful verification/certification.
Parameters: p_worker_id bigint, p_id text, p_expected_version bigint, p_note text DEFAULT NULL::text, p_verification_method text DEFAULT 'independent_check'::text
Returns: JSON audit/trust result with target/batch/version/certificate or failure metadata.
Semantics/constraints: Low-level/compatibility export; prefer the ordinary/newest documented wrapper.
Deeper help: help('audit').

### certify_object_ex_base_v4_legacy_recomposition_equivalence
Signature: __template__.certify_object_ex_base_v4_legacy_recomposition_equivalence(p_worker_id bigint, p_id text, p_expected_version bigint, p_note text DEFAULT NULL::text, p_verification_method text DEFAULT 'independent_check'::text) -> jsonb
Purpose: Record successful verification/certification.
Parameters: p_worker_id bigint, p_id text, p_expected_version bigint, p_note text DEFAULT NULL::text, p_verification_method text DEFAULT 'independent_check'::text
Returns: JSON audit/trust result with target/batch/version/certificate or failure metadata.
Semantics/constraints: Low-level/compatibility export; prefer the ordinary/newest documented wrapper.
Deeper help: help('audit').

### certify_object_guarded
Signature: __template__.certify_object_guarded(p_worker_id bigint, p_id text, p_expected_object_version bigint, p_expected_math_version bigint, p_note text DEFAULT NULL::text, p_verification_method text DEFAULT 'independent_check'::text) -> jsonb
Purpose: Record successful verification/certification.
Parameters: p_worker_id bigint, p_id text, p_expected_object_version bigint, p_expected_math_version bigint, p_note text DEFAULT NULL::text, p_verification_method text DEFAULT 'independent_check'::text
Returns: JSON audit/trust result with target/batch/version/certificate or failure metadata.
Semantics/constraints: Version-guarded; use exact current versions and reread on conflict.
Deeper help: help('audit').

### fail_object
Signature: __template__.fail_object(p_worker_id bigint, p_id text, p_expected_version bigint, p_reason text) -> jsonb
Purpose: Record audit failure under version guard.
Parameters: p_worker_id bigint, p_id text, p_expected_version bigint, p_reason text
Returns: JSON audit/trust result with target/batch/version/certificate or failure metadata.
Semantics/constraints: Version-guarded; use exact current versions and reread on conflict.
Deeper help: help('audit').

### flag_audit_anomaly
Signature: __template__.flag_audit_anomaly(p_worker_id bigint, p_id text, p_reason text, p_priority integer DEFAULT 100) -> jsonb
Purpose: Record an audit anomaly or packaging/context issue.
Parameters: p_worker_id bigint, p_id text, p_reason text, p_priority integer DEFAULT 100
Returns: JSON audit/trust result with target/batch/version/certificate or failure metadata.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('audit').

### local_audit_edge_repair
Signature: __template__.local_audit_edge_repair(p_worker_id bigint, p_from_id text, p_to_id text, p_kind text, p_action text DEFAULT 'add'::text, p_metadata jsonb DEFAULT '{}'::jsonb, p_reason text DEFAULT NULL::text) -> jsonb
Purpose: Apply a narrow audited repair.
Parameters: p_worker_id bigint, p_from_id text, p_to_id text, p_kind text, p_action text DEFAULT 'add'::text, p_metadata jsonb DEFAULT '{}'::jsonb, p_reason text DEFAULT NULL::text
Returns: JSON audit/trust result with target/batch/version/certificate or failure metadata.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('audit').

### local_audit_repair
Signature: __template__.local_audit_repair(p_worker_id bigint, p_id text, p_expected_version bigint, p_patch jsonb, p_reason text) -> jsonb
Purpose: Apply a narrow audited repair.
Parameters: p_worker_id bigint, p_id text, p_expected_version bigint, p_patch jsonb, p_reason text
Returns: JSON audit/trust result with target/batch/version/certificate or failure metadata.
Semantics/constraints: Version-guarded; use exact current versions and reread on conflict.
Deeper help: help('audit').

### open_audit_batch
Signature: __template__.open_audit_batch(p_worker_id bigint, p_additional_ids text[] DEFAULT '{}'::text[], p_content text DEFAULT 'math'::text, p_page_chars integer DEFAULT 12000) -> jsonb
Purpose: Open the shared exact read basis for an audit batch.
Parameters: p_worker_id bigint, p_additional_ids text[] DEFAULT '{}'::text[], p_content text DEFAULT 'math'::text, p_page_chars integer DEFAULT 12000
Returns: JSON session/page payload with cursor/content plus consistency/version metadata.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('audit').

### open_audit_batch_base_recomposition_equivalence
Signature: __template__.open_audit_batch_base_recomposition_equivalence(p_worker_id bigint, p_additional_ids text[] DEFAULT '{}'::text[], p_content text DEFAULT 'math'::text, p_page_chars integer DEFAULT 12000) -> jsonb
Purpose: Open the shared exact read basis for an audit batch.
Parameters: p_worker_id bigint, p_additional_ids text[] DEFAULT '{}'::text[], p_content text DEFAULT 'math'::text, p_page_chars integer DEFAULT 12000
Returns: JSON session/page payload with cursor/content plus consistency/version metadata.
Semantics/constraints: Low-level/compatibility export; prefer the ordinary/newest documented wrapper.
Deeper help: help('audit').

### open_audit_batch_v2
Signature: __template__.open_audit_batch_v2(p_worker_id bigint, p_additional_ids text[] DEFAULT '{}'::text[], p_content text DEFAULT 'math'::text, p_page_chars integer DEFAULT 12000) -> jsonb
Purpose: Open the shared exact read basis for an audit batch.
Parameters: p_worker_id bigint, p_additional_ids text[] DEFAULT '{}'::text[], p_content text DEFAULT 'math'::text, p_page_chars integer DEFAULT 12000
Returns: JSON session/page payload with cursor/content plus consistency/version metadata.
Semantics/constraints: Stronger/current guarded variant where specialized help recommends it.
Deeper help: help('audit').

### open_audit_bundle
Signature: __template__.open_audit_bundle(p_worker_id bigint, p_target_id text, p_content text DEFAULT 'full'::text, p_page_chars integer DEFAULT 12000) -> jsonb
Purpose: Open exact audit context around a target.
Parameters: p_worker_id bigint, p_target_id text, p_content text DEFAULT 'full'::text, p_page_chars integer DEFAULT 12000
Returns: JSON session/page payload with cursor/content plus consistency/version metadata.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('audit').

### open_audit_bundle_v2
Signature: __template__.open_audit_bundle_v2(p_worker_id bigint, p_target_id text, p_additional_ids text[] DEFAULT '{}'::text[], p_content text DEFAULT 'math'::text, p_page_chars integer DEFAULT 12000) -> jsonb
Purpose: Open exact audit context around a target.
Parameters: p_worker_id bigint, p_target_id text, p_additional_ids text[] DEFAULT '{}'::text[], p_content text DEFAULT 'math'::text, p_page_chars integer DEFAULT 12000
Returns: JSON session/page payload with cursor/content plus consistency/version metadata.
Semantics/constraints: Stronger/current guarded variant where specialized help recommends it.
Deeper help: help('audit').

### open_audit_bundle_v2_base_recomposition_equivalence
Signature: __template__.open_audit_bundle_v2_base_recomposition_equivalence(p_worker_id bigint, p_target_id text, p_additional_ids text[] DEFAULT '{}'::text[], p_content text DEFAULT 'math'::text, p_page_chars integer DEFAULT 12000) -> jsonb
Purpose: Open exact audit context around a target.
Parameters: p_worker_id bigint, p_target_id text, p_additional_ids text[] DEFAULT '{}'::text[], p_content text DEFAULT 'math'::text, p_page_chars integer DEFAULT 12000
Returns: JSON session/page payload with cursor/content plus consistency/version metadata.
Semantics/constraints: Low-level/compatibility export; prefer the ordinary/newest documented wrapper.
Deeper help: help('audit').

### release_all_audit_claims
Signature: __template__.release_all_audit_claims(p_worker_id bigint, p_reason text DEFAULT NULL::text) -> jsonb
Purpose: Release audit claims.
Parameters: p_worker_id bigint, p_reason text DEFAULT NULL::text
Returns: JSON audit/trust result with target/batch/version/certificate or failure metadata.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('audit').

### release_all_audit_claims
Signature: __template__.release_all_audit_claims(p_worker_id bigint, p_reason text, p_receive_followup boolean) -> jsonb
Purpose: Release audit claims.
Parameters: p_worker_id bigint, p_reason text, p_receive_followup boolean
Returns: JSON audit/trust result with target/batch/version/certificate or failure metadata.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('audit').

### release_audit_claims
Signature: __template__.release_audit_claims(p_worker_id bigint, p_reason text DEFAULT NULL::text) -> jsonb
Purpose: Release audit claims.
Parameters: p_worker_id bigint, p_reason text DEFAULT NULL::text
Returns: JSON audit/trust result with target/batch/version/certificate or failure metadata.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('audit').

### release_audit_claims
Signature: __template__.release_audit_claims(p_worker_id bigint, p_reason text, p_receive_followup boolean) -> jsonb
Purpose: Release audit claims.
Parameters: p_worker_id bigint, p_reason text, p_receive_followup boolean
Returns: JSON audit/trust result with target/batch/version/certificate or failure metadata.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('audit').

### request_audit
Signature: __template__.request_audit(p_worker_id bigint, p_id text, p_priority integer DEFAULT 50, p_reason text DEFAULT NULL::text) -> jsonb
Purpose: Request audit work at object/reaudit/chain scope.
Parameters: p_worker_id bigint, p_id text, p_priority integer DEFAULT 50, p_reason text DEFAULT NULL::text
Returns: JSON audit/trust result with target/batch/version/certificate or failure metadata.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('audit').

### request_chain_audit
Signature: __template__.request_chain_audit(p_worker_id bigint, p_root_id text, p_priority integer DEFAULT 100, p_reason text DEFAULT NULL::text) -> jsonb
Purpose: Request audit work at object/reaudit/chain scope.
Parameters: p_worker_id bigint, p_root_id text, p_priority integer DEFAULT 100, p_reason text DEFAULT NULL::text
Returns: JSON audit/trust result with target/batch/version/certificate or failure metadata.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('audit').

### request_reaudit
Signature: __template__.request_reaudit(p_worker_id bigint, p_id text, p_priority integer, p_reason text) -> jsonb
Purpose: Request audit work at object/reaudit/chain scope.
Parameters: p_worker_id bigint, p_id text, p_priority integer, p_reason text
Returns: JSON audit/trust result with target/batch/version/certificate or failure metadata.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('audit').

### require_verification
Signature: __template__.require_verification(p_worker_id bigint, p_id text, p_requirement text, p_reason text) -> jsonb
Purpose: Attach an explicit verification requirement.
Parameters: p_worker_id bigint, p_id text, p_requirement text, p_reason text
Returns: JSON audit/trust result with target/batch/version/certificate or failure metadata.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('audit').

### stage_audit_batch
Signature: __template__.stage_audit_batch(p_worker_id bigint, p_label text, p_operations jsonb) -> jsonb
Purpose: Create staged operations for race-safe publication.
Parameters: p_worker_id bigint, p_label text, p_operations jsonb
Returns: JSON stage/status payload with identity/revision and guards/conflicts/verification as applicable.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('audit').

### submit_audit_batch
Signature: __template__.submit_audit_batch(p_worker_id bigint, p_decisions jsonb) -> jsonb
Purpose: Submit audit decisions atomically.
Parameters: p_worker_id bigint, p_decisions jsonb
Returns: JSON audit/trust result with target/batch/version/certificate or failure metadata.
Semantics/constraints: Use through the project-schema wrapper in active managed-project context.
Deeper help: help('audit').

### submit_audit_batch_v2
Signature: __template__.submit_audit_batch_v2(p_worker_id bigint, p_decisions jsonb, p_consumer_impacts jsonb DEFAULT '[]'::jsonb) -> jsonb
Purpose: Submit audit decisions atomically.
Parameters: p_worker_id bigint, p_decisions jsonb, p_consumer_impacts jsonb DEFAULT '[]'::jsonb
Returns: JSON audit/trust result with target/batch/version/certificate or failure metadata.
Semantics/constraints: Stronger/current guarded variant where specialized help recommends it.
Deeper help: help('audit').
