# Opposite-end reversal structure forces a Hamiltonian six-support or six-vertex order disagreement

## Statement

Assume the hard endpoint-reversal residue of hardreversal_fiveshell01, with fixed endpoints a,b and at least four outside vertices. For every four distinct outside vertices y,z,w,t, put S={a,b,y,z,w,t}. Then either H[S] is Hamiltonian, in which case S is a proper Hamiltonian six-set whose complement is non-Hamiltonian with path-cover number two, or H[S] contains explicit order disagreement between Hamiltonian paths on two of its five-vertex deletions. Thus every four-label slice of the hard endpoint-reversal residue enters the Hamiltonian-six or order-disagreement interface.

## Body

By hardreversal_fiveshell01, deleting any one of y,z,w,t from S leaves a Hamiltonian five-set. Hence S has at least four Hamiltonian one-vertex deletions. If H[S] is non-Hamiltonian, apply astra004fourgooddisagree to those four deletion labels; it yields two Hamilton paths on distinct five-vertex deletions of S that order a common vertex pair oppositely, giving the order-disagreement alternative. If H[S] is Hamiltonian, S is proper because the hard-residue path P has at least one internal vertex outside {a,b} and the outside set has at least four vertices, so V(H)-S is nonempty. Minimum-counterexample calculus gives path-cover number at most two for H-S; it cannot be Hamiltonian, since a Hamilton path on S together with one on H-S would two-cover H. Therefore H-S is non-Hamiltonian with path-cover number two.