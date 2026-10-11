# Near-midpoint hub witnesses and concrete splice-failure tests

# Near-midpoint hub witnesses and concrete splice-failure tests

High-index permutation arguments force authentic endpoint-opposed geodesics and central physical-face interactions near the midpoint of the cube. The core question is whether such witnesses can be cut and reassembled along a common actual vertex without creating too many new window-color changes. The local connector calculations below keep all four possible splices, not just an abstract sign coincidence.

## A genuine two-seam splicing law at a common physical hub; locally rigid bichromatic hubs automatically repair both seams

Let n>=6, and let c be ANY binary coloring of physical ORDERED three-faces of Q_n. Let P and Q be two genuine full directed antipodal cube geodesics rooted at SAME physical vertex x, with direction words
\[
P=(a_1,\ldots,a_\ell,b_1,\ldots,b_{n-\ell}),\qquad
Q=(a'_1,\ldots,a'_\ell,b'_1,\ldots,b'_{n-\ell}),
\]
for some 3<=ell<=n-3, and suppose their first-ell used-direction sets coincide:
\[
\{a_1,\ldots,a_\ell\}=\{a'_1,\ldots,a'_\ell\}=S.
\]
Thus BOTH pass at time ell through the SAME physical cube vertex y=x⊕S. ALL FOUR paths obtained by choosing either prefix and either suffix are genuine full antipodal geodesics, because the first block uses S and second block uses its coordinate complement.

**THEOREM 1 (exact physical two-window splice).** Given any prefix A with last directions (u,v) and any suffix B with first directions (w,t), the ordered-three-face color word of their full splice A B is
\[
\boxed{\operatorname{Int}_3(A),\
c(F(y;\{u,v,w\}),(u,v,w)),\
c(F(y;\{v,w,t\}),(v,w,t)),\
\operatorname{Int}_3(B).}
\]
Here \operatorname{Int}_3(A) is the actual color word of the ell-2 ordered three-face windows entirely inside A, and \operatorname{Int}_3(B) is the actual color word of the n-ell-2 windows entirely inside B, preserving each branch's physical face identities. In particular BOTH NEW splice windows are actual ordered physical three-faces THROUGH THE SAME PHYSICAL INTERMEDIATE VERTEX y; they are not virtual/interpolated colors.

**Proof.** All windows wholly before/after the cut preserve precisely the same physical exterior bits, because both choices of prefix reach the same y. There are exactly two crossing windows of ordered directions (u,v,w) and (v,w,t). Their physical first vertices lie respectively at y⊕u⊕v and y⊕v, so each corresponding free-face contains y. This is the displayed formula. QED.

**THEOREM 2 (automatic seam compatibility at a locally rigid bichromatic hub).** Assume additionally that y is a bichromatic hub in the LOCAL UNIQUE-CERTIFIED-COLOR case of Item nori_every_bichromatic_hub_local_shared_edge_or_uniform_mixed_cap_dichotomy_20261008. Let A_y,B_y be its genuine certified incident direction color classes, with assigned bits h(i)∈{0,1}. Suppose the LAST prefix direction v belongs to A_y∪B_y, the FIRST suffix direction w belongs to A_y∪B_y, and their certified bits differ:
\[
h(v)\ne h(w).
\]
Then regardless of the neighboring directions u,t, the two actual crossing window colors are
\[
\boxed{c(F(y;\{u,v,w\}),(u,v,w))=h(v),\quad
c(F(y;\{v,w,t\}),(v,w,t))=h(w).}
\]
This follows DIRECTLY from the proved local mixed-middle selector at y: in each ordered triple, the MIDDLE direction has a neighboring free direction in the opposite certified color class.

**COROLLARY 3 (actual full one-switch extraction from compatible monochromatic branches).** Under Theorem2, suppose A is a genuinely MONOCHROMATIC ell-edge geodesic from x to y of ordered-window color h(v), and B is a genuinely MONOCHROMATIC (n−ell)-edge geodesic from y to bar x of ordered-window color h(w). Then their full concatenation P=A B is a full antipodal directed geodesic with ordered-face window-color word
\[
h(v)^{\ell-1}\ h(w)^{n-\ell-1},
\]
and hence has EXACTLY ONE change. It works regardless of the direction order in the rest of A or B.

