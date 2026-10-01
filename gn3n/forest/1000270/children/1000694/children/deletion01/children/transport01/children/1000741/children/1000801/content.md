# Cyclic comparison triangles give radius-two stable complements

## Statement

In a minimum counterexample, if a three-set T has a directed comparison 3-cycle and U is its complement, then U and every one- or two-vertex deletion of U is non-Hamiltonian with path-cover number two; every exact two-cover of U has both sides of order at least three.

## Body

For distinct d,e in U, T union {d,e} is Hamiltonian, since a non-Hamiltonian five-set has acyclic comparison digraph while T already contains a directed comparison cycle. Therefore U-{d,e} cannot be Hamiltonian, or complementary Hamilton paths would two-cover H; minimality gives path-cover number two. If U-d were Hamiltonian, deleting an endpoint e from such a path would Hamiltonize U-{d,e}, contradiction. Thus U-d has path-cover number two. Also U is non-Hamiltonian because T itself is a tight three-path, so T together with a Hamilton path of U would two-cover H. Finally a one- or two-vertex component in an exact two-cover of U would leave the other component Hamiltonian on one of the forbidden deletions.
