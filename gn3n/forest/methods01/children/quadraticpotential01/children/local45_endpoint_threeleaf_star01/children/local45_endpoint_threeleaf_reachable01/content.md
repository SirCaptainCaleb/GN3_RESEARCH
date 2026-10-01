# The endpoint three-leaf star lifts to reachable four-sides and synchronized interior locks

## Statement

In the setting of local45_endpoint_threeleaf_star01, the three leaves z_1,z_2,z_3 may be chosen together with witnesses w_1,w_2,w_3 in W such that A_i={u,v,z_i,w_i} is the four-side of a reachable balanced 4|5 plateau state A_i|B_i|P, the five-set {u,v,z_i,p_1,p_m} is Hamiltonian, and M union {w_i} is non-Hamiltonian with w_i noninsertable into the displayed path M. Consequently either at least two distinct witness labels occur among w_1,w_2,w_3, giving two distinct common-interior locks, or w_1=w_2=w_3=w and the plateau contains three reachable Hamiltonian four-sides {u,v,w,z_i} sharing the common three-core {u,v,w}, while w is locked against M.

## Body

In the proof of local45_endpoint_threeleaf_star01, each good triple T_i={u,v,z_i} belongs to the three-shadow of the family F of reachable Hamiltonian four-sides. Hence choose A_i in F containing T_i and let w_i be the unique vertex of A_i-T_i. By construction A_i|B_i|P is a reachable balanced plateau state in the same component. The definition of good gives T_i union {p_1,p_m} Hamiltonian. Since A_i|B_i|P is componentwise Phi-minimal, local_four_allfour_interior_lock01 applies to A_i and P, so M union {w_i} is non-Hamiltonian and w_i is noninsertable into every position of M. If the witnesses are not all equal, at least two distinct common-interior locks occur. If all three equal one label w, then the three distinct four-sides A_i={u,v,w,z_i} are reachable, Hamiltonian, and share the common three-core {u,v,w}; their pairwise differences are reciprocal one-label swaps, and the same w is locked against M.
