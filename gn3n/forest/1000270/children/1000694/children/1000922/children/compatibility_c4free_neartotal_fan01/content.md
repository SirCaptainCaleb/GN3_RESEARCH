# Deletion-cover compatibility is C4-free, forcing a near-total anchored crossing fan

## Statement

Let H have path-cover number greater than 2, and let D be m at least 4 deletion labels with chosen two-covers F_d of H-d. If no pair is support-compatible but order-incompatible, then the full-compatibility graph C on D has at most one common neighbor for every pair of vertices. Hence
avgdeg(C) <= (1 + sqrt(4m-3))/2.
Therefore some anchor x has at least ceil((2m-3-sqrt(4m-3))/2) support-incompatible covers. Relative to F_x=P|Q, each such cover has the crossing certificate from 1000922. Also the number of support-incompatible pairs is at least binom(m,2)-m(1+sqrt(4m-3))/4, and there is a pairwise support-incompatible subfamily of size at least ceil(2m/(3+sqrt(4m-3))).

## Body

Let C be the full-compatibility graph.

Suppose first that ab is a nonedge and x,y are distinct common neighbors. Compare the restrictions of F_a and F_b to the common vertex set with a and b removed. Deleting x makes these two ordered two-block states identical, because both are then the corresponding restriction of F_x; deleting y does the same. By pairdeletionreconstruct01, two distinct equalizing deletions force the original states to have the same supports, with at most the pair x,y as an order disagreement. Thus F_a and F_b are support-compatible. The standing hypothesis excludes support-compatible order-incompatible pairs, so F_a and F_b would be fully compatible, contradiction. Thus every nonedge has at most one common neighbor.

Now suppose ab is an edge with distinct common neighbors x,y. If xy were an edge, a,b,x,y would form four mutually compatible deletion covers, forbidden by the four-cover gluing obstruction in 1000694 because pc(H)>2. Hence xy is a nonedge, but then it has the two common neighbors a,b, contradiction. So every pair of vertices of C has at most one common neighbor.

Counting length-two paths gives sum_v binom(d_v,2) <= binom(m,2). If dbar is the average degree, convexity yields dbar(dbar-1) <= m-1, hence dbar <= (1+sqrt(4m-3))/2. This gives the claimed edge bound and therefore the quadratic lower bound on incompatible pairs. Some vertex x has compatibility degree at most dbar, so its number of nonneighbors is at least ceil((2m-3-sqrt(4m-3))/2). Under the standing hypothesis every nonneighbor is support-incompatible, and 1000922 supplies the stated crossing witness for each.

Finally, the standard greedy bound alpha(C) >= m/(dbar+1) gives alpha(C) >= 2m/(3+sqrt(4m-3)), yielding the pairwise support-incompatible subfamily.

Thus the former m/3 anchored fan sharpens to m-O(sqrt(m)), with a simultaneous quadratic supply of incompatible pairs.