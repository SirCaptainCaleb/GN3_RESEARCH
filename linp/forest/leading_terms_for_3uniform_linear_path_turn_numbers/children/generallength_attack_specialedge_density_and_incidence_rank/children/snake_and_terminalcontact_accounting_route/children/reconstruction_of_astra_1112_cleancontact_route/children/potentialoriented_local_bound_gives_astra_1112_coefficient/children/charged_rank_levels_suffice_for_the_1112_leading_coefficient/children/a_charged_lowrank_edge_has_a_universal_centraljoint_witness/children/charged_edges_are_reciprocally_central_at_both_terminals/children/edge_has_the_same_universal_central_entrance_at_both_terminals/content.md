# A half-rank charged edge has the same universal central entrance at both terminals

## Statement

Let e={x,u,v} be an ascending nonspecial edge of rank q, with unique entrance x. Suppose
  phi(u)=phi(v)=2q-2.
Then for every maximum (2q-2)-edge path ending physically at either terminal u or v, the unique central joint is x.

Equivalently, if
  P_v=(g_1,...,g_{2q-2})
ends at v, then
  x=g_{q-1}∩g_q,
and if
  P_u=(h_1,...,h_{2q-2})
ends at u, then
  x=h_{q-1}∩h_q.

## Body

Since phi(u)=phi(v), the edge e is potential-charged at both terminals.

Apply cf6ab8703be5 to e viewed as charged at terminal v. It gives that on every maximum (2q-2)-edge v-ending path, the universal central joint is the unique entrance x.

Now interchange u and v. The hypotheses are unchanged: e is still ascending nonspecial of rank q with unique entrance x, u is a terminal of endpoint potential 2q-2, and the opposite terminal v has potential at least phi(u) (indeed equality). Applying cf6ab8703be5 again gives that on every maximum u-ending path the central joint is also x.

Thus the same low-potential entrance x is universally pinned at the middle of both terminal endpoint-path systems.