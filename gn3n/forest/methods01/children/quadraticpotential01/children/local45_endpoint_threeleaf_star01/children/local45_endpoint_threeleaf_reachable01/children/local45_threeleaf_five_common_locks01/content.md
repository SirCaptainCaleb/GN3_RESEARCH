# The endpoint three-leaf star forces five common long-interior locks

## Statement

Let H be a minimum counterexample and let X|Y|P be a componentwise Phi-minimal 4|5|m state with m>=6. In the endpoint three-leaf configuration of local45_endpoint_threeleaf_reachable01, the five distinct labels u,v,z_1,z_2,z_3 are all noninsertable into the same displayed interior M=(p_2,...,p_{m-1}). Consequently either a first-type failed-insertion obstruction among these five labels yields a Hamiltonian four-window or the universal cyclic four-kernel, or two second-type obstructions share a gap and yield a Hamiltonian mixed four-set, or m>=8 and the five labels occupy five distinct second-type gaps of M with the full pairwise spacing trichotomy. In particular, for m=6 or 7 a bounded Hamiltonian four-window or cyclic four-kernel is forced.

## Body

By local45_endpoint_threeleaf_reachable01, for each i there is a reachable balanced plateau state A_i|B_i|P with A_i={u,v,z_i,w_i}. Every such state is componentwise Phi-minimal. Apply local_four_allfour_interior_lock01 to A_i and P. It says every vertex of A_i is noninsertable into M. Hence u,v and each z_i are all noninsertable into M, giving five distinct common locks. Apply insert01 to these five labels. If any obstruction is first-type, 0425e03e2aa3 gives a Hamiltonian four-window or the universal cyclic four-kernel. Otherwise all are second-type. If two use the same gap, 36fccff06d48 gives a Hamiltonian four-set on those two labels and the gap edge. If neither bounded outcome occurs, the five second-type gaps are distinct. M has m-2 vertices and m-3 displayed gaps, so m-3>=5 and m>=8. The remaining pairwise statements are exactly the adjacent/separated conclusions of 36fccff06d48.
