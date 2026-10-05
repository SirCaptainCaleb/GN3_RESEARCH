# Research workflow


# Research workflow

## Working principle

**Publish cheaply downward; compress deliberately upward.**

Use Brainstorms for loose ideation, Subsections for local mathematical development, Sections for coherent research regions, Articles for top-level routes, and Toolkit for reusable mathematics that naturally crosses routes.

## Development and composition

Development records the mathematics being worked on. Composition is the current concise canonical rendering of that same node.

Create local branches freely as Subsections. Edit earlier development whenever later mathematics improves it. Compose when a node has enough coherent mathematics to deserve a readable canonical form.

Composition is selective: preserve useful lower-level development even when the composition omits it.

## Dependencies

The dependency graph alternates between development and composition layers.

- A composition automatically depends on the current development version of the same node.
- Section development may depend on selected Subsection compositions.
- Article development may depend on selected Section compositions.
- Subsection development declares an explicit empty dependency list.
- Every development save records its direct dependencies explicitly.

Staleness records an exact source-version mismatch. A stale source remains usable as recorded context; downstream staleness begins when the exact source layer and version named by a dependency changes.

## Research flow

Read the current composition first, then inspect the specific development or dependencies relevant to the task. Use changes(...) to refresh work beyond the artifact snapshot and read(...) for exact live content.

When new mathematics changes the best exposition, update the relevant development and recompose upward when the synthesis is worthwhile.

## Audits

Audit canonical mathematical claims. When an audit finds a localized gap or correction, publish a focused audit Subsection stating the claim, the issue, and the repair obligation. Recompose after the repaired mathematics has stabilized.

## Concurrent publication

Use staged batches for related multi-object writes. Review the decoded batch for overlap, then commit it atomically.

## Style

Use standard mathematical vocabulary and the project Dictionary. State results publication-style, preserve useful failed routes as development evidence, and keep operational instructions concise and affirmative.
