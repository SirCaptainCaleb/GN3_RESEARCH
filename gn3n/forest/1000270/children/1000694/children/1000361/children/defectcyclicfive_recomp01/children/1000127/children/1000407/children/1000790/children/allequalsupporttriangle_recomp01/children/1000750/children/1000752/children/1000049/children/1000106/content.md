# Successful transferred-label insertions fill the antipodal switch by a four-state singleton-transfer corridor

## Statement

Assume the all-three-successful-insertion branch of 1278e049ce8e. Fix cyclic indices i,i+1,i+2 and put T={t_i,t_{i+1},t_{i+2}} and U=H-M_{i+2}. Then U has four two-covers
M_i | (M_{i+1} union T),
(A_i) | S_{i+1},
S_i | (M_{i+1},t_{i+2}),
(M_i union T) | M_{i+1},
where A_i=(t_i,M_i), S_i=(t_i,M_i,t_{i+1}), S_{i+1}=(t_{i+1},M_{i+1},t_{i+2}), and the first and last mixed supports are the successful-insertion Hamiltonian supports M_{i+1} union T and M_i union T. Consecutive covers differ by moving exactly one transferred label from the right support to the left, in the order t_i,t_{i+1},t_{i+2}. Thus the antipodal support switch of 1278e049ce8e is filled by a four-state singleton-transfer corridor.

## Body

By 1278e049ce8e, M_i union T and M_{i+1} union T are Hamiltonian. The inherited paths M_i,M_{i+1}, A_i=(t_i,M_i), S_i=(t_i,M_i,t_{i+1}), S_{i+1}=(t_{i+1},M_{i+1},t_{i+2}), and (M_{i+1},t_{i+2}) are all tight from the base, support-triangle, and antipodal cube covers. Hence each displayed pair is a two-cover of U=H-M_{i+2}. The subtournament U is non-Hamiltonian because M_{i+2} is a tight path and a Hamilton path on U together with M_{i+2} would two-cover H. Comparing successive support partitions shows that the first move transfers only t_i, the second only t_{i+1}, and the third only t_{i+2}, always from the right support to the left while the M_i and M_{i+1} cores remain fixed.
