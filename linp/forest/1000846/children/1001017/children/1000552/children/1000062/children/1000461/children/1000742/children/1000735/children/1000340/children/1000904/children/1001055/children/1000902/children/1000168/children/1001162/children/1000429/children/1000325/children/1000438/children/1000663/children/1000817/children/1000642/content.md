# Paid top-output cells give distinct top-potential lens attachments on one host path

## Statement

In the global-top setup of b7a21d8e4f90, let P_v=(g_1,...,g_L) be the chosen maximum host path and let Y be the paid occupied interior cells. For every paid cell with output edge g_j={z_{j-1},b_j,z_j}, the private host vertex b_j satisfies phi(b_j)=L. Choosing any maximum L-edge endpoint path P_{b_j}, the pair P_v,P_{b_j} contains a clean balanced elementary endpoint lens attached at b_j. Distinct paid cells give distinct attachment vertices b_j. Thus the Y paid cells yield Y distinct top-potential balanced-lens states on the single host path P_v.

## Body

By b7a21d8e4f90 every paid cell has an all-top rank-L output edge g_j. Its three vertices on the host path are the backward joint z_{j-1}, the private vertex b_j of g_j, and the forward joint z_j, so in particular phi(b_j)=L. Since b_j lies on the maximum L-edge host path P_v and b_j is not the last vertex v, apply b35b0fd4e4cd with Q=P_v and y=b_j. For any maximum endpoint path P_{b_j}, this gives a second common vertex and a clean elementary lens adjacent to b_j whose two sides have equal edge length. If two paid cells have different output indices j, their private vertices b_j are distinct path-private vertices, so the resulting lens states have distinct attachment endpoints on P_v. Therefore all Y paid outputs are simultaneously realized as balanced endpoint lenses attached at distinct top-potential vertices of the same maximum host path.
