# For endpoint potential at least three, the weighted local snake defect is at least one

## Statement

Let H be a finite linear 3-graph and let v satisfy p=phi(v)>=3. Define
  a(v)=(2p-3)-t_ns(v),
  b(v)=(2p-1)-d_D^-(v).
Then
  (1/2)a(v)+b(v)>=1.

Equivalently, the two smallest possible local slack patterns (0,0) and (1,0) are both impossible.

## Body

The pattern (0,0) is excluded by 064168e95fae.

Suppose now for contradiction that a(v)=1 and b(v)=0. Then
  t_ns(v)=2p-4,
  d_D^-(v)=2p-1.

Choose any maximum p-edge path P ending at v. By the double-blocker compensation 3a0d8866aba9, b(v)=0 forces the chosen-path double-blocker count B_v=0. If the last edge h of P were nonspecial with v terminal, the stronger h-in-F case of 672725540541 would give
  t_ns(v)-D(v)<=2p-5,
where D(v)<=B_v=0. This contradicts t_ns(v)=2p-4. Hence every maximum p-edge path ending at v has a special last edge.

It follows that every nonspecial terminal edge e through v has rank at most p-1: if phi(e)=p, then because v is terminal for e there exists a p-edge path ending in e with last vertex v, which would be a maximum endpoint path with nonspecial last edge, contradiction.

Therefore all t_ns(v)=2p-4 nonspecial terminal edges through v have rank at most p-1. Apply the certified cumulative nonspecial-terminal bound 0e550ff0eadd with q=p-1>=2:
  t_ns(v)<=2(p-1)-3=2p-5,
again a contradiction.

Thus (1,0) is impossible. Since a(v),b(v) are nonnegative integers, every remaining pair satisfies (1/2)a(v)+b(v)>=1.