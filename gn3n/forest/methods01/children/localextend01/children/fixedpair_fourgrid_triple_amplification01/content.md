# A complete fixed-pair Hamiltonian four-grid amplifies over every outside triple

## Statement

Let H be a boundary tournament, let a,b be distinct vertices, and let Y be disjoint from {a,b} with |Y|>=3. Suppose {a,b,y,z} is Hamiltonian for every two distinct y,z in Y. Then for every three distinct y,z,w in Y, either {a,b,y,z,w} is Hamiltonian, or at least one of {a,y,z,w} and {b,y,z,w} is Hamiltonian.

## Body

Fix distinct y,z,w in Y. The four-sets
W_yz={a,b,y,z}, W_yw={a,b,y,w}, and W_zw={a,b,z,w}
are Hamiltonian by hypothesis. Put S={a,b,y,z,w}.

If H[S] is Hamiltonian, the first conclusion holds. Suppose instead that H[S] is non-Hamiltonian. By the certified five-vertex small-set theorem smallset01, a non-Hamiltonian five-set has at most one non-Hamiltonian four-subset. Hence at least four of the five four-subsets of S are Hamiltonian. Three of them are already W_yz, W_yw, and W_zw. Therefore at least one of the two remaining four-subsets
S-{a}={b,y,z,w} and S-{b}={a,y,z,w}
is Hamiltonian, as required.
