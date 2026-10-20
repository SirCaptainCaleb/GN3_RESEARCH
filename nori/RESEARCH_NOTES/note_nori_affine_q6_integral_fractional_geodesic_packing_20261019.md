# Affine Q6: integral vertex packing versus fractional and edge packing

- Stable ID: note_nori_affine_q6_integral_fractional_geodesic_packing_20261019
- Author: session_nori_r11913_4
- Primary home: subsection:obstruction_compatibility_and_a_programme_for_nori1_closure
- Labels: NORI1, paired-flat, Q6, vertex-disjoint, fractional-packing, edge-disjoint, square-switch, affine, method-obstruction
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11913_4
- Updated session: session_nori_r11913_4
- Disposition: none
- Successor: none

## Related references

- note:note_nori_disjoint_packing_square_stability_r11876

## Research note

# Affine Q6 separates integral vertex, fractional vertex, and edge geodesic packings

Work over F_2 with pair bits p_i=x_{2i}+x_{2i+1} and q_i=x_{2i}, i=0,1,2. Color direction 2i by f_i and direction 2i+1 by 1+f_i, where f_0=q_2, f_1=q_2, f_2=q_1. Each gate ignores its own pair and is antipodally odd. The coloring is undirected and has three red incident edges at every vertex.

Let P be its set of unoriented red full antipodal geodesics. Let nu_v denote maximum vertex-disjoint packing, nu_v^* the fractional packing with unit vertex capacities, and nu_e maximum edge-disjoint packing.

THEOREM. |P|=96, nu_v=4, nu_v^*=16/3, and nu_e=8.

VERTEX UPPER BOUND. Under a red pair-i step, p_i flips and q_i changes by 1+f_i. On the pair (q_1,q_2), moves of types 1 and 2 respectively toggle q_1 iff q_2=0 and toggle q_2 iff q_1=0. The state 11 is isolated. To end at the antipode, a red full path must begin in state 01 or 10 and end in the other; its subword on pair labels 1,2 is forced to be 1212 or 2121 respectively (check the six two-use words). Because q_0 changes once, its two pair-0 moves must occur once with q_2=0 and once with q_2=1. Consequently the state (q_1,q_2)=01 occurs along each full path as a single three-vertex segment: one step of pair 0 and one of pair 1, both changing p_0 or p_1 while q_0,p_2 remain fixed. Thus this segment comprises three vertices in one of four disjoint four-vertex blocks
B_{a,b}={(p,q):q_1=0,q_2=1,q_0=a,p_2=b}, a,b in F_2.
Any two three-element subsets of a block intersect. Therefore nu_v<=4.

FOUR DISJOINT WITNESSES. Encode x as sum_j 2^j x_j. The following red full geodesics have pairwise disjoint vertex sets:
(57,49,51,35,34,38,6);
(50,58,56,40,44,12,13);
(46,14,15,11,27,19,17);
(37,5,1,0,16,24,26).
Each traverses the six original directions once. Hence nu_v=4.

FRACTIONAL VALUE. For either successful starting (q_1,q_2) state, there are six allowed insertions of pair 0's two steps into the forced four-letter pair-1,2 word. There are 32 successful roots, giving 192 oriented and 96 unoriented red full geodesics. Every path meets U={(q_1,q_2)=01} in three vertices. Assigning weight 1/3 to each of the sixteen vertices in U is a fractional cover of cost 16/3, proving nu_v^*<=16/3. The coloring is invariant under translations of all p bits and under complementing q_0. These act transitively on each sixteen-vertex fixed-(q_1,q_2) sector. Counting the six insertions, the number of geodesics visiting any one vertex in sectors 00,10,01,11 is respectively 8,16,18,0. Weighting every one of the 96 geodesics by 1/18 is therefore a fractional packing of total weight 16/3.

EDGE PACKING. Within its block B_{a,b}, each full red path traverses two adjacent red edges, one of pair 0 and one of pair 1. Choose two opposite edges of the induced four-cycle in each of the four blocks; these eight edges meet all red full geodesics, proving nu_e<=8. Equality is witnessed by these eight pairwise edge-disjoint red full geodesics, again represented by vertex sequences:
(5,4,36,32,48,50,58);
(6,38,34,35,51,49,57);
(12,13,45,41,57,59,51);
(15,47,46,42,58,56,48);
(17,25,27,11,10,14,46);
(18,26,24,8,12,44,45);
(24,16,18,2,6,7,39);
(27,19,17,1,5,37,36).

SCOPE. A universal guarantee of five vertex-disjoint red full geodesics fails already for legal affine balanced paired-flat Q6 colorings. The known Q6 paired-square avoidance theorem still holds. This example retains edge packing eight and fractional vertex packing 16/3, so those stronger avenues are unaffected. It supplies no reduction for unrestricted NORI1 or the simple original-vertex boundary-tournament statement.
