# Antipodally opposed transitive star orders can block full rainbow cube paths

- Stable ID: note_antipodal_transitive_star_orders_block_full_rainbow_paths
- Author: unspecified; session provenance retained
- Primary home: subsection:rainbow_terminal_edge_theorem_for_locally_tournament_ordered_graphs
- Labels: obstruction, proved, grand-conjecture
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6176_2
- Updated session: session_nori_r6176_2
- Disposition: none
- Successor: none

## Related references

- None

## Research note

Let \(n\ge3\). Choose a coordinate \(s\) which is neither least nor greatest in a fixed linear order \(<\) of \([n]\). At each cube vertex \(x\), linearly order the \(n\) incident edges by their directions: use \(<\) if \(x_s=0\), and use the reverse of \(<\) if \(x_s=1\). Direct each local star tournament from earlier to later.

**Proposition.** Every star tournament is transitive, the tournament at \(\bar x\) reverses the tournament at \(x\) under the direction identification, and no full antipodal cube geodesic is increasing at all its internal vertices.

**Proof.** Let \(p=(p_1,\ldots,p_n)\) be a coordinate order for a full geodesic starting at \(x\), and let \(p_j=s\). If \(x_s=0\), then every comparison between successive direction labels before traversing \(s\) uses \(<\), and every comparison after traversing \(s\) uses its reverse. Thus positivity at every internal vertex would require
\[
 p_1<\cdots<p_j>\cdots>p_n.
\]
This makes \(s=p_j\) the greatest direction, contrary to the choice of \(s\). If \(x_s=1\), positivity instead requires \(p_1>\cdots>p_j<\cdots<p_n\), making \(s\) least. Both cases are impossible. The antipodal vertex has the opposite \(s\)-bit, so it has the dual star order. \(\square\)

Already \(Q_3\) with \(0<s=1<2\) supplies an obstruction. Thus antipodal opposition and transitivity of local comparisons alone cannot force a full increasing geodesic. Any shared topological completion theorem using local tournaments needs the additional compatibility enjoyed by tournaments constructed from a single coloring of underlying cube edges. This result concerns star comparisons and does not contradict the unrestricted NORI1 conjecture.
