# Sharp linear query complexity of constructive feedback-two NORI1 theorem

- Stable ID: note_e23fd851d91dffb623101afa
- Author: unspecified; session provenance retained
- Primary home: subsection:directed_influence_components_and_monotone_seam_lifting
- Labels: NORI1, oracle-complexity, feedback-two, lower-bound
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11123_2
- Updated session: session_nori_r11123_2
- Disposition: none
- Successor: none

## Related references

- None

## Research note

For every n>=3, the two-feedback bisection algorithm needs O(n) edge-color queries and this is worst-case optimal for deterministic oracle algorithms. Lower-bound family: direction rules c_a=x_b, c_b=x_a, and c_i=x_a xor alpha_i for all other n-2 directions i, with independent hidden phase bits alpha_i. Every coloring is legal odd, and deleting a,b leaves an acyclic influence digraph. A query in direction i among the n-2 leaf directions reveals only alpha_i; no other edge query reveals that phase. If an algorithm outputs a full monochromatic path without querying some leaf i, flipping alpha_i leaves the observed query transcript and every other edge color unchanged but reverses its i-edge color. Since n>=3, at least one assignment makes the path non-monochromatic. Thus guaranteed deterministic output requires querying every leaf direction, at least n-2 edge evaluations. This matches the O(n) upper bound of the antipodal bisection algorithm, assuming the feedback pair and influence topological order are supplied. The result is a sharp oracle-query theorem, not a new coloring class.
