# Every overlap-maximal return-order inversion pays one edge of metric deficit

## Statement

Retain the return-order inversion branch (C) of c10cb2dd049c. Choose the maximum endpoint path S with last vertex x, among those avoiding u,v, to maximize |V(S) intersect V(R)| as in 813525f7f639. Let z_R be the common vertex nearest x in the R-order, and let z_S be the common vertex nearest x in the S-order. Then
  z_R != z_S,
with z_R between z_S and x on R and z_S between z_R and x on S.

Put
  s=|R[z_R,x]|,
  d=|S[z_R,x]|.
Then
  d >= s+1.

Thus every return-order inversion on an overlap-maximal source-clean maximum path carries a strict integer metric deficit; the zero-deficit saturation alternative of 813525f7f639 cannot occur in branch (C).

## Body

By 813525f7f639,
  d>=s.
Suppose for contradiction that d=s. Then every internal vertex of the S-segment S[z_R,x] belongs to V(R).

Because z_S lies strictly between z_R and x on S, the terminal S-segment S[z_S,x] is nonempty. A nonempty segment of a 3-uniform linear path between two distinct boundary vertices contains at least one vertex other than its two boundary vertices: if it has one edge, that edge has a third vertex; if it has more than one edge, it has internal path vertices. Every such vertex is an internal vertex of S[z_R,x].

By the assumed equality d=s and the saturation conclusion, that vertex belongs to R. It therefore gives a common vertex of S and R strictly between z_S and x along S, contradicting the definition of z_S as the common vertex nearest x in the S-order.

Hence equality is impossible and
  d>=s+1.
