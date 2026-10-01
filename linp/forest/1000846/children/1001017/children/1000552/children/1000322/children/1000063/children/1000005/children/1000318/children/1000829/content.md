# Human counterexample at the 2/3 equality threshold

## Statement

There is an 11-vertex linear 3-graph H with minimum degree 4 and no P_6^(3) containing a globally maximum-rank nonspecial edge e of rank 5 whose three vertices all have degree 5. Thus the maximum-rank local degree conjecture is false, and equality delta=2ell/3 cannot suffice in the dense-core all-special conjecture at ell=6.

## Body

Let H have the 17 edges
147, 378, 279, 245, 156, 6710, 3410, 018, 057, 026, 369, 1910, 589, 468, 2810, 123, 049,
where, for example, 3410 denotes {3,4,10}. Every pair of vertices occurs in at most one displayed triple, so H is linear. Direct degree counting gives degree sequence
(4,5,5,4,5,4,5,5,5,5,4),
hence delta(H)=4 and d(2)=d(7)=d(9)=5.

Let e=279. Since H has only 11 vertices while a 6-edge linear 3-uniform path uses 13 vertices, H is automatically P_6-free, so every edge has rank at most 5. The sequence
3410, 468, 156, 057, 279
is a linear 5-edge path, with consecutive joints 4,6,5,7 and all nonconsecutive pairs disjoint. Hence phi(e)=5, and this path enters e through 7.

It remains to show that no longest path ending in e can enter through 2 or 9.

Suppose a 5-edge path ends in e through 2. Its first three edges must avoid all of {2,7,9}, and its fourth edge is an edge through 2 avoiding {7,9}. The only edges avoiding {2,7,9} are
A=156, B=3410, C=018, D=468.
Their intersection graph has edges AC, AD, BD, CD. Consequently its only induced 3-vertex paths, up to reversal, are
B-D-A and B-D-C.
The possible fourth edges through 2 and avoiding {7,9} are
245, 026, 2810, 123.
None can append to B-D-A without a chord: respectively 245 also meets B and D at 4; 026 also meets D at 6; 2810 misses A; and 123 also meets B at 3.
None can append to B-D-C either: 245 misses C; 026 also meets D at 6; 2810 also meets B at 10 and D at 8; and 123 also meets B at 3.
Thus entrance 2 is impossible.

Now suppose a 5-edge path ends in e through 9. Again its first three edges must be among the same four edges A,B,C,D, hence are B-D-A or B-D-C up to reversal. The possible fourth edges through 9 and avoiding {2,7} are
369, 1910, 589, 049.
For B-D-A, these respectively also meet B/D, also meet B, also meet D, or miss A, so none appends chordlessly.
For B-D-C, they respectively miss C, also meet B, also meet D, or also meet B. Thus entrance 9 is impossible.

Therefore every longest path ending in e enters through 7. Hence e is nonspecial with phi(e)=5. Since all three vertices of e have degree 5,
min_{v in e} d(v)=5 > 4=floor(2(5+1)/3).
Also delta(H)=4=2*6/3, so this same explicit human example shows that the dense-core all-special threshold cannot be weakened from delta>2ell/3 to delta>=2ell/3 at ell=6.