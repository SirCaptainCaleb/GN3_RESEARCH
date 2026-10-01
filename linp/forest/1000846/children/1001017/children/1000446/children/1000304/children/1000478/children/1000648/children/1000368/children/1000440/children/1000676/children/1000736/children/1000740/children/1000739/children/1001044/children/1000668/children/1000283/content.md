# The two-contact 4455 low-low branch is a rigid four-cycle plus rank-five triangle

## Statement

Continue in the {b,c} witness geometry of the p=5 pattern (4,4,5,5), and let h={x,v,u} be the second rank-five charged edge.

Assume h meets both g2 and g4. Then:
1. h∩g4 is the private vertex of g4;
2. h∩g2 is the joint g1∩g2.

Consequently
  h,g2,g3,g4
form a linear 4-cycle, while
  h,g4,e5
form a linear 3-cycle. Thus the whole two-contact obstruction is a rigid theta consisting of a 4-cycle and a 3-cycle sharing the edge-pair h,g4.

## Body

By 96ce63c6b236, h is disjoint from g_3. Because h and e_5 already share v, linearity forbids h from meeting g_4 at d=g_4∩e_5. Because h is disjoint from g_3, it cannot meet g_4 at c=g_3∩g_4. Hence its g_4-contact is the private vertex z of g_4.

Let y be the h-contact with g_2. Since h is disjoint from g_3, y≠a=g_2∩g_3. Thus y is either the private vertex of g_2 or the joint g_1∩g_2.

Suppose y is private to g_2. Then h is disjoint from g_1, while g_1 and g_4 are disjoint in the original path P. Therefore
  (g_1,g_2,h,g_4)
is a four-edge linear path: consecutive intersections are the original g_1∩g_2 joint, then y, then z; all nonconsecutive pairs are disjoint. Its last edge is g_4, entered through z. The vertex c∈g_4 is distinct from z and can be chosen as the last vertex. Hence phi(c)>=4, contradicting phi(c)=3.

Therefore y=g_1∩g_2.

Now h and g_2 meet at y; g_2 and g_3 meet at a; g_3 and g_4 meet at c; and g_4 and h meet at z. These four joints are distinct: y,a,c are distinct path joints and z is private to g_4. Nonconsecutive pairs h,g_3 and g_2,g_4 are disjoint. Hence h,g_2,g_3,g_4 form a linear 4-cycle.

Finally h∩e_5={v}, e_5∩g_4={d}, and g_4∩h={z}, with v,d,z distinct, so h,g_4,e_5 form a linear 3-cycle.
