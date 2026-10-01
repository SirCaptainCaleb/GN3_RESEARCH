# A low edge can meet a high entrance rail late only as a double blocker

## Statement

In the setup of 21dfd53c201f, let e={x,v,u} be the low rank-q edge and let Q_i=(r_1,...,r_q) be a canonical q-edge entrance rail for a rank-(q+1) high edge h_i={y_i,v,z_i}, with phi(y_i)=q.

Then e meets Q_i. If e has exactly one contact vertex w on Q_i and k is the last path-edge index containing w, then
  3<=k<=q-2.
Thus a one-contact low blocker lies in the interior rail band r_3,...,r_{q-2}; if e meets either of the final two rail edges r_{q-1},r_q, then e has two contacts on Q_i.

## Body

The lower bound k>=3 is the terminal tail-blocker conclusion from c0798e59ef02 as used in 21dfd53c201f: the rank-q edge e, terminal at v, must meet one of the final q-2 precursor edges of the (q+1)-path Q_i,h_i, namely r_3,...,r_q.

For the upper bound, suppose e has exactly one contact w on Q_i. Consider
  r_1,...,r_k,e,h_i.
Because e has no other contact with Q_i, it meets the retained prefix only at w. The edges e and h_i meet exactly at v by linearity. The path Q_i avoids v and z_i, and y_i is not in e because e and h_i already share v. Hence the displayed sequence is linear.

It has length k+2. Its last edge is h_i, and the predecessor e meets h_i at v, so y_i is a last vertex. Therefore
  k+2<=phi(y_i)=q,
giving k<=q-2.

Combining the bounds yields 3<=k<=q-2. Hence any contact of e in r_{q-1} or r_q cannot be the unique contact; e must then use both non-v vertices on Q_i.