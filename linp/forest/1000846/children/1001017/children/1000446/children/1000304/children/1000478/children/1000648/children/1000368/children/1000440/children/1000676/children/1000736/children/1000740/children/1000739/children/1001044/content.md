# Potential-five pattern 4455 has only two rank-four witness geometries

## Statement

Let phi(v)=5 and suppose four potential-charged ascending nonspecial edges through v have ordered ranks (4,4,5,5). Fix a maximum five-edge path
  P=(g1,g2,g3,g4,e5)
ending in one rank-five charged edge e5 at v, and write
  a=g2∩g3,
  b=the private vertex of g3,
  c=g3∩g4.

For the two rank-four charged edges, their path-relative witnesses are two distinct vertices of {a,b,c}. The witness pair {a,c} is impossible. Hence, up to ordering, the only possible rank-four witness sets are
  {a,b} or {b,c}.

Moreover b is necessarily an entrance witness in either case; in the {b,c} case both b and c are entrances and phi(b)=phi(c)=3.

## Body

For p=5 and rank q=4, the path-relative central-window theorem localizes every rank-four witness to the three vertices of g3, namely a,b,c. Distinct charged edges have disjoint non-v pairs, so the two selected witnesses are distinct.

By the same prefix argument used in 9a7eac176b49, a terminal witness cannot occupy an index-3 slot. Thus b, the private index-3 vertex, and c, the right joint of index 3, must be entrance witnesses whenever they occur. In particular a used witness may be entrance or terminal, while b,c are entrances with potential three.

Suppose the two witnesses were {a,c}. Let f_a be the rank-four charged edge whose selected witness is a. Regardless of whether a is its entrance or opposite terminal, f_a contains both a and the common terminal v.

Apply the endpoint-chord lemma a570c0ad0001 to the path P with i=2. Since a=g2∩g3 and c=g3∩g4, the existence of an edge containing a and v gives
  phi(c)>=min{4,4}=4.

But c is the witness of the other rank-four charged edge, and because c is an index-3 slot it is necessarily that edge's unique entrance. Hence
  phi(c)=4-1=3,
a contradiction.

Therefore {a,c} is impossible.

The remaining two-element subsets are {a,b} and {b,c}. In both, b is an index-3 witness and hence an entrance. In {b,c}, both are entrances, so phi(b)=phi(c)=3.
