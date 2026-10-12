# Q5 red tree contains two antipodal pairs but no red cycle

- Stable ID: note_nori_xi_q5_two_pair_red_tree
- Author: unspecified; session provenance retained
- Primary home: section:nori_matroid_generalizations_conjectures
- Labels: cube, matroid, red-component-tree, multiple-self-contacts, obstruction
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6430_2
- Updated session: session_nori_r6430_2
- Disposition: none
- Successor: none

## Related references

- None

## Research note

A fully specified antipodally odd Q5 coloring has a red connected component that is a tree and contains TWO antipodal vertex pairs. Vertices are encoded by 0,...,31, with antipode u xor 31. Red component R={0,1,2,3,4,5,7,14,15,22,23,30,31}. Its red edges are (0,2),(0,4),(1,3),(1,5),(2,3),(3,7),(7,23),(14,30),(15,31),(22,30),(23,31),(30,31). These twelve edges form a tree on thirteen vertices. It contains antipodal pairs (0,31) and (1,30), with no others. To reconstruct the full coloring, enumerate all undirected Q5 edges (u,v) in increasing u and coordinate index, assign each antipodal edge-pair one bit in first-encounter order, and use mask 0x1f8002266 to declare the canonical representative red when its bit is one and the mate red when its bit is zero. The 40 red edges form a globally reversal-odd assignment and BFS reproduces R. Endpoint red degrees are 2 and 3 for both pairs. This refutes the auxiliary claim that two distinct self-contact pairs in one monochromatic component force a nontrivial monochromatic graphic cycle. Thus even multiple port-loop bundles can be carried by a tree. This is not a counterexample to NORI1: the two antipodal pairs have red shortest paths of length five.
