# Q6 paired-flat square-orbit avoidance and Q4 forced incidence

- Stable ID: note_nori_q6_square_orbit_avoidance_20261018_r11755
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: NORI1, paired-flat, square-switch, square-avoidance, Q4, Q6, finite-enumeration, transfer-gap
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11755_2
- Updated session: session_nori_r11755_2
- Disposition: none
- Successor: none

## Related references

- None

## Research note

# Paired-flat square-orbit avoidance in dimension six

Let the directions of Q_(2m) be paired as P_i={2i,2i+1}. For each i, the gate f_i depends only on the directions outside P_i, with f_i(bar z)=1+f_i(z). The two P_i-direction colors are f_i and 1+f_i. A square-pair orbit consists of a square supported on P_i and its antipodal square.

**Proposition 1 (four-dimensional obstruction; proved).** Every paired-flat Q4 coloring has eight rooted red full geodesics, and each meets all four square-pair orbits, once apiece.

*Proof.* Write A,B for the two direction pairs. Two consecutive steps from one pair have opposite colors, so every red full path has pair-word ABAB or BABA. An odd Boolean rule on the two exterior bits reads precisely one of them, plus a constant. For ABAB, the first B-step must use the bit read by the A-rule; the second A-step must use the bit read by the B-rule. The order of the four directions is therefore determined. Requiring the initial A- and B-steps to be red fixes two independent root bits; two remain free. This gives four red paths for ABAB, and likewise four for BABA. Within each pair, the exterior states at its two steps differ in one bit and hence represent different antipodal square-pair orbits. Every red path therefore visits both orbits of each pair. QED.

**Proposition 2 (six-dimensional avoidance; exhaustive computational proof).** Every paired-flat legal coloring of Q6 has a red full antipodal geodesic avoiding any prescribed square-pair orbit.

*Verification.* There are 3*2^(6-3)=24 independent square-pair parameters. Relabeling the three pairs and translating the exterior bits acts transitively on parameter orbits, so fix orbit S=0. Enumerate all 2^6*6!=46,080 rooted full direction orders. For a step in direction d belonging to P_i, write z for the exterior assignment and z0=min(z,bar z). The red requirement on the indexed parameter x_(i,z0) is
x_(i,z0) = [z != z0] + [d=2i+1] (mod 2).
Discard paths meeting S, and discard paths placing contradictory requirements on a repeated parameter. There are 9,216 paths meeting S, 25,216 paths avoiding S with inconsistent requirements, and 11,648 consistent avoiding paths. Deduplication leaves 5,824 partial parameter assignments. The union of their satisfying Boolean subcubes contains all 2^24=16,777,216 assignments. The independent path enumerator checks the antipodal endpoint condition, and a separately implemented binary MILP containing the negation of all 5,824 certificates was reported infeasible by HiGHS. Source checker: nori_q6_square_avoidance.cpp (independent executable; no externally validated proof log). Thus the finite claim follows from the exhaustive bitset enumeration and its stated encoding.

**Transfer scope.** In Q4, retaining an unaffected path is impossible for every switched orbit; a witness must be replaced after the flip. In Q6, avoidance holds. In higher dimension, a six-direction face obtained by freezing other directions need not satisfy oddness under the six-direction antipode, so the Q6 theorem alone yields no full-class induction. A lifting theorem must transport a six-direction avoiding witness across complementary exterior fibers while also inserting the remaining directions in a monochromatic order. The non-odd frozen-face phenomenon is the explicit missing implication.

## Two-square-orbit strengthening (verified 19 October 2026)

**Theorem (computer-assisted).** Every legal paired-flat coloring of \(Q_6\) has a red full antipodal geodesic avoiding any prescribed two distinct antipodal square-pair orbits.

*Certificate.* The twenty-four square-pair orbits consist of eight for each of three direction pairs. Pair permutations and vertex translations preserve the coloring class and act transitively on these twenty-four orbits. Normalize the first forbidden orbit to orbit \(0\). Independently check every second orbit \(t\in\{1,\ldots,23\}\). For each of the \(2^6 6!=46,080\) rooted full orders, reject any path meeting either forbidden orbit or placing contradictory red requirements on a shared gate parameter. Every surviving path determines a partial assignment to the twenty-four independent antipodally paired gate parameters. Mark all \(2^{24}\) assignments extending at least one surviving partial assignment. In each of the twenty-three cases the bitset contains all \(16,777,216\) assignments; results are recorded in q6_pair_audit.txt. The standalone C++ verifier nori_q6_pair_avoidance.cpp independently constructs all orbit labels, all red path certificates and the coverage bitset, selecting \(t\) by command-line argument.

Consequently a set of fewer than three square-pair orbits cannot meet every red full geodesic of a paired-flat \(Q_6\) coloring. This is a finite result; the oddness of a six-direction frozen face generally fails in larger paired-flat cubes, so the theorem does not justify unrestricted higher-dimensional avoidance.
