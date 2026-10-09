# Canonical odd-dimensional central window: exact two-sided compatibility on noncrossing permutohedron faces; first failure at five-block

# CANONICAL CENTRAL-TRIPLE SELECTOR: PHYSICAL NORI HELLY COMPATIBILITY THROUGH PERMUTOHEDRAL FACE DIMENSION THREE, FIRST OBSTRUCTION AT A FIVE-BLOCK

Let n=2m+1>=7 be ODD, fix any actual cube root x∈F2^n, and consider ALL rooted full cube-geodesic direction permutations pi=(p1,...,pn), or ANY reversal-invariant subset of them such as the team's genuine endpoint-opposed permutations forming K_x. The true directed full path starts at x. Let
  A_pi={p1,...,p_(m−1)}           (prefix USED support),
  T_pi={p_m,p_(m+1),p_(m+2)}      (CENTRAL THREE-EDGE window support),
  R_pi={p_(m+3),...,p_n}          (suffix support).
Let P(pi) be the actual directed THREE-EDGE geodesic consisting of that central ordered triple, rooted at the physical vertex x XOR A_pi. It is automatically monochromatic (one ordered-three-face window), and its complete physical face is the TRUE middle ordered face of the full path. Let E3 denote the actual Θ-equivariant two-sided root-box flag nerve for all actual 3-edge NORI geodesic paths.

**THEOREM 1 (literal equivariance of central selection).**
For the full path Θ(pi)=rev pi rooted at the SAME root x, one has
  P(rev pi)=Θ(P(pi))
as actual ROOTED and ORDERED physical three-edge paths, not merely up to equality of unordered free-coordinate triples.

PROOF. The physical antipodal reversal of the full x-rooted path is the rev pi-order path again rooted x, because its full endpoint is bar x. The central triple of rev pi is the reversed central triple of pi, and its starting root is x XOR R_pi. Meanwhile the actual reversal Θ of P(pi) has root
  (x XOR A_pi) XOR ([n]\T_pi)
     = (x XOR A_pi) XOR (A_pi union R_pi)
     = x XOR R_pi.
Their ordered direction words and starting roots coincide. QED.

**THEOREM 2 (EXACT central-window E3 edge criterion).**
For ANY two distinct full orders pi,sigma rooted at x, the physical two-sided root boxes of their central three-geodesics intersect iff
  A_pi intersect R_sigma = empty
AND
  A_sigma intersect R_pi = empty.
Equivalently, their root/support compatibility test reduces exactly to
  A_pi △ A_sigma subset T_pi union T_sigma.
Thus central-window two-sided box failure means SOME actual cube direction jumps DIRECTLY from the prefix of one rooted full order to the suffix of the other, never occupying the central triple in either order.

PROOF. The root of P(pi) is x XOR A_pi, and its middle free set and used set are BOTH T_pi. The exact proven two-sided-box intersection criterion says compatibility iff supp((x XOR A_pi) XOR (x XOR A_sigma)) subset T_pi union T_sigma, i.e. A_pi △ A_sigma subset T_pi union T_sigma. If a direction lies in A_pi\A_sigma and outside both T, it must lie in R_sigma, since it lies in A_pi and cannot lie in T_pi; similarly for the opposite difference. This is exactly the displayed no prefix-to-opposite-suffix condition. QED.

**THEOREM 3 (all small-block order faces are automatically compatible).**
Let H be ANY face of the ordinary permutohedron P_n; it corresponds to an ORDERED PARTITION of the coordinate-direction set into consecutive blocks B1|B2|...|Bh, within each of which every permutation vertex of H may freely reorder its elements. Say H is CENTRAL-NONCROSSING if NO block occupies BOTH position m−1 (last prefix position) AND position m+3 (first suffix position). Then for EVERY pair of permutation vertices pi,sigma of H, their literal central path boxes B(P(pi)), B(P(sigma)) INTERSECT. Consequently for ANY subset of actual permutation vertices of H, ALL their selected central boxes have ONE COMMON literal two-sided Boolean root pair, by coordinate-box Helly-2.

