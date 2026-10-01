# Every order-five transversal design has a spanning seven-edge linear path

## Statement

Every transversal design TD(3,5), equivalently every Latin square of order 5, contains a spanning linear path P_7^(3).

## Body

Represent a cell (r,c) carrying symbol s by the hyperedge (r,c,s). Row, column, and symbol relabeling, together with row-column transposition, preserve the associated transversal design and its linear paths.

We classify order-five Latin squares by whether they contain an intercalate.

INTERCALATE CASE.
Normalize an intercalate to rows 0,1, columns 0,1, symbols 0,1, and reduce the first row and first column. Thus
row 0 = 0 1 2 3 4,
and after conjugating the labels 2,3,4 we may take
row 1 = 1 0 3 4 2.
Indeed the last three entries of row 1 form a derangement of {2,3,4}, hence a 3-cycle.

Now inspect the entry in row 2, column 1. It is either 3 or 4 after the same normalization.

If L(2,1)=3, Latin constraints force L(2,2)=4 and leave L(2,3),L(2,4)={0,1}. The two possibilities complete uniquely to
A =
0 1 2 3 4
1 0 3 4 2
2 3 4 1 0
3 4 0 2 1
4 2 1 0 3

or
B =
0 1 2 3 4
1 0 3 4 2
2 3 4 0 1
3 4 1 2 0
4 2 0 1 3.
Here B=A^T.

If L(2,1)=4, Latin constraints force L(2,4)=3 and leave L(2,2),L(2,3)={0,1}. The two possibilities complete uniquely to
C =
0 1 2 3 4
1 0 3 4 2
2 4 0 1 3
3 2 4 0 1
4 3 1 2 0

or
D =
0 1 2 3 4
1 0 3 4 2
2 4 1 0 3
3 2 4 1 0
4 3 0 2 1.

In A the seven cells
(0,1,1),
(4,2,1),
(1,2,3),
(1,3,4),
(3,3,2),
(2,0,2),
(2,4,0)
form a linear path. Consecutive intersections use, in order, symbol 1, column 2, row 1, column 3, symbol 2, row 2; every nonconsecutive pair has distinct row, column, and symbol coordinates. Transposition gives a P_7 in B.

In both C and D the seven cells
(0,0,0),
(1,0,1),
(1,2,3),
(2,4,3),
(2,1,4),
(3,1,2),
(4,3,2)
form a linear path. The consecutive joints are column 0, row 1, symbol 3, row 2, column 1, symbol 2, and every nonconsecutive pair is disjoint.

INTERCALATE-FREE CASE.
Reduce the first row and first column to 0,1,2,3,4. Relative to the first row, every other row is a derangement of the five symbols. A derangement of cycle type 2+3 would give an intercalate with the first row, so row 1 must be a 5-cycle. Conjugating symbols 1,2,3,4 while preserving the reduction gives
row 1 = 1 2 3 4 0.

Let x=L(2,1). Column 1 already contains 1,2, so x is one of 0,3,4.

If x=3, the Latin constraints successively force
row 2 = 2 3 4 0 1,
row 3 = 3 4 0 1 2,
row 4 = 4 0 1 2 3,
the cyclic square L(r,c)=r+c mod 5.

If x=0, row 2 is forced to 2 0 4 1 3. Completion forces row 3 to be either 3 4 0 2 1 or 3 4 1 0 2; in either case row 4 begins 4 3, so rows 3,4 and columns 0,1 form the intercalate [3 4; 4 3], contradiction.

If x=4, row 2 is either 2 4 0 1 3 or 2 4 1 0 3. In the first case completion forces rows 3,4 to 3 0 4 2 1 and 4 3 1 0 2, and rows 2,4 on columns 2,3 form [0 1; 1 0]. In the second case row 3 is either 3 0 4 1 2 or 3 0 4 2 1. The first alternative gives an intercalate on rows 1,3 and columns 1,4, namely [2 0; 0 2]; the second forces row 4=4 3 0 1 2 and gives an intercalate on rows 2,4 and columns 2,3, namely [1 0; 0 1]. Thus both alternatives contradict intercalate-freeness.

Hence the only intercalate-free reduced square is the cyclic one. In it the seven cells
(0,0,0),
(0,2,2),
(1,2,3),
(4,4,3),
(2,4,1),
(3,3,1),
(3,1,4)
form a linear path. The consecutive joints are row 0, column 2, symbol 3, column 4, symbol 1, row 3, and every nonconsecutive pair is disjoint.

Thus every order-five Latin square gives a TD(3,5) containing P_7^(3). Such a path uses all 15 vertices, so it is spanning and has the maximum possible length.