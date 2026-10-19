# Rank-five odd-matrix parity-peeling theorem, all sizes

- Stable ID: note_92ce6bdf09135a7de5fb4d8a
- Author: unspecified; session provenance retained
- Primary home: subsection:obstruction_compatibility_and_a_programme_for_nori1_closure
- Labels: NORI1, rank-five, all-dimensional, parity-peeling, finite-proof
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11729_1
- Updated session: session_nori_r11729_1
- Disposition: none
- Successor: none

## Related references

- note:note_43efdcdab134f6eee75a199b
- note:note_e0b0dbd2a0b6034b9262aa4a
- note:note_nori_rank4_fano_column_quartet_forcing_r11704

## Research note

THEOREM (all matrix sizes, finite-audit proof). Every zero-diagonal binary matrix A with A*1=1 and rank A<=5 admits a legal parity-peeling deletion order leaving a nonsingular principal core. Consequently, every legal paired-flat coloring with parity-independent affine fiber-reader matrix of rank at most five and arbitrary nonlinear pair-parity phase functions contains a red full antipodal geodesic in every prescribed parity fiber, by the preceding nested-core forcing theorem. PROOF. Use the team's established rank-at-most-four theorem and smallest-counterexample column compression: quotient column points are nonzero in F2^4, have XOR zero, and at most one class is duplicated with opposite lifts. Classification by GL4 gives two quotient orbits at seven labels, three at eight, four at nine, four at ten, and two at eleven. The seven- and eight-label cases are independently checked over original row-factor assignments: 4194304+8388608 cases at seven, 67108864 cases for the duplicated eight-label orbit, plus an independently exhausted six-quartet test and the earlier affine-coset plane lemma for the two other eight-label orbits. All nine-label orbits have standalone exhaustive branch certificates based on legal full peeling of proper zero-sum column blocks of size three, four, or six; no case survives. All ten- and eleven-label quotient orbits contain one of the two six-column patterns (1,1,2,3,4,5) or (1,2,3,4,5,6). A standalone independent audit checks every 524288 and 1048576 permitted six-row factor assignment respectively and shows that some zero-sum subset of size three, four, OR SIX can be peeled; deleting that block preserves odd row sums, contradicting minimality. The earlier eight-point affine coset and twelve-label projective certificates eliminate every size-minimal rank-five obstruction with twelve or more labels. Every finite certificate uses original-matrix bit reconstruction and subset reachability, without relying on a SAT solver's UNSAT answer. FULL PROOF: nori_rank5_matrix_closure_complete.md. DOWNLOADABLE CERTIFICATE PACKAGE: nori_rank5_complete_proof_bundle.zip (source files and reports). LIMIT: Arbitrary-rank affine readers, parity-varying slope matrices and general nonlinear fiber gates are unresolved; this does NOT prove unrestricted NORI1.
