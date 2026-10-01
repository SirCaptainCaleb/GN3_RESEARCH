# Rigid half-neighborhoods force an unused-color safe target connector

## Statement

In the rigid zero-slack half-neighborhood branch, an alternate target port y is complete to c/2 forest triples and its k=3c/2 incident DXX edges use all colors once. Since the witness uses only c-1 colors, c/2+1 unused-color y-edges land in those c/2 triples. Hence some target triple T_i has at least two unused-color y-connectors, and at least one avoids the unique locally unsafe port. Thus a fixed-target 2-opt obstruction can no longer be blamed on the target connector; the remaining obstruction is the return connector.

## Body


Assume the rigid zero-slack half-neighborhood conclusion of 21fb5bf1458a for an alternate target port y. Thus A is a set of c/2 forest triples, y is adjacent in the DXX graph to every one of their 3c/2=k vertices, and y has no DXX neighbors outside their union.

The fixed alternating witness uses exactly c-1 connector colors. Since the total color set has size
  k=3c/2,
the number of colors unused by the witness is
  k-(c-1)=c/2+1.

Because the DXX coloring is proper and d(y)=k, the k edges incident with y use every threshold color exactly once. All these edges land in the c/2 triples of A. Hence exactly c/2+1 of the y-edges into A have colors unused by the witness.

Distribute those c/2+1 unused-color y-edges among the c/2 triples of A. Some triple T_i in A receives at least two of them. They meet two distinct vertices of T_i because the graph is simple.

For the fixed-target 2-opt exchange decf9b49b8d7 at cut i, at most one vertex of T_i is forbidden by the local port-safety condition (namely the port used by the retained connector on the appropriate side). Therefore at least one of the two unused-color y-connectors f from T_i to e is port-safe. Its color is globally unused by the original witness, so it automatically avoids every retained connector color and can also be chosen independently of any return connector g unless g uses that same unused color; with two candidate unused-color f's, even that single conflict can be avoided whenever both are port-safe, and otherwise the unique port-safe choice is the only remaining color issue.

Thus, in the rigid complete-half-neighborhood branch, target-side color/port compatibility cannot globally obstruct every 2-opt move. There exists a cut i in A for which the target connector f may be chosen with an unused witness color and a safe target-side port. The remaining obstruction is concentrated entirely in finding a compatible return connector from T_{i+1} to T_1 (or the corresponding block-reversal return in the alternate 767380617163 formulation).
