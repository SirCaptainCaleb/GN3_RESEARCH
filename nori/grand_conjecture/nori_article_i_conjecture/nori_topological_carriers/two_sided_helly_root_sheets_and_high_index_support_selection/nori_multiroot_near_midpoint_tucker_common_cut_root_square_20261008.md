# Multiroot Tucker theorem synchronizes two genuine NORI path packets across any physical root square at a shared interior cut

# ROOT-SQUARE TUCKER SYNCHRONIZATION: an entire physical square of roots shares one near-midpoint cut across two genuine NORI path packets

Let n>=7 and c be any ACTIVE NORI coloring of physical ordered three-faces with antipodal-reversal oddness. Fix ANY t distinct physical roots X=(x_1,...,x_t) with 1<=t<=n−2. The previously proved multiroot permutohedral path-packet complex K_X (Item nori_multiroot_permutohedral_endpoint_zero_synchronized_face_packets_high_index_20261008) has:
- vertices P=(pi_1,...,pi_t), one ACTUAL full x_i-rooted endpoint-opposed geodesic order pi_i for each root x_i; all pi_i belong to a common proper face of the standard (n−1)-permutohedron;
- simplices when ALL permutation orders appearing in ALL constituent packet vertices belong to ONE common proper permutohedron face;
- free involution tau(P)=(rev pi_1,...,rev pi_t);
- mod2 first cover class w with w^(n−2−t) != 0 on K_X/tau.

For each packet vertex P, assign the ONE-BIT signed median-switch-side label
  eps(P)=eps(pi_1)∈{+1,−1}
for its first designated root, with eps(pi) defined in proved Item nori_binary_switch_side_tucker_near_bisection_actual_rooted_full_paths_20261008. This is genuinely odd: eps(tau P)=−eps(P).

**GENERAL THEOREM (t-root interior-cut Tucker synchronization).** Assume n>=t+5 and put
  k=floor((n−1−t)/2) >=2.
Then there exist two genuine packet vertices P=(pi_1,...,pi_t) and Q=(sigma_1,...,sigma_t), satisfying:
1. eps(pi_1)=−eps(sigma_1);
2. for SOME common coordinate subset S⊂[n] of rank ell with
       k <= ell <= n−k,
   EVERY ONE of the 2t direction permutations pi_1,...,pi_t,sigma_1,...,sigma_t has S as its first ell used-coordinate SUPPORT;
3. therefore for EVERY s=1,...,t, the two corresponding ACTUAL full x_s-rooted antipodal geodesics meet at the SAME physical intermediate cube vertex y_s=x_s XOR S after ell steps. ALL these 2t paths use S before the cut and its coordinate complement after the cut;
4. the packet vertices are distinct and are not mere antipodal reversals, since a common proper permutohedron face cannot contain a direction permutation together with its complete reversal.

**PROOF (equivariant outer-facet elimination).** Put d=n−2−t, so w^d!=0 on the ACTUAL multi-root packet complex K_X. For every nonempty proper subset T of coordinate directions of OUTER rank |T|<=k−1 or |T|>=n−k+1, define D_T⊆K_X as the full simplex of genuine packet vertices whose EVERY constituent order lies in the permutohedron facet H_T corresponding to first-block support T. Let O_k=union D_T. Each D_T is indeed a simplex by the definition of K_X. Every nonempty finite intersection D_T1∩...∩D_Ts requires T_1,...,T_s to be strictly nested, because one genuine permutation order cannot have two incomparable prefix supports. The index poset has ranks among 1,...,k−1,n−k+1,...,n−1; hence the equivariant nerve has dimension at most 2k−3. Reversal exchanges D_T with D_(T^c), and no inclusion chain contains complementary sets, so the nerve action is free. As in the previously proved macroscopic-cut Tucker theorem, finite equivariant open thickening plus partition of unity produces an odd/equivariant map O_k to this nerve and shows
  w^(2k−2)|O_k=0.
Choose an invariant regular neighborhood U of O_k with the same vanishing.

Linearly extend eps(P)∈{±1} to an odd PL scalar f on |K_X|. If f had no zero OUTSIDE O_k, then on the invariant open complement V=K_X\O_k one could normalize f to an equivariant map V→S^0, so w|V=0. The relative cup product for open cover U∪V=K_X forces w^(2k−1)=0 globally. But our k satisfies
  2k−1 <= n−2−t = d,
contradicting w^d!=0. Therefore some scalar zero z lies outside O_k. Its minimal supporting packet simplex contains two actual packet vertices P,Q with eps(P)=−eps(Q). Since that simplex belongs to K_X yet is outside O_k, its constituent genuine permutation vertices lie in a common proper permutohedron facet H_S of INNER rank k<=|S|<=n−k. That exact support S is shared by ALL 2t full geodesic orders from ALL chosen physical roots, proving the claim. QED.

