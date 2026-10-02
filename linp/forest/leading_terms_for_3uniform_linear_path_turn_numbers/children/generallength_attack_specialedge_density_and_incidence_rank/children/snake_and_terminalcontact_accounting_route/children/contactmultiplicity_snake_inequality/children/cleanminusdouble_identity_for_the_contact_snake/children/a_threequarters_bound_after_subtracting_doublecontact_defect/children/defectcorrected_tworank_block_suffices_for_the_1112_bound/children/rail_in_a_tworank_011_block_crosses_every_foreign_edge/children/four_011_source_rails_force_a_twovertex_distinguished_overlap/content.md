# Four 0-1-1 source rails force a two-vertex distinguished overlap

## Statement

For four source-clean 0-1-1 edges through one assigned terminal, with ranks in any two consecutive levels, choose their clean source rails Q_i. Then some pair Q_i,Q_j shares at least two distinct vertices among the eight non-v source/terminal vertices of the four edges. This follows purely by double counting: each rail contains its own source plus one vertex from each of the other three disjoint source-terminal pairs, giving four 4-subsets of an 8-set and total pair-intersection mass at least 8.

## Body


Let
  e_i={x_i,v,u_i}, i=1,2,3,4,
be four 0-1-1 ascending nonspecial edges through the common terminal v, with ranks in {q,q+1}, and let Q_i be their chosen clean source rails as in 3d93f4d4b775.

By linearity, the eight non-v vertices
  X={x_1,u_1,...,x_4,u_4}
are all distinct.

For each ordered pair i!=j, 3d93f4d4b775 says Q_i meets e_j, hence Q_i contains at least one of {x_j,u_j}. Also Q_i contains its own endpoint x_i and avoids u_i.

For each i choose one witness
  w_{ij} in Q_i cap {x_j,u_j}
for every j!=i, and define
  S_i={x_i} union {w_{ij}:j!=i}.
Then S_i is a 4-element subset of the eight-element set X, and
  S_i subseteq V(Q_i).

Let d(a)=|{i:a in S_i}| for a in X. Since sum_i |S_i|=16,
  sum_{a in X} d(a)=16.
Moreover
  sum_{1<=i<j<=4}|S_i cap S_j|
   = sum_{a in X} binom(d(a),2).

For eight nonnegative integers with total 16, convexity of t -> binom(t,2) gives
  sum_a binom(d(a),2) >= 8,
with equality when all d(a)=2.

There are only six unordered pairs {i,j}. Therefore some pair satisfies
  |S_i cap S_j|>=2.

Since S_i subseteq V(Q_i) and S_j subseteq V(Q_j), the corresponding source rails Q_i,Q_j have at least two distinct common vertices, and these common vertices can be chosen among the eight distinguished sources/terminals of the four offending edges.
