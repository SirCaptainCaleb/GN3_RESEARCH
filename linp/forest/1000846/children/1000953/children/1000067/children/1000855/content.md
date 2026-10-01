# PG(4,2) has a spanning P15

## Statement

The binary projective Steiner triple system PG(4,2) on 31 points contains a spanning linear path with 15 edges. Hence the PG(3,2) non-Hamiltonicity phenomenon does not extend to the next binary projective dimension.

## Body

Represent the points by the nonzero vectors of F_2^5, encoded as integers 1,...,31 with addition given by XOR. The following 16 points are the successive end/joint vertices of a spanning path:
1,2,4,8,16,21,31,11,17,13,22,15,29,14,9,23.
The 15 remaining path vertices are their successive XORs:
3,6,12,24,5,10,20,26,28,27,25,18,19,7,30.
These two lists are disjoint and together are exactly {1,...,31}. For each i, the corresponding path edge is {a_{i-1}, a_{i-1}+a_i, a_i}, a projective line. Because every vertex occurs exactly once in the alternating vertex sequence, these 15 lines form a spanning linear path.