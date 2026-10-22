# Exceptional Coxeter root-square octagon in the common-edge path nerve

- Stable ID: note_nori_xvii_root_square_octagon_common_edge_nerve_r12074
- Author: unspecified; session provenance retained
- Primary home: subsection:central_freudenthal_subdivision_and_the_all_root_geodesic_chamber_sphere
- Labels: topology, obstruction
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r12074_2
- Updated session: session_nori_r12074_2
- Disposition: none
- Successor: none

## Related references

- None

## Research note

For n>=5 let X_n be the dual all-root Freudenthal Coxeter sphere and N_n the nerve whose vertices are rooted full antipodal geodesics, with a simplex on each nonempty family whose original edge sets share an edge. Adjacent chambers share an edge: r_0 preserves the first edge; r_k (k>=1) preserves all edges except those in positions k,k+1. Thus the chamber assignment extends equivariantly across dual edges.

Every rank-two residue other than (r_0,r_1) has one edge common to all chambers: r_0,r_j (j>=2) share the first edge; commuting r_i,r_j (i,j>=1) change at most four edge positions, leaving n-4>=1; type-A braid r_i,r_(i+1) changes at most three, leaving n-3>=2. Hence their chamber sets span simplices in N_n.

For the (r_0,r_1) octagon, fix an ij-square F and a tail order rho of the remaining n-2 dimensions. Its eight paths are indexed by a corner u of F and either initial order ij or ji. Let K_F be their induced common-edge nerve. Each path uses two adjacent square edges and then n-2 edges in the outside-dimension face at u+e_i+e_j. Distinct roots give disjoint tail faces. Every original edge e of F belongs to four of the eight paths, yielding a tetrahedron T_e. Consecutive T_e intersect in edges, opposite T_e are disjoint, and triple intersections vanish. Hence their union is homotopy equivalent to S^1. At each root u, the two alternative paths have disjoint square routes but share their entire nonempty tail. Their pair contributes one additional maximal edge of K_F, contained in no triangle. Adding the four root-pair edges gives |K_F| homotopy equivalent to a wedge of five circles.

The Coxeter octagon boundary traverses each root-pair edge once. A 1-cochain supported on any such edge is a cocycle and evaluates to one on the octagon. Thus its class is nonzero in H_1(K_F;F2). A filling of the exceptional B-type four-braid residue cannot use solely its eight full-path witnesses in this carrier. It must involve additional paths or enriched coherence data. The class may die upon inclusion K_F -> N_n, so this gives no global forcing claim.
