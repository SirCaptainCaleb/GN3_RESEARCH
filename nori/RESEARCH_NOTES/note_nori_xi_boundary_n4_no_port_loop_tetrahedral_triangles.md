# Boundary n=4 tetrahedral triangle components give loop-free contact K4

- Stable ID: note_nori_xi_boundary_n4_no_port_loop_tetrahedral_triangles
- Author: unspecified; session provenance retained
- Primary home: section:nori_matroid_generalizations_conjectures
- Labels: boundary-tournament, matroid, port-loop-obstruction, finite-certificate
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

On n=4 original vertices 0,1,2,3, let the 12 reversal pairs of ordered triples be indexed by middle vertex increasing, then by ascending outer pair a<c. Give the representative the corresponding bit of mask 0x555; complement on reversal. The ordered-pair covering graph S(K4) has 12 vertices (a,b), degree four, and 24 edges corresponding to ordered triples. The red edge subgraph has four connected components, each a directed triangle: {(0,1),(1,2),(2,0)}, {(0,2),(2,3),(3,0)}, {(0,3),(3,1),(1,0)}, {(1,3),(3,2),(2,1)}. No triangle contains a reversal-pair (a,b),(b,a); hence the red zero-turn contact graph has NO loops. Every ordered-pair vertex has red degree two, so each original unordered pair {a,b} contributes 2*2=4 contact edges between the red triangles containing (a,b),(b,a). Every two of the four red components receive one such bundle, so the contact graph is K4 with four parallel edges per edge, total 24 edges and degree 12 at each contact vertex. It is connected, Eulerian, nonbipartite, even-size and loop-free: odd girth three and minimum unrestricted port cocircuit intersection four. Exhaustive enumeration of all 4096 reversal-odd n=4 boundary colorings finds precisely two with loop-free contact graphs: 0x555 and 0xAAA. This does NOT contradict the spanning at-most-one-turn boundary conjecture: a spanning word on 4 original vertices has only two triple colors, hence at most one change. The case proves the cube port-parallel-loop property is not a universal axiom of the shared antipodal graphic-flat matroid class.
