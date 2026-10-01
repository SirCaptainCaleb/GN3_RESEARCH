# Project-specific policy

## Statement



## Body

TEMPORARY BANS: No computation or literature search. Do not pursue infinite case-analysis ladders. A case split is permitted only when the complete parameter/configuration space is proved a priori to be finite and uniformly bounded across the entire theorem class, independently of which counterexample or instance is chosen. It is not enough that the currently selected instance is finite, that a smallest unproved/minimal counterexample has finite order, or that one side of a decomposition is bounded. Workers must not justify case analysis by fixing the current smallest, minimal, or otherwise selected counterexample and enumerating its finitely many possibilities. Any family whose case parameters can take infinitely many values over the theorem class is disallowed; for example, 5|(n-5) is an infinite ladder because the second parameter ranges without bound. The criterion is a theorem-level finite case space, not instance-level finiteness and not whether n appears in the notation.

For routine navigation, prefer search_compact(query,limit,under_id,include_superseded) when full bodies are unnecessary. For simple current-version publication, canonical_object_id(id), revise_current(worker,id,patch,...), add_dependency_current(worker,consumer,premise,...), and publish_with_dependencies(worker,object_spec,dependency_ids) resolve unique supersession chains and current versions automatically. Continue to use staged publication when a larger multi-object read/write set or custom sequencing must be locked atomically.

ELEVATION METHODOLOGY: Every elevation target receives a strengthening pass, regardless of whether it is a general lemma, route-specific theorem, local technical result, recomposition, or other mathematical object. For each target, identify the mechanism really enabling the result and seek the strongest correct formulation. Explicitly test abstractions and generalizations; alternative or negative-space formulations (for example matching-versus-cover or obstruction-versus-transversal viewpoints); additional unstated structure forced by the proof; stronger consequences; and which hypotheses, thresholds, extremality assumptions, ambient context, predecessor machinery, or route assumptions are actually unnecessary. Ask what the result says at its natural maximal strength, not merely whether its current wording can be broadened.

When a target naturally belongs to a predecessor chain, also try to apply it earlier without importing all predecessor steps. Identify the minimum additional conditions needed earlier and ask whether those conditions can themselves be proved or forced there.

When a target is a general or standalone lemma/theorem/result with no natural earlier location, do not invent an artificial earlier placement. Instead find every known consumer or use site. At each consumer, ask whether the result can be invoked earlier, replace predecessor work, simplify the route, or expose a stronger consequence. Independently perform the full strengthening pass on the standalone result itself.

When strengthening reveals genuine supersession, record the supersedes relation immediately while leaving retirement/effect audit-gated. Preserve alternate reasoning branches unless genuinely superseded.