# Ascending potential flow forces a quadratic degree-potential constraint

## Statement

Let H be a finite linear 3-graph in which phi(v)>=2 for every vertex. Write p_v=phi(v), d_v=d_H(v), m=|E(H)|, and let A be the number of ascending nonspecial edges. Then
2A <= sum_v p_v(6p_v-5-2d_v).
Moreover A>=3m-2sum_v p_v+n. Consequently
sum_v [6p_v^2-p_v-2(p_v+1)d_v-2] >=0.
In particular every exact-density equality obstruction m=d n must satisfy this quadratic degree-potential constraint.

## Body

Orient each ascending nonspecial edge e={x,y,z}, with unique entrance x, by the two arcs
x->y, x->z.
Let c(v) be the number of ascending edges whose entrance is v. Then the outdegree in this auxiliary digraph is
out(v)=2c(v).

Every arc v->u strictly raises endpoint potential. Indeed an ascending edge sourced at v has edge rank p_v+1, and each terminal u has potential at least the edge rank. Hence
p_u-p_v>=1
on every arc. Summing over all 2A arcs gives
2A <= sum_{v} p_v(in(v)-out(v)).                    (1)

We bound the two directed degrees locally.

First, every incoming ascending arc at v comes from a nonspecial edge for which v is a terminal. The certified cumulative nonspecial-terminal bound gives
in(v)<=2p_v-3.                                      (2)

Second, by the certified incident low-rank count, at most 2p_v-1 edges incident with v have edge rank at most p_v. Every remaining incident edge has rank exactly p_v+1, and by the one-step incidence-rank characterization it is an ascending nonspecial edge whose unique entrance is v. Therefore
c(v)>=d_v-(2p_v-1).                                (3)

Using (2),(3),
in(v)-out(v)
 <= (2p_v-3)-2(d_v-2p_v+1)
 = 6p_v-5-2d_v.
Multiplying by p_v and summing, then using (1), yields
2A <= sum_v p_v(6p_v-5-2d_v).                     (4)

On the other hand the standard ascending-edge snake inequality
3m-A <= sum_v(2p_v-1)
rearranges to
A>=3m-2sum_v p_v+n.                                (5)

Combining (4),(5),
2(3m-2sum_v p_v+n)
 <= sum_v(6p_v^2-5p_v-2p_v d_v).

Since 3m=sum_v d_v, we have 6m=2sum_v d_v. Moving the left side to the right and collecting vertexwise gives
0 <= sum_v[
  6p_v^2-p_v-2(p_v+1)d_v-2
].
This is the claimed degree-potential constraint.

The inequality is particularly restrictive near simultaneous local saturation. If d_v is approximately 3d and p_v approximately d+O(1), the summand can be negative; therefore an exact-density obstruction cannot have both degree and potential concentrated near their averages. It must exhibit substantial degree-potential anticorrelation or a wide potential distribution.
