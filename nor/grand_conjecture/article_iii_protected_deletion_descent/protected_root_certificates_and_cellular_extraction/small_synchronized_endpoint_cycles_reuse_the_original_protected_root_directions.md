# Small synchronized endpoint cycles reuse the original protected root directions

## Composition

(none yet)

## Development

Consider the injective synchronized endpoint obstruction of root 87:
rho_i=e_{x_i}-e_{x_{i+1}},
D_i=e_{a_{i+1}}-e_{a_i},
with all x_i distinct, all a_i distinct, and a_i distinct from x_i and x_{i+1}.

Assume the partner coordinate set equals the physical cycle coordinate set.

For k=3, the avoidance conditions force
a_i=x_{i-1}
cyclically, since among the three cycle coordinates the only choice other than x_i and x_{i+1} is x_{i-1}. Therefore
D_i=e_{x_i}-e_{x_{i-1}}=rho_{i-1}.

For k=4, the allowed partner matching from indices i to cycle coordinates excludes the diagonal i and successor i+1. The remaining bipartite graph is an 8-cycle and has exactly two perfect matchings. Hence either
a_i=x_{i-1} for every i
or
a_i=x_{i+2} for every i.
In the first case D_i=rho_{i-1}; in the second case
D_i=e_{x_{i+3}}-e_{x_{i+2}}=rho_{i+2}.

Thus for synchronized endpoint cycles of length three or four whose partner set equals the physical cycle set, the entire secondary cut-defect circulation is just a cyclic reindexing of the original protected-root circulation.

Equivalently, no new physical root directions occur. The obstruction is purely that each known protected root is carried at a different rank-two cut from the one needed to concatenate the Johnson orbit.

This sharply identifies the remaining low-length problem as provenance alignment. A successful local theorem need not manufacture a new root; it only needs to transport an already-realized protected direction to the adjacent rank-two cut. For k=3 this lives over the triangle Delta(3,2); for k=4 over one of the two cyclic shift patterns in J(4,2).

If the partner set is not equal to the physical set, or k>=5, arbitrary derangements remain possible and the conclusion need not hold.
