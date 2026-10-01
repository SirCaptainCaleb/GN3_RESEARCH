# Near-saturated gap-one vertices force linearly many balanced endpoint lenses on one maximum path

## Statement

Retain the gap-one switching setup of fecba48a3ffd. Thus phi(v)=q+1, q(v)=q, P is an arbitrary maximum (q+1)-edge path ending at v, and
delta=gamma(q)-(t(v)-X_v^T).
Then P supports at least
gamma(q)-ceil((3q-4)/4)-delta
distinct balanced endpoint-lens states.

More precisely, there are that many distinct retained vertices c on P, each belonging to a switching edge f={v,c,d} that is double on a rank-q anchor path and single on P, such that for every chosen maximum endpoint path P_c ending at c, the pair P,P_c contains a balanced elementary lens adjacent to c.

Consequently a near-saturated gap-one vertex forces
(5/8)q-O(1)-delta
pairwise distinct endpoint labels on one maximum path, each carrying a balanced-lens/no-piercing barrier.

## Body

By fecba48a3ffd there is a switching matching of size
s>=gamma(q)-ceil((3q-4)/4)-delta.
For every switching edge f={v,c,d}, exactly one of c,d lies on P outside its last edge; call it c. Distinct switching edges have disjoint non-v pairs, so these retained vertices c are distinct.

Now apply b35b0fd4e4cd to the maximum path P and the vertex c. For any maximum endpoint path P_c ending at c, the two paths P and P_c have a second common vertex, and the elementary lens adjacent to c obtained from consecutive common vertices is balanced.

Thus each of the s distinct retained vertices contributes a distinct balanced endpoint-lens state attached to P, proving the exact lower bound. The asymptotic form follows from the exact floor-ceiling evaluation in fecba48a3ffd.
