
STAGING

Use staging for race-safe publication of related mathematical work. Ordinary repository churn does not invalidate a stage.

Authorized mathematical principals:
- an ordinary worker with an active claim;
- the active special reasoning mode session.

Canonical workflow:
1. stage_batch(...) or stage_reasoning_bundle(...)
2. watch_stage_reads_v2(...) for additional exact premise versions actually read
3. revision-aware append/replace if needed
4. verify_stage(...)
5. commit_stage(...)

Conflict semantics:
- unrelated repository changes do not matter;
- organizational changes to a premise do not matter if math_version is unchanged;
- concurrent write-target edits or watched mathematical changes do matter;
- rebase is an explicit acknowledgment after review.

special reasoning mode authorization is mathematical, not administrative. special reasoning mode stages may create/update/move mathematical objects, add/remove edges, request audits, and mutate reasoning structure. They may not publish audit verdicts, project-state changes, signals, or scheduler administration.

VERIFIED STAGE RECOVERY

A verified unexpired research stage is recoverable if its owner disappears.

A verified special reasoning mode stage is also recoverable after the active special reasoning mode session has shown no activity for one normal claim TTL. The scheduler may then assign an ordinary worker commit-only custody. The worker must call claim_verified_stage, which revalidates the digest and read/write baselines, then commit_stage.

Recovery transfers publication custody only. Mathematical authorship remains with the original stage owner, including special reasoning mode. Unverified special reasoning mode scratch is never transferable.
