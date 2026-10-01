# The no-c second-rank-five state in terminal-left 4455 is uniquely clean

## Statement

In the setting of 362087e475d5, assume c∉h. Let z be the private vertex of g4. Then
  h={z,v,u},
where z is the unique entrance of h and u∉V(P).

Thus the no-c branch has exactly one form: h meets the fixed path P only in z∈g4 and v∈e5, with z=private(g4) and the opposite terminal u outside P.

## Body

By 362087e475d5, h is disjoint from g2∪g3 and meets g4 at its private vertex z.

Let t be the other non-v vertex of h. It cannot lie in g4 by linearity. It cannot lie in e5 because h and e5 already share v. Thus the only possible further contact with P is in g1.

Suppose t∈g1. Since h is disjoint from g2∪g3, and e5 is disjoint from g1∪g2∪g3, the sequence
  (e5,h,g1,g2,g3)
is a five-edge linear path. Its final edge g3 is entered through a=g2∩g3, so the private vertex b can be chosen as physical last vertex. Hence phi(b)>=5, contradicting phi(b)=3.

Therefore t∉V(P). So h meets P only at z and v.

If z were the terminal t and the off-path vertex were the entrance, then
  (g1,g2,g3,g4,h)
would be a five-edge linear path ending in the nonspecial rank-five edge h and entering it through the terminal z, contradicting unique rank-five entrance. Therefore z is the unique entrance of h. Since h is ascending of rank five, phi(z)=4. Writing the off-path terminal as u gives the stated form.
