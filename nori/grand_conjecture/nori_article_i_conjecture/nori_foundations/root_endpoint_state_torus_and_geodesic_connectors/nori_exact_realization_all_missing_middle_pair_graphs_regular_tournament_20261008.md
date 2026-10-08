# Every feasible globally missing connector-pair graph is exactly realizable by active NORI for odd n≥13

# Exact realization of ALL feasible globally missing middle-direction-pair graphs by valid NORI colorings

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
