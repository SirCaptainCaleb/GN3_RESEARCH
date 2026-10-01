# The all-equal barrier branch canonically enters the four-side complement frontier

## Statement

Assume the synchronized endpoint-barrier branch of e5d3ccfef9bb. For each i modulo three let Q_i=(b_i,t_i,t_{i+2},a_{i+1}), the certified tight four-path from 2bac72daae4a. Then V(Q_i) is a Hamiltonian four-vertex support and H-V(Q_i) is non-Hamiltonian with path-cover number two. Hence choosing any two-cover P_i|R_i of H-V(Q_i) gives a spanning three-cover Q_i|P_i|R_i with a four-vertex path. The three four-sides are cyclically linked: Q_i and Q_{i+1} intersect exactly in t_i, and their union pattern is fixed by the transferred labels.

## Body

By 2bac72daae4a each Q_i is a tight four-vertex path, so its support is Hamiltonian. It is proper because the all-equal minimum counterexample has order n=3r>10. Minimum-counterexample calculus therefore gives pc(H-V(Q_i))<=2. The complement cannot be Hamiltonian: otherwise a Hamilton path on H-V(Q_i) together with Q_i would be a spanning two-cover of H. Thus pc(H-V(Q_i))=2. Choosing any two-cover P_i|R_i of the complement yields the stated three-cover. Pairwise overlap follows directly from Q_i={b_i,t_i,t_{i+2},a_{i+1}} and Q_{i+1}={b_{i+1},t_{i+1},t_i,a_{i+2}}; in the all-equal minimum-counterexample setting the endpoint labels are distinct, so the intersection is exactly {t_i}.