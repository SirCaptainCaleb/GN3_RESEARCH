# Short legal cocircuit with two-point intersection need not be resource-simple

- Stable ID: note_nori_xi_two_intersection_not_directed_resource_faithful
- Author: unspecified; session provenance retained
- Primary home: section:nori_matroid_generalizations_conjectures
- Labels: obstruction, boundary-tournament, matroid
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6430_3
- Updated session: session_nori_r6430_3
- Disposition: none
- Successor: none

## Related references

- None

## Research note

In the n=6 boundary coloring encoded by 60-bit mask 0x6c08f53c2725f48 using the increasing-middle-vertex, lexicographically increasing outer-pair convention of the existing Article XI six-vertex certificate, every distinguished full-resource six-word closing cocircuit has at least four intersections with its port cycle. Nevertheless the legal ordered-triple overlap graph contains this six-edge path from a triple to its reversal: (0,1,2) -> (1,2,4) -> (2,4,3) -> (4,3,1) -> (3,1,0) -> (1,0,4) -> (2,1,0). Its seven state colors are [1,1,1,1,0,0,0], so it has one change. The six projected triple reversal-orbits are distinct, giving a shortest port cocircuit of size seven and intersection two. The chain repeats original resources and makes its last transition backward, so it is not a coherent resource-simple forward tight path. Exhaustive enumeration over the 120 triple states at n=6 yields 28,800 rooted six-step reversal paths with simple projected cycles for each mask; for this mask, 816 have one color change, 12,768 have three and 15,216 have five. This proves that all minimum port cocircuits of the legal-turn matroid are strictly too broad a witness family for the boundary objective.
