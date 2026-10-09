# Five-direction odd-cycle transport: at least 24 of 120 root-neighbor orders good; universal ≥1/5 rank-five density

# UNIVERSAL FIVE-DIRECTION ROOT-NEIGHBOR TRANSPORT: >=24 OF 120 ORDERS GOOD, EXACT >=1/5 RANK-FIVE ONE-SWITCH DENSITY, NO ODDNESS NEEDED

Let n>=5 and c be ANY binary coloring of physical ORDERED three-dimensional faces of Q_n, with NO antipodal NORI axiom assumed. Fix ANY set B={a,b,c,d,e} of five distinct coordinate directions and ANY physical cube root r∈Q_n. We use genuine directed five-edge cube geodesics with five distinct directions from B.

For any ordered triple of distinct directions (i,j,k) in B, define
  H_r(i,j,k)=c(F(r;{i,j,k}),(i,j,k)),
where F(r;{i,j,k}) is the actual physical three-face through r, with all exterior coordinates fixed to r. The ordered physical face color H_r is a literal color from c, not a fictitious root-dependent edge color.

**THEOREM 1 (every root has >=24 one-switch five-geodesics originating at its FIVE NEIGHBORS).** For at least TWENTY-FOUR of the 5!=120 permutations pi=(p1,p2,p3,p4,p5) of B, the actual FIVE-EDGE geodesic rooted at
  x=r XOR e_(p1)
and using pi has AT MOST ONE ordered-three-face window-color change.

PROOF. Fix any CYCLIC ordering of the five directions, modulo cyclic rotation. There are (5−1)!=24 distinct cyclic orderings, each with exactly5 linear rotations. Write one such cycle (a,b,c,d,e), understood cyclically. Look at the five ACTUAL ordered physical face colors through the SAME root r:
  h1=H_r(a,b,c),
  h2=H_r(b,c,d),
  h3=H_r(c,d,e),
  h4=H_r(d,e,a),
  h5=H_r(e,a,b).
Since binary colors around a cycle of ODD length five cannot alternate on ALL five adjacent edges, some consecutive pair hi,h_(i+1) (cyclic indices) is EQUAL. Rotate the cycle so this pair becomes
  H_r(p1,p2,p3)=H_r(p2,p3,p4)=q.

Take the ACTUAL physical rooted five-geodesic with starting root x=r XOR p1 and directed order (p1,p2,p3,p4,p5). Its FIRST ordered-3-face window has free directions (p1,p2,p3) and contains r, because x and r differ ONLY in free coordinate p1; hence its color is H_r(p1,p2,p3)=q. After the first direction p1 has been flipped, the path reaches r. Its SECOND physical ordered-3-face window with free directions (p2,p3,p4) therefore also contains r and has color H_r(p2,p3,p4)=q. Its THIRD window may have arbitrary color. So its three-window color word is (q,q,*) and has at most one change.

Each of the 24 distinct cyclic classes contributes a distinct LINEAR permutation pi with this property, proving the >=24 claim. The resulting roots lie among the five immediate physical cube neighbors r XOR a (a∈B). QED.

**THEOREM 2 (exact universal >=1/5 density of GOOD rank-five directed paths).** For EVERY fixed five-coordinate support B, among all 2^n*120 actual rooted five-edge B-geodesics in Q_n, at least
  24*2^n
have at most one ordered-three-face color change. Equivalently,
  Pr_(uniform root and uniform direction order on B)(<=1 switch)>=1/5
for ANY physical ordered-three-face coloring (active NORI or not).

PROOF. Theorem1 holds for EVERY r∈Q_n, yielding at least24 successful ordered permutations pi under the rerooting map
  (r,pi) -> (x=r XOR first(pi),pi).
This map is a BIJECTION on all pairs (r,pi), with inverse r=x XOR first(pi). Therefore summing >=24 successes over each r counts DISTINCT actual rooted paths and gives >=24*2^n of the 120*2^n possible pairs. QED.

