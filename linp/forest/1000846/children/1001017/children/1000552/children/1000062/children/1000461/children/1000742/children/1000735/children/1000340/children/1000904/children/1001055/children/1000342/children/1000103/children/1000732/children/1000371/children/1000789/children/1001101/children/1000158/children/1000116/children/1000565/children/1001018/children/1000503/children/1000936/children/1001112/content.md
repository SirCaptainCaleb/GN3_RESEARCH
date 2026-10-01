# Unique source-path intersections label fundamental-cycle neighbors by reciprocal terminals

## Statement

Let
  e={x,v,u}
be an ascending nonspecial edge of edge rank r, with unique entrance x and terminals v,u. Let f and g be ascending nonspecial edges such that f is terminal at v, g is terminal at u, and
  phi(f),phi(g)>=r.
Choose maximum endpoint paths R_e,R_f,R_g ending at the unique entrances of e,f,g respectively, each avoiding the two terminals of its last edge.

Assume
  V(R_e) intersect V(R_f)={s_f},
  V(R_e) intersect V(R_g)={s_g}.
Then:
(1) u belongs to V(R_f);
(2) v belongs to V(R_g).

More precisely, R_f must meet e at u rather than x, and R_g must meet e at v rather than x. Consequently, when f and g are the two fundamental-cycle neighbors of a minimum-edge-rank nonforest chord e, the hard unique-intersection residual has exact reciprocal-terminal labels on the two neighboring source paths.

## Body

Because e and f are ascending nonspecial edges terminal at the common vertex v and phi(e)<=phi(f), downward completeness of the maximum source path R_f gives
  R_f intersects {x,u}.
The path R_f avoids v.

Suppose x belongs to R_f. Since R_e ends at x, x belongs to V(R_e) intersect V(R_f). But the intersection is assumed to be the singleton {s_f}. Thus s_f=x. This is impossible by the unique-intersection theorem 5854d853a44b: the unique common vertex of two maximum endpoint paths ending at distinct vertices must be an internal aligned joint on both paths, whereas x is the last vertex of R_e. Therefore x is not on R_f, and the forced contact is
  u in V(R_f).

The proof for g is symmetric. The edges e and g are terminal at the common vertex u and phi(e)<=phi(g), so R_g must meet {x,v}. If it met x, the unique intersection R_e intersect R_g would be the last vertex x of R_e, again contradicting 5854d853a44b. Hence
  v in V(R_g).

In the maximum-rank-forest setting, minimum edge rank of e on its fundamental cycle gives phi(f),phi(g)>=phi(e), so the hypotheses apply automatically to the two cycle neighbors.
