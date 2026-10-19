# Walk-pumping collapse and shortest-path blue cut forcing

- Stable ID: note_nori_xvi_walk_pumping_shortest_repair_20261018
- Author: Independent NORI1 mathematician
- Primary home: subsection:obstruction_compatibility_and_a_programme_for_nori1_closure
- Labels: NORI1, walk-pumping, shortest-path, Gibbs
- Lifecycle: active
- Epistemic status: proved
- Current version: 3
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11531_1
- Updated session: session_nori_r11531_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

WALK-PUMPING COLLAPSE AND SHORTEST-PATH REPAIR. Let A0(c) be red-antipodally connected roots and D0(c) the minimum blue-edge count of a full geodesic rooted in A0. All orders pi from any x in A0 occur as roundings of some red antipodal walk: prepend closed red excursions A_i,i,i,reverse(A_i) in pi order, taking A_i to a red i-edge of a given red antipodal path. Replacing designated red edges with 2M+1 consecutive red traversals makes independent uniform odd-ordinal sampling round to pi with probability tending to one. Thus the intrinsic uniform-odd Gibbs energy, and all hybrid or causal-coupled energies that contain this policy, equal D0(c) for EVERY beta>0. The original within-walk theorems remain valid, but unrestricted-WALK minimization adds no global forcing. REPAIR: Restrict Gibbs energy S_beta to globally shortest red antipodal paths. Product shortest paths project to shortest factor paths, and all interleavings of shortest factor paths are product shortest; the earlier pathwise Gibbs tensor law therefore proves S_beta(c box d)=S_beta(c)+S_beta(d). The uniform o(n) bound needed for NORI1 is OPEN. SHORT-PATH FLUX: Between consecutive occurrences of a repeated direction j in ANY shortest red path, at least one intervening red edge changes color under translation by e_j. Otherwise remove both j steps and shift the intervening strip, contradicting shortestness. If m_i counts occurrences, m_j-1 <= sum_{i influenced by j}m_i, and the total active time-derivative witness count on a shortest red antipodal path is at least length(P)-n. On a flat-curvature strip the flux is even, hence at least two. Proof and independent testing: /mnt/data/nori_xvi_walk_pumping_collapse_and_shortest_path_repair.md and /mnt/data/nori_xvi_walk_pumping_verify.py, /mnt/data/nori_xvi_walk_pumping_random_verify.py, /mnt/data/nori_xvi_shortest_path_flux_verify.py. 245 legal colorings tested for root-order pumping; 3488 repeated-direction gaps on 6427 legal-coloring red shortest paths verified. NORI1 remains open.

STRONGER PARALLEL-FACE CUT THEOREM. In a shortest red path, let two consecutive j-moves bound a red segment S: a ->(j) a+e_j ->S b+e_j ->(j) b. Subpath optimality gives d_red(a,b)=|S|+2 and d_red(a+e_j,b+e_j)=|S|. Write r=Hamming(a,b)>=1. Every monotone full geodesic from a to b inside the r-face F=[a,b] must encounter blue, as its length r<=|S| is shorter than red distance |S|+2. The red-reachable set U from a in the directed monotone face excludes b and has a wholly blue directed outward edge cut. This cut has at least r edges: r cyclic rotations of the r distinct directions give r edge-disjoint monotone full geodesics, each crossing the cut. This is a shared-face edge constraint, not just a derivative of one chosen strip. This theorem holds for arbitrary two-colorings; no global incompatibility result yet. Independent verifier /mnt/data/nori_xvi_shortest_path_face_cut_verify.py checked all 3488 repeated-direction gaps; blue-cut lower bound attained in 2268 finite instances. Detailed manuscript /mnt/data/nori_xvi_walk_pumping_collapse_and_shortest_path_repair.md.
