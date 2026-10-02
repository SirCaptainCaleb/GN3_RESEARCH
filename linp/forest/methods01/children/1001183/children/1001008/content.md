# A consistently oriented shared block has descending rank at every ascending edge

## Statement

Let
  h_1,...,h_t
be a consistently oriented common block as in e552a55fe162. For 1<=s<t, put
  y_s=h_s intersect h_{s+1}.
Assume y_s is the unique entrance of h_s and is terminal at h_{s+1}. Write
  r_s=phi(h_s).

Then:

(1) if h_s is ascending, then
  r_{s+1} <= r_s-1;

(2) if r_1,...,r_t all lie in an integer interval of width D, and B is the number of indices s<t for which h_s is nonascending, then
  t-1 <= (D+1)B + D.

Equivalently,
  B >= (t-1-D)/(D+1).

Thus a long consistently oriented common block confined to a narrow edge-rank band contains many nonspecial nonascending edges.

## Body

Fix s<t. Because y_s is terminal at h_{s+1},
  r_{s+1}=phi(h_{s+1})=phi(h_{s+1},y_s)<=phi(y_s).

If h_s is ascending and y_s is its unique entrance, then by definition
  phi(y_s)=phi(h_s)-1=r_s-1.
Therefore
  r_{s+1}<=r_s-1,
proving (1).

For (2), let A be the number of ascending indices s<t, so
  A+B=t-1.
Put
  Delta_s=r_{s+1}-r_s.
For every ascending index, part (1) gives Delta_s<=-1. For every nonascending index, the width-D hypothesis gives Delta_s<=D. Summing,
  r_t-r_1 = sum_{s=1}^{t-1} Delta_s
            <= -A + DB.
Since all ranks lie in one interval of width D,
  r_t-r_1 >= -D.
Hence
  -D <= -A+DB,
so
  A <= DB+D.
Substituting A=t-1-B yields
  t-1-B <= DB+D,
or
  t-1 <= (D+1)B+D.
The displayed lower bound for B follows.