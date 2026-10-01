# Persistent-defect shell coupling has multiplicity three when the defects are nonadjacent

## Statement

In each seven-vertex shell graph Omega_j of threeside01, fix distinct persistent defects z,z'. They have at least one common neighbor c outside {z,z'}; if zz' is not an edge of Omega_j, they have at least three such common neighbors. Every such c yields the paired Hamiltonian five-sets W_j-{z,c} and W_j-{z',c} with a common four-core, hence the full six-set transport dichotomy of 1000476.

## Body

Let S=V(Omega_j)-{z,z'}, so |S|=5. If zz' is an edge, N(z)∩S and N(z')∩S each have size at least 3 because delta(Omega_j)>=4, so their intersection has size at least 1. If zz' is not an edge, both neighborhoods lie in S and each has size at least 4, so their intersection has size at least 3. For any common neighbor c, the shell-edge definition makes both W_j-{z,c} and W_j-{z',c} Hamiltonian. They share W_j-{z,z',c}, so 1000476 applies.