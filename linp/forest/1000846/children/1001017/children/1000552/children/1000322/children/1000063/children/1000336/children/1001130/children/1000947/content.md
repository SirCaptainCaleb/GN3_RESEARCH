# All-entrance flat chains require labeled overlap, not generic two-path overlap

## Statement

In an all-entrance flat transfer chain, every step e_i->e_{i+1} supplies a (q-2)-edge path R_i between the consecutive entrance vertices x_i,x_{i+1}, with phi(x_i)=phi(x_{i+1})=q-1 and with R_i avoiding both terminal pairs. If R_i and R_{i+1} have no cross-intersections beyond their common entrance, they concatenate to a (2q-4)-edge linear path. However no generic bounded-cross-degree theorem can force a 3q/2-scale induced path when cross-intersections are present. A successful argument must use the additional blocker-memory: the preceding transfer edge is forced into the final q-2 tail of every longest witness for the next edge, together with entrance/terminal potential labels.

## Body

The intersection graph between two linear paths has bounded cross-degree because each hyperedge has only three vertices and a fixed hypergraph vertex can occur in at most two consecutive edges of the other path. Nevertheless two induced paths joined by a bounded-degree matching-like cross graph need not contain an induced path of length comparable to their total length; abstract cubic-like examples fence such a purely graph-theoretic claim. Thus 932e2a9de86d is useful only together with 6ff5b5590ee3 and 2a6eed0ab1f4. The next obligation is a labeled overlap lemma in which cross contacts are charged to previous-edge blocker memories or to vertices of endpoint potential at least q.