**COROLLARY 4 (exact additive defect formula for nonmonochromatic branches).** Under Theorem2, suppose the LAST internal ordered window of A has color h(v), and the FIRST internal ordered window of B has color h(w), but their other windows may change. Let d_A,d_B be the number of changes in their respective internal window-color words. Then the full spliced word has
\[
\boxed{D(A B)=d_A+d_B+1.}
\]
Indeed the two new splice windows match their adjacent internal side colors and differ exactly once from one another. Thus local hub certification supplies a ZERO-EXCESS connector: there are NO uncontrolled seam changes. In particular, if d_A=d_B=0, grand closure is immediate.

**RELATION TO THE TOPOLOGICAL TUCKER PAIR.** Item nori_odd_dimension_permutohedral_tucker_common_vertex_opposite_mirror_switch_pair_20261008 proves unconditionally, in EVERY odd n>=7 and at EVERY root x, TWO actual endpoint-opposed full paths P,Q sharing some proper interior vertex y and carrying opposite mirrored switch labels. Theorem1 now turns this topologically forced common vertex into an ACTUAL two-seam geodesic rectangle, with both seam colors lying in physical faces through y. If y is a locally rigid bichromatic hub and the boundary directions of one of the four splice combinations cross the certified A_y/B_y cut with matching adjacent window colors, then Corollaries3-4 give exact switch-controlled extraction/defect bookkeeping. Such additional properties of y or the splice do not follow automatically from the Tucker pair theorem and remain the outstanding GLOBAL COMBINATORIAL task.

**Scope.** Theorem1 uses no NORI antipodal law; Theorem2 uses physical hub rigidity proved under ACTIVE NORI. The topological pairing and the one-switch extraction are both rigorous but their unconditional conjunction is NOT proved. No claim of unrestricted grand closure is made.

## Kneser forces a same-root, same-center, two-sided reversal square of genuine six-edge geodesics

Let n>=8 and let c be ANY binary coloring of actual physical ORDERED 3-faces of Q_n, not necessarily satisfying antipodal oddness. Fix ANY physical cube vertex z. For each ordered triple alpha=(a,b,c) of distinct direction names, define h_z(alpha) to be the physical color of the ordered 3-face through z with ordered free directions alpha.

**Theorem (unconditional centered six-edge two-sided reversal square).** There exist DISJOINT unordered direction triples A,B with ordered orientations alpha=(a1,a2,a3) on A and gamma=(b1,b2,b3) on B, and two bits q,r∈{0,1}, such that
\[
h_z(\alpha)=h_z(\operatorname{rev}\gamma)=q,\qquad
h_z(\operatorname{rev}\alpha)=h_z(\gamma)=r.
\tag{1}
\]
Consequently from the ONE SAME ROOT x=z XOR A to the ONE SAME ENDPOINT y=z XOR B there exist FOUR ACTUAL six-edge direction-distinct geodesics:
\[
P_{00}=(\alpha,\operatorname{rev}\gamma),\quad
P_{01}=(\alpha,\gamma),\quad
P_{10}=(\operatorname{rev}\alpha,\operatorname{rev}\gamma),\quad
P_{11}=(\operatorname{rev}\alpha,\gamma).
\tag{2}
\]
All four traverse the SAME physical hub z at their midpoint after three moves, and ALL FOUR physical ordered-three-face window faces of EVERY path contain z. Their initial/final ordered-window color pairs are the complete two-by-two table
\[
\begin{array}{c|cc}
 &\operatorname{rev}\gamma&\gamma\\
\hline
\alpha&(q,q)&(q,r)\\
\operatorname{rev}\alpha&(r,q)&(r,r)
\end{array}.
\tag{3}
\]
In particular the two diagonal paths P00 and P11 each have either ZERO or EXACTLY TWO ordered-window color changes (since their four-window color words begin and end with the same bit). The other two have opposite endpoint colors precisely when q≠r. NO conclusion is asserted about the two interior window bits or the existence of a monochromatic/one-switch SIX-edge path.

