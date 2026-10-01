# Boundary entrance-path rotation graph has no sinks

## Statement

Let H be a finite linear 3-graph with minimum degree at least q, and let f be an ascending nonspecial edge of rank q with unique entrance x, so phi(x)=q-1. Let S(f,x) be the finite set of (q-1)-edge linear paths P that have last vertex x and have f as their last edge. For every P in S(f,x), there is a distinct P_prime in S(f,x) obtained by a single-blocker endpoint-preserving rotation. Consequently the directed rotation graph on S(f,x), with all such rotations as arcs, has positive outdegree at every state and therefore contains a directed cycle.

## Body

Fix P=(g_1,...,g_{q-1}) in S(f,x) and let a be either last vertex of g_1 at the end opposite x. No edge through a distinct from g_1 can be clean relative to P: prepending such an edge would give a q-edge path with last vertex x, contradicting phi(x)=q-1. Let S,D be the numbers of single- and double-blocking edges through a other than g_1. Since d_H(a)>=q, S+D>=q-1. Their blocker sets are disjoint by linearity and lie in V(P) minus g_1, which has 2q-4 vertices, so S+2D<=2q-4. Hence S>=2. At most one of the single blockers can use x, since two distinct edges through a and x would violate linearity. Choose a single blocker h with blocker w!=x. By 912c72c000da there is another (q-1)-edge path P_prime with last vertex x and using h. The new edge h avoids x, because x would otherwise be its blocker. In the original path P, x occurs only in the last edge f; the explicit rotation in 912c72c000da retains that last edge. Hence P_prime also has f as its last edge, so P_prime lies in S(f,x). It is distinct from P because it uses h notin E(P). Thus every state has positive outdegree. Finiteness gives a directed cycle.
