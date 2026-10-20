# Q6 universal orbit avoidance and a two-geodesic switch certificate

- Stable ID: note_nori_q6_universal_orbit_avoidance_two_witness_source_r11982
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: NORI1, paired-flat, nonlinear, square-switch, two-witness, Q6, finite-certificate
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11982_1
- Updated session: session_nori_r11982_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

UNRESTRICTED TWO-WITNESS SWITCH CERTIFICATE. In any legal paired-flat coloring of Q_(2m), fix direction pair i. For a red full antipodal geodesic P let O_i(P) be the set of antipodal exterior-assignment orbits occupied by the two i-direction edges of P. Thus |O_i(P)|<=2. If two red full geodesics P,Q satisfy O_i(P) intersect O_i(Q)=empty, then every legal paired-square switch in pair i preserves red success: for every orbit S_(i,z), at least one of P,Q avoids S_(i,z) altogether, and survives its switch. The paths need not be edge-disjoint outside pair i. This provides an all-dimensional two-witness forcing criterion, sharper as a sufficient certificate for a fixed pair than requiring five globally edge-disjoint geodesics. No theorem producing such a packet in every successful coloring is known.

Q6 UNIVERSAL AVOIDANCE, EXHAUSTIVE. Any antipodally odd paired-flat Q6 coloring is specified by three independent eight-bit gate masks, 2^24 colorings in total. For each coloring and each of the 24 antipodal square orbits (3 pairs, 8 exterior complement classes), a direction-subset red reachability recurrence after deleting all eight edges of the orbit finds a full red antipodal geodesic. The exhaustive C++ computation covered 16,777,216 coloring assignments and 402,653,184 coloring/orbit tests, with zero failures. The recurrence D(x,U)=OR_(d unused, red from x, not in orbit) D(x xor 2^d,U union d), with D(x,all)=true, is equivalent to existence of a full red antipodal geodesic avoiding the orbit, since all original directions are used once. Independently enumerated rooted original-direction orders for 100,000 sampled Q6 colorings confirm the same statement. Source: nori_universal_avoid_exhaustive_q6.cpp; output: nori_universal_avoid_exhaustive_q6.log; detailed proof record: nori_q6_square_avoidance_and_two_witnesses.md.

TRANSFER GAP. The result concerns all legal Q6 colorings, but no argument extends it to arbitrary nonlinear higher-dimensional paired-flat colorings. Restrictions of a higher-dimensional coloring to Q6 faces need not be antipodally odd in those face dimensions; the project's least-counterexample analysis excludes uncomplicated three-pair outgoing-closed reductions. Nor does global avoidance for each orbit formally imply existence of one pair of geodesics with disjoint O_i sets: a triangle of two-element supports avoids every single orbit but has no disjoint pair. Thus universal two-witness production remains an unproved, stronger source theorem.

LOCAL EXCHANGE OBSTRUCTIONS. Direct Q6 enumeration gives legal gates (0xb7,0x0f,0xf0) with a pair-0 orbit z=1 having no successful red root, only one distinct partner orbit among red full paths that encounter it, yet 152 avoiding red full paths. Therefore any proof must not rely on a universal lower bound of two partner orbits. A separate test found that fixing the relative order of all outside original directions also fails as an endpoint-anchor-or-avoidance source, so cross-order exchanges must be permitted.

CRITICAL-BOUNDARY REDUNDANCY. A red exterior geodesic joining corresponding corners of the switched antipodal squares extends with one red face-direction edge at each end to a red full geodesic rooted at the orbit. Therefore absence of orbit-rooted full red geodesics implies zero red exterior return. This is not an independent critical-boundary hypothesis.

CLASSIFICATION. The two-path sufficiency theorem is all-dimensional, the Q6 avoidance assertion is computer-assisted finite, and the all-dimensional source theorem and unrestricted NORI1 remain open. No higher-dimensional closure claim is made.
