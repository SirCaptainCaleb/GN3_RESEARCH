# Rainbow matchings and the APS expansion obstruction in legal cube colorings

- Stable ID: note_ff817c340f78afdb8b73c22f
- Author: unspecified; session provenance retained
- Primary home: subsection:paired_direction_involutions_and_geodesic_endpoint_matchings
- Labels: NORI1, rainbow-paths, direction-labels, APS
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r10712_1
- Updated session: session_nori_r10712_1
- Disposition: none
- Successor: none

## Related references

- toolkit:literature_alon_pokrovskiy_sudakov_long_rainbow_cycles_2017

## Research note

Proposition A. Every set of cube edges with pairwise distinct direction labels is acyclic: a closed walk changes each bit an even number of times, hence every cycle repeats some direction.

Proposition B. For n>=6, the red subgraph of every antipodally odd cube coloring contains a matching with one edge of every one of the n direction labels. Each direction has 2^(n-2) red edges (one per antipodal edge orbit). After picking k disjoint red edges from different directions, their 2k endpoints obstruct at most 2k edges in the next direction because those edges form a matching. Since 2^(n-2)>2(n-1), the greedy choice succeeds through all n directions. This is a red rainbow matching with n components, not a long red geodesic.

Proposition C. For every b between 1 and 2^(n-2), there are two b-vertex subsets of Q_n having no edges between them: choose subsets of the faces with first two bits 00 and 11. Consequently, the expansion hypothesis used for path-forest absorption by Alon, Pokrovskiy and Sudakov, that all disjoint pairs of b-vertex sets have many reserve edges between them, fails for any subgraph of the cube at the small b values needed to join paths using only O(n) vertices.

Proposition D. Sampling direction labels independently and keeping every cube edge with a selected label gives a disjoint union of 2^(n-|S|) subcubes Q_|S| where S is the selected direction set. Unless S contains every direction, the sampled graph is disconnected. Sampling just the red edges in those directions cannot repair this. Moreover the direction-labeled cube has no rainbow cycle, by Proposition A.

The near-spanning rainbow-cycle theorem of Alon--Pokrovskiy--Sudakov (2017) thus does not apply directly to the canonical proper direction labeling of Q_n. Its graph-theoretic rainbow forest obstacle is trivial here, while its connecting-reserve hypothesis is impossible at relevant size scales. A viable transfer must encode endpoint transport and unused direction labels in a different auxiliary graph and simultaneously respect the independent binary edge coloring. These proofs apply without restrictions on rule complexity.
