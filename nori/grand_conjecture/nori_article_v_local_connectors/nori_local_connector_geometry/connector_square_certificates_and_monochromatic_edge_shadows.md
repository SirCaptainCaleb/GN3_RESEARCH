# Connector square certificates and monochromatic edge shadows

# Connector square certificates and monochromatic edge shadows

A monochromatic four-geodesic passing through an edge or root square is a physical certificate: the neighboring ordered three-faces have equal color on one actual path. As those certificates are glued along their physical edges, a two-color shadow appears, with either a shared edge certified by both colors or a rigid one-color assignment. Local square combinatorics then constrains allowable extensions.

## Monochromatic six-edge hub geodesics from finite ordered-hypergraph Ramsey

Let \(c(F,\pi)\in\{0,1\}\) be ANY coloring of physical ORDERED three-dimensional faces in Q_n. We impose NO antipodal or reversal condition. Let \(N=R_3(6;64)\) denote any finite 64-color Ramsey number guaranteeing a monochromatic six-vertex subset in every 64-coloring of 3-element subsets of an N-element set.

**Theorem (unconditional six-edge monochromatic hub path).** For all \(n\ge N\), EVERY cube vertex z lies on a monochromatic cube geodesic of length SIX whose four ordered-three-face windows all contain z as a common physical vertex. In particular, for n>=N the maximum monochromatic-geodesic length is at least six, independently of the coloring.

**Proof.** Fix z and a fixed linear order on the n coordinate directions. To every 3-element set T={a<b<c}, assign its ordered-face **profile**
\[
\Phi_z(T)=\big(c(F(z;T),\pi):\pi\text{ ranges over all six permutations of }(a,b,c)\big)\in\{0,1\}^6.
\]
This gives at most 64 colors on triples of coordinate directions. By the definition of N, there is a six-element subset W={p1<...<p6} on which \Phi_z is constant on all C(6,3) three-subsets. In particular, for all increasing ordered triples of p's, the common ordered-face color is one fixed bit q.

Start at the cube vertex \(x=z\oplus\{p_1,p_2,p_3\}\), and traverse the six distinct coordinates in order p1,...,p6. The path is a six-edge geodesic, and after the first three edges it passes through z. Its four successive ordered-three-face windows have triples
\[
(p_1,p_2,p_3),\ (p_2,p_3,p_4),\ (p_3,p_4,p_5),\ (p_4,p_5,p_6).
\]
Each physical three-face contains z: the first ends at z, the last starts there, and the middle two pass through it. Hence all four are among the prescribed equal-color faces F(z;T), so every window color equals q. QED.

**Optimal hub-span observation.** All ordered three-edge windows of any L-edge geodesic share a common physical vertex precisely when their vertex-index intervals [0,3],[1,4],...,[L-3,L] have nonempty intersection. This requires L-3<=3, or L<=6. Thus the fixed-hub reduction to ONE ordered triple coloring can certify six-edge monochromatic paths but cannot by itself certify longer paths: an L>=7 path has no common vertex in all its three-face windows. Proving unbounded-length monochromatic geodesics therefore requires coherent color transport between distinct hub vertices, not merely a stronger Ramsey bound on one hub.

**General k-face extension.** For ordered k-face colorings, put N_k=R_k(2k;2^{k!}). If n>=N_k, every cube vertex z lies on a monochromatic 2k-edge geodesic with all k-edge windows passing through z. The proof labels each k-subset by its k!-entry ordered color profile and selects 2k coordinate directions with constant profile. The window intersection criterion is L<=2k.

**Relation to NORI.** For active ordered-three-face NORI, the resulting six-edge monochromatic path supplies an actual reachable terminal-two-tail support of size four from some root. This is a qualitative dimension-independent reachability-rank floor in very high dimensions, stronger than the universal four-edge seed. It does not force complementary reversed-tail support overlap and therefore does not prove grand closure.

## Exact realization of ALL feasible globally missing middle-direction-pair graphs by valid NORI colorings

