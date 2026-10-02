# Every d-containing top-boundary pattern has a common blocker moat

## Statement

In the half-rank top-boundary q,(q+1)^3 configuration with q>=4, suppose the occupied high-entrance slots include d=g_q∩g_{q+1}. Then the high opposite terminals split 1-versus-2 across the central block. Every terminal on the left side has last path-edge occurrence at most q-4, while every terminal on the right side lies strictly to the right of g_q. More precisely: abd has z_d left with last<=q-4 and z_a,z_b right of g_q; acd has z_d,z_c left with last<=q-4 and z_a right of g_q; bcd has z_d,z_c left with last<=q-4 and z_b right of g_q. No q+2 first-occurrence bound is asserted; g_{q+1} is an exact residual cross-block state.

## Body


The bcd statement is c0b8ea014642.

For acd, the corrected moat 5d36d3a8d0ec gives
  last(z_d)<=q-4,
  z_a strictly to the right of g_q,
and e0bd1cc438eb gives last(z_c)<=q-3. We sharpen the latter by one. Since z_a is strictly right of g_q, it is absent from the left prefix. Let j be the last left occurrence of z_c. The sequence
  g_1,...,g_j,h_c,h_a,g_{q-1}
is linear: the prefix meets h_c only at z_c; h_c,h_a meet at v; h_a meets g_{q-1} at entrance a; z_a is right; c is on omitted g_q; and z_c is not in g_{q-1}. It has length j+3 and ends at x, so j+3<=q-1 and j<=q-4.

Now consider abd. Since d and b are occupied, 94bd984bc952 says u is absent from the left prefix and z_d occurs no later than g_{q-3}. Apply the bd conflict in 872bb5f4effc. The alternative putting z_d in g_{q-1} or the right suffix is impossible because z_d already occurs by q-3 and a path vertex can occur only in one edge or two consecutive edges. Hence z_b lies strictly to the right of g_q.

Likewise 4b2eb2497cf0 puts z_a strictly to the right of g_q.

Finally let i be the last left occurrence of z_d. Since z_b is strictly right of g_q,
  g_1,...,g_i,h_d,h_b,g_{q-1}
is linear, has length i+3, and ends at x. Thus i<=q-4.

Therefore the rigorously established common moat for every d-containing pattern is:
- every terminal on the left side has last occurrence at most q-4;
- every terminal on the right side is strictly to the right of g_q.

No claim is made that a right-side terminal first occurs at q+2. The exact g_{q+1} state remains possible because the reverse splice through h_*,h_d is cross-blocked by h_d meeting g_{q+1} at entrance d.
