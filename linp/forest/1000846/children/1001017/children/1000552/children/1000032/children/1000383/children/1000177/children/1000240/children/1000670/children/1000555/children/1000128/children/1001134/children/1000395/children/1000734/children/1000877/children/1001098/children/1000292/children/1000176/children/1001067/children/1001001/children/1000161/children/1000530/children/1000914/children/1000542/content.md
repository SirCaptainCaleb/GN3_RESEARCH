# Strict-gap U11 whole chords carry a three-cycle packet

## Statement

Let e={x,u,v} be an ascending nonspecial edge of rank r. Let t be either terminal u or v, and let P_t be a maximum endpoint path ending at t with phi(t)>r. Assume e is terminal-single on P_t. Let c_t be the unique vertex of e\{t} occurring on the precursor of P_t, and let b_t be the last path-edge index containing c_t.

Then e together with the suffix of P_t from that last occurrence of c_t to the endpoint t is a linear cycle C_t containing e, and
  |C_t|<=r.

Consequently every strict-gap doubly-terminal-single edge carries two canonical rank-budgeted terminal cycles C_u,C_v.

If, in addition, e is a whole chord on a path R avoiding the third/common terminal and containing its entrance x and the opposite terminal, then e also carries the anchor cycle
  C_R=e union R[x,opposite terminal],
again of length at most r.

Hence a same-terminal selected whole-chord edge in the strict-gap U11 class naturally carries a three-cycle packet, all three cycles containing the same nonspecial edge e and each having length at most phi(e).

## Body

Fix a terminal t. Since phi(t)>r, e is not an edge of P_t. Let c_t be the unique off-t e-contact with the precursor, guaranteed by terminal-singleness. Choose the last path edge g_b containing c_t. The endpoint t lies in the final path edge, and linearity prevents c_t from lying in that final edge together with t, since e is distinct from it.

By the choice of the last occurrence, the suffix g_b,...,g_s meets e only at c_t in its first edge and at t in its final edge. The other vertex of e\{t,c_t} is absent from P_t by terminal-singleness. Thus
  e,g_b,...,g_s
is a linear cycle containing e. The cycle-rank theorem f2925a904b8e yields length at most r.

Apply this independently at u and v to obtain the two terminal cycles.

For the anchor cycle, use cd38122f7d7d: any path avoiding one terminal and containing the other two vertices of e closes with e to a linear cycle, again of length at most r.

No selected-cell details are needed once the whole-chord and U11 hypotheses have been established.