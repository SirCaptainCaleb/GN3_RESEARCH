# Exact equivariant two-sided NORI root-sheet nerve: grand iff fixed point; no-grand index is 3 or 4

# EXACT TWO-SIDED HELLY NERVE OF PHYSICAL NORI PATH WITNESSES — GRAND FIXED POINT AND UNIVERSAL INDEX-FOUR CEILING

Let n>=6 and let c be ANY active binary NORI coloring of actual physical ORDERED 3-faces, c(bar F,rev π)=1−c(F,π). Let P range over ALL ACTUAL directed direction-distinct cube geodesic PATH STATES (root + direction word) of length k between 3 and n inclusive whose consecutive physical ordered-three-face windows have AT MOST ONE color change. (Length3 is always admitted, since its word has one color.) Let ΘP be the physical antipodal complement and vertex-sequence reversal; Θ preserves this path class and is a fixed-point-free involution on its VERTICES.

For each admitted rooted P=(x,π), define its exact certified root sheet
 S(P) = x + span_F2{e_i:i belongs to every ordered-three-face window of π}.
Its real cubical hull |S(P)|⊂[0,1]^n is an axis-aligned coordinate face of dimension m(k)=max(6−k,0), and EVERY binary root in S(P) produces the SAME entire sequence of physical window faces in the SAME direction order and hence the same <=1-switch property. This is the exact physical-face fiber theorem of nori_exact_middle_window_root_fiber_dimension_and_root_support_antipodal_action_20261008. We reuse S for both its finite vertex set and its real cubical hull when no ambiguity arises.

Define the TWO-SIDED PHYSICAL CERTIFICATE BOX
   B(P)= |S(P)| × |S(ΘP)| ⊂ [0,1]^(2n).
It is a coordinate product box of dimension 2m(k)<=6. Let
   U = ⋃_(admitted P) B(P)
and define the actual two-sided HELLY NERVE E whose vertices are the admitted path states P and whose simplices are the finite families σ with ⋂_(P∈σ) B(P) nonempty.

THEOREM 1 (honest flag complex with the CORRECT physical involution). Any family of coordinate product faces of [0,1]^(2n) is 2-Helly: pairwise intersection implies whole-family intersection, because each intersection condition is consistency of prescribed 0/1 values on fixed coordinates. Hence E is the FLAG (clique) complex of its genuine pairwise box-intersection graph. Every E simplex is certified simultaneously by one REAL starting cube root for its original path states and one REAL starting root for all their Θ-images; unlike convex averaging, both roots may be chosen Boolean because the intersection box is a coordinate face. The involution Θ is SIMPLICIAL, since
   B(ΘP)=swap(B(P)),  swap(a,b)=(b,a).
The finite convex-box nerve lemma applies equivariantly: E is Θ-equivariantly homotopy equivalent to U with its factor-swap involution. One can construct the equivariant map E→U explicitly on barycentric subdivision: to the barycenter of a nerve simplex σ assign the coordinate center of ⋂_(P∈σ)B(P); nested simplices have their centers inside the smallest intersection, so linear interpolation stays in U. Every map commutes with swap. The reverse nerve map can be built using sufficiently small swap-symmetric open thickenings of the finitely many coordinate boxes, their contractible intersections, and an equivariant partition of unity.

THEOREM 2 (EXACT grand closure fixed-point equivalence). The following are equivalent:
 (i) there is a FULL n-edge antipodal geodesic of c with at most one window-color change;
 (ii) the geometric union U intersects the swap-fixed DIAGONAL {(r,r):r∈[0,1]^n};
 (iii) E has a Θ-fixed point;
 (iv) E has an edge joining one path state P to its physical Θ-image ΘP.

PROOF. Let W be used directions of P, D=[n]\W. Physical reversal sends its root x to x XOR D and its order to rev π. Every coordinate i∈D is fixed in S(P) to bit x_i and fixed in S(ΘP) to bit 1−x_i. Hence if D nonempty, the two sheets S(P),S(ΘP) are disjoint. If D empty, W=[n], the starting roots of P and ΘP are THE SAME, and their middle-coordinate root-sheet translation sets are identical under reversal, so S(P)=S(ΘP). Thus B(P) meets the diagonal iff P is a FULL good path, and B(P)∩B(ΘP) nonempty iff P is FULL. This proves (i)⇔(ii)⇔(iv). An opposite edge has Θ-fixed midpoint. Conversely a Θ-fixed point in the nerve has a Θ-INVARIANT minimal supporting simplex; any vertex P in that simplex has ΘP there too, forcing their intersection B(P)∩B(ΘP) and hence a FULL good path. QED.

