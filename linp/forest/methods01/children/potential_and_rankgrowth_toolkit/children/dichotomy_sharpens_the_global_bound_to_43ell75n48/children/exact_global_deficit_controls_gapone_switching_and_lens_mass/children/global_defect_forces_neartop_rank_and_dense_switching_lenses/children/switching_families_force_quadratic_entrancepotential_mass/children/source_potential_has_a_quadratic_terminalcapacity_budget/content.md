# Ascending source potential has a quadratic terminal-capacity budget

## Statement

Let H be a finite linear 3-graph. For each ascending nonspecial edge e={x,u,v}, let x be its unique entrance. Then
  2 sum_{e ascending} phi(x)
  <= sum_{y in V(H)} (phi(y)-1) max(0,2phi(y)-3).
In particular, if phi(y)>=2 on every nonisolated vertex, then
  2 sum_{e ascending} phi(x)
  <= sum_y (phi(y)-1)(2phi(y)-3).

Consequently, for any simultaneously chosen center-indexed switching families F_v,
  sum_v sum_{f in F_v} phi(x_f)
  <= sum_y (phi(y)-1) max(0,2phi(y)-3).

## Body

Orient every ascending nonspecial edge e={x,u,v}, with unique entrance x, by the two arcs x->u and x->v.

For an arc x->y coming from an ascending edge of rank r=phi(e), ascendingness gives
  phi(x)=r-1,
while y is a terminal of e and therefore
  phi(y)>=r.
Hence
  phi(x)<=phi(y)-1.                                    (1)

Let d_in(y) be the indegree of y in this auxiliary digraph. It is exactly the number of ascending nonspecial edges for which y is a terminal. This is at most the total number of nonspecial terminal incidences at y. By the certified cumulative terminal bound 0e550ff0eadd,
  d_in(y)<=max(0,2phi(y)-3).                           (2)

Each ascending hyperedge contributes two arcs, both carrying source weight phi(x). Therefore
  2 sum_{e ascending}phi(x)
   = sum_{arcs x->y} phi(x)
   <= sum_{arcs x->y}(phi(y)-1)
   = sum_y (phi(y)-1)d_in(y)
   <= sum_y (phi(y)-1)max(0,2phi(y)-3),
proving the first assertion.

For the switching-family consequence, an ascending hyperedge has exactly two terminal vertices, so it can belong to center-indexed switching families at at most two centers. Thus
  sum_v sum_{f in F_v}phi(x_f)
  <=2 sum_{e ascending}phi(x_e),
and the preceding estimate applies.