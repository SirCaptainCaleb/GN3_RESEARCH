# In the terminal-left 4455 branch the second rank-five edge either uses c or is pushed to the private g4 slot

## Statement

Continue in the terminal-a subcase of 1734829a2326. Thus
  f_a={x,v,a}
has terminal a, entrance x off P,
  f_b={b,v,u_b}
has entrance b,
and
  phi(b)=3,
while phi(a),phi(c)>=5.

Let h be the second rank-five charged edge through v.

Then h contains neither a nor b. Hence h∩g3 is either empty or {c}.

If c∉h, then h is disjoint from g3, has no contact with g2, and its terminal-tail contact in g2∪g3∪g4 is necessarily the private vertex of g4.

## Body

The edges h,f_a,f_b are distinct charged edges through the common vertex v. By linearity, two such edges cannot share any second vertex. Since a∈f_a and b∈f_b, we have a,b∉h. Therefore h can meet g3={a,b,c} only at c.

Assume c∉h. Then h is disjoint from g3.

We claim h is also disjoint from g2. If h met g2, then
  (e5,h,g2,g3)
would be a four-edge linear path. Consecutive intersections are e5∩h={v}, the h-contact in g2, and g2∩g3={a}. The nonconsecutive pairs e5,g2 and e5,g3 are disjoint by the original path P, while h,g3 are disjoint by assumption. This path ends in g3, entered through a, so the private vertex b can be chosen as physical last vertex. Hence phi(b)>=4, contradicting phi(b)=3.

Thus h is disjoint from g2∪g3.

Apply the terminal-tail blocker lemma to the rank-five edge h against the five-edge path P ending at the common terminal v. Since h≠e5, one of the two non-v vertices of h occurs in the final three precursor edges g2∪g3∪g4. The first two have just been excluded, so h meets g4.

This g4-contact cannot be c because c∉h. It cannot be d=g4∩e5 because h and e5 already share v, and linearity forbids a second common vertex. Hence the contact is the private vertex of g4.
