# Genuine reachability sets can have robust convex overlap without an antipodal pair

Work in Q_14, with its coordinates divided into seven pairs B_p={2p-1,2p}, p=1,...,7. Let the seven lines on these points be
123, 145, 167, 246, 257, 347, 356.
Every line has three points, every point lies on three lines, and every two lines intersect. These assertions follow directly from the displayed list (equivalently the points are nonzero vectors of F_2^3 and each line is {a,b,a+b}).

For a line L, let D_L be the union of the three pairs B_p for p in L, and let M_L=[14]\D_L. Define the downset
A = union_L 2^(M_L).
Thus a support lies in A exactly when it avoids all six coordinates of at least one doubled line.

THEOREM. There is an antipodally odd binary EDGE coloring of Q_14 whose genuine color-free monochromatic-geodesic reachability set satisfies R(0)=A and R(1)=bar A. These two sets are disjoint, while
[3/7,4/7]^14 is contained in conv R(0) intersect conv R(1).
In particular their convex hulls overlap in a full-dimensional central box, and the center is interior to both convex hulls.

Proof of realizability. Every singleton belongs to A, since each point is omitted by some line. If U in A and V in bar A, choose lines L,K such that U avoids D_L and V contains D_K. A point p in L intersect K supplies two coordinates on which U is zero and V is one. Hence d_H(U,V)>=2. Apply the exact downset-realization theorem, nori_monochromatic_root_downset_realization_20261008. It gives an actual antipodally odd coloring with every initial edge at 0 colored 0 and R(0)=A. Oddness gives R(1)=bar A.

Proof of the convex claim. Each M_L has size eight, and each coordinate belongs to exactly four of the seven M_L. Therefore
(0 + sum_L 1_(M_L))/8 = (1/2,...,1/2).
These eight actual reachable vertices already have center as their equal-weight barycenter. For the stronger box claim, a convex hull of a downset is coordinatewise downward closed inside the nonnegative orthant: decreasing one coordinate of a generating vertex preserves membership, and mixtures of these decreases give arbitrary coordinate decreases of a convex combination. The average of the seven maximal vectors is (4/7,...,4/7), so [0,4/7]^14 lies in conv A. Complementation gives [3/7,1]^14 in conv bar A. Their common box has side length 1/7 and contains an L-infinity neighborhood of radius 1/14 about the center. QED.

A fully specified coloring. For an edge U -> V=U union {i}, use the following first-applicable rule:
(1) if V in A, color 0;
(2) if U in A, color 1;
(3) if bar U in A, color 1;
(4) if bar V in A, color 0;
(5) otherwise color |U| mod 2.
Rules (1)-(4) are the realization construction. Their domain is antipodally invariant. On remaining edges, n=14 implies that antipodal lower ranks |U| and 13-|U| have opposite parity, so rule (5) is odd too.

This explicit coloring DOES have a full monochromatic geodesic elsewhere. Number coordinates 1,...,14, encode a root by sum_i x_i 2^(i-1), and take root 4572 with direction order
(9,14,13,12,8,10,7,11,5,6,4,2,3,1).
Substitution in rules (1)-(5) gives color 0 on every edge. Thus the construction is an obstruction to convex-label extraction at a specified root, and is compatible with the existential edge conjecture.

Independent finite verification enumerated all 114688 undirected edges, checked antipodal oddness, and computed both monochromatic reachability families from 0 by the exact subset recurrence. It found R_0(0)=A with 1534 vertices, maximum rooted geodesic length 8, and R_1(0)={0}; no antipodal pair lies in A. The theorem and the central box follow from the preceding symbolic proofs.

CONSEQUENCE FOR THE BROADCAST. Replacing an actual uncolored R(x) by its ordinary convex hull in R^n loses the exact overlap criterion even for honest reachability sets in a legitimate odd coloring. A convex coincidence can occur with a robust positive margin while literal overlap is absent. The high-dimensional target simplex remains exact, and the simplicial/cubical witness carriers remain candidates. Any lower-dimensional geometric label must prove an extraction property beyond convex balance. The global problem remains to force literal overlap for some root while retaining cross-root compatibility; this result does not close NORI.
