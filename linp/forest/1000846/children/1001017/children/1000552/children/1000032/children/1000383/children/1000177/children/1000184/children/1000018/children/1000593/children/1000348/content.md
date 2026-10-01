# A left-joint high entrance cannot close onto the central edge

## Statement

In the half-rank top-boundary q,(q+1)^3 gadget, if a=g_{q-2}∩g_{q-1} is a high entrance h_a={a,v,z_a}, then z_a cannot lie in g_q. Indeed g_1,...,g_{q-2},h_a,g_q is a q-edge path ending at x=g_{q-1}∩g_q, contradicting phi(x)=q-1. Hence z_a lies strictly in the right suffix g_{q+1},...,g_{2q-3}. In particular the proposed missing-slot closures z_a=d in abc and z_a=c in abd are impossible.

## Body

Retain the half-rank top-boundary setup
  P=(g_1,...,g_{2q-2}),
  x=g_{q-1} cap g_q,
  phi(x)=q-1,
and suppose
  a=g_{q-2} cap g_{q-1}
is occupied by a rank-(q+1) high entrance
  h_a={a,v,z_a}.

Assume for contradiction that z_a lies in g_q.

Consider
  g_1,...,g_{q-2}, h_a, g_q.                       (*)

This is a linear path:
- g_{q-2} meets h_a at a, since a lies in g_{q-2} and g_{q-1}, with g_{q-1} omitted;
- h_a meets g_q at z_a;
- the prefix g_1,...,g_{q-2} is disjoint from g_q, because g_q is two path positions beyond g_{q-2};
- the third vertex v of h_a is absent from the prefix and g_q because P ends at v only in g_{2q-2}.

The displayed path has
  (q-2)+2=q
edges.

Its final edge is g_q. The predecessor h_a meets g_q at z_a, while
  x=g_{q-1} cap g_q
is distinct from z_a: h_a cannot contain x because h_a and the low edge e already share v. Since g_{q-1} is omitted, x occurs only in the final edge of (*), so x is a last vertex.

Hence
  phi(x)>=q,
contradicting phi(x)=q-1.

Therefore z_a is never on g_q.

Combining with 8479f1cdc5d5, which puts z_a in the right suffix g_q,...,g_{2q-3}, one gets the sharper universal localization
  z_a in V(g_{q+1} union ... union g_{2q-3}).

Consequences:
- in pattern abc the proposed missing-slot closure z_a=d is impossible;
- in pattern abd the proposed missing-slot closure z_a=c is impossible.
Thus the two exact central escape states from 8d8bc213d83c do not survive.
