# Joint-pair conflict collapses to a left blocker or the missing right-private slot

## Statement

In the all-visible top-boundary q,(q+1)^3 gadget, if both joint slots a and d are occupied, then either the opposite terminal z_d of the d-edge lies in the strict left prefix g_1,...,g_{q-2}, or the opposite terminal z_a of the a-edge equals c, the right-private slot. Consequently in pattern acd one necessarily has z_d in the left prefix, while in pattern abd the only alternative is the exact missing-slot closure z_a=c.

## Body

Retain the all-visible top-boundary four-slot notation, and suppose the joint slots a and d are both occupied by high entrances:
  h_a={a,v,z_a},   h_d={d,v,z_d}.

By 8479f1cdc5d5,
  z_a in V(g_q union ... union g_{2q-3}).                 (1)

Apply the conflict-pair lemma 872bb5f4effc to the occupied pair {a,d}. It gives at least one of:
  z_d in V(g_1 union ... union g_{q-2}),                  (2)
or
  z_a in V(g_1 union ... union g_{q-2} union g_q).        (3)

Combining (1) and (3), the second alternative can hold only with
  z_a in g_q.
Now
  g_q={x,c,d},
where x is the low rank-q entrance, c is the right-private slot, and d is the occupied right-joint high entrance.

Linearity excludes z_a=x because h_a and the low edge e already share v.
Linearity excludes z_a=d because h_a and h_d already share v.
Hence the only possibility under alternative (3) is
  z_a=c.

Therefore, whenever a,d are occupied, either
  z_d lies in the strict left prefix g_1,...,g_{q-2},
or
  z_a=c.                                                  (4)

If c is also occupied as a high entrance, then z_a=c is impossible because h_a and h_c would share both v and c. Hence in the occupied triple {a,c,d}, necessarily
  z_d in V(g_1 union ... union g_{q-2}).

If instead the occupied triple is {a,b,d}, the only escape from a left-crossing z_d is the exact closure
  z_a=c,
where c is precisely the unique unoccupied central slot.
