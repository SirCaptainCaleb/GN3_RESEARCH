# Local structure and escape in the boundary fixed-target rotation graph

## Statement

In the setting of 68593c300c9c, let G(f,x) be the undirected graph whose vertices are the (q-1)-edge paths ending at x with last edge f, with two states adjacent when one is obtained from the other by an endpoint-preserving single-blocker rotation.

(1) Every rotation has a canonical inverse. Every state has degree at least two, and after traversing any rotation edge there is a noninverse rotation available from the other free opposite endpoint.

(2) Every triangle in G(f,x) has one common exchanged path edge, necessarily g_2. Writing g_1={a,b,c} with c=g_1∩g_2, d=g_2∩g_3, and p for the private vertex of g_3, its two alternative states have the form (g_1,h_a,g_3,...,g_t) and (g_1,h_b,g_3,...,g_t), where h_a contains a and one of {d,p}, h_b contains b and one of {d,p}, and each new edge has its third vertex outside the original path. Conversely such a linear configuration gives the corresponding rotation triangle. No such triangle is a connected component: it has a noninverse exit outside the triangle, with the analogous exit forced on each endpoint side.

(3) Every chordless 4-cycle is supported in the first four path positions. From any base state P_0=(g_1,...,g_t), if its two incident square rotations delete g_i and g_j with i<j, then (i,j) is one of (1,2),(1,3),(2,3),(2,4); hence all four states share the tail g_5,...,g_t when t>=5. No such square is a connected component: at least one state has a non-x single-blocker rotation outside the square, and in pivot types (2,3) and (2,4) the blocker-universe argument forces the corresponding exit on each endpoint side.

## Body

Fix P=(g_1,...,g_t) in the boundary fixed-target state space of 68593c300c9c, with fixed last vertex x and last edge f.

Canonical inverse and genuine branching.  Let a be a free opposite vertex of g_1 and let h be a non-x single blocker through a. The explicit rotation formula of 912c72c000da has three cases. If the blocker lies only in g_2, the rotated path is (h,g_2,...,g_t) and the omitted edge is g_1. If it lies only in g_j with j>=3, the rotated path is (g_{j-2},...,g_1,h,g_j,...,g_t) and the omitted edge is g_{j-1}. If it is the joint g_j∩g_{j+1}, the rotated path is (g_{j-1},...,g_1,h,g_{j+1},...,g_t) and the omitted edge is g_j. In each case the omitted edge r meets a free opposite vertex of the new first edge and is itself single-blocking there; applying the same rotation rule with r restores P. Thus every rotation edge has a canonical inverse.

At either free opposite vertex a of g_1 there is no clean incident edge, since prepending one would produce a q-edge path ending at x, contradicting phi(x)=q-1. If S,D are the numbers of single- and double-blocking incident edges other than g_1, then minimum degree and linearity give
S+D >= q-1,   S+2D <= 2q-4.
Hence S>=2. At most one single blocker can use x, so each of the two free opposite endpoints supports a non-x single-blocker rotation. The two resulting neighbors are distinct: the corresponding new edges use different free vertices of g_1, and one edge cannot contain both without meeting g_1 twice. Therefore every state has degree at least two. Moreover, after traversing one rotation, its canonical inverse uses the omitted edge at one specific free endpoint of the new first edge; the same S>=2 argument at the other free endpoint supplies a different non-x single blocker, giving a noninverse next move.

Triangles.  Every rotation changes the edge set by deleting one path edge and adding one external edge. Three equal-size edge sets that are pairwise one-edge exchanges form a Johnson triangle. The common-union form would require one external rotation edge to delete two different path edges from P, impossible because the blocker position in P uniquely determines the omitted edge in the explicit rotation formula. Hence the three states share a common size-(t-1) core: the two alternatives from P delete one common g_k and add distinct edges h_1,h_2.

