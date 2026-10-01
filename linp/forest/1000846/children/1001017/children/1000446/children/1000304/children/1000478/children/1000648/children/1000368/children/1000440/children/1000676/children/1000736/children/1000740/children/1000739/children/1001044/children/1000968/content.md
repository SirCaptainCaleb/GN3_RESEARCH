# The low-low witness geometry in the potential-five 4455 pattern is impossible

## Statement

In the p=5 charged pattern (4,4,5,5), use the notation of e6eec0f670ed:
  P=(g1,g2,g3,g4,e5)
ends in a rank-five charged nonspecial edge e5 at terminal v, and
  g3={a,b,c}
with a=g2∩g3, b private in g3, c=g3∩g4.

The rank-four witness set cannot be {b,c}. Therefore the only remaining witness geometry for 4455 is {a,b}.

## Body

Assume the witness set is {b,c}. By e6eec0f670ed, both b and c are the unique entrances of the two rank-four charged edges. Let
  f_b={b,v,u_b}
be the edge with entrance b. Since f_b is potential-charged at v and phi(v)=5,
  phi(u_b)>=5.

We first show u_b∈V(g1∪g2). If not, then f_b is disjoint from g1,g2 and meets g3 only at b. The rank-five edge e5 is disjoint from g1,g2,g3 and meets f_b at v. Hence
  (g1,g2,g3,f_b,e5)
is a five-edge linear path ending in e5 and entering e5 through v. But e5 is nonspecial of rank five and v is one of its terminals, not its unique entrance. Contradiction.

Thus u_b lies in g1 or g2. Choose i∈{1,2} with u_b∈g_i.

Now
  (g_i,f_b,e5,g4)
is a four-edge linear path. Consecutive intersections are:
- g_i∩f_b={u_b};
- f_b∩e5={v};
- e5∩g4={d}, where d is the entrance of e5 on P.

For nonconsecutive pairs: g_i is disjoint from e5 and g4 because these are path edges separated from g_i in P; and f_b is disjoint from g4 because its vertices are b,v,u_b, with b∈g3\\g4, v∈e5\\g4, and u_b∈g1∪g2 disjoint from g4.

The last edge g4 is entered through d. The distinct vertex
  c=g3∩g4
can therefore be chosen as the last vertex. Hence phi(c)>=4.

But c is the unique entrance of the other rank-four ascending edge in the {b,c} witness geometry, so phi(c)=3. Contradiction.

Therefore {b,c} is impossible, and e6eec0f670ed leaves only {a,b}.
