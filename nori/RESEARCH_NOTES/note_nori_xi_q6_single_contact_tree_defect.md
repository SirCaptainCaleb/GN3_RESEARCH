# Q6 red tree with unique antipodal pair of distance eight

- Stable ID: note_nori_xi_q6_single_contact_tree_defect
- Author: unspecified; session provenance retained
- Primary home: section:nori_matroid_generalizations_conjectures
- Labels: cube, matroid, obstruction, tree-component, finite-certificate
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

Full antipodally odd Q6 coloring certificate. Vertices 0..63, antipode x xor 63. Red orbit bits mask 0x6228f060010108000780d (index edge orbits by first encounter scanning undirected edges (u,u xor 2^i), u<v, in increasing u then i; bit one makes lexicographically smaller edge red, otherwise its mate red). Red component of 0 has vertices {0,1,4,8,9,13,29,31,41,45,47,61,63}; red edges (0,1),(0,4),(0,8),(8,9),(9,41),(13,29),(13,45),(29,61),(31,63),(41,45),(47,63),(61,63). This is a tree with the sole antipodal pair (0,63), whose unique red path (0,8,9,41,45,13,29,61,63) has length eight, not six. Its graphic rank twelve saturates Article XI endpoint-star defect bound at n=6,q=1, and its antipodal cut pair is disjoint. Another red component contains a geodesic (3,2,6,22,20,52,60). Thus even a one-contact tree attaining the rank bound need not have a geodesic; closure must compare separate components or use global information.
