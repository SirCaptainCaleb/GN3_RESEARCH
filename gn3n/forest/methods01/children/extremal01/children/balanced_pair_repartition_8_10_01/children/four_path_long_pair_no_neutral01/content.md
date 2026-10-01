# A four-path beside any path of order at least six has no neutral quadratic residue

## Statement

Let H be a boundary tournament, let X be a tight path on four vertices, and let P be a vertex-disjoint tight path of order m>=6. Regard X|P as a two-path cover of its union. Then either V(X) union V(P) has a two-path cover with strictly smaller quadratic contribution than 4^2+m^2, or H contains the localized relative-order disagreement supplied by four_path_long_pair_escape01. In particular the former neutral 4|6 to 6|4 migration is not a genuine equality case: when m=6, X union P has a Hamiltonian 5|5 partition and the quadratic contribution drops from 52 to 50.

## Body

If m=6, apply balanced_pair_repartition_8_10_01 to the pair X|P. Their union has order ten and the displayed orders are 4 and 6, so a legal pairwise repartition into two Hamiltonian five-sets exists and strictly lowers the quadratic contribution by two. If m>=7, apply four_path_long_pair_escape01. Its alternatives are strict quadratic descent, localized relative-order disagreement, or the unique neutral migration; by that theorem the neutral migration can occur only at m=6, which is excluded in this case. Thus only strict descent or localized order disagreement remain for every m>=6.
