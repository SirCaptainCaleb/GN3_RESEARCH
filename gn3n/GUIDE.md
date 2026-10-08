# Research workflow

## Working principle

**Develop freely in atomic Items; publish selectively upward.**

Use Brainstorms for loose ideation, Items for individual research contributions, Subsections for local mathematical development, Sections for coherent regions, Articles for principal arguments, and Toolkit for reusable mathematics across routes.

## Session lifecycle

Call boot() once per conversational worker. Reuse its session_id for subsequent writes. Use status() for project state, changes(...) for updates since the artifact snapshot, and read(...) for exact live content.

## Atomic Items and compositions

Each Item belongs directly to a Subsection and is an atomic contribution: for example, a theorem, proof, audit addendum, technique, relationship, question, clarification, or shared code. Give it a descriptive kind, title, body, and appropriate mathematical statement, proof, status, and references. Items have versions and may consume other Items, but contain no child research nodes and have no compositions. The retired Result node type is not used; the ordinary mathematical word “result” remains appropriate.

Only Subsections, Sections, and Articles have compositions. A missing composition is valid: never invent prose to fill it. Compose when selected child material supports a coherent mathematical exposition, not merely because new Items exist. Update an Item when its mathematics changes and recompose higher levels when the best argument warrants it.

## Publication standard and selective synthesis

A composition is nearly publication-ready mathematical prose, not a digest, inventory, chronology, or progress report. Integrate the strongest relevant child mathematics into a coherent argument with explicit hypotheses, definitions, statements, proofs, logical dependencies, and clearly identified gaps. Distinguish theorems from conjectures and heuristics. Use standard terminology, the project Dictionary, and natural mathematical language. Establish every reduction and additional assumption; do not silently transfer a claim from a special class to a broader one. Explain unresolved obligations mathematically rather than in managerial language.

**Selective synthesis** means both integrating chosen contributions rigorously and omitting superseded, redundant, exploratory, inconclusive, or irrelevant material. An Article may omit Sections, a Section may omit Subsections, and a Subsection may omit Items; omission does not delete the underlying work. Dependencies identify what the exposition actually uses, not every descendant. Never mistake permission to omit material for permission to omit necessary arguments.

An Article must stand alone as a manuscript: include indispensable local mathematics and proofs directly rather than citing internal Sections or Items as substitutes. Only precise Dictionary definitions and explicitly identified Toolkit results may serve as external mathematical prerequisites. Sections may rely on established Article context; Subsections may rely on identified Section context. **All three levels require the same rigor and editorial quality.** Define objects before referring to them, introduce notation before using it, write continuous arguments with lemmas where helpful, and revise grammar and mathematical phrasing as carefully as correctness. A composition's database status alone does not certify publication quality.

## Dependencies and staleness

A Subsection composition selects atomic Items as sources; a Section composition selects Subsection compositions; an Article composition selects Section compositions. Only a newer version of an explicitly depended-on composition causes dependency staleness. Frontier metadata separately records which lower-level material existed at composition time. Item consumption relationships are independent of containment, composition, and proof status; an Item may be consumed by multiple research nodes without nesting.

## Research flow and auditing

Read current compositions before their supporting children. If an Article or Section is incomplete, inspect the relevant Subsections and atomic Items before deciding the proof frontier; recency is not evidence of mathematical strength. Compose bottom-up only when each level admits a rigorous synthesis.

Audit exact mathematical claims. For a localized gap, publish a focused audit Item identifying the affected claim, the missing justification or counterexample, and a repair obligation. Preserve surrounding valid arguments. Request independent verification when a substantive repair warrants it. Keep useful failed approaches as research evidence without promoting them as established mathematics.

For concurrent publication, stage related writes, inspect the decoded batch for conflicts, and commit atomically.

## Storage and auxiliary workflows

Articles, Sections, Subsections, Items, Toolkit records, Brainstorms, and auxiliary documents share each project's typed nodes table with project-unique IDs; data holds their records. The former Result node type has been retired, and its research content was migrated to Items without changing IDs. The consumption API resolves types from IDs: set_consumes(session,parent_id,child_ids) and set_consumed_by(session,child_id,consumer_ids). The child's consumed_by list is authoritative; a parent's consumes list is maintained when relationships change.

Brainstorms remain typed nodes, accessible using brainstorms(), save_brainstorm(...), and promote_brainstorm(...). Promotion preserves the original seed and full body in an Item under a newly created Subsection.

For bulk manuscript intake, use article_subsection_intake(...) and article_results(...) only where available as legacy read-only interfaces; names containing “result” reflect historical APIs, not a current Result node type. Verify what each returns against live Items. Build compositions in order: Subsection, Section, Article.
