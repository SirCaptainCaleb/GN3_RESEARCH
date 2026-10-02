# The top-boundary q,(q+1)^3 obstruction has a fixed four-slot witness normal form

## Statement

Let v have p=phi(v)=2q-2, q>=3. Suppose four potential-charged ascending nonspecial edges are terminal at v with ranks
  q,q+1,q+1,q+1.
Let e={x,v,u} be the rank-q edge. Fix any maximum p-edge path
  P=(g_1,...,g_{2q-2})
ending at v.

Put
  a=g_{q-2}∩g_{q-1},
  b=private(g_{q-1}),
  x=g_{q-1}∩g_q,
  c=private(g_q),
  d=g_q∩g_{q+1}.

Then x is the universal entrance of e. The three rank-(q+1) competitors admit distinct path-relative witnesses occupying three of the four vertices {a,b,c,d}. Moreover any witness equal to c or d is necessarily the unique entrance of its rank-(q+1) edge. Terminal-only witnesses are possible only at a or b.

In particular at least one rank-(q+1) competitor has a visible entrance in {c,d}, of potential q.

## Body

The universal central entrance x=g_{q-1}∩g_q for the rank-q edge is cf6ab8703be5.

Apply the path-relative witness localization 220a14637b5f to each rank-(q+1) competitor on P, whose length is r=2q-2. The possible witness positions for rank Q=q+1 are:
- private positions r-Q+2 through Q-1, namely q-1 through q;
- joint positions r-Q+1 through Q-1, namely q-2 through q.
Thus every selected witness lies among the five vertices
  a,b,x,c,d.

The rank-q edge contains x and v. Every competitor also contains v. By linearity no competitor can contain x, for otherwise it would share both v and x with e. Hence the three high-edge witnesses lie in {a,b,c,d}. Distinct competitors through v have disjoint non-v pairs, so their selected witnesses are distinct. Therefore they occupy three of those four slots.

It remains to label terminal-only witnesses. Let h={y,v,z} have rank q+1, with entrance y absent from P, and let z be its selected opposite-terminal witness.

If z is private in g_i, terminal-tail localization gives
  i>=r-(q+1)+2=q-1.
Because y is absent, the prefix g_1,...,g_i,h enters h through the wrong terminal z. Since h is nonspecial of rank q+1, this path has at most q edges, so i+1<=q and i<=q-1. Hence i=q-1, so the only private terminal witness is b.

If z is the joint g_i∩g_{i+1}, terminal-tail localization gives
  i>=r-(q+1)+1=q-2,
while the same wrong-entrance prefix has length i+1<=q, so i<=q-1. Thus the only possible joint terminal witnesses are a (i=q-2) and x (i=q-1). But x is unavailable by linearity with the low edge e. Hence only a remains.

Therefore c and d can only be entrance witnesses. Since three of four outer slots are occupied, at least one of c,d is occupied, giving a visible rank-(q+1) entrance there. Ascendingness gives its endpoint potential q.