# Above order seventeen global minimum-side deletion normalization yields strict quadratic descent or explicit disagreement

## Statement

Let H be a minimum counterexample of order n>=18 and let mu be the minimum smaller-component order among all one-vertex deletion two-covers. Then the global minimum-side deletion normalization yields at least one of the following: (1) an explicit support crossing—meaning an ordinary edge in a comparison cover whose endpoints lie in two different displayed path supports of the inherited deletion-state decomposition—or order disagreement; (2) a spanning three-cover lying in a pairwise-repartition component with strictly smaller quadratic potential than the natural three-cover supplied by the corresponding bounded Hamiltonian support or deletion singleton lift. In particular, at order at least eighteen the Hamiltonian four-window, Hamiltonian five-window, and endpoint cross-triple outputs of the minimum-side normalization are all nonterminal.

## Body

Apply 813e43ab1ba2. If its support-crossing or order-disagreement alternative occurs, outcome (1) holds, with support crossing understood as the explicit ordinary edge joining different displayed path supports in the compared deletion-state decomposition.

Suppose it gives a proper Hamiltonian five-set W with non-Hamiltonian path-cover-two complement. Since n>=18, ham5_large_escape01 gives strict Phi descent in the pairwise-repartition component of W|P|Q, or order disagreement.

Suppose instead it gives a proper Hamiltonian four-set W with path-cover-two complement. Apply 7bab8dd31d87: either W|P|Q has strict Phi descent, or order disagreement occurs, or there is a proper Hamiltonian six-set U with non-Hamiltonian path-cover-two complement. In the six-set branch apply ham6_large_escape01 to obtain strict descent or order disagreement.

Finally suppose 813e43ab1ba2 gives the minimum-side endpoint cross triple. Then 51d1f5232d68 gives strict Phi descent except at the order-eleven equality case; n>=18 excludes that exception. These cases exhaust the minimum-side normalization.