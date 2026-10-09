# Physical window-shift paths and root-shuttle transport

# Physical window-shift paths and root-shuttle transport

A moving root or adjacent direction exchange transports a physical ordered three-face through a graph of genuine window shifts. The shift graph carries the extra data that a coordinate-label-only model discards: fixed exterior bits, ordered free directions, and the actual root-square used in a shuttle. Antipodal routes in this graph admit explicit constructions and distance estimates.

THEOREM (EXACT LOCAL NO-GO FOR THE NAIVE PERMUTOHEDRAL GAP-SIDE LABEL). In Q7 there exists an ACTIVE NORI binary ordered-three-face coloring such that TWO full antipodal geodesics from the SAME root x=0000000, whose coordinate orders differ by ONE ADJACENT TRANSPOSITION, both have opposite first/last window colors and exactly THREE window-color changes, but the location of their unique EQUAL adjacent window pair lies on opposite sides of the middle. Hence the tempting +/- label on endpoint-balanced bad geodesics recording whether their unique equal seam belongs to positions {1,2} or {3,4} is NOT locally constant even along legal adjacent-swap edges that preserve endpoint balance. The local crossing does not by itself guarantee an at-most-one-switch witness.
EXPLICIT CERTIFICATE. Use coordinate directions 0,1,...,6 and root x=0. Let P have order p=(0,1,2,3,4,5,6), and prescribe its five genuine ordered 3-face window colors as (0,1,1,0,1), with its only equal adjacent pair at seam2. Let Q have order p'=(0,1,3,2,4,5,6), obtained by swapping positions3 and4, and prescribe its five ordered 3-face window colors as (0,1,0,0,1), with its only equal pair at seam3. Each word starts0 and ends1, and has exactly three changes; both are BAD in a hypothetical grand counterexample but locally do not themselves contradict closure. Their actual ordered face data, written as (ordered free triple; exterior fixed bits represented by the integer mask of coordinates fixed to1), are:
 P: (0,1,2;0)->0, (1,2,3;1)->1, (2,3,4;3)->1, (3,4,5;7)->0, (4,5,6;15)->1.
 Q: (0,1,3;0)->0, (1,3,2;1)->1, (3,2,4;3)->0, (2,4,5;11)->0, (4,5,6;15)->1.
The only EXACT common ordered physical face is the last (4,5,6;15), prescribed consistently color1. None of the other prescribed ordered faces is the antipodal physical face with REVERSED free-coordinate order of another prescribed face: if such a pair existed, their free triples would be reverse orders and their exterior masks would be complements on the four fixed directions, which the displayed list plainly excludes. Therefore the ten partial color assignments extend to a GLOBAL active NORI coloring by independently choosing colors for each remaining orbit under (F,pi)->(bar F,rev pi), and giving orbit mates complementary colors. This validates the example without any SAT or literature search.
LIMITATION OF EXAMPLE. The constructed full coloring MAY have other good one-switch geodesics; it is NOT a counterexample to NORI. It disproves only the asserted LOCAL CONTINUITY/NO-CROSSING statement for the simple zero-seam-side label on actual bad endpoint-balanced adjacent permutation vertices. A higher-index permutohedral proof must incorporate richer ordered-window certificates or a cellwise carrier, rather than depending on that one-bit label being locally constant.

## Two-step movable-root shuttles halve the antipodal window transport length

Let n>=5 and fix a distinguished direction i. Write W_z(a,i,b) for the ACTUAL physical ordered 3-face through vertex z with ordered free directions (a,i,b). Its physical identity depends only on the bits of z outside {a,i,b}. Let H_i denote the genuine four-edge window-shift graph retaining i in the two middle directions, as in Item nori_certified_square_complex_connected_antipodal_one_class_20261008.

**Lemma (exact two-step exterior-bit shuttle).** For distinct a,b,d,i,k, the two edges
 W_z(a,i,b) -- W_z(i,b,k) -- W_(z xor k)(d,i,b)
are genuine physical consecutive-window-shift edges of H_i. The first edge has full direction word (a,i,b,k), the second has (d,i,b,k) read backward. Their intermediate ordered physical face is literally the SAME because k belongs to its free triple, and its outside fixed bits coincide. More generally choose an arbitrary representative of the initial face differing in free coordinates, and the endpoint d-face can have its newly fixed a-bit freely selected. Replacing z xor k by z gives an equally valid two-step move that swaps the outer direction a→d without toggling k. Interchanging a,d reverses the construction.

