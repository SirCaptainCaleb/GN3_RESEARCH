# The fixed-target single-blocker rotation graph is K4-free

## Statement

In the boundary fixed-target endpoint-preserving single-blocker rotation graph of 68593c300c9c, no four distinct path states are pairwise rotation-adjacent. Equivalently, the rotation graph contains no K4.

## Body

Suppose for contradiction that P,P_1,P_2,P_3 span a K4. Write
  P=(g_1,...,g_t),
and let a,b be the two free opposite vertices of g_1.

For each pair i!=j, the triple P,P_i,P_j is a rotation triangle. By the exact triangle normal form f173a72fd8b2, every such triangle has common removed edge g_2. Hence, for i=1,2,3,
  E(P_i)=E(P)-{g_2}+{h_i}
for three distinct external rotation edges h_i.

Again by f173a72fd8b2, in any rotation triangle P,P_i,P_j the two replacement edges h_i,h_j use opposite free endpoints of g_1: one contains a and the other contains b. (Each contains exactly one free endpoint; containing both would make it meet g_1 in two vertices, impossible by linearity.)

Thus assign each h_i one of two types, A or B, according as it contains a or b. Pairwise adjacency of P_i and P_j forces h_i and h_j to have different types for every distinct i,j.

But three objects cannot be pairwise different under a two-type partition. By the pigeonhole principle two of h_1,h_2,h_3 have the same type, contradicting the triangle normal form for the corresponding triangle with P.

Therefore no K4 exists.
