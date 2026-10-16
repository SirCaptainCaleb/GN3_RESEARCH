# Bridge-root line metric and one-edge rigidity

- Stable ID: note_eeeacb5aff2df062871b1761
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: bridge-signature, global, rigidity
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r9311_1
- Updated session: session_nori_r9311_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

**Bridge signature line metric (unrestricted).** Let P be an arbitrary full dimension-simple antipodal geodesic of Q_n, and let w_j be the endpoint of its direction-j edge lying in facet x_j=0. For distinct i,j define D(i,j)=1+d_H(w_i|_{[n]\{i,j}},w_j|_{[n]\{i,j}}). If pi is the order of directions along P, then D(i,j)=|pi^{-1}(i)-pi^{-1}(j)|. Indeed, for any bit position k different from i,j, the values of w_i and w_j at k differ precisely when direction k lies between i and j in pi. Thus the entire list of bridge roots reconstructs the direction order up to reversal, because D is the metric of n labeled points occupying the n positions of a line. It also reconstructs the unoriented geodesic: after choosing an orientation pi, each initial root bit r_k is w_j(k) XOR [k precedes j] for any j != k. **One-edge overlap rigidity.** If two full antipodal geodesics have the same direction-j edges for all j except one direction i, then they coincide up to reversal, or their different i-edges are antipodal and the two paths result from moving the i-edge from one endpoint of their common (n-1)-edge chain to the other. Proof: remove the i-edge from the first geodesic. If i was internal, the remaining edges form two disjoint nonempty chains. Among their four pairs of endpoints, only the original i-edge joins at Hamming distance one, so no alternative path exists. If i was terminal, the remaining edges form one (n-1)-edge chain. Reattaching an i-edge at either endpoint gives the only two completions; those i-edges are antipodal. **Consequence for antipodally odd colorings.** Two different full antipodal geodesics that each have a single interior wrong-color edge of the same color cannot share their direction-j edges in all but one direction. Otherwise both wrong-color edges would have to occupy the differing direction and be either identical or antipodal; distinct same-colored wrong edges are neither. Therefore the two witness bridge signatures differ in at least two directions. All statements are independent of locality and dimension.
