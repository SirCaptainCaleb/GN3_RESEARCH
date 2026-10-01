# Unique auxiliary intersections of crossing endpoint lenses preserve potential-minus-position slack

## Statement

Let P be a maximum p-edge path ending at v. Let balanced endpoint lenses for retained vertices c,d have crossing host intervals [a,c] and [b,d] with a<b<c<d, and let P_c,P_d be the corresponding maximum endpoint paths ending at c,d. Let kappa_P(c),kappa_P(d) denote the host-prefix edge counts to the chosen occurrences of c,d on P. Suppose the two off-host lens sides have a clean intersection w and that w is the unique common vertex of the full maximum paths P_c and P_d. Then
phi(c)-kappa_P(c)=phi(d)-kappa_P(d).
Consequently, for a crossing pair of balanced endpoint lenses, either P_c and P_d have at least two common vertices, or their endpoint slack phi(.)-kappa_P(.) is equal.

## Body

Let the first host interval be [a,c] and the second [b,d]. Write L_1=|P[a,c]| and L_2=|P[b,d]|. Let alpha be the off-host distance from a to w along P_c and beta the off-host distance from b to w along P_d. By the exact crossing-lens cross-splice equality ff85a782d098, the first hybrid maximum path has length p, which gives alpha-beta=|P[a,b]|. Since the lens sides are balanced, the distance from w to the endpoint c along P_c is L_1-alpha, and from w to d along P_d is L_2-beta. Therefore the edge index of w measured from the initial end of P_c is phi(c)-(L_1-alpha), while on P_d it is phi(d)-(L_2-beta). If w is their unique common vertex, universal unique-intersection alignment 5854d853a44b forces these two indices to be equal. Substitute alpha-beta=|P[a,b]| together with L_1=|P[a,c]| and L_2=|P[b,d]|. After cancellation this becomes phi(c)-kappa_P(c)=phi(d)-kappa_P(d), where kappa_P(c),kappa_P(d) are the corresponding host-prefix coordinates. If the slack values differ, the unique-intersection alternative is impossible, so the two maximum endpoint paths must share a second vertex.
