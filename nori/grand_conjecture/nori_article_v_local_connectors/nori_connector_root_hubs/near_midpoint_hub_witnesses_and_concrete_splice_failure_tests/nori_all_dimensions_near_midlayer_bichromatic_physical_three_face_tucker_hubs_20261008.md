# All-dimensional Tucker: every root's near-middle Hamming band contains a genuine two-color three-face hub

# EVERY ROOT HAS A GENUINE BICHROMATIC ORDERED THREE-FACE HUB IN ITS NEAR-MID HAMMING LAYERS, ALL n>=7

Let n>=7 and let c be any ACTIVE NORI binary coloring of PHYSICAL ORDERED cube three-faces with c(bar F,rev σ)=1−c(F,σ). Fix ANY cube root x. Let K_x be the team's proven free-antipodal endpoint-opposed rooted full-geodesic permutohedral face nerve; its vertices are REAL full x-rooted direction permutations pi for which the first and last physical ordered 3-face window colors differ, with known nonzero w1^(n−3). Θ acts as reversal of full direction order and keeps x fixed.

Define one CANONICAL CENTRAL physical ordered-three-face selection J(pi) equivariantly as follows.
(ODD n=2m+1) Take j(pi)=m, the unique central consecutive three-edge window index; its free triple spans edge positions m,m+1,m+2.
(EVEN n=2m) Choose a fixed numerical total ordering on cube directions. Let j(pi)=m−1 if p_m<p_(m+1), and let j(pi)=m otherwise. These are the two near-central consecutive three-edge windows. Under full direction reversal the compared central direction names SWAP, so
  j(rev pi)=(n−1)−j(pi),
the correct reversal of window indices 1,...,n−2.
In both cases set the genuine central selected physical-face color
  q(pi)=w_(j(pi))(x,pi)∈{0,1}.

**THEOREM 1 (literal oddness).** q(rev pi)=1−q(pi). PROOF: active NORI physical reversal gives w_j(x,rev pi)=1−w_(n−1−j)(x,pi), and our selected index obeys j(rev pi)=n−1−j(pi). Hence q is a bona fide odd ONE-BIT color label on all genuine endpoint-opposed path vertices. The even-dimensional tie-break does not refer to virtual barycenters and preserves the complete path physical provenance.

**THEOREM 2 (all-dimensional near-middle bicOLOR hub forcing).** Put
  k=floor((n−2)/2).
For EVERY x∈Q_n, there exist two ACTUAL full x-rooted antipodal direction orders pi,sigma whose endpoint window colors are opposite, with
  q(pi)=0, q(sigma)=1,
and a NONEMPTY PROPER used-coordinate prefix support S shared by both orders, of size
  k<=s=|S|<=n−k.
Thus both real full paths traverse the SAME physical cube vertex
  y=x XOR S
after s edges. The actual selected ordered THREE-FACES of opposite colors BOTH CONTAIN y as a physical vertex. So every root x has a genuine physically witnessed bichromatic ordered-three-face hub y inside its near-middle Hamming shells.

**PROOF.** Apply the team's proved general one-bit near-bisection Tucker theorem nori_binary_switch_side_tucker_near_bisection_actual_rooted_full_paths_20261008 to the ACTUAL odd ±1-valued label (-1)^q on K_x. That proof needs only antipodal oddness and the source index n−3, so it gives actual pi,sigma with opposite q in ONE inner permutohedron facet H_S at rank k<=s<=n−k. Hence they genuinely pass through y=x XOR S at step s.

Check that their selected physical 3-edge windows BOTH include this rank s, regardless of the central tie-break:
 - for n=2m+1, k=m−1 and n−k=m+2; the selected window j=m traverses precisely path vertex ranks m−1,m,m+1,m+2.
 - for n=2m, k=m−1 and n−k=m+1; selected window j=m−1 traverses ranks m−2,...,m+1, while j=m traverses ranks m−1,...,m+2. The COMMON rank interval present in BOTH possibilities is m−1,...,m+1, which contains every allowed s.
Thus y is a literal physical VERTEX on both selected 3-edge subpaths, and so belongs to both corresponding actual free-coordinate physical three-faces. Their colors are q(pi),q(sigma), which are opposite. QED.

