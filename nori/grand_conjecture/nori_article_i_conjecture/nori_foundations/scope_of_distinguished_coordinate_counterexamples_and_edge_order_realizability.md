# Scope of distinguished-coordinate counterexamples and edge-order realizability

# Scope of the distinguished-coordinate construction and edge-order realizability

The dimension-nine NORI counterexample separates physical ordered-three-face colorings from two more constrained structures: lower-arity distinguished-coordinate colorings and boundary 3-tournaments. This subsection proves the relevant distinctions. It establishes no counterexample to general NORI1 or NORI2.

## The one-face distinguished-coordinate family always has a monochromatic antipodal geodesic

Let the cube directions be D together with s. For every ordinary direction d in D choose a bit a_d, and color its physical edges by c_d(x)=x_s XOR a_d. Color each s-edge by g(x_D), where g(complement y)=1-g(y). These are legal undirected antipodally odd edge colors.

**Proposition.** Every such coloring admits a monochromatic full antipodal geodesic.

**Proof.** Let D_0 and D_1 be the directions with a_d=0 and a_d=1. Choose z in {0,1} and y with g(y)=z; antipodal oddness guarantees such y. Set x_s=z and x_D=y XOR D_0. Traverse all directions in D_0, then s, then all directions in D_1. Before s, each ordinary edge has color z. The s-edge is traversed at ordinary-coordinate vector y and also has color z. After s, each ordinary edge has color (1-z) XOR 1=z. Every direction occurs once. This covers empty D_0 or D_1 as well. QED.

## The two-face distinguished-coordinate family always has a one-switch antipodal geodesic

Here NORI2 means binary colors of ordered physical squares satisfying c(complement F,(b,a))=1-c(F,(a,b)).

**Lemma.** Every binary coloring of the edges of a complete graph has a Hamilton vertex order whose consecutive edge colors change at most once.

**Proof.** Maintain vertex-disjoint paths R and B covering the vertices already inserted, with all R-edges color 0 and all B-edges color 1; either path may be empty. To insert x with both paths nonempty, write r,b for their final vertices. If rx has color 0, append x to R. If bx has color 1, append x to B. In the remaining case rx has color 1 and bx color 0. If rb has color 0, remove b from B and append b,x to R. If rb has color 1, remove r from R and append r,x to B. Every operation preserves the path colors and disjoint coverage. With one path empty, append x to the other if its endpoint edge has the required color, and otherwise put x alone in the empty path. Begin with one singleton path. Finally concatenate R and B. The connecting edge has one of the two colors, so the resulting edge word has at most one change. QED.

Let h(a,b)=h(b,a) be any binary edge coloring on D. Define ordered-square colors by
- c(F,(a,b))=z_s(F) XOR h(a,b) for a,b in D;
- c(F,(s,a))=1;
- c(F,(a,s))=0.

**Proposition.** Every such legal NORI2 coloring has a good full antipodal geodesic.

**Proof.** Symmetry of h and the complementary endpoint constants verify the combined antipodal-reversal law. Choose a Hamilton order d_1,...,d_m of D supplied by the lemma. Traverse (s,d_1,...,d_m). Its square colors are 1 followed by (1-z) XOR h(d_i,d_{i+1}), where z is the initial s-bit. For m>=2 choose z=h(d_1,d_2). Then the initial 1 agrees with the first ordinary square color, and the remainder has at most one change. The cases m<=1 are immediate. QED.

These propositions rule out the direct lower-arity versions of this construction in every dimension. They leave more general reductions and colorings open.

## Boundary 3-tournaments are orientations of a line graph

A boundary 3-tournament on V chooses exactly one of (a,b,c) and (c,b,a) for every triple of distinct vertices with specified middle vertex b. Call the chosen triples right.

**Proposition.** Boundary 3-tournaments on V correspond bijectively to orientations of the line graph L(K_V).

**Proof.** Vertices of L(K_V) are unordered pairs ab. Its adjacent vertices ab and bc share a unique vertex b. Orient ab -> bc exactly when (a,b,c) is right. Reversal of the triple reverses this one line-graph edge. Every adjacency corresponds to exactly one such reversal pair, proving the bijection. QED.

**Corollary (exact edge-order realizability).** A boundary 3-tournament arises from one strict ordering of the edges of K_V, with (a,b,c) right precisely when ab < bc, if and only if the corresponding orientation of L(K_V) is acyclic.

**Proof.** An edge ordering is a strictly increasing potential on every directed line-graph edge, which forbids directed cycles. Conversely a topological ordering of any finite acyclic orientation orders the vertices of the line graph, hence the original graph edges, and realizes every specified comparison. QED.

For a noncomplete graph G the same statement holds for the partial triple system on actual two-edge paths. An increasing vertex-simple path in G is exactly a sequence of distinct original vertices whose successive original edges form a directed line-graph path. Arbitrary directed paths in the line graph need not have this property: they may repeatedly pass through the same original vertex. Thus the original path-incidence and vertex-distinctness constraints remain essential.

Transitivity of the comparison tournament at each individual middle vertex is necessary but insufficient for global realizability. Already on three vertices the comparisons ab<bc, bc<ca, ca<ab give a cycle while each individual vertex has only two incident edges and hence a transitive local comparison.

## Why the NORI3 example gives no immediate boundary-tournament or increasing-path bound

In the distinguished-coordinate NORI3 construction, for every ordered face avoiding s,
c(F,(a,b,c))=z_s(F) XOR h(a,b,c),
where h(a,b,c)=h(c,b,a).
Thus a triple and its reverse have the same color at that face. A boundary 3-tournament requires opposite memberships. The three-class auxiliary rule of the Q15 example also has this reversal-even property.

Consequently the construction supplies no boundary 3-tournament under the direction-triple identification, and supplies no edge ordering through the comparison representation above. Any further transfer would have to prove its own preservation of admissible paths and quantify the relation between path lengths or covering numbers. No new extremal bound for those classes follows here.

## A candidate additional symmetry

One possible class for future investigation imposes, besides the combined NORI k-face law,
c(F,reverse pi)=c(F,pi) XOR rho_k, where rho_k=binom(k,2) mod 2.
The combined law then gives c(complement F,pi)=c(F,pi) XOR (1 XOR rho_k).

For k=1 the added reversal identity is automatic and retains every NORI1 coloring. For k=3 it retains all direction-only boundary 3-tournaments and requires antipodal invariance with the order fixed. It excludes the present distinguished-coordinate counterexamples. Only reversal is prescribed; other permutations of directions remain free. This is a candidate class, with no general existence theorem asserted.
