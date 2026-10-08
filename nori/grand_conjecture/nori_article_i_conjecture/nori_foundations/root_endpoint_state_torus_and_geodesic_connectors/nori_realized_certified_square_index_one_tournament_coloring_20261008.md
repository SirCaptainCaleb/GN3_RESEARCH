# Real NORI coloring realizes complete-minus-one-pair certified squares and index one

# An ACTUAL active NORI coloring realizes the dense low-index square-complex no-go model exactly

For every ODD n>=13 choose two distinguished cube directions i,j (distinct). Identify all n directions with cyclic group Z_n, and define an antisymmetric regular tournament color f(a,c)∈F2 for a≠c:
 f(a,c)=1 iff (c-a mod n) belongs to {1,...,(n-1)/2}; otherwise f(a,c)=0.
Thus f(c,a)=1-f(a,c). For each fixed vertex v and each q=0,1, exactly (n-1)/2 outer directions a have f(a,v)=q, and exactly (n-1)/2 directions d have f(v,d)=q.

Define a coloring h(a,b,c) of ORDERED TRIPLES of distinct cube directions as follows:
(1) When the exceptional pair {i,j} occupies the FIRST TWO ordered positions, set h(i,j,a)=h(j,i,a)=1.
(2) When {i,j} occupies the LAST TWO ordered positions, set h(a,i,j)=h(a,j,i)=0.
(3) On every other ordered triple (including triples with i,j separated by a middle direction, as well as triples containing zero or one distinguished direction), set h(a,b,c)=f(a,c).
Set the physical ordered-three-face coloring to be c(F,(a,b,c))=h(a,b,c), independent of the exterior cube bits.

**THEOREM 1 (validity).** This is a genuine active NORI coloring:
  c(bar F,(c,b,a))=1-c(F,(a,b,c))
for every physical ordered face F. Indeed reversing an order interchanges the cases (1) and (2), with complementary assigned bits, while cases (3) are closed under reversal and obey f(c,a)=1-f(a,c). As c is independent of the physical face exterior bits, complementation F->bar F has no other effect.

**THEOREM 2 (exact certified-square set).** Let X_c be the cubical 2-complex whose physical squares are certified by some actual MONOCHROMATIC directed four-edge cube geodesic having that square's two free coordinate directions as its middle pair, as in NORI item nori_certified_center_square_complex_high_degree_eight_components_20261008. Then for THIS explicit active coloring:
  X_c = Y_(i,j)
where Y_(i,j) contains ALL 2^n cube vertices, ALL n*2^(n-1) physical edges, and ALL physical coordinate squares EXCEPT the 2^(n-2) squares with free pair {i,j}. Thus every other unordered direction pair is certified at EVERY physical cube hub, not just somewhere.

PROOF. For the exceptional middle pair (i,j), any centered 4-path direction word (a,i,j,d), with four distinct coordinates, has first 3-window color h(a,i,j)=0 and second h(i,j,d)=1. Therefore no such path is monochromatic; similarly for middle order (j,i). Thus NO {i,j}-square is certified.

Now fix any OTHER ordered middle pair (b,c)≠(i,j),(j,i). Let
  W=[n]\{i,j,b,c}.
It excludes at most four directions, so |W|>=n-4. For any a,d∈W, the ordered triples (a,b,c) and (b,c,d) do NOT contain both exceptional i,j. Consequently their colors are f(a,c) and f(b,d), respectively, with NO exceptional cases. For any chosen q∈{0,1}, there are at least (n-1)/2 -4 >=2 valid a∈W with f(a,c)=q, and at least the same number of valid d∈W with f(b,d)=q. Pick a and d distinct (possible since each candidate set has >=2 elements). This gives a genuine four-edge centered cube geodesic word (a,b,c,d) with both ordered-three-face window colors q. Because c depends only on the ordered direction triple and not the physical exterior bits, the SAME word certifies the physical square with middle free directions b,c through EVERY hub z∈Q_n. All nonexceptional middle pairs are thus certified globally, and each automatically supplies all its boundary edges. For n>=13 there are plenty of other pairs incident to every coordinate, hence ALL ordinary cube edges lie in X_c. QED.

**THEOREM 3 (EXACT index one despite HONEST monochromatic certificates).** The certified-square complex X_c has the free cube-antipodal involution. It is CONNECTED (contains all cube edges), so its Z2 antipodal-cover class w1 is nonzero. Nevertheless projection onto exceptional coordinates
  pr_(i,j):X_c -> boundary([0,1]^2) ≅ S^1
is well-defined and antipodally equivariant: every INCLUDED square fixes at least one of i,j to 0 or1, because the only omitted square class has both exceptional directions free. The boundary square carries the half-turn involution. Therefore w1^2=0 and the equivariant cohomological index of X_c is EXACTLY ONE.

This construction promotes NORI's previous abstract low-index example nori_dense_antipodal_square_complex_index_one_no_go_20261008 to an ACTUALLY REALIZABLE certified-square complex arising from a valid NORI coloring. So one cannot force a second-index Tucker/Borsuk–Ulam obstruction merely from connectedness, overwhelming square density, and authentic MONOCHROMATIC four-geodesic certificates: an honest coloring exhibits all those properties and still has index one. A grand-closure proof would need additional LONG-WITNESS information or a topology conditioned on the ABSENCE of a good full geodesic (the constructed coloring is not claimed to be a counterexample to grand closure).

**Related rigidity.** The missing middle-pair direction graph classification item nori_globally_absent_middle_pair_graph_disjoint_even_cycles_paths_20261008 proves any globally missing middle-pair graph has maximum degree2 and even cycles only, and that its component pattern can be enforced by coordinate-only colorings. Here the global missing-pair graph is EXACTLY one edge {i,j}, realized with the strongest possible certification of all other pairs.
