# Three pairwise uniquely intersecting equal-length maximum paths have one common joint

## Statement

Let A,B,C be maximum endpoint paths of the same length L. Suppose every pair has exactly one common vertex. Then the three pairwise intersections are the same vertex y. Moreover y is an internal joint at the same edge index on all three paths.

## Body

Write y_AB, y_AC, y_BC for the unique pairwise intersections. By the aligned-joint theorem for unique intersections of maximum endpoint paths, each y_UV is a joint at the same index on U and V.

Assume the three vertices are not all equal. If two were equal, that vertex would belong to the third pair as well, and uniqueness would force the third intersection to be equal too. Hence y_AB,y_AC,y_BC are three distinct vertices. Their aligned indices a,b,c are therefore pairwise distinct: for example, if a=b, then on A the distinct vertices y_AB and y_AC would both be the intersection of the same two consecutive edges, impossible in a linear hypergraph.

Relabel A,B,C so that a<b<c and so that A contains y_AB at level a and y_AC at level b, B contains y_AB at level a and y_BC at level c, and C contains y_AC at level b and y_BC at level c. The A-segment from y_AB to y_AC has b-a edges. The route from y_AB along B from level a to level c and then backwards along C from level c to level b has (c-a)+(c-b) edges, strictly more than b-a. Since the three pairwise intersections are exactly the displayed vertices, the interior of this replacement route is disjoint from the remainder of A and its two constituent segments meet only at y_BC. Replacing the A-segment by this route therefore gives a linear path with the same last vertex as A and more than L edges, contradicting maximality of A.

Thus all three pairwise intersections coincide at one vertex y. The aligned-joint theorem then places y at the same internal index on all three paths.