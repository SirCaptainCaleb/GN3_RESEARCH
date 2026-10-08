# Ordered three-face doubling creates two uncontrolled splice windows

# What cube doubling does for ordered three-face colorings

Let b be an arbitrary binary coloring of ordered three-faces in Q_n. Form Q_(n+1)=Q_n x {0,1} with new direction g. On faces omitting g, define C((F,0),pi)=b(F,pi) and C((F,1),pi)=1-b(bar F,rev pi). On g-containing ordered faces choose colors in arbitrary complementary antipodal-reversal pairs. Then C(bar E,rev pi)=1-C(E,pi), so this is the exact ordered-three-face analogue of the antipodally odd doubled edge coloring. The naive formula C((F,1),pi)=1-b(F,pi) generally violates NORI oddness: reversal of the ordered triple is mandatory.

LEMMA (two new splice windows). Suppose b is reversal-blind, meaning b(F,rev pi)=b(F,pi). Let an antipodal full geodesic in the doubled cube start in the lower facet, cross g once, and have a monochromatic C-word of color q. Let its pre-g direction list be U and its post-g list V, with starting lower vertex x and crossing vertex y (in Q_n coordinates). Complement every Q_n vertex of its upper-facet suffix, giving a directed path from bar y to x in direction order V; concatenate the original lower prefix x to y in direction order U. The resulting Q_n path from bar y to y is a full antipodal geodesic with order (V,U). Every triple completely inside V has b-color 1-q; every triple completely inside U has b-color q. The only unprescribed triples are the two windows straddling the V|U splice (or fewer when one block is short). Thus the decoded b-word has the form (1-q,...,1-q, z_1,z_2,q,...,q) and may have THREE color changes. When both long constant flanks exist it has at most one change exactly when (z_1,z_2) is NOT (q,1-q). The forbidden pair creates (1-q,q,1-q,q) with three changes.

For a general ordered b without reversal-blindness, an additional obstruction arises: the upper-facet induced color at order pi is 1-b(bar F,rev pi), whereas the decoded upper suffix requires b(bar F,pi). Thus the doubled monochromatic path need not even control its decoded suffix colors. Ordered-face reversal and the two splice windows are independent obstructions to the straightforward Feder-Subi/Norine equivalence argument.

SHARP EXAMPLE (dimension six). Partition six directions into marked m1,m2 and unmarked a1,a2,a3,a4. Define the reversal-even, position-independent coloring
b(F,(u,v,w))=1 iff v is unmarked and at least one of u,w is marked; otherwise b=0.
For every six-direction order its four b-window colors have at least two changes. Indeed if marker positions are i<j, then the color of the triple centered at position t (t=2,3,4,5) is (1-z_t)(z_(t-1) OR z_(t+1)), where z_s indicates a marked position. Up to reversing the six positions, the nine marker pairs and their four-bit words are
(1,2):0100; (1,3):1010; (1,4):1101; (1,5):1010; (1,6):1001; (2,3):0010; (2,4):0101; (2,5):0110; (3,4):1001.
Each has at least two changes.

Make the doubled C on Q_7 using the formula above; since b is reversal-even and position-independent, C=b in the lower facet and C=1-b in the upper facet. Consider the seven-direction order
(m1,a1,a2,g,a3,m2,a4)
from any chosen initial vertex with g-bit zero. Its first window (m1,a1,a2) is in the lower facet and has C-color 1. Its last window (a3,m2,a4) is in the upper facet and has C-color 1. Prescribe color 1 on the three intervening ordered faces with free triples (a1,a2,g), (a2,g,a3), (g,a3,m2) reached by the path, and color 0 on their antipodal reversals. These six ordered-face objects are pairwise distinct; complete all other g-face reversal pairs arbitrarily. This constructs a legitimate NORI-odd C with a MONOCHROMATIC seven-edge antipodal geodesic.

But its decoded Q_6 direction order is (a3,m2,a4,m1,a1,a2), with b-word (0,1,0,1), realizing all three changes. In fact no Q_6 full geodesic is one-change for b, by the marker-pair argument. Therefore a monochromatic doubled NORI geodesic does NOT imply an unrestricted one-change geodesic downstairs. The elementary doubling proof of the edge-color equivalence fails sharply for ordered three-face colors.

SCOPE. The example refutes the putative implication for this doubled coloring, and the unrestricted spanning one-change three-face statement is already false in Q_6. It does not settle whether every NORI-odd three-face coloring has a monochromatic antipodal geodesic. The all-dimensional NORI one-change conjecture remains separate.