THEOREM 3 (NONSPURIOUS odd unused-sign labeling, with honest simplicial cells). Define the signed-unused-coordinate vector η(P)=bar(endpoint(P))−root(P)∈{-1,0,+1}^n. As previously proved, η(ΘP)=−η(P), and η_i(P) is nonzero precisely for UNUSED coordinate i. For any simplex σ of E, the original sheets S(P), P∈σ, have a COMMON ACTUAL ROOT r. Whenever coordinate i is unused in P and Q it is fixed in both S(P),S(Q), so r_i=x_i(P)=x_i(Q), hence η_i(P)=η_i(Q). Thus NO E simplex ever contains both +1 and−1 at the same coordinate: E is SIGN-COHERENT. Its affine η-map E→R^n is Θ-ODD, and its zero is a LITERAL FULL admissible path certificate, not a spurious averaged coincidence.

THEOREM 4 (the universal index-FOUR CEILING: short physical root sheets cannot supply an index-n proof). Assume the GRAND conjecture FAILS, hence no admitted path is full, U is off the diagonal and swap acts FREELY. Let U_3 be the union of boxes B(P) for length-THREE (one-window) paths. These paths are automatically admitted for EVERY ordered triple, root, and physical exterior assignment. Consequently
 U_3 = ⋃_(W⊂[n], |W|=3; exterior bits ε∈{0,1}^([n]\W))
        F_W(ε) × F_W(1−ε),
where F_W(ε) is the full 3-dimensional root coordinate face with bits ε fixed outside W. This is coloring-independent.

Put δ(a,b)=b−a. Each 3-path box has δ_i=±1 outside its three free directions and arbitrary δ_i∈[−1,1] in those three directions. Hence δ(U_3) is PRECISELY the THREE-SKELETON X_3=(∂[−1,1]^n)^(3) of the centrally antipodal cube boundary. The map
  s(δ)=((1−δ)/2,(1+δ)/2)
is an equivariant section X_3→U_3 of δ. The homotopy keeping δ fixed and moving the midpoint (a+b)/2 linearly to (1/2,...,1/2) remains IN THE ORIGINAL BOX: outside W the two bits are already complementary endpoints, while inside W both coordinates are free. Thus U_3 Θ-equivariantly STRONGLY deformation retracts onto the section s(X_3).

The free antipodal three-skeleton X_3 has cohomological Z2 index EXACTLY 3 for n>=4. Upper bound: dim X_3=3. Lower bound: X_3/Θ is the 3-skeleton of ∂[−1,1]^n/Θ≅RP^(n−1), with its ordinary quotient cubical CW structure. Inclusion of a CW 3-skeleton into RP^(n−1) induces an INJECTION in H³(F2), so the third power of the first antipodal-cover class survives.

Now every LONGER admitted path (k>=4) has root-sheet dimension m(k)<=2, so B(P) has dimension at most FOUR (k=4:4; k=5:2; k>=6:0). The finite union U is a Θ-invariant cubical CW complex obtained by attaching to U_3 ONLY cubical cells of dimension <=4 (some attachments may share faces), hence its free-action quotient (U/Θ,U_3/Θ) has no relative cochains above degree4. Therefore H^j(U/Θ,U_3/Θ;F2)=0 for j>=5. Since U_3/Θ≃X_3/Θ has no cohomology above degree3, the long exact pair sequence gives
   H^j(U/Θ;F2)=0 for ALL j>=5.
So ind_Z2(U)<=4. Conversely U_3⊂U has w_1^3≠0, so ind_Z2(U)>=3. By equivariant nerve equivalence E≃_Θ U,
   3 <= ind_Z2(E) <= 4.
This is UNIFORM in cube dimension n and in the physical NORI coloring under the grand no-closure assumption.

**CRUCIAL TOPOLOGICAL CONSEQUENCE.** The universal 3-face geometry furnishes exactly a genuine index-3 antipodal base, and longer fixed-window root sheets can raise it at most to index4. For n>=5, the exact signed-unused Tucker closure criterion demands index>=n to force a zero in R^n. Therefore NO argument operating solely on the static two-sided root-invariance boxes of certified <=1-switch paths can provide such a high-index proof. To reach the unrestricted GRAND NORI conjecture, one MUST adjoin genuinely NEW topological cells coming from ORDER/PREFIX EXCHANGES, WITNESS-PRESERVING TRANSPORT, root/support memory holonomy, or higher-dimensional compatible repairs whose equivariant topology is not captured by the boxes. The theorem is an exact constructive carrier and an exact sharp dimensional NO-GO, not a counterexample to grand NORI.
