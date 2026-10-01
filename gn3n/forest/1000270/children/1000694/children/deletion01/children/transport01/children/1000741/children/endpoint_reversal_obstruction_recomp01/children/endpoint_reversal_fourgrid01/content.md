# A maximal endpoint reversal yields a fixed-endpoint Hamiltonian four-grid away from its distinguished witness

## Statement

Let H be a minimum counterexample. Suppose P=(p_0,...,p_m), m>=2, and x outside P realize a maximal unresolved initial-end reversal (p_1,p_0,x), in the sense of adecd58bef3d. Then either H contains one of the bounded four-vertex configurations or proper Hamiltonian four/five-supports already listed in adecd58bef3d, or else, with Y=V(H)-(V(P) union {x}), one has |Y|>=3 and for every two distinct y,z in Y the four-set {p_0,p_m,y,z} is Hamiltonian. In the latter branch every such proper four-set has non-Hamiltonian complement of path-cover number two.

## Body

Apply adecd58bef3d. If its bounded four-vertex alternative or one of its Hamiltonian four/five-support alternatives occurs, we are done. Otherwise its residual conclusion holds for every vertex y in Y:=V(H)-(V(P) union {x}):
(p_1,p_0,y), (p_m,y,p_0), and (y,p_m,p_{m-1}) are tight.

In particular (p_m,y,p_0) is tight for every y in Y. Apply endpoint_reversal_fixedpair01 with b=p_m, a=p_0 and outside set Y. Then every distinct y,z in Y gives a Hamiltonian four-set {p_0,p_m,y,z}; explicitly, one of (y,p_m,z,p_0) and (z,p_m,y,p_0) is a tight Hamilton path.

Minimum-counterexample calculus says every tight path leaves at least four vertices, so |V(H)-V(P)|>=4. Since x is one of those vertices, |Y|>=3. Also n>10, so every displayed four-set is proper. Minimum-counterexample calculus then gives a non-Hamiltonian complement of path-cover number two.

No displayed path is reversed and no cyclic permutation of a tight triple is used.