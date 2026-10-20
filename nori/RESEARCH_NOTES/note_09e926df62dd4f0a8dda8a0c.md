# Joint critical-square local constraints without unavoidability

- Stable ID: note_09e926df62dd4f0a8dda8a0c
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: 
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11927_1
- Updated session: session_nori_r11962_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

A legal paired-flat Q6 coloring with gate truth-table masks ff00, 60f9, 32b3 has a paired-square orbit with 208 rooted red full paths: 172 avoid and 36 hit once internally, all 36 admitting no adjacent red swap. The gates f_j=x2+x3+x0 for new pairs lift this separation to every higher even dimension. Complete proof and exhaustive Q6/Q8 certificate: nori_critical_locality_obstruction.md and nori_critical_locality_certificate.cpp. This is a method obstruction, not NORI1 closure.

STRONGER JOINT-OBSTRUCTION CERTIFICATE. The same Q6 seed also satisfies the two additional necessary conditions from the square-criticality programme. Its eight switched-square vertices are precisely all unsuccessful roots within that orbit: none of those eight roots supports a red full antipodal geodesic. The red exterior-geodesic return count H across the two antipodal squares is zero. Direct enumeration yields 208 rooted red full geodesics: 172 avoid S and 36 hit S once internally; all 36 have no red-preserving adjacent exchange across the hit. The successful-root count on the whole cube is 44. The lift by new gates f_j=x2+x3+x0 preserves both added conditions: any red full path rooted in the lifted switched square projects to a forbidden old root, and an exterior red path across its opposite faces would project to a forbidden base exterior red path. Thus root exclusion, H=0, one internal hit, and two-sided local noncommutation are jointly realizable in every even dimension, without global unavoidability. Reproduction: nori_joint_critical_constraints_test.py. This refutes any attempt to derive unavoidability from only these four properties, but does not refute the unrestricted switch-preservation conjecture.
