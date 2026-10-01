# In the rising low-terminal branch the three high edges are disjoint two-sided chords

## Statement

Retain the surviving one-low odd-central 0-1-1 state, with low edge
  e={x,v,C}
of rank q, where phi(v)=2q-3 and C is the sole P_v-contact. Suppose the opposite terminal rises:
  phi(C)=2q-2.

Let
  R=(r_1,...,r_{2q-2})
be the globally chosen maximum C-ending path. By 436d55f14de2,
  x=r_{q-1}∩r_q
is the sole e-contact on R, and v is absent from R.

Let h_1,h_2,h_3 be the three rank-(q+1) 0-1-1 high edges through v. Then every h_i meets each of the two halves
  R_L=(r_1,...,r_{q-1}),
  R_R=(r_q,...,r_{2q-2}).

Moreover h_i contains exactly one non-v vertex in R_L and exactly one non-v vertex in R_R. Thus the three high edges form three pairwise vertex-disjoint two-sided chords across the central cut of R.

## Body

Fix a high edge h={y,v,z}.

Because h and e are distinct edges through v, linearity gives h∩e={v}; hence h does not contain x or C.

Suppose h were disjoint from the left half R_L. Since R_L ends at x (the next edge r_q is omitted), the sequence
  r_1,...,r_{q-1}, e, h
is linear: R_L meets e only at x; e meets h only at v; and h is disjoint from R_L by assumption. It has
  (q-1)+2=q+1
edges and ends in h through terminal v.

But h is nonspecial of rank q+1 with unique entrance y≠v. This is a longest h-path with wrong entrance, contradiction. Therefore h meets R_L.

The same argument applies to the right half in reverse. The sequence
  r_{2q-2},r_{2q-3},...,r_q,e,h
has q+1 edges and is linear if h misses R_R: the reversed half ends at x, then e is entered through x and h through v. Thus h must also meet R_R.

The two halves intersect only in the vertex x, and h cannot contain x. Therefore the required contacts with R_L and R_R are distinct vertices.

The edge h has exactly two vertices other than v. Hence those two vertices are exactly the two half-contacts: one lies in R_L and one in R_R.

Finally distinct high edges through v have disjoint non-v pairs by linearity. Thus the three high edges give three pairwise disjoint two-sided chords across the central cut.
