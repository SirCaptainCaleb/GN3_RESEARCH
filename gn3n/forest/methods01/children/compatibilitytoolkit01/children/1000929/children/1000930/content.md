# Compatibility blocks retain one fixed Hamilton path except for a spanning odd cycle

## Statement

Under the hypotheses of the arbitrary selected-support theorem, every edge block and every cyclic block of the full-compatibility graph G has one fixed ordered Hamilton path Q shared by all of its covers, except possibly when G itself is a spanning odd cycle with balanced selected covers. In a block with shared Q, the other path at label d has support V(H)-Q-{d}, and V(H)-Q is non-Hamiltonian. In particular, if G is 2-connected and its label set is V(H), then G is the spanning odd cycle and all its deletion-cover paths have order (|V(H)|-1)/2.

## Body

Let H,D,F_d,J,G be as in 1000929. A block here means a maximal 2-connected subgraph or a bridge with its endpoints; isolated vertices are excluded.


If J is a forest, each block of L(J) is the clique formed by the edges incident to a fixed nonleaf vertex of J. This follows directly from the fact that an edge of a tree whose two endpoints are nonleaves is a cut vertex of its line graph: deleting that line-graph vertex separates the edges on its two sides. Consequently any 2-connected subgraph of the full compatibility graph G lies in one such clique. All covers indexed by that subgraph therefore share one component support Q.

Moreover, they share the same displayed Hamilton order on Q. Along every compatibility edge the order on Q agrees, and the subgraph is connected. The other path in each cover has support V(H)-Q-{d}. Thus all variation in this block occurs within one fixed non-Hamiltonian set V(H)-Q, while Q is one fixed Hamilton path. The set V(H)-Q is non-Hamiltonian because otherwise its Hamilton path together with Q would two-cover H.

The same assertion for a bridge block is the shared-support lemma plus compatibility. If J is the exceptional odd cycle, L(J) is that same cycle, and G is a subgraph of it. Hence either G has no cyclic block, or G is the full spanning odd cycle.

We obtain the following global description: every cyclic block of G carries one fixed Hamilton path, except possibly when G itself is a spanning odd cycle and all its selected deletion covers are balanced.

In particular, if G is 2-connected and its labels are all of V(H), then it must be this spanning odd cycle. Indeed, in the forest case a common support Q carried by all covers would omit every ground vertex (the cover at d omits d), forcing Q to be empty, which is impossible.


No statement about globally longest paths or gluing of these ordered blocks is asserted.