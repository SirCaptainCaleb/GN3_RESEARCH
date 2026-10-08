# Audit synthesis: g=1 boundary repair is complete locally; iteration still needs a common potential — preserved pre-item development

## Composition

(none yet)

## Development

This is a synthesis/audit note.

The old g=1 missing-boundary-window issue is solved and should not be reopened:
- the audited g=1 A2 splice either closes at the checked suffix boundary or yields a genuine protected deletion witness with the complete outside order fixed;
- that witness transports the threshold four windows and has profile (p+4,q-4);
- the one-step phase-transfer trichotomy is valid;
- the equality profile q=p+4 is impossible by the dedicated equality-case argument.

However, this does not by itself prove global termination under repeated g=1 transports. A subsequent protected witness need not still be globally minimum-first-phase, so the scalar phase-imbalance decrease cannot simply be iterated without proving that all later states stay in one admissible class on which the same branch lemmas apply.

Current correct use:
1. Treat the local g=1 boundary reconnection and equality case as finished.
2. Do not use the former missing suffix bit as a research target.
3. If repeated g=1 transport is needed, first establish a closed state class and one common well-founded potential, or a direct escape lemma.
4. The active ternary frontier is the antipodal residual state and its two boundary-preserving exits, especially the need for an iterable boundary-state transport theorem that tracks both ordered boundary pairs and the complete mismatch block.

This note supersedes any stronger informal claim that the entire g=1 iterative branch is already globally closed.
