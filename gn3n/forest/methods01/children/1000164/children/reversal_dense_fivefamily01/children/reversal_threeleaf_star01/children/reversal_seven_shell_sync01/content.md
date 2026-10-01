# Every minimum counterexample has a seven-vertex reversal shell with synchronized bounded outputs

## Statement

Let H be a minimum counterexample. Then there exist a genuine reversing tight triple T, a vertex y outside T, and three distinct vertices z_1,z_2,z_3 outside T union {y} such that each five-set C union {z_i} is Hamiltonian, where C=V(T) union {y}. For arbitrary Hamilton paths P_i on C union {z_i}, at least one of the following occurs inside the seven-vertex shell C union {z_1,z_2,z_3}: (1) two P_i have order disagreement on C; (2) for some i!=j, C union {z_i,z_j} is Hamiltonian; (3) there is a Hamiltonian four-set contained in the shell; (4) for some i!=j and c in C, a tight triple on {z_i,c,z_j} reverses a displayed root-core edge of P_i or P_j. In outcomes (2) and (3), every resulting proper Hamiltonian support has non-Hamiltonian path-cover-two complement.

## Body

By reversal_threeleaf_star01, choose a genuine reversing tight triple T and an exterior vertex y incident in J_T to at least floor((n-4)/2) leaves. Since every minimum counterexample has n>10, floor((n-4)/2)>=3, so choose distinct leaves z_1,z_2,z_3. Put C=V(T) union {y}. By definition of the reversal star, each C union {z_i} is Hamiltonian. Choose arbitrary Hamilton paths P_i on those five-sets and apply three_fourcore_extensions_sync01 to the common four-core C and roots z_1,z_2,z_3. This gives exactly outcomes (1)-(4). Any Hamiltonian support arising in (2) has order six, and any in (3) has order four; both are proper because n>10. Minimum-counterexample calculus gives path-cover number at most two for the complement, while a Hamiltonian complement would combine with the Hamiltonian support to two-cover H. Hence each such complement is non-Hamiltonian with path-cover number two.
