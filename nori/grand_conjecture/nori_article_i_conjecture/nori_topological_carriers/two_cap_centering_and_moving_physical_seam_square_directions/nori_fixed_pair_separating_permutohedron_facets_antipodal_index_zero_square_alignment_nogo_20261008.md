# Fixing the two physical seam-square directions across a permutohedral cut destroys Tucker index (zero-index separated-facet carrier)

# Fixed root-square seam alignment kills antipodal Tucker index: separated-coordinate facets form an index-zero carrier

Let n>=5, fix any two DISTINCT coordinate directions a,b∈[n], and let K be either (i) the genuine endpoint-opposed full x-rooted permutohedral face nerve K_x with involution direction-order reversal, or (ii) the team's genuine t-root synchronized packet nerve K_X whose vertices are tuples of full permutations and whose involution reverses every constituent word. Both are free simplicial antipodal complexes, and their simplices are collections of genuine direction orders lying in some common proper permutohedron face.

For a nonempty proper direction subset S⊂[n], let H_S be the permutohedron facet whose orders all have exact prefix support S (the first |S| direction names are precisely S). Let D_S⊆K be the full simplex on those vertex orders (or packet vertices all of whose constituent orders lie in H_S).

Define the **FIXED-PAIR SEPARATING CUT SUBCOMPLEX**
  K_sep(a,b)= union_(S: |S∩{a,b}|=1) D_S.
This is invariant under full reversal, because reversal maps facet H_S to H_([n]\S), and the complement still separates a,b.

**THEOREM (separating two prescribed seam directions has equivariant index ZERO).** The complex K_sep(a,b) admits an explicit continuous antipodally odd map to S^0. Consequently
  **ind_Z2(K_sep(a,b))=0**
whenever it is nonempty (for n>=7 the endpoint-opposed complexes have such simplices in typical cases; the formula does not require nonemptiness).

**PROOF.** For an actual full direction permutation π let
  sgn_(a,b)(π)=+1 if a occurs BEFORE b in π,
                   −1 if b occurs BEFORE a in π.
On any facet H_S with exactly one of a,b∈S, ALL its permutations have the SAME sign: the member of {a,b} inside the prefix S necessarily precedes the member outside S. Thus sign is CONSTANT on each D_S and hence on every simplex of their union K_sep(a,b); if two such facets' simplices meet in a packet vertex, the constituent direction order at the distinguished first root has one unique a-before-b sign, so the two constants agree. Define the map f on each simplex by this sign. It is continuous (locally constant on the simplicial components). Physical NORI path reversal on the rooted permutation complex sends π to reverse π and hence interchanges relative order of a,b, giving
  f(τv)=−f(v).
For packets take the order of any fixed constituent root, which is consistent across each simplex by the common facet property. Thus f is an explicit equivariant map K_sep→S^0. Pulling back the sign double-cover class from RP^0 (a point) forces w1(K_sep/τ)=0, so no positive antipodal index remains. QED.

**CRITICAL CONNECTION TO TWO-SEAM ROOT-SQUARE FLATNESS.** If a genuine full path is spliced at support cut S, the two common free directions of its two physical seam windows are v (LAST used prefix direction) and w (FIRST unused suffix direction). By definition v∈S and w∉S. Therefore the unique physical root square on which BOTH seam window face objects are simultaneously invariant is always spanned by ONE direction on EACH SIDE of the prefix cut. If we PRESELECT a physical root square with free directions {a,b}, demanding that the resulting Tucker shared cut S make that square coincide with the seam square NECESSARILY requires |S∩{a,b}|=1.

But restricting the current permutohedral high-index Tucker carrier to such separating cuts gives precisely K_sep(a,b), which is index ZERO. Thus an index-theoretic argument based on the current permutohedral carrier CANNOT obtain the required alignment just by first prescribing the square {a,b} and then restricting to its separating facets: the high index disappears completely, because the relative order of a,b becomes an odd sign.

**GRAND-FORCING IMPLICATION.** The earlier t=4 multiroot Tucker theorem guarantees synchronized full-path packets for ANY prescribed physical root square and SOME common inner support cut; it does NOT guarantee that the square's two directions are on opposite sides of that cut, much less equal to the LAST-prefix/FIRST-suffix seam pair. This theorem identifies an exact topology-destroying restriction, explaining why the proposed direct fixed-square seam alignment cannot simply be inferred from the high-index carrier. A viable full grand proof must let the physical square direction pair VARY TOGETHER WITH THE SELECTED CUT (as in a coupled root-square/order complex), or add honest exchange/repair cells that transport between the two relative-order chambers while retaining the physical face-memory certificates.

**Scope.** This is a precise equivariant-index NO-GO FOR ONE RESTRICTED STRATEGY. It does not imply that no compatible square/pair exists and does NOT refute or solve the unrestricted NORI grand conjecture. It applies even without any coloring assumptions beyond existence of the chosen genuine path/packet vertices.
