# Connector and retrieval guidance

**Status: STARTUP MECHANICS.**

This file governs how GN3 startup material is retrieved and read. It is not mathematical policy.

## Whole-file invariant

When `START.md`, this file, or any role-specific startup instruction directs a worker to read a file, that means **read the entire current file**.

A search hit, excerpt, truncated connector response, summary, remembered content, or partial line range does not count as having read that file. Do not begin substantive work while a required startup file is only partially read.

If a connector cannot return a long file in one response, obtain the file's exact blob/revision and read the complete contents through the connector's whole-file/blob mechanism. If complete retrieval is not possible, stop and repair retrieval rather than silently proceeding from fragments.

## Revision coherence

For a fresh ordinary startup, pin one repository revision and read all required startup files from that same revision when practical. Do not mix policy, proof-spine, research-tree, or toolkit files from unrelated revisions merely because `main` advances during initialization.

## Ordinary role routes

After reading this file completely:

### Researcher

Read completely:

1. `INIT/01_ARCHITECTURE.md`
2. `INIT/02_MATHEMATICAL_LANGUAGE.md`
3. `INIT/03_RESEARCH_PROTOCOL.md`
4. `INIT/05_COMPUTATION_DISCIPLINE.md`
5. `INIT/06_TERMINOLOGY.md`
6. `INIT/07_COMMUNICATION_STANDARD.md`

Then read completely, from the same startup revision:

- `PROOF_SPINE/TWO_TIGHT_PATHS.md`
- `RESEARCH_TREE.md`
- `TOOLKIT/README.md`
- every standalone toolkit module currently indexed by `TOOLKIT/README.md`

Retrieve shelf files only when current guidance or assigned mathematics depends on them.

### Vice Director

Read completely:

1. `INIT/01_ARCHITECTURE.md`
2. `INIT/02_MATHEMATICAL_LANGUAGE.md`
3. `INIT/03_RESEARCH_PROTOCOL.md`
4. `INIT/04_AUDIT_PROTOCOL.md`
5. `INIT/05_COMPUTATION_DISCIPLINE.md`
6. `INIT/06_TERMINOLOGY.md`
7. `INIT/07_COMMUNICATION_STANDARD.md`

Then read completely the same proof spine, research tree, toolkit index, and indexed toolkit modules required of a Researcher. Read the core shelves relevant to the live proof coordinate during synchronization.

### Auditor

Read completely:

1. `INIT/01_ARCHITECTURE.md`
2. `INIT/02_MATHEMATICAL_LANGUAGE.md`
3. `INIT/04_AUDIT_PROTOCOL.md`
4. `INIT/05_COMPUTATION_DISCIPLINE.md`
5. `INIT/06_TERMINOLOGY.md`
6. `INIT/07_COMMUNICATION_STANDARD.md`
7. `INIT/AUDITOR.md`

Then read the exact assigned target and every exact dependency needed to audit it. Auditors do not perform a universal proof-spine/toolkit/shelf soak unless the target itself requires it.

## Astra

Astra does not use the ordinary startup route. After `START.md`, read `INIT/ASTRA.md` completely and follow its lean shelf-delta protocol.

## Staying current

Initialization is one-time for a continuing worker. Use `#gn3-changelog` as the normal continuity stream.

If a changelog entry says a file must be reread, reread that file **completely** unless the entry explicitly identifies a self-contained replacement section that is itself the whole required unit. Do not defensively restart full initialization for ordinary project movement.

Astra follows the stricter catch-up rules in `INIT/ASTRA.md`.
