# The rising low-terminal branch has a pure four-slot cross-cut entrance gadget

## Statement

In the rising low-terminal branch of d734b1420b2f, let
  R=(r_1,...,r_{2q-2})
be the chosen maximum C-ending path with
  x=r_{q-1}∩r_q,
and let h_i={y_i,v,z_i}, i=1,2,3, be the three rank-(q+1) high edges. Then each entrance y_i belongs to exactly one of the four central slots
  L=r_{q-2}∩r_{q-1},
  A=private(r_{q-1}),
  B=private(r_q),
  R'=r_q∩r_{q+1}.
The central joint x itself is impossible.

The three entrances are distinct, so they occupy three of these four slots. For each high edge, its opposite terminal z_i lies on the half of R opposite its entrance.

## Body

By d734b1420b2f, each high edge h_i has exactly one non-v vertex on the left half r_1,...,r_{q-1} and exactly one on the right half r_q,...,r_{2q-2}. These two vertices are y_i and z_i.

Since h_i is ascending of rank q+1,
  phi(y_i)=q.
Apply the position-sensitive endpoint-potential bound to y_i on the (2q-2)-edge path R.

If y_i is private in r_j, then
  phi(y_i)>=max{j,(2q-2)-j+1}=max{j,2q-1-j}.
For this to be at most q, one must have
  q-1<=j<=q.
Thus the only private possibilities are A=private(r_{q-1}) and B=private(r_q).

If y_i=r_j∩r_{j+1} is a joint, then
  phi(y_i)>=max{j,(2q-2)-j}.
For this to be at most q,
  q-2<=j<=q.
The three joint possibilities are
  L=r_{q-2}∩r_{q-1},
  x=r_{q-1}∩r_q,
  R'=r_q∩r_{q+1}.

But h_i and the low edge e={x,v,C} already share v. If h_i also contained x, the two hyperedges would share {v,x}, violating linearity. Hence y_i≠x.

Therefore y_i lies in {L,A,B,R'}.

Distinct high edges through v have disjoint non-v pairs, so their entrances y_i are distinct. Hence three of the four slots are occupied.

Finally d734b1420b2f says h_i has one non-v vertex in each half. Since y_i lies on one half, its other non-v vertex z_i lies on the opposite half.
