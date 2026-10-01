# Large-order endpoint reversal reduces to descent, a Hamiltonian six-set, or order disagreement

## Statement

Let H be a minimum counterexample of order at least fifteen containing a maximal unresolved endpoint reversal as in adecd58bef3d. Then either one of the earlier bounded four/five-vertex configurations from the reversal-localization chain occurs, or H admits a spanning three-cover with strictly smaller quadratic potential than the anchored state, or H contains a proper Hamiltonian six-vertex induced set U whose complement is non-Hamiltonian of path-cover number two, or H contains explicit relative-order disagreement between Hamiltonian paths on overlapping bounded supports.

## Body

Apply endpoint_reversal_sixdescent01. Since |V(H)|>=15, its small-order alternative is excluded. If one of its earlier bounded four/five-vertex alternatives occurs, this is the first conclusion. If its strict quadratic-descent alternative occurs, this is the second conclusion. Otherwise it yields a six-vertex set U.

If H[U] is Hamiltonian, U is proper. If H-U were Hamiltonian, Hamilton paths on U and H-U would form a spanning two-cover of H, impossible. Since H-U is a proper induced subtournament of the minimum counterexample, minimum-counterexample calculus gives path-cover number at most two; non-Hamiltonicity therefore gives path-cover number exactly two.

If H[U] is non-Hamiltonian, endpoint_reversal_sixdescent01 gives explicit relative-order disagreement among Hamiltonian one-vertex deletion paths of U. This is the final conclusion.