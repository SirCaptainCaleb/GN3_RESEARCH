# A repeated longest-path three-window generates quadratically many Hamiltonian five-sets

## Statement

Let C be a fixed three-consecutive-vertex subpath of a globally longest tight path P. Suppose a concentrated witness family supplies h pairwise vertex-disjoint exterior pairs, so its endpoint pool U has 2h distinct vertices outside C, and every witness uses the same window C. Then at least h(h-1) unordered pairs {u,v}⊂U satisfy that H[C∪{u,v}] is Hamiltonian. Equivalently, the Hamiltonicity graph on U for five-sets over the fixed core C has at least h(h-1) edges and average degree at least h-1; in particular some exterior vertex u has at least h-1 partners v for which C∪{u,v} is Hamiltonian.

## Body

The three vertices of C form a tight path. Apply Section 1 of the certified local-extension calculus localextend01 to the exterior set U of order 2h. Its bad-pair graph B_C(U), joining u,v when C∪{u,v} is non-Hamiltonian, is triangle-free. Mantel therefore gives e(B_C(U))≤floor((2h)^2/4)=h^2. There are binom(2h,2)=h(2h-1) exterior pairs in total, so the complementary Hamiltonian-pair graph has at least h(2h-1)-h^2=h(h-1) edges. Its average degree is at least 2h(h-1)/(2h)=h-1, giving the final star conclusion. Notice that after the exact core C has been synchronized, this conclusion no longer depends on whether the original witnesses were four-set or five-set witnesses; it uses only the 2h distinct exterior endpoints and the fixed tight three-core.
