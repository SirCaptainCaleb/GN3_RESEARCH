# Three-chain affine-exterior theorem: eight monochromatic antipodal roots per direction order

# Three residue chains force fully monochromatic grand geodesics for a wide affine-exterior ordered-face class

Let n>=4, let a=(a_1,...,a_n) in F_2^n be FIXED, and let h(i,j,k) be an ARBITRARY binary function on ordered triples of pairwise distinct cube coordinate directions. Define an ordered-three-face binary coloring by
  c(F,(i,j,k)) = h(i,j,k) + sum_{t notin{i,j,k}} a_t z_t   (mod 2),
where z_t denotes the fixed exterior bit of the physical 3-face F on coordinate t. This is genuinely corner-independent on F, and may vary arbitrarily with the ordered triple h. An optional antipodal-reversal-oddness axiom is satisfied precisely when
  h(k,j,i) + h(i,j,k) = 1 + sum_{t notin{i,j,k}} a_t (mod 2).
Because ordered triples are distinct from their reverse, this constraint is always internally consistent and can be imposed for any fixed a. The existence theorem below does NOT require this antipodal symmetry.

**Theorem A (exact eight roots for each admissible direction order).** Let pi=(p_1,...,p_n) be a permutation of [n]. Suppose every one of the three index-progression chains
  r,r+3,r+6,... <= n  (r=1,2,3)
contains AT MOST ONE position t with a_(p_t)=0. Then there are EXACTLY 2^3=8 distinct cube roots x in {0,1}^n for which the full antipodal geodesic of direction word pi beginning at x has ALL ordered-three-face-window colors equal (zero switches).

**Proof.** Let C_j denote the physical ordered-face color of its jth window (directions p_j,p_(j+1),p_(j+2)), for 1<=j<=n-2. When shifting to C_(j+1), the only exterior bits that change in the *comparison of faces* are p_j, which leaves the free triple and has already been flipped, and p_(j+3), which enters the free triple and was not yet flipped. Therefore
  C_j+C_(j+1)
  =h(p_j,p_(j+1),p_(j+2)) + h(p_(j+1),p_(j+2),p_(j+3))
   + a_(p_j)(1+x_(p_j)) + a_(p_(j+3)) x_(p_(j+3))  (mod2).
The requirement of monochromaticity is exactly the system of n-3 affine equations
  a_(p_j) x_(p_j) + a_(p_(j+3)) x_(p_(j+3))
   = h_j+h_(j+1)+a_(p_j),  j=1,...,n-3.
The equations decouple into three distinct PATHS on position indices, with consecutive vertices distance 3. In each path, the coefficient of variable at position t is a_(p_t), identically in both incident equations. If all coefficients in that path are 1, the path incidence matrix over F2 has full ROW rank (length-1) and its solution space has 2 elements. If precisely one coefficient is 0, the remaining vertex variables form an invertible square reduced incidence matrix (deleting one column from a tree incidence matrix), so the equations have a unique assignment to nonzero-coefficient variables, while the zero-coefficient vertex bit is arbitrary: again 2 solutions. Therefore each of the three paths has exactly 2 choices, independently and for ANY right-hand-side bits h_j+h_(j+1)+a_(p_j). Total exactly 2^3 roots. Each direction-order/root pair yields a full antipodal path, and equality of all consecutive colors means it is MONOCHROMATIC. QED.

**Theorem B (global closure if <=3 exterior coefficients vanish).** Suppose z=#{i:a_i=0}<=3. Choose a permutation pi placing the z zero-coefficient directions at positions of DISTINCT congruence classes mod3, e.g. among positions 1,2,3. Then Theorem A applies, so the coloring has a fully monochromatic antipodal geodesic. This holds for arbitrary h, and in particular every valid active NORI coloring of this affine-exterior form satisfies the GRAND conclusion in a strictly stronger zero-switch version.

**Corollary C (exact quantitative path count in full-parity class).** If all a_i=1, EVERY direction order pi is admissible and each has exactly eight monochromatic starting roots. Therefore this coloring has EXACTLY 8 n! directed fully monochromatic antipodal geodesics, regardless of h. The total number of directed antipodal geodesics is 2^n n!, giving monochromatic density EXACTLY 2^(3-n).

**Corollary D (explicit lower bound for up to three zero coefficients).** Let L_r be the number of positions in [n] congruent to r modulo 3, r=1,2,3, and e_z(L_1,L_2,L_3) the zth elementary symmetric polynomial (e_0=1). The number of permutations assigning the z distinct zero-coefficient directions to DISTINCT residue classes is z!(n-z)! e_z(L_1,L_2,L_3). For each of them there are 8 distinct monochromatic roots. Hence the number of directed full monochromatic antipodal geodesics is at least
  8*z!*(n-z)!*e_z(L_1,L_2,L_3).
No assumption about the triple-order function h or NORI oddness is needed for these estimates.

**Conceptual point.** The three-chain system is a forest (not merely a parity heuristic). The fixed-exterior coefficient pattern near all-one retains enough independent root bits to solve EVERY window equality constraint, with three free root degrees. Even when a valid exterior-parity coloring has disjoint prescribed opposite terminal basins (previous NORI parity example, n>=8), it necessarily has abundant full monochromatic geodesics globally. Thus failure of one chosen Hex/KKM basin intersection may coexist with exceptionally strong full closure. The result establishes a broad explicit solvable subclass, not the universal NORI conjecture.

**Limit.** When >=4 coefficients vanish, at least one index progression must contain at least two zeros for every pi. The corresponding linear system may have dependent or zero rows and be unsolvable for an arbitrary h. This is only a limitation of the uniform *any-h forest argument*, not a constructed global counterexample. In general active NORI ordered-face colors need not have a single fixed exterior linear coefficient vector a, so the theorem does not close the grand conjecture.

**Corollary E (the entire switch-vector law is EXACTLY uniform).** In Theorem A, the n−3 affine equality/difference equations have full row rank; therefore the change-vector map D_pi:F2^n→F2^(n−3) is SURJECTIVE, and EVERY desired change pattern y∈F2^(n−3) is realized by EXACTLY 8 starting roots. In particular, for each integer t=0,...,n−3, precisely
   8 * binom(n−3,t)
starting roots yield EXACTLY t changes along the fixed admissible direction order pi. Thus a uniformly random cube root produces n−3 independent fair bits of window-color change, regardless of the arbitrary ordered-triple function h. Exactly 8(n−2) roots yield at most ONE change, while 8 roots are completely monochromatic. For all a_i=1, this holds for EVERY permutation pi, so the total number of fully GOOD one-switch directed full antipodal geodesics is exactly 8(n−2)n!, independently of h. The fraction of all 2^n n! directed full antipodal geodesics that are good is (n−2)/2^(n−3).

**Proof.** Full row rank n−3 makes the affine change map onto F2^(n−3). Its kernel has dimension n−(n−3)=3, so each image point has exactly 2³=8 preimages. There are binom(n−3,t) vectors of Hamming weight t; summing gives the formulas. Unlike a random-coloring heuristic, this is an EXACT algebraic statement for every arbitrary h in the indicated affine-exterior family.