Proof. If some direction lies in A_pi intersect R_sigma, its position under pi is <=m−1 and under sigma is >=m+3. But since both permutations are vertices of ONE permutohedron face H, each direction remains in the SAME fixed ordered partition block B_j in both, so that block spans both boundary positions m−1 and m+3. The central-noncrossing hypothesis prohibits it; likewise A_sigma intersect R_pi is empty. Apply Theorem2. Coordinate-box 2-Helly supplies common intersection for any finite family, whose coordinate root assignments can be taken Boolean.

Conversely, if H has a flexible block spanning both positions m−1 and m+3, one can pick a direction i from that block and two permutation vertices pi,sigma of H putting i at position m−1 and m+3 respectively. Then i belongs to A_pi intersect R_sigma, violating central-box compatibility. Hence central-noncrossing is EXACTLY equivalent to pairwise compatibility of the central boxes over ALL permutation vertices of H (though a particular smaller subset of endpoint-balanced orders may remain compatible inside a crossing face).

**COROLLARY 4 (first physical incompatibility requires a FIVE-direction permutation block).**
Any ordered partition block spanning positions m−1 and m+3 has at least FIVE consecutive positions. Such a block contributes at least4 to the dimension of its permutohedron face (dim H=Σ(|B_j|−1)). Therefore EVERY permutohedron face of dimension at most THREE is central-noncrossing; its original permutation vertices' selected central physical three-geodesics ALL have a common literal two-sided root box.

Conversely the minimal block crossing from m−1 through m+3 consists of exactly FIVE directions and spans a four-dimensional permutohedron face (an ordered-5 permutohedron), and its full vertex set has physically incompatible selected central three-windows. Thus four-dimensional permutation-order freedom is the FIRST level at which the canonical central-selector can fail physically, precisely matching the independently proved exact index-three ceiling of the static two-sided root-sheet carrier.

**COROLLARY 5 (an explicit equivariant low-order-face subcomplex maps to the physical nerve).**
Let K_x be the genuine high-index endpoint-opposed permutohedral FACE NERVE: its vertices are actual x-rooted endpoint-opposed full direction orders, and its simplices are finite sets of such orders contained together in some PROPER permutohedron face. Let K_x^safe be the SUBCOMPLEX of simplices that can be carried by a central-noncrossing proper permutohedron face. By Theorem3 + Helly2, the canonical central selection induces a Θ-equivariant SIMPLICIAL MAP
  K_x^safe -> E3.
Therefore its cohomological antipodal index is at most THREE. The source K_x has index at least n−3 (previous NORI theorem), so in odd n>=7 with n−3>3, i.e. n>=9, the globally high index CANNOT be assembled using only these safe face cells; necessarily some genuine simplices/edges require five-coordinate or larger block exchanges across the entire central window.

***IMPORTANT PHYSICAL/TOPOLOGICAL DISTINCTION.*** K_x is the FLAG / FACE nerve on original permutation vertices, so an ABSTRACT GRAPH EDGE of K_x may connect vertices of a permutohedron face of dimension much HIGHER than one. Hence Corollary4 concerns the **ordinary polytope face dimension**, NOT the abstract simplicial dimension of an edge/simplex in K_x. A long-chord edge in the abstract packet graph can be incompatible even though each adjacent-transposition edge of the original permutohedron graph is compatible. It would be false to claim that the entire 3-skeleton of K_x automatically maps to E3. The accurate statement is: all actual vertices jointly carried by a face with blocks of size<=4 (or, more generally, central-noncrossing) are compatible; incompatibility first appears through a flexible order block spanning the ENTIRE 3-direction physical window.

**NEXT EXACT REPAIR PROBLEM.**
Prove that at every genuine endpoint-balanced pair pi,sigma in a CENTRAL-CROSSING five-direction block, the forced physical middle-three-face order values either yield an actual <=1-switch root/terminal connector, OR admit a witness-preserving replacement of the central selector by neighboring mono4/mono5 windows whose two-sided root boxes become compatible with the already selected boundary sheets. A repair law on these MINIMAL FIVE-DIRECTION ORDER-EXCHANGE CELLS, respecting Θ and actual physical faces, would be a concrete route to filling the high-index packet complex and closing grand NORI. No universal five-block repair law is proved here; the theorem locates the exact first obstructions and supplies a complete low-order facewise filling.