**Proof.** Associate to each unordered 3-set T the pair (h_z(alpha_T),h_z(rev alpha_T)), for an arbitrarily selected orientation alpha_T. Orientation reversal interchanges the two bits. Up to this interchange there are exactly THREE orbit types: 00,11,{01,10}. Thus the unordered 3-subsets of [n] are colored with THREE types. The classical Kneser chromatic theorem gives chi(KG(n,3))=n-4>3 for n>=8, so two DISJOINT triples A,B have the same orbit type. Reorient alpha and gamma so that the second triple signature is the SWAPPED signature of the first, yielding precisely the two equations (1). For n>=10 one may avoid the named Kneser input and instead use the elementary cyclic-interval disjoint-triple count already proved in Item nori_same_order_antipodal_root_pairs_endpoint_opposition_disjoint_triple_orbits_20261008.

Every word in (2) uses the same six distinct directions A union B, first the A directions then B, so from root x=z XOR A each reaches z after 3 moves and then ends at y=z XOR B. The four length-three free-coordinate windows begin at path positions1,2,3,4. In window1 the already fixed directions outside the first triple are still at their z-bits, because root differs from z only in the three FREE A bits. In windows2,3 the remaining untraversed A directions are still the only differing bits from z and are FREE in the window. After the third move the path is at z; window4 is the B-face through z. Hence ALL four physical face windows contain z. Their first and last ordered free triples are just the selected A and B orientations; (1) gives their color pairs (3). An even-parity number of changes follows for a four-bit word whose first/last bits agree, so the diagonal words have 0 or2 changes. \(\square\)

**Topology-first significance.** This creates at EVERY physical hub a literal four-vertex square in the space of genuine SAME-root/SAME-endpoint six-edge paths, indexed by two INDEPENDENT reversals of 3-direction prefix/suffix blocks. Unlike a fixed-root pair of unrelated endpoint-balanced full paths, these four certificates have a COMMON midpoint z and complete agreement of their used support. The input is a TOPLOGICAL Kneser coloring obstruction with only three signature orbits. Under active NORI oddness the four-path square also has the usual physically antipodal mate centered at bar z with complemented-reversed ordered windows.

The unresolved step is to transport this certified six-edge square through the other n−6 directions, using physical face incidence/root slides, so that an equivariant fixed-point collision produces a complete n-edge path with ≤1 change. The diagonal endpoint-equality condition alone is weaker than monochromaticity, and cannot be inflated to a global grand result without controlling the two middle seam windows and later exterior-bit changes.


## Exact moving-hub shift representation and its certified root squares

**Setting.** Let n>=5. For any binary coloring C of physical ordered three-faces of Q_n, define its hub table h_z(a,b,c)=C(F(z;{a,b,c}),(a,b,c)), where z is a cube vertex and a,b,c are distinct coordinate directions.

**Theorem 1 (complete hub coordinates).** The tables satisfy h_(z xor e_t)(a,b,c)=h_z(a,b,c) for t in {a,b,c}. Conversely any family with these invariances defines a unique physical ordered-three-face coloring. Its active NORI antipodal oddness is precisely h_(bar z)(c,b,a)=1-h_z(a,b,c).

Proof: toggling a free coordinate leaves its physical face unchanged, and any two points of a face differ only in free coordinates. The antipodal face contains bar z and reverses the ordered free tuple under the axiom.

**Theorem 2 (EXACT PATHWISE moving-hub identity).** For ANY full rooted geodesic (x,p), p=(p_1,...,p_n), let z_i=x xor e_(p_1) xor ... xor e_(p_i) and t_i=(p_i,p_(i+1),p_(i+2)) for i=1,...,n-2. If w_i denotes its ACTUAL physical ordered-three-face window color then
  w_i=h_(z_i)(t_i),
  h_(z_i)(t_(i+1))=h_(z_(i+1))(t_(i+1)),
and consequently each switch indicator is
  w_i xor w_(i+1)=h_(z_i)(p_i,p_(i+1),p_(i+2)) xor h_(z_i)(p_(i+1),p_(i+2),p_(i+3)),  i=1,...,n-3.
These are pointwise equations for EACH path, independent of any averaging or choice of a different witness.

Proof: the i-th physical window, with free directions t_i, contains both z_(i-1) and z_i, so its color is h_(z_i)(t_i). The hubs z_i,z_(i+1) differ in p_(i+1), which belongs to the free set of t_(i+1), so invariance gives the second identity.

