# All full antipodal edge-color patterns for disjoint signed-symmetric odd self-dual gates on functional block graphs

# Nonlinear odd-MAJORITY block-dependent antipodal edge colorings: universal realization of all full geodesic color patterns

**Set-up.** Fix n>=2 and a partition of coordinate directions into m>=2 nonempty blocks B_1,...,B_m. Choose NONEMPTY PAIRWISE DISJOINT subsets M_j⊆[n] of ODD cardinality, each inside an OTHER block B_(sigma(j)), where sigma:[m]->[m] is ANY fixed-point-free FUNCTION; branching is permitted. For each j, choose arbitrary fixed input signs s_{j,u}∈F2 for u∈M_j and define the self-dual Boolean majority gate
  g_j(y)=Maj_(|M_j|) ( (y_u+s_{j,u})_(u∈M_j) )
with majority of odd size. Also allow output sign t_j∈F2 by replacing g_j with g_j+t_j; this can be absorbed into direction biases. Let b_v∈F2 be an arbitrary independent bias for each coordinate direction v. Define the actual UNDIRECTED PHYSICAL edge color in direction v∈B_j at vertex x by
  c_v(x)=b_v + g_j(x_(M_j)).
Because M_j∩B_j=empty, this color is independent of x_v. Because |M_j| is odd and signed majority obeys g_j(bar y)=1+g_j(y), the full coloring is antipodally odd: c_v(bar x)=1+c_v(x).

**THEOREM (NONLINEAR all-pattern geodesic closure in every dimension).** For every coloring in the above class and EVERY prescribed direction-indexed target T∈F2^n, there exist an actual cube starting root x and a full permutation p of all n coordinate directions such that the TRUE full n-edge antipodal geodesic P(x,p) has physical color T_v on the unique edge in direction v, for all v simultaneously. In particular T=0 and T=1 give full MONOCHROMATIC antipodal geodesics. This resolves a genuinely NONLINEAR, arbitrarily high input-arity family, not just the affine edge case.

**Lemma 1 (alternating majority trajectory in any prescribed input order).** Let k=2h+1 be ODD, choose arbitrary input sign vector s∈F2^k and ANY permutation (u_1,...,u_k) of the input coordinates. For either desired output initial bit alpha∈F2, there is an actual initial input assignment y∈F2^k such that
  g(y xor {u_1,...,u_t})=alpha+t mod2
for every 0<=t<=k, where g is signed majority of the k inputs.
Proof. Let z_i=y_(u_i)+s_(u_i) be the EFFECTIVE signed input value in the specified order. To realize alpha=0 choose z_i=0 for odd i and z_i=1 for even i. Then initially exactly h of the k signed inputs are 1, so majority is 0. Flipping the first signed input from 0 to1 raises the number of ones to h+1 and the majority to1; flipping the second signed input from1 to0 lowers it to h; and so on. The majority alternates 0,1,0,1,... at EVERY successive step. To realize alpha=1 complement all effective input bits, yielding output 1,0,1,0,... by majority's self-duality. Finally set y_(u_i)=z_i+s_(u_i). This works for EVERY prescribed permutation and BOTH initial output values. QED.

