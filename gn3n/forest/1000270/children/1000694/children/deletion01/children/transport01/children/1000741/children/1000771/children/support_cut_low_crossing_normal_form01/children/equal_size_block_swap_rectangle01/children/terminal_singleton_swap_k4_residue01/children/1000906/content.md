# The paired terminal singleton-swap residue contains two positioned Hamiltonian five-supports

## Statement

Continue the hard same-end branch of terminal_singleton_swap_k4_residue01. Thus distinct labels x,y are swapped between tight flanks L,R of order at least two, and the endpoint four-sets are non-Hamiltonian matching-block K4s. Let l_1,l_2 be the last two vertices of L and r_1,r_2 the first two vertices of R, and put
U={l_1,l_2,x,y,r_1,r_2}.
Then at least two distinct d in {l_1,l_2,r_1,r_2} have H[U-{d}] Hamiltonian. Every such Hamiltonian five-set contains the swapped pair {x,y}; in a minimum counterexample its complement is non-Hamiltonian with path-cover number exactly two.

Consequently the paired matching-block six-vertex residue is not terminal: the hard terminal singleton-swap branch always produces at least two positioned Hamiltonian five-supports through the swapped pair. Combining this with the other branches of terminal_singleton_swap_k4_residue01, every terminal singleton swap with both flanks of order at least two produces a proper Hamiltonian support with non-Hamiltonian pc2 complement.

## Body

The six vertices in the paired endpoint residue are distinct because L,R and {x,y} are disjoint supports in the spanning three-cover. Apply sixset_prescribed_pair_menu01 to U with prescribed pair p=x,q=y and four-set A={l_1,l_2,r_1,r_2}. Its unconditional first conclusion gives at least two distinct d in A for which U-{d} is Hamiltonian. No matching-block hypothesis is needed for this existence statement; the paired residue merely supplies the naturally positioned six-window U.

Each U-{d} is a proper Hamiltonian five-set. Since H is a minimum counterexample, mincex01 implies that its complement has path-cover number at most two; it cannot be Hamiltonian, because a Hamilton path on U-{d} together with one on its complement would two-cover H. Hence the complement is non-Hamiltonian with path-cover number exactly two.

Thus the final matching-block alternative of terminal_singleton_swap_k4_residue01 immediately lifts to two standard Hamiltonian-five-side inputs retaining x,y. The other alternatives of that theorem already give a proper Hamiltonian support with pc2 complement, so every long-flank terminal singleton swap has such an output.