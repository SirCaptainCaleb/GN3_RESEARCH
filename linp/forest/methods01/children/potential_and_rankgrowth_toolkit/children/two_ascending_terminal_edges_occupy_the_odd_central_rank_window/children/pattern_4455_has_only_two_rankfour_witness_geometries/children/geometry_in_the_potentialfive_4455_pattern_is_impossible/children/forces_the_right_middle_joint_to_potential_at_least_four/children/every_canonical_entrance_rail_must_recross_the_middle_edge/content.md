# If the left 4455 witness is an entrance, every canonical entrance rail must recross the middle edge

## Statement

Assume the surviving p=5 4455 witness geometry {a,b} from 7b36d8822911, with
  g3={a,b,c},
  phi(b)=3.
Suppose a is the unique entrance of its rank-four charged edge f_a. Then phi(a)=3.

Let
  R_a=(h1,h2,h3)
be any canonical three-edge entrance path ending physically at a such that R_a,f_a is a four-edge path ending in f_a through a and R_a avoids the two terminals of f_a.

Then R_a meets g3 at some vertex other than a. Equivalently, at least one of b,c belongs to V(h1∪h2).

## Body

Suppose R_a meets g3 only at a. Since R_a ends physically at a, its final edge h3 contains a, and by assumption g3 is disjoint from h1,h2 and meets h3 exactly at a.

Therefore
  (h1,h2,h3,g3)
is a four-edge linear path.

Its final edge is g3, entered through a. The private vertex b of g3 is distinct from a and can be chosen as a physical last vertex. Hence
  phi(b)>=4.

But b is the unique entrance of the other rank-four ascending edge in the surviving {a,b} witness geometry, so phi(b)=3 by 7b36d8822911. Contradiction.

Thus R_a has an additional g3-contact. Because h3 and g3 already meet at a, linearity forbids h3 from containing b or c. Hence the additional contact lies in h1 or h2.