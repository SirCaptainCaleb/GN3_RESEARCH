# Bridge-root line metric equivalence for cube geodesics

- Stable ID: note_c943eddf68ee0a9b46e8164c
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: global-closure, metric-gluing
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

Bridge-root metric selection theorem (unrestricted, n>=3). Let P be a full dimension-simple antipodal geodesic, and for each direction j let w_j be the lower endpoint of its unique direction-j edge, represented by bits outside j. Define D_ij=1+d_H(w_i restricted away from i,j, w_j restricted away from i,j). Then D_ij=|rank_P(i)-rank_P(j)|. Indeed, a bit k outside i,j differs at the two bridge endpoints precisely when direction k occurs strictly between i,j along P. Conversely, suppose a family of candidate bridge endpoints has D_ij=|rank(i)-rank(j)| for some permutation of the n directions. Adjacent directions in that permutation have D=1, so their endpoint labels agree at every bit other than their two direction bits. Hence for any fixed k, the kth bits of the other endpoints are constant on each side of k in the proposed order. If k is internal, the two endpoints adjacent to k have D=2; every shared bit other than k agrees by the adjacent-pair equalities, so their kth bits differ. Choose initial root bit r_k as the common kth bit of all earlier endpoints if there are earlier ones; if k is first, set r_k to the complement of the common kth bit of all later endpoints. Then w_j(k)=r_k XOR [k precedes j] for all j different from k. The path starting at r and traversing the proposed order has precisely the given bridge endpoints. The line metric recovers the direction order up to reversal and then determines the unoriented geodesic uniquely. This was exhaustively audited over all candidate bridge endpoint assignments: 24 valid families in Q3 and 192 in Q4, matching their numbers of unoriented antipodal geodesics. NORI1 therefore has a complete unrestricted metric-selection reformulation: For an odd cube-edge coloring c, in each direction j let Z_j be the lower endpoints of its zero edges (one choice from every antipodal edge pair). A monochromatic-zero antipodal geodesic exists if and only if one can select w_j in Z_j for every j so that D is a consecutive-integer line metric. A healing antipodal edge orbit produces an otherwise zero-colored line-metric selection with its unique wrong-color chosen edge in the healed direction.
