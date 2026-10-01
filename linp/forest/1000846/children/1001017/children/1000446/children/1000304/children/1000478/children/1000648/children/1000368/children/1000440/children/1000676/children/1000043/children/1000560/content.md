# In the p=5 pattern 4445, both high terminals are forced into the first two path edges

## Statement

In the p=5 charged pattern (4,4,4,5), use the notation of 0b8e51bfe396 and let
  P=(g1,g2,g3,g4,e5)
be the fixed rank-five path ending in the rank-five charged nonspecial edge e5 at terminal v. Let
  f_b={b,v,u_b},
  f_c={c,v,u_c}
be the two rank-four charged edges with forced entrances b,c in g3.

Then
  u_b,u_c ∈ V(g1∪g2).
Moreover neither lies in g3, and u_b≠u_c.

## Body

We prove the assertion for u_b; the argument for u_c is identical.

By 9a7eac176b49, b is the unique entrance of the rank-four nonspecial edge f_b. Thus b∈g3 and
  f_b∩g3={b}
by linearity. In particular u_b∉g3.

Suppose u_b∉V(g1∪g2). Consider
  g1,g2,g3,f_b,e5.

The first three edges are consecutive edges of P. The edge f_b meets g3 exactly at b. It is disjoint from g1 and g2: its vertex v occurs only in the last edge e5 of P; its entrance b lies in g3; and by the supposition its remaining vertex u_b lies in none of g1,g2, while u_b∉g3 by linearity.

The edge e5 meets f_b at v. Since e5 was the last edge of the original path P and g4 separates it from g3, it is disjoint from g1,g2,g3.

Therefore
  g1,g2,g3,f_b,e5
is a five-edge linear path ending in e5. Its predecessor f_b meets e5 at v, so this path enters e5 through v.

But e5 is nonspecial of rank five and v is a terminal of e5; its unique rank-five entrance is the original P-contact g4∩e5, not v. This is a contradiction.

Hence u_b∈V(g1∪g2). Likewise u_c∈V(g1∪g2).

Finally f_b and f_c are distinct edges sharing v, so linearity gives f_b∩f_c={v}. Hence u_b≠u_c.