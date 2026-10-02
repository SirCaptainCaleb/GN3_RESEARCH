# Human symmetry proof for the punctured cyclic STS(13) all-special calibration

## Statement

Deleting one point from the cyclic STS(13) gives a 12-vertex linear 3-graph in which every remaining edge has edge rank 5 and is special.

## Body


Write A_i={i,i+1,i+4} and B_i={i,i+2,i+7} in Z_13. Delete 0 and its six incident blocks. The map μ(x)=3x is an automorphism fixing 0, with μ(A_i)=A_{3i-1} and μ(B_i)=B_{3i+6}. The surviving blocks form the μ-orbits
(A1,A2,A5), (A3,A8,A10), (A4,A11,A6), (A7),
(B1,B9,B7), (B8,B4,B5), (B12,B3,B2), (B10).

Since H has 12 vertices, no linear path has 6 edges, so every edge rank is at most 5. The following are 5-edge linear paths; the final parenthesized number is the entrance into the last edge.

A1:
A8,A7,A6,A2,A1 (2);
B10,B4,A7,B7,A1 (1).

A8:
A1,A2,A6,A7,A8 (8);
B4,A2,B3,B5,A8 (12).

A4:
A11,A10,A6,A5,A4 (5);
B9,B7,A6,B8,A4 (8).

B1:
A6,B5,A11,B9,B1 (3);
A6,B4,A11,A1,B1 (1).

B8:
A3,B4,A5,A1,B8 (2);
B7,A5,B4,B10,B8 (10).

B12:
A7,B8,B3,A5,B12 (6);
A3,A7,B8,A1,B12 (1).

For A7, B12,A5,B3,B8,A7 ends through 8. Since μ fixes A7 and cycles 7,8,11, its images give distinct longest entrances. For B10, A2,B1,A7,B5,B10 ends through 12; μ fixes B10 and cycles 12,10,4.

Direct inspection shows consecutive blocks meet once and nonconsecutive blocks are disjoint. Thus each representative has rank 5 and at least two maximum-path entrance vertices, hence is special. μ carries the conclusion to every surviving block.