**Exact admissible zigzag model.** Use states (z,t), z a cube vertex and t an injective ordered triple. Horizontal arrows at fixed z shift (a,b,c) to (b,c,d), d distinct; vertical arrows flip a coordinate in the fixed triple t, preserving h exactly. Each genuine full n-edge geodesic yields the zigzags
 (z_i,t_i) -> (z_i,t_(i+1)) -> (z_(i+1),t_(i+1))
for i=1,...,n-3, where the second arrow flips p_(i+1). Its switches are precisely its color-changing horizontal arrows. A valid zigzag must also come from one globally injective length-n direction word and coherent root x; arbitrary walks in this enlarged graph do not automatically encode cube geodesics. Grand closure is exactly existence of an admissible full zigzag with <=1 color-changing horizontal arrow.

**Theorem 3 (two certified commuting root directions).** The switch bit s_z(a,b,c,d):=h_z(a,b,c) xor h_z(b,c,d) is unchanged when z is toggled in coordinate b, c, or both. Thus each horizontal arrow has a geometrically certified square of four parallel horizontal comparisons over the 2-dimensional root face on {b,c}, with identical switch values. Toggling a changes the physical (b,c,d)-face while leaving the (a,b,c)-face fixed, and toggling d changes the physical (a,b,c)-face while leaving the (b,c,d)-face fixed; the geometry alone imposes no analogous invariance for a or d.

Proof: the two ordered triples share exactly their middle two directions {b,c}. Invariance of both face colors under toggling either shared coordinate proves the equalities. The remaining toggles change exactly one of the two actual physical faces; its color can be independently prescribed (with antipodal reversed mates fixed by the NORI axiom).

**Corollary (a rigorous limitation on automatic pentagon annuli).** A centered physical shift pentagon on five distinct coordinates p_0,...,p_4 uses ordered face triples t_i=(p_i,p_(i+1),p_(i+2)) modulo five. Their five free sets have EMPTY intersection. Therefore no nonzero coordinate toggle is guaranteed by the physical-face invariance to preserve every vertex color of the pentagon at once. Merely tensoring a centered pentagon with a fixed root-direction edge is not a universally certified product annulus; any successful antipodally transported good-window annulus must allow nonuniform root/order repair with literal shared path certificates. This is a limitation of the automatic face-preserving operation, not a theorem forbidding other annuli.

**Theorem 4 (exact full-switch mean equals same-hub graph cut energy).** Define
 A(C)=[2^n*(n)_4]^{-1} sum_{z in Q_n} sum_{(a,b,c,d) injective} 1{h_z(a,b,c)=h_z(b,c,d)},
where (n)_4=n(n-1)(n-2)(n-3).
For a uniform root X and uniform direction permutation P,
  E[D(X,P)]=(n-3)*(1-A(C)),
where D is the number of color changes among its n-2 physical window colors. Moreover A(C)>=1/5 for any binary physical ordered-three-face coloring, without NORI oddness.

Proof: for every fixed switch position i, (z_i,p_i,p_(i+1),p_(i+2),p_(i+3)) is uniform over all cube vertices and injective ordered quadruples: conditioned on P, the map X->z_i is a bijection. The pathwise identity makes the probability of an equality exactly A(C), independent of i. Summation gives the expectation. To prove the lower bound, at each fixed hub z form the directed shift graph G_n: vertices are injective ordered triples and arcs are injective ordered quadruples (a,b,c,d) from (a,b,c) to (b,c,d). Every cyclic ordered 5-tuple of distinct directions yields a directed odd pentagon, necessarily containing at least one equal-color arc. There are (n)_5/5 distinct directed pentagons and each arc belongs to n-4 of them. Hence at least (n)_4/5 arcs are equal-colored at each hub, so A(C)>=1/5. This recovers the team's universal E[D]<=4(n-3)/5 theorem by an exact moving-hub graph calculation.

**Research frontier.** The pointwise hub identities and the 2-direction commuting root squares are genuine, dimension-independent local chart transitions. They give a concrete means to seek coherent moving-hub higher cells, linking the physical pentagon parity cocycle and the exact same-root complementary reversed-two-tail extraction. The full proof still requires a global certificate-preserving selection/holonomy/descent that synchronizes horizontal equalities along ONE admissible n-coordinate zigzag. The mean and the local commuting squares alone do not provide that selection; unrestricted grand NORI closure remains open.

