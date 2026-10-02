# Overlap-maximal gap-one pairs have at most one nontrivial switchable cell, regardless of intersection order

## Statement

Let Q be a q-edge path and P a maximum (q+1)-edge path, both ending at v, with P chosen to maximize the number of Q-edges it contains. Consider any simultaneously switchable family of nontrivial two-common-vertex cells, where each cell consists of a Q-subpath and P-subpath joining the same boundary vertices and the replacement interiors are pairwise vertex-disjoint; the two subpaths may traverse the boundary vertices in the same or opposite order. If their lengths are A_i,B_i on Q,P respectively, then A_i<=B_i, sum_i(B_i-A_i)<=1, and no balanced cell A_i=B_i can occur. Hence such a family contains at most one nontrivial switchable cell.

## Body

For one cell, replacing its P-subpath by the Q-subpath, oriented between the same boundary vertices, preserves a path ending at v; maximality of P gives A_i<=B_i. For a simultaneously switchable family, perform all replacements of Q-subpaths by P-subpaths inside Q at once. Pairwise interior disjointness ensures the resulting walk is a linear path ending at v, of length q+sum_i(B_i-A_i), at most phi(v)=q+1. Hence the total positive imbalance is at most one. If some cell were balanced, replacing its P-side by the equal-length Q-side would preserve maximum length and endpoint while increasing Q-edge overlap, contradicting the choice of P. Thus every surviving cell costs one full unit and at most one exists.