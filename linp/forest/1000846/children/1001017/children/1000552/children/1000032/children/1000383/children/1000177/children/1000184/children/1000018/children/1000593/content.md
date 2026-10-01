# A left-joint high entrance forces its high terminal across the central cut

## Statement

In the half-rank top-boundary q,(q+1)^3 configuration, if the left joint a=g_{q-2}∩g_{q-1} is a rank-(q+1) high entrance, then that high edge's opposite terminal must occur in the right suffix g_q,...,g_{2q-3}. Otherwise h_a,g_{2q-2},...,g_q is a q-edge path ending at the low entrance x, contradicting phi(x)=q-1.

## Body


Retain the top-boundary setup
  p=2q-2,
  P=(g_1,...,g_p) ending physically at v,
  e={x,v,u} rank q,
  x=g_{q-1} cap g_q.
Let
  a=g_{q-2} cap g_{q-1}
be the left-joint slot, and suppose a is the unique entrance of a rank-(q+1) high competitor
  h_a={a,v,z}.

Then z must occur in the right retained suffix
  g_q,g_{q+1},...,g_{p-1}.

Indeed suppose z were absent from that suffix. Consider
  h_a,g_p,g_{p-1},...,g_q.

The first two edges meet at v. The entrance a lies only in the omitted left-central edges g_{q-2},g_{q-1}; by assumption z is absent from g_q,...,g_{p-1}; and z cannot be v. Hence h_a has no nonconsecutive contact with the reversed suffix. The displayed sequence is therefore a linear path.

Its length is
  1+(p-q+1)=1+(q-1)=q.
Its final edge is g_q. Since g_{q-1} is omitted, the central joint x=g_{q-1} cap g_q occurs only in the final edge, and x is not in h_a because h_a and e already share v. Thus x is a physical last vertex of this q-edge path.

This contradicts phi(x)=q-1, since x is the entrance of the ascending rank-q edge e.

Therefore z lies in V(g_q union ... union g_{p-1}). Since phi(z)>=phi(v)=2q-2 by charging, a left-joint high entrance forces a high-potential opposite terminal across the central cut to the right.
