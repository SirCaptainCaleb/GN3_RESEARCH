# A loss-one two-cycle has a fixed hole with unavoidable external attachment surplus

## Statement


In the canonical loss-one double-blocker two-cycle, both rotated states omit the same path vertex b_{i+1}; their second omitted vertices differ. This fixed hole b has at least two neighbor incidences outside the original path. Hence either one edge through b is otherwise disjoint from the original path, or at least two distinct b-edges are one-contact external chords.


## Body


Write Q=(g_1,...,g_t), with g_1={a,a',c_1}, and A_j={b_j,c_j} the two new vertices at step j. Let h={a,u,b_{i+2}} be the loss-one blocker, with u in A_i and d the other vertex of A_i. The canonical states are
  P_0=(g_{i-1},...,g_1,h,g_{i+2},...,g_t),
  P_1=(g_2,...,g_i,h,g_{i+2},...,g_t).
Tracking cells shows
  V(P_0)=V(Q) minus {b_{i+1},d},
  V(P_1)=V(Q) minus {b_{i+1},a'}.
Thus b=b_{i+1} is a fixed hole of both states.

The vertex b is private to g_{i+1}. Minimum degree q gives at least q-1 edges through b besides g_{i+1}. By linearity these edges use pairwise disjoint vertices outside b and cannot use the other two vertices of g_{i+1}. Hence they contribute at least 2q-2 distinct neighbors, while V(Q) minus g_{i+1} has only 2q-4 vertices. At least two neighbor incidences therefore lie outside V(Q). If two occur on one b-edge, that edge meets Q only at b. Otherwise they occur on at least two distinct edges, each having exactly one further Q-contact and one outside vertex. This is the fixed-hole attachment surplus.
