# Complete five-direction repair obstruction: 30-bit atlas permits all 120 paths alternating and both central colors

# COMPLETE 30-bit classification of a five-direction chart in which ALL 120 anchored permutations have two changes, with arbitrary opposite central colors

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
