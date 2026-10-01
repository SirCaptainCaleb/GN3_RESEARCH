# A failed transferred-label insertion forces a cyclic support or an explicit endpoint hook

## Statement

In the all-equal support-triangle setting, fix j modulo three and suppose the transferred label t_{j+1} is noninsertable into P_{j-1}, with H[S_{j-1} union {t_{j+1}}] non-Hamiltonian. Then, writing P_j=(t_j,b_j,...,a_j,t_{j+1}), at least one of the following holds: (1) (t_j,t_{j+1},a_j) is tight; (2) (b_j,t_j,t_{j+1}) is tight; or (3) S_j has the tight cyclic order (t_{j+1},t_j,b_j,...,a_j). Thus the noninsertable/non-Hamiltonian branch of the all-equal argument yields an explicit endpoint hook at one end of the adjacent support or makes that entire support cyclic.

## Body

The terminal barrier for S_{j-1}, applied to d=t_{j+1}, gives Q=(t_{j+1},t_j,a_{j-1}) as a tight path. Compare Q with P_j=(t_j,b_j,...,a_j,t_{j+1}). Their only common vertices are the endpoints t_j,t_{j+1}, in reverse order. Specialize the proof of pathcalc01 Section 4. The detour Q from t_{j+1} back to t_j is the single ordinary edge t_{j+1}t_j. The two join triples required to close P_j with this edge are (a_j,t_{j+1},t_j) and (t_{j+1},t_j,b_j). If the first is non-tight, boundary antisymmetry gives its reverse (t_j,t_{j+1},a_j), outcome (1). If the second is non-tight, its reverse (b_j,t_j,t_{j+1}) is tight, outcome (2). If both are tight, the cyclic word (t_{j+1},t_j,b_j,...,a_j) has every cyclic consecutive triple tight, giving outcome (3). No cyclic permutation of an ordered triple is used.