**THEOREM 3 (automatic antipodal paired hub).** The Θ-reversed x-rooted full paths rev pi,rev sigma meet at the antipodal physical vertex bar y after n−s edges, and their selected central ordered faces are the antipodal images (with reversed directions) of those at y, so colors are complemented and again opposite. Thus y and bar y are BOTH bichromatic ordered-three-face hubs. The allowed Hamming interval is symmetric under s↦n−s.

**ROOT-LAYER SEPARATOR FORMULATION.** Let B_c be the set of cube vertices through which AT LEAST ONE ordered physical three-face of each binary color passes. The proof establishes:
  B_c is antipodally invariant,
  for EVERY physical x∈Q_n, there exists y∈B_c with
     floor((n−2)/2) <= d_H(x,y) <= n−floor((n−2)/2).
Moreover y is witnessed by TWO genuine endpoint-opposed full x-rooted paths agreeing on a near-midpoint used-coordinate prefix and carrying opposite physical central-window colors. This is a quantitative *layer hitting property* stronger than a bare global existence of a bichromatic physical face hub.

**RELATION TO PRIOR RESULTS AND LIMIT.** This extends the odd-dimensional theorem nori_odd_dim_near_midlayer_bichromatic_ordered_three_face_hub_from_tucker_20261008 to ALL n>=7, using the EVEN-DIMENSION CENTRAL-DIRECTION-COMPARISON tie-break. It also strengthens the team's opposite-color mono4 near-middle Tucker result in a DIFFERENT direction: both selected one-window ordered three-faces now literally SHARE ONE PHYSICAL HUB, whereas opposite-color longer mono4 subpaths may occur at unrelated positions. But a pair of different-color THREE-FACE windows alone is NOT a monochromatic four-edge connector, let alone a full <=1-switch NORI path. Their three-free-direction supports may be disjoint, their direction orders incomparable, and no physical same-root complementary reversed-tail pair is forced. The next combinatorial extraction should upgrade this topologically forced common physical hub, ideally preserving the TWO full-path near-middle-prefix memories. No GRAND closure is claimed.

**COROLLARY 4 (TOPLOGICALLY FORCED LITERAL BICHROMATIC FOUR-PATH PHASE BOUNDARY).**
The near-midpoint hub y in Theorem2 can be chosen so that there exist FOUR PAIRWISE DISTINCT coordinate directions a,b,c,d with
 c(F(y;{a,b,c}),(a,b,c))
    !=
 c(F(y;{b,c,d}),(b,c,d)).
Thus y is the center of an ACTUAL directed FOUR-EDGE physical cube geodesic of direction word (a,b,c,d) with EXACTLY ONE color switch; its two physical ordered 3-face windows INTERSECT IN THE ACTUAL PHYSICAL 2-FACE with free directions {b,c} through y. This is a literal color-transition square in Q_n, not an abstract pair of faces merely sharing a vertex.

PROOF. For a fixed physical hub y, construct the undirected shift graph G_y on all ORDERED triples (a,b,c) of pairwise distinct cube directions. Connect (a,b,c) to (b,c,d) whenever a,b,c,d are pairwise distinct. The actual physical ordered-3-face color through y is a vertex coloring of G_y. The graph is CONNECTED for n>=5: for any distinct a,b,c,d, one may change the FIRST coordinate a to d while keeping b,c fixed using a two-edge route via (b,c,e), where e is any fifth direction outside {a,b,c,d}. One may similarly change the LAST coordinate c to d while fixing a,b via an intermediate (e,a,b). These operations permit arbitrary changes of first/last entries with the middle fixed. To change the middle coordinate b to any desired d distinct from a,c, first change the last entry to d, then traverse one shift edge, putting d in the middle; after that independently adjust the two outer coordinates. Thus all ordered triples lie in one component.

By Theorem2 there are at least one color0 and one color1 ordered triple through y. Along an undirected G_y path between them there is an EDGE with differently colored endpoints. That edge is exactly the displayed pair of consecutive ordered windows of a REAL centered four-edge directed cube geodesic. Both 3-faces contain y, have common free axes b,c, and share the same physical square F(y;{b,c}); the two colors differ, so the four-path has exactly one change. QED.

**No mistaken GRAND extraction:** These length-four one-switch physical paths are not n-edge antipodal geodesics for n>=7, and the topologically forced original pair of endpoint-opposed full paths need not contain the new four-path from the shift graph. The corollary does, however, give an honest color-transition square in EVERY root's near-mid Hamming band, a concrete physical interface suitable for witness-compatible topological carriers.