Let n be any ODD integer >=13. Fix an arbitrary simple graph M on the n cube direction coordinates. The earlier necessary theorem nori_globally_absent_middle_pair_graph_disjoint_even_cycles_paths_20261008 proved that for ANY valid active NORI coloring the graph of unordered direction pairs which NEVER appear as a middle pair in any actual monochromatic directed four-edge geodesic has maximum degree at most TWO and no odd cycle.

**CONVERSE THEOREM (exact classification for odd n>=13).** Conversely, if M is ANY disjoint union of (possibly trivial) paths and EVEN cycles, there is a valid ACTIVE NORI coloring c of ordered PHYSICAL three-faces whose GLOBAL MISSING-MIDDLE-PAIR GRAPH is EXACTLY M. More strongly, it can be chosen independent of the exterior face bits, and for EVERY nonedge {b,c} of M, the physical square in directions b,c at EVERY cube vertex is certified by a genuine monochromatic centered four-edge cube geodesic. Thus its certified-square complex X_c is exactly the entire two-dimensional coordinate cubical skeleton of Q_n MINUS all squares whose free direction pair is an edge of M; all ordinary cube edges and vertices are included.

**Construction.** Alternately two-color the EDGES of each path or even cycle component of M so any two incident M-edges have opposite binary signatures q_e. Define a regular tournament bit f(u,v) on ordered distinct directions using a cyclic order of all n labels:
  f(u,v)=1 if (v-u mod n)∈{1,...,(n−1)/2}, else0.
Then f(v,u)=1-f(u,v); for each fixed direction v, each q∈{0,1} occurs on exactly (n−1)/2 inputs f(u,v) and likewise f(v,u).

Construct a direction-only ordered triple label h(a,b,c) on distinct directions:
- If the FIRST TWO positions (a,b) form a missing edge e∈M, require h(a,b,c)=1-q_e.
- If the LAST TWO positions (b,c) form a missing edge e∈M, require h(a,b,c)=q_e.
- If neither adjacent ordered pair is in M, put h(a,b,c)=f(a,c).

This is CONSISTENT when both (a,b) and (b,c) belong M, because they are incident and q_bc=1-q_ab, so the two forced values coincide. It is also reversal-odd: reversing a triple interchanges 'first pair' and 'last pair', with complementary forced bits; if no adjacent pair is missing, f flips. Thus c(F,(a,b,c)):=h(a,b,c) is a genuine active NORI coloring, independent of exterior assignment.

**Every pair in M is absent.** For missing inner ordered pair (b,c)∈M, and any distinct outer a,d, the first window of its centered four-geodesic has triple (a,b,c), where missing edge (b,c) occupies LAST TWO positions, hence color q_bc. The second window has (b,c,d), where that edge occupies FIRST TWO positions, hence color 1-q_bc. Therefore the path is never monochromatic in any physical hub. This also applies to reverse middle order since q is unoriented.

**Every other pair is certified everywhere.** Fix ordered middle pair (b,c) with {b,c}∉M. Choose outer a outside {b,c}∪N_M(b), and outer d outside {b,c}∪N_M(c). Each forbidden set has size at most 4 because deg M<=2. Thus the triples (a,b,c) and (b,c,d) have NO adjacent M-edge and both fall in the tournament-rule case, with colors f(a,c) and f(b,d). For a chosen bit q, the first candidate set has at least (n−1)/2−4 >=2 possible a with f(a,c)=q, and the second has at least two possible d with f(b,d)=q. Choose a≠d. The genuine centered four-direction path (a,b,c,d) then has both ordered-three-face windows of equal color q. Since h is independent of exterior bits, precisely the same certificate exists at EVERY hub z in Q_n. Thus exactly the M pair classes are globally absent.

**Topology of the genuinely certified square carrier.** The resulting X_c is antipodally invariant, contains the complete cube graph, and is connected with free cube-antipodal involution. If M is NONEMPTY, choose any missing pair e={i,j}∈M. Every included square has at least one of directions i,j FIXED (otherwise it would be an omitted {i,j}-square). Therefore coordinate projection X_c→∂[0,1]^2≅S1 on (i,j) is continuous and equivariant. Its antipodal-cover class w1 is nonzero by connectedness, yet w1²=0 by the circle factorization. Thus the equivariant cohomological index of X_c is exactly one for EVERY NONEMPTY feasible missing-pair pattern M.