**COROLLARY 3 (a fully genuine local repair for the classified 30-bit five-block bad-root charts).** Suppose every five-direction full path anchored at a particular root r is BAD with exactly two changes, including the full 30-independent-bit local atlas classified by nori_exact_five_block_all_120_two_switch_atlas_thirty_binary_parameters_20261008. Nevertheless among the SAME five-coordinate directions, at least24 of their full five-direction orders produce GOOD at-most-one-switch paths once their starting root is transported across JUST ONE physical direction edge r->r XOR first(pi). This repair is forced by the ordinary five-cycle parity of ACTUAL first-layer physical ordered-face colors, with no appeal to a nonexistent same-root local repair lemma.

**TOPOLOGY-FIRST UTILITY AND LIMIT.** Theorem2 supplies a dimension-independent positive density of genuine rank-five <=1-switch partial path states, paired with explicit one-edge physical ROOT TRANSPORT; these are the first nontrivial color-sensitive objects not captured by the old static rooted path-sheet cube. A higher-index path/order repair carrier might use the root-neighbor transport as valid transition arrows between adjacent permutohedron charts and literal root layers. However the certificate transports a five-edge path, NOT automatically a longer or full n-edge path, and the local root r may depend on the direction order. It does not establish grand NORI closure for arbitrary n.

## Cohomological strengthening: each physical pentagon has an ODD number of literal root-transport repairs

Fix the cyclic five-tuple (p0,p1,p2,p3,p4) used in Theorem1 and denote h_i=H_r(p_i,p_(i+1),p_(i+2))∈F2 (indices modulo5). Define the *good marked root-transport edge bit*
  e_i=1+h_i+h_(i+1)∈F2.
Then e_i=1 iff the genuine rooted full five-geodesic with first direction p_i, following the cyclic permutation, and starting root r XOR p_i has its FIRST TWO ordered-three-face colors equal. Such a path automatically has <=1 switch (the third window is free to vary). Its witness is the actual ordered-physical-face pair through r.

**THEOREM 4 (odd physical repair count, exact mod-two index).**
  Σ_(i modulo5) e_i =1 (mod2).
In particular not only one but an ODD number (1,3,or5) of the five root-neighbor shifted cyclic full paths have a certified monochromatic four-window prefix and hence a one-switch full five-direction completion. The parity is completely INDEPENDENT of coloring, exterior bits, root r, active NORI oddness, and the choice of five distinct directions.

**Proof.** Σ e_i =5+Σh_i+Σh_(i+1)=1 in F2. This is exactly the identity that the constant-one edge cochain of the physical shift pentagon cannot be a vertex-color coboundary. QED.

**Topological identification with the project's good-window cohomology.** On the actual ordered-window shift graph through r define α(uv)=1+c(u)+c(v) on consecutive-window edges, where '1' is the physical face-center distance parity β=1. This is the project's monochromatic-shift cocycle α=β+δc from nori_good_window_set_complex_metric_parity_extension_and_full_span_edge_20261009. Theorem4 says its pairing with EVERY genuine centered five-window pentagon is 1. Each selected edge with α=1 is NOW GIVEN AN EXPLICIT ROOT-TRANSPORT INTERPRETATION: the four-edge monochromatic connector between the two shift-adjacent real physical windows is rooted at a CUBE NEIGHBOR of the pentagon's physical hub; appending its fifth distinct coordinate gives a genuine rank-five <=1-switch geodesic. Thus the nonzero temporal/antipodal cohomological class has actual root-moving good-path certificates, not just abstract mod-two voltage.

Under active NORI, α descends to the quotient and the previously proved identity [α_bar]=[β_bar]+w makes this a concrete physical realization of the nontrivial temporal-antipodal class in the team's four-sheeted (Z2)^2 window-cover program. The mod-two pairing is genuinely topological, but its nonzero degree ONE does not automatically yield a nonzero HIGH-degree cup product or a full n-geodesic. The missing work is to glue these odd repair-pentagons in independent coordinate directions into higher-dimensional certified cup products while keeping the actual path order/physical faces compatible.
