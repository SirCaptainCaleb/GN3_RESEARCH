# Disjoint full-geodesic packing and square-switch resilience

- Stable ID: note_nori_disjoint_packing_square_stability_r11876
- Author: session_nori_r11876_4
- Primary home: subsection:obstruction_compatibility_and_a_programme_for_nori1_closure
- Labels: NORI1, paired-flat, square-switch, vertex-disjoint, dimension-uniform
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11876_4
- Updated session: session_nori_r11876_4
- Disposition: none
- Successor: none

## Related references

- None

## Research note

A paired-square orbit contains eight vertices and four originally red edges. Hence at most four vertex-disjoint or edge-disjoint red full antipodal geodesics can meet it; after t switches at least h-4t paths survive from a packing of size h. At a good-to-bad critical square the good coloring has red-geodesic packing number at most four. NONLINEAR PATH-DOUBLING THEOREM: Given h disjoint red full antipodal geodesics in a legal paired-flat core H, adjoin a new pair b with any antipodally odd gate G reading only old pair bits; old gates ignore b. On each old red full path, G has opposite values at its antipodal endpoints, hence changes across some old edge u-v. Insert one red b-step before this edge and one after. Since G(u)!=G(v), the steps use the two distinct original b directions, old red steps survive, and the endpoint is antipodal. Both initial q_b bits yield two vertex-disjoint red full paths: their q_b bits differ at matching stages, while repeated old projected vertices occur at opposite new parity bits. Lifts of different old paths are disjoint by old projection. Therefore h disjoint red geodesics give 2h in either prescribed new parity. Repeating k times gives 2^k vertex-disjoint red full geodesics in EACH parity fiber whenever the old core was successful fiberwise and the new gates read only earlier pair bits, with arbitrary legal nonlinear dependence. Any t later legal square switches in any pairs preserve at least 2^k-4t original red geodesics per parity fiber, so 4t<2^k forces success. Full proof and verifier: nori_disjoint_geodesic_packing_report.md and bundle in the conversation. Scope: unrestricted NORI1 and vertex-simple boundary tournaments remain open.
