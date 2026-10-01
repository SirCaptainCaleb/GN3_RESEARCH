# At the half-rank boundary a charged low-rank edge has a universal central-joint witness

## Statement

Let v have phi(v)=2q-2 and let e={x,v,u} be a potential-charged ascending nonspecial edge of rank q with v terminal. Then on every maximum (2q-2)-edge path P=(g_1,...,g_{2q-2}) ending at v, the path-relative witness for e is the unique central joint g_{q-1}∩g_q. Hence either the entrance x is that central joint (if x lies on P) or the opposite terminal u is that central joint (if x is absent).

## Body


Let v have endpoint potential p=2q-2, and let e={x,v,u} be a potential-charged ascending nonspecial edge of rank q, with v terminal and phi(u)>=p.

Fix any p-edge path
  P=(g_1,...,g_p)
ending physically at v.

Apply the path-relative witness localization 220a14637b5f to e on P with Q=q. For a rank-q edge, every possible private witness lies in positions
  p-q+2,...,q-1,
and every possible joint witness lies in positions
  p-q+1,...,q-1.

Substituting p=2q-2 gives
  private positions: q,...,q-1, hence none;
  joint positions:   q-1,...,q-1, hence exactly one.

Therefore the selected witness of e on P is forced to be
  c(P):=g_{q-1} cap g_q.

By the witness construction, this selected witness is x if the entrance x lies on P, and otherwise is the opposite terminal u. Thus for every maximum p-edge path P ending at v,
  c(P) in {x,u},
and more precisely:
- if x in V(P), then x=c(P);
- if x notin V(P), then u=c(P).

So every maximum v-path places one of the two non-v vertices of e at the unique central joint, with no private-slot alternative.
