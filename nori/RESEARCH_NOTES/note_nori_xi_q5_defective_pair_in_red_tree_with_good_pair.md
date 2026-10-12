# Q5 red tree has one defective antipodal pair and one geodesic pair

- Stable ID: note_nori_xi_q5_defective_pair_in_red_tree_with_good_pair
- Author: unspecified; session provenance retained
- Primary home: section:nori_matroid_generalizations_conjectures
- Labels: cube, matroid, distance-defect, root-exchange, finite-certificate
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

A full antipodally odd Q5 edge coloring shows that even a red tree component can contain an antipodal pair whose red path is two edges longer than a geodesic, while another pair in the SAME component has a red geodesic. Encode cube vertices 0,...,31, with antipode x xor 31. Let red representative bits be 0x82bcf4a09, indexing 40 antipodal edge-orbits by scanning undirected cube edges (u,u xor 2^i) in increasing u then coordinate i, with u<v and assigning a new bit at the first encountered orbit. For each orbit, the canonical lexicographically smaller undirected edge is red when the bit is one and its opposite edge is red when the bit is zero. Independent decoding gives red component R={0,1,2,3,8,10,11,13,15,25,27,29,31}, with red tree edges (0,1),(0,8),(2,3),(2,10),(3,11),(8,10),(11,15),(13,29),(15,31),(25,29),(27,31),(29,31). It contains two antipodal pairs: (0,31) has red distance 7 (cube distance 5), while (2,29) has red distance 5. Its tree rank is 12. The other large red component also has antipodal geodesics. Thus a proof cannot select an arbitrary port-loop root or self-contact pair and expect a minimum-distance lift; it must choose or exchange roots. This is not a counterexample to NORI1. Verification uses a 32-vertex red-graph BFS and the antipodal-orbit check for all 80 cube edges.
