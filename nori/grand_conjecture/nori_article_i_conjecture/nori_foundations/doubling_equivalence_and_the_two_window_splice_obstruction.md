# Doubling equivalence and the two-window splice obstruction

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

---

# Exact antipodal pairing of facet one-change geodesics

Let c be an antipodal-reversal-odd ordered-three-face coloring of Q_(n+1), and let H_0,H_1 be opposite n-facets normal to direction g. If a full n-edge geodesic P inside H_0 has direction order p=(p_1,...,p_n) and ordered-three-face color word w=(w_1,...,w_(n-2)), its antipodal reversal J(P) in H_1 has direction order rev(p) and color word
J(w)=(1-w_(n-2),...,1-w_1).
This is immediate from the defining NORI oddness involution, applied to each ordered face.

In particular, if w=0^r 1^s has one change then J(w)=0^s 1^r still has one change (the change orientation remains 0-to-1); likewise if w=1^r 0^s, the dual is 1^s 0^r. Hence antipodal face symmetry by itself preserves the number of changes; it does NOT turn a one-change facet geodesic into a monochromatic geodesic in the opposite facet.

EXACT ENDPOINT EXTENSION CRITERION. Suppose P has exactly one change and appending the as-yet-unused direction g produces a full (n+1)-edge geodesic P*g. Let beta be the color of its one new ordered-three-face window (p_(n-1),p_n,g), taken at the actual face. Then P*g is one-change if and only if beta=w_(n-2), the terminal old-window color. Otherwise it has exactly two changes. The antipodal reversal J(P*g), which begins with g and follows J(P), has exactly the same number of changes: its word is the reversed complement of (w,beta). Therefore passing to the antipodal partner duplicates this endpoint match/mismatch without resolving it.

This identifies a concrete induction invariant: seek one-change facet geodesics with *terminal extension compatibility* for at least one omitted direction g, or prove a witness-exchange operation forcing compatibility among candidate paths. Pairing a single path with its antipodal dual is insufficient. Any stronger argument must compare genuinely different facet geodesics, change their endpoints, or exploit additional face overlaps.

The result is elementary, requires no information about colorings outside the chosen path and its dual, and applies to any n>=4 for which two or more face windows occur.

---

SHARED-TAIL TERMINAL EXCHANGE. Let c be any binary ordered-three-face coloring of Q_(n+1). Fix an n-dimensional facet normal to g. Suppose P and P' are two full n-edge geodesics in the facet, each with exactly one color change. Assume they share the same final vertex y and the same ordered last two directions (a,b), and that their final three-face colors are different. Then one of P*g or P'*g is a full antipodal geodesic with at most one change. PROOF. The added last window in both extensions is the identical ordered three-face with free-direction order (a,b,g) and exterior bits prescribed by their common endpoint y. It therefore has one common color beta. Exactly one of the two old terminal colors equals beta, so appending g adds zero changes to that geodesic. QED. More generally it is enough that the extensions use the same final ordered three-face and the old terminal colors differ. This is an exact sufficient condition with no antipodal symmetry hypothesis. For NORI induction the open obligation is to create two such compatible one-change facet witnesses by exchanging directions or changing the path. Antipodal reversal preserves extension mismatch and does not itself create the needed pair.