**Lemma 2 (simulation of independent parity registers by signed majority along a full geodesic).** Fix any permutation p of ALL coordinate directions, and prescribe arbitrary bits alpha_j (one for each support M_j). There is a SINGLE actual starting cube root x such that for all j simultaneously, the true gate g_j evaluated at each intermediate cube vertex of the p-geodesic satisfies
  g_j(x xor (directions already traversed))
       = alpha_j + (# of directions from M_j already traversed) mod 2.
Proof. For each j, restrict p to its induced ordering on the coordinates in M_j; apply Lemma1 with desired initial alpha_j to choose the starting bits x on M_j. Because the M_j are PAIRWISE DISJOINT, these input assignments are independent and extend to one global root x. Toggling directions outside M_j cannot change g_j, and toggling the M_j directions in their p-order flips g_j on every step by Lemma1. QED.

**PROOF OF THE THEOREM.** Construct an AUXILIARY AFFINE PARITY coloring on the SAME actual cube with the SAME block graph, marks, and direction biases:
  c_v^lin(y)=b_v + Σ_{u∈M_j} y_u, v∈B_j.
The theorem in Item nori_k1_disjoint_odd_support_functional_block_digraph_all_pattern_closure_20261009 proves that, for ANY prescribed T, there exist a genuine full direction permutation p and root y such that c_v^lin along P(y,p) equals T_v for EVERY coordinate v.
Let alpha_j=Σ_{u∈M_j} y_u. Along P(y,p), the affine parity register of class j after an arbitrary prefix of p is
  alpha_j + (# already traversed directions belonging to M_j) mod2.
Apply Lemma2 to THIS SAME order p and THESE EXACT initial bits alpha_j, obtaining a different actual root x whose nonlinear gates g_j reproduce the corresponding affine parity register at EVERY intermediate path position.
For the direction-v edge, with v∈B_j, the actual nonlinear color along P(x,p) is
  b_v+g_j(x at traversal start)
 =b_v+alpha_j+(# already traversed directions in M_j mod2)
 =c_v^lin(the corresponding edge of P(y,p))
 =T_v.
All coordinates are used once, so P(x,p) is an actual full antipodal geodesic. QED.

**General abstract alternating-gate theorem.** The proof uses ONLY that each g_j has the following UNIVERSAL ALTERNATING TRAJECTORY property: for every ordering of M_j and for both alpha∈F2, some input starting assignment makes the gate outputs alternate alpha,alpha+1,alpha,... along that coordinate-distinct geodesic. Consequently ANY self-dual Boolean gates possessing this property can replace signed majority, with exactly the same all-pattern closure result, provided the input supports M_j remain pairwise disjoint and lie in other blocks along a loopless functional dependency sigma. Odd-input parity and signed majority of ANY ODD size are both examples. Further gate classes can be admitted after verifying this precise finite local property.

**Substantive novelty.** This extends NORI's prior ORIGINAL k=1 edge-color solutions from single-coordinate driver functions, odd linear parity driver blocks, and affine corank≤2 to arbitrarily many NONLINEAR three-input majority gates, or majority gates of arbitrarily high odd arity, coupled through any directed functional block graph with branching. The nonlinear edge functions depend essentially on all bits of their supports for size>=3. The proof gives an explicit algorithm: solve the affine reference instance via cycle/tree parity padding (polynomial time), then choose each majority gate's signed input root pattern alternating in the resulting marked-coordinate order. No generic search over all roots or permutations is needed.

**Sharp boundary.** Overlapping input supports destroy independent simultaneous gate simulation; each bit choice can then be prescribed inconsistently by different gate trajectories. A gate without a fully alternating input geodesic in a chosen order may also resist simulation. Both obstacles exist in arbitrary edge colorings, and full unrestricted edge-color closure and ordered-three-face NORI remain open.

**STRONGER COROLLARY: arbitrary signed-symmetric SELF-DUAL gates of odd arity, not just majority.** In the theorem, replace every signed majority g_j by
  g_j(y)=F_j(Σ_{u∈M_j}(y_u+s_(j,u)))
where |M_j|=2h_j+1 is odd and F_j:{0,1,...,2h_j+1}->F2 is ANY symmetric bit function satisfying
  F_j(k-t)=1+F_j(t) for every integer 0<=t<=k.
No monotonicity, threshold property, or affine property is required. Then the exact same all-target antipodal-geodesic conclusion holds.

*Proof of the generalized alternating-gate hypothesis.* Fix any ordering (u_1,...,u_k) of the signed input bits, and put h=(k-1)/2. Choose effective initial bits in this order as 0,1,0,1,...,0, containing h ones. Flipping the inputs successively in this order changes the effective Hamming weight in sequence
  h, h+1, h, h+1, ..., h+1.
Because F is self-dual and k=2h+1, F(h+1)=1+F(h); hence the gate's actual output alternates at EVERY flip. Complementing ALL effective starting input bits changes the initial weight to h+1 and interchanges the two output bits, realizing whichever initial gate output alpha is desired. Input signs are absorbed by setting y_(u_t) to the desired effective value plus s_(u_t). This produces an alternating trace in ANY named input permutation and for BOTH initial output bits. The general abstract alternating-gate theorem in this Item now applies verbatim. QED.

This family strictly contains both odd-parity functions and odd-majority functions, including highly nonmonotone symmetric self-dual nonlinear color gates, with any per-gate independent signed input coordinate transformations. For arity 2h+1, there are 2^(h+1) possible symmetric self-dual truth tables F (one independent output choice for each weight 0,...,h), and the theorem includes ALL of them. Each gate may choose a different arity, different F, and different signed input pattern. The support disjointness and loopless functional block-incidence remain the only extra conditions.

**Precise first nonlinear 3-input specialization.** Every antipodally self-dual Boolean function of at most THREE essential input bits is either an odd parity on 1 or3 variables (up to a constant) or a signed majority of 3 variables (up to input sign). Therefore, if each block B_j has one common odd gate of at most three exterior coordinates, and the gates' ESSENTIAL input supports are pairwise disjoint and contained in other blocks B_(sigma(j)), the full all-target theorem holds for EVERY possible choice of self-dual three-junta gates. This covers the complete small-junta Boolean classification within the block class.