**Theorem 5 (a universal genuine ROOT-MOVING essential seven-cycle).** Fix ANY five distinct directions (a,b,c,d,e), ANY physical hub z and ANY physical ordered-three-face coloring in n>=5. In the actual good-window shift graph (hence inside W_good) there is the following SEVEN-VERTEX SIMPLE CYCLE. Write [T;y] for the actual ordered face with ordered free triple T passing through hub y:
 u_0=[(a,b,c);z],
 u_1=[(b,c,d);z],
 u_2=[(c,d,e);z xor b],
 u_3=[(d,e,a);z xor b xor d],
 u_4=[(e,a,b);z xor b],
 u_5=[(a,b,c);z xor e],
 v=[(b,c,e);z].
Then
  u_0 - u_1 - u_2 - u_3 - u_4 - u_5 - v - u_0
is a cycle of SEVEN DISTINCT actual ordered physical windows. EVERY edge is the pair of consecutive ordered windows of an actual directed four-edge cube geodesic and therefore is genuinely certified as a W_good edge for EVERY coloring. It contains BOTH ordered (a,b,c)-faces with exterior e-bit differing by one.

Proof (literal intermediate hubs). For the first five edges the common actual hubs are, in order:
 z, z xor b, z xor b xor d, z xor b, z xor b xor e.
The ordered triple pairs are respectively
 (abc,bcd), (bcd,cde), (cde,dea), (dea,eab), (eab,abc).
Every pair shares the last two directions of the first tuple with the first two of the second, and its two face objects really pass through the stated common hub. Invariance in the free directions verifies all displayed hub representatives agree. For the last two edges, [(a,b,c);z xor e] and [(b,c,e);z] both pass through z xor e on their respective physical faces (e is free for the latter), and [(b,c,e);z] and [(a,b,c);z] share hub z. Their order as undirected shift edges is legitimate. Every such pair has the explicit four-edge certificate with direction order of the corresponding shift, starting at hub XOR its first direction. All listed vertices are pairwise distinct: the only repeated ordered direction triple is (a,b,c), and those two ordered physical faces differ in exterior bit e. QED.

**Nontrivial integral-mod-two temporal homology.** Every edge in this literal seven-cycle has physical face-center L1-distance one, so the established intrinsic temporal cocycle beta(edge)=distance mod2 evaluates to 7=1 in F2. Since beta extends as a genuine 1-cocycle on all W_good simplices, this cycle C_7 is NOT a boundary of any 2-chain in W_good and is nonzero in H_1(W_good;F2). Likewise the same-color connector cocycle alpha=beta+delta(color) evaluates to 1. In active NORI, the cycle projects to a closed path in W_good/tau with beta_bar=1 and covering voltage w=0 (it already closes upstairs).

**Exact exterior sensitivity parity.** Let E_j be the equality indicator (1 for equal colors, 0 otherwise) on the seven consecutive edges. Telescoping the endpoint color differences around the FIVE-edge segment u_0 -> ... -> u_5 yields
 sum_{j=0}^{4} E_j = 1 + h_z(a,b,c) + h_(z xor e)(a,b,c)   (mod 2).
Along the TWO-edge bridge u_5 -> v -> u_0, one has
 E_5+E_6 = h_z(a,b,c)+h_(z xor e)(a,b,c) (mod 2).
The sum around all seven edges is therefore 1, as required. This makes a cross-root physical-face derivative visible through a genuine five-window transport, while its two-edge shortcut canonically closes an odd homology cycle. The seven-cycle itself is a graph 1-cycle and DOES NOT supply a certified two-dimensional annulus, a cup product, or a full n-geodesic.

**Suggested next implication to prove.** Search for actual W_good triangles allowing two such exterior-bit seven-cycles on distinct coordinates d,e to commute through good-window path homotopies. Any resulting certified annular transport around an antipodal root loop would activate the team's proved beta_bar cup w forcing criterion. The current theorem provides explicit, universally valid root-mobile one-dimensional cycles and common physical hubs for that search, but does not establish commuting homotopies or grand closure.




*The scope-specific limitation and complete proof are preserved in linked research note note_fixed_hub_six_square_end_face_extension_failure.*
