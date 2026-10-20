# Q4 forces endpoint-square repairs; avoidance-only closure is false

- Stable ID: note_nori_q4_unavoidable_orbit_endpoint_repair_20261020_r11979
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: NORI1, paired-flat, square-switch, method-obstruction, Q4, endpoint-repair
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11979_1
- Updated session: session_nori_r11979_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

Q4 is a sharp obstruction to an avoidance-only proof of paired-square preservation.

THEOREM (all legal paired-flat Q4 colorings). Pair original directions (0,1) and (2,3). Assume undirected paired-flat red selectors f0(x2,x3), f1(x0,x1), each antipodally odd. Every such coloring has precisely eight ROOTED red full antipodal geodesics (four unoriented). Every red full antipodal geodesic traverses one red edge in EACH of the four antipodally paired alternating-square orbits (two orbits per direction pair). Consequently no red full antipodal geodesic avoids any prescribed orbit, yet switching any one orbit preserves the positive count of eight rooted red geodesics.

PROOF. An antipodally odd Boolean function of two outside bits is necessarily one outside bit or its complement. Each of the two pair labels must occur twice in any full red geodesic. They cannot occur consecutively: an immediate repetition traverses the same red matching edge backward, duplicating the original direction. Hence the pair word must be 0101 or 1010. For either word, demanding the two directions in each pair be different forces the middle step in pair1 to use the reader direction of f0 and the middle step in pair0 to use the reader direction of f1. The original direction order is consequently uniquely determined by the pair word and the two gate readers. The colors of the first two steps determine one bit from each pair independently, leaving two arbitrary root bits. Each of the two alternating pair words therefore has four admissible roots. Each pair is visited twice with precisely one exterior original-direction step between visits. The exterior two-bit parity changes, so the two hits lie in distinct complementary outside-bit orbits. The claim follows for both pair labels.

Independent enumeration verifies all 16 legal Q4 gate assignments, 64 gate/orbit instances, and all 16*24 starting-root/direction-order combinations: every gate assignment has eight rooted red full geodesics, each meeting each prescribed orbit once, and a legal orbit switch retains the same count. Program nori_q4_square_unavoidability_verify.py.

TRANSFER AND LIMITS. This refutes the universal statement that every red-successful paired-flat coloring admits a red full geodesic avoiding every prescribed alternating-square orbit. It does NOT refute switch preservation, and it does NOT refute the strictly weaker proposed endpoint-or-avoiding source theorem: when avoidance fails in Q4, some red full geodesic meets the orbit in its first or final edge. At a hypothetical critical good-to-bad boundary the established two-hit transport forces all old red witnesses to hit once strictly internally; an endpoint-or-avoiding theorem in arbitrary even dimension would contradict that criticality and prove unrestricted NORI1. That source theorem remains unproved, and the Q4 mechanism cannot simply be frozen within an arbitrary larger cube because the induced two-pair face gates need not be odd under complementation of those four face bits. The team already has a Q6 avoidance result, but no dimension-uniform transfer.
ADDITIONAL ROOT-ANCHOR CENSUS. Every Q4 orbit S consists of eight vertices; in each of the 16 legal gate choices, precisely four of those eight vertices support a red full antipodal geodesic. The eight red-successful roots of the cube are distinct. The exhaustive verifier also checks this stronger 16-by-4 statement. Thus in the Q4 model unavoidable square crossings are accompanied by S-rooted red full geodesics; the known strict-internal-hit critical-boundary condition is absent. A proposed unrestricted endpoint-anchor-or-avoidance source theorem is consistent with this model, but remains unproved in higher dimensions.
