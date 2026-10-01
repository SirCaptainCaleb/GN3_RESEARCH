# Every top-boundary q,(q+1)^3 pattern contains a genuine crossed high-edge pair

## Statement

Assume q>=4 and the all-visible top-boundary q,(q+1)^3 configuration on a maximum
  P=(g_1,...,g_{2q-2})
ending at v, with low entrance
  x=g_{q-1}∩g_q
and high entrance slots
  a=g_{q-2}∩g_{q-1},
  b=private(g_{q-1}),
  c=private(g_q),
  d=g_q∩g_{q+1}.

Then among the three occupied high edges there exist two,
  h_L={y_L,v,z_L}, h_R={y_R,v,z_R},
such that
  y_L∈V(g_{q-1})\{x},   z_L∈V(g_q∪...∪g_{2q-3}),
while
  y_R∈V(g_q)\{x},       z_R∈V(g_1∪...∪g_{q-2}).

Thus one high edge crosses the central cut left-to-right and another crosses it right-to-left.

Moreover, if d is occupied then the right-to-left terminal may be chosen with last occurrence at most q-4 and the left-to-right terminal with first occurrence at least q+2, by d22fb281de15.

## Body

If d is occupied, this is exactly the crossed-terminal orientation supplied by d22fb281de15: in each of abd, acd, bcd there are occupied entrances on opposite sides whose opposite terminals lie on the opposite far sides.

It remains only pattern abc. Here a,c are occupied. By 4b2eb2497cf0,
  z_a∈V(g_{q+1}∪...∪g_{2q-3}),
so h_a crosses left-to-right.

Apply the ac conflict of 872bb5f4effc. Its alternatives are
  z_c∈V(g_1∪...∪g_{q-2})
or
  z_a∈V(g_1∪...∪g_{q-2}∪g_q).
The second is impossible because 4b2eb2497cf0 places z_a strictly in the right suffix starting at g_{q+1}. Hence z_c lies in the left prefix, and h_c crosses right-to-left.

This proves the universal crossed-pair statement.
