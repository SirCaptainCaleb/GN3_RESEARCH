# Exact all-window antipodal shift-graph distance and stronger universal monochromatic connector density

# Exact shortest antipodal path in the physical middle-direction window-shift graph

Let n>=5, choose a distinguished cube coordinate i, and let H_i be the actual physical ordered-three-face window-shift graph: vertices are all actual ordered three-faces containing i; edges join consecutive windows of an actual physical 4-edge geodesic with i among the TWO overlapping middle directions. The direction order of any edge is (a,b,c,d) with i in {b,c}. The physical antipodal reversal is tau(F,(a,b,c))=(bar F,(c,b,a)); it exchanges colors under active NORI oddness, though the graph-distance statement requires NO COLORING. Let
  L(n) := max{ 6, 2 ceil((n-1)/2) }.
Then L(5)=6, L(6)=6, L(7)=6, L(8)=8, L(9)=8, L(10)=10, etc.

**THEOREM (EXACT ANTIPODAL WINDOW DISTANCE).** For EVERY actual window v of H_i (all three positions of i),
  d_H_i(v,tau v) = L(n).
In particular, physical root/face transport from a middle-i window to its reversed antipode requires only O(n) exact local shifts, and the optimal coefficient in its path length is asymptotically ONE.

**Proof, reduction and local realization.** Cube-bit translations and direction permutations fixing i are automorphisms of H_i, commuting with tau and transitive on windows with i in the MIDDLE position. We may therefore take i=0, initial v=(1,0,2) with all fixed exterior bits zero, and target tau v=(2,0,1) with all fixed exterior bits one. The graph H_i is bipartite between windows with i in their middle position and windows with i in an outer position. Along a consecutive shift, precisely one free direction leaves the ordered triple and one distinct new direction enters. Each adjacent pair of proposed ordered triples having the literal shift overlap (last two of one equal first two of next, or reversed) and FOUR distinct directions can be realized by actual physical faces if their fixed outside bits agree on all coordinates fixed in BOTH faces.

The constructive sequences below have an explicit global compatible choice of faces: start with all exterior bits zero; when an outside direction k>=3 enters a free triple for its FIRST time, keep its fixed bit zero until its entry, and on its LAST exit assign its outside bit one. Between consecutive windows keep all common exterior fixed bits unchanged. Original coordinates 1,2 may have arbitrary fixed bits while temporarily outside the triple, since they are free at both endpoints. At a repeated exterior visit (n=6), retain its previously set outside bit one. Thus every consecutive pair has matching common outside bits and is realized by a genuine centered ordered 4-edge cube geodesic; the final window has all exterior bits one.

**Construction for odd n>=7:** Use the literal ordered-triple sequence
  (1,0,2), (3,1,0), (1,0,4), (5,1,0), (1,0,6), (7,1,0), ..., (1,0,n-3),
followed by FOUR more windows
  (0,n-3,n-2), (2,0,n-3), (n-1,2,0), (2,0,1).
The initial alternating chain has n-5 edges, ending with (1,0,n-3), followed by four. Total L=n-1. Every exterior coordinate 3,...,n-1 appears free and is later retired to outside value one.

**Construction for even n>=8:** Use
  (1,0,2), (3,1,0), (1,0,2), (4,1,0), (1,0,5), (6,1,0), (1,0,7), ... , (1,0,n-3),
followed by the SAME four-window suffix
  (0,n-3,n-2), (2,0,n-3), (n-1,2,0), (2,0,1).
The first three windows return to the SAME ORDERED TRIPLE (1,0,2), now on a DIFFERENT actual physical face with exterior coordinate 3 toggled through its free occurrence in (3,1,0). Subsequent alternating shifts introduce directions 4,...,n-3 one at a time. The initial chain has n-4 edges, followed by four, for L=n. All outside bits are finally complemented.

**Construction for n=6:** The six-edge sequence
  (1,0,2), (3,1,0), (1,0,4), (0,4,3), (2,0,4), (5,2,0), (2,0,1)
has all actual consecutive physical comparisons. The exterior coordinate 3 is temporarily free a second time after already being toggled, and retains bit one upon its last exit. Coordinates 4 and 5 are toggled likewise.

**Construction for n=5:** The six-edge sequence
  (1,0,2), (0,2,3), (4,0,2), (3,4,0), (4,0,1), (0,1,3), (2,0,1)
has i in the genuine overlap-middle pair of every edge. Assign fixed exterior bits 3 and 4 to one after their last free occurrences, obtaining the target tau v.

