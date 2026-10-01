# PG(4,2) has a spanning 15-edge linear path

## Statement

The binary projective Steiner triple system PG(4,2) on the nonzero vectors of F_2^5 contains a spanning linear path with 15 edges. Hence the PG(3,2) non-Hamiltonicity phenomenon does not extend automatically to the next binary projective dimension.

## Body

Identify the 31 points with the nonzero integers 1,...,31 under 5-bit XOR; the blocks are triples {a,b,c} with a xor b xor c=0. The following 15 blocks form a linear path:
{4,26,30}, {4,25,29}, {10,23,29}, {15,23,24}, {13,21,24}, {5,8,13}, {5,17,20}, {7,17,22}, {1,6,7}, {1,2,3}, {2,9,11}, {9,18,27}, {14,18,28}, {12,16,28}, {12,19,31}.
Each listed triple is a PG(4,2) line because its XOR is zero. Consecutive triples intersect in exactly one point; nonconsecutive triples are disjoint. Their union is all 31 nonzero vectors. Thus they form a spanning P_15^(3).
