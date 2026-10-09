# Exact universal even-edge middle-belt carrier: two-color Johnson geodesics with physical two-route certificates and caps

# Arbitrary even-dimensional physical cube EDGE colorings: exact Johnson-geodesic middle-belt criterion

Let n=2k>=4, and c assign arbitrary bits to ACTUAL undirected physical edges of Q_n. Antipodal oddness may be imposed, but is NOT needed for the basic exact criterion. Let J=J(2k,k) be the Johnson graph whose vertices are the physical rank-k cube vertices, viewed as k-subsets S⊆[2k], and whose edges connect S,T with |S∩T|=k−1. Each J edge has a UNIQUE ordered exchange T=S\{a} ∪{b}, where a∈S, b∉S.

**Definition (genuinely q-certified two-route Johnson edge).** For q∈{0,1}, call S—T q-certified when at least one of the following ACTUAL two-edge cube geodesics is monochromatic of edge color q:
 LOWER: S -> S\{a} -> T (physical rank sequence k,k−1,k);
 UPPER: S -> S∪{b} -> T (physical rank sequence k,k+1,k).
Every selected route uses the two directions a,b exactly once. Denote by J_q the spanning graph of J consisting of all q-certified edges. A Johnson edge may lie in neither, one or both of J_0,J_1 (if its distinct upper/lower physical routes certify different colors).

**THEOREM (necessary AND sufficient exact middle-belt criterion).** The actual colored cube has a monochromatic full 2k-edge antipodal cube geodesic of color q all of whose vertices have Hamming rank k−1,k, or k+1 IF AND ONLY IF at least ONE of two concrete alternatives holds:

(M) (MIDDLE-RANK ROOT.) There is a Johnson GEODESIC
  S_0,S_1,...,S_k=S_0^c
of k J-edges, all belonging to J_q. This is a path between complementary ksets at maximum Johnson distance k.

(O) (OUTER-RANK ROOT AND TWO CAPS.) There is a Johnson GEODESIC
  S_0,S_1,...,S_(k−1)
of k−1 J-edges all belonging to J_q and whose endpoints satisfy |S_0∩S_(k−1)|=1. Let h denote their unique COMMON coordinate, and g denote the unique coordinate outside their UNION. At least one of the following TWO ACTUAL paired terminal-cap arrangements has both physical edges colored q:
  LOWER START/UPPER END:
    c(S_0\{h} -- S_0)=q AND c(S_(k−1) -- S_(k−1)∪{g})=q;
  UPPER START/LOWER END:
    c(S_0∪{g} -- S_0)=q AND c(S_(k−1) -- S_(k−1)\{h})=q.

**Proof (sufficiency).** In case M, choose independently for each Johnson step S_{j−1}—S_j ANY of its genuine q-monochromatic upper/lower 2-edge physical routes. Because S_0 and S_k are complementary and the Johnson path is shortest length k, its k removed coordinates and k added coordinates are each pairwise distinct and together exhaust ALL 2k cube coordinates. Therefore the concatenated 2k-edge physical path flips each direction exactly once, hence is a full antipodal geodesic; all intermediate ranks are k−1,k,k+1 and all edges color q.

In case O, if the first cap arrangement holds, start at physical root X=S_0\{h}, add h to S_0, realize each J_q step by a chosen q-good upper/lower route, and finally add g from S_(k−1). The Johnson-geodesic property ensures the exchanged directions are exactly (S_0\{h})\(S_(k−1)) and S_(k−1)\S_0, all distinct and disjoint from h,g. Thus all n=2k directions are flipped precisely once and the endpoint S_(k−1)∪{g}=X^c. The second cap arrangement starts at X=S_0∪{g}, removes g to S_0, follows the same Johnson q-routes, then removes h; again the final endpoint S_(k−1)\{h}=X^c. Every physical edge has color q by its cap or certified route.

