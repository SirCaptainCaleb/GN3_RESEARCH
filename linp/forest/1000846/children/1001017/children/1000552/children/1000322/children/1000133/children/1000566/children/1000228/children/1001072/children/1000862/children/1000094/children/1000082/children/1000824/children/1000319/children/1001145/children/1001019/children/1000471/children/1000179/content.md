# Odd-k rigid zero-slack branch must contain an S-to-B connector

## Statement

In the odd-k rigid zero-slack no-switch setting of 6894769a092f, alternative (B) is impossible. Hence alternative (A) must hold: there is a DXX edge joining S to B_X.

## Body

Assume alternative (B) of 6894769a092f. Then
N_G(x)=N_G(y)=N_G(z)=S,
where e={x,y,z}, |S|=k, and
X=S disjoint-union B_X disjoint-union {x,y,z}
with |X|=2k. Therefore
|B_X|=2k-k-3=k-3.

By definition of alternative (B), none of x,y,z has a neighbor in B_X. Because adjacency is symmetric, no vertex of B_X is adjacent to x,y, or z.

Also alternative (A) fails in branch (B), so there is no DXX edge joining S to B_X. Hence no vertex of B_X has a neighbor in S either.

Therefore every neighbor in G of a vertex b∈B_X must lie inside B_X itself. But G is k-regular in the zero-slack model, while B_X has only k-3 vertices. Thus
d_G(b) <= |B_X|-1 = k-4,
contradicting d_G(b)=k.

Hence alternative (B) cannot occur. The rigid odd-k branch necessarily contains an S-B_X connector as in alternative (A).