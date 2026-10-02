# Every persistent-defect shell yields order disagreement or a full two-label square

## Statement

In the three-side fixed-defect transport setup, fix distinct persistent defects z,z' in Z. For each rooted seven-set shell W_j, there is a vertex c_j such that U_j=W_j-{c_j} contains two Hamiltonian five-deletions U_j-z and U_j-z'. Then one of the following holds for that shell: (1) U_j is non-Hamiltonian, in which case two Hamilton paths on distinct five-deletions of U_j exhibit relative-order disagreement on common vertices; or (2) U_j is Hamiltonian, H-U_j is non-Hamiltonian with path-cover number two, and U_j contains a full two-label square: there are distinct d,e in U_j such that H-U_j, H-(U_j-{d}), H-(U_j-{e}), and H-(U_j-{d,e}) are all non-Hamiltonian with path-cover number two, while U_j-d, U_j-e, and U_j-{d,e} are Hamiltonian. Thus each of the four shells supplies either localized order disagreement or a Hamiltonian-six-set two-label transport square.

## Body

Fix a shell index j. By defects_share_a_shell_neighbor_in_every_rooted_sevenset there is c_j such that U_j=W_j-{c_j} has the two Hamiltonian one-vertex deletions U_j-z and U_j-z'. Moreover defects_share_a_shell_neighbor_in_every_rooted_sevenset obtains U_j from two Hamiltonian five-sets with a common four-core, so the dichotomy of yield_a_hamiltonian_sixset_or_fourgooddeletion_transport applies.

If U_j is non-Hamiltonian, yield_a_hamiltonian_sixset_or_fourgooddeletion_transport says its Hamiltonian-deletion set has order at least four. The six-set U_j is proper because H is a minimum counterexample of order greater than ten. Therefore four_good_six_interface01 applies and yields two Hamilton paths on distinct five-vertex deletions of U_j with relative-order disagreement on common vertices.

If U_j is Hamiltonian, yield_a_hamiltonian_sixset_or_fourgooddeletion_transport gives that H-U_j is non-Hamiltonian with path-cover number two. Apply ham6goodsquare01 to U_j. It supplies distinct d,e in U_j such that U_j-d, U_j-e, and U_j-{d,e} are Hamiltonian, while each of H-U_j, H-(U_j-{d}), H-(U_j-{e}), and H-(U_j-{d,e}) is non-Hamiltonian with path-cover number two.

The argument is independent of j, so it holds in all four rooted shells. This converts the shellwise persistent-defect coupling into the standard disturbance fork of localized order disagreement versus a full two-label path-cover square.