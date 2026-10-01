# Greedy endpoint transport carries a mandatory deletion-crossing cut at every successful step

## Statement

Assume the endpoint-transport branch of endpoint_hamiltonicity_crossing_plus_transport01. In the terminal-end orientation, let R_j be the greedy Hamilton path on S_j=X union {c_0,...,c_j} ending in c_j for 0<=j<=h, where h<m is the first failed append index. Then for every j=0,...,h, every two-cover of H-c_j contains an ordinary path edge crossing the cut (S_j-{c_j}) | (V(H)-S_j). At j=h the failed append additionally gives the tight reverse end hook (c_{h+1},c_h,q), where q is the predecessor of c_h in R_h. The initial-end orientation is symmetric.

## Body

The greedy endpoint-transport theorem 1000437 supplies the Hamilton paths R_j on S_j at every successful stage through the first failed append h<m. Fix j<=h. The cut sides are both nonempty: S_j-{c_j} contains X, while V(H)-S_j contains at least c_{j+1} and the third displayed component. Since H[S_j] is Hamiltonian, hamiltonian_enlargement_forces_crossing01 applied with deletion label c_j forces every two-cover of H-c_j to cross the displayed cut. This holds independently for every successful stage. At j=h, 1000437 also supplies the failed final append and hence the reverse end hook (c_{h+1},c_h,q).