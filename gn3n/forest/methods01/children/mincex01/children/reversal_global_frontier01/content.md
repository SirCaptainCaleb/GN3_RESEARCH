# Every prescribed pair has a sharp linear star of Hamiltonian four-sets with two-path complements

## Statement

Let H be a minimum counterexample and fix distinct vertices L,R. On the r=|V(H)|-2 exterior vertices, join y,z when {L,R,y,z} is Hamiltonian. Then this graph has independence number at most two. Consequently it has at least binom(r,2)-floor(r^2/4) edges and some exterior vertex y has at least floor((r-1)/2)=floor((|V(H)|-3)/2) neighbors z. Thus every prescribed pair lies in a linear star of Hamiltonian four-sets sharing the triple {L,R,y}; every complementary subtournament is non-Hamiltonian with path-cover number two.

## Body

For any three exterior labels D, partition them according to whether (L,y,R) or (R,y,L) is tight. Two labels y,z share a class. Boundary antisymmetry on the appropriate triple then gives a Hamilton path on {L,R,y,z}, exactly as in the fixed-pair argument. Hence every exterior three-set spans an edge in the graph J whose edges are Hamiltonian four-extensions of {L,R}; equivalently alpha(J)<=2. The complement is triangle-free, so Mantel gives e(J)>=binom(r,2)-floor(r^2/4), and some y has degree at least floor((r-1)/2). Every corresponding four-set is proper because |H|>10. Its complement cannot be Hamiltonian or it would two-cover H; minimality therefore makes the complement pc2. The Mantel degree bound is sharp from alpha(J)<=2 alone. No endpoint-reversal classification or maximal witness is needed.