If M is empty, X_c is the full cube 2-skeleton; it has the expected higher equivariant index (at least 2). Thus in actual NORI colorings the global absence of a SINGLE middle pair is sufficient to collapse the certified-square carrier's index to one—even if every other physical square is certified.

**Interpretive guardrail.** This is an *exact realization theorem for local MONOCHROMATIC FOUR-EDGE witness geometry*, not a constructed counterexample to the full one-switch grand conjecture. The dimension restriction 'odd n>=13' is a convenient sufficient condition for the cyclic regular-tournament filler; no necessity for that threshold is claimed. In particular, genuine path certifications of virtually every cube square plus antipodal symmetry alone cannot supply a universal index-two fixed-point proof. One would need to show grand NO-CLOSURE prohibits the missing-pair phenomenon, or use a relative/higher-memory carrier with additional long-path constraints.

## Strengthened realization: the same coloring can have a monochromatic FULL antipodal geodesic from EVERY cube root

There is a strengthening of the exact-realization theorem that is crucial when interpreting its low-index certified-square complex: choose the cyclic regular tournament order **adaptively**, using a Hamiltonian cycle in the COMPLEMENT of M.

Because every vertex in the missing-pair graph M has degree at most2, the complement graph G=K_n\M has minimum degree at least n−3. For odd n>=13 this is at least n/2. By the classical Dirac Hamilton-cycle theorem (or its standard elementary longest-cycle proof), G has a Hamiltonian cycle. Fix its directed cyclic order
  p1,p2,...,pn,p1.
Define the regular tournament filler f with RESPECT TO THIS CYCLIC ORDER (rather than an arbitrary labeling of directions by Z_n), exactly as in the preceding construction. All degree and uniformity arguments remain valid.

Every consecutive pair {p_t,p_(t+1)} of this cyclic order belongs to G, hence is NOT a prescribed missing pair. Consequently for the full direction permutation pi=(p1,...,pn), each consecutive ordered triple (p_t,p_(t+1),p_(t+2)) has no adjacent missing-pair edge. Its prescribed window color is therefore the FALLBACK rule
 h(p_t,p_(t+1),p_(t+2)) = f(p_t,p_(t+2))=1,
