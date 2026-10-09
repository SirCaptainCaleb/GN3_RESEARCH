# A valid NORI coloring has maximal fixed-root permutohedral index but no good rooted paths in a linear Hamming ball

# Fundamental FIXED-ROOT high-index no-go for NORI: maximal permutohedral index with no good full path, and exact root-distance gap

Fix ANY EVEN n>=6 and ANY designated root rho∈F2^n. Define the physical ordered-three-face coloring
  c_rho(F,(i,j,k)) = Σ_(t notin{i,j,k}) [z_t(F) XOR rho_t] (mod2),
independent of the ORDER of the three free directions. Here z_t(F) is the fixed exterior coordinate bit of physical 3-face F.

**THEOREM A (a fully valid active NORI coloring).** Because n is even, n−3 is ODD, and complementing all n−3 exterior bits changes the displayed parity by1. Therefore
  c_rho(bar F,rev(i,j,k))=1−c_rho(F,(i,j,k)).
So c_rho obeys the exact ACTIVE antipodal-reversal-odd NORI law, not a weaker local substitute.

**THEOREM B (EVERY full path from rho has the maximum possible number of color changes).** Fix ANY full direction permutation pi=(p1,...,pn). Along its full geodesic from rho, the jth physical ordered-three-face window traverses exactly j−1 previously flipped exterior coordinate bits (the preceding directions), since the current window's free coordinates have not yet been flipped. Therefore
  w_j(rho,pi)=(j−1) mod2,    j=1,...,L=n−2.
The window color word is 0,1,0,1,...,1 (L even). It has EXACTLY n−3 successive changes, the MAXIMUM possible. For n>=6 there is NO one-switch (or monochromatic) FULL antipodal geodesic rooted at rho, for ANY permutation.

**THEOREM C (maximal topological index at the bad root).** On the standard full-path permutohedron P_n, define endpoint imbalance q_rho(pi)=w_1+w_L−1 as in item nori_permutohedral_antipodal_sphere_endpoint_color_balance_high_index_20261008. Here EVERY permutation vertex has w_1=0 and w_L=1, hence q_rho(pi)=0. Its odd PL extension F_rho is IDENTICALLY ZERO on all of ∂P_n. Therefore
  Z_rho=F_rho^(-1)(0)=∂P_n ≅_equiv S^(n−2),
  ind_Z2(Z_rho)=n−2 (MAXIMUM),
yet NO actual rooted full geodesic from rho has <=1 switch.

This is a rigorous COUNTEREXAMPLE to the tempting intermediate assertion: 'high index of the endpoint-balanced permutohedral carrier at one root forces a one-switch full geodesic AT THAT ROOT.' The earlier proved high-index theorem remains mathematically CORRECT; what fails is any attempt to derive a universal fixed-root grand conclusion from that index alone.

**THEOREM D (EXACT distance to the nearest good rooted full path).** For any starting root y, write s_i=y_i XOR rho_i and t=|s| (Hamming distance from rho). For any full direction order pi the jth successive window change bit is
   D_j(y,pi) = 1 XOR s_(p_j) XOR s_(p_(j+3)),  j=1,...,n−3.
Thus a path has at most ONE change iff along the three disjoint position chains r,r+3,r+6,..., for r=1,2,3, the 0/1 string s in position order has ALL consecutive neighbors different except for at most ONE equality edge ACROSS ALL CHAINS.

If a position chain has length ell, a perfectly alternating string has at least floor(ell/2) ones. Allowing one equality edge can lower its minimum number of ones BY ONE if ell is even, and cannot lower it if ell is odd. (Proof: with z zeros,o ones and at most one 00 adjacency, z<=o+2, hence ones>=ceil((ell−2)/2). For odd ell this gives floor(ell/2); for even ell it gives ell/2−1. Alternating and one-00-defect words achieve the bounds. A 11 equality never gives fewer ones.) Since n is even, at least one of the three position-chain lengths ell_r=#{j∈[n]:j≡r (mod3)} is even. Hence the EXACT minimum Hamming distance from rho to ANY root y admitting a full one-switch antipodal geodesic of c_rho is
  delta_n = Σ_(r=1)^3 floor(ell_r/2) −1
          = { n/2−1, if n≡0 mod6;
              n/2−2, if n≡2 or 4 mod6. }
The minimum is attained by choosing any direction permutation, assigning alternating root-difference bits on two chains and an alternating string with one 00 doublet on an even third chain. The resulting word has exactly ONE nonzero D_j. Conversely any one-switch root for ANY order meets the lower bound since all three chain lengths are permutation-independent.

**COROLLARY E (a macroscopic ball of BAD physical roots).** EVERY starting vertex y with
  d_H(y,rho) < delta_n
fails to admit ANY full antipodal geodesic with <=1 change, regardless of direction order. Thus c_rho has an entire Hamming ball of radius delta_n−1=Θ(n) containing exclusively BAD ROOTS, even though the global NORI conclusion holds elsewhere (e.g. exactly 8 mono roots per fixed direction order, from the proved full-parity three-chain theorem).

For example n=6 gives delta=2; n=8 gives delta=2; n=10 gives delta=3; n=12 gives delta=5; n=18 gives delta=8. A local root-slide or short-radius carrier cannot guarantee a good rooted path near an ARBITRARY chosen root.

**METHODOLOGICAL COROLLARY (CRITICAL for the user-requested topology-first proof).** The fixed-root permutohedral carrier is a valuable HIGH-INDEX geometric completion, but its maximal index can coexist with exclusively bad actual vertex paths. Therefore a proof of GLOBAL grand NORI must use topology that COUPLES DIFFERENT PHYSICAL ROOTS or literal reversed-tail SAME-ROOT reachability extracted from a root-connected witness complex. One must NOT claim that an equivariant low-sphere map on the fixed-root zero carrier can be constructed from '>=3 changes everywhere at that root' alone: the present coloring has precisely that property together with maximal-index Z_rho, so such a universal map is impossible.

Any successful high-index argument must use additional physical information involving OTHER roots and the manner their ordered-face colors share actual physical faces. This is not a counterexample to the global NORI grand conjecture. It is a PROVED strong no-go and a quantitative root-localization barrier that should replace the outdated fixed-root-only closure strategy in the high-priority broadcast.
