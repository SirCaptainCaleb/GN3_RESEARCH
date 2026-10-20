# Root-free square without one-edge repairs in every even dimension

- Stable ID: note_nori_rootfree_no_single_edge_repair_lift_r11981
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: 
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11981_1
- Updated session: session_nori_r11981_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

Q8 CONSTRUCTION. Four direction pairs (0,1),(2,3),(4,5),(6,7). For pair i pack the six exterior bits of x into z_i in increasing dimension order. Let f_i(x)=bit_(min(z_i,63-z_i))(M_i) xor [z_i>=32], with masks (M0,M1,M2,M3)=(0xA1714415,0x0C3C7FFF,0xCC3F8FBF,0xFD332300). The red direction in pair i is 2i+f_i(x). Gates ignore their own pair and satisfy antipodal oddness. Let S be the two antipodal pair-0 squares with exterior indices 0,63.

INDEPENDENT ENUMERATION. Old rooted red full geodesics 10362; switched-side rooted red full geodesics 10332; old red geodesics avoiding S 10332; old red geodesics meeting S once internally 30. No S vertex begins a red full geodesic. There are zero full direction-simple antipodal paths whose only old-blue edge is a single edge of S, with all remaining edges old red. Further, zero full paths have one old-blue and one old-red S edge with every other edge red. The root-4 original-direction order (0,3,4,7,2,6,5,1) is an old red avoiding witness. Independent Python subset DP and C++ enumeration of all 256*8! rooted direction orders reproduce the counts.

DIMENSION-UNIFORM THEOREM. For all m>=4, a legal paired-flat Q_(2m) coloring and a square orbit S_m exist with (i) red full geodesics both avoiding and meeting S_m, (ii) no S_m-rooted red full geodesic, (iii) no path with precisely one formerly blue S_m edge and all other edges red. Keep the Q8 gates independent of added pairs, give every added pair gate x_0, and let S_m have outside bits old z0=0 and added zeros, paired with the antipodal outside assignment. Deleting added-pair steps from any path in class (ii) or (iii) produces a full path in the base Q8. Rooted success contradicts base S-root failure. A one-blue repair projects to a base one-blue path with at most one more old-red S edge, because pair 0 contributes only two original directions; both path types were ruled out in the base certificate. For successful red lifts, insert one red step from every added pair before the old direction-0 step and its complementary red step after: each added gate x0 reverses across this step, so both original directions occur once. Initial added bits can be selected so a lifted S-hitting path hits S_m. An avoiding old red path lifts to an avoiding one. This completes the proof.

A separate Q10 DP counts 589468 S5-avoiding red geodesics and zero S5 one-blue repairs. Code: nori_oneblue_countercheck.py, nori_oneblue_independent_enumerator.cpp, nori_oneblue_lift_test.cpp. Full report: nori_single_edge_repair_obstruction.md. This refutes universal root-exclusion-to-one-edge-repair forcing. It does not refute NORI1: all the examples retain avoiding red full geodesics. A critical boundary additionally requires all old red full geodesics to meet S, so that global condition remains essential.
