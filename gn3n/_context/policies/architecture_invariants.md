
PROJECT RESEARCH ENGINE ARCHITECTURE INVARIANTS

1. Current state, not history. Do not persist historical document bodies, full prior versions, transcripts, or telemetry time series.
3. Bounded lightweight continuity. The change journal is capped and stores only logical operations/IDs/details, never historical bodies.
4. Nonrecursive operational design. Prefer bounded direct queries, explicit focus/context pulls, and finite current-state surfaces.
5. Efficiency. Startup and continuation must stay compact; broad material is pulled on demand.
6. Mathematical identity is separate from organization. Reparenting/reclassification does not invalidate a proof; statement/body/direct proof-premise changes do.
7. Asynchronous autonomy. No process may require a synchronous council or routine human scheduling.
8. Ordinary operation is scheduler-autonomous: the system itself surfaces/claims audits, coordination, rehearsals, methodology review, literature bridging, and special reasoning mode recommendations. Operator and worker steering normally enters as soft assignment requests that influence arbitration without bypassing trust, lease, continuity, collision, or special reasoning mode-handoff invariants. force_role is an exceptional administrative escape hatch, not an ordinary scheduling primitive.


LOCK ORDER

When a transaction needs multiple PROJECT synchronization domains, acquire them in this order:
1. the relevant coarse advisory lock (tree / assignment / bounded pool) before row locks;
2. owned transient row such as stage/claim;
3. object rows in deterministic object-id order;
4. singleton project state if the operation explicitly mutates it;
5. observability/need side effects last.

Do not introduce a path that holds an object row and then waits for the tree advisory lock. Presence is advisory collision avoidance plus its own bounded lock; it is not a substitute for structural database locking.


STARTUP SIZE / PROGRESSIVE DISCLOSURE

Startup is curated deliberately. There is no startup character budget and no automatic startup compaction. If material belongs in startup, it is returned unchanged.

A configurable startup-size warning threshold exists only as observability. Exceeding it may raise a soft warning so maintainers can inspect for accidental duplication or unnecessary always-loaded material. It never truncates, demotes, compacts, or blocks a worker packet.

Progressive disclosure remains a content-design principle: exact proofs, broad toolkits, optional historical material and other material that does not belong in every startup should be designed as on-demand surfaces in the first place, not automatically removed after serialization.

WORKER LOSS / DISPOSABLE WORKERS

Worker identity is never durable ownership of mathematical responsibility.

- Claims are short leases only.
- Needs, audit requests, project focus, and other durable obligations survive worker disappearance and become claimable again after lease expiry.
- Runs provide same-conversation continuity only; they must never be required to keep an obligation alive.
- Durable mathematics and obligations must not depend on a particular worker ever returning.


STARTUP NON-COMPACTION

PROJECT never automatically compacts startup. Startup-size warnings are diagnostic only. If startup becomes too large, review and deliberately edit the startup design; never let a runtime threshold decide what a worker is allowed to see.

NEED HYGIENE

Special needs are current trigger state, not a work-history ledger. Repeated reports of the same active trigger coalesce into one generation. Signal-backed methodology/coordination needs may auto-retire when their triggering signals and semantic health condition are already gone, provided no worker is actively servicing that generation. This prevents stale maintenance assignments from consuming research cognition.


RESEARCH CONTINUITY AND SOFT STEERING

Research continuity is represented by scheduler hysteresis rather than a hard role reservation. A live deep-research line receives a continuity preference, while stronger audit/need/recovery pressure can still win at a genuine assignment boundary. Operator/worker preferences use request_assignment(...); priority is a soft contribution rather than authority.

defer_to_research is now a compatibility convenience that queues a one-shot research request. It does not destroy the current assignment and does not certify, fail, resolve, or consume the underlying audit/maintenance obligation.


RPC-ONLY INTERNAL SCHEMA SECURITY

Every ordinary table in every managed project schema must have row-level security enabled. There are intentionally no client-facing row policies: PUBLIC, anon, authenticated, and service_role have no direct table access. Legitimate client access is through the gn3n.* SECURITY DEFINER wrapper surface. Wrappers must remain postgres-owned and pin search_path to control_center, the active project schema, pg_catalog. All shared executable machinery lives in control_center and is not directly executable by client roles. Any migration creating a managed-project table must enable RLS in the same migration. gn3n.health() reports the project security posture, and migration preflight fails closed if this invariant drifts.

