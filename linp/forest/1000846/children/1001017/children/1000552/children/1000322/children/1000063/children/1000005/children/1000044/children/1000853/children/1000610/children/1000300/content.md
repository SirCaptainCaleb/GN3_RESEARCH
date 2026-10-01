# Open-chain endpoints in Class III are exactly the terminal defects

## Statement

Let H be a 12-vertex 5-regular linear triple system and let P=(g_1,g_2,g_3,g_4,e) be a maximum five-edge path ending in a nonspecial edge e={x,y,z} through entrance x. For v in {y,z}, if B_P(v)=3, let w_v be the W-contact of the unique single blocker {v,o,w_v}, and let v* be the unique uncovered mate of v. Then the two vertices unmatched by the double-blocker matching M_v are exactly {w_v,v*}; if B_P(v)=4 then M_v is perfect on W and v*=o. Consequently: in the (4,3) blocker-count case, the unique open alternating path in M_y union M_z has endpoints w_v and v* for the terminal v with B_P(v)=3; in the (3,3) case, the two path-component defects are determined exactly by the two unmatched sets {w_y,y*} and {w_z,z*}.

## Body

Put W=V(P)\e and let o be the unique vertex outside P. Fix a terminal v.

The four edges through v other than e have pairwise disjoint off-v pairs and cover eight of the nine vertices in V(H)\e except for the unique uncovered mate v*.

If B_P(v)=4, all four off-v pairs lie in W, so they partition W. Thus M_v is a perfect matching on W. The only vertex outside W among V(H)\e is o, hence the omitted mate is v*=o.

If B_P(v)=3, exactly one v-edge is a single blocker. By 5-regularity and the counting in 8a2c12515954, it has the form {v,o,w_v} with w_v in W, while the other three v-edges are double blockers and their three pairs form M_v. These three pairs cover six vertices of W. The single blocker accounts for w_v and the unique globally uncovered mate accounts for the only other point not covered by the four off-v pairs. Hence the two vertices of W unmatched by M_v are exactly w_v and v*.

Now let G=M_y union M_z. A vertex has degree one in G exactly when it is unmatched by one of the two matchings and matched by the other; it is isolated exactly when it is unmatched by both. All nontrivial components of G are alternating paths or even cycles.

In the (4,3) case, one matching is perfect and the other has unmatched set {w_v,v*}. Therefore exactly w_v and v* have degree one, so the unique path component supplied by 8a2c12515954 is the alternating path joining those two vertices; every other component is a cycle.

In the (3,3) case, the unmatched sets are U_y={w_y,y*} and U_z={w_z,z*}. Thus the degree-one vertices are U_y symmetric-difference U_z and the isolated vertices are U_y intersection U_z. Since 8a2c12515954 gives exactly two path components counting isolates, these unmatched sets completely determine the two open defects: if they are disjoint there are two nontrivial paths pairing the four degree-one vertices; if they meet in one point there is one isolated vertex and one nontrivial path; if they coincide, both path components are isolated and every other component is an alternating cycle.

By 0dbbb7d78a48, each single-blocker contact w_v is either in the early set W∩V(g_1∪g_2), or lies in g_4\e as the genuine penultimate exception. Thus every open-chain defect arising from a single blocker is pinned to an explicitly localized path position.