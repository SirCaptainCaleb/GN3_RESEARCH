# Balanced paired-order geodesics form a connected central-layer repair graph

PAIRED-ORDER CENTRAL-LAYER REPAIR GRAPH.

Let n=2r>=4 and k=r-2. Fix ANY root x in Q_n with exactly r zero bits and r one bits among its n coordinate directions. Let A={coordinates with x_v=0} and B={coordinates with x_v=1}, so |A|=|B|=r. Call a full direction order p=(p1,...,p_(2r)) PAIRED when each consecutive pair (p_(2j-1),p_(2j)) contains one direction from A and one from B.

THEOREM (central-layer carrier and connectivity).
(1) Every paired order p, starting at the fixed root x, has exterior Hamming weights K_i in {r-2,r-1} for ALL n-2 ordered-three-face windows. The number of paired orders is exactly 2^r(r!)^2.
(2) The graph whose vertices are these paired orders and whose edges are adjacent transpositions of coordinate directions that preserve the paired property is CONNECTED. Each edge connects two actual full antipodal geodesics with the SAME root x, and preserves every ordered-three-face window outside at most FOUR consecutive windows.
(3) Reversal p->rev p is a fixed-point-free involution on this graph and preserves the paired property. If c is an antipodal-reversal-odd NORI coloring, the corresponding full-window color words satisfy
 w(x,rev p) = 1 + rev(w(x,p))
with the complement taken bitwise. Thus this is a connected root-fixed, involution-compatible, entirely central-layer repair family for ANY NORI coloring, including arbitrary dependence on exterior face bits.

PROOF OF (1). Let y_i=x_(p_i) be the starting bits in p-order, so y_(2j-1)+y_(2j)=1 for each j and sum_(i=1)^n y_i=r. Put S_j=sum_(i=1)^j y_i, with S_0=0. The exterior weight at window i is
 K_i = (i-1)-S_(i-1) + r-S_(i+2) = r+i-1-S_(i-1)-S_(i+2).
For i=2j-1 odd, S_(i-1)=j-1 and S_(i+2)=j+y_(2j+1), so K_i=r-1-y_(2j+1). For i=2j even, S_(i-1)=j-1+y_(2j-1) and S_(i+2)=j+1, so K_i=r-1-y_(2j-1). Every K_i is therefore r-1 or r-2. To count paired orders, list the A directions in r! orders, the B directions in r! orders, and orient each resulting pair in one of 2 ways, giving 2^r(r!)^2.

PROOF OF (2). Adjacent swaps within one pair flip that pair's orientation and preserve the paired property. Normalize all pairs to the orientation (A,B) using these swaps. In the four-direction block (a,b,c,d), where a,c belong to A and b,d to B, the adjacent-swap sequence
 (a,b,c,d)->(b,a,c,d)->(b,c,a,d)->(c,b,a,d)
interchanges the adjacent A members a,c while every intermediate ordering remains paired. Similarly
 (a,b,c,d)->(a,b,d,c)->(a,d,b,c)->(a,d,c,b)
interchanges the adjacent B members b,d while every intermediate ordering remains paired. These elementary operations generate independent arbitrary permutations of the A and B lists, and pair-orientation flips are also allowed, so every paired order can be reached from any other. An adjacent transposition in a direction permutation changes only the intermediate path vertex between those two moves; all other physical path vertices are identical. A consecutive ordered-three-face window is a four-vertex subpath, so at most four windows containing that intermediate vertex can change. This holds for arbitrary face-dependent c.

PROOF OF (3). Reversing the order reverses both the order of pairs and the two members within each pair, hence preserves the paired condition. No order of distinct directions equals its own reversal. The path starting at x with order rev p is the antipodal image of the ordinary reversed path with order p. Its ordered-three-face windows are, in opposite order, antipodal faces with reversed free-coordinate orders. NORI oddness therefore complements every color, giving the displayed word identity. QED.

TOPOLOGICAL ROLE. For EACH balanced root x, the paired-order graph supplies a connected finite 1-skeleton of actual rooted Freudenthal chambers, closed under antipodal path reversal, and all supported on central exterior-weight faces. Every repair edge has a bounded locality of four consecutive colored windows. This is a concrete candidate on which to formulate Hartman's least-unreachable witness labeling. CONNECTIVITY ALONE does not establish NORI closure: a further labeling/overlap theorem must force a low-switch chamber.
