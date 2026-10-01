# Cartesian products multiply available linear-path lengths

## Statement

Let H and K be finite linear 3-graphs containing linear paths of lengths a>=1 and b>=1. Then their Cartesian product H square K contains a linear path of length (a+1)(b+1)-1. Consequently, if H has n vertices, m edges, and maximum linear-path length L>=1, then its t-fold Cartesian power has edge/vertex ratio t(m/n) and maximum linear-path length at least (L+1)^t-1. Thus repeated Cartesian powering of a fixed component cannot yield a positive asymptotic coefficient in (|E|/|V|)/ell when ell is one plus the maximum path length.

## Body

Write a Cartesian-product edge as either e x {y}, with e in E(H), or {x} x f, with f in E(K). Let E_1,...,E_a be a linear path in H and choose distinct terminal vertices p in E_1\E_2 and q in E_a\E_{a-1} (for a=1 choose two distinct vertices of E_1). Let F_1,...,F_b be a linear path in K. Choose y_0 in F_1\F_2, y_i=F_i intersect F_{i+1} for 1<=i<b, and y_b in F_b\F_{b-1}, with the evident endpoint choices when b=1.

For each i=0,...,b, place a copy of the H-path in the fiber over y_i, alternating its orientation. Between the copies over y_{i-1} and y_i insert the product edge {s_i} x F_i, where s_i is their common H-terminal coordinate. Because the orientations alternate, s_i alternates between p and q.

This sequence has (b+1)a+b=(a+1)(b+1)-1 edges. Consecutive pieces intersect in exactly the intended point (s_i,y_{i-1}) or (s_i,y_i). Distinct H-fiber copies are disjoint. A bridge {s_i} x F_i can meet a selected H-fiber only over y_{i-1} or y_i, and there it meets only the terminal edge of the corresponding H-path copy. Two bridges with consecutive K-indices use different H-coordinates p,q and are therefore disjoint; bridges whose indices differ by at least two are disjoint because the corresponding nonconsecutive K-path edges are disjoint. Hence every nonconsecutive pair of edges in the displayed sequence is disjoint, so it is a linear path.

For the t-fold power H^{square t}, the vertex count is n^t and the edge count is t m n^{t-1}, hence density t(m/n). Iterating the path construction gives maximum path length at least (L+1)^t-1. Therefore at the first forbidden path length ell_t, one has ell_t >= (L+1)^t and
 (|E(H^{square t})|/|V(H^{square t})|)/ell_t <= t(m/n)/(L+1)^t -> 0.
In particular Cartesian powering cannot amplify the 11-vertex, 15-edge P5 extremal component into an asymptotic improvement of the 1/3 lower coefficient.
