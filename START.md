# GN3 startup

This file is the only bootstrap.

Initialization is role-specific. Do not make every worker ingest every GN3 policy file.

Repository: SirCaptainCaleb/GN3_RESEARCH

The repository root is the active GN3 project. ARCHAEOLOGY/ is legacy material, provenance, and recovery evidence; it is not current operating authority.

## Role routing

Use the following startup path.

### Researcher

Read completely, in order:

1. INIT/01_ARCHITECTURE.md
2. INIT/02_MATHEMATICAL_LANGUAGE.md
3. INIT/03_RESEARCH_PROTOCOL.md
4. INIT/05_COMPUTATION_DISCIPLINE.md
5. INIT/06_TERMINOLOGY.md
6. INIT/07_COMMUNICATION_STANDARD.md

Researchers do not need the detailed Auditor protocol and do not read INIT/AUDITOR.md unless they are explicitly switching roles.

### Vice Director

Read completely, in order:

1. INIT/01_ARCHITECTURE.md
2. INIT/02_MATHEMATICAL_LANGUAGE.md
3. INIT/03_RESEARCH_PROTOCOL.md
4. INIT/04_AUDIT_PROTOCOL.md
5. INIT/05_COMPUTATION_DISCIPLINE.md
6. INIT/06_TERMINOLOGY.md
7. INIT/07_COMMUNICATION_STANDARD.md

The Vice Director owns synthesis, guidance, audit triage, research-tree maintenance, shelf integration, and routine project-state propagation.

### Auditor

Read completely, in order:

1. INIT/01_ARCHITECTURE.md
2. INIT/02_MATHEMATICAL_LANGUAGE.md
3. INIT/04_AUDIT_PROTOCOL.md
4. INIT/05_COMPUTATION_DISCIPLINE.md
5. INIT/06_TERMINOLOGY.md
6. INIT/07_COMMUNICATION_STANDARD.md
7. INIT/AUDITOR.md

Auditors do not need INIT/03_RESEARCH_PROTOCOL.md unless an assigned audit genuinely depends on project-strategy context.

### Astra

Astra is a scarce strategic resource and has a special lean startup.

Read:

1. START.md
2. INIT/ASTRA.md

Then follow INIT/ASTRA.md. Astra does not perform the ordinary full worker initialization unless a concrete strategic dependency actually requires additional files.

Other roles do not read INIT/ASTRA.md.

## Numbered and role-specific init files

The numbered INIT files are shared policy modules. They are not automatically mandatory for every role; the role table above is authoritative.

Role-specific files are intentionally unnumbered:

- INIT/ASTRA.md — lean strategic startup and operating protocol for Astra only;
- INIT/AUDITOR.md — detailed independent-audit operation for Auditors only.

If a future policy file is added, START.md must be updated at the same time to say which roles read it. Directory enumeration is not a substitute for role routing.

## Mathematical startup after policy initialization

### Researcher and Vice Director

Read completely from one coherent repository revision:

- PROOF_SPINE/TWO_TIGHT_PATHS.md;
- RESEARCH_TREE.md;
- TOOLKIT/README.md and every standalone toolkit module currently indexed there.

The shelves are retrieved by mathematical relevance rather than read universally. A Vice Director normally reads the current SHELVES/CORE/ files touching the live proof coordinate during synchronization; researchers read shelf files when current guidance or their assigned mathematics depends on them.

### Auditor

Do not perform a universal proof-spine/toolkit/shelf soak merely because an audit begins.

Read the exact assigned target, the canonical facts and explicit dependencies needed to verify it, and enough surrounding context to type the statement correctly. INIT/AUDITOR.md governs the detailed retrieval posture.

### Astra

Do not perform the ordinary mathematical startup above. INIT/ASTRA.md governs Astra synchronization and explicitly prefers live deltas and exact strategic dependencies over a full-project soak.

## Preferred retrieval when shell Git is available

For ordinary workers, use one repository revision for policy and mathematical startup. Sparse checkout is encouraged when useful.

For example:

git clone --filter=blob:none --sparse https://github.com/SirCaptainCaleb/GN3_RESEARCH.git
cd GN3_RESEARCH
git sparse-checkout set INIT PROOF_SPINE TOOLKIT RESEARCH_TREE.md

Read only the files required by the assigned role.

## GitHub-connector retrieval

Pin initialization to one main-branch commit.

1. Fetch the main branch and record the commit SHA.
2. Fetch only the role-required INIT files at that revision.
3. Read each required file completely.
4. For Researcher/Vice Director startup, read the required proof spine, research tree, and indexed toolkit from the same revision.
5. For Auditor or Astra startup, follow the role-specific minimal retrieval rules above instead of expanding automatically.

For a long file that must be read completely, obtain its blob SHA and read the complete blob rather than relying on truncated excerpts.

## Staying current after initialization

Initialization is one-time for a continuing worker.

Use #gn3-changelog as the normal continuity stream. A material change to START.md, any init policy relevant to a role, the canonical proved/open boundary, or another durable fact an already-initialized worker needs must be surfaced there.

A changelog entry should state a sufficiently precise delta or explicitly name what must be reread. Full reinitialization is exceptional and must be stated explicitly when genuinely required.

For each relevant new changelog entry:

- incorporate a sufficiently precise stated delta directly;
- reread a named file or section when the delta is not enough to work safely;
- read exact current mathematics when a task depends on changed exact text;
- do not restart the full initialization sequence merely because ordinary project state advanced.

Astra has the stricter resource-conservation rule in INIT/ASTRA.md: continued Astra conversations should synchronize through live deltas rather than resoak the project.
