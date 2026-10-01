# Every top-boundary pattern containing d has a forced crossed-terminal orientation

## Statement

Assume q>=4 and the all-visible top-boundary q,(q+1)^3 four-slot normal form. Write
  a=g_{q-2}∩g_{q-1},
  b=private(g_{q-1}),
  x=g_{q-1}∩g_q,
  c=private(g_q),
  d=g_q∩g_{q+1},
and for an occupied slot y write
  h_y={y,v,z_y}.

Then every occupied triple containing d has the following forced orientation.

(1) Pattern abd:
  z_d has a path occurrence no later than g_{q-3};
  z_a lies in the right suffix g_q,...,g_{2q-3};
  z_b lies in the right suffix g_q,...,g_{2q-3}.

(2) Pattern bcd:
  z_d has a path occurrence no later than g_{q-3};
  z_b lies in the right suffix g_q,...,g_{2q-3}.

(3) Pattern acd:
  z_d has last occurrence at most q-4;
  z_c has last occurrence at most q-3;
  z_a has first occurrence at least q+2.

Thus every d-pattern contains at least one right-entrance/left-terminal high edge h_d and at least one left-entrance/right-terminal high edge; acd contains two right-entrance/left-terminal edges.

## Body

By 94bd984bc952, occupancy of d implies that the low terminal u is absent from the left prefix, and z_d lies in the left prefix. If b is also occupied, linearity excludes the exceptional possibility z_d=b, so z_d occurs no later than g_{q-3}. This proves the stated z_d bounds in abd and bcd. In acd, the sharper bound last(z_d)<=q-4 is 5d36d3a8d0ec.

If a is occupied, 8479f1cdc5d5 forces z_a into the right suffix g_q,...,g_{2q-3}. This gives z_a right in abd; in acd the sharper first-occurrence bound q+2 is again 5d36d3a8d0ec.

It remains to place z_b when b,d are occupied. Apply the conflict-pair lemma 872bb5f4effc to {b,d}. At least one of
  z_b ∈ V(g_{q+1}∪...∪g_{2q-3}),
or
  z_d ∈ V(g_{q+1}∪...∪g_{2q-3}∪g_{q-1})
must hold.
But z_d occurs on the strict left side no later than g_{q-3}, and because h_d already meets the path at entrance d and is linear, its opposite terminal cannot simultaneously occur in the disjoint right suffix. Hence the second alternative is impossible. Thus z_b lies in the right suffix. This proves (1) and (2).

Finally the z_c placement in acd is e0bd1cc438eb, completing (3).