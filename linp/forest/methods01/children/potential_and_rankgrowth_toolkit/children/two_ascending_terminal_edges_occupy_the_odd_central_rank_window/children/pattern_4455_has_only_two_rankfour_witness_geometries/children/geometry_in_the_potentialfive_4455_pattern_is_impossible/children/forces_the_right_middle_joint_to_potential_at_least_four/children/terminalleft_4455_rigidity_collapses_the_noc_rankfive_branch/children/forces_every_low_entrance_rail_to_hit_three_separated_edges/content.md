# The clean terminal-left 4455 state forces every low entrance rail to hit three separated edges

## Statement

Continue in the clean no-c terminal-a state of 14c89ddd9ef1:
  f_a={x,v,a}
is rank four with unique entrance x, phi(x)=3, and x∉V(P);
  h={z,v,u}
is the second rank-five edge with entrance z=private(g4) and u∉V(P);
and e5 is the fixed rank-five edge.

Let
  Q=(q1,q2,q3)
be any canonical three-edge entrance path ending physically at x and avoiding the terminals v,a, so Q,f_a is a four-edge path ending in f_a through x.

Then Q meets each of the three edges
  g3, e5, h.
Because Q avoids a and v, these contacts lie respectively in:
  {b,c}, {d,w}, {z,u}.

## Body

Suppose first that Q is disjoint from g3. Since Q,f_a is canonical and f_a meets g3 at a, the concatenation
  (q1,q2,q3,f_a,g3)
is a five-edge linear path ending in g3 through a. The private vertex b of g3 is distinct from a and can be chosen as physical last vertex. Hence phi(b)>=5, contradicting phi(b)=3.

Thus Q meets g3. Since Q avoids the terminal a of f_a and a∈g3, the contact is b or c.

Suppose next that Q is disjoint from e5. The edge f_a meets e5 at the common terminal v, while Q avoids v. Hence
  (q1,q2,q3,f_a,e5)
is a five-edge linear path ending in the nonspecial rank-five edge e5 through v, a terminal rather than its unique entrance. Contradiction. Therefore Q meets e5. As Q avoids v, the contact is one of the two non-v vertices d,w.

Finally suppose Q is disjoint from h. The edges f_a and h are distinct charged edges through v, so they meet exactly at v. Again Q avoids v. Thus
  (q1,q2,q3,f_a,h)
is a five-edge linear path ending in the nonspecial rank-five edge h through the terminal v rather than through its unique entrance z. Contradiction. Hence Q meets h. Since Q avoids v, the contact is z or u.

In the clean state g3 is disjoint from h, g3 is disjoint from e5, and h,e5 meet only at v, which is absent from Q. Thus these are three genuinely separated contact requirements on the same three-edge rail.