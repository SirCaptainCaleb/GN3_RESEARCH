# Research workflow

## Working principle

**Publish cheaply downward; compress deliberately upward.**

Use Brainstorms for loose ideation, Items for local mathematical development (including audits, strategic notes, techniques, and findings), Subsections for groups of Items, Sections for coherent research regions, Articles for top-level routes, and Toolkit for reusable mathematics that naturally crosses routes.

## Session lifecycle

Use boot() once at conversational-worker startup. Keep the returned session_id and reuse it for every later write in that conversation. Use status() for current project state and changes(...) for incremental updates.

## Development and composition

Items are the primary development objects, and each Item may contain multiple named Results. Subsections, Sections, and Articles organize collections of their direct children and expose compositions. Historical Subsection development is retained as legacy-development Items.

Treat each composition as a deliberately lossy compression of the material below it.

Create Items freely in the relevant Subsection. Develop their individual Results with statements, evidence, proofs, and status. Compose an Item when its Results form a useful synthesis, then compose its parent Subsection, Section, and Article at natural accumulation points.

## Composition eligibility and publication standard

Articles, Sections, and Subsections may have **no composition**. That is an ordinary, valid state, not an error or an obligation to manufacture prose. Compose only when the child material supports a coherent mathematical argument. In all read, status, tree, and mirror interfaces, distinguish absent composition from an existing composition and never substitute an invented summary or a child inventory as if it were a mathematical composition.

Every composition that does exist must read as a genuine mathematical publication at its level: an Article as an integrated paper-scale argument, a Section as a developed section of that paper, and a Subsection as a coherent local mathematical exposition. State precisely defined hypotheses, objects, results, proofs or explicitly identified proof gaps, and logical dependencies. Define every technical term in the composition itself or in the project Dictionary; distinguish proved claims from conjectures, heuristics, and strategic tasks. Synthesize children mathematically rather than listing them or narrating the work history. A list of item titles, numbered container references, status bullet points, or a progress report is not a composition. When the material is not yet ripe for mathematical synthesis, leave its parent composition absent and keep working in Items and Results.

## Publication-worthy selective synthesis

**Publication-worthy selective synthesis** is the two-part operation of (1) integrating selected lower-level mathematics into a coherent, precise, publication-quality argument and (2) deliberately omitting lower-level material that is superseded, redundant, exploratory, inconclusive, or no longer relevant to the strongest route. An Article may omit Sections, a Section may omit Subsections, and a Subsection may omit Items or individual Results. Omitted material remains preserved in its own lower-level records; omission means exclusion from the higher-level exposition, not deletion. Dependencies identify the selected mathematical inputs, not every child in the container. A composition is not a catalog, progress report, or mandatory summary of all children.

## Dependencies and staleness

Dependencies belong to compositions. An Item composition compresses its Results. A Subsection composition may depend on selected direct Item compositions; a Section composition may depend on selected direct Subsection compositions; an Article composition may depend on selected direct Section compositions.

A composition becomes stale only when an explicitly depended-on composition is replaced by a newer composition version. Frontier metadata separately records what lower-level material existed when the composition was written.

## Research flow

Read the current composition first, then inspect its dependent children. Use Subsections to locate Items and Items to locate individual Results. Use changes(...) to refresh work beyond the artifact snapshot and read(...) for exact live content.

When new mathematics changes the best exposition, update the relevant Item or Result and recompose upward when accumulation makes a synthesis worthwhile.

## Audits

Audit canonical mathematical claims. When an audit finds a localized gap or correction, publish a focused audit Item in the appropriate Subsection stating the claim, the issue, and the repair obligation. Recompose after the repaired mathematics has stabilized.

After making a substantive repair, judge whether the repaired result should be audited by another worker; request an audit when independent verification is warranted.

## Concurrent publication

Use staged batches for related multi-object writes. Review the decoded batch for overlap, then commit it atomically.

## Style

Use standard mathematical vocabulary and the project Dictionary. State results publication-style, preserve useful failed routes as development evidence, and keep operational instructions concise and affirmative.

## Publication-quality selective synthesis

Publication-quality selective synthesis combines two operations: integrating selected child mathematics into a coherent, rigorous argument, and deliberately omitting material superseded by stronger arguments, redundant, exploratory, or no longer part of the best route. The composition must read as mathematical publication prose, with precise statements, proofs or clear gaps, and every technical term defined locally or in the Dictionary. Articles may omit Sections, Sections may omit Subsections, and Subsections may omit Items or individual Results. Omission from a composition never deletes the underlying research. Dependencies identify the child compositions actually used, not an inventory of all children.


## Consumption references

