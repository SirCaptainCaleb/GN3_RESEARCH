# Overlap-maximal source-clean paths make entrance-side inversions pay deficit or saturation

## Statement

Let e={x,v,u} be an ascending nonspecial edge of edge rank r with unique entrance x. Let R be a linear path avoiding v and containing x,u, oriented so that x occurs before u.

Among all maximum endpoint paths S with last vertex x that avoid u,v, choose S maximizing
  |V(S) intersect V(R)|.
Let a,b be common vertices of S and R such that the R-segment R[a,b]:
(1) lies entirely on the side of x opposite u, and
(2) meets S only at a,b.

Put
  s=|R[a,b]|,  d=|S[a,b]|
for the corresponding S-segment between a,b.

Then d>=s. If d=s, every internal vertex of S[a,b] belongs to V(R).

In particular, in the return-order inversion branch of c10cb2dd049c, let z_R be the common vertex nearest x in the R-order. Then
  |S[z_R,x]| >= |R[z_R,x]|.
If equality holds, every internal vertex of S[z_R,x] lies somewhere on R. Thus an order inversion at an overlap-maximal clean source path either pays a positive integer length deficit or lies inside a source segment completely saturated by common-precursor vertices.

## Body

The proof is the overlap-maximal switching argument of 47e9d5af3551, with the additional observation that the replacement stays inside the class of maximum x-ending paths avoiding u,v.

Because R[a,b] lies on the side of x opposite u and R avoids v, its vertices avoid u,v. By hypothesis its open segment is disjoint from S. Replace the S-segment S[a,b] by R[a,b]. The result S' is a linear path ending at x, still avoiding u,v, with
  |S'|=|S|-d+s.
Since S is maximum at x, s<=d.

Suppose d=s. Then S' is again a maximum x-ending path avoiding u,v, so it is an admissible competitor in the overlap-maximal choice of S. The R-segment R[a,b] has 2s-1 internal vertices, all new to S because R[a,b] meets S only at a,b. The removed S[a,b] also has 2s-1 internal vertices. If even one of those removed internal vertices were absent from R, the switch would gain strictly more R-vertices than it loses, contradicting maximality of |V(S) intersect V(R)|. Hence every internal vertex of S[a,b] lies on R.

For the final assertion, in branch (C) of c10cb2dd049c the vertex z_R is by definition the R-nearest common vertex to x. Hence R[z_R,x] meets S only at its endpoints and lies on the entrance side, so the preceding argument applies.