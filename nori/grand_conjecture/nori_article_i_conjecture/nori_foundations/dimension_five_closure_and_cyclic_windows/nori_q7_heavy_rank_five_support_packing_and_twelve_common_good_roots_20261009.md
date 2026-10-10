# Heavy Q7 five-supports form a six-edge intersecting family; any twelve share ≥4 good roots

# Heavy rank-five supports cannot have disjoint two-coordinate complements; twelve-way Q7 synchronization

Consider any legal antipodal-reversal-odd binary coloring of physical ordered 3faces of Q7. For a five-direction support B let E_B be its set of bad starting vertices, i.e. vertices from which EVERY rooted five-direction order on B has alternating three-window colors. A B-support is *heavy* if |E_B|>=10.

**LEMMA 1 (heavy supports must overlap in four directions).** If B,B' are two different heavy five-supports, then |B∩B'|=4. In particular any legal Q7 coloring has at most SIX distinct heavy five-supports.

**Proof.** Let D=[7]\B be the two exterior directions. NORI reversal sends a rooted B-path at x to the reversed B-path at a root with the SAME B-bits and BOTH D-bits complemented. The paired exterior five-faces have the same number of bad roots. By arbitrary Q5 bad-root classification, that number is one of 0,1,2,4. Hence
 |E_B|=2(t_0+t_1), where t_0,t_1∈{0,1,2,4}.
For |E_B|>=10, at least one antipodal PAIR of exterior five-faces has exactly four bad roots each. On this pair the full ordered-face coloring is the canonical H-square template and its complemented mate.

Suppose |B∩B'|=3. Write T=B∩B', P=B\T and Q=B'\T, each with |P|=|Q|=2. Pick the exterior Q-bits w from one four-bad-root pair of B, and pick exterior P-bits v and v+(1,1) from one four-bad-root pair of B'. In the B five-face with exterior Q=w, the canonical H-template has square axis A⊂B of size2. Choose an order t of the three common free directions T for which the template has slope zero in the exterior fixed B-coordinates: if |A∩T|=0 choose T-pattern CCC; if 1 choose CAC; if 2 choose ACA. The physical ordered T-face color is then independent of both P bits, hence equal for v and v+(1,1). But B' has canonical H in its exterior P-fiber v and the complementary H in the opposite P-fiber v+(1,1): by reversal-evenness of H, on the SAME ordered T-face (with Q fixed) these two colors are opposite. Contradiction.

Thus any two heavy supports have at least four common directions; distinct five-subsets of a seven-set meet in at most four directions. Equivalently, their complementary 2-subsets of [7] are PAIRWISE INTERSECTING. An intersecting family of two-element subsets has size at most six: if all pairs share a common vertex it is a star with at most six edges; otherwise three pairwise-intersecting edges without common vertex form a triangle, and no additional distinct edge meets all three. QED.

**THEOREM 2 (twelve-support common good roots).** For ANY twelve specified (possibly repeated) five-direction supports B_1,...,B_12 in a legal Q7 coloring, there are at least FOUR physical starting vertices x such that, for every i, some direction-distinct five-edge path starting at x and using B_i has at most ONE three-window color switch. If all the twelve supports are unsaturated (|E_B|<16), at least EIGHT such common good roots exist.

**Proof.** A support with |E_B|<10 has |E_B|<=8 by the exact possible counts; a heavy unsaturated support has |E_B|<=12; a saturated support has |E_B|=16. Among any twelve specified supports at most six are DISTINCT heavy supports, by Lemma 1. Repetitions of a support do not increase the union of its E_B sets, so first remove repetitions; hence in a maximal union count there are at most six heavy supports.

If none is saturated, the bad-root union has size at most
 6*12 + (12-6)*8 = 120,
so at least 128-120=8 roots are good for every support.

If k>=1 supports are saturated, the paired-support rigidity theorem establishes that ALL saturated E_B sets coincide: intersection-size three is impossible for them, and intersection-size four forces identical E_B via the exact 160-template gluing certificate. Thus the union of all saturated bad sets contributes only16 roots. With at most six heavy supports total, its total size is at most
 16 + (6-1)*12 + (12-6)*8 =124.
Therefore at least four roots are good simultaneously. QED.

**Remarks on stronger directions.** At least one complementary pair of exterior five-fibers is maximally bad for every heavy support. The direct ordered-triple slope-zero contradiction is a geometric disjointness mechanism that limits global packing of high-defect five-supports. This extends the ten-support theorem to twelve without requiring any classification of intermediate two-bad-root fiber colorings. Seven-dimensional grand closure still requires a path/order compatibility principle upgrading these simultaneous rank-five witnesses into a full seven-edge one-switch geodesic.
