# Three successful transferred-label insertions create antipodal common-core two-covers

## Statement

Assume the all-equal support-triangle setting and suppose, for every i modulo three, the transferred label t_{i+2} is insertable into P_i=(t_i,M_i,t_{i+1}). Put T={t_1,t_2,t_3}. Then H[M_i union T] is Hamiltonian for each i. Consequently, for every permutation {i,j,k}={1,2,3}, the proper subtournament U_k=H-M_k is non-Hamiltonian of path-cover number two and has the two explicit two-covers (M_i union T)|M_j and M_i|(M_j union T). Thus the all-three-insertable branch creates an antipodal common-core support switch in which the entire three-label set T moves from one core to the other.

## Body

Inserting t_{i+2} into P_i produces a Hamilton path R_i on S_i union {t_{i+2}}. Since S_i=V(A_i) union {t_{i+1}}=M_i union {t_i,t_{i+1}}, its support is exactly M_i union T. Fix distinct i,j,k. The sets M_i union T and M_j are disjoint and cover V(H)-M_k, so R_i|M_j is a two-cover of U_k=H-M_k. Similarly M_i|R_j is a two-cover of U_k. The subtournament U_k cannot be Hamiltonian, because M_k is itself a tight path and a Hamilton path on U_k together with M_k would give a spanning two-cover of H, contradicting pc(H)>2. Hence pc(U_k)=2. Their common cores are M_i,M_j, while all three labels in T lie on the first core in one cover and on the second core in the other.
