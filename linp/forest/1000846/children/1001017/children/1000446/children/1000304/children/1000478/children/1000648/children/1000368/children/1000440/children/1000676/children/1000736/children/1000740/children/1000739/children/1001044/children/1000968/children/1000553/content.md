# The surviving 4455 witness geometry forces the right middle joint to potential at least four

## Statement

Assume the p=5 charged pattern (4,4,5,5) in its only surviving witness geometry {a,b}, with
  P=(g1,g2,g3,g4,e5),
  a=g2∩g3,
  b private in g3,
  c=g3∩g4.
Let f_b={b,v,u_b} be the rank-four charged edge whose witness b is necessarily its unique entrance.

Then:
1. phi(b)=3;
2. u_b∈V(g1∪g2);
3. phi(c)>=4.

The lower bound phi(c)>=4 is witnessed both by the endpoint chord through a and v and by an explicit four-edge path through f_b and e5.

## Body

Since b is an index-3 witness for a rank-four ascending edge, e6eec0f670ed gives that b is its unique entrance, hence phi(b)=3.

We show u_b∈g1∪g2. If not, then f_b is disjoint from g1,g2 and meets g3 only at b. Thus
  (g1,g2,g3,f_b,e5)
is a five-edge linear path ending in the nonspecial rank-five edge e5 and entering it through v, a terminal rather than its unique entrance. Contradiction.

Choose i∈{1,2} with u_b∈g_i. Then
  (g_i,f_b,e5,g4)
is a four-edge linear path: consecutive contacts are u_b, v, and d=e5∩g4, while all nonconsecutive pairs are disjoint by linearity and by the original path P. The last edge g4 is entered through d, so c=g3∩g4 can be chosen as physical last vertex. Hence phi(c)>=4.

Independently, the other rank-four witness is a. Its charged edge contains a and v, so the endpoint-chord lemma a570c0ad0001 applied at i=2 also gives phi(c)>=4.
