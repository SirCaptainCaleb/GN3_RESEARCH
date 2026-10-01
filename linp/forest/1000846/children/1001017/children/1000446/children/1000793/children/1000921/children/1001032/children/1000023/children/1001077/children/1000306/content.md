# Minimum-potential equality is a 3-regular special core plus an all-ascending remainder

## Statement

Assume H satisfies phi(v)>=2 for every vertex and equality in eeb9576892:
  sum_v phi(v)=m+n.
Then every vertex lies in exactly three special hyperedges. Consequently the special-edge subhypergraph is 3-uniform and 3-regular, and the number s of special edges equals n.

Moreover every nonspecial edge is ascending. In particular, if m=dn then H has exactly n special edges and (d-1)n nonspecial edges, all of the latter ascending.

## Body

Equality in eeb9576892 forces, at every vertex v,
  delta_ns(v)=1, delta_sn(v)=0,
where
  delta_ns(v)=(2phi(v)-3)-t_ns(v),
  delta_sn(v)=(2phi(v)-1)-d_D^-(v).
Thus
  t_ns(v)=2phi(v)-4
and
  d_D^-(v)=2phi(v)-1.

The total snake indegree at v is the number t_ns(v) of nonspecial terminal incidences plus the number s_v of special edges containing v. Therefore
  s_v=d_D^-(v)-t_ns(v)=3.
So every vertex belongs to exactly three special edges.

Since the special-edge subhypergraph is 3-uniform and every vertex has special degree three,
  3s=3n,
hence s=n.

Now use ascending-edge accounting 419519f0efa5:
  3m-A <= sum_v(2phi(v)-1).
Under sum_v phi(v)=m+n, the right side is
  2m+n.
Hence
  A>=m-n.

But the number of nonspecial edges is
  m-s=m-n.
Every ascending edge is nonspecial, so A<=m-s=m-n. Therefore
  A=m-n,
and every nonspecial edge is ascending.

At exact density m=dn this becomes
  s=n,
  m-s=(d-1)n,
  A=(d-1)n.
Thus the equality configuration decomposes exactly into a 3-regular special core and an all-ascending nonspecial remainder.
