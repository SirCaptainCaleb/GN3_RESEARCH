# Joint critical-square local constraints without unavoidability

- Stable ID: note_09e926df62dd4f0a8dda8a0c
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: 
- Lifecycle: active
- Epistemic status: proved
- Current version: 3
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11927_1
- Updated session: session_nori_r11993_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

A legal paired-flat Q6 coloring with gate truth-table masks ff00, 60f9, 32b3 has a paired-square orbit with 208 rooted red full paths: 172 avoid and 36 hit once internally, all 36 admitting no adjacent red swap. The gates f_j=x2+x3+x0 for new pairs lift this separation to every higher even dimension. Complete proof and exhaustive Q6/Q8 certificate: nori_critical_locality_obstruction.md and nori_critical_locality_certificate.cpp. This is a method obstruction, not NORI1 closure.

STRONGER JOINT-OBSTRUCTION CERTIFICATE. The same Q6 seed also satisfies the two additional necessary conditions from the square-criticality programme. Its eight switched-square vertices are precisely all unsuccessful roots within that orbit: none of those eight roots supports a red full antipodal geodesic. The red exterior-geodesic return count H across the two antipodal squares is zero. Direct enumeration yields 208 rooted red full geodesics: 172 avoid S and 36 hit S once internally; all 36 have no red-preserving adjacent exchange across the hit. The successful-root count on the whole cube is 44. The lift by new gates f_j=x2+x3+x0 preserves both added conditions: any red full path rooted in the lifted switched square projects to a forbidden old root, and an exterior red path across its opposite faces would project to a forbidden base exterior red path. Thus root exclusion, H=0, one internal hit, and two-sided local noncommutation are jointly realizable in every even dimension, without global unavoidability. Reproduction: nori_joint_critical_constraints_test.py. This refutes any attempt to derive unavoidability from only these four properties, but does not refute the unrestricted switch-preservation conjecture.

JOINT MIXED-FACE COMPATIBILITY (20 October 2026, session session_nori_r11993_1). The Q6 example above realizes all four mixed antipodal face blockers of note_nori_strict_square_mixed_face_blockers_r11992_6 on the same S, in addition to root exclusion, H=0, 36 strictly internal one-hit red witnesses and their two-sided noncommutation. Use the exterior four-bit selector masks (0xff00,0x60f9,0x32b3) and square pair i=1 at exterior assignments 3,12. Its square vertices are {3,7,11,15,48,52,56,60}. For each other pair j=0,2, the two frozen mixed pair words t are 1,2 (interpret t=x_(2j)+2*x_(2j+1)). Each of the four frozen Q4 faces F(0,1),F(0,2),F(2,1),F(2,2) has zero rooted red full geodesics, and also zero blue full geodesics by global oddness and the complementary t=1,2 pairing. Direct selector-table certificates: in F(0,1),F(0,2) the remaining selector f_2 is constant 1,0 respectively; in F(2,1),F(2,2), BOTH remaining selectors f_0,f_1 are constant, respectively (0,1) and (1,0). A constant selector in a two-pair frozen Q4 prevents red full direction-simple paths, since both original directions in that pair would have to be red at their occurrences, while the same one is always selected. The same original-direction enumeration gives 208 rooted red full geodesics in G: 172 avoid S and 36 meet S once internally. Hence the blocked-face conditions, root exclusion, exterior-return vanishing, local curvature, and one-hit red-witness existence are jointly realized in a single shared legal coloring, with global unavoidability missing. No contradiction follows from those other hypotheses alone. A critical-square closure argument must directly exploit the statement that EVERY red full witness hits the same S, beyond the resulting frozen-face blockers.