**Lower bound.** Each actual initially exterior coordinate k outside {a,i,b} must change from its original fixed bit to its complementary final fixed bit, so it must become FREE in an intermediate window. Since a shift introduces at most one new free coordinate, this costs at least n-3 distinct new entries. Moreover the ordered left and right outer coordinates a and b MUST each leave the triple and re-enter before they can occupy the opposite outer position. To see this, observe that every pair of consecutive two-step transitions between middle-i windows has form
  (A,i,B) -- (i,B,k) -- (D,i,B)
or
  (A,i,B) -- (k,A,i) -- (A,i,D):
exactly ONE outer position is replaced, the other is retained in its original slot. The roles of a and b cannot cross while both are present, so each must depart and later re-enter. Their two required reentries are distinct from the n-3 first-time entries of original exterior coordinates. Therefore every H_i path from v to tau v has at least (n-3)+2=n-1 edges. It also has EVEN length because i is middle at both endpoints and every H_i edge toggles the middle-vs-end position of i.

Finally at least THREE two-step replacements are needed to exchange the ordered outer pair (a,b): a temporary third outer coordinate is required, then one original direction is reintroduced, then the other is reintroduced. Hence every such path has length >=6. Combining yields L>=max{6,2ceil((n-1)/2)}. The explicit constructions attain this bound. QED.

**COROLLARY (SHARPENED PHYSICAL CONNECTOR DENSITY).** Assume active binary NORI oddness. For each fixed coordinate i, let N_i count DISTINCT monochromatic physical ordered-window shift edges of H_i. The edges form two transitive orbits under cube translations and coordinate permutations fixing i, with
 E0=2^(n-2)(n-1)(n-2)(n-3)
edges in EACH orbit, according to whether i occupies the first or second middle slot. Antipodal reversal exchanges the two orbits and complements both window colors, giving equal good-edge counts N_L=N_R. Every group translate gP of an EVEN length-L(n) path from v to tau v has endpoint colors OPPOSITE, so its edge color word cannot alternate everywhere: it includes at least one good edge. Uniform orbit averaging therefore gives
  1<=L(n)*N_L/E0
and hence the STRONG numerical bound
  N_i >= 2 ceil(2^(n-2)(n-1)(n-2)(n-3)/L(n)).
Examples: n=5 gives N_i>=64, n=6 gives N_i>=320, n=7 gives N_i>=1280, n=8 gives N_i>=3360. This improves the preceding bounds based on length 4n-6 and length 2n root shuttles. No proof of universal optimality of the resulting COUNT bound is claimed, only of the transport distance L(n).

**Global relation and precise unsolved forcing step.** The construction is an EXPLICIT certified cross-root chart system with optimal antipodal transport length and mandatory monochromatic connectors. It fixes the position and origin of the required physical root changes. It does not force good edges chosen along different translated paths to share a root, a monochromatic run, or reversed terminal two-coordinate memory. To close the grand conjecture one must glue the selected edges/triangles through actual joint geodesic certificates, forcing complementary-support overlap R_(a,b)(x) with R_(b,a)(x) at ONE x, or derive a strict descent in the full-geodesic switch count. The index-one certified-square example remains a guardrail against inferring higher cohomological index from abundance alone.

## Elevation: the same exact distance holds for EVERY window, including outer-i positions

The proof above dealt with i in the middle position. Here is an explicit extension to windows with i in an OUTER position. It strengthens the theorem to ALL physical vertices of H_i:
  d_H_i(v,tau v) = L(n) = max{6,2ceil((n-1)/2)}
for EVERY v.

Normalize by coordinate permutations and cube-bit translations to i=0, initial ordered triple v=(0,1,2), all exterior fixed bits zero, and reversed antipode tau v=(2,1,0) with all exterior bits one. The following sequences contain only genuine consecutive shifts with 0 in their overlap middle pair:

- ODD n>=7: Begin (0,1,2),(3,0,1), then the alternating entries (4,3,0),(3,0,5),(6,3,0),(3,0,7),... ending at (3,0,n-2). Append (0,n-2,n-1),(1,0,n-2),(2,1,0). Total edges n-1.

- EVEN n>=6: Begin (0,1,2),(3,0,1),(2,3,0), then the alternating entries (3,0,4),(5,3,0),(3,0,6),(7,3,0),(3,0,8),... ending at (3,0,n-2). Append (0,n-2,n-1),(1,0,n-2),(2,1,0). Total edges n. The early free-coordinate revisit of 2 permits the required parity.

- n=5: Use (0,1,2),(3,0,1),(2,3,0),(3,0,4),(0,4,2),(1,0,4),(2,1,0), length six.

