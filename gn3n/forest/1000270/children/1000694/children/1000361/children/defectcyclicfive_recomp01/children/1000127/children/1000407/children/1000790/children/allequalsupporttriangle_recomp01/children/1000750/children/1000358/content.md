# The all-equal barrier geometry has a rigid nine-label endpoint shell

## Statement

In the all-equal endpoint-barrier branch, put Omega={t_i,b_i,a_i : i=1,2,3}. Then all nine labels are distinct. For indices modulo three, E_i={b_{i+1},a_{i+1},t_{i+2},a_{i+2}}. Hence the six natural endpoint supports L_i={t_i,b_i} union E_i and R_i={a_i,t_{i+1}} union E_i satisfy L_i=Omega-{a_i,t_{i+1},b_{i+2}} and R_i={a_1,a_2,a_3} union {t_{i+1},b_{i+1},t_{i+2}}. Consequently the three omitted triples Omega-L_i are pairwise disjoint and partition Omega, while R_1,R_2,R_3 have common intersection {a_1,a_2,a_3} and pairwise intersections {a_1,a_2,a_3,t_j} for the appropriate transferred label t_j. This is a purely set-theoretic shell description; no Hamiltonicity of the six supports is asserted.

## Body

In a minimum counterexample the all-equal cube has n=3r>10, hence r>=4. Thus each M_i has order r-1>=3, so t_i,b_i,a_i are distinct within A_i, and different A_i are disjoint. Therefore Omega has order nine. By definition, E_i consists of the displayed endpoints of M_{i+1} and A_{i+2}; these are b_{i+1},a_{i+1},t_{i+2},a_{i+2}. Substitution gives L_i={t_i,b_i} union E_i=Omega-{a_i,t_{i+1},b_{i+2}} and R_i={a_i,t_{i+1}} union E_i={a_1,a_2,a_3} union {t_{i+1},b_{i+1},t_{i+2}}. The omitted triples Omega-L_i use each a-label, t-label and b-label exactly once as i varies, so they partition Omega. The common-core and pairwise-intersection formulas for the R_i follow immediately. The earlier Hamiltonicity assertion depended on 3ed34cc96c0d and is intentionally removed.
