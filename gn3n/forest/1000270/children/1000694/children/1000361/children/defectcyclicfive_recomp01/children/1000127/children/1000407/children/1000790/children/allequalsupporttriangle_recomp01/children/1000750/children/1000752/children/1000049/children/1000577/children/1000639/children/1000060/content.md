# Successful insertion forces an endpoint-edge reversing triple; the cycle alternative is impossible

## Statement

Assume the all-three-successful-insertion branch of 1278e049ce8e. Then for some i there is a tight triple that reverses one of the two displayed endpoint edges of P_i=(t_i,M_i,t_{i+1}). In particular the order disagreement from e677f3148059 can, in this branch, always be localized to a component-end edge; the full-support tight-cycle alternative of b2f0a8047d8d never occurs.

## Body

Fix any j and let R_j be obtained by inserting t_{j+2} into P_j=(t_j,M_j,t_{j+1}). If the inserted t_{j+2} occurs before the terminal t_{j+1}, then R_j orders t_{j+2} before t_{j+1}, opposite to P_{j+1}, which orders t_{j+1} before t_{j+2}. Apply b2f0a8047d8d with i=j+1. In the decomposition of c36d628fe858, the reversed R_j-segment from t_{j+2} to t_{j+1} ends at the terminal vertex of R_j, so its exterior suffix R is empty. The cycle branch is impossible because c36d628fe858 would then Hamiltonize U=H-M_j, contradicting the known non-Hamiltonicity of that subtournament. Hence an endpoint-edge reversing triple is forced. Dually, if t_{j+2} occurs after the initial t_j, then R_j orders t_j before t_{j+2}, opposite to P_{j+2}, which orders t_{j+2} before t_j. Apply b2f0a8047d8d with i=j+2. Now the reversed segment begins at the initial vertex of R_j, so the exterior prefix L is empty, again excluding the cycle branch by c36d628fe858. Every insertion position is either before t_{j+1} or after t_j (indeed an internal insertion satisfies both), so one of the two arguments always applies.
