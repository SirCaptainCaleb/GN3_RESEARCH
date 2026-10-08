# Research workflow

## Working principle

**Publish cheaply downward; compress deliberately upward.**

Use Brainstorms for loose ideation, Items for local mathematical development (including audits, strategic notes, techniques, and findings), Subsections for groups of Items, Sections for coherent research regions, Articles for top-level routes, and Toolkit for reusable mathematics that naturally crosses routes.

## Session lifecycle

Use boot() once at conversational-worker startup. Keep the returned session_id and reuse it for every later write in that conversation. Use status() for current project state and changes(...) for incremental updates.

## Development and composition

Items are atomic research contributions directly under Subsections. Each Item independently records one theorem, proof, audit addendum, note, technique, question, clarification, code contribution, or other research contribution, with its own kind, body, status, version, and dependencies. Items contain no child research nodes and have no compositions. Subsections, Sections, and Articles organize direct children and may expose compositions. Historical Subsection development is retained as legacy-development Items.

Treat each composition as a deliberately lossy compression of the material below it.

Create atomic Items freely in the relevant Subsection. Give mathematical Items precise statements, evidence, proofs, and status in the Item itself; use other Item kinds for audits, techniques, questions, clarifications, and code. Compose the parent Subsection, Section, and Article when the material supports coherent mathematical synthesis. Never compose Items.

## Composition eligibility and publication standard

Articles, Sections, and Subsections may have **no composition**. That is an ordinary, valid state, not an error or an obligation to manufacture prose. Compose only when the child material supports a coherent mathematical argument. In all read, status, tree, and mirror interfaces, distinguish absent composition from an existing composition and never substitute an invented summary or a child inventory as if it were a mathematical composition.

Every composition that does exist must read as a genuine mathematical publication at its level: an Article as an integrated paper-scale argument, a Section as a developed section of that paper, and a Subsection as a coherent local mathematical exposition. State precisely defined hypotheses, objects, mathematical results, proofs or explicitly identified proof gaps, and logical dependencies. Define every technical term in the composition itself or in the project Dictionary; distinguish proved claims from conjectures, heuristics, and strategic tasks. Synthesize children mathematically rather than listing them or narrating the work history. A list of Item titles, numbered container references, status bullet points, or a progress report is not a composition. When material is not ripe for mathematical synthesis, leave its parent composition absent and keep working in Items.

## Publication-worthy selective synthesis

**Publication-worthy selective synthesis** is the two-part operation of (1) integrating selected lower-level mathematics into a coherent, precise, publication-quality argument and (2) deliberately omitting lower-level material that is superseded, redundant, exploratory, inconclusive, or no longer relevant to the strongest route. An Article may omit Sections, a Section may omit Subsections, and a Subsection may omit Items. Omitted material remains preserved in its own lower-level records; omission means exclusion from higher-level exposition, not deletion. Dependencies identify selected mathematical inputs, not every child in the container.

## Dependencies and staleness

Dependencies of compositions belong to Articles, Sections and Subsections. A Subsection composition may select direct atomic Items as sources; a Section composition may depend on selected direct Subsection compositions; an Article composition may depend on selected direct Section compositions. An Item may declare research consumption relationships independently, without acquiring a composition.

A composition becomes stale only when an explicitly depended-on composition is replaced by a newer composition version. Frontier metadata separately records what lower-level material existed when the composition was written.

## Research flow

Read the current composition first, then inspect its dependent children. Use Subsections to locate their atomic Items. Use changes(...) to refresh work beyond the artifact snapshot and read(...) for exact live content.

When new mathematics changes the best exposition, update the appropriate atomic Item and recompose its Subsection, Section and Article when accumulation makes a synthesis worthwhile.

## Audits

Audit canonical mathematical claims. When an audit finds a localized gap or correction, publish a focused audit Item in the appropriate Subsection stating the claim, the issue, and the repair obligation. Recompose after the repaired mathematics has stabilized.

After making a substantive repair, judge whether the repaired result should be audited by another worker; request an audit when independent verification is warranted.

## Concurrent publication

Use staged batches for related multi-object writes. Review the decoded batch for overlap, then commit it atomically.

## Style

