# Every direction order admits four antipodal roots whose full paths traverse only certified center squares

# Every coordinate order has >=4 fully center-square-certified antipodal rooted geodesics

Let n>=5, and let c be an ACTIVE NORI ordered-three-face coloring. Write X_c for the genuine certified-center square subcomplex: a physical square with free middle pair {b,c} lies in X_c iff some actual monochromatic centered four-edge geodesic with middle pair (b,c) or (c,b) certifies it. Write G=X_c^(1), the graph of physical cube edges incident with at least one certified center square.

INPUTS (already proved in the current NORI project):
(A) nori_certified_square_complex_connected_antipodal_one_class_20261008: at each vertex at most ONE coordinate direction is isolated from its link, hence G has minimum degree >=n−1; in active NORI every global direction occurs in a certified square somewhere.
(B) Each certified square includes BOTH of its parallel edges in each of its two middle directions. Hence any missing edge of G has absent middle direction in its links at both ends; since each vertex has at most one missing incident edge, the missing-edge set M=E(Q_n)\E(G) is a MATCHING.
(C) The centered shift graph on ordered triples through a FIXED hub z that contain a chosen middle direction i is connected and bipartite, with the bipartition defined by whether i is in the MIDDLE of the triple or at one of its ENDS; connectivity follows from the legal two-step outer-direction replacement walks in the proof of Theorem 2 of item (A), without the exterior-bit-flip moves.

**THEOREM 1 (no perfect missing-center matching).** The matching M cannot cover every cube vertex under active antipodal-reversal oddness. Consequently, because M is antipodally invariant with two-element edge orbits for n>=5,
  |M| <= 2^(n−1)−2.

**Proof.** Suppose M is perfect. For each vertex z let d(z) be the unique direction of its missing incident cube edge. Equivalently d(z) is the unique isolated coordinate in the link graph of certified center squares at z.

The LOCAL shift-graph connectivity fact (C) implies a rigid coloration around such a hub: there is a single bit t_z such that EVERY actual ordered triple face through z containing d(z) has color t_z if d(z) occurs in the MIDDLE position, and 1−t_z if d(z) occurs at an END. Indeed all legal shift edges joining the two position types must be BICHROMATIC (otherwise a square with d(z) as a middle direction would be certified), and a connected bipartite graph has exactly these two proper binary colorings.

Now take any physical cube edge zz' with z'=z xor e_j. Suppose d(z)=i and d(z')=k are different. Symmetry of the missing-edge set implies j is distinct from BOTH i and k: if j=i then zz' is missing at z, so d(z')=i also; if j=k then zz' is missing at z', so d(z)=k also. Thus i,j,k are three distinct directions. The ordered physical 3-faces through z and through z' with free set {i,j,k} are IDENTICAL, because j is free. Compare their two orders:
  (i,j,k): the i-rigidity at z (i END) assigns 1−t_z; the k-rigidity at z' (k END) assigns 1−t_z', forcing t_z=t_z'.
  (j,i,k): the i-rigidity at z (i MIDDLE) assigns t_z; the k-rigidity at z' (k END) assigns 1−t_z', forcing t_z=1−t_z'.
Contradiction. Therefore d(z)=d(z') on EVERY physical cube edge, and cube connectedness makes d constant: d(z)=i for all z. Then every i-parallel cube edge is absent from G, so there is no certified center square with i as a middle pair direction anywhere. This contradicts the unconditional active-NORI global-direction-certification theorem (A). Hence M is not perfect.

The matching has at most 2^(n−1) edges; strict inequality gives <=2^(n−1)−1. Active antipodal reversal preserves the certified square set, so it preserves M. Every physical cube edge has a DISTINCT antipodal partner for n>=3, so |M| is even. Consequently |M|<=2^(n−1)−2. QED.

**THEOREM 2 (every direction permutation admits FOUR fully certified starting roots).** Fix ANY permutation p of all n directions. For at least FOUR starting cube vertices x, the full antipodal directed geodesic P(x,p) has the property that ALL of its n physical cube edges lie in G, so every traversed edge belongs to some ACTUAL monochromatic centered four-geodesic square witness. These four roots include at least TWO antipodal root pairs.

**Proof.** Fix a physical cube edge e in direction i. Across all 2^n roots, the p-geodesic traverses e at the unique step where p flips direction i for EXACTLY two roots: all n−1 other root bits are fixed by e and the prefix-flip assignment, while the initial i-bit may be either endpoint of e. Therefore each missing edge in M disqualifies exactly two rooted p-geodesics. Union bound gives
  #{x: P(x,p) has ALL edges in G} >= 2^n−2|M| >=4.
Since M and G are antipodally invariant, complementing the root x maps a fully G-covered p-geodesic to another fully G-covered p-geodesic. Thus these qualifying roots occur in antipodal pairs, at least two. QED.

**Improvement over prior path-coverage result.** Item nori_every_fixed_order_four_fully_local_witness_covered_antipodal_roots_20261008 proved a similar four-root count for the LARGER edge union of all mono four-paths; its 'dead-edge' matching misses edges not traversed by any mono4 path. Here G is specifically the 1-skeleton of the true **center-certified TWO-DIMENSIONAL SQUARE carrier**. Every surviving full path is covered by actual monochromatic SQUARE witnesses, not merely arbitrary four-path traversals.

**Exact remaining obstacle.** The guaranteed square certificates may vary with each step, with incompatible direction orders or alternating colors. A sequence of physically adjacent squares does not necessarily lift to ONE monochromatic or one-switch directed antipodal geodesic. The theorem certifies a strong geometric skeleton for every prescribed order but does not prove the NORI grand conjecture.
