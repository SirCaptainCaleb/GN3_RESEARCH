# Every root has a high-index permutohedral endpoint-opposition carrier and a real opposite-end full geodesic

# A canonical HIGH-INDEX permutohedral sphere for EVERY physical root: topological endpoint-opposition forcing in NORI

Fix n>=7 and a binary active NORI coloring of ordered physical 3-faces satisfying
  c(bar F,rev(i,j,k)) = 1-c(F,(i,j,k)).
Fix ANY cube root x∈Q_n. Every full n-edge cube geodesic from x is specified by a coordinate permutation pi=(p1,...,pn). Its L=n−2 consecutive actual ordered-three-face window colors are
  w_j(x,pi)∈{0,1}, j=1,...,L.
Let alpha(pi)=w_1(x,pi), beta(pi)=w_L(x,pi), and define the integral ENDPOINT IMBALANCE
  q_x(pi)=alpha(pi)+beta(pi)−1 ∈ {−1,0,+1}.
Thus q=0 iff the FIRST and LAST physical ordered-three-face colors are OPPOSITE.

**THEOREM 1 (literal NORI antipodality on the permutohedron).** Let P_n be the STANDARD (n−1)-dimensional permutohedron in the affine hyperplane sum_i t_i=n(n+1)/2, whose vertex indexed by pi has coordinates
  v_pi(i)=position of direction i in pi.
Its center is o=((n+1)/2,...,(n+1)/2), and reversing a permutation gives
  v_(rev pi)=2o−v_pi.
Therefore ∂P_n is an (n−2)-sphere with a FREE CENTRAL-ANTIPODAL action pi↦rev pi on its vertices.

For a FULL antipodal geodesic from root x, physical complement followed by path reversal has starting root
  bar(x xor [n])=x.
Its direction order is rev pi, and by ACTIVE NORI oddness the COMPLETE color word becomes complemented-reversed:
  w_j(x,rev pi)=1−w_(L+1−j)(x,pi).
Consequently
  q_x(rev pi)=−q_x(pi).
This uses actual physical ordered faces and does not assume a fictitious complement action on direction supports.

