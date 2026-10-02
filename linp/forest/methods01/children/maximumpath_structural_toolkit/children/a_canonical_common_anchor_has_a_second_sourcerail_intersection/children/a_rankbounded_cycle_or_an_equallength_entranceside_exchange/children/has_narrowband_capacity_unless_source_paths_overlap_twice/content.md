# A common exchange return vertex has narrow-band capacity unless source paths overlap twice

## Statement

Let R be a linear path and let z be a fixed vertex of R. For i=1,...,m let
  e_i={x_i,v,u_i}
be distinct ascending nonspecial edges terminal at v, with edge ranks r_i, and let S_i be maximum endpoint paths with last vertices x_i, so phi(x_i)=r_i-1.

Assume:
(1) z and x_i are common vertices of R and S_i;
(2) the R-segment R[z,x_i] and the S_i-segment S_i[z,x_i] are internally vertex-disjoint and have the same number of edges;
(3) the x_i are distinct.

If all edge ranks r_i lie in an integer interval [Q-D,Q], then either
  m<=D+1,
or there exist i!=j such that
  |V(S_i) intersect V(S_j)|>=2.

Equivalently, D+2 equal-length path exchanges sharing one return vertex z in an edge-rank band of width D force a pair of the corresponding maximum source paths to have at least two common vertices.

## Body

Assume that every pair S_i,S_j has exactly one common vertex. Since z belongs to every S_i, this unique common vertex must be z.

Apply the certified unique-intersection theorem 5854d853a44b to each pair S_i,S_j. It follows that z is an internal joint at the same path-edge index on S_i and S_j. Hence there is one integer t such that, on every S_i, z is the joint after t path edges when S_i is oriented toward its last vertex x_i.

The total length of S_i is
  phi(x_i)=r_i-1.
Therefore the S_i-segment from z to x_i has
  (r_i-1)-t
edges. By the equal-length exchange hypothesis,
  |R[z,x_i]|=(r_i-1)-t.                              (1)

Orient R from the fixed vertex z toward the side containing the x_i under consideration. Equation (1) shows that the distance of x_i from z on R is determined by r_i:
  dist_R(z,x_i)=r_i-1-t.
Distinct x_i have distinct distances from z. Since r_i belongs to [Q-D,Q], there are only D+1 possible values of the right-hand side. Hence
  m<=D+1.

Contrapositively, if m>=D+2, some pair S_i,S_j does not have unique intersection. Canonical maximum source paths of distinct common-terminal ascending nonspecial edges are pairwise intersecting by 0c885137ea8c, so such a pair has at least two common vertices.

If the x_i occur on both sides of z in R, apply the argument separately to the two sides; this gives the immediate two-sided variant m<=2(D+1) under pairwise unique intersections.