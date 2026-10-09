# Static path-nerve index limits and five-block root repairs

# Static path-nerve index limits and five-block root repairs

Take the static two-sided witness nerve defined by simultaneous compatibility of literal root/support boxes. Short paths may form connected antipodal pieces, while long paths can become isolated once their supported root fibers separate. This yields a sharp index limitation for the static carrier and focuses attention on root slides and adjacent direction exchanges that change the physical boxes.

## PHYSICAL ROOT MOBILITY IS MATHEMATICALLY NECESSARY: NO SAME-ROOT OPPOSITE-SHORE BOX CONTACT ABOVE DIMENSION SIX

Retain the genuine two-sided physical root-box carrier of
nori_two_sided_root_sheet_helly_equivariant_exact_grand_fixedpoint_index_four_ceiling_20261008,
and the exact pairwise box edge test of
nori_two_sided_box_exact_root_support_edge_test_high_index_packet_graph_selection_20261008.

Let r>=2, n>2r, and let P,Q be ACTUAL admitted <=1-switch directed geodesic PATH STATES for a binary physical ordered-r-face coloring, with SAME starting root x∈Q_n. Their lengths k_P,k_Q are at least r and at most n; their used sets W_P,W_Q, unused D_P,D_Q, and common r-window free-coordinate sets M_P,M_Q are as usual, with
  |D_P|=n−k_P, |M_P|=max(2r−k_P,0)
and likewise Q. Physical antipodal complement+path reversal maps P to ΘP whose new root is x XOR D_P, and whose exact root sheet has the same middle free-coordinate set M_P.

**THEOREM 1 (EXACT cross-shore same-root criterion).** The two boxes B(P) and B(ΘQ) have a common actual source-target root pair if and ONLY if
  D_Q ⊆ M_P
AND
  D_P ⊆ M_Q.
This is an exact physical-face criterion, independent of ordered face colors once P,Q have been admitted.

PROOF. The source factor of B(P) is S(P)=x+span M_P, and that of B(ΘQ) is S(ΘQ)=(x XOR D_Q)+span M_Q. Their intersection is nonempty precisely when D_Q⊆M_P∪M_Q; since unused D_Q is disjoint from its own used M_Q, this means D_Q⊆M_P. The target factor of B(P) is S(ΘP)=(x XOR D_P)+span M_P and that of B(ΘQ) is S(Q)=x+span M_Q. Their intersection is nonempty precisely when D_P⊆M_P∪M_Q; since D_P∩M_P=empty, this is equivalent to D_P⊆M_Q. Both factors must intersect, proving the equivalence. QED.

**THEOREM 2 (NO SAME-ROOT MIXED CONTACT IN n>2r EXCEPT FULL GRAND WITNESSES).** If n>2r and B(P)∩B(ΘQ) is nonempty, then BOTH P and Q must be FULL n-edge geodesics. Consequently, under hypothetical GRAND FAILURE, there is NO opposite-shore mixed box edge of this form at any common physical root.

PROOF. If P is full then D_P=empty, and because n>2r its middle common set M_P=empty. Theorem1 forces D_Q=empty, so Q is full also. Similarly with P,Q exchanged.

Now suppose both P,Q are incomplete. By Theorem1,
  n−k_P=|D_P| <= |M_Q|<=max(2r−k_Q,0),
  n−k_Q=|D_Q| <= |M_P|<=max(2r−k_P,0).
Since both left sides are POSITIVE, both right sides are positive, so k_P,k_Q<2r and the maxima can be dropped. Adding gives
  (n−k_P)+(n−k_Q) <= (2r−k_Q)+(2r−k_P),
i.e. n<=2r, contradicting n>2r. QED.

**NORI SPECIALIZATION (r=3).** In EVERY dimension n>=7, suppose P,Q are genuine <=1-switch partial geodesics from the SAME physical cube root x. Then their two-sided product boxes B(P),B(ΘQ) CAN meet only if P,Q are ALREADY full good antipodal geodesics. In particular, among the universal single-window monochromatic THREE-EDGE paths at one root, the full 'positive' clique and its reflected negative clique have NO cross edge in the two-sided Helly nerve. Merely taking all local path branches from ONE physical root and their Θ-images can never provide the mixed-face topology required for grand closure in n>=7.

