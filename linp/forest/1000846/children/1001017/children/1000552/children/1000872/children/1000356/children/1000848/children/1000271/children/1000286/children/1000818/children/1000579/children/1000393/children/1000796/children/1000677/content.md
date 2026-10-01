# Every foreign contact in a four-edge 0-1-1 block is a balanced-lens certificate

## Statement

Let e_i={x_i,v,u_i}, i=1,2,3,4, be source-clean 0-1-1 ascending nonspecial edges through a common assigned terminal v, with ranks in two consecutive levels, and let Q_i be their chosen maximum source paths ending at x_i.

For every ordered pair i!=j, choose any foreign contact
w in V(Q_i) intersect {x_j,u_j},
whose existence is guaranteed by complete foreign-edge transversality.

Then Q_i and the chosen maximum endpoint path P_w share at least two vertices and contain a balanced elementary lens adjacent to w.

In particular:
- if w=x_j, then P_w=Q_j may be used, so every directed source hit x_j in Q_i creates a balanced source-source lens between Q_i and Q_j;
- if w=u_j, the contact creates a balanced source-terminal lens between Q_i and P_{u_j}.

Hence the twelve directed foreign-contact obligations in a four-edge 0-1-1 block are simultaneously twelve balanced-lens/no-piercing certificates.

## Body

By complete foreign-edge transversality 3d93f4d4b775, for every i!=j the foreign edge e_j meets Q_i. Since Q_i avoids the common assigned terminal v, this contact lies in {x_j,u_j}; choose one and call it w.

The path Q_i is maximum at its endpoint x_i. The chosen path P_w is maximum at w. Also w!=x_i: otherwise the distinct hyperedges e_i and e_j would share both v and x_i, violating linearity. Thus b35b0fd4e4cd applies directly to the occurrence w in V(Q_i), and gives a second common vertex together with a balanced elementary lens adjacent to w.

If w=x_j, the chosen maximum source rail Q_j itself is a maximum endpoint path at x_j, so P_w may be taken to be Q_j. If w=u_j, take the globally chosen maximum terminal path at u_j. This proves all assertions.
