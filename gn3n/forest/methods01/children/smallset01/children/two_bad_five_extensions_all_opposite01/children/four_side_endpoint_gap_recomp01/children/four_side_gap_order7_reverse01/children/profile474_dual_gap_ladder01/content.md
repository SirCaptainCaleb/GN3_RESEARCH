# Dual hard locks in a 4|7|4 cover force four gap-aligned triple-component Hamiltonian four-sets

## Statement

Let H be a minimum counterexample and let A|R|B be a spanning three-cover of component orders 4|7|4, with displayed four-paths A=(a_0,a_1,a_2,a_3), B=(c_0,c_1,c_2,c_3), and R=(r_0,r_1,...,r_6). Put M=(r_1,...,r_5). Suppose applying four_side_endpoint_lock_gap_network01 to each of A|R and B|R yields neither a strict quadratic-potential descent nor a genuinely mixed Hamiltonian four/five-support. Then both pairs lie in the hard gap-network branch, their obstruction-gap assignments are synchronized as g(a_i)=g(c_i)=4-i, and for each i=0,1,2,3 the four-set W_i={a_i,c_i,r_{4-i},r_{5-i}} is Hamiltonian. Each W_i meets all three original components and H-W_i is non-Hamiltonian with path-cover number two.

## Body

Because |R|=7, outcome (1) of four_side_endpoint_lock_gap_network01 would be a strict (4,7)->(5,6) quadratic descent, while outcome (2) is exactly a genuinely mixed Hamiltonian four/five-support. By hypothesis neither occurs for A|R or B|R, so both are in the hard gap-network outcome (3). Apply four_side_gap_order7_reverse01 to A and to B. With M=(r_1,...,r_5), its four gaps are r_1|r_2, r_2|r_3, r_3|r_4, r_4|r_5, indexed 1,2,3,4. Hence g(a_i)=g(c_i)=4-i for every i. Fix i and set k=4-i. Then a_i and c_i have second-type failed-insertion obstructions at the same gap r_k|r_{k+1} of M. Apply the equal-gap case of 36fccff06d48. It gives a tight Hamiltonian four-path on {a_i,c_i,r_k,r_{k+1}}, so W_i is Hamiltonian. Since H is a minimum counterexample and W_i is proper, mincex01 gives that H-W_i is non-Hamiltonian with path-cover number two. Each W_i contains one vertex from A, one from B, and two from R, so it is genuinely triple-component positioned.
