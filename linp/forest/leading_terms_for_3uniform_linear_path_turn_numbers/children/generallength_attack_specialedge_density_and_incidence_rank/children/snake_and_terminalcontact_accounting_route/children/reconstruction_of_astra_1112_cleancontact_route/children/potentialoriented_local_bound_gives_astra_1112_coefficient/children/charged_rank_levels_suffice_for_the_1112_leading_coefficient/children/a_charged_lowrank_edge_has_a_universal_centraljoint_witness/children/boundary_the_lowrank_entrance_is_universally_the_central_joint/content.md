# At the half-rank boundary the low-rank entrance is universally the central joint

## Statement

Let v have phi(v)=2q-2 and let
  e={x,v,u}
be a potential-charged ascending nonspecial edge of rank q with v terminal. Then for every maximum (2q-2)-edge path
  P=(g_1,...,g_{2q-2})
ending physically at v,
  x=g_{q-1}∩g_q.

In particular the opposite-terminal witness alternative in 351720508b02 never occurs.

## Body

By 351720508b02, the unique central joint
  c=g_{q-1}∩g_q
is either x or u. Suppose for contradiction that c=u, so x is absent from P.

Because P ends physically at v, the vertex v occurs only in the final edge g_{2q-2}. Hence the prefix
  (g_1,...,g_{q-1})
avoids v. It also avoids x by assumption. Its last edge g_{q-1} contains u=c.

Therefore
  (g_1,...,g_{q-1},e)
is a linear q-edge path: the only intersection of e with the prefix is u on its final edge. The last edge e is entered through u, while x is a distinct vertex of e, so x can be chosen as the physical last vertex. Thus
  phi(x)>=q.

But e is ascending of rank q with unique entrance x, so
  phi(x)=q-1,
a contradiction.

Hence c=x on every maximum path ending at v.