**CROSS-ROOT TRANSPORT IS REQUIRED.** If P is rooted at x and Q at y (possibly distinct), the exact general cross-shore box compatibility test is
   supp(x XOR y XOR D_Q) ⊆ M_P∪M_Q,
   supp(x XOR y XOR D_P) ⊆ M_P∪M_Q.
Equivalently the ROOT DISPLACEMENT mask x XOR y must agree with BOTH unused support masks D_P and D_Q OUTSIDE the tiny union M_P∪M_Q. In particular, if k_P,k_Q>=6 for ordered three-face NORI, then both middle common sets are empty, so compatibility requires
  x XOR y = D_P = D_Q.
This is a genuinely large, support-dependent PHYSICAL root shift, not a local root slide.

**TOPOLOGICAL INTERPRETATION.** The high-index global program cannot be carried by sign-complementing LOCAL witnesses at one fixed root. Equivariant mixed-carrier faces beyond the universal low-rank skeleton necessarily use different physical roots with exterior differences synchronized to the UNUSED direction masks. This is an exact local-to-global obstruction in the honest double Helly nerve, and explains why a high-dimensional Tucker proof must incorporate root transport/path order exchanges INSIDE its topological framework. It does NOT prove that such transport always exists and does not close the unrestricted NORI grand conjecture.

## Moving-seam cubical transport through central permutohedral adjacent swaps: both genuine face objects preserved by the crossing swap

Let n>=6 and let c be ANY binary coloring of physical ordered three-faces on Q_n. Take a full rooted cube-geodesic direction order p=(p1,...,pn), choose any cut rank ell with 2<=ell<=n−2, and denote four consecutive direction names
  c0=p_(ell−1), a=p_ell, b=p_(ell+1), d=p_(ell+2),
which are pairwise distinct. Let S be the first ell used directions and y=x XOR S the true physical cut vertex of the path from root x. Its TWO actual crossing three-face window objects are
  L=(F(y;{c0,a,b}),(c0,a,b)),
  R=(F(y;{a,b,d}),(a,b,d)).
The two underlying physical faces are flat across the root square spanned by a,b.

**THEOREM 1 (cross-cut central transposition preserves BOTH physical seam face objects).** Let p' be obtained from p by interchanging only the adjacent positions ell,ell+1, replacing (c0,a | b,d) by (c0,b | a,d). The NEW used prefix set is S'=S symmetric-difference {a,b}, so the new cut vertex is y'=y XOR a XOR b, the OPPOSITE corner of the physical seam square. Its two crossing ordered face windows are
  L'=(F(y';{c0,b,a}),(c0,b,a)),
  R'=(F(y';{b,a,d}),(b,a,d)).
