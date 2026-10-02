# The two-contact p=5 4455 low-low state is impossible

## Statement

In the p=5 charged pattern (4,4,5,5), the {b,c} witness geometry cannot occur in the two-contact state of 3d216d397f78. Hence, within the {b,c} geometry, the second rank-five charged edge must be in the unique clean state of 96ce63c6b236: its sole contact with g2∪g3∪g4 is its entrance at the private vertex of g4.

## Body

Assume the two-contact state. By 3d216d397f78, write
  r=g1∩g2,
  a=g2∩g3,
and let h be the second rank-five charged edge. Then
  h∩g2={r},
  h∩g3=empty.
Also h and e5 are distinct edges through v, so
  h∩e5={v}.

Consider the four edges
  e5,h,g2,g3.

Consecutive intersections are:
  e5∩h={v},
  h∩g2={r},
  g2∩g3={a}.

The nonconsecutive pairs are disjoint:
- e5 is disjoint from g2 and g3 because P=(g1,g2,g3,g4,e5) is a linear path;
- h is disjoint from g3 by the two-contact normal form.

Thus
  e5,h,g2,g3
is a four-edge linear path.

Its final edge is g3={a,b,c}, entered through a. Hence c, which is distinct from a, may be chosen as the last vertex. Therefore
  phi(c)>=4.

But in the {b,c} witness geometry, c is the entrance of a rank-four ascending edge and hence
  phi(c)=3.
Contradiction.

Therefore the two-contact state is impossible. By 96ce63c6b236, the only remaining {b,c} state is the clean one in which the second rank-five edge meets g2∪g3∪g4 only at its entrance, the private vertex of g4.