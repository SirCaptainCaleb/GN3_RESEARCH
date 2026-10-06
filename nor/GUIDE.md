# Research workflow

## Working principle

**Publish cheaply downward; compress deliberately upward.**

Use Brainstorms for loose ideation, Subsections for local mathematical development, Sections for coherent research regions, Articles for top-level routes, and Toolkit for reusable mathematics that naturally crosses routes.

## Development and composition

Subsections are the manuscript development objects. Sections and Articles organize material and expose compositions rather than independent development prose.

Treat each composition as a deliberately lossy compression of the material below it.

Create local mathematical branches freely as Subsections. Edit earlier Subsection development whenever later mathematics improves it. Recompose Sections and Articles when a better synthesis is worthwhile.

## Dependencies and staleness

Dependencies belong to compositions. A Section composition may depend on selected direct Subsection compositions; an Article composition may depend on selected direct Section compositions; a Subsection composition has no lower composition layer.

A composition becomes stale only when an explicitly depended-on composition is replaced by a newer composition version. Frontier metadata separately records what lower-level material existed when the composition was written.

## Research flow

Read the current composition first, then inspect the Subsections or dependencies relevant to the task. Use changes(...) to refresh work beyond the artifact snapshot and read(...) for exact live content.

When new mathematics changes the best exposition, update the relevant Subsection development and recompose upward when the synthesis is worthwhile.

## Audits

Audit canonical mathematical claims. When an audit finds a localized gap or correction, publish a focused audit Subsection stating the claim, the issue, and the repair obligation. Recompose after the repaired mathematics has stabilized.

After making a substantive repair, judge whether the repaired result should be audited by another worker; request an audit when independent verification is warranted.

## Concurrent publication

Use staged batches for related multi-object writes. Review the decoded batch for overlap, then commit it atomically.

## Style

Use standard mathematical vocabulary and the project Dictionary. State results publication-style, preserve useful failed routes as development evidence, and keep operational instructions concise and affirmative.
