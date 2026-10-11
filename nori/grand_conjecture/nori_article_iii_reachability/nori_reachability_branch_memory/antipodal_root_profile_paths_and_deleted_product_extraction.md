# Antipodal root-profile paths and deleted-product extraction

# Antipodal root-profile paths and deleted-product extraction

An antipodal root-profile construction seeks a path in a mixed-sign interface between complementary monochromatic support labels. Reachable support families need not form Boolean downsets, and the root-bit fiber of a partial path may have nontrivial dimension. The following propositions state the exact topological and combinatorial conditions under which a profile coincidence is extractable.

## Geodesic reachability regions are accessible but NOT Boolean downsets, even with antipodal oddness

Let Q_n be an UNDIRECTED binary edge-colored cube satisfying c(bar e)=1−c(e). As usual let R(x) consist of endpoints of monochromatic geodesics from x, allowing either color, including x. For each root x define the reachable coordinate-support family
\[
\mathcal R_x=\{S⊆[n]:x⊕S∈R(x)\}.
\]

**THEOREM 1 (accessibility).** For every nonempty S∈\mathcal R_x, there exists at least one i∈S with S\{i}∈\mathcal R_x. In fact a witness monochromatic shortest path for S certifies every prefix of its specific direction order.

**Proof.** A shortest x→x⊕S path changes every coordinate of S once. Deleting its last edge leaves a monochromatic geodesic from x to x⊕(S\{i}) for the last direction i. Repeat for prefixes. QED.



*The exact Boolean-downset counterexample is documented in a linked research note.*

## EXACT second-index criterion for a two-shore carrier with one contractible shore: an antipodal path IN THE OVERLAP

Let X be a finite simplicial or regular CW complex with a free cellular involution τ and a decomposition X=A∪τA by subcomplexes. Put C=A∩τA and assume A is NONEMPTY and CONTRACTIBLE (as an ordinary space). If C is empty, put index0. Otherwise the following conditions are EQUIVALENT:

(i) The first Stiefel–Whitney class w=w1(X→X/τ) has NONZERO square w²≠0 in H²(X/τ;F2), i.e. the cohomological antipodal index of X is AT LEAST TWO.

(ii) Some connected component C0 of the overlap C is invariant under τ: τ(C0)=C0.

(iii) The ONE-SKELETON of C contains a physical/abstract vertex u and a finite edge path from u to its involution mate τu.

(iv) There exists a continuous τ-equivariant map g:S¹→C (with antipodal half-turn on S¹).

**Proof (i→ii).** This is the previously proved general upper-index two-shore theorem nori_index_two_forces_antipodal_path_in_bichromatic_edge_overlap_20261008: if all C components occur in τ-exchanged pairs, assign ±1 to the two partners, producing an equivariant map C→S⁰; extend it over A to one closed semicircle and by τ over τA to the opposite semicircle, giving X→S¹. Such a map forces w²=0. Contraposition yields (i→ii).

**Proof (ii→iii).** Since C is a finite CW complex, its connected components are path-connected. Choose any vertex u in the τ-invariant component C0. Its mate τu is a vertex of the SAME component. A path in a CW complex can be homotoped into the 1-skeleton without altering endpoint vertices; cells of dimension>=2 do not join different components of the 1-skeleton. Hence u and τu are connected by an edge path entirely in C.

**Proof (iii→iv).** Parametrize an edge path γ:[0,1]→C from u to τu. Define g on the circle R/(2Z) by
  g(t)=γ(t), for 0<=t<=1;
  g(t)=τγ(t−1), for 1<=t<=2.
The two formulas match at t=1, because γ(1)=τu=τγ(0); they match at the identified endpoints t=0 and2 because τγ(1)=u. They also obey g(t+1)=τg(t), so g is a continuous equivariant S¹→C map.

**Proof (iv→i).** Since A is contractible, the composite g:S¹→C⊂A is ordinary nullhomotopic and extends to a disk G:D²→A. Apply the team's proved equivariant equator-capping theorem nori_equivariant_witness_equator_capping_raises_antipodal_index_20261008: glue G on the upper hemisphere of S² to τG on the lower hemisphere. This produces an equivariant map S²→X. The induced quotient RP²→X/τ pulls w back to the nonzero generator a∈H¹(RP²;F2), so w² pulls back to a²≠0. Thus w²≠0. QED.

**Exact NORI mixed-root PROFILE application (under the hypothetical absence of grand closure).** Let Ω be the ordered-terminal-pair/support label alphabet with involution τ(J,U)=(reverse J, D_J\U). For every physical root x, let L_x⊆Ω be the labels of ACTUAL either-color MONOCHROMATIC geodesic branches from x with terminal ordered pair J and preterminal support U. Let
  A=⋃_x Δ(L_x),
  K=A∪τA,
  C=A∩τA = ⋃_(x,y) Δ(L_x∩τL_y).
The universal one-coordinate 3-edge monochromatic branches give a common singleton-support apex to EVERY Δ(L_x), making A a CONE, hence contractible. The active grand conjecture is equivalent to C containing an edge {u,τu}, in which case the midpoint is fixed; so under a hypothetical no-closure assumption K carries a FREE τ-action. The exact criterion above yields:

  w1(K/τ)²≠0
  **IF AND ONLY IF**
  there exist label u∈Ω and a finite graph path
       u=u0—u1—...—um=τu
  in the 1-skeleton of the GENUINE mixed root-profile interface C.

Each edge ui—u_(i+1) of this graph lies in some simplex Δ(L_x∩τL_y), and thus has an explicit pair of physical-root witnesses certifying BOTH of its labels as monochromatically reachable from one root x and their complemented reversed-tail labels as reachable from a possibly other root y. The graph path need not retain a SINGLE common root along its successive edges; hence it does NOT automatically give a grand witness, nor is its endpoint u,τu necessarily an edge of C. The distinction between a τ-CONNECTING PATH and the desired τ-PAIR EDGE is the exact remaining combinatorial/topological shortening problem.

**Topological significance.** The second-index condition for the exact K carrier has become a FINITE GRAPH REACHABILITY question over real certified labels, not a mysterious abstract cup product. Higher w powers still require higher-dimensional overlap information; the equivalence established here is SPECIFICALLY for the nontrivial square w². No unconditional existence of an interface connecting path is claimed.

## Exact witness-root fiber dimension and the correct antipodal-reversal action in 2n-bit root/support geometry

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

Deleted-product or equivariant index information becomes a closure theorem only after establishing that the selected simplex represents two physically compatible monochromatic tails. The converse obstruction examples explain the necessary hypotheses.
