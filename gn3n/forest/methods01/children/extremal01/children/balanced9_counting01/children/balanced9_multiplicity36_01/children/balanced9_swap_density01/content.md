# Nine-vertex balanced covers have at least sixty reciprocal-swap adjacencies

## Statement

Let H be a boundary tournament on nine vertices. Form the graph whose vertices are Hamiltonian 4|5 partitions, represented by their four-vertex side A, and join A,A' when |A intersect A'|=3. Then this graph has at least 36 vertices and at least 60 edges. Consequently some balanced 4|5 partition has at least four distinct one-for-one reciprocal support swaps preserving Hamiltonicity on both sides.

## Body

By balanced9_multiplicity36_01, there are at least m=36 balanced partitions. Let F be the corresponding family of Hamiltonian four-sides; distinct four-sides determine distinct partitions because the complementary five-side is unique.

For each three-set S of the nine-vertex ground set, let x_S be the number of members A in F containing S. Two distinct four-sets A,A' are adjacent in J(9,4) exactly when they share a three-set, and that common three-set is unique. Hence the number e of reciprocal-swap adjacencies is e=sum_S binom(x_S,2). Also sum_S x_S=4m, because every four-set contains four three-subsets.

For m=36, the sum of the 84 nonnegative integers x_S is at least144. Subject to a fixed integer sum, sum binom(x_S,2) is minimized when the x_S differ by at most one. Distributing 144 incidences over 84 three-sets therefore gives 60 values equal to2 and 24 equal to1 in the minimizing configuration, so e>=60. If m>36, deleting balanced partitions down to any 36-element subfamily preserves a 36-vertex induced subgraph with at least60 edges, so the full graph also has at least60 edges.

Average degree in the 36-vertex subgraph is at least120/36>3, hence some vertex has degree at least4. If A|B is that partition and A'=A-{a}+{b} is a neighbor, then B'=B-{b}+{a} is its complementary five-side; both A',B' are Hamiltonian by definition. Thus each incident graph edge is exactly a reciprocal one-for-one support swap preserving a balanced Hamiltonian 4|5 cover.
