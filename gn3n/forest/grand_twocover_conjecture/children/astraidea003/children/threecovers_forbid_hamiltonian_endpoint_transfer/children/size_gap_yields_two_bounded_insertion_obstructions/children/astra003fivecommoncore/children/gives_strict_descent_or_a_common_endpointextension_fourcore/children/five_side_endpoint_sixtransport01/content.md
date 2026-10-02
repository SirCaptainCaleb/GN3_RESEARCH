# A trapped five-side exposes a positioned six-support or four-good-deletion transport package

## Statement

Let H be a minimum counterexample and let X|P|Q be a spanning three-cover that minimizes quadratic potential within its connected pairwise-repartition component, where |X|=5 and P=(p_1,...,p_m) has m>=7. Then either one legal pairwise repartition of X|P strictly decreases quadratic potential, or there exist distinct x,z_1,z_2 in X and the six-set U=(X-{x}) union {p_1,p_m} such that U-{p_1}, U-{p_m}, U-{z_1}, and U-{z_2} are Hamiltonian. In the latter branch, either U itself is Hamiltonian, with H-U non-Hamiltonian of path-cover number two, or U is non-Hamiltonian and its graph on Hamiltonian deletions contains the four positioned labels p_1,p_m,z_1,z_2; in particular H-U+d is non-Hamiltonian of path-cover number two for every Hamiltonian deletion label d, and the graph defined by Hamiltonian two-vertex deletions has minimum degree at least one.

## Body

Apply bc48e8bb931a. If an endpoint transfer from P into X gives strict descent, we are done. Otherwise both six-sets X union {p_1} and X union {p_m} are non-Hamiltonian. Apply five_side_two_bad_endpoint_sixpackage01 to X with e=p_1 and f=p_m. It yields distinct x,z_1,z_2 in X such that U=(X-{x}) union {p_1,p_m} has the four named Hamiltonian deletions p_1,p_m,z_1,z_2.

If U is Hamiltonian, it is proper and minimum-counterexample calculus gives pc(H-U)<=2; H-U cannot be Hamiltonian, since together with U that would two-cover H. Hence H-U is non-Hamiltonian with path-cover number two.

If U is non-Hamiltonian, apply d2205c472e75. Its Hamiltonian-deletion set contains the four named labels, every one-label complement extension H-U+d is non-Hamiltonian with path-cover number two, and the graph on Hamiltonian deletion labels defined by Hamiltonian two-deletions has minimum degree at least one, with every graph edge giving the corresponding two-label pc2 complement extension. This is the asserted positioned transport package.