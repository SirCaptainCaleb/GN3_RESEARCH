# Compatibility edges have codegree at most two

## Statement

Let H be a boundary tournament with pc(H)>2 and choose one deletion cover F_x for each deletion label under consideration. In the graph whose vertices are deletion labels and whose edges join compatible covers, every edge has at most two common neighbors. More precisely, for a compatible pair F_a,F_b, let P be the common Hamilton path on the support into which a and b restore. If the insertion slots of a and b in P are adjacent, then at most one label c can be compatible with both F_a and F_b; if the slots coincide, then at most two labels c can be compatible with both, namely the vertices of P immediately flanking that slot when they exist.

## Body

# Compatibility edges have codegree at most two

Fix a compatible pair F_a,F_b. By d43a7c9e2f61, on H-{a,b} the two covers have common ordered supports P|Q; both omitted labels restore to P, and their insertion slots in P are equal or adjacent.

Let c be any deletion label whose chosen cover F_c is compatible with both F_a and F_b. Then F_a,F_b,F_c form a compatibility triangle. By compattriangle01, after removing a,b,c the three labels occupy one common insertion gap in the common base order.

View this relative to the fixed path P on H-{a,b}. Deleting c from P must merge the insertion slot of a in P and the insertion slot of b in P into the single common gap supplied by compattriangle01. Deleting one vertex of an ordered path merges exactly the two slots immediately before and after that vertex and leaves every other slot distinct.

Therefore:

- if the insertion slots of a and b are adjacent, c must be the unique vertex of P lying between those two slots;
- if the insertion slots coincide at a slot s, then c can only be one of the at most two vertices of P incident with s, because only deleting such a vertex makes s one of the two slots merged into the common gap.

Thus a compatible edge has at most two common neighbors, and an adjacent-slot edge has at most one. Endpoint slots simply reduce the number of candidates.

The statement uses only pc(H)>2 and the chosen deletion covers; no minimum-counterexample hypothesis is needed.
