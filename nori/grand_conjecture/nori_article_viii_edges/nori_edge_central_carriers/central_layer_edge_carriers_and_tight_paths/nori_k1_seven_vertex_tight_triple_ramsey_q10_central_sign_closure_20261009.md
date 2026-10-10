# Tight 3-path Ramsey on seven vertices forces complement-odd 5-hypergraph and Q10 central edge closure

# Seven-vertex tight-triple Ramsey theorem and complete Q10 central-vertex-sign edge closure

Let V be a seven-element set. For a binary coloring t of its three-element subsets, a tight path is a sequence of distinct vertices whose consecutive unordered three-subsets have the same color.

**THEOREM 1 (seven vertices suffice).** Every binary coloring t:binom(V,3)->{0,1} has a monochromatic tight path on SIX distinct vertices, with FOUR consecutive three-subset windows. No antipodal hypothesis is required. The seven-vertex threshold is sharp: on six vertices, color a triple 1 precisely when it contains a distinguished vertex v. Any tight six-vertex path has four windows with empty total intersection, so some window omits v; their union is all six vertices, so some window contains v. Hence every six-vertex path is bichromatic.

**Proof of sufficiency.** First obtain a monochromatic tight path on five distinct vertices. Fix c in V. Color the edges of the complete graph on five other vertices by t({c,u,v}). Every two-coloring of K5 has a monochromatic graph path of three edges, say a-b-d-e; For completeness: if every vertex has two incident edges of each color, the red edges form a five-cycle and contain such a path. Otherwise some vertex o has three red neighbors u,v,w. If an edge among u,v,w is red, the red path w-o-u-v (after relabeling) works. If the neighbor triangle is wholly blue, its blue three-vertex path extends through the fifth vertex unless that vertex has red edges to all three neighbors; in that case u-o-v-fifth is a red path. Thus a monochromatic four-vertex graph path always exists. Its three edges give the monochromatic tight triple path (a,b,c,d,e). Call this color red. There remain two distinct unused vertices x,y.

Suppose no monochromatic six-vertex tight triple path exists. Extending the red path at either end forces all four triples {x,a,b},{y,a,b},{d,e,x},{d,e,y} to be blue.

The six-vertex order (y,a,b,x,d,e) then has blue triple windows {y,a,b}, {a,b,x}, and {x,d,e}; to prevent a blue tight path, {b,x,d} must be red. Interchanging x and y forces {b,y,d} red.

The six-vertex order (a,c,b,d,x,y) now has its first three triple windows {a,b,c}, {b,c,d}, {b,d,x} red. Consequently {d,x,y} is blue. Similarly (e,c,d,b,x,y) has its first three windows {c,d,e},{b,c,d},{b,d,x} red, so {b,x,y} is blue.

Finally the order (a,b,x,y,d,e) has FOUR blue windows:
{a,b,x}, {b,x,y}, {d,x,y}, {d,e,y}.
This is the forbidden monochromatic six-vertex path, a contradiction. QED.

**THEOREM 2 (complement-odd five-subsets on ten directions).** Let |U|=10 and let lambda:binom(U,5)->{0,1} satisfy lambda(U\S)=1-lambda(S). Then lambda has a monochromatic tight 5-uniform path on NINE distinct ground elements, with FIVE consecutive 5-subset windows.

**Proof.** Fix two distinct elements h1,h2 of U, and choose any seven of the other eight elements. Apply Theorem 1 to the coloring t(T)=lambda({h1,h2} union T) of its three-subsets. Obtain six distinct elements a,b,c,d,e,f whose consecutive three-subsets are t-monochromatic. The eight-element sequence
(a,b,c,h1,h2,d,e,f)
has four consecutive 5-subset windows, all of the same lambda-color q: the windows are {h1,h2} adjoined respectively to {a,b,c},{b,c,d},{c,d,e},{d,e,f}.

Let u,v be the two unused ground elements. Prepending u creates the 5-subset {u,a,b,c,h1}; appending v creates {h2,d,e,f,v}. These two 5-subsets are complementary in U, since their disjoint union is U. Exactly one has lambda-color q. Perform the corresponding end extension. This gives a monochromatic tight 5-path on nine distinct vertices. QED.

**COROLLARY (genuine Q10 physical edge paths).** For EVERY antipodally odd central-vertex-sign UNDIRECTED edge coloring of Q10, namely one in which each belt edge between ranks 4,5 or 5,6 has color lambda(S) at its unique rank-5 endpoint and lambda(S^c)=1-lambda(S), there exists a fully monochromatic antipodal TEN-edge cube geodesic confined to ranks 4,5,6. Edge colors away from this three-layer belt are unrestricted subject to the global edge antipodality law.

**Proof.** Obtain a nine-element tight path (z1,...,z9) from Theorem 2, with monochromatic 5-windows W_i={z_i,...,z_(i+4)} (i=1,...,5). Let z10 be the remaining direction. Start the cube at the rank-4 vertex whose support is {z1,z2,z3,z4}. Flip coordinates in the order
(z5,z1,z6,z2,z7,z3,z8,z4,z9,z10).
The five rank-5 vertices visited in order are precisely W1,...,W5, and every cube edge touches exactly one of them. Therefore every edge has their common color q. The final vertex has support {z5,z6,z7,z8,z9,z10}, the antipode of the start. Each coordinate is flipped exactly once. QED.

**Scope.** This establishes the previously open k=5 precursor and completes the entire central-vertex-sign subclass of the original antipodally odd EDGE conjecture in n=10, extending the established n=4,6,8 special-class cases. The active NORI ordered-three-face conjecture, general physical edge colorings, and the analogous k>=6 tight-path forcing remain open.

**Next reduction.** Fixing the two central coordinates in the analogous dimension 2k reduces its precursor to a two-colored (k-2)-uniform tight path on 2k-4 distinct vertices among 2k-2 available. For k=6 this asks whether every binary coloring of four-subsets of ten elements has a monochromatic tight 4-path on eight distinct elements (five 4-subset windows). A uniform proof of this r-uniform statement for all r>=2 would close the entire central-vertex-sign family in every even dimension.