SCHEMA / API LAYOUT
- Each managed research project is exactly one schema containing project state (including observability state) and thin unprefixed public API wrappers. No internal executable machinery belongs in a managed project schema.
- control_center contains all shared executable machinery: every generalized public RPC implementation, every internal helper, scheduler/trust/observability routine, and every trigger function. Public generalized RPCs do not take a project-schema argument. The calling wrapper pins search_path to control_center, the project schema, then pg_catalog; control_center derives the unique managed project structurally from that path.
- Public project API functions are thin wrappers over control_center; project acronym prefixes on public API functions are not part of the managed interface.
- control_center.public_rpc_contract is the canonical public API membership contract. Every managed project, including __template__, exposes exactly that thin wrapper surface. __template__ is only a blank managed-project schema seed for convenient project creation; it is not the source of shared behavior, policy, configuration, or API authority. Project-specific machinery belongs outside a managed project schema.
- Project-specific auxiliary subsystems live outside the managed project schema; gn3_archaeology is the current example.
- Split *_api, *_next, and *_observability schemas are legacy architecture and should not be recreated.

- No per-project implementation/helper layer is permitted: project wrapper -> control_center is the complete executable call boundary. Internal calls remain inside control_center; unqualified relation references fall through to the selected project schema.

- Managed-project identity is structural rather than registry-based. A new project may be initialized from the blank template seed or equivalent schema DDL; recognition depends on the canonical local state-table shape, while public API membership is checked independently against control_center.public_rpc_contract.
- Stateful control_center functions fail closed unless exactly one managed project is present in search_path. Pure IMMUTABLE utilities may run without project context.
- Trigger functions are centralized in control_center; they bootstrap project context from TG_TABLE_SCHEMA because trigger execution does not enter through a public wrapper.
- Function/procedure DDL inside a managed project schema is blocked by event triggers unless an explicit transaction-local wrapper-maintenance bypass is enabled. Ordinary roles also lack CREATE on managed project schemas.

- Project-ambivalent instruction/configuration data lives once in control_center rather than being copied into managed project schemas. Shared policies are canonical; the computation guard is a structured row inside the shared policy corpus; projects read the same rows directly.
- Project-local data is limited in principle to research state, project definitions/standardization vocabulary, and genuinely project-specific policy. Equality across projects is not itself the criterion; semantic scope is.

- Shared machinery settings live once in control_center.settings. Project-local operational policy state belongs in project_policy_settings; currently this contains the special reasoning mode veto fields.

- Shared policy text is stored canonically in control_center.policy_definitions using gn3n. RPC placeholders. control_center.policies is the rendered read surface for the active project; do not copy rendered policy rows back into project schemas.

- Architecture acceptance is shared current-state machinery data in control_center.acceptance_status. It is not copied per project. Material shared-architecture changes advance control_center.settings.architecture_version and invalidate prior acceptance until the centralized regression suite is rerun.


PROJECT-LOCAL RELATION RESOLUTION


UNARY-CHAIN STANDALONE BARRIER
objects.unary_chain_standalone is project-local organizational state. For an active proved object, true forces unary_chain_length=0 and resets any proved descendant chain. This flag expresses an intentional exposition decision, not mathematical status, and changing it must not bump math_version or invalidate mathematical trust.

Unary-chain detection is advisory. A detected chain requires case-by-case mathematical and expository judgment; it is not a mandate to shorten the tree. Authentic sequential reasoning MUST remain nested: parent-child descent records causal continuation, while siblings represent branches or alternate routes. Never flatten a sequential chain into siblings merely to reduce unary length. If an authentic contiguous unary segment is over-granular, the structural cure is recomposition into one equivalent-or-stronger replacement node; the replacement takes the segment position, terminal children and external consumers are preserved, the old segment is retired, and downstream trust is held until the replacement is verified. Distinct reusable standalone results should instead be rehomed beneath the canonical Toolkit.


CROSS-PROJECT ADMIN EXCEPTION
copy_subtrees_between_projects is intentionally not bound to one active wrapper project: it operates between two explicitly named managed project schemas and validates both structurally before mutation. Architecture posture therefore treats it as a declared cross-project administrative exception rather than an unguarded ordinary stateful helper.


PROJECT FACTORY ADMIN EXCEPTION
create_project_from_template, sync_project_wrappers, sync_all_project_wrappers, and replace_project_seed_token are intentional cross-project administrative functions. They do not bind to active_project() because they operate on an explicitly named project schema or discover managed schemas structurally. This is analogous to copy_subtrees_between_projects and must not be treated as an unguarded ordinary stateful helper.


GLOBAL CONFIGURATION INVARIANT
Operational tuning values belong in control_center.configuration and are global across managed projects. Shared machinery should not embed tunable priorities, TTLs, retention windows, batch sizes, list caps, preview budgets, scheduler weights, cadence thresholds, project/schema lists, or similar policy constants directly in function bodies. Read them through control_center.config_* helpers. Hard-coded literals are reserved for intrinsic mathematical constants, SQL/PostgreSQL API constants, enum/protocol structure, and truly non-tunable implementation identities. No project-specific configuration column exists at present; if project-specific overrides are ever needed, add that capability deliberately later rather than hard-coding project names.
