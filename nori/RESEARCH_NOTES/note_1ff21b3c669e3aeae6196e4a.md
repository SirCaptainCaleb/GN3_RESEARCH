# Hall expansion for balanced geodesic-support layers and Aharoni-Haxell midpoint obstruction

- Stable ID: note_1ff21b3c669e3aeae6196e4a
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: NORI1, Hall, Aharoni-Haxell, open-conjecture
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r9928_1
- Updated session: session_nori_r9928_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

PROVED: For any vertex-balanced antipodally odd Q_(2m) coloring, root x, color b, rank k<m, and family F of reachable k-direction sets, its family of legal one-step (k+1)-extensions satisfies |N(F)| >= (m-k)/(k+1)*|F|. Hence Hall gives rank-saturating injection when 2k+1<=m. Sharpness: pair directions a_j,b_j, color c_(a_j)=x_(b_(j+1)), c_(b_j)=1+x_(b_(j+1)) cyclically. This is legal balanced; on face b=0 only a-direction edges are red, so rooted rank profiles are C(m,k), attaining the bound and ruling out injection past middle rank. PROVED: For red adjacency R, R^2-mI is symmetric nonnegative with row/column sums m(m-1), counting red 2-step geodesics; Hall gives perfect matching between roots and red distance-2 endpoints. Also m-regular red graph decomposes into m perfect matchings, and two different perfect matching factors produce a 3-partite perfect matching of two-step red geodesics. Beyond 2 steps factor-rainbow walks can have directions (i,j,i) and fail dimension simplicity. OPEN: endpoint reachability relation by red/blue k-step geodesics has perfect matching for every k<=m; tested random balanced Q4,Q6,Q8,Q10 including square-flip samples. TRIPARTITE LINK: hyperedges (root x, midpoint v, support S), v=x XOR S, S of size m and red halfpath exists. Link at fixed root or fixed midpoint is a matching. AH hypergraph Hall threshold nu(link(X))>=2|X|-1 cannot hold for all 2^(2m) roots as support class has C(2m,m) vertices; AH/Ryser r=3 give disjoint midpoint hyperedges, whereas NORI1 requires antipodal roots sharing a midpoint. If NORI1 fails, at each midpoint at most C(2m,m)/2 roots can red-reach it. Explicit good balanced Q6 example c_i=x_(i+1 mod 3), c_(3+i)=1-x_(i+1 mod3) has perfect midpoint endpoint matchings in both colors but no complementary red-blue supports at root zero (6 red vs 1 blue). AUDIT /mnt/data/nori_hall_hypergraph_reachability_audit.py. Literature Aharoni-Haxell 2000 economical-hierarchical triangulation; Aharoni Ryser r=3 2001; Haxell-Narins-Szabo extremal matching complexes.
