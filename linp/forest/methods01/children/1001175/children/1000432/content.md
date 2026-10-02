# The fixed hole has three external incidences relative to the rotated state

## Statement

In the canonical loss-one two-cycle setting of 0501d7730fd2 and bf82e5f39180, let P_1 be the rotated x-ending path of length q-2 and let b=b_{i+1} be the vertex omitted from P_1. Then among the edges through b other than g_{i+1}, the total number of non-b vertices lying outside V(P_1) is at least three. Consequently either some edge through b is disjoint from P_1, or at least three distinct edges through b meet P_1 in exactly one vertex and have their third vertex outside P_1.

## Body

Write P_1=(g_2,g_3,...,g_i,h,g_{i+2},...,g_t), where t=q-1. The omitted original edge is g_{i+1}={c_i,b,c_{i+1}}. Both c_i and c_{i+1} lie on P_1: c_i lies in g_i and c_{i+1} lies in g_{i+2}. Since d_H(b)>=q, there are at least q-1 edges f distinct from g_{i+1} through b. By linearity, no such f can contain c_i or c_{i+1}, because otherwise f and g_{i+1} would share two vertices. Also distinct such edges have disjoint non-b vertex pairs. Thus these q-1 edges contribute at least 2q-2 distinct non-b vertices, while at most |V(P_1)|-2=(2(q-2)+1)-2=2q-5 of them can lie on P_1. Hence at least three lie outside V(P_1). If some incident edge contributes two outside vertices, then b is also outside P_1 and that edge is disjoint from P_1. Otherwise every outside incidence belongs to a distinct edge having exactly one P_1 contact, so there are at least three such one-contact edges.