If k>=3, after the h_1-rotation the first edge is g_{k-1}. For h_2 also to rotate that state, one of its path vertices must be a free opposite vertex of g_{k-1}; but h_2 already contains its original free endpoint in g_1 and its unique blocker in the retained suffix. This would give h_2 two blocker-side vertices of the original path, contradicting that it was single-blocking relative to P. Thus k<=2.

The case k=1 is impossible. Deleting g_1 forces a blocker at the private vertex p_2 of g_2. If h_1 is one such alternative, then in the h_1-state that p_2 becomes the joint h_1∩g_2 and the old joint c=g_1∩g_2 becomes private in g_2. A second alternative h_2 capable of deleting h_1 from that state would have to use c as blocker, while as a direct g_1-deleting alternative from P it also contains a free endpoint of g_1 and p_2. It would therefore meet g_1 twice, contradicting linearity.

Hence k=2. Write g_1={a,b,c}, with a,b free and c=g_1∩g_2; put d=g_2∩g_3 and let p be the private vertex of g_3. Every g_2-deleting rotation edge contains one of a,b and one of {d,p}, with third vertex outside V(P). Thus the two alternatives are precisely
P_a=(g_1,h_a,g_3,...,g_t),   P_b=(g_1,h_b,g_3,...,g_t),
with h_a through a and h_b through b as stated. Conversely, in such a linear configuration each alternative rotates to the other as well as to P, giving the triangle.

A triangle cannot trap the rotation graph. Consider endpoint a in P and P_b. The blocker universe changes by replacing the private vertex r of g_2 with the external third vertex of h_b. Suppose neither state has an outside non-x rotation at a. Then in P the only single blockers at a are h_a and the unique possible x-single. The two inequalities above are therefore tight: every remaining blocker vertex belongs to a unique double blocker. In particular r belongs to a double blocker k through a, whose other blocker v is not x. After the h_b-rotation, r leaves the path while v remains, so k becomes a non-x single blocker at a in P_b, distinct from h_a, producing an outside neighbor. The argument at b is symmetric.

Chordless squares.  A chordless Johnson-graph 4-cycle has two distinct path pivots g_i,g_j and two distinct external additions h,k:
E(P_1)=E(P_0)-{g_i}+{h},  E(P_3)=E(P_0)-{g_j}+{k},
E(P_2)=E(P_0)-{g_i,g_j}+{h,k}.
If i,j>=3, take the h-rotation first. The first edge becomes g_{i-1}. For k, which was single-blocking relative to P_0, to remain a rotation edge, its unique blocker-side vertex must become a free opposite vertex of g_{i-1}. Translating through the explicit rotation formula forces j in {i-2,i-1}. Reversing the roles forces i in {j-2,j-1}, impossible. Hence min{i,j}<=2.

Assume i<j. If i=1, h contains a free endpoint of g_1 and the private vertex of g_2. After deleting g_j first, h can still meet a free opposite vertex of the new first edge only when j<=3. If i=2, h contains a free endpoint of g_1 and a blocker in g_3; the same argument gives j<=4. Therefore the only pivot pairs are (1,2),(1,3),(2,3),(2,4), and all four states agree outside those pivot edges, giving the common tail g_5,...,g_t.

Finally every chordless square has an outside exit. For pivot types (1,2) and (1,3), both square rotations out of the base state use the same free endpoint a of g_1, so the other free endpoint b supports, by the degree-count argument, a non-x single blocker distinct from both square edges; this immediately exits the square. For pivot types (2,3) and (2,4), write h for the g_2-rotation through endpoint a and k for the other rotation through b. Comparing P_0 with the k-rotated state P_3 changes the blocker universe at a by removing the private vertex r of g_j and inserting the external third vertex of k. If neither state had an outside non-x rotation at a, the single blockers in P_0 would again be exactly h and the unique possible x-single, forcing saturation of blocker capacity. The removed private vertex r then lies in a double blocker d through a whose other blocker v is not x. After the k-rotation, r disappears while v remains, so d becomes an outside non-x single blocker at a in P_3. The symmetric argument applies at b. This proves the claimed square exits and completes the compression of the local-cycle analysis.
