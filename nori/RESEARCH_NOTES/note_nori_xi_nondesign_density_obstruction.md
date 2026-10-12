# Equal changed-turn density need not fix stationary-child costs without a two-design

- Stable ID: note_nori_xi_nondesign_density_obstruction
- Author: unspecified; session provenance retained
- Primary home: section:nori_matroid_generalizations_conjectures
- Labels: counterexample, Cayley, binary matroid, two-design
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

For V=F2^4 with bit-coded generator set S={1,2,4,8,11} and distinguished t=7, the minimum t-generator triples are {1,2,4} and {4,8,11}; they do not form a pair design. There are 16 shortest turn cycles and 144 stationary children. To specify deck-odd colorings, represent an edge of generator s by its sorted unordered endpoints (x,x XOR s); compare it lexicographically with its deck translate by t and use the smaller representative. List edge-orbit representatives ordered by increasing generator s and then lexicographic endpoint pair; assign bits from mask M1=0x9b4f4 or M2=0xe7c68, and complement the deck translate. Both give 40 changed quotient turns, but the numbers of children increasing their geodesic-parent turn cost by two are 33 and 41, respectively. Independently verified by enumerating all 20 covering edge orbits, eight quotient-vertex stars, and all 16 shortest cycles. Thus the 2-design scalar conservation formula cannot be extended to arbitrary pointed binary generator matroids on the basis of total changed-turn density alone; pair incidence coefficients are essential.
