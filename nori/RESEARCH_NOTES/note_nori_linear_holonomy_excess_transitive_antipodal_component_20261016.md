# Linear holonomy length excess inside a transitive commutator orbit

- Stable ID: note_nori_linear_holonomy_excess_transitive_antipodal_component_20261016
- Author: unspecified; session provenance retained
- Primary home: subsection:paired_direction_involutions_and_geodesic_endpoint_matchings
- Labels: holonomy, commutator, dimension-uniform, antipodal, obstruction
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r10917_4
- Updated session: session_nori_r10917_4
- Disposition: none
- Successor: none

## Related references

- subsection:paired_direction_involutions_and_geodesic_endpoint_matchings
- note:note_nori_xi_q6_single_contact_tree_defect

## Research note

**Theorem (linear antipodal holonomy excess on a transitive derived-group orbit).** For every integer n≥6, there is an antipodally odd binary coloring of Q_n with a red connected component C such that (i) C contains antipodal pairs, (ii) the commutator subgroup G_c' of the red edge-swap group acts transitively on C, and (iii) every antipodal pair x,bar x in C has red graph distance
\[
d_{R}(x,\bar x)=n+2\lfloor n/6\rfloor.
\]
Consequently every even-generator word sending a root x∈C to its antipode has length at least \(2n+2\lfloor n/6\rfloor\), and this length is attained. In particular no root choice in C permits a doubled-direction return word, even though all its vertices lie in one transported-square-holonomy orbit.

*Certificate for the six-dimensional block.* Use the previously published legal Q_6 coloring encoded by antipodal-edge-orbit mask 0x6228f060010108000780d under the following convention: scan undirected edges (u,u xor 2^i) with u<v in increasing u, then i, and introduce an orbit upon its first occurrence. A set bit makes the first encountered edge red; its antipodal mate blue. An independent decoder confirms that the red component T of 0 consists of vertices {0,1,4,8,9,13,29,31,41,45,47,61,63}, with the twelve red edges
\[
(0,1),(0,4),(0,8),(8,9),(9,41),(13,29),(13,45),(29,61),(31,63),(41,45),(47,63),(61,63).
\]
This is a tree, and its sole antipodal pair is {0,63}, joined by the eight-edge red path \(0,8,9,41,45,13,29,61,63\). This base certificate was already recorded in note_nori_xi_q6_single_contact_tree_defect; the new result is its dimension-uniform quantitative holonomy amplification.

*Proof of amplification.* Write \(n=6k+r\), with \(k\ge1\) and \(0\le r<6\). On the first 6k dimensions take k independent copies of the certified six-dimensional coloring. For each remaining direction j set \(c_j(x)=x_0\), where bit 0 belongs to the first six-dimensional block. The original block rules ignore all additional bits. All rules ignore their own direction bit and reverse under global complementation, so the resulting coloring is legal.

The red component \(C=T^k\times Q_r\) is connected: the k tree factors are connected, and when the first factor is at vertex 0 all r added directions are red, permitting any changes in the last r bits. No red edge leaves \(C\), because the block rules do not change between added-bit slices, and added-direction edges preserve every block state. Every antipodal pair in C has in each T factor the endpoints 0 and 63. Therefore every red path connecting it has at least eight moves in each six-dimensional block and r moves in the additional directions, giving length at least \(8k+r=n+2k\).

For the upper bound, follow the eight-edge tree path in each block. If the first block starts at 0, toggle all r additional bits before traversing the first block; otherwise the first block ends at 0, so toggle the additional bits after reaching that endpoint. All these moves are red. Thus every antipodal pair in C has red distance \(8k+r\).

By the derived-orbit classification theorem (DO2) in the live Article XI subsection paired_direction_involutions_and_geodesic_endpoint_matchings, G_c' is transitive on every red component containing an antipodal pair, including C. By its rootwise even-holonomy metric theorem (EH1), the minimum length of an even-generator word from x to bar x is \(n+d_R(x,\bar x)=2n+2k\). The same lower bound holds uniformly over every antipodal root in C. \(\square\)

Here \(|C|=13^k2^r\), and C contains \(2^{k+r-1}\) unordered antipodal pairs. For n=6k, the excess is n/3 over the target even-word length 2n. The obstruction addresses compression within a commutator orbit; other red components and the opposite color may still contain full antipodal geodesics.
