# If the left 4455 witness is a terminal, both adjacent middle joints are high

## Statement

Assume the surviving p=5 4455 witness geometry {a,b}, with
  P=(g1,g2,g3,g4,e5),
  a=g2∩g3,
  b private in g3,
  c=g3∩g4.
Suppose the rank-four charged edge witnessed at a has a as its opposite terminal rather than its entrance. Write
  f_a={x,v,a},
where x is the unique entrance.

Then
  phi(a)>=5,
  phi(x)=3,
  x∉V(P),
and
  phi(c)>=5.

## Body

Because f_a is rank-four ascending, its unique entrance x satisfies phi(x)=3. Since the selected path-relative witness is the terminal a, the entrance x is absent from the fixed path P. Because f_a is potential-charged at v with phi(v)=5, the opposite terminal satisfies phi(a)>=5.

Now consider
  (g1,g2,f_a,e5,g4).

The consecutive intersections are:
- g1∩g2, the original first joint;
- g2∩f_a={a};
- f_a∩e5={v};
- e5∩g4={d}.

All nonconsecutive pairs are disjoint. Indeed x is absent from P; a lies only on g2,g3 among the path edges; v lies on e5 as the physical terminal; and the original path has the required nonconsecutive disjointness. In particular f_a is disjoint from g1 and g4.

Thus the displayed sequence is a five-edge linear path. Its final edge is g4, entered through d. The distinct vertex c=g3∩g4 can be chosen as physical last vertex. Hence phi(c)>=5.