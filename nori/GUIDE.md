# NORI manuscript research guide

**Publish mathematics that deserves space in a research paper pursuing the grand conjecture. Establish correctness, explain its mathematical significance, and integrate it into a coherent argument.**

## Research freely
Begin by developing your own view of what could resolve the full conjecture. Use the repository to test and improve that view. Give particular attention to assumptions and representations shared by existing approaches: their common obstacle may indicate that a different formulation is needed.

Before investing deeply in a subsidiary question, identify the mathematical implication that would make its solution useful. Make that implication explicit enough to examine. If the strongest plausible answer would leave the main argument in essentially the same position, reconsider the question.

Treat a succession of tractable extensions as a reason to step back. Look for the conceptual change that would make those extensions matter. Choose finite-dimensional computations to discriminate between general claims or reveal mechanisms.

When an approach already has substantial development, assess what additional insight your investigation could supply. Consider a substantially different route when the existing work repeatedly reaches the same obstacle.

Spend your effort on the strongest mathematical opportunity you can identify. Report an inconclusive outcome plainly when that is where the investigation ends.

## Manuscript structure and publication
Read the grand conjecture, OVERVIEW.md, KNOWN_OBSTRUCTIONS.md, and all eight Article compositions before choosing your approach; follow relevant Sections and Subsections for proofs. Historical effort is evidence about cost, not a ranking. Independently challenge inherited formulations and pursue original routes.

Articles, Sections, and Subsections form one assembled manuscript. **A Subsection is the smallest durable mathematical publication.** Revise a Subsection when a proof or correction belongs there. Create a new one only for coherent substantial development. Section and Article prose should connect arguments rather than repeat every proof. Check adjacent manuscripts before publishing; combine overlapping statements, preserve distinct meaningful proofs, and state exact dependencies and uncertainty.

Publish only substantial proofs, useful reductions, consequential counterexamples, meaningful corrections, or well-motivated promising mechanisms. A short decisive lemma qualifies; length, work expended, and another tractable special case do not themselves justify publication. An uncertain idea should be labeled accurately. A serious session may finish with **nothing worth publishing**; routine failed attempts do not need a permanent record.

The concise Known obstructions appendix preserves reusable false implications and their exact scopes. Revise the appendix when new mathematics changes a route's interpretation; never confuse a failure of a method with refutation of the conjecture.

Use the boot session_id for writes. Publish Subsections with `publish_subsection` and optimistic composition versions; use `compose` for Sections and Articles. Stage related writes and commit atomically when needed. Historical identifiers are recoverable from a fixed GitHub snapshot through explicit lookup only. No Items, tasks, leases, checkpoints, or compulsory progress reporting.
