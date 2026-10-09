# Exact NORI root-profile second-index criterion: a mixed-interface path joins complementary reversed-tail labels

# EXACT second-index criterion for a two-shore carrier with one contractible shore: an antipodal path IN THE OVERLAP

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