**THEOREM (short antipodal path, all dimensions).** For each actual ordered window v=W_z(a,i,b), there exists an EVEN H_i path from v to its actual antipodal reversal tau v=W_(bar z)(b,i,a) of length at most
 L_n = 2n-2 if n is EVEN, and L_n=2n if n is ODD.
This path involves genuine physical ordered-face windows at every step; no abstract identification of distinct root charts is used.

**Proof.** Choose one buffer direction d outside {a,b,i}; let K=[n]\{a,b,i,d}, of size m=n-4>=1. Starting with W_z(a,i,b), process every k in K exactly once by the above two-edge shuttle, alternately replacing the left outer direction a by d and d by a, and toggling the exterior bit k. This costs precisely 2m window-shift edges. While d is free, its eventual exterior fixed bit on returning to a can be selected arbitrarily through the hub representative at the intermediate face: the intermediate (i,b,k) face has d as a fixed coordinate when the left outer is a, but after the a→d move, d is free, and can be set before the d→a move. Choose this d-bit to be the COMPLEMENT of its initial value on the last d→a transition. The original a-bit is free at both the initial and final a-middle windows and poses no constraint. The original exterior bits k∈K have each been toggled exactly once; the b and i free bits are irrelevant to the physical ordered face.

If m is even, the outer direction returns to a after 2m edges; the resulting physical face has the same free triple and order (a,i,b), with EVERY exterior bit in K∪{d} complemented. If m is odd, the outer direction is d; use one additional two-edge no-flip shuttle d→a with helper k_0∈K. This leaves the already flipped k_0 exterior bit unchanged and lets us choose the final d-bit as above. The exterior bits are now all complemented. Finally, at this fixed physical hub, swap the two outer free directions by three two-edge SAME-HUB direction replacements
 (a,i,b) -> (h,i,b) -> (h,i,a) -> (b,i,a),
where h is a third direction distinct from a,b,i; each arrow is a two-edge genuine window-shift path with a helper direction distinct from the four involved directions, possible because n>=5. This six-edge operation does not change the exterior bit assignment of the original {a,b,i} face. Hence we reach tau v with length
 2(n-4)+6 = 2n-2 if n even,
 2(n-4)+2+6 = 2n if n odd.
The length is even. QED.

