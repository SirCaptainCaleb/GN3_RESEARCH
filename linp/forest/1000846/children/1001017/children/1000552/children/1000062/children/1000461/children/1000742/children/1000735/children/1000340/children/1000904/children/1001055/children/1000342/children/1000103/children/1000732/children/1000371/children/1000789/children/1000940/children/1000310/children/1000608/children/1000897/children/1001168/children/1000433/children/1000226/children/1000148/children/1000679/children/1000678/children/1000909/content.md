# A nonboundary odd tight U_11 collision forces a full-length rotation and near-owner-rank output

## Statement

Retain the nonboundary odd tight collision of 9b00516e2965:
  r_i=2m+1 with m>=2,
  r_j=m+1,
  r_{j+1}=m+2,
  R_i=(g_1,...,g_{2m}),
  x_j=g_m intersect g_{m+1},
and assume E_{j+1}!=h=g_{2m}.

Then the exact contact of E_{j+1} on the precursor of R_i is the private vertex b_m of g_m. Consequently E_{j+1} intersect V(R_i)={b_m,x_i}, and
  g_1,...,g_m,E_{j+1},g_{2m},g_{2m-1},...,g_{m+2}
is a 2m-edge linear path.

In particular phi(g_{m+2})>=2m=r_i-1; and if z_{m+1}=g_{m+1} intersect g_{m+2} and b_{m+2} is the private vertex of g_{m+2}, then phi(z_{m+1}),phi(b_{m+2})>=2m.

No assertion is made here for the isolated boundary case m=2,E_{j+1}=h.

## Body

By 9b00516e2965, the genuine exact contact c_{j+1} is either a=g_{m-1} intersect g_m or the private vertex b_m of g_m.

The first possibility is impossible. The edge E_{j+1} contains a and the last vertex x_i of the 2m-edge path R_i. Apply a570c0ad0001 with p=2m and index m-1. It gives phi(g_m intersect g_{m+1})>=min{m+1,m+2}=m+1. But g_m intersect g_{m+1}=x_j is the unique entrance of the ascending rank-(m+1) edge E_j, so phi(x_j)=m, a contradiction. Therefore c_{j+1}=b_m.

Because E_{j+1}!=h, 608468bb403b gives E_{j+1} intersect V(R_i)={b_m,x_i}. Since b_m is private to g_m, a51a7f9cff95 applies with p=2m and contact index m, producing the 2m-edge path
  g_1,...,g_m,E_{j+1},g_{2m},g_{2m-1},...,g_{m+2}.
Its last edge is g_{m+2}, so phi(g_{m+2})>=2m.

The private vertex b_{m+2} is absent from every preceding edge of the rotated path. The joint z_{m+1}=g_{m+1} intersect g_{m+2} lies in the omitted edge g_{m+1}; by linearity it lies in no other retained g-edge, and it is absent from E_{j+1} because that edge meets R_i exactly at b_m and x_i. Hence either b_{m+2} or z_{m+1} may serve as the last vertex, giving vertex rank at least 2m for both.

The earlier unrestricted formulation omitted the boundary exclusion E_{j+1}!=h; this corrected lemma leaves the isolated boundary case to 9b023ed3d700.