**THEOREM 2 (discrete endpoint-balance lemma: every root has a REAL opposite-end path).** For n>=7, an edge of the 1-skeleton of P_n corresponds to swapping two ADJACENT POSITIONS in the direction permutation. Such a swap changes AT MOST ONE of alpha(pi),beta(pi):
- the first physical three-face depends on the first three ordered directions (and on root x);
- the last physical three-face depends on the final three ordered directions and the SET of previously flipped directions;
- when n>=7 these first and last three-position blocks have at least one position separating them, and swapping adjacent entries cannot alter both physical faces simultaneously.
Hence for adjacent permutohedron vertices,
  |q_x(pi)−q_x(pi')|<=1.
The graph of P_n is connected. Starting at any pi with q≠0 and following an adjacent-transposition path to rev pi, whose q-value is −q, the integer-valued 1-Lipschitz q must pass through zero at some VERTEX. If q(pi)=0 already, stop. Therefore for EVERY starting root x there exists an ACTUAL full antipodal cube geodesic with opposite first and last ordered-three-face window colors.

Under hypothetical grand failure, every such actual endpoint-opposed full geodesic necessarily has at least THREE window-color changes, because its number of changes is ODD and at most one is prohibited. This provides a physically witnessed, antipodally invariant 'middle defect' on every root's full permutation space.

**THEOREM 3 (canonical HIGH INDEX endpoint-opposition zero carrier).** Define an odd piecewise-linear function F_x:∂P_n→R as follows. Use the barycentric subdivision of the proper nonempty face poset of P_n. At the barycenter b_H of a face H, set F_x(b_H) to the arithmetic MEAN of q_x(pi) over all ORIGINAL permutation vertices v_pi of H, and extend affinely over each barycentric simplex. Central inversion sends H→−H and q→−q, so
  F_x(−z)=−F_x(z).
At the original vertices F_x(v_pi)=q_x(pi).

Let Z_x=F_x^{-1}(0), the literal PL ZERO SET. It is closed, antipodally invariant, and admits a finite antipodally symmetric triangulation as a subpolyhedron. Let w be the first Stiefel–Whitney class of its free antipodal quotient double cover. Then
  w^(n−3) !=0 in H^(n−3)(Z_x/(±1);F2).
Equivalently, the cohomological Z2 index of the endpoint-opposition carrier Z_x is AT LEAST n−3, one dimension below the full permutohedron boundary's index n−2.

**Proof of index bound (relative cup-product form of Borsuk–Ulam).** More generally let S^d carry the antipodal action and let F:S^d→R be any continuous ODD map with zero locus Z. Suppose w^(d−1) vanished on Z/(±1). For our PL Z choose a sufficiently small invariant regular neighborhood U retracting equivariantly onto Z; then w^(d−1) vanishes on U/(±1). Choose a smaller invariant neighborhood U0 whose closure lies in U, and set B=S^d\U0, a closed invariant complement avoiding zeros. On B the SIGN of F defines an equivariant map to S^0, hence the double cover over B is trivial and w|B=0. In the quotient X=RP^d, the vanishing classes lift to relative classes in
  H^(d−1)(X,U/(±1)) and H^1(X,B/(±1)).
Their relative cup product represents w^d in H^d(X,(U∪B)/(±1))=H^d(X,X)=0. But w^d is the NONZERO top generator of H^d(RP^d;F2), contradiction. Therefore w^(d−1)|Z is nonzero. Apply d=n−2. QED.

**COROLLARY 4 (an EXACT topological grand-closure target).** Since ind(Z_x)>=n−3, there is NO antipodally equivariant continuous map Z_x→S^(n−4). Thus a TOPLOGICAL proof of GRAND NORI closure would follow if, under the hypothetical assumption that EVERY full geodesic has at least two changes, one constructs an honest antipodally equivariant LOW-SPHERE MAP
  Phi_x:Z_x→S^(n−4)
from the ordered-face change pattern, with all cellwise extensions justified by physical face/coordinate-swap combinatorics. Such a map would contradict Theorem3.

Concretely, at ACTUAL endpoint-opposed permutation vertices q_x(pi)=0, the color-change vector
  s_j(pi)=w_j(x,pi) xor w_(j+1)(x,pi), j=1,...,n−3,
has ODD Hamming weight, and in a hypothetical counterexample at least THREE 1s. Physical reversal sends this change vector to its position reversal, while keeping the root x fixed. The missing extraction step is to turn this equivariant MULTI-SWITCH LABELING into a continuous sphere map on ALL of Z_x (or a combinatorial Tucker complementary-edge certificate whose physical local repair yields a good path). Merely assigning switch labels at permutation vertices does NOT automatically define such a map on higher-dimensional faces; proving the extension is the essential combinatorial obligation INSIDE the high-index topological frame.

**CRITICAL COMPARISON WITH THE OLD PATH-HISTORY INDEX-ONE BARRIER.** The earlier NORI history-poset carrier has small Z2 index because its legal-prefix topology collapses. P_n is a DIFFERENT, canonically supplied, centrally symmetric convex polytopal COMPLETION of the set of all FULL direction orders, with index n−2 on its boundary. Its higher faces encode permutations and their swaps, NOT automatically compatible monochromatic paths. Theorem2 gives a literal actual geodesic at the FIRST zero-level because endpoint imbalance is 1-Lipschitz under legitimate adjacent swaps. Higher-dimensional Tucker extraction STILL requires additional physical-cell compatibility rather than treating arbitrary PL barycenters as real geodesics. This is the sharp, topology-first direction for global closure.

**Status.** Theorem1–3 and the conditional obstruction in Corollary4 are proved. Constructing the sphere map Phi_x or a valid combinatorial carrier extraction remains open; unrestricted grand NORI closure has NOT been obtained.

## Quantitative actual-path separator: at least n−1 endpoint-opposed full permutations per root

**THEOREM 5.** For every n>=7 and EVERY fixed physical cube root x, at least n−1 DISTINCT full antipodal ordered-direction geodesics rooted at x have opposite initial and final ordered-three-face window colors.

**Proof.** Let V_+, V_0, V_- partition the vertex set of the standard (n−1)-dimensional permutohedron P_n according to q_x(pi)=+1,0,−1. Reversal of direction order interchanges V_+ and V_- and preserves V_0. If V_+ is empty, then V_- is also empty, so ALL n! permutation vertices are in V_0 and the assertion is immediate. Otherwise both V_+ and V_- are nonempty. The proved 1-Lipschitz adjacent-swap property of q says there is NO permutohedron GRAPH EDGE directly between V_+ and V_-. Thus deleting V_0 disconnects the 1-skeleton of P_n into at least the two nonempty groups V_+, V_-. Balinski's elementary d-vertex-connectivity theorem for convex d-polytopes says the graph of P_n has vertex connectivity at least d=n−1. Hence |V_0|>=n−1. Every vertex in V_0 is one genuine full rooted cube geodesic with physically opposite endpoint colors. QED.

**Topology inside combinatorics.** The count is a direct finite shadow of the high-index endpoint-zero hypersurface: the genuine zero-LABELED vertices, not merely virtual PL zeros, form an antipodally invariant vertex separator in an (n−1)-connected polytopal graph. This strengthens the nonempty actual balanced-path theorem and quantifies a minimum amount of certified endpoint diversity at EACH root.

This theorem uses the classical convex-polytope graph connectivity result. It does not assert that any of these >=n−1 paths has only one change; under hypothetical grand failure each has at least THREE, an odd number. For a universal grand proof the endpoint-balanced high-index hypersurface must additionally force a defect-removal transition among its actual adjacent-swap witnesses.
