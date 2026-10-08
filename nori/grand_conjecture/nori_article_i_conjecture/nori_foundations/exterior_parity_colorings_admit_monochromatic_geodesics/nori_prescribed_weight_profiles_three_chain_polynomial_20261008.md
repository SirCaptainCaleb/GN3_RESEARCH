# Exact three-chain generating polynomial for all exterior-weight profiles

EXACT THREE-CHAIN SOLUTION OF PRESCRIBED EXTERIOR-WEIGHT PROFILES.

Let p=(p1,...,pn) be a fixed permutation of the n coordinate directions, x_i the initial bit at p_i, and K_i=sum_(t<i)(1-x_t)+sum_(t>i+2)x_t the exterior Hamming weight at the i-th three-direction window. As usual
 K_(i+1)-K_i=1-x_i-x_(i+3)
for 1<=i<=n-3.

THEOREM (exact generating-function characterization). Fix ANY prescribed signed increment vector delta=(delta_1,...,delta_(n-3)) in {-1,0,+1}^(n-3). Partition coordinate positions 1,...,n into the three chains (r,r+3,r+6,...), r=1,2,3. On each chain, interpret each seam relation between x_i and x_(i+3) as follows:
 delta_i=0 requires (x_i,x_(i+3)) in {(0,1),(1,0)};
 delta_i=+1 requires (0,0);
 delta_i=-1 requires (1,1).
If a chain's edge requirements are inconsistent, the profile has no root. Otherwise:
(A) a chain containing at least one nonzero delta_i has EXACTLY ONE binary labeling of its coordinates; denote the number of 1-bits among its exterior positions (indices >=4) by a_r.
(B) a chain with all zero delta_i has exactly TWO alternating binary labelings; if it has L_r exterior positions, the two possible numbers of exterior ones are floor(L_r/2) and ceil(L_r/2), counting multiplicity if L_r is even.
Define the polynomial
 P_delta(z)=product_(r=1)^3 P_r(z),
where P_r(z)=z^(a_r) in case A, and P_r(z)=z^floor(L_r/2)+z^ceil(L_r/2) in case B. If any chain is inconsistent set P_delta=0. Then for EVERY integer q, the coefficient [z^q]P_delta is EXACTLY the number of roots x for which K_1=q and K_(i+1)-K_i=delta_i for all i. In particular the unconstrained initial-weight fiber size is 2^(number of chains with no nonzero seam), and every exact fiber has size at most 8.

PROOF. Each difference equation is equivalent to its displayed allowed bit-pair condition. Relations on distinct residue classes modulo 3 share no variables. On one chain with all delta=0, the first bit may be chosen arbitrarily and all later bits alternate, giving two solutions with the stated exterior weights. On a chain with some nonzero delta, that edge fixes both endpoint bits, and the remaining relations propagate uniquely to both ends (or contradict another fixed edge). Therefore valid assignments multiply across the three chains. The exponent of the corresponding monomial records the contribution to K_1 from each chain. Polynomial multiplication counts exactly the assignments with a given total exterior weight q. QED.

TWO-JUMP COMPATIBILITY. Let n be even and k=(n-4)/2. To prescribe the central profile k before seam j, k+1 between seams j<l, and k thereafter, put delta_j=+1, delta_l=-1, other deltas0 and test [z^k]P_delta>0. Whenever j,l lie on the same residue chain, chain compatibility REQUIRES (l-j)/3 even (equivalently 6 divides l-j). If they lie on distinct chains, the chain equations are automatically consistent, though the weight coefficient can still vanish. Reversing the jump signs gives the complementary high/low/high profile with K_1=k+1 and is equivalent by complementing all root bits.

TWO-SEAM COLOR CANCELLATION. Suppose c(F,pi)=h(pi)+f(K(F)), where n is even and f(k+1)=1+f(k). Fix an order p and two distinct color-change seams j<l of its coordinate-only h-word. If [z^k]P_delta>0 for delta_j=+1, delta_l=-1, delta_i=0 otherwise, the corresponding central-profile root toggles the f-color exactly at j and l and cancels BOTH chosen changes, leaving exactly r-2 changes when the h-word has r changes. For r<=3 this yields a full one-change NORI geodesic (assuming the original coloring satisfies NORI oddness). The criterion applies to ANY two change seams; it does not require they be consecutive within the list of changes.

SCOPE. This completely determines which arbitrary signed exterior-weight profiles are realizable, and strengthens the earlier single central jump by an exact multiple-jump test. A two-jump pattern may fail even when its seams are on distinct residue chains because the total initial exterior weight cannot be the central value. Such failures show the limit of root-only central-weight cancellation, and motivate exchanging the direction order p.
