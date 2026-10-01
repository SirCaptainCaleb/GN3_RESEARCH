# 43/48 near-extremizers carry one-eighth paid progress-or-obstruction mass

## Statement

Let (H_j) satisfy the near-extremal hypotheses of d287da5967d5: S_j=sum_v phi(v), S_j/n_j^+ -> infinity, and |E(H_j)| >= (43/48)S_j-o(S_j). For each active misaligned vertex v use the switching family and chosen maximum path from b032348c1a8a, and let D_v^cell be the number of doubly occupied interior blocker cells while Y_v is the number of paid occupied cells in the sense of 9586a4d2317f. Then sum_v(D_v^cell+Y_v) >= (1/8-o(1))S_j. Every Y_v event is one of: a strict output-rank rise above phi(v); a special output edge of rank phi(v); or a nonspecial rank-phi(v) output whose forward joint has endpoint potential at least phi(v). Every D_v^cell event contains a linear 3-cycle formed by the host edge and its two blocker edges.

## Body

By d287da5967d5, the total local defect satisfies sum_v eta_v=o(S_j), the total endpoint-potential mass on inactive or aligned vertices is o(S_j), and therefore the active misaligned vertices carry S_j-o(S_j) potential mass. Vertices of bounded potential contribute O(n_j^+)=o(S_j), so we may discard them. For each remaining active misaligned vertex v, with p_v=phi(v), theorem 9586a4d2317f gives D_v^cell+Y_v >= p_v/8-eta_v-O(1). Summing over active misaligned vertices yields sum_v(D_v^cell+Y_v) >= (1/8)sum_v p_v - sum_v eta_v - O(n_j^+) = (1/8-o(1))S_j. The classification of Y_v and the 3-cycle structure of a doubly occupied cell are exactly the corresponding conclusions of 9586a4d2317f.
