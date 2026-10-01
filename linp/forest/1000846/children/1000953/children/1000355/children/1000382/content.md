# Odd-order additive Latin blow-ups lift every base linear cycle

## Statement

Let T be a linear 3-graph containing a linear cycle of length s, and let q be odd. In the additive Z_q blow-up of T, that base cycle lifts to a linear cycle of length sq. Hence a fixed template with v vertices and m edges has normalized density at its first forbidden path length at most m/(vs). In particular the 11-vertex, 15-edge P5-extremal template G0 contains a base 5-cycle, so its additive blow-up contains a 5q-cycle and is bounded by 3/11<1/3.

## Body

Write the base cycle as E_1,...,E_s with joint clusters X_0,...,X_{s-1} and private clusters P_i. In the additive transversal design over Z_q, restrict edge type E_i to triples whose successive joint coordinates satisfy y=x+a_i. The private coordinate is -2x-a_i, injective in x because q is odd. Choose the shifts so A=sum_i a_i generates Z_q, for instance a_1=1 and the rest zero. One circuit sends state x in X_0 to x+A, so q circuits traverse all q states before returning. Joint vertices are used only by their two consecutive lifted edges, private coordinates are all distinct within an edge type, and nonconsecutive base cycle edges are disjoint. Thus the lift is a linear cycle of length sq.

The blow-up has qv vertices and q^2m edges, hence density mq/v. Removing one edge from the sq-cycle gives a path of length sq-1, so the first forbidden length is at least sq and the normalized density is at most m/(vs).

For G0 from the standard one-factorization of K_6, the graph edges 01,13,23,24,04 have five distinct colors and lift to a base linear 5-cycle. Therefore its additive blow-up contains a 5q-cycle. Since v=11 and m=15, the normalized density is at most 15/(11·5)=3/11, decisively below one third.
