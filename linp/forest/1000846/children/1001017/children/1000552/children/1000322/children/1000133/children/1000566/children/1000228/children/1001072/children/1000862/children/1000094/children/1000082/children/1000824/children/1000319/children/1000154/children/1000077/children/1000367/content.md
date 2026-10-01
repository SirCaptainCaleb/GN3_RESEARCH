# Rigid zero-slack half-neighborhoods always contain an uncolored fixed-target 2-opt cut

## Statement

In the rigid zero-slack half-neighborhood branch of fb4fc1ee4179, with alternating witness
  T_1,C_1,...,T_{c-1},T_c=e,
let A be the common c/2-element neighbor-index set of the alternate ports y,z. Then there exists an index i∈A, 1<=i<=c-2, such that the contracted graph R contains an edge T_1 T_{i+1}.

Thus at cut i the two uncolored adjacencies required by the fixed-target exchange decf9b49b8d7 are both present:
- y (and z) is adjacent to T_i;
- T_1 is adjacent to T_{i+1}.

## Body

By the definition of B in 4468081d47b0, the original connector C_{c-2} between T_{c-2} and T_{c-1} implies c-1∈B. Since A and B partition {1,...,c-1}, we have c-1∉A. Therefore
  A⊂{1,...,c-2}
and |A|=c/2.

By 4596218dad6, the contracted graph R has minimum degree at least c/2. Hence T_1 has at least c/2 neighbors. At most one of them is T_c=e. Therefore T_1 has at least c/2-1 neighbors among T_2,...,T_{c-1}.

Let
  C={i∈{1,...,c-2}: T_{i+1} is adjacent to T_1}.
Then |C|>=c/2-1.

Both A and C lie in the universe {1,...,c-2}, of size c-2. Hence
  |A∩C| >= |A|+|C|-(c-2)
          >= c/2+(c/2-1)-(c-2)
          =1.
Choose i∈A∩C. Since i∈A, y and z are each adjacent to every vertex of T_i in the rigid branch. Since i∈C, T_{i+1} is adjacent to T_1. These are exactly the two contracted adjacencies used in decf9b49b8d7.