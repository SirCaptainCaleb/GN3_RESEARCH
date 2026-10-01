# Every anchored four-window has a repeated cross-endpoint five-set exchange core

## Statement

Let H be a minimum counterexample, let W be a Hamiltonian four-vertex support, and let H-W=P|Q be a two-cover with P=(p_0,...,p_m), Q=(q_0,...,q_s). Put E_P={p_0,p_m} and E_Q={q_0,q_s}. Then there exists w in W and two distinct cross pairs {e_1,f_1},{e_2,f_2} in E_P x E_Q such that both induced five-sets
F_1=(W-{w}) union {e_1,f_1},
F_2=(W-{w}) union {e_2,f_2}
are Hamiltonian. Consequently each H-F_i is non-Hamiltonian of path-cover number two. Thus every Hamiltonian four-side with two-cover complement contains a fixed three-vertex core supporting at least two distinct endpoint-pair Hamiltonian exchanges across the two complementary paths.

## Body

For each of the four cross pairs {e,f} with e in E_P and f in E_Q, apply the certified theorem twofourhamdeletions01 to the disjoint two-set {e,f} and the four-set W. It gives at least two vertices w in W for which {e,f} union (W-{w}) is Hamiltonian. Hence across the four cross pairs there are at least 8 incidences (w,{e,f}) with this property. Since W has four vertices, some w is incident with at least two distinct cross pairs. Fix such w and two corresponding pairs. The two resulting five-sets are proper Hamiltonian supports in a minimum counterexample, so each complement is non-Hamiltonian and has path-cover number exactly two by mincex01.
