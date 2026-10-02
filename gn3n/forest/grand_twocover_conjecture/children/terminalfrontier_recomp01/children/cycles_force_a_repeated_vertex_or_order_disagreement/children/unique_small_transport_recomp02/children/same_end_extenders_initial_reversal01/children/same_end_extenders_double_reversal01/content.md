# Universal same-end extenders force a synchronized double endpoint reversal

## Statement

Under the hypotheses of same_end_extenders_initial_reversal01, assume a residual two-cover T=R|S of H-{x,y} has no order disagreement with any displayed core. Then one of the following synchronized alternatives holds: (i) one extender z∈{x,y} fails to prepend both R and S, so the initial edge of each residual component is cross-core and its boundary reversal through z is tight; or (ii) one residual component U∈{R,S} cannot be prepended by either x or y, so its cross-core initial edge has tight boundary reversals through both extenders. The terminal-extender version is symmetric.

## Body

Write R=(r_1,r_2,...) and S=(s_1,s_2,...), with both components of order at least two as in same_end_extenders_initial_reversal01. In the no-order-disagreement branch, for each extender z∈{x,y} and each residual component U, failure of z to prepend U can occur only when the first two vertices of U lie in different displayed cores; boundary flip then gives a tight reverse cross triple through z.

Form the bipartite graph B with left vertices {x,y}, right vertices {R,S}, and edge zU exactly when z can be prepended to U. If B had a perfect matching, assigning the two extenders to the matched residual components would produce two tight paths covering all of H, contrary to pc(H)>2. Hence B has no perfect matching.

By Hall's theorem for this 2-by-2 graph, either some left vertex has empty neighborhood or some right vertex has empty neighborhood. In the first case one extender z fails to prepend both R and S; therefore both initial edges are cross-core and both boundary-reversed triples through z are tight. In the second case one residual component U is not prependable by either extender; therefore its initial edge is cross-core and its boundary reversals through x and y are both tight.

This is strictly stronger than the existence of one reverse cross triple: the obstruction is synchronized either by a common reversing label or by a common reversed residual edge. No additional size assumptions are used.