**Proof (necessity).** Let P be ANY monochromatic full cube geodesic confined to the three central ranks. Its initial rank must be k−1,k, or k+1, and final rank is the complementary rank k+1,k, or k−1. If its initial rank is k, the first and last vertices are rank-k complements and, since each cube step flips Hamming rank by exactly1, the path returns to rank k every TWO steps. Its successive rank-k vertices give a J geodesic of k swaps from S_0 to S_0^c; each swap is one of the two physical q-monochromatic routes, proving M. If the initial rank is k+1, REVERSE P to obtain an equally monochromatic physical geodesic beginning at k−1 and ending at k+1. The first and last steps meet rank k, and the 2k−2 intervening steps decompose into k−1 rank-k-to-rank-k excursions of two physical steps each. Distinct coordinate directions along P make these a genuine J geodesic of length k−1, with endpoint intersection exactly one and exterior complement exactly one. The actual first/last physical edges are precisely one of the two paired terminal-cap alternatives displayed above, proving O. QED.

**Exact specialization to complement-odd middle-vertex labels.** Suppose every physical belt edge adjacent to middle-rank S is colored lambda(S), with lambda(S^c)=1+lambda(S). Then a J edge S—T belongs to J_q precisely when lambda(S)=lambda(T)=q; BOTH its lower/upper routes have that color. Alternative M is impossible because it would require equal labels at antipodal middle endpoints S_0,S_0^c. In O, BOTH cap arrangements automatically have color q whenever its middle path is lambda-monochromatic. Thus the general exact criterion reduces PERFECTLY to the Johnson/tight-path equivalence proved in nori_k1_even_central_vertex_gate_exact_johnson_tight_path_correspondence_20261009. The latter is therefore the zero-local-memory specialization of this FULL arbitrary-edge carrier.

**Universal nontrivial local density (all binary colorings, any n=2k).** Every physical cube vertex U of rank k+1 has exactly k+1 incident rank-k neighbors (delete one of its k+1 coordinates). The actual physical U-to-middle edge colors split these k+1 neighbors into two classes of sizes a and k+1−a. Every pair in one class gives a DISTINCT monochromatic 2-edge UPPER q-certified Johnson route, in the color of those two physical edges. Their total count is
  binom(a,2)+binom(k+1−a,2) >= floor(k²/4).
Likewise EVERY physical rank-(k−1) vertex L has exactly k+1 rank-k neighbors (add one unused coordinate), and supplies at least floor(k²/4) LOWER monochromatic two-edge Johnson routes. There are binom(2k,k+1)=binom(2k,k−1) hubs of each kind. Consequently the TOTAL number of distinct (route,J edge) certified incidences is at least
  2 binom(2k,k−1) floor(k²/4).
Each Johnson edge has exactly TWO physically different possible routes (one upper, one lower), and so the UNION J_0∪J_1 contains at least
  binom(2k,k−1) floor(k²/4)
DISTINCT Johnson edges, a fraction at least
  [2k/(k+1)] [floor(k²/4)/k²]
of all (1/2)binom(2k,k)k² Johnson edges. This approaches 1/2 as k→∞.

If the active antipodal-odd law c(bar e)=1+c(e) holds, the global involution S→S^c maps q-certified routes to (1−q)-certified routes (UPPER↔LOWER), hence |E(J_0)|=|E(J_1)|. The local density bound does NOT imply the existence of an antipodal or near-antipodal J_q geodesic with compatible endpoint caps: the remaining forcing problem is global, topological/combinatorial, and EXACTLY the desired even-dimensional center-belt closure statement.

**Research significance.** This supplies a completely physical, color-sensitive, two-state (q=0/1) Johnson-graph formulation of the UNRESTRICTED original antipodally odd EDGE problem restricted to the even-dimensional three-level belt. It preserves every two-edge route and both terminal cap bits; no false identification of different physical squares or paths is used. A global cohomological index/Hex or short-path-cover forcing statement for these forced dense antipodally interchanged Johnson carriers would prove a substantial belt theorem, and proving such a belt theorem in every even dimension would—by the already established dimension-lifting observation—solve the original edge-color conjecture in all dimensions.
