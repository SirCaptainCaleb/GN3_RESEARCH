# Equality in the U_11 collision rank-sum bound has an exact central normal form

## Statement

Retain an interior U_11 color-terminal collision x_i=v_j on a rainbow terminal-pair path with nondecreasing parent edge ranks. Let
  R_i=(g_1,...,g_{r_i-1})
be the chosen maximum path with last vertex x_i, and let c_j,c_{j+1} be the exact contacts of E_j,E_{j+1} with R_i.

Assume the minimum possible adjacent rank sum occurs:
  r_j+r_{j+1}=r_i+2.

Then the collision is of the local linear 3-cycle type, and the following more precise alternatives hold.

(Even owner rank.) If r_i=2q, then
  r_j=r_{j+1}=q+1.
The only possible contact vertices for either edge are
  g_{q-1} intersect g_q,
  the private vertex of g_q,
  g_q intersect g_{q+1}.
Thus c_j and c_{j+1} are two distinct vertices of g_q, and
  g_q,E_j,E_{j+1}
is the local linear 3-cycle.

(Odd owner rank.) If r_i=2q+1, then
  r_j=q+1,   r_{j+1}=q+2.
Moreover
  c_j=g_q intersect g_{q+1}.
The other exact contact c_{j+1} is one of
  g_{q-1} intersect g_q,
  the private vertex of g_q,
  the private vertex of g_{q+1},
  g_{q+1} intersect g_{q+2}.
Accordingly the local linear 3-cycle uses host edge g_q or g_{q+1}.

## Body

By 867efd696575,
  r_j >= ceil((r_i+1)/2)
and
  r_{j+1} >= ceil((2r_i+3)/4).
Since r_j+r_{j+1}=r_i+2, equality must hold in these lower bounds.

If r_i=2q, both lower bounds equal q+1, so
  r_j=r_{j+1}=q+1.
The host path R_i has length p=2q-1. Apply the exact singleton window of 49080cbf1371 at rank q+1. Its eligible private positions satisfy
  p-(q+1)+2 <= t <= q,
so t=q, giving only the private vertex of g_q. Its eligible joint positions satisfy
  p-(q+1)+1 <= t <= q,
so t is q-1 or q, giving the two joints adjacent to g_q. Hence both exact contacts lie among precisely the three vertices displayed in the statement. They are distinct by 608468bb403b, so they lie together on g_q. Therefore g_q,E_j,E_{j+1} is the local linear 3-cycle.

Now let r_i=2q+1. Equality in the ordered lower bounds gives
  r_j=q+1, r_{j+1}=q+2.
Here R_i has length p=2q. For rank q+1, the singleton window has no eligible private vertex and exactly one eligible joint, namely
  g_q intersect g_{q+1}.
Thus c_j is that joint.

For rank q+2, the eligible private vertices are the private vertices of g_q and g_{q+1}, while the eligible joints are
  g_{q-1} intersect g_q,
  g_q intersect g_{q+1},
  g_{q+1} intersect g_{q+2}.
Since exact contacts of E_j and E_{j+1} are distinct, c_{j+1} is not the middle joint c_j, leaving the four displayed possibilities. In the first two cases both contacts lie on g_q; in the last two they lie on g_{q+1}. The local 3-cycle assertion follows from 3216d2e9afcd.