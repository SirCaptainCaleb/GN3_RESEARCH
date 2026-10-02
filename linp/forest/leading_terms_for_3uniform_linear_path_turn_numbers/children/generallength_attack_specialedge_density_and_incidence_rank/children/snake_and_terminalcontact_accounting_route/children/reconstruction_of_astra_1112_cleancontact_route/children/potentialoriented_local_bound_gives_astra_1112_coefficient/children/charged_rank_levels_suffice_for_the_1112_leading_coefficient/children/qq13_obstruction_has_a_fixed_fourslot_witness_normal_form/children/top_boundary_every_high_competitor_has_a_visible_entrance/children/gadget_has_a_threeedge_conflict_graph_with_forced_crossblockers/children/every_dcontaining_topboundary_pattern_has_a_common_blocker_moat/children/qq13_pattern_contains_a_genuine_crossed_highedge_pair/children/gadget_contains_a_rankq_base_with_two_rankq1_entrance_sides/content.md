# Every top-boundary critical gadget contains a rank-q base with two rank-(q+1) entrance sides

## Statement

In the half-rank top-boundary q,(q+1)^3 configuration, q>=4, let
  P=(g_1,...,g_{2q-2})
be maximum at v and
  x=g_{q-1}∩g_q
the universal entrance of the low rank-q edge.

Then
  phi(g_{q-1})=phi(g_q)=q,
and both g_{q-1},g_q are ascending nonspecial edges with unique entrance x.

Writing
  g_{q-1}={x,a,b},
  g_q={x,c,d},
the three high entrances occupy three of {a,b,c,d}. Therefore at least one of the pairs {a,b}, {c,d} is fully occupied.

Consequently the critical gadget contains a linear 3-cycle
  g_*, h_r, h_s
where g_* has rank q and unique entrance x, while h_r,h_s have rank q+1, share the common terminal v, and their respective entrances r,s are exactly the two terminal vertices of g_*.

## Body

Because x lies on g_{q-1}, the incidence inequality gives
  phi(g_{q-1})<=phi(x)+1=q.
On the other hand the prefix
  g_1,...,g_{q-1}
has q-1 edges and can end physically at x, while adjoining the low edge e gives a q-edge witness through x; equivalently the path-position lower bound on g_{q-1} yields phi(g_{q-1})>=q. Hence phi(g_{q-1})=q.
The same argument, reversing the suffix side of the maximum path around the central joint x, gives phi(g_q)>=q, while the same incidence inequality gives phi(g_q)<=q. Thus phi(g_q)=q.

At an incidence x∈g with phi(g)=phi(x)+1, the certified incidence-defect characterization says g is ascending nonspecial and x is its unique entrance. Thus both central edges are rank-q ascending with entrance x.

Now
  g_{q-1}={x,a,b},
  g_q={x,c,d}.
The all-visible normal form says the three high entrances are three distinct vertices among a,b,c,d. By pigeonhole, at least one side pair {a,b} or {c,d} is fully occupied.

Suppose for instance a,b are occupied, with
  h_a={a,v,z_a}, h_b={b,v,z_b}.
Then
  g_{q-1}∩h_a={a},
  g_{q-1}∩h_b={b},
  h_a∩h_b={v},
and these three joints are distinct. Hence the three edges form a linear 3-cycle. The c,d case is identical.