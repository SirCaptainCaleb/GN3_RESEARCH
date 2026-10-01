# Minimum-potential equality forces two-step ascent on every nonspecial edge

## Statement

Assume the minimum-potential equality setting of 41d502ff7771: sum_v phi(v)=m+n. Then:

1. For every vertex v with p=phi(v), every maximum p-edge path ending at v has a special last edge.

2. Every nonspecial edge e is ascending, and if q=phi(e) with unique entrance x and terminals u,v, then
   phi(x)=q-1,
   phi(u)>=q+1,
   phi(v)>=q+1.
Equivalently every entrance-to-terminal arc in the auxiliary DAG raises endpoint potential by at least two.

In particular no nonspecial edge has rank equal to the endpoint potential of either terminal.

## Body

Fix a vertex v and put p=phi(v). By 41d502ff7771,
  d_D^-(v)=2p-1
and
  t_ns(v)=2p-4.

Choose an incoming snake edge h at v of maximum terminal rank t=phi(h,v), and let P be a t-edge path witnessing it, ending with h at v.

The snake-indegree proof d4e8b1c27a65 gives
  d_D^-(v)-1 <= 2(t-1).
Since d_D^-(v)=2p-1 and t<=phi(v)=p, equality forces t=p.

Moreover, the proof gives that every other incoming edge f at v meets V(P)\h. There are exactly
  2p-2
other incoming edges and exactly
  |V(P)\h|=2p-2
vertices there.

All incoming edges at v share v. By linearity, their contact sets with V(P)\h are pairwise disjoint. Since every one of the 2p-2 other incoming edges has at least one contact in a set of size 2p-2, each has exactly one contact and these contacts partition V(P)\h.

Suppose h were nonspecial. Because P ends in h at last vertex v, v is a terminal of h, so h is counted among the nonspecial terminal edges at v. The certified saturation lemma 672725540541 says, in the case h is nonspecial,
  t_ns(v)-D(v) <= 2p-5,
where D(v) counts other nonspecial terminal edges having both non-v vertices in V(P)\h.
Since t_ns(v)=2p-4, this forces D(v)>=1.

But exact snake saturation above showed every other incoming edge, hence every other nonspecial terminal edge, has exactly one contact with V(P)\h. Therefore D(v)=0, contradiction.

So h must be special.

Now take any maximum p-edge path ending at v. Its last edge is an incoming snake edge at v of terminal rank p, hence it is itself a maximum-rank incoming edge and the preceding argument applies. Thus every maximum endpoint path at v has special last edge.

Finally let e={x,u,w} be nonspecial. By 41d502ff7771 every nonspecial edge is ascending, so if q=phi(e),
  phi(x)=q-1,
while terminal potentials satisfy phi(u),phi(w)>=q in general.

If phi(u)=q, then a q-edge path ending in e with last vertex u is a maximum phi(u)-edge path ending at u whose last edge e is nonspecial, contradicting the result just proved. Hence phi(u)>=q+1, and similarly phi(w)>=q+1.

Therefore each auxiliary arc from the entrance x to either terminal raises potential by at least two.