**PHYSICAL ROOT-SQUARE COROLLARY (main target).** Let n>=11, choose ANY actual 2-dimensional ROOT CUBE face with corners x_1,...,x_4, and apply the theorem with t=4. Then
  k=floor((n−5)/2)>=3.
There exist TWO packet families of FOUR actual full endpoint-opposed antipodal NORI geodesics (eight real paths total), one from EACH of the four roots per packet, such that all eight direction words share ONE SAME used-coordinate prefix set S of cardinality
  floor((n−5)/2) <= |S| <= n−floor((n−5)/2).
For each of the four physical roots x_s, both packet paths reach y_s=x_s XOR S at the SAME rank, and the four vertices {y_s} form the translation of the original root square by XOR S, so they again constitute an actual physical coordinate square. Two of the paths from distinguished root x_1 carry OPPOSITE signed median-switch-side bits, hence are not identical. Both sides of the cut have at least three edges, so all their physical ordered-three-face internal windows are well-defined.

**HIGHER CUBICAL GENERALIZATION.** When 2^h<=n−2 and n>=2^h+5, the same theorem simultaneously synchronizes all 2^h roots of ANY chosen h-dimensional physical root subcube, with
  k=floor((n−1−2^h)/2).
Two genuine full-path packets translate that entire h-cube of roots into one h-cube of shared physical intermediate vertices at one common cut rank, with opposed median-side sign at a distinguished root.

**TOPOLOGICAL/PHYSICAL CLOSURE GAP.** This strengthens the simple Borsuk–Ulam 'common proper order face' packet to an actual COMMON INTERIOR CUBE CUT OF GENUINE PATHS, preserving the physical geometry of arbitrary root squares/cubes. Still, the two ordered-three-face windows at a splice of any two packet paths are NOT automatically monochromatic, and endpoint-opposed full paths may have many switches. Proving a cubical fixed-point or Hex/Sperner compatibility law for the physical FOUR-corner square of seam windows could now turn this near-middle root-mobile packet into the exact reversed-tail monochromatic reachability overlap or a strict switch-defect descent. This missing extraction is not assumed here. Grand NORI remains open.

## ELEVATION: high-index multiroot Tucker packets cannot map into static two-sided admissible root-sheet carriers under grand failure

The newly proved exact two-sided root-sheet result nori_two_sided_root_sheet_helly_equivariant_exact_grand_fixedpoint_index_four_ceiling_20261008 defines a genuine physical Θ-equivariant simplicial witness-sheet complex E_c on all ACTUAL <=1-switch partial NORI geodesics (length>=3). It proves that, under the hypothetical NO-GRAND-CLOSURE assumption, E_c has a FREE Θ-involution and cohomological index at most FOUR, uniformly in ambient cube dimension:
  w_E^5=0.
The upper bound is geometric: three-edge paths give a 3-skeleton base in signed-unused endpoint space, whereas genuine root-fiber sheets of longer paths have dimensions <=2 and their two-sided boxes dimensions <=4.

**THEOREM (exact high-index map obstruction).** Fix t distinct roots with 1<=t<=n−7. Under hypothetical grand NORI failure, there exists NO equivariant continuous map
   Φ:|K_X|→|E_c|,
where K_X is the actual t-root endpoint-opposed permutohedral packet complex with coordinate-order reversal involution, and E_c is the two-sided actual <=1-switch path root-sheet nerve with physical Θ involution.

**Proof.** K_X has nonzero w_K^(n−2−t) by the established multiroot Borsuk–Ulam packet theorem. The inequality t<=n−7 gives n−2−t>=5 and hence w_K^5!=0. If Φ were equivariant between these two free involution complexes, then the associated double-cover first cohomology class pulls back:
  w_K=Φ^*(w_E).
But w_E^5=0 because ind(E_c)<=4, so w_K^5=Φ^*(w_E^5)=0, contradiction. QED.

**Root-square instance.** For ANY physical root 2-cube and n>=11 (t=4), the two genuine near-midpoint endpoint-opposed packet carriers proved above have high index n−6>=5; yet the static certified one-switch two-sided sheet complex has index<=4 under grand failure. Thus no entire equivariant PL 'repair selection' from their ACTUAL packet complex into the existing static partial-path certificate nerve can exist in a counterexample.

**RESEARCH PROGRAM.** An explicit equivariant *cellwise* map from the high-index packet complex into the honest two-sided one-switch witness nerve, with correct physical antipodal reversal and literal face overlaps on every simplex, would prove the grand NORI conjecture immediately for the applicable n. This is NOT produced by taking a set-theoretic choice of one short witness per Tucker vertex; continuity/simplicial compatibility and the involution matter. The theorem pinpoints why a topological proof must enrich the order-exchange / suffix seam-transport cell structure rather than only convexify static root cubes. This is an exact index-gap obstruction, not an unconditional proof of the conjecture.
