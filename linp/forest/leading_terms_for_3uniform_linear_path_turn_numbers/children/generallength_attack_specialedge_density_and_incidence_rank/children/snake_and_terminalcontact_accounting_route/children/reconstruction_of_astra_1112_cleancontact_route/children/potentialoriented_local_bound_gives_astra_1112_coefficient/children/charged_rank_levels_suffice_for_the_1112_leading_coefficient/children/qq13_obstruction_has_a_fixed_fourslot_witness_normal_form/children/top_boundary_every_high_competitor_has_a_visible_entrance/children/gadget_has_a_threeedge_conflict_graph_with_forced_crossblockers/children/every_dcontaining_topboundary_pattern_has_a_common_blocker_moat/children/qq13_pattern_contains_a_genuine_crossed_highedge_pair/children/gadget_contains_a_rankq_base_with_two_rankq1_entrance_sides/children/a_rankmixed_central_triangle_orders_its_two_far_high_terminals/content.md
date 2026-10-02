# A rank-mixed central triangle orders its two far high terminals

## Statement

In the top-boundary q,(q+1)^3 configuration, suppose the left central base
  g_{q-1}={x,a,b}
has both terminals a,b occupied as high entrances:
  h_a={a,v,z_a}, h_b={b,v,z_b}.
Then z_a,z_b lie to the right of g_q. Let k_a,k_b be their first path-edge occurrence indices. Then
  k_a<=k_b.

Dually, if the right central base
  g_q={x,c,d}
has both c,d occupied, and i_c,i_d are the last path-edge occurrence indices of their opposite terminals on the left, then
  i_d>=i_c.

Thus on either fully occupied central base, the far terminal belonging to the joint entrance is weakly closer to the center in path order than the far terminal belonging to the private entrance.

## Body

Assume first that a,b are occupied. By 4b2eb2497cf0 and eddd8ad49835, z_a,z_b occur on the right side, with z_a strictly beyond g_q.

Suppose for contradiction that k_a>k_b. Consider
  g_1,...,g_{q-2}, h_a,h_b,
  g_{k_b},g_{k_b-1},...,g_q.
The prefix meets h_a at a. The two high edges meet at v. The edge h_b meets the reversed suffix at z_b, using its first occurrence so any possible second occurrence lies in the omitted edge g_{k_b+1}. The entrance b lies on omitted g_{q-1}. Since k_a>k_b, z_a is absent from the retained suffix; entrance a has already been used consecutively at the prefix end. Also v is absent from all retained P-edges because the final edge g_{2q-2} is omitted. Hence the sequence is linear.

Its length is
  (q-2)+2+(k_b-q+1)=k_b+1.
Its final edge is g_q. The predecessor in the reversed suffix meets g_q at its inherited right joint (or, if k_b=q, h_b meets g_q at z_b), while x=g_{q-1}∩g_q is distinct and g_{q-1} is omitted. Thus x is a physical last vertex.

Since k_b>=q, this gives a path of length at least q+1 ending at x, contradicting phi(x)=q-1. Therefore k_a<=k_b.

The right-base statement is the exact reversal. Under reversal of P, d is the joint entrance and c the private entrance. Applying the proved left-base inequality in reversed indices gives
  (2q-1-i_d) <= (2q-1-i_c),
hence i_d>=i_c.