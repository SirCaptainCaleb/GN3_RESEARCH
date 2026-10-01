# Every order-eleven pair deletion has at least twelve star-shaped balanced restoration states

## Statement

Let H be an eleven-vertex boundary tournament with path-cover number greater than two, and fix distinct vertices x,y. Then H-{x,y} has at least twelve distinct Hamiltonian 4|5 covers A|B. For every such cover, the bipartite absorption graph on {x,y} and {A,B}, with edge z-S when H[V(S) union {z}] is Hamiltonian, has matching number at most one and hence lies in one star. Consequently, among the twelve covers there are at least three for which one common obstruction type occurs: x is nonabsorbable into both sides, y is nonabsorbable into both sides, neither label extends the four-side, or neither label extends the five-side.

## Body

By balanced9_multiplicity01, the nine-vertex subtournament H-{x,y} has at least twelve distinct balanced 4|5 covers A|B. Fix one. If its absorption graph contained a matching of size two, then after perhaps exchanging x and y or A and B, both A union {x} and B union {y} would be Hamiltonian. Hamilton paths on these disjoint sets would form a spanning two-cover of H, contradicting the hypothesis. Hence the absorption graph has matching number at most one.

A bipartite graph on two left and two right vertices with matching number at most one has all edges incident with a common vertex. Thus for each cover at least one of four obstruction types holds: x has degree zero; y has degree zero; the four-side A has degree zero; or the five-side B has degree zero. Choose one valid type for each of the at least twelve covers. By pigeonhole, one of the four types is chosen on at least three distinct covers. This gives the synchronized conclusion.