Since a,b are free directions of BOTH old physical faces,
  F(y';{c0,a,b})=F(y;{c0,a,b}),
  F(y';{a,b,d})=F(y;{a,b,d}).
Thus the old/new pairs L,L' are DIFFERENT ORIENTATIONS of exactly the SAME actual physical three-face, and likewise R,R' are different orientations of exactly the SAME actual second physical three-face. The four actual seam-window colors are
  c(F_L,(c0,a,b)), c(F_L,(c0,b,a)),
  c(F_R,(a,b,d)),  c(F_R,(b,a,d)),
with two fixed physical faces F_L,F_R. Every one of these four values remains unchanged when the STARTING ROOT is independently flipped in a, b, or both. This gives a literal 2-by-4 physically grounded seam-color table, unlike an interpolated Tucker label.

**THEOREM 2 (adjacent moves on either side transport one physical seam face).**
(a) Swap the two last directions of the prefix, positions ell−1,ell: (c0,a | b,d) becomes (a,c0 | b,d). The cut USED support S and physical cut vertex y do not change. The new LEFT crossing window has triple (a,c0,b) and uses the SAME underlying physical face F_L=F(y;{c0,a,b}), while the new RIGHT window has triple (c0,b,d) on a generally different physical face. The seam-square axes change from {a,b} to {c0,b}, two squares sharing direction b.
(b) Swap the first two suffix directions, positions ell+1,ell+2: (c0,a | b,d) becomes (c0,a | d,b). The cut support and y again do not change. The new RIGHT crossing window has triple (a,d,b) on the SAME underlying physical face F_R=F(y;{a,b,d}), while the new LEFT window has triple (c0,a,d) on a generally different face. The seam-square axes change from {a,b} to {a,d}, two squares sharing direction a.

**PROOF.** For Theorem1 the transposition crosses the cut, so S' replaces a by b, changing the cut vertex by a XOR b. Each crossing face's free triple includes both a and b, so changing the reference vertex y on those two coordinates leaves the physical face literally unchanged. The ordered triples transform exactly as stated. Flipping starting root in any subset of {a,b} changes the cut vertex only on the same free directions, establishing the four-root square invariance. For Theorem2 the transpositions lie wholly inside S or its complement, so the cut endpoint y is unchanged. The left seam free 3-set {c0,a,b} is unchanged by the left transposition, and the right free set {a,b,d} is unchanged by the right transposition, whereas the other seam free set generally changes. The resulting direction words determine the displayed orientations. QED.

**PHYSICAL ORDER-EXCHANGE FRAMEWORK.** These three elementary adjacent permutation moves give genuine transport rules for a root-coupled moving seam-square label:
- crossing swap: the physical root cut moves by a XOR b, the pair {a,b} stays fixed, and BOTH physical seam faces are preserved;
- left-neighbor swap: cut root fixed, seam pair changes {a,b}->{c0,b}, LEFT physical face preserved;
- right-neighbor swap: cut root fixed, seam pair changes {a,b}->{a,d}, RIGHT physical face preserved.

The central root-square label pair {a,b} cannot be fixed globally without killing antipodal index, by Item nori_fixed_pair_separating_permutohedron_facets_antipodal_index_zero_square_alignment_nogo_20261008. The present theorem identifies the precise COLOR-INDEPENDENT GEOMETRIC transport operations for a MOVING pair, requiring only genuine physical faces and adjacent-coordinate exchanges. Color memory remains attached to these actual ordered faces. These operations are promising 1-cells for an enriched equivariant root-square / permutohedral repair complex.

**LIMITATION.** The active NORI antipodal-reversal law relates colors on antipodal faces with reversed entire direction triples; it does NOT relate two different orders of the SAME physical face. Thus the four crossing-swap seam bits above can be arbitrarily assigned locally, and none of the three elementary moves is automatically defect-decreasing. The missing forcing step is a parity/holonomy or fixed-point principle applied to the WHOLE system of these actual ordered-face transport moves, using all-root antipodal compatibility and genuine path-window color incidence. This theorem is a rigorous geometric toolkit item, NOT an unrestricted grand proof.

## COMPLETE 30-bit classification of a five-direction chart in which ALL 120 anchored permutations have two changes, with arbitrary opposite central colors

Fix a physical cube Q_n, n>=5, an ordered FIVE-element coordinate subset B, and a specific starting physical cube vertex r of a five-coordinate B-face (all coordinates outside B fixed). Consider the 120 genuine five-edge cube geodesics rooted at r that traverse EACH direction in B exactly once, with direction order (a,b,c,d,e) a permutation of B. These paths have three ordered-three-face windows, hence color words of length three. For a binary ordered-PHYSICAL-three-face coloring, 'bad relative to the one-switch target' for an anchored length-five path means its three window colors have EXACTLY TWO switches, i.e. (q,1-q,q).

Define the ACTUAL local ordered-face colors by their physical exterior-B bit layers relative to the anchored root r:
- F_0(a,b,c): actual face with free ordered triple (a,b,c), both remaining B exterior coordinates d,e still at root r values (zero of them flipped);
- F_1(b,c,d;a): actual face with free ordered triple (b,c,d), outside it a already flipped relative to r and e unflipped;
- F_2(c,d,e): actual face with free ordered triple (c,d,e), outside it both remaining B directions a,b flipped relative to r.
All exterior coordinates outside B are fixed by the ambient anchored five-face. These are genuine, distinct physical face objects at the indicated layers, and their colors need not be affine or coordinate-only. For each five-order (a,b,c,d,e), its actual color word is
  (F_0(a,b,c), F_1(b,c,d;a), F_2(c,d,e)).

**THEOREM 1 (complete classification, NECESSARY AND SUFFICIENT).**
Every one of the 120 anchored five-orders has exactly two changes IF AND ONLY IF there is a uniquely determined family of 30 arbitrary binary parameters
  t(c,A) ∈ F2,
indexed by the choice of a MIDDLE DIRECTION c∈B and an UNORDERED two-element set A⊂B\{c}, such that, for EVERY ordered list of distinct directions a,b,c,d,e exhausting B,
  F_0(a,b,c)    = t(c,{a,b}),
  F_1(b,c,d;a) = 1−t(c,{a,b}),
  F_2(c,d,e)   = t(c,{a,b})
                    = t(c, B\{c,d,e}).
The 30 parameters are independent. The number of possible assignments to all local ordered-physical-three-face objects of the anchored five-face satisfying this property is EXACTLY 2^30.

**Proof.** If all 120 length-five paths are two-switch, every ordered permutation satisfies
  F_0(a,b,c)=F_2(c,d,e)=1−F_1(b,c,d;a).
Fix c and a,b,d,e distinct in B\{c}. Swapping d,e while keeping (a,b,c) fixed shows F_2(c,d,e)=F_2(c,e,d). Swapping a,b while keeping (c,d,e) fixed shows F_0(a,b,c)=F_0(b,a,c). Therefore F_0(a,b,c) depends only on c and the UNORDERED set A={a,b}; call its bit t(c,A). Then every F_2(c,d,e) is forced to the value t(c,B\{c,d,e}) and every mixed-layer central F_1(b,c,d;a) is forced to 1−t(c,{a,b}). Conversely these formulas make every full 5-path word exactly (t,1−t,t), hence two-switch. The 30 parameters are uniquely read from the 5*choose(4,2)=30 independent first-layer ordered-face color classes. Every ordered physical three-face supported on B has exactly TWO exterior B directions, in one of the four exterior states 00,10,01,11; it appears in precisely one of the layer categories F_0,F_1,F_2 above as its ordered triple and exterior state vary, so there are NO hidden consistency conditions. QED.

**THEOREM 2 (opposite central colors coexist with universal local failure).** Let L:B→F2 be ANY nonconstant binary function and specialize t(c,A)=L(c) for all unordered A. Then ALL 120 anchored full five-geodesics have the word
  (L(c),1−L(c),L(c)),
where c is their THIRD (middle) coordinate direction. Therefore every anchored full five-path has TWO changes, even though the actual CENTRAL ORDERED-THREE-FACE windows take BOTH binary colors among the 120 permutations. A bichromatic central three-face pair in a single five-direction order-exchange block is not sufficient to force even a one-switch full FIVE-edge path rooted at the common chart corner.

**THEOREM 3 (compatibility with the genuine ACTIVE NORI axiom).** For any n>=6, the arbitrary anchored-five-face assignment of Theorem1 extends to a genuine binary ordered physical three-face coloring of the ENTIRE Q_n satisfying
   c(bar F,rev π)=1−c(F,π).
Reason: physical antipodality of any ordered face inside the anchored five-coordinate subcube complements at least one FIXED EXTERIOR coordinate OUTSIDE B, sending that physical face to a different parallel B-face. Hence NO two prescribed ordered face objects in the anchored five-face belong to one physical antipodal-reversal orbit. Assign the complement-reversal mate bit consistently, and choose the remaining orbits arbitrarily.

When n=5 (the anchored five-face is the WHOLE cube), the genuine active axiom imposes the exact additional condition
  t(c,A)+t(c,(B\{c})\A)=1
for each c and unordered A. These conditions pair the six A's per c into three complementary pairs and leave exactly 15 independent bits; hence even in Q5 there are exactly 2^15 valid active NORI colorings with ALL 120 full geodesics BAD from the prescribed corner r. (This does NOT mean grand NORI fails globally; other starting roots may have good full paths.)

**TOPOLOGY-FIRST INTERPRETATION.** This is a sharp LOCAL COUNTEREXAMPLE to the hoped-for five-block repair lemma 'two opposite central-window face colors force a compatible <=1-switch five-geodesic in that block.' The central color interface can vary arbitrarily with the middle coordinate c while EVERY rooted five-order has alternating window colors. The first obstruction identified by the canonical central-window chart is thus a REAL topological transition/holonomy problem across MULTIPLE charts and physical roots, not a single five-block obstruction one can eliminate using its own local opposite colors alone.

The surviving global target is a color-dependent obstruction to extending the 30-bit local atlases consistently across overlapping B-faces and genuine root transport. This theorem classifies the exact local failure configurations and does NOT assert unrestricted grand closure.

Five-direction repair diagrams are locally rich, but their solutions need not glue globally across different permutohedron faces. A dynamic, physically certified carrier is necessary to exceed the static-index ceiling.
