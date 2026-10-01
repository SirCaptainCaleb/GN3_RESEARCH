# Every five-path to a high terminal of the 4445 triangle is suffix-blocked by the middle edge

## Statement

In the 4445 triangle setting of 0b8e51bfe396, let
  f_b={b,v,u_b}
and let g_3 contain b,c with phi(c)=3.

For every five-edge path
  R=(r_1,r_2,r_3,r_4,r_5)
ending at u_b, at least one of the following holds:
(i) r_4 meets f_b;
(ii) r_4 meets g_3;
(iii) r_5 meets g_3.

Equivalently, the four-edge sequence
  r_4,r_5,f_b,g_3
can never be a linear path.

Symmetrically, for every five-edge path ending at u_c, the analogous suffix through f_c and g_3 is blocked; otherwise it would give a four-edge path ending at b.

## Body

Because R ends at u_b, its last edge r_5 contains u_b. The edge f_b also contains u_b. By linearity, r_5∩f_b={u_b}.

Also f_b∩g_3={b}, by the canonical triangle 0b8e51bfe396. Hence the consecutive intersections required for
  r_4,r_5,f_b,g_3
are already valid:
  r_4∩r_5 is the path joint,
  r_5∩f_b={u_b},
  f_b∩g_3={b}.

Suppose none of (i),(ii),(iii) holds. Then r_4 is disjoint from the nonconsecutive edges f_b and g_3, and r_5 is disjoint from the nonconsecutive edge g_3. Therefore
  (r_4,r_5,f_b,g_3)
is a linear four-edge path.

Its last edge is g_3, and since the preceding edge f_b meets g_3 at b while c is a distinct vertex of g_3, c can be chosen as the last vertex. Hence phi(c)>=4, contradicting phi(c)=3.

Thus at least one of (i)-(iii) must hold. The argument with b,c and f_b,f_c interchanged proves the symmetric assertion.
