# Clean doubly-terminal-single minimum-terminal edges violate spacing in two double cells

## Statement

For every integer R>=39 there is a finite linear 3-graph with four ascending nonspecial edges e_i={x_i,v,u_i}, edge ranks (R+1,R+1,R+7,R+7), and phi(v)=phi(u_i)=R+9. All four chosen source paths are clean and all four edges are terminal-single on the common maximum v-path and on their respective maximum u_i-paths. Their contacts form two doubly occupied cells. Thus conditions 1-4 of the paid target do not imply four-edge spacing. Both cells are unpaid apart from their single triangle contribution, and this is not a counterexample to the full selected paid-switching hypothesis.

## Body

## Construction
Fix an integer R>=39. Let
  g_j={z_{j-1},b_j,z_j}, 1<=j<=R+9,
be a loose path, with all displayed vertices distinct except the intended shared joints. Put p=R+9 and v=b_p. Define
  x_1=b_R, x_2=z_R, x_3=b_{R+6}, x_4=z_{R+6},
  r_1=r_2=R, r_3=r_4=R+6,
  t_1=t_2=9, t_3=t_4=3.
At each x_i attach a fresh loose path B_i of t_i edges, with first vertex x_i and last vertex u_i. All vertices of these branches other than their specified x_i are fresh and pairwise disjoint. Finally add
  e_i={x_i,v,u_i}, i=1,2,3,4.
The resulting hypergraph is linear. In particular e_i meets the first and last edges of B_i at distinct vertices, and t_i>=3; all distinct e_i meet only at v.

## Rooted-path reduction
Delete the first R-1 backbone edges. The remaining hypergraph has
  10+2*9+2*3+4=38
edges. Thus a path avoiding those first R-1 edges has length at most 38<R. The deleted tail attaches to the rest only through g_R. Any path ending at one of the displayed core vertices or e_i and using the tail traverses it monotonically. Extending its initial tail segment back to g_1 introduces no new intersection. Consequently, whenever the maximum in question is at least R, an upper bound may be checked solely on paths starting with the full prefix g_1,...,g_R. Below call these rooted paths.

A branch B_i cannot occur internally in a linear path: to pass from its x_i end to its u_i end and continue, the path would have to use e_i, which meets both end edges of B_i, a nonconsecutive intersection. The reverse traversal is forbidden for the same reason. Thus any branch portion is terminal in a rooted path.

## Complete upper bound on rooted paths
Write s=R+6, so p=s+3. Both low sources x_1,x_2 belong to g_R; both high sources x_3,x_4 belong to g_s.

A rooted path has the following possibilities after g_R.
1. It follows a low branch, and ends there, adding at most 9 edges.
2. It continues forward on the backbone. It may end there, enter a high branch at g_s and add at most 3 branch edges, or use a high e_i immediately after g_s. In the last case it can then follow either its own branch from u_i for at most 2 edges, or go through g_p and backward to g_{s+2}, for at most 2 further host edges. It cannot use another e_j: a low e_j would meet the earlier g_R and a high e_j would meet the earlier g_s. All these paths have length at most R+9.
3. It uses a low e_i immediately after g_R. It cannot then use the other low e_j, since that edge meets the nonconsecutive g_R. It can continue along its own branch backward from u_i for at most 8 edges; this gives length at most R+9. Alternatively it can enter g_p and move backward on the backbone, stopping no later than g_{R+2}; g_{R+1} meets the earlier g_R. This uses at most 8 host edges after e_i. If it instead leaves that backward segment along a high branch, it reaches a high source after at most 4 host edges and has at most 3 branch edges, also below R+9. The last possibility is a high e_j immediately after the low e_i. A third v-edge is impossible. It may now follow a high branch for at most 2 edges, or enter the backbone at the high source. A backward host segment has at most 5 edges, from g_s to g_{R+2}; a forward one stops before g_p. If it changes to the other high branch, it does so at g_s and has at most 3 branch edges. These paths have length at most R+7.

This list is exhaustive: away from the backbone and the e_i, every edge lies in a branch, and every e_i is incident only with v, its own source, and its own branch terminal. Hence all rooted paths, and therefore all paths in H, have length at most p=R+9. The full backbone attains p.

