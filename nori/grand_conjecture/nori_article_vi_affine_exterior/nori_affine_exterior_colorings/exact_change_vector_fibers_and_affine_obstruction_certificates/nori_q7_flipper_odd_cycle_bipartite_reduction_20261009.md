# Exact g-third extraction as a 480-vertex odd-cycle forcing problem

# Exact odd-cycle reduction of seven-dimensional one-flipper NORI

Let R be six coordinate directions, and let g be a seventh universal exterior flipper in an antipodally reversal-odd physical ordered-three-face coloring. Write c=x_g+f for faces omitting g; then f is complement-reversal even on residual Q_6. Let h be the restriction to faces containing g, complement-reversal odd.

A *packet* is a six-coordinate starting root y on R and an order (a,b,c,d,e,f) of R, with the full seven-coordinate order (a,b,g,c,d,e,f). Its three g-containing window colors form
G(y,p)=(h(a,b,g),h(b,g,c),h(g,c,d)).
Let A(y,p),B(y,p) denote the genuine residual ordered-three-faces (c,d,e),(d,e,f), using their actual prefix-toggled exterior bits. The full color word is (G_1,G_2,G_3,z+f(A),z+f(B)) for freely selected z∈F_2.

Let V be the 480 complement-reversal orbits of residual ordered physical three-faces, and let Γ_h be the undirected multigraph on V with an edge [A][B] for every packet (y,p) whose G word has exactly one change. Loops are allowed; equivalently, a loop is an odd cycle of length one.

**Lemma (exact graph-theoretic extraction).** For each fixed legal h, the following are equivalent:

(i) Some complement-reversal-even residual coloring f produces no good full seven-geodesic with g as the third move, for any starting root.

(ii) Every packet G(y,p) is nonconstant, and Γ_h is bipartite (in particular loopless).

**Proof.** If G is constant, choose z so its fourth color equals G_3; then its trailing fifth color adds at most one change, giving a good geodesic for every f. If G has exactly one change, a good full geodesic exists for some z precisely when f(A)=f(B). If G alternates, its first three colors have two changes, so every completion is bad. Consequently simultaneous failure for both g-start bits at all packets is exactly the conjunction: (a) all G are nonconstant and (b) f(A)≠f(B) on every Γ_h edge. An assignment of binary f-values respecting the even involution is exactly a 2-coloring of the vertices V. Condition (b) is solvable iff Γ_h is bipartite. QED.

**Finite odd-cycle forcing statement (computer-tested).** Every complement-reversal-odd h on the g-containing faces satisfies: either a packet G is constant, or Γ_h has an odd cycle. This is equivalent to unsatisfiability of the exact 1200-variable CNF certificate in Item nori_q7_universal_exterior_flipper_computer_verified_full_closure_20261009 (the 720 h-variables plus the 480 vertex-bipartition f-variables). The completed SAT computation returned UNSAT; a conceptual odd-cycle argument and independent SAT proof certificate remain desirable.

**Proof strategy.** The full physical adjacent-window graph on residual faces contains genuine odd pentagons from five-direction cyclic shifts. The color-dependent Γ_h retains exactly those local adjacency edges whose g-window triple is one-switch. The desired all-h theorem is an odd-cycle survival principle: antipodal oddness of h forces a constant G or a surviving odd cycle in Γ_h. Seek a small physically realized pentagon or an equivariant graph-cycle argument. This formulation isolates the color-dependent topological carrier needed for all-dimensional extensions.
