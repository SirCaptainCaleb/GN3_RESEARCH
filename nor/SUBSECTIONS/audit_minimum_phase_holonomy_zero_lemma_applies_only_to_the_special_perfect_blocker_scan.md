# Audit: minimum-phase holonomy-zero lemma applies only to the special perfect-blocker scan

## Metadata

- ID: audit_minimum_phase_holonomy_zero_lemma_applies_only_to_the_special_perfect_blocker_scan
- Parent Section: ternary_protected_bridges_and_scan_obstructions
- Position: 44
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

The holonomy-zero and holonomy-flip arguments require the old special scan 1^(p+1)0^q. All-insertion blocking does not force that scan: arbitrary flat blocked scans exist. Therefore these lemmas close a real special branch only and must not be used as unconditional flat-sector statements. The arbitrary-scan theory continues through threshold-band repair and protected-root extraction.

## Development


Scope audit of subsection 42.

Subsection 42 assumes an omitted "perfect blocker" with scan

1^(p+1) 0^q.

In the project vocabulary this is the old special perfect-blocker scan, not an arbitrary coordinate whose insertion fails in every gap.

The earlier audit "Insertion blocking does not force the special blocker scan" gives flat realizable fully blocked scans different from 1^(p+1)0^q. Therefore the hypothesis of subsection 42 is not automatic for a general deletion witness in the corrected arbitrary-scan flat theory.

The proof of subsection 42 itself is valid under its stated special-scan hypothesis: minimum first-phase extremality forces the residual double-full holonomy bit t to equal 0.

Correct use:

- special perfect-scan branch: t=0 may be assumed in the canonical double-full packet;
- arbitrary insertion-blocking branch: t remains unconstrained unless additional provenance first proves the special scan or reproduces the same swap identities by another argument.

Thus subsection 42 closes a real subcase but does not by itself restore the earlier claimed unconditional flat-sector closure.
