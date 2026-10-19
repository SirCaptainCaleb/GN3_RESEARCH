# Secondary blue-cut stability and stronger anchored triple

- Stable ID: note_nori_xvi_secondary_face_cut_gap_20261018
- Author: Independent NORI1 mathematician
- Primary home: subsection:obstruction_compatibility_and_a_programme_for_nori1_closure
- Labels: 
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11531_1
- Updated session: session_nori_r11531_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

UNRESTRICTED SHARP THEOREM. For r>=5, an r-dimensional directed Boolean face with red endpoint stars and no red monotone antipodal geodesic must have at least T+r-4 blue edges, T=r(r-1), UNLESS its entire early or late interior rank layer is blue. The bound is achieved by the outgoing blue cut from ranks 0,1 plus one rank2 vertex. A symbolic counting proof covers r>=9: reduce to the red-reachability cut, whose two interior terminal red-layer counts a,b are at least2. Put s=min(a,b), d=(r-2)(r-3), M=blue strictly middle edges, q=total blue-T. Cross-layer counting yields q>=(r-4)M/(r-2) and s(d-s-q+M)<=2(r-3)M. For q<r-4 these are incompatible, by the algebraic difference (s-2)(d-s)>=0 evaluated at q=r-4, and positivity of d-s-q in r>=9. The small base ranks 5-8 are exhaustively certified by integer maxflow, protecting terminal stars plus one red early and one red late interior edge; the 20,30,42,56 cases yield min blue sizes 21,32,45,60. For r>=9, at equality without a complete blue interior terminal layer, one layer is wholly red and the other has two red edges, with r-2 blue middle edges. STRONGER ANCHORED TRIPLE: the anchored rank-r faces and red edges of the previous article require a maximum blue-face count at least T+r-4, rather than merely T+1. If all surpluses are <r-4, each face contains a complete early or late blue layer. Anchors make faces A,C choose early; whichever choice B makes, an overlapping pair has disjoint conflicting layer patterns needing at least r-1 additional blue edges, contradiction. Tests r5-11. Full proof /mnt/data/nori_xvi_sharp_secondary_face_cut_gap.md; verifiers /mnt/data/nori_xvi_second_cut_gap_verify.py and /mnt/data/nori_xvi_secondary_gap_anchored_triple_verify.py. NORI1 remains open; generating the anchored triple from arbitrary shortest antipodal red paths is unresolved.
