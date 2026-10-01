# Two disjoint triples carry at least three cross-paired common-core transport presentations

## Statement

Let H be a minimum counterexample and let C,T be disjoint triples, U=C union T. Let r be the number of c in C for which U-c is Hamiltonian and s the number of t in T for which U-t is Hamiltonian, and put h=r+s. Then 1<=r,s<=3, h>=4, and rs>=3(h-3). Thus h=4 gives at least three cross-pairs, h=5 gives at least six, and h=6 gives all nine. Equality rs=3 occurs exactly when {r,s}={1,3}; hence if there are exactly three cross-paired Hamiltonian deletions, one side has all three Hamiltonian deletions and the other has exactly one. For every cross-pair (c,t), the Hamiltonian five-sets U-c and U-t share the four-core U-{c,t}, so 1000476 supplies a common-four-core six-set transport package. Every Hamiltonian five-lift has non-Hamiltonian path-cover-two complement. In particular there are Hamiltonian lifts preserving either triple in full, one side has at least two Hamiltonian deletions, and for any family of triples T disjoint from a fixed C some fixed two-core C-{c} Hamiltonizes at least ceil(|F|/3) family members.

## Body

Four-of-six gives at least four Hamiltonian deletions of U. Since C and T each have only three vertices, each side contributes at least one Hamiltonian deletion. Thus 1<=r,s<=3 and h=r+s>=4.

The product admits a sharper bound than rs>=3. Because r,s<=3,
(r-3)(s-3)>=0,
so rs>=3(r+s-3)=3(h-3). Hence h=4,5,6 force respectively at least 3,6,9 cross-pairs. If rs=3, the only positive integer possibility with r,s<=3 and r+s>=4 is {r,s}={1,3}. Conversely that split gives exactly three cross-pairs. Thus the minimum-multiplicity case is rigid: one triple contributes all three Hamiltonian deletions and the other contributes exactly one.

For each cross-pair (c,t), the Hamiltonian five-sets U-c and U-t intersect in U-{c,t}, so 1000476 applies to their common six-set U with that four-core. Minimum-counterexample calculus makes the complement of every Hamiltonian five-lift non-Hamiltonian with path-cover number two.

The directional statements are immediate: choose any Hamiltonian deletion from C to preserve T in full, and any Hamiltonian deletion from T to preserve C in full. Since r+s>=4, one of r,s is at least two. For a family F disjoint from fixed C, choose one Hamiltonian deletion c(T) in C for each T; pigeonholing among three choices produces one fixed C-{c} for at least ceil(|F|/3) members.
