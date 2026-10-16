# Facet imbalance extremality and weighted-majority local maxima

- Stable ID: note_nori_facet_imbalance_extremal_20261014
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: extremal, facet-imbalance
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r9344_2
- Updated session: session_nori_r9344_2
- Disposition: none
- Successor: none

## Related references

- None

## Research note

THEOREM. For any legal antipodally odd coloring c of Q_n, let B_j be the sum of edge signs on facet x_j=0 and set E(c)=sum_j B_j^2. Every one-antipodal-pair-flip local maximum of E has a monochromatic full antipodal geodesic. PROOF. For edge-pair p of direction i, choose one edge e with sign s, and set v_i=0, v_j=(-1)^{x_j} for j!=i, where x is one endpoint. Then B=sum_p s_p v_p and E(c^p)-E(c)=4[(n-1)-s_p B.v_p]. Local maximality forces s_p B.v_p>=n-1>0. Hence every direction-i edge is signed according to the nonvanishing field sum_{j!=i} B_j(-1)^{x_j}. Absorb weight signs into cube bits and put a_j=|B_j|. Partition positive weights P,N to minimize D=|a(P)-a(N)|, P heavier. Every weight in P exceeds D: moving a smaller weight reduces D, while equality yields a zero direction-i field, excluded by local maximality. Zero-weight dimensions imply D>0 by the same nonvanishing condition. Starting with bit signs + on P and - on N, traverse N, then zero-weight dimensions, then P. At an N step the field is at least D+a_i>0, at a zero-weight step it is a(P)+a(N)>0, and at a P step it is at least a_i-D>0. The path is monochromatic. QED. COROLLARY. A bad coloring that maximizes E among bad colorings possesses an energy-increasing antipodal edge-pair flip; every such flip heals the coloring and is a restoration-critical internal pivot.
