# The rising low-terminal branch recreates an all-visible four-slot crossed-chord gadget

## Statement

Retain the rising branch of d734b1420b2f. Thus
  e={x,v,C}
has rank q,
  phi(C)=2q-2,
and the chosen maximum C-ending path is
  R=(r_1,...,r_{2q-2}),
with
  x=r_{q-1}∩r_q
the sole e-contact and v absent.

Let
  h_i={y_i,v,z_i}, i=1,2,3,
be the three rank-(q+1) 0-1-1 high edges. Then their entrances y_i are three distinct vertices among the four slots
  a=r_{q-2}∩r_{q-1},
  b=private(r_{q-1}),
  c=private(r_q),
  d=r_q∩r_{q+1}.
Moreover:
- if y_i∈{a,b}, then z_i lies in the right half V(r_q∪...∪r_{2q-2});
- if y_i∈{c,d}, then z_i lies in the left half V(r_1∪...∪r_{q-1}).

Thus the three high edges form an all-visible three-of-four central entrance gadget, and each is a two-contact chord crossing the central cut.

## Body

By d734b1420b2f, every h_i meets each half of R exactly once, using its two non-v vertices y_i,z_i.

Since h_i is ascending of rank q+1, its unique entrance satisfies
  phi(y_i)=q.
Apply the position-sensitive endpoint-potential bound 8b1790d79d74 to the (2q-2)-edge path R.

If y_i is private in r_j, then
  q=phi(y_i)>=max{j,2q-1-j},
so j∈{q-1,q}.

If y_i=r_j∩r_{j+1}, then
  q>=max{j,2q-2-j},
so j∈{q-2,q-1,q}.

The central joint with j=q-1 is x. But h_i and e are distinct edges through v, so h_i cannot also contain x; otherwise they share {v,x}. Hence y_i lies in exactly one of the four displayed outer slots a,b,c,d.

Distinct high edges through v have disjoint non-v pairs by linearity, so their entrances are distinct. Hence the three y_i occupy three of the four slots.

Finally d734b1420b2f says each h_i has one contact in each half. If y_i is in the left pair {a,b}, its other non-v vertex z_i must be the right-half contact. If y_i is in the right pair {c,d}, z_i must be the left-half contact.
