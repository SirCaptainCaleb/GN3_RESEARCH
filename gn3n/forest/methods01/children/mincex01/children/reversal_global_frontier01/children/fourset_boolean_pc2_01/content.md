# A non-Hamiltonian four-set gives path-cover-two stability for every nonempty proper complement extension

## Statement

Let H be a minimum counterexample, let X be any non-Hamiltonian four-vertex set, and put K=H-X. Then for every nonempty proper subset S of X, the induced subtournament H[V(K) union S] is non-Hamiltonian with path-cover number two. In particular, if X is the matching-block four-set in reversal_global_frontier01, then the fourteen states K+S indexed by nonempty proper subsets S of X form a complete Boolean family of non-Hamiltonian path-cover-two extensions around K.

## Body

Fix a nonempty proper subset S of X. The complementary set X-S has order one, two, or three. Every boundary tournament of order at most three is Hamiltonian, so H[X-S] has a tight Hamilton path. If H[K union S] were Hamiltonian, a Hamilton path on K union S together with one on X-S would form a spanning two-cover of H, contradicting that H is a counterexample. Thus H[K union S] is non-Hamiltonian. It is a proper induced subtournament of the minimum counterexample H, so mincex01 gives path-cover number at most two; non-Hamiltonicity excludes path-cover number one, hence its path-cover number is exactly two. A four-set has fourteen nonempty proper subsets, so all fourteen states K union S satisfy the conclusion. No orientation property of X beyond |X|=4 and non-Hamiltonicity is needed.