**Quantitative corollary (strengthens Item nori_equivariant_window_shift_short_antipodal_path_many_middle_connectors_20261009).** Under active NORI oddness, write N_i for the number of DISTINCT monochromatic certified window-shift edges having i in their middle pair. Antipodal reversal pairs the two directional edge-orbits, so their good-edge counts agree, N_L=N_R. Let E0=2^(n-2)(n-1)(n-2)(n-3) be the exact number of edges in EACH oriented H_i orbit. For any path P of the above length L<=L_n, every translated-and-coordinate-permuted (fixing i) copy gP joins a face to its antipodal reversed mate in EVEN steps; because its endpoint colors are opposite, gP has at least ONE equal-color adjacent window pair. Orbit averaging yields
 1 <= E_g[# good edges on gP] = L*N_L/E0.
Consequently
  N_L=N_R >= ceil(E0/L_n),
  N_i >= 2*ceil(2^(n-2)(n-1)(n-2)(n-3)/L_n).
In particular n=5 gives N_i>=40, n=6 gives N_i>=192, n=7 gives N_i>=550. These are exponentially many actual monochromatic directed four-edge connectors per direction, with balanced i-middle orientations.

**Global forcing gap.** The two-step shuttles give exact coordinatewise physical root transport using ONE shared intermediate actual ordered face and a linear-length equivariant antipodal connector. This improves the previous 4n-6 path-length bound and its per-coordinate counting certificate. Nonetheless translated short paths may choose different good edges. The result gives a concrete local cross-root transition chart, but does NOT imply that these monochromatic connectors globally synchronize into one reversed-two-tail support collision or a full one-switch geodesic. The missing gluing theorem must relate edges selected from DIFFERENT translated shuttles while retaining full terminal two-direction and monochromatic run memory.

## Root-bit shuttle squares are literal induced 4-cycles with two forbidden diagonals

Fix n>=5 and four distinct directions a,i,b,k. For an actual physical cube vertex z, use the notation W_z(p,q,r) for the actual ordered three-face through z with ordered free directions (p,q,r). Put
  A  = W_z(a,i,b),
  B  = W_z(i,b,k),
  A' = W_(z xor e_k)(a,i,b),
  C  = W_z(k,a,i) = W_(z xor e_k)(k,a,i).
The equality in C holds because k is a free direction. A and A' are DIFFERENT actual physical ordered-face windows: k is fixed outside their common free triple and its bit is opposite.

**THEOREM (exact shuttle-square incidence, coloring-independent).** The four actual physical windows A,B,A',C are distinct and form an INDUCED FOUR-CYCLE in the full physical window-shift graph H_i:
 A--B--A'--C--A.
All four edges remain edges of W_good(c), the simplicial complex of jointly realizable <=1-switch geodesic windows, for EVERY binary physical ordered-three-face coloring c, because any consecutive two-window four-edge geodesic has at most one switch. However BOTH diagonals
 A--A' and B--C
are ABSENT even from the full color-free actual cooccurrence relation on direction-distinct geodesics. In particular the induced W_good complex on these four windows is exactly a C4 with NO 2-simplex. Neither local triangular subdivision of this square on its four vertices is valid.

**Proof of the four edges.** A and B are the two consecutive actual windows of an ordered four-edge path with direction word (a,i,b,k) centered through z. Because B is FREE in k, it is the SAME ordered physical three-face when represented by z xor k, so B and A' are also consecutive actual windows of another path with the same four-direction order (a,i,b,k). Likewise C and A are consecutive windows with word (k,a,i,b), and C and A' are consecutive windows with that same order represented by z xor k. Every comparison has i in the shared middle pair. Thus these are four literal sector H_i shift edges.

**Proof of the forbidden diagonals.** A and A' have identical ordered free-direction triples (a,i,b) but are distinct physical faces. Along any direction-distinct geodesic, the unordered free triples of windows at different positions are distinct: equality would repeat at least one direction. Thus no genuine path contains BOTH A,A'. For B and C, the ordered free triples are respectively (i,b,k) and (k,a,i); they share exactly the two free directions {i,k}. If two windows with a two-direction free overlap occur along a direction-distinct geodesic, their window positions must differ by exactly one, and their ordered triples must have a literal two-letter de Bruijn overlap, either the final two directions of B equaling the initial two of C or vice versa. Here (b,k)!=(k,a) and (a,i)!=(i,b). Hence no such path contains BOTH B,C. The induced 4-vertex complex has exactly the four claimed edges and no diagonals or triangles. QED.

**Alternating obstruction is ACTUALLY REALIZABLE in active NORI.** Assign c(A)=c(A')=0 and c(B)=c(C)=1. These are valid independent face assignments: none of the four displayed ordered physical faces is the antipodal reversed mate of another (the potential pair A/A' has different ordered orientation under reversal since a!=b; B/C have different free triples). Therefore extend to a legal GLOBAL active coloring by assigning complementary colors to all physical antipodal-reversal mates and choosing any colors on remaining orbits. In this coloring the shuttle 4-cycle has NO monochromatic window-shift edge at all (all four compare unequal colors), although its four literal good-window-complex edges remain available as at-most-one-switch four-geodesics. In particular an arbitrary centered shuttle square need not yield a single good connector, nor can its two transport orders be merged into a good-window triangle using only these four windows.

**Global interpretation.** The optimal-length antipodal root transport theorem (Item nori_exact_optimal_antipodal_window_shift_transport_length_and_density_20261009) constructs sector routes as sequences of genuine shifts. Its binary endpoint-parity forces an ODD number of monochromatic edges on the complete antipodal path, but this local 4-cycle shows why the elementary root-bit-shuttle relation cannot be filled automatically in W_good. A prospective beta*w pentagon annulus must recruit ADDITIONAL physical ordered windows and actual common <=1-switch geodesic certificates. The present no-go is local and sharp: it rules out the naive four-vertex triangular filler, not arbitrary longer annuli or the full NORI conjecture.

Short antipodal transport and abundant monochromatic short connectors do not force a monochromatic or one-switch full path unless the successive transported windows are simultaneously certified by compatible geodesics.

## Recent witness refinement

# Root-bit shuttle squares are literal induced 4-cycles with two forbidden diagonals

Fix n>=5 and four distinct directions a,i,b,k. For an actual physical cube vertex z, use the notation W_z(p,q,r) for the actual ordered three-face through z with ordered free directions (p,q,r). Put
  A  = W_z(a,i,b),
  B  = W_z(i,b,k),
  A' = W_(z xor e_k)(a,i,b),
  C  = W_z(k,a,i) = W_(z xor e_k)(k,a,i).
The equality in C holds because k is a free direction. A and A' are DIFFERENT actual physical ordered-face windows: k is fixed outside their common free triple and its bit is opposite.

**THEOREM (exact shuttle-square incidence, coloring-independent).** The four actual physical windows A,B,A',C are distinct and form an INDUCED FOUR-CYCLE in the full physical window-shift graph H_i:
 A--B--A'--C--A.
All four edges remain edges of W_good(c), the simplicial complex of jointly realizable <=1-switch geodesic windows, for EVERY binary physical ordered-three-face coloring c, because any consecutive two-window four-edge geodesic has at most one switch. However BOTH diagonals
 A--A' and B--C
are ABSENT even from the full color-free actual cooccurrence relation on direction-distinct geodesics. In particular the induced W_good complex on these four windows is exactly a C4 with NO 2-simplex. Neither local triangular subdivision of this square on its four vertices is valid.

**Proof of the four edges.** A and B are the two consecutive actual windows of an ordered four-edge path with direction word (a,i,b,k) centered through z. Because B is FREE in k, it is the SAME ordered physical three-face when represented by z xor k, so B and A' are also consecutive actual windows of another path with the same four-direction order (a,i,b,k). Likewise C and A are consecutive windows with word (k,a,i,b), and C and A' are consecutive windows with that same order represented by z xor k. Every comparison has i in the shared middle pair. Thus these are four literal sector H_i shift edges.

**Proof of the forbidden diagonals.** A and A' have identical ordered free-direction triples (a,i,b) but are distinct physical faces. Along any direction-distinct geodesic, the unordered free triples of windows at different positions are distinct: equality would repeat at least one direction. Thus no genuine path contains BOTH A,A'. For B and C, the ordered free triples are respectively (i,b,k) and (k,a,i); they share exactly the two free directions {i,k}. If two windows with a two-direction free overlap occur along a direction-distinct geodesic, their window positions must differ by exactly one, and their ordered triples must have a literal two-letter de Bruijn overlap, either the final two directions of B equaling the initial two of C or vice versa. Here (b,k)!=(k,a) and (a,i)!=(i,b). Hence no such path contains BOTH B,C. The induced 4-vertex complex has exactly the four claimed edges and no diagonals or triangles. QED.

**Alternating obstruction is ACTUALLY REALIZABLE in active NORI.** Assign c(A)=c(A')=0 and c(B)=c(C)=1. These are valid independent face assignments: none of the four displayed ordered physical faces is the antipodal reversed mate of another (the potential pair A/A' has different ordered orientation under reversal since a!=b; B/C have different free triples). Therefore extend to a legal GLOBAL active coloring by assigning complementary colors to all physical antipodal-reversal mates and choosing any colors on remaining orbits. In this coloring the shuttle 4-cycle has NO monochromatic window-shift edge at all (all four compare unequal colors), although its four literal good-window-complex edges remain available as at-most-one-switch four-geodesics. In particular an arbitrary centered shuttle square need not yield a single good connector, nor can its two transport orders be merged into a good-window triangle using only these four windows.

**Global interpretation.** The optimal-length antipodal root transport theorem (Item nori_exact_optimal_antipodal_window_shift_transport_length_and_density_20261009) constructs sector routes as sequences of genuine shifts. Its binary endpoint-parity forces an ODD number of monochromatic edges on the complete antipodal path, but this local 4-cycle shows why the elementary root-bit-shuttle relation cannot be filled automatically in W_good. A prospective beta*w pentagon annulus must recruit ADDITIONAL physical ordered windows and actual common <=1-switch geodesic certificates. The present no-go is local and sharp: it rules out the naive four-vertex triangular filler, not arbitrary longer annuli or the full NORI conjecture.
