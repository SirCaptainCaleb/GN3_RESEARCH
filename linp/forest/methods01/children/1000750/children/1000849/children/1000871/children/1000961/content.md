# The diagonal product C7 tensor C7 has maximum path length at most 81

## Statement

Let C7 be the 3-uniform linear seven-cycle. In the diagonal product C7 tensor C7, every linear path has at most 81 edges. More generally, if C_s is a linear s-cycle and a path in C_s tensor C_s has L edges, then a simple type count gives 3L <= 5s^2-1, hence L <= floor((5s^2-1)/3). For s=7 this gives L<=81. Thus the natural C7 tensor C7 subproduct cannot supply the 97-edge path needed to fence PG(3,2) tensor PG(3,2); instead it exhibits substantial path suppression under diagonal product.

## Body

Write the vertices of C_s as joint vertices J_i and private vertices P_i, i in Z_s, with edge E_i={J_i,P_i,J_{i+1}}. Product vertices in C_s tensor C_s have four types JJ, JP, PJ, PP, with s^2 vertices of each type.

Every diagonal-product triple comes from a bijection between two factor edges. Call it aligned if the private vertex P_i of the first factor edge is matched to the private vertex P_j of the second. An aligned product triple has type multiset {JJ,JJ,PP}. Every other bijection is crossed and has type multiset {JJ,JP,PJ}.

Let Q be a linear path of L hyperedges and let x be the number of aligned edges. The total number of JJ incidences in Q is
  2x+(L-x)=L+x.
Any vertex can lie in at most two edges of a linear path, so, since there are s^2 JJ vertices,
  L+x <= 2s^2.                                      (1)

A linear L-edge path has exactly 2L+1 distinct vertices. The ambient product has 4s^2 vertices, so Q omits exactly 4s^2-(2L+1) vertices. Only aligned product edges contain PP vertices, one PP incidence each. Therefore Q uses at most x distinct PP vertices and omits at least s^2-x PP vertices. Hence
  s^2-x <= 4s^2-(2L+1),
or
  x >= 2L+1-3s^2.                                  (2)

Combining (1) and (2),
  L+(2L+1-3s^2) <= 2s^2,
so
  3L <= 5s^2-1.
Therefore
  L <= floor((5s^2-1)/3).

For s=7, this is L<=floor(244/3)=81.

The argument is purely structural and uses no computation. It also shows why a Hamilton loose cycle in C_s tensor C_s is impossible: covering many PP vertices forces many aligned edges, while every aligned edge consumes an extra JJ incidence beyond the unavoidable one-JJ-per-product-edge budget.
