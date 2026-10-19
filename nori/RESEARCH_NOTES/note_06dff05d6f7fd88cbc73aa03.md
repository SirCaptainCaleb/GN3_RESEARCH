# Even-lift Fano full peeling and one rank-five nine-label orbit

- Stable ID: note_06dff05d6f7fd88cbc73aa03
- Author: unspecified; session provenance retained
- Primary home: subsection:obstruction_compatibility_and_a_programme_for_nori1_closure
- Labels: NORI1, rank-five, Fano-plane, finite-certificate
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

An independent C++17 exhaustive enumeration proves that every seven-point Fano quotient block with zero full-column sum and row factors u_i=(1,z_i), column factors v_i=(epsilon_i,t_i), epsilon_i=z_i dot t_i, admits a legal full peeling of all seven labels. Normalize a common three-bit gauge by z_0=0. The verifier examines all 131072 permitted even-sum row-factor assignments and finds no failure. File nori_fano7_even_full_exhaust.cpp. Consequently the rank-five nine-label quotient orbit with multiset (1,1,2,4,6,8,10,12,14), orbit size 120 under GL(4,2), is never a size-minimal peeling counterexample. Its seven nonduplicated quotient points form a Fano 3-space and have zero full-column sum because the two duplicated lifts add to s=(1,0,0,0,0). Delete those seven labels; the remaining two duplicated labels read each other in both directions, so their 2x2 principal matrix is invertible. This is computer-assisted finite proof, independent of SAT. The other three rank-five nine-label quotient orbits remain unresolved by this argument; unrestricted NORI1 remains open.
