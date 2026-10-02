# Synchronized endpoint barriers force reverse hooks on the first internal edges

## Statement

Assume the endpoint-barrier branch of e5d3ccfef9bb and |M_i|>=2. Write M_i=(b_i,c_i,...,z_i,a_i), where c_i is the second vertex and z_i the penultimate vertex of M_i (so for |M_i|=2, c_i=a_i and z_i=b_i). Then for every complementary endpoint d in E_i, both (c_i,b_i,d) and (d,a_i,z_i) are tight. Thus every blocked complementary endpoint creates reverse hooks on both first internal edges of the displayed support path P_i, uniformly in the length of M_i.

## Body

Fix d in E_i in the endpoint-barrier branch. By definition of this branch, H[S_i union {d}] is non-Hamiltonian, so d is automatically noninsertable into the displayed Hamilton path P_i=(t_i,b_i,c_i,...,z_i,a_i,t_{i+1}). The start barrier from e5d3ccfef9bb is (b_i,t_i,d), hence by cyclic invariance also (t_i,d,b_i) is tight. If (d,b_i,c_i) were tight, inserting d immediately after t_i in P_i would give a Hamilton path on S_i union {d}, contradiction. Hence (d,b_i,c_i) is non-tight, and boundary antisymmetry gives (c_i,b_i,d) tight. Dually, the terminal barrier (d,t_{i+1},a_i) cyclically gives (a_i,d,t_{i+1}) tight. If (z_i,a_i,d) were tight, inserting d immediately before t_{i+1} would Hamiltonize S_i union {d}, again a contradiction. Therefore its reverse (d,a_i,z_i) is tight. Apply to every d and every i.