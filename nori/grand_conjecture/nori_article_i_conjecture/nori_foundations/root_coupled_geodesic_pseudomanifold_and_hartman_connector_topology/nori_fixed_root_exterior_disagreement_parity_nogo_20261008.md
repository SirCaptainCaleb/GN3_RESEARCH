# Odd face-local parity makes every geodesic from a prescribed antipodal pair alternate

FIXED-ROOT OBSTRUCTION INSIDE VALID FACE-LOCAL NORI; NECESSITY OF ROOT MOBILITY.

Let n>=6 be EVEN, and fix an arbitrary reference cube vertex a in F2^n. For any ordered three-face (F,pi), let W be its three free coordinates and let y_j (j outside W) be its fixed exterior bits. Define
 c_a(F,pi)=sum_(j outside W)(y_j XOR a_j) mod 2.
This is independent of the choice of starting corner within the face, and independent of the order pi of its three free directions.

THEOREM.
(1) c_a satisfies the ACTIVE NORI oddness condition c_a(bar F,rev pi)=1 XOR c_a(F,pi).
(2) Every full antipodal geodesic starting at the specific root a has window color word
 (0,1,0,1,...) of length n-2, hence exactly n-3 changes. Every full geodesic starting at bar a has complementary alternating word and the same maximal number of changes. Thus NO geodesic from EITHER endpoint of the antipodal root pair {a,bar a} has at most one change.
(3) Nevertheless, for EVERY direction order p, there exist exactly eight starting roots yielding a MONOCHROMATIC full antipodal geodesic under c_a. Hence c_a is an explicit valid NORI coloring with abundant global closure but complete failure of the two prescribed antipodal endpoint-root charts.

PROOF. Every ordered three-face has m=n-3 exterior coordinates, and m is odd. Replacing F by bar F flips each exterior y_j and hence changes the parity of the sum by m mod2=1. Reversing the three free directions does not affect the formula. This proves (1).

For a full path starting at a, at its i-th consecutive three-face window precisely the i-1 previously traversed exterior coordinates have been toggled relative to a, while all later exterior coordinates agree with a. Thus the displayed parity is i-1 mod2, independent of the direction permutation. For a path starting at bar a, the i-1 previously traversed exterior coordinates have been toggled into agreement with a, while the remaining n-(i+2) exterior coordinates still disagree with a, so the window color is (m-(i-1)) mod2=1 XOR (i-1 mod2). Both color words alternate throughout, giving n-3 changes. This proves (2).

For any direction order p, write the differences between the proposed starting root y and a as d_i=y_(p_i) XOR a_(p_i). The exterior disagreement count J_i satisfies J_(i+1)-J_i=1-d_i-d_(i+3). Impose d_(i+3)=1-d_i for i=1,...,n-3. The three freely chosen initial bits d1,d2,d3 determine exactly eight roots, and make all J_i identical. Therefore the parity of J_i, which is exactly c_a at the i-th window, is constant. This proves (3). QED.

STRATEGIC CONSEQUENCE. This is a SHARP COUNTEREXAMPLE to any purported theorem guaranteeing a one-change geodesic with a prescribed antipodal endpoint pair, even under genuine ordered-face locality and full NORI oddness. It shows that root mobility is logically necessary for a uniform NORI proof. The root-progress 2n-cube, endpoint root slides, and the topological gluing of distinct Freudenthal root charts cannot be replaced by a fixed-root argument. It is not a counterexample to the grand conjecture; indeed it has eight monochromatic starts for every coordinate order.
