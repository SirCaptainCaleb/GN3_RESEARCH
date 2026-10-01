# Joint-only blockers in the p=5 pure rank-five obstruction are pushed away from the final joint

## Statement

In the p=5 pure rank-five setup, fix
  P=(g1,g2,g3,g4,e4)
ending in the rank-five nonspecial edge e4 at terminal v. Put
  r=g1∩g2,
  a=g2∩g3,
  c=g3∩g4,
  d=g4∩e4.

Let f be another rank-five charged edge through v whose only precursor vertex is a path joint.

Then that joint cannot be c.

If the joint is a, then phi(c)>=5.

## Body

Suppose first that the only precursor vertex of f is c=g3∩g4. Then f meets both g3 and g4 at c and meets e4 at v, but is disjoint from g1,g2.

The sequence
  (g1,g2,g3,f,e4)
is a five-edge linear path: consecutive intersections are the original g1-g2 and g2-g3 joints, then c, then v. Nonconsecutive pairs are disjoint because f has no other precursor vertex and the original P is linear.

This path ends in the nonspecial rank-five edge e4 and enters it through v, a terminal rather than its unique entrance d. Contradiction. Thus c is impossible.

Now suppose the only precursor vertex of f is a=g2∩g3. Then f is disjoint from g1,g4 and meets e4 at v. Hence
  (g1,g2,f,e4,g4)
is a five-edge linear path. Its final edge g4 is entered through d=e4∩g4. The distinct vertex c=g3∩g4 can be chosen as physical last vertex. Therefore phi(c)>=5.