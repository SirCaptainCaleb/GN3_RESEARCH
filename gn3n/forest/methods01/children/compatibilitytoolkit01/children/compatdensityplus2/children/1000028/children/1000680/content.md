# Compatibility density is at most one edge above Mantel

## Statement

Let H be a boundary tournament with pc(H)>2, let D be a set of m>=7 deletion labels, and choose one deletion cover F_d of H-d for each d in D. If G is the compatibility graph on D, then e(G)<=floor(m^2/4)+1.

## Body

# Proof

The compatibility-triangle geometry gives two hereditary graph properties: every compatibility edge lies in at most two compatibility triangles, and every compatibility triangle has an edge lying in no other compatibility triangle. Hence compatdensityplus2 gives
e(G)<=floor(m^2/4)+2.

Assume for contradiction that equality holds:
e(G)=floor(m^2/4)+2.

By the extremal peeling lemma 09e7cbdc7705, G contains an induced seven-vertex subgraph J isomorphic to the complement of C_7. Label the vertices of the complementary 7-cycle cyclically by 0,1,...,6. Thus in J two labels are compatible exactly when they are not consecutive on the cycle.

Consider the compatibility edge a b = 0 2. Its common neighbors in J are exactly c=4 and d=5. Since the full compatibility edge ab has at most two common neighbors, these are also its only common neighbors in G. The vertices c,d are consecutive on the complementary 7-cycle, so they are incompatible.

Now apply the order-reversal separator lemma f7c79b595b2e to the edge ab and common neighbors c,d. Since c,d are incompatible, every compatibility path from c to d must contain a or b.

But J-{a,b} already contains such a path avoiding a,b: for example
4 - 1 - 5,
because 4 and 1 are nonconsecutive on C_7, and 1 and 5 are nonconsecutive on C_7. Both edges therefore belong to J and hence to G. This contradicts the separator conclusion.

Thus equality in the +2 bound is impossible, and since the number of edges is integral,
e(G)<=floor(m^2/4)+1.
