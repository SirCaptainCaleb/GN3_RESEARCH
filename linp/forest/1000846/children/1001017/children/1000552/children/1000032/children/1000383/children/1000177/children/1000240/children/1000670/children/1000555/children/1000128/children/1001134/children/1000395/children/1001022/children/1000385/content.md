# Unlabeled lens-free overlap of maximum paths can be complete

## Statement

For every q>=5 with q not congruent to 1 modulo 3, there is a finite linear 3-uniform hypergraph on 2q+1 vertices containing two edge-disjoint q-edge maximum endpoint paths Q,R with
  V(Q)=V(R),
and with no genuine clean internal lens between Q and R. In particular Q is overlap-maximal relative to R, yet the pair has no shared edge and cannot be simplified by a clean internal lens.

Thus macroscopic overlap plus overlap-maximal lens-free normalization alone cannot force a shared-edge core or a longer-path contradiction. Any post-43/48 braid classification must use the distinguished ascending-edge labels or additional ambient structure.

## Body

Put N=2q+1 and take vertex set Z_N. Since q is not congruent to 1 modulo 3, gcd(3,N)=1. Define
  Q_i={2i,2i+1,2i+2},  0<=i<q,
where the displayed representatives lie in {0,...,N-1}. These edges form a q-edge linear path Q using all N vertices.

Let r_j=3j mod N for 0<=j<N, and define
  R_i={r_{2i},r_{2i+1},r_{2i+2}},  0<=i<q.
Because multiplication by 3 permutes Z_N, the r_j are all distinct, so the R_i form another q-edge linear path R using all N vertices.

The union H=Q union R is linear. Indeed, within each family this is immediate from the path ordering. If a Q-edge and an R-edge shared two vertices, the difference of those two residues would belong both to
  {+/-1,+/-2}
and to
  {+/-3,+/-6}
modulo N.
For N=2q+1>=11 these two sets are disjoint, a contradiction. Hence every cross-pair of edges meets in at most one vertex. In particular Q and R share no hyperedge.

Every linear 3-uniform path with k edges uses exactly 2k+1 distinct vertices. Since H has only 2q+1 vertices, no path in H has more than q edges. Therefore Q and R are maximum endpoint paths. Orient Q to end at 2q and R to end at r_{2q}=N-3; these last vertices are distinct. Because V(Q)=V(R)=Z_N, Q already has the largest possible vertex overlap with R.

Finally there is no genuine clean internal lens between Q and R. Any nontrivial subpath side between two boundary vertices contains a further vertex, and every vertex of either path belongs to the other full path. Hence the required interior-disjointness of a clean lens fails.

This gives the claimed complete-overlap, edge-disjoint, lens-free pair of maximum paths.