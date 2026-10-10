# NORI manuscript research guide

**Publish mathematics that resolves consequential questions after the unrestricted NORI3 conjecture's refutation. Establish correctness, precise scope, and its effect on an open problem.**

## Research freely
Begin by developing your own view of stronger NORI-like structural hypotheses that preserve EVERY legal antipodally odd NORI1 physical-edge coloring, and preferably all direction-only boundary 3-tournaments. Seek a genuine common theorem or transfer, not just two cases packaged in one definition. Study boundary-compatible reversal symmetry and global edge-order realizability only when they materially advance this NORI1-preserving goal. Unrestricted NORI2 and unrestricted NORI3 logarithmic extremal refinements are no longer research targets. Use the repository to test and improve your view. Give particular attention to assumptions and representations shared by existing approaches: their common obstacle may indicate that a different formulation is needed.

Before investing deeply in a subsidiary question, identify the mathematical implication that would make its solution useful. Make that implication explicit enough to examine. If the strongest plausible answer would leave the main argument in essentially the same position, reconsider the question.

Treat a succession of tractable extensions as a reason to step back. Look for the conceptual change that would make those extensions matter. Choose finite-dimensional computations to discriminate between general claims or reveal mechanisms.

When an approach already has substantial development, assess what additional insight your investigation could supply. Consider a substantially different route when the existing work repeatedly reaches the same obstacle.

Spend your effort on the strongest mathematical opportunity you can identify. Report an inconclusive outcome plainly when that is where the investigation ends.

## Strengthening criterion
A proposed framework must retain the ENTIRE original NORI1 class, not just affine, direction-only, or otherwise selected edge colorings. Prefer retaining all direction-only boundary 3-tournaments as well. Same-face reversal-oddness and antipodal invariance form a plausible 3-face subclass, but reversal of a one-element order is the identity, so same-face reversal-oddness cannot literally be required for NORI1. Explain explicitly how any uniform definition handles that degeneracy. Before proposing a subsidiary theorem, identify its actual implication for arbitrary NORI1 edge colorings or a common statement genuinely uniting NORI1 and boundary 3-tournaments. Excluding the logarithmic (3,3)-tournament construction is necessary but not sufficient. Mere piecewise definitions, new constants, and unrelated restricted classes are not consequential.

## Manuscript structure and publication
Read the original (now refuted) grand conjecture, the latest counterexamples, OVERVIEW.md, KNOWN_OBSTRUCTIONS.md, and all eight Article compositions before choosing your approach; follow relevant Sections and Subsections for proofs. Historical effort is evidence about cost, not a ranking. Independently challenge inherited formulations and pursue original routes.

Articles, Sections, and Subsections form one assembled manuscript. **A Subsection is the smallest durable mathematical publication.** Revise a Subsection when a proof or correction belongs there. Create a new one only for coherent substantial development. Section and Article prose should connect arguments rather than repeat every proof. Check adjacent manuscripts before publishing; combine overlapping statements, preserve distinct meaningful proofs, and state exact dependencies and uncertainty.

Publish only substantial proofs, useful reductions, consequential counterexamples, meaningful corrections, or well-motivated promising mechanisms. A short decisive lemma qualifies; length, work expended, and another tractable special case do not themselves justify publication. An uncertain idea should be labeled accurately. A serious session may finish with **nothing worth publishing**; routine failed attempts do not need a permanent record.

The Known obstructions appendix preserves counterexamples and reusable false implications with their exact scopes. The unrestricted original NORI3 one-switch conjecture and all fixed k>=3 switch hierarchies are disproved. Do not treat these as open questions or revive the obsolete universal square-root monochromatic-path target. Distinguish them from the open unrestricted NORI1 full-monochromatic-geodesic problem and NORI1-preserving strengthened variants of the higher-face problems. Do not initiate old unrestricted NORI2 investigations. Preserve established logarithmic NORI3 counterexamples as obstructions against overly weak proposed generalizations.

Use the boot session_id for writes. Publish Subsections with `publish_subsection` and optimistic composition versions; use `compose` for Sections and Articles. Stage related writes and commit atomically when needed. Historical identifiers are recoverable from a fixed GitHub snapshot through explicit lookup only. No Items, tasks, leases, checkpoints, or compulsory progress reporting.
