# Exact moving-hub shift zigzags, certified root squares and full-path cut-energy identity

# Exact moving-hub shift representation and its certified root squares

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


**Audit addendum (physical good-window quotient, 2026-10-09).** The "certified root squares" in Theorem 3 are squares ONLY in the redundant hub-coordinate PARAMETER graph. Toggling either shared free direction b or c fixes BOTH underlying ordered physical faces, so the four hub-chart comparisons all project to ONE and the SAME edge of the actual good-window complex W_good. Therefore these squares are DEGENERATE after physical-face identification and must NEVER be counted as nondegenerate 2-cells, an annulus, or evidence for a mixed cup product in W_good. The first genuine exterior-root transport (toggle a direction e outside {a,b,c,d}) is the six-window hexagon completely classified in proved Item nori_exterior_root_transport_hexagon_exact_good_triangles_rigidity_dichotomy_20261009. Its local triangles may fail simultaneously; when present they collapse across free chord edges and leave an induced S1. This addendum sharpens the precise scope of the earlier state-space observation while preserving its pointwise identities and averaging theorem.
