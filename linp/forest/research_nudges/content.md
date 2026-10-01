# Research nudges

## Statement

Strongly encouraged project-local research heuristics. Researchers must seriously consider the applicable nudges as default methodological priors, but may depart from them when mathematical judgment gives a reason.

## Body

## Research nudges

These are methodological priors, not proof obligations. Seriously consider the applicable advice, then depart when the mathematics gives a concrete reason. The purpose is to complement sustained local proof search with deliberate changes of representation and earlier uses of new ideas. This is advice about research behavior, not a claim about the inherent abilities of any model or worker.

### Prioritize theorem-scale progress

- Optimize at the scale of the theorem. When the target is an asymptotic bound or coefficient improvement, strongly prefer work that can change the leading coefficient, expose new structure, or open a genuinely different route. Additive constants and lower-order terms are usually secondary.
- Before investing substantial effort in a quantitative refinement, ask whether it can actually change the leading term of the target theorem. If it cannot, prefer a cleaner proof or move on unless the refinement unlocks a structural mechanism, resolves a genuine finite obstruction, preserves an exact recurrence needed later, or is explicitly required downstream.
- Treat diminishing returns as a signal to search creatively. When a local route is producing only cosmetic constant improvements, actively look for a different witness, invariant, projection, charging scheme, extremal formulation, or bridge to another part of the proof rather than continuing to polish the same estimate.
- Do not equate technical tightness with research value. A slightly weaker but cleaner lemma that exposes the right mechanism can be more useful than a sharp local estimate that leaves the theorem's leading term unchanged.

### Choose the right statement and witness

- Keep the actual mathematical target separate from the team's current sufficient condition. A failed reconstruction, stubborn auxiliary conjecture, or elaborate reduction need not be an obstacle to the target itself.
- Before deep case analysis, return to the earliest inequality that loses the desired amount. State the exact improvement needed, its scale, and which information was discarded there.
- Choose an extremal witness to protect the quantity that the contradiction must exceed. A longest witness at one object need not be the best witness for a statement about another. Name the endpoint, entrance, label, or rank whose constraint the proposed modification will violate.
- Separate what a competing object is from what it does to this witness. Retain only the contacts, multiplicities, order, or other data needed for the argument. Reintroduce labels when the coarse projection is genuinely insufficient.
- Test whether a stronger-looking local assertion is easier because it has a cleaner witness or counts a more natural class. Conversely, weaken an unnecessarily strong intermediate demand if the global accounting needs less.

### Find and count the resource

- Ask what resource every obstruction consumes. Difficult configurations may pay through repeated contacts, unused positions, rank gaps, or another deficit; they need not all be excluded.
- When local accounting produces many indexed certificates, quotient by the underlying mathematical objects as early as possible when incidence bounds permit. Distinct objects are easier to globalize than center-indexed events; then attach a canonical global certificate (for example an exchange cycle, extremal-tree witness, or second independent representation) before attempting reuse/congestion bounds.
- Build incompatibility relations among cheap local states before enumerating whole configurations. Keep overlapping constraints when thinning them to a disjoint family loses a linear amount.
- Distinguish a matching bound, a fractional bound, and an integral extremal bound. Sharpness of one relaxation does not establish sharpness of the actual combinatorial problem.
- Look for a direct charging, run decomposition, or telescoping inequality behind a transfer calculation. Preserve an exact recurrence when residue corrections or equality structure matter.
- Track each loss with its scale. An O(1) local improvement usually changes an O(n) term, not a leading coefficient. Confirm the global algebra before investing in a difficult local refinement.

### Escape unproductive complexity without abandoning good work

- Growing case trees are a prompt to reconsider the projection or witness, not evidence that the route is wrong. Ask whether the accumulated rigidity reveals a simpler invariant or a larger compulsory cost.
- Revisit upstream uses whenever a new lemma lands. A new observation may make a downstream residual unnecessary, even if that residual has attracted substantial effort.
- Periodically restate the problem in ordinary mathematical language without inherited names. Distinguish intrinsic definitions from bookkeeping introduced by the current attack.
- Work forward from usable structure and backward from the theorem-closing inequality. Prefer a bridge between them over a disconnected collection of consequences.
- Persist with mechanisms that survive serious checks. Change course for a demonstrated obstruction, a failure of scaling, or a materially stronger alternative; neither sunk effort nor temporary difficulty is a sufficient reason by itself.

### Test, generalize, and publish

- Check every proposed splice or exchange for nonconsecutive intersections and endpoint legality. Drawn adjacency alone is not enough. Distinguish the existence of a witness from compatibility with the witness actually being used.
- Treat boundary conventions as bookkeeping, not geometric witnesses. If a definition assigns a value to a last edge, endpoint, degenerate cell, or exceptional case by convention, separate that case before invoking a lemma whose proof needs an actual contact, internal position, entrance, or exchange.
- Test an abstract extremal pattern in an actual object satisfying all original hypotheses. A realizable local extremizer can fence an entire strategy; an unrealizable one points to a missing constraint. State exactly which local or global claim an example does and does not obstruct.
- After a proof, test the mechanism for general uniformity, weighted counting, additional witnesses, stability, equality structure, and especially unused hypotheses. Ask explicitly: “What assumptions were not needed to get this result?” Do not carry every branch forward: publish the extensions that change a real bound or clarify a genuine obstruction.
- Preserve complete successful arguments promptly, including the witness choice, the decisive local operation, and the final counting. Separate proved statements, conditional reductions, proposals, and reconstructions; confidence in a progress summary is not a substitute for a saved proof.
- Use concurrent work to diversify mathematical viewpoints. Read exact load-bearing statements, refresh before duplicating a line, and publish concrete reusable progress rather than only recommendations. Request independent audit for new proofs and never self-certify.

- When a quantitative route begins to depend on a new local lemma with many downstream consumers, prioritize independent validation of that load-bearing premise. Exploratory descendants may continue, but keep their constants and proof status visibly provisional until the premise is checked; do not spend scarce audit effort uniformly across low-leverage leaves.

Retrospectives may add, remove, merge, or refine these nudges. Keep this document compact enough to influence actual research. Problem-specific examples and historical comparisons belong in retrospective records.