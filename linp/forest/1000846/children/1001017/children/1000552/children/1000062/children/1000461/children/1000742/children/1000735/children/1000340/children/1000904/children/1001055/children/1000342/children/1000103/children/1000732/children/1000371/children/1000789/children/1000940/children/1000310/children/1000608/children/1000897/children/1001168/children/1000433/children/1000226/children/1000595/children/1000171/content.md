# The sharp 2q-1 cut barrier; the 2q-2 boundary gives overlap except for the rank-4 triangle

## Statement


Let
v_0v_1...v_k
be a rainbow terminal-pair path whose parent hyperedges
E_s={x_s,v_{s-1},v_s}
belong to U_11 and have nondecreasing edge ranks
r_1<=...<=r_k.

Fix a cut between E_t and E_{t+1}, and put
  q=r_t,  s=r_{t+1}.

For every interior color-terminal collision x_i=v_j crossing this cut, so j<t<i, one has
  s<=2q-2.

Consequently:

(1) If s>=2q-1, no color-terminal collision crosses the cut.

(2) If s=2q-2, every crossing collision has
  r_i=2q-2,
  r_j=r_{j+1}=q.
If q=3, then r_i=4 and the collision closes a local linear 3-cycle.
If q>=4, the collision is in the even central case with m=q-1>=3; the exact contact of E_j with the chosen maximum source path R_i is its unique entrance x_j, and therefore
  |V(R_i) intersect V(R_j)|>=2.

(3) If q>=4 and M collisions cross a cut with s=2q-2, then at least ceil(M/2) can be chosen so that their source-path pairs (R_i,R_j) are index-disjoint and every selected pair has at least two common vertices. At q=3, every crossing collision is instead one of the rank-4 local-triangle cases from (2).


## Body


Let x_i=v_j cross the cut. Since j<t<i and the edge ranks are nondecreasing,
  r_j<=q,
  r_{j+1}<=q,
and
  r_i>=s.
The universal collision bound 867efd696575 gives
  r_j+r_{j+1}>=r_i+2.
Hence
  s+2<=r_i+2<=r_j+r_{j+1}<=2q,
so
  s<=2q-2.
This proves (1).

Assume now s=2q-2. Equality holds throughout the preceding chain, so
  r_i=2q-2
and
  r_j=r_{j+1}=q.
Thus the collision is tight and even, with r_i=2m for m=q-1.

If q=3, then m=2 and r_i=4. This is exactly the low-rank even case of 9b023ed3d700, which gives a local linear 3-cycle. No source-path overlap assertion is needed in this exceptional case.

Suppose q>=4. Then m=q-1>=3, so f0f28f03b0d9 applies. Its two exact contacts are the private vertex and forward joint of the middle host edge, and both are the unique entrances of their parent edges. In particular the exact contact belonging to E_j is x_j, hence x_j belongs to V(R_i).

The chosen maximum source path R_j has last vertex x_j. If R_i and R_j had no other common vertex, then 5854d853a44b would force their sole common vertex x_j to be an internal aligned joint of R_j, contradicting that x_j is the last vertex of R_j. Therefore
  |V(R_i) intersect V(R_j)|>=2.
This proves (2).

For (3), assume q>=4 and direct each crossing collision from its owner index i to its hit index j. Each index has outdegree at most one because x_i is a fixed entrance vertex, and indegree at most one because the entrance labels on a rainbow terminal-pair path are pairwise distinct. Every arc points backward, so the directed graph is a disjoint union of directed paths. A matching in those paths contains at least ceil(M/2) arcs. By (2), every selected arc gives an index-disjoint pair (R_i,R_j) with at least two common vertices. For q=3, (2) already gives the stated local-triangle alternative for every crossing collision.