since its first and last directions are forward cyclic distance2 (which lies in the tournament's positive half for n>=5). This holds for EVERY 1<=t<=n−2.

Thus **EVERY ONE of the 2^n possible starting roots** gives a FULL antipodal geodesic along this same pi whose ENTIRE ordered-three-face window word is monochromatic 1. Reversing direction order gives monochromatic 0 by active odd reversal. The certified-square carrier STILL has exactly the desired missing-pair graph M and, when M is nonempty, STILL has equivariant index exactly1.

This supplies a particularly strong sanity check: authentic full monochromatic NORI geodesics can coexist with an arbitrarily dense yet index-one local certified-square complex. Therefore fixed-point proofs must use topology informed by long witnesses or the no-closure hypothesis; no bare local-square index argument can distinguish successful colorings from potential counterexamples.


## Witness-root cubical domination, and why a global single-valued reachability label is impossible

Let n>=5 and color actual physical ORDERED three-faces of Q_n by bits; antipodal reversal oddness is imposed only for the explicit obstruction example below. Define
  R_4={x in Q_n : there exists a genuine monochromatic FOUR-EDGE directed cube geodesic ROOTED at x}.
No requirement is placed on prescribed terminal directions in this coarse root set.

**THEOREM 1 (root-witness dominating set, all binary colorings).** Every physical cube vertex z has an ACTUAL cube neighbor x∈R_4. Equivalently, R_4 dominates the entire cube graph Q_n. In particular
  |R_4|>=ceil(2^n/(n+1)).
More precisely for each hub z there is a physical 2-dimensional ROOT SQUARE Q_root consisting entirely of starting vertices for the SAME ordered monochromatic four-edge word with identical ordered physical three-face windows, and one of the square's four vertices is a neighbor of z.

**Proof.** The centered five-direction odd-cycle theorem (proved separately in NORI; needs no NORI antipodal oddness) supplies at z some genuine monochromatic CENTERED four-edge path with ordered distinct direction word (a,b,c,d). Its start root is r=z xor {a,b}. Both consecutive physical ordered three-face windows of this path have free coordinates b,c. Therefore as proved in the middle-root-square lemma, the SAME two physical faces in the SAME order are traversed for every starting root
  r xor H, H⊆{b,c}.
All four starting vertices belong to R_4. In particular r xor b=z xor a is a CUBE NEIGHBOR of z. Since z was arbitrary, R_4 is dominating. Each chosen root in R_4 dominates at most n+1 cube vertices including itself, so |R_4|(n+1)>=2^n, yielding the cardinality bound. QED.

**THEOREM 2 (sharp qualitative warning: R_4 need not equal the whole cube even under ACTIVE NORI).** For every n>=6 and every PRESCRIBED physical cube root x, there exists a genuine binary coloring of ORDERED PHYSICAL 3-faces satisfying the active NORI axiom
  c(bar F,reverse pi)=1-c(F,pi)
such that NO FOUR-EDGE ordered cube geodesic rooted at x is monochromatic. In particular x∉R_4.

**Construction and proof.** For each physical ordered three-face (F,pi) let T be its three free coordinates. Define its *exterior Hamming distance from x* as
  d_x(F)=#{i∉T: fixed exterior bit of F in coordinate i differs from x_i}.
There are n−3 exterior coordinates. Prescribe color0 on ALL ordered physical 3-faces with d_x(F)=0, and color1 on ALL ordered physical 3-faces with d_x(F)=1, regardless of the direction order pi. These prescriptions are compatible with NORI antipodal-reversal-oddness when n−3>=3: under the face antipode, d_x(bar F)=(n−3)−d_x(F), so the antipodal mate of a 0-layer face lies at distance n−3>=3 and is unprescribed, while the mate of a 1-layer face lies at distance n−4>=2 and is unprescribed. No prescribed face lies in the reversal orbit of another prescribed face. Complete the remaining antipodal-reversal orbit colors freely, always setting mate colors complementary.

Now take ANY four distinct directions (a,b,c,d) and its genuine rooted four-edge path starting at x. Its FIRST ordered three-face (a,b,c) contains root x, so has d_x=0 and color0. Its SECOND ordered three-face (b,c,d) begins after direction a was flipped; since a lies outside {b,c,d}, the physical face's exterior bits differ from x on EXACTLY coordinate a, so it has d_x=1 and color1. Therefore every rooted four-path at x has the two-window word (0,1), hence NONE is monochromatic. QED.

**Topological architecture implication.** The center-based certified-square complex X_c has ALL physical cube vertices and genuine middle-pair squares and is connected under active NORI; each certified centered four-path also generates a separate FULL 2-face in the space of STARTING ROOTS. The union of these genuine root-squares projects to a DOMINATING vertex set, but not necessarily to all of Q_n. One may therefore build a multivalued/witnessed topological cover using closed vertex stars of these root-squares, rather than assume every physical root has a monochromatic rank-two terminal label. However thickening a witness square to cover an adjacent root does NOT turn that adjacent root into a genuine four-path witness: the combinatorial incidence/face-provenance must be retained in a carrier before applying Tucker, cubical Sperner, or KKM.

**Scope.** This does not force full grand closure; it identifies the precise geometric amount of universal local reachability and disproves the too-strong claim that every root admits even a four-edge monochromatic start in all valid colorings. The correct topological object is a supported/multivalued root-chart complex with honest certificates.

The color shadow is not a substitute for the original ordered faces. Any global conclusion must be lifted from its certified edges to a single full path retaining the correct order of overlapping three-windows.
