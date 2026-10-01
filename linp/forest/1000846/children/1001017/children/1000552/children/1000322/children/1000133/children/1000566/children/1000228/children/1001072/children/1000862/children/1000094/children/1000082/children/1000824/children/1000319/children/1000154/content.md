# If both alternate ports fail the zero-slack two-switch, they have an identical complete half-neighborhood

## Statement

In the zero-slack alternating witness
  T_1,C_1,...,C_{c-1},T_c=e={x,y,z},
let B⊂{1,...,c-1} be as in 4468081d47b0. For p∈{y,z}, let
  A_p={j: p has a DXX neighbor in T_j}.

Suppose the uncolored adjacency requirement of the entrance-switch lemma 767380617163 fails for both alternate ports y and z, i.e.
  A_y∩B=A_z∩B=∅.
Then
  A_y=A_z={1,...,c-1}\B,
and this common set has size c/2.

Moreover, for every j in this common set, both y and z are adjacent in the DXX graph to all three vertices of T_j; and neither y nor z has any DXX neighbor in a triple indexed by B.

## Body

Apply 4468081d47b0 first to y. Since A_y∩B is empty, its equality branch gives
|A_y|=c/2, |B|=c/2-1,
and A_y∪B={1,...,c-1}.
Thus A_y is exactly the complement of B.

Apply the same lemma to z. The set B depends only on the fixed witness and T_{c-1}, not on the chosen alternate port. Since A_z∩B is also empty, the equality branch again gives that A_z is the complement of B. Hence A_y=A_z=:A and |A|=c/2.

The vertex y has degree k=3c/2 in the zero-slack DXX graph. Its neighbors all lie outside e and, by definition of A, all lie in the c/2 triples T_j with j∈A. Those triples contain exactly 3(c/2)=3c/2=k vertices total. Since G is simple and y has k distinct neighbors, it must be adjacent to every vertex in their union and to no vertex outside it. The same argument applies to z.