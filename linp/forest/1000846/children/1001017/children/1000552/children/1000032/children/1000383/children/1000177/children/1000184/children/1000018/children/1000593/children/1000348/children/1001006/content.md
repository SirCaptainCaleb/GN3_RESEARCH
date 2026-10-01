# Every top-boundary pattern contains a far crossed pair

## Statement

Assume q>=4 and the all-visible top-boundary q,(q+1)^3 normal form
   P=(g_1,...,g_{2q-2}),
   a=g_{q-2}∩g_{q-1},
   b=private(g_{q-1}),
   x=g_{q-1}∩g_q,
   c=private(g_q),
   d=g_q∩g_{q+1},
with phi(x)=q-1. For every occupied slot y let
   h_y={y,v,z_y}
be its rank-(q+1) high edge.

For a path vertex w, write first_P(w) for the least index of a path edge containing w.

Then:

1. If c is occupied, z_c lies in the left prefix and
      first_P(z_c) <= q-4.

2. If d is occupied, z_d lies in the left prefix and
      first_P(z_d) <= q-4.

3. If a is occupied, z_a lies strictly in the right suffix
      V(g_{q+1}∪...∪g_{2q-3}).

4. If b and d are both occupied, z_b lies in the same strict right suffix.

Consequently every one of the four occupied triples abc, abd, acd, bcd contains a far crossed pair
   h_L={L,v,z_L}, h_R={R,v,z_R}
with
   L∈{a,b}, R∈{c,d},
   z_L∈V(g_{q+1}∪...∪g_{2q-3}),
   first_P(z_R)<=q-4.

## Body

We use first-occurrence coordinates for prefix splices, so a joint blocker is met only on the final retained prefix edge.

First consider an occupied right entrance r∈{c,d} once its opposite terminal z_r is known to lie in the left prefix. Let i=first_P(z_r). Then
   g_1,...,g_i,h_r,g_q
is linear: the prefix meets h_r only at z_r on g_i, the entrance r lies on g_q (for d also on omitted g_{q+1}), and v is absent from the precursor. The final edge g_q contains x, distinct from r, and g_{q-1} is omitted, so x is a physical last vertex. Hence
   i+2 <= phi(x)=q-1,
thus i<=q-3.                                            (A)

If in addition there is an occupied left entrance L∈{a,b} whose opposite terminal z_L lies strictly right of g_q, then the prefix through g_i avoids L by (A), and
   g_1,...,g_i,h_r,h_L,g_{q-1}
is linear. It has length i+3 and ends physically at x. Therefore
   i+3<=q-1,
so
   i<=q-4.                                               (B)

Now check the four slot patterns.

If a is occupied, 4b2eb2497cf0 gives z_a strictly in the right suffix. Thus assertion (3) holds.

For abc and acd, apply the conflict pair ac from 872bb5f4effc. Since z_a is neither left nor on g_q, the conflict alternative forces z_c into the left prefix. Taking h_L=h_a in (B) yields first_P(z_c)<=q-4.

For d, if b is occupied (patterns abd,bcd), 94bd984bc952 gives a left occurrence of z_d no later than g_{q-3}; hence z_d is in the left prefix and first_P(z_d)<=q-3. If instead the pattern is acd, the conflict pair ad and the strict-right localization of z_a force z_d into the left prefix, after which (A) again gives first_P(z_d)<=q-3.

In abd and acd, h_a supplies the left-to-right edge required in (B), so first_P(z_d)<=q-4.

It remains to treat bcd and to place z_b. We already have first_P(z_d)<=q-3. Apply the bd conflict from 872bb5f4effc. Its second alternative would place z_d on g_{q-1} or in the right suffix. This is impossible: a vertex whose first path occurrence is at most q-3 can occur only on that edge and possibly the immediately following edge, by linearity of P. Hence z_b lies in the strict right suffix. Now h_b is a left-to-right edge, so (B) sharpens first_P(z_d)<=q-4.

Finally, when c is occupied in bcd, 94bd984bc952 says the low terminal u is absent from the left prefix. Therefore the conditional recoil cad178c6e7ff applies to h_c and puts z_c in the left prefix. Using h_b in (B) gives first_P(z_c)<=q-4.

Thus every occupied right entrance has its terminal first contact by q-4, assertions (1)-(4) hold, and each slot pattern contains the stated far crossed pair.
