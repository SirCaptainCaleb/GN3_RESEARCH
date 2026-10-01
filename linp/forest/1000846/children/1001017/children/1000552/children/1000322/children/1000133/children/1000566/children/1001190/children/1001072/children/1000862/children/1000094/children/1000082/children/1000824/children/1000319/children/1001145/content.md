# Double failure of the zero-slack switch forces a color derangement on a common neighborhood

## Statement

In the setting of 4468081d47b0, suppose the uncolored two-switch adjacency fails for both alternate terminal ports y,z of e=T_c. Then their contracted neighbor-index sets coincide:
A_y=A_z=A={1,...,c-1}\B,
with |A|=c/2. Moreover both y and z are adjacent in G to every vertex of every triple T_j with j∈A and to no X-vertex outside those triples. Hence y and z have the same k-element X-neighborhood S. Coloring the yS and zS edges by D gives two bijections alpha,beta:S->D with alpha(w)≠beta(w) for every w∈S; equivalently beta∘alpha^{-1} is a fixed-point-free permutation of the k colors.

## Body

Apply 4468081d47b0 separately to y and z. The shifted set B depends only on the fixed alternating witness and its penultimate triple T_{c-1}, not on the chosen terminal port.

If the uncolored switch adjacency fails for y, the equality branch of 4468081d47b0 gives
A_y=U\B
and |A_y|=c/2.
The same failure for z gives
A_z=U\B.
Thus A_y=A_z=:A.

Again by the equality statement of 4468081d47b0, for every j∈A the port y is adjacent to all three vertices of T_j. Since there are |A|=c/2 such triples, this accounts for
3c/2=k
neighbors, which is the full degree of y in the DXX graph. Thus y has no X-neighbor outside the union
S=union_{j∈A} V(T_j).
The same holds for z. Hence
N_G(y)=N_G(z)=S
and |S|=k.

In zero slack every vertex has exactly one incident edge of each color d∈D. Therefore the color on yw, as w ranges over S, defines a bijection
alpha:S->D,
and similarly the colors on zw define a bijection
beta:S->D.

For each w∈S, alpha(w)≠beta(w), because the two edges yw and zw are incident at w and G is properly edge-colored. Therefore the permutation
beta∘alpha^{-1}:D->D
has no fixed point.