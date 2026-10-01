# A right-joint high entrance excludes the low terminal from the left half

## Statement

In the half-rank top-boundary q,(q+1)^3 configuration with q>=4, suppose the right joint
 d=g_q∩g_{q+1}
is occupied by a rank-(q+1) high entrance h_d={d,v,z_d}. Let e={x,v,u} be the low rank-q edge with x=g_{q-1}∩g_q.

Then u is absent from the entire left prefix g_1∪...∪g_{q-1}.

Consequently z_d lies in the left prefix. More precisely, by 1adad81ca72e,
 z_d=b=private(g_{q-1})
or z_d has a path occurrence no later than g_{q-3}.
If b is itself occupied as another high entrance, the first alternative is impossible by linearity, so z_d occurs by g_{q-3}.

## Body

Suppose u occurs in the left prefix. By 1adad81ca72e(i), u is then the private vertex of g_1.

Consider
  g_2,g_3,...,g_{q-1}, e, g_{2q-2},g_{2q-3},...,g_{q+1}.

The left segment has q-2 edges and ends at x=g_{q-1}∩e. Because u is private in the omitted edge g_1, e has no other contact with this left segment. The edge e meets g_{2q-2} at v, and v is absent from the precursor because P ends at v. The reversed right suffix is separated from the left segment by the omitted central edge g_q. Hence the displayed sequence is linear.

Its length is
  (q-2)+1+(q-2)=2q-3.

Its final edge is g_{q+1}. Since g_q is omitted,
 d=g_q∩g_{q+1}
is a last vertex. But d is the entrance of a rank-(q+1) ascending edge, so phi(d)=q. For q>=4,
  2q-3>q,
contradiction.

Thus u is absent from the left prefix.

Now apply 1adad81ca72e(ii): z_d lies in the left prefix and is either b or occurs no later than g_{q-3}. If b is occupied as the entrance of another high edge h_b, then z_d=b would make h_d and h_b share both v and b, violating linearity.
