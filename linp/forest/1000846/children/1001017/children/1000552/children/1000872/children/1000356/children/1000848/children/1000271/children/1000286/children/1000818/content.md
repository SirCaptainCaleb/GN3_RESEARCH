# Source-clean rails in a two-rank 0-1-1 block are pairwise intersecting

## Statement

For any two 0-1-1 ascending edges through the same assigned terminal whose ranks lie in two consecutive levels, their chosen source-clean maximum endpoint paths intersect. If the first rail meets the second edge at its source, the source itself is common. If it meets only the opposite terminal, then disjoint rails would concatenate through that edge to a path ending at the first source longer than its endpoint potential. Hence a four-edge violation gives a K4 of pairwise-intersecting source rails, with some pair overlapping in at least two distinguished vertices.

## Body

Let e_i={x_i,v,u_i} and e_j={x_j,v,u_j} be distinct 0-1-1 ascending nonspecial edges through the same assigned terminal v, with ranks in {q,q+1}. Let
  Q_i=(g_1,...,g_{p_i}),   p_i=phi(x_i),
  Q_j=(h_1,...,h_{p_j}),   p_j=phi(x_j)
be their chosen source-clean maximum paths, ending at x_i,x_j respectively. Thus
  p_i,p_j in {q-1,q},
so |p_i-p_j|<=1, and Q_i avoids v,u_i while Q_j avoids v,u_j.

By 3d93f4d4b775, e_j meets Q_i.

If x_j lies on Q_i, then V(Q_i) cap V(Q_j) is already nonempty because x_j is the endpoint of Q_j.

Otherwise every Q_i-contact of e_j is u_j. Let ell be the last index for which u_j lies in g_ell, and put
  S=(g_ell,...,g_{p_i}),
viewed as the suffix from u_j to the last vertex x_i.

Suppose for contradiction that Q_i and Q_j are vertex-disjoint. Then x_j is absent from S, Q_j is disjoint from S, and v is absent from both source rails. Therefore
  h_1,...,h_{p_j}, e_j, g_ell,...,g_{p_i}
is a linear path: Q_j ends at x_j, e_j joins x_j to u_j, and S begins at u_j; all other intersections are absent by the assumed disjointness and source cleanness.

Its length is
  p_j+1+(p_i-ell+1)
  >= p_j+2
  >= p_i+1,
because p_j>=p_i-1.

It ends at x_i, contradicting phi(x_i)=p_i.

Therefore Q_i and Q_j must intersect.

Since i,j were arbitrary, in every four-edge 0-1-1 violation the four chosen source-clean maximum rails are pairwise vertex-intersecting. Together with f8803379f9a3, they form a K4 intersection system in which at least one pair has at least two distinguished common vertices.