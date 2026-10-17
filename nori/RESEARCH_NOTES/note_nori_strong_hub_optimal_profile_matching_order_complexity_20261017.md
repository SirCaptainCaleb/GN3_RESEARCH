# Optimal direction-order routing in strongly connected hub colorings

- Stable ID: note_nori_strong_hub_optimal_profile_matching_order_complexity_20261017
- Author: unspecified; session provenance retained
- Primary home: subsection:full_geodesic_color_profiles_span_the_entire_binary_space
- Labels: 
- Lifecycle: active
- Epistemic status: proved
- Current version: 3
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11254_3
- Updated session: session_nori_r11254_3
- Disposition: none
- Successor: none

## Related references

- None

## Research note

For each n at least four, an antipodally odd hub coloring with strongly connected directed influence has a perfect root-profile matching using two to the power n minus two direction orders, and fewer orders cannot suffice.

PROOF AND SHARPNESS. Put B={0,...,n-2} and h=n-1. Choose a Boolean function g on the leaves satisfying g(y+1)=1+g(y), with g(0)=0, and define c_j(x)=x_h for leaf j, c_h(x)=g(x_B). Parity on the n-1 leaves works when n is even; majority with first-leaf tie-breaking works when n>=5 is odd. Both depend on all leaves, so the directed influence graph contains the bidirected spanning star. The latter rule is nonlinear. If S is the subset of leaves after h in an order, the profile from root x=(u,b) obeys w_B=b*1_B+1_S, w_h=g(u+1_(B minus S)). Each root supports 2^(n-1) profiles, as also noted by another researcher in note_nori_affine_matching_flat_rigidity_20261017_r11377. Every fixed order produces only FOUR profiles over all roots: its leaf word is 1_S or its complement, and its hub bit takes either value by balancedness. Hence at least 2^(n-2) distinct orders are needed to cover all profile targets. For the matching construction choose one representative S of each complement pair {S,B minus S}, and the order (B minus S,h,S). These 2^(n-2) selected orders define a regular bipartite root-profile graph of degree 2^(n-2): each root gets distinct leaf-word complement classes, and every target fixes the selected S and hub root bit b, leaving 2^(n-2) possible leaf-root vectors u. Counting edges proves Hall's condition, so a perfect root-profile matching exists using only the selected orders. The order lower bound is therefore attained for every n>=4. DIAGONAL COST. For root x, put leaf j before h iff x_j=x_h. Every leaf profile color becomes x_j, while the hub color is 1-x_h because all leaf bits are 1-x_h at that step. The profile is x+e_h. This common-translation perfect matching requires 2^(n-1) global order types: the leaf-before-h partition is forced and every possible subset occurs. It uses twice the minimum order budget.

AFFINE ROOT-SYNDROME TRANSVERSAL LEMMA. For any affine legal coloring c(x)=a+Ax, put R=im A, K=ker A, q=dim K and t(pi)_i=sum of A_ij over all j preceding i in pi. A rooted profile equals a+Ax+t(pi). Assume that the t(pi) meet every coset of R. Choose one order pi_z for each of the 2^q quotient cosets z, choose a complementary space U with F2^n=U direct_sum K, and choose a bijection f from K to the quotient. Assign to root x=u+k the profile a+Au+t(pi_(f(k))). Each target coset receives a bijective image of U, and different k use disjoint cosets, so this is a perfect matching using 2^q orders. Since a single order has only |R| attainable profiles, fewer than 2^q orders cannot cover the profile cube. Conversely any perfect matching implies that the syndrome set meets every quotient coset. The existing affine corank-at-most-two theorem therefore gives optimal perfect matchings with at most four distinct orders in that class, but higher-corank affine surjectivity remains open. VERIFIERS: nori_hub_order_complexity_verify.py checks legality, directed strong connectivity, restricted degree regularity, perfect matching, and canonical diagonal orders for n=4 through 8. nori_affine_hall_order_matching.py checks the affine lemma on 800 sampled legal matrices through n=7. Independent exhaustive C++ tools nori_hall_q4.cpp and nori_bijection_q4.cpp enumerate all 65,536 legal Q4 colorings: each admits a root-profile perfect matching, but 59,648 have no single fixed order mapping all roots bijectively to profiles. This Q4 audit is finite, not a dimension-uniform Hall assertion. Full proof: /mnt/data/nori_strong_feedback_hub_latin_transversal.md. The unrestricted NORI1 conjecture remains open.
