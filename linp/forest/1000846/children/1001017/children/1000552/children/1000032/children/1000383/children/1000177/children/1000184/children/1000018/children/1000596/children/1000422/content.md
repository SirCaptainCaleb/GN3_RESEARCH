# Corrected acd top-boundary blocker moat

## Statement

In the half-rank top-boundary q,(q+1)^3 configuration, suppose the occupied high-entrance slots are a,c,d (so b is omitted). Write
 h_a={a,v,z_a}, h_c={c,v,z_c}, h_d={d,v,z_d}.
Then:
(1) z_d has a path occurrence in the left prefix, and its last occurrence index there is at most q-4;
(2) z_a has a path occurrence in the right suffix and does not lie in g_q, hence its first path-edge occurrence on the right is at least q+1;
(3) z_c has a path occurrence in the left prefix, with last occurrence at most q-3.

Thus the two right-side high edges have distinct high-potential opposite terminals strictly left of the central cells, while the left-side high edge has its opposite terminal strictly right of g_q.

## Body

By 8479f1cdc5d5, since a is a high entrance, z_a lies in the right suffix g_q,...,g_{2q-3}. Because c,d are occupied high entrances and x belongs to the low edge, linearity forbids z_a from being any of x,c,d, the three vertices of g_q. Hence z_a does not occur in g_q, so its first right occurrence index is at least q+1.

Apply 872bb5f4effc to the conflict pair a,d. Since z_a is absent from both the left prefix and g_q, the other alternative is forced:
  z_d∈V(g_1∪...∪g_{q-2}).

Let i be the last edge index in the left prefix containing z_d. Consider
  g_1,...,g_i,h_d,h_a,g_{q-1}.
The prefix meets h_d only at its last z_d occurrence; h_d and h_a meet at v; h_a meets g_{q-1} at entrance a. Entrance d and terminal z_a are omitted. Thus the path is linear, has length i+3, and ends at x in g_{q-1}. Since phi(x)=q-1,
  i+3<=q-1,
so i<=q-4.

Finally apply 872bb5f4effc to a,c. Since z_a is absent from the left prefix and from g_q, it forces
  z_c∈V(g_1∪...∪g_{q-2}).
Let j be the last occurrence index of z_c there. The path
  g_1,...,g_j,h_c,g_q
is linear and ends at x. It has length j+2, so
  j+2<=phi(x)=q-1,
hence j<=q-3.

Correction from v1: no claim is made that first(z_a)>=q+2. If first(z_a)=q+1, the attempted reverse-suffix splice through h_a,h_d is cross-blocked because h_d also meets g_{q+1} at its entrance d.
