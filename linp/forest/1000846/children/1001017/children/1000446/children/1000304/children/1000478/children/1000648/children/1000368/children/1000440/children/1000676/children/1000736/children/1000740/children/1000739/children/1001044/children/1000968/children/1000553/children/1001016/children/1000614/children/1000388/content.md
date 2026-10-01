# A single far contact in entrance-a 4455 forces full middle-edge saturation of the entrance rail

## Statement

Continue in branch (E) of 4455. Let
  R_a=(h1,h2,h3)
be a canonical a-ending entrance rail for f_a={a,v,u_a}. Assume e5 meets R_a in exactly one vertex.

Then:
1. the e5-contact is the private vertex of h3;
2. g3 meets both h1 and h2, in addition to its endpoint contact a∈h3.

Thus g3 intersects every edge of R_a.

## Body

By 8b0147365e90, the unique e5-contact lies in h3.

Let s=h2∩h3. The contact cannot be s. If e5∩R_a={s}, then e5 meets h2 and h3 at s, while f_a meets R_a only at a∈h3 and e5∩f_a={v}. The sequence
  (h1,h2,e5,f_a)
is a four-edge linear path: h1∩h2 is the first joint, h2∩e5={s}, e5∩f_a={v}, and the nonconsecutive pairs are disjoint by the unique-contact and canonical-rail hypotheses. It ends in f_a through v, contradicting the unique rank-four entrance a. Hence the unique e5-contact is the private vertex of h3.

By e277460104ac, g3 has an additional R_a-contact besides a, lying in h1 or h2.

Suppose g3 is disjoint from h1. Then its additional contact lies in h2. Since e5 meets R_a only in the private vertex of h3, e5 is disjoint from h1,h2. The sequence
  (h1,h2,g3,f_a,e5)
is a five-edge linear path: g3∩f_a={a} and f_a∩e5={v}, while all nonconsecutive pairs are disjoint under the stated hypotheses. It ends in e5 through terminal v, contradicting the unique rank-five entrance of e5.

Therefore g3 meets h1.

Similarly suppose g3 is disjoint from h2. Then its additional contact lies in h1. The reversed-start sequence
  (h2,h1,g3,f_a,e5)
is a five-edge linear path, again ending in e5 through v; the nonconsecutive pair h2,g3 is disjoint by assumption, and e5 is disjoint from h1,h2. This is the same contradiction.

Hence g3 meets both h1 and h2. Together with a∈g3∩h3, it meets every rail edge.
