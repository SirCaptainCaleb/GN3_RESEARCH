
API MODIFICATION MANUAL

Purpose
All shared executable machinery lives in control_center. Managed project schemas contain project state plus thin public wrappers only. Do not add internal helpers, trigger functions, scheduler logic, trust logic, observability logic, or other executable machinery to a project schema.

Architecture
- Public call path: project_schema.rpc(...) -> control_center.rpc(...).
- The wrapper pins search_path to: control_center, project_schema, pg_catalog.
- Public generalized control_center RPCs do not take a project-schema argument.
- Stateful control_center functions call control_center.active_project() and fail closed unless exactly one structurally valid managed project is present in search_path.
- Internal helper calls remain entirely inside control_center.
- Unqualified project-state relations fall through from control_center to the selected project schema.
- Trigger functions live in control_center and bootstrap project context from TG_TABLE_SCHEMA.
- Pure IMMUTABLE utilities may be project-independent and need not require active project context.

Changing internal machinery
1. Change or add the helper only in control_center.
2. Use an unqualified helper name for calls from other control_center machinery unless explicit qualification improves clarity.
3. Use unqualified project-state relation names; do not hard-code linp, gn3n, template, or another project schema.
4. Stateful helpers must validate project context at entry with control_center.active_project().
5. Trigger helpers must live in control_center and establish context from TG_TABLE_SCHEMA.
6. Do not create a project-local copy. No wrapper is needed for an internal-only helper.

Adding or changing a public RPC
1. Implement the generalized RPC once in control_center, with the public RPC signature and no schema-name parameter.
2. Add/update the signature in control_center.public_rpc_contract in the same migration; this central contract, not template, defines public API membership.
2. If it is stateful, validate project context at function entry.
3. Keep the implementation schema-generic: no hard-coded project schema qualifiers or project-name allowlist.
4. Create or replace the thin wrapper with the same public signature in every managed project schema. The wrapper body should only call control_center.rpc(...) and must pin search_path to control_center, that project schema, pg_catalog.
5. Keep wrapper definitions structurally identical except for the project schema name.
6. Preserve RPC security: postgres-owned SECURITY DEFINER wrapper; no PUBLIC/anon/authenticated execution; service_role may execute the wrapper; client roles may not directly execute control_center machinery.
7. Verify wrapper parity across every managed project after the migration.

Wrapper-maintenance DDL guard
Function/procedure DDL in a structurally managed project schema is blocked by event triggers. During an intentional synchronized wrapper migration only, use a transaction-local bypass:
  SELECT set_config('control_center.allow_project_function_ddl','on',true);
Perform the synchronized wrapper CREATE/ALTER/DROP work in the same transaction, then restore:
  SELECT set_config('control_center.allow_project_function_ddl','off',true);
The bypass is not permission to place implementation logic in project schemas.

Adding a new project
Instantiate a managed-project schema from the blank template seed or equivalent schema DDL, then give its thin wrappers the new project search path. The __template__ schema is a convenience seed only; shared behavior, policy, configuration, and API authority come from control_center. Managed-project recognition is structural; no project registry entry is required. The new project must expose exactly control_center.public_rpc_contract.

Required verification after API/machinery changes
- Every managed project has the same public wrapper signatures and normalized wrapper bodies.
- Project schemas contain no non-wrapper functions.
- Shared machinery has no hard-coded project-schema qualifiers or project-name allowlists.
- Stateful control_center functions reject execution without exactly one managed project in search_path.
- Trigger functions used by managed project tables resolve to control_center.
- Client ACL/security posture remains valid.
- DDL guards remain enabled.
- Run representative calls through at least two distinct project wrappers to verify project-state isolation.

Useful inspection
- project_schema.help('api_modification') -- this manual.
- project_schema.rpc_signatures(name) -- exact public signatures.
- project_schema.health() -- semantic/security health; DDL-guard health is silent unless broken.


SHARED VS PROJECT-LOCAL DATA
- Shared/project-ambivalent doctrine and help live once in control_center.policy_definitions. Use gn3n. for project RPC examples; control_center.policies renders that placeholder for the active project.
- Shared machinery configuration lives once in control_center.configuration; control_center.settings is only a compatibility view.
- Shared architecture regression state lives once in control_center.acceptance_status.
- Managed project schemas retain only project-local research/runtime state, project definitions in standardization_dictionary, and genuinely project-specific policy/state such as the project_policy object and project_policy_settings.
- Do not clone or synchronize central policy/configuration rows into projects. If data would have to be updated identically in every project, first ask whether it belongs centrally instead.
- Equality today is not sufficient reason to centralize: the semantic question is whether the datum is inherently project-specific.


CENTRAL PUBLIC API CONTRACT
control_center.public_rpc_contract is authoritative for which generalized control_center functions have project wrappers. template has no special authority. Public API migrations update the central implementation, the contract row, and all managed-project wrappers atomically under the transaction-local wrapper-maintenance bypass; then advance architecture_version and recertify.


PROJECT-LOCAL TABLE RULE
When editing control_center machinery, keep project-state table references unqualified. An explicit control_center.<table> reference is valid only for a genuinely shared central table. After machinery changes, scan control_center function bodies for control_center-qualified names matching managed-project relations; the expected count is zero.


Configuration changes
- control_center.configuration is the canonical shared configuration store.
- Use config_int/config_numeric/config_bool/config_text/config_interval/config_json rather than embedding operational thresholds or lists in shared machinery.
- control_center.settings is now only a compatibility view backed by configuration; do not add new settings columns or mutable state there.
- Configuration is currently global. Do not add project-name branches or project-specific overrides unless the architecture is explicitly extended later.
