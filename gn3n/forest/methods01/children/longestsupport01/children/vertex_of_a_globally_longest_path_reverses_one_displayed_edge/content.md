# Every exterior vertex of a globally longest path reverses one displayed edge

## Statement

Let H be a boundary tournament and let A=(a_0,...,a_{lambda-1}), lambda>=2, be a globally longest tight path. Then for every vertex x outside V(A), there is an index i with 0<=i<=lambda-2 such that a tight triple contains the displayed edge a_i a_{i+1} in the reverse order.

Equivalently, every exterior label of a globally longest path is individually a displayed-edge reversal witness.

## Body

Fix x outside V(A). If x could be inserted into any position of the displayed order of A, the resulting sequence would be a tight path of order lambda+1, contradicting global maximality of A. Hence x is noninsertable into every displayed position of A.

Apply acdec36ae3ca. It gives a tight triple reversing one displayed edge of A.

Since x was arbitrary, the conclusion holds for every exterior vertex.