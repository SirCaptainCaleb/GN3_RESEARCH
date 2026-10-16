# Gauge-averaged avoidance of one antipodal vertex pair

- Stable ID: note_vertex_avoidance_gauge_flux_20261015
- Author: unspecified; session provenance retained
- Primary home: subsection:curvature_realization_gauge_phases_and_rooted_square_defect_transport
- Labels: gauge, antipodal, geodesic
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r10003_1
- Updated session: session_nori_r10003_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

THEOREM. For any legal odd edge coloring of Q_n (n>=2), any antipodal vertex pair V={v,bar v}, and uniformly random antipodally invariant vertex gauge h, the expected number of rooted zero full geodesics avoiding V equals n! (1 - n/2^(n-1)). Proof: every full geodesic visits n distinct antipodal vertex pairs. Vertex-transitivity thus gives 2n! (2^(n-1)-n) rooted oriented full geodesics avoiding V. Root sliding cyclically moves the path window, preserves its visited projective vertex set, and flips one color bit through antipodal oddness, so half of the avoiding paths have even total edge-color parity. Each even-parity path is made all zero by a fraction 2^(-(n-1)) of all antipodally invariant vertex gauges, and odd-parity paths never are. Summing gives the formula. The complementary hitting average is n! n/2^(n-1). COUNTEREXAMPLE to the stronger pointwise avoidance assertion: On Q3 define c0(x)=1+x1, c1(x)=x0, c2(x)=x1 (all modulo 2). The four zero rooted full geodesics have (root,direction order) equal to (011,012), (111,012), (000,210), (100,210); all visit V={000,111}. Their antipodal translates give the one-colored geodesics and likewise meet V. Thus a good legal coloring need not have a monochromatic geodesic avoiding a designated antipodal vertex pair. The star-flip-preservation equivalence of NORI1 is unaffected. The gauge-average avoidance theorem does not imply pointwise avoidance.