Consumption is independent of containment and independent of the existence of a composition. Each Section, Subsection, Item, and Result stores an authoritative, possibly empty, multi-valued consumed_by list. A mathematical component may be consumed by multiple parents at the next research level, including reusable Article-local lemmas; it need not enter the Toolkit. Articles, Sections, Subsections, and Items expose a cached consumes list, recalculated only when a child consumption relationship changes. Workers may atomically replace a parent's consumed set via set_consumes(session, parent_type, parent_id, child_ids); this updates each child and removes only the omitted relation to this parent, retaining other consumers. Workers may update a child directly via set_consumed_by(session, child_type, child_id, consumer_ids). Parent creation and metadata edits may pass consumes as a JSON array. Omitting consumes leaves relationships unchanged; [] clears this parent's links. A consumption relationship does not assert that a composition exists or that mathematics has been proved.


## Unified typed research nodes

Articles, Sections, Subsections, Items, and Results are represented in one per-schema nodes table keyed by globally unique ID (within that schema). The type column identifies the level; data holds the full typed record. All Article, Section, Subsection, Item, Result, Toolkit, and auxiliary-document records live exclusively in the per-schema nodes table. Their globally unique IDs are enforced by its primary key; the retired level-specific content tables no longer exist. Consumption APIs resolve types from IDs automatically: set_consumes(session, parent_id, child_ids) and set_consumed_by(session, child_id, consumer_ids). Do not supply redundant type parameters. The child consumed_by array is authoritative and the parent consumes array is updated on changes, not on reads.


## Brainstorms are typed research nodes

Brainstorms are stored in the same per-project nodes table as Articles, Sections, Subsections, Items, Results, Toolkit records, and auxiliary documents, with type=brainstorm. Their id is globally unique within the project schema. Brainstorm metadata (title, seed, body, version, created_at, updated_at, closed_at, outcome, promoted_to_id) lives in nodes.data and the corresponding projected columns. There is no separate brainstorms table. Use brainstorms(), save_brainstorm(session,payload,expected_version), or promote_brainstorm(session,id,payload,expected_version) as before. Promotion now preserves both the original seed and full body in a new Item under a newly created Subsection of the promoted Section, rather than putting mathematical development in the Section body. Original provenance and declared promotion dependencies remain in the Item metadata. Promotion and brainstorm closing are atomic.


## Bottom-up Article composition intake

When Article/Section/Subsection compositions are blank or stale, do not guess the proof frontier. Start with article_subsection_intake(article_id, offset, limit, result_order) (default offset 0, limit 25, newest). This pages ALL Subsections whose parent Section is explicitly assigned to that Article. Each entry includes Section ordering, Subsection ID/title/number, the Subsection composition version (null if not composed), full Items and their full Results, Item composition versions, and creation_global_revision metadata where available. Follow has_more and increment offset by limit until every Subsection is acquired. Compose each Subsection from its Items and Results, then compose Sections, then the Article as a coherent current argument. For a flat creation-ordered feed use article_results(article_id,offset,limit,order), order newest or oldest (defaults newest). Results sort by global creation revision where known, otherwise creation timestamps. Never equate latest Result with strongest proof. These intake APIs are read-only and exist in NOR, GN3N, LINP, and the project template.


## Article and Section manuscript self-containment (mandatory)
An Article composition is a self-contained mathematical manuscript. A reader must be able to follow its definitions, hypotheses, deductions and exact unresolved proof obligations without reading its Sections, Subsections, Items, Results, research history, prior Articles or broadcasts. The only permitted external mathematical prerequisites are explicitly identified results in the Toolkit and terminology already defined precisely in the Dictionary. When a local result is indispensable, integrate its precise statement and the mathematical proof (or a genuinely sufficient proof) directly into the Article; a citation to an internal Section or a phrase such as "the earlier reductions show" is not a substitute. Any dependency on a conjectural or unproved step must be identified before it is used, and the conclusion must retain that qualification.

A Section composition is a publication-ready mathematical section: all reasoning must be rigorous, grammatically natural and internally coherent, but it may use definitions and established hypotheses already introduced by the containing Article. A Subsection composition is publication-ready local exposition and may rely on explicitly identified local context at its Section level. This difference concerns self-containment only, not standards of proof.

Prefer ordinary professional mathematical prose: introduce objects with "Let X be ...", specifying assumptions and scope, before using definite references such as "the object". Do not write "fix the ..." unless the object has already been introduced, or the quantification has otherwise been stated. Introduce notation when used; define each technical noun locally or rely on an exact Dictionary definition. Do not conflate a general problem with a special subclass; every reduction or additional hypothesis must be established before use. Explain and prove every reduction in scope or explicitly cite an applicable Toolkit theorem. Avoid managerial phrases ("current frontier", "the existing construction", "research route", "our progress") in the body of the manuscript; express an unresolved obligation mathematically after the preceding argument naturally leads to it. Write as a continuous proof with clear lemmas or theorem statements where needed, not as a chronology or inventory of Results. Revise phrasing for idiomatic English and readability as carefully as for correctness. Publication-ready does not mean merely marked current by the composition database.
