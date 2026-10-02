# Every order-four transversal design has a maximum-length linear path

## Statement

Every transversal design TD(3,4), equivalently every Latin square of order 4, contains a linear path of length 5. This is best possible because such a path uses 11 vertices and TD(3,4) has 12 vertices.

## Body

It suffices to work with reduced Latin squares, since permuting rows, columns, or symbols preserves the associated transversal design and its linear paths. Write the symbols as 0,1,2,3 and reduce so that the first row and first column are 0,1,2,3.

The second row begins with 1. Its entry in column 1 is one of 0,2,3. If it is 0, the row is forced to be 1,0,3,2. Completing the remaining two rows gives exactly two reduced squares:
L_1=
0 1 2 3
1 0 3 2
2 3 0 1
3 2 1 0
and
L_2=
0 1 2 3
1 0 3 2
2 3 1 0
3 2 0 1.
If the (1,1)-entry is 2, Latin constraints force
L_3=
0 1 2 3
1 2 3 0
2 3 0 1
3 0 1 2.
If the (1,1)-entry is 3, they force
L_4=
0 1 2 3
1 3 0 2
2 0 3 1
3 2 1 0.
Thus these four squares are all reduced Latin squares of order 4.

Represent a cell (r,c) carrying symbol s by the hyperedge (r,c,s). In L_1 and L_3 the five cells
(0,2,2),(0,0,0),(1,0,1),(2,3,1),(2,1,3)
form a linear path: consecutive triples share respectively a row, a column, a symbol, and a row, while every nonconsecutive pair is disjoint.

In L_2 the five cells
(0,1,1),(0,0,0),(2,0,2),(1,3,2),(1,2,3)
form such a path.

In L_4 the five cells
(0,3,3),(0,0,0),(2,0,2),(3,1,2),(3,2,1)
form such a path.

Hence every reduced order-4 Latin square, and therefore every order-4 Latin square, gives a TD(3,4) containing P_5^(3). A 6-edge linear 3-uniform path would require 13 vertices, so length 5 is maximal on 12 vertices.