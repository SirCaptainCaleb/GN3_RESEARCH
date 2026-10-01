# Project-specific policy

## Statement



## Body

TEMPORARY BANS: All computation, all literature search, and all infinite case-analysis ladders. A case split is permitted only when the complete parameter/configuration space is proved a priori to be finite and uniformly bounded across the entire theorem class, independently of which counterexample or instance is chosen. It is not enough that the currently selected instance is finite, that a smallest unproved/minimal counterexample has finite order, or that one side of a decomposition is bounded. Workers must not justify case analysis by fixing the current smallest, minimal, or otherwise selected counterexample and enumerating its finitely many possibilities. Any family whose case parameters can take infinitely many values over the theorem class is disallowed; for example, 5|(n-5) is an infinite ladder because the second parameter ranges without bound. The criterion is a theorem-level finite case space, not instance-level finiteness and not whether n appears in the notation.

## Mandatory research-startup reading

Every worker entering research mode must read research_nudges in full before substantial proof search. The nudges are mandatory reading and must be seriously considered as default methodological priors, though a researcher may depart from an individual nudge when mathematical judgment gives a concrete reason. If research_nudges changes during a run, reread it before the next substantial route commitment.

## Mandatory strengthening pass after a result

Whenever a researcher obtains a result that is worth persisting, using downstream, or treating as progress, do not immediately move on. First make a serious attempt to strengthen or generalize it by asking:

“What assumptions were not needed to get this result?”

Inspect the proof rather than merely the statement. Determine which hypotheses were actually used, which can be weakened or removed, whether the witness or ambient setting can be generalized, and whether the same mechanism yields a cleaner or more reusable statement. Persist the stronger formulation when the proof supports it.

This strengthening pass is mandatory; prolonged optimization is not. Do not spend substantial effort polishing additive constants or lower-order terms unless that refinement affects the target leading term, unlocks a structural argument, resolves a genuine finite obstruction, or is explicitly needed by a downstream theorem.