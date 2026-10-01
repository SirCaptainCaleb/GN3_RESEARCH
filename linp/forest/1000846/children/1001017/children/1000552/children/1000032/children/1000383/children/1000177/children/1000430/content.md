# Every one-rank-higher charged competitor blocks the low entrance rail

## Statement

Let e={x,v,u} be an ascending nonspecial edge of rank q with unique entrance x and terminal v. Let
  R=(r_1,...,r_{q-1})
be a canonical entrance path ending physically at x and avoiding v,u.

Let h={y,v,z} be a distinct ascending nonspecial edge of rank q+1 for which v is a terminal. Then
  h∩V(R) is nonempty.

More precisely, h cannot contain x, so every R-contact of h lies in {y,z}. Hence h has either one or two R-contact vertices.

## Body

Suppose h∩V(R)=∅. Since R ends at x and R avoids v,u, the sequence
  R,e,h
is a linear path of length
  (q-1)+2=q+1:
R meets e only at x, e∩h={v}, and h is disjoint from R.

This path ends in h and enters h through v. Because h is nonspecial and v is a terminal of h, v cannot be an entrance label of a longest (q+1)-edge path ending in h. Contradiction.

Thus h meets R.

Also h cannot contain x: both h and e contain v, so if h contained x they would share the pair {v,x}, contradicting linearity. Therefore every R-contact of h is one of its two non-v vertices y,z. By linearity of R and h, each such vertex lies in one or two consecutive path edges, and h has at most two distinct R-contact vertices.