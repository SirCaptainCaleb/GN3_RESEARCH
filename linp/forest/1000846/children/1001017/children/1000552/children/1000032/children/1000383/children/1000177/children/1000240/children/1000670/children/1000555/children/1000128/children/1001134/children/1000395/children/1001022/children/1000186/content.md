# Overlap-maximal maximum path pairs admit no clean complementary switch

## Statement

Let R be a maximum endpoint path ending at y, and among all maximum endpoint paths ending at x choose Q to maximize |V(Q) intersect V(R)|. Let A be a nonempty union of pairwise internally vertex-disjoint internal subpaths of Q, and B a nonempty union of pairwise internally vertex-disjoint internal subpaths of R, with the same boundary attachment vertices.

Assume:
(i) replacing A by B in Q produces a linear path Q* ending at x;
(ii) replacing B by A in R produces a linear path R* ending at y;
(iii) every interior vertex of A is outside R, and every interior vertex of B is outside Q.

Then no such complementary switch exists.

## Body

Put a=|E(A)| and b=|E(B)|, summing over components. Since Q* is a path ending at x,
  |Q*|=|Q|-a+b.
Maximality of Q gives b<=a.

Similarly,
  |R*|=|R|-b+a,
and maximality of R gives a<=b. Hence a=b, so Q* is again a maximum endpoint path ending at x.

By (iii), replacing A by B deletes no vertex of V(Q) intersect V(R) except boundary attachment vertices, all of which remain. On the other hand every interior vertex of B lies on R and was absent from Q. Since B is nonempty and internal, at least one such new R-vertex is inserted. Therefore
  |V(Q*) intersect V(R)|>|V(Q) intersect V(R)|,
contradicting the overlap-maximal choice of Q.

Thus an overlap-maximal pair of maximum endpoint paths has no clean complementary switch.
