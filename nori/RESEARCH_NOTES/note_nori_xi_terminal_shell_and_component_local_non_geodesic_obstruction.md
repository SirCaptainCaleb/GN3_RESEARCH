# Terminal-shell rigidity and nongeodesic antipodal component obstruction

- Stable ID: note_nori_xi_terminal_shell_and_component_local_non_geodesic_obstruction
- Author: unspecified; session provenance retained
- Primary home: section:nori_matroid_generalizations_conjectures
- Labels: zero-turn-contraction, cube, antipodal-geodesic, matroid, obstruction, terminal-shell
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

Research obstruction and terminal-shell necessary conditions for the zero-turn contraction program (Article XI).

MINIMAL ANTIPODAL MONOCHROM PATH TERMINAL SHELL. Let c be an antipodally odd edge coloring of Q_n, and let P=(v_0,...,v_L) be a monochromatic path of globally minimum length among all monochromatic antipodal paths, so v_L=τv_0. Assume its color is red. Then:
(i) For any 2≤k≤L−1, if v_k is adjacent to v_0 in Q_n, their connecting edge must be red. For if it were blue, the antipodal edge τv_k--τv_0 is red, and the red path v_k→...→τv_0→τv_k would join antipodes in L−k+1<L steps, contradicting minimality.
(ii) Dually, for 1≤k≤L−2, if v_k is adjacent to v_L, their connecting edge must be red. Otherwise the red antipode edge τv_k--v_0, followed by v_0→...→v_k, joins τv_k and v_k in k+1<L steps.
The identities a_x+a_{τx}=n for red degrees show that the red direction sets at antipodal endpoints partition [n]. Thus the first and last path directions must differ. These facts are necessary for any hypothetical q>0 counterexample but do not suffice to shorten the path.

LOCAL GRAPH OBSTRUCTION, VALID IN ALL n≥5. Write cube vertices as subsets of [n] and begin with the following x=emptyset to τx=[n] path:
directions 2,1,3,1,4,1,5,6,...,n.
This has length n+2. For n=5 its vertices (encoded as bits) are
0,2,3,7,6,14,15,31.
Let R be the red subgraph comprising this path and, additionally, every edge incident with [n] except the edge in direction 2. Then the red degree at emptyset is 1 and at [n] it is n−1, summing to n, and R contains a single pair of antipodal vertices, namely emptyset and [n]. Their distance inside R is n+2. The path avoids the blue endpoint-neighbor configurations of (i),(ii).

For n=5, an independent graph BFS gives red antipodal pairs [(0,31,7)] and 10 red edges in R. The constructed R is a partial red edge subgraph, NOT a claim that its complement can be filled into a counterexample to NORI1; such a global coloring would have to satisfy all deck-odd edge assignments, which can force other red components or a distinct monochromatic geodesic.

Consequence: all arguments using only a single red antipodal connected component, endpoint-degree complementarity and immediate terminal-shell constraints cannot imply q=0. Any deterministic matroid closure proof must use global covering/cocycle constraints across the component-contact graph, or a coordinated exchange involving multiple color components. Preserve as research note, not manuscript theorem.
