# Every high entrance rail in the critical two-rank pattern crosses the low edge

## Statement

Let
  e={x,v,u}
be an ascending nonspecial edge of rank q with unique entrance x. Let
  h={y,v,z}
be a distinct ascending nonspecial edge of rank q+1 through the same terminal v.

Let
  R=(r_1,...,r_q)
be a canonical q-edge entrance path ending physically at y such that
  R,h
is a longest (q+1)-edge path ending in h through its unique entrance y; in particular R avoids the terminals v,z.

Then
  V(R)∩{x,u} is nonempty.

Consequently, in a q,(q+1)^3 configuration, the three canonical entrance rails of the high edges each cross the two-vertex gate {x,u}; hence two of the three rails cross the same gate vertex.

## Body

Suppose R avoided both x and u. By construction it also avoids v and z. Since h and e are distinct edges through v, linearity gives
  h∩e={v}.
The last edge r_q of R meets h at y, and R is disjoint from e.

Therefore
  (r_1,...,r_q,h,e)
is a linear path of length q+2. Its last edge is e. This contradicts
  phi(e)=q.

Hence R contains x or u. The final pigeonhole statement is immediate for three high rails and the two possible gate vertices.