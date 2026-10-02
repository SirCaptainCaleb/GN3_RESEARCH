# Repeated hub colors obstruct extraction from an arbitrary long shadow path

## Statement

For every t there is a linear 3-graph H_t whose 2-shadow contains the graph path x_0x_1...x_t, while every linear hypergraph path in H_t has at most four edges. Namely, with two additional vertices z,w, take e_i={x_{i-1},x_i,z} for odd i and e_i={x_{i-1},x_i,w} for even i. Thus no argument for the 2-shadow route can rely only on extracting a positive fraction of an arbitrary ordinary shadow path; repeated color/hub structure must be used rather than discarded.

## Body

The system is linear. Consecutive e_i,e_{i+1} share only x_i because they use different hubs. Two nonconsecutive edges of the same parity share exactly their common hub z or w, and edges of opposite parity with nonconsecutive indices are disjoint.

The shadow contains every pair x_{i-1}x_i, hence contains x_0x_1...x_t as an ordinary graph path. On the other hand, any linear hypergraph path can contain at most two odd-indexed edges: every odd-indexed edge contains z, so if three occurred in the hypergraph path, the first and third among them would be nonconsecutive path edges intersecting in z. If two odd edges occur, they must be consecutive in the hypergraph path. The same argument applies to the even-indexed edges using w. Therefore every linear hypergraph path has at most four edges. For sufficiently large t the bound four is attained, for example by e_1,e_5,e_4,e_8. Hence arbitrarily long ordinary shadow paths need not contain even an unbounded linear-hypergraph-path subpath or subsequence.