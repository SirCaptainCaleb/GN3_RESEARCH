# Loss-one sinks have saturated index graphs forcing a nonlocal blocker or lossless rotation

## Statement

In the boundary setting q=delta, suppose a loss-one x-ending path P' of length q-2 avoiding y,z has opposite endpoint a' with neither a safe clean extension nor a safe single-blocker rotation.

Then d_H(a')=q and the endpoint fan is exactly saturated. In Type A with no singleton blocker, the double blockers use every blocker vertex; in Type A with one singleton, that singleton is x-type and exactly one blocker vertex is uncovered; in Type B, the two singleton blockers and the double blockers partition all blocker vertices.

Partition V(P')p_1 into the standard two-vertex cells A_i and form the double-blocker index graph J on the cells. Then Delta(J)<=2. In Type A with no singleton, J is a union of cycles; in the other two cases J is a union of cycles plus one path component, with endpoint defects exactly the singleton/uncovered blocker incidences.

If no double blocker gives a length-preserving splice, then J must contain a nonlocal edge joining A_i,A_j with |i-j|>=2. Equivalently, every loss-one sink exposes either a lossless double-blocker rotation or a nonlocal double blocker.

## Body

Let C,S,D be the clean, single-blocking, and double-blocking counts at a' relative to P'. The endpoint-deficiency inequality gives 2C+S>=4, while disjoint blocker vertices give S+2D<=2q-6 and C+S+D=d_H(a')-1>=q-1. Combining these with the exact Type A/Type B alternatives of 87a6758ddc73 forces equality throughout.

For Type A with S=0, one gets D=q-3 and d_H(a')=q, with all 2q-6 blocker vertices used by double blockers. For Type A with S=1, necessarily the singleton is x-type, D=q-4, and exactly one blocker vertex is uncovered. For Type B, C=1,S=2,D=q-4,d_H(a')=q, and all blocker vertices are partitioned between the two singletons and the double blockers.

Now let A_i be the two-vertex cells obtained by deleting earlier path vertices from p_i. A double blocker cannot use both vertices from one cell, by linearity with p_i, so it determines an edge of a loopless multigraph J on the cell indices. Since each cell has only two vertices and blocker sets through a' are pairwise disjoint, Delta(J)<=2.

Exact saturation determines the degree deficits of J. In Type A with S=0, every cell contributes degree two, so J is 2-regular and hence a disjoint union of cycles. In Type A with S=1, the total degree deficit is two, at the x-type singleton and the unique uncovered blocker vertex, so J is cycles plus exactly one path component. The Type B case is analogous, with the two singleton blockers giving the two path-end defects.

Finally assume no double blocker yields a length-preserving splice. If every edge of J joined consecutive cells, the certified adjacent-blocker analysis forces each consecutive blocker to use the private vertex of the earlier cell and the forward joint of the later cell. Hence J is a simple subgraph of the ordinary chain on the cell indices.

The Type A, S=0 case is then impossible because such a graph has no cycle. In Type A with S=1 or Type B, J has |V(J)|-1 edges and consists of cycles plus one path; as a forest subgraph of the cell chain it must therefore equal the full chain. Its only endpoint defects are c_2 and b_{q-2}. But one endpoint defect must be the x-type singleton, while x=c_{q-2} is used by the final chain adjacency rather than being a defect. Contradiction. Thus some double blocker is nonlocal unless a length-preserving double-blocker splice already exists.
