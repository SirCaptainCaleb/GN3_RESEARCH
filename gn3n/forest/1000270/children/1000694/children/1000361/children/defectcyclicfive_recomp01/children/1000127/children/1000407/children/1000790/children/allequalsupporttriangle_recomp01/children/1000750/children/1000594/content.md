# Three endpoint barriers force mixed Hamiltonian five-sets with two-coverable complements

## Statement

Assume the endpoint-barrier branch of e5d3ccfef9bb. Fix i and choose any three distinct vertices d_1,d_2,d_3 in E_i. Then both five-sets {t_i,b_i,d_1,d_2,d_3} and {a_i,t_{i+1},d_1,d_2,d_3} are Hamiltonian. Since H is a minimum counterexample, the complement of each proper Hamiltonian five-set is non-Hamiltonian and has path-cover number two. Thus whenever |E_i|>=3, the all-equal residue supplies, at each end of S_i, a family of bounded mixed Hamiltonian supports with two-coverable non-Hamiltonian complements.

## Body

For each d in E_i, e5d3ccfef9bb gives (b_i,t_i,d) tight, hence by cyclic invariance (t_i,d,b_i) tight. Apply the certified three-common-endpoint Hamilton-five-path lemma in smallset01 with outer vertices t_i,b_i and middle vertices d_1,d_2,d_3. This gives a Hamilton path on {t_i,b_i,d_1,d_2,d_3}. Likewise the terminal barriers (d,t_{i+1},a_i) cyclically give (a_i,d,t_{i+1}) for all d, so the same lemma gives Hamiltonicity of {a_i,t_{i+1},d_1,d_2,d_3}. Each five-set is proper. By the minimum-counterexample calculus, the complement of any proper Hamiltonian support has path-cover number two; it cannot be Hamiltonian, since otherwise H itself would have a spanning two-cover.
