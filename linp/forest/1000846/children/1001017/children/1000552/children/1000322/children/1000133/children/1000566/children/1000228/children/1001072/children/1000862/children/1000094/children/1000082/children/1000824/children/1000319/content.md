# Failure of an uncolored entrance switch forces an exact half-neighborhood partition

## Statement

In the zero-slack alternating witness
T_1,C_1,...,C_{c-1},T_c=e,
fix an alternate terminal port y∈e. Let
A_y={j∈{1,...,c-1}: some DXX connector joins y to T_j}
and
B={j∈{2,...,c-1}: some DXX connector joins T_{j-1} to T_{c-1}}.
Then |A_y|>=c/2 and |B|>=c/2-1. Hence either A_y∩B is nonempty, supplying the two contracted adjacencies required by the entrance-switch lemma 767380617163, or else:
|A_y|=c/2, |B|=c/2-1,
A_y and B partition {1,...,c-1},
every triple T_j with j∈A_y contains exactly three neighbors of y in the DXX graph,
and the contracted degree of T_{c-1} is exactly c/2.

## Body

The port y lies in the forest triple e. In zero slack it has degree k in the DXX graph G, with k distinct X-neighbors because G is simple. No neighbor lies inside e. Any other forest triple contains only three vertices, so at least
ceil(k/3)=k/3=c/2
distinct forest triples contain neighbors of y. Hence |A_y|>=c/2.

Now consider the contracted simple graph R from 4596218dad6. The node T_{c-1} has degree at least c/2. One of its neighbors is T_c=e, witnessed by the final connector C_{c-1}. Every other neighbor is among T_1,...,T_{c-2}; shifting T_i to the index j=i+1 gives B. Therefore
|B|>=c/2-1.

Both A_y and B are subsets of U={1,...,c-1}, whose size is c-1. If they intersect, choose j in the intersection. Then there is a connector h from y to T_j and a connector g from T_{j-1} to T_{c-1}, exactly the two contracted adjacencies appearing in 767380617163 (with the endpoint cases j=1 handled separately if desired).

Suppose instead A_y∩B is empty. Then
c-1=|U|>=|A_y|+|B|>=c/2+(c/2-1)=c-1.
Thus equality holds throughout:
|A_y|=c/2,
|B|=c/2-1,
and A_y∪B=U.

Since y has exactly k=3c/2 distinct X-neighbors distributed among exactly c/2 triples, with at most three neighbors per triple, every T_j for j∈A_y contains all three of its vertices as neighbors of y.

Likewise T_{c-1} has exactly |B|+1=c/2 contracted neighbors: the |B| earlier triples encoded by B and T_c. Thus its contracted degree is exactly the Dirac lower bound c/2.