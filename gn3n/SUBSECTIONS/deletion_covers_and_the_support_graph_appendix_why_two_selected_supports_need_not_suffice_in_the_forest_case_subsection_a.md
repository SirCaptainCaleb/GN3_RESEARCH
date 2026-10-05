# deletion_covers_and_the_support_graph_appendix_why_two_selected_supports_need_not_suffice_in_the_forest_case_subsection_a

## Metadata

- ID: deletion_covers_and_the_support_graph_appendix_why_two_selected_supports_need_not_suffice_in_the_forest_case_subsection_a
- Parent Section: deletion_covers_and_the_support_graph_appendix_why_two_selected_supports_need_not_suffice_in_the_forest_case
- Position: 1
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Cold composition

(none yet)

## Development

The forest alternative cannot in general be completed by choosing two supports already present in the selected family.

Let \(J\) be a connected selected-support tree, with support \(S_u\) at each vertex \(u\). For vertices \(u,v\), let \(P_{uv}\) be their tree path.

**Proposition A.1.** The union \(S_u\cup S_v\) equals \(V(H)\) if and only if \(P_{uv}\) has even length and every edge outside \(P_{uv}\) is pendant and attached to a vertex of \(P_{uv}\) at odd distance from \(u\).

**Proof.** For an edge label \(e\), membership in \(S_w\) is determined by the parity of the distance from \(w\) to the nearer endpoint of \(e\): the label belongs to \(S_w\) exactly at odd distance. If \(P_{uv}\) has odd length, its first edge label is omitted by both supports. Assume the path has even length. Every label on the path then belongs to exactly one of \(S_u,S_v\). For an edge off the path, the first edge of its branch belongs to both supports exactly when its attachment point is at odd distance from \(u\); a second edge on the same branch would then be omitted by both. This proves the criterion. \(\square\)

Consequently, if branching remains after suppressing degree-two vertices on one side of the tree bipartition and deleting leaves on that side, no two selected supports cover all vertices. Any two-cover must then use a Hamiltonian support not already present among the selected deletion-cover components. This obstruction concerns only selection from the existing support family; it does not obstruct the theorem itself.