## Exact ranks and unique entrances
Every rooted path has already encountered x_1,x_2 in g_R. It can end at either of them only at g_R itself. Core-only paths have length less than R. Thus
  phi(x_1)=phi(x_2)=R.
A rooted path containing a low e_i must use it immediately after g_R, because e_i meets g_R. Thus every maximum e_i-ending path has length R+1 and enters through x_i. Therefore
  phi(e_1)=phi(e_2)=R+1,
and both are ascending nonspecial.

For the high sources, the normal backbone prefix has length s=R+6. In case 3 above, a route through a low e_i and g_p first reaches b_s after only R+5 edges and z_s after only R+4 edges. A route through a low e_i and a high e_j reaches a high source in e_j after R+2 edges, or the other high source through g_s after R+3 edges. A source cannot be made a last vertex later in such a path, after it has already occurred. These are all alternatives to the ordinary backbone prefix. Hence
  phi(x_3)=phi(x_4)=R+6.
A rooted path ending in a high e_i either follows the ordinary prefix through g_s, giving R+7 edges with entrance x_i, or follows a low e_j directly into e_i, giving only R+2 edges. A route through g_p already contains v and cannot later end in e_i; a route through B_i already contains x_i and cannot later end in e_i. Thus
  phi(e_3)=phi(e_4)=R+7,
and both are ascending nonspecial.

For each i, the backbone prefix through g_{r_i} followed by B_i is a p-edge path with last vertex u_i. Together with the global upper bound this gives
  phi(u_i)=p  for all i.
Also phi(v)=p by the full backbone. In particular each e_i has a strict edge-rank gap at both terminals, and v is a minimum-rank terminal, with equality of the two terminal ranks.

## Chosen clean and single witnesses
Choose the source path at x_i to be the prefix g_1,...,g_{r_i}. It is maximum by the exact ranks above and avoids both v and u_i, so the source is clean.
Choose P_v to be the full backbone. Each e_i has the unique off-v contact x_i.
Choose P_{u_i} to be the backbone prefix through g_{r_i} followed by B_i. It has length p. It avoids v, and the only off-u_i vertex of e_i on its precursor is x_i. Thus every e_i is terminal-single on both chosen terminal paths.
These choices are compatible: all designated source and terminal vertices are distinct, apart from the common v.

The ordered edge ranks are
  (R+1,R+1,R+7,R+7).
Consequently
  2q_2=2R+2 < 2R+9=q_1+q_4+1.
For R=100 these are (101,101,107,107), with both terminal ranks 109.

## Exact payment boundary
The four contacts occupy the two cells C_R={b_R,z_R} and C_s={b_s,z_s}, both doubly. Thus each cell has a genuine triangle formed by its host edge and its two e_i. Nevertheless this is not a counterexample to the full selected paid-switching class.

In fact both rotation output cells are unpaid. Their outputs are g_{R+2} and g_{s+2}. Standard rotations explicitly give p-edge paths ending in each output. Their forward joints have rank p-1:
  phi(z_{R+2})=R+8,
  phi(z_{s+2})=R+8.
For the first joint, the witness is g_1,...,g_R,e_1,g_p,g_{p-1},...,g_{R+3}; the rooted-path classification bounds any other route by this length. For the second, the ordinary prefix through g_{s+2}=g_{R+8} witnesses R+8; the same classification gives the upper bound. Since each output edge has rank p while its forward joint has rank p-1, every longest path into it must enter through that joint (otherwise the joint could be a last vertex of rank p). Thus each output is nonspecial ascending in the unpaid branch.

Each double unpaid cell contributes only one D-unit, not one independent payment for each of its two occupants. Moreover, the four edges have not been shown double on one common shorter anchor path, as required for the switching family. Indeed the last backbone edge itself is ascending of rank p: its only longest rooted path is the full backbone, and its entrance z_{p-1} has rank p-1. Hence this vertex is aligned, not an active misaligned center of e6137a4bc902.

The example refutes the charged four-edge conjecture a4ddc7455f1c and shows that conditions 1-4 of the narrow target, even supplemented by two occupied double cells, do not imply the midpoint inequality. It does not refute the full hypothesis 5. Any proof of that target must use genuine common-anchor switching and/or the exact selected payment allocation; a triangle containing an edge alone is insufficient.
