# Half-rank boundary edges have reciprocal central-joint constraints at both terminals

## Statement

Let e={x,u,v} be ascending nonspecial of rank q, with unique entrance x. Suppose
  phi(u)=phi(v)=2q-2.
Then for every maximum (2q-2)-edge path P_v ending at v, its unique central joint
  c_v=g_{q-1}∩g_q
lies in {x,u}; and for every maximum (2q-2)-edge path P_u ending at u, its unique central joint lies in {x,v}.

Equivalently, if a maximum v-ending path avoids the entrance x, then u is its central joint; if a maximum u-ending path avoids x, then v is its central joint.

## Body

Since e has rank q and is ascending, phi(x)=q-1. At terminal v we have phi(v)=2q-2 and the opposite terminal u has phi(u)=2q-2>=phi(v), so e is potential-charged at v. Apply 351720508b02 to obtain the first central-joint conclusion.

Symmetrically, e is potential-charged at u because phi(v)=phi(u). Applying 351720508b02 with u and v interchanged gives the second conclusion.
