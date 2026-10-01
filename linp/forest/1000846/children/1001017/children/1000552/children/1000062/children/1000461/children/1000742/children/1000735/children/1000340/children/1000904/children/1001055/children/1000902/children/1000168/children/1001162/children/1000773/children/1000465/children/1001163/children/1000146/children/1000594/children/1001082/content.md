# A narrow vertex-rank band bounds uniquely-intersecting crossing pairs

## Statement

Retain the setup and notation of 85d576d60e7e. Let X be any graph on the same vertex set C whose edges are crossing interval pairs for which the auxiliary maximum paths satisfy the cross-splice hypotheses of 20606dbd4cd9. Split
  E(X)=E_1 disjoint union E_2,
where cd is in E_1 when P_c and P_d have exactly one common vertex, and cd is in E_2 when they have at least two common vertices.

Assume every c in C has vertex rank in an integer interval [A,B], and put R=B-A+1. Then
  |E_1| <= (R-1)|C|/2.
Consequently
  |E_2| >= |E(X)|-(R-1)|C|/2.

Thus, whenever the crossing graph has more than (R-1)|C|/2 edges, at least one crossing pair has auxiliary maximum paths with at least two common vertices; any excess above that threshold counts distinct such crossing pairs.

## Body

Consider the graph U=(C,E_1). By 85d576d60e7e, every connected component of U has at most R vertices.

If a component has s vertices, it has at most binom(s,2) edges, and because s<=R,
  binom(s,2) <= (R-1)s/2.
Summing over all components gives
  |E_1| <= (R-1)|C|/2.

Since E_2 is the complement of E_1 inside E(X), the second inequality follows immediately.