In every sequence use the SAME EXPLICIT PHYSICAL FACE REALIZATION rule as above: assign each initially exterior coordinate k>=3 fixed bit zero before its first free occurrence and one after its final exit; if it enters again, retain bit one at the later exterior positions. Assign temporary exterior bits of original coordinates 1,2 arbitrarily because they are free at both endpoints. Each consecutive pair shares all common fixed exterior bits and has an exact four-distinct-direction overlap with 0 in the middle pair. Consequently all steps are genuine physical window shifts; the last ordered window is exactly tau of the first.

For the UNIFORM LOWER BOUND, one may avoid the middle-vertex replacement calculation. For ANY adjacent physical windows, the relative ordering of any two directions which are free in BOTH windows is preserved: the common free directions occupy the SAME relative order in the underlying four-distinct-direction word, read in either orientation. In particular, the relative order of i with any coordinate which never leaves the free triple is invariant along the path. But reversing the initial ordered triple reverses the relative orders (i,a) and (i,b) for the two other initial directions a,b. Hence BOTH a and b must leave and later REENTER the free triple. Every initially exterior direction k must become free somewhere to change its fixed bit under antipodality. This forces at least (n-3)+2=n-1 distinct new-entry steps. Both v and tau v lie in the SAME bipartition class of H_i (whether i is middle or outer), so the path length is even.

The six-step floor also holds for outer-i starts. For v=(i,a,b) a two-step sector walk ending again with i in an outer position has exactly two possible ordered-type patterns: either (i,a,d), retaining middle direction a while i stays first, or (e,d,i), with a NEW middle direction d outside the original triple and i now last. A further two-step walk to the target (b,a,i) is impossible in the first case: any two-step first-i to last-i walk introduces a new middle direction different from the prior a. It is impossible in the second case: any two-step last-i to last-i walk RETAINS its current middle direction d, different from desired a. Thus there is no length-four path from (i,a,b) to (b,a,i). By antipodal reversal, the same holds for a last-i starting window. The middle-i case was handled in the main proof. Hence every such path has length >=6. This completes the full all-window exact-distance theorem.

**Additional applicability.** Every NORI sector vertex, whether i is the first, middle, or last free direction, now admits an optimally short even actual window-shift route to its reversed antipode. On EVERY such route the antipodally odd face colors force an ODD number of genuine monochromatic connector edges. The earlier connector density estimate needs only the middle-i orbit; the extension supplies equally short topological root transport throughout the entire connected sector graph H_i. The global terminal-memory compatibility gap remains unchanged.

## Exact equivariant systole and the new short-annulus target

Let B_i=H_i/tau, where tau is the free physical antipodal reversal on the sector graph, and let w_i in H^1(B_i;F_2) be the classifying class of the connected two-sheeted cover H_i->B_i. Define the w_i-systole to be the smallest number of edges in a closed B_i-walk on which w_i evaluates to one. Any such closed walk lifts to an actual physical H_i-walk from some vertex v to tau v, and conversely any such path projects to a w_i-odd loop. Therefore the preceding ALL-WINDOW distance theorem proves the exact identity
  sys(B_i,w_i) = L(n) = max{6,2ceil((n-1)/2)}.
This is a genuinely color-independent topological measurement of antipodal root/face transport.

For an active NORI coloring, the phase g_i(u)=c(u)+s_i(u), where s_i marks middle position of i, is tau-odd; its edge coboundary is EXACTLY the indicator of monochromatic physical four-window connectors. The induced quotient-edge cocycle of those good edges represents w_i (see Item nori_equivariant_coordinate_sector_cut_atlas_exact_gluing_and_switch_energy_20261009). Thus every shortest w_i-odd loop is a L(n)-edge ACTUAL physical connector-chain with an ODD number of monochromatic edges. This is a colored short-loop certificate of the cover class.

By contrast, the physical five-window cyclic pentagon in the FULL window-shift graph H projects to a loop with temporal parity beta=1 and antipodal voltage w=0, whereas a shortest sector w_i-loop has temporal parity beta=0 because it is even and its sector is bipartite. These give two canonical, length-controlled independent directions of first-degree holonomy inside the good-window complex W_good and its quotient.

**Precise next construction:** For a given short w_i-loop P of length L(n), seek a certificate-preserving homotopy transporting one actual centered physical pentagon (beta=1,w=0) around P via genuine good-window triangles, with all local two-window incidence and root-bit constraints checked. Such a transport would produce the certified pentagon annulus needed for a mixed beta*w class in the higher-dimensional good-window carrier. A priori existence of this annulus remains UNPROVED; the point is that the antipodal-transport side now admits a CANONICAL O(n)-length optimal path at every actual window, so the remaining obstruction is precisely the compatibility of its transported pentagon triangles. This is the stage at which genuinely higher-dimensional root/terminal-memory information must enter; first-degree parity alone has been exhausted.
