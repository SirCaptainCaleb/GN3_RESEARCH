PROOF REHEARSAL MODE

A proof rehearsal is a fresh global proof-design AND proof-building exercise over the current trusted mathematical state. Its purpose is not to ask whether one named route closes the theorem. Its purpose is to survey the whole current landscape, choose the strongest route or combination of routes, and actively try to construct the best end-to-end proof now available.

SCHEDULER NEUTRALITY
A scheduler-forced proof rehearsal is route-neutral. The scheduler requests a rehearsal of the grand theorem; it must not choose, endorse, or implicitly assign a proof route. Any recently changed theorem IDs, stale recompositions, or newly certified results carried with the pressure are orientation metadata only. They are evidence that the global landscape changed, not targets that the worker must center. Never reinterpret a scheduler target or recent-result list as the question "does this route now close the theorem?"

GLOBAL ROUTE SELECTION
Begin from the entire current trusted landscape, not from the previous rehearsal, current composition, scheduler target, most recent theorem, or historically dominant bottleneck. Inspect the live major routes, current compositions, reusable toolkits, newly certified mathematics, fences/counterexamples, and known interfaces. Ask: given everything now known, what route or combination of routes is most likely to yield a complete proof? Select the attempted organization from that assessment. You may change routes during the rehearsal whenever the global picture suggests a better one.

DRAFT THE COMPOSITION FROM START TO FINISH
Write the attempted proof composition explicitly from the theorem hypotheses toward the conclusion. Identify the mathematical role of each substantial step and which trusted result supplies it. Recombine branches when useful, bypass obsolete intermediate steps, and distinguish reusable toolkit results from steps that genuinely belong in the proof chain. Look deliberately for shortcuts, stronger intermediate statements, and opportunities to replace several local lemmas by one theorem-level mechanism.

ACTIVE GAP ATTACK IS REQUIRED
Reaching an unsupported inference is not, by itself, completion of a rehearsal. When the attempted composition first hits a gap, actively try to bridge it before stopping:
- search the current trusted repository for results from other routes that can close or weaken the gap;
- try a different organization of the same ingredients;
- attempt a strengthening, shortcut, or local lemma suggested by the composition;
- if the chosen route is locally stuck, compare against other major live routes and switch when one now has better theorem leverage;
- publish any genuinely new proved strengthening or reusable result produced by the rehearsal, then revise the attempted composition around it.

Only after a serious attempt to remove or bypass the gap may the rehearsal record that inference as the current bottleneck. A response equivalent to "this route still does not close" is incomplete.

PROOF COMPRESSION AND STRUCTURE
Actively look for proof compression. Notice when results from different branches have become one causal chain, when a purported proof step is actually standalone toolkit, or when a stronger result bypasses an older chain. Do not compress genuinely independent reusable mathematics merely to make the proof look linear.

COMPLETION RECORD
A non-closing rehearsal must record:
- attempted_organization: a start-to-finish draft of the strongest composition attempted, not merely the local route inspected;
- route_selection: why this route or combination was chosen after surveying the current landscape;
- bridge_attempts: the concrete attempts made to remove, strengthen, or bypass the first apparent gap;
- first_unsupported_inference and/or gap_id: the exact residual inference that remains after those attempts;
- shortcuts_or_strengthenings: any proof compression, stronger intermediate statement, or newly identified reusable theorem;
- changed_bottleneck: whether the theorem-level bottleneck or reasoning-tree organization changed;
- highest_leverage_next_result: the missing result that now appears to have the greatest theorem leverage.

For a closure candidate, publish or identify the complete reusable composition and provide composition_id.

A rehearsal should inform subsequent research allocation. Distinguish the actual closure bottleneck from merely unfinished local lines, and identify which missing result would have the highest theorem leverage. It may recommend promoting, demoting, composing, reparenting, or marking standalone existing results when the global proof design clarifies their true role.

A rehearsal is a historical attempt, not itself an active theorem result. Completed rehearsals are stored chronologically under Archive -> Proof Rehearsals. Archive content is excluded from ordinary discovery search and remains available by deliberate navigation and exact reads. A reusable proof composition may separately be published or revised in the live reasoning tree when genuinely useful.

SCHEDULER-FORCED PROOF REHEARSAL
The scheduler may request a new rehearsal after substantial theorem-scale change or sufficient elapsed repository progress. The assignment is always to rehearse the grand theorem globally. Completion requires a genuinely fresh global end-to-end proof attempt plus active bridge work as above. Recent-result or stale-composition metadata may explain why the rehearsal became due, but must never determine the chosen route.
