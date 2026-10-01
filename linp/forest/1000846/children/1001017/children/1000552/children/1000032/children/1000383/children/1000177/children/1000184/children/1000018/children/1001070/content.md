# Every left-central high entrance sends its opposite terminal across the cut

## Statement

In the half-rank top-boundary q,(q+1)^3 configuration, let
 y∈{a,b}⊂V(g_{q-1})\{x}
be an occupied high entrance, and write h_y={y,v,z_y}. Then
  z_y ∈ V(g_q∪g_{q+1}∪...∪g_{2q-3}).
Thus every high edge whose entrance lies on the left central edge g_{q-1} sends its charged opposite terminal across the central cut to the right.

## Body

Suppose z_y were absent from the right suffix g_q,...,g_{2q-3}.

Consider
  h_y,g_{2q-2},g_{2q-3},...,g_q.

The edge h_y meets g_{2q-2} at the common terminal v. Its entrance y lies on g_{q-1}, which is omitted, and by assumption z_y is absent from the retained suffix. Hence h_y has no other contact with the suffix. The displayed sequence is therefore a linear path.

Its length is
  1+[(2q-2)-q+1]=q.

Its final edge is g_q. Since g_{q-1} is omitted, x=g_{q-1}∩g_q is a last vertex. Also x∉h_y because h_y and the low edge e already share v. Thus phi(x)>=q, contradicting phi(x)=q-1.

Therefore z_y lies in the right suffix.