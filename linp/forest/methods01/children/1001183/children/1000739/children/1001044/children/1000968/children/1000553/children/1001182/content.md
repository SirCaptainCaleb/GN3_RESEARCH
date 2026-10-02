# Terminal-left 4455 rigidity collapses the no-c rank-five branch

## Statement

Assume the surviving p=5 terminal-left 4455 geometry with
P=(g1,g2,g3,g4,e5),
a=g2∩g3, b the private vertex of g3, c=g3∩g4,
and suppose the rank-four charged edge at a is
f_a={x,v,a}
with a terminal and x its unique entrance. Then phi(a),phi(c)>=5, phi(x)=3, and x∉V(P).

Let f_b be the charged edge with entrance b, and let h be the second rank-five charged edge through v. Then h contains neither a nor b, so h∩g3 is either empty or {c}. If c∉h, then h is disjoint from g2∪g3 and meets g4 at its private vertex z. In fact this no-c branch is uniquely clean:
h={z,v,u},
where z is the unique entrance of h and u∉V(P); hence h meets P only at z and v.

## Body

Because f_a is rank-four ascending, phi(x)=3. Since a is the path-relative terminal witness, x is absent from P and phi(a)>=5. The sequence (g1,g2,f_a,e5,g4) is a five-edge linear path ending in g4 through d=g4∩e5, so c can be chosen as last vertex and phi(c)>=5.

The distinct charged edges h,f_a,f_b share v and, by linearity, no second vertex. Hence a,b∉h, so h∩g3 is empty or {c}. Assume c∉h. If h met g2, then (e5,h,g2,g3) would be a four-edge linear path ending in g3 through a, allowing b as last vertex and contradicting phi(b)=3. Thus h is disjoint from g2∪g3. The terminal-tail blocker lemma applied to h and P forces a contact in g2∪g3∪g4; the first two are excluded, and linearity excludes d=g4∩e5, so the contact is the private vertex z of g4.

Let t be the other non-v vertex of h. It cannot lie in g4 by linearity or in e5 because h and e5 already share v. If t lay in g1, then (e5,h,g1,g2,g3) would be a five-edge linear path ending in g3 through a, again forcing phi(b)>=5. Hence t∉V(P), and h meets P only at z and v. Finally z cannot be a terminal of the nonspecial rank-five edge h: otherwise (g1,g2,g3,g4,h) would be a five-edge path entering h through a terminal, contradicting its unique rank-five entrance. Therefore z is the unique entrance, phi(z)=4, and writing the off-path terminal as u gives h={z,v,u} with u∉V(P).