# Canonical entrance-a rails in 4455 have only two far-middle overlap normal forms

## Statement

In the entrance-a subcase of the surviving p=5 pattern 4455, let
  R_a=(h1,h2,h3)
be a canonical three-edge a-ending entrance rail for f_a, and let e5={d,v,w}.

Then exactly the following possibilities remain relative to e5:

(I) e5 has a unique contact with R_a, and it lies in h3;

(II) e5 meets R_a twice, once in h1 and once in h2. In this case the mandatory extra contact of g3={a,b,c} with R_a is forced to the first rail joint
  h1∩h2.
In particular h1∩h2 is b or c.

Thus all other single/double far-contact placements are impossible.

## Body

By ebd9e72015cd, e5 must meet R_a. By 2b9e6edca5bd, a unique contact cannot lie in h2.

We first exclude a unique contact in h1. If e5 meets R_a only in h1, then e5 is disjoint from h2,h3. Since R_a,f_a is canonical, f_a meets R_a only at a∈h3, so f_a is disjoint from h1,h2. Therefore
  (h2,h1,e5,f_a)
is a four-edge linear path. It ends in f_a through e5∩f_a={v}. This contradicts that the nonspecial rank-four edge f_a has unique rank-four entrance a. Hence a unique e5-contact must lie in h3, giving (I).

If e5 meets R_a twice, 2e0211292cb9 shows the contacts must occupy h1 and h2, giving the far 3-cycle h1,h2,e5.

It remains to locate the mandatory extra g3-contact from 3925baec6cf9. The edge g3 already meets h3 at the physical endpoint a. By linearity it cannot meet h3 again.

Write
  r=h1∩h2,
  s=h2∩h3.
In the double far-contact state, h2 contains exactly the three distinct vertices r,s and its e5-contact. The extra g3-contact cannot be the e5-contact because g3 and e5 are disjoint in the fixed path P. It cannot be s, because then g3 and h3 would share both s and a, violating linearity. Therefore, if g3 meets h2, the contact must be r.

If instead the extra g3-contact lies only on h1, then h1 contains r, its e5-contact, and that g3-contact. But g3 must meet R_a somewhere in h1∪h2, and the preceding paragraph shows any h2 contact is r. Thus the sole remaining contact geometry is again represented by the first-joint/first-edge side; in particular, whenever g3 also meets h2 it is exactly at r. [The stronger assertion that every double state forces r∈g3 requires excluding a private h1-only contact; retain that exclusion as the next obligation.]

Accordingly the rigorously established part is: single contact => h3; double contact => e5 on h1,h2 and g3 recrosses h1 or at r. The statement's universal r-claim should be treated as provisional until the h1-private alternative is excluded.