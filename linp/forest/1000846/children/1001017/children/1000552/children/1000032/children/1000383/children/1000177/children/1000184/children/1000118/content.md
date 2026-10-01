# A right-joint high entrance has only one near-central blocker slot

## Statement

In the top-boundary q,(q+1)^3 setting of 28445330afcc, suppose the right joint d=g_q∩g_{q+1} is the selected witness of a high competitor h_d={d,v,z}. Then d is its unique entrance and phi(d)=q. Let e={x,v,u} be the rank-q edge, with x=g_{q-1}∩g_q.

(i) If u lies in the left prefix g_1∪...∪g_{q-1}, then u is a free/private vertex of g_1.

(ii) If u is absent from the left prefix, then z lies in the left prefix. Moreover either z is the private vertex b of g_{q-1}, or z has a path occurrence no later than g_{q-3}. In particular z cannot be the left joint a=g_{q-2}∩g_{q-1}.

## Body

The entrance assertion is 28445330afcc, so phi(d)=q.

For (i), let i be the last path-edge occurrence of u before x. Since e and g_{q-1} already share x, linearity gives i<=q-2. The path
  g_1,...,g_i,e,g_{2q-2},g_{2q-3},...,g_{q+1}
has length i+q-1 and ends at d. It is linear because x lies in the omitted central edges and v is the e-to-last-edge joint. Hence
  i+q-1<=phi(d)=q,
so i=1. Thus u is free/private in g_1.

For (ii), if both u and z were absent from the left prefix, then
  g_1,...,g_{q-1},e,h_d
would be a (q+1)-edge path ending at d, contradicting phi(d)=q. Hence z is on the left prefix.

If z has an occurrence whose last relevant edge index i is at most q-2, then
  g_1,...,g_i,h_d,e
is linear: the prefix avoids x and u, h_d meets it only at z, h_d∩e={v}, and x is a last vertex of e. Therefore
  i+2<=phi(x)=q-1,
so i<=q-3.

It remains to inspect contacts involving g_{q-1}. The high edge cannot contain x, because it already shares v with e. If z is the joint
  a=g_{q-2}∩g_{q-1},
then
  g_1,...,g_{q-2},h_d,e
is a q-edge path ending at x, contradicting phi(x)=q-1. Thus the only contact whose last occurrence is g_{q-1} and which escapes the preceding splice is the private vertex b of g_{q-1}.

Hence, when u is absent, z is either b or lies no later than g_{q-3}.
