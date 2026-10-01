# The same-end shell-edge residue forces doubled reverse endpoint triples

## Statement

In the setting of 5a58f63e599d, suppose R=V(M) union {a,b} is non-Hamiltonian and both a,b have the same successful endpoint insertion position in the displayed path M. Then the Hamiltonian-support alternative in outcome (6) of 5a58f63e599d is impossible. Consequently the two explicit reverse endpoint triples supplied by 7b9f6ae39813 must both be tight.

## Body

Assume both labels left-extend M; the right-end case is symmetric. The inherited path P=(e,M,f) gives the opposite right extension (M,f). Apply 7b9f6ae39813 to a,b,M,f.

If its Hamiltonian alternative occurred, its proof supplies a tight Hamilton path on V(M) union {a,b,f} with f as the final vertex. Deleting this final endpoint leaves a tight Hamilton path on V(M) union {a,b}=V(R), contradicting the hypothesis that R is non-Hamiltonian.

Therefore only the reverse-endpoint alternative of 7b9f6ae39813 remains, giving both reverse triples through the initial vertex of M. The right-end version follows by symmetry.
