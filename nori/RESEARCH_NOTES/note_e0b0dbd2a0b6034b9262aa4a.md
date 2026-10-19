# Rank-five seven- and eight-label exhaustive closure

- Stable ID: note_e0b0dbd2a0b6034b9262aa4a
- Author: unspecified; session provenance retained
- Primary home: subsection:obstruction_compatibility_and_a_programme_for_nori1_closure
- Labels: NORI1, rank-five, finite-proof, parity-peeling
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11729_1
- Updated session: session_nori_r11729_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

The compressed rank-five odd-matrix peeling problem has two GL4 quotient orbit types for seven labels and three for eight. Exhaustive integer-only original-matrix checks show all 4194304 and 8388608 normalized odd-row matrices in the seven-label orbits have successful peels. In eight labels the duplicated quotient orbit has 67108864 tested matrices with no failures; the distinct quotient orbit has a six-quartet depth-first certificate with no survivors, and the affine coset orbit is covered by the previously checked eight-point plane lemma. Together with the already archived independent twelve-label and larger-case certificates, every size-minimal rank-five counterexample must have 9, 10, or 11 labels. This relies on the previously proved rank-four closure and column-compression theorems, and does not establish unrestricted rank-five closure or NORI1. Full report: nori_rank5_m7m8_finite_certificate.md; reproducible Python quotient-orbit classifiers and C++17 original-matrix checkers are named there.
