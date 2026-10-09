# Ordered-r-face path root fibers have dimension max(2r-k,0); antipodal reversal complements only unused root bits

# Exact witness-root fiber dimension and the correct antipodal-reversal action in 2n-bit root/support geometry

Fix 1<=r<=k<=n, a direction-distinct k-edge cube geodesic with starting root x∈F2^n and ordered direction word pi=(p1,...,pk), and an arbitrary coloring of the PHYSICAL ORDERED r-faces. Its (k−r+1) ordered-r-face windows have free-coordinate sets
  W_j={p_j,p_(j+1),...,p_(j+r−1)} for j=1,...,k−r+1.
Define
  M(pi)=intersection_{j=1}^{k−r+1} W_j
       ={p_(k−r+1),...,p_r} if k<=2r−1,
       =empty if k>=2r.
Then |M(pi)|=max(2r−k,0).

**THEOREM 1 (exact physical-face root-fiber).** For a root translation vector h∈F2^n, the SAME ordered direction word pi, now starting at x+h, has EXACTLY THE SAME physical ordered r-face windows in ALL positions as pi rooted at x IF AND ONLY IF supp(h)⊆M(pi). Thus the set of starting roots realizing a given fixed COMPLETE sequence of ordered physical window faces and orders is exactly one coordinate affine cube
  x+span{e_i : i∈M(pi)}
of dimension max(2r−k,0). Every arbitrary binary color-word predicate (monochromatic, at most one switch, prescribed pattern, etc.) is constant on this actual face-certified root fiber.

**Proof.** The physical face of window j along pi is fixed by the cube bits OUTSIDE W_j. Translating the original starting root by h changes that face's exterior bit assignment precisely on supp(h)\W_j, regardless of prefix flips (the same fixed prefix appears for both roots). Therefore that window's physical face remains unchanged iff supp(h)⊆W_j. This must hold for ALL windows, i.e. supp(h)⊆intersection_j W_j=M(pi). Sliding equal-length consecutive windows have common positions [k−r+1,r] when this interval is nonempty, yielding |M|=2r−k; otherwise the intersection is empty. QED.

**THEOREM 2 (EXACT physical antipodal reversal in root/support coordinates).** Let U={p1,...,pk} be the USED coordinate support, D=[n]\U its UNUSED complement, and let bar denote bitwise complementation of physical cube vertices. Applying physical antipodal complementation and reversing the vertex sequence of the directed k-geodesic sends
  (root x, direction order pi)
    --> (root x XOR D, direction order rev pi).
Indeed the original endpoint is y=x XOR U, so the reversed-complemented geodesic root is bar y=x XOR U XOR [n]=x XOR D. The USED support is PRESERVED, NOT COMPLEMENTED, whereas the UNUSED root bits in D are all complemented.

For an ACTIVE ordered-r-face NORI-type coloring satisfying
  c(bar F,rev sigma)=1−c(F,sigma),
the color word of the transformed path is the reverse and bitwise complement of the original color word, preserving the exact number of switches.

This action is an involution on the full finite ordered-path state set; for k>=2 it is FIXED-POINT-FREE because the ordered direction word cannot equal its reverse when all directions are distinct. For k=n, D is empty and the ROOT is fixed, so antipodal path reversal acts purely by reversing direction order—important for any supposed root-bit topological Tucker labeling. For k<n, it complements precisely the unused root-coordinate bits and not the used support bits.

**COROLLARY 3 (critical ordered-three-face ranks).** For r=3 the exact fixed-path root-fiber dimensions are
  k=3:3, k=4:2, k=5:1, and k>=6:0.
Thus each genuine mono4 witness carries an entire 2D square of equally certified root states; mono5 carries a single rooted edge; mono6 carries no nontrivial coordinate root translation preserving ALL of its physical window faces. This geometric rank collapse is independent of coloring complexity.

**COROLLARY 4 (proper anti-symmetry of root-square carriers).** For fixed pi with 3<=k<=5 and used support U, the antipodal-reversal map sends the physical root-fiber cube
  x+span(M(pi))
to
  (x XOR D)+span(M(pi))
paired with the reversed direction word rev(pi) and complementary reversed window colors. The middle root-coordinate set is unchanged by order reversal, M(rev pi)=M(pi). This gives a rigorously defined free equivariant pairing of SAME-DIMENSION witness-root cubes.

**TOPOLOGICAL RESEARCH CONSEQUENCE.** The natural geometrical "2n bits" consist of an n-bit root and an n-bit progress/used-support coordinate; physical antipodal reversal of an actual short path has the support-preserving but EXTERIOR-complementing form above. Tucker's required FULL sign-vector anticomplementarity must be attached to genuinely reversed EXTERIOR root coordinates (or a proven alternative involution), not casually to USED support. Building a high-index path carrier beyond k=6 therefore requires genuine *coordinate-order exchanges, root slides between different path certificates, or memory-compatible support insertions*; one cannot infer high-dimensional filling from a single fixed geodesic's root-face cube, because its exact physical fiber is a point at k>=6. This is a proved geometry/cubical-fiber statement, not grand closure.
