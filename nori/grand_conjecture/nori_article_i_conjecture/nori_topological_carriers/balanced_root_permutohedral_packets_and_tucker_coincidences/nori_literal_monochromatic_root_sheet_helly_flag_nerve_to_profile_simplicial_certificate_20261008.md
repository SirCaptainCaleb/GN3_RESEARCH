# Literal monochromatic root sheets satisfy Helly-2, and their flag nerve maps simplicially onto NORI reachability

# Exact cubical Helly witness-root nerve and simplicial passage to NORI root profiles (topology with literal physical provenance)

Let n>=4 and c be any binary coloring of physical ordered 3-faces, optionally satisfying active NORI reversal oddness. Consider any genuine MONOCHROMATIC directed k-edge geodesic, 3<=k<=n, with distinct direction order pi=(p1,...,pk), starting at root x. Let W_j be its jth ordered-three-face free direction set and
  M(pi)=intersection_j W_j={p_(k−2),...,p_3} for 3<=k<=5, empty for k>=6.
By item nori_exact_middle_window_root_fiber_dimension_and_root_support_antipodal_action_20261008, changing root bits precisely in M(pi) preserves the ENTIRE sequence of ordered physical face windows. Define the LITERAL CERTIFIED ROOT SHEET
  F(P)={ x XOR h : supp(h)⊆M(pi) }⊆{0,1}^n.
Geometrically its ordinary convex hull |F(P)| is an axis-aligned (possibly zero-dimensional) cubical FACE of the standard real cube [0,1]^n, and all its cube vertices certify the SAME actual monochromatic path direction order with same physical window faces. For k=4 these are honest 2-faces of ROOTS, for k=5 edges, for k>=6 vertices.

**THEOREM 1 (strong 2-Helly property of genuine rooted path sheets).** For ANY finite collection of such path sheets F(P_1),...,F(P_s), if EVERY PAIR has a common literal cube root, then ALL s sheets have one COMMON literal cube root. In fact
   ⋂_i F(P_i)
is a coordinate subcube of Q_n, and |⋂_i F(P_i)|=2^h for some h>=0.

**Proof.** Each F(P_i) specifies a subset E_i⊆[n] of FIXED coordinates and a bit assignment b_i:E_i→{0,1}. For two coordinate subcubes, their intersection is nonempty iff the prescribed bits agree on E_i∩E_j. Pairwise intersections therefore force a CONSISTENT bit assignment on the union ⋃E_i. Assign these collectively prescribed bits and choose arbitrary values on unprescribed coordinates. This yields a common binary root. The resulting intersection fixes precisely the union ⋃E_i and leaves h=n−|⋃E_i| free coordinates, giving exactly 2^h common roots. QED.

**THEOREM 2 (actual root-sheet nerve is a FLAG complex, and its topology is physical).** Let S be any finite family of distinct physical-window mono-geodesic sheets. Form the nerve N_root(S): its vertices are sheets P∈S and a finite collection spans a simplex iff the corresponding root sets F(P) have a COMMON literal root. By Theorem1 this is the CLIQUE/FLAG complex of its pairwise-intersection graph. Every simplex carries at least one REAL common starting cube vertex, with ALL its member path certificates simultaneously valid; no convex averaging of binary root coordinates is involved.

Moreover the geometric union U(S)=⋃_(P∈S) conv(F(P)) is a finite union of cubical faces of [0,1]^n. Every nonempty finite face intersection is a contractible cubical face, so by the ordinary finite good-cover nerve lemma (or a direct barycentric subdivision face-poset carrier argument) the nerve N_root(S) is ordinarily HOMOTOPY EQUIVALENT to U(S). Thus its topology reflects actual overlapping physical root faces rather than invented high-dimensional simplices.

**THEOREM 3 (surjective simplicial certificate map to the exact positive reachability carrier).** Restrict the family S to actual monochromatic terminal branches of length k>=3 whose last two ordered direction coordinates form a tail J=(a,b) and whose used prefix before the tail has nonempty PROPER support U⊊D_J. Map each root-sheet vertex P to its formal exact terminal memory label
   λ(P)=(J,U)∈Omega.
Then λ induces a SIMPLICIAL MAP
   λ:N_root(S)→A=⋃_(x∈Q_n)Delta(L_x),
where L_x is the genuine either-color monochromatic terminal memory profile.

**Proof.** If sheets P_1,...,P_s span a simplex, Theorem1 supplies one LITERAL common physical starting root x. Each path can be rerooted at this x without changing its physical window faces or mono color, so each label λ(P_i) belongs to THE SAME genuine profile L_x. Hence their labels form an allowed simplex in A. This proves simpliciality, including possible duplicate labels (collapsed simplices). If S comprises ALL genuine monochromatic terminal-branch sheets with eligible support, then λ is SURJECTIVE ON ALL SIMPLICES: any simplex {u1,...,us}⊆L_x is witnessed by choosing one actual mono-geodesic rooted at x for each ui; their root sheets all contain x and their images are exactly that simplex. QED.

**CRITICAL EQUIVARIANCE WARNING (not a minor technicality).** Physical antipodal reversal of a k-edge path with used support W sends its root x to x XOR ([n]\W) and its ordered direction word to its reversal; it also changes the terminal direction memory to the reverse of its OLD FIRST directions, and the formal label tau(J,U)=(rev J,D_J\U) is NOT generally its physical reversal. Two different paths have different unused supports, so their root-square sheets are shifted by DIFFERENT exterior vectors under physical reversal. This does not preserve the pairwise root-intersection relation in general. Consequently, while λ:N_root(S)→A is a genuine simplicial map, it is NOT automatically a map of free-Z2 complexes. Treating the ordinary root-sheet nerve as an antipodal topological carrier without repairing this involution would invalidate a Tucker/Borsuk–Ulam proof.

**RESEARCH OUTLOOK.** This establishes an honest topology WITH COMBINATORICS INSIDE: a flag witness complex whose simplices are certified by literal common roots, together with a simplicial surjection onto the exact positive root-profile nerve carrier A. For global closure, construct an augmented memory/repair complex linking these sheets so the formal complementary-reversed-tail tau action becomes an honest free involution ON THE CARRIER, while retaining the Helly same-root extraction; or instead work directly in C=A∩tau A and use the root-sheet model to prove its connectivity/homology. The existing full-root parity no-go shows why a carrier built from one chosen root alone cannot suffice.