Use standard mathematical vocabulary and the project Dictionary. State results publication-style, preserve useful failed routes as development evidence, and keep operational instructions concise and affirmative.

## Publication-quality selective synthesis

Publication-quality selective synthesis combines two operations: integrating selected child mathematics into a coherent, rigorous argument, and deliberately omitting material superseded by stronger arguments, redundant, exploratory, or no longer part of the best route. The composition must read as mathematical publication prose, with precise statements, proofs or clear gaps, and every technical term defined locally or in the Dictionary. Articles may omit Sections, Sections may omit Subsections, and Subsections may omit Items. Omission from a composition never deletes the underlying research. Dependencies identify child compositions or atomic Item sources actually used, not an inventory of all children.


## Consumption references

Consumption is independent of containment and of composition. Sections, Subsections and Items maintain authoritative consumed_by relationships with other research nodes; multiple consumers may reuse the same Item. Articles, Sections, and Subsections may expose cached consumes lists. Workers can atomically set consumes or consumed_by through the project APIs; ID-based calls resolve types. An Item can cite other Items without containing them. A consumption relation does not imply a composition or a proved claim.


## Unified typed research nodes

Articles, Sections, Subsections, and atomic Items are represented in one per-schema nodes table keyed by an ID unique within that schema. The type identifies the level and data holds the full record. A former Result node is now an Item, with its original ID, statement, proof, status and provenance retained. There is no separate Result node type and no Item composition. Toolkit and auxiliary records share the nodes table. Consumption APIs resolve node types by ID.


## Brainstorms are typed research nodes

Brainstorms are stored in the same per-project nodes table as Articles, Sections, Subsections, Items, Toolkit records, and auxiliary documents, with type=brainstorm. Their IDs are globally unique within the project schema. Brainstorm metadata lives in nodes.data and projected columns. Use brainstorms(), save_brainstorm(session,payload,expected_version), or promote_brainstorm(session,id,payload,expected_version). Promotion preserves the original seed and full body in an Item under a Subsection of the promoted Section.


## Bottom-up Article composition intake

When Article/Section/Subsection compositions are blank or stale, read the existing compositions and all relevant atomic Items to establish the real proof frontier; never infer strength solely from recency. Use article_subsection_intake(article_id, offset, limit, result_order) or article_results(article_id,offset,limit,order) only as historical read-only compatibility APIs if available: their result-named fields reflect older layouts and must be interpreted as atomic Item content. Read direct Items and their current versions, and compose bottom-up: Subsection, Section, Article. Do not create Result nodes or Item compositions.


## Article and Section manuscript self-containment (mandatory)
An Article composition is a self-contained mathematical manuscript. A reader must be able to follow its definitions, hypotheses, deductions and exact unresolved proof obligations without reading its Sections, Subsections, Items, research history, prior Articles or broadcasts. Only explicitly identified Toolkit theorems and precise Dictionary definitions are permitted as external mathematical prerequisites. Integrate indispensable local statements and proofs directly into the Article. Qualify every conjectural or unproved step.

A Section composition is a publication-ready mathematical section: all reasoning must be rigorous, grammatically natural and internally coherent, but it may use definitions and established hypotheses already introduced by the containing Article. A Subsection composition is publication-ready local exposition and may rely on explicitly identified local context at its Section level. This difference concerns self-containment only, not standards of proof.

Prefer ordinary professional mathematical prose: introduce objects with "Let X be ...", specifying assumptions and scope, before using definite references such as "the object". Do not write "fix the ..." unless the object has already been introduced, or the quantification has otherwise been stated. Introduce notation when used; define each technical noun locally or rely on an exact Dictionary definition. Do not conflate a general problem with a special subclass; every reduction or additional hypothesis must be established before use. Explain and prove every reduction in scope or explicitly cite an applicable Toolkit theorem. Avoid managerial phrases ("current frontier", "the existing construction", "research route", "our progress") in the body of the manuscript; express an unresolved obligation mathematically after the preceding argument naturally leads to it. Write as a continuous proof with clear lemmas or theorem statements where needed, not as a chronology or inventory of Results. Revise phrasing for idiomatic English and readability as carefully as for correctness. Publication-ready does not mean merely marked current by the composition database.
