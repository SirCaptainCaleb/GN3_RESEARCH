# Half-rank charged edges are reciprocally central at both terminals

## Statement

If e={x,v,u} is ascending nonspecial of rank q, charged at terminal v with phi(v)=2q-2 and phi(u)>=phi(v), then phi(u)=phi(v)=2q-2. Consequently the central-joint localization of 351720508b02 applies symmetrically at both terminals: every maximum (2q-2)-edge path ending at v or u has the witness for e at its unique central joint.

## Body

Retain the setting of 351720508b02:
  e={x,v,u}
is a potential-charged ascending nonspecial edge of rank q,
  phi(v)=2q-2,
v is terminal, and phi(u)>=phi(v).

The certified terminal-potential bound a7b7670e955a for an ascending rank-q edge gives
  phi(u)<=2q-2
and
  phi(v)<=2q-2.
Therefore
  phi(u)=phi(v)=2q-2.

Now apply 351720508b02 first at terminal v and then symmetrically at terminal u. For every maximum (2q-2)-edge path P_v ending physically at v, the selected witness of e is the unique central joint
  c_v=g_{q-1} cap g_q,
which is x if x lies on P_v and otherwise u.

Likewise, for every maximum (2q-2)-edge path P_u ending physically at u, the selected witness of e is the unique central joint
  c_u=h_{q-1} cap h_q,
which is x if x lies on P_u and otherwise v.

Thus the half-rank boundary is reciprocal: both terminals have the same extremal potential and every maximum endpoint path at either terminal places one of the other two vertices of e at its